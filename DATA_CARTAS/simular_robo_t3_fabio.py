import random

deck_restante = [
    "Suijin", "Kazejin", "Dark Magician", "Gaia the Fierce Knight",
    "Labyrinth Wall", "White Magical Hat", "White Magical Hat",
    "Witch of the Black Forest", "Sangan", "Man-Eater Bug",
    "Penguin Soldier", "Penguin Soldier", "Hane-Hane", "Hane-Hane", "Mask of Darkness",
    "Kuriboh", "Kuriboh",
    "Tremendous Fire", "Fissure", "Fissure", "Dark Hole",
    "Heavy Storm", "Swords of Revealing Light", "Monster Reborn",
    "Stop Defense", "Stop Defense", "Red Medicine", "Red Medicine",
    "Magic Jammer", "Magic Jammer", "Just Desserts", "Just Desserts",
    "Two-Pronged Attack"
]

random.shuffle(deck_restante)
robo_turno_3 = deck_restante.pop()
print("ROBO_TURNO_3:", robo_turno_3)
