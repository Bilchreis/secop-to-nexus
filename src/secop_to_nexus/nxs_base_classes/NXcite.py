"""Auto-generated from NXcite.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXcite(NXobject):
    """A literature reference

    Definition to include references for example for detectors,
    manuals, instruments, acquisition or analysis software used.

    The idea would be to include this in the relevant NeXus object:
    :ref:`NXdetector` for detectors, :ref:`NXinstrument` for instruments, etc.
    """

    description: Optional[NX_CHAR] = None
    url: Optional[NX_CHAR] = None
    doi: Optional[NX_CHAR] = None
    endnote: Optional[NX_CHAR] = None
    bibtex: Optional[NX_CHAR] = None
