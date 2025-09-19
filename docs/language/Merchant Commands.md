# Merchant Commands

This reference covers merchant-related commands available in X3TC scripting. Each entry shows the basic syntax.

- `<RefObj> add merchant name=<Var/String> wanted wares=<Var/Array> owned wares=<Var/Array> cash=<Var/Number> rank=<Var/Number>`
- `<RetVar> get data for merchant <Var/String> : item number=<Var/Number>`
- `<RetVar> <RefObj> get merchants`
- `merchant <Var/String> got ware <Var/Ware> : quantity=<Var/Number>`
- `merchant <Var/String> sold ware <Var/Ware> : quantity=<Var/Number>`
- `remove merchant <Var/String>`
- `reset merchant <Var/String> expiry`
- `<RefObj> trademaster: add trader=<Value> to dock as merchant`
- `<RetVar> trademaster: is <Value> a trader`
- `<RetVar> trademaster: is trader=<Value> a merchant`
- `trademaster: remove trader=<Value> from dock`
- `<RetVar> trademaster order: find and register order for <Var/Ware>`
- `trademaster order: trader=<Value> delivery aborted`
- `trademaster order: trader=<Value> delivery of amount=<Var/Ware> successful`

