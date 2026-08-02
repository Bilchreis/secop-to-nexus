"""Auto-generated from NXhistory.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXactivity import NXactivity
    from secop_to_nexus.nxs_base_classes.NXnote import NXnote


@dataclass
class NXhistory(NXobject):
    """A set of activities that occurred to a physical entity prior/during experiment.

    Ideally, a full report of the previous operations (or links to a chain of operations).
    Alternatively, notes allow for additional descriptors in any format.
    """

    identifierNAME: dict[str, NX_CHAR] = dc_field(
        default_factory=dict
    )  # nameType: partial
    activities: dict[str, NXactivity] = dc_field(
        default_factory=dict
    )  # Any activity that was performed on the physical entity prior or during the experiment.
    notes: dict[str, NXnote] = dc_field(
        default_factory=dict
    )  # A descriptor to keep track of the treatment of the physical entity before or during the
