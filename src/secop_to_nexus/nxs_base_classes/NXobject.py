from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from secop_to_nexus.nxs_base_classes.NXdtypes import NX_CHAR
from secop_to_nexus.nxs_base_classes.NXreference import NXreference as NXref


@dataclass
class NXobject:
    default: Optional[NXref] = None
    title: Optional[NX_CHAR] = None
    parent: NXobject = field(default=None, init=False, repr=False)
    _name: Optional[str] = field(default=None, init=False, repr=False)

    def finalize(self) -> None:
        """Walk the object tree and wire up parent/_name on all NXobject children."""
        for attr, value in vars(self).items():
            if isinstance(value, NXobject) and attr not in ("parent",):
                value._name = attr
                value.parent = self
                value.finalize()

    def get_path(self) -> str:
        name = self._name or self.__class__.__name__.lower()
        if self.parent is None:
            return f"/{name}"
        return f"{self.parent.get_path()}/{name}"
