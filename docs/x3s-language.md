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
- **al.register.noquote**: `al engine: register script=al.LI.FDN.event`
- **inc**: `inc $sector.count =`
- **set.global.var.null**: `set global variable: name=$var value=null`
- **menu.info**: `add custom menu info line to array $menu: text=$txt`
- **menu.heading**: `add custom menu heading to array $menu: title=$txt`
- **menu.item**: `add custom menu item to array $menu: text=$txt returnvalue=$return.array`
- **menu.section**: `add section to custom menu: $menu`
- **menu.group.start**: `add new grouping to menu: $menu, text=$txt, open=$check`
- **menu.group.end**: `add end grouping to menu: $menu`
- **menu.nonselect**: `add non selectable menu item: $menu, text=$temp.array`
- **display.subtitle**: `display subtitle text: text=$txt duration=2000 ms`
- **menu.open**: `open custom menu: title=$txt description=null option array=$menu`
- **skip.if.eq**: `skip if $open.menu == 1`

## Fixtures

Known-good mod fixtures live under `tools/fixtures/known_good/<mod_name>`. Each mod
provides `src/scripts/*.x3s` as the canonical source along with any `t/` text pages
or optional `director/` XML. These fixtures are generated from `tools/fixtures/mods/<mod_name>`
via `python tools/convert_mods.py` and are used by the test suite.
