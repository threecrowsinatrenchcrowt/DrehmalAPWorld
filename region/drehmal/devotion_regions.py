from __future__ import annotations

from worlds.drehmal.region.mc_regions_consts import *
from worlds.drehmal.region.regions_helper import create_locations_and_connect, smart_add_rule
from worlds.drehmal.logic.vanilla_logic import *

def create_devotion_regions(world: FabricMinecraftWorld):
    create_locations_and_connect(world, "Menu", "DahrDevotion", {
        "Writ of Authority +0": RELICS,
        "Writ of Authority +1": RELICS,
        "Writ of Authority +2": RELICS,
        "Writ of Authority +3": RELICS
    }, (MAELS_DESOLATION | LO_DAHR) & LORAHN_KAHL)

    create_locations_and_connect(world, "Menu", "DrehmalDevotion", {
        "Effloresce +0": RELICS,
        "Effloresce +1": RELICS,
        "Effloresce +2": RELICS,
        "Effloresce +3": RELICS
    }, PALISADES_HEATH | LO_DAHR)

    create_locations_and_connect(world, "Menu", "KhiveDevotion", {
        "Mysterial +0": RELICS,
        "Mysterial +1": RELICS,
        "Mysterial +2": RELICS,
        "Mysterial +3": RELICS
    })

    create_locations_and_connect(world, "Menu", "LaiDevotion", {
        "Ardorbrand +0": RELICS,
        "Ardorbrand +1": RELICS,
        "Ardorbrand +2": RELICS,
        "Ardorbrand +3": RELICS
    }, MERIJOOL | LO_DAHR)

    create_locations_and_connect(world, "Menu", "LoeDevotion", {
        "Cryostatic +0": RELICS,
        "Cryostatic +1": RELICS,
        "Cryostatic +2": RELICS,
        "Cryostatic +3": RELICS
    }, FAEHRCYLE | LO_DAHR)

    create_locations_and_connect(world, "Menu", "MaelihsDevotion", {
        "Sprout of Anguish +0": RELICS,
        "Sprout of Anguish +1": RELICS,
        "Sprout of Anguish +2": RELICS,
        "Sprout of Anguish +3": RELICS
    }, (CARMINE | LO_DAHR) & CRAFT_TNT)

    create_locations_and_connect(world, "Menu", "RihelmaDevotion", {
        "Mirror of Frailty": RELICS,
        "Mirror of Lethargy": RELICS,
        "Mirror of Miasma": RELICS,
        "Mirror of Entropy": RELICS
    }, (DAWN_ISLAND | LO_DAHR) & VERUHKT_PLATEAU)

    create_locations_and_connect(world, "Menu", "TaihgelDevotion", {
        "Orogeny +0": RELICS,
        "Orogeny +1": RELICS,
        "Orogeny +2": RELICS,
        "Orogeny +3": RELICS
    }, (GRAND_PIKE_CANYON | LO_DAHR) & HELLCRAGS)

    create_locations_and_connect(world, "Menu", "VayniklahDevotion", {
        "Resplendence +0": RELICS,
        "Resplendence +1": RELICS,
        "Resplendence +2": RELICS,
        "Resplendence +3": RELICS
    }, (AKHLO_ROHMA | LO_DAHR) & ANYR_NOGUR)

    create_locations_and_connect(world, "Menu", "VirtuoDevotion", {
        "Purifying Light +0": RELICS,
        "Purifying Light +1": RELICS,
        "Purifying Light +2": RELICS,
        "Purifying Light +3": RELICS
    }, (BLACK_JUNGLE | LO_DAHR) & (CASAI | NORTH_HEARTWOOD))

    create_locations_and_connect(world, "Menu", "VoynahlahDevotion", {
        "Mortality +0": RELICS,
        "Mortality +1": RELICS,
        "Mortality +2": RELICS,
        "Mortality +3": RELICS
    }, (CASAI | LO_DAHR) & LO_DAHR)