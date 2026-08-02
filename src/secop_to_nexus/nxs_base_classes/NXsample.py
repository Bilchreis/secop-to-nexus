"""Auto-generated from NXsample.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_DATE_TIME,
    NX_FLOAT,
    NX_INT,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXbeam import NXbeam
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXenvironment import NXenvironment
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXhistory import NXhistory
    from secop_to_nexus.nxs_base_classes.NXlog import NXlog
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry
    from secop_to_nexus.nxs_base_classes.NXpositioner import NXpositioner
    from secop_to_nexus.nxs_base_classes.NXsample_component import NXsample_component


@dataclass
class NXsample(NXcomponent):
    """Any information on the sample.

    This could include scanned variables that
    are associated with one of the data dimensions, e.g. the magnetic field, or
    logged data, e.g. monitored temperature vs elapsed time.
    """

    name: Optional[NX_CHAR] = None
    chemical_formula: Optional[NX_CHAR] = None
    temperature: Optional[NX_FLOAT] = None  # units: NX_TEMPERATURE
    electric_field: Optional[NX_FLOAT] = None  # units: NX_VOLTAGE
    magnetic_field: Optional[NX_FLOAT] = None  # units: NX_ANY
    stress_field: Optional[NX_FLOAT] = None  # units: NX_ANY
    pressure: Optional[NX_FLOAT] = None  # units: NX_PRESSURE
    changer_position: Optional[NX_INT] = None  # units: NX_UNITLESS
    unit_cell_abc: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    unit_cell_alphabetagamma: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    unit_cell: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    unit_cell_volume: Optional[NX_FLOAT] = None  # units: NX_VOLUME
    sample_orientation: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    orientation_matrix: Optional[NX_FLOAT] = None
    ub_matrix: Optional[NX_FLOAT] = None
    mass: Optional[NX_FLOAT] = None  # units: NX_MASS
    density: Optional[NX_FLOAT] = None  # units: NX_MASS_DENSITY
    relative_molecular_mass: Optional[NX_FLOAT] = None  # units: NX_MASS
    type: Optional[NX_CHAR] = (
        None  # enum: sample | sample+can | can | sample+buffer | buffer ...
    )
    situation: Optional[NX_CHAR] = (
        None  # enum: air | vacuum | inert atmosphere | oxidising atmosph...
    )
    description: Optional[NX_CHAR] = None
    preparation_date: Optional[NX_DATE_TIME] = None
    component: Optional[NX_CHAR] = None
    sample_component: Optional[NX_CHAR] = None  # enum: sample | can | atmosphere | kit
    concentration: Optional[NX_FLOAT] = None  # units: NX_MASS_DENSITY
    volume_fraction: Optional[NX_FLOAT] = None
    scattering_length_density: Optional[NX_FLOAT] = (
        None  # units: NX_SCATTERING_LENGTH_DENSITY
    )
    unit_cell_class: Optional[NX_CHAR] = (
        None  # enum: triclinic | monoclinic | orthorhombic | tetragonal ...
    )
    space_group: Optional[NX_CHAR] = None
    point_group: Optional[NX_CHAR] = None
    path_length: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    path_length_window: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    external_DAC: Optional[NX_FLOAT] = None  # units: NX_ANY
    short_title: Optional[NX_CHAR] = None
    rotation_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    x_translation: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    distance: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    physical_form: Optional[NX_CHAR] = None
    geometry: Optional[NXgeometry] = (
        None  # The position and orientation of the center of mass of the sample
    )
    beams: dict[str, NXbeam] = dc_field(
        default_factory=dict
    )  # Details of beam incident on sample - used to calculate sample/beam interaction point
    sample_components: dict[str, NXsample_component] = dc_field(
        default_factory=dict
    )  # One group per sample component
    transmission: Optional[NXdata] = None  # As a function of Wavelength
    temperature_log: Optional[NXlog] = (
        None  # temperature_log.value is a link to e.g. temperature_env.sensor1.value_log.value
    )
    temperature_env: Optional[NXenvironment] = (
        None  # Additional sample temperature environment information
    )
    magnetic_field: Optional[NXlog] = (
        None  # magnetic_field.value is a link to e.g. magnetic_field_env.sensor1.value
    )
    magnetic_field_log: Optional[NXlog] = (
        None  # magnetic_field_log.value is a link to e.g. magnetic_field_env.sensor1.value_log.value
    )
    magnetic_field_env: Optional[NXenvironment] = (
        None  # Additional sample magnetic environment information
    )
    external_ADC: Optional[NXlog] = (
        None  # logged value (or logic state) read from user's setup
    )
    positioners: dict[str, NXpositioner] = dc_field(
        default_factory=dict
    )  # Any positioner (motor, PZT, ...) used to locate the sample
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the sample
    environments: dict[str, NXenvironment] = dc_field(
        default_factory=dict
    )  # Any environmental or external stimuli/measurements.
    history: Optional[NXhistory] = (
        None  # A set of physical processes that occurred to the sample prior/during experiment.
    )
