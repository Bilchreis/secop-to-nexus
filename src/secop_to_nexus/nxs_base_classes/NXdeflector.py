"""Auto-generated from NXdeflector.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
class NXdeflector(NXcomponent):
    """Component of an electron analyzer that deflects the paths of electrons. This includes electrostatic and electromagnetic deflectors."""

    type: Optional[NX_CHAR] = None  # enum: dipole | quadrupole | hexapole | octupole
    name: Optional[NX_CHAR] = None
    voltage: Optional[NX_NUMBER] = None  # units: NX_VOLTAGE
    current: Optional[NX_NUMBER] = None  # units: NX_CURRENT
    offset_x: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    offset_y: Optional[NX_NUMBER] = None  # units: NX_LENGTH
