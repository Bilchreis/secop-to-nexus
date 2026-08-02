"""Auto-generated from NXevent_data.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_DATE_TIME,
    NX_FLOAT,
    NX_INT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXevent_data(NXobject):
    """NXevent_data is a special group for storing data from neutron
    detectors in event mode.  In this mode, the detector electronics
    emits a stream of detectorID, timestamp pairs. With detectorID
    describing the detector element in which the neutron was detected
    and timestamp the timestamp at which the neutron event was
    detected. In NeXus detectorID maps to event_id, event_time_offset
    to the timestamp.

    As this kind of data is common at pulsed neutron
    sources, the timestamp is almost always relative to the start of a
    neutron pulse. Thus the pulse timestamp is recorded too together
    with an index in the event_id, event_time_offset pair at which data for
    that pulse starts. At reactor source the same pulsed data effect
    may be achieved through the use of choppers or in stroboscopic
    measurement setups.

    In order to make random access to timestamped data
    faster there is an optional array pair of
    cue_timestamp_zero and cue_index. The cue_timestamp_zero will
    contain courser timestamps then in the time array, say
    every five minutes. The cue_index will then contain the
    index into the event_id,event_time_offset pair of arrays for that
    courser cue_timestamp_zero.
    """

    event_time_offset: Optional[NX_NUMBER] = None  # units: NX_TIME_OF_FLIGHT
    event_id: Optional[NX_INT] = None  # units: NX_DIMENSIONLESS
    event_time_zero: Optional[NX_NUMBER] = None  # units: NX_TIME
    event_index: Optional[NX_INT] = None  # units: NX_DIMENSIONLESS
    pulse_height: Optional[NX_FLOAT] = None  # units: NX_DIMENSIONLESS
    cue_timestamp_zero: Optional[NX_DATE_TIME] = None  # units: NX_TIME
    cue_index: Optional[NX_INT] = None
