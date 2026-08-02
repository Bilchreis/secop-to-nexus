"""Auto-generated from NXfit.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXfit_function import NXfit_function
    from secop_to_nexus.nxs_base_classes.NXpeak import NXpeak


@dataclass
class NXfit(NXprocess):
    """Description of a fit procedure using a scalar valued global function"""

    label: Optional[NX_CHAR] = None
    figure_of_meritMETRIC: dict[str, NX_NUMBER] = dc_field(
        default_factory=dict
    )  # nameType: partial; units: NX_UNITLESS
    data: Optional[NXdata] = None  # Data and results of the fit.
    peakPEAK: dict[str, NXpeak] = dc_field(default_factory=dict)  # nameType: partial
    backgroundBACKGROUND: dict[str, NXpeak] = dc_field(
        default_factory=dict
    )  # nameType: partial
    global_fit_function: Optional[NXfit_function] = (
        None  # Function used to describe the overall fit to the data, taking into account the parameters of the
    )
    error_function: Optional[NXfit_function] = (
        None  # Function used to optimize the parameters during peak fitting.
    )
