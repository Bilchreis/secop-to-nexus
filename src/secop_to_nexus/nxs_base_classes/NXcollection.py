"""Auto-generated from NXcollection.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXcollection(NXobject):
    """An unvalidated set of terms, such as the description of a beam line.

    Use :ref:`NXcollection` to gather together any set of terms.
    The original suggestion is to use this as a container
    class for the description of a beamline.

    For NeXus validation, :ref:`NXcollection` will always generate
    a warning since it is always an optional group.
    Anything (groups, fields, or attributes) placed in
    an :ref:`NXcollection` group will not be validated.

    .. admonition:: NXcollection content is not validated.

       :ref:`NXcollection` is and will always be for unvalidated content.

       Any and all content within a :ref:`NXcollection` group specified by
       an application definition cannot be validated.

       It is suggested to use a :ref:`NXparameters` group for similar
       content which should be validated.
    """
