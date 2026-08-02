"""Auto-generated from NXaberration.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXaberration(NXobject):
    """Quantified aberration coefficient in an aberration_model.

    For an introduction in the details about aberrations with relevance for electron microscopy
    see `R. Dunin-Borkowski et al. <https://doi.org/10.1017/9781316337455.022>`_ and
    `S. J. Pennycock and P. D. Nellist <https://doi.org/10.1007/978-1-4419-7200-2>`_ (page 44ff, and page 118ff)
    for different definitions available and further details.
    Table 7-2 of Ibid. publication (page 305ff) documents how to convert from the Nion to the CEOS definitions.
    Conversion tables are also summarized by `Y. Liao <https://www.globalsino.com/EM/page3740.html>`_ an introduction.

    The use of the base class is not restricted to electron microscopy but can also be useful for classical optics.
    """

    magnitude: Optional[NX_NUMBER] = None  # units: NX_ANY
    magnitude_errors: Optional[NX_NUMBER] = None  # units: NX_ANY
    magnitude_errors_model: Optional[NX_CHAR] = None
    delta_time: Optional[NX_NUMBER] = None  # units: NX_TIME
    angle: Optional[NX_NUMBER] = None  # units: NX_ANGLE
    name: Optional[NX_CHAR] = None
    alias: Optional[NX_CHAR] = None
