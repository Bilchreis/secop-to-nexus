from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXreference:
    """Reference to another object in the same NeXus tree.

    Resolved to the target's absolute HDF5 path at serialization time, so
    ``finalize()`` must have been called on the tree root before serializing.
    """

    target: NXobject

    def resolve(self) -> str:
        return self.target.get_path()
