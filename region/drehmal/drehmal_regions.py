from __future__ import annotations

from worlds.drehmal.region.mc_regions_consts import *
from worlds.drehmal.region.regions_helper import create_locations_and_connect, smart_add_rule
from worlds.drehmal.logic.vanilla_logic import *

def create_drehmal_regions(world: FabricMinecraftWorld):
    create_locations_and_connect(world, "Menu", "CapitalValley", {
        "Children of Drehmal": ADVANCEMENT_EXPLORATION,
        "Chamber of Dreams": ADVANCEMENT_EXPLORATION,
        "Deja Vu": ADVANCEMENT_EXPLORATION
    })

    create_locations_and_connect(world, "Menu", "PalisadesHeath", {
        "Serpent's Chosen": ADVANCEMENT_EXPLORATION,

        "Palisades Heath Tower": TERMINUS_TOWERS
    }, PALISADES_HEATH)

    create_locations_and_connect(world, "Menu", "AvSal", {
        "Remnant of Avsohm": ADVANCEMENT_EXPLORATION,

        "Inert Mythbreaker": MYTHICALS,

        "Av'Sal Tower": TERMINUS_TOWERS
    }, AV_SAL)
    smart_add_rule(world,"Inert Mythbreaker", INERT_MB, MYTHICALS)

    create_locations_and_connect(world, "Menu", "GulfOfDrehmal", {
        "Gulf of Drehmal Tower": TERMINUS_TOWERS
    }, GULF_OF_DREHMAL)

    create_locations_and_connect(world, "Menu", "Merijool", {
        "I.C.S. Arbiter": ADVANCEMENT_EXPLORATION,
        "Village of Autumn": ADVANCEMENT_EXPLORATION,
        "Glade of the Giant": ADVANCEMENT_EXPLORATION,
        "Ash Heap": ADVANCEMENT_EXPLORATION,

        "Parenchyma": LEGENDARIES,
        "Whispersong": LEGENDARIES,

        "Merijool Tower": TERMINUS_TOWERS,

        "Glade of the Giant Stone of Agony": QUEST_ITEMS
    }, MERIJOOL)
    smart_add_rule(world,"Parenchyma", CHESTS & SWIM, LEGENDARIES)
    smart_add_rule(world,"Whispersong", CHESTS, LEGENDARIES)
    smart_add_rule(world, "Glade of the Giant Stone of Agony", CHESTS, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "Casai", {  
        "Jewel of Casai": ADVANCEMENT_EXPLORATION,
        "Vault of Knowledge": ADVANCEMENT_EXPLORATION,
        "Death's Embrace": ADVANCEMENT_EXPLORATION,

        "Ultva's Bowblade": LEGENDARIES,

        "Casai Tower": TERMINUS_TOWERS,

         "Zarha Ruins Stone of Luxury": QUEST_ITEMS
    }, CASAI)
    smart_add_rule(world,"Ultva's Bowblade", CHESTS, LEGENDARIES)
    smart_add_rule(world, "Zarha Ruins Stone of Luxury", CHESTS & EBONFIRE, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "AnyrNogur", {
        "The Foundry": ADVANCEMENT_EXPLORATION,
        "Rip & Tear": ADVANCEMENT_EXPLORATION,
        "Supersoldier Certification": ADVANCEMENT_EXPLORATION,
        "Capital of War": ADVANCEMENT_EXPLORATION,
        
        "Zenith": MYTHICALS,

        "Emperor Anyr's Scepter": LEGENDARIES,
        "Warp Horse Armor": LEGENDARIES,
        "Warp Horse Receiver": LEGENDARIES,

        "Anyr'Nogur Tower": TERMINUS_TOWERS,

        "Foundry Speedrun Stone of Luxury": QUEST_ITEMS,
        "Tall Tower Stone of Worry": QUEST_ITEMS,
        "Tank Keyfob": QUEST_ITEMS,
        "Foundry Lever 3": QUEST_ITEMS
    }, ANYR_NOGUR)
    smart_add_rule(world,"Rip & Tear", FOUNDRY_ENTRY, ADVANCEMENT_EXPLORATION)
    smart_add_rule(world,"Supersoldier Certification", FOUNDRY_ENTRY & HARD_COMBAT_MANUAL_LOCK, ADVANCEMENT_EXPLORATION)
    smart_add_rule(world,"Zenith", FOUNDRY_ENTRY & HARD_COMBAT_MANUAL_LOCK, MYTHICALS)
    smart_add_rule(world,"Emperor Anyr's Scepter", CHESTS, LEGENDARIES)
    smart_add_rule(world,"Warp Horse Armor", CHESTS & RIGHT_BLADE_FRAG, LEGENDARIES)
    smart_add_rule(world,"Warp Horse Receiver", CHESTS & RIGHT_BLADE_FRAG, LEGENDARIES)
    smart_add_rule(world, "Foundry Speedrun Stone of Luxury", FOUNDRY_ENTRY & HARD_COMBAT_MANUAL_LOCK & OPEN_WORLD, QUEST_ITEMS)
    smart_add_rule(world, "Tall Tower Stone of Worry", CHESTS, QUEST_ITEMS)
    smart_add_rule(world, "Tank Keyfob", CHESTS & RIGHT_BLADE_FRAG, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "Ebonfire", {
        "Children of Mael": ADVANCEMENT_EXPLORATION,
        "Wall of the West": ADVANCEMENT_EXPLORATION,

        "Flammer": LEGENDARIES,

        "Mt. Ebonfire Tower": TERMINUS_TOWERS,

        "Foundry Lever 1": QUEST_ITEMS
    }, EBONFIRE)
    smart_add_rule(world,"Flammer", CHESTS, LEGENDARIES)

    create_locations_and_connect(world, "Menu", "NimahjSwamp", {
        "All That Remains": ADVANCEMENT_EXPLORATION,

        "Voidtear Dagger": LEGENDARIES,

        "Nimahj Swamp Tower": TERMINUS_TOWERS,

        "Right Blade Fragment": QUEST_ITEMS
    }, NIMAHJ_SWAMP)
    smart_add_rule(world,"Voidtear Dagger", EXODUS_ENTRY & SWIM, LEGENDARIES)
    smart_add_rule(world, "Right Blade Fragment", RIGHT_BLADE_FRAG, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "EbonyVeldt", {
        "Underground Fortress": ADVANCEMENT_EXPLORATION,

        "Penumbra": LEGENDARIES,

        "Ebony Veldt Tower": TERMINUS_TOWERS,

        "Caer Adacia Stone of Worry": QUEST_ITEMS,
        "Foundry Lever 2": QUEST_ITEMS
    }, EBONY_VELDT)
    smart_add_rule(world,"Penumbra", CHESTS, LEGENDARIES)

    create_locations_and_connect(world, "Menu", "LorahnKahl", {
        "Village of Three Moons": ADVANCEMENT_EXPLORATION,
        "The Moonlight Sanctum": ADVANCEMENT_EXPLORATION,

        "Ascendance": MYTHICALS,

        "Lorahn'Kahl Tower": TERMINUS_TOWERS,

        "Moonlight Sanctum Stone of Agony": QUEST_ITEMS
    }, LORAHN_KAHL)
    smart_add_rule(world,"Ascendance", CRAFT_TNT | HARD_COMBAT_MANUAL_LOCK, MYTHICALS)
    smart_add_rule(world,"Moonlight Sanctum Stone of Agony", CHESTS, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "NorthTharxax", {
        "The Old Guard": ADVANCEMENT_EXPLORATION,

        "Osteogenesis": LEGENDARIES,

        "North Tharxax Tower": TERMINUS_TOWERS
    }, NORTH_THARXAX)
    smart_add_rule(world,"Osteogenesis", CHESTS, LEGENDARIES)

    create_locations_and_connect(world, "Menu", "SouthTharxax", {
        "Lofty Laboratory": ADVANCEMENT_EXPLORATION,
        "Ohh, bouncy!": ADVANCEMENT_EXPLORATION,
        "WUPOM (Wealthy Under Protection of Mael)": ADVANCEMENT_EXPLORATION,

        "AvPod": LEGENDARIES,

        "South Tharxax Tower": TERMINUS_TOWERS,

        "Loraga Keep Stone of Luxury": QUEST_ITEMS
    }, SOUTH_THARXAX)
    smart_add_rule(world,"AvPod", CHESTS, LEGENDARIES)
    smart_add_rule(world, "Loraga Keep Stone of Luxury", CHESTS, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "Carmine", {
        "Meat. They're made out of meat.": ADVANCEMENT_EXPLORATION,
        "City of Chaos": ADVANCEMENT_EXPLORATION,
        "Rites of Cruelty": ADVANCEMENT_EXPLORATION,

        "Eyebiter": LEGENDARIES,

        "Carmine Tower": TERMINUS_TOWERS
    }, CARMINE)
    smart_add_rule(world,"Eyebiter", CHESTS, LEGENDARIES)

    create_locations_and_connect(world, "Menu", "Hellcrags", {
        "Domain of Maelihs": ADVANCEMENT_EXPLORATION,
        "The Burnt Palace": ADVANCEMENT_EXPLORATION,

        "Malevolentia": MYTHICALS,

        "Hellcrags Tower": TERMINUS_TOWERS,

        "Burnt Palace Stone of Luxury": QUEST_ITEMS
    }, HELLCRAGS)
    smart_add_rule(world,"Malevolentia", HARD_COMBAT_MANUAL_LOCK, MYTHICALS)
    smart_add_rule(world, "Burnt Palace Stone of Luxury", CHESTS, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "AkhloRohma", {
        "Upper-Upper Class": ADVANCEMENT_EXPLORATION,
        "The Painted City": ADVANCEMENT_EXPLORATION,
        "Flower Power": ADVANCEMENT_EXPLORATION,

        "Orchidaceae": LEGENDARIES,

        "Akhlo'Rohma Tower": TERMINUS_TOWERS,

        "Ancehl Castle Stone of Agony": QUEST_ITEMS
    }, AKHLO_ROHMA)
    smart_add_rule(world,"Orchidaceae", CHESTS, LEGENDARIES)

    create_locations_and_connect(world, "Menu", "NorthHeartwood", {
        "People of the Heartwood": ADVANCEMENT_EXPLORATION,
        "The Beast's Den": ADVANCEMENT_EXPLORATION,
        "The Scarred Castle": ADVANCEMENT_EXPLORATION,

        "The Heartaxe": LEGENDARIES,
        "One Thousand Scars": LEGENDARIES,

        "North Heartwood Tower": TERMINUS_TOWERS,

        "North Heartwood Stone of Luxury": QUEST_ITEMS
    }, NORTH_HEARTWOOD)
    smart_add_rule(world,"The Heartaxe", CHESTS, LEGENDARIES)
    smart_add_rule(world,"One Thousand Scars", CHESTS, LEGENDARIES)
    smart_add_rule(world, "North Heartwood Stone of Luxury", CHESTS, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "PurityPeaks", {
        "Temporal Ruins": ADVANCEMENT_EXPLORATION,
        
        "Avsohm'Kohl": LEGENDARIES,

        "Purity Peaks Tower": TERMINUS_TOWERS,

        "Left Blade Fragment": QUEST_ITEMS,
        "Tehrmari Monastery Stone of Luxury": QUEST_ITEMS
    }, PURITY_PEAKS)
    smart_add_rule(world, "Avsohm'Kohl", JUMP & SPRINT & CHESTS, LEGENDARIES)
    smart_add_rule(world, "Left Blade Fragment", LEFT_BLADE_FRAG, QUEST_ITEMS)
    smart_add_rule(world, "Tehrmari Monastery Stone of Luxury", CHESTS & GRAND_PIKE_CANYON, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "MaelsDesolation", {
        "This place was beautiful, once": ADVANCEMENT_EXPLORATION,
        "Avast!": ADVANCEMENT_EXPLORATION,
        
        "Calamity": MYTHICALS,

        "South Heartwood Tower": TERMINUS_TOWERS,

        "Epicenter of the Desolation Stone of Worry": QUEST_ITEMS
    }, MAELS_DESOLATION)
    smart_add_rule(world, "Calamity", HARD_COMBAT_MANUAL_LOCK, MYTHICALS)
    smart_add_rule(world, "Epicenter of the Desolation Stone of Worry", CHESTS, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "SpearheadForest", {
        "Disappearing Act": ADVANCEMENT_EXPLORATION,
        "The Insohmic Library": ADVANCEMENT_EXPLORATION,
        "Children of Virtuo": ADVANCEMENT_EXPLORATION,

        "Hovadchear's Greathammer": LEGENDARIES,
        "Peace Treaty": LEGENDARIES,

        "Spearhead Forest Tower": TERMINUS_TOWERS,

        "Coven of Potentia Stone of Agony": QUEST_ITEMS
    }, SPEARHEAD_FOREST)
    smart_add_rule(world, "Hovadchear's Greathammer", CHESTS, LEGENDARIES)
    smart_add_rule(world, "Peace Treaty", CHESTS, LEGENDARIES)
    smart_add_rule(world, "Coven of Potentia Stone of Agony", CHESTS, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "BlackJungle", {
        "Pilgrim's Eye": ADVANCEMENT_EXPLORATION,
        "City of Tides": ADVANCEMENT_EXPLORATION,
        "Monastery of Virtuo": ADVANCEMENT_EXPLORATION,

        "Masayoshi": LEGENDARIES,
        "Pure Corruption": LEGENDARIES,

        "Black Jungle Tower": TERMINUS_TOWERS,

        "Blackstone Ruins Stone of Agony": QUEST_ITEMS
    }, BLACK_JUNGLE)
    smart_add_rule(world, "Masayoshi", CHESTS, LEGENDARIES)
    smart_add_rule(world, "Pure Corruption", CHESTS, LEGENDARIES)
    smart_add_rule(world, "Blackstone Ruins Stone of Agony", CHESTS, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "VeruhktPlateau", {
        "Secret Sanctum": ADVANCEMENT_EXPLORATION,

        "Tul'Vohaln": LEGENDARIES,

        "Veruhkt Plateau Tower": TERMINUS_TOWERS,

        "Sal'Veruhkt Stone of Luxury": QUEST_ITEMS
    }, VERUHKT_PLATEAU)
    smart_add_rule(world, "Tul'Vohaln", CHESTS, LEGENDARIES)
    smart_add_rule(world, "Sal'Veruhkt Stone of Luxury", CHESTS & GRAND_PIKE_CANYON, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "GrandPikeCanyon", {
        "I'm on the moooon... it's made of cheeeeese...": ADVANCEMENT_EXPLORATION,
        "Shatterhorn Gulch": ADVANCEMENT_EXPLORATION,
        "If These Walls Could Talk": ADVANCEMENT_EXPLORATION,

        "Festering Strides": LEGENDARIES,

        "Grand Pike Canyon Tower": TERMINUS_TOWERS
    }, GRAND_PIKE_CANYON)

    create_locations_and_connect(world, "Menu", "HighfallTundra", {
        "Impoverished Nobles": ADVANCEMENT_EXPLORATION,

        "Highfall Tundra Tower": TERMINUS_TOWERS,

        "Highfall Tundra Ruins Stone of Worry": QUEST_ITEMS
    }, HIGHFALL_TUNDRA)
    smart_add_rule(world, "Highfall Tundra Ruins Stone of Worry", CHESTS, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "FrozenBite", {
        "Frozen Bite Tower": TERMINUS_TOWERS,

        "Nihilist's Notes": QUEST_ITEMS
    }, FROZEN_BITE)
    smart_add_rule(world, "Nihilist's Notes", CHESTS, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "Faehrcyle", {
        "Finders Keepers": ADVANCEMENT_EXPLORATION,
        "Grave of Frost": ADVANCEMENT_EXPLORATION,
        "The Lost Cavern": ADVANCEMENT_EXPLORATION,
        "At the Mountain of Madness": ADVANCEMENT_EXPLORATION,

        "Oblivion": MYTHICALS,

        "The Frostfang": LEGENDARIES,
        "Rehntite Plate Mail": LEGENDARIES,

        "Faehrcyle Tower": TERMINUS_TOWERS,

        "Oblivion Labyrinth Stone of Worry": QUEST_ITEMS
    }, FAEHRCYLE)
    smart_add_rule(world, "Oblivion", OBLIVION_LABYRINTH, MYTHICALS)
    smart_add_rule(world, "The Frostfang", CHESTS, LEGENDARIES)
    smart_add_rule(world, "Rehntite Plate Mail", CHESTS, LEGENDARIES)
    smart_add_rule(world, "Oblivion Labyrinth Stone of Worry", CHESTS & OBLIVION_LABYRINTH, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "DawnIsland", {
        "Place of Conversion": ADVANCEMENT_EXPLORATION,
        
        "Island of Dawn Tower": TERMINUS_TOWERS,

        "Xor'huul Stone of Agony": QUEST_ITEMS,
        "West of Yavhlix Stone of Agony": QUEST_ITEMS
    }, DAWN_ISLAND)
    smart_add_rule(world, "Xor'huul Stone of Agony", CHESTS, QUEST_ITEMS)
    smart_add_rule(world, "West of Yavhlix Stone of Agony", CHESTS & FAEHRCYLE, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "DuskIsland", {
        "Crystal Digging Claws": LEGENDARIES,

        "Island of Dusk Tower": TERMINUS_TOWERS
    }, DUSK_ISLAND)
    smart_add_rule(world, "Crystal Digging Claws", CHESTS, LEGENDARIES)

    create_locations_and_connect(world, "Menu", "Sahd", {
        "The Forgotten City": ADVANCEMENT_EXPLORATION,

        "Frenzy": MYTHICALS,

        "Sahd Tower": TERMINUS_TOWERS,

        "Fragment of Fury": QUEST_ITEMS,
        "Fragment of Hate": QUEST_ITEMS,
        "Fragment of Pain": QUEST_ITEMS,
        "Fragment of Rage": QUEST_ITEMS,
        "Fragment of Wrath": QUEST_ITEMS,
        "Sahd Stone of Worry": QUEST_ITEMS
    }, SAHD)
    smart_add_rule(world, "Frenzy", FRENZY, MYTHICALS)
    smart_add_rule(world, "Fragment of Fury", CHESTS, QUEST_ITEMS)
    smart_add_rule(world, "Fragment of Hate", CHESTS, QUEST_ITEMS)
    smart_add_rule(world, "Fragment of Pain", CHESTS, QUEST_ITEMS)
    smart_add_rule(world, "Fragment of Rage", CHESTS, QUEST_ITEMS)
    smart_add_rule(world, "Fragment of Wrath", CHESTS, QUEST_ITEMS)
    smart_add_rule(world, "Sahd Stone of Worry", CHESTS, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "LoDahr", {
        "Greyspire Castle": ADVANCEMENT_EXPLORATION,
        "Augural Tangle": ADVANCEMENT_EXPLORATION,
        "Challenger's Grotto": ADVANCEMENT_EXPLORATION,
        "Ancient Enterprise": ADVANCEMENT_EXPLORATION,
        "Abyssal Rise": ADVANCEMENT_EXPLORATION,
        "Class in Session": ADVANCEMENT_EXPLORATION,
        "What Puzzles Do You Bear?": ADVANCEMENT_EXPLORATION,
        "Mystic Gallery": ADVANCEMENT_EXPLORATION,
        "Brightwyrm's Caldarium": ADVANCEMENT_EXPLORATION,
        "Apotheosis": ADVANCEMENT_EXPLORATION,
        "Distant Lights": ADVANCEMENT_EXPLORATION,
        "Hypogean Labyrinth": ADVANCEMENT_EXPLORATION,
        "Final Harvest": ADVANCEMENT_EXPLORATION,
        "A Bridge Between Worlds": ADVANCEMENT_EXPLORATION,
        "Star-Rise Orrery": ADVANCEMENT_EXPLORATION,
        "Put a Ring on it": ADVANCEMENT_EXPLORATION,
        "Some Hope For the Future?": ADVANCEMENT_EXPLORATION,
        "Atop Paradise": ADVANCEMENT_EXPLORATION,
        "Heart of the Tempest": ADVANCEMENT_EXPLORATION,
        "Temple of Life": ADVANCEMENT_EXPLORATION,
        "Pantheon": ADVANCEMENT_EXPLORATION,

        "Syzygy": MYTHICALS,

        "Aeongale": LEGENDARIES,
        "Eldermead": LEGENDARIES,
        "Magestep": LEGENDARIES,
        "Proxigea": LEGENDARIES,
        "Stasis Bolts": LEGENDARIES,
        "Thundercrux": LEGENDARIES,

        "Fort Aelon Stone of Agony": QUEST_ITEMS,
        "Greyspire Castle Stone of Worry": QUEST_ITEMS,
        "Naharja Stone of Luxury": QUEST_ITEMS
    }, LO_DAHR)
    smart_add_rule(world, "Some Hope For the Future?", SWIM, ADVANCEMENT_EXPLORATION)
    smart_add_rule(world, "Heart of the Tempest", (NO_LEGENDARIES & LEFT_BLADE_FRAG) | (YES_LEGENDARIES & HAS_WINGS), ADVANCEMENT_EXPLORATION)
    smart_add_rule(world, "Syzygy", SWIM, MYTHICALS)
    smart_add_rule(world, "Aeongale", HARD_COMBAT_MANUAL_LOCK & CHESTS, LEGENDARIES)
    smart_add_rule(world, "Eldermead", CHESTS, LEGENDARIES)
    smart_add_rule(world, "Magestep", CHESTS & JUMP & SPRINT, LEGENDARIES)
    smart_add_rule(world, "Proxigea", CHESTS & SWIM & HARD_COMBAT_MANUAL_LOCK, LEGENDARIES)
    smart_add_rule(world, "Stasis Bolts", CHESTS, LEGENDARIES)
    smart_add_rule(world, "Thundercrux", ((NO_LEGENDARIES & LEFT_BLADE_FRAG) | (YES_LEGENDARIES & HAS_WINGS)) & CHESTS, LEGENDARIES)
    smart_add_rule(world, "Fort Aelon Stone of Agony", CHESTS, QUEST_ITEMS)
    smart_add_rule(world, "Greyspire Castle Stone of Worry", CHESTS, QUEST_ITEMS)
    smart_add_rule(world, "Naharja Stone of Luxury", CHESTS, QUEST_ITEMS)

    create_locations_and_connect(world, "Menu", "Aphelion", {
        "Aphelion Tower": TERMINUS_TOWERS,
        "Lo'Dahr Tower": TERMINUS_TOWERS
    }, APHELION)
    smart_add_rule(world, "Aphelion Tower", JUMP & SPRINT, TERMINUS_TOWERS)
    smart_add_rule(world, "Lo'Dahr Tower", JUMP & SPRINT, TERMINUS_TOWERS)

    create_locations_and_connect(world, "Menu", "Yavhlix", {
        "Yavhlix Lever 1": QUEST_ITEMS,
        "Yavhlix Lever 2": QUEST_ITEMS,
        "Yavhlix Lever 3": QUEST_ITEMS
    }, YAVHLIX)
    smart_add_rule(world, "Yavhlix Lever 1", HARD_COMBAT_MANUAL_LOCK, QUEST_ITEMS)
    smart_add_rule(world, "Yavhlix Lever 2", HARD_COMBAT_MANUAL_LOCK, QUEST_ITEMS)
    smart_add_rule(world, "Yavhlix Lever 3", HARD_COMBAT_MANUAL_LOCK, QUEST_ITEMS)