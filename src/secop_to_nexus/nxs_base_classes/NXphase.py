"""Auto-generated from NXphase.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
    from secop_to_nexus.nxs_base_classes.NXatom import NXatom
    from secop_to_nexus.nxs_base_classes.NXunit_cell import NXunit_cell


@dataclass
class NXphase(NXobject):
    """Base class to describe a (thermodynamic) phase as a component of a material.

    Instances of phases can be crystalline.
    """

    phase_id: Optional[NX_INT] = None  # units: NX_UNITLESS
    name: Optional[NX_CHAR] = None
    unit_cells: dict[str, NXunit_cell] = dc_field(default_factory=dict)
    atoms: dict[str, NXatom] = dc_field(default_factory=dict)
