"""SECoP describe message + recorded values -> .nxs file."""

import json
import logging
from pathlib import Path

import h5py
import numpy as np
import pytest

from secop_to_nexus import ParameterLog, build_nexus_tree, nexus_bytes, write_nexus

DATA = Path(__file__).parent / "data"
T0 = 1_760_000_000.0  # 2025-10-09T08:53:20Z


@pytest.fixture
def cryostat() -> dict:
    return json.loads((DATA / "cryostat_describe.json").read_text())


@pytest.fixture
def cryostat_logs() -> dict:
    t = T0 + np.arange(3.0)
    return {
        "T_reg": {
            "value": (t, [4.2, 4.3, 4.4]),
            "target": ([T0], [4.5]),
            "status": (t, [[300, "ramping"], [300, "ramping"], [100, "at target"]]),
            "ramp": (t[:2], [150, 200]),  # scaled ints on the wire
            "_heater_on": ([T0], [True]),
            "_pid": ([T0], [{"p": 2.5, "i": 30}]),
            "_limits": ([T0], [[0.0, 300.0]]),
        },
        # deliberately unsorted, with an error report (None) in between
        "T_sample": {"value": ([T0 + 2, T0, T0 + 1], [4.0, 3.8, None])},
        "T_vti": {"value": (t, [4.1, 4.2, 4.3])},
        "field": {"value": ([T0], [0.001])},
        "spectrum": {
            "value": (t[:2], [[1, 2, 3], [4, 5, 6]]),
            "_peaks": ([T0], [[{"pos": 1.0, "height": 2.0}]]),
            "_future": ([T0], [[1.0, 2.0]]),
        },
        "io": {
            "_last_reply": ([T0], ["OK"]),
            "_raw": ([T0], ["AAEC"]),
        },
    }


@pytest.fixture
def nxs(tmp_path, cryostat, cryostat_logs):
    path = tmp_path / "cryo.nxs"
    write_nexus(path, cryostat, cryostat_logs)
    with h5py.File(path, "r") as f:
        yield f


def _str(ds) -> str:
    value = ds[()]
    return value.decode() if isinstance(value, bytes) else value


def _strs(ds) -> list[str]:
    return [v.decode() for v in ds[()]]


INST = "entry/instrument"


def test_root_and_entry(nxs):
    assert nxs.attrs["NX_class"] == "NXroot"
    assert nxs.attrs["creator"] == "secop-to-nexus"
    assert nxs.attrs["NeXus_version"].startswith("v20")
    entry = nxs["entry"]
    assert _str(entry["title"]) == "SECoP log of cryo7.example.org"
    assert _str(entry["start_time"]) == "2025-10-09T08:53:20+00:00"
    assert _str(entry["end_time"]) == "2025-10-09T08:53:22+00:00"
    assert entry["duration"][()] == 2
    assert entry["duration"].attrs["units"] == "s"


def test_modules_classified_by_interface_class(nxs):
    classes = {
        name: g.attrs["NX_class"]
        for name, g in nxs[INST].items()
        if isinstance(g, h5py.Group)
    }
    assert classes == {
        "T_reg": "NXactuator",
        "T_sample": "NXsensor",
        "T_vti": "NXsensor",
        "field": "NXsensor",
        "spectrum": "NXsensor",
        "io": "NXcollection",
        "secop_description": "NXnote",
        "firmware": "NXprogram",
    }
    assert _str(nxs[f"{INST}/name"]) == "cryo7.example.org"
    describe = json.loads(_str(nxs[f"{INST}/secop_description/data"]))
    assert set(describe["modules"]) == {
        "T_reg",
        "T_sample",
        "T_vti",
        "field",
        "spectrum",
        "io",
    }


def test_meaning_fills_quantity_fields(nxs):
    assert _str(nxs[f"{INST}/T_reg/physical_quantity"]) == "temperature"
    assert _str(nxs[f"{INST}/T_reg/actuation_target"]) == "/entry/sample"
    assert _str(nxs[f"{INST}/T_sample/measurement"]) == "temperature"
    assert _str(nxs[f"{INST}/field/measurement"]) == "magnetic_field"
    assert "measurement" not in nxs[f"{INST}/spectrum"]


def test_float_log_with_relative_time(nxs):
    log = nxs[f"{INST}/T_reg/value_log"]
    assert log.attrs["NX_class"] == "NXlog"
    np.testing.assert_allclose(log["value"][()], [4.2, 4.3, 4.4])
    assert log["value"].attrs["units"] == "K"
    np.testing.assert_allclose(log["time"][()], [0.0, 1.0, 2.0])
    assert log["time"].attrs["units"] == "s"
    assert log["time"].attrs["start"] == "2025-10-09T08:53:20+00:00"
    assert _str(log["description"]) == "regulation temperature"
    assert json.loads(log["value"].attrs["secop_datainfo"])["unit"] == "K"


def test_none_dropped_and_sorted(nxs):
    log = nxs[f"{INST}/T_sample/value_log"]
    np.testing.assert_allclose(log["time"][()], [0.0, 2.0])
    np.testing.assert_allclose(log["value"][()], [3.8, 4.0])


def test_scaled_values_converted(nxs):
    ramp = nxs[f"{INST}/T_reg/ramp_log/value"]
    np.testing.assert_allclose(ramp[()], [1.5, 2.0])
    assert ramp.attrs["units"] == "K/min"


def test_status_split_into_code_and_text(nxs):
    codes = nxs[f"{INST}/T_reg/status_log/value"]
    assert codes[()].tolist() == [300, 300, 100]
    assert json.loads(codes.attrs["secop_enum"])["BUSY"] == 300
    # the changing status text is not written: NXlog holds numbers
    assert "status_text_log" not in nxs[f"{INST}/T_reg"]
    assert "status_text" not in nxs[f"{INST}/T_reg"]


def test_changing_text_dropped_constant_text_kept(tmp_path, cryostat):
    path = tmp_path / "text.nxs"
    t = T0 + np.arange(3.0)
    write_nexus(path, cryostat, {"io": {"_last_reply": (t, ["OK", "ERR", "OK"])}})
    with h5py.File(path, "r") as f:
        assert [k for k in f[f"{INST}/io"] if k.startswith("_last_reply")] == []
    write_nexus(path, cryostat, {"io": {"_last_reply": (t, ["OK", "OK", "OK"])}})
    with h5py.File(path, "r") as f:
        assert _str(f[f"{INST}/io/_last_reply"]) == "OK"


def test_constant_parameter_becomes_field(tmp_path, cryostat):
    path = tmp_path / "const.nxs"
    t = T0 + np.arange(3.0)
    logs = {
        "T_reg": {
            "value": (t, [4.2, 4.2, 4.2]),
            "target": (t, [4.5, 4.5, 4.6]),
            "status": (t, 3 * [[100, "at target"]]),
            "_pid": (t, 3 * [{"p": 2.5, "i": 30}]),
        },
        "spectrum": {"value": (t, 3 * [[1, 2, 3]])},
    }
    write_nexus(path, cryostat, logs)
    with h5py.File(path, "r") as f:
        group = f[f"{INST}/T_reg"]
        assert group["value"].shape == () and group["value"][()] == 4.2
        # time of the first recorded value
        assert group["value"].attrs["timestamp"] == "2025-10-09T08:53:20+00:00"
        assert "value_log" not in group and "data" not in group
        assert group["target_log/value"].shape == (3,)
        assert group["status"][()] == 100
        assert _str(group["status_text"]) == "at target"
        assert json.loads(_str(group["_pid"])) == {"p": 2.5, "i": 3.0}
        np.testing.assert_array_equal(f[f"{INST}/spectrum/value"][()], [1, 2, 3])


def test_node_and_module_properties(tmp_path, cryostat):
    cryostat["implementor"] = "ACME"
    cryostat["timeout"] = 12.5
    cryostat["_site"] = {"hall": 3}
    module = cryostat["modules"]["T_reg"]
    module["implementation"] = "acme.cryo.Regulation"
    module["group"] = "vti"
    module["features"] = []
    cryostat["modules"]["io"]["implementation"] = "acme.io.Serial"
    path = tmp_path / "props.nxs"
    write_nexus(path, cryostat, {})
    with h5py.File(path, "r") as f:
        inst = f[INST]
        assert _str(inst["description"]) == "test cryostat with VTI and sample stick"
        assert inst["firmware"].attrs["NX_class"] == "NXprogram"
        assert _str(inst["firmware/program"]) == "frappy 0.20"
        assert inst["fabrication"].attrs["NX_class"] == "NXfabrication"
        assert _str(inst["fabrication/vendor"]) == "ACME"
        # properties without a NeXus field: @secop_<name>
        assert inst.attrs["secop_timeout"] == 12.5
        assert json.loads(inst.attrs["secop__site"]) == {"hall": 3}
        assert "secop_firmware" not in inst.attrs
        group = inst["T_reg"]
        assert group["implementation"].attrs["NX_class"] == "NXprogram"
        assert _str(group["implementation/program"]) == "acme.cryo.Regulation"
        assert list(group.attrs["secop_interface_classes"]) == [
            "Drivable",
            "Writable",
            "Readable",
        ]
        assert group.attrs["secop_group"] == "vti"
        assert json.loads(group.attrs["secop_meaning"])["importance"] == 20
        assert "secop_features" not in group.attrs  # empty
        assert _str(inst["io/implementation/program"]) == "acme.io.Serial"


def test_bool_string_blob(nxs):
    assert nxs[f"{INST}/T_reg/_heater_on"][()] == np.True_
    assert _str(nxs[f"{INST}/io/_last_reply"]) == "OK"
    assert _str(nxs[f"{INST}/io/_raw"]) == "AAEC"
    assert _str(nxs[f"{INST}/io/description"]) == "serial communicator"


def test_struct_tuple_and_unknown_types_stored_as_json(nxs):
    pid = nxs[f"{INST}/T_reg/_pid"]
    assert pid.attrs["secop_encoding"] == "json"
    # the scaled struct member is converted to its physical value
    assert json.loads(_str(pid)) == {"p": 2.5, "i": 3.0}
    # a JSON list stays one string, also as a scalar field
    assert json.loads(_str(nxs[f"{INST}/T_reg/_limits"])) == [0.0, 300.0]
    peaks = _str(nxs[f"{INST}/spectrum/_peaks"])
    assert json.loads(peaks) == [{"pos": 1.0, "height": 2.0}]
    assert json.loads(_str(nxs[f"{INST}/spectrum/_future"])) == [1.0, 2.0]


def test_single_value_becomes_field(nxs):
    group = nxs[f"{INST}/T_reg"]
    # recorded once: a scalar field, no NXlog
    assert "target_log" not in group
    target = group["target"]
    assert target.shape == () and target[()] == 4.5
    assert target.attrs["units"] == "K"
    assert target.attrs["timestamp"] == "2025-10-09T08:53:20+00:00"
    assert target.attrs["description"] == "setpoint"
    assert json.loads(target.attrs["secop_datainfo"])["type"] == "double"
    # recorded several times: still an NXlog, no field
    assert "value" not in group and "ramp" not in group
    assert group["value_log"].attrs["NX_class"] == "NXlog"
    # the value of a sensor, too
    field = nxs[f"{INST}/field"]
    assert "value_log" not in field
    assert field["value"][()] == 0.001


def test_single_status_becomes_code_and_text_fields(tmp_path, cryostat):
    path = tmp_path / "status.nxs"
    write_nexus(path, cryostat, {"T_reg": {"status": ([T0], [[100, "at target"]])}})
    with h5py.File(path, "r") as f:
        group = f[f"{INST}/T_reg"]
        assert group["status"][()] == 100
        assert "IDLE" in json.loads(group["status"].attrs["secop_enum"])
        assert _str(group["status_text"]) == "at target"
        assert "status_log" not in group and "status_text_log" not in group


def test_single_array_value_becomes_1d_field(tmp_path):
    describe = (DATA / "shall_mass_spec_describe.json").read_text()
    path = tmp_path / "array.nxs"
    write_nexus(path, describe, {"mass_spec": {"value": ([T0], [[1e-9, 2e-9]])}})
    with h5py.File(path, "r") as f:
        np.testing.assert_allclose(f[f"{INST}/mass_spec/value"][()], [1e-9, 2e-9])


def test_field_never_shadows_a_nexus_name(tmp_path, cryostat):
    # a parameter called like a NeXus field of the group keeps its log
    cryostat["modules"]["T_reg"]["accessibles"]["name"] = {
        "description": "custom",
        "datainfo": {"type": "double"},
        "readonly": True,
    }
    path = tmp_path / "clash.nxs"
    write_nexus(path, cryostat, {"T_reg": {"name": ([T0], [1.5])}})
    with h5py.File(path, "r") as f:
        assert _str(f[f"{INST}/T_reg/name"]) == "T_reg"
        assert f[f"{INST}/T_reg/name_log/value"][()].tolist() == [1.5]


def test_sample_links_field_of_single_value(tmp_path, cryostat):
    path = tmp_path / "single.nxs"
    write_nexus(path, cryostat, {"T_sample": {"value": ([T0], [3.8])}})
    with h5py.File(path, "r") as f:
        sample = f["entry/sample"]
        assert "temperature_log" not in sample
        link = sample.get("temperature", getlink=True)
        assert link.path == "/entry/instrument/T_sample/value"
        assert sample["temperature"][()] == 3.8


def test_numeric_array_is_2d(nxs):
    value = nxs[f"{INST}/spectrum/value_log/value"]
    assert value.shape == (2, 3)
    assert value.dtype == np.int64


def test_commands_and_unrecorded_parameters_skipped(nxs):
    assert "stop_log" not in nxs[f"{INST}/T_reg"]
    assert "communicate_log" not in nxs[f"{INST}/io"]
    assert "status_log" not in nxs[f"{INST}/T_vti"]


def test_sample_environment_links(nxs):
    sample = nxs["entry/sample"]
    assert sample.attrs["NX_class"] == "NXsample"
    env = sample["temperature_env"]
    assert env.attrs["NX_class"] == "NXenvironment"
    assert _str(env["name"]) == "cryo7.example.org"
    links = {
        name: env.get(name, getlink=True).path
        for name in env
        if isinstance(env.get(name, getlink=True), h5py.SoftLink)
    }
    assert links == {
        "T_reg": "/entry/instrument/T_reg",
        "T_sample": "/entry/instrument/T_sample",
        # list-style (SECoP 1.x) meaning counts as sample meaning
        "T_vti": "/entry/instrument/T_vti",
    }
    assert env["T_reg"].attrs["NX_class"] == "NXactuator"
    # highest importance measuring module, never the regulation one
    link = sample.get("temperature_log", getlink=True)
    assert link.path == "/entry/instrument/T_sample/value_log"
    np.testing.assert_allclose(sample["temperature_log/value"][()], [3.8, 4.0])
    # belongs_to defaults to "other": the field probe is not a sample environment
    assert "magnetic_field_env" not in sample


def test_no_sample_without_sample_meanings(tmp_path):
    describe = json.loads((DATA / "shall_mass_spec_describe.json").read_text())
    tree = build_nexus_tree(describe, {})
    assert tree.entries["entry"].samples == {}


def test_shall_node_ragged_arrays_fall_back_to_json(tmp_path):
    describe = (DATA / "shall_mass_spec_describe.json").read_text()
    logs = {
        "mass_spec": {
            "value": ParameterLog([T0, T0 + 1], [[1e-9, 2e-9], [3e-9, 4e-9]]),
            "_mass": ParameterLog([T0, T0 + 1], [[1.0, 2.0], [3.0, 4.0, 5.0]]),
            "_mid_descriptor": ParameterLog(
                [T0, T0 + 1],
                [{"device": [1.0], "mass": [28.0]}, {"device": [2.0], "mass": [28.0]}],
            ),
        }
    }
    path = tmp_path / "shall.nxs"
    write_nexus(path, describe, logs)
    with h5py.File(path, "r") as f:
        group = f[f"{INST}/mass_spec"]
        assert group.attrs["NX_class"] == "NXsensor"
        assert group["value_log/value"].shape == (2, 2)
        assert [json.loads(v) for v in _strs(group["_mass_log/value"])] == [
            [1.0, 2.0],
            [3.0, 4.0, 5.0],
        ]
        assert json.loads(_strs(group["_mid_descriptor_log/value"])[0])["mass"] == [
            28.0
        ]


def test_unknown_parameter_warns(cryostat, caplog):
    with caplog.at_level(logging.WARNING):
        build_nexus_tree(cryostat, {"T_reg": {"nope": ([T0], [1.0])}})
    assert "T_reg:nope" in caplog.text


def test_mismatched_lengths_rejected(cryostat):
    with pytest.raises(ValueError, match="2 timestamps but 1 values"):
        build_nexus_tree(cryostat, {"T_reg": {"value": ([T0, T0 + 1], [1.0])}})


def test_nexus_bytes_and_json_describe(cryostat, cryostat_logs):
    data = nexus_bytes(json.dumps(cryostat).encode(), cryostat_logs, title="run 42")
    assert data[:8] == b"\x89HDF\r\n\x1a\n"


def test_empty_logs(tmp_path, cryostat):
    path = tmp_path / "empty.nxs"
    write_nexus(path, cryostat, {})
    with h5py.File(path, "r") as f:
        assert "start_time" not in f["entry"]
        assert f[f"{INST}/T_reg"].attrs["NX_class"] == "NXactuator"
        assert "value_log" not in f[f"{INST}/T_reg"]


def _nxdata(f) -> list[str]:
    found = []
    f.visititems(
        lambda name, g: (
            found.append(name)
            if isinstance(g, h5py.Group) and g.attrs.get("NX_class") == "NXdata"
            else None
        )
    )
    return sorted(found)


def test_one_nxdata_per_module_with_numeric_value(nxs):
    # nothing at entry level; io has no value, field only a single one
    assert _nxdata(nxs) == [
        f"{INST}/{m}/data" for m in ("T_reg", "T_sample", "T_vti", "spectrum")
    ]


def test_readable_plot_links_into_value_log(nxs):
    plot = nxs[f"{INST}/T_sample/data"]
    assert plot.attrs["signal"] == "value"
    assert "auxiliary_signals" not in plot.attrs
    assert plot.attrs["axes"] == "time"
    assert plot.attrs["time_indices"] == 0
    assert _str(plot["title"]) == "T_sample"
    assert plot.get("value", getlink=True).path == f"/{INST}/T_sample/value_log/value"
    assert plot.get("time", getlink=True).path == f"/{INST}/T_sample/value_log/time"
    assert plot["value"].attrs["long_name"] == "T_sample:value (K)"
    assert plot["time"].attrs["long_name"] == "time since start_time (s)"
    assert nxs[f"{INST}/T_sample"].attrs["default"] == "data"


def test_plot_has_only_the_value(nxs):
    # T_reg has a target, but it has its own time axis: not part of the plot
    plot = nxs[f"{INST}/T_reg/data"]
    assert sorted(plot) == ["time", "title", "value"]
    assert "auxiliary_signals" not in plot.attrs
    np.testing.assert_allclose(plot["value"][()], [4.2, 4.3, 4.4])


def test_nxdata_2d_array(nxs):
    plot = nxs[f"{INST}/spectrum/data"]
    assert list(plot.attrs["axes"]) == ["time", "."]
    assert plot["value"].shape == (2, 3)


def test_default_plot_is_main_sample_quantity(nxs):
    assert nxs.attrs["default"] == "entry"
    assert nxs["entry"].attrs["default"] == "instrument"
    assert nxs[INST].attrs["default"] == "T_sample"


def test_default_plot_without_sample(tmp_path):
    describe = (DATA / "shall_mass_spec_describe.json").read_text()
    logs = {
        "mass_spec": {
            "_emission": ([T0], [1.0]),
            "value": ([T0, T0 + 1], [[1.0, 2.0], [3.0, 4.0]]),
        }
    }
    path = tmp_path / "shall.nxs"
    write_nexus(path, describe, logs)
    with h5py.File(path, "r") as f:
        assert f[INST].attrs["default"] == "mass_spec"
        assert f[f"{INST}/mass_spec"].attrs["default"] == "data"


def test_no_default_plot_without_numeric_logs(tmp_path, cryostat):
    path = tmp_path / "strings.nxs"
    write_nexus(path, cryostat, {"io": {"_last_reply": ([T0], ["OK"])}})
    with h5py.File(path, "r") as f:
        assert "default" not in f["entry"].attrs
        assert _nxdata(f) == []
