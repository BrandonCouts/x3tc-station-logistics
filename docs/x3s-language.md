# X3S Language

## New Statements Recognized
- **write.log**: `write to log file $DebugID append=[FALSE] value=$txt`
- **dec**: `dec $s`
- **remove.array.elem**: `remove element from array $config.Array at index $s`
- **skip.if**: `skip if $section`
- **al.description.var**: `al engine: set plugin $al.PluginID description to $plugin.description`
- **al.timer.var**: `al engine: set plugin $al.PluginID timer interval to 25 s`
- **set.global.var**: `set global variable: name=$al.PluginID value=$al.Settings`
- **return.var**: `return $al.Ret`
- **append.array**: `append $station to array $exclude.array`
- **gosub**: `gosub Debug.Sub:`
- **label**: `Debug.Sub:`
- **endsub**: `endsub`
- **obj.add.units**: `= $station-> add $amount units of $ware`
- **wait.random**: `= wait randomly from 500 to 1000 ms`

## Fixtures

Known-good mod fixtures live under `tools/fixtures/known_good/<mod_name>`. Each mod
provides `src/scripts/*.x3s` as the canonical source along with any `t/` text pages
or optional `director/` XML. These fixtures are generated from `tools/fixtures/mods/<mod_name>`
via `python tools/convert_mods.py` and are used by the test suite.
