# -*- coding: utf-8 -*-
"""
Calculador exacto del duelo Maksu vs Paul
"""
import sys

# Mazo restante de Maksu tras el barajado
deck_maksu_orden = [
    "Injection Fairy Lily",
    "Dimension Fusion",
    "Robbin' Goblin",
    "Book of Moon",
    "Witch of the Black Forest",
    "Ring of Destruction",
    "Reinforcement of the Army",
    "Delinquent Duo",
    "Tribe-Infecting Virus",
    "Book of Moon",
    "Snatch Steal",
    "Painful Choice",
    "Magician of Faith",
    "Chaos Emperor Dragon - Envoy of the End",
    "Black Luster Soldier - Envoy of the Beginning"
]

print("Top 15 orden real de Maksu:")
for i, c in enumerate(deck_maksu_orden, 1):
    print(f"  {i}: {c}")
