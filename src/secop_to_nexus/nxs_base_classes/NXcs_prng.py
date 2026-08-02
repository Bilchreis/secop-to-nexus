"""Auto-generated from NXcs_prng.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_INT,
    NX_UINT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXprogram import NXprogram


@dataclass
class NXcs_prng(NXobject):
    """Computer science description of pseudo-random number generator.

    The purpose of this base class is to identify if exactly the same sequence can be
    reproduced, like for a PRNG or not, like for a true physically random source.
    """

    type: Optional[NX_CHAR] = None  # enum: physical | system_clock | mt19937 | other
    seed: Optional[NX_INT] = None  # units: NX_UNITLESS
    warmup: Optional[NX_UINT] = None  # units: NX_UNITLESS
    programs: dict[str, NXprogram] = dc_field(
        default_factory=dict
    )  # Name of the PRNG implementation and version. If such information is not
