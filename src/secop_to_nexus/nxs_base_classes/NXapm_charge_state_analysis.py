"""Auto-generated from NXapm_charge_state_analysis.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_FLOAT,
    NX_INT,
    NX_UINT,
)
from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXparameters import NXparameters


@dataclass
class NXapm_charge_state_analysis(NXprocess):
    """Base class to document the parameters, configuration, and results of a processing for recovering
    the charge state and nuclide composition of an ion from ranging definitions as used in the research
    field of atom probe microscopy.

    A ranging definition classically reports only the mass-to-charge-state-ratio interval plus the
    elemental composition, but not necessarily the nuclide that compose the ion.

    As the mass-resolving-power in an atom probe instrument is finite and typically lower
    than for cutting edge tandem mass spectrometry it is possible that different combinations of nuclides
    are indistinguishable and thus multiple ions in eventually even different charge states can be valid
    labels for a given mass-to-charge-state-ratio peak. Enumerating the possible combinations
    is a programmatic approach that can help with peak identification.
    """

    charge_state: Optional[NX_INT] = None  # units: NX_UNITLESS
    nuclide_hash: Optional[NX_UINT] = None  # units: NX_UNITLESS
    mass: Optional[NX_FLOAT] = None  # units: NX_MASS
    natural_abundance_product: Optional[NX_FLOAT] = None  # units: NX_DIMENSIONLESS
    shortest_half_life: Optional[NX_FLOAT] = None  # units: NX_TIME
    config: Optional[NXparameters] = (
        None  # Parameters for the algorithm used to recover which combinations of nuclides
    )
