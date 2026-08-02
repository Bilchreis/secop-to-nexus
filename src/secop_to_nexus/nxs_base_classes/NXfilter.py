"""Auto-generated from NXfilter.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_CHAR,
    NX_FLOAT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXlog import NXlog
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry
    from secop_to_nexus.nxs_base_classes.NXsensor import NXsensor


@dataclass
class NXfilter(NXcomponent):
    """For band pass beam filters.

    If uncertain whether to use :ref:`NXfilter` (band-pass filter)
    or :ref:`NXattenuator` (reduces beam intensity), then use
    :ref:`NXattenuator`.
    """

    description: Optional[NX_CHAR] = None
    status: Optional[NX_CHAR] = None  # enum: in | out
    temperature: Optional[NX_FLOAT] = None  # units: NX_TEMPERATURE
    thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    density: Optional[NX_NUMBER] = None  # units: NX_MASS_DENSITY
    chemical_formula: Optional[NX_CHAR] = None
    unit_cell_a: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    unit_cell_b: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    unit_cell_c: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    unit_cell_alpha: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    unit_cell_beta: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    unit_cell_gamma: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    unit_cell_volume: Optional[NX_FLOAT] = None  # units: NX_VOLUME
    orientation_matrix: Optional[NX_FLOAT] = None
    m_value: Optional[NX_FLOAT] = None  # units: NX_DIMENSIONLESS
    substrate_material: Optional[NX_CHAR] = None
    substrate_thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    coating_material: Optional[NX_CHAR] = None
    substrate_roughness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    coating_roughness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    depends_on: Optional[NX_CHAR] = None
    geometries: dict[str, NXgeometry] = dc_field(
        default_factory=dict
    )  # Geometry of the filter
    transmission: Optional[NXdata] = None  # Wavelength transmission profile of filter
    temperature_log: Optional[NXlog] = None  # Linked temperature_log for the filter
    sensor_type: Optional[NXsensor] = (
        None  # Sensor(s)used to monitor the filter temperature
    )
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the beam line component
