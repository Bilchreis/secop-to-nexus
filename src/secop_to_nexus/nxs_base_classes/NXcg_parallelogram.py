"""Auto-generated from NXcg_parallelogram.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
)
from secop_to_nexus.nxs_base_classes.NXcg_primitive import NXcg_primitive

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcg_face_list_data_structure import (
        NXcg_face_list_data_structure,
    )


@dataclass
class NXcg_parallelogram(NXcg_primitive):
    """Computational geometry description of a set of parallelograms.

    This class can also be used to describe rectangles or squares, irrespective
    whether these are axis-aligned or not. The class represents different
    access and description levels to embrace applied scientists and computational
    geometry experts with their different views:

    * The simplest case is the communication of dimensions aka the size of a
      region of interest in the 2D plane. In this case, communicating the
      alignment with axes is maybe not as relevant as it is to report the area
      of the ROI.
    * In other cases the extent of the parallelogram is relevant though.
    * Finally, in CAD models it should be possible to specify the polygons
      which the parallelograms represent with exact numerical details.

    Parallelograms are important geometrical primitives as their usage for
    describing many scanning experiments shows where typically parallelogram-shaped
    ROIs are scanned across the surface of a sample.

    The term parallelogram will be used throughout this base class thus including
    the important special cases rectangle, square, 2D box, axis-aligned bounding box
    (AABB), or optimal bounding box (OBB) as analogous 2D variants to their 3D
    counterparts. See :ref:`NXcg_hexahedron` for the generalization in 3D.

    An axis-aligned bounding box is a common data object in computational science
    and simulation codes to represent a rectangle whose edges are aligned with the
    axes of a coordinate system. As a part of binary trees AABBs are important data
    objects for executing time- as well as space-efficient queries
    of geometric primitives in techniques like kd-trees.

    An optimal bounding box is a common data object which provides the best, i.e.
    most tightly fitting box about an arbitrary object. In general such boxes are
    rotated. Other than in 3D dimensions, the rotation caliper method offers
    a rigorous approach to compute an optimal bounding box to a point set in 2D.
    """

    is_rectangle: Optional[NX_BOOLEAN] = None
    is_axis_aligned: Optional[NX_BOOLEAN] = None
    parallelograms: Optional[NXcg_face_list_data_structure] = (
        None  # Combined storage of all parallelograms.
    )
    parallelogramID: dict[str, NXcg_face_list_data_structure] = dc_field(
        default_factory=dict
    )  # nameType: partial
