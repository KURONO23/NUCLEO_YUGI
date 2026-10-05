# -*- coding: utf-8 -*-
import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

deck_maksu_chaos = [
    # Jefes del Caos (3)
    "Chaos Emperor Dragon - Envoy of the End",
    "Black Luster Soldier - Envoy of the Beginning",
    "Jinzo",
    # Monstruos (11)
    "Yata-Garasu",
    "Breaker the Magical Warrior",
    "Tribe-Infecting Virus",
    "Injection Fairy Lily",
    "Spirit Reaper",
    "Don Zaloog",
    "Sangan",
    "Witch of the Black Forest",
    "Magician of Faith",
    "Cyber Jar",
    "Fiber Jar",
    # Magias (18)
    "Painful Choice",
    "Graceful Charity",
    "Pot of Greed", "Pot of Greed",
    "Delinquent Duo",
    "The Forceful Sentry",
    "Harpie's Feather Duster",
    "Raigeki", "Dark Hole",
    "Dimension Fusion",
    "Snatch Steal", "Change of Heart",
    "Premature Burial",
    "Book of Moon", "Book of Moon",
    "Reinforcement of the Army",
    "United We Stand",
    "Nobleman of Crossout",
    # Trampas (8)
    "Ring of Destruction", "Ring of Destruction",
    "Mirror Force",
    "Torrential Tribute",
    "Imperial Order",
    "Solemn Judgment",
    "Magic Cylinder",
    "Robbin' Goblin"
]

deck_madame_xue = [
    # Monstruos (14)
    "Lava Golem", "Lava Golem",
    "Stealth Bird", "Stealth Bird", "Stealth Bird",
    "Des Koala", "Des Koala", "Des Koala",
    "Princess of Tsurugi", "Princess of Tsurugi",
    "Morphing Jar", "Cyber Jar",
    "Kuriboh", "Kuriboh",
    # Magias (12)
    "Wave-Motion Cannon", "Wave-Motion Cannon", "Wave-Motion Cannon",
    "Messenger of Peace", "Messenger of Peace",
    "Swords of Revealing Light", "Level Limit - Area B",
    "Pot of Greed", "Graceful Charity",
    "Dark Hole", "Scapegoat", "Scapegoat",
    # Trampas (14)
    "Secret Barrel", "Secret Barrel", "Secret Barrel",
    "Just Desserts", "Just Desserts",
    "Gravity Bind", "Gravity Bind",
    "Ojama Trio", "Ojama Trio",
    "Ceasefire", "Ring of Destruction", "Magic Cylinder",
    "Imperial Order", "Solemn Judgment"
]

rng = secrets.SystemRandom()

print(f"Maksu Chaos-Yata: {len(deck_maksu_chaos)} cartas")
print(f"Madame Xue: {len(deck_madame_xue)} cartas")

rng.shuffle(deck_maksu_chaos)
rng.shuffle(deck_madame_xue)

coin = rng.choice(["MAKSU", "MADAME XUE"])
print(f"\nMoneda al aire en Victoria Peak: Gana {coin} y elige.")

mano_maksu = [deck_maksu_chaos.pop(0) for _ in range(5)]
mano_xue = [deck_madame_xue.pop(0) for _ in range(5)]

print("\n=== MANO INICIAL MAKSU (TU MANO) ===")
for i, c in enumerate(mano_maksu, 1):
    print(f"  [{i}] {c}")

print("\n=== TOPDECK MAKSU (Próximos 3 robos) ===")
for i, c in enumerate(deck_maksu_chaos[:3], 1):
    print(f"  + Robo T{i*2}: {c}")

print("\n=== MANO INICIAL MADAME XUE (OCULTA) ===")
for c in mano_xue:
    print(f"  * {c}")

print("\n=== TOPDECK MADAME XUE (Próximos 3 robos) ===")
for i, c in enumerate(deck_madame_xue[:3], 1):
    print(f"  * T{i*2+1}: {c}")
