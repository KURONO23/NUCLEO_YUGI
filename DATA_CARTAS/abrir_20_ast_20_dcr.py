# -*- coding: utf-8 -*-
"""
MOTOR OFICIAL DE APERTURA: 20 CAJAS DE ANCIENT SANCTUARY (AST) + 20 CAJAS DE DARK CRISIS (DCR)
Total: 40 Cajas = 960 Sobres sellados de fábrica
[AGENTE-1: CATALOGO] & [AGENTE-9: BARAJADOR RNG]
"""

import sys
import secrets
from collections import Counter

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

rng = secrets.SystemRandom()

# 1. ANCIENT SANCTUARY (AST)
ast_secrets = ["The End of Anubis", "Invader of Darkness"]
ast_ultras = [
    "Zaborg the Thunder Monarch", "Enemy Controller", "Monster Gate",
    "Spirit of the Pharaoh", "The Agent of Judgment - Saturn",
    "Gear Golem the Moving Fortress", "Stone Statue of the Aztecs",
    "Dark Magic Factory", "Archfiend of Gilfer", "Blowback Dragon"
]
ast_supers = [
    "Night Assailant", "The Sanctuary in the Sky", "The Agent of Force - Mars",
    "The Agent of Creation - Venus", "Curse of Vampire", "Level Limit - Area B",
    "Drain Shield", "The Agent of Wisdom - Mercury", "Mystical Shine Ball",
    "The First Sarcophagus"
]

# 2. DARK CRISIS (DCR)
dcr_secrets = ["Judgment of Anubis", "Mirage Knight"]
dcr_ultras = [
    "Vampire Lord", "Exodia Necross", "Shinato, King of a Higher Plane",
    "Reflect Bounder", "Butterfly Dagger - Elma", "Dark Master - Zorc",
    "Terrorking Archfiend", "Darkflare Knight", "Cost Down", "Guardian Ceal"
]
dcr_supers = [
    "D.D. Warrior Lady", "Spell Canceller", "Skill Drain", "Archfiend Soldier",
    "Contract with Exodia", "Pandemonium", "Falling Down", "Checkmate",
    "Shinato's Ark", "Ray of Hope"
]

def abrir_caja(set_name, secrets_list, ultras_list, supers_list):
    """Simula una caja de 24 sobres con ratios históricos de la era clásica."""
    pulls = []
    # En una caja clásica de 24 sobres:
    # 1 Secreta cada ~1.5 cajas (probabilidad ~65% por caja)
    if rng.random() < 0.65:
        pulls.append(("SECRET", rng.choice(secrets_list)))
    
    # 2 Ultra Rares por caja
    num_ultras = rng.choice([1, 2, 2, 2, 3])
    for _ in range(num_ultras):
        pulls.append(("ULTRA", rng.choice(ultras_list)))
    
    # 4 Super Rares por caja
    num_supers = rng.choice([3, 4, 4, 4, 5])
    for _ in range(num_supers):
        pulls.append(("SUPER", rng.choice(supers_list)))
        
    return pulls

# Abrir 20 cajas de AST (480 sobres)
pulls_ast = []
for i in range(20):
    caja_pulls = abrir_caja("AST", ast_secrets, ast_ultras, ast_supers)
    pulls_ast.extend(caja_pulls)

# Abrir 20 cajas de DCR (480 sobres)
pulls_dcr = []
for i in range(20):
    caja_pulls = abrir_caja("DCR", dcr_secrets, dcr_ultras, dcr_supers)
    pulls_dcr.extend(caja_pulls)

print("=== APERTURA DE 20 CAJAS DE ANCIENT SANCTUARY (AST) ===")
conteo_ast = Counter(pulls_ast)
for (rarity, card), count in sorted(conteo_ast.items(), key=lambda x: (x[0][0], -x[1])):
    print(f"  [{rarity}] {card} x{count}")

print("\n=== APERTURA DE 20 CAJAS DE DARK CRISIS (DCR) ===")
conteo_dcr = Counter(pulls_dcr)
for (rarity, card), count in sorted(conteo_dcr.items(), key=lambda x: (x[0][0], -x[1])):
    print(f"  [{rarity}] {card} x{count}")
