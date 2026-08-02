"""Auto-generated from NXem_event_data.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_DATE_TIME,
    NX_INT,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXem_instrument import NXem_instrument
    from secop_to_nexus.nxs_base_classes.NXimage import NXimage
    from secop_to_nexus.nxs_base_classes.NXspectrum import NXspectrum
    from secop_to_nexus.nxs_base_classes.NXuser import NXuser


@dataclass
class NXem_event_data(NXobject):
    """Base class to store state and (meta)data of events for electron microscopy.

    Event-related (meta)data, typically measured datasets like images and spectra.
    To avoid repetitively storing static instrument-related metadata,
    the dynamic (meta)data that typically changes for each image and spectrum
    is split from the static (meta)data.

    Which temporal granularity is adequate to log events depends on the situation and
    research question. Using a model which enables a collection of events offers
    the most flexible way to cater for both experiments with controlled electron
    beams in a real microscope or the simulation of such experiments or
    individual aspects of such experiments.

    Electron microscopes are dynamic. Scientists often report that microscopes
    *perform differently* across sessions. That *they* perform differently from
    one day or another. In some cases, root causes for performance differences
    are unclear. Users of the instrument may consider such conditions impractical,
    or *too poor*, and thus abort their session. Alternatively, users may try to
    bring the microscope into a state where conditions are considered better
    or of whatever high enough quality for starting or continuing the measurement.

    In all these use cases it is useful to have a mechanism whereby time-dependent
    data of the instrument state can be stored and documented in an representation
    that facilitates interoperability. This is the idea behind this base class.

    :ref:`NXem_event_data` represents an instance to describe and serialize flexibly
    whatever is considered a time interval during which the instrument is
    considered stable enough for allowing any working on tasks with it.
    Examples of such tasks are the collecting of data (images and spectra) or
    the calibrating the instrument or individual of its components. Users may wish to take
    only a single scan or image and complete their session thereafter.
    Alternatively, users are working for much longer time at the instrument,
    perform recalibrations in between and take several scans (of different
    ROIs on the specimen), or they explore the state of the microscope for
    service or maintenance tasks.

    :ref:`NXem_event_data` serves the harmonization and documentation of these cases:

    * Firstly, via a header section whose purpose is to contextualize
      and identify the event instance in time.
    * Secondly, via a data and metadata section where individual data
      collections can be stored in a standardized representation.

    We are aware of the fact that given the variety how an electron microscope
    is used, there is a need for a flexible and adaptive documentation system.
    At the same time we are also convinced though that just because one has
    different requirements for some specific aspect under the umbrella of settings
    to an electron microscope, this does not necessarily warrant that one has to
    cook up an own data schema.

    Instead, the electron microscopy community should work towards reusing schema
    components as frequently as possible. This will enable that there is at all
    not only a value of harmonizing electron microscopy research content but also
    there is a technical possibility to build services around such harmonized data.

    Arguably it is oftentimes tricky to specify a clear time interval when the
    microscope is *stable enough*. Take for instance the acquisition of an image
    or a stack of spectra. Having to deal with instabilities is a common theme in
    electron microscopy practice. Numerical protocols can be used during data
    post-processing to correct for some of the instabilities.
    A few exemplar references provide an overview on the subject:

    * `C. Ophus et al. <https://dx.doi.org/10.1016/j.ultramic.2015.12.002>`_
    * `B. Berkels et al. <https://doi.org/10.1016/j.ultramic.2018.12.016>`_
    * `L. Jones et al. <https://link.springer.com/article/10.1186/s40679-015-0008-4>`_

    For specific simulation purposes, mainly in an effort to digitally repeat or simulate
    the experiment (digital twin), it is tempting to consider dynamics of the instrument,
    implemented as time-dependent functional descriptions of e.g. lens excitations,
    beam shape functions, trajectories of groups of electrons and ions, or detector noise models.
    This also warrants to document the time-dependent details of individual components
    of the microscope via the here implemented class :ref:`NXem_event_data`.
    """

    start_time: Optional[NX_DATE_TIME] = None
    end_time: Optional[NX_DATE_TIME] = None
    identifier_event: Optional[NX_INT] = None  # units: NX_UNITLESS
    identifier_sample: Optional[NX_CHAR] = None  # units: NX_UNITLESS
    type: Optional[NX_CHAR] = None
    users: dict[str, NXuser] = dc_field(default_factory=dict)
    em_instruments: dict[str, NXem_instrument] = dc_field(default_factory=dict)
    images: dict[str, NXimage] = dc_field(default_factory=dict)
    spectrums: dict[str, NXspectrum] = dc_field(default_factory=dict)
