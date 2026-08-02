"""Auto-generated from NXpid_controller.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXsensor import NXsensor


@dataclass
class NXpid_controller(NXcomponent):
    """A description of a feedback system in terms of the settings of a proportional-integral-derivative (PID) controller.

    Automated control of a physical quantity is often achieved by connecting the output of a sensor to an actuator
    (e.g. using a thermocouple to monitor the effect of a heater and influence the power provided to it). The physical
    quantity being operated on is typically referred to as the "Process Variable", with the desired value being the
    "Setpoint" (which may vary as a function of time) and the "Error Value" is the time-varying function of the difference
    between the Setpoint value and the concurrent measurement of the Process Variable  (Error Value = Setpoint - Process Variable).

    A PID controller calculates an output value for use as an input signal to an actuator via the weighted sum of four terms:
    * Proportional: the current Error Value
    * Integral: the integral of the Error Value function
    * Derivative: the first derivative of the Error Value function
    * Feed Forward: A model of the physical system (optional)

    The weightings of these terms are given by the corresponding constants:
    * K_p
    * K_i
    * K_d
    * K_ff

    A classic PID controller only implements the P, I and D terms and the values of the K_p, K_i and K_d constants are sufficient to fully
    describe the behavior of the feedback system implemented by such a PID controller. The inclusion of a Feed Forward term in a feedback system
    is a modern adaptation that aids optimization of the automated control. It is not present in all PID controllers, but it is also not uncommon.

    Note that the ``NXpid_controller`` is designed to be a child object of the actuator that its output is connected to. The parent object
    representing the actuator is likely to be represented by an ``NXactuator`` or ``NXpositioner`` base class, but there is a wide variety
    of possible applications for PID controllers.
    """

    description: Optional[NX_CHAR] = None
    setpoint: Optional[NX_FLOAT] = None  # units: NX_ANY
    K_p: Optional[NX_NUMBER] = None
    K_i: Optional[NX_NUMBER] = None
    K_d: Optional[NX_NUMBER] = None
    K_ff: Optional[NX_NUMBER] = None
    feed_forward_model: Optional[NX_CHAR] = None
    control_action: Optional[NX_CHAR] = None  # enum: direct | reverse
    pv_sensor: Optional[NXsensor] = (
        None  # The sensor representing the Process Value used in the feedback loop for the PID.
    )
