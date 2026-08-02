"""Auto-generated from NXmonochromator.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
    from secop_to_nexus.nxs_base_classes.NXcrystal import NXcrystal
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXgrating import NXgrating
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry
    from secop_to_nexus.nxs_base_classes.NXvelocity_selector import NXvelocity_selector


@dataclass
class NXmonochromator(NXcomponent):
    """A  wavelength defining device.

    This is a base class for everything which
    selects a wavelength or energy, be it a
    monochromator crystal, a velocity selector,
    an undulator or whatever.

    The expected units are:

    * wavelength: angstrom
    * energy:     eV
    """

    wavelength: Optional[NX_FLOAT] = None  # units: NX_WAVELENGTH
    wavelength_error: Optional[NX_FLOAT] = None  # units: NX_WAVELENGTH; deprecated
    wavelength_errors: Optional[NX_FLOAT] = None  # units: NX_WAVELENGTH
    energy: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    energy_error: Optional[NX_FLOAT] = None  # units: NX_ENERGY; deprecated
    energy_errors: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    energy_dispersion: Optional[NX_FLOAT] = None  # units: eV/mm
    wavelength_dispersion: Optional[NX_FLOAT] = None  # units: nm/mm
    depends_on: Optional[NX_CHAR] = None
    entrance_slit: Optional[NXaperture] = (
        None  # Size, position and shape of the entrance slit of the monochromator.
    )
    exit_slit: Optional[NXaperture] = (
        None  # Size, position and shape of the exit slit of the monochromator.
    )
    distribution: Optional[NXdata] = None
    geometry: Optional[NXgeometry] = None
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the beam line component
    crystals: dict[str, NXcrystal] = dc_field(
        default_factory=dict
    )  # Use as many crystals as necessary to describe
    velocity_selectors: dict[str, NXvelocity_selector] = dc_field(default_factory=dict)
    gratings: dict[str, NXgrating] = dc_field(
        default_factory=dict
    )  # For diffraction grating based monochromators
