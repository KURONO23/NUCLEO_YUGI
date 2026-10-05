# -*- coding: utf-8 -*-
import sys
import secrets

# Mazo de Klaus:
# Cartas sacadas: Pot of Greed, Senju (campo), Mirror Force (campo), Senju (mano), Breaker (mano), Sangan (cementerio), Black Illusion Ritual (cementerio), Relinquished (campo), Swords of Revealing Light (campo).
# Restan 31 cartas en el mazo de Klaus

deck_klaus_rem = [
    "Thunder Dragon", "Thunder Dragon", "Thunder Dragon",
    "Sonic Bird", "Sonic Bird",
    "Witch of the Black Forest",
    "Sinister Serpent", "Magician of Faith", "D.D. Warrior Lady",
    "Black Illusion Ritual", "Metamorphosis", "Metamorphosis",
    "Nobleman of Crossout", "Nobleman of Crossout",
    "Mystical Space Typhoon", "Mystical Space Typhoon",
    "Graceful Charity", "Raigeki", "Dark Hole", "Harpie's Feather Duster",
    "Snatch Steal", "Premature Burial", "Card Destruction",
    "Solemn Judgment", "Solemn Judgment", "Imperial Order", "Torrential Tribute",
    "Ring of Destruction", "Call of the Haunted", "Magic Jammer", "Senju of the Thousand Hands"
]

rng = secrets.SystemRandom()
rng.shuffle(deck_klaus_rem)

draw_klaus_t5 = deck_klaus_rem[0]
print("Klaus roba en T5:", draw_klaus_t5)
