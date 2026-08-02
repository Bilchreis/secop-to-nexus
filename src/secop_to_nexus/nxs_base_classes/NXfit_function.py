"""Auto-generated from NXfit_function.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXparameters import NXparameters


@dataclass
class NXfit_function(NXobject):
    """This describes a fit function that is used to fit data to any functional form.

    A fit function is used to describe a set of data :math:`y_k, k = 1 ... M`,  which are collected as a function
    of one or more independent variables :math:`x` at the points :math:`x_k`. The fit function :math:`f` describes
    these data in an approximate way as :math:`y_k \\approx f(a_0, . . . a_n, x_k)`,
    where :math:`a_i, i = 0 . . . n` are the *fit parameters* (which are stored the instances of ``NXfit_parameter``).
    """

    function_type: Optional[NX_CHAR] = None
    description: Optional[NX_CHAR] = None
    formula_description: Optional[NX_CHAR] = None
    fit_parameters: Optional[NXparameters] = None
