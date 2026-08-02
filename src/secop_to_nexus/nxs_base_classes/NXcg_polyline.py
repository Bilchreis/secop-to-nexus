"""Auto-generated from NXcg_polyline.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_INT,
    NX_NUMBER,
    NX_UINT,
)
from secop_to_nexus.nxs_base_classes.NXcg_primitive import NXcg_primitive


@dataclass
class NXcg_polyline(NXcg_primitive):
    """Computational geometry description of a set of polylines.

    Each polyline is built from a sequence of vertices (points with identifiers).
    Each polyline must have a start and an end point.
    The sequence describes the traversal along the polyline when
    walking from the first to the last vertex.
    """

    depends_on: Optional[NX_CHAR] = None
    number_of_unique_vertices: Optional[NX_UINT] = None  # units: NX_UNITLESS
    number_of_total_vertices: Optional[NX_UINT] = None  # units: NX_UNITLESS
    number_of_vertices: Optional[NX_UINT] = None  # units: NX_UNITLESS
    vertices: Optional[NX_NUMBER] = None  # units: NX_ANY
    vertices_are_unique: Optional[NX_BOOLEAN] = None
    polylines: Optional[NX_INT] = None  # units: NX_UNITLESS
