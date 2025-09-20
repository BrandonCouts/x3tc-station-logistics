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
