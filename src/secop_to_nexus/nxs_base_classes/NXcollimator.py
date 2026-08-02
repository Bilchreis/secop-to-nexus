"""Auto-generated from NXcollimator.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXlog import NXlog
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry


@dataclass
class NXcollimator(NXcomponent):
    """A beamline collimator."""

    type: Optional[NX_CHAR] = None  # enum: Soller | radial | oscillating | honeycomb
    soller_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    divergence_x: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    divergence_y: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    frequency: Optional[NX_FLOAT] = None  # units: NX_FREQUENCY
    blade_thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    blade_spacing: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    absorbing_material: Optional[NX_CHAR] = None
    transmitting_material: Optional[NX_CHAR] = None
    depends_on: Optional[NX_CHAR] = None
    geometries: dict[str, NXgeometry] = dc_field(
        default_factory=dict
    )  # position, shape and size
    frequency_log: Optional[NXlog] = None  # Log of frequency
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the beam line component
