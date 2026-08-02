#!/usr/bin/env python3
"""Generate NeXus base-class dataclasses from NXDL definitions.

Downloads the official NXDL definitions release tarball (pinned to
``DEFAULT_TAG``, cached under the user cache dir), parses every
``*.nxdl.xml`` in ``base_classes/``, and emits one dataclass module per class
into ``src/secop_to_nexus/nxs_base_classes/`` plus the package
``__init__.py``. ``NXobject`` itself stays hand-written (tree plumbing +
serializer); everything else is overwritten on each run.

Usage:
    python tools/generate_nx_classes.py [--tag TAG | --definitions PATH] [--check]

``--tag`` picks a release tag from
https://github.com/nexusformat/definitions/releases (default: DEFAULT_TAG).
``--definitions`` bypasses the download and uses a local checkout's
``base_classes`` directory instead (provenance then comes from its git state).
``--check`` regenerates in memory and fails if the committed files differ
(used by pre-commit to catch hand-edits and forgotten regeneration).
"""

from __future__ import annotations

import argparse
import io
import json
import keyword
import os
import shutil
import subprocess
import sys
import tarfile
import textwrap
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

import black

NS = "{http://definition.nexusformat.org/nxdl/3.1}"

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = REPO_ROOT / "src" / "secop_to_nexus" / "nxs_base_classes"

DEFINITIONS_REPO = "nexusformat/definitions"
# release tag the committed classes are generated from; bump deliberately and
# regenerate in the same commit
DEFAULT_TAG = "v2026.01"

# hand-written modules the generator must never touch
HAND_WRITTEN = {"NXobject.py", "NXdtypes.py", "NXreference.py", "__init__.py"}

# NXDL field type token -> annotation exported by NXdtypes
DTYPE_MAP = {
    "NX_CHAR": "NX_CHAR",
    "NX_BOOLEAN": "NX_BOOLEAN",
    "NX_FLOAT": "NX_FLOAT",
    "NX_INT": "NX_INT",
    "NX_UINT": "NX_UINT",
    "NX_POSINT": "NX_POSINT",
    "NX_NUMBER": "NX_NUMBER",
    "NX_DATE_TIME": "NX_DATE_TIME",
    "NX_COMPLEX": "NX_COMPLEX",
    "NX_BINARY": "NX_BINARY",
    "NX_CHAR_OR_NUMBER": "NX_CHAR_OR_NUMBER",
}

# NXDL attribute type token -> plain python annotation (attributes are not datasets)
ATTR_TYPE_MAP = {
    "NX_CHAR": "str",
    "NX_NUMBER": "float | int",
    "NX_INT": "int",
    "NX_POSINT": "int",
    "NX_BOOLEAN": "bool",
    "NX_DATE_TIME": "str",
    "NX_CHAR_OR_NUMBER": "str | float | int",
}


@dataclass
class Member:
    py_name: str
    code: str  # rendered dataclass field line(s), without indentation
    dtype_imports: set[str] = field(default_factory=set)
    group_import: str | None = None  # class name to import under TYPE_CHECKING


@dataclass
class ClassModel:
    name: str
    extends: str
    doc: str
    members: list[Member] = field(default_factory=list)


def _doc_text(el: ET.Element | None) -> str:
    if el is None:
        return ""
    node = el.find(f"{NS}doc")
    if node is None or node.text is None:
        return ""
    return textwrap.dedent(node.text).strip()


def _first_doc_line(el: ET.Element) -> str:
    doc = _doc_text(el)
    return doc.splitlines()[0].strip() if doc else ""


def _sanitize(name: str) -> tuple[str, bool]:
    """Return a valid python identifier and whether it was changed."""
    py = name
    if not py.isidentifier():
        py = "".join(c if c.isalnum() or c == "_" else "_" for c in py)
        if py and py[0].isdigit():
            py = f"_{py}"
    if keyword.iskeyword(py):
        py = f"{py}_"
    return py, py != name


def _comment(parts: list[str]) -> str:
    parts = [p for p in parts if p]
    if not parts:
        return ""
    text = "  # " + "; ".join(parts)
    return text if len(text) <= 100 else text[:97] + "..."


def _enum_comment(el: ET.Element) -> str:
    enum = el.find(f"{NS}enumeration")
    if enum is None:
        return ""
    values = [item.get("value", "") for item in enum.findall(f"{NS}item")]
    text = "enum: " + " | ".join(values)
    return text if len(text) <= 60 else text[:57] + "..."


def _pluralize(class_name: str) -> str:
    t = class_name[2:] if class_name.startswith("NX") else class_name
    if t.endswith("data"):
        return t
    if t.endswith(("lens", "ss")):
        return t + "es"
    if t.endswith("s"):  # already plural-looking (parameters, transformations, ...)
        return t
    if t.endswith(("sh", "ch", "x", "z")):
        return t + "es"
    if t.endswith("y") and t[-2:-1] not in "aeiou":
        return t[:-1] + "ies"
    return t + "s"


def parse_definition(path: Path) -> ClassModel:
    root = ET.parse(path).getroot()
    model = ClassModel(
        name=root.get("name", ""),
        extends=root.get("extends", "NXobject") or "NXobject",
        doc=_doc_text(root),
    )
    used_names: set[str] = set()

    def add(member: Member) -> None:
        model.members.append(member)
        used_names.add(member.py_name)

    for attr in root.findall(f"{NS}attribute"):
        name = attr.get("name", "")
        if name == "default":
            continue  # inherited from the hand-written NXobject base
        py_name, renamed = _sanitize(name)
        annotation = ATTR_TYPE_MAP.get(attr.get("type", "NX_CHAR"), "str")
        meta = {"kind": "attribute"}
        if renamed:
            meta["nx_name"] = name
        if attr.get("nameType") in ("any", "partial"):
            # template attribute (e.g. AXISNAME_indices): arbitrary names, dict key
            # is the concrete attribute name
            comment = _comment(
                [f"attribute, nameType: {attr.get('nameType')}", _first_doc_line(attr)]
            )
            code = (
                f"{py_name}: dict[str, {annotation}] = "
                f"dc_field(default_factory=dict, metadata={meta!r}){comment}"
            )
        else:
            comment = _comment(
                ["attribute", _enum_comment(attr), _first_doc_line(attr)]
            )
            code = (
                f"{py_name}: Optional[{annotation}] = "
                f"dc_field(default=None, metadata={meta!r}){comment}"
            )
        add(Member(py_name, code))

    for fld in root.findall(f"{NS}field"):
        name = fld.get("name", "")
        py_name, renamed = _sanitize(name)
        dtype = DTYPE_MAP.get(fld.get("type", "NX_CHAR"), "NX_CHAR")
        name_type = fld.get("nameType", "specified")
        units = fld.get("units")
        parts = [
            f"units: {units}" if units else "",
            "deprecated" if fld.get("deprecated") else "",
            _enum_comment(fld),
        ]
        if name_type in ("any", "partial"):
            comment = _comment([f"nameType: {name_type}"] + parts)
            code = (
                f"{py_name}: dict[str, {dtype}] = "
                f"dc_field(default_factory=dict){comment}"
            )
        else:
            comment = _comment(parts)
            if renamed:
                code = (
                    f"{py_name}: Optional[{dtype}] = "
                    f"dc_field(default=None, metadata={{'nx_name': {name!r}}}){comment}"
                )
            else:
                code = f"{py_name}: Optional[{dtype}] = None{comment}"
        add(Member(py_name, code, dtype_imports={dtype}))

    group_members: list[Member] = []
    for grp in root.findall(f"{NS}group"):
        gtype = grp.get("type", "")
        gname = grp.get("name")
        name_type = grp.get("nameType", "specified")
        doc_line = _first_doc_line(grp)
        if gname is None or name_type in ("any", "partial"):
            base = gname if gname is not None else _pluralize(gtype)
            py_name, _ = _sanitize(base)
            while py_name in used_names:
                py_name += "_groups"
            comment = _comment(
                [f"nameType: {name_type}"] if gname is not None else [doc_line]
            )
            code = (
                f"{py_name}: dict[str, {gtype}] = "
                f"dc_field(default_factory=dict){comment}"
            )
        else:
            py_name, renamed = _sanitize(gname)
            comment = _comment([doc_line])
            if renamed:
                code = (
                    f"{py_name}: Optional[{gtype}] = "
                    f"dc_field(default=None, metadata={{'nx_name': {gname!r}}}){comment}"
                )
            else:
                code = f"{py_name}: Optional[{gtype}] = None{comment}"
        member = Member(py_name, code, group_import=gtype)
        group_members.append(member)
        used_names.add(py_name)
    model.members.extend(group_members)
    return model


def render_module(model: ClassModel, source_name: str) -> str:
    dtype_imports = sorted(
        set().union(*(m.dtype_imports for m in model.members), set())
    )
    group_imports = sorted(
        {m.group_import for m in model.members if m.group_import}
        - {model.name, model.extends}
    )

    lines = [
        f'"""Auto-generated from {source_name} by tools/generate_nx_classes.py — do not edit."""',
        "",
        "from __future__ import annotations",
        "",
        "from dataclasses import dataclass",
        "from dataclasses import field as dc_field  # noqa: F401",
        "from typing import TYPE_CHECKING, Optional  # noqa: F401",
        "",
    ]
    if dtype_imports:
        lines.append(
            "from secop_to_nexus.nxs_base_classes.NXdtypes import (  # noqa: F401"
        )
        lines += [f"    {name}," for name in dtype_imports]
        lines.append(")")
    lines.append(
        f"from secop_to_nexus.nxs_base_classes.{model.extends} import {model.extends}"
    )
    if group_imports:
        lines += ["", "if TYPE_CHECKING:"]
        lines += [
            f"    from secop_to_nexus.nxs_base_classes.{name} import {name}"
            for name in group_imports
        ]
    lines += ["", "", "@dataclass", f"class {model.name}({model.extends}):"]

    if model.doc:
        doc = model.doc.replace("\\", "\\\\").replace('"""', r"\"\"\"")
        lines.append('    """' + doc.splitlines()[0])
        for docline in doc.splitlines()[1:]:
            lines.append(f"    {docline}".rstrip())
        lines.append('    """')
        lines.append("")

    if not model.members:
        if not model.doc:
            lines.append("    pass")
    else:
        for member in model.members:
            for i, code_line in enumerate(member.code.splitlines()):
                lines.append(f"    {code_line}")
    return "\n".join(lines).rstrip() + "\n"


def render_init(class_names: list[str]) -> str:
    lines = [
        '"""Auto-generated by tools/generate_nx_classes.py — do not edit."""',
        "",
        "from secop_to_nexus.nxs_base_classes._provenance import (  # noqa: F401",
        "    NXDL_COMMIT,",
        "    NXDL_VERSION,",
        ")",
    ]
    lines += [
        f"from secop_to_nexus.nxs_base_classes.{name} import {name}"
        for name in class_names
    ]
    lines += ["", "__all__ = ["]
    lines += [f'    "{name}",' for name in class_names]
    lines += ["]", ""]
    return "\n".join(lines)


def _definitions_version(definitions: Path) -> tuple[str, str]:
    def git(*args: str) -> str:
        result = subprocess.run(
            ["git", "-C", str(definitions), *args],
            capture_output=True,
            text=True,
        )
        return result.stdout.strip() if result.returncode == 0 else ""

    return (
        git("describe", "--always", "--dirty") or "unknown",
        git("rev-parse", "HEAD") or "unknown",
    )


def _cache_dir() -> Path:
    base = os.environ.get("XDG_CACHE_HOME")
    root = Path(base) if base else Path.home() / ".cache"
    return root / "secop-to-nexus"


def _resolve_tag_commit(tag: str) -> str:
    """Look up the commit sha a release tag points at (best effort)."""
    url = f"https://api.github.com/repos/{DEFINITIONS_REPO}/commits/{tag}"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return json.load(response).get("sha", "unknown")
    except (urllib.error.URLError, TimeoutError, ValueError):
        return "unknown"


def fetch_definitions(tag: str) -> Path:
    """Return the base_classes dir for a release tag, downloading it if needed.

    The extracted tarball is cached under the user cache dir keyed by tag, so
    repeated runs (pre-commit) are offline after the first download. The tag's
    commit sha is resolved once at download time and stored alongside, keeping
    provenance stable regardless of later network availability.
    """
    cache = _cache_dir() / f"nxdl-{tag}"
    base_classes = cache / "base_classes"
    if base_classes.is_dir():
        return base_classes

    url = f"https://github.com/{DEFINITIONS_REPO}/archive/refs/tags/{tag}.tar.gz"
    print(f"downloading NeXus definitions {tag} from {url}", file=sys.stderr)
    with urllib.request.urlopen(url, timeout=60) as response:
        data = response.read()

    tmp = cache.with_name(f"{cache.name}.tmp")
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir(parents=True)
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
        try:
            tar.extractall(tmp, filter="data")
        except TypeError:  # python < 3.11.4 without the filter parameter
            tar.extractall(tmp)
    (top,) = [p for p in tmp.iterdir() if p.is_dir()]
    if not (top / "base_classes").is_dir():
        shutil.rmtree(tmp)
        raise SystemExit(f"tarball for {tag} has no base_classes directory")
    (top / "COMMIT").write_text(_resolve_tag_commit(tag) + "\n")
    if cache.exists():
        shutil.rmtree(cache)
    top.rename(cache)
    shutil.rmtree(tmp)
    return base_classes


def render_provenance(version: str, commit: str) -> str:
    return "\n".join(
        [
            '"""Auto-generated by tools/generate_nx_classes.py — do not edit."""',
            "",
            "# Version of the NeXus NXDL definitions the base classes were generated from",
            f'NXDL_VERSION = "{version}"',
            f'NXDL_COMMIT = "{commit}"',
            "",
        ]
    )


def build_outputs(definitions: Path, version: str, commit: str) -> dict[str, str]:
    """Render every generated file as {filename: black-formatted content}."""
    xml_files = sorted(definitions.glob("*.nxdl.xml"))
    if not xml_files:
        raise SystemExit(f"no .nxdl.xml files found in {definitions}")

    black_mode = black.Mode(line_length=88)

    def fmt(code: str) -> str:
        return black.format_str(code, mode=black_mode)

    outputs: dict[str, str] = {}
    models = []
    for path in xml_files:
        model = parse_definition(path)
        if model.name == "NXobject":  # hand-written base
            continue
        models.append(model)
        outputs[f"{model.name}.py"] = fmt(render_module(model, path.name))

    class_names = sorted(["NXobject"] + [m.name for m in models])
    outputs["__init__.py"] = fmt(render_init(class_names))
    outputs["_provenance.py"] = fmt(render_provenance(version, commit))
    return outputs


def check(outputs: dict[str, str]) -> int:
    """Compare rendered outputs against the files on disk; return exit code."""
    drifted = [
        name
        for name, content in outputs.items()
        if not (OUTPUT_DIR / name).is_file()
        or (OUTPUT_DIR / name).read_text() != content
    ]
    stale = sorted(
        p.name
        for p in OUTPUT_DIR.glob("*.py")
        if p.name not in outputs and p.name not in HAND_WRITTEN
    )
    if not drifted and not stale:
        print("generated NeXus classes are up to date")
        return 0
    if drifted:
        print(
            f"out of date (regenerate with tools/generate_nx_classes.py): {', '.join(sorted(drifted))}"
        )
    if stale:
        print(f"stale modules (rerun the generator to remove): {', '.join(stale)}")
    return 1


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tag",
        default=DEFAULT_TAG,
        help="NeXus definitions release tag to download "
        f"(default: {DEFAULT_TAG}, see https://github.com/{DEFINITIONS_REPO}/releases)",
    )
    parser.add_argument(
        "--definitions",
        type=Path,
        default=None,
        help="use this local base_classes directory instead of downloading "
        "a release (provenance then comes from its git state)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="do not write anything; fail if committed files differ from "
        "freshly generated output",
    )
    args = parser.parse_args()

    if args.definitions is not None:
        if not args.definitions.is_dir():
            raise SystemExit(f"definitions not found at {args.definitions}")
        definitions = args.definitions
        version, commit = _definitions_version(definitions)
    else:
        try:
            definitions = fetch_definitions(args.tag)
        except (urllib.error.URLError, TimeoutError) as exc:
            # offline and not cached: the drift check has nothing to compare
            # against, so skip rather than fail every commit
            print(
                f"warning: could not download definitions {args.tag} ({exc}), "
                "skipping",
                file=sys.stderr,
            )
            return
        version = args.tag
        commit = (definitions.parent / "COMMIT").read_text().strip()

    outputs = build_outputs(definitions, version, commit)

    if args.check:
        sys.exit(check(outputs))

    for name, content in outputs.items():
        (OUTPUT_DIR / name).write_text(content)

    stale = [
        p
        for p in OUTPUT_DIR.glob("*.py")
        if p.name not in outputs and p.name not in HAND_WRITTEN
    ]
    for p in stale:
        p.unlink()

    n_classes = sum(1 for name in outputs if name.startswith("NX"))
    print(f"generated {n_classes} classes into {OUTPUT_DIR}")
    if stale:
        print(f"removed stale modules: {', '.join(sorted(p.name for p in stale))}")


if __name__ == "__main__":
    main()
