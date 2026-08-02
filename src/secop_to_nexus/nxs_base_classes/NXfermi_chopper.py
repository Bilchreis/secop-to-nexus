"""Auto-generated from NXfermi_chopper.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
class NXfermi_chopper(NXcomponent):
    """A Fermi chopper, possibly with curved slits."""

    type: Optional[NX_CHAR] = None
    rotation_speed: Optional[NX_FLOAT] = None  # units: NX_FREQUENCY
    radius: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    slit: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    r_slit: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    number: Optional[NX_INT] = None  # units: NX_UNITLESS
    height: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    width: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    distance: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    wavelength: Optional[NX_FLOAT] = None  # units: NX_WAVELENGTH
    energy: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    absorbing_material: Optional[NX_CHAR] = None
    transmitting_material: Optional[NX_CHAR] = None
    depends_on: Optional[NX_CHAR] = None
    geometries: dict[str, NXgeometry] = dc_field(
        default_factory=dict
    )  # geometry of the fermi chopper
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the beam line component
