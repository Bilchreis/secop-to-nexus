"""Auto-generated from NXmanipulator.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXactuator import NXactuator
    from secop_to_nexus.nxs_base_classes.NXpositioner import NXpositioner
    from secop_to_nexus.nxs_base_classes.NXsensor import NXsensor


@dataclass
class NXmanipulator(NXcomponent):
    """Base class to describe the use of manipulators and sample stages."""

    name: Optional[NX_CHAR] = None
    description: Optional[NX_CHAR] = None
    type: Optional[NX_CHAR] = None
    cryostat: Optional[NXactuator] = (
        None  # Cryostat for cooling the sample (and, potentially, the whole manipulator).
    )
    temperature_sensor: Optional[NXsensor] = (
        None  # Temperature sensor measuring the sample temperature.
    )
    sample_heater: Optional[NXactuator] = None  # Device to heat the sample.
    drain_current_ammeter: Optional[NXsensor] = (
        None  # Ammeter measuring the drain current of the sample and sample holder.
    )
    sample_bias_potentiostat: Optional[NXactuator] = (
        None  # Actuator applying a voltage between sample holder and sample.
    )
    sample_bias_voltmeter: Optional[NXsensor] = (
        None  # Sensor measuring the voltage applied to sample and sample holder.
    )
    actuators: dict[str, NXactuator] = dc_field(
        default_factory=dict
    )  # Any additional actuator on the manipulator used to control an external
    sensors: dict[str, NXsensor] = dc_field(
        default_factory=dict
    )  # Any additional sensors on the manipulator used to monitor an external condition.
    positioners: dict[str, NXpositioner] = dc_field(
        default_factory=dict
    )  # Class to describe the motors that are used in the manipulator.
