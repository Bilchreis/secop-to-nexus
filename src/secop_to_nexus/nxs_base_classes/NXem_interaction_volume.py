"""Auto-generated from NXem_interaction_volume.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXprocess import NXprocess


@dataclass
class NXem_interaction_volume(NXobject):
    """Base class to describe the volume of interaction for particle-matter interaction.

    Computer models like Monte Carlo or molecular dynamics / electron- or ion-beam
    interaction simulations can be used to qualify and (or) quantify the shape of
    the interaction volume. Results of such simulations can be summary statistics
    or single-particle-resolved sets of trajectories.

    Explicit or implicit descriptions of the geometry of this
    interaction volume are possible:

    * An implicit description is via a set of electron/specimen interactions
      represented ideally as trajectory data from the computer simulation.
    * An explicit description is via iso-contour surface using either
      a simulation grid or a triangulated surface mesh of the approximated
      iso-contour surface evaluated at specific threshold values.
      Iso-contours could be computed from electron or particle flux through
      an imaginary control surface (the iso-surface) or energy-levels
      (e.g. the case of X-rays). Details depend on the model.
    * Another explicit description is via theoretical models which may
      be relevant e.g. for X-ray spectroscopy

    Further details on how the interaction volume can be quantified
    is available in the literature for example:

    * `S. Richter et al. <https://doi.org/10.1088/1757-899X/109/1/012014>`_
    * `J. Bünger et al. <https://doi.org/10.1017/S1431927622000083>`_
    * `J. F. Ziegler et al. <https://doi.org/10.1007/978-3-642-68779-2_5>`_
    """

    data: dict[str, NXdata] = dc_field(default_factory=dict)
    processes: dict[str, NXprocess] = dc_field(default_factory=dict)
