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
