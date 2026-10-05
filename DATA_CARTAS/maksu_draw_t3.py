# -*- coding: utf-8 -*-
import sys

# Mazo de Maksu:
# Sacadas: United We Stand, Solemn Judgment, Painful Choice (GY), Fiber Jar (campo), Ring of Destruction (GY).
# Por Painful Choice: Harpie's Feather Duster (mano), Jinzo (GY), Tribe (GY), Premature (GY), Graceful (GY).
# Turno 1 Draw o Turno 3 Draw:
# Veamos la lista de cartas restantes de Maksu:
deck_maksu_rem = [
    "Breaker the Magical Warrior",
    "Pot of Greed", "Pot of Greed",
    "Change of Heart", "Dark Hole", "Raigeki",
    "Delinquent Duo", "The Forceful Sentry",
    "Book of Moon", "Book of Moon",
    "Snatch Steal", "Reinforcement of the Army", "Nobleman of Crossout",
    "Magic Cylinder", "Magic Cylinder", "Waboku", "Waboku", "Mirror Force", "Torrential Tribute", "Imperial Order",
    "Spirit Reaper", "Spirit Reaper", "Goblin Attack Force", "Zombyra the Dark", "Spear Dragon", "Don Zaloog",
    "Sangan", "Witch of the Black Forest", "Cyber Jar", "Injection Fairy Lily"
]

import secrets
rng = secrets.SystemRandom()
rng.shuffle(deck_maksu_rem)

draw_t3 = deck_maksu_rem[0]
print("Maksu roba en Turno 3:", draw_t3)
