# Flow Control Interrupt Optional Parameters

This reference tracks the optional arguments accepted by interrupt-based flow-control commands.

## `<RefObj> interrupt with script <Script Name> and priority <Var/Number>: arg1=<Value> arg2=<Value> arg3=<Value> arg4=<Value>`
- **arg1** – First optional value passed to the interrupted script. Commonly carries a position array or object reference (e.g. `$target.pos`).
- **arg2** – Second optional value. Use `null` when no additional data is needed.
- **arg3** – Third optional value provided to the script; set to `null` when unused.
- **arg4** – Fourth optional value. Typically omitted by setting it to `null` when the script only expects one argument.

## `<RefObj> interrupt task <Var/Number> with script <Script Name> and priority <Var/Number>: arg1=<Value0> arg2=<Value1> arg3=<Value2> arg4=<Value3>`
- **arg1** – First optional argument forwarded to the script that replaces the running task.
- **arg2** – Second optional argument available to the script.
- **arg3** – Third optional argument for additional context.
- **arg4** – Fourth optional argument for the task switch.
