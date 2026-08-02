"""Auto-generated from NXsensor.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_FLOAT,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXlog import NXlog
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry
    from secop_to_nexus.nxs_base_classes.NXorientation import NXorientation


@dataclass
class NXsensor(NXcomponent):
    """A sensor used to monitor an external condition

    The condition itself is described in :ref:`NXenvironment`.
    """

    model: Optional[NX_CHAR] = None
    name: Optional[NX_CHAR] = None
    short_name: Optional[NX_CHAR] = None
    attached_to: Optional[NX_CHAR] = None
    measurement: Optional[NX_CHAR] = (
        None  # enum: temperature | pH | magnetic_field | electric_field ...
    )
    type: Optional[NX_CHAR] = None
    run_control: Optional[NX_BOOLEAN] = None
    high_trip_value: Optional[NX_FLOAT] = None  # units: NX_ANY
    low_trip_value: Optional[NX_FLOAT] = None  # units: NX_ANY
    value: Optional[NX_FLOAT] = None  # units: NX_ANY
    value_deriv1: Optional[NX_FLOAT] = None  # units: NX_ANY
    value_deriv2: Optional[NX_FLOAT] = None  # units: NX_ANY
    external_field_brief: Optional[NX_CHAR] = (
        None  # enum: along beam | across beam | transverse | solenoidal ...
    )
    depends_on: Optional[NX_CHAR] = None
    geometry: Optional[NXgeometry] = (
        None  # Defines the axes for logged vector quantities if they are not the global instrument axes.
    )
    value_log: Optional[NXlog] = None  # Time history of sensor readings
    value_deriv1_log: Optional[NXlog] = (
        None  # Time history of first derivative of sensor readings
    )
    value_deriv2_log: Optional[NXlog] = (
        None  # Time history of second derivative of sensor readings
    )
    external_field_full: Optional[NXorientation] = (
        None  # For complex external fields not satisfied by External_field_brief
    )
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the sensor when necessary.
