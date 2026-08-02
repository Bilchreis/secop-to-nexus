"""Auto-generated from NXapm_instrument.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
)
from secop_to_nexus.nxs_base_classes.NXinstrument import NXinstrument

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent
    from secop_to_nexus.nxs_base_classes.NXdetector import NXdetector
    from secop_to_nexus.nxs_base_classes.NXfabrication import NXfabrication
    from secop_to_nexus.nxs_base_classes.NXmanipulator import NXmanipulator
    from secop_to_nexus.nxs_base_classes.NXparameters import NXparameters
    from secop_to_nexus.nxs_base_classes.NXpump import NXpump


@dataclass
class NXapm_instrument(NXinstrument):
    """Base class for instrument-related details of a real or simulated
    atom probe tomograph or field-ion microscope.

    For collecting data and experiments which are simulations of an atom probe
    microscope or a session with such instrument use the :ref:`NXapm` application definition
    and the :ref:`NXapm_event_data` groups it provides.

    This base class implements the concept of :ref:`NXapm` whereby (meta)data are distinguished
    whether these typically change during a session, so-called dynamic, or not, so-called static metadata.
    This design allows to store e.g. hardware related concepts only once instead of demanding
    that each image or spectrum from the session needs to be stored also with the static metadata.
    """

    type: Optional[NX_CHAR] = (
        None  # enum: Inspico | 3DAP | LAWATAP | LEAP 3000 Si | LEAP 3000...
    )
    location: Optional[NX_CHAR] = None
    flight_path: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    comment: Optional[NX_CHAR] = None
    fabrication: Optional[NXfabrication] = None
    reflectron: Optional[NXcomponent] = (
        None  # Device which reduces ToF differences of ions in ToF experiments.
    )
    decelerate_electrode: Optional[NXcomponent] = (
        None  # A counter electrode of the LEAP 6000 series atom probes.
    )
    local_electrode: Optional[NXcomponent] = (
        None  # A local electrode guiding the ion flight path.
    )
    ion_detector: Optional[NXdetector] = (
        None  # Detector for taking raw time-of-flight and ion/hit impact positions data.
    )
    pulser: Optional[NXcomponent] = (
        None  # Laser- and/or voltage-pulsing device to trigger ion removal.
    )
    stage: Optional[NXmanipulator] = None
    analysis_chamber: Optional[NXcomponent] = None
    buffer_chamber: Optional[NXcomponent] = None
    load_lock_chamber: Optional[NXcomponent] = None
    getter_pump: Optional[NXpump] = None
    roughening_pump: Optional[NXpump] = None
    turbomolecular_pump: Optional[NXpump] = None
    control: Optional[NXparameters] = (
        None  # Relevant quantities during a measurement with a LEAP system as were
    )
