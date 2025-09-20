# String Commands

This reference lists string commands available in X3TC scripting.

- `<RetVar> convert number <Var/Number> to string`
- `<RetVar> find position of pattern <Var/String1> in <Var/String2>`
- `<RetVar> format seconds=<Var/String> to Zura time string`
- `<RetVar> format time: <Var/Number>`
- `<RetVar/IF> get length of string <Var/String>`
- `<RetVar/IF> get string font length: <Var/String>`
- #### Rule: `<RetVar> get substring of <Var/String> offset=<Var/Number1> length=<Var/Number2>`
- **Full Description:** `<RetVar> get substring of <Var/String> offset=<Var/Number1> length=<Var/Number2>`
- **Examples:**
  - `$check = get substring of $var offset=0 length=5`
- **Edge Cases:** _None._
- `<RetVar/IF> get text id: ware=<Var/Ware>`
- `load text: id=<Var/Number>`
- `<RetVar/IF> match regular expression: <Var/String1> to string <Var/String2>`
- #### Rule: `<RetVar> read text: page=<Var/Number1> id=<Var/Number2>`
- **Full Description:** `<RetVar> read text: page=<Var/Number1> id=<Var/Number2>`
- **Examples:**
  - `$txt = read text: page=$PageID id=103`
- **Edge Cases:** _None._
- `<RetVar/IF> read text: page id=<Var/Number1>, from <Var/Number2> to <Var/Number3> to array, include empty=<Var/Number4>`
- `<RetVar/IF> read text: page id=<Var/Number>, id=<Var/Number> exists`
- `<RetVar> sprintf: fmt=<Var/String>, <Value0>, <Value1>, <Value2>, <Value3>, <Value4>`
- #### Rule: `<RetVar> sprintf: pageid=<Var/Number> textid=<Var/Number>, <Value0>, <Value1>, <Value2>, <Value3>, <Value4>`
- **Full Description:** `<RetVar> sprintf: pageid=<Var/Number> textid=<Var/Number>, <Value0>, <Value1>, <Value2>, <Value3>, <Value4>`
- **Examples:**
  - `$return = sprintf: pageid=$PageID textid=134, $name, $id, null, null, null`
- **Edge Cases:** _None._
- `<RetVar> string <Var/String> to integer`
- `<RetVar> substitute in string <Var/String1>: pattern <Var/String2> with <Var/String3>`
