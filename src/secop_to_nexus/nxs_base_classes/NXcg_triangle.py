"""Auto-generated from NXcg_triangle.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_INT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcg_primitive import NXcg_primitive

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcg_face_list_data_structure import (
        NXcg_face_list_data_structure,
    )


@dataclass
class NXcg_triangle(NXcg_primitive):
    """Computational geometry description of a set of triangles."""

    number_of_unique_vertices: Optional[NX_INT] = None  # units: NX_UNITLESS
    edge_length: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    interior_angle: Optional[NX_NUMBER] = None  # units: NX_ANGLE
    triangles: Optional[NXcg_face_list_data_structure] = (
        None  # Combined storage of all primitives of all triangles.
    )
    triangleID: dict[str, NXcg_face_list_data_structure] = dc_field(
        default_factory=dict
    )  # nameType: partial
