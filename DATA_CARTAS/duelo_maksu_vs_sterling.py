# -*- coding: utf-8 -*-
import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

deck_maksu_yata = [
    # Monstruos (14)
    "Yata-Garasu", "Yata-Garasu",
    "Spirit Reaper", "Spirit Reaper",
    "Don Zaloog",
    "Sangan", "Witch of the Black Forest",
    "Jinzo",
    "Fiber Jar", "Cyber Jar", "Morphing Jar",
    "Magician of Faith",
    "Breaker the Magical Warrior",
    "Tribe-Infecting Virus",
    # Mágicas (18)
    "Messenger of Peace",
    "Reinforcement of the Army",
    "Book of Moon", "Book of Moon",
    "Delinquent Duo", "Delinquent Duo",
    "The Forceful Sentry", "The Forceful Sentry",
    "Confiscation",
    "Painful Choice",
    "Card Destruction",
    "Pot of Greed", "Pot of Greed",
    "Raigeki", "Dark Hole",
    "Harpie's Feather Duster",
    "Snatch Steal", "Change of Heart",
    # Trampas (8)
    "Trap Dustshoot",
    "Drop Off",
    "Robbin' Goblin",
    "Ring of Destruction",
    "Imperial Order",
    "Torrential Tribute",
    "Mirror Force",
    "Solemn Judgment"
]

deck_sterling = [
    # Monstruos (15)
    "Buster Blader", "Buster Blader",
    "Chaos Command Magician", "Chaos Command Magician",
    "Archfiend Soldier", "Archfiend Soldier", "Archfiend Soldier",
    "Slate Warrior", "Slate Warrior",
    "Reflect Bounder", "Reflect Bounder",
    "Breaker the Magical Warrior",
    "Sangan", "Witch of the Black Forest",
    "D.D. Warrior Lady",
    # Magias (11)
    "Pot of Greed", "Graceful Charity", "Raigeki", "Dark Hole", "Heavy Storm",
    "Mystical Space Typhoon", "Mystical Space Typhoon",
    "Nobleman of Crossout", "Nobleman of Crossout",
    "Premature Burial", "Snatch Steal",
    # Trampas (14)
    "Solemn Judgment", "Solemn Judgment", "Solemn Judgment",
    "Magic Jammer", "Magic Jammer",
    "Seven Tools of the Bandit", "Seven Tools of the Bandit",
    "Royal Oppression", "Royal Oppression",
    "Mirror Force", "Ring of Destruction", "Torrential Tribute",
    "Imperial Order", "Call of the Haunted"
]

rng = secrets.SystemRandom()

print(f"Maksu Yata total: {len(deck_maksu_yata)}")
print(f"Sterling total: {len(deck_sterling)}")

rng.shuffle(deck_maksu_yata)
rng.shuffle(deck_sterling)

coin = rng.choice(["MAKSU", "STERLING"])
print(f"\nMoneda al aire: Gana {coin} y elige.")

mano_maksu = [deck_maksu_yata.pop(0) for _ in range(5)]
mano_sterling = [deck_sterling.pop(0) for _ in range(5)]

print("\n--- MANO INICIAL MAKSU (TU MANO) ---")
for i, c in enumerate(mano_maksu, 1):
    print(f"  [{i}] {c}")

print("\n--- PROXIMO ROBO (Topdeck) ---")
print(f"  Turno 2 Draw: {deck_maksu_yata[0]}")

print("\n--- MANO INICIAL STERLING (OCULTA) ---")
for c in mano_sterling:
    print(f"  * {c}")
