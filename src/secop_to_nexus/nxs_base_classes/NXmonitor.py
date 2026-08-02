"""Auto-generated from NXmonitor.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_DATE_TIME,
    NX_FLOAT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXlog import NXlog
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry


@dataclass
class NXmonitor(NXcomponent):
    """A monitor of incident beam data.

    It is similar to the :ref:`NXdata` groups containing
    monitor data and its associated axis coordinates, e.g. time_of_flight or
    wavelength in pulsed neutron instruments. However, it may also include
    integrals, or scalar monitor counts, which are often used in both in both
    pulsed and steady-state instrumentation.
    """

    mode: Optional[NX_CHAR] = None  # enum: monitor | timer
    start_time: Optional[NX_DATE_TIME] = None
    end_time: Optional[NX_DATE_TIME] = None
    preset: Optional[NX_NUMBER] = None  # units: NX_ANY
    distance: Optional[NX_FLOAT] = None  # units: NX_LENGTH; deprecated
    range: Optional[NX_FLOAT] = None  # units: NX_ANY
    nominal: Optional[NX_NUMBER] = None  # units: NX_ANY
    integral: Optional[NX_NUMBER] = None  # units: NX_ANY
    type: Optional[NX_CHAR] = None  # enum: Fission Chamber | Scintillator
    time_of_flight: Optional[NX_FLOAT] = None  # units: NX_TIME_OF_FLIGHT
    efficiency: Optional[NX_NUMBER] = None  # units: NX_DIMENSIONLESS
    data: Optional[NX_NUMBER] = None  # units: NX_ANY
    sampled_fraction: Optional[NX_FLOAT] = None  # units: NX_DIMENSIONLESS
    count_time: Optional[NX_FLOAT] = None  # units: NX_TIME
    depends_on: Optional[NX_CHAR] = None
    integral_log: Optional[NXlog] = None  # Time variation of monitor counts
    geometries: dict[str, NXgeometry] = dc_field(
        default_factory=dict
    )  # Geometry of the monitor
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the beam line component
