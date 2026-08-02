import dataclasses

import pytest

import secop_to_nexus.nxs_base_classes as nxs
from secop_to_nexus.nxs_base_classes import (
    NXactuator,
    NXcomponent,
    NXdata,
    NXentry,
    NXinstrument,
    NXobject,
    NXroot,
    NXsensor,
)


@pytest.fixture(scope="module")
def all_classes():
    return [getattr(nxs, name) for name in nxs.__all__]


def test_all_classes_exported(all_classes):
    assert len(all_classes) == 142


def test_every_class_instantiable_and_serializable(all_classes):
    for cls in all_classes:
        instance = cls()
        assert instance.to_nexus_dict() == {"@NX_class": cls.__name__}


def test_every_class_extends_nxobject(all_classes):
    for cls in all_classes:
        assert issubclass(cls, NXobject)


def test_actuator_inherits_component():
    assert issubclass(NXactuator, NXcomponent)
    actuator = NXactuator()
    assert hasattr(actuator, "description")
    assert hasattr(actuator, "depends_on")
    assert actuator.outputVALUE == {}


def test_arbitrarily_named_groups_are_dicts():
    entry = NXentry()
    for field_name in ("users", "samples", "instruments", "subentries"):
        assert getattr(entry, field_name) == {}
    assert NXinstrument().sensors == {}
    assert NXroot().entries == {}


def test_nxdata_signal_and_axes_are_attributes():
    fields = {f.name: f for f in dataclasses.fields(NXdata)}
    for name in ("signal", "axes", "auxiliary_signals"):
        assert fields[name].metadata.get("kind") == "attribute"
    # DATA / AXISNAME are the arbitrarily named dataset containers
    assert fields["DATA"].default_factory is dict
    assert fields["AXISNAME"].default_factory is dict


def test_sensor_has_spec_fields():
    sensor = NXsensor()
    for name in ("name", "measurement", "value", "value_log", "run_control"):
        assert hasattr(sensor, name)
