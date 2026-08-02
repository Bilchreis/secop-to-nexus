"""Auto-generated from NXimage.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess


@dataclass
class NXimage(NXobject):
    """Base class for reporting a set of images representing specializations of NXdata.

    The most commonly used scanning methods are supported. That is one-,
    two-, three-dimensional ROIs discretized using regular Euclidean tilings.

    Colloquially, an image is understood as a discretized representation of intensity distribution
    detected or simulated for some ROI. When discretized with regular Euclidean tilings, the terms
    pixel and voxel identify the smallest discretization unit. In this case, pixel and voxel are polygonal
    or polyhedral unit cells respectively of the underlying tiling of the ROI within the reference space.
    For all other tilings e.g. non-equispaced, the shape and size of pixel and voxel differs. Using the term
    image point is eventually more appropriate when working with such tilings.

    Therefore, all docstrings in this base class refer to points. Points are considered
    exact synonyms for pixel and voxel, which are terms used for regular tilings.

    Point coordinates identify the location of the barycenter.

    For images in reciprocal space in practice, complex numbers are encoded via some formatted pair of real values.
    Typically, fast algorithms for computing Fourier transformations (FFT) are used to encode images in reciprocal
    (frequency) space. FFT libraries are used for implementing the key functionalities of these mathematical operations.
    Different libraries use different representations and encoding of the images.
    Details can be found in the respective sections of the typical FFT libraries documentations:

    * `FFTW by M. Frigo and S. G. Johnson <https://www.fftw.org/fftw3_doc/Tutorial.html#Tutorial>`_
    * `Intel MKL by the Intel Co. <https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-c/2024-2/fourier-transform-functions.html>`_
    * `cuFFT by the NVidia Co. <https://docs.nvidia.com/cuda/cufft/index.html>`_
    * `NFFT by the TU Chemnitz group <https://www-user.tu-chemnitz.de/~potts/nfft/>`_ for non-equispaced computations

    Users are strongly advised to inspect carefully which specific conventions their library uses
    to enable storing and modifying the implementation of their code such that the serialized
    representations as they are detailed here for NeXus match.

    It is often the case that several images are combined using processing. In this case,
    the number of images which are combined into collections is not necessarily the same
    for each collection. The NXimage base class addresses this logical distinction
    through the notation of indices_image and indices_group concepts.
    That is indices_image are always counting from offset in increments of one
    as each image is its own entity. By contrast, a group may contain no, or several images.
    Consequently, indices_group are not required to be contiguous.

    Classically, images depict objects in real space. Such usage of NXimage essentially is equivalent to
    storing pictures. For this purpose the image_1d, image_2d, or image_3d NXdata instances respectively
    should be used such that all their axes axis_i, axis_j, axis_k are constrained to NeXus Unit Category NX_LENGTH.

    Imaging modes in electron microscopy are typically more versatile, specifically for use cases
    in scanning transmission electron microscopy, so-called 4DSTEM. In this case, one two-dimensional
    diffraction image is taken for each point that gets scanned in real space. Consequently,
    image_3d and image_4d NXdata instances should be used for these cases with axis_k and axis_m
    respectively of NeXus Unit Category NX_LENGTH and axis_i and axis_j respectively of
    NeXus Unit Category NX_WAVENUMBER or NX_UNITLESS.
    """

    processes: dict[str, NXprocess] = dc_field(
        default_factory=dict
    )  # Details how NXdata instance were processed from detector readings/raw data.
    image_1d: Optional[NXdata] = None  # One-dimensional image.
    image_2d: Optional[NXdata] = None  # Two-dimensional image.
    image_3d: Optional[NXdata] = None  # Three-dimensional image.
    image_4d: Optional[NXdata] = None  # Four-dimensional image.
    stack_1d: Optional[NXdata] = None  # Collection of one-dimensional images.
    stack_2d: Optional[NXdata] = None  # Collection of two-dimensional images.
    stack_3d: Optional[NXdata] = None  # Collection of three-dimensional images.
