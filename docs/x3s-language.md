# X3S Language Reference

#### Rule: `Copy array elements into scalar variables before reuse`
- **Short Description:** Inline array access cannot be used inside conditions, arithmetic, or command arguments; read the value into a scalar first.
- **One Example:**
  - `$_pct = $cfg[$MAX_PCT]`
- **Edge Cases:** Store command results in scalars before writing them back into an array slot.

#### Rule: `Prefix returning commands with '=' when discarding the result`
- **Short Description:** Commands that return a value still require the `=` prefix when you ignore the result.
- **One Example:**
  - `= wait 1 ms`
- **Edge Cases:** Use standard assignments when you need the result (for example, `$value = [THIS]-> call script 'lib.slx.util' : ...`).

#### Rule: `Quote script names and keep argument labels identifier-safe`
- **Short Description:** Script names must be wrapped in quotes and argument labels cannot contain spaces.
- **One Example:**
  - `= [THIS]-> call script 'plugin.config.addscript' : PluginName=$menuTitle, Author=null, ScriptName='plugin.slx.station.menu', DisplayAuthor=[FALSE], AddToSection=$section, Menu=null`
- **Edge Cases:** Apply the same quoting to other script-name parameters such as interrupts.

#### Rule: `Terminate gosub commands with ':'`
- **Short Description:** Every `gosub` command must end with a colon.
- **One Example:**
  - `gosub ProcessWare:`
- **Edge Cases:** _None._

#### Rule: `Use bracketed script reference types for user input`
- **Short Description:** User-input commands require bracketed script reference tokens exactly as provided by the editor, even when the token contains spaces.
- **One Example:**
  - `$station = null-> get user input: type=[Var/Ship/Station owned by Player], title=$prompt`
- **Edge Cases:** Copy the bracketed token verbatim for other script reference categories to avoid typos.

#### Rule: `Pad sprintf fmt arguments with null placeholders`
- **Short Description:** The `sprintf: fmt=` variant expects five argument slots; fill unused slots with `null`.
- **One Example:**
  - `$txt = sprintf: fmt='%s (Auto)', $txt, null, null, null, null`
- **Edge Cases:** Continue padding with `null` after providing all required values.

#### Rule: `<RetVar/IF> <RefObj> exists`
- **Short Description:** `<RetVar/IF> <RefObj> exists`
- **One Example:**
  - `if $dock-> exists`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> get command`
- **Short Description:** `<RetVar/IF> <RefObj> get command`
- **One Example:**
  - `$target.command = $target-> get command`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> get command target`
- **Short Description:** `<RetVar/IF> <RefObj> get command target`
- **One Example:**
  - `$target.pos = $target-> get command target`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> get position as array`
- **Short Description:** `<RetVar/IF> <RefObj> get position as array`
- **One Example:**
  - `$target.pos = $target-> get position as array`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> get sector`
- **Short Description:** `<RetVar/IF> <RefObj> get sector`
- **One Example:**
  - `$target.sector = $target-> get sector`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> is of class <Var/Class>`
- **Short Description:** `<RetVar/IF> <RefObj> is of class <Var/Class>`
- **One Example:**
  - `if $target-> is of class [Moveable Ship]`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> is detectable`
- **Short Description:** `<RetVar/IF> <RefObj> is detectable`
- **One Example:**
  - `$detectable = $factory-> is detectable`
- **Edge Cases:** _None._

#### Rule: `append <Value> to array <Var/Array>`
- **Short Description:** `append <Value> to array <Var/Array>`
- **One Example:**
  - `append $format to array $menu`
- **Edge Cases:** _None._

#### Rule: `resize array <Var/Array> to <Var/Number>`
- **Short Description:** `resize array <Var/Array> to <Var/Number>`
- **One Example:**
  - `resize array $target.pos to 0`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> get jumps from sector <Var/Sector1> to sector <Var/Sector2>`
- **Short Description:** `<RetVar/IF> get jumps from sector <Var/Sector1> to sector <Var/Sector2>`
- **One Example:**
  - `$jumps.needed = get jumps from sector $this.sector to sector $target.sector`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> get amount of ware <Var/Ware> in cargo bay`
- **Short Description:** `<RetVar/IF> <RefObj> get amount of ware <Var/Ware> in cargo bay`
- **One Example:**
  - `if [THIS]-> get amount of ware {Advanced Jumpdrive} in cargo bay`
- **Edge Cases:** _None._

#### Rule: `<RefObj> interrupt with script <Script Name> and priority <Var/Number>: arg1=<Value> arg2=<Value> arg3=<Value> arg4=<Value>`
- **Short Description:** `<RefObj> interrupt with script <Script Name> and priority <Var/Number>: arg1=<Value> arg2=<Value> arg3=<Value> arg4=<Value>`
- **One Example:**
  - `[THIS]-> interrupt with script 'plugin.advjump.jump' and priority 40: arg1=$target.pos arg2=null arg3=null arg4=null`
- **Optional Parameter Definitions:** See [Flow Control Interrupt Optional Parameters](options/flow-control-interrupt-options.md).
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> get global variable: name=<Var/String>`
- **Short Description:** Retrieves the value of a named global variable.
- **One Example:**
  - `$config.Array = get global variable: name='config.scripts'`
- **Edge Cases:** _None._

#### Rule: `set global variable: name=<Var/String> value=<Value>`
- **Short Description:** Sets or creates a global variable.
- **One Example:**
  - `set global variable: name='al.LI.FDN.event' value=$al.Settings`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> get global variables: regular expression=<Var/String>`
- **Short Description:** `<RetVar/IF> get global variables: regular expression=<Var/String>`
- **One Example:**
  - `$glb.Array = get global variables: regular expression='FDND.*'`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> get name`
- **Short Description:** `<RetVar/IF> <RefObj> get name`
- **One Example:**
  - `$name = $object-> get name`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> get ID code`
- **Short Description:** `<RetVar/IF> <RefObj> get ID code`
- **One Example:**
  - `$id = $object-> get ID code`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> get local variable: name=<Var/String>`
- **Short Description:** `<RetVar/IF> <RefObj> get local variable: name=<Var/String>`
- **One Example:**
  - `$ware.array = $value-> get local variable: name=$pointer`
- **Edge Cases:** _None._

#### Rule: `<RefObj> set local variable: name=<Var/String> value=<Value>`
- **Short Description:** `<RefObj> set local variable: name=<Var/String> value=<Value>`
- **One Example:**
  - `$value-> set local variable: name=$pointer value=$ware.settings`
- **Edge Cases:** _None._

#### Rule: `<RetVar> read text: page=<Var/Number1> id=<Var/Number2>`
- **Short Description:** `<RetVar> read text: page=<Var/Number1> id=<Var/Number2>`
- **One Example:**
  - `$section = read text: page=$PageID id=101`
- **Edge Cases:** _None._

#### Rule: `<RetVar> sprintf: pageid=<Var/Number> textid=<Var/Number>, <Value0>, <Value1>, <Value2>, <Value3>, <Value4>`
- **Short Description:** `<RetVar> sprintf: pageid=<Var/Number> textid=<Var/Number>, <Value0>, <Value1>, <Value2>, <Value3>, <Value4>`
- **One Example:**
  - `$txt = sprintf: pageid=$PageID textid=2002, $factory.count, $product.count, $resource.count, null, null`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> find factory: buys <Var/Ware> with best price: min.price=<Var/Number1>, amount=<Var/Number2>, max.jumps=<Var/Number3>, startsector=<Var/Sector>, trader=<Var/Ship/Station>, exclude array=<Var/Array>`
- **Short Description:** Finds the best-price factory buying a ware from a given sector, honoring jump and exclusion limits.
- **One Example:**
  - `$sell.Station = find factory: buys $ware with best price: min.price=$sell.at, amount=null, max.jumps=0, startsector=$sector, trader=null, exclude array=$exclude.array`
- **Optional Parameter Definitions:** See [Station Trading Search Optional Parameters](options/station-trading-search-options.md).
- **Edge Cases:** _None._

#### Rule: `<RetVar> create ship: type=<Var/Ship Type> owner=<Var/Race> addto=<value> x=<Var/Number1> y=<Var/Number2> z=<Var/Number3>`
- **Short Description:** Spawns a ship of the specified type, owner, and position.
- **One Example:**
  - `$drone = create ship: type={Argon Mercury Super Freighter XL} owner=[Player] addto=$sell.Station x=null y=null z=null`
- **Edge Cases:** _None._

#### Rule: `<RefObj> set homebase to <Var/Ship/Station>`
- **Short Description:** Assigns a new homebase station for a ship.
- **One Example:**
  - `$drone-> set homebase to $dock`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> get relation to object <Var/Ship/Station>`
- **Short Description:** Returns the relation standing toward another object.
- **One Example:**
  - `$relation = $dock-> get relation to object $sell.Station`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> get max amount of ware <Var/Ware> that can be stored in cargo bay`
- **Short Description:** Retrieves the cargo capacity for a specific ware on a ship.
- **One Example:**
  - `$drone.max = $drone-> get max amount of ware $ware that can be stored in cargo bay`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> add <Var/Number> units of <Var/Ware>`
- **Short Description:** Adds a quantity of ware to a ship's cargo bay.
- **One Example:**
  - `= $value-> add $remove units of $ware`
- **Edge Cases:** _None._

#### Rule: `<RefObj> remove product from factory or dock: <Var/Ware>`
- **Short Description:** `<RefObj> remove product from factory or dock: <Var/Ware>`
- **One Example:**
  - `$value-> remove product from factory or dock: $ware`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> sell ware <Var/Ware>`
- **Short Description:** Commands a ship to sell a ware from its cargo.
- **One Example:**
  - `$sold = $drone-> sell $sell.amount units of $ware`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> wait randomly from <Var/Number> to <Var/Number> ms`
- **Short Description:** Pauses script execution for a random duration within the specified range.
- **One Example:**
  - `= wait randomly from 1000 to 2000 ms`
- **Edge Cases:** _None._

#### Rule: `<RefObj> destruct: show no explosion=<Var/Number>`
- **Short Description:** Destroys an object optionally hiding the explosion.
- **One Example:**
  - `$drone-> destruct: show no explosion=[TRUE]`
- **Edge Cases:** _None._

#### Rule: `<RetVar> get substring of <Var/String> offset=<Var/Number1> length=<Var/Number2>`
- **Short Description:** `<RetVar> get substring of <Var/String> offset=<Var/Number1> length=<Var/Number2>`
- **One Example:**
  - `$check = get substring of $var offset=0 length=5`
- **Edge Cases:** _None._

#### Rule: `<RetVar> create custom menu array: heading=<Var/String>`
- **Short Description:** `<RetVar> create custom menu array: heading=<Var/String>`
- **One Example:**
  - `$menu = create custom menu array: heading=$txt`
- **Edge Cases:** _None._

#### Rule: `add custom menu info line to array <value>: text=<Var/String>`
- **Short Description:** `add custom menu info line to array <value>: text=<Var/String>`
- **One Example:**
  - `add custom menu info line to array $menu: text=$txt`
- **Edge Cases:** _None._

#### Rule: `add custom menu item to array <value>: text=<Var/String> returnvalue=<value>`
- **Short Description:** `add custom menu item to array <value>: text=<Var/String> returnvalue=<value>`
- **One Example:**
  - `add custom menu item to array $menu: text=$txt returnvalue='switch.menu'`
- **Edge Cases:** _None._

#### Rule: `add custom menu heading to array <Var/Array>: title=<Var/String>`
- **Short Description:** `add custom menu heading to array <Var/Array>: title=<Var/String>`
- **One Example:**
  - `add custom menu heading to array $menu: title=$txt`
- **Edge Cases:** _None._

#### Rule: `add custom menu heading to array <Var/Array>: page=<Var/Number1> id=<Var/Number2>`
- **Short Description:** `add custom menu heading to array <Var/Array>: page=<Var/Number1> id=<Var/Number2>`
- **One Example:**
  - `add custom menu heading to array $menu: page=$PageID id=110`
- **Edge Cases:** _None._

#### Rule: `add custom menu info line to array <Var/Array>: page=<Var/Number1> id=<Var/Number2>`
- **Short Description:** `add custom menu info line to array <Var/Array>: page=<Var/Number1> id=<Var/Number2>`
- **One Example:**
  - `add custom menu info line to array $menu: page=$PageID id=119`
- **Edge Cases:** _None._

#### Rule: `add custom menu item to array <Var/Array>: page=<Var/Number1> id=<Var/Number2> returnvalue=<Value>`
- **Short Description:** `add custom menu item to array <Var/Array>: page=<Var/Number1> id=<Var/Number2> returnvalue=<Value>`
- **One Example:**
  - `add custom menu item to array $menu: page=$PageID id=158 returnvalue='product.all.on'`
- **Edge Cases:** _None._

#### Rule: `add section to custom menu: <Var/Array>`
- **Short Description:** `add section to custom menu: <Var/Array>`
- **One Example:**
  - `add section to custom menu: $menu`
- **Edge Cases:** _None._

#### Rule: `dim <Var/Array> = <Value> [, <Value> ] [, <Value> ] ... [, <Value> ]`
- **Short Description:** `dim <Var/Array> = <Value> [, <Value> ] [, <Value> ] ... [, <Value> ]`
- **One Example:**
  - `dim $return.array = 'show.factory', $s`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> = <Var/Array>[<Var/Number>]`
- **Short Description:** `<RetVar/IF> = <Var/Array>[<Var/Number>]`
- **One Example:**
  - `$script = $script.Array[0]`
- **Edge Cases:** _None._

#### Rule: `<Var/Array>[<Var/Number>] = <Value>`
- **Short Description:** `<Var/Array>[<Var/Number>] = <Value>`
- **One Example:**
  - `$settings.array[2] = 1`
- **Edge Cases:** _None._

#### Rule: `<RetVar> array alloc: size=<Var/Number>`
- **Short Description:** `<RetVar> array alloc: size=<Var/Number>`
- **One Example:**
  - `$factory.show.array = array alloc: size=$s`
- **Edge Cases:** _None._

#### Rule: `<RetVar> create new array, arguments=<Value0>, <Value1>, <Value2>, <Value3>, <Value4>`
- **Short Description:** `<RetVar> create new array, arguments=<Value0>, <Value1>, <Value2>, <Value3>, <Value4>`
- **One Example:**
  - `$format = create new array, arguments=$temp.array, $return.array, null, null, null`
- **Edge Cases:** _None._

#### Rule: `remove element from array <Var/Array> at index <Var/Number>`
- **Short Description:** `remove element from array <Var/Array> at index <Var/Number>`
- **One Example:**
  - `remove element from array $dock.array at index $s`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> reverse array <Value>`
- **Short Description:** `<RetVar/IF> reverse array <Value>`
- **One Example:**
  - `$factory.array = reverse array $factory.array`
- **Edge Cases:** _None._

#### Rule: `<RetVar> sort array <Value>`
- **Short Description:** `<RetVar> sort array <Value>`
- **One Example:**
  - `$factory.array = sort array $factory.array`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> size of array <Var/Array>`
- **Short Description:** `<RetVar/IF> size of array <Var/Array>`
- **One Example:**
  - `$s = size of array $config.Array`
- **Edge Cases:** _None._

#### Rule: `dec <Var>`
- **Short Description:** `dec <Var>`
- **One Example:**
  - `dec $s`
- **Edge Cases:** _None._

#### Rule: `inc <Var>`
- **Short Description:** `inc <Var>`
- **One Example:**
  - `inc $sector.count`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF/START> <RefObj> call script <Script Name> : [ arg1=<Value> arg2=<Value> ... arga=<Value> ]`
- **Short Description:** `<RetVar/IF/START> <RefObj> call script <Script Name> : [ arg1=<Value> arg2=<Value> ... arga=<Value> ]`
- **One Example:**
  - `START null-> call script 'plugin.LI.FDN.Menu.DC.Details_D' :`
- **Edge Cases:** _None._

#### Rule: `gosub <Label Name>:`
- **Short Description:** `gosub <Label Name>:`
- **One Example:**
  - `gosub Ware.User.Input.Sub:`
- **Edge Cases:** _None._

#### Rule: `endsub`
- **Short Description:** `endsub`
- **One Example:**
  - `endsub`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> get station array: of race <Var/Race> class/type=<value>`
- **Short Description:** `<RetVar/IF> get station array: of race <Var/Race> class/type=<value>`
- **One Example:**
  - `$dock.array = get station array: of race [Player] class/type=[Dock]`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> find station: sector=<Var/Sector> class or type=<value> race=<Var/Race> flags=<Var/Number> refobj=<value> maxdist=<Var/Number2> maxnum=<Var/Number> refpos=<Var/Array>`
- **Short Description:** `<RetVar/IF> find station: sector=<Var/Sector> class or type=<value> race=<Var/Race> flags=<Var/Number> refobj=<value> maxdist=<Var/Number2> maxnum=<Var/Number> refpos=<Var/Array>`
- **One Example:**
  - `$factory.array = find station: sector=$sector class or type=[Factory] race=[Player] flags=$flags refobj=null maxdist=null maxnum=999 refpos=null`
- **Edge Cases:** _None._

#### Rule: `<RetVar> format time: <Var/Number>`
- **Short Description:** `<RetVar> format time: <Var/Number>`
- **One Example:**
  - `$d.time = format time: $d.time`
- **Edge Cases:** _None._

#### Rule: `<RetVar> convert number <Var/Number> to string`
- **Short Description:** `<RetVar> convert number <Var/Number> to string`
- **One Example:**
  - `$min.txt = convert number $min to string`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> get user input: type=<Script Reference Type>, title=<Var/String>`
- **Short Description:** `<RetVar/IF> <RefObj> get user input: type=<Script Reference Type>, title=<Var/String>`
- **One Example:**
  - `$ware = null-> get user input: type=[Var/Ware], title=$txt`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> open custom info menu: title=<Var/String> description=<Var/String> option array=<Var/Array> maxoptions=<Var/Number>`
- **Short Description:** `<RetVar/IF> open custom info menu: title=<Var/String> description=<Var/String> option array=<Var/Array> maxoptions=<Var/Number>`
- **One Example:**
  - `$return = open custom info menu: title=$txt description=null option array=$menu maxoptions=2`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> open custom menu: title=<Var/String> description=<Var/String> option array=<Var/Array>`
- **Short Description:** `<RetVar/IF> open custom menu: title=<Var/String> description=<Var/String> option array=<Var/Array>`
- **One Example:**
  - `$return = open custom menu: title=$txt description=null option array=$menu`
- **Edge Cases:** _None._

#### Rule: `display subtitle text: text=<Var/String> duration=<Var/Number> ms`
- **Short Description:** `display subtitle text: text=<Var/String> duration=<Var/Number> ms`
- **One Example:**
  - `display subtitle text: text=$txt duration=2000 ms`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> get free amount of ware <Var/Ware> in cargo bay`
- **Short Description:** `<RetVar/IF> <RefObj> get free amount of ware <Var/Ware> in cargo bay`
- **One Example:**
  - `if not $destination-> get free amount of ware $ware in cargo bay`
- **Edge Cases:** _None._

#### Rule: `write to log file <Var/Number> append=<Var/Number> value=<Value>`
- **Short Description:** `write to log file <Var/Number> append=<Var/Number> value=<Value>`
- **One Example:**
  - `write to log file $DebugID append=[FALSE] value=$txt`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> playing time`
- **Short Description:** `<RetVar/IF> playing time`
- **One Example:**
  - `$d.time = playing time`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> get production cycle time: account for secondary resources=<Var/Number>`
- **Short Description:** `<RetVar/IF> <RefObj> get production cycle time: account for secondary resources=<Var/Number>`
- **One Example:**
  - `$full.time = $factory-> get production cycle time: account for secondary resources=[FALSE]`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> get remaining production cycle time`
- **Short Description:** `<RetVar/IF> <RefObj> get remaining production cycle time`
- **One Example:**
  - `$check.time = $factory-> get remaining production cycle time`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> get tradeable ware array from station`
- **Short Description:** `<RetVar/IF> <RefObj> get tradeable ware array from station`
- **One Example:**
  - `$ware.Array = $station-> get tradeable ware array from station`
- **Edge Cases:** _None._

#### Rule: `<RetVar> get average price of ware <Var/Ware>`
- **Short Description:** `<RetVar> get average price of ware <Var/Ware>`
- **One Example:**
  - `$avg = get average price of ware $ware`
- **Edge Cases:** _None._

#### Rule: `<RetVar> get max price of ware <Var/Ware>`
- **Short Description:** `<RetVar> get max price of ware <Var/Ware>`
- **One Example:**
  - `$max = get max price of ware $ware`
- **Edge Cases:** _None._

#### Rule: `<RetVar> get min price of ware <Var/Ware>`
- **Short Description:** `<RetVar> get min price of ware <Var/Ware>`
- **One Example:**
  - `$min = get min price of ware $ware`
- **Edge Cases:** _None._

#### Rule: `<RetVar> get maintype of ware <Var/Ware>`
- **Short Description:** `<RetVar> get maintype of ware <Var/Ware>`
- **One Example:**
  - `$main.t = get maintype of ware $ware`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> is equipment: ware=<Var/Ware>`
- **Short Description:** `<RetVar/IF> is equipment: ware=<Var/Ware>`
- **One Example:**
  - `if not is equipment: ware=$ware`
- **Edge Cases:** _None._
