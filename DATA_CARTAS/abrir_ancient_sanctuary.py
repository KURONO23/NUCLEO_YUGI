# -*- coding: utf-8 -*-
"""
SIMULADOR DE APERTURA DE SOBRES - ANCIENT SANCTUARY (AST) & DARK CRISIS (DCR)
[AGENTE-1: CATALOGO / BIBLIOTECARIO]
"""

import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ast_secrets = ["The End of Anubis", "Invader of Darkness"]
ast_ultras = [
    "Zaborg the Thunder Monarch", "Enemy Controller", "Monster Gate",
    "Spirit of the Pharaoh", "Archfiend of Gilfer", "Blowback Dragon",
    "The Agent of Judgment - Saturn", "Gear Golem the Moving Fortress",
    "Stone Statue of the Aztecs", "Dark Magic Factory"
]
ast_supers = [
    "Night Assailant", "The Sanctuary in the Sky", "The Agent of Force - Mars",
    "The Agent of Creation - Venus", "Curse of Vampire", "Level Limit - Area B",
    "Drain Shield", "The Agent of Wisdom - Mercury", "Mystical Shine Ball",
    "The First Sarcophagus"
]

print("Base de datos de Ancient Sanctuary (AST) cargada con éxito en el Núcleo.")
