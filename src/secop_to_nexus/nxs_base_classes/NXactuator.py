"""Auto-generated from NXactuator.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
    from secop_to_nexus.nxs_base_classes.NXpid_controller import NXpid_controller


@dataclass
class NXactuator(NXcomponent):
    """An actuator used to control an external condition.

    The condition itself is described in :ref:`NXenvironment`.
    """

    name: Optional[NX_CHAR] = None
    short_name: Optional[NX_CHAR] = None
    actuation_target: Optional[NX_CHAR] = None
    physical_quantity: Optional[NX_CHAR] = None
    type: Optional[NX_CHAR] = None
    outputVALUE: dict[str, NX_NUMBER] = dc_field(
        default_factory=dict
    )  # nameType: partial; units: NX_ANY
    pid_controllers: dict[str, NXpid_controller] = dc_field(
        default_factory=dict
    )  # If the actuator is PID-controlled, the settings of the PID controller can be
