"""Auto-generated from NXuser.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXuser(NXobject):
    """Contact information for a user.

    The format allows more
    than one user with the same affiliation and contact information,
    but a second :ref:`NXuser` group should be used if they have different
    affiliations, etc.
    """

    name: Optional[NX_CHAR] = None
    role: Optional[NX_CHAR] = None
    affiliation: Optional[NX_CHAR] = None
    address: Optional[NX_CHAR] = None
    telephone_number: Optional[NX_CHAR] = None
    fax_number: Optional[NX_CHAR] = None
    email: Optional[NX_CHAR] = None
    facility_user_id: Optional[NX_CHAR] = None
    ORCID: Optional[NX_CHAR] = None
