"""Auto-generated from NXcs_memory.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcircuit import NXcircuit


@dataclass
class NXcs_memory(NXcomponent):
    """Base class for reporting the description of the memory system of a computer."""

    circuits: dict[str, NXcircuit] = dc_field(
        default_factory=dict
    )  # Typically, computers have multiple instances of memory.
