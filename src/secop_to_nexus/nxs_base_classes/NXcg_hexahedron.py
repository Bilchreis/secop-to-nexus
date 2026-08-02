"""Auto-generated from NXcg_hexahedron.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcg_primitive import NXcg_primitive

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcg_face_list_data_structure import (
        NXcg_face_list_data_structure,
    )
    from secop_to_nexus.nxs_base_classes.NXcg_half_edge_data_structure import (
        NXcg_half_edge_data_structure,
    )
    from secop_to_nexus.nxs_base_classes.NXcg_unit_normal import NXcg_unit_normal


@dataclass
class NXcg_hexahedron(NXcg_primitive):
    """Computational geometry description of a set of hexahedra in Euclidean space.

    This class can also be used to describe cuboids or cubes, axis-aligned or not.
    The class represents different access and description levels to offer both
    applied scientists and computational geometry experts an approach whereby
    different specific views can be implemented using the same base class:

    * In the simplest case experimentalists may use this base class to describe
      the dimensions or size of a specimen. In this case the alignment with axes
      is not relevant as eventually only the volume of the specimen is of interest.
    * In many cases, take for example an experiment where a specimen was cut out
      from a specifically deformed piece of material, the orientation of the
      specimen's edges with the experiment coordinate system is of high relevance.
      Examples include knowledge about the specimen edge, whether it is
      parallel to the rolling, the transverse, or the normal direction.
    * While the above-mentioned use cases are sufficient to pinpoint the sample
      within a known laboratory/experiment coordinate system, these descriptions
      are not detailed enough to specify e.g. a CAD model of the specimen.
    * Therefore, groups and fields for an additional, computational-geometry-
      based view of hexahedra is offered to serve additional computational
      tasks: storage-oriented simple views or detailed topological/graph-based
      descriptions.

    Hexahedra are important geometrical primitives, which are among the most
    frequently used elements in finite element meshing/modeling.

    As a specialization of the :ref:`NXcg_primitive` base class hexahedra
    are assumed non-degenerated, closed, and built of polygons that are
    not self-intersecting.

    The term hexahedra will be used throughout this base class but includes
    the special cases cuboid, cube, box, axis-aligned bounding box (AABB),
    and optimal bounding box (OBB).

    An axis-aligned bounding box is a common data object in computational science
    and simulation codes to represent a cuboid whose edges are aligned with the
    base vectors of a coordinate system. As a part of binary trees, these data
    objects are important for making time- as well as space-efficient queries
    of geometric primitives in techniques like kd-trees.

    An optimal bounding box is a common data object which provides the best
    tightly fitting box about an arbitrary object. In general, such boxes are
    rotated. Exact and substantially faster in practice approximate algorithms
    exist to compute optimal or near optimal bounding boxes for sets of points.
    """

    shape: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    length: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    width: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    height: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    volume: Optional[NX_NUMBER] = None  # units: NX_VOLUME
    area: Optional[NX_NUMBER] = None  # units: NX_AREA
    face_area: Optional[NX_NUMBER] = None  # units: NX_AREA
    is_box: Optional[NX_BOOLEAN] = None
    is_axis_aligned: Optional[NX_BOOLEAN] = None
    vertex_normal: Optional[NXcg_unit_normal] = None
    edge_normal: Optional[NXcg_unit_normal] = None
    face_normal: Optional[NXcg_unit_normal] = None
    hexahedra: Optional[NXcg_face_list_data_structure] = (
        None  # Combined storage of all primitives of all hexahedra.
    )
    hexahedronID: dict[str, NXcg_face_list_data_structure] = dc_field(
        default_factory=dict
    )  # nameType: partial
    hexahedron_half_edgeID: dict[str, NXcg_half_edge_data_structure] = dc_field(
        default_factory=dict
    )  # nameType: partial
