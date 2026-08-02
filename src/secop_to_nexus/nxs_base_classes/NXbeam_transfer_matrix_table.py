"""Auto-generated from NXbeam_transfer_matrix_table.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXbeam_transfer_matrix_table(NXobject):
    """Contains data structures of an experimental optical setup (i.e., multiple
    transfer matrix tables).   These data structures are used to relate physical
    properties of two beams (NXbeam) which have one common optical component
    (NXcomponent) (one specific transfer matrix).
    One of these beams is an input beam and the other one is an output beam.

    The data describes the change of beam properties, e.g. the intensity of a
    beam is reduced because the transmission coefficient of the beam device is
    lower than 1.
    """

    datatype_N: dict[str, NX_CHAR] = dc_field(
        default_factory=dict
    )  # nameType: partial; enum: aperture | focal length | orientation | jones matrix
    matrix_elements: Optional[NX_CHAR] = None
    TRANSFER_MATRIX: dict[str, NX_NUMBER] = dc_field(
        default_factory=dict
    )  # nameType: any
