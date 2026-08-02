"""Auto-generated from NXshape.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXshape(NXobject):
    """legacy class - (used by :ref:`NXgeometry`) - the shape and size of a component.

    This is the description of the general shape and size of a
    component, which may be made up of ``numobj`` separate
    elements - it is used by the :ref:`NXgeometry` class
    """

    shape: Optional[NX_CHAR] = (
        None  # enum: nxflat | nxcylinder | nxbox | nxsphere | nxcone | n...
    )
    size: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    direction: Optional[NX_CHAR] = None  # enum: concave | convex
