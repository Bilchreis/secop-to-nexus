"""Auto-generated from NXcg_tetrahedron.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
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


@dataclass
class NXcg_tetrahedron(NXcg_primitive):
    """Computational geometry description of a set of tetrahedra.

    Among hexahedral elements, tetrahedral elements are one of the most
    frequently used geometric primitive for meshing and describing volumetric
    objects in continuum-field simulations.
    """

    face_area: Optional[NX_NUMBER] = None  # units: NX_AREA
    edge_length: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    tetrahedra: Optional[NXcg_face_list_data_structure] = (
        None  # Combined storage of all primitives of all tetrahedra.
    )
    tetrahedronID: dict[str, NXcg_face_list_data_structure] = dc_field(
        default_factory=dict
    )  # nameType: partial
    tetrahedron_half_edgeID: dict[str, NXcg_half_edge_data_structure] = dc_field(
        default_factory=dict
    )  # nameType: partial
