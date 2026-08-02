"""Auto-generated from NXwaveplate.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXsample import NXsample


@dataclass
class NXwaveplate(NXcomponent):
    """A waveplate or retarder."""

    type: Optional[NX_CHAR] = (
        None  # enum: zero-order | achromatic | multiple-order | dual-wav...
    )
    retardance: Optional[NX_CHAR] = None  # enum: full-wave | half-wave | quarter-wave
    wavelengths: Optional[NX_NUMBER] = None
    diameter: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    clear_aperture: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    reflectance: Optional[NX_NUMBER] = None  # units: NX_UNITLESS
    retardance_distribution: Optional[NXdata] = (
        None  # Wavelength resolved retardance of the waveplate.
    )
    substrate: Optional[NXsample] = (
        None  # Describe the material of the substrate of the waveplate in
    )
    coating: Optional[NXsample] = (
        None  # Is the waveplate coated? If yes, specify the type and material of the
    )
