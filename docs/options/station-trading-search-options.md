# Station Trading Search Optional Parameters

Definitions for optional keywords shared by factory and dock search commands.

- **min.price / max.price** – Price filter for the ware. Use `min.price` when searching buyers and `max.price` when searching sellers.
- **amount** – Quantity of the ware the trader must be able to buy or sell.
- **max.jumps** – Maximum number of sector jumps allowed for the search.
- **startsector** – Sector used as the origin of the search algorithm.
- **trader** – Ship or station performing the trade; can be `null` when no trader is involved.
- **exclude array** – Array of stations or docks that should be ignored by the search.
