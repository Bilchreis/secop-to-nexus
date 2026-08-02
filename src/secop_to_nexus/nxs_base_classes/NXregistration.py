"""Auto-generated from NXregistration.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
)
from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXtransformations import NXtransformations


@dataclass
class NXregistration(NXprocess):
    """Describes image registration procedures."""

    applied: Optional[NX_BOOLEAN] = None
    depends_on: Optional[NX_CHAR] = None
    description: Optional[NX_CHAR] = None
    transformations: dict[str, NXtransformations] = dc_field(
        default_factory=dict
    )  # To describe the operations of image registration (combinations of rigid
