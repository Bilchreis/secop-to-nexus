from dataclasses import dataclass
from typing import Optional

from src.nxs_base_classes.NXdtypes import NX_CHAR


@dataclass
class NXEntry:
    # default: Optional[NXref] = None
    description: Optional[NX_CHAR] = None
    title: Optional[NX_CHAR] = None
