import random

# Baraja inicial canónica de Joey Wheeler (pre-Reino de los Duelistas / episodio 3)
deck_joey_canon_pre_reino = [
    "Swordsman of Landstar (Guerrero | Nivel 3 | 500 ATK / 1200 DEF)",
    "Baby Dragon (Dragón | Nivel 3 | 1200 ATK / 700 DEF)",
    "Kojikocy (Guerrero | Nivel 4 | 1500 ATK / 1200 DEF)",
    "Tiger Axe (Guerrero-Bestia | Nivel 4 | 1300 ATK / 1100 DEF)",
    "Axe Raider (Guerrero | Nivel 4 | 1700 ATK / 1150 DEF)",
    "Armored Lizard (Reptil | Nivel 4 | 1500 ATK / 1200 DEF)",
    "Masaki the Legendary Swordsman (Guerrero | Nivel 4 | 1100 ATK / 1100 DEF)",
    "Rock Ogre Grotto #1 (Roca | Nivel 3 | 800 ATK / 1200 DEF)",
    "Mountain Warrior (Guerrero-Bestia | Nivel 3 | 600 ATK / 1000 DEF)",
    "Leogun (Bestia | Nivel 5 | 1750 ATK / 1550 DEF)"
]

random.shuffle(deck_joey_canon_pre_reino)

# Joey roba 5 cartas iniciales + 1 carta de turno 2
mano_joey = [deck_joey_canon_pre_reino.pop() for _ in range(6)]
print("MANO_JOEY:", mano_joey)
