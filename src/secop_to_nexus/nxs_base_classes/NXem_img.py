"""Auto-generated from NXem_img.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXimage import NXimage


@dataclass
class NXem_img(NXprocess):
    """Base class for method-specific generic imaging with electron microscopes.

    In the majority of cases simple d-dimensional regular scan patterns are used
    to probe regions-of-interest (ROIs). Examples can be single point aka spot
    measurements, line profiles, or (rectangular) surface mappings.
    The latter pattern is the most frequently used.

    For now the base class provides for scans for which the settings,
    binning, and energy resolution is the same for each scan point.
    """

    images: dict[str, NXimage] = dc_field(default_factory=dict)
