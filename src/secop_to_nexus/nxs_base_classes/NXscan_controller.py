"""Auto-generated from NXscan_controller.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
    from secop_to_nexus.nxs_base_classes.NXcircuit import NXcircuit
    from secop_to_nexus.nxs_base_classes.NXdeflector import NXdeflector


@dataclass
class NXscan_controller(NXcomponent):
    """The scan box or scan controller is a component that is used to deflect a
    beam of charged particles in a controlled manner.

    The scan box is instructed by (an) instance(s) of :ref:`NXprogram`, some control software,
    which is not necessarily the same program as the one controlling other parts of the instrument.

    The scan box directs the probe of charged particles (electrons, ions)
    to controlled locations according to a scan scheme and plan.
    """

    scan_schema: Optional[NX_CHAR] = None
    dwell_time: Optional[NX_NUMBER] = None  # units: NX_TIME
    flyback_time: Optional[NX_NUMBER] = None  # units: NX_TIME
    deflectors: dict[str, NXdeflector] = dc_field(
        default_factory=dict
    )  # Details about components which realize the deflection technically.
    circuits: dict[str, NXcircuit] = dc_field(default_factory=dict)
