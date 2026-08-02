"""Auto-generated from NXfabrication.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_DATE_TIME,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXfabrication(NXobject):
    """Details about a component as it is defined by its manufacturer."""

    vendor: Optional[NX_CHAR] = None
    model: Optional[NX_CHAR] = None
    serial_number: Optional[NX_CHAR] = None
    construction_date: Optional[NX_DATE_TIME] = None
    capability: Optional[NX_CHAR] = None
