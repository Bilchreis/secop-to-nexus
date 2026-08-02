"""Auto-generated from NXcg_point.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_DATE_TIME,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcg_primitive import NXcg_primitive


@dataclass
class NXcg_point(NXcg_primitive):
    """Computational geometry description of a set of points.

    Points may have an associated time value. Users are advised though to store
    time data of point sets rather as instances of time events, where for each
    point in time there is an :ref:`NXcg_point` instance which specifies the
    points' locations.

    This is a frequent situation in experiments and computer simulations, where
    positions of points are taken at the same point in time (real time or
    simulated physical time). Thereby, the storage of redundant timestamp
    information per point is considered as obsolete.
    """

    position: Optional[NX_NUMBER] = None  # units: NX_ANY
    time: Optional[NX_NUMBER] = None  # units: NX_TIME
    timestamp: Optional[NX_DATE_TIME] = None
    time_offset: Optional[NX_DATE_TIME] = None
