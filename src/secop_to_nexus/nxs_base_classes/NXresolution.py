"""Auto-generated from NXresolution.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcalibration import NXcalibration
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXnote import NXnote
    from secop_to_nexus.nxs_base_classes.NXparameters import NXparameters


@dataclass
class NXresolution(NXobject):
    """Describes the resolution of a physical quantity."""

    physical_quantity: Optional[NX_CHAR] = None
    type: Optional[NX_CHAR] = None  # enum: estimated | derived | calibrated | other
    resolution: Optional[NX_FLOAT] = None  # units: NX_ANY
    resolution_errors: Optional[NX_FLOAT] = None  # units: NX_ANY
    relative_resolution: Optional[NX_FLOAT] = None  # units: NX_ANY
    relative_resolution_errors: Optional[NX_FLOAT] = None  # units: NX_DIMENSIONLESS
    resolution_formula_description: Optional[NX_CHAR] = None
    note: Optional[NXnote] = (
        None  # Additional details of the estimate or description of the calibration procedure
    )
    response_function: Optional[NXdata] = (
        None  # The response of the instrument or part of the instrument to a infinitesimally sharp input signal
    )
    formula_symbols: Optional[NXparameters] = (
        None  # Symbols linking to another path in the NeXus tree to be referred to from the
    )
    calibrations: dict[str, NXcalibration] = dc_field(
        default_factory=dict
    )  # For storing details and data of a calibration to derive a resolution from data.
