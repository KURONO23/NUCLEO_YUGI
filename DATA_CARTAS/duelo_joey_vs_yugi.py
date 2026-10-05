# -*- coding: utf-8 -*-
import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

deck_joey = [
    # Monstruos (20)
    "Jinzo",
    "Gearfried the Swordmaster",
    "Goblin Attack Force", "Goblin Attack Force",
    "Zombyra the Dark",
    "Panther Warrior",
    "Gearfried the Iron Knight", "Gearfried the Iron Knight",
    "Rocket Warrior",
    "Hayabusa Knight",
    "Marauding Captain", "Marauding Captain",
    "Exiled Force",
    "Sangan",
    "Little-Winguard",
    "Cyber-Tech Alligator",
    "Don Zaloog",
    "Axe Raider",
    "Alligator's Sword",
    # Mágicas (12)
    "Pot of Greed",
    "Raigeki",
    "Mystical Space Typhoon",
    "Change of Heart",
    "Monster Reborn",
    "Reinforcement of the Army", "Reinforcement of the Army",
    "Book of Moon", "Book of Moon",
    "Release Restraint",
    "Scapegoat",
    "Giant Trunade",
    "Question",
    # Trampas (8)
    "Mirror Force",
    "Torrential Tribute",
    "Bottomless Trap Hole",
    "Trap Hole",
    "Call of the Haunted",
    "Kunai with Chain",
    "Roulette Spider",
    "Magic Arm Shield",
    "Waboku"
]

deck_yugi = [
    # Monstruos (18)
    "Dark Magician", "Dark Magician",
    "Buster Blader",
    "Dark Magician Girl",
    "Skilled Dark Magician", "Skilled Dark Magician", "Skilled Dark Magician",
    "Breaker the Magical Warrior",
    "Tribe-Infecting Virus",
    "Apprentice Magician", "Apprentice Magician",
    "Old Vindictive Magician", "Old Vindictive Magician",
    "Magician of Faith", "Magician of Faith",
    "Witch of the Black Forest",
    "Sangan",
    "Kuriboh",
    # Mágicas (16)
    "Diffusion Wave-Motion", "Diffusion Wave-Motion",
    "Dark Magic Attack",
    "Thousand Knives",
    "Polymerization",
    "Pot of Greed",
    "Graceful Charity",
    "Raigeki",
    "Dark Hole",
    "Monster Reborn",
    "Premature Burial",
    "Change of Heart",
    "Mystical Space Typhoon",
    "Swords of Revealing Light",
    "Book of Moon",
    "Heavy Storm",
    # Trampas (6)
    "Mirror Force",
    "Torrential Tribute",
    "Call of the Haunted",
    "Magic Cylinder",
    "Waboku", "Waboku"
]

rng = secrets.SystemRandom()

# Ajustar tamaño a 40 exactas si falta/sobra alguna
print(f"Joey total cartas: {len(deck_joey)}")
print(f"Yugi total cartas: {len(deck_yugi)}")

# Barajar
rng.shuffle(deck_joey)
rng.shuffle(deck_yugi)

coin = rng.choice(["JONOUCHI", "YUGI"])
print(f"Moneda al aire: Gana {coin} y elige iniciar.")

# Manos iniciales (5 cartas)
mano_joey = [deck_joey.pop(0) for _ in range(5)]
mano_yugi = [deck_yugi.pop(0) for _ in range(5)]

print("\n--- MANO INICIAL JOEY ---")
for c in mano_joey:
    print(f"  * {c}")

print("\n--- MANO INICIAL YUGI ---")
for c in mano_yugi:
    print(f"  * {c}")

# Topdecks turnos 1 a 6
print("\n--- PROXIMOS TOPDECKS JOEY ---")
for i in range(5):
    print(f"  Turno {i+1}: {deck_joey.pop(0)}")

print("\n--- PROXIMOS TOPDECKS YUGI ---")
for i in range(5):
    print(f"  Turno {i+1}: {deck_yugi.pop(0)}")
