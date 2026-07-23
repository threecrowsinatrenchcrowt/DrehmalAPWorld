from __future__ import annotations


from typing import TYPE_CHECKING, Optional

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from worlds.drehmal.logic.vanilla_logic import *
from worlds.drehmal.region.mc_regions_consts import *

if TYPE_CHECKING:
   from worlds.drehmal import FabricMinecraftWorld


from BaseClasses import Region, Location, CollectionState, Entrance
from worlds.drehmal.location.minecraft_locations import location_table

# HELPER METHODS #######################################################################################################

# Determines whether a location is included
def blacklisted_location(world: FabricMinecraftWorld, location_type: int):
    exclusions = {
        ADVANCEMENT: "Normal" in world.options.excluded_advancements.value,
        ADVANCEMENT_HARD: "Hard" in world.options.excluded_advancements.value,
        ADVANCEMENT_EXPLORATION: "Exploration" in world.options.excluded_advancements.value,
        ADVANCEMENT_UNREASONABLE: "Unreasonable" in world.options.excluded_advancements.value,

        MYTHICALS: not world.options.randomized_mythicals,
        LEGENDARIES: not world.options.randomized_legendaries,
        TERMINUS_TOWERS: world.options.randomized_terminus_towers == 0,
        QUEST_ITEMS: not world.options.randomized_quest_items,
        RELICS: world.options.randomized_relics == 0
    }

    if location_type in exclusions:
        if exclusions[location_type]:
            return True

    return False

# Creates a Region with Locations, and Excludes Unused Locations based on settings
def create_locations_advanced(world: FabricMinecraftWorld, region_name: str, locations: dict[str, int]):
   location_list = []

   for location, location_type in locations.items():
       if blacklisted_location(world, location_type):
           continue

       location_list.append(location)

   return create_locations(world, region_name, location_list)

# Creates a Region and Locations
def create_locations(world: FabricMinecraftWorld, region_name: str, locations: list[str]):
   region = Region(region_name, world.player, world.multiworld, region_name)

   for name in locations:
       location = Location(world.player, name, location_table[name], region)
       region.locations.append(location)

   world.multiworld.regions.append(region)


# Connects 2 Regions together!
def connect(world, source: str, target: str, rule=None) -> Optional[Entrance]:
   source_region = world.multiworld.get_region(source, world.player)
   target_region = world.multiworld.get_region(target, world.player)


   connection = Entrance(world.player, source + " ==> " + target, source_region)

   if rule is not None:
       world.set_rule(connection, rule)


   source_region.exits.append(connection)
   connection.connect(target_region)


   return connection

# Creates a Region with Locations, and Connects it to a parent Region
def create_locations_and_connect(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: dict[str, int], rule=None):
   create_locations_advanced(world, new_region_name, locations)
   connect(world, region_name, new_region_name, rule)

def smart_add_rule(world: FabricMinecraftWorld, location: str, rule: Rule, location_type: int):
    if blacklisted_location(world, location_type):
        return
    
    world.set_rule(world.get_location(location), rule)