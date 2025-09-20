# Flow Control Commands

This reference covers flow control commands available in X3TC scripting. Each entry shows the basic syntax.

- `<RefObj> begin task <Var/Number> with script <Script Name> and priority <Var/Number>: arg1=<Value0> arg2=<Value1> arg3=<Value2> arg4=<Value3> arg5=<Value4>`
- `<RetVar/IF> <RefObj> call named script: script=<Var/String>, <Value>, <Value>, <Value>, <Value>, <Value>`
- `<RetVar/IF/START> <RefObj> call script <Script Name> : [ arg1=<Value> arg2=<Value> ... arga=<Value> ]`
- `START <RefObj> command <Object Command> : arg1=<Value>, arg2=<Value>, arg3=<Value>, arg4=<Value>`
- `START <RefObj> delayed command <Object Command> : arg1=<Value>, arg2=<Value>, arg3=<Value>, arg4=<Value>`
- `endsub`
- `gosub <Label Name>:`
- `goto label <Label Name>:`
- `<RefObj> interrupt task <Var/Number> with script <Script Name> and priority <Var/Number>: arg1=<Value0> arg2=<Value1> arg3=<Value2> arg4=<Value3>`
- `<RefObj> interrupt with script <Script Name> and priority <Var/Number>`
- #### Rule: `<RefObj> interrupt with script <Script Name> and priority <Var/Number>: arg1=<Value> arg2=<Value> arg3=<Value> arg4=<Value>`
- **Full Description:** `<RefObj> interrupt with script <Script Name> and priority <Var/Number>: arg1=<Value> arg2=<Value> arg3=<Value> arg4=<Value>`
- **Examples:**
  - `[THIS]-> interrupt with script 'plugin.advjump.jump' and priority 40: arg1=$target.pos arg2=null arg3=null arg4=null`
  - `[THIS]-> interrupt with script 'plugin.advjump.jump' and priority 40: arg1=$target.sector arg2=null arg3=null arg4=null`
- **Edge Cases:** _None._
- `<RefObj> launch named script: task=<Var/Number> scriptname=<Var/String> prio=<Var/Number>, <Value>, <Value>, <Value>, <Value>, <Value>`
- `<RetVar/IF> wait <Var/Number> ms`
- `<RetVar/IF> wait randomly from <Var/Number> to <Var/Number> ms`
- `START <RefObj> wing command <Var/Wing Command> : arg1=<Value>, arg2=<Value>, arg3=<Value>, arg4=<Value>`

