"""Auto-generated from NXsample_component.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXhistory import NXhistory


@dataclass
class NXsample_component(NXcomponent):
    """One group like this per component can be recorded for a sample consisting of multiple components."""

    name: Optional[NX_CHAR] = None
    chemical_formula: Optional[NX_CHAR] = None
    unit_cell_abc: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    unit_cell_alphabetagamma: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    unit_cell_volume: Optional[NX_FLOAT] = None  # units: NX_VOLUME
    sample_orientation: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    orientation_matrix: Optional[NX_FLOAT] = None
    mass: Optional[NX_FLOAT] = None  # units: NX_MASS
    density: Optional[NX_FLOAT] = None  # units: NX_MASS_DENSITY
    relative_molecular_mass: Optional[NX_FLOAT] = None  # units: NX_MASS
    description: Optional[NX_CHAR] = None
    volume_fraction: Optional[NX_FLOAT] = None
    scattering_length_density: Optional[NX_FLOAT] = (
        None  # units: NX_SCATTERING_LENGTH_DENSITY
    )
    unit_cell_class: Optional[NX_CHAR] = (
        None  # enum: triclinic | monoclinic | orthorhombic | tetragonal ...
    )
    space_group: Optional[NX_CHAR] = None
    point_group: Optional[NX_CHAR] = None
    transmission: Optional[NXdata] = None  # As a function of Wavelength
    history: Optional[NXhistory] = (
        None  # A set of physical processes that occurred to the sample component prior/during
    )
