# -*- coding: utf-8 -*-
import sys
import secrets

deck_maksu_rem = [
    "Yata-Garasu", # segunda copia
    "Spirit Reaper", # segunda copia
    "Don Zaloog", "Sangan", "Witch of the Black Forest", "Jinzo",
    "Fiber Jar", "Cyber Jar", "Morphing Jar",
    "Breaker the Magical Warrior", "Tribe-Infecting Virus",
    "Reinforcement of the Army", "Book of Moon", "Book of Moon",
    "Delinquent Duo", # segunda copia
    "The Forceful Sentry", # segunda copia
    "Confiscation",
    "Painful Choice", "Card Destruction", "Pot of Greed", "Pot of Greed",
    "Raigeki", "Dark Hole", "Harpie's Feather Duster", "Change of Heart",
    "Trap Dustshoot", "Drop Off", "Ring of Destruction", "Imperial Order",
    "Solemn Judgment"
]

rng = secrets.SystemRandom()
rng.shuffle(deck_maksu_rem)

draw_maksu_t12 = deck_maksu_rem[0]
print("Maksu roba en T12:", draw_maksu_t12)
