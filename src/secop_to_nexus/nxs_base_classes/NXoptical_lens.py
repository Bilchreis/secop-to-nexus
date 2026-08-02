"""Auto-generated from NXoptical_lens.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_FLOAT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXsample import NXsample


@dataclass
class NXoptical_lens(NXcomponent):
    """Description of an optical lens."""

    type: Optional[NX_CHAR] = (
        None  # enum: biconcave | plano-concave | convexo-concave | bicon...
    )
    chromatic: Optional[NX_BOOLEAN] = None
    lens_diameter: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    reflectance: Optional[NX_CHAR] = None  # units: NX_UNITLESS
    transmission: Optional[NX_CHAR] = None  # units: NX_UNITLESS
    focal_length: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    curvature_radius_FACE: dict[str, NX_NUMBER] = dc_field(
        default_factory=dict
    )  # nameType: partial; units: NX_LENGTH
    Abbe_number: Optional[NX_NUMBER] = None  # units: NX_UNITLESS
    numerical_aperture: Optional[NX_NUMBER] = None
    magnification: Optional[NX_FLOAT] = None
    substrate: Optional[NXsample] = (
        None  # Properties of the substrate material of the lens. If the lens has a
    )
    COATING: dict[str, NXsample] = dc_field(default_factory=dict)  # nameType: any
