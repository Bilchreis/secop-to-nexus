"""Auto-generated from NXcorrector_cs.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXaperture import NXaperture
    from secop_to_nexus.nxs_base_classes.NXdeflector import NXdeflector
    from secop_to_nexus.nxs_base_classes.NXelectromagnetic_lens import (
        NXelectromagnetic_lens,
    )
    from secop_to_nexus.nxs_base_classes.NXoptical_lens import NXoptical_lens
    from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess


@dataclass
class NXcorrector_cs(NXcomponent):
    """Base class for a corrector reducing (spherical) aberrations of an electron optical setup.

    Different technology partners use different conventions and
    models for quantifying the aberration coefficients.

    Aberration correction components are especially important for (scanning)
    transmission electron microscopy. Composed of multiple lenses and multipole stigmators,
    their technical details are specific for the technology partner as well as
    the microscope and instrument. Most technical details are proprietary knowledge.

    If one component corrects for multiple types of aberrations (like it is the case
    reported here `CEOS <https://www.ceos-gmbh.de/en/research/electrostat>`_) follow this
    design when using corrector and monochromator in an application definition:

    * Use :ref:`NXcorrector_cs` for spherical aberration
    * Use :ref:`NXmonochromator` for energy filtering or chromatic aberration
    * Use the group corrector_ax in :ref:`NXem` for axial astigmatism aberration

    Although this base class currently provides concepts that are foremost used in
    the field of electron microscopy using this base class is not restricted to this
    research field. NXcorrector_cs can also serve as a container to detail, in
    combination with :ref:`NXaberration`, about measured aberrations in classical optics.
    In optics, though, the difference is that the design of the :ref:NXoptical_lens`
    itself (e.g., using aspheric lenses or combinations of lenses) enables to
    reduce spherical aberrations.
    """

    applied: Optional[NX_BOOLEAN] = None
    tableauID: dict[str, NXprocess] = dc_field(
        default_factory=dict
    )  # nameType: partial
    electromagnetic_lenses: dict[str, NXelectromagnetic_lens] = dc_field(
        default_factory=dict
    )
    optical_lenses: dict[str, NXoptical_lens] = dc_field(default_factory=dict)
    apertures: dict[str, NXaperture] = dc_field(default_factory=dict)
    deflectors: dict[str, NXdeflector] = dc_field(default_factory=dict)
