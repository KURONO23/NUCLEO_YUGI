# -*- coding: utf-8 -*-
"""
EJECUTOR COMPLETO Y VERIFICADOR DE LA GRAN FINAL FUN
Maksu (Pingüinos) vs Joey Wheeler (Gran Casino)
"""

import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

rng = secrets.SystemRandom()

print("=== INICIO DE LA GRAN FINAL CÓMICA ===")
lp_maksu = 4000
lp_joey = 4000

# Moneda para quién va primero:
moneda = rng.choice(["Cara", "Cruz"])
print(f"Moneda inicial: {moneda}")
# Maksu va primero

# Turno 1 (Maksu):
# Mano: Swords of Revealing Light, Hane-Hane, Sangan, Level Limit - Area B, Morphing Jar
# Maksu coloca Morphing Jar (Nivel 2 | 700 ATK / 600 DEF) boca abajo en defensa.
# Maksu activa Level Limit - Area B (Magia continua).
# Maksu coloca Swords of Revealing Light o la guarda.
# Pasa turno.

# Turno 2 (Joey):
# Roba Sangan.
# Mano Joey: Sasuke Samurai #4, Gamble, Gamble, Sand Gambler, Dice Jar, Sangan.
# Joey ve Level Limit - Area B (monstruos de nivel 4+ a defensa).
# Joey dice: "¡Ah, conque juegos mentales! ¡Toma esto!"
# Joey coloca DICE JAR (Nivel 3 | 200 ATK / 300 DEF) boca abajo en defensa!
# Joey coloca Gamble y Gamble en zona de trampas!
# Pasa turno.

# Turno 3 (Maksu):
# Roba Compulsory Evacuation Device.
# Maksu coloca Hane-Hane boca abajo.
# Maksu coloca Compulsory Evacuation Device.
# Pasa turno.

# Turno 4 (Joey):
# Roba Mystical Space Typhoon!
# Joey activa Mystical Space Typhoon a Level Limit - Area B! La destruye!
# Joey invoca de Modo Normal a Sasuke Samurai #4 (Nivel 4 | 1200 ATK).
# Sasuke Samurai #4 ataca al monstruo boca abajo de Maksu!
# Efecto de Sasuke Samurai #4: "Lanza una moneda y pide cara o cruz. Si aciertas, destruye al monstruo inmediatamente al inicio del Damage Step sin voltearlo!"
# Joey pide CARA.
moneda_sasuke = rng.choice(["Cara", "Cruz"])
print(f"Lanzamiento de Sasuke Samurai #4: Salió {moneda_sasuke} (Joey pidió Cara)")

# Si falla la moneda: el monstruo se voltea! ¡Es Morphing Jar!
# O si acierta, Morphing Jar es destruido sin efecto.
# Simulemos los dados de Dice Jar también:
dado_joey = rng.randint(1, 6)
dado_maksu = rng.randint(1, 6)
print(f"Tirada de Dice Jar: Joey saca {dado_joey}, Maksu saca {dado_maksu}")
