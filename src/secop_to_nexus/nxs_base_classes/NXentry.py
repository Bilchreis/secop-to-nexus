from dataclasses import dataclass
from typing import Optional

from secop_to_nexus.nxs_base_classes.NXdtypes import NX_CHAR
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXEntry(NXobject):
    description: Optional[NX_CHAR] = None
