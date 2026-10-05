# -*- coding: utf-8 -*-
"""
SIMULADOR OFICIAL - DUELO DE CUARTOS DE FINAL KC GRAND CHAMPIONSHIP
JOEY WHEELER VS JAFAR SHIN
"""

import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

deck_joey = [
    "Black Luster Soldier - Envoy of the Beginning", "Chaos Sorcerer", "Jinzo",
    "Blade Knight", "Blade Knight", "D.D. Warrior Lady", "Rocket Warrior", "Freed the Brave Wanderer",
    "Gearfried the Iron Knight", "Gearfried the Iron Knight", "Gearfried the Swordmaster",
    "Zombyra the Dark", "Don Zaloog", "Goblin Attack Force",
    "Marauding Captain", "Marauding Captain", "Exiled Force", "Sangan",
    "Reinforcement of the Army", "Reinforcement of the Army", "The Warrior Returning Alive",
    "Pot of Greed", "Raigeki", "Dark Hole", "Change of Heart", "Mystical Space Typhoon",
    "Book of Moon", "Book of Moon", "Smashing Ground", "Release Restraint",
    "United We Stand", "Question",
    "Mirror Force", "Torrential Tribute", "Bottomless Trap Hole",
    "Compulsory Evacuation Device", "Call of the Haunted", "Kunai with Chain", "Waboku",
    "Ring of Destruction"
]

deck_jafar = [
    "La Jinn the Mystical Genie of the Lamp", "La Jinn the Mystical Genie of the Lamp", "La Jinn the Mystical Genie of the Lamp",
    "Ancient Lamp", "Ancient Lamp", "Ancient Lamp",
    "Mystical Beast Serket", "Mystical Beast Serket",
    "Temple of the Kings", "Temple of the Kings",
    "Apophis the Swamp Deity", "Apophis the Swamp Deity",
    "Pot of Greed", "Tribute to The Doomed", "Mystical Space Typhoon",
    "Swords of Revealing Light", "Card Destruction", "Monster Reborn",
    "Magic Jammer", "Seven Tools of the Bandit",
    "Dust Tornado", "Dust Tornado",
    "Mirror Force", "Jar of Greed", "Jar of Greed",
    "Trap Hole", "Trap Hole", "Waboku",
    "Gravekeeper's Spy", "Gravekeeper's Spy", "Gravekeeper's Spy",
    "Gravekeeper's Guard", "Gravekeeper's Guard",
    "Necrovalley", "Necrovalley",
    "Rite of Spirit", "Rite of Spirit",
    "Terraforming", "Raigeki", "Heavy Storm"
]

rng = secrets.SystemRandom()
j_shuffled = list(deck_joey)
rng.shuffle(j_shuffled)

jafar_shuffled = list(deck_jafar)
rng.shuffle(jafar_shuffled)

print("Mano Joey (5):", j_shuffled[:5])
print("Topdeck Joey (5):", j_shuffled[5:10])
print("\nMano Jafar (5):", jafar_shuffled[:5])
print("Topdeck Jafar (5):", jafar_shuffled[5:10])
