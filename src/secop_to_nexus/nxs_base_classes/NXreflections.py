"""Auto-generated from NXreflections.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_FLOAT,
    NX_INT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXreflections(NXobject):
    """Reflection data from diffraction experiments"""

    description: Optional[str] = dc_field(
        default=None, metadata={"kind": "attribute"}
    )  # attribute; Describes the dataset
    experiments: Optional[NX_CHAR] = None
    h: Optional[NX_NUMBER] = None
    k: Optional[NX_NUMBER] = None
    l: Optional[NX_NUMBER] = None
    id: Optional[NX_INT] = None
    reflection_id: Optional[NX_INT] = None
    entering: Optional[NX_BOOLEAN] = None
    det_module: Optional[NX_INT] = None
    flags: Optional[NX_INT] = None
    d: Optional[NX_FLOAT] = None
    partiality: Optional[NX_FLOAT] = None
    predicted_frame: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    predicted_x: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    predicted_y: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    predicted_phi: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    predicted_px_x: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    predicted_px_y: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    observed_frame: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    observed_frame_var: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    observed_frame_errors: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    observed_px_x: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    observed_px_x_var: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    observed_px_x_errors: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    observed_px_y: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    observed_px_y_var: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    observed_px_y_errors: Optional[NX_FLOAT] = None  # units: NX_UNITLESS
    observed_phi: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    observed_phi_var: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    observed_phi_errors: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    observed_x: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    observed_x_var: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    observed_x_errors: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    observed_y: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    observed_y_var: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    observed_y_errors: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    bounding_box: Optional[NX_INT] = None  # units: NX_UNITLESS
    background_mean: Optional[NX_FLOAT] = None
    int_prf: Optional[NX_FLOAT] = None
    int_prf_var: Optional[NX_FLOAT] = None
    int_prf_errors: Optional[NX_FLOAT] = None
    int_sum: Optional[NX_FLOAT] = None
    int_sum_var: Optional[NX_FLOAT] = None
    int_sum_errors: Optional[NX_FLOAT] = None
    lp: Optional[NX_FLOAT] = None
    prf_cc: Optional[NX_FLOAT] = None
    overlaps: Optional[NX_INT] = None
    polar_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    azimuthal_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
