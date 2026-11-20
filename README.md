# secop-to-nexus

Write [NeXus](https://www.nexusformat.org/) files for arbitrary
[SECoP](https://github.com/SampleEnvironment/SECoP) SEC nodes: the node's
describe message determines the file structure, and the recorded parameter
values become `NXlog` groups. It is meant to be embedded in
[secant-service](https://github.com/Bilchreis/secant-service) so users can
download a `.nxs` file for a SEC node.

## Usage

```python
from secop_to_nexus import ParameterLog, write_nexus, nexus_bytes

logs = {
    # module -> parameter -> (Unix timestamps in s, SECoP wire values)
    "T_reg": {
        "value": ParameterLog([1760000000.0, 1760000001.0], [4.2, 4.3]),
        "status": ([1760000000.0], [[100, "at target"]]),
    },
}
write_nexus("node.nxs", describe_message, logs)   # describe: dict, JSON str or bytes
data = nexus_bytes(describe_message, logs)         # same, returned as bytes
```

`build_nexus_tree()` returns the NeXus object tree without writing it.

## File layout

One SEC node per file:

```
/entry                        NXentry       title, start_time, end_time, duration
/entry/instrument             NXinstrument  name = equipment_id, description
    firmware                  NXprogram     node firmware
    secop_description         NXnote        raw describe message (JSON)
    <module>                  NXsensor      Readable
                              NXactuator    Writable / Drivable
                              NXcollection  anything else (e.g. Communicator)
        <param>_log           NXlog         one per parameter that changed
        status_log            NXlog         status code (enum members in @secop_enum)
        <param>, status, ...  field         instead of the NXlog, if the value never changed
        implementation        NXprogram     module implementation
        data                  NXdata        plot of value over time
/entry/sample                 NXsample      only if a module's meaning belongs to the sample
    <quantity>_env            NXenvironment links to the sensors/actuators
    <quantity>_log            link to the log of the most important measuring module
```

Every module with a numeric `value` gets one `NXdata` group `data` next to its
logs. Its `value` signal and `time` axis are soft links into `value_log`, so
nothing is stored twice. Other parameters, including `target`, are not
plotted: they have their own timestamps and are never resampled. Array values plot as 2D (`@axes = ["time", "."]`). The
`@default` chain (root → `entry` → `instrument` → module → `data`) picks the
sample's main quantity, e.g. the highest-importance `temperature` module, and
otherwise the first module with a plot, so viewers such as h5web or NeXpy open
a useful plot directly.

Only parameters that change over time become an `NXlog`. A parameter whose
recorded value never changed (including one recorded only once) is written as a
plain field named like the parameter (`target`, `_gastype`, `status` and
`status_text`). The field keeps the units and the `@secop_*` attributes and
carries the time the value was first recorded in `@timestamp` (ISO 8601) and
the parameter description in `@description`. A parameter named like a field
NeXus already defines for the group (e.g. `name`, `type`) keeps its `NXlog`. A
module whose `value` is such a field gets no plot, and the sample then links
the field as `<quantity>` instead of `<quantity>_log`.

String and blob parameters that do change (typically the status text) are not
written at all, because `NXlog` is defined for numbers. Structured values
stored as JSON are kept.

Node and module properties go to the matching NeXus fields:

| SECoP property | NeXus |
|---|---|
| node `equipment_id` | `instrument/name` |
| node `description` | `instrument/description` |
| node `firmware` | `instrument/firmware` (`NXprogram/program`) |
| node `implementor` | `instrument/fabrication` (`NXfabrication/vendor`) |
| module `description` | `<module>/description` |
| module `implementation` | `<module>/implementation` (`NXprogram/program`) |
| module `meaning.function` | `NXsensor/measurement`, `NXactuator/physical_quantity` |
| anything else (`interface_classes`, `group`, `features`, `meaning`, `timeout`, custom `_...`) | `@secop_<property>` attribute of the instrument / module group; non-trivial values as JSON |

`NXentry/duration` is the time between the first and the last recorded value.

`meaning.function` fills `NXsensor/measurement` and
`NXactuator/physical_quantity`, using the NeXus spelling (`magneticfield` becomes
`magnetic_field`, and so on). A meaning belongs to the sample if `belongs_to`
is `"sample"`. Old list-style meanings (`[function, importance]`) always count
as sample meanings. `*_regulation` modules are linked into the environment but
never become `<quantity>_log`.

`NXlog/time` holds seconds relative to its `@start` attribute (ISO 8601, the
first timestamp in the file). Each value dataset carries the parameter's
datainfo as JSON in `@secop_datainfo`.

| SECoP datainfo | dataset |
|---|---|
| double, scaled | NX_FLOAT (scaled values converted to physical values) |
| int, enum | NX_INT (enum: `@secop_enum` name→code map) |
| bool | NX_BOOLEAN |
| string, blob | NX_CHAR (blob stays base64) |
| array of numbers/bools/enums | 2D array, one row per timestamp |
| tuple, struct, other arrays, ragged arrays, types frappy can't parse | NX_CHAR, one JSON string per timestamp (`@secop_encoding = "json"`) |

Datainfo is parsed with frappy's `get_datatype`. Files are written with
[NexusCreator](https://pypi.org/project/nexuscreator/).

## NeXus base classes

`src/secop_to_nexus/nxs_base_classes/` holds dataclasses for all NeXus base
classes, generated from the official NXDL definitions (version pinned in
`tools/generate_nx_classes.py`). Do not edit the generated `NX*.py` files;
regenerate them instead:

```sh
uv run python tools/generate_nx_classes.py          # regenerate
uv run python tools/generate_nx_classes.py --check  # pre-commit drift check
```

`NXobject.py`, `NXdtypes.py` and `NXreference.py` are hand-written.

## Development

```sh
make venv     # uv venv (Python 3.13) + all dependency groups
uv run pytest
make pretty   # pre-commit on all files
```
