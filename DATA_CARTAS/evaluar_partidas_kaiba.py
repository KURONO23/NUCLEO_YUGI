# -*- coding: utf-8 -*-
"""
EVALUADOR DE ENCUENTROS: MAKSU VS. KAIBA (5 SEMILLAS RNG)
Buscando el duelo más intenso, técnico y épico para el Capítulo de Novela.
"""

import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from simular_duelo_kaiba_vs_maksu import deck_maksu, deck_kaiba

def evaluar_encuentros(n=5):
    rng = secrets.SystemRandom()
    for i in range(1, n+1):
        m_deck = list(deck_maksu)
        k_deck = list(deck_kaiba)
        rng.shuffle(m_deck)
        rng.shuffle(k_deck)
        
        m_hand = [m_deck.pop(0) for _ in range(5)]
        k_hand = [k_deck.pop(0) for _ in range(5)]
        
        print(f"\n==================== PARTIDA RNG #{i} ====================")
        print("MAKSU MANO:", m_hand)
        print("MAKSU ROBO T1-T3:", [m_deck[j] for j in range(3)])
        print("---")
        print("KAIBA MANO:", k_hand)
        print("KAIBA ROBO T1-T3:", [k_deck[j] for j in range(3)])

if __name__ == "__main__":
    evaluar_encuentros(5)
