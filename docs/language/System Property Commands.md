# System Property Commands

This reference lists system property commands available in X3TC scripting.

- `capture screen`
- `set monitor mode and viewpoint: monitor=<Var/Number> cockpit=<Var/Number> mode=<Var/Number> alpha=<Var/Number> beta=<Var/Number> gamma=<Var/Number> range=<Var/Number>`
- `<RetVar/IF> system date is month=<Var/Number1>, day=<Var/Number2>`
- `write to log file <Var/Number> append=<Var/Number> printf: fmt=<Var/String>, <Value0>, <Value1>, <Value2>, <Value3>, <Value4>`
- `write to log file <Var/Number> append=<Var/Number> printf: pageid=<Var/Number2> textid=<Var/Number3>, <Value0>, <Value1>, <Value2>, <Value3>, <Value4>`
- `write to log file <Var/Number> append=<Var/Number> value=<Value>`
- **Examples:**
  - `write to log file $DebugID append=[TRUE] value=$txt`
  - `write to log file $DebugID append=[FALSE] value=$txt`
- **Edge Cases:** _None._
