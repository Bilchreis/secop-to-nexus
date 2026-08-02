"""Auto-generated from NXcg_face_list_data_structure.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_INT,
    NX_NUMBER,
    NX_UINT,
)
from secop_to_nexus.nxs_base_classes.NXcg_primitive import NXcg_primitive


@dataclass
class NXcg_face_list_data_structure(NXcg_primitive):
    """Computational geometry of primitives via a face-and-edge-list data structure.

    Primitives must neither be degenerated nor self-intersect but can have different
    properties. A face-and-edge-list-based description of primitives is
    frequently used for triangles and polyhedra to store them on disk for
    visualization purposes (see OFF, PLY, VTK, or STL file formats).

    Although this description is storage efficient, it is not well-suited for
    topological analyses. In this case using a half-edge data structure is
    an alternative.

    Having an own base class for the data structure how primitives are stored is
    useful to embrace both users with small or detailed specification demands.

    Indices can be used as identifier and thus names for individual instances.
    """

    number_of_vertices: Optional[NX_UINT] = None  # units: NX_UNITLESS
    number_of_edges: Optional[NX_UINT] = None  # units: NX_UNITLESS
    number_of_faces: Optional[NX_UINT] = None  # units: NX_UNITLESS
    index_offset_vertex: Optional[NX_INT] = None  # units: NX_UNITLESS
    index_offset_edge: Optional[NX_INT] = None  # units: NX_UNITLESS
    index_offset_face: Optional[NX_INT] = None  # units: NX_UNITLESS
    indices_vertex: Optional[NX_INT] = None  # units: NX_UNITLESS
    indices_edge: Optional[NX_INT] = None  # units: NX_UNITLESS
    indices_face: Optional[NX_INT] = None  # units: NX_UNITLESS
    vertices: Optional[NX_NUMBER] = None  # units: NX_ANY
    edges: Optional[NX_INT] = None  # units: NX_UNITLESS
    faces: Optional[NX_INT] = None  # units: NX_UNITLESS
    vertices_are_unique: Optional[NX_BOOLEAN] = None
    edges_are_unique: Optional[NX_BOOLEAN] = None
    faces_are_unique: Optional[NX_BOOLEAN] = None
    winding_order: Optional[NX_INT] = None  # units: NX_UNITLESS
