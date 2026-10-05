# -*- coding: utf-8 -*-
import sys
import secrets

deck_maksu_rem = [
    "Jinzo",
    "Injection Fairy Lily",
    "Tribe-Infecting Virus",
    "Spirit Reaper", "Spirit Reaper",
    "Goblin Attack Force",
    "Zombyra the Dark",
    "Spear Dragon",
    "Don Zaloog",
    "Sangan", "Witch of the Black Forest",
    "Cyber Jar", "Fiber Jar",
    "Graceful Charity",
    "Pot of Greed", # segunda copia
    "Raigeki", "Dark Hole",
    "Harpie's Feather Duster",
    "Delinquent Duo",
    "The Forceful Sentry",
    "Painful Choice",
    "Book of Moon", "Book of Moon",
    "Change of Heart",
    "United We Stand",
    "Nobleman of Crossout",
    "Premature Burial",
    "Magic Cylinder", "Magic Cylinder",
    "Waboku", "Waboku",
    "Mirror Force",
    "Imperial Order",
    "Ring of Destruction",
    "Solemn Judgment"
]

rng = secrets.SystemRandom()
rng.shuffle(deck_maksu_rem)

draw1 = deck_maksu_rem.pop(0)
draw2 = deck_maksu_rem.pop(0)

print("Pot of Greed roba:")
print("  Carta 1:", draw1)
print("  Carta 2:", draw2)
