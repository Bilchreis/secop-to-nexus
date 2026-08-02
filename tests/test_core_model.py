from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional

import pytest

from secop_to_nexus.nxs_base_classes.NXdtypes import (
    NX_BOOLEAN,
    NX_CHAR,
    NX_DATE_TIME,
    NX_FLOAT,
    NX_INT,
    NX_POSINT,
    NX_UINT,
    Placeholder,
)
from secop_to_nexus.nxs_base_classes.NXobject import NXobject
from secop_to_nexus.nxs_base_classes.NXreference import NXreference


class TestDtypes:
    def test_scalar_float(self):
        assert NX_FLOAT(1.5).to_dict() == {"@dtype": "NX_FLOAT64", "@value": 1.5}

    def test_array_inferred(self):
        assert NX_INT([1, 2]).to_dict() == {"@dtype": "NX_INT64[]", "@value": [1, 2]}

    def test_units_and_attrs(self):
        d = NX_FLOAT(1.0, units="K", attrs={"long_name": "temperature"}).to_dict()
        assert d["@units"] == "K"
        assert d["@long_name"] == "temperature"

    def test_numeric_placeholder_is_bare_name(self):
        d = NX_FLOAT(Placeholder("t_data"), array=True).to_dict()
        assert d == {"@dtype": "NX_FLOAT64[]", "@value": "t_data"}

    def test_char_placeholder_uses_template_syntax(self):
        d = NX_CHAR(Placeholder("run_title")).to_dict()
        assert d["@value"] == "${run_title}"

    def test_explicit_array_flag_overrides_inference(self):
        assert NX_FLOAT(Placeholder("x")).to_dict()["@dtype"] == "NX_FLOAT64"
        assert (
            NX_FLOAT(Placeholder("x"), array=True).to_dict()["@dtype"] == "NX_FLOAT64[]"
        )

    def test_missing_value_raises(self):
        with pytest.raises(ValueError):
            NX_FLOAT(units="K").to_dict()

    def test_uint_posint_boolean_tokens(self):
        assert NX_UINT(1).to_dict()["@dtype"] == "NX_UINT64"
        assert NX_POSINT(1).to_dict()["@dtype"] == "NX_UINT64"
        assert NX_BOOLEAN(True).to_dict()["@dtype"] == "NX_BOOLEAN"

    def test_datetime_written_as_iso_char(self):
        dt = datetime(2026, 8, 2, 12, 0, tzinfo=timezone.utc)
        d = NX_DATE_TIME(dt).to_dict()
        assert d == {"@dtype": "NX_CHAR", "@value": "2026-08-02T12:00:00+00:00"}

    def test_naive_datetime_gets_offset(self):
        value = NX_DATE_TIME(datetime(2026, 8, 2, 12, 0)).to_dict()["@value"]
        assert "+" in value or "-" in value[10:]


@dataclass
class _Inner(NXobject):
    reading: Optional[NX_FLOAT] = None


@dataclass
class _Outer(NXobject):
    signal: Optional[str] = field(default=None, metadata={"kind": "attribute"})
    title: Optional[NX_CHAR] = None
    renamed: Optional[NX_CHAR] = field(default=None, metadata={"nx_name": "class"})
    inner: Optional[_Inner] = None
    inners: dict[str, _Inner] = field(default_factory=dict)


class TestSerializer:
    def test_nx_class_from_type_name(self):
        assert _Outer().to_nexus_dict()["@NX_class"] == "_Outer"

    def test_none_and_empty_dicts_skipped(self):
        assert _Outer().to_nexus_dict() == {"@NX_class": "_Outer"}

    def test_attribute_kind_emits_at_key(self):
        d = _Outer(signal="counts").to_nexus_dict()
        assert d["@signal"] == "counts"
        assert "signal" not in d

    def test_nx_name_override(self):
        d = _Outer(renamed=NX_CHAR("x")).to_nexus_dict()
        assert d["class"]["@value"] == "x"
        assert "renamed" not in d

    def test_nested_groups_and_dict_children(self):
        tree = _Outer(
            inner=_Inner(reading=NX_FLOAT(1.0)),
            inners={"a": _Inner(), "b": _Inner()},
        )
        d = tree.to_nexus_dict()
        assert d["inner"]["@NX_class"] == "_Inner"
        assert d["inner"]["reading"]["@value"] == 1.0
        assert d["a"]["@NX_class"] == "_Inner"
        assert d["b"]["@NX_class"] == "_Inner"

    def test_extra_fields_and_groups(self):
        tree = _Outer()
        tree.extra_fields["stamp"] = NX_INT(3)
        tree.extra_groups["log"] = _Inner()
        d = tree.to_nexus_dict()
        assert d["stamp"]["@value"] == 3
        assert d["log"]["@NX_class"] == "_Inner"

    def test_unserializable_value_raises(self):
        tree = _Outer()
        tree.extra_fields["bad"] = object()
        with pytest.raises(TypeError):
            tree.to_nexus_dict()


class TestReferences:
    def _tree(self) -> _Outer:
        root = _Outer(inner=_Inner(), inners={"named": _Inner()})
        root.finalize()
        return root

    def test_root_path_is_file_root(self):
        assert self._tree().get_path() == ""

    def test_paths_after_finalize(self):
        root = self._tree()
        assert root.inner.get_path() == "/inner"
        assert root.inners["named"].get_path() == "/named"

    def test_reference_resolves_to_path(self):
        root = self._tree()
        assert NXreference(root.inners["named"]).resolve() == "/named"

    def test_reference_as_attribute_value(self):
        root = _Outer(inner=_Inner())
        root.default = NXreference(root.inner)
        root.finalize()
        assert root.to_nexus_dict()["@default"] == "/inner"

    def test_reference_as_child_becomes_link(self):
        root = _Outer(inner=_Inner())
        root.extra_fields["alias"] = NXreference(root.inner)
        root.finalize()
        assert root.to_nexus_dict()["alias"] == {"@link": "/inner"}
