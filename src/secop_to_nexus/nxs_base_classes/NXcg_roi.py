"""Auto-generated from NXcg_roi.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcg_cylinder import NXcg_cylinder
    from secop_to_nexus.nxs_base_classes.NXcg_ellipsoid import NXcg_ellipsoid
    from secop_to_nexus.nxs_base_classes.NXcg_hexahedron import NXcg_hexahedron
    from secop_to_nexus.nxs_base_classes.NXcg_parallelogram import NXcg_parallelogram
    from secop_to_nexus.nxs_base_classes.NXcg_polyhedron import NXcg_polyhedron


@dataclass
class NXcg_roi(NXobject):
    """Base class for a region-of-interest (ROI) bound by geometric primitives.

    So-called region-of-interest(s) (ROIs) are typically used to describe a
    region in space (and time) where an observation is made or for which
    a computer simulation is performed with given boundary conditions.
    """

    cg_ellipsoids: dict[str, NXcg_ellipsoid] = dc_field(default_factory=dict)
    cg_cylinders: dict[str, NXcg_cylinder] = dc_field(default_factory=dict)
    cg_parallelograms: dict[str, NXcg_parallelogram] = dc_field(default_factory=dict)
    cg_hexahedrons: dict[str, NXcg_hexahedron] = dc_field(default_factory=dict)
    cg_polyhedrons: dict[str, NXcg_polyhedron] = dc_field(default_factory=dict)
