"""Auto-generated from NXflipper.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
class NXflipper(NXcomponent):
    """A spin flipper."""

    type: Optional[NX_CHAR] = None  # enum: coil | current-sheet
    flip_turns: Optional[NX_FLOAT] = None  # units: NX_PER_LENGTH
    comp_turns: Optional[NX_FLOAT] = None  # units: NX_PER_LENGTH
    guide_turns: Optional[NX_FLOAT] = None  # units: NX_PER_LENGTH
    flip_current: Optional[NX_FLOAT] = None  # units: NX_CURRENT
    comp_current: Optional[NX_FLOAT] = None  # units: NX_CURRENT
    guide_current: Optional[NX_FLOAT] = None  # units: NX_CURRENT
    thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    depends_on: Optional[NX_CHAR] = None
