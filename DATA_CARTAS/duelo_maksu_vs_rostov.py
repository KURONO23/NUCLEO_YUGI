# -*- coding: utf-8 -*-
import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

deck_maksu_silencio = [
    # Monstruos (15)
    "Jinzo", "Jinzo",
    "Airknight Parshath",
    "Injection Fairy Lily",
    "Goblin Attack Force",
    "Zombyra the Dark",
    "Spear Dragon",
    "Kycoo the Ghost Destroyer",
    "Don Zaloog",
    "Exiled Force",
    "Spirit Reaper",
    "Breaker the Magical Warrior",
    "Witch of the Black Forest",
    "Sangan",
    "Cyber Jar",
    # Mágicas (16)
    "Pot of Greed",
    "Graceful Charity",
    "Raigeki",
    "Dark Hole",
    "Harpie's Feather Duster",
    "Monster Reborn",
    "Premature Burial",
    "Change of Heart",
    "Snatch Steal",
    "Reinforcement of the Army",
    "Book of Moon", "Book of Moon",
    "Painful Choice",
    "Delinquent Duo",
    "The Forceful Sentry",
    "Mystical Space Typhoon",
    # Trampas (9)
    "Ring of Destruction", "Ring of Destruction",
    "Imperial Order",
    "Mirror Force",
    "Torrential Tribute",
    "Call of the Haunted",
    "Bottomless Trap Hole",
    "Solemn Judgment",
    "Waboku"
]

deck_rostov = [
    # Monstruos Roca y Tierra
    "Guardian Sphinx", "Guardian Sphinx",
    "Gigantes", "Gigantes", "Gigantes",
    "Golem Sentry", "Golem Sentry", "Golem Sentry",
    "Medusa Worm", "Medusa Worm",
    "Morphing Jar", "Cyber Jar",
    "Giant Rat", "Giant Rat", "Giant Rat",
    "Slate Warrior", "Slate Warrior",
    "Sangan",
    # Mágicas
    "Pot of Greed", "Graceful Charity", "Raigeki", "Dark Hole",
    "Heavy Storm", "Mystical Space Typhoon", "Mystical Space Typhoon",
    "Swords of Concealing Light", "Swords of Concealing Light",
    "Book of Moon", "Book of Moon", "Monster Reborn", "Premature Burial",
    "Snatch Steal",
    # Trampas
    "Mirror Force", "Torrential Tribute", "Ring of Destruction",
    "Waboku", "Waboku", "Compulsory Evacuation Device", "Compulsory Evacuation Device",
    "Bottomless Trap Hole"
]

rng = secrets.SystemRandom()

print(f"Maksu Silencio total: {len(deck_maksu_silencio)}")
print(f"Rostov total: {len(deck_rostov)}")

rng.shuffle(deck_maksu_silencio)
rng.shuffle(deck_rostov)

coin = rng.choice(["MAKSU", "ROSTOV"])
print(f"\nMoneda al aire: Gana {coin} y elige.")

mano_maksu = [deck_maksu_silencio.pop(0) for _ in range(5)]
mano_rostov = [deck_rostov.pop(0) for _ in range(5)]

print("\n--- MANO INICIAL MAKSU (TU MANO) ---")
for i, c in enumerate(mano_maksu, 1):
    print(f"  [{i}] {c}")

print("\n--- PROXIMO ROBO (Topdeck) ---")
print(f"  Turno 2 Draw: {deck_maksu_silencio[0]}")

print("\n--- MANO INICIAL ROSTOV (OCULTA) ---")
for c in mano_rostov:
    print(f"  * {c}")
