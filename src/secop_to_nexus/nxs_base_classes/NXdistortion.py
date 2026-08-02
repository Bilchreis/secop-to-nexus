"""Auto-generated from NXdistortion.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_FLOAT,
    NX_INT,
)
from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess


@dataclass
class NXdistortion(NXprocess):
    """Subclass of NXprocess to describe post-processing distortion correction."""

    applied: Optional[NX_BOOLEAN] = None
    symmetry: Optional[NX_INT] = None  # units: NX_UNITLESS
    original_centre: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    original_points: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    cdeform_field: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    rdeform_field: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    description: Optional[NX_CHAR] = None
