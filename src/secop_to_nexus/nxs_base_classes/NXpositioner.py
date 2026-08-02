"""Auto-generated from NXpositioner.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
class NXpositioner(NXcomponent):
    """A generic positioner such as a motor or piezo-electric transducer."""

    name: Optional[NX_CHAR] = None
    description: Optional[NX_CHAR] = None
    value: Optional[NX_NUMBER] = None  # units: NX_ANY
    raw_value: Optional[NX_NUMBER] = None  # units: NX_ANY
    target_value: Optional[NX_NUMBER] = None  # units: NX_ANY
    tolerance: Optional[NX_NUMBER] = None  # units: NX_ANY
    soft_limit_min: Optional[NX_NUMBER] = None  # units: NX_ANY
    soft_limit_max: Optional[NX_NUMBER] = None  # units: NX_ANY
    velocity: Optional[NX_NUMBER] = None  # units: NX_ANY
    acceleration_time: Optional[NX_NUMBER] = None  # units: NX_ANY
    controller_record: Optional[NX_CHAR] = None
    depends_on: Optional[NX_CHAR] = None
