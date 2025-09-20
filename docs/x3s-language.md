# X3S Language Reference

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
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> get global variable: name=<Var/String>`
- **Short Description:** Retrieves the value of a named global variable.
- **One Example:**
  - `$al.Settings = get global variable: name='al.LI.FDN.event'`
- **Edge Cases:** _None._

#### Rule: `set global variable: name=<Var/String> value=<Value>`
- **Short Description:** Sets or creates a global variable.
- **One Example:**
  - `set global variable: name=$var value=null`
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
  - `$settings.array = $factory-> get local variable: name=$pointer`
- **Edge Cases:** _None._

#### Rule: `<RefObj> set local variable: name=<Var/String> value=<Value>`
- **Short Description:** `<RefObj> set local variable: name=<Var/String> value=<Value>`
- **One Example:**
  - `$factory-> set local variable: name=$pointer value=$settings.array`
- **Edge Cases:** _None._

#### Rule: `<RetVar> read text: page=<Var/Number1> id=<Var/Number2>`
- **Short Description:** `<RetVar> read text: page=<Var/Number1> id=<Var/Number2>`
- **One Example:**
  - `$txt = read text: page=$PageID id=180`
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
  - `= $drone-> add $sell.amount units of $ware`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> sell ware <Var/Ware>`
- **Short Description:** Commands a ship to sell a ware from its cargo.
- **One Example:**
  - `$sold = $drone-> sell $sell.amount units of $ware`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> wait randomly from <Var/Number> to <Var/Number> ms`
- **Short Description:** Pauses script execution for a random duration within the specified range.
- **One Example:**
  - `= wait randomly from 500 to 1000 ms`
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

#### Rule: `add custom menu heading to array <Var/Array>: title=<Var/String>`
- **Short Description:** `add custom menu heading to array <Var/Array>: title=<Var/String>`
- **One Example:**
  - `add custom menu heading to array $menu: title=$txt`
- **Edge Cases:** _None._

#### Rule: `add custom menu heading to array <Var/Array>: page=<Var/Number1> id=<Var/Number2>`
- **Short Description:** `add custom menu heading to array <Var/Array>: page=<Var/Number1> id=<Var/Number2>`
- **One Example:**
  - `add custom menu heading to array $menu: page=$PageID id=157`
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
  - `$factory = $factory.array[$sf]`
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
  - `$s = size of array $sector.array`
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
  - `$sector.array = null-> call script 'plugin.LI.FDN.Sector.Array' : search=4`
- **Edge Cases:** _None._

#### Rule: `gosub <Label Name>:`
- **Short Description:** `gosub <Label Name>:`
- **One Example:**
  - `gosub Factory.Summary.Sub:`
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

#### Rule: `<RetVar/IF> <RefObj> get user input: type=<Script Reference Type>, title=<Var/String>`
- **Short Description:** `<RetVar/IF> <RefObj> get user input: type=<Script Reference Type>, title=<Var/String>`
- **One Example:**
  - `$destination = null-> get user input: type=[Var/Ship/Station owned by Player], title=$txt`
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
  - `write to log file $DebugID append=[TRUE] value=$txt`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> playing time`
- **Short Description:** `<RetVar/IF> playing time`
- **One Example:**
  - `$d.time = playing time`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> <RefObj> get tradeable ware array from station`
- **Short Description:** `<RetVar/IF> <RefObj> get tradeable ware array from station`
- **One Example:**
  - `$ware.Array = $station-> get tradeable ware array from station`
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
