"""Auto-generated from NXcs_profiling_event.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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


@dataclass
class NXcs_profiling_event(NXobject):
    """Computer science description of a profiling event."""

    start_time: Optional[NX_DATE_TIME] = None
    end_time: Optional[NX_DATE_TIME] = None
    description: Optional[NX_CHAR] = None
    elapsed_time: Optional[NX_NUMBER] = None  # units: NX_TIME
    max_processes: Optional[NX_UINT] = None  # units: NX_UNITLESS
    max_threads: Optional[NX_UINT] = None  # units: NX_UNITLESS
    max_gpus: Optional[NX_UINT] = None  # units: NX_UNITLESS
    max_virtual_memory_snapshot: Optional[NX_NUMBER] = None  # units: NX_ANY
    max_resident_memory_snapshot: Optional[NX_NUMBER] = None  # units: NX_ANY
