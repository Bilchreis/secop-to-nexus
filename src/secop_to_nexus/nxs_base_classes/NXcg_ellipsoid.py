"""Auto-generated from NXcg_ellipsoid.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcg_primitive import NXcg_primitive


@dataclass
class NXcg_ellipsoid(NXcg_primitive):
    """Computational geometry description of a set of ellipsoids."""

    semi_axes_value: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    semi_axes_values: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    radius: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    radii: Optional[NX_NUMBER] = None  # units: NX_LENGTH
