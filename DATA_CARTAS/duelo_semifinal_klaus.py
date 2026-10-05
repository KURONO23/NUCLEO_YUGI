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
    # Mágicas (17)
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
    # Trampas (9)
    "Trap Dustshoot",
    "Drop Off",
    "Messenger of Peace",
    "Robbin' Goblin",
    "Ring of Destruction",
    "Imperial Order",
    "Torrential Tribute",
    "Mirror Force",
    "Solemn Judgment"
]

deck_klaus = [
    # Monstruos (15)
    "Relinquished", "Relinquished",
    "Senju of the Thousand Hands", "Senju of the Thousand Hands",
    "Sonic Bird", "Sonic Bird",
    "Thunder Dragon", "Thunder Dragon", "Thunder Dragon",
    "Sangan", "Witch of the Black Forest",
    "Breaker the Magical Warrior",
    "Sinister Serpent",
    "Magician of Faith",
    "D.D. Warrior Lady",
    # Magias (17)
    "Black Illusion Ritual", "Black Illusion Ritual",
    "Metamorphosis", "Metamorphosis",
    "Nobleman of Crossout", "Nobleman of Crossout",
    "Mystical Space Typhoon", "Mystical Space Typhoon",
    "Pot of Greed", "Graceful Charity",
    "Raigeki", "Dark Hole",
    "Harpie's Feather Duster",
    "Snatch Steal", "Premature Burial",
    "Swords of Revealing Light",
    "Card Destruction",
    # Trampas (8)
    "Solemn Judgment", "Solemn Judgment",
    "Imperial Order",
    "Mirror Force", "Torrential Tribute",
    "Ring of Destruction", "Call of the Haunted",
    "Magic Jammer"
]

rng = secrets.SystemRandom()

print(f"Maksu Yata Total: {len(deck_maksu_yata)}")
print(f"Klaus Total: {len(deck_klaus)}")

rng.shuffle(deck_maksu_yata)
rng.shuffle(deck_klaus)

coin = rng.choice(["MAKSU", "KLAUS"])
print(f"\nMoneda al aire: Gana {coin} y elige la iniciativa.")

# Mano inicial (5 cartas)
mano_maksu = [deck_maksu_yata.pop(0) for _ in range(5)]
mano_klaus = [deck_klaus.pop(0) for _ in range(5)]

print("\n=== MANO INICIAL MAKSU (TU MANO) ===")
for i, c in enumerate(mano_maksu, 1):
    print(f"  [{i}] {c}")

print("\n=== TOPDECK MAKSU (Próximos 3 robos) ===")
for i, c in enumerate(deck_maksu_yata[:3], 1):
    print(f"  + Robo T{i*2}: {c}")

print("\n=== MANO INICIAL KLAUS (OCULTA) ===")
for c in mano_klaus:
    print(f"  * {c}")

print("\n=== TOPDECK KLAUS (Próximos 3 robos) ===")
for i, c in enumerate(deck_klaus[:3], 1):
    print(f"  * T{i*2+1}: {c}")
