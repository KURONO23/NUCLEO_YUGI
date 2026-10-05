# -*- coding: utf-8 -*-
import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Baraja 2: Protocolo Yata-Lock V2.1 (40 Cartas)
deck_yata_lock = [
    # Monstruos (14)
    "Yata-Garasu", "Yata-Garasu",
    "Spirit Reaper", "Spirit Reaper",
    "Don Zaloog",
    "Sangan",
    "Witch of the Black Forest",
    "Jinzo",
    "Fiber Jar",
    "Cyber Jar",
    "Morphing Jar",
    "Magician of Faith",
    "Breaker the Magical Warrior",
    "Tribe-Infecting Virus",
    # Mágicas (17)
    "Reinforcement of the Army",
    "Book of Moon", "Book of Moon",
    "Delinquent Duo", "Delinquent Duo",
    "The Forceful Sentry", "The Forceful Sentry",
    "Confiscation",
    "Painful Choice",
    "Card Destruction",
    "Pot of Greed", "Pot of Greed",
    "Raigeki",
    "Dark Hole",
    "Harpie's Feather Duster",
    "Snatch Steal",
    "Change of Heart",
    # Trampas (9)
    "Trap Dustshoot",
    "Drop Off", "Drop Off",
    "Robbin' Goblin",
    "Ring of Destruction",
    "Imperial Order",
    "Torrential Tribute",
    "Mirror Force",
    "Solemn Judgment"
]

# Kageyama's Deck: Fiend Control / Aggro Beatdown (40 Cartas)
deck_kageyama = [
    "Ha Des the Dark Ruler", "Ha Des the Dark Ruler",
    "Lesser Fiend", "Lesser Fiend",
    "Archfiend Soldier", "Archfiend Soldier", "Archfiend Soldier",
    "Opticlops", "Opticlops", "Opticlops",
    "Slate Warrior", "Slate Warrior",
    "Sangan", "Witch of the Black Forest",
    "Cyber Jar",
    # Magias
    "Pot of Greed", "Graceful Charity", "Raigeki", "Dark Hole",
    "Heavy Storm", "Mystical Space Typhoon", "Mystical Space Typhoon",
    "Snatch Steal", "Change of Heart", "Monster Reborn", "Premature Burial",
    "Book of Moon", "Book of Moon", "Nobleman of Crossout", "Nobleman of Crossout",
    # Trampas
    "Mirror Force", "Torrential Tribute", "Call of the Haunted",
    "Ring of Destruction", "Imperial Order", "Bottomless Trap Hole", "Bottomless Trap Hole",
    "Waboku", "Waboku", "Drop Off"
]

rng = secrets.SystemRandom()

print(f"Yata-Lock total cartas: {len(deck_yata_lock)}")
print(f"Kageyama total cartas: {len(deck_kageyama)}")

rng.shuffle(deck_yata_lock)
rng.shuffle(deck_kageyama)

coin = rng.choice(["MAKSU", "KAGEYAMA"])
print(f"\nMoneda al aire: Gana {coin} y elige.")

mano_maksu = [deck_yata_lock.pop(0) for _ in range(5)]
mano_kageyama = [deck_kageyama.pop(0) for _ in range(5)]

print("\n--- MANO INICIAL MAKSU (TU MANO) ---")
for i, c in enumerate(mano_maksu, 1):
    print(f"  [{i}] {c}")

print("\n--- PROXIMO TOPDECK MAKSU ---")
print(f"  Turno 1/2 Draw: {deck_yata_lock[0]}")

print("\n--- MANO INICIAL KAGEYAMA (OCULTA) ---")
for c in mano_kageyama:
    print(f"  * {c}")
