"""Auto-generated from NXpeak.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXfit_function import NXfit_function


@dataclass
class NXpeak(NXobject):
    """Base class for describing a peak, its functional form, and support values
    i.e., the discretization points at which the function has been evaluated.
    """

    label: Optional[NX_CHAR] = None
    total_area: Optional[NX_NUMBER] = None  # units: NX_ANY
    data: Optional[NXdata] = None
    function: Optional[NXfit_function] = (
        None  # The functional form of the peak. This could be a Gaussian, Lorentzian, Voigt,
    )
