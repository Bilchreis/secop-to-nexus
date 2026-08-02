"""Auto-generated from NXdisk_chopper.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
    NX_INT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry


@dataclass
class NXdisk_chopper(NXcomponent):
    """A device blocking the beam in a temporal periodic pattern.

    A disk which blocks the beam but has one or more slits to periodically
    let neutrons through as the disk rotates. Often used in pairs, one
    NXdisk_chopper should be defined for each disk.

    The rotation of the disk is commonly monitored by recording a timestamp for
    each full rotation of disk, by having a sensor in the stationary disk housing
    sensing when it is aligned with a feature (such as a magnet) on the disk.
    We refer to this below as the "top-dead-center signal".

    Angles and positive rotation speeds are measured in an anticlockwise
    direction when facing away from the source.
    """

    type: Optional[NX_CHAR] = (
        None  # enum: Chopper type single | contra_rotating_pair | synchr...
    )
    rotation_speed: Optional[NX_FLOAT] = None  # units: NX_FREQUENCY
    slits: Optional[NX_INT] = None
    slit_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    pair_separation: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    slit_edges: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    top_dead_center: Optional[NX_NUMBER] = None  # units: NX_TIME
    beam_position: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    radius: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    slit_height: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    phase: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    delay: Optional[NX_NUMBER] = None  # units: NX_TIME
    ratio: Optional[NX_INT] = None
    distance: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    wavelength_range: Optional[NX_FLOAT] = None  # units: NX_WAVELENGTH
    depends_on: Optional[NX_CHAR] = None
    geometries: dict[str, NXgeometry] = dc_field(default_factory=dict)
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the beam line component
