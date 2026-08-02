"""Auto-generated from NXdetector_channel.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_FLOAT,
    NX_INT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXdetector_channel(NXobject):
    """Description and metadata for a single channel from a multi-channel detector.

    Given an :ref:`NXdata` group linked as part of an NXdetector group that has an axis with named channels (see the
    example in :ref:`NXdata </NXdata@default_slice-attribute>`), the NXdetector will have a series of NXdetector_channel groups, one for each
    channel, named CHANNELNAME_channel.

    Example, given these axes in the NXdata group::

      @axes = ["image_id", "channel", ".", "."]

    And this list of channels in the NXdata group::

      channel = ["threshold_1", "threshold_2", "difference"]

    The NXdetector group would have three NXdetector_channel groups::

      detector:NXdetector
        ...
        threshold_1_channel:NXdetector_channel
          threshold_energy = float
          flatfield = float[i, j]
          pixel_mask = uint[i, j]
          flatfield_applied = bool
          pixel_mask_applied = bool
        threshold_2_channel:NXdetector_channel
          threshold_energy = float
          flatfield = float[i, j]
          pixel_mask = uint[i, j]
          flatfield_applied = bool
          pixel_mask_applied = bool
        difference_channel:NXdetector_channel
          threshold_energy = float[2]
    """

    threshold_energy: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    flatfield_applied: Optional[NX_BOOLEAN] = None
    flatfield: Optional[NX_NUMBER] = None
    flatfield_errors: Optional[NX_FLOAT] = None
    pixel_mask_applied: Optional[NX_BOOLEAN] = None
    pixel_mask: Optional[NX_INT] = None
    saturation_value: Optional[NX_NUMBER] = None
    underload_value: Optional[NX_NUMBER] = None
