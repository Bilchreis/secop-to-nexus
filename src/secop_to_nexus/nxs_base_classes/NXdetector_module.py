"""Auto-generated from NXdetector_module.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_INT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXdetector_module(NXobject):
    """Geometry and logical description of a detector module. When used, child group to NXdetector.

    Many detectors consist of multiple
    smaller modules. Sometimes it is important to know the exact position of such
    modules.
    This is the purpose of this group. It is a child group to NXdetector.

    Note, the pixel size is given as values in the array fast_pixel_direction and slow_pixel_direction.
    """

    data_origin: Optional[NX_INT] = None
    data_size: Optional[NX_INT] = None
    module_offset: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    fast_pixel_direction: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    slow_pixel_direction: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    depends_on: Optional[NX_CHAR] = None
