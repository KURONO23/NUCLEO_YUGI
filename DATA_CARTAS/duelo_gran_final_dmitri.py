# -*- coding: utf-8 -*-
import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

deck_maksu_reflejo = [
    # Monstruos (14)
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
    # Magias (17)
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
    # Trampas (9)
    "Magic Cylinder", "Magic Cylinder",
    "Waboku", "Waboku",
    "Mirror Force",
    "Torrential Tribute",
    "Imperial Order",
    "Ring of Destruction",
    "Solemn Judgment"
]

deck_dmitri = [
    # Monstruos (16)
    "Mechanicalchaser", "Mechanicalchaser", "Mechanicalchaser",
    "Cyber-Tech Alligator", "Cyber-Tech Alligator",
    "Jinzo",
    "Reflect Bounder", "Reflect Bounder", "Reflect Bounder",
    "Heavy Mech Support Platform", "Heavy Mech Support Platform",
    "Sangan", "Witch of the Black Forest",
    "Breaker the Magical Warrior",
    "Cannon Soldier", "Cannon Soldier",
    # Magias (16)
    "Limiter Removal", "Limiter Removal", "Limiter Removal",
    "Premature Burial", "Snatch Steal",
    "Pot of Greed", "Graceful Charity",
    "Raigeki", "Dark Hole", "Heavy Storm", "Harpie's Feather Duster",
    "Mystical Space Typhoon", "Mystical Space Typhoon",
    "United We Stand", "Mage Power", "Nobleman of Crossout",
    # Trampas (8)
    "Mirror Force", "Torrential Tribute", "Ring of Destruction", "Imperial Order",
    "Solemn Judgment", "Solemn Judgment",
    "Call of the Haunted", "Magic Jammer"
]

rng = secrets.SystemRandom()

print(f"Maksu Reflejo Mortal: {len(deck_maksu_reflejo)} cartas")
print(f"Dmitri Vor Machine: {len(deck_dmitri)} cartas")

rng.shuffle(deck_maksu_reflejo)
rng.shuffle(deck_dmitri)

coin = rng.choice(["MAKSU", "DMITRI"])
print(f"\nMoneda al aire de la Gran Final: Gana {coin} y elige.")

mano_maksu = [deck_maksu_reflejo.pop(0) for _ in range(5)]
mano_dmitri = [deck_dmitri.pop(0) for _ in range(5)]

print("\n=== MANO INICIAL MAKSU (TU MANO) ===")
for i, c in enumerate(mano_maksu, 1):
    print(f"  [{i}] {c}")

print("\n=== TOPDECK MAKSU (Próximos 3 robos) ===")
for i, c in enumerate(deck_maksu_reflejo[:3], 1):
    print(f"  + Robo T{i*2}: {c}")

print("\n=== MANO INICIAL DMITRI (OCULTA) ===")
for c in mano_dmitri:
    print(f"  * {c}")

print("\n=== TOPDECK DMITRI (Próximos 3 robos) ===")
for i, c in enumerate(deck_dmitri[:3], 1):
    print(f"  * T{i*2+1}: {c}")
