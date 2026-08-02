"""End-to-end: NXobject tree -> NexusCreator dict -> injected values -> .nxs file."""

import h5py
import numpy as np
import pytest
from libraries.NeXusHDF5 import NexusHDF5Writer, NexusValueInjector

from secop_to_nexus.nxs_base_classes import (
    NXdata,
    NXentry,
    NXinstrument,
    NXroot,
    NXsensor,
)
from secop_to_nexus.nxs_base_classes.NXdtypes import NX_CHAR, NX_FLOAT, Placeholder


@pytest.fixture
def tree() -> NXroot:
    root = NXroot(
        entries={
            "entry": NXentry(
                title=NX_CHAR("SECoP demo measurement"),
                default="data",
                instruments={
                    "cryostat": NXinstrument(
                        name=NX_CHAR("cryostat"),
                        sensors={
                            "temp_sensor": NXsensor(
                                name=NX_CHAR("sample temperature"),
                                measurement=NX_CHAR("temperature"),
                                value=NX_FLOAT(Placeholder("temp_data"), units="K"),
                            )
                        },
                    )
                },
                data={
                    "data": NXdata(
                        signal="temperature",
                        axes="time",
                        DATA={
                            "temperature": NX_FLOAT(
                                Placeholder("temp_data"), units="K", array=True
                            )
                        },
                        AXISNAME={
                            "time": NX_FLOAT(
                                Placeholder("time_data"), units="s", array=True
                            )
                        },
                    )
                },
            )
        }
    )
    root.finalize()
    return root


def test_serialized_dict_shape(tree):
    d = tree.to_nexus_dict()
    assert d["@NX_class"] == "NXroot"
    entry = d["entry"]
    assert entry["@NX_class"] == "NXentry"
    assert entry["@default"] == "data"
    assert entry["title"] == {"@dtype": "NX_CHAR", "@value": "SECoP demo measurement"}
    data = entry["data"]
    assert data["@signal"] == "temperature"
    assert data["temperature"]["@value"] == "temp_data"
    assert data["temperature"]["@dtype"] == "NX_FLOAT64[]"


def test_write_and_read_back_nxs(tree, tmp_path):
    nexus_object = tree.to_nexus_dict()
    library = {
        "temp_data": [4.2, 4.3, 4.5],
        "time_data": [0.0, 1.0, 2.0],
    }
    NexusValueInjector(library).inject(nexus_object)
    outfile = tmp_path / "e2e.nxs"
    NexusHDF5Writer(nexus_object).write(str(outfile))

    with h5py.File(outfile, "r") as f:
        assert f.attrs["NX_class"] == "NXroot"
        assert f["entry"].attrs["NX_class"] == "NXentry"
        assert f["entry"].attrs["default"] == "data"
        assert f["entry/title"][()].decode() == "SECoP demo measurement"

        sensor = f["entry/cryostat/temp_sensor"]
        assert sensor.attrs["NX_class"] == "NXsensor"
        # scalar placeholder got the injected array
        np.testing.assert_allclose(sensor["value"][()], [4.2, 4.3, 4.5])
        assert sensor["value"].attrs["units"] == "K"

        data = f["entry/data"]
        assert data.attrs["signal"] == "temperature"
        assert data.attrs["axes"] == "time"
        np.testing.assert_allclose(data["temperature"][()], [4.2, 4.3, 4.5])
        np.testing.assert_allclose(data["time"][()], [0.0, 1.0, 2.0])
