"""Auto-generated from NXcg_primitive.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_INT,
    NX_NUMBER,
    NX_POSINT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcg_unit_normal import NXcg_unit_normal


@dataclass
class NXcg_primitive(NXobject):
    """Computational geometry description of a set of primitives in Euclidean space.

    Primitives must neither be degenerated nor self-intersect.
    Individual primitives can differ in their properties (e.g. size, shape, rotation).
    """

    depends_on: Optional[NX_CHAR] = None
    dimensionality: Optional[NX_POSINT] = None  # units: NX_UNITLESS; enum: 1 | 2 | 3
    cardinality: Optional[NX_POSINT] = None  # units: NX_UNITLESS
    index_offset: Optional[NX_INT] = None  # units: NX_UNITLESS
    indices: Optional[NX_INT] = None
    center: Optional[NX_NUMBER] = None  # units: NX_ANY
    is_center_of_mass: Optional[NX_BOOLEAN] = None
    shape: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    length: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    width: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    height: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    is_closed: Optional[NX_BOOLEAN] = None
    volume: Optional[NX_NUMBER] = None  # units: NX_ANY
    area: Optional[NX_NUMBER] = None  # units: NX_AREA
    orientation: Optional[NX_NUMBER] = None  # units: NX_DIMENSIONLESS
    is_mesh: Optional[NX_BOOLEAN] = None
    is_triangle_mesh: Optional[NX_BOOLEAN] = None
    is_surface_mesh: Optional[NX_BOOLEAN] = None
    is_geodesic_mesh: Optional[NX_BOOLEAN] = None
    description: Optional[NX_CHAR] = None
    vertex_normal: Optional[NXcg_unit_normal] = None
    edge_normal: Optional[NXcg_unit_normal] = None
    face_normal: Optional[NXcg_unit_normal] = None
