"""Auto-generated from NXcs_profiling.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_DATE_TIME,
    NX_NUMBER,
    NX_UINT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcs_computer import NXcs_computer
    from secop_to_nexus.nxs_base_classes.NXcs_profiling_event import (
        NXcs_profiling_event,
    )


@dataclass
class NXcs_profiling(NXobject):
    """Computer science description for performance and profiling data of an application.

    Performance monitoring and benchmarking of software is a task where questions
    can be asked at various levels of detail. In general, there are three main
    contributions to performance:

    * Hardware capabilities and configuration
    * Software configuration and capabilities
    * Dynamic effects of the system in operation and the system working together
      with eventually multiple computers, especially when these have to exchange
      information across a network and these are used usually by multiple users.

    At the most basic level users may wish to document how long e.g. a data
    analysis with a scientific software, i.e. an app took.

    A frequent idea is here to answer practical questions like how critical is the
    effect on the workflow of the scientists, i.e. is the analysis possible in
    a few seconds or would it take days if I were to run this analysis on a
    comparable machine?
    For this more qualitative performance monitoring, mainly the order of
    magnitude is relevant, as well as how this was achieved using parallelization
    (i.e. reporting the number of CPU and GPU resources used, the number of
    processes and threads configured, and providing basic details about the computer).

    At more advanced levels benchmarks may go as deep as detailed temporal tracking
    of individual processor instructions, their relation to other instructions, the
    state of call stacks; in short eventually the entire app execution history
    and hardware state history. Such analyses are mainly used for performance
    optimization, i.e. by software and hardware developers as well as for
    tracking bugs. Specialized software exists which documents such performance
    data in specifically-formatted event log files or databases.

    This base class cannot and should not replace these specific solutions for now.
    Instead, the intention of the base class is to serve scientists at the
    basic level to enable simple monitoring of performance data and log profiling
    data of key algorithmic steps or parts of computational workflows, so that
    these pieces of information can guide users which order of magnitude differences
    should be expected or not.

    Developers of application definitions should add additional fields and
    references to e.g. more detailed performance data to which they wish to link
    the metadata in this base class.
    """

    current_working_directory: Optional[NX_CHAR] = None
    command_line_call: Optional[NX_CHAR] = None
    start_time: Optional[NX_DATE_TIME] = None
    end_time: Optional[NX_DATE_TIME] = None
    total_elapsed_time: Optional[NX_NUMBER] = None  # units: NX_TIME
    max_processes: Optional[NX_UINT] = None  # units: NX_UNITLESS
    max_threads: Optional[NX_UINT] = None  # units: NX_UNITLESS
    max_gpus: Optional[NX_UINT] = None  # units: NX_UNITLESS
    cs_computers: dict[str, NXcs_computer] = dc_field(
        default_factory=dict
    )  # A collection with one or more computing nodes each with own resources.
    eventID: dict[str, NXcs_profiling_event] = dc_field(
        default_factory=dict
    )  # nameType: partial
