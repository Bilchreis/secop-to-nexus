"""Auto-generated from NXcs_filter_boolean_mask.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_UINT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXcs_filter_boolean_mask(NXobject):
    """Base class for packing and unpacking booleans.

    The field mask should be constructed from packing a vector of booleans
    (a bitfield) into unsigned integers with bytesize bitdepth. Padding to
    an integer number of such integers is assumed.

    Thereby, this base class can be used to inform software about necessary modulo
    operations to decode the mask to recover e.g. set membership of objects in sets
    whose membership has been encoded as a vector of booleans.

    This is useful e.g. when processing object sets such as point cloud data.
    If e.g. a spatial filter has been applied to a set of points, we may wish to document
    memory-space efficiently which points were analyzed. An array of boolean values
    is one option to achieve this. A value is true if the point is included and false otherwise.
    """

    depends_on: Optional[NX_CHAR] = None
    number_of_objects: Optional[NX_UINT] = None  # units: NX_UNITLESS
    bitdepth: Optional[NX_UINT] = None  # units: NX_UNITLESS
    mask: Optional[NX_UINT] = None  # units: NX_UNITLESS
