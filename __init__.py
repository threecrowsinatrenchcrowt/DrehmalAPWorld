from typing import Mapping, Any

from BaseClasses import ItemClassification, Item
from worlds.AutoWorld import World, WebWorld
from worlds.drehmal.item.items_helper import item_table
from worlds.drehmal.item.items_init import create_local_fill_items, create_items
from worlds.drehmal.location.minecraft_locations import location_table
from worlds.drehmal.options import FMCOptions
from worlds.drehmal.region.regions_init import create_regions


class FMCWebWorld(WebWorld):
    option_groups = options.option_groups

class FabricMinecraftWorld(World):
    game = "Drehmal"
    options_dataclass = FMCOptions
    options: FMCOptions
    topology_present = True
    web = FMCWebWorld()

    item_name_to_id = {
        item.name: item.item_id for item in item_table.values()
    }

    location_name_to_id = location_table


    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)
        self.max_ruby_count = 0
        self.local_fill_amount = 0

    def create_regions(self):
        create_regions(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        self.create_puml(False)

        advancements = 0
        for location in self.multiworld.get_locations():
            advancements += 1

        return {
            "world_version": self.world_version.as_simple_string(),
            # Base
            "goal_condition": self.options.goal_condition.value,
            # Rubies
            "rubies_to_goal": self.options.percentage_of_rubies_needed.value,
            "total_rubies": self.max_ruby_count,
            "deathlink": self.options.deathlink_enabled.value,
            "traplink": self.options.traplink_enabled.value,
            # Other Options
            "excluded_advancements": self.options.excluded_advancements.value,
            "randomized_abilities": self.options.randomized_abilities.value,
            "possible_randomized_abilities": self.options.randomized_abilities.valid_keys,
            "randomized_mythicals": self.options.randomized_mythicals.value,
            "randomized_legendaries": self.options.randomized_legendaries.value,
            "randomized_terminus_towers": self.options.randomized_terminus_towers.value,
            "randomized_quest_items": self.options.randomized_quest_items.value,
            "randomized_relics": self.options.randomized_relics.value,
            "scout_tedious_locations": self.options.scout_tedious_locations.value,
        }

    def create_item(self, name: str) -> "Item":
        return Item(name, ItemClassification.progression, self.item_name_to_id[name], self.player)

    def create_items(self):
        create_items(self)

    def pre_fill(self) -> None:
        create_local_fill_items(self)


    # Creates Puml for checking Logic
    def create_puml(self, create: bool):
        if create:
            from Utils import visualize_regions
            state = self.multiworld.get_all_state()
            state.update_reachable_regions(self.player)

            reachable_regions = state.reachable_regions[self.player]
            unreachable_regions: set[Region] = set()  # type: ignore
            for regionb in self.multiworld.regions:
                if regionb not in reachable_regions:
                    unreachable_regions.add(regionb)

            visualize_regions(self.get_region("Menu"), f"{self.player_name}_world.puml", show_entrance_names=True,
                              regions_to_highlight=unreachable_regions)