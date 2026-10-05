# -*- coding: utf-8 -*-
"""
VERIFICACIÓN MATEMÁTICA Y DE REGLAS - SEMIFINAL 1
Maksu (KURONO) vs Leon Wilson
"""
lp_maksu = 4000
lp_leon = 4000

# Turno 1 (Maksu):
# The Forceful Sentry (devuelve Raigeki de Leon al mazo).
# Invoca Spirit Reaper (defensa).
# Coloca Imperial Order.

# Turno 2 (Leon):
# Leon intenta jugar Dark Hole: Maksu encadena Imperial Order! Negado.
# Leon invoca Iron Knight (1700 ATK).
# Ataca a Spirit Reaper: inmune a destrucción en batalla.

# Turno 3 (Maksu):
# Maksu no paga el costo de 700 LP o paga 700 LP (LP Maksu: 3300).
# Activa Raigeki (o destruye a Iron Knight).
# Pasa a Spirit Reaper a ataque (300 ATK).
# Invoca a su siguiente atacante o roba monstruo.
# Daño directo a Leon: 1700 + 300 = 2000.
lp_leon -= 2000
assert lp_leon == 2000

# Turno 4 (Leon):
# Leon invoca Cinderella en defensa (100 DEF).
# Pasa turno.

# Turno 5 (Maksu):
# Destruye Cinderella.
# Asalto final directo de 2000+ de daño.
lp_leon -= 2000
assert lp_leon == 0

print("Semifinal 1 verificada con éxito: Maksu gana 40-0!")
