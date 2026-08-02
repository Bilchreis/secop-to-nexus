"""Auto-generated from NXem_eds.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess


@dataclass
class NXem_eds(NXprocess):
    """Base class method-specific for energy-dispersive X-ray spectroscopy (EDS/EDXS).

    `IUPAC instead of Siegbahn notation <https://doi.org/10.1002/xrs.1300200308>`_ should be used.

    X-ray spectroscopy is a surface-sensitive technique. Therefore, three-dimensional elemental
    characterization requires typically a sequence of characterization and preparation of the
    surface to expose new surface layer that can be characterized in the next acquisition.
    In effect, the resulting three-dimensional elemental information mappings are truly the
    result of a correlation and post-processing of several measurements which is the field
    of correlative tomographic usage of electron microscopy.
    """

    indexing: Optional[NXprocess] = (
        None  # Details about computational steps how peaks were indexed as elements.
    )
