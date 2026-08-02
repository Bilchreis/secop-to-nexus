"""Auto-generated from NXebeam_column.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXactuator import NXactuator
    from secop_to_nexus.nxs_base_classes.NXaperture import NXaperture
    from secop_to_nexus.nxs_base_classes.NXbeam import NXbeam
    from secop_to_nexus.nxs_base_classes.NXcorrector_cs import NXcorrector_cs
    from secop_to_nexus.nxs_base_classes.NXdeflector import NXdeflector
    from secop_to_nexus.nxs_base_classes.NXelectromagnetic_lens import (
        NXelectromagnetic_lens,
    )
    from secop_to_nexus.nxs_base_classes.NXmonochromator import NXmonochromator
    from secop_to_nexus.nxs_base_classes.NXscan_controller import NXscan_controller
    from secop_to_nexus.nxs_base_classes.NXsensor import NXsensor
    from secop_to_nexus.nxs_base_classes.NXsource import NXsource


@dataclass
class NXebeam_column(NXcomponent):
    """Base class for a set of components providing a controllable electron beam.

    The idea behind defining :ref:`NXebeam_column` as an own base class vs. adding these
    concepts in :ref:`NXem_instrument` is that the electron beam generating component
    might be worthwhile to use also in other types of experiments.
    """

    operation_mode: Optional[NX_CHAR] = None
    electron_source: Optional[NXsource] = (
        None  # A physical part of an electron or ion microscope from which
    )
    electromagnetic_lenses: dict[str, NXelectromagnetic_lens] = dc_field(
        default_factory=dict
    )
    apertures: dict[str, NXaperture] = dc_field(default_factory=dict)
    deflectors: dict[str, NXdeflector] = dc_field(default_factory=dict)
    blankerID: dict[str, NXdeflector] = dc_field(
        default_factory=dict
    )  # nameType: partial
    monochromators: dict[str, NXmonochromator] = dc_field(
        default_factory=dict
    )  # Device to improve energy resolution or chromatic aberration.
    corrector_cs: dict[str, NXcorrector_cs] = dc_field(default_factory=dict)
    corrector_ax: Optional[NXcomponent] = (
        None  # Component that reshapes an ellipse-shaped electron beam into a circular one.
    )
    biprismID: dict[str, NXcomponent] = dc_field(
        default_factory=dict
    )  # nameType: partial
    phaseplateID: dict[str, NXcomponent] = dc_field(
        default_factory=dict
    )  # nameType: partial
    sensors: dict[str, NXsensor] = dc_field(default_factory=dict)
    actuators: dict[str, NXactuator] = dc_field(default_factory=dict)
    beams: dict[str, NXbeam] = dc_field(
        default_factory=dict
    )  # Individual characterization results for the position, shape,
    components: dict[str, NXcomponent] = dc_field(default_factory=dict)
    scan_controller: Optional[NXscan_controller] = None
