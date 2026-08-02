"""Auto-generated from NXpolarizer.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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


@dataclass
class NXpolarizer(NXcomponent):
    """A spin polarizer."""

    type: Optional[NX_CHAR] = None
    composition: Optional[NX_CHAR] = None
    reflection: Optional[NX_INT] = None  # units: NX_UNITLESS
    efficiency: Optional[NX_FLOAT] = None  # units: NX_DIMENSIONLESS
    depends_on: Optional[NX_CHAR] = None
