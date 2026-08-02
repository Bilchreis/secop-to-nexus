"""Auto-generated from NXapm_reconstruction.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
)
from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcollection import NXcollection
    from secop_to_nexus.nxs_base_classes.NXnote import NXnote
    from secop_to_nexus.nxs_base_classes.NXparameters import NXparameters
    from secop_to_nexus.nxs_base_classes.NXprogram import NXprogram


@dataclass
class NXapm_reconstruction(NXprocess):
    """Base class for the configuration and results of a reconstruction algorithm.

    Generating a tomographic reconstruction of the specimen uses selected and
    calibrated ion hit positions, the evaporation sequence, and voltage curve data.
    Very often scientists use own software scripts according to published procedures,
    so-called reconstruction protocols.
    """

    reconstructed_positions: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    quality: Optional[NX_CHAR] = None
    volume: Optional[NX_FLOAT] = None  # units: NX_VOLUME
    field_of_view: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    programs: dict[str, NXprogram] = dc_field(default_factory=dict)
    notes: dict[str, NXnote] = dc_field(default_factory=dict)
    config: Optional[NXparameters] = (
        None  # Parameters that configure a reconstruction algorithm which takes
    )
    naive_discretization: Optional[NXprocess] = None
    obb: Optional[NXcollection] = (
        None  # Tight, axis-aligned bounding box about the point cloud of the reconstruction.
    )
