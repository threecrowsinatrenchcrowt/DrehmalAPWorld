from __future__ import annotations

from worlds.drehmal.item.items.create_items import create_items
from worlds.drehmal.item.items.vanilla_items import vanilla_items
from worlds.drehmal.item.items.drehmal_items import *


########################################################################################################################
# ALL ITEMS IN RANDOMIZER ##############################################################################################
########################################################################################################################

# Adds all the items to a list for turning into a dictionary
def get_all_items():
    items = []
    items += drehmal_mythicals
    items += drehmal_legendaries
    items += drehmal_terminus_towers
    items += drehmal_quest_items
    items += drehmal_relics
    items += vanilla_items # Vanilla Items
    #items += create_items # Create Items
    return items