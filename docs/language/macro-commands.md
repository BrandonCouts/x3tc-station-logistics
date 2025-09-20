# Macro Commands

This reference lists macro commands available in X3TC scripting.

- #### Rule: `add custom menu heading to array <Var/Array>: page=<Var/Number1> id=<Var/Number2>`
- **Full Description:** `add custom menu heading to array <Var/Array>: page=<Var/Number1> id=<Var/Number2>`
- **Examples:**
  - `add custom menu heading to array $menu: page=$PageID id=123`
  - `add custom menu heading to array $menu: page=$PageID id=124`
  - `add custom menu heading to array $menu: page=$PageID id=125`
  - `add custom menu heading to array $menu: page=$PageID id=108`
  - `add custom menu heading to array $menu: page=$PageID id=126`
  - `add custom menu heading to array $menu: page=$PageID id=127`
- **Edge Cases:** _None._
- #### Rule: `add custom menu info line to array <Var/Array>: page=<Var/Number1> id=<Var/Number2>`
- **Full Description:** `add custom menu info line to array <Var/Array>: page=<Var/Number1> id=<Var/Number2>`
- **Examples:**
  - `add custom menu info line to array $menu: page=$PageID id=119`
  - `add custom menu info line to array $menu: page=$PageID id=129`
- **Edge Cases:** _None._
- #### Rule: `add custom menu item to array <Var/Array>: page=<Var/Number1> id=<Var/Number2> returnvalue=<Value>`
- **Full Description:** `add custom menu item to array <Var/Array>: page=<Var/Number1> id=<Var/Number2> returnvalue=<Value>`
- **Examples:**
  - `add custom menu item to array $menu: page=$PageID id=128 returnvalue='master.reset'`
- **Edge Cases:** _None._
- #### Rule: `dim <Var/Array> = <Value> [, <Value> ] [, <Value> ] ... [, <Value> ]`
- **Full Description:** `dim <Var/Array> = <Value> [, <Value> ] [, <Value> ] ... [, <Value> ]`
- **Examples:**
  - `dim $return.array = 'add.dc', $dock`
  - `dim $return.array = 'change.dc', $dock`
- **Edge Cases:** _None._
- `for <Var> = <Var/Number1> to <Var/Number2> step <Number>`
- `for each <Var> in array <Var/Array>`
- `for each <Var1> in array <Var/Array> using counter <Var2>`
