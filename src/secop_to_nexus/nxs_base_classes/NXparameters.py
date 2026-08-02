"""Auto-generated from NXparameters.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR_OR_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXparameters(NXobject):
    """Container for parameters used in processing or analysing data.

    Typically, this group is stored in a :ref:`NXprocess` group in
    order to contain parameters that are either inputs to or
    resulting from the process defined by the parent group. However,
    this base class can also be added to other groups for use in
    other contexts.

    Although this base class can be used to store any kind of
    parameter, one possible use case is to store parameters that are
    refined by a fitting function or model. A number of attributes
    have been defined to store metadata associated with such a
    refinement.
    """

    model: Optional[str] = dc_field(
        default=None, metadata={"kind": "attribute"}
    )  # attribute; The name of the model used in optimizing the parameter
    PARAMETER: dict[str, NX_CHAR_OR_NUMBER] = dc_field(
        default_factory=dict
    )  # nameType: any
