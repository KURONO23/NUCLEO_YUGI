# -*- coding: utf-8 -*-
import sys

# Mazo de Klaus después del turno 1:
# Sacadas: Pot of Greed, Senju (campo), Mirror Force (campo), Senju, Breaker, Sangan, Black Illusion Ritual, Relinquished (mano)
# Quedan 32 cartas en el mazo de Klaus

# Veamos qué roba Klaus en T3 y cuál es su jugada óptima
deck_klaus_rem = [
    "Thunder Dragon", "Thunder Dragon", "Thunder Dragon",
    "Sonic Bird", "Sonic Bird",
    "Witch of the Black Forest",
    "Sinister Serpent", "Magician of Faith", "D.D. Warrior Lady",
    "Black Illusion Ritual", "Metamorphosis", "Metamorphosis",
    "Nobleman of Crossout", "Nobleman of Crossout",
    "Mystical Space Typhoon", "Mystical Space Typhoon",
    "Graceful Charity", "Raigeki", "Dark Hole", "Harpie's Feather Duster",
    "Snatch Steal", "Premature Burial", "Swords of Revealing Light", "Card Destruction",
    "Solemn Judgment", "Solemn Judgment", "Imperial Order", "Torrential Tribute",
    "Ring of Destruction", "Call of the Haunted", "Magic Jammer"
]

import secrets
rng = secrets.SystemRandom()
rng.shuffle(deck_klaus_rem)

draw_klaus_t3 = deck_klaus_rem[0]
print("Klaus roba en T3:", draw_klaus_t3)
