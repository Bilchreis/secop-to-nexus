"""Auto-generated from NXtranslation.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_FLOAT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry


@dataclass
class NXtranslation(NXobject):
    """legacy class - (used by :ref:`NXgeometry`) - general spatial location of a component."""

    distances: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    geometry: Optional[NXgeometry] = (
        None  # Link to other object if we are relative, else absent
    )
