"""Auto-generated from NXxraylens.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_FLOAT,
    NX_INT,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXnote import NXnote
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry


@dataclass
class NXxraylens(NXcomponent):
    """An X-ray lens, typically at a synchrotron X-ray beam line.

    Based on information provided by Gerd Wellenreuther (DESY).
    """

    lens_geometry: Optional[NX_CHAR] = (
        None  # enum: paraboloid | spherical | elliptical | hyperbolical
    )
    symmetric: Optional[NX_BOOLEAN] = None
    cylindrical: Optional[NX_BOOLEAN] = None
    focus_type: Optional[NX_CHAR] = None  # enum: line | point
    lens_thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    lens_length: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    curvature: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    aperture: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    number_of_lenses: Optional[NX_INT] = None
    lens_material: Optional[NX_CHAR] = None
    gas: Optional[NX_CHAR] = None
    gas_pressure: Optional[NX_FLOAT] = None  # units: NX_PRESSURE
    depends_on: Optional[NX_CHAR] = None
    cylinder_orientation: Optional[NXnote] = None  # Orientation of the cylinder axis.
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the beam line component
