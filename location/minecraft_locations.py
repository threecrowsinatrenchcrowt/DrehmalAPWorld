from worlds.drehmal.location.vanilla.vanilla_advancements import vanilla_advancements

from worlds.drehmal.location.drehmal.drehmal_mythicals import drehmal_mythicals
from worlds.drehmal.location.drehmal.drehmal_legendaries import drehmal_legendaries
from worlds.drehmal.location.drehmal.drehmal_terminus_towers import drehmal_terminus_towers
from worlds.drehmal.location.drehmal.drehmal_quest_items import drehmal_quest_items
from worlds.drehmal.location.drehmal.drehmal_relics import drehmal_relics

########################################################################################################################
# ALL LOCATIONS IN RANDOMIZER ##########################################################################################
########################################################################################################################

def get_location_table():
    table = {}
    # DREHMAL LOCATIONS
    table.update(add_locations(table, drehmal_mythicals))
    table.update(add_locations(table, drehmal_legendaries))
    table.update(add_locations(table, drehmal_terminus_towers))
    table.update(add_locations(table, drehmal_quest_items))
    table.update(add_locations(table, drehmal_relics))
    # VANILLA LOCATIONS
    table.update(add_locations(table, vanilla_advancements))
    return table

def add_locations(table: dict[str, int], locations: list[str]):
    return {name: (index + len(table) + 1) for index, name in enumerate(locations)}

# Table of EVERY LOCATION
location_table = get_location_table()