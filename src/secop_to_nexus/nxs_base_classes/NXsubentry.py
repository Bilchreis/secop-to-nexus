"""Auto-generated from NXsubentry.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_DATE_TIME,
    NX_FLOAT,
    NX_INT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcollection import NXcollection
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXinstrument import NXinstrument
    from secop_to_nexus.nxs_base_classes.NXmonitor import NXmonitor
    from secop_to_nexus.nxs_base_classes.NXnote import NXnote
    from secop_to_nexus.nxs_base_classes.NXparameters import NXparameters
    from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess
    from secop_to_nexus.nxs_base_classes.NXsample import NXsample
    from secop_to_nexus.nxs_base_classes.NXuser import NXuser


@dataclass
class NXsubentry(NXobject):
    """Group of multiple application definitions for "multi-modal" (e.g. SAXS/WAXS) measurements.

    ``NXsubentry`` is a base class virtually identical to :ref:`NXentry`
    and is used as the (overlay) location for application definitions.
    Use a separate ``NXsubentry`` for each application definition.

    To use ``NXsubentry`` with a hypothetical application definition
    called ``NXmyappdef``:

    * Create a group with attribute ``NX_class="NXsubentry"``
    * Within that group, create a field called ``definition="NXmyappdef"``.
    * There are two optional attributes of definition: ``version`` and ``URL``

    The intended use is to define application definitions for a
    multi-modal (a.k.a. multi-technique) :ref:`NXentry`.
    Previously, an application definition
    replaced :ref:`NXentry` with its own definition.
    With the increasing popularity of instruments combining
    multiple techniques for data collection (such as SAXS/WAXS instruments),
    it was recognized the application definitions must be entered in the NeXus
    data file tree as children of :ref:`NXentry`.
    """

    IDF_Version: Optional[str] = dc_field(
        default=None, metadata={"kind": "attribute"}
    )  # attribute; ISIS Muon IDF_Version
    title: Optional[NX_CHAR] = None
    experiment_identifier: Optional[NX_CHAR] = None
    experiment_description: Optional[NX_CHAR] = None
    collection_identifier: Optional[NX_CHAR] = None
    collection_description: Optional[NX_CHAR] = None
    entry_identifier: Optional[NX_CHAR] = None
    definition: Optional[NX_CHAR] = None
    definition_local: Optional[NX_CHAR] = None
    start_time: Optional[NX_DATE_TIME] = None
    end_time: Optional[NX_DATE_TIME] = None
    duration: Optional[NX_INT] = None  # units: NX_TIME
    collection_time: Optional[NX_FLOAT] = None  # units: NX_TIME
    run_cycle: Optional[NX_CHAR] = None
    program_name: Optional[NX_CHAR] = None
    revision: Optional[NX_CHAR] = None
    pre_sample_flightpath: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    experiment_documentation: Optional[NXnote] = (
        None  # Description of the full experiment (document in pdf, latex, ...)
    )
    notes: Optional[NXnote] = None  # Notes describing entry
    thumbnail: Optional[NXnote] = (
        None  # A small image that is representative of the entry. An example of this is a 640x480
    )
    users: dict[str, NXuser] = dc_field(default_factory=dict)
    samples: dict[str, NXsample] = dc_field(default_factory=dict)
    instruments: dict[str, NXinstrument] = dc_field(default_factory=dict)
    collections: dict[str, NXcollection] = dc_field(default_factory=dict)
    monitors: dict[str, NXmonitor] = dc_field(default_factory=dict)
    data: dict[str, NXdata] = dc_field(default_factory=dict)
    parameters: dict[str, NXparameters] = dc_field(default_factory=dict)
    processes: dict[str, NXprocess] = dc_field(default_factory=dict)
