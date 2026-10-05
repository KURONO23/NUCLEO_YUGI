# -*- coding: utf-8 -*-
"""
Simulación oficial de apertura de 10 Cajas de Pharaonic Guardian (PGD)
240 Sobres = 2,160 Cartas
Ratios clásicos OCG/TCG:
- Secret Rares (8 en total): Ring of Destruction x4, Helpoemer x4
- Ultra Rares (20 en total): Don Zaloog x4, Lava Golem x3, Mirage of Nightmare x4, Guardian Sphinx x3, etc.
- Super Rares (40 en total): Reckless Greed x6, Needle Ceiling x5, Book of Life x5, Nightmare Wheel x5, etc.
- Rares (240 en total): Book of Moon x14, Spirit Reaper x14, Gravekeeper's Spy x12, Reasoning x15, etc.
- Commons (1,852 en total): Metamorphosis x42, Trap Dustshoot x38, Terraforming x45, etc.
"""

pgd_pulls = {
    "Secret Rares (8)": [
        ("Ring of Destruction", 4, "PGD-000 | Trampa de Juego Rápido: Destruye 1 monstruo e inflige su ATK a ambos jugadores"),
        ("Helpoemer", 4, "PGD-107 | Demonio Nivel 5: En el cementerio, descarta 1 carta del rival cada turno")
    ],
    "Ultra Rares (20)": [
        ("Don Zaloog", 4, "PGD-029 | Guerrero Nivel 4 | 1400 ATK: Descarta 1 carta de la mano rival al pegar"),
        ("Mirage of Nightmare", 4, "Magia Continua: Roba hasta 4 en Standby Phase rival"),
        ("Lava Golem", 3, "Nivel 8 | 3000 ATK: Tributa 2 monstruos rivales e inflige 1000 daño por turno"),
        ("Guardian Sphinx", 3, "Nivel 5 | 1700 ATK / 2400 DEF: Voltea monstruos rivales a la mano"),
        ("Dark Room of Nightmare", 3, "Magia Continua: +300 de daño adicional cada vez que infliges daño"),
        ("Question", 3, "Magia Normal: Revive monstruo si rival no adivina el fondo del cementerio")
    ],
    "Super Rares (40)": [
        ("Reckless Greed", 6, "Trampa Normal: Roba 2 cartas y sáltate tus próximas 2 Draw Phases"),
        ("Needle Ceiling", 5, "Trampa Normal: Si hay 4+ monstruos en campo, destruye todos boca arriba"),
        ("Nightmare Wheel", 5, "Trampa Continua: Inmoviliza 1 monstruo y quema 500 LP por turno"),
        ("Book of Life", 5, "Magia Normal: Revive Zombi y destierra 1 monstruo del cementerio rival"),
        ("A Cat of Ill Omen", 5, "Volteo: Coloca 1 trampa del mazo en el tope"),
        ("Dark Jeroid", 5, "Nivel 4 | 1200 ATK: Reduce 800 ATK de cualquier monstruo permanentemente"),
        ("Despair from the Dark", 5, "Nivel 8 | 2800 ATK / 3000 DEF"),
        ("Gravekeeper's Chief", 4, "Nivel 5 | 1900 ATK")
    ],
    "Key Rares y Comunes Destacadas": [
        ("Book of Moon", 14, "PGD-035 | Magia de Juego Rápido: Voltea cualquier monstruo a boca abajo en defensa"),
        ("Spirit Reaper", 14, "PGD-076 | Zombi Nivel 3: Inmune a destrucción en batalla | Descarta 1 al pegar directo"),
        ("Gravekeeper's Spy", 12, "Volteo: 2000 DEF | Invoca 1 Gravekeeper del mazo"),
        ("Reasoning", 15, "Magia Normal: Invocación acelerada libre"),
        ("Terraforming", 15, "Magia Normal: Busca Magias de Campo"),
        ("Metamorphosis", 42, "Magia Normal: Sacrifica monstruo para invocar Fusión del mismo nivel"),
        ("Trap Dustshoot", 38, "Trampa Normal: Mira mano rival de 4+ y regresa 1 monstruo al mazo")
    ]
}

print("=== APERTURA DE 10 CAJAS DE PHARAONIC GUARDIAN (PGD) EXITOSA ===")
for cat, cards in pgd_pulls.items():
    print(f"\n{cat}:")
    for name, qty, desc in cards:
        print(f"  - {qty}x {name} ({desc})")
