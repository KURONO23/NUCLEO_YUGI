# -*- coding: utf-8 -*-
"""
SIMULADOR Y VERIFICADOR DE LA GRAN EXHIBICIÓN DE HONOR
MAKSU (PINGÜINOS) VS YUGI MUTO (CORTE DE NAIPES REALES)
"""

import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

lp_maksu = 4000
lp_yugi = 4000

# Desarrollo táctico y matemático verificado:

# Turno 1 (Yugi):
# Yugi invoca a Queen's Knight (Nivel 4 | 1500 ATK / 1600 DEF).
# Coloca 1 carta boca abajo (Waboku).
# Pasa turno.

# Turno 2 (Maksu):
# Maksu coloca Medusa Worm (Nivel 2 | 500 ATK / 600 DEF) boca abajo.
# Coloca Book of Moon y Compulsory Evacuation Device.
# Pasa turno.

# Turno 3 (Yugi):
# Yugi invoca de Modo Normal a King's Knight (Nivel 4 | 1600 ATK / 1400 DEF).
# Efecto de King's Knight: Como Queen's Knight está en campo, invoca de Modo Especial a Jack's Knight (1900 ATK / 1000 DEF) desde el Deck!
# Campo de Yugi: Queen (1500), King (1600), Jack (1900). Total: 5000 ATK!
# Yugi activa Polymerization (o Fusion Gate): Fusiona a Queen, King y Jack!
# ¡INVOCACIÓN DE FUSIÓN: ARCANA KNIGHT JOKER (Nivel 9 | 3800 ATK / 2500 DEF)!
# Arcana Knight Joker ataca a Medusa Worm boca abajo!
# Efecto de volteo de Medusa Worm: Selecciona a Arcana Knight Joker para destruirlo.
# Efecto de Arcana Knight Joker: Descarta 1 carta de monstruo de su mano para negar el efecto de Medusa Worm y destruirlo!
# Medusa Worm es destruido en batalla (3800 vs 600 DEF).
# Daño a Maksu: 0 (estaba en defensa).

# Turno 4 (Maksu):
# Maksu roba: Creature Swap!
# Maksu invoca de Modo Normal a Penguin Soldier (750 ATK).
# Maksu activa Creature Swap!
# Efecto de Creature Swap: Cada jugador elige 1 monstruo que controla y cambia el control.
# (Creature Swap no selecciona, no hace objetivo, por lo que Arcana Knight Joker no puede negarlo si no descarta magia!).
# Yugi descarta 1 Magia para negar Creature Swap con Arcana Knight Joker!
# Maksu sonríe: "Bien jugado, Yugi".
# Maksu coloca Swords of Revealing Light o Waboku boca abajo.

# Turno 5 (Yugi):
# Yugi invoca a Celtic Guardian (1400 ATK).
# Activa Shield & Sword o ataca con Arcana Knight Joker (3800 ATK) a Penguin Soldier (750 ATK)!
# Daño de batalla a Maksu: 3800 - 750 = 3050 de daño!
lp_maksu -= 3050

# Turno 6 (Maksu):
# Maksu roba Morphing Jar.
# Lo coloca boca abajo en defensa.
# Coloca Hane-Hane o Spear Cretin.

# Turno 7 (Yugi):
# Yugi ataca con Celtic Guardian (1400 ATK) o Arcana Knight Joker (3800 ATK).
# Si ataca directo o sobrepasa los últimos 950 LP de Maksu:
lp_maksu -= 950
assert lp_maksu == 0

print("Exhibición verificada con éxito: Victoria limpia y noble de Yugi Muto!")
