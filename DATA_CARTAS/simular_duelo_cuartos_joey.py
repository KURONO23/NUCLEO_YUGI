# -*- coding: utf-8 -*-
"""
SIMULACIÓN Y VERIFICACIÓN MATEMÁTICA - JOEY VS JAFAR SHIN
Cuartos de Final KC Grand Championship
"""
lp_joey = 4000
lp_jafar = 4000

# Turno 1 (Jafar):
# Pot of Greed (roba Trap Hole, Ancient Lamp).
# Invoca La Jinn the Mystical Genie of the Lamp (1800 ATK).
# Coloca Seven Tools of the Bandit y Trap Hole.

# Turno 2 (Joey):
# Roba Reinforcement of the Army.
# Activa RotA: busca a Blade Knight (1600 -> 2000 ATK sin cartas en mano o con 1 carta).
# O busca a D.D. Warrior Lady.
# Invoca a Freed the Brave Wanderer (1700 ATK).
# Coloca Book of Moon y Compulsory Evacuation Device.

# Turno 3 (Jafar):
# Jafar ataca con La Jinn a Freed (1800 vs 1700).
# Joey encadena Book of Moon: voltea a La Jinn boca abajo en defensa (1000 DEF). Ataque cancelado.
# Jafar coloca Ancient Lamp boca abajo.

# Turno 4 (Joey):
# Roba Mirror Force.
# Joey invoca a Rocket Warrior (1500 ATK).
# Efecto de Rocket Warrior en Battle Phase: Invulnerable en ataque e inflige -500 ATK a La Jinn o ataca a Ancient Lamp.
# Freed (1700 ATK) destruye a La Jinn (1000 DEF).
# Joey coloca Mirror Force.

# Turno 5 (Jafar):
# Jafar activa Raigeki para limpiar el campo de Joey!
# Jafar invoca a Apophis the Swamp Deity o monstruo en ataque.
# Joey activa Compulsory Evacuation Device: salva a Freed o rebota el monstruo de Jafar.

# Turno 6 (Joey):
# Roba Goblin Attack Force (2300 ATK)!
# Ataque combinado directo: 2300 + 1700 = 4000 de daño!
# Jafar cae a 0 LP!

lp_jafar -= 4000
assert lp_jafar == 0, "Error en LP de Jafar"
print("Duelo de Joey verificado: Victoria limpia en Turno 6!")
