from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, ClassVar, TypeAlias

import numpy as np


class Placeholder(str):
    """Name of a NexusCreator library key whose value is injected later.

    Numeric datasets serialize the bare key name; string datasets serialize
    ``${key}`` because NexusCreator's injector never resolves bare names
    inside NX_CHAR datasets.
    """

    __slots__ = ()


NXCharValue: TypeAlias = str | list["NXCharValue"]
NXBooleanValue: TypeAlias = bool | list["NXBooleanValue"]
NXFloatValue: TypeAlias = float | list["NXFloatValue"]
NXIntValue: TypeAlias = int | list["NXIntValue"]


@dataclass
class NXdtype:
    value: Any = None
    units: str | None = None
    # extra dataset attributes, written as @key: value
    attrs: dict[str, Any] = field(default_factory=dict)
    # array-ness cannot be inferred when value is a Placeholder; set explicitly
    array: bool | None = None

    # "@dtype" token understood by NexusCreator's HDF5 writer
    nx_dtype: ClassVar[str] = ""
    # string-typed datasets need ${...} placeholder syntax (see Placeholder)
    is_char: ClassVar[bool] = False

    def is_array(self) -> bool:
        if self.array is not None:
            return self.array
        return isinstance(self.value, (list, tuple, np.ndarray))

    def serialized_value(self) -> Any:
        if isinstance(self.value, Placeholder):
            return f"${{{self.value}}}" if self.is_char else str(self.value)
        return self.value

    def to_dict(self) -> dict[str, Any]:
        if self.value is None:
            raise ValueError(f"{type(self).__name__} has no value or Placeholder set")
        d: dict[str, Any] = {
            "@dtype": f"{self.nx_dtype}{'[]' if self.is_array() else ''}",
            "@value": self.serialized_value(),
        }
        if self.units is not None:
            d["@units"] = self.units
        for key, val in self.attrs.items():
            d[f"@{key.lstrip('@')}"] = val
        return d


@dataclass
class NX_CHAR(NXdtype):
    value: NXCharValue | Placeholder | None = None
    nx_dtype = "NX_CHAR"
    is_char = True


@dataclass
class NX_BOOLEAN(NXdtype):
    value: NXBooleanValue | Placeholder | None = None
    nx_dtype = "NX_BOOLEAN"


@dataclass
class NX_FLOAT(NXdtype):
    value: NXFloatValue | Placeholder | None = None
    nx_dtype = "NX_FLOAT64"


@dataclass
class NX_INT(NXdtype):
    value: NXIntValue | Placeholder | None = None
    nx_dtype = "NX_INT64"


@dataclass
class NX_UINT(NXdtype):
    value: NXIntValue | Placeholder | None = None
    nx_dtype = "NX_UINT64"


@dataclass
class NX_POSINT(NXdtype):
    value: NXIntValue | Placeholder | None = None
    nx_dtype = "NX_UINT64"


@dataclass
class NX_COMPLEX(NXdtype):
    # NexusCreator's writer has no complex dtype; it falls back to a string dataset
    value: Any = None
    nx_dtype = "NX_COMPLEX"


@dataclass
class NX_BINARY(NXdtype):
    # NexusCreator's writer has no binary dtype; it falls back to a string dataset
    value: Any = None
    nx_dtype = "NX_BINARY"


@dataclass
class NX_DATE_TIME(NXdtype):
    # Written as an ISO8601 NX_CHAR dataset; naive datetimes get the local offset
    value: datetime | str | Placeholder | None = None
    nx_dtype = "NX_CHAR"
    is_char = True

    def serialized_value(self) -> Any:
        if isinstance(self.value, datetime):
            dt = self.value
            if dt.tzinfo is None:
                dt = dt.astimezone()
            return dt.isoformat()
        return super().serialized_value()


# Generic numeric type
NX_NUMBER: TypeAlias = NX_INT | NX_UINT | NX_POSINT | NX_FLOAT
NX_CHAR_OR_NUMBER: TypeAlias = NX_CHAR | NX_INT | NX_UINT | NX_POSINT | NX_FLOAT
