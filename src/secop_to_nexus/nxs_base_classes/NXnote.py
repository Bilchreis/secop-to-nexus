"""Auto-generated from NXnote.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BINARY,
    NX_CHAR,
    NX_DATE_TIME,
    NX_POSINT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXnote(NXobject):
    """Any additional freeform information not covered by the other base classes.

    This class can be used to store additional information in a
    NeXus file e.g. pictures, movies, audio, additional text logs
    """

    author: Optional[NX_CHAR] = None
    date: Optional[NX_DATE_TIME] = None
    type: Optional[NX_CHAR] = None
    file_name: Optional[NX_CHAR] = None
    identifierNAME: dict[str, NX_CHAR] = dc_field(
        default_factory=dict
    )  # nameType: partial
    checksum: Optional[NX_CHAR] = None
    algorithm: Optional[NX_CHAR] = None
    description: Optional[NX_CHAR] = None
    sequence_index: Optional[NX_POSINT] = None
    data: Optional[NX_BINARY] = None
