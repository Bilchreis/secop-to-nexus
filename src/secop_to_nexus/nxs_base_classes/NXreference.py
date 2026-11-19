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
    ``field`` points at a dataset of the target group instead of the group.
    """

    target: NXobject
    field: str | None = None

    def resolve(self) -> str:
        path = self.target.get_path()
        return f"{path}/{self.field}" if self.field else path
