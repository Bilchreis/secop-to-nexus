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
    texts = nxs[f"{INST}/T_reg/status_text_log/value"]
    assert _strs(texts) == ["ramping", "ramping", "at target"]


def test_bool_string_blob(nxs):
    assert nxs[f"{INST}/T_reg/_heater_on_log/value"][()].tolist() == [True]
    assert _strs(nxs[f"{INST}/io/_last_reply_log/value"]) == ["OK"]
    assert _strs(nxs[f"{INST}/io/_raw_log/value"]) == ["AAEC"]
    assert _str(nxs[f"{INST}/io/description"]) == "serial communicator"


def test_struct_tuple_and_unknown_types_stored_as_json(nxs):
    pid = nxs[f"{INST}/T_reg/_pid_log/value"]
    assert pid.attrs["secop_encoding"] == "json"
    # the scaled struct member is converted to its physical value
    assert json.loads(_strs(pid)[0]) == {"p": 2.5, "i": 3.0}
    assert json.loads(_strs(nxs[f"{INST}/T_reg/_limits_log/value"])[0]) == [0.0, 300.0]
    peaks = _strs(nxs[f"{INST}/spectrum/_peaks_log/value"])
    assert json.loads(peaks[0]) == [{"pos": 1.0, "height": 2.0}]
    assert json.loads(_strs(nxs[f"{INST}/spectrum/_future_log/value"])[0]) == [1.0, 2.0]


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
            "_mid_descriptor": ParameterLog([T0], [{"device": [1.0], "mass": [28.0]}]),
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
    # nothing at entry level; io has no value
    assert _nxdata(nxs) == [
        f"{INST}/{m}/data" for m in ("T_reg", "T_sample", "T_vti", "field", "spectrum")
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
            "value": ([T0], [[1.0, 2.0]]),
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
