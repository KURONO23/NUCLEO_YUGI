# -*- coding: utf-8 -*-
import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

deck_maksu_v71 = [
    # Jefes (3)
    "Jinzo",
    "Jinzo",
    "Airknight Parshath",
    # Fuerza Terrestre (8)
    "Injection Fairy Lily",
    "Goblin Attack Force",
    "Zombyra the Dark",
    "Spear Dragon",
    "Kycoo the Ghost Destroyer",
    "Don Zaloog",
    "Exiled Force",
    "Spirit Reaper",
    # Buscadores (2)
    "Witch of the Black Forest",
    "Sangan",
    # Volteos (2)
    "Fiber Jar",
    "Cyber Jar",
    # Magias (17)
    "Reinforcement of the Army",
    "Book of Moon",
    "Book of Moon",
    "United We Stand",
    "Mage Power",
    "Painful Choice",
    "Giant Trunade",
    "Delinquent Duo",
    "Delinquent Duo",
    "The Forceful Sentry",
    "The Forceful Sentry",
    "Snatch Steal",
    "Nobleman of Crossout",
    "Pot of Greed",
    "Pot of Greed",
    "Raigeki",
    "Harpie's Feather Duster",
    # Trampas (8)
    "Ring of Destruction",
    "Ring of Destruction",
    "Magic Cylinder",
    "Magic Cylinder",
    "Torrential Tribute",
    "Imperial Order",
    "Mirror Force",
    "Solemn Judgment"
]

deck_madame_xue = [
    # Monstruos (14)
    "Lava Golem",
    "Lava Golem",
    "Stealth Bird",
    "Stealth Bird",
    "Stealth Bird",
    "Des Koala",
    "Des Koala",
    "Des Koala",
    "Princess of Tsurugi",
    "Princess of Tsurugi",
    "Morphing Jar",
    "Cyber Jar",
    "Kuriboh",
    "Kuriboh",
    # Magias (12)
    "Wave-Motion Cannon",
    "Wave-Motion Cannon",
    "Wave-Motion Cannon",
    "Messenger of Peace",
    "Messenger of Peace",
    "Swords of Revealing Light",
    "Level Limit - Area B",
    "Pot of Greed",
    "Graceful Charity",
    "Dark Hole",
    "Scapegoat",
    "Scapegoat",
    # Trampas (14)
    "Secret Barrel",
    "Secret Barrel",
    "Secret Barrel",
    "Just Desserts",
    "Just Desserts",
    "Gravity Bind",
    "Gravity Bind",
    "Ojama Trio",
    "Ojama Trio",
    "Ceasefire",
    "Ring of Destruction",
    "Magic Cylinder",
    "Imperial Order",
    "Solemn Judgment"
]

rng = secrets.SystemRandom()

print(f"Maksu V7.1 Total Cartas: {len(deck_maksu_v71)}")
print(f"Madame Xue Total Cartas: {len(deck_madame_xue)}")

rng.shuffle(deck_maksu_v71)
rng.shuffle(deck_madame_xue)

coin = rng.choice(["MAKSU", "MADAME XUE"])
print(f"\nMoneda al aire: Gana {coin} y elige ir primero.")

# Manos iniciales (5 cartas c/u)
mano_maksu = [deck_maksu_v71.pop(0) for _ in range(5)]
mano_xue = [deck_madame_xue.pop(0) for _ in range(5)]

print("\n=== MANO INICIAL MAKSU (TU MANO) ===")
for i, c in enumerate(mano_maksu, 1):
    print(f"  [{i}] {c}")

print("\n=== TOPDECK MAKSU (Próximos 3 robos) ===")
for i, c in enumerate(deck_maksu_v71[:3], 1):
    print(f"  + Robo T{i*2}: {c}")

print("\n=== MANO INICIAL MADAME XUE (OCULTA) ===")
for c in mano_xue:
    print(f"  * {c}")

print("\n=== TOPDECK MADAME XUE (Próximos 3 robos) ===")
for i, c in enumerate(deck_madame_xue[:3], 1):
    print(f"  * T{i*2+1}: {c}")
