# -*- coding: utf-8 -*-
"""
EJECUTOR OFICIAL DEL DUELO DE CUARTOS DE FINAL (KC GRAND CHAMPIONSHIP)
MAKSU (KURONO) VS PAUL McGREGOR (DETECTIVE)
Multi-Agente Autónomo: Agente 9 (RNG), Agente 2 (Juez), Agente 3 (LP), Agente 8 (Meta GOAT)
"""

import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def ejecutar_duelo():
    # Mazo Maksu (Chaos-Yata Tier 0 - 40 cartas)
    deck_maksu = [
        "Chaos Emperor Dragon - Envoy of the End", "Black Luster Soldier - Envoy of the Beginning",
        "Jinzo", "Yata-Garasu", "Breaker the Magical Warrior", "Tribe-Infecting Virus",
        "Injection Fairy Lily", "Spirit Reaper", "Don Zaloog", "Sangan",
        "Witch of the Black Forest", "Magician of Faith", "Cyber Jar", "Fiber Jar",
        "Painful Choice", "Graceful Charity", "Pot of Greed", "Pot of Greed",
        "Delinquent Duo", "The Forceful Sentry", "Harpie's Feather Duster", "Raigeki",
        "Dark Hole", "Dimension Fusion", "Snatch Steal", "Change of Heart",
        "Premature Burial", "Book of Moon", "Book of Moon", "Reinforcement of the Army",
        "United We Stand", "Nobleman of Crossout", "Ring of Destruction", "Ring of Destruction",
        "Mirror Force", "Torrential Tribute", "Imperial Order", "Solemn Judgment",
        "Magic Cylinder", "Robbin' Goblin"
    ]

    # Mazo Paul McGregor (Dragon Detective Beatdown - 40 cartas)
    deck_paul = [
        "Mirage Dragon", "Mirage Dragon", "Mirage Dragon",
        "Cave Dragon", "Cave Dragon", "Cave Dragon",
        "Luster Dragon", "Luster Dragon", "Luster Dragon",
        "Spear Dragon", "Spear Dragon",
        "Armed Dragon LV3", "Armed Dragon LV3", "Armed Dragon LV5",
        "The Stern Mystic", "The Stern Mystic", "Lord of D.",
        "Masked Dragon", "Masked Dragon",
        "Stamping Destruction", "Stamping Destruction",
        "Dragon's Gunfire", "Dragon's Gunfire",
        "Different Dimension Capsule", "Different Dimension Capsule",
        "Prohibition", "Prohibition", "Question",
        "Pot of Greed", "Heavy Storm", "Snatch Steal", "Mystical Space Typhoon",
        "The Flute of Summoning Dragon", "Dragon's Rage", "Dragon's Rage",
        "Trap Hole", "Trap Hole", "Bottomless Trap Hole", "Ring of Destruction",
        "Call of the Haunted"
    ]

    rng = secrets.SystemRandom()
    m_maksu = list(deck_maksu)
    m_paul = list(deck_paul)
    rng.shuffle(m_maksu)
    rng.shuffle(m_paul)

    return m_maksu, m_paul

if __name__ == "__main__":
    m_maksu, m_paul = ejecutar_duelo()
    print("=== MAZO COMPLETO MAKSU (40) ===")
    for idx, c in enumerate(m_maksu):
        print(f"M[{idx}]: {c}")
    print("\n=== MAZO COMPLETO PAUL (40) ===")
    for idx, c in enumerate(m_paul):
        print(f"P[{idx}]: {c}")

