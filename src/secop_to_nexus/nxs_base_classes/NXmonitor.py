from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional

from secop_to_nexus.nxs_base_classes.NXdtypes import (
    NX_CHAR,
    NX_DATE_TIME,
    NX_FLOAT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry


@dataclass
class NXmonitor(NXobject):
    mode: Optional[NX_CHAR] = None  # e.g. "monitor", "timer"
    start_time: Optional[NX_DATE_TIME] = None
    end_time: Optional[NX_DATE_TIME] = None
    preset: Optional[NX_NUMBER] = None
    distance: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    range: Optional[NX_FLOAT] = None  # units: NX_ANY
    nominal: Optional[NX_NUMBER] = None
    integral: Optional[NX_NUMBER] = None  # units: NX_ANY
    type: Optional[NX_CHAR] = None
    time_of_flight: Optional[NX_FLOAT] = None  # units: NX_TIME_OF_FLIGHT
    efficiency: Optional[NX_NUMBER] = None
    data: Optional[NX_NUMBER] = None  # units: NX_ANY
    sampled_fraction: Optional[NX_FLOAT] = None
    count_time: Optional[NX_FLOAT] = None  # units: NX_TIME
    depends_on: Optional[NX_CHAR] = None

    # Arbitrarily named groups
    off_geometries: dict[str, NXoff_geometry] = field(default_factory=dict)
