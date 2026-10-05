# -*- coding: utf-8 -*-
import sys
import secrets

# Mazo de Maksu completo (40 cartas):
deck_maksu = [
    "Jinzo",
    "Injection Fairy Lily",
    "Tribe-Infecting Virus",
    "Breaker the Magical Warrior",
    "Spirit Reaper", "Spirit Reaper",
    "Goblin Attack Force",
    "Zombyra the Dark",
    "Spear Dragon",
    "Don Zaloog",
    "Sangan", "Witch of the Black Forest",
    "Cyber Jar", "Fiber Jar",
    "Graceful Charity",
    "Pot of Greed", "Pot of Greed",
    "Raigeki", "Dark Hole",
    "Harpie's Feather Duster",
    "Delinquent Duo",
    "The Forceful Sentry",
    "Painful Choice",
    "Book of Moon", "Book of Moon",
    "Snatch Steal", "Change of Heart",
    "United We Stand",
    "Reinforcement of the Army",
    "Nobleman of Crossout",
    "Premature Burial",
    "Magic Cylinder", "Magic Cylinder",
    "Waboku", "Waboku",
    "Mirror Force",
    "Torrential Tribute",
    "Imperial Order",
    "Ring of Destruction",
    "Solemn Judgment"
]

# Mazo de Dmitri completo (40 cartas):
deck_dmitri = [
    "Mechanicalchaser", "Mechanicalchaser", "Mechanicalchaser",
    "Cyber-Tech Alligator", "Cyber-Tech Alligator",
    "Jinzo",
    "Reflect Bounder", "Reflect Bounder", "Reflect Bounder",
    "Heavy Mech Support Platform", "Heavy Mech Support Platform",
    "Sangan", "Witch of the Black Forest",
    "Breaker the Magical Warrior",
    "Cannon Soldier", "Cannon Soldier",
    "Limiter Removal", "Limiter Removal", "Limiter Removal",
    "Premature Burial", "Snatch Steal",
    "Pot of Greed", "Graceful Charity",
    "Raigeki", "Dark Hole", "Heavy Storm", "Harpie's Feather Duster",
    "Mystical Space Typhoon", "Mystical Space Typhoon",
    "United We Stand", "Mage Power", "Nobleman of Crossout",
    "Mirror Force", "Torrential Tribute", "Ring of Destruction", "Imperial Order",
    "Solemn Judgment", "Solemn Judgment",
    "Call of the Haunted", "Magic Jammer"
]

rng = secrets.SystemRandom()

rng.shuffle(deck_maksu)
rng.shuffle(deck_dmitri)

# Ambos roban 5 cartas nuevas
mano_maksu_5 = [deck_maksu.pop(0) for _ in range(5)]
mano_dmitri_5 = [deck_dmitri.pop(0) for _ in range(5)]

print("=== NUEVA MANO MAKSU TRAS FIBER JAR ===")
for i, c in enumerate(mano_maksu_5, 1):
    print(f"  [{i}] {c}")

print("\n=== NUEVA MANO DMITRI (OCULTA) ===")
for c in mano_dmitri_5:
    print(f"  * {c}")
