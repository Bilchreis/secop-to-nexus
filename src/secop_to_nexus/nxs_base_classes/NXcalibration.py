"""Auto-generated from NXcalibration.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_FLOAT,
)
from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXnote import NXnote
    from secop_to_nexus.nxs_base_classes.NXparameters import NXparameters


@dataclass
class NXcalibration(NXprocess):
    """Subclass of NXprocess to describe post-processing calibrations."""

    description: Optional[NX_CHAR] = None
    physical_quantity: Optional[NX_CHAR] = None
    identifier_calibration_method: Optional[NX_CHAR] = None
    identifier_calibration_reference: Optional[NX_CHAR] = None
    last_process: Optional[NX_CHAR] = None
    applied: Optional[NX_BOOLEAN] = None
    original_axis: Optional[NX_FLOAT] = None  # units: NX_ANY
    fit_formula_description: Optional[NX_CHAR] = None
    mapping_MAPPING: dict[str, NX_FLOAT] = dc_field(
        default_factory=dict
    )  # nameType: partial
    calibrated_axis: Optional[NX_FLOAT] = None  # units: NX_ANY
    calibration_object: Optional[NXnote] = (
        None  # A file serialization of a calibration which may not be publicly available (externally from th...
    )
    fit_formula_inputs: Optional[NXparameters] = (
        None  # Additional input axis to be used in the formula.
    )
    calibration_parameters: Optional[NXparameters] = (
        None  # Fit coefficients to be used in ``fit_formula_description``.
    )
    data: dict[str, NXdata] = dc_field(
        default_factory=dict
    )  # Any data acquired/used during the calibration that does not fit the `NX_FLOAT` fields above.
