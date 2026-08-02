"""Auto-generated from NXelectron_detector.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
)
from secop_to_nexus.nxs_base_classes.NXdetector import NXdetector


@dataclass
class NXelectron_detector(NXdetector):
    """A subclass of NXdetector for detectors that detect electrons."""

    amplifier_type: Optional[NX_CHAR] = None
    detector_type: Optional[NX_CHAR] = None
    detector_voltage: Optional[NX_FLOAT] = None  # units: NX_VOLTAGE
    amplifier_voltage: Optional[NX_FLOAT] = None  # units: NX_VOLTAGE
    amplifier_bias: Optional[NX_FLOAT] = None  # units: NX_VOLTAGE
