"""Auto-generated from NXcs_processor.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcircuit import NXcircuit


@dataclass
class NXcs_processor(NXcomponent):
    """Base class for reporting the description of processing units of a computer.

    Examples are e.g. classical so-called central processing units (CPUs),
    coprocessors, graphic cards, accelerator processing units or a system of these.
    """

    circuits: dict[str, NXcircuit] = dc_field(
        default_factory=dict
    )  # Typical examples for the granularization of processing units are:
