from __future__ import annotations


from typing import TYPE_CHECKING, Optional

from worlds.drehmal.region.regions_helper import create_locations_advanced
from worlds.drehmal.region.vanilla.vanilla_advancement_regions import create_vanilla_advancement_regions
from worlds.drehmal.region.drehmal.drehmal_regions import create_drehmal_regions
from worlds.drehmal.region.drehmal.devotion_regions import create_devotion_regions
from worlds.drehmal.logic.vanilla_logic import *

if TYPE_CHECKING:
   from worlds.drehmal import FabricMinecraftWorld

def get_goal_condition(world: FabricMinecraftWorld):
    goal_id = world.options.goal_condition.value

    if goal_id == 0: # Ender Dragon
        return TETHLAEN
    elif goal_id == 1: # Ruby Hunt
        return PLACEHOLDER
    
    return PLACEHOLDER

# Creates all Regions in the Randomizer!
def create_regions(world: FabricMinecraftWorld):
    # Creates a Main Region for everything to branch from!
    create_locations_advanced(world, "Menu", {})
    # Drehmal Regions (geographic)
    create_drehmal_regions(world)
    # Drehmal Devotion regions
    create_devotion_regions(world)
    # Miscellaneous Advancement Regions
    create_vanilla_advancement_regions(world)

    world.set_completion_rule(get_goal_condition(world))
