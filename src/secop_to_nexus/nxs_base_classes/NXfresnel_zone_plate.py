"""Auto-generated from NXfresnel_zone_plate.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent


@dataclass
class NXfresnel_zone_plate(NXcomponent):
    """A fresnel zone plate"""

    focus_parameters: Optional[NX_FLOAT] = None
    outer_diameter: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    outermost_zone_width: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    central_stop_diameter: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    fabrication: Optional[NX_CHAR] = (
        None  # enum: etched | plated | zone doubled | other
    )
    zone_height: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    zone_material: Optional[NX_CHAR] = None
    zone_support_material: Optional[NX_CHAR] = None
    central_stop_material: Optional[NX_CHAR] = None
    central_stop_thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    mask_thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    mask_material: Optional[NX_CHAR] = None
    support_membrane_material: Optional[NX_CHAR] = None
    support_membrane_thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    depends_on: Optional[NX_CHAR] = None
