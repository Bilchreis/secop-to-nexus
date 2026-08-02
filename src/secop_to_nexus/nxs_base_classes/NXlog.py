"""Auto-generated from NXlog.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
    NX_INT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXlog(NXobject):
    """Information recorded as a function of time.

    Description of information that is recorded against
    time. There are two common use cases for this:

    - When logging data such as temperature during a run
    - When data is taken in streaming mode data acquisition,
      i.e. just timestamp, value pairs are stored and
      correlated later in data reduction with other data,


    In both cases, NXlog contains
    the logged or streamed  values and the times at which they were measured as elapsed time since a starting
    time recorded in ISO8601 format. The time units are
    specified in the units attribute. An optional scaling attribute
    can be used to accommodate non standard clocks.


    This method of storing logged data helps to distinguish instances in which a variable contains signal or
    axis coordinate values of plottable data, in which case it is stored
    in an :ref:`NXdata` group, and instances in which it is logged during the
    run, when it should be stored in an :ref:`NXlog` group.

    In order to make random access to timestamped data faster there is an optional array pair of
    ``cue_timestamp_zero`` and ``cue_index``. The ``cue_timestamp_zero`` will
    contain coarser timestamps than in the time array, say
    every five minutes. The ``cue_index`` will then contain the
    index into the time,value pair of arrays for that
    coarser ``cue_timestamp_zero``.
    """

    time: Optional[NX_NUMBER] = None  # units: NX_TIME
    value: Optional[NX_NUMBER] = None  # units: NX_ANY
    raw_value: Optional[NX_NUMBER] = None  # units: NX_ANY
    description: Optional[NX_CHAR] = None
    average_value: Optional[NX_FLOAT] = None  # units: NX_ANY
    average_value_error: Optional[NX_FLOAT] = None  # units: NX_ANY; deprecated
    average_value_errors: Optional[NX_FLOAT] = None  # units: NX_ANY
    minimum_value: Optional[NX_FLOAT] = None  # units: NX_ANY
    maximum_value: Optional[NX_FLOAT] = None  # units: NX_ANY
    duration: Optional[NX_FLOAT] = None  # units: NX_ANY
    cue_timestamp_zero: Optional[NX_NUMBER] = None  # units: NX_TIME
    cue_index: Optional[NX_INT] = None
