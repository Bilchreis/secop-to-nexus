"""Auto-generated from NXspindispersion.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
    from secop_to_nexus.nxs_base_classes.NXdeflector import NXdeflector
    from secop_to_nexus.nxs_base_classes.NXelectromagnetic_lens import (
        NXelectromagnetic_lens,
    )
    from secop_to_nexus.nxs_base_classes.NXhistory import NXhistory


@dataclass
class NXspindispersion(NXcomponent):
    """Class to describe spin filters in photoemission experiments."""

    type: Optional[NX_CHAR] = None
    figure_of_merit: Optional[NX_FLOAT] = None  # units: NX_DIMENSIONLESS
    shermann_function: Optional[NX_FLOAT] = None  # units: NX_DIMENSIONLESS
    scattering_energy: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    scattering_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    scattering_target: Optional[NX_CHAR] = None
    scattering_target_history: Optional[NXhistory] = (
        None  # A set of activities that occurred to the ``scattering_target`` prior to/during the.
    )
    deflectors: dict[str, NXdeflector] = dc_field(
        default_factory=dict
    )  # Deflectors in the spin dispersive section
    electromagnetic_lenses: dict[str, NXelectromagnetic_lens] = dc_field(
        default_factory=dict
    )  # Individual lenses in the spin dispersive section
