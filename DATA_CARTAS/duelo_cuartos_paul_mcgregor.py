# -*- coding: utf-8 -*-
"""
SIMULADOR Y EJECUTOR OFICIAL DE DUELO - CUARTOS DE FINAL KC GRAND CHAMPIONSHIP
Maksu (KURONO) vs Paul McGregor (Detective)
Auditoría estricta de Reglas, Life Points y True RNG Shuffler
"""

import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# 1. DECK DE MAKSU: Protocolo Apocalipsis V8.0 (40 Cartas)
deck_maksu = [
    "Chaos Emperor Dragon - Envoy of the End",
    "Black Luster Soldier - Envoy of the Beginning",
    "Jinzo",
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
    "Painful Choice",
    "Graceful Charity",
    "Pot of Greed",
    "Pot of Greed",
    "Delinquent Duo",
    "The Forceful Sentry",
    "Harpie's Feather Duster",
    "Raigeki",
    "Dark Hole",
    "Dimension Fusion",
    "Snatch Steal",
    "Change of Heart",
    "Premature Burial",
    "Book of Moon",
    "Book of Moon",
    "Reinforcement of the Army",
    "United We Stand",
    "Nobleman of Crossout",
    "Ring of Destruction",
    "Ring of Destruction",
    "Mirror Force",
    "Torrential Tribute",
    "Imperial Order",
    "Solemn Judgment",
    "Magic Cylinder",
    "Robbin' Goblin"
]

# 2. DECK DE PAUL McGREGOR: Detective Dragon Beatdown (40 Cartas)
deck_paul = [
    "Mirage Dragon", "Mirage Dragon", "Mirage Dragon",
    "Cave Dragon", "Cave Dragon", "Cave Dragon",
    "Luster Dragon", "Luster Dragon", "Luster Dragon",
    "Spear Dragon", "Spear Dragon",
    "Armed Dragon LV3", "Armed Dragon LV3",
    "Armed Dragon LV5",
    "The Stern Mystic", "The Stern Mystic",
    "Lord of D.",
    "Masked Dragon", "Masked Dragon",
    "Stamping Destruction", "Stamping Destruction",
    "Dragon's Gunfire", "Dragon's Gunfire",
    "Different Dimension Capsule", "Different Dimension Capsule",
    "Prohibition", "Prohibition",
    "Question",
    "Pot of Greed",
    "Heavy Storm",
    "Snatch Steal",
    "Mystical Space Typhoon",
    "The Flute of Summoning Dragon",
    "Dragon's Rage", "Dragon's Rage",
    "Trap Hole", "Trap Hole",
    "Bottomless Trap Hole",
    "Ring of Destruction",
    "Call of the Haunted"
]

rng = secrets.SystemRandom()

# Barajado criptografico Fisher-Yates
shuffled_maksu = list(deck_maksu)
rng.shuffle(shuffled_maksu)

shuffled_paul = list(deck_paul)
rng.shuffle(shuffled_paul)

print("=== [AGENTE-9: BARAJADOR RNG] BARAJADO COMPLETADO CON EXITO ===")
print(f"Mazo Maksu: {len(shuffled_maksu)} cartas barajadas.")
print(f"Mazo Paul: {len(shuffled_paul)} cartas barajadas.\n")

# Extraer manos iniciales (5 cartas c/u)
mano_maksu = [shuffled_maksu.pop(0) for _ in range(5)]
mano_paul = [shuffled_paul.pop(0) for _ in range(5)]

print("--- MANO INICIAL MAKSU (5) ---")
for i, c in enumerate(mano_maksu, 1):
    print(f"  [{i}] {c}")

print("\n--- MANO INICIAL PAUL McGREGOR (5) ---")
for i, c in enumerate(mano_paul, 1):
    print(f"  [{i}] {c}")

print("\n--- SIGUIENTES 5 DEL TOPE DE MAKSU ---")
for i in range(5):
    print(f"  Turno +{i+1}: {shuffled_maksu[i]}")

print("\n--- SIGUIENTES 5 DEL TOPE DE PAUL ---")
for i in range(5):
    print(f"  Turno +{i+1}: {shuffled_paul[i]}")
