"""Auto-generated from NXguide.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
    NX_INT,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry


@dataclass
class NXguide(NXcomponent):
    """A neutron optical element to direct the path of the beam.

    :ref:`NXguide` is used by neutron instruments to describe
    a guide consists of several mirrors building a shape through which
    neutrons can be guided or directed. The simplest such form is box shaped
    although elliptical guides are gaining in popularity.
    The individual parts of a guide usually have common characteristics
    but there are cases where they are different.
    For example,  a neutron guide might consist of 2 or 4 coated walls or
    a supermirror bender with multiple, coated vanes.

    To describe polarizing supermirrors such as used in neutron reflection,
    it may be necessary to revise this definition of :ref:`NXguide`
    to include :ref:`NXpolarizer` and/or :ref:`NXmirror`.

    When even greater complexity exists in the definition of what
    constitutes a *guide*,  it has been suggested that :ref:`NXguide`
    be redefined as a :ref:`NXcollection` of :ref:`NXmirror` each
    having their own :ref:`NXgeometry` describing their location(s).

    For the more general case when describing mirrors, consider using
    :ref:`NXmirror`.

    NOTE: The NeXus International Advisory Committee welcomes
    comments for revision and improvement of
    this definition of :ref:`NXguide`.
    """

    description: Optional[NX_CHAR] = None
    incident_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    bend_angle_x: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    bend_angle_y: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    interior_atmosphere: Optional[NX_CHAR] = None  # enum: vacuum | helium | argon
    external_material: Optional[NX_CHAR] = None
    m_value: Optional[NX_FLOAT] = None
    substrate_material: Optional[NX_FLOAT] = None
    substrate_thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    coating_material: Optional[NX_FLOAT] = None
    substrate_roughness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    coating_roughness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    number_sections: Optional[NX_INT] = None  # units: NX_UNITLESS
    depends_on: Optional[NX_CHAR] = None
    geometries: dict[str, NXgeometry] = dc_field(
        default_factory=dict
    )  # TODO:  Explain what this NXgeometry group means.  What is intended here?
    reflectivity: Optional[NXdata] = (
        None  # Reflectivity as function of reflecting surface and wavelength
    )
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the beam line component
