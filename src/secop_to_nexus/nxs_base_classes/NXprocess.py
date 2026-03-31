from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional

from secop_to_nexus.nxs_base_classes.NXdtypes import NX_CHAR, NX_DATE_TIME, NX_INT
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXnote import NXnote
    from secop_to_nexus.nxs_base_classes.NXparameters import NXparameters


@dataclass
class NXprocess(NXobject):
    program: Optional[NX_CHAR] = None
    sequence_index: Optional[NX_INT] = None  # positive integer, processing order
    version: Optional[NX_CHAR] = None
    date: Optional[NX_DATE_TIME] = None

    # Arbitrarily named groups
    notes: dict[str, NXnote] = field(default_factory=dict)
    parameters: dict[str, NXparameters] = field(default_factory=dict)
    data: dict[str, NXdata] = field(default_factory=dict)
