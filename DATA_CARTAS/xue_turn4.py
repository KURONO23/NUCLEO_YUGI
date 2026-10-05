# -*- coding: utf-8 -*-
import sys
import secrets

deck_xue_rem = [
    "Lava Golem", "Lava Golem",
    "Stealth Bird", "Stealth Bird",
    "Des Koala", "Des Koala",
    "Morphing Jar", "Cyber Jar",
    "Swords of Revealing Light", "Level Limit - Area B",
    "Pot of Greed", "Graceful Charity", "Dark Hole", "Scapegoat", "Scapegoat",
    "Gravity Bind",
    "Ojama Trio", "Ojama Trio", "Ceasefire", "Ring of Destruction",
    "Magic Cylinder", "Imperial Order", "Solemn Judgment"
]

rng = secrets.SystemRandom()
rng.shuffle(deck_xue_rem)

draw_turn4 = deck_xue_rem[0]
print("Madame Xue roba:", draw_turn4)
