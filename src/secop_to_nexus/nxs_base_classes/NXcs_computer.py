"""Auto-generated from NXcs_computer.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcs_memory import NXcs_memory
    from secop_to_nexus.nxs_base_classes.NXcs_processor import NXcs_processor
    from secop_to_nexus.nxs_base_classes.NXcs_storage import NXcs_storage


@dataclass
class NXcs_computer(NXobject):
    """Base class for reporting the description of a computer"""

    name: Optional[NX_CHAR] = None
    operating_system: Optional[NX_CHAR] = None
    uuid: Optional[NX_CHAR] = None
    processorID: dict[str, NXcs_processor] = dc_field(
        default_factory=dict
    )  # nameType: partial
    memoryID: dict[str, NXcs_memory] = dc_field(
        default_factory=dict
    )  # nameType: partial
    storageID: dict[str, NXcs_storage] = dc_field(
        default_factory=dict
    )  # nameType: partial
