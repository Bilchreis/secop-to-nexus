"""Auto-generated from NXunit_cell.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_NUMBER,
    NX_POSINT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXatom import NXatom


@dataclass
class NXunit_cell(NXobject):
    """Base class to describe structural aspects of an arrangement of
    atoms or ions including a crystallographic unit cell.

    Following recommendations of `CIF <https://www.iucr.org/resources/cif/spec/version1.1>`_ and `International Tables of Crystallography <https://it.iucr.org/>`_.
    """

    reference_frame: Optional[NX_CHAR] = None
    dimensionality: Optional[NX_POSINT] = None  # enum: 1 | 2 | 3
    a_b_c: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    a: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    b: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    c: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    alpha_beta_gamma: Optional[NX_NUMBER] = None  # units: NX_ANGLE
    alpha: Optional[NX_NUMBER] = None  # units: NX_ANGLE
    beta: Optional[NX_NUMBER] = None  # units: NX_ANGLE
    gamma: Optional[NX_NUMBER] = None  # units: NX_ANGLE
    crystal_system: Optional[NX_CHAR] = (
        None  # enum: triclinic | monoclinic | orthorhombic | tetragonal ...
    )
    laue_group: Optional[NX_CHAR] = None
    point_group: Optional[NX_CHAR] = None
    space_group: Optional[NX_CHAR] = None
    is_centrosymmetric: Optional[NX_BOOLEAN] = None
    is_chiral: Optional[NX_BOOLEAN] = None
    area: Optional[NX_NUMBER] = None  # units: NX_AREA
    volume: Optional[NX_NUMBER] = None  # units: NX_VOLUME
    atoms: dict[str, NXatom] = dc_field(default_factory=dict)
