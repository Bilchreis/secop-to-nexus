"""Auto-generated from NXem_instrument.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
)
from secop_to_nexus.nxs_base_classes.NXinstrument import NXinstrument

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXactuator import NXactuator
    from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent
    from secop_to_nexus.nxs_base_classes.NXdetector import NXdetector
    from secop_to_nexus.nxs_base_classes.NXebeam_column import NXebeam_column
    from secop_to_nexus.nxs_base_classes.NXem_optical_system import NXem_optical_system
    from secop_to_nexus.nxs_base_classes.NXfabrication import NXfabrication
    from secop_to_nexus.nxs_base_classes.NXibeam_column import NXibeam_column
    from secop_to_nexus.nxs_base_classes.NXmanipulator import NXmanipulator
    from secop_to_nexus.nxs_base_classes.NXpump import NXpump
    from secop_to_nexus.nxs_base_classes.NXsensor import NXsensor


@dataclass
class NXem_instrument(NXinstrument):
    """Base class for instrument-related details of a real or simulated electron microscope.

    For collecting data and experiments which are simulations of an electron
    microscope (or such session) use the :ref:`NXem` application definition and
    the :ref:`NXem_event_data` groups it provides.

    This base class implements the concept of :ref:`NXem` whereby (meta)data are distinguished
    whether these typically change during a session (dynamic) or not (static metadata).
    This design allows to store e.g. hardware related concepts only once instead of demanding
    that each image or spectrum from the session needs to be stored also with the static metadata.
    """

    name: Optional[NX_CHAR] = None
    location: Optional[NX_CHAR] = None
    type: Optional[NX_CHAR] = None  # enum: sem | fib | tem
    fabrications: dict[str, NXfabrication] = dc_field(default_factory=dict)
    ebeam_columns: dict[str, NXebeam_column] = dc_field(default_factory=dict)
    ibeam_columns: dict[str, NXibeam_column] = dc_field(default_factory=dict)
    em_optical_systems: dict[str, NXem_optical_system] = dc_field(default_factory=dict)
    detectors: dict[str, NXdetector] = dc_field(
        default_factory=dict
    )  # Description of the type of the detector.
    stageID: dict[str, NXmanipulator] = dc_field(
        default_factory=dict
    )  # nameType: partial
    nanoprobeID: dict[str, NXmanipulator] = dc_field(
        default_factory=dict
    )  # nameType: partial
    gas_injector: Optional[NXcomponent] = (
        None  # Gas injection systems (GIS) are components of microscopes that are equipped with focused-ion ...
    )
    pumps: dict[str, NXpump] = dc_field(default_factory=dict)
    sensors: dict[str, NXsensor] = dc_field(default_factory=dict)
    actuators: dict[str, NXactuator] = dc_field(default_factory=dict)
