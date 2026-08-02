"""Auto-generated from NXvelocity_selector.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
    NX_INT,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry


@dataclass
class NXvelocity_selector(NXcomponent):
    """A neutron velocity selector"""

    type: Optional[NX_CHAR] = None
    rotation_speed: Optional[NX_FLOAT] = None  # units: NX_FREQUENCY
    radius: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    spwidth: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    length: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    num: Optional[NX_INT] = None  # units: NX_UNITLESS
    twist: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    table: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    height: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    width: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    wavelength: Optional[NX_FLOAT] = None  # units: NX_WAVELENGTH
    wavelength_spread: Optional[NX_FLOAT] = None  # units: NX_WAVELENGTH
    depends_on: Optional[NX_CHAR] = None
    geometry: Optional[NXgeometry] = None
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the beam line component
