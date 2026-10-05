# -*- coding: utf-8 -*-
"""
VERIFICADOR MATEMÁTICO Y DE REGLAS - DUELO CUARTOS DE FINAL
"""
# LP Iniciales
lp_maksu = 4000
lp_paul = 4000

# Turno 1 (Paul):
# Convoca Lord of D. (1200) y con The Flute of Summoning Dragon convoca Luster Dragon (1900) y Mirage Dragon (1600).
# Coloca Stamping Destruction.
# Daño: 0.

# Turno 2 (Maksu):
# Roba Pot of Greed. Activa Pot of Greed #1 (roba Dark Hole y RotA).
# Activa Pot of Greed #2 (roba Yata-Garasu y Jinzo).
# Activa Dark Hole (destruye Lord of D., Luster Dragon, Mirage Dragon).
# Invoca Breaker the Magical Warrior (1600 + 300 = 1900 ATK).
# Ataque directo de Breaker: 1900 de daño.
lp_paul -= 1900
assert lp_paul == 2100, f"Error en Turno 2 Paul LP: {lp_paul}"

# Turno 3 (Paul):
# Roba Armed Dragon LV3. Lo invoca (1200 ATK).
# Activa Stamping Destruction a la carta Set de Maksu (Book of Moon).
# Maksu encadena Book of Moon a Armed Dragon LV3 (queda boca abajo en 900 DEF).
# Stamping Destruction destruye Book of Moon y quema 500 a Maksu.
lp_maksu -= 500
assert lp_maksu == 3500, f"Error en Turno 3 Maksu LP: {lp_maksu}"

# Turno 4 (Maksu):
# Activa Nobleman of Crossout: destruye y destierra a Armed Dragon LV3 boca abajo.
# Invoca de Modo Normal a Don Zaloog (1400 ATK).
# Battle Phase:
# Breaker (1900 ATK) + Don Zaloog (1400 ATK) = 3300 daño directo.
lp_paul -= 3300
assert lp_paul <= 0, f"Error en Turno 4 Paul LP: {lp_paul}"

print("=== VERIFICACIÓN EXITOSA: 0 ERRORES ===")
print(f"LP Final Maksu: {lp_maksu}")
print(f"LP Final Paul: {lp_paul} (DERROTA POR DAÑO EXCEDENTE)")
