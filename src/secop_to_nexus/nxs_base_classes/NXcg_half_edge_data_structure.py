"""Auto-generated from NXcg_half_edge_data_structure.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_INT,
    NX_NUMBER,
    NX_POSINT,
    NX_UINT,
)
from secop_to_nexus.nxs_base_classes.NXcg_primitive import NXcg_primitive


@dataclass
class NXcg_half_edge_data_structure(NXcg_primitive):
    """Computational geometry description of a half-edge data structure.

    Such a data structure can be used to efficiently circulate around faces
    and iterate over vertices of a planar graph. The data structure is also
    known as a doubly connected edge list.

    Indices can be used as identifier and thus names for individual instances.
    """

    dimensionality: Optional[NX_POSINT] = None  # units: NX_UNITLESS
    number_of_vertices: Optional[NX_UINT] = None  # units: NX_UNITLESS
    number_of_edges: Optional[NX_UINT] = None  # units: NX_UNITLESS
    index_offset_vertex: Optional[NX_INT] = None  # units: NX_UNITLESS
    index_offset_edge: Optional[NX_INT] = None  # units: NX_UNITLESS
    index_offset_face: Optional[NX_INT] = None
    position: Optional[NX_NUMBER] = None  # units: NX_ANY
    vertex_incident_half_edge: Optional[NX_INT] = None  # units: NX_UNITLESS
    face_half_edge: Optional[NX_INT] = None  # units: NX_UNITLESS
    half_edge_vertex_origin: Optional[NX_INT] = None  # units: NX_UNITLESS
    half_edge_twin: Optional[NX_INT] = None  # units: NX_UNITLESS
    half_edge_incident_face: Optional[NX_INT] = None  # units: NX_UNITLESS
    half_edge_next: Optional[NX_INT] = None  # units: NX_UNITLESS
    half_edge_prev: Optional[NX_INT] = None  # units: NX_UNITLESS
    weinberg_vector: Optional[NX_CHAR] = None
