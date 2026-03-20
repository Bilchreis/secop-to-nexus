from dataclasses import dataclass
from typing import Any, TypeAlias

import numpy as np

NXCharValue: TypeAlias = str | list["NXCharValue"]
NXBooleanValue: TypeAlias = bool | list["NXBooleanValue"]
NXFloatValue: TypeAlias = float | list["NXFloatValue"]
NXIntValue: TypeAlias = int | list["NXIntValue"]


class NXdtype:

    value: Any

    def is_array(self) -> str:
        if isinstance(self.value, (list, tuple, np.ndarray)):
            return "[]"
        return ""


@dataclass
class NX_CHAR(NXdtype):
    value: NXCharValue

    def __call__(self) -> dict[str, Any]:
        return {
            "@dtype": f"NX_CHAR{self.is_array()}",
            "@value": self.value,
        }


@dataclass
class NX_BOOLEAN(NXdtype):
    value: NXBooleanValue

    def __call__(self) -> dict[str, Any]:
        return {"@dtype": f"NX_BOOLEAN{self.is_array()}", "@value": self.value}


@dataclass
class NX_FLOAT(NXdtype):
    value: NXFloatValue

    def __call__(self) -> dict[str, Any]:
        return {"@dtype": f"NX_FLOAT64{self.is_array()}", "@value": self.value}


@dataclass
class NX_INT(NXdtype):
    value: NXIntValue

    def __call__(self) -> dict[str, Any]:
        return {"@dtype": f"NX_INT64{self.is_array()}", "@value": self.value}
