"""Auto-generated from NXgeometry.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_INT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXorientation import NXorientation
    from secop_to_nexus.nxs_base_classes.NXshape import NXshape
    from secop_to_nexus.nxs_base_classes.NXtranslation import NXtranslation


@dataclass
class NXgeometry(NXobject):
    """legacy class - recommend to use :ref:`NXtransformations` now

    It is recommended that instances of :ref:`NXgeometry` be converted to
    use :ref:`NXtransformations`.

    This is the description for a general position of a component.
    It is recommended to name an instance of :ref:`NXgeometry` as "geometry"
    to aid in the use of the definition in simulation codes such as McStas.
    Also, in HDF, linked items must share the same name.
    However, it might not be possible or practical in all situations.
    """

    description: Optional[NX_CHAR] = None
    component_index: Optional[NX_INT] = None
    shapes: dict[str, NXshape] = dc_field(
        default_factory=dict
    )  # shape/size information of component
    translations: dict[str, NXtranslation] = dc_field(
        default_factory=dict
    )  # translation of component
    orientations: dict[str, NXorientation] = dc_field(
        default_factory=dict
    )  # orientation of component
