"""Auto-generated from NXcollectioncolumn.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXaperture import NXaperture
    from secop_to_nexus.nxs_base_classes.NXdeflector import NXdeflector
    from secop_to_nexus.nxs_base_classes.NXelectromagnetic_lens import (
        NXelectromagnetic_lens,
    )


@dataclass
class NXcollectioncolumn(NXcomponent):
    """Electron collection column of an electron analyzer."""

    scheme: Optional[NX_CHAR] = None
    extractor_voltage: Optional[NX_FLOAT] = None  # units: NX_VOLTAGE
    extractor_current: Optional[NX_FLOAT] = None  # units: NX_CURRENT
    working_distance: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    lens_mode: Optional[NX_CHAR] = None
    projection: Optional[NX_CHAR] = None  # enum: real | reciprocal
    angular_acceptance: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    spatial_acceptance: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    magnification: Optional[NX_FLOAT] = None  # units: NX_DIMENSIONLESS
    apertures: dict[str, NXaperture] = dc_field(
        default_factory=dict
    )  # The size and position of an aperture inserted in the column, e.g. field aperture
    deflectors: dict[str, NXdeflector] = dc_field(
        default_factory=dict
    )  # Deflectors in the collection column section
    electromagnetic_lenses: dict[str, NXelectromagnetic_lens] = dc_field(
        default_factory=dict
    )  # Individual lenses in the collection column section
