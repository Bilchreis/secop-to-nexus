"""Auto-generated from NXmoderator.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_FLOAT,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXlog import NXlog
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry


@dataclass
class NXmoderator(NXcomponent):
    """A neutron moderator"""

    distance: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    type: Optional[NX_CHAR] = (
        None  # enum: H20 | D20 | Liquid H2 | Liquid CH4 | Liquid D2 | So...
    )
    poison_depth: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    coupled: Optional[NX_BOOLEAN] = None
    coupling_material: Optional[NX_CHAR] = None
    poison_material: Optional[NX_CHAR] = None  # enum: Gd | Cd
    temperature: Optional[NX_FLOAT] = None  # units: NX_TEMPERATURE
    depends_on: Optional[NX_CHAR] = None
    geometries: dict[str, NXgeometry] = dc_field(
        default_factory=dict
    )  # "Engineering" position of moderator
    temperature_log: Optional[NXlog] = None  # log file of moderator temperature
    pulse_shape: Optional[NXdata] = None  # moderator pulse shape
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the moderator
