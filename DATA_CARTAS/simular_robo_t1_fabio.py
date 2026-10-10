import random

deck_restante = [
    "Suijin", "Kazejin", "Dark Magician", "Gaia the Fierce Knight",
    "Labyrinth Wall", "Mystical Elf", "White Magical Hat", "White Magical Hat",
    "Witch of the Black Forest", "Sangan", "Sangan", "Man-Eater Bug",
    "Penguin Soldier", "Penguin Soldier", "Hane-Hane", "Hane-Hane", "Mask of Darkness",
    "Kuriboh", "Kuriboh",
    "Tremendous Fire", "Fissure", "Fissure", "Dark Hole",
    "Heavy Storm", "Swords of Revealing Light", "Monster Reborn",
    "Stop Defense", "Stop Defense", "Red Medicine", "Red Medicine",
    "Magic Jammer", "Magic Jammer", "Just Desserts", "Just Desserts",
    "Two-Pronged Attack"
]

random.shuffle(deck_restante)
carta_robada = deck_restante.pop()
print("ROBO_TURNO_1:", carta_robada)
