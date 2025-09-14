==========
OK Traders
==========

Summary
=======

OK Trade (trade command) 
- Operates as a free trader when no homebase is set (like UT) 
- When homebase is set it trades multiple wares for its homebase (like CAG) 
- Coordinates with other OK Traders 
- Monitors and replans 
- Scans for hostiles and escapes before getting attacked. 
- No micromanagement, levels or special equipment requirements. 

Configuration Options 
- Auto-rename (off by default) 
- Trade illegal wares (free trader only, off by default) 
- Sector blacklist (for station selection, not move-pathing) 
- Respects dockware manager ware limits 
- Optionally tether a free trader to a sector and set a range it can trade in. 
- Economy boost mode for free traders. 

Requirements 
- Trade command software MK2 

Compatibility 
- Terran Conflict and Albion Prelude 

Change Log
==========

1.7.1
- Fix a bug which could lead to station ware limit settings corruption, and causing free traders to gradually use more CPU. If corruption is detected in 1.7.1 the station ware limit config will be reset to default.
- Fix a bug where homebased traders with jumpdrives would perform a 'best chance' station search instead of 'best price'.
- When evaluating docks to buy or sell at, examine other elligible docks trading at the same price to determine a more favourable stock level.

1.7.0
- Add Stock Limits settings accessible from homebased trader menus to support intermediate ware trading. Traders avoid selling below the minimum stock limit and avoid buying above the maximum stock limit. The limits apply to all traders at that homebase.
- Fix a bug with trading energy cells that could cause homebased traders to sit around in a station (1.6.2 regression)

1.6.4
- Add option for broadcasting OK trade to AP fleets
- Allow broadcasting from free traders in addition to homebased traders

1.6.3
- Add a blacklist menu option for adding all sectors belonging to a selected race
- Fix a bug where homebased traders would sell all their jumpfuel before returning home after a sale (1.6.2 regression)

1.6.2
- Fix a bug with the blacklist Clear button not working (1.6.1 regression)
- Prevent traders from selling Replicators
- Optimize the amount of jump energy for homebased traders based on current activity and reduce free trader energy stores by 20%

1.6.1
- Remove the ship ID code from auto-naming and instead add it explicitly into the attached warning message
- Let stations be blacklisted in addition to sectors
- Set default ware trade mode for intermediate products to None

1.6.0
- Added a broadcast option for homebased traders to share settings with multiple ships.
- Changed auto naming scheme for homebased traders. Names now include job names where applicable (e.g. Weapons Dealer)
- Set default ware mode for dock class homebases to No Trade
- Added equipping options to disable cargo life support and duplex scanners
- Avoid buying duplex when triplex is available
- Fix traders were only buying from docks when no factories qualified
- Fix eco traders not buying from docks

1.5.2
- Exempt traders homebased at docks from the 'Min Stock Level Trade %' setting when selling the dock's wares. The setting still applies to buying.

1.5.1
- Add equipping option for rudder optimizations
- Disable laser and missile equipping by default for new installs
- Rename Settings menu to Global Settings
- Add config option to disable the alert noise when trader is targetted
- Add text files for DE, PL, CS, IT, ES, FR, RU with English strings.

1.5.0
- Add simple global on/off equipment options to the config menu (lasers, shields, missiles, drones, docking computer, jumpdrive, triplex)
- If the trader lacks engine tunings or jumpdrive (if enabled) it will fly directly to docks to buy these goods in that order as top priority.
- For all other equipment the trader will only buy them if it happens to be docked at a station selling that item.
- Traders retain installed lasers and shields even when the these options are disabled.

1.4.3
- Fix: traders might not refuel before selling a ware outside their jump fuel range.

1.4.2
- Several performance enhancements, notably for economy boosting traders.
- Fix: exclude marines and mercenaries from being traded (always been present)
- Fix: free traders with docking computers would buy more wares than the destination station could buy. (1.4.0 regression)

1.4.1
- Improve eco trader performance a little when evaluating wares to trade
- Fix: prevent eco traders from selling secondary resources to stalled factories, not helping economy
- Fix: ships buying wares at docks would sell the ware back to the dock afterwards (1.4.0 regression)

1.4.0
- Add an economy boost mode for free traders, where they prioritize trading at stalled factories.
- Add free trader tether sector and tether range options to restrict free trader movement
- Have homebased traders observe dockware manager stock level limits configured on player docks.
- Traders now make use of docking computers when installed, and will buy a docking computer if they happen to dock at a place that sells one.
- Performance optimizations.
- Fix: repair shipyard selection was failing to respect blacklist
- Fix: homebased trader ware settings were not updated when wares were added/removed from the homebase tradeable ware list.

1.3.2
- Balance statistics are now resettable and display with comma separators. Collective balance now tracked in a global rather than summing trader values.
- Fix: balance statistics rollover when exceeding signed int max. Now tracks billions (thousand millions) in a separate integer.
- Fix: blacklisting non jumpable sectors could add duplicate list entries, and would blacklist sectors with jump beacons

1.3.1
- Homebased traders now only test the homebase can afford 1 unit of a ware rather than an amount equal to min(free space ship, free space station).

1.3.0
- Homebased traders now buy jumpdrives in addition to free traders.
- Traders repair hull damage at shipyard
- When docked opportunistically buy and equip a quantity of missiles, drones, tunings (not cargo), scanner, jumpdrive, shields
- Reserve against sale a quantity of supported missile types, compatible lasers (ex. TB, MDS), installed shields, drones, and a jump beacon.
- Launch missiles and drones when under attack
- Increase intelligence around refuelling and fleeing.
- Add blacklist options to add pirate, non-jumpable, and war sectors.
- Increase the attacked warning subtitle message duration from 3 to 6 seconds.
- Rapidly restart the command script on version upgrade, rather than waiting on action completion. May not take effect until +1 releases ahead.
- Display collective free trader balance underneath the current traders balance in the free trader's menu. Note this only includes profits from currently existing player ships.
- Disable selling wares to player owned stations.
- Fix: traders could erroneously believe they had sufficient jump energy to jump when they didn't (since 1.0.0)
- Fix: attempting to top up jump energy exceeding available cargo space (since 1.1.0)
- Fix: take into account infinite buyers when free traders assess trade run profits (since 1.2.0)
- Fix: monitor task could exit on version upgrade and not start again until the ship's move action completes, leaving traders vulnerable (since 1.1.0). May not take effect until subsequent upgrades.
- Fix: race condition where 2 free traders could perform the same trade (since 1.2.0)

1.2.3
- Switch display command to COMMAND_REFUEL when moving to an SPP.
- Revised criteria for searching stations by best-price vs best-chance vs nearest.
- When rerouting a buying mission check the ship can jump to the new destination, otherwise reevaluate.

1.2.2
- Fix if the cargo bay is completely full a trader won't sell the ware (introduced 1.2.0)

1.2.1
- Free traders will buy a jumpdrive if they don't have one already.
- Preserve free trader's profit tracking balance between command restarts. This primarily avoids resetting to 0 on upgrade.
- Fix attempting to buy a ware if there are insufficient funds to buy 1 unit.
- Fix docks not being taken into account when searching for a station to buy a ware at
- Fix a bug in infinite ware buying detection (introduced 1.2.0)
- Fix selling of wares to infinite buyers not awarding reputation
- Fix a bug where homebase traders would not return to homebase in order to load the ware for a sale mission (introduced 1.2.0)

1.2.0
- OK Trade can now be enabled on ships without homebases. They act as free traders and roam the galaxy in search of profit.
- When a ship is already running the command, the trade menu will display the ships's current settings or profit/loss so far in the case of a free trader.

1.1.0
- Change the OK trade command ID from 42 to 48 to resolve a conflict. Note that following upgrade from 1.0.0 existing OK traders will temporarily show "Unknown command!" until their current action completes and the scripts restart.
- Automatically enable autojump and set min jumps to 0 when starting the OK trade command.
- Detect danger and return to homebase. Display subtitle messages when a trader detects danger.
- Reroute to new destination if current trade mission is invalidated, for example if destination ware price becomes unacceptable with respect to homebase selling price
- Buy wares without first returning to homebase if ship has sufficient jump energy to get there and home again, or if the ship isn't jump capable
- Add a minimum stock level percentage trade threshold with default of 10% (sell when above 10% stock, buy when below 90% stock).
- Improve displyed command action details
- Fix amount of ware on order calculation to include amount in cargobay

1.0.0
- Initial release

Setup
=====

Install
- The script and t folders from the zip should be copied to the folders of the same name in the Terran Conflict folder. For Albion Prelude, copy into the script and t folders in the addon subfolder.
- The setup script should run after starting or loading a game. The OK Trade command should then appear in ship trade menus.

Upgrade/Downgrade
- Replace the script files and load the game. The setup script will automatically upgrade settings, re-creating them on downgrade.
- Running OK Trade scripts will restart themselves following completion of their current activities

Uninstall
- First run the uninstall command from the OK Trade menu. This will replace running scripts with appropriate default commands (sell ware, buy ware, return home) to avoid disrupting immediate activities.
- Then save the game and remove the setup script. Upon reload the trade command should be gone.

Details
=======

When issuing the OK Trade command the user can configure how the trader should handle each of the homebase wares in terms of buy, sell, or no-trade. Appropriate defaults are detected, so that the trading in all wares can readily be activated without adjuting these values.

The trader will then select the highest priority ware to trade, where priority is determined by the relative stock levels adjusted for amount of ware on order or already bought and being shipped in. A station is selected within the homebase max jumps range. If the ship has a jumpdrive and sufficient energy available the station will be selected using the 'best price' method within the station's jumprange. If the ship could jump there but not back again, the 'best chance' method is selected, otherwise it looks for nearest station with sufficient price.

When docked at a station that trades energy cells or at the homebase, the trader will stock up on 2.5x homebase max jumps worth of fuel. Typically the trader will have enough energy left after a sale to jump immediately to another station to buy a ware, without having to refuel, or to jump home to escape danger.

Optimizations
=============
- If the script detects that the target station can buy an infinite amount of the ware (e.g. docks that buy shields, lasers, missiles), it'll load as much as it can carry when selling to that station.
- If incoming hostiles or missiles are detected in scan range the trader will try and flee to homebase before being attacked and warn the user via subtitle message.
- If the price at the destination changes and no longer meets the homebase price, the trader will attempt to reroute or return home for refuelling.
- After selling a ware the trader can buy a ware without returning home first, if the ship has sufficient jump energy.
- The amount of a ware on order and in cargo bay by other traders is taken into account when comparing stock levels to determine what to trade.
- The trader will not perform an identical trade mission to another OK trader; ware, destination and trade mode (buy/sell) must differ.

References
==========
- Developed using X-Studio: http://forum.egosoft.com/viewtopic.php?t=301433

Resources Used
==============

Text File
  9055
Trade Commands
  448: COMMAND_TYPE_TRADE_48