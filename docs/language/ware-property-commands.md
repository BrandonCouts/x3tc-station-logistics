# Ware Property Commands

This reference lists ware property commands available in X3TC scripting.

- `<RetVar> get average price of ware <Var/Ware>`
- #### Rule: `<RetVar> get maintype of ware <Var/Ware>`
- **Full Description:** `<RetVar> get maintype of ware <Var/Ware>`
- **Examples:**
  - `$main.t = get maintype of ware $ware`
- **Edge Cases:** _None._
- `<RetVar> get max price of ware <Var/Ware>`
- `<RetVar> get max price of ware <Var/Ware> as secondary resource`
- `<RetVar> get min price of ware <Var/Ware>`
- `<RetVar> get min price of ware <Var/Ware> as secondary resource`
- `<RetVar> get missile flags of <Var/Ware>`
- `<RetVar/IF> <RefObj> get price of ware <Var/Ware>`
- `<RetVar> get relvalue of <Var/Ware>`
- `<RetVar> get subtype of ware <Var/Ware>`
- `<RetVar> get transport class of ware <Var/Ware>`
- `<RetVar> get volume of ware <Var/Ware>`
- `<RetVar> get ware from maintype <Var/Number1> and subtype <Var/Number2>`
- #### Rule: `<RetVar/IF> is equipment: ware=<Var/Ware>`
- **Full Description:** `<RetVar/IF> is equipment: ware=<Var/Ware>`
- **Examples:**
  - `if not is equipment: ware=$ware`
- **Edge Cases:** _None._
- `<RetVar/IF> is inventory: ware=<Var/Ware>`
- `<RetVar/IF> is upgrade: ware=<Var/Ware>`
- `<RetVar/IF> is ware <Var/Ware> illegal in <Var/Race> sectors`
