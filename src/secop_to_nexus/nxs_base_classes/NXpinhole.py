"""Auto-generated from NXpinhole.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent


@dataclass
class NXpinhole(NXcomponent):
    """A simple pinhole.

    For more complex geometries, :ref:`NXaperture` should be used.
    """

    depends_on: Optional[NX_CHAR] = None
    diameter: Optional[NX_NUMBER] = None  # units: NX_LENGTH
