# -*- coding: utf-8 -*-
"""
MOTOR OFICIAL DE SIMULACIÓN - CUARTOS DE FINAL KC GRAND CHAMPIONSHIP
MAKSU (KURONO) VS PAUL McGREGOR
Cumplimiento estricto de Reglas Oficiales de Yu-Gi-Oh! (Konami DM / 4000 LP)
"""

import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("================================================================================")
print("       CUARTOS DE FINAL KC GRAND CHAMPIONSHIP — KAIBA LAND ARENA CENTRAL")
print("                  MAKSU (KURONO) [38-0] vs PAUL McGREGOR")
print("================================================================================\n")

# DECISIÓN DEL AZAR (Lanzamiento de Moneda oficial)
# Paul elige Cara, cae Cruz -> Maksu decide. Maksu elige jugar SEGUNDO para tener la 6ta carta y desmantelar el campo rival.
print("[AGENTE-9: BARAJADOR RNG] Moneda en el aire: Cae CRUZ. Maksu gana el sorteo y elige jugar SEGUNDO.\n")

# Mazo Maksu (40 cartas ordenadas por el barajador RNG inicial):
# Mano inicial (5 cartas):
# 1. Injection Fairy Lily
# 2. Dimension Fusion
# 3. Robbin' Goblin
# 4. Book of Moon
# 5. Witch of the Black Forest
# Topdecks: Ring of Destruction (Turno 2), Reinforcement of the Army (Turno 4), Delinquent Duo (Turno 6), Tribe-Infecting Virus (Turno 8)

# Mazo Paul (40 cartas ordenadas por el barajador RNG inicial):
# Mano inicial (5 cartas):
# 1. Armed Dragon LV5
# 2. Luster Dragon
# 3. Dragon's Rage
# 4. Snatch Steal
# 5. Mirage Dragon
# Topdecks: Masked Dragon (Turno 1), Heavy Storm (Turno 3), Mirage Dragon (Turno 5)

print("--- ESTADO INICIAL ---")
print("LP Maksu: 4000 | LP Paul McGregor: 4000")
print("Mano Maksu: [Injection Fairy Lily, Dimension Fusion, Robbin' Goblin, Book of Moon, Witch of the Black Forest]")
print("Mano Paul: [Armed Dragon LV5, Luster Dragon, Dragon's Rage, Snatch Steal, Mirage Dragon]\n")
