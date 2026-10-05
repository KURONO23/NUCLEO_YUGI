# -*- coding: utf-8 -*-
"""
SIMULADOR OFICIAL RNG: MAKSU (KURONO) VS. SETO KAIBA
Lugar: KaibaCorp Tower Rooftop Arena / Kaiba Dome (Domino City)
Reglas: 4000 LP Oficiales, Sistema Duel Disk Estado Sólido
"""

import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Baraja de Maksu: Protocolo Apocalipsis V8.0 (Chaos-Yata Control Tier 0)
deck_maksu = [
    # Monstruos (14)
    "Chaos Emperor Dragon - Envoy of the End",
    "Black Luster Soldier - Envoy of the Beginning",
    "Jinzo",
    "Yata-Garasu",
    "Breaker the Magical Warrior",
    "Tribe-Infecting Virus",
    "Injection Fairy Lily",
    "Spirit Reaper",
    "Don Zaloog",
    "Sangan",
    "Witch of the Black Forest",
    "Magician of Faith",
    "Cyber Jar",
    "Fiber Jar",
    # Magias (18)
    "Painful Choice",
    "Graceful Charity",
    "Pot of Greed",
    "Delinquent Duo",
    "The Forceful Sentry",
    "Harpie's Feather Duster",
    "Raigeki",
    "Dark Hole",
    "Dimension Fusion",
    "Snatch Steal",
    "Change of Heart",
    "Premature Burial",
    "Book of Moon",
    "Book of Moon",
    "Reinforcement of the Army",
    "United We Stand",
    "Nobleman of Crossout",
    "Pot of Greed",
    # Trampas (8)
    "Ring of Destruction",
    "Ring of Destruction",
    "Mirror Force",
    "Torrential Tribute",
    "Imperial Order",
    "Solemn Judgment",
    "Magic Cylinder",
    "Robbin' Goblin"
]

# Baraja de Seto Kaiba: Dragón Blanco & Caos Corporativo
deck_kaiba = [
    # Monstruos (17)
    "Blue-Eyes White Dragon",
    "Blue-Eyes White Dragon",
    "Blue-Eyes White Dragon",
    "Chaos Emperor Dragon - Envoy of the End",
    "Blade Knight",
    "Blade Knight",
    "Vorse Raider",
    "Vorse Raider",
    "Spear Dragon",
    "Spear Dragon",
    "Kaiser Sea Horse",
    "Lord of D.",
    "Lord of D.",
    "Cyber-Stein",
    "Cyber Jar",
    "Sangan",
    "Twin-Headed Behemoth",
    # Magias (15)
    "The Flute of Summoning Dragon",
    "The Flute of Summoning Dragon",
    "Polymerization",
    "Pot of Greed",
    "Graceful Charity",
    "Soul Exchange",
    "Cost Down",
    "Shrink",
    "Enemy Controller",
    "Enemy Controller",
    "Heavy Storm",
    "Mystical Space Typhoon",
    "Monster Reborn",
    "Premature Burial",
    "Card of Demise",
    # Trampas (8)
    "Ring of Destruction",
    "Ring of Defense",
    "Crush Card Virus",
    "Interdimensional Matter Transporter",
    "Shadow Spell",
    "Cloning",
    "Torrential Tribute",
    "Mirror Force"
]

def simular_partida():
    rng = secrets.SystemRandom()
    m_deck = list(deck_maksu)
    k_deck = list(deck_kaiba)
    
    rng.shuffle(m_deck)
    rng.shuffle(k_deck)
    
    m_hand = [m_deck.pop(0) for _ in range(5)]
    k_hand = [k_deck.pop(0) for _ in range(5)]
    
    print("=== ESTADO INICIAL BARAJADO CON CRUPIER SECRETS ===")
    print(f"Cartas en Mazo Maksu: {len(m_deck)} | Mano: {len(m_hand)}")
    print(f"Cartas en Mazo Kaiba: {len(k_deck)} | Mano: {len(k_hand)}")
    
    print("\n--- MANO INICIAL DE MAKSU (5 Cartas) ---")
    for i, c in enumerate(m_hand, 1):
        print(f"  {i}. {c}")
        
    print("\n--- MANO INICIAL DE KAIBA (5 Cartas) ---")
    for i, c in enumerate(k_hand, 1):
        print(f"  {i}. {c}")
        
    print("\n--- TOPDECKS DE MAKSU (Siguientes 5 cartas) ---")
    for i in range(5):
        print(f"  T+{i+1}: {m_deck[i]}")
        
    print("\n--- TOPDECKS DE KAIBA (Siguientes 5 cartas) ---")
    for i in range(5):
        print(f"  T+{i+1}: {k_deck[i]}")

if __name__ == "__main__":
    simular_partida()
