# -*- coding: utf-8 -*-
"""
SIMULACIÓN COMPLETA Y RIGUROSA DE LA GRAN FINAL CÓMICA
Maksu (Pingüinos & Flip-Flop) vs Joey Wheeler (Gran Casino)
"""

import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

rng = secrets.SystemRandom()

# Turno 1 (Maksu):
# Coloca Hane-Hane (Nivel 2 | 450 ATK / 500 DEF) boca abajo.
# Activa Level Limit - Area B.
# Coloca Compulsory Evacuation Device.
# Pasa turno.

# Turno 2 (Joey):
# Roba Sangan.
# Ve Level Limit - Area B (monstruos de Nivel 4+ a defensa).
# Joey coloca DICE JAR (Nivel 3 | 200 ATK / 300 DEF) boca abajo.
# Coloca Gamble y Gamble.
# Pasa turno.

# Turno 3 (Maksu):
# Roba: Penguin Soldier! (Nivel 2 | 750 ATK / 500 DEF).
# Maksu invoca de Modo Normal a Penguin Soldier (750 ATK).
# Al ser nivel 2, NO le afecta Level Limit - Area B!
# Penguin Soldier (750 ATK) ataca a la carta boca abajo de Joey (DICE JAR)!
# ¡Efecto de Volteo de DICE JAR!
# Ambos tiran 1d6:
# Joey tira: 3.
# Maksu tira: 6!
# Regla de Dice Jar: Si el ganador saca un 6 y el perdedor saca 1-5, el perdedor recibe 3.000 de daño de efecto!
# ¡La jarra de dados explota hacia el lado de Joey!
# LP Joey: 4000 - 3000 = 1000 LP!
# Luego, en el cálculo de daño: 750 ATK de Penguin Soldier vs 300 DEF de Dice Jar.
# Dice Jar es destruida en batalla.
# Maksu coloca Morphing Jar boca abajo.
# Pasa turno.

# Turno 4 (Joey):
# Joey está con la cara tiznada de carbón a 1000 LP.
# Joey roba: Mystical Space Typhoon!
# Activa MST: destruye Level Limit - Area B de Maksu!
# Joey invoca a Sasuke Samurai #4 (Nivel 4 | 1200 ATK).
# Activa Gamble! Moneda: Cara o Cruz para robar 5 cartas.
# Moneda de Gamble:
moneda_gamble = rng.choice(["Cara", "Cruz"])
print(f"Moneda de Gamble de Joey: {moneda_gamble}")
# Si Cruz: el rival roba 1 carta o Joey pierde turno.

# Joey ataca con Sasuke Samurai #4 a Penguin Soldier de Maksu (750 ATK).
# Sasuke Samurai #4 moneda:
moneda_sasuke = rng.choice(["Cara", "Cruz"])
print(f"Moneda Sasuke: {moneda_sasuke}")

# Turno 5 (Maksu):
# Roba Waboku o Creature Swap!
# Maksu tiene Penguin Soldier en mano o en campo.
# Voltea a Hane-Hane o activa Creature Swap para cambiar de monstruo, o ataca con un ejército de pingüinos!
