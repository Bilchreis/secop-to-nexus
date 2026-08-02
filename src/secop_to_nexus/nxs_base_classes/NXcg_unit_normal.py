"""Auto-generated from NXcg_unit_normal.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_INT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXcg_unit_normal(NXobject):
    """Computational geometry description of a set of (oriented) unit normal vectors.

    Store normal vector information as properties of primitives.
    Use only only as a child of an instance of :ref:`NXcg_primitive`
    so that this instance acts as the parent to define a context.
    """

    normals: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    orientation: Optional[NX_INT] = None  # units: NX_UNITLESS
