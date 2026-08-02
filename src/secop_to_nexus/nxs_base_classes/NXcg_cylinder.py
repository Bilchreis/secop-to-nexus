"""Auto-generated from NXcg_cylinder.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcg_primitive import NXcg_primitive


@dataclass
class NXcg_cylinder(NXcg_primitive):
    """Computational geometry description of a set of cylinders or (truncated) cones.

    The radius can either be defined in the radii field or by filling the upper_cap_radii
    and lower_cap_radii fields respectively. The latter field case can
    thus be used to represent (truncated) cones.

    It is possible to define only one of the cap_radii fields
    to represent half-open cylinder.
    """

    height: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    radius: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    radii: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    upper_cap_radii: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    lower_cap_radii: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    lateral_surface_area: Optional[NX_NUMBER] = None  # units: NX_AREA
    upper_cap_surface_area: Optional[NX_NUMBER] = None  # units: NX_AREA
    lower_cap_surface_area: Optional[NX_NUMBER] = None  # units: NX_AREA
    total_surface_area: Optional[NX_NUMBER] = None  # units: NX_AREA
