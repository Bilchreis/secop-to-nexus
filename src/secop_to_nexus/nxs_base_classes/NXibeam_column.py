"""Auto-generated from NXibeam_column.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXactuator import NXactuator
    from secop_to_nexus.nxs_base_classes.NXaperture import NXaperture
    from secop_to_nexus.nxs_base_classes.NXbeam import NXbeam
    from secop_to_nexus.nxs_base_classes.NXdeflector import NXdeflector
    from secop_to_nexus.nxs_base_classes.NXelectromagnetic_lens import (
        NXelectromagnetic_lens,
    )
    from secop_to_nexus.nxs_base_classes.NXmonochromator import NXmonochromator
    from secop_to_nexus.nxs_base_classes.NXscan_controller import NXscan_controller
    from secop_to_nexus.nxs_base_classes.NXsensor import NXsensor
    from secop_to_nexus.nxs_base_classes.NXsource import NXsource


@dataclass
class NXibeam_column(NXcomponent):
    """Base class for a set of components equipping an instrument with FIB capabilities.

    Focused-ion-beam (FIB) capabilities turn especially scanning electron microscopes
    into specimen preparation labs. FIB is a material preparation technique whereby
    portions of the sample are illuminated with a focused ion beam with controlled
    intensity. The beam is controlled such that it is intense, focused, and equipped
    with sufficient ion having sufficient momentum to remove material in a controlled
    manner.

    The fact that an electron microscope with FIB capabilities achieves these functionalities
    via a second component (aka the ion gun) that has its own relevant control circuits,
    focusing lenses, and other components, warrants the definition of an own base class
    to group these components and distinguish them from the lenses and components for creating
    and shaping the electron beam.

    For more details about the relevant physics and application examples
    consult the literature, for example:

    * `L. A. Giannuzzi et al. <https://doi.org/10.1007/b101190>`_
    * `E. I. Preiß et al. <https://link.springer.com/content/pdf/10.1557/s43578-020-00045-w.pdf>`_
    * `J. F. Ziegler et al. <https://www.sciencedirect.com/science/article/pii/S0168583X10001862>`_
    * `J. Lili <https://www.osti.gov/servlets/purl/924801>`_
    * `N. Yao <https://doi.org/10.1017/CBO9780511600302>`_
    """

    operation_mode: Optional[NX_CHAR] = None
    ion_source: Optional[NXsource] = None  # The source which creates the ion beam.
    electromagnetic_lenses: dict[str, NXelectromagnetic_lens] = dc_field(
        default_factory=dict
    )
    apertures: dict[str, NXaperture] = dc_field(default_factory=dict)
    deflectors: dict[str, NXdeflector] = dc_field(default_factory=dict)
    blankerID: dict[str, NXdeflector] = dc_field(
        default_factory=dict
    )  # nameType: partial
    monochromators: dict[str, NXmonochromator] = dc_field(default_factory=dict)
    sensors: dict[str, NXsensor] = dc_field(default_factory=dict)
    actuators: dict[str, NXactuator] = dc_field(default_factory=dict)
    beams: dict[str, NXbeam] = dc_field(
        default_factory=dict
    )  # Individual characterization results for the position, shape,
    components: dict[str, NXcomponent] = dc_field(default_factory=dict)
    scan_controller: Optional[NXscan_controller] = None
