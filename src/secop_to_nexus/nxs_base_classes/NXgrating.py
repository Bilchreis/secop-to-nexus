"""Auto-generated from NXgrating.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry
    from secop_to_nexus.nxs_base_classes.NXshape import NXshape
    from secop_to_nexus.nxs_base_classes.NXtransformations import NXtransformations


@dataclass
class NXgrating(NXcomponent):
    """A diffraction grating, as could be used in a soft X-ray monochromator"""

    angles: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    period: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    duty_cycle: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    depth: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    diffraction_order: Optional[NX_INT] = None  # units: NX_UNITLESS
    deflection_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    interior_atmosphere: Optional[NX_CHAR] = None  # enum: vacuum | helium | argon
    substrate_material: Optional[NX_CHAR] = None
    substrate_density: Optional[NX_FLOAT] = None  # units: NX_MASS_DENSITY
    substrate_thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    coating_material: Optional[NX_CHAR] = None
    substrate_roughness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    coating_roughness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    layer_thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    depends_on: Optional[NX_CHAR] = None
    shape: Optional[NXshape] = (
        None  # A NXshape group describing the shape of the mirror
    )
    figure_data: Optional[NXdata] = (
        None  # Numerical description of the surface figure of the mirror.
    )
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the beam line component
    transformations: dict[str, NXtransformations] = dc_field(
        default_factory=dict
    )  # "Engineering" position of the grating
