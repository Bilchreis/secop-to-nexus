"""Auto-generated from NXcg_grid.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_INT,
    NX_NUMBER,
    NX_UINT,
)
from secop_to_nexus.nxs_base_classes.NXcg_primitive import NXcg_primitive

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcg_polyhedron import NXcg_polyhedron


@dataclass
class NXcg_grid(NXcg_primitive):
    """Computational geometry description of a grid of Wigner-Seitz cells in Euclidean space.

    Three-dimensional grids with cubic cells are if not the most frequently used
    example of such grids. Numerical methods and models that use grids are used
    in many cases in the natural sciences and engineering disciplines. Examples are
    discretizations in space and time used for phase-field, cellular automata, or Monte Carlo
    modeling.
    """

    origin: Optional[NX_NUMBER] = None  # units: NX_ANY
    symmetry: Optional[NX_CHAR] = None  # enum: cubic
    cell_dimensions: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    extent: Optional[NX_INT] = None  # units: NX_UNITLESS
    position: Optional[NX_NUMBER] = None  # units: NX_ANY
    coordinate: Optional[NX_INT] = None  # units: NX_DIMENSIONLESS
    number_of_boundaries: Optional[NX_UINT] = None  # units: NX_UNITLESS
    boundaries: Optional[NX_CHAR] = None
    boundary_conditions: Optional[NX_INT] = None  # units: NX_UNITLESS
    surface_reconstruction: Optional[NX_CHAR] = None
    bounding_box: Optional[NXcg_polyhedron] = (
        None  # A tight bounding box about the grid.
    )
