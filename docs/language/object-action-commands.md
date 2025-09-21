# Object Action Commands

This reference lists object-related action commands available in X3TC scripting. Each entry shows the basic syntax.

- `<RefObj> add lasers per value=<Var/Number> flags=<Var/Number>`
- `<RefObj> add shields per value=<Var/Number>`
- `<RefObj> destroy object: killer=<value>, show no explosion=<Var/Number>`
- `<RefObj> destruct: show no explosion=<Var/Number>`
- **Examples:**
  - `$drone-> destruct: show no explosion=[TRUE]`
- **Edge Cases:** _None._
- `<RefObj> force position: x=<Var/Number> y=<Var/Number> z=<Var/Number>`
- `<RefObj> put into environment <RefObj>`
- `<RefObj> send signal <Object Signal> : arg1=<value>, arg2=<value>, arg3=<value>, arg4=<value>`
- `<RefObj> set command: <Object Command> target=<value> target2=<value> par1=<value> par2=<value>`

