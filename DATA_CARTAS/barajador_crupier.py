# -*- coding: utf-8 -*-
"""
MOTOR OFICIAL DE ALEATORIEDAD - [AGENTE-9: BARAJADOR RNG]
Módulo de Barajado Criptográfico e Imparcial para NÚCLEO_YUGI
"""

import sys
import secrets
import random

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

class BarajadorCrupier:
    def __init__(self, nombre_mazo, lista_cartas):
        self.nombre_mazo = nombre_mazo
        self.mazo_original = list(lista_cartas)
        self.mazo_actual = []
        self.mano = []
        self.cementerio = []
        self.desterradas = []
        self.campo_monstruos = []
        self.campo_magias_trampas = []
        self.barajar()

    def barajar(self):
        """Aplica Fisher-Yates usando generador seguro de entropia del sistema."""
        self.mazo_actual = list(self.mazo_original)
        rng = secrets.SystemRandom()
        rng.shuffle(self.mazo_actual)
        print(f"[AGENTE-9: BARAJADOR RNG] Mazo '{self.nombre_mazo}' barajado con exito. Total cartas: {len(self.mazo_actual)}")

    def robar_mano_inicial(self, cantidad=5):
        """Extrae de forma estricta las primeras 'cantidad' cartas del tope."""
        self.mano = []
        for _ in range(cantidad):
            if self.mazo_actual:
                self.mano.append(self.mazo_actual.pop(0))
        return self.mano

    def robar_carta(self, cantidad=1):
        """Roba estrictamente la carta del tope (Topdeck)."""
        robadas = []
        for _ in range(cantidad):
            if self.mazo_actual:
                c = self.mazo_actual.pop(0)
                self.mano.append(c)
                robadas.append(c)
        return robadas

    def barajar_mazo_restante(self):
        """Re-baraja las cartas restantes tras un buscador como RotA o Painful Choice."""
        rng = secrets.SystemRandom()
        rng.shuffle(self.mazo_actual)
        print(f"[AGENTE-9: BARAJADOR RNG] Baraja restante ({len(self.mazo_actual)} cartas) re-barajada legalmente.")

    def estado(self):
        return {
            "mazo_restante": len(self.mazo_actual),
            "mano_actual": self.mano,
            "cementerio": len(self.cementerio)
        }

if __name__ == "__main__":
    deck_v71 = [
        "Jinzo", "Jinzo", "Airknight Parshath", "Injection Fairy Lily",
        "Goblin Attack Force", "Zombyra the Dark", "Spear Dragon", "Kycoo the Ghost Destroyer",
        "Don Zaloog", "Exiled Force", "Spirit Reaper", "Witch of the Black Forest",
        "Sangan", "Fiber Jar", "Cyber Jar",
        "Reinforcement of the Army", "Book of Moon", "Book of Moon", "United We Stand",
        "Mage Power", "Painful Choice", "Giant Trunade", "Delinquent Duo", "Delinquent Duo",
        "The Forceful Sentry", "The Forceful Sentry", "Snatch Steal", "Nobleman of Crossout",
        "Pot of Greed", "Pot of Greed", "Raigeki", "Harpie's Feather Duster", "Graceful Charity",
        "Ring of Destruction", "Ring of Destruction", "Magic Cylinder", "Magic Cylinder",
        "Torrential Tribute", "Imperial Order", "Solemn Judgment"
    ]
    
    print(f"Total cartas cargadas: {len(deck_v71)}")
    crupier = BarajadorCrupier("Protocolo Silencio V7.1", deck_v71)
    mano_5 = crupier.robar_mano_inicial(5)
    print("\n--- MANO INICIAL REAL AL AZAR (5 CARTAS) ---")
    for i, c in enumerate(mano_5, 1):
        print(f"  [{i}] {c}")
        
    topdeck_1 = crupier.robar_carta(1)
    print(f"\n--- ROBO TURNO SIGUIENTE (TOPDECK): {topdeck_1[0]} ---")
    print(f"Cartas restantes en mazo: {crupier.estado()['mazo_restante']}")
