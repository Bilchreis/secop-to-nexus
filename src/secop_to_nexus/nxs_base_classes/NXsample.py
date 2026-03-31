from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional

from secop_to_nexus.nxs_base_classes.NXdtypes import (
    NX_CHAR,
    NX_DATE_TIME,
    NX_FLOAT,
    NX_INT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXbeam import NXbeam
    from secop_to_nexus.nxs_base_classes.NXenvironment import NXenvironment
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry
    from secop_to_nexus.nxs_base_classes.NXpositioner import NXpositioner
    from secop_to_nexus.nxs_base_classes.NXsample_component import NXsample_component


@dataclass
class NXsample(NXobject):
    name: Optional[NX_CHAR] = None
    chemical_formula: Optional[NX_CHAR] = None
    temperature: Optional[NX_FLOAT] = None  # units: NX_TEMPERATURE
    electric_field: Optional[NX_FLOAT] = None  # units: NX_VOLTAGE
    magnetic_field: Optional[NX_FLOAT] = None  # units: NX_ANY
    stress_field: Optional[NX_FLOAT] = None  # units: NX_ANY
    pressure: Optional[NX_FLOAT] = None  # units: NX_PRESSURE
    changer_position: Optional[NX_INT] = None
    unit_cell_abc: Optional[NX_FLOAT] = None  # units: NX_LENGTH, 3 elements
    unit_cell_alphabetagamma: Optional[NX_FLOAT] = None  # units: NX_ANGLE, 3 elements
    unit_cell: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    unit_cell_volume: Optional[NX_FLOAT] = None  # units: NX_VOLUME
    sample_orientation: Optional[NX_FLOAT] = None  # units: NX_ANGLE, 3 elements
    orientation_matrix: Optional[NX_FLOAT] = None
    ub_matrix: Optional[NX_FLOAT] = None
    mass: Optional[NX_FLOAT] = None  # units: NX_MASS
    density: Optional[NX_FLOAT] = None  # units: NX_MASS_DENSITY
    relative_molecular_mass: Optional[NX_FLOAT] = None  # units: NX_MASS
    type: Optional[NX_CHAR] = None  # e.g. "sample", "can", "sample+can", ...
    situation: Optional[NX_CHAR] = None  # e.g. "air", "vacuum", ...
    description: Optional[NX_CHAR] = None
    preparation_date: Optional[NX_DATE_TIME] = None
    component: Optional[NX_CHAR] = None
    sample_component: Optional[NX_CHAR] = None  # e.g. "sample", "solvent", ...
    concentration: Optional[NX_FLOAT] = None  # units: NX_MASS_DENSITY
    volume_fraction: Optional[NX_FLOAT] = None
    scattering_length_density: Optional[NX_FLOAT] = None
    unit_cell_class: Optional[NX_CHAR] = None  # e.g. "triclinic", "monoclinic", ...
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

    # Arbitrarily named groups
    beams: dict[str, NXbeam] = field(default_factory=dict)
    sample_components: dict[str, NXsample_component] = field(default_factory=dict)
    positioners: dict[str, NXpositioner] = field(default_factory=dict)
    off_geometries: dict[str, NXoff_geometry] = field(default_factory=dict)
    environments: dict[str, NXenvironment] = field(default_factory=dict)
