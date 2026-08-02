"""Auto-generated from NXinsertion_device.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
    NX_INT,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry


@dataclass
class NXinsertion_device(NXcomponent):
    """An insertion device, as used in a synchrotron light source."""

    type: Optional[NX_CHAR] = None  # enum: undulator | wiggler | wavelength_shifter
    gap: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    taper: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    phase: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    poles: Optional[NX_INT] = None  # units: NX_UNITLESS
    magnetic_wavelength: Optional[NX_FLOAT] = None  # units: NX_WAVELENGTH
    k: Optional[NX_FLOAT] = None  # units: NX_DIMENSIONLESS
    length: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    power: Optional[NX_FLOAT] = None  # units: NX_POWER
    energy: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    bandwidth: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    harmonic: Optional[NX_INT] = None  # units: NX_UNITLESS
    depends_on: Optional[NX_CHAR] = None
    spectrum: Optional[NXdata] = None  # spectrum of insertion device
    geometries: dict[str, NXgeometry] = dc_field(
        default_factory=dict
    )  # "Engineering" position of insertion device
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the beam line component
