"""Auto-generated from NXem_optical_system.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXem_optical_system(NXobject):
    """Base class for qualifying an electron optical system."""

    camera_length: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    magnification: Optional[NX_NUMBER] = None  # units: NX_DIMENSIONLESS
    defocus: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    semi_convergence_angle: Optional[NX_NUMBER] = None  # units: NX_ANGLE
    field_of_view: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    working_distance: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    probe: Optional[NX_NUMBER] = None
    probe_current: Optional[NX_NUMBER] = None  # units: NX_CURRENT
    dose_management: Optional[NX_CHAR] = None
    dose_rate: Optional[NX_NUMBER] = None  # units: 1/(angstrom^2*s)
    rotation: Optional[NX_NUMBER] = None  # units: NX_ANGLE
    focal_length: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    tilt_correction: Optional[NX_BOOLEAN] = None
    dynamic_focus_correction: Optional[NX_BOOLEAN] = None
    dynamic_refocusing: Optional[NX_CHAR] = None
