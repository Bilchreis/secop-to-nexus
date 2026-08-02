"""Auto-generated from NXaperture.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXnote import NXnote
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry
    from secop_to_nexus.nxs_base_classes.NXpositioner import NXpositioner


@dataclass
class NXaperture(NXcomponent):
    """A beamline aperture.

    Note, the group was incorrectly documented as deprecated, but it is not and it is in common use.

    You can specify the geometry of the aperture using either NXoff_geometry or for simpler geometry shape and size.
    """

    depends_on: Optional[NX_CHAR] = None
    material: Optional[NX_CHAR] = None
    description: Optional[NX_CHAR] = None
    shape: Optional[NX_CHAR] = (
        None  # enum: straight slit | curved slit | pinhole | circle | sq...
    )
    size: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # Use this group to describe the shape of the aperture.
    positioners: dict[str, NXpositioner] = dc_field(
        default_factory=dict
    )  # Stores the raw positions of aperture motors.
    geometries: dict[str, NXgeometry] = dc_field(
        default_factory=dict
    )  # Location and shape of aperture
    BLADE_GEOMETRY: Optional[NXgeometry] = None  # location and shape of each blade
    notes: dict[str, NXnote] = dc_field(
        default_factory=dict
    )  # Describe any additional information in a note.
