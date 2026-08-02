"""Auto-generated from NXcircuit.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcalibration import NXcalibration
    from secop_to_nexus.nxs_base_classes.NXfabrication import NXfabrication


@dataclass
class NXcircuit(NXcomponent):
    """Base class for documenting circuit devices.

    Electronic circuits are hardware components that connect several electronic components to achieve
    specific functionality, e.g. amplifying a voltage or convert a voltage to binary numbers, etc.
    """

    components: Optional[NX_CHAR] = None
    connections: Optional[NX_CHAR] = None
    power_source: Optional[NX_CHAR] = None
    signal_type: Optional[NX_CHAR] = None
    operating_frequency: Optional[NX_NUMBER] = None  # units: NX_FREQUENCY
    bandwidth: Optional[NX_NUMBER] = None  # units: NX_FREQUENCY
    input_impedance: Optional[NX_NUMBER] = None  # units: NX_ANY
    output_impedance: Optional[NX_NUMBER] = None  # units: NX_ANY
    gain: Optional[NX_NUMBER] = None  # units: NX_UNITLESS
    noise_level: Optional[NX_NUMBER] = None  # units: NX_ANY
    temperature_range: Optional[NX_NUMBER] = None  # units: NX_ANY
    offset: Optional[NX_NUMBER] = None  # units: NX_ANY
    output_channels: Optional[NX_NUMBER] = None
    output_signal: Optional[NX_NUMBER] = None  # units: NX_ANY
    power_consumption: Optional[NX_NUMBER] = None  # units: NX_ANY
    status_indicators: Optional[NX_CHAR] = None
    protection_features: Optional[NX_CHAR] = None
    acquisition_time: Optional[NX_NUMBER] = None  # units: NX_TIME
    output_slew_rate: Optional[NX_CHAR] = None
    hardware: Optional[NXfabrication] = (
        None  # Hardware where the circuit is implanted; includes information about the
    )
    calibration: Optional[NXcalibration] = None  # Calibration data for the circuit.
