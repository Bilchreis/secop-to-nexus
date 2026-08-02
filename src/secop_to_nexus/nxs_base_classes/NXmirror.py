"""Auto-generated from NXmirror.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
    from secop_to_nexus.nxs_base_classes.NXshape import NXshape


@dataclass
class NXmirror(NXcomponent):
    """A beamline mirror or supermirror."""

    type: Optional[NX_CHAR] = None  # enum: single | multi
    description: Optional[NX_CHAR] = None
    incident_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    bend_angle_x: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    bend_angle_y: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    interior_atmosphere: Optional[NX_CHAR] = None  # enum: vacuum | helium | argon
    external_material: Optional[NX_CHAR] = None
    m_value: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    substrate_material: Optional[NX_CHAR] = None
    substrate_density: Optional[NX_FLOAT] = None  # units: NX_MASS_DENSITY
    substrate_thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    coating_material: Optional[NX_CHAR] = None
    substrate_roughness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    coating_roughness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    even_layer_material: Optional[NX_CHAR] = None
    even_layer_density: Optional[NX_FLOAT] = None  # units: NX_MASS_DENSITY
    odd_layer_material: Optional[NX_CHAR] = None
    odd_layer_density: Optional[NX_FLOAT] = None  # units: NX_MASS_DENSITY
    layer_thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    depends_on: Optional[NX_CHAR] = None
    geometries: dict[str, NXgeometry] = dc_field(default_factory=dict)
    reflectivity: Optional[NXdata] = None  # Reflectivity as function of wavelength
    shape: Optional[NXshape] = (
        None  # A NXshape group describing the shape of the mirror
    )
    figure_data: Optional[NXdata] = (
        None  # Numerical description of the surface figure of the mirror.
    )
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the beam line component
