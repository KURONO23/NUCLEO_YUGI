# -*- coding: utf-8 -*-
"""
SIMULADOR Y EJECUTOR DE SEMIFINAL 1: MAKSU VS LEON WILSON
Multi-Agente: Agente 9 (RNG), Agente 2 (Juez), Agente 3 (LP), Agente 8 (Meta GOAT)
"""
import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

deck_maksu = [
    "Chaos Emperor Dragon - Envoy of the End", "Black Luster Soldier - Envoy of the Beginning",
    "Jinzo", "Yata-Garasu", "Breaker the Magical Warrior", "Tribe-Infecting Virus",
    "Injection Fairy Lily", "Spirit Reaper", "Don Zaloog", "Sangan",
    "Witch of the Black Forest", "Magician of Faith", "Cyber Jar", "Fiber Jar",
    "Painful Choice", "Graceful Charity", "Pot of Greed", "Pot of Greed",
    "Delinquent Duo", "The Forceful Sentry", "Harpie's Feather Duster", "Raigeki",
    "Dark Hole", "Dimension Fusion", "Snatch Steal", "Change of Heart",
    "Premature Burial", "Book of Moon", "Book of Moon", "Reinforcement of the Army",
    "United We Stand", "Nobleman of Crossout", "Ring of Destruction", "Ring of Destruction",
    "Mirror Force", "Torrential Tribute", "Imperial Order", "Solemn Judgment",
    "Magic Cylinder", "Robbin' Goblin"
]

deck_leon = [
    "Cinderella", "Cinderella", "Cinderella",
    "Pumpkin Carriage", "Pumpkin Carriage",
    "Iron Hans", "Iron Hans", "Iron Hans",
    "Iron Knight", "Iron Knight", "Iron Knight",
    "Tom Thumb", "Tom Thumb",
    "Little Red Riding Hood", "Little Red Riding Hood",
    "Forest Hunter", "Forest Hunter",
    "Glass Slippers", "Glass Slippers", "Glass Slippers",
    "Curse of Thorns", "Curse of Thorns",
    "Gloomy Woods", "Gloomy Woods",
    "Pot of Greed", "Monster Reborn", "Raigeki", "Dark Hole",
    "Mystical Space Typhoon", "Heavy Storm", "Swords of Revealing Light",
    "Mirror Force", "Waboku", "Waboku", "Magic Cylinder",
    "Seven Tools of the Bandit", "Solemn Wishes", "Solemn Wishes",
    "Spinning Wheel Spindle", "100-Year Awakening"
]

rng = secrets.SystemRandom()
m_shuffled = list(deck_maksu)
rng.shuffle(m_shuffled)

l_shuffled = list(deck_leon)
rng.shuffle(l_shuffled)

print("Mano Maksu (5):", m_shuffled[:5])
print("Topdeck Maksu (5):", m_shuffled[5:10])
print("\nMano Leon (5):", l_shuffled[:5])
print("Topdeck Leon (5):", l_shuffled[5:10])
