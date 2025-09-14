"""Unit-style tests for station logistics transfers.

These tests simulate simple station inventories and ensure that
transfer helpers respect chunk sizes and reason codes.  Engine
dependencies are avoided by providing mock implementations of the
`lib.slx.transfer` and `lib.slx.query` modules.
"""

from __future__ import annotations

import importlib
import sys
import types
import unittest

# ---------------------------------------------------------------------------
# Mock modules
# ---------------------------------------------------------------------------

# Create package structure: lib -> slx -> (transfer, query)
lib_mod = types.ModuleType("lib")
slx_mod = types.ModuleType("lib.slx")
lib_mod.slx = slx_mod
sys.modules.setdefault("lib", lib_mod)
sys.modules.setdefault("lib.slx", slx_mod)

transfer_mod = types.ModuleType("lib.slx.transfer")
query_mod = types.ModuleType("lib.slx.query")
sys.modules["lib.slx.transfer"] = transfer_mod
sys.modules["lib.slx.query"] = query_mod


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

class Station:
    """Minimal station with inventory and config state."""

    def __init__(self, name: str, sector: str, capacity: dict, inventory: dict, configs: dict):
        self.name = name
        self.sector = sector
        self.capacity = capacity
        self.inventory = inventory
        self.configs = configs
        self.last_reason: dict = {}


# ---------------------------------------------------------------------------
# lib.slx.query mocks
# ---------------------------------------------------------------------------


def get_station_ware_config(station: Station, ware: str) -> dict:
    return station.configs[ware]


def get_station_ware_pct(station: Station, ware: str) -> float:
    return station.inventory[ware] * 100 / station.capacity[ware]


def get_sector(station: Station) -> str:
    return station.sector


def set_last_reason(station: Station, ware: str, text: str) -> None:
    station.last_reason[ware] = text


query_mod.GetStationWareConfig = get_station_ware_config
query_mod.GetStationWarePct = get_station_ware_pct
query_mod.GetSector = get_sector
query_mod.SetLastReason = set_last_reason


# ---------------------------------------------------------------------------
# lib.slx.transfer mocks
# ---------------------------------------------------------------------------


def can_move(src: Station, dst: Station, ware: str, amount: float) -> bool:
    src_cfg = query_mod.GetStationWareConfig(src, ware)
    dst_cfg = query_mod.GetStationWareConfig(dst, ware)
    src_new = (src.inventory[ware] - amount) * 100 / src.capacity[ware]
    dst_new = (dst.inventory[ware] + amount) * 100 / dst.capacity[ware]
    if src_new < src_cfg["min_pct"]:
        return False
    if dst_new > dst_cfg["max_pct"]:
        return False
    return True


def apply_move(src: Station, dst: Station, ware: str, amount: float) -> None:
    src.inventory[ware] -= amount
    dst.inventory[ware] += amount


transfer_mod.CanMove = can_move
transfer_mod.ApplyMove = apply_move


# Import the mocks so tests can reference them
transfer = importlib.import_module("lib.slx.transfer")
query = importlib.import_module("lib.slx.query")


# ---------------------------------------------------------------------------
# Helper implementing producer->store logic similar to X3 script
# ---------------------------------------------------------------------------


def producer_to_store(src: Station, dst: Station, ware: str) -> float:
    """Simulate the producer logic transferring ware to a store."""

    cfg = query.GetStationWareConfig(src, ware)
    dst_cfg = query.GetStationWareConfig(dst, ware)

    src_amt = src.inventory[ware]
    src_cap = src.capacity[ware]
    dst_amt = dst.inventory[ware]
    dst_cap = dst.capacity[ware]

    src_chunk = src_cap * cfg["chunk_pct"] / 100
    dst_chunk = dst_cap * dst_cfg["chunk_pct"] / 100
    available = src_amt - (cfg["max_pct"] * src_cap / 100)
    room = (dst_cfg["max_pct"] * dst_cap / 100) - dst_amt

    amount = min(src_chunk, dst_chunk, available, room)
    if amount > 0 and transfer.CanMove(src, dst, ware, amount):
        transfer.ApplyMove(src, dst, ware, amount)
        query.SetLastReason(src, ware, "P2S")
        query.SetLastReason(dst, ware, "P2S_RECV")
        return amount

    query.SetLastReason(src, ware, "NO_STORE")
    return 0


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TransferTests(unittest.TestCase):
    def setUp(self) -> None:
        self.producer = Station(
            "prod",
            "A",
            capacity={"e": 1000},
            inventory={"e": 900},
            configs={"e": {"role": "producer", "min_pct": 20, "max_pct": 80, "chunk_pct": 20}},
        )
        self.store = Station(
            "store",
            "A",
            capacity={"e": 1000},
            inventory={"e": 100},
            configs={"e": {"role": "store", "min_pct": 0, "max_pct": 90, "chunk_pct": 10}},
        )

    def test_can_move_respects_limits(self) -> None:
        # Moving too much drops producer below its minimum percentage.
        self.assertFalse(transfer.CanMove(self.producer, self.store, "e", 800))

        # Reasonable amount succeeds.
        self.assertTrue(transfer.CanMove(self.producer, self.store, "e", 100))

        # Destination cannot exceed its maximum percentage.
        self.store.inventory["e"] = 850
        self.assertFalse(transfer.CanMove(self.producer, self.store, "e", 100))

    def test_producer_to_store_chunk_and_reasons(self) -> None:
        amt = producer_to_store(self.producer, self.store, "e")
        self.assertEqual(amt, 100)
        self.assertEqual(self.producer.inventory["e"], 800)
        self.assertEqual(self.store.inventory["e"], 200)
        self.assertEqual(self.producer.last_reason["e"], "P2S")
        self.assertEqual(self.store.last_reason["e"], "P2S_RECV")

    def test_no_room_sets_reason_code(self) -> None:
        self.store.inventory["e"] = 900  # Store already full
        amt = producer_to_store(self.producer, self.store, "e")
        self.assertEqual(amt, 0)
        self.assertEqual(self.producer.last_reason["e"], "NO_STORE")
        self.assertNotIn("e", self.store.last_reason)


if __name__ == "__main__":  # pragma: no cover - allow standalone execution
    unittest.main()

