# x3tc-station-logistics

SLX is a lightweight station-to-station logistics mod for X3TC: Terran Conflict. It moves wares between enrolled player stations (same- or cross-sector) via per-ware roles (Producer, Consumer, Store) with Min/Max/Chunk thresholds and a priority-based transfer loop.

## Reference Fixtures

Historical `.x3s` conversions from other mods live under `tools/fixtures/`. They demonstrate how different MSCI constructs map into our text format and provide architectural reference points. Treat them as pseudo code only: the commands and behaviors captured there are not linted and should not be considered authoritative.

Our canonical sources are the scripts in `src/scripts/`. When in doubt, align new work with the patterns that already ship in that directory.

## Testing

Run the consolidated test harness to lint the project and execute supporting unit tests:

```sh
python tools/test_x3s.py
```

The harness lints only the sources in `src/scripts/` before running the tests under `tools/tests/`. If you need to lint manually, call the linter directly:

```sh
python tools/x3s_lint.py src/scripts
```

## Repository Layout

- `src/scripts/` – primary `.x3s` sources for the mod.
- `t/` – in-game text resources (`89xxx-L044.xml`).
- `docs/` – language reference, ID allocations, and design notes.
- `tools/` – linter, tests, and historical fixture references.
- `prompts/` – internal development briefs.


# Station Logistics X3 (SLX)

## Overview
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

