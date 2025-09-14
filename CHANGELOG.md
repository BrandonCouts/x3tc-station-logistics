# Changelog

## 0.1.5-internal
- Removed unused call to nonexistent `plugin.slx.Wares` from setup script.
- Added reason codes for store balancing and filled-to-max events with supporting text.
- Transfer logic now sets these codes when moves exhaust headroom or balance stores.

## 0.1.4-internal
- Manager tick now runs continuously every ~10 seconds.

## 0.1.3-internal
- Added station enrollment toggle with default ware settings.
- Fixed menu row formatting for per-ware display.

## 0.1.2-internal
- Added init script to register plugin config and launch manager.
- Implemented station configuration menu for per-ware settings.

## 0.1.1-internal
- Added manager tick script to balance wares between stations.
- Introduced basic status reason strings and formatter.

## 0.1.0-internal
- Initial scaffolding: documentation, script stubs, and ID registry.
- Added core SLX utility, query, transfer, and UI helper scripts.

