"""Auto-generated from NXdetector.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401
    NX_BOOLEAN,
    NX_CHAR,
    NX_DATE_TIME,
    NX_FLOAT,
    NX_INT,
    NX_NUMBER,
)
from secop_to_nexus.nxs_base_classes.NXcomponent import NXcomponent

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXcollection import NXcollection
    from secop_to_nexus.nxs_base_classes.NXdata import NXdata
    from secop_to_nexus.nxs_base_classes.NXdetector_channel import NXdetector_channel
    from secop_to_nexus.nxs_base_classes.NXdetector_module import NXdetector_module
    from secop_to_nexus.nxs_base_classes.NXgeometry import NXgeometry
    from secop_to_nexus.nxs_base_classes.NXnote import NXnote


@dataclass
class NXdetector(NXcomponent):
    """A detector, detector bank, or multidetector."""

    time_of_flight: Optional[NX_FLOAT] = None  # units: NX_TIME_OF_FLIGHT
    raw_time_of_flight: Optional[NX_INT] = None  # units: NX_PULSES
    detector_number: Optional[NX_INT] = None
    data: Optional[NX_NUMBER] = None  # units: NX_ANY
    data_errors: Optional[NX_NUMBER] = None  # units: NX_ANY
    x_pixel_offset: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    y_pixel_offset: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    z_pixel_offset: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    distance: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    polar_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    azimuthal_angle: Optional[NX_FLOAT] = None  # units: NX_ANGLE
    description: Optional[NX_CHAR] = None
    serial_number: Optional[NX_CHAR] = None
    local_name: Optional[NX_CHAR] = None
    solid_angle: Optional[NX_FLOAT] = None  # units: NX_SOLID_ANGLE
    x_pixel_size: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    y_pixel_size: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    dead_time: Optional[NX_FLOAT] = None  # units: NX_TIME
    gas_pressure: Optional[NX_FLOAT] = None  # units: NX_PRESSURE
    detection_gas_path: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    crate: Optional[NX_INT] = None
    slot: Optional[NX_INT] = None
    input: Optional[NX_INT] = None
    type: Optional[NX_CHAR] = None
    real_time: Optional[NX_NUMBER] = None  # units: NX_TIME
    start_time: Optional[NX_FLOAT] = None  # units: NX_TIME
    stop_time: Optional[NX_FLOAT] = None  # units: NX_TIME
    calibration_date: Optional[NX_DATE_TIME] = None
    layout: Optional[NX_CHAR] = None  # enum: point | linear | area
    count_time: Optional[NX_NUMBER] = None  # units: NX_TIME
    sequence_number: Optional[NX_INT] = None
    beam_center_x: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    beam_center_y: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    frame_start_number: Optional[NX_INT] = None
    diameter: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    acquisition_mode: Optional[NX_CHAR] = (
        None  # enum: gated | triggered | summed | event | histogrammed |...
    )
    angular_calibration_applied: Optional[NX_BOOLEAN] = None
    angular_calibration: Optional[NX_FLOAT] = None
    flatfield_applied: Optional[NX_BOOLEAN] = None
    flatfield: Optional[NX_FLOAT] = None
    flatfield_errors: Optional[NX_FLOAT] = None
    pixel_mask_applied: Optional[NX_BOOLEAN] = None
    pixel_mask: Optional[NX_INT] = None
    image_key: Optional[NX_INT] = None
    countrate_correction_applied: Optional[NX_BOOLEAN] = None
    countrate_correction_lookup_table: Optional[NX_NUMBER] = None
    virtual_pixel_interpolation_applied: Optional[NX_BOOLEAN] = None
    bit_depth_readout: Optional[NX_INT] = None
    detector_readout_time: Optional[NX_FLOAT] = None  # units: NX_TIME
    trigger_delay_time: Optional[NX_FLOAT] = None  # units: NX_TIME
    trigger_delay_time_set: Optional[NX_FLOAT] = None  # units: NX_TIME
    trigger_internal_delay_time: Optional[NX_FLOAT] = None  # units: NX_TIME
    trigger_dead_time: Optional[NX_FLOAT] = None  # units: NX_TIME
    frame_time: Optional[NX_FLOAT] = None  # units: NX_TIME
    gain_setting: Optional[NX_CHAR] = None
    saturation_value: Optional[NX_NUMBER] = None
    underload_value: Optional[NX_NUMBER] = None
    number_of_cycles: Optional[NX_INT] = None
    sensor_material: Optional[NX_CHAR] = None
    sensor_thickness: Optional[NX_FLOAT] = None  # units: NX_LENGTH
    threshold_energy: Optional[NX_FLOAT] = None  # units: NX_ENERGY
    depends_on: Optional[NX_CHAR] = None
    geometries: dict[str, NXgeometry] = dc_field(
        default_factory=dict
    )  # Position and orientation of detector
    CHANNELNAME_channel: dict[str, NXdetector_channel] = dc_field(
        default_factory=dict
    )  # nameType: partial
    efficiency: Optional[NXdata] = (
        None  # Spectral efficiency of detector with respect to e.g. wavelength
    )
    calibration_method: Optional[NXnote] = (
        None  # summary of conversion of array data to pixels (e.g. polynomial
    )
    data_file: Optional[NXnote] = None
    collections: dict[str, NXcollection] = dc_field(
        default_factory=dict
    )  # Use this group to provide other data related to this NXdetector group.
    detector_modules: dict[str, NXdetector_module] = dc_field(
        default_factory=dict
    )  # For use in special cases where the data in NXdetector
