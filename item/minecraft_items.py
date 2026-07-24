from __future__ import annotations

from .items.create_items import create_items
from .items.vanilla_items import vanilla_items
from .items.drehmal_items import *


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