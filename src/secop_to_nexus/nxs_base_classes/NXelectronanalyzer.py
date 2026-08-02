"""Auto-generated from NXelectronanalyzer.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

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
    from secop_to_nexus.nxs_base_classes.NXcollectioncolumn import NXcollectioncolumn
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXdeflector import NXdeflector
    from secop_to_nexus.nxs_base_classes.NXdetector import NXdetector
    from secop_to_nexus.nxs_base_classes.NXelectromagnetic_lens import (
        NXelectromagnetic_lens,
    )
    from secop_to_nexus.nxs_base_classes.NXenergydispersion import NXenergydispersion
    from secop_to_nexus.nxs_base_classes.NXfabrication import NXfabrication
    from secop_to_nexus.nxs_base_classes.NXresolution import NXresolution
    from secop_to_nexus.nxs_base_classes.NXspindispersion import NXspindispersion


@dataclass
class NXelectronanalyzer(NXcomponent):
    """Basic class for describing an electron analyzer.

    This concept is related to term `12.59`_ of the ISO 18115-1:2023 standard.

    .. _12.59: https://www.iso.org/obp/ui/en/#iso:std:iso:18115:-1:ed-3:v1:en:term:12.59
    """

    description: Optional[NX_CHAR] = None
    name: Optional[NX_CHAR] = None
    work_function: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    voltage_range: Optional[NX_FLOAT] = None  # units: NX_VOLTAGE
    fast_axes: Optional[NX_CHAR] = None
    slow_axes: Optional[NX_CHAR] = None
    energy_resolution: Optional[NXresolution] = (
        None  # Energy resolution of the analyzer with the current setting. May be linked from an
    )
    momentum_resolution: Optional[NXresolution] = (
        None  # Momentum resolution of the electron analyzer (FWHM)
    )
    angular_resolution: Optional[NXresolution] = (
        None  # Angular resolution of the electron analyzer (FWHM)
    )
    spatial_resolution: Optional[NXresolution] = (
        None  # Spatial resolution of the electron analyzer (Airy disk radius)
    )
    transmission_function: Optional[NXdata] = (
        None  # Transmission function of the electron analyzer.
    )
    collectioncolumns: dict[str, NXcollectioncolumn] = dc_field(
        default_factory=dict
    )  # Describes the electron collection (spatial and momentum imaging) column
    energydispersions: dict[str, NXenergydispersion] = dc_field(
        default_factory=dict
    )  # Describes the energy dispersion section
    spindispersions: dict[str, NXspindispersion] = dc_field(
        default_factory=dict
    )  # Describes the spin dispersion section
    detectors: dict[str, NXdetector] = dc_field(
        default_factory=dict
    )  # Describes the electron detector
    deflectors: dict[str, NXdeflector] = dc_field(
        default_factory=dict
    )  # Deflectors outside the main optics ensembles described by the subclasses
    electromagnetic_lenses: dict[str, NXelectromagnetic_lens] = dc_field(
        default_factory=dict
    )  # Individual lenses outside the main optics ensembles described by the subclasses
    fabrications: dict[str, NXfabrication] = dc_field(default_factory=dict)
    resolutions: dict[str, NXresolution] = dc_field(
        default_factory=dict
    )  # Any other resolution not explicitly named in this base class.
