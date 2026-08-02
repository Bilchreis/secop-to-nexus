"""Auto-generated from NXorientation.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
class NXorientation(NXobject):
    """legacy class - recommend to use :ref:`NXtransformations` now

    Description for a general orientation of a component - used by :ref:`NXgeometry`
    """

    value: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    geometries: dict[str, NXgeometry] = dc_field(
        default_factory=dict
    )  # Link to another object if we are using relative positioning, else absent
