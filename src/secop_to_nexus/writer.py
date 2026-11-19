"""Write the NeXus tree of a SEC node to an HDF5 file via NexusCreator."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from typing import Any, Mapping

from nexuscreator.libraries.NeXusHDF5 import NexusHDF5Writer

from secop_to_nexus.mapping import Logs, build_nexus_tree


def write_nexus(
    path: str | os.PathLike[str],
    describe: Mapping[str, Any] | str | bytes,
    logs: Logs,
    **kwargs: Any,
) -> None:
    """Write a .nxs file for one SEC node; ``kwargs`` go to build_nexus_tree."""
    tree = build_nexus_tree(describe, logs, **kwargs)
    NexusHDF5Writer(tree.to_nexus_dict()).write(str(path))


def nexus_bytes(
    describe: Mapping[str, Any] | str | bytes, logs: Logs, **kwargs: Any
) -> bytes:
    """Like write_nexus, but return the file content (e.g. for a download)."""
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "node.nxs"
        write_nexus(path, describe, logs, **kwargs)
        return path.read_bytes()
