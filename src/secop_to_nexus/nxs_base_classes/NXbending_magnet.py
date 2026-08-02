"""Auto-generated from NXbending_magnet.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry


@dataclass
class NXbending_magnet(NXcomponent):
    """A bending magnet"""

    critical_energy: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    bending_radius: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    magnetic_field: Optional[NX_FLOAT] = None  # units: NX_CURRENT
    accepted_photon_beam_divergence: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    source_distance_x: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    source_distance_y: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    divergence_x_plus: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    divergence_x_minus: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    divergence_y_plus: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    divergence_y_minus: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    depends_on: Optional[NX_CHAR] = None
    spectrum: Optional[NXdata] = None  # bending magnet spectrum
    geometries: dict[str, NXgeometry] = dc_field(
        default_factory=dict
    )  # "Engineering" position of bending magnet
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the beam line component
