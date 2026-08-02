"""Auto-generated from NXattenuator.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry


@dataclass
class NXattenuator(NXcomponent):
    """A device that reduces the intensity of a beam by attenuation.

    If uncertain whether to use :ref:`NXfilter` (band-pass filter)
    or :ref:`NXattenuator` (reduces beam intensity), then choose
    :ref:`NXattenuator`.
    """

    distance: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    type: Optional[NX_CHAR] = None
    thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    scattering_cross_section: Optional[NX_FLOAT] = None  # units: NX_CROSS_SECTION
    absorption_cross_section: Optional[NX_FLOAT] = None  # units: NX_CROSS_SECTION
    attenuator_transmission: Optional[NX_FLOAT] = None  # units: NX_DIMENSIONLESS
    status: Optional[NX_CHAR] = None  # enum: in | out | moving
    depends_on: Optional[NX_CHAR] = None
    shape: Optional[NXoff_geometry] = (
        None  # Shape of this component. Particularly useful to define the origin for position and orientatio...
    )
