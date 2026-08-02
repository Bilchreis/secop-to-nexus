"""Auto-generated from NXcylindrical_geometry.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_INT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXcylindrical_geometry(NXobject):
    """Geometry description for cylindrical shapes.
    This class can be used in place of ``NXoff_geometry`` when an exact
    representation for cylinders is preferred.
    For example, for Helium-tube, neutron detectors.
    It can be used to describe the shape of any component, including detectors.
    In the case of detectors it can be used to define the shape of a single pixel, or,
    if the pixel shapes are non-uniform, to describe the shape of the whole detector.
    """

    vertices: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    cylinders: Optional[NX_INT] = None
    detector_number: Optional[NX_INT] = None
