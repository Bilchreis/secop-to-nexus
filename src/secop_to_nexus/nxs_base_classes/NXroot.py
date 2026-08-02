"""Auto-generated from NXroot.nxdl.xml by tools/generate_nx_classes.py — do not edit."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as dc_field  # noqa: F401
from typing import TYPE_CHECKING, Optional  # noqa: F401

from secop_to_nexus.nxs_base_classes.NXobject import NXobject

if TYPE_CHECKING:
    from secop_to_nexus.nxs_base_classes.NXentry import NXentry


@dataclass
class NXroot(NXobject):
    """The root of a NeXus file.

    In the NeXus standard, only NXentry groups are allowed at the
    root level of a file, although it is permitted to include
    additional groups and fields that are not part of the NeXus
    standard and will not be validated by NeXus tools. NeXus defines
    a number of root-level attributes that can be used to annotate
    the NeXus tree.

    Note that NXroot is the only base class that does not inherit
    from the NXobject class, since the latter permits the inclusion
    of NeXus objects that are not allowed at the root level.
    """

    file_time: Optional[str] = dc_field(
        default=None, metadata={"kind": "attribute"}
    )  # attribute; Date and time file was originally created
    file_name: Optional[str] = dc_field(
        default=None, metadata={"kind": "attribute"}
    )  # attribute; File name of original NeXus file
    file_update_time: Optional[str] = dc_field(
        default=None, metadata={"kind": "attribute"}
    )  # attribute; Date and time of last file change at close
    NeXus_version: Optional[str] = dc_field(
        default=None, metadata={"kind": "attribute"}
    )  # attribute; Version of NeXus API used in writing the file.
    NeXus_repository: Optional[str] = dc_field(
        default=None, metadata={"kind": "attribute"}
    )  # attribute; A repository containing the application definitions
    NeXus_release: Optional[str] = dc_field(
        default=None, metadata={"kind": "attribute"}
    )  # attribute; The version of NeXus definitions used in writing the file. This can either be a da...
    HDF_version: Optional[str] = dc_field(
        default=None, metadata={"kind": "attribute"}
    )  # attribute; Version of HDF (version 4) library used in writing the file
    HDF5_Version: Optional[str] = dc_field(
        default=None, metadata={"kind": "attribute"}
    )  # attribute; Version of HDF5 library used in writing the file.
    XML_version: Optional[str] = dc_field(
        default=None, metadata={"kind": "attribute"}
    )  # attribute; Version of XML support library used in writing the XML file
    h5py_version: Optional[str] = dc_field(
        default=None, metadata={"kind": "attribute"}
    )  # attribute; Version of h5py Python package used in writing the file
    creator: Optional[str] = dc_field(
        default=None, metadata={"kind": "attribute"}
    )  # attribute; facility or program where file originated
    creator_version: Optional[str] = dc_field(
        default=None, metadata={"kind": "attribute"}
    )  # attribute; Version of facility or program used in writing the file
    entries: dict[str, NXentry] = dc_field(default_factory=dict)  # entries
