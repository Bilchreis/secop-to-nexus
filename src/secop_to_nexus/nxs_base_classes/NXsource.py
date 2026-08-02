"""Auto-generated from NXsource.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_FLOAT,
    NX_INT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXaperture import NXaperture
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXdeflector import NXdeflector
    from secop_to_nexus.nxs_base_classes.NXelectromagnetic_lens import (
        NXelectromagnetic_lens,
    )
    from secop_to_nexus.nxs_base_classes.NXfabrication import NXfabrication
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXnote import NXnote
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry


@dataclass
class NXsource(NXcomponent):
    """Radiation source emitting a beam.

    Examples include particle sources (electrons, neutrons, protons) or sources for electromagnetic radiation (photons).
    This base class can also be used to describe neutron or x-ray storage ring/facilities.
    """

    distance: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    name: Optional[NX_CHAR] = None
    type: Optional[NX_CHAR] = (
        None  # enum: Spallation Neutron Source | Pulsed Reactor Neutron ...
    )
    probe: Optional[NX_CHAR] = (
        None  # enum: neutron | photon | x-ray | muon | electron | ultrav...
    )
    power: Optional[NX_FLOAT] = None  # units: NX_POWER
    emittance_x: Optional[NX_FLOAT] = None  # units: NX_EMITTANCE
    emittance_y: Optional[NX_FLOAT] = None  # units: NX_EMITTANCE
    sigma_x: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    sigma_y: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    flux: Optional[NX_FLOAT] = None  # units: NX_FLUX
    energy: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    current: Optional[NX_FLOAT] = None  # units: NX_CURRENT
    voltage: Optional[NX_FLOAT] = None  # units: NX_VOLTAGE
    frequency: Optional[NX_FLOAT] = None  # units: NX_FREQUENCY
    period: Optional[NX_FLOAT] = None  # units: NX_PERIOD
    target_material: Optional[NX_CHAR] = (
        None  # enum: Ta | W | depleted_U | enriched_U | Hg | Pb | C
    )
    number_of_bunches: Optional[NX_INT] = None
    bunch_length: Optional[NX_FLOAT] = None  # units: NX_TIME
    bunch_distance: Optional[NX_FLOAT] = None  # units: NX_TIME
    pulse_width: Optional[NX_FLOAT] = None  # units: NX_TIME
    mode: Optional[NX_CHAR] = None  # enum: Single Bunch | Multi Bunch
    top_up: Optional[NX_BOOLEAN] = None
    last_fill: Optional[NX_NUMBER] = None  # units: NX_CURRENT
    wavelength: Optional[NX_FLOAT] = None  # units: NX_WAVELENGTH
    pulse_energy: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    peak_power: Optional[NX_FLOAT] = None  # units: NX_POWER
    anode_material: Optional[NX_CHAR] = None
    filament_current: Optional[NX_FLOAT] = None  # units: NX_CURRENT
    emission_current: Optional[NX_FLOAT] = None  # units: NX_CURRENT
    gas_pressure: Optional[NX_FLOAT] = None  # units: NX_PRESSURE
    previous_source: Optional[NX_CHAR] = None
    depends_on: Optional[NX_CHAR] = None
    notes: Optional[NXnote] = None  # any source/facility related messages/events that
    bunch_pattern: Optional[NXdata] = (
        None  # For storage rings, description of the bunch pattern.
    )
    pulse_shape: Optional[NXdata] = None  # source pulse shape
    geometry: Optional[NXgeometry] = None  # "Engineering" location of source.
    apertures: dict[str, NXaperture] = dc_field(
        default_factory=dict
    )  # The size and position of an aperture inside the source.
    electromagnetic_lenses: dict[str, NXelectromagnetic_lens] = dc_field(
        default_factory=dict
    )  # Individual electromagnetic lenses inside the source.
    deflectors: dict[str, NXdeflector] = dc_field(
        default_factory=dict
    )  # Deflectors inside the source.
    fabrications: dict[str, NXfabrication] = dc_field(default_factory=dict)
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the beam line component
    distribution: Optional[NXdata] = (
        None  # The wavelength or energy distribution of the source
    )
