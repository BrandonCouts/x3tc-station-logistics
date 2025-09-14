# Station Logistics X3 (SLX)

SLX moves wares instantly between player-owned stations using simple per-ware rules.
It ignores NPC trading and focuses purely on balancing your own production network.

## Install
1. Copy the contents of `src/scripts` to your X3TC `scripts/` directory.
2. Copy the files in `t/` to your game `t/` directory.
3. Start or reload your game; the setup script will register SLX.

## How it works
- Enroll a station via Plugin Config > SLX > Station Logistics.
- Each ware can be set as **Producer**, **Consumer**, or **Store** with Min/Max/Chunk limits.
- A manager task runs roughly every 10 seconds and transfers wares in priority order:
    1. Producer -> Store when above Max%.
    2. Store -> Consumer when Consumer below Min%.
    3. Producer -> Consumer when Producer above Min% and Consumer below Max%.
    4. Store balancing last.
- Transfers occur instantly without ships and respect each station's limits.
- The station menu displays the last transfer reason for each ware.

