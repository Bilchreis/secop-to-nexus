"""Convert recorded SECoP values into NeXus dataset columns, driven by datainfo.

frappy's ``get_datatype`` parses (and validates) the datainfo; the class of the
resulting datatype decides how a column of values is stored:

========================  ==========================================
SECoP type                NeXus dataset
========================  ==========================================
double, scaled            NX_FLOAT (scaled values multiplied by scale)
int, enum                 NX_INT (enum gets a ``secop_enum`` attribute)
bool                      NX_BOOLEAN
string, blob              NX_CHAR (blob stays base64 as transported)
array of numbers/bools    2D NX_FLOAT/NX_INT/NX_BOOLEAN (one row per
                          timestamp); ragged arrays fall back to JSON
array of anything else,   NX_CHAR, one JSON string per timestamp
tuple, struct
========================  ==========================================

Values are expected in SECoP wire format (as JSON-decoded from the data
report), so scaled integers are converted to physical values here — also
inside tuples, structs and arrays before they are JSON-encoded.
"""

from __future__ import annotations

import json
import logging
from collections.abc import Sequence
from typing import Any

import numpy as np
from frappy.datatypes import (
    ArrayOf,
    BLOBType,
    BoolType,
    DataType,
    EnumType,
    FloatRange,
    IntRange,
    ScaledInteger,
    StringType,
    StructOf,
    TupleOf,
    get_datatype,
)

from secop_to_nexus.nxs_base_classes.NXdtypes import (
    NX_BOOLEAN,
    NX_CHAR,
    NX_FLOAT,
    NX_INT,
    NXdtype,
)

log = logging.getLogger(__name__)

_NUMERIC = (FloatRange, ScaledInteger, IntRange, EnumType, BoolType)


def parse_datainfo(datainfo: dict[str, Any], name: str = "") -> DataType | None:
    """frappy datatype for ``datainfo``, or None if frappy cannot parse it
    (e.g. a type newer than the installed frappy); such values become JSON."""
    try:
        return get_datatype(datainfo, name)
    except Exception as exc:  # frappy raises several error types here
        log.warning("cannot parse datainfo of %r (%s), storing JSON", name, exc)
        return None


def to_physical(dt: DataType | None, value: Any) -> Any:
    """Wire value -> JSON-compatible physical value (scaled ints become floats)."""
    if value is None or dt is None:
        return value
    if isinstance(dt, ScaledInteger):
        return value * dt.scale
    if isinstance(dt, ArrayOf):
        return [to_physical(dt.members, v) for v in value]
    if isinstance(dt, TupleOf):
        return [to_physical(m, v) for m, v in zip(dt.members, value)]
    if isinstance(dt, StructOf):
        return {k: to_physical(dt.members.get(k), v) for k, v in value.items()}
    return value


def _unit(dt: DataType | None) -> str | None:
    unit = getattr(dt, "unit", None) if dt is not None else None
    return unit or None


def _nx_class_for_scalar(dt: DataType) -> tuple[type[NXdtype], Any]:
    if isinstance(dt, (FloatRange, ScaledInteger)):
        return NX_FLOAT, np.float64
    if isinstance(dt, BoolType):
        return NX_BOOLEAN, np.bool_
    return NX_INT, np.int64  # IntRange, EnumType


def _as_array(values: Sequence[Any], np_type: Any) -> np.ndarray | None:
    """numpy array of ``values``, or None if they don't fit ``np_type`` or are
    ragged (arrays of different length); the caller then falls back to JSON."""
    try:
        return np.asarray(values, dtype=np_type)
    except (ValueError, TypeError):
        log.warning("values are ragged or do not match their datainfo, storing JSON")
        return None


def column(
    dt: DataType | None, values: Sequence[Any], datainfo: dict[str, Any]
) -> NXdtype:
    """Build the NeXus dataset holding ``values`` (one entry per timestamp)."""
    attrs: dict[str, Any] = {"secop_datainfo": json.dumps(datainfo)}
    members = dt.members if isinstance(dt, ArrayOf) else None

    if isinstance(dt, _NUMERIC):
        nx_cls, np_type = _nx_class_for_scalar(dt)
        arr = _as_array(values, np_type)
        if arr is not None and arr.ndim == 1:
            if isinstance(dt, ScaledInteger):
                arr = arr * dt.scale
            if isinstance(dt, EnumType):
                attrs["secop_enum"] = json.dumps(datainfo.get("members", {}))
            return nx_cls(arr, units=_unit(dt), attrs=attrs, array=True)

    if isinstance(members, _NUMERIC):
        nx_cls, np_type = _nx_class_for_scalar(members)
        arr = _as_array(values, np_type)
        if arr is not None and arr.ndim == 2:
            if isinstance(members, ScaledInteger):
                arr = arr * members.scale
            if isinstance(members, EnumType):
                attrs["secop_enum"] = json.dumps(
                    datainfo.get("members", {}).get("members", {})
                )
            return nx_cls(arr, units=_unit(members), attrs=attrs, array=True)

    if isinstance(dt, (StringType, BLOBType)):
        return NX_CHAR([str(v) for v in values], attrs=attrs, array=True)

    # tuple, struct, non-numeric or ragged arrays, unparseable datainfo
    attrs["secop_encoding"] = "json"
    return NX_CHAR(
        [json.dumps(to_physical(dt, v)) for v in values],
        units=_unit(members) or _unit(dt),
        attrs=attrs,
        array=True,
    )


def is_status(dt: DataType | None) -> bool:
    """SECoP status: tuple(enum code, string message)."""
    return (
        isinstance(dt, TupleOf)
        and len(dt.members) == 2
        and isinstance(dt.members[0], EnumType)
        and isinstance(dt.members[1], StringType)
    )
