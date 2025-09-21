# Language Gotchas

This reference collects common pitfalls encountered when writing X3S scripts.

- #### Rule: `Copy array elements into scalar variables before reuse`
- **Full Description:** Inline array element access is only safe when directly assigning to or from a scalar variable. When you need an element for comparisons, arithmetic, or as an argument to another command, read the value into a standalone variable first and then use that variable.
- **Examples:**
  - `$_pct = $cfg[$MAX_PCT]`
  - `if $pct >= $_pct`
  - `$_amount = $dstEntry[$IDX_AMOUNT]`
  - `$dstEntry.amount = $_amount + $bestAmount`
  - `$dstEntry[$IDX_AMOUNT] = $dstEntry.amount`
  - `$src.sector = $src[$IDX_SECTOR]`
  - `$candDistance = get jumps from sector $src.sector to sector $dst.sector`
- **Edge Cases:** Command results must pass through a scalar variable before being written back into an array slot (for example, `$pct.value = null-> call script 'lib.slx.util' : function='Percent', part=$srcEntry[$IDX_AMOUNT], whole=$srcEntry[$IDX_CAP]` followed by `$srcEntry[$IDX_PCT] = $pct.value`).

- #### Rule: `Prefix returning commands with '=' when discarding the result`
- **Full Description:** Commands that yield a return value still require the `=` prefix when you do not capture that value. Omitting the prefix causes the command to be ignored at runtime.
- **Examples:**
  - `= wait 1 ms`
  - `= null-> call script 'lib.slx.query' : function='SetStationWareConfig', station=$station, ware=$ware, cfg=$cfg`
  - `= null-> call script 'lib.slx.query' : function='SetLastReason', station=$station, ware=$ware, code='BAL_OK'`
- **Edge Cases:** When you need the return value, assign it to a variable as usual (for example, `$result = [THIS]-> call script 'lib.slx.util' : ...`).

- #### Rule: `Quote script names and keep argument labels identifier-safe`
- **Full Description:** Script names passed to `call script` must be wrapped in single quotes, and named arguments cannot contain spaces or punctuation that would break identifier parsing. Use camelCase or underscores for multi-word labels.
- **Examples:**
  - `= [THIS]-> call script 'plugin.config.addscript' : PluginName=$menuTitle, Author=null, ScriptName='plugin.slx.station.menu', DisplayAuthor=[FALSE], AddToSection=$section, Menu=null`
- **Edge Cases:** Applying the same quoting rule to other commands that accept script names (such as interrupts) avoids ambiguous parsing.

- #### Rule: `Terminate gosub commands with ':'`
- **Full Description:** The `gosub` command requires a trailing colon. Leaving it off results in a syntax error when compiling the script.
- **Examples:**
  - `gosub ProcessWare:`
- **Edge Cases:** This applies to every label jump, even when the label name already ends with special characters.

- #### Rule: `Use bracketed script reference types for user input`
- **Full Description:** User-input commands expect their `type` parameter to be one of the engine's script reference tokens wrapped in brackets. Use the exact token text provided by the editor, including any embedded spaces.
- **Examples:**
  - `$station = null-> get user input: type=[Var/Ship/Station], title=$prompt`
  - `$destination = null-> get user input: type=[Var/Ship/Station owned by Player], title=$prompt`
  - `$min = null-> get user input: type=[Var/Number], title=$minPrompt`
- **Edge Cases:** Apply the same bracketed form to all script reference categories—copy the precise token from the script editor to avoid typos.

- #### Rule: `Pad sprintf fmt arguments with null placeholders`
- **Full Description:** The `sprintf: fmt=` variant always expects five argument slots. Provide `null` for any unused slot so the command parser can align the parameters correctly.
- **Examples:**
  - `$txt = sprintf: fmt='%s (Auto)', $txt, null, null, null, null`
- **Edge Cases:** When formatting more than one value, supply each argument in order and continue padding the remaining slots with `null`.

