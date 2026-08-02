"""Auto-generated from NXatom.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_NUMBER,
    NX_UINT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXatom(NXobject):
    """Base class for documenting a set of atoms.

    Atoms in the set may be bonded. The set may have
    a net charge to represent an ion.
    An ion can be a molecular ion.
    """

    name: Optional[NX_CHAR] = None
    id: Optional[NX_UINT] = None  # units: NX_UNITLESS
    identifier_chemical: Optional[NX_CHAR] = None  # enum: inchi
    charge: Optional[NX_NUMBER] = None  # units: NX_CHARGE
    charge_state: Optional[NX_NUMBER] = None  # units: NX_UNITLESS
    volume: Optional[NX_NUMBER] = None  # units: NX_VOLUME
    indices: Optional[NX_CHAR] = None
    type: Optional[NX_UINT] = None  # units: NX_UNITLESS
    position: Optional[NX_NUMBER] = None  # units: NX_ANY
    occupancy: Optional[NX_NUMBER] = None  # units: NX_DIMENSIONLESS
    nuclide_hash: Optional[NX_UINT] = None  # units: NX_UNITLESS
    nuclide_list: Optional[NX_UINT] = None  # units: NX_UNITLESS
    mass_to_charge_range: Optional[NX_NUMBER] = None  # units: NX_ANY
