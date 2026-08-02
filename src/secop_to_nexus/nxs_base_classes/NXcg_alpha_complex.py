"""Auto-generated from NXcg_alpha_complex.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcg_primitive import NXcg_primitive

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcg_point import NXcg_point
    from secop_to_nexus.nxs_base_classes.NXcg_tetrahedron import NXcg_tetrahedron
    from secop_to_nexus.nxs_base_classes.NXcg_triangle import NXcg_triangle


@dataclass
class NXcg_alpha_complex(NXcg_primitive):
    """Computational geometry of alpha complexes (alpha shapes or alpha wrappings) about primitives.

    For details see:

    * https://dx.doi.org/10.1109/TIT.1983.1056714 for 2D,
    * https://dx.doi.org/10.1145/174462.156635 for 3D,
    * https://dl.acm.org/doi/10.5555/871114 for weighted, and
    * https://doc.cgal.org/latest/Alpha_shapes_3 for 3D implementation of alpha shapes, and
    * https://doc.cgal.org/latest/Manual/packages.html#PkgAlphaWrap3 for 3D alpha wrappings

    in CGAL, the Computational Geometry Algorithms Library respectively.
    As a starting point, we follow the conventions of the CGAL library.

    In general, an alpha complex is a not necessarily connected or not necessarily pure complex,
    i.e. singular faces may exist. The number of cells, faces, and edges depends on how a specific
    alpha complex is filtered for lower-dimensional simplices. The fields is_regularized and
    regularization can be used to provide details about regularization procedures.
    """

    type: Optional[NX_CHAR] = None  # enum: convex_hull | alpha_shape | alpha_wrapping
    regularization: Optional[NX_CHAR] = None
    is_regularized: Optional[NX_BOOLEAN] = None
    alpha: Optional[NX_NUMBER] = None  # units: NX_ANY
    offset: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    cg_points: dict[str, NXcg_point] = dc_field(
        default_factory=dict
    )  # Point cloud serving as input for the computation of the alpha complex.
    TRIANGLE_SOUP: dict[str, NXcg_triangle] = dc_field(
        default_factory=dict
    )  # nameType: any
    ALPHA_COMPLEX: dict[str, NXcg_triangle] = dc_field(
        default_factory=dict
    )  # nameType: any
    TETRAHEDRALIZATION: dict[str, NXcg_tetrahedron] = dc_field(
        default_factory=dict
    )  # nameType: any
