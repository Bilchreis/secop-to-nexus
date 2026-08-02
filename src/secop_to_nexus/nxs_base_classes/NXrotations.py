"""Auto-generated from NXrotations.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject


@dataclass
class NXrotations(NXobject):
    """Base class to detail a set of rotations, orientations, and disorientations.

    For getting a more detailed insight into the discussion of the
    parameterized description of orientations in materials science see:

    * `H.-J. Bunge <https://doi.org/10.1016/C2013-0-11769-2>`_
    * `T. B. Britton et al. <https://doi.org/10.1016/j.matchar.2016.04.008>`_
    * `D. Rowenhorst et al. <https://doi.org/10.1088/0965-0393/23/8/083501>`_
    * `A. Morawiec <https://doi.org/10.1007/978-3-662-09156-2>`_

    Once orientations are defined, one can continue to characterize the
    misorientation and specifically the disorientation. The misorientation describes
    the rotation that is required to register the lattices of two oriented objects
    (like crystal lattice) into a crystallographic equivalent orientation:

    * `R. Bonnet <https://doi.org/10.1107/S0567739480000186>`_

    The concepts of mis- and disorientation are relevant when analyzing the
    crystallography of interfaces.
    """

    reference_frame: Optional[NX_CHAR] = None
    crystal_symmetry: Optional[NX_CHAR] = None
    sample_symmetry: Optional[NX_CHAR] = None
    rotation_quaternion: Optional[NX_NUMBER] = None  # units: NX_DIMENSIONLESS
    rotation_euler: Optional[NX_NUMBER] = None  # units: NX_ANGLE
    is_antipodal: Optional[NX_BOOLEAN] = None
    orientation_quaternion: Optional[NX_NUMBER] = None  # units: NX_DIMENSIONLESS
    orientation_euler: Optional[NX_NUMBER] = None  # units: NX_ANGLE
    misorientation_quaternion: Optional[NX_NUMBER] = None  # units: NX_DIMENSIONLESS
    misorientation_angle: Optional[NX_NUMBER] = None  # units: NX_ANGLE
    misorientation_axis: Optional[NX_NUMBER] = None  # units: NX_DIMENSIONLESS
    disorientation_quaternion: Optional[NX_NUMBER] = None  # units: NX_DIMENSIONLESS
    disorientation_angle: Optional[NX_NUMBER] = None  # units: NX_ANGLE
    disorientation_axis: Optional[NX_NUMBER] = None  # units: NX_DIMENSIONLESS
