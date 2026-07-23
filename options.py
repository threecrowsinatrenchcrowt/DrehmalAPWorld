from dataclasses import dataclass

from Options import PerGameCommonOptions, Choice, Range, ItemSet, OptionSet, OptionGroup, Toggle


########################################################################################################################
# GOAL CONDITION #######################################################################################################
########################################################################################################################

class GoalCondition(Choice):
    """
    Your Goal Condition for your game

    ender_dragon - Goal when the Ender Dragon (Tethlaen) is defeated
    ruby_hunt - Goal when a certain amount of rubies are collected (McGuffin hunt)
    Todo: Add Emissary goal option
    """
    option_ender_dragon = 0
    option_ruby_hunt = 1
    default = 0

class TotalRubiesInGame(Range):
    """
    Maximum possible number of Rubies that will be in the item pool

    If fewer available locations exist in the pool than this number, the number of available locations will be used instead.

    Required Percentage of Rubies will be calculated based off of that number.

    (Only Takes Effect when going for the Ruby Hunt Goal)
    """
    display_name = "Total Rubies In Game"
    range_start = 1
    range_end = 500
    default = 16

class RubyPercentageNeeded(Range):
    """
    The Percentage of Rubies that need to be collected to Goal for Ruby Hunt.
    (Only Takes Effect when going for the Ruby Hunt Goal)
    """
    display_name = "Ruby Percentage Needed"
    range_start = 1
    range_end = 100
    default = 100

########################################################################################################################
# General Options ######################################################################################################
########################################################################################################################

class ExcludedAdvancementTypes(OptionSet):
    """
    Determines Blacklisted advancements in the Randomizer

    Options:
        "Normal" - Disables regular advancements
        "Hard" - Disables advancements that are Hard
        "Exploration" - Disables advancements that are given for discovering a location
        "Unreasonable" - Disables advancements that are EXTREMELY Hard
    """
    display_name = "Excluded Locations"
    default = {
        "Unreasonable"
    }
    valid_keys = {
        "Normal",
        "Hard",
        "Exploration",
        "Unreasonable"
    }

class RandomizedAbilities(OptionSet):
    """
    Determines which abilities and recipes/interactions will be added as items in the item pool
    If an ability is not present in the list they will be treated as unlocked from the start

    These should be treated for now as unstable options
    Drehmal's logic for these, especially in strange combinations, is still very questionable
    """
    display_name = "Ability Shuffle"
    default = {
    }
    valid_keys = {
        "Chests",
        "Jump",
        "Sprint",
        "Swim",
        "Spawn_Point",
        "Wither_Summoning",
        "Trading",
        "Bartering",
        "Brewing",
        "Enchanting",
        "Smithing",
        "Misc_Stations",
        "Bucket",
        "Igniter",
        "Minecarts",
        "Brush",
        "Spyglass",
        "Shears",
        "Ender_Eye",
        "Fishing",
        "Bottles",
        "Compacting",
        "Shield",
        "Bundles",
        "TNT",
        "Tools",
        "Weapons",
        "Archery",
        "Armor",
        "Smelting",
        "Dyes"
    }

class RandomizedMythicals(Toggle):
    """
    Adds Drehmal's Mythical weapons to the item and location pool.
    """

    display_name = "Randomize Mythicals"

class RandomizedLegendaries(Toggle):
    """
    Adds Drehmal's Legendary items to the item and location pool.
    """

    display_name = "Randomize Legendaries"

class RandomizedTerminusTowers(Choice):
    """
    Adds Drehmal's fast travel Terminus towers to the item and location pool. 
    If option region_locks is selected, you will not be able to enter a region until you have obtained its corresponding Terminus tower.
    (Capital Valley tower will always be unlocked to prevent softlocks.)
    """
    option_no = 0
    option_yes = 1
    option_region_locks = 2

class RandomizedQuestItems(Toggle):
    """
    Adds miscellaneous quest items from Drehmal to the item and location pool.
    Fervor Stones, Frenzy Fragments, Left and Right Blade Fragments, Nihilist's Notes, Yavhlix Overrides
    """

class RandomizedRelics(Toggle):
     """
    Adds all four stages of each of the 11 relics to the item and location pool.
    """

class ScoutTediousLocations(Toggle):
    """
    Automatically sends hints for tedious locations, including devotion relics and items locked behind clearing the Foundry
    """ 

########################################################################################################################
# TRAP STUFF ###########################################################################################################
########################################################################################################################

class TrapFillPercentage(Range):
    """
    Replace a percentage of junk items in the item pool with random traps
    """
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 0

class BaseTrapWeight(Choice):
    """
    Base Class for Trap Weights
    """
    option_none = 0
    option_low = 1
    option_medium = 2
    option_high = 4
    default = 2

class ReverseControlsTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which causes WASD, Shift, Jump, Break, and Place to Swap for a short duration
    """
    display_name = "Reverse Controls Trap Weight"

class InvertedMouseTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which causes the Mouse to Invert for a short duration
    """
    display_name = "Inverted Mouse Trap Weight"

class IceTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which causes all blocks to become slippery for a short duration
    """
    display_name = "Ice Trap Weight"

class RandomEffectTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which applies a random Negative Status Effect
    """
    display_name = "Random Status Effect Trap Weight"

class StunTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap that temporarily stops movement of the player
    """
    display_name = "Stun Trap Weight"

class TNTTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap that spawns a block of lit TNT on the player's position
    """
    display_name = "TNT Trap Weight"

class TeleportTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap that Teleports the player similar to Chorus Fruit
    """
    display_name = "Teleport Trap Weight"

class BeeTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap that Spawns 6 angry bees near the player
    """
    display_name = "Bee Trap Weight"

class LiteratureTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap that Opens Literature Pop-Ups
    """
    display_name = "Literature Trap Weight"

class DeathLink(Toggle):
    """
    Enable DeathLink
    """
    display_name = "DeathLink"
    default = False

class TrapLink(Toggle):
    """
    Enable TrapLink
    """
    display_name = "TrapLink"
    default = False


@dataclass
class FMCOptions(PerGameCommonOptions):
    # Goal Related Options
    goal_condition: GoalCondition
    percentage_of_rubies_needed: RubyPercentageNeeded
    total_rubies: TotalRubiesInGame
    # General Settings
    excluded_advancements: ExcludedAdvancementTypes
    randomized_abilities: RandomizedAbilities
    randomized_mythicals: RandomizedMythicals
    randomized_legendaries: RandomizedLegendaries
    randomized_terminus_towers: RandomizedTerminusTowers
    randomized_quest_items: RandomizedQuestItems
    randomized_relics: RandomizedRelics
    scout_tedious_locations: ScoutTediousLocations
    # Traps
    trap_fill_percentage: TrapFillPercentage
    reverse_controls_trap_weight: ReverseControlsTrapWeight
    inverted_mouse_trap_weight: InvertedMouseTrapWeight
    ice_trap_weight: IceTrapWeight
    random_effect_trap_weight: RandomEffectTrapWeight
    stun_trap_weight: StunTrapWeight
    tnt_trap_weight: TNTTrapWeight
    teleport_trap_weight: TeleportTrapWeight
    bee_trap_weight: BeeTrapWeight
    literature_trap_weight: LiteratureTrapWeight
    # Link Options
    deathlink_enabled: DeathLink
    traplink_enabled: TrapLink

option_groups = [
    OptionGroup(
        "Goal Options",
        [GoalCondition, RubyPercentageNeeded, TotalRubiesInGame]
    ),
    OptionGroup(
        "Item Pools",
        [ExcludedAdvancementTypes, RandomizedAbilities, RandomizedMythicals, RandomizedLegendaries, RandomizedTerminusTowers, RandomizedQuestItems, RandomizedRelics, ScoutTediousLocations]
    ),
    OptionGroup(
        "Traps Options",
        [TrapFillPercentage, ReverseControlsTrapWeight, InvertedMouseTrapWeight, IceTrapWeight, RandomEffectTrapWeight, StunTrapWeight, TNTTrapWeight, TeleportTrapWeight, BeeTrapWeight, LiteratureTrapWeight]
    ),
    OptionGroup(
        "World Link Options",
        [DeathLink, TrapLink]
    )
]
