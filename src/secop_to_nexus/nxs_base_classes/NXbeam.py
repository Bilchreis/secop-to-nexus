"""Auto-generated from NXbeam.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXtransformations import NXtransformations


@dataclass
class NXbeam(NXobject):
    """Properties of the neutron or X-ray beam at a given location.

    This group is intended to be referenced
    by beamline component groups within the :ref:`NXinstrument` group or by the :ref:`NXsample` group. This group is
    especially valuable in storing the results of instrument simulations in which it is useful
    to specify the beam profile, time distribution etc. at each beamline component. Otherwise,
    its most likely use is in the :ref:`NXsample` group in which it defines the results of the neutron
    scattering by the sample, e.g., energy transfer, polarizations. Finally, There are cases where the beam is
    considered as a beamline component and this group may be defined as a subgroup directly inside
    :ref:`NXinstrument`, in which case it is recommended that the position of the beam is specified by an
    :ref:`NXtransformations` group, unless the beam is at the origin (which is the sample).

    Note that ``incident_wavelength``, ``incident_energy``, and related fields can be a scalar values or arrays, depending on the use case.
    To support these use cases, the explicit dimensionality of these fields is not specified, but it can be inferred
    by the presence of and shape of accompanying fields, such as incident_wavelength_weights for a polychromatic beam.
    """

    distance: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    incident_energy: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    incident_energy_spread: Optional[NX_NUMBER] = None  # units: NX_ENERGY
    incident_energy_weights: Optional[NX_NUMBER] = None  # units: NX_ENERGY
    final_energy: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    energy_transfer: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    incident_wavelength: Optional[NX_FLOAT] = None  # units: NX_WAVELENGTH
    incident_wavelength_weights: Optional[NX_FLOAT] = None
    incident_wavelength_spread: Optional[NX_FLOAT] = None  # units: NX_WAVELENGTH
    incident_beam_divergence: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    extent: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    final_wavelength: Optional[NX_FLOAT] = None  # units: NX_WAVELENGTH
    incident_polarization: Optional[NX_NUMBER] = None  # units: NX_ANY
    final_polarization: Optional[NX_NUMBER] = None  # units: NX_ANY
    incident_polarization_stokes: Optional[NX_NUMBER] = None  # units: NX_ANY
    final_polarization_stokes: Optional[NX_NUMBER] = None  # units: NX_ANY
    final_wavelength_spread: Optional[NX_FLOAT] = None  # units: NX_WAVELENGTH
    final_beam_divergence: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    flux: Optional[NX_FLOAT] = None  # units: NX_FLUX
    pulse_energy: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    average_power: Optional[NX_FLOAT] = None  # units: NX_POWER
    fluence: Optional[NX_FLOAT] = None  # units: mJ/cm^2
    pulse_duration: Optional[NX_FLOAT] = None  # units: NX_TIME
    pulse_delay: Optional[NX_FLOAT] = None  # units: NX_TIME
    frog_trace: Optional[NX_FLOAT] = None
    frog_delays: Optional[NX_FLOAT] = None  # units: NX_TIME
    frog_frequencies: Optional[NX_FLOAT] = None  # units: NX_FREQUENCY
    chirp_type: Optional[NX_CHAR] = None
    chirp_GDD: Optional[NX_FLOAT] = None  # units: NX_TIME
    depends_on: Optional[NX_CHAR] = None
    data: dict[str, NXdata] = dc_field(
        default_factory=dict
    )  # Distribution of beam with respect to relevant variable e.g. wavelength. This is mainly
    transformations: dict[str, NXtransformations] = dc_field(
        default_factory=dict
    )  # Direction (and location) for the beam. The location of the beam can be given by
