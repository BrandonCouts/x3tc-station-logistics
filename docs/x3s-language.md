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

#### Rule: `append <Value> to array <Var/Array>`
- **Short Description:** `append <Value> to array <Var/Array>`
- **One Example:**
  - `append $target.sector to array $target.pos`
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

#### Rule: `<RetVar> read text: page=<Var/Number1> id=<Var/Number2>`
- **Short Description:** `<RetVar> read text: page=<Var/Number1> id=<Var/Number2>`
- **One Example:**
  - `$txt = read text: page=$PageID id=103`
- **Edge Cases:** _None._

#### Rule: `<RetVar> sprintf: pageid=<Var/Number> textid=<Var/Number>, <Value0>, <Value1>, <Value2>, <Value3>, <Value4>`
- **Short Description:** `<RetVar> sprintf: pageid=<Var/Number> textid=<Var/Number>, <Value0>, <Value1>, <Value2>, <Value3>, <Value4>`
- **One Example:**
  - `$return = sprintf: pageid=$PageID textid=134, $name, $id, null, null, null`
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
  - `add custom menu info line to array $menu: text=$temp.array`
- **Edge Cases:** _None._

#### Rule: `add custom menu heading to array <Var/Array>: page=<Var/Number1> id=<Var/Number2>`
- **Short Description:** `add custom menu heading to array <Var/Array>: page=<Var/Number1> id=<Var/Number2>`
- **One Example:**
  - `add custom menu heading to array $menu: page=$PageID id=123`
- **Edge Cases:** _None._

#### Rule: `add custom menu info line to array <Var/Array>: page=<Var/Number1> id=<Var/Number2>`
- **Short Description:** `add custom menu info line to array <Var/Array>: page=<Var/Number1> id=<Var/Number2>`
- **One Example:**
  - `add custom menu info line to array $menu: page=$PageID id=119`
- **Edge Cases:** _None._

#### Rule: `add custom menu item to array <Var/Array>: page=<Var/Number1> id=<Var/Number2> returnvalue=<Value>`
- **Short Description:** `add custom menu item to array <Var/Array>: page=<Var/Number1> id=<Var/Number2> returnvalue=<Value>`
- **One Example:**
  - `add custom menu item to array $menu: page=$PageID id=128 returnvalue='master.reset'`
- **Edge Cases:** _None._

#### Rule: `dim <Var/Array> = <Value> [, <Value> ] [, <Value> ] ... [, <Value> ]`
- **Short Description:** `dim <Var/Array> = <Value> [, <Value> ] [, <Value> ] ... [, <Value> ]`
- **One Example:**
  - `dim $return.array = 'add.dc', $dock`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> = <Var/Array>[<Var/Number>]`
- **Short Description:** `<RetVar/IF> = <Var/Array>[<Var/Number>]`
- **One Example:**
  - `$PageID = $al.Settings[1]`
- **Edge Cases:** _None._

#### Rule: `<Var/Array>[<Var/Number>] = <Value>`
- **Short Description:** `<Var/Array>[<Var/Number>] = <Value>`
- **One Example:**
  - `$temp.array[0] = 1`
- **Edge Cases:** _None._

#### Rule: `<RetVar> array alloc: size=<Var/Number>`
- **Short Description:** `<RetVar> array alloc: size=<Var/Number>`
- **One Example:**
  - `$temp.array = array alloc: size=4`
- **Edge Cases:** _None._

#### Rule: `<RetVar> create new array, arguments=<Value0>, <Value1>, <Value2>, <Value3>, <Value4>`
- **Short Description:** `<RetVar> create new array, arguments=<Value0>, <Value1>, <Value2>, <Value3>, <Value4>`
- **One Example:**
  - `$format = create new array, arguments=$temp.array, $return.array, null, null, null`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF> size of array <Var/Array>`
- **Short Description:** `<RetVar/IF> size of array <Var/Array>`
- **One Example:**
  - `$s = size of array $dock.array`
- **Edge Cases:** _None._

#### Rule: `dec <Var>`
- **Short Description:** `dec <Var>`
- **One Example:**
  - `dec $s`
- **Edge Cases:** _None._

#### Rule: `<RetVar/IF/START> <RefObj> call script <Script Name> : [ arg1=<Value> arg2=<Value> ... arga=<Value> ]`
- **Short Description:** `<RetVar/IF/START> <RefObj> call script <Script Name> : [ arg1=<Value> arg2=<Value> ... arga=<Value> ]`
- **One Example:**
  - `$txt = [THIS]-> call script 'plugin.LI.FDN.Format.Name' : object=$dc`
- **Edge Cases:** _None._

#### Rule: `gosub <Label Name>:`
- **Short Description:** `gosub <Label Name>:`
- **One Example:**
  - `gosub Add.DC.Menu.Sub:`
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
