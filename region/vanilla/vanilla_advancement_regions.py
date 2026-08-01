from __future__ import annotations


from typing import TYPE_CHECKING, Optional

from ..mc_regions_consts import *
from ..regions_helper import create_locations_and_connect, smart_add_rule
from ...logic.vanilla_logic import *


if TYPE_CHECKING:
   from ... import FabricMinecraftWorld


def create_vanilla_advancement_regions(world: FabricMinecraftWorld):
    # BASE (REQUIRES NOTHING TO GET)
    create_locations_and_connect(world, "Menu", "MenuVanillaAdvancements", {
        "How Did We Get Here?": ADVANCEMENT_UNREASONABLE,
        "A Furious Cocktail": ADVANCEMENT_UNREASONABLE,
        "Arbalistic": ADVANCEMENT_UNREASONABLE,
        "The Cutest Predator": ADVANCEMENT,
        "A Balanced Diet": ADVANCEMENT_HARD,
        "Two by Two": ADVANCEMENT_UNREASONABLE,
        "The Parrots and the Bats": ADVANCEMENT,
        "Alchemy": ADVANCEMENT,
        "Bullseye": ADVANCEMENT,
        "A Complete Catalogue": ADVANCEMENT_UNREASONABLE,
        "Bring Home the Asterial Array": ADVANCEMENT_HARD,
        "Asterial Arrayinator": ADVANCEMENT_UNREASONABLE,
        "Necromantic Reversal": ADVANCEMENT_HARD,
        "Oh Shiny": ADVANCEMENT,
        "Runic Magic": ADVANCEMENT,
        "Fishy Business": ADVANCEMENT,
        "Spooky Scary Skeleton": ADVANCEMENT,
        "Drehmari Hero": ADVANCEMENT_HARD,
        "Sticky Situation": ADVANCEMENT,
        "Monster Hunter": ADVANCEMENT,
        "Monsters Hunted": ADVANCEMENT_UNREASONABLE,
        "The Healing Power of Friendship": ADVANCEMENT_HARD,
        "Surge Protector": ADVANCEMENT_HARD,
        "Diamonds!": ADVANCEMENT,
        "Serious Dedication": ADVANCEMENT,
        "Ol' Betsy": ADVANCEMENT,
        "A Seedy Place": ADVANCEMENT,
        "Return to Sender": ADVANCEMENT,
        "Whatever Floats your Goat!": ADVANCEMENT,
        "Bee Our Guest": ADVANCEMENT,
        "Cover Me with Diamonds": ADVANCEMENT,
        "Take Aim": ADVANCEMENT,
        "Total Beelocation": ADVANCEMENT_HARD,
        "Sweet Dreams": ADVANCEMENT,
        "Sniper Duel": ADVANCEMENT_HARD,
        "Is It a Plane?": ADVANCEMENT,
        "Is It a Balloon?": ADVANCEMENT,
        "Is It a Bird?": ADVANCEMENT,
        "Hired Help": ADVANCEMENT,
        "Soulgrafting": ADVANCEMENT_HARD,
        "Tactical Fishing": ADVANCEMENT,
        "Best Friends Forever": ADVANCEMENT,
        "Postmortal": ADVANCEMENT,
        "What a Deal!": ADVANCEMENT,
        "Two Birds, One Arrow": ADVANCEMENT_HARD,
        "No Place Like Home": ADVANCEMENT,
        "Voluntary Exile": ADVANCEMENT,
        "Light as a Rabbit": ADVANCEMENT,
        "Who's the Mikhmari Now?": ADVANCEMENT,

        # Lo'Dahr Advancements
        "Crazy Dragon Lady": ADVANCEMENT_UNREASONABLE,
        "BE NOT AFRAID": ADVANCEMENT_HARD,
        "Otherworldly Expedition": ADVANCEMENT,
        "Now You're Thinking With...": ADVANCEMENT,
        "The Sky is Falling!": ADVANCEMENT,
        "One Small Step": ADVANCEMENT,
        "Catching Stars": ADVANCEMENT_UNREASONABLE,
        "Local Traditions": ADVANCEMENT,
        "Cover Me in Starstuff": ADVANCEMENT,
        "Stellar Refuse": ADVANCEMENT,
        "Invasive Species": ADVANCEMENT,
        "A Gentle Slaughter": ADVANCEMENT,
        "Glimpse Into the Cosmos": ADVANCEMENT_UNREASONABLE,
        "Survive the Wastes": ADVANCEMENT_UNREASONABLE,
        "A Throwaway Joke": ADVANCEMENT,
        "Very Very Frightening": ADVANCEMENT_HARD,
        "Bundled Up": ADVANCEMENT
    })
    # tbh i have no idea how you do these two in drehmal, so i'm putting as many requirements on them as I can think of
    smart_add_rule(world, "How Did We Get Here?", OPEN_WORLD & CAN_BREW & HARD_COMBAT_MANUAL_LOCK, ADVANCEMENT_UNREASONABLE)
    smart_add_rule(world, "A Furious Cocktail", OPEN_WORLD & CAN_BREW & HARD_COMBAT_MANUAL_LOCK, ADVANCEMENT_UNREASONABLE)
    
    smart_add_rule(world, "Arbalistic", (CRAFT_CROSSBOW | SYZYGY) & CAN_ENCHANT & HIGH_TOWER_COUNT, ADVANCEMENT_UNREASONABLE)
    smart_add_rule(world, "The Cutest Predator", CRAFT_BUCKET & BLACK_JUNGLE & LOW_TOWER_COUNT, ADVANCEMENT)
    # there's probably more subtle logic I could add for this, but according to the discord, the only enchanted golden apple is in Merijool, so this is fine for now
    smart_add_rule(world, "A Balanced Diet", OPEN_WORLD & CAN_SMELT, ADVANCEMENT_HARD)
    smart_add_rule(world, "Two by Two", OPEN_WORLD, ADVANCEMENT_UNREASONABLE)
    # Parrots and the Bats is always sphere 1
    smart_add_rule(world, "Alchemy", CAN_BREW & LOW_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Bullseye", SYZYGY & MEDIUM_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "A Complete Catalogue", OPEN_WORLD, ADVANCEMENT_UNREASONABLE)
    smart_add_rule(world, "Bring Home the Asterial Array", CAN_SUMMON_WITHER & HARD_COMBAT_MANUAL_LOCK & HIGH_TOWER_COUNT, ADVANCEMENT_HARD)
    smart_add_rule(world, "Asterial Arrayinator", CAN_SUMMON_WITHER & OPEN_WORLD & CRAFT_IRON_TOOLS, ADVANCEMENT_UNREASONABLE)
    smart_add_rule(world, "Necromantic Reversal", CAN_BREW & MEDIUM_TOWER_COUNT, ADVANCEMENT_HARD)
    smart_add_rule(world, "Oh Shiny", CAN_BARTER & MEDIUM_TOWER_COUNT & CARMINE, ADVANCEMENT)
    smart_add_rule(world, "Runic Magic", CAN_ENCHANT & LOW_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Fishy Business", CRAFT_FISHING_ROD & LOW_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Spooky Scary Skeleton", LO_DAHR & MEDIUM_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Drehmari Hero", BLACK_JUNGLE & HARD_COMBAT_MANUAL_LOCK & HIGH_TOWER_COUNT, ADVANCEMENT_HARD)
    smart_add_rule(world, "Sticky Situation", AKHLO_ROHMA & LOW_TOWER_COUNT, ADVANCEMENT)
    # Monster Hunter is always sphere 1
    smart_add_rule(world, "Monsters Hunted", OPEN_WORLD & HARD_COMBAT_MANUAL_LOCK, ADVANCEMENT_UNREASONABLE)
    smart_add_rule(world, "The Healing Power of Friendship", CRAFT_BUCKET & BLACK_JUNGLE & SWIM & MEDIUM_TOWER_COUNT, ADVANCEMENT_HARD)
    # Almost certainly false but I will fix it later
    smart_add_rule(world, "Surge Protector", LO_DAHR & HIGH_TOWER_COUNT, ADVANCEMENT_HARD)
    smart_add_rule(world, "Diamonds!", CRAFT_IRON_TOOLS & MEDIUM_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Serious Dedication", CRAFT_NETHERITE_TOOLS & HIGH_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Ol' Betsy", CRAFT_CROSSBOW & LOW_TOWER_COUNT, ADVANCEMENT)
    # A Seedy Place is always sphere 1
    smart_add_rule(world, "Return to Sender", (HELLCRAGS | LO_DAHR) & MEDIUM_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Whatever Floats your Goat!", (LO_DAHR | AKHLO_ROHMA) & LOW_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Bee Our Guest", AKHLO_ROHMA & MEDIUM_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Cover Me with Diamonds", CRAFT_IRON_TOOLS & LOW_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Take Aim", CRAFT_BOW & LOW_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Total Beelocation", AKHLO_ROHMA & CAN_ENCHANT & HIGH_TOWER_COUNT, ADVANCEMENT_HARD)
    smart_add_rule(world, "Sweet Dreams", CAN_SLEEP & LOW_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Sniper Duel", SYZYGY & MEDIUM_TOWER_COUNT, ADVANCEMENT_HARD)
    smart_add_rule(world, "Is It a Plane?", YAVHLIX & LO_DAHR & HIGH_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Is It a Balloon?", LO_DAHR & HIGH_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Is It a Bird?", LO_DAHR & MEDIUM_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Hired Help", CRAFT_STONE_TOOLS & CAN_COMPACT & MEDIUM_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Soulgrafting", CAN_SUMMON_WITHER & HIGH_TOWER_COUNT, ADVANCEMENT_HARD)
    smart_add_rule(world, "Tactical Fishing", CRAFT_BUCKET & LOW_TOWER_COUNT, ADVANCEMENT)
    # Best Friends Forever is always sphere 1
    smart_add_rule(world, "Postmortal", LO_DAHR & MEDIUM_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "What a Deal!", CAN_TRADE & LOW_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Two Birds, One Arrow", (CRAFT_CROSSBOW | SYZYGY) & (CARMINE | LO_DAHR) & CAN_ENCHANT & HIGH_TOWER_COUNT, ADVANCEMENT_HARD)
    smart_add_rule(world, "No Place Like Home", MEDIUM_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Voluntary Exile", BLACK_JUNGLE & MEDIUM_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Light as a Rabbit", CRAFT_LEATHER_ARMOR & FAEHRCYLE & LOW_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Who's the Mikhmari Now?", CRAFT_CROSSBOW & BLACK_JUNGLE & LOW_TOWER_COUNT, ADVANCEMENT)

    smart_add_rule(world, "Crazy Dragon Lady", LO_DAHR & HIGH_TOWER_COUNT, ADVANCEMENT_UNREASONABLE)
    smart_add_rule(world, "BE NOT AFRAID", ((NO_LEGENDARIES & CARMINE & CHESTS) | (YES_LEGENDARIES & HAS_EYEBITER)) & LO_DAHR & MEDIUM_TOWER_COUNT, ADVANCEMENT_HARD)
    smart_add_rule(world, "Otherworldly Expedition", LO_DAHR & HIGH_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Now You're Thinking With...", LO_DAHR & FAEHRCYLE & HELLCRAGS & NIMAHJ_SWAMP & MERIJOOL & SPEARHEAD_FOREST & BLACK_JUNGLE & HIGH_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "The Sky is Falling!", LO_DAHR & MEDIUM_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "One Small Step", LO_DAHR & LOW_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Catching Stars", LO_DAHR & APHELION & HIGH_TOWER_COUNT, ADVANCEMENT_UNREASONABLE)
    smart_add_rule(world, "Local Traditions", LO_DAHR & MEDIUM_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Cover Me in Starstuff", LO_DAHR & CRAFT_NETHERITE_ARMOR & HIGH_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Stellar Refuse", LO_DAHR & CRAFT_DIAMOND_TOOLS & MEDIUM_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Invasive Species", LO_DAHR & ((NO_LEGENDARIES & RIGHT_BLADE_FRAG & ANYR_NOGUR) | (YES_LEGENDARIES & HAS_WARP_HORSE)) & MEDIUM_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "A Gentle Slaughter", LO_DAHR & CAN_ENCHANT & MEDIUM_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Glimpse Into the Cosmos", LO_DAHR & JUMP & SPRINT & SWIM & HIGH_TOWER_COUNT, ADVANCEMENT_UNREASONABLE)
    smart_add_rule(world, "Survive the Wastes", LO_DAHR & CRAFT_NETHERITE_ARMOR & CAN_ENCHANT & HIGH_TOWER_COUNT, ADVANCEMENT_UNREASONABLE)
    smart_add_rule(world, "A Throwaway Joke", LO_DAHR & LOW_TOWER_COUNT, ADVANCEMENT)
    smart_add_rule(world, "Very Very Frightening", LO_DAHR & HIGH_TOWER_COUNT, ADVANCEMENT_HARD)
    smart_add_rule(world, "Bundled Up", LO_DAHR & CRAFT_LEATHER_ARMOR & MEDIUM_TOWER_COUNT, ADVANCEMENT)

def create_region(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: dict[str, int], rule=None):
    create_locations_and_connect(world, region_name + "VanillaAdvancements", new_region_name + "VanillaAdvancements", locations, rule)