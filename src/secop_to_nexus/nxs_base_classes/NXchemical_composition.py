"""Auto-generated from NXchemical_composition.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXatom import NXatom


@dataclass
class NXchemical_composition(NXobject):
    """Chemical composition of a sample or a set of things."""

    normalization: Optional[NX_CHAR] = None  # enum: atom_percent | weight_percent
    total: Optional[NX_NUMBER] = None  # units: NX_UNITLESS
    ELEMENT: dict[str, NXatom] = dc_field(default_factory=dict)  # nameType: any
