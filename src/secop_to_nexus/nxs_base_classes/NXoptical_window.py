"""Auto-generated from NXoptical_window.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_FLOAT,
)
from secop_to_nexus.nxs_base_classes.NXaperture import NXaperture

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess


@dataclass
class NXoptical_window(NXaperture):
    """A window of a cryostat, heater, vacuum chamber or a simple glass slide.

    This describes cryostat windows and other possible influences for ellipsometry
    measurements.

    For environmental measurements, the environment (liquid, vapor
    etc.) is enclosed in a cell, which has windows both in the
    direction of the source (entry window) and the detector (exit
    window) (looking from the sample).

    The windows also add a phase shift to the light altering the
    measured signal. This shift has to be corrected based on measuring
    a known sample (reference sample) or the actual sample of interest
    in the environmental cell. State if a window correction has been
    performed in 'window_effects_corrected'. Reference measurements should be
    considered as a separate experiment (with a separate NeXus file), and
    the reference data shall be :ref:`linked <Design-Links>` in
    ``reference_data_link``.

    The window is considered to be a part of the sample stage but also
    beam path. Hence, its position within the beam path should be
    defined by the 'depends_on' field.
    """

    window_effects_corrected: Optional[NX_BOOLEAN] = None
    window_effects_type: Optional[NX_CHAR] = (
        None  # enum: interference effects | light absorption | light sca...
    )
    material: Optional[NX_CHAR] = (
        None  # enum: quartz | diamond | calcium fluoride | zinc selenide...
    )
    material_other: Optional[NX_CHAR] = None
    thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    orientation_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    window_correction: Optional[NXprocess] = (
        None  # Group to describe any window correction - if none performed, then omit this
    )
