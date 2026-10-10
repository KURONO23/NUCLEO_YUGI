import random

# Baraja restante de Joey
deck_joey = [
    "Tiger Axe (1300 ATK)", "Leogun (1750 ATK)", "Swordsman of Landstar (500 ATK)",
    "Kojikocy (1500 ATK)", "Rock Ogre Grotto #1 (800 ATK / 1200 DEF)",
    "Baby Dragon (1200 ATK)", "Masaki the Legendary Swordsman (1100 ATK)"
]

random.shuffle(deck_joey)
robo_joey_t4 = deck_joey.pop()
print("ROBO_JOEY_T4:", robo_joey_t4)
