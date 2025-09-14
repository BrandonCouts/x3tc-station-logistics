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

### New Statements Recognized
- **break**: `break`
- **continue**: `continue`
- **do.if**: `do if $Config[$Config.Debug.Enabled]`
- **resize.array**: `resize array $State to 30`
- **append.const**: `append 0 to array $Mins`
- **copy.array**: `copy array $Arg2 index 0 ... $Arg2.Length into array $rc at index $Arg1.Length`
- **return.int**: `return 0`
- **skip.if.any**: `skip if $rc >= 0`
- **write.log.printf**: `write to log file $PageId append=1 printf: fmt='New install', null, null`
- **write.logbook.printf**: `write to player logbook: printf: pageid=$PageId textid=$Id.Logbook.Installed, null, null`
- **set.command.upgrade**: `set script command upgrade: command=[GLEN_OK_TRADE]  upgrade=[TRUE]`
- **global.script.map**: `global script map: set: key=[GLEN_OK_TRADE], class=[Moveable Ship], race=[Player], script=glen.trade.ok.cmd, prio=0`
- **set.command.preload**: `set ship command preload script: command=[GLEN_OK_TRADE] script=glen.trade.ok.menu`
- **add.money**: `add money to player: $Cost`
- **set.script.command**: `set script command: [GLEN_OK_TRADE]`
- **send.message**: `send incoming message $Msg to player: display it=0`
- **play.sample**: `play sample 972`

### New Statements Recognized
- **menu.open.info**: `open custom info menu: title=$txt description=null option array=$menu maxoptions=2`
- **al.timer.vars**: `al engine: set plugin $plugin.ID timer interval to $interval s`
- **speak.text**: `= speak text: page=13 id=1276 priority=0`
- **speak.array**: `= speak array: $d prio=0`

### New Statements Recognized
- **send.message.literal**: `send incoming message 'ECS Not Detected - Comms with ships and stations will be disabled !' to player: display it=[TRUE]`
- **return.bool**: `return [TRUE]`
- **start.speak.text**: `START speak text: page=13 id=131 priority=0`
- **unregister.hotkey**: `unregister hotkey $hotkey.id`

### New Statements Recognized
- **gosub.label**: `gosub dodock`
- **send.message.var.bool**: `send incoming message $msg to player: display it=[TRUE]`
- **set.command.upgrade.software**: `set script command upgrade: command=ANARKIS_DOCKALL  upgrade=Carrier Command Software`
- **set.command.upgrade.bool**: `set script command upgrade: command=ANARKIS_STATIONDEFENSE  upgrade=[TRUE]`
- **global.script.map.simple**: `global script map: set: key=ANARKIS_DOCKALL, class=M1, race=Player, script=anarkis.acc.cmd.dock.all.pl, prio=0`
- **goto.label**: `goto label exit`
- **add.money.literal**: `add money to player: -50000`
- **menu.item.num**: `add custom menu item to array $menu: text=$dialog.yes returnvalue=1`
- **insert.array**: `insert $my.news into array $news.list at index 0`
- **copy.array.literal**: `copy array $setup index 0 ... 6 into array $config.to.update at index 0`
- **start.command.args**: `START $new.leader -> command $cmd.name : arg1=$arg1, arg2=$arg2, arg3=$arg3, arg4=null`

### New Statements Recognized
- **append.class**: `append M2 to array $class.list`
- **menu.value.selection**: `add value selection to menu: $menu, text=$st, value array=$sel.threat, default=$sel.threat.selection, return id=$sel.threat.id`

### New Statements Recognized
- **play.sample.named**: `play sample [IncomingTransmission.SOS]`
- **menu.item.textnum**: `add custom menu item to array $menu: text='1' returnvalue=1`

### New Statements Recognized
- **remove.array.elem.num**: `remove element from array $wing.array at index 0`
- **set.player.tracking.aim**: `set player tracking aim to $m.selected ->`
- **menu.item.enum**: `add custom menu item to array $menu: text=$st returnvalue=Carrier`

### New Statements Recognized
- **append.player**: `append Player to array $ignore`
- **append.null**: `append null to array $setup`

## Fixtures

Known-good mod fixtures live under `tools/fixtures/known_good/<mod_name>`. Each mod
provides `src/scripts/*.x3s` as the canonical source along with any `t/` text pages
or optional `director/` XML. These fixtures are generated from `tools/fixtures/mods/<mod_name>`
via `python tools/convert_mods.py` and are used by the test suite.

### New Statements Recognized
- **write.log.num**: `write to log file #8513  append=1  value=$m`
- **append.string**: `append 'anarkis.lib.cmd.attackland' to array $cmd`

### New Statements Recognized
- **append.race**: `append Argon to array $res`
- **append.station**: `append Military Outpost to array $military.types`
- **set.discovered.status**: `set discovered status: type=$race status=$show`
- **set.notoriety**: `set notoriety of $base.race -> $target.race to $new.noto points`
