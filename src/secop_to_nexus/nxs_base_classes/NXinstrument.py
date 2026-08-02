"""Auto-generated from NXinstrument.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXactuator import NXactuator
    from secop_to_nexus.nxs_base_classes.NXaperture import NXaperture
    from secop_to_nexus.nxs_base_classes.NXattenuator import NXattenuator
    from secop_to_nexus.nxs_base_classes.NXbeam import NXbeam
    from secop_to_nexus.nxs_base_classes.NXbeam_stop import NXbeam_stop
    from secop_to_nexus.nxs_base_classes.NXbending_magnet import NXbending_magnet
    from secop_to_nexus.nxs_base_classes.NXcapillary import NXcapillary
    from secop_to_nexus.nxs_base_classes.NXcollection import NXcollection
    from secop_to_nexus.nxs_base_classes.NXcollimator import NXcollimator
    from secop_to_nexus.nxs_base_classes.NXcrystal import NXcrystal
    from secop_to_nexus.nxs_base_classes.NXdetector import NXdetector
    from secop_to_nexus.nxs_base_classes.NXdetector_group import NXdetector_group
    from secop_to_nexus.nxs_base_classes.NXdisk_chopper import NXdisk_chopper
    from secop_to_nexus.nxs_base_classes.NXevent_data import NXevent_data
    from secop_to_nexus.nxs_base_classes.NXfabrication import NXfabrication
    from secop_to_nexus.nxs_base_classes.NXfermi_chopper import NXfermi_chopper
    from secop_to_nexus.nxs_base_classes.NXfilter import NXfilter
    from secop_to_nexus.nxs_base_classes.NXflipper import NXflipper
    from secop_to_nexus.nxs_base_classes.NXguide import NXguide
    from secop_to_nexus.nxs_base_classes.NXhistory import NXhistory
    from secop_to_nexus.nxs_base_classes.NXinsertion_device import NXinsertion_device
    from secop_to_nexus.nxs_base_classes.NXmirror import NXmirror
    from secop_to_nexus.nxs_base_classes.NXmoderator import NXmoderator
    from secop_to_nexus.nxs_base_classes.NXmonochromator import NXmonochromator
    from secop_to_nexus.nxs_base_classes.NXpolarizer import NXpolarizer
    from secop_to_nexus.nxs_base_classes.NXpositioner import NXpositioner
    from secop_to_nexus.nxs_base_classes.NXsensor import NXsensor
    from secop_to_nexus.nxs_base_classes.NXsource import NXsource
    from secop_to_nexus.nxs_base_classes.NXtransformations import NXtransformations
    from secop_to_nexus.nxs_base_classes.NXvelocity_selector import NXvelocity_selector
    from secop_to_nexus.nxs_base_classes.NXxraylens import NXxraylens


@dataclass
class NXinstrument(NXobject):
    """Collection of the components of the instrument or beamline.

    Template of instrument descriptions comprising various beamline components.
    Each component will also be a NeXus group defined by its distance from the
    sample. Negative distances represent beamline components that are before the
    sample while positive distances represent components that are after the sample.
    This device allows the unique identification of beamline components in a way
    that is valid for both reactor and pulsed instrumentation.
    """

    name: Optional[NX_CHAR] = None
    actuators: dict[str, NXactuator] = dc_field(default_factory=dict)
    apertures: dict[str, NXaperture] = dc_field(default_factory=dict)
    attenuators: dict[str, NXattenuator] = dc_field(default_factory=dict)
    beams: dict[str, NXbeam] = dc_field(default_factory=dict)
    beam_stops: dict[str, NXbeam_stop] = dc_field(default_factory=dict)
    bending_magnets: dict[str, NXbending_magnet] = dc_field(default_factory=dict)
    collimators: dict[str, NXcollimator] = dc_field(default_factory=dict)
    collections: dict[str, NXcollection] = dc_field(default_factory=dict)
    capillaries: dict[str, NXcapillary] = dc_field(default_factory=dict)
    crystals: dict[str, NXcrystal] = dc_field(default_factory=dict)
    detectors: dict[str, NXdetector] = dc_field(default_factory=dict)
    detector_groups: dict[str, NXdetector_group] = dc_field(default_factory=dict)
    disk_choppers: dict[str, NXdisk_chopper] = dc_field(default_factory=dict)
    event_data: dict[str, NXevent_data] = dc_field(default_factory=dict)
    fabrications: dict[str, NXfabrication] = dc_field(default_factory=dict)
    fermi_choppers: dict[str, NXfermi_chopper] = dc_field(default_factory=dict)
    filters: dict[str, NXfilter] = dc_field(default_factory=dict)
    flippers: dict[str, NXflipper] = dc_field(default_factory=dict)
    guides: dict[str, NXguide] = dc_field(default_factory=dict)
    histories: dict[str, NXhistory] = dc_field(default_factory=dict)
    insertion_devices: dict[str, NXinsertion_device] = dc_field(default_factory=dict)
    mirrors: dict[str, NXmirror] = dc_field(default_factory=dict)
    moderators: dict[str, NXmoderator] = dc_field(default_factory=dict)
    monochromators: dict[str, NXmonochromator] = dc_field(default_factory=dict)
    polarizers: dict[str, NXpolarizer] = dc_field(default_factory=dict)
    positioners: dict[str, NXpositioner] = dc_field(default_factory=dict)
    sensors: dict[str, NXsensor] = dc_field(default_factory=dict)
    sources: dict[str, NXsource] = dc_field(default_factory=dict)
    DIFFRACTOMETER: Optional[NXtransformations] = None
    velocity_selectors: dict[str, NXvelocity_selector] = dc_field(default_factory=dict)
    xraylenses: dict[str, NXxraylens] = dc_field(default_factory=dict)
