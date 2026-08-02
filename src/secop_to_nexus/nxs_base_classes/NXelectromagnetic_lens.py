"""Auto-generated from NXelectromagnetic_lens.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_CHAR_OR_NUMBER,
    NX_NUMBER,
    NX_UINT,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent


@dataclass
class NXelectromagnetic_lens(NXcomponent):
    """Base class for an electro-magnetic lens or a compound lens.

    For :ref:`NXtransformations` the origin of the coordinate system is placed
    in the center of the lens its pole piece, pinhole, or another point of reference.
    The origin should be specified in the :ref:`NXtransformations`.

    For details of electro-magnetic lenses in the literature see e.g.

    * `L. Reimer: Scanning Electron Microscopy <https://doi.org/10.1007/978-3-540-38967-5>`_
    * `P. Hawkes: Magnetic Electron Lenses <https://link.springer.com/book/10.1007/978-3-642-81516-4>`_
    * `Y. Liao: Practical Electron Microscopy and Database <https://www.globalsino.com/EM/>`_
    """

    name: Optional[NX_CHAR] = None
    description: Optional[NX_CHAR] = None
    power_setting: Optional[NX_CHAR_OR_NUMBER] = None  # units: NX_ANY
    mode: Optional[NX_CHAR] = None
    voltage: Optional[NX_NUMBER] = None  # units: NX_VOLTAGE
    current: Optional[NX_NUMBER] = None  # units: NX_CURRENT
    type: Optional[NX_CHAR] = (
        None  # enum: single | double | quadrupole | hexapole | octupole ...
    )
    number_of_poles: Optional[NX_UINT] = None  # units: NX_UNITLESS
