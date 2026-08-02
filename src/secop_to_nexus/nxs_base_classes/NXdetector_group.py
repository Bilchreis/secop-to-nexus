"""Auto-generated from NXdetector_group.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_INT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXdetector_group(NXobject):
    """Logical grouping of detectors. When used, describes a group of detectors.

    Each detector is represented as an NXdetector
    with its own detector data array.  Each detector data array
    may be further decomposed into array sections by use of
    NXdetector_module groups.  Detectors can be grouped logically
    together using NXdetector_group. Groups can be further grouped
    hierarchically in a single NXdetector_group (for example, if
    there are multiple detectors at an endstation or multiple
    endstations at a facility).  Alternatively, multiple
    NXdetector_groups can be provided.

    The groups are defined hierarchically, with names given
    in the group_names field, unique identifying indices given
    in the field group_index, and the level in the hierarchy
    given in the group_parent field.  For example if an x-ray
    detector group, DET, consists of four detectors in a
    rectangular array::

                 DTL	DTR
                 DLL	DLR

    We could have::

        group_names: ["DET", "DTL", "DTR", "DLL", "DLR"]
        group_index: [1, 2, 3, 4, 5]
        group_parent:  [-1, 1, 1, 1, 1]
    """

    group_names: Optional[NX_CHAR] = None
    group_index: Optional[NX_INT] = None
    group_parent: Optional[NX_INT] = None
    group_type: Optional[NX_INT] = None
