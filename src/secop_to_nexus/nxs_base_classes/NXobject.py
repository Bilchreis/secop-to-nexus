from __future__ import annotations

import dataclasses
from dataclasses import dataclass, field
from typing import Any, Optional

from secop_to_nexus.nxs_base_classes.NXdtypes import NXdtype
from secop_to_nexus.nxs_base_classes.NXreference import NXreference

# bookkeeping fields that never appear in the NeXus output
_INTERNAL_FIELDS = ("parent", "_name")


@dataclass
class NXobject:
    """Base of all NeXus group classes.

    Per NXobject.nxdl.xml every group may carry a ``default`` attribute and
    arbitrarily named extra datasets/groups (FIELDNAME_set, GROUPNAME_log,
    NXcollection/NXdata/NXlog/NXnote/NXparameters children, ...) — model those
    via ``extra_fields`` / ``extra_groups`` with the HDF5 name as dict key.
    """

    # @default attribute: name of (or reference to) the default child to plot
    default: Optional[str | NXreference] = field(
        default=None, metadata={"kind": "attribute"}
    )
    # arbitrary additional datasets, key is the HDF5 dataset name
    extra_fields: dict[str, NXdtype] = field(default_factory=dict)
    # arbitrary additional child groups, key is the HDF5 group name
    extra_groups: dict[str, NXobject] = field(default_factory=dict)

    parent: Optional[NXobject] = field(default=None, init=False, repr=False)
    _name: Optional[str] = field(default=None, init=False, repr=False)

    def finalize(self) -> None:
        """Walk the object tree and wire up parent/_name on all NXobject children.

        Call this on the tree root before get_path()/NXreference resolution.
        """
        for f in dataclasses.fields(self):
            if f.name in _INTERNAL_FIELDS:
                continue
            value = getattr(self, f.name)
            if isinstance(value, NXobject):
                value._name = f.metadata.get("nx_name", f.name)
                value.parent = self
                value.finalize()
            elif isinstance(value, dict):
                for key, item in value.items():
                    if isinstance(item, NXobject):
                        item._name = key
                        item.parent = self
                        item.finalize()

    def get_path(self) -> str:
        """Absolute HDF5 path; the tree root corresponds to the file root ''."""
        if self.parent is None:
            return "" if self._name is None else f"/{self._name}"
        name = self._name or type(self).__name__.lower()
        return f"{self.parent.get_path()}/{name}"

    def to_nexus_dict(self) -> dict[str, Any]:
        """Serialize this group (and everything below it) to the nested dict
        format consumed by NexusCreator's NexusValueInjector/NexusHDF5Writer."""
        out: dict[str, Any] = {"@NX_class": type(self).__name__}
        for f in dataclasses.fields(self):
            if f.name in _INTERNAL_FIELDS:
                continue
            value = getattr(self, f.name)
            if value is None or (isinstance(value, dict) and not value):
                continue
            name = f.metadata.get("nx_name", f.name)
            if f.metadata.get("kind") == "attribute":
                if isinstance(value, dict):
                    # template attribute (nameType any/partial): key is the
                    # concrete attribute name
                    for key, item in value.items():
                        out[f"@{key}"] = self._serialize_attribute(item)
                else:
                    out[f"@{name}"] = self._serialize_attribute(value)
            else:
                self._serialize_child(out, name, value)
        return out

    @staticmethod
    def _serialize_attribute(value: Any) -> Any:
        if isinstance(value, NXreference):
            return value.resolve()
        if isinstance(value, NXdtype):
            return value.serialized_value()
        return value

    def _serialize_child(self, out: dict[str, Any], name: str, value: Any) -> None:
        if isinstance(value, NXobject):
            out[name] = value.to_nexus_dict()
        elif isinstance(value, NXdtype):
            out[name] = value.to_dict()
        elif isinstance(value, NXreference):
            # internal soft link to the referenced object
            out[name] = {"@link": value.resolve()}
        elif isinstance(value, dict):
            for key, item in value.items():
                self._serialize_child(out, key, item)
        else:
            raise TypeError(
                f"cannot serialize field {name!r} of {type(self).__name__}: "
                f"unexpected value type {type(value).__name__}"
            )
