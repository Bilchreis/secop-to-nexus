"""Auto-generated from NXbeam_stop.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
    from secop_to_nexus.nxs_base_classes.NXcylindrical_geometry import (
        NXcylindrical_geometry,
    )
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry


@dataclass
class NXbeam_stop(NXcomponent):
    """A device that blocks the beam completely, usually to protect a detector.

    Beamstops and their positions are important for SANS
    and SAXS experiments.
    """

    description: Optional[NX_CHAR] = None  # enum: circular | rectangular
    size: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    x: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    y: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    distance_to_detector: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    status: Optional[NX_CHAR] = None  # enum: in | out
    depends_on: Optional[NX_CHAR] = None
    geometries: dict[str, NXgeometry] = dc_field(
        default_factory=dict
    )  # engineering shape, orientation and position of the beam stop.
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the beam line component
    cylindrical_geometries: dict[str, NXcylindrical_geometry] = dc_field(
        default_factory=dict
    )  # This group is an alternative to NXoff_geometry for describing the shape
