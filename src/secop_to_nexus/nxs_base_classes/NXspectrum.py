"""Auto-generated from NXspectrum.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess


@dataclass
class NXspectrum(NXobject):
    """Base class container for reporting a set of spectra.

    The mostly commonly used scanning methods are supported. That is one-,
    two-, three-dimensional ROIs discretized using regular Euclidean tilings.

    Use stack for all other tilings.
    """

    processes: dict[str, NXprocess] = dc_field(
        default_factory=dict
    )  # Details how spectra were processed from the detector readings.
    spectrum_0d: Optional[NXdata] = (
        None  # One spectrum for a point of a 0d ROI. Also known as spot measurement.
    )
    spectrum_1d: Optional[NXdata] = None  # One spectrum for each point of a 1d ROI.
    spectrum_2d: Optional[NXdata] = None  # One spectrum for each scan point of 2d ROI.
    spectrum_3d: Optional[NXdata] = None  # One spectrum for point of a 3d ROI.
    stack_0d: Optional[NXdata] = None  # Multiple instances of spectrum_0d.
    stack_2d: Optional[NXdata] = None  # Multiple instances of spectrum_2d.
    stack_3d: Optional[NXdata] = None  # Multiple instances of spectrum_3d.
