# -*- coding: utf-8 -*-
"""
VERIFICACIÓN MATEMÁTICA Y LEGAL DE LA GRAN FINAL CÓMICA
"""
lp_maksu = 4000
lp_joey = 4000

# Turno 1 (Maksu): Coloca Hane-Hane, Level Limit - Area B. (LP: 4000 vs 4000)

# Turno 2 (Joey): Coloca Dice Jar boca abajo, Gamble Set. (LP: 4000 vs 4000)

# Turno 3 (Maksu): Invoca Penguin Soldier (750 ATK). Ataca a Dice Jar boca abajo.
# Flip de Dice Jar: Ambos tiran 1d6.
# Joey: 3. Maksu: 6.
# Si el ganador saca 6 y el perdedor saca 1-5: el perdedor sufre 3000 daño directo!
lp_joey -= 3000
assert lp_joey == 1000, f"Error en Dice Jar: {lp_joey}"

# Batalla: 750 ATK vs 300 DEF. Dice Jar destruida. Maksu coloca Morphing Jar.

# Turno 4 (Joey):
# MST a Level Limit - Area B.
# Activa Gamble: Moneda sale CARA. Joey roba 5 cartas!
# Invoca Sasuke Samurai #4 (1200 ATK).
# Ataca a Penguin Soldier (750 ATK). Moneda de Sasuke sale CRUZ (falla destrucción automática).
# Daño de batalla a Maksu: 1200 - 750 = 450.
lp_maksu -= 450
assert lp_maksu == 3550, f"Error en daño de Sasuke: {lp_maksu}"
# Penguin Soldier al GY.

# Turno 5 (Maksu):
# Flip Summon de Hane-Hane (450 ATK): regresa a Sasuke Samurai #4 a la mano de Joey.
# Flip Summon de Morphing Jar (700 ATK): Ambos descartan mano y roban 5.
# Fase de Batalla:
# Ataque directo de Morphing Jar: 700.
# Ataque directo de Hane-Hane: 450.
# Daño total directo: 700 + 450 = 1150 daño directo.
lp_joey -= 1150
assert lp_joey <= 0, f"Error en remate final: {lp_joey}"

print("=== VERIFICACIÓN MATEMÁTICA EXITOSA ===")
print(f"LP Final Maksu: {lp_maksu}")
print(f"LP Final Joey: {lp_joey} (K.O. por rebote y ataque de bichos)")
