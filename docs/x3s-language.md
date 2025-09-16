# X3S Language

## Rules
- Arrays can only be indexed by numbers or numeric variables. String keys like $arr['foo'] are invalid.
- Script object constants (such as races or station classes) must be wrapped in square brackets, e.g., `get station array: of race [Player] class/type=[Station]`.
- See `x3s-races.md` for valid races and `x3s-stations.md` for station classes.

## Statements
Placeholders like `<var>` denote a variable.

- **write.log**: `write to log file $DebugID append=[FALSE] value=$txt`
- **dec**: `dec <var>`
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
- **wait.random**: `wait randomly from 500 to 1000 ms`
- **al.register.noquote**: `al engine: register script=al.LI.FDN.event`
- **inc**: `inc $sector.count`
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
- **menu.open.info**: `open custom info menu: title=$txt description=null option array=$menu maxoptions=2`
- **al.timer.vars**: `al engine: set plugin $plugin.ID timer interval to $interval s`
- **speak.text**: `= speak text: page=13 id=1276 priority=0`
- **speak.array**: `= speak array: $d prio=0`
- **send.message.literal**: `send incoming message 'ECS Not Detected - Comms with ships and stations will be disabled !' to player: display it=[TRUE]`
- **return.bool**: `return [TRUE]`
- **start.speak.text**: `START speak text: page=13 id=131 priority=0`
- **unregister.hotkey**: `unregister hotkey $hotkey.id`
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
- **append.class**: `append M2 to array $class.list`
- **menu.value.selection**: `add value selection to menu: $menu, text=$st, value array=$sel.threat, default=$sel.threat.selection, return id=$sel.threat.id`
- **play.sample.named**: `play sample [IncomingTransmission.SOS]`
- **menu.item.textnum**: `add custom menu item to array $menu: text='1' returnvalue=1`
- **remove.array.elem.num**: `remove element from array $wing.array at index 0`
- **set.player.tracking.aim**: `set player tracking aim to $m.selected ->`
- **menu.item.enum**: `add custom menu item to array $menu: text=$st returnvalue=Carrier`
- **append.player**: `append Player to array $ignore`
- **append.null**: `append null to array $setup`
- **write.log.num**: `write to log file #8513  append=1  value=$m`
- **append.string**: `append 'anarkis.lib.cmd.attackland' to array $cmd`
- **append.race**: `append Argon to array $res`
- **append.station**: `append Military Outpost to array $military.types`
- **set.discovered.status**: `set discovered status: type=$race status=$show`
- **set.notoriety**: `set notoriety of $base.race -> $target.race to $new.noto points`
- **find.station**: `$refobject = find station: sector=$sector class or type=Station race=$race flags=[Find.Random] refobj=null maxdist=null maxnum=1 refpos=null`
- **find.ship**: `$ship.list = find ship: sector=$sector class or type=Moveable Ship race=null flags=$flags refobj=$refobject maxdist=null maxnum=50 refpos=null`
- **size.of.array**: `$ship.count = size of array $ship.list`
- **create.station**: `$select = create station: type=$station.type owner=$race addto=$sector x=$x y=$y z=$z`
- **random.value**: `$p.face = = random value from 0 to 4 - 1`
- **array.alloc**: `$sel.role = array alloc: size=0`
- **menu.create**: `$menu = create custom menu array`
- **skip.if.find.array**: `skip if  find $plugin.id in array: $ecs.installed`
- **skip.if.datatyp**: `skip if  is datatyp[ $setup ] == DATATYP_ARRAY`
- **skip.if.not.var**: `skip if not $sound`
- **skip.if.var.exists**: `skip if $target -> exists`
- **skip.if.global.var**: `skip if get global variable: name='plugin.ecs.setup'`
- **skip.if.call.register**: `skip if [THIS] -> call script plugin.sk.ecs.register :  Setup Array=$setup`
- **skip.if.call.unregister**: `skip if [THIS] -> call script plugin.sk.ecs.unregister :  Plugin ID='plugin.ecs.dummy'`
- **skip.if.is.class**: `skip if $target -> is of class $plugin.config.class`
- **skip.if.not.eq.num**: `skip if not $mycount == 0`
- **array.get.index**: `$index =  get index of $plugin.id in array $ecs.installed offset=-1 + 1`
- **get.station.array.by.race**: `$arr = get station array: of race [Player] class/type=[Station]` — returns an array of stations filtered by race and class. The race token and station class must be bracketed. `class/type` accepts `[Station]`, `[Dock]`, `[Complex Hub]`, `[Shipyard]`, or `null`.
- **destruct.no.explosion**: `$s -> destruct: show no explosion=[TRUE]`

## Fixtures
Historical mod conversions live under `tools/fixtures/known_good/<mod_name>`. Each
mod folder mirrors the structure of a typical package (`src/scripts/*.x3s`, `t/`,
and optional `director/`). Treat these files as illustrative pseudo code only:
they are no longer linted by the automated test suite and may drift from the
current rule set. Use them as architectural references, not as definitive sources.

## Appendix: Lint Tokens

The linter's pattern rules share these reusable tokens:

- `<ws>` – `\s+`
- `<var>` – `$` followed by letters, numbers, underscores or dots
- `<ident>` – `[A-Za-z_][A-Za-z0-9_]*`
- `<number>` – signed integer value
- `<bool>` – `[TRUE]` or `[FALSE]`
- `<string>` – single-quoted MSCI string
- `<time_unit>` – `ms|s|sec|secs|seconds|m|min|mins|minutes`
- `<value>` – `<var>` / `<number>` / `<string>` / `<bool>`
- `<namedArg>` – `<ident> = <value>`
- `<expr>` – any expression (loose catch‑all)
- `<label>` – label name using letters, numbers, underscores or dots

Examples in `tools/x3s_rules.json` mirror the constructs described here to keep documentation and lint checks in sync.

