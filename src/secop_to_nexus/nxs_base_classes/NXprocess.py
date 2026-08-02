"""Auto-generated from NXprocess.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_DATE_TIME,
    NX_POSINT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXnote import NXnote
    from secop_to_nexus.nxs_base_classes.NXparameters import NXparameters


@dataclass
class NXprocess(NXobject):
    """The :ref:`NXprocess` class describes an operation used to
    process data as part of an analysis workflow, providing
    information such as the software used, the date of the
    operation, the input parameters, and the resulting data.
    """

    program: Optional[NX_CHAR] = None
    sequence_index: Optional[NX_POSINT] = None
    version: Optional[NX_CHAR] = None
    date: Optional[NX_DATE_TIME] = None
    notes: dict[str, NXnote] = dc_field(
        default_factory=dict
    )  # The note will contain information about how the data was
    parameters: dict[str, NXparameters] = dc_field(
        default_factory=dict
    )  # Parameters used in performing the data analysis.
    data: dict[str, NXdata] = dc_field(
        default_factory=dict
    )  # The data resulting from the operation.
