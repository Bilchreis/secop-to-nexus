"""Auto-generated from NXcg_polygon.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_INT,
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
class NXcg_polygon(NXcg_primitive):
    """Computational geometry description of a set of polygons in Euclidean space.

    Polygons are specialized polylines:

    * A polygon is a geometric primitive that is bounded by a closed polyline
    * All vertices of this polyline lay in the d-1 dimensional plane.
      whereas vertices of a polyline do not necessarily lay on a plane.
    * A polygon has at least three vertices.

    Each polygon is built from a sequence of vertices (points with identifiers).
    The members of a set of polygons may have a different number of vertices.
    Sometimes a collection/set of polygons is referred to as a soup of polygons.

    As three-dimensional objects, a set of polygons can be used to define the
    hull of what is effectively a polyhedron; however users are advised to use
    the specific :ref:`NXcg_polyhedron` base class if they wish to describe closed
    polyhedra. Even more general complexes can be thought of. An example are the
    so-called piecewise-linear complexes used in the TetGen library.

    As these complexes can have holes though, polyhedra without holes are one
    subclass of such complexes, users should rather design their own base class
    e.g. NXcg_polytope to describe such even more complex primitives instead
    of abusing this base class for such purposes.
    """

    number_of_total_vertices: Optional[NX_UINT] = None  # units: NX_UNITLESS
    edge_length: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    interior_angle: Optional[NX_NUMBER] = None  # units: NX_ANGLE
    shape: Optional[NX_INT] = None  # units: NX_UNITLESS
    polygons: Optional[NXcg_face_list_data_structure] = (
        None  # Combined storage of all primitives of all polygons.
    )
    polygonID: dict[str, NXcg_face_list_data_structure] = dc_field(
        default_factory=dict
    )  # nameType: partial
    polygon_half_edgeID: dict[str, NXcg_half_edge_data_structure] = dc_field(
        default_factory=dict
    )  # nameType: partial
