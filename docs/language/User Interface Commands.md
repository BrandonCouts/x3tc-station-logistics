# User Interface Commands

This reference covers user interface-related commands available in X3TC scripting. Each entry shows the basic syntax.

- `add custom menu heading to array <value>: title=<Var/String>`
- `add custom menu info line to array <value>: text=<Var/String>`
- `add custom menu item to array <value>: text=<Var/String> returnvalue=<value>`
- `add section to custom menu: <Var/Array>`
- `add value selection to menu: <Var/Array>, text=<Var/String>, value array=<Var/Array>, default=<Var/Number>, return id=<Var/String>`
- `<RetVar> create custom menu array`
- `<RetVar> create custom menu array, info lines=<Var/String>, <Var/String>, <Var/String>, <Var/String>`
- `<RetVar> create custom menu array: heading=<Var/String>`
- `<RetVar> create text for custom menu, left=<Var/String>, right=<Var/String>`
- `display subtitle text: text=<Var/String> duration=<Var/Number> ms`
- `<RetVar/IF> <RefObj> get user input: type=<Script Reference Type>, title=<Var/String>`
- `<RetVar/IF> <RefObj> get user input <Script Reference Type>, title=<Var/String>, sector=<Var/Sector>`
- `<RetVar/IF> get user input without sector type=<Script Reference Type>, title=<Var/String>`
- `<RetVar/IF> open custom info menu: title=<Var/String> description=<Var/String> option array=<Var/Array> maxoptions=<Var/Number>`
- `<RetVar/IF> open custom menu: title=<Var/String> description=<Var/String> option array=<Var/Array>`
- `play sample <Var/Number>`
- `play sample: incoming transmission <Var/Number>, from object <value>`
- `<RefObj> send audio message <Var/Number> to player`
- `<RefObj> send incoming message: text=<Var/String> temporary=<Var/Number>`
- `send incoming message <Var/String> to player: display it=<Var/Number>`
- `send incoming question <Var/String> to player: script=<Script Name>`
- `send incoming message <Var/String> to player: callback=<Script Name> flags=<Var/Number>`
- `<RetVar/> <RefObj> serialise object`
- `<RetVar/IF/START> speak array: <value> prio=<Var/Number>`
- `<RetVar/IF/START> speak text: page=<Var/Number> textid=<Var/Number> priority=<Var/Number>`
- `<RefObj> write to logbook <value>`
- `write to player logbook <value>`
- `write to player logbook: printf: fmt=<Var/String>, <Value0>, <Value1>, <Value2>, <Value3>, <Value4>`
- `write to player logbook: printf: pageid=<Var/Number> textid=<Var/Number>, <Value0>, <Value1>, <Value2>, <Value3>, <Value4>`
