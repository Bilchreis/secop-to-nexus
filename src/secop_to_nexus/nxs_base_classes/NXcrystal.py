"""Auto-generated from NXcrystal.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_FLOAT,
    NX_INT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXlog import NXlog
    from secop_to_nexus.nxs_base_classes.NXoff_geometry import NXoff_geometry
    from secop_to_nexus.nxs_base_classes.NXshape import NXshape


@dataclass
class NXcrystal(NXcomponent):
    """A crystal monochromator or analyzer.

    Permits double bent
    monochromator comprised of multiple segments with anisotropic
    Gaussian mosaic.

    If curvatures are set to zero or are absent, array
    is considered to be flat.

    Scattering vector is perpendicular to surface. Crystal is oriented
    parallel to beam incident on crystal before rotation, and lies in
    vertical plane.
    """

    usage: Optional[NX_CHAR] = None  # enum: Bragg | Laue
    type: Optional[NX_CHAR] = None
    chemical_formula: Optional[NX_CHAR] = None
    order_no: Optional[NX_INT] = None
    cut_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    space_group: Optional[NX_CHAR] = None
    unit_cell: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    unit_cell_a: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    unit_cell_b: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    unit_cell_c: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    unit_cell_alpha: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    unit_cell_beta: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    unit_cell_gamma: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    unit_cell_volume: Optional[NX_FLOAT] = None  # units: NX_VOLUME
    orientation_matrix: Optional[NX_FLOAT] = None
    wavelength: Optional[NX_FLOAT] = None  # units: NX_WAVELENGTH
    d_spacing: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    scattering_vector: Optional[NX_FLOAT] = None  # units: NX_WAVENUMBER
    reflection: Optional[NX_INT] = None  # units: NX_UNITLESS
    thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    density: Optional[NX_NUMBER] = None  # units: NX_MASS_DENSITY
    segment_width: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    segment_height: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    segment_thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    segment_gap: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    segment_columns: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    segment_rows: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    mosaic_horizontal: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    mosaic_vertical: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    curvature_horizontal: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    curvature_vertical: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    is_cylindrical: Optional[NX_BOOLEAN] = None
    cylindrical_orientation_angle: Optional[NX_NUMBER] = None  # units: NX_ANGLE
    polar_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    azimuthal_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    bragg_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    temperature: Optional[NX_FLOAT] = None  # units: NX_TEMPERATURE
    temperature_coefficient: Optional[NX_FLOAT] = None  # units: NX_ANY
    depends_on: Optional[NX_CHAR] = None
    geometries: dict[str, NXgeometry] = dc_field(
        default_factory=dict
    )  # Position of crystal
    temperature_log: Optional[NXlog] = None  # log file of crystal temperature
    reflectivity: Optional[NXdata] = None  # crystal reflectivity versus wavelength
    transmission: Optional[NXdata] = None  # crystal transmission versus wavelength
    shape: Optional[NXshape] = (
        None  # A NXshape group describing the shape of the crystal arrangement
    )
    off_geometries: dict[str, NXoff_geometry] = dc_field(
        default_factory=dict
    )  # This group describes the shape of the beam line component
