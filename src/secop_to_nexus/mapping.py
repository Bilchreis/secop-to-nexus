"""Map a SECoP SEC node (describe message + recorded values) onto a NeXus tree.

Layout (one SEC node per file)::

    /                                  NXroot
    /entry                             NXentry   title, start_time, end_time,
                                                 duration
    /entry/instrument                  NXinstrument  name = equipment_id
        description                    node description
        firmware                       NXprogram, program = node firmware
        fabrication                    NXfabrication, vendor = node implementor
        secop_description              NXnote   raw describe message (JSON)
        <module>                       NXsensor (Readable)
                                       NXactuator (Writable, Drivable)
                                       NXcollection (anything else)
            value_log, target_log, <param>_log          NXlog per parameter
            status_log, status_text_log                 NXlog (code, message)
            value, target, <param>, status, status_text
                                       plain field instead of the NXlog if the
                                       parameter never changed its value
            implementation             NXprogram, program = implementation
    /entry/sample                      NXsample  only if a meaning belongs to it
        <quantity>_env                 NXenvironment, links to the modules
        <quantity>_log                 link to the most important measuring log
        <quantity>                     link to its field, if it never changed

Each module with a numeric ``value`` gets one NXdata group ``data`` next to
its logs: ``value`` and ``time`` are links into ``value_log``, nothing is
copied or resampled. The ``@default``
chain root -> entry -> instrument -> module -> data leads to the sample's main
quantity, else to the first module that has a plot.

Only parameters that change over time become an NXlog. Changing string and
blob parameters (e.g. the status text) are not written at all: NXlog holds
numbers. Node and module properties without a NeXus field of their own are
kept as ``@secop_<property>`` attributes of the instrument / module group.

Modules are classified by their interface classes; ``meaning.function``
fills ``NXsensor/measurement`` and ``NXactuator/physical_quantity``.
A meaning belongs to the sample if ``belongs_to`` is ``"sample"``; old
list-style meanings (``[function, importance]``, SECoP 1.x) predate
``belongs_to`` and always referred to the sample.
"""

from __future__ import annotations

import dataclasses
import json
import logging
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
from importlib.metadata import PackageNotFoundError, version
from typing import Any

import h5py
import numpy as np

from secop_to_nexus.datainfo import column, is_status, parse_datainfo
from secop_to_nexus.nxs_base_classes import (
    NXDL_VERSION,
    NXactuator,
    NXcollection,
    NXdata,
    NXentry,
    NXenvironment,
    NXfabrication,
    NXinstrument,
    NXlog,
    NXnote,
    NXobject,
    NXprogram,
    NXroot,
    NXsample,
    NXsensor,
)
from secop_to_nexus.nxs_base_classes.NXdtypes import (
    NX_CHAR,
    NX_DATE_TIME,
    NX_FLOAT,
    NX_INT,
    NXdtype,
)
from secop_to_nexus.nxs_base_classes.NXreference import NXreference

log = logging.getLogger(__name__)

PROGRAM_NAME = "secop-to-nexus"
SAMPLE_PATH = "/entry/sample"
PLOT_NAME = "data"  # NXdata group inside each module

# SECoP meaning functions whose NeXus spelling differs (NXsensor/measurement)
_NEXUS_QUANTITY = {
    "magneticfield": "magnetic_field",
    "electricfield": "electric_field",
    "surfacepressure": "surface_pressure",
    "ph": "pH",
    "flowrate": "flow",
}
_ACTUATOR_CLASSES = {"Writable", "Drivable", "Acquisition"}
_SENSOR_CLASSES = {"Readable", "AcquisitionChannel"}


@dataclass
class ParameterLog:
    """Recorded history of one parameter.

    ``timestamps`` are Unix seconds; ``values`` are SECoP wire values as
    JSON-decoded from the data reports (``None`` entries, e.g. from error
    reports, are dropped).
    """

    timestamps: Sequence[float] | np.ndarray
    values: Sequence[Any] | np.ndarray


# {module: {parameter: ParameterLog | (timestamps, values)}}
Logs = Mapping[
    str, Mapping[str, "ParameterLog | tuple[Sequence[float], Sequence[Any]]"]
]


@dataclass(frozen=True)
class Meaning:
    function: str
    importance: float
    belongs_to: str

    @property
    def regulation(self) -> bool:
        return self.function.endswith("_regulation")

    @property
    def quantity(self) -> str:
        base = self.function.removesuffix("_regulation")
        return _NEXUS_QUANTITY.get(base, base)

    @classmethod
    def parse(cls, raw: Any) -> Meaning | None:
        if isinstance(raw, (list, tuple)) and len(raw) >= 2:
            return cls(str(raw[0]), float(raw[1]), "sample")
        if isinstance(raw, Mapping) and raw.get("function"):
            return cls(
                str(raw["function"]),
                float(raw.get("importance", 0)),
                str(raw.get("belongs_to", "other")),
            )
        return None


@dataclass
class _SampleLink:
    meaning: Meaning
    module: str
    group: NXobject
    log: NXlog | None
    field: str | None = None  # name of the field in group, if there is no log


def _load_describe(describe: Mapping[str, Any] | str | bytes) -> dict[str, Any]:
    if isinstance(describe, (bytes, bytearray)):
        describe = describe.decode("utf-8")
    if isinstance(describe, str):
        return json.loads(describe)
    return dict(describe)


def _normalize(plog: Any) -> tuple[np.ndarray, list[Any]]:
    if not isinstance(plog, ParameterLog):
        plog = ParameterLog(*plog)
    ts = np.asarray(plog.timestamps, dtype=np.float64)
    values = list(plog.values)
    if len(ts) != len(values):
        raise ValueError(f"{len(ts)} timestamps but {len(values)} values")
    keep = [i for i, v in enumerate(values) if v is not None]
    if len(keep) != len(values):
        ts, values = ts[keep], [values[i] for i in keep]
    if len(ts) > 1 and np.any(np.diff(ts) < 0):
        order = np.argsort(ts, kind="stable")
        ts, values = ts[order], [values[i] for i in order]
    return ts, values


def _iso(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()


def _parameter_logs(
    pname: str,
    accessible: Mapping[str, Any],
    ts: np.ndarray,
    values: list[Any],
    t0: float,
) -> dict[str, NXlog]:
    """NXlog group(s) for one parameter, keyed by HDF5 group name."""
    datainfo = accessible["datainfo"]
    dt = parse_datainfo(datainfo, pname)
    description = accessible.get("description")

    def nxlog(value_column: Any, desc: str | None) -> NXlog:
        return NXlog(
            time=NX_FLOAT(ts - t0, units="s", attrs={"start": _iso(t0)}, array=True),
            value=value_column,
            description=NX_CHAR(desc) if desc else None,
        )

    if pname == "status" and is_status(dt):
        code_info, text_info = datainfo["members"]
        return {
            "status_log": nxlog(
                column(dt.members[0], [v[0] for v in values], code_info),
                description,
            ),
            "status_text_log": nxlog(
                column(dt.members[1], [v[1] for v in values], text_info),
                f"status message: {description}" if description else None,
            ),
        }
    return {f"{pname}_log": nxlog(column(dt, values, datainfo), description)}


def _field(nxlog: NXlog, timestamp: float) -> NXdtype:
    """Plain field for a parameter that never changed: the value of ``nxlog``
    with the time it was first recorded and its description as attributes."""
    column = nxlog.value
    value = column.value[0]
    attrs = dict(column.attrs, timestamp=_iso(timestamp))
    if nxlog.description is not None:
        attrs["description"] = nxlog.description.value
    if isinstance(column, NX_CHAR):
        # wrapped in a list: the writer would parse a bare "[...]" string
        return NX_CHAR([value], units=column.units, attrs=attrs, array=False)
    return type(column)(
        value, units=column.units, attrs=attrs, array=np.ndim(value) > 0
    )


def _constant(column: NXdtype) -> bool:
    """True if all recorded values of ``column`` are the same."""
    values = column.value
    if isinstance(values, np.ndarray):
        first = np.broadcast_to(values[0], values.shape)
        return np.array_equal(values, first, equal_nan=values.dtype.kind == "f")
    return all(v == values[0] for v in values)


def _is_text(column: NXdtype) -> bool:
    """SECoP string or blob (JSON-encoded structured values are not text)."""
    return isinstance(column, NX_CHAR) and "secop_encoding" not in column.attrs


def _secop_attrs(properties: Mapping[str, Any], mapped: set[str]) -> dict[str, Any]:
    """``@secop_<name>`` attributes for the node/module properties that have
    no NeXus field: strings, numbers and lists of strings as they are,
    anything else as JSON."""
    attrs: dict[str, Any] = {}
    for name, value in properties.items():
        if name in mapped or value is None or value == [] or value == "":
            continue
        plain = isinstance(value, (str, int, float)) or (
            isinstance(value, list) and all(isinstance(v, str) for v in value)
        )
        attrs[f"secop_{name}"] = value if plain else json.dumps(value)
    return attrs


def _field_names(group: NXobject) -> set[str]:
    """Names a parameter field must not take in ``group``: the fields and
    groups NeXus defines for its class (``value`` is the exception, it means
    the same thing there) and the plot."""
    names = {f.metadata.get("nx_name", f.name) for f in dataclasses.fields(group)}
    return (names - {"value"}) | {PLOT_NAME}


def _plot(module: str, value_log: NXlog | None) -> NXdata | None:
    """NXdata of a module: its value over time, as links into value_log;
    None if the value is not numeric."""
    if value_log is None or not isinstance(value_log.value, (NX_FLOAT, NX_INT)):
        return None
    value, time = value_log.value, value_log.time
    # attributes on the log datasets; the links in NXdata share them
    label = f"{module}:value"
    value.attrs["long_name"] = f"{label} ({value.units})" if value.units else label
    time.attrs["long_name"] = "time since start_time (s)"
    return NXdata(
        signal="value",
        axes="time" if np.ndim(value.value) == 1 else ["time", "."],
        AXISNAME_indices={"time_indices": 0},
        DATA={"value": NXreference(value_log, "value")},
        AXISNAME={"time": NXreference(value_log, "time")},
        title=NX_CHAR(module),
    )


def _module_group(
    name: str, module: Mapping[str, Any], meaning: Meaning | None
) -> NXsensor | NXactuator | NXcollection:
    classes = set(module.get("interface_classes", []))
    description = NX_CHAR(module["description"]) if module.get("description") else None
    quantity = NX_CHAR(meaning.quantity) if meaning else None
    if classes & _ACTUATOR_CLASSES:
        on_sample = meaning is not None and meaning.belongs_to == "sample"
        return NXactuator(
            name=NX_CHAR(name),
            description=description,
            physical_quantity=quantity,
            actuation_target=NX_CHAR(SAMPLE_PATH) if on_sample else None,
        )
    if classes & _SENSOR_CLASSES:
        return NXsensor(
            name=NX_CHAR(name), description=description, measurement=quantity
        )
    group = NXcollection()
    if description is not None:
        group.extra_fields["description"] = description
    return group


def _module_properties(group: NXobject, module: Mapping[str, Any]) -> None:
    """Module properties that are not covered by _module_group."""
    if module.get("implementation"):
        program = NXprogram(program=NX_CHAR(str(module["implementation"])))
        if isinstance(group, NXcollection):
            group.extra_groups["implementation"] = program
        else:
            group.programs["implementation"] = program
    group.extra_attrs.update(
        _secop_attrs(module, {"accessibles", "description", "implementation"})
    )


def _build_sample(
    links: list[_SampleLink], equipment_id: str, node_description: str | None
) -> NXsample:
    sample = NXsample()
    by_quantity: dict[str, list[_SampleLink]] = {}
    for link in links:
        by_quantity.setdefault(link.meaning.quantity, []).append(link)

    for quantity, items in by_quantity.items():
        env = NXenvironment(
            name=NX_CHAR(equipment_id),
            description=NX_CHAR(node_description) if node_description else None,
        )
        for item in items:
            if isinstance(item.group, NXactuator):
                env.actuators[item.module] = NXreference(item.group)
            elif isinstance(item.group, NXsensor):
                env.sensors[item.module] = NXreference(item.group)
        sample.environments[f"{quantity}_env"] = env

        measuring = [
            i for i in items if not i.meaning.regulation and (i.log or i.field)
        ]
        if measuring:
            best = max(measuring, key=lambda i: i.meaning.importance)
            if best.log is not None:
                sample.extra_groups[f"{quantity}_log"] = NXreference(best.log)
            else:
                sample.extra_fields[quantity] = NXreference(best.group, best.field)
    return sample


def _version() -> str:
    try:
        return version("secop-to-nexus")
    except PackageNotFoundError:
        return "unknown"


def build_nexus_tree(
    describe: Mapping[str, Any] | str | bytes,
    logs: Logs,
    *,
    title: str | None = None,
) -> NXroot:
    """Finalized NeXus tree for one SEC node and its recorded parameter logs."""
    node = _load_describe(describe)
    equipment_id = node.get("equipment_id") or "sec_node"
    node_description = node.get("description")
    modules: Mapping[str, Any] = node.get("modules", {})

    data = {
        (mname, pname): _normalize(plog)
        for mname, params in logs.items()
        for pname, plog in params.items()
    }
    for mname, pname in data:
        if pname not in modules.get(mname, {}).get("accessibles", {}):
            log.warning("no describe entry for %s:%s, skipping its log", mname, pname)
    all_ts = [ts for ts, _ in data.values() if len(ts)]
    t0 = min(float(ts[0]) for ts in all_ts) if all_ts else None
    t1 = max(float(ts[-1]) for ts in all_ts) if all_ts else None

    instrument = NXinstrument(name=NX_CHAR(equipment_id))
    if node_description:
        instrument.extra_fields["description"] = NX_CHAR(node_description)
    if node.get("firmware"):
        instrument.extra_groups["firmware"] = NXprogram(
            program=NX_CHAR(str(node["firmware"]))
        )
    if node.get("implementor"):
        instrument.fabrications["fabrication"] = NXfabrication(
            vendor=NX_CHAR(str(node["implementor"]))
        )
    instrument.extra_attrs.update(
        _secop_attrs(
            node,
            {"modules", "equipment_id", "description", "firmware", "implementor"},
        )
    )
    instrument.extra_groups["secop_description"] = NXnote(
        type=NX_CHAR("application/json"),
        description=NX_CHAR("SECoP describe message of the SEC node"),
        data=NX_CHAR(json.dumps(node)),
    )

    sample_links: list[_SampleLink] = []
    plotted: list[str] = []  # modules that have an NXdata group
    for mname, module in modules.items():
        meaning = Meaning.parse(module.get("meaning"))
        group = _module_group(mname, module, meaning)
        _module_properties(group, module)

        reserved = _field_names(group)
        for pname, accessible in module.get("accessibles", {}).items():
            if accessible.get("datainfo", {}).get("type") == "command":
                continue
            ts, values = data.get((mname, pname), (np.empty(0), []))
            if not len(ts):
                continue
            for logname, nxlog in _parameter_logs(
                pname, accessible, ts, values, t0
            ).items():
                name = logname.removesuffix("_log")
                if name not in reserved and _constant(nxlog.value):
                    group.extra_fields[name] = _field(nxlog, float(ts[0]))
                elif _is_text(nxlog.value):
                    continue  # NXlog holds numbers: no log of changing text
                elif logname == "value_log" and isinstance(group, NXsensor):
                    group.value_log = nxlog
                else:
                    group.extra_groups[logname] = nxlog
            # SECoP 2: a meaning may also sit on a single parameter
            p_meaning = Meaning.parse(accessible.get("meaning"))
            if p_meaning and p_meaning.belongs_to == "sample":
                sample_links.append(
                    _SampleLink(
                        p_meaning,
                        mname,
                        group,
                        group.extra_groups.get(f"{pname}_log"),
                        pname if pname in group.extra_fields else None,
                    )
                )

        value_log = getattr(group, "value_log", None) or group.extra_groups.get(
            "value_log"
        )
        plot = _plot(mname, value_log)
        if plot is not None:
            group.extra_groups[PLOT_NAME] = plot
            group.default = PLOT_NAME
            plotted.append(mname)
        if meaning and meaning.belongs_to == "sample":
            sample_links.append(
                _SampleLink(
                    meaning,
                    mname,
                    group,
                    value_log,
                    "value" if "value" in group.extra_fields else None,
                )
            )

        if isinstance(group, NXactuator):
            instrument.actuators[mname] = group
        elif isinstance(group, NXsensor):
            instrument.sensors[mname] = group
        else:
            instrument.collections[mname] = group

    entry = NXentry(
        title=NX_CHAR(title or f"SECoP log of {equipment_id}"),
        start_time=(
            NX_DATE_TIME(datetime.fromtimestamp(t0, tz=timezone.utc))
            if t0 is not None
            else None
        ),
        end_time=(
            NX_DATE_TIME(datetime.fromtimestamp(t1, tz=timezone.utc))
            if t1 is not None
            else None
        ),
        duration=NX_INT(round(t1 - t0), units="s") if t0 is not None else None,
        program_name=NX_CHAR(PROGRAM_NAME, attrs={"version": _version()}),
        instruments={"instrument": instrument},
    )
    main_modules: list[str] = []
    if sample_links:
        sample = _build_sample(sample_links, equipment_id, node_description)
        entry.samples["sample"] = sample
        # modules whose value is the sample's <quantity>_log
        main_modules = [
            link.module
            for ref in sample.extra_groups.values()
            for link in sample_links
            if isinstance(ref, NXreference) and link.log is ref.target
        ]
    # default plot: the sample's main quantity, else the first plotted module
    defaults = [m for m in main_modules if m in plotted] + plotted
    if defaults:
        instrument.default = defaults[0]
        entry.default = "instrument"

    root = NXroot(
        default="entry",
        file_time=datetime.now(timezone.utc).isoformat(),
        creator=PROGRAM_NAME,
        creator_version=_version(),
        NeXus_version=NXDL_VERSION,
        HDF5_Version=h5py.version.hdf5_version,
        h5py_version=h5py.version.version,
        entries={"entry": entry},
    )
    root.finalize()
    return root
