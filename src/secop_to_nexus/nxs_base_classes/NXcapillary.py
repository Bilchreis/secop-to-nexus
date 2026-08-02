"""Auto-generated from NXcapillary.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata


@dataclass
class NXcapillary(NXcomponent):
    """A capillary lens to focus the X-ray beam.

    Based on information provided by Gerd Wellenreuther (DESY).
    """

    type: Optional[NX_CHAR] = (
        None  # enum: single_bounce | polycapillary | conical_capillary
    )
    manufacturer: Optional[NX_CHAR] = None
    maximum_incident_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    accepting_aperture: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    working_distance: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    focal_size: Optional[NX_FLOAT] = None
    depends_on: Optional[NX_CHAR] = None
    gain: Optional[NXdata] = None  # The gain of the capillary as a function of energy
    transmission: Optional[NXdata] = (
        None  # The transmission of the capillary as a function of energy
    )
