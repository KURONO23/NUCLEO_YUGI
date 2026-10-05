# -*- coding: utf-8 -*-
"""
MOTOR OFICIAL DE SIMULACIÓN - LA GRAN FINAL FUN
MAKSU (PINGÜINOS & FLIP-FLOP) VS JOEY WHEELER (GRAN CASINO & DADOS)
True RNG con secrets.SystemRandom()
"""

import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

deck_maksu_fun = [
    "Penguin Soldier", "Penguin Soldier", "Penguin Soldier",
    "Hane-Hane", "Hane-Hane",
    "Medusa Worm", "Medusa Worm",
    "Golem Sentry", "Golem Sentry",
    "Man-Eater Bug", "Man-Eater Bug",
    "Spear Cretin", "Spear Cretin",
    "Magician of Faith", "Magician of Faith",
    "Morphing Jar", "Sangan", "Night Assailant",
    "Book of Moon", "Book of Moon", "Book of Moon",
    "Swords of Concealing Light", "Swords of Concealing Light",
    "Level Limit - Area B", "Level Limit - Area B",
    "Pot of Greed", "Monster Reborn", "Creature Swap",
    "Mystical Space Typhoon", "Heavy Storm", "Swords of Revealing Light",
    "The Shallow Grave",
    "Compulsory Evacuation Device", "Compulsory Evacuation Device",
    "Gravity Bind", "Gravity Bind",
    "Waboku", "Waboku",
    "Ceasefire", "Desert Sunlight"
]

deck_joey_fun = [
    "Dice Jar", "Dice Jar", "Dice Jar",
    "Time Wizard", "Time Wizard",
    "Blowback Dragon", "Blowback Dragon",
    "Blindly Loyal Goblin", "Blindly Loyal Goblin",
    "Maximum Six", "Maximum Six",
    "Sasuke Samurai #4", "Sasuke Samurai #4",
    "Sand Gambler", "Sand Gambler",
    "Sangan", "Abyssal Carper", "Abyssal Carper",
    "Second Coin Toss", "Second Coin Toss",
    "Dangerous Machine Type-6", "Dangerous Machine Type-6",
    "Question", "Question",
    "Graceful Dice", "Graceful Dice",
    "Monster Reborn", "Pot of Greed", "Heavy Storm",
    "Mystical Space Typhoon", "Swords of Revealing Light", "Book of Moon",
    "Fairy Box", "Fairy Box",
    "Skull Dice", "Skull Dice",
    "Gamble", "Gamble",
    "Roulette Spider", "Call of the Haunted"
]

rng = secrets.SystemRandom()
m_shuffled = list(deck_maksu_fun)
rng.shuffle(m_shuffled)

j_shuffled = list(deck_joey_fun)
rng.shuffle(j_shuffled)

print("=== BARAJADO OFICIAL DE LA GRAN FINAL FUN ===")
print("Mano Maksu (5):", m_shuffled[:5])
print("Topdeck Maksu (5):", m_shuffled[5:10])
print("\nMano Joey (5):", j_shuffled[:5])
print("Topdeck Joey (5):", j_shuffled[5:10])
