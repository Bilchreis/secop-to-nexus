"""Auto-generated from NXapm_ranging.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXnote import NXnote
    from secop_to_nexus.nxs_base_classes.NXprogram import NXprogram


@dataclass
class NXapm_ranging(NXprocess):
    """Base class for the configuration and results of ranging definitions.

    Ranging is a data post-processing step used in the research field of
    atom probe during which elemental, isotopic, and/or molecular identities
    are assigned to mass-to-charge-state ratios within certain intervals.
    The documentation of these steps is based on ideas that
    have been described in the literature:

    * `M. K. Miller <https://doi.org/10.1002/sia.1719>`_
    * `D. Haley et al. <https://doi.org/10.1017/S1431927620024290>`_
    * `M. Kühbach et al. <https://doi.org/10.1017/S1431927621012241>`_
    """

    programs: dict[str, NXprogram] = dc_field(default_factory=dict)
    notes: dict[str, NXnote] = dc_field(default_factory=dict)
    mass_to_charge_distribution: Optional[NXprocess] = (
        None  # Specifies the mass-to-charge-state ratio histogram.
    )
    background_quantification: Optional[NXprocess] = (
        None  # Details of the background model that was used to
    )
    peak_search_and_deconvolution: Optional[NXprocess] = (
        None  # How were peaks in the mass-to-charge-state ratio histogram identified.
    )
    peak_identification: Optional[NXprocess] = (
        None  # Details about how peaks, with taking into account
    )
