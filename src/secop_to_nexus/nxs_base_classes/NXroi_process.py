"""Auto-generated from NXroi_process.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess


@dataclass
class NXroi_process(NXprocess):
    """Base class to report on the characterization of an area or volume of material.

    This area or volume of material is considered a region-of-interest (ROI).

    This base class should be used when the characterization was achieved by
    processing data from experiment or computer simulations into models of
    the microstructure of the material and the properties of the material or its
    crystal defects within this ROI. Microstructural features is a narrow synonym
    for these crystal defects.

    This base class can also be used to store data and metadata of the
    representation of the ROI, i.e. its discretization and shape.

    Methods from computational geometry are typically used for
    defining a discretization of the area and volume.

    Do not confuse this base class with :ref:`NXregion`. The purpose
    of the :ref:`NXregion` base class is to document data access i.e.
    I/O pattern on arrays. Therefore, concepts from :ref:`NXregion` operate
    in data space rather than in real or simulated real space.
    """

    processes: dict[str, NXprocess] = dc_field(default_factory=dict)
