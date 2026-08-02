"""Auto-generated from NXem_eels.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess


@dataclass
class NXem_eels(NXprocess):
    """Base class method-specific for Electron Energy Loss Spectroscopy (EELS)."""

    zlp_correction: Optional[NXprocess] = (
        None  # Details about computational steps how the zero-loss peak was threaded.
    )
    indexing: Optional[NXprocess] = (
        None  # Details about computational steps how peaks were indexed as elements.
    )
