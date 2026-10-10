import random

# Simular robo de mano inicial de 5 cartas para Fabio y Joey
deck_fabio = [
    "Suijin", "Kazejin", "Dark Magician", "Gaia the Fierce Knight", "Curse of Dragon",
    "Labyrinth Wall", "Mystical Elf", "White Magical Hat", "White Magical Hat",
    "Witch of the Black Forest", "Sangan", "Sangan", "Man-Eater Bug",
    "Penguin Soldier", "Penguin Soldier", "Hane-Hane", "Hane-Hane", "Mask of Darkness",
    "Kuriboh", "Kuriboh", "Armored Lizard",
    "Tremendous Fire", "Tremendous Fire", "Fissure", "Fissure", "Dark Hole",
    "Heavy Storm", "Swords of Revealing Light", "Monster Reborn", "Share the Pain",
    "Stop Defense", "Stop Defense", "Red Medicine", "Red Medicine",
    "Trap Hole", "Magic Jammer", "Magic Jammer", "Just Desserts", "Just Desserts",
    "Two-Pronged Attack"
]

deck_joey_novato = [
    "Swordsman of Landstar (500 ATK)", "Baby Dragon (1200 ATK)", "Alligator's Sword (1500 ATK)",
    "Tiger Axe (1300 ATK)", "Axe Raider (1700 ATK)", "Kojikocy (1500 ATK)",
    "Armored Lizard (1500 ATK)", "Rock Ogre Grotto #1 (1400 DEF)", "Masaki the Legendary Swordsman",
    "Hinotama", "Sparks", "Kunai with Chain", "Trap Hole", "Shield & Sword"
]

random.shuffle(deck_fabio)
mano_fabio = [deck_fabio.pop() for _ in range(5)]

print("MANO_FABIO:", mano_fabio)
