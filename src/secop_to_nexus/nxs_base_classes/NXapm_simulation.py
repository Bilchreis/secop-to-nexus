"""Auto-generated from NXapm_simulation.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXparameters import NXparameters
    from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess
    from secop_to_nexus.nxs_base_classes.NXprogram import NXprogram


@dataclass
class NXapm_simulation(NXobject):
    """Base class for simulation of ion extraction from matter via laser and/or voltage
    pulsing.
    """

    programs: dict[str, NXprogram] = dc_field(default_factory=dict)
    parameters: dict[str, NXparameters] = dc_field(default_factory=dict)
    processes: dict[str, NXprocess] = dc_field(default_factory=dict)
    data: dict[str, NXdata] = dc_field(default_factory=dict)
