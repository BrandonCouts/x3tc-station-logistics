# Changelog

## 0.1.9-internal
- Added passenger command reference.

## 0.1.8-internal
- Linter now rejects positional argument syntax and scripts use named parameters.
- Fixed remaining positional-style references in ware config query.
- Enforced numeric array indexing for ware configs and linter rejects string keys.

## 0.1.7-internal
- Added overview section to SLX README for clarity.

## 0.1.6-internal
- Added peer store status reason codes and auto-role mapping in UI helper.

## 0.1.5-internal
- Added store balancing loop and auto role inference with prefixed last reason codes.
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

