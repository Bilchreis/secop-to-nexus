"""Auto-generated from NXtransformations.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXtransformations(NXobject):
    """Collection of axis-based translations and rotations to describe a geometry.
    May also contain axes that do not move and therefore do not have a transformation
    type specified, but are useful in understanding coordinate frames within which
    transformations are done, or in documenting important directions, such as the
    direction of gravity.

    A nested sequence of transformations lists the translation and rotation steps
    needed to describe the position and orientation of any movable or fixed device.

    There will be one or more transformations (axes) defined by one or more fields
    for each transformation. Transformations can also be described by NXlog groups when
    the values change with time. The all-caps name ``AXISNAME`` designates the
    particular axis generating a transformation (e.g. a rotation axis or a translation
    axis or a general axis).   The attribute ``units="NX_TRANSFORMATION"`` designates the
    units will be appropriate to the ``transformation_type`` attribute:

    * ``NX_LENGTH`` for ``translation``
    * ``NX_ANGLE`` for ``rotation``
    * ``NX_UNITLESS`` for axes for which no transformation type is specified

    This class will usually contain all axes of a sample stage or goniometer or
    a detector.  The NeXus default McSTAS coordinate frame is assumed, but additional
    useful coordinate axes may be defined by using axes for which no transformation
    type has been specified.

    The entry point (``depends_on``) will be outside of this class and point to a
    field in here (or to an instance of ``NX_coordinate_system``). Following the
    chain may also require following ``depends_on`` links to transformations outside,
    for example to a common base table.  If a relative path is given, it is relative
    to the group enclosing the ``depends_on`` specification.

    For a chain of three transformations, where :math:`T_1` depends on :math:`T_2`
    and that in turn depends on :math:`T_3`, the final transformation :math:`T_f` is

    .. math:: T_f = T_3 T_2 T_1

    In explicit terms, the transformations are a subset of affine transformations
    expressed as 4x4 matrices that act on homogeneous coordinates, :math:`w=(x,y,z,1)^T`.

    For rotation and translation,

    .. math:: T_r &= \\begin{pmatrix} R & o \\\\ 0_3 & 1 \\end{pmatrix} \\\\ T_t &= \\begin{pmatrix} I_3  & t + o \\\\ 0_3 & 1 \\end{pmatrix}

    where :math:`R` is the usual 3x3 rotation matrix, :math:`o` is an offset vector,
    :math:`0_3` is a row of 3 zeros, :math:`I_3` is the 3x3 identity matrix and
    :math:`t` is the translation vector.

    :math:`o` is given by the ``offset`` attribute, :math:`t` is given by the ``vector``
    attribute multiplied by the field value, and :math:`R` is defined as a rotation
    about an axis in the direction of ``vector``, of angle of the field value.

    NOTE

    One possible use of ``NXtransformations`` is to define the motors and
    transformations for a diffractometer (goniometer).  Such use is mentioned
    in the ``NXinstrument`` base class.  Use one ``NXtransformations`` group
    for each diffractometer and name the group appropriate to the device.
    Collecting the motors of a sample table or xyz-stage in an NXtransformations
    group is equally possible.


    Following the section on the general description of axis in NXtransformations is a section which
    documents the fields commonly used within NeXus for positioning purposes and their meaning. Whenever
    there is a need for positioning a beam line component please use the existing names. Use as many fields
    as needed in order to position the component. Feel free to add more axis if required. In the description
    given below, only those attributes which are defined through the name are specified. Add the other attributes
    of the full set:

    * vector
    * offset
    * transformation_type
    * depends_on

    as needed.

    NOTE

    ``NXtransformations`` follows the **active** transformation convention. This means that the transformation describes
    how an object is moved or rotated within the coordinate system. In other words, the transformation
    actively changes the position or orientation of the object itself. This is in contrast to a **passive** transformation,
    which changes the frame of reference or coordinate system, while the object remains fixed. In case it is needed
    to describe multiple coordinate systems, it is strongly suggested to use the :ref:`NXcoordinate_system` base class.
    """

    AXISNAME: dict[str, NX_NUMBER] = dc_field(
        default_factory=dict
    )  # nameType: any; units: NX_TRANSFORMATION
    AXISNAME_end: dict[str, NX_NUMBER] = dc_field(
        default_factory=dict
    )  # nameType: partial; units: NX_TRANSFORMATION
    AXISNAME_increment_set: dict[str, NX_NUMBER] = dc_field(
        default_factory=dict
    )  # nameType: partial; units: NX_TRANSFORMATION
