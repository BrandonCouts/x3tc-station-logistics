# Station Property Commands

This reference covers station property commands available in X3TC scripting. Each entry shows the basic syntax.

- `<RetVar/IF> <RefObj> can buy ware <Var/Ware>`
- `<RetVar/IF> <RefObj> can sell ware <Var/Ware>`
- `<RetVar/IF> <RefObj> get average price of station ware <Var/Ware>`
- `<RetVar/IF> <RefObj> get best store amount of ware <Var/Ware>`
- `<RetVar/IF> <RefObj> get intermediates buyable`
- `<RetVar/IF> <RefObj> get intermediates sellable`
- `<RetVar/IF> <RefObj> get max. store amount of ware <Var/Ware>`
- `<RetVar/IF> <RefObj> get money`
- `<RetVar/IF> <RefObj> get number of primary resources`
- `<RetVar/IF> <RefObj> get number of products per cycle`
- `<RetVar/IF> <RefObj> get number of resources`
- `<RetVar> <RefObj> get number of resources per cycle for ware <Var/Ware>`
- `<RetVar/IF> <RefObj> get number of secondary resources`
- `<RetVar/IF> <RefObj> get production cycle time: account for secondary resources=<Var/Number>`
- `<RetVar/IF> <RefObj> get production status: as percentage=<Var/Number>`
- `<RetVar/IF> <RefObj> get products`
- `<RetVar/IF> <RefObj> get product ware`
- `<RetVar/IF> <RefObj> get remaining production cycle time`
- `<RetVar/IF> <RefObj> get serial name of station`
- #### Rule: `<RetVar/IF> <RefObj> get tradeable ware array from station`
- **Full Description:** `<RetVar/IF> <RefObj> get tradeable ware array from station`
- **Examples:**
  - `$ware.Array = $station-> get tradeable ware array from station`
- **Edge Cases:** _None._
- `<RetVar/IF> <RefObj> is docking possible of <Value>`
- `<RetVar/IF> <RefObj> is military outpost`
- `<RetVar/IF> <RefObj> only player own ships can trade with`
- `<RefObj> set intermediates buyable to <Var/Number>`
- `<RefObj> set intermediates sellable to <Var/Number>`
- `<RefObj> set price of ware <Var/Ware> to <Var/Number> cr`
- `<RefObj> set serial name of station to <Var/Stations Serial>`
- `<RetVar> station <Var/Station>: is ware <Var/Ware> for race <Var/Race> locked`
- `<RetVar/IF> <RefObj> trades with ware <Var/Ware>`
- `<RetVar/IF> <RefObj> uses ware <Var/Ware> as primary resource`
- `<RetVar/IF> <RefObj> uses ware <Var/Ware> as product`
- `<RetVar/IF> <RefObj> uses ware <Var/Ware> as secondary resource`
