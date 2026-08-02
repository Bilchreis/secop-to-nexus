"""Auto-generated from NXpump.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
class NXpump(NXcomponent):
    """Device to reduce an atmosphere to a controlled pressure."""

    design: Optional[NX_CHAR] = (
        None  # enum: membrane | rotary_vane | roots | turbo_molecular | ...
    )
    base_pressure: Optional[NX_FLOAT] = None  # units: NX_PRESSURE
    medium: Optional[NX_CHAR] = None  # enum: vacuum | liquid | gas | slurry | powder
