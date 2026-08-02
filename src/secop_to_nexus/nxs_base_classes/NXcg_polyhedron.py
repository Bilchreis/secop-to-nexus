"""Auto-generated from NXcg_polyhedron.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_NUMBER,
    NX_UINT,
)
from secop_to_nexus.nxs_base_classes.NXcg_primitive import NXcg_primitive

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcg_face_list_data_structure import (
        NXcg_face_list_data_structure,
    )
    from secop_to_nexus.nxs_base_classes.NXcg_half_edge_data_structure import (
        NXcg_half_edge_data_structure,
    )


@dataclass
class NXcg_polyhedron(NXcg_primitive):
    """Computational geometry description of a set of polyhedra in Euclidean space.

    Polyhedra or so-called cells (especially in the convex of tessellations) are
    constructed from polygon meshes. Polyhedra may make contact to allow a usage
    of this base class for a description of tessellations.

    For the description of more complicated manifolds and especially for polyhedra
    with holes, users are advised to check if their particular needs are described
    by creating customized instances of an :ref:`NXcg_polygon`.
    """

    number_of_faces: Optional[NX_UINT] = None  # units: NX_UNITLESS
    face_area: Optional[NX_NUMBER] = None  # units: NX_AREA
    number_of_edges: Optional[NX_UINT] = None
    edge_length: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    polyhedra: Optional[NXcg_face_list_data_structure] = (
        None  # Combined storage of all primitives of all polyhedra.
    )
    polyhedronID: dict[str, NXcg_face_list_data_structure] = dc_field(
        default_factory=dict
    )  # nameType: partial
    polyhedron_half_edgeID: dict[str, NXcg_half_edge_data_structure] = dc_field(
        default_factory=dict
    )  # nameType: partial
