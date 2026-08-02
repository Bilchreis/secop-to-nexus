"""Auto-generated from NXapm_event_data.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_DATE_TIME,
    NX_INT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXapm_instrument import NXapm_instrument


@dataclass
class NXapm_event_data(NXobject):
    """Base class to store state and (meta)data of events over the course of an atom probe experiment.

    Having at least one instance for an instance of NXapm is recommended.

    This base class applies the concept of the :ref:`NXem_event_data` base class to the specific needs
    of atom probe research. Again static and dynamic quantities are split to avoid a duplication
    of information. Specifically, the time interval considered is the entire time
    starting at start_time until end_time during which we assume the pulser triggered pulses.
    These pulses are identified via the pulse_id field. The point in time when each pulse was
    fired can be recovered from analyzing start_time and delta_time.

    Which temporal granularity is adequate depends on the situation and research question.
    Using a model which enables a collection of events offers the most flexible way to cater for
    both atom probe experiments or simulation. To monitor the course of an ion extraction experiment
    (or simulation) it makes sense to track time explicitly via time stamps or implicitly
    via e.g. a clock inside the instrument, such as the clock of the pulser and respective pulse_id.
    """

    start_time: Optional[NX_DATE_TIME] = None
    end_time: Optional[NX_DATE_TIME] = None
    delta_time: Optional[NX_NUMBER] = None  # units: NX_TIME
    pulse_id_offset: Optional[NX_INT] = None  # units: NX_UNITLESS
    pulse_id: Optional[NX_INT] = None  # units: NX_UNITLESS
    instrument: Optional[NXapm_instrument] = (
        None  # Place to store dynamic metadata of the instrument to document as close as possible
    )
