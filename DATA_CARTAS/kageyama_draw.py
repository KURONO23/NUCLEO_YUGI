# -*- coding: utf-8 -*-
import sys

# Revisar la semilla de Kageyama ejecutando la misma lógica
import secrets
rng = secrets.SystemRandom()

# Generar secuencia de Kageyama
deck_kageyama = [
    "Ha Des the Dark Ruler", "Ha Des the Dark Ruler",
    "Lesser Fiend", "Lesser Fiend",
    "Archfiend Soldier", "Archfiend Soldier", "Archfiend Soldier",
    "Opticlops", "Opticlops", "Opticlops",
    "Slate Warrior", "Slate Warrior",
    "Sangan", "Witch of the Black Forest",
    "Cyber Jar",
    "Pot of Greed", "Graceful Charity", "Raigeki", "Dark Hole",
    "Heavy Storm", "Mystical Space Typhoon",
    "Snatch Steal", "Change of Heart", "Monster Reborn", "Premature Burial",
    "Book of Moon", "Book of Moon", "Nobleman of Crossout", "Nobleman of Crossout",
    "Mirror Force", "Torrential Tribute", "Call of the Haunted",
    "Ring of Destruction", "Imperial Order", "Bottomless Trap Hole", "Bottomless Trap Hole",
    "Waboku", "Drop Off"
]
rng.shuffle(deck_kageyama)
top_5 = [deck_kageyama.pop(0) for _ in range(5)]
print("Kageyama robos siguientes:")
for i in range(5):
    print(f"  Turno {i+1}: {deck_kageyama.pop(0)}")
