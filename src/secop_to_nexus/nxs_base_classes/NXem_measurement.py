"""Auto-generated from NXem_measurement.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXem_event_data import NXem_event_data
    from secop_to_nexus.nxs_base_classes.NXem_instrument import NXem_instrument


@dataclass
class NXem_measurement(NXobject):
    """Base class for documenting a measurement with an electron microscope."""

    instrument: Optional[NXem_instrument] = None
    eventID: dict[str, NXem_event_data] = dc_field(
        default_factory=dict
    )  # nameType: partial
