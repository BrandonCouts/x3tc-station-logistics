# SLX (Station Logistics for X3) – Spec (v0.2)

This version incorporates the clarified behavior for **Producers, Consumers, and Stores** as discussed.

---

## Core Goals
- Move wares **between enrolled player stations only** (same- and cross-sector).
- No NPC trade, no discovery, no satellites.
- Configuration is **station‑local** via CPC menu (and optionally later a station command).
- Per‑ware settings: **Role**, **Min %**, **Max %**, **Chunk %**.

### Roles
- **Producer** – makes a ware.
- **Consumer** – uses a ware.
- **Store** – buffers a ware (trade docks, EQ docks, complex hubs, etc.).

---

## Updated Behavioral Rules (Authoritative)

### Producers
- **Export down to Min**: Producers should attempt to export a ware until their stock reaches **Min%** (never below it).
- **If above Max**: Producers **prioritize exporting to Stores** first until they are ≤ **Max%**.
- **General Export**: After Store priority, Producers can export to Consumers up to Consumers’ **Max%**.

### Consumers
- **Import up to Max**: Consumers should import a ware until they reach **Max%**.
- **If below Min**: Consumers **prioritize importing from Stores** first until they are ≥ **Min%**.

### Stores
- **Passive buffer**: Stores may **import and export**, but they always respect their own **Min/Max** and act **last** in scheduling after Producer→Store and Store→Consumer priorities are handled.

---

## Transfer Order per Tick (per Ware)
1. **Producer → Store (P→S) – Surplus bleed**
   - Trigger: Producer stock > **Max%**.
   - Action: Export toward Producer **Max%** (not below **Min%**) into Stores without pushing Stores over **Max%**.
2. **Store → Consumer (S→C) – Shortage fill**
   - Trigger: Consumer stock < **Min%**.
   - Action: Import from Stores (not below Store **Min%**) at least up to Consumer **Min%**.
3. **Producer → Consumer (P→C) – General balancing**
   - Trigger: Producer stock > **Min%** and Consumer stock < **Max%**.
   - Action: Move toward Producer **Min%** and Consumer **Max%**.
4. **Store balancing** (lowest priority)
   - Stores above **Max%** may export to Consumers below **Max%**.
   - Producers above **Min%** may top up Stores below **Min%**.

> **Chunk % cap** applies to **both source and target**: the transfer amount per move is `min(source_chunk_cap, target_chunk_cap, available_to_send, room_to_fill)`.

---

## Preferences & Constraints
- **Same‑sector first**, then cross‑sector if no suitable same‑sector match exists.
- Never move a ware if the action would violate **source Min%** or **target Max%**.
- Ties are broken by: (1) same‑sector, (2) lowest target % first, (3) highest source % first, (4) shortest jump distance.

---

## Configuration UI (CPC)
- **Plugin Config → SLX → Station Logistics** → choose station → per‑ware editor.
- Row fields: **Role | Min% | Max% | Chunk% | Status/Reason**.
- Status shows last decision (e.g., "At Min (no export)", "No store headroom", "Filled to Max").

---

## Data Model (per station, per ware)
```
slx.enrolled                [bool]
slx.ware.role               ['producer'|'consumer'|'store'|'auto']
slx.ware.min_pct            [int 0..100]
slx.ware.max_pct            [int 0..100]
slx.ware.chunk_pct          [int 1..100]
slx.ware.last_reason        [string]
```

---

## Scheduler
- Lightweight manager tick (~10s). Evaluates each ware with the **Transfer Order** above.
- Moves are atomic and obey **Chunk%**; multiple moves may occur across ticks until equilibrium is reached.

---

## Out of Scope (intentionally)
- NPC trading (buy/sell), price management, satellite scanning, or automatic station discovery.
- Player ships are not required for transfers; movement is internal/instant.

---

## Next Steps
- Flesh out per‑ware editor actions in `plugin.slx.Station.Menu`.
- Implement `plugin.slx.Manager.Tick` with the priority order above.
- Add a debug overlay showing **why** a transfer was skipped.

