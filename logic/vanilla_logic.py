from __future__ import annotations

from math import floor
from typing import TYPE_CHECKING


from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, HasFromList, Rule, CanReachRegion, True_

from worlds.drehmal.options import *

if TYPE_CHECKING:
   from worlds.drehmal import FabricMinecraftWorld

PLACEHOLDER = True_()

JUMP = Has("Jump", options=[OptionFilter(RandomizedAbilities, "Jump", operator="contains")], filtered_resolution=True)
SPRINT = Has("Sprint", options=[OptionFilter(RandomizedAbilities, "Sprint", operator="contains")], filtered_resolution=True)
SWIM = Has("Swim", options=[OptionFilter(RandomizedAbilities, "Swim", operator="contains")], filtered_resolution=True)
CHESTS = Has("Chests & Barrels", options=[OptionFilter(RandomizedAbilities, "Chests", operator="contains")], filtered_resolution=True)

REGION_LOCK = [OptionFilter(RandomizedTerminusTowers, 2)]
NOT_REGION_LOCK = [OptionFilter(RandomizedTerminusTowers, 2, operator="ne")]

PALISADES_HEATH = Has("Palisades Heath Tower") | NOT_REGION_LOCK
AV_SAL = Has("Av'Sal Tower") | NOT_REGION_LOCK
GULF_OF_DREHMAL = Has("Gulf of Drehmal Tower") | NOT_REGION_LOCK
MERIJOOL = Has("Merijool Tower") | NOT_REGION_LOCK
CASAI = Has("Casai Tower") | NOT_REGION_LOCK
ANYR_NOGUR = Has("Anyr'Nogur Tower") | NOT_REGION_LOCK
EBONFIRE = Has("Mt. Ebonfire Tower") | NOT_REGION_LOCK
NIMAHJ_SWAMP = Has("Nimahj Swamp Tower") | NOT_REGION_LOCK
EBONY_VELDT = Has("Ebony Veldt Tower") | NOT_REGION_LOCK
LORAHN_KAHL = Has("Lorahn'Kahl Tower") | NOT_REGION_LOCK
NORTH_THARXAX = Has("North Tharxax Tower") | NOT_REGION_LOCK
SOUTH_THARXAX = Has("South Tharxax Tower") | NOT_REGION_LOCK
CARMINE = Has("Carmine Tower") | NOT_REGION_LOCK
HELLCRAGS = Has("Hellcrags Tower") | NOT_REGION_LOCK
AKHLO_ROHMA = Has("Akhlo'Rohma Tower") | NOT_REGION_LOCK
NORTH_HEARTWOOD = Has("North Heartwood Tower") | NOT_REGION_LOCK
PURITY_PEAKS = Has("Purity Peaks Tower") | NOT_REGION_LOCK
MAELS_DESOLATION = Has("South Heartwood Tower") | NOT_REGION_LOCK
SPEARHEAD_FOREST = Has("Spearhead Forest Tower") | NOT_REGION_LOCK
BLACK_JUNGLE = Has("Black Jungle Tower") | NOT_REGION_LOCK
VERUHKT_PLATEAU = Has("Veruhkt Plateau Tower") | NOT_REGION_LOCK
GRAND_PIKE_CANYON = Has("Grand Pike Canyon Tower") | NOT_REGION_LOCK
HIGHFALL_TUNDRA = Has("Highfall Tundra Tower") | NOT_REGION_LOCK
FROZEN_BITE = Has("Frozen Bite Tower") | NOT_REGION_LOCK
FAEHRCYLE = Has("Faehrcyle Tower") | NOT_REGION_LOCK
DAWN_ISLAND = Has("Island of Dawn Tower") | NOT_REGION_LOCK
DUSK_ISLAND = Has("Island of Dusk Tower") | NOT_REGION_LOCK
SAHD = Has("Sahd Tower") | NOT_REGION_LOCK

CRAFT_IRON_TOOLS = Has("Progressive Tools", count=2, options=[OptionFilter(RandomizedAbilities, "Tools", operator="contains")], filtered_resolution=True)
CRAFT_DIAMOND_ARMOR = Has("Progressive Armor", count=4, options=[OptionFilter(RandomizedAbilities, "Armor", operator="contains")], filtered_resolution=True) & CRAFT_IRON_TOOLS
CRAFT_DIAMOND_WEAPONS = Has("Progressive Weapons", count=3, options=[OptionFilter(RandomizedAbilities, "Weapons", operator="contains")], filtered_resolution=True) & CRAFT_IRON_TOOLS
CRAFT_BOW = Has("Progressive Archery", count=1, options=[OptionFilter(RandomizedAbilities, "Archery", operator="contains")], filtered_resolution=True)

HARD_COMBAT_MANUAL_LOCK = JUMP & SPRINT & CRAFT_BOW & CRAFT_DIAMOND_ARMOR & CRAFT_DIAMOND_WEAPONS


YES_QUEST_ITEMS = [OptionFilter(RandomizedQuestItems, True)]
NO_QUEST_ITEMS = [OptionFilter(RandomizedQuestItems, False)]

LO_DAHR = (Has("Lo'Dahr Tower") & (AV_SAL | FAEHRCYLE | GRAND_PIKE_CANYON | MERIJOOL | SOUTH_THARXAX | BLACK_JUNGLE | HELLCRAGS)) | NOT_REGION_LOCK
CAN_DO_MYTHBREAKER_RUN = Has("Inert Mythbreaker") & LO_DAHR & FAEHRCYLE & JUMP & SPRINT
YAVHLIX = CAN_DO_MYTHBREAKER_RUN | Has("Yavhlix Tower")
TETHLAEN = YAVHLIX & HARD_COMBAT_MANUAL_LOCK & (HasFromList("Yavhlix Lever 1", "Yavhlix Lever 2", "Yavhlix Lever 3", "Duplicate Yavhlix Lever", count=3) | NO_QUEST_ITEMS)

APHELION = (Has("Aphelion Tower") | NOT_REGION_LOCK) & AV_SAL

OPEN_WORLD = PALISADES_HEATH & AV_SAL & GULF_OF_DREHMAL & MERIJOOL & CASAI & ANYR_NOGUR & EBONFIRE & NIMAHJ_SWAMP & EBONY_VELDT & LORAHN_KAHL & NORTH_THARXAX & SOUTH_THARXAX & CARMINE & HELLCRAGS & AKHLO_ROHMA & NORTH_HEARTWOOD & PURITY_PEAKS & MAELS_DESOLATION & SPEARHEAD_FOREST & BLACK_JUNGLE & GRAND_PIKE_CANYON & VERUHKT_PLATEAU & HIGHFALL_TUNDRA & FROZEN_BITE & FAEHRCYLE & DAWN_ISLAND & DUSK_ISLAND & SAHD & LO_DAHR & YAVHLIX

TEMPORAL_ENGINE = PURITY_PEAKS
LEFT_BLADE_FRAG = TEMPORAL_ENGINE & JUMP & SPRINT

EXODUS_ENTRY = NIMAHJ_SWAMP
RIGHT_BLADE_FRAG = EXODUS_ENTRY & SWIM & SPRINT 

INERT_MB = AV_SAL & ((Has("Left Blade Fragment") & Has("Right Blade Fragment") & YES_QUEST_ITEMS) | (LEFT_BLADE_FRAG & RIGHT_BLADE_FRAG & NO_QUEST_ITEMS))

CRAFT_TNT = Has("TNT Recipes", options=[OptionFilter(RandomizedAbilities, "TNT", operator="contains")], filtered_resolution=True)

FOUNDRY_ENTRY = (HasFromList("Foundry Lever 1", "Foundry Lever 2", "Foundry Lever 3", count=3) & YES_QUEST_ITEMS) | (EBONFIRE & EBONY_VELDT & ANYR_NOGUR & NO_QUEST_ITEMS)

YES_LEGENDARIES = [OptionFilter(RandomizedLegendaries, True)]
NO_LEGENDARIES = [OptionFilter(RandomizedLegendaries, False)]

HAS_WINGS = Has("Avsohm'Kohl")
HAS_EYEBITER = Has("Eyebiter")
HAS_WARP_HORSE = Has("Warp Horse Armor") & Has("Warp Horse Receiver")

OBLIVION_LABYRINTH = FAEHRCYLE & ((Has("Nihilist's Notes") & YES_QUEST_ITEMS) | (FROZEN_BITE & NO_QUEST_ITEMS))

FRENZY = SAHD & ((HasFromList("Fragment of Fury", "Fragment of Hate", "Fragment of Pain", "Fragment of Rage", "Fragment of Wrath", count=5) & YES_QUEST_ITEMS) | (CHESTS & NO_QUEST_ITEMS))

CRAFT_STONE_TOOLS = Has("Progressive Tools", count=1, options=[OptionFilter(RandomizedAbilities, "Tools", operator="contains")], filtered_resolution=True)
CRAFT_DIAMOND_TOOLS = Has("Progressive Tools", count=3, options=[OptionFilter(RandomizedAbilities, "Tools", operator="contains")], filtered_resolution=True)
CRAFT_NETHERITE_ARMOR = Has("Progressive Armor", count=5, options=[OptionFilter(RandomizedAbilities, "Armor", operator="contains")], filtered_resolution=True) & CRAFT_DIAMOND_TOOLS & LO_DAHR
CRAFT_NETHERITE_TOOLS = Has("Progressive Tools", count=4, options=[OptionFilter(RandomizedAbilities, "Tools", operator="contains")], filtered_resolution=True) & LO_DAHR

CAN_ENCHANT = Has("Enchanting", options=[OptionFilter(RandomizedAbilities, "Enchanting", operator="contains")], filtered_resolution=True) & CRAFT_IRON_TOOLS
CAN_BREW = Has("Brewing", options=[OptionFilter(RandomizedAbilities, "Brewing", operator="contains")], filtered_resolution=True)
CAN_SMELT = Has("Progressive Smelting", count=1, options=[OptionFilter(RandomizedAbilities, "Smelting", operator="contains")], filtered_resolution=True)
CAN_TRADE = Has("Villager Trading", options=[OptionFilter(RandomizedAbilities, "Trading", operator="contains")], filtered_resolution=True)
CAN_BARTER = Has("Piglin Bartering", options=[OptionFilter(RandomizedAbilities, "Bartering", operator="contains")], filtered_resolution=True)
CAN_SLEEP = Has("Sleeping", options=[OptionFilter(RandomizedAbilities, "Spawn_Point", operator="contains")], filtered_resolution=True)
CAN_COMPACT =  Has("Resource Compacting Recipes", options=[OptionFilter(RandomizedAbilities, "Compacting", operator="contains")], filtered_resolution=True)

CRAFT_LEATHER_ARMOR = Has("Progressive Armor", options=[OptionFilter(RandomizedAbilities, "Armor", operator="contains")], filtered_resolution=True)

CRAFT_CROSSBOW = Has("Progressive Archery", count=2, options=[OptionFilter(RandomizedAbilities, "Archery", operator="contains")], filtered_resolution=True)
CRAFT_BUCKET = Has("Bucket Recipes", options=[OptionFilter(RandomizedAbilities, "Bucket", operator="contains")], filtered_resolution=True)
CRAFT_FISHING_ROD = Has("Fishing Rod Recipes", options=[OptionFilter(RandomizedAbilities, "Fishing", operator="contains")], filtered_resolution=True)

CAN_SUMMON_WITHER = LO_DAHR & HARD_COMBAT_MANUAL_LOCK & Has("Wither Summoning", options=[OptionFilter(RandomizedAbilities, "Wither_Summoning", operator="contains")], filtered_resolution=True)



def canGoalEnderDragon(world: FabricMinecraftWorld, state: CollectionState):
    return True
    # return canAccessEnd(world, state)

def canCompleteRubyHunt(world: FabricMinecraftWorld, state: CollectionState):
    createMethod = True

    return state.has("Ruby", world.player, floor(world.max_ruby_count * (world.options.percentage_of_rubies_needed.value * 0.01))) and createMethod

def canAccessVanillaEndGame(world: FabricMinecraftWorld, state: CollectionState):
    return True