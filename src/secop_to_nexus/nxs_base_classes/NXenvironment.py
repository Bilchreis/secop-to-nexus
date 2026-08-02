"""Auto-generated from NXenvironment.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXactuator import NXactuator
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXnote import NXnote
    from secop_to_nexus.nxs_base_classes.NXsensor import NXsensor
    from secop_to_nexus.nxs_base_classes.NXtransformations import NXtransformations


@dataclass
class NXenvironment(NXobject):
    """Parameters for controlling external conditions"""

    name: Optional[NX_CHAR] = None
    short_name: Optional[NX_CHAR] = None
    type: Optional[NX_CHAR] = None
    description: Optional[NX_CHAR] = None
    program: Optional[NX_CHAR] = None
    value: Optional[NX_FLOAT] = None  # units: NX_ANY
    depends_on: Optional[NX_CHAR] = None
    position: Optional[NXgeometry] = (
        None  # The position and orientation of the apparatus.
    )
    transformations: dict[str, NXtransformations] = dc_field(
        default_factory=dict
    )  # This is the group recommended for holding the chain of translation
    notes: dict[str, NXnote] = dc_field(
        default_factory=dict
    )  # Additional information, LabView logs, digital photographs, etc
    actuators: dict[str, NXactuator] = dc_field(
        default_factory=dict
    )  # Any actuator used to control the environment. This can be linked to an actuator
    sensors: dict[str, NXsensor] = dc_field(
        default_factory=dict
    )  # Any sensor used to monitor the environment. This can be linked to a sensor
