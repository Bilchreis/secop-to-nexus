"""Auto-generated from NXcoordinate_system.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXtransformations import NXtransformations


@dataclass
class NXcoordinate_system(NXobject):
    """Base class to detail a coordinate system (CS).

    Instances of ``NXcoordinate_system`` can be used to describe coordinate systems
    other than the default `NeXus coordinate system <https://manual.nexusformat.org/design.html#the-nexus-coordinate-system>`_.

    Whenever possible, all instances of :ref:`NXcoordinate_system`
    should be used at the top-level (i.e, directly below ``NXentry``)
    within an application definition or within a NeXus file.

    ``NXcoordinate_system`` can be part of the transformations chain
    using :ref:`NXtransformations`, where it acts as a linear
    change-of-basis transformation (using a 3x3 matrix with the basis
    vectors ``x``, `y``, and ``z`` as columns).

    Any group that has an optional ``depends_on`` field or any field
    that has an optional ``depends_on`` attribute has a fallback when
    ``depends_on`` is not provided. The fallback behavior involves
    traversing up the hierarchy until the first ancestor that contains one
    and only one ``NXcoordinate_system`` group is found. If such an ancestor
    exists, its coordinate system applies. If none is found or more than
    one instance of ``NXcoordinate_system`` is found at the same level,
    then the current coordinate system is not defined with respect to
    anything else. As an example, if there is only one ``NXcoordinate_system``
    called "my_coordinate_system" defined directly under ``NXentry``, each
    optional ``depends_on`` field/attribute that is not defined
    automatically defaults to ``depends_on=my_coordinate_system``.

    How many groups of type ``NXcoordinate_system`` should be used in
    an application definition?

    * 0; if there is no instance of ``NXcoordinate_system`` across the
      entire tree, you can use ``depends_on="."`` to state that this
      transformation depends on the default
      `NeXus coordinate system <https://manual.nexusformat.org/design.html#the-nexus-coordinate-system>`_
      (which is the same as the one used by `McStas <https://mcstas.org/>`_).

      For the sake of clarity, even in this case it is better
      to be explicit and consistent for every other coordinate system definition
      to support users with interpreting the content and logic behind
      every instance of the tree.

      The default NeXus coordinate system (i.e., the McStas coordinate
      system) can be expressed as follows:

      .. code-block::

        mcstas@NXcoordinate_system
            x = [1, 0, 0]
            y = [0, 1, 0]
            z = [0, 0, 1]
            @y_direction = "opposite to gravity"
            @z_direction = "direction of the primary beam"

      Note that this assumes that the direction of the beam is not defined in the ``NXbeam`` instance.

    * 1; if only one :ref:`NXcoordinate_system` is defined, it should be
      placed as high up in the tree hierarchy (ideally right below an
      instance of NXentry) of the application definition tree as possible.
      This coordinate system shall be named such that it is clear how this
      coordinate system is typically referred to in a community. For the
      NeXus McStas coordinate system, it is advised to call it ``mcstas``
      for the sake of improved clarity.

      If this is the case, it is assumed that this ``NXcoordinate_system``
      overwrites the NeXus default McStas coordinate system, i.e. users
      can thereby conveniently and explicitly specify the
      coordinate system that they wish to use.

      This case has the advantage that it is explicit and offers no
      ambiguities. However, in reality typically multiple coordinate
      systems have to be mastered especially for complex multi-signal
      modality experiments.

      If this case is realized, the best practice is that in every
      case where this coordinate system should be referred to the respective
      group has a ``depends_on`` field, to clearly indicate which
      specific coordinate systems is referred to.

    * 2 and more; as soon as more than one :ref:`NXcoordinate_system`
      is specified somewhere in the tree, different interpretations are
      possible as to which of these coordinate systems
      apply or take preference.
      While these ambiguities should be avoided if possible, the
      opportunity for multiples instances enables to have coordinate
      system conventions that are specific for some part of the NeXus
      tree. This is especially useful for deep groups where
      multiple scientific methods are combined or cases where having a
      definition of global conversion tables how to convert between
      representations in different coordinate systems is not desired
      or available for now.

      To resolve the possible ambiguities which specific coordinate systems
      in an :ref:`NXtransformations` train is referred to, it is even more
      important to use the ``depends_on`` field in groups and the ``depends_on``
      attribute in NXtransformations to refer to one of the ``NXcoordinate_system``
      instances.

      In the case of two or more instances of ``NXcoordinate_system`` it
      is advised to specify the relationship between the two coordinate
      systems by using the :ref:`NXtransformations` group within
      ``NXcoordinate_system``.

    In any case, users are encouraged to write explicit and clean
    ``depends_on`` fields in all groups that encode information for which
    the interpretation of coordinate systems and transformations is relevant.
    If these ``depends_on`` instances are not provided or no instance of
    ``NX_coordinate_system`` exists in the upper part of the hierarchy,
    the application definition is considered underconstrained. Note that this
    is the case for all files that were created before ``NXcoordinate_system``
    was added.
    """

    origin: Optional[NX_CHAR] = None
    type: Optional[NX_CHAR] = None  # enum: undefined | cartesian
    x_alias: Optional[NX_CHAR] = None
    x_direction: Optional[NX_CHAR] = None
    x: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    y_alias: Optional[NX_CHAR] = None
    y_direction: Optional[NX_CHAR] = None
    y: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    z_alias: Optional[NX_CHAR] = None
    z_direction: Optional[NX_CHAR] = None
    z: Optional[NX_NUMBER] = None  # units: NX_LENGTH
    depends_on: Optional[NX_CHAR] = None
    transformations: dict[str, NXtransformations] = dc_field(
        default_factory=dict
    )  # Collection of axis-based translations and rotations to describe this coordinate system
