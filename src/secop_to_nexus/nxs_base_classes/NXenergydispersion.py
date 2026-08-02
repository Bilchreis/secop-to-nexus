"""Auto-generated from NXenergydispersion.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
    from secop_to_nexus.nxs_base_classes.NXfabrication import NXfabrication


@dataclass
class NXenergydispersion(NXcomponent):
    """Energy dispersion section of an electron analyzer."""

    scheme: Optional[NX_CHAR] = None
    pass_energy: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    kinetic_energy: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    drift_energy: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    center_energy: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    energy_interval: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    diameter: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    radius: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    energy_scan_mode: Optional[NX_CHAR] = (
        None  # enum: fixed_analyzer_transmission | fixed_retardation_rat...
    )
    tof_distance: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    apertures: dict[str, NXaperture] = dc_field(
        default_factory=dict
    )  # Size, position and shape of a slit in dispersive analyzer, e.g. entrance and
    deflectors: dict[str, NXdeflector] = dc_field(
        default_factory=dict
    )  # Deflectors in the energy dispersive section
    electromagnetic_lenses: dict[str, NXelectromagnetic_lens] = dc_field(
        default_factory=dict
    )  # Individual lenses in the energy dispersive section
    fabrications: dict[str, NXfabrication] = dc_field(default_factory=dict)
