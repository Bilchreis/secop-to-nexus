"""Auto-generated from NXcomponent.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXfabrication import NXfabrication
    from secop_to_nexus.nxs_base_classes.NXprogram import NXprogram
    from secop_to_nexus.nxs_base_classes.NXtransformations import NXtransformations


@dataclass
class NXcomponent(NXobject):
    """Base class for components of an instrument - real ones or simulated ones."""

    applied: Optional[NX_BOOLEAN] = None
    name: Optional[NX_CHAR] = None
    description: Optional[NX_CHAR] = None
    inputs: Optional[NX_CHAR] = None
    outputs: Optional[NX_CHAR] = None
    depends_on: Optional[NX_CHAR] = None
    fabrications: dict[str, NXfabrication] = dc_field(default_factory=dict)
    programs: dict[str, NXprogram] = dc_field(default_factory=dict)
    transformations: dict[str, NXtransformations] = dc_field(
        default_factory=dict
    )  # Collection of axis-based translations and rotations to describe the
