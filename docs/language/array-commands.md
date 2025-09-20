# Array Commands

This reference lists array commands available in X3TC scripting.

- `<RetVar/IF> = <Var/Array>[<Var/Number>]`
- `<RetVar/IF> = <Var/Array>[<Var/Number1>][<Var/Number2>]`
- `<Var/Array>[<Var/Number1>][<Var/Number2>] = <Value>`
- `<Var/Array>[<Var/Number>] = <Value>`
- `<Var/Array1>[<Var/Number1>] = <Var/Array2>[<Var/Number2>]`
- #### Rule: `append <Value> to array <Var/Array>`
- **Full Description:** `append <Value> to array <Var/Array>`
- **Examples:**
  - `append $target.sector to array $target.pos`
  - `append $target.sector to array $target.pos`
  - `append 0 to array $target.pos`
  - `append 0 to array $target.pos`
  - `append 0 to array $target.pos`
  - `append $target to array $target.pos`
- **Edge Cases:** _None._
- `<RetVar> array alloc: size=<Var/Number>`
- `<RetVar/IF> arrays <Value1> and <Value2> are equal`
- `<RetVar> clone array <Var/Array> : index <Var/Number1> ... <Var/Number2>`
- `copy array <Var/Array1> index <Var/Number1> ... <Var/Number2> into array <Var/Array2> at index <Var/Number3>`
- `<RetVar> create new array, arguments=<Value0>, <Value1>, <Value2>, <Value3>, <Value4>`
- `<RetVar/IF> find <Value> in array: <Value>`
- `<RetVar> get index of <Value> in array <Var/Array> offset=<Var/Number>`
- `<RetVar/IF> <RefObj> get object name array`
- `insert <Value> into array <Var/Array> at index <Var/Number>`
- `remove element from array <Var/Array> at index <Var/Number>`
- #### Rule: `resize array <Var/Array> to <Var/Number>`
- **Full Description:** `resize array <Var/Array> to <Var/Number>`
- **Examples:**
  - `resize array $target.pos to 0`
- **Edge Cases:** _None._
- `<RetVar/IF> reverse array <Value>`
- `<RetVar/IF> size of array <Var/Array>`
- `<RetVar> sort array <Value>`
- `<RetVar> sort array: data=<Value> sort values=<Value>`
