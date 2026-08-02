"""Auto-generated from NXactivity.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_DATE_TIME,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXnote import NXnote


@dataclass
class NXactivity(NXobject):
    """A planned or unplanned action that has a temporal extension and for some time depends on some entity.

    This class is a super class for all other activities.
    """

    start_time: Optional[NX_DATE_TIME] = None
    end_time: Optional[NX_DATE_TIME] = None
    description: Optional[NX_CHAR] = None
    notes: dict[str, NXnote] = dc_field(
        default_factory=dict
    )  # This can be any data or other descriptor acquired during the activity
