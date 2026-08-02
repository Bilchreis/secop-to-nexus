"""Auto-generated from NXapm_measurement.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXapm_event_data import NXapm_event_data
    from secop_to_nexus.nxs_base_classes.NXapm_instrument import NXapm_instrument


@dataclass
class NXapm_measurement(NXobject):
    """Base class for collecting a run with a real or a simulated atom probe or field-ion microscope.

    The term run is understood as an exact synonym for session, i.e. the usage of a real or simulated
    tomograph or microscope for a certain amount of time during which one characterizes a single specimen.

    Research workflows for experiments and simulations of atom probe and related field-evaporation
    evolve continuously and become increasingly connected with other methods used for material
    characterization specifically electron microscopy. A few examples in this direction are:

    * `T. Kelly et al. <https://doi.org/10.1017/S1431927620022205>`_
    * `C. Fleischmann et al. <https://doi.org/10.1016/j.ultramic.2018.08.010>`_
    * `W. Windl et al. <https://doi.org/10.1093/micmic/ozad067.294>`_
    * `C. Freysoldt et al. <https://doi.org/10.1103/PhysRevLett.124.176801>`_
    * `G. da Costa et al. <https://doi.org/10.1038/s41467-024-54169-2>`_

    The majority of atom probe research is performed using the so-called Local Electrode Atom Probe (LEAP) instruments
    from AMETEK/Cameca. In addition, several research groups have built their own instruments and shared different
    aspects of the technical specifications and approaches including how these groups apply data processing e.g.:

    * `M. Monajem et al. <https://doi.org/10.1017/S1431927622003397>`_
    * `P. Stender et al. <https://doi.org/10.1017/S1431927621013982>`_
    * `I. Dimkou et al. <https://doi.org/10.1093/micmic/ozac051>`_

    to name but a few.
    """

    status: Optional[NX_CHAR] = None  # enum: success | aborted
    quality: Optional[NX_CHAR] = None
    apm_instruments: dict[str, NXapm_instrument] = dc_field(default_factory=dict)
    apm_event_data: dict[str, NXapm_event_data] = dc_field(default_factory=dict)
