from dataclasses import dataclass
from typing import Optional

from secop_to_nexus.nxs_base_classes.NXdtypes import NX_CHAR
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXuser(NXobject):
    name: Optional[NX_CHAR] = None
    role: Optional[NX_CHAR] = None
    affiliation: Optional[NX_CHAR] = None
    address: Optional[NX_CHAR] = None
    telephone_number: Optional[NX_CHAR] = None
    fax_number: Optional[NX_CHAR] = None
    email: Optional[NX_CHAR] = None
    facility_user_id: Optional[NX_CHAR] = None
    ORCID: Optional[NX_CHAR] = None
