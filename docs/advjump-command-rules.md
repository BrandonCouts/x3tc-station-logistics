# Advanced Jump Command Rules

This reference rebuilds the rule set exercised by the advanced jump command script. Each entry lists the core rule, an example pulled directly from the script, and notes describing how that example applies the command differently from the generic instruction.

## Flow Control Constructs

### `if <condition>`
- **Example**
  ```
  if !$advjump AND !$stdjump
  ```
- **Usage Note**: Combines two negated flags to guard the menu. Demonstrates that multiple Boolean checks can be chained with `AND` before entering the branch.

### `if not <object>-> is of class <Class>`
- **Example**
  ```
  if not $ship-> is of class [Ship]
  ```
- **Usage Note**: Uses `not` with an object-class test to detect wing controllers. Highlights that `is of class` returns a Boolean suitable for inversion.

### `else / else if`
- **Example**
  ```
  else if $ret == 'ftl'
  ```
- **Usage Note**: Shows that `else if` chains allow different menu return values to be handled without nesting separate `if` blocks.

### `while [TRUE]`
- **Example**
  ```
  while [TRUE]
  ```
- **Usage Note**: Creates a persistent menu loop. The script relies on early `return` statements to exit, underscoring that infinite loops must still provide termination paths.

### `for each <var> in array <array> using counter <index>`
- **Example**
  ```
  for each $wing.ship in array $aWingShips using counter $c
  ```
- **Usage Note**: Iterates wing members while tracking index `$c`. Demonstrates that `using counter` is optional but enables retrieving the original array slot for lookup later.

### `skip if <value>`
- **Example**
  ```
  skip if $jumps
  ```
- **Usage Note**: Checks whether `$jumps` evaluates to non-zero before skipping the next line, which resets `$jumps` to `0`. Shows how skip guards post-calculation corrections.

### `do if <condition>`
- **Example**
  ```
  do if $sector-> exists
  ```
- **Usage Note**: Uses inline `do if` to execute a single `return` when the user-selected sector is valid, avoiding a separate block.

### `return <value>`
- **Example**
  ```
  return [PLAYERSHIP]
  ```
- **Usage Note**: Returns either objects, arrays, or literal values from the menu handler depending on the branch that fires.

## Text and Formatting Rules

### `sprintf: fmt=<format>`
- **Example**
  ```
  $text = sprintf: fmt='%s (%s, %s, %s)', $sector, $x, $y, $z, null
  ```
- **Usage Note**: Illustrates literal format strings to build coordinate readouts. Only four placeholders are populated even though six parameters are accepted.

### `sprintf: pageid=<page> textid=<id>`
- **Example**
  ```
  $text = sprintf: pageid=$pageid textid=28, $sSector, null, null, null, null
  ```
- **Usage Note**: Pulls template text from the language file and injects a sector name. Demonstrates padding with `null` when fewer than five substitutions are needed.

### `read text: page=<page> id=<id>`
- **Example**
  ```
  $text = read text: page=$pageid id=3
  ```
- **Usage Note**: Loads localized menu labels. By swapping IDs inside conditionals, the script shows how to present advanced and standard variants with the same rule.

### `display subtitle text`
- **Example**
  ```
  display subtitle text: text=$text duration=5000 ms
  ```
- **Usage Note**: Broadcasts a five-second warning when neither jumpdrive is installed, demonstrating timed feedback before returning.

## Menu Construction Rules

### `create custom menu array`
- **Example**
  ```
  $menu = create custom menu array
  ```
- **Usage Note**: Initializes the container the script populates with headings, choices, and info lines before opening the menu.

### `add custom menu heading to array <menu>`
- **Example**
  ```
  add custom menu heading to array $menu: title=$text
  ```
- **Usage Note**: Inserts descriptive dividers at multiple points (mode selection, history). Highlights that headings can be repeated inside the same menu.

### `add custom menu item to array <menu>`
- **Examples**
  ```
  add custom menu item to array $menu: page=$pageid id=4 returnvalue='sector'
  add custom menu item to array $menu: text=$text returnvalue=$shipyard
  ```
- **Usage Note**: Shows both localized (`page`/`id`) and direct text entries, along with return values ranging from keywords to object references.

### `add custom menu info line to array <menu>`
- **Example**
  ```
  add custom menu info line to array $menu: page=2022 id=$cmd.id
  ```
- **Usage Note**: Mixes static blank separators with localized info rows to display jumpdrive requirements and wing inventories within the menu.

### `open custom menu`
- **Example**
  ```
  $ret = open custom menu: title=$title description=$text option array=$menu
  ```
- **Usage Note**: Launches the assembled menu, capturing the return value so the handler can branch on the player’s selection.

## Object and Data Retrieval Rules

### `get global variable: name='<id>'`
- **Examples**
  ```
  $pageid = get global variable: name='advjump.pageid'
  $lastPos = get global variable: name='advjump.lastpos'
  ```
- **Usage Note**: Pulls persistent state used to build history entries and resolve the language page.

### `<object>-> get sector`
- **Examples**
  ```
  $ship.sector = $ship-> get sector
  $sSector = $shipyard-> get sector
  ```
- **Usage Note**: Retrieves the current sector for ships and stations, enabling comparisons and text substitutions.

### `[PLAYERSHIP]-> get sector`
- **Example**
  ```
  $player.sector = [PLAYERSHIP]-> get sector
  ```
- **Usage Note**: Demonstrates calling commands on a global object constant to detect cross-sector jumps.

### `find station in galaxy`
- **Example**
  ```
  $shipyard = find station in galaxy: startsector=$ship.sector class or type=[Shipyard] race=null flags=$flags refobj=$ship serial=null max.jumps=100
  ```
- **Usage Note**: Searches galaxy-wide with combined flags for proximity, knowledge, and docking rights. Variants filter by different station classes.

### `get station array`
- **Example**
  ```
  $aStations = get station array: of race [Player] class/type=[Station]
  ```
- **Usage Note**: Collects player-owned stations to enable “My Stations” menu entries, verifying the array and its size before adding items.

### `size of array <array>`
- **Example**
  ```
  if size of array $aBeacons
  ```
- **Usage Note**: Confirms that helper scripts returned non-empty arrays before presenting selection options.

### `[THIS]-> call script '<name>'`
- **Examples**
  ```
  if [THIS]-> call script 'plugin.advjump.getsectors' :
  $aBeacons = [THIS]-> call script 'lib.cycrow.findbeacons' :
  ```
- **Usage Note**: Uses the calling ship as context when querying helper scripts for sector lists and beacon arrays.

### `<object>-> call script '<name>'`
- **Example**
  ```
  $eq = $ship-> call script 'lib.cycrow.findnearestproduct' : argument1={Energy Cells}
  ```
- **Usage Note**: Invokes a library script on the controlled ship to locate the nearest energy-cell supplier.

### `<object>-> exists`
- **Example**
  ```
  if $eq-> exists
  ```
- **Usage Note**: Guards menu additions and returns so the script never exposes stale references to deleted stations or sectors.

### `get flight wing ship array`
- **Example**
  ```
  $aWingShips = get flight wing ship array: wing=$ship
  ```
- **Usage Note**: Pulls wing membership when the caller is a wing leader, preparing the info section that lists their jumpdrive hardware.

### `create new array, arguments=<count>, ...`
- **Example**
  ```
  $text = create new array, arguments=20, $wing.ship, -1, {Advanced Jumpdrive}, null
  ```
- **Usage Note**: Reuses the info-line helper that expects an array payload. The script fills the first slots with ship and ware tokens while leaving the remainder empty.

### `sort array <array>`
- **Example**
  ```
  $aSectors = sort array $aSectors
  ```
- **Usage Note**: Sorts sectors returned from the helper script before presenting them in a menu, ensuring predictable ordering.

### `get user input`
- **Examples**
  ```
  $sector = $ship-> get user input: type=[Var/Sector], title=$text
  $gate = $ship-> get user input: type=[Var/Warpgate], title=$text
  ```
- **Usage Note**: Requests objects or coordinates from the player. Branches demonstrate how the requested type changes with the menu selection.

### `<sector>-> get user input`
- **Example**
  ```
  $pos = $sector-> get user input: type=[Var/Sector Position], title='sector position'
  ```
- **Usage Note**: Uses the chosen sector as context for acquiring coordinates before returning an array position.

### `$ship-> get name`
- **Example**
  ```
  $text = $ship-> get name
  ```
- **Usage Note**: Supplies the menu description, highlighting that info lines and titles may draw from object properties instead of text resources.

## Calculations and Inventory Rules

### `needed jump drive energy for jump`
- **Example**
  ```
  $needed = $ship-> needed jump drive energy for jump to sector $ship.sector
  ```
- **Usage Note**: Calculates the energy requirement for a same-sector jump to report how many jumps remain with the current fuel.

### `get true amount of ware <ware> in cargo bay`
- **Examples**
  ```
  $got = $ship-> get true amount of ware {Energy Cells} in cargo bay
  if $wing.ship-> get true amount of ware {Advanced Jumpdrive} in cargo bay
  ```
- **Usage Note**: Checks both consumables and equipment installations, driving the energy summary and wing hardware list.

### Arithmetic assignments
- **Example**
  ```
  $jumps = $got / $needed
  ```
- **Usage Note**: Performs integer division to estimate remaining jumps. The script immediately normalizes invalid results using `skip if`.

### Array indexing
- **Example**
  ```
  $sector = $lastPos[3]
  ```
- **Usage Note**: Extracts sector and coordinate components from a stored position array before formatting them for history entries.

## Constants and Literals

### `[TRUE]`, `[PLAYERSHIP]`, ware constants
- **Example**
  ```
  $isWing = [TRUE]
  return [PLAYERSHIP]
  ```
- **Usage Note**: Shows how predefined constants flag state (`[TRUE]`), reference the player’s ship, and identify wares such as `{Energy Cells}` within the rule system.

### String literals as return tokens
- **Example**
  ```
  add custom menu item to array $menu: page=$pageid id=4 returnvalue='sector'
  ```
- **Usage Note**: Confirms that return values can be arbitrary tokens (strings) that drive the later `else if` dispatch.

## User Interaction Outcomes

### `return null`
- **Example**
  ```
  if $ret == -1
  return null
  ```
- **Usage Note**: Cancels the command when the player closes the menu without making a selection, keeping the calling script safe.

### `return <object or array>`
- **Examples**
  ```
  return $gate
  return $ret
  ```
- **Usage Note**: Depending on the branch, the script returns gates, stations, sectors, coordinate arrays, or pass-through tokens, showing the flexibility of command outcomes.

