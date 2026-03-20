from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional

from secop_to_nexus.nxs_base_classes.NXdtypes import (
    NX_CHAR,
    NX_DATE_TIME,
    NX_FLOAT,
    NX_INT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcollection import NXcollection
    from secop_to_nexus.nxs_base_classes.NXinstrument import NXinstrument
    from secop_to_nexus.nxs_base_classes.NXmonitor import NXmonitor
    from secop_to_nexus.nxs_base_classes.NXparameters import NXparameters
    from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess
    from secop_to_nexus.nxs_base_classes.NXsample import NXsample
    from secop_to_nexus.nxs_base_classes.NXsubentry import NXsubentry
    from secop_to_nexus.nxs_base_classes.NXuser import NXuser


@dataclass
class NXEntry(NXobject):
    # title and default are inherited from NXobject

    experiment_identifier: Optional[NX_CHAR] = None
    experiment_description: Optional[NX_CHAR] = None
    collection_identifier: Optional[NX_CHAR] = None
    collection_description: Optional[NX_CHAR] = None
    entry_identifier: Optional[NX_CHAR] = None
    entry_identifier_uuid: Optional[NX_CHAR] = None
    features: Optional[NX_CHAR] = None
    definition: Optional[NX_CHAR] = None
    start_time: Optional[NX_DATE_TIME] = None
    end_time: Optional[NX_DATE_TIME] = None
    duration: Optional[NX_INT] = None  # units: NX_TIME
    collection_time: Optional[NX_FLOAT] = None  # units: NX_TIME
    run_cycle: Optional[NX_CHAR] = None
    program_name: Optional[NX_CHAR] = None
    revision: Optional[NX_CHAR] = None
    pre_sample_flightpath: Optional[NX_FLOAT] = None  # units: NX_LENGTH

    # Arbitrarily named groups — key is the instance name
    users: dict[str, NXuser] = field(default_factory=dict)
    samples: dict[str, NXsample] = field(default_factory=dict)
    instruments: dict[str, NXinstrument] = field(default_factory=dict)
    collections: dict[str, NXcollection] = field(default_factory=dict)
    monitors: dict[str, NXmonitor] = field(default_factory=dict)
    parameters: dict[str, NXparameters] = field(default_factory=dict)
    processes: dict[str, NXprocess] = field(default_factory=dict)
    subentries: dict[str, NXsubentry] = field(default_factory=dict)
