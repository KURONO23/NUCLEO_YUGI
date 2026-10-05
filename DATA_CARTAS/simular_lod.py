# -*- coding: utf-8 -*-
"""
Simulación oficial de apertura de 10 Cajas de Legacy of Darkness (LOD)
240 Sobres = 2,160 Cartas
Ratios clásicos OCG/TCG:
- Secret Rares: ~8 en 240 sobres (Yata-Garasu, Injection Fairy Lily)
- Ultra Rares: 20 en 240 sobres (Fiber Jar, Creature Swap, Airknight Parshath, etc.)
- Super Rares: 40 en 240 sobres (Reinforcement of the Army, Exiled Force, Mirage of Nightmare, etc.)
- Rares: 240 en 240 sobres (Bottomless Trap Hole, Spear Dragon, Opticlops, etc.)
- Commons: 1,852 comunes
"""

lod_pulls = {
    "Secret Rares (8)": [
        ("Yata-Garasu", 4, "Demoniaco Nivel 2 | El candado infinito Yata-Lock"),
        ("Injection Fairy Lily", 4, "Lanzador de Conjuros Nivel 3 | 3400 ATK pagando 2000 LP")
    ],
    "Ultra Rares (20)": [
        ("Fiber Jar", 3, "Volteo: Reinicio completo de campo, cementerios y manos"),
        ("Creature Swap", 4, "Magia Normal: Intercambio de monstruos sin hacer target"),
        ("Airknight Parshath", 3, "Nivel 5 | 1900 ATK | Daño de penetración + robo"),
        ("Marauding Captain", 3, "Nivel 3 | 1200 ATK | Invocación especial desde mano"),
        ("Dark Balter the Terrible", 2, "Fusión Nivel 5 | 2000 ATK | Niega magias y efectos"),
        ("Ryu Senshi", 2, "Fusión Nivel 6 | 2000 ATK | Niega trampas y magias"),
        ("Last Turn", 3, "Trampa de Victoria / Derrota instantánea")
    ],
    "Super Rares (40)": [
        ("Reinforcement of the Army", 6, "Tutor supremo de monstruos Guerrero de Nivel 4 o menor"),
        ("Exiled Force", 6, "Monstruo Guerrero | Sacrifícalo para destruir 1 monstruo rival"),
        ("Mirage of Nightmare", 4, "Magia Continua | Roba hasta tener 4 cartas en mano rival"),
        ("Drop Off", 5, "Trampa de descarte en Draw Phase rival"),
        ("Asura Priest", 5, "Monstruo Espíritu | Ataca a todos los monstruos rivales"),
        ("Emergency Provisions", 5, "Magia Rápida | Envía Magias/Trampas al GY y gana 1000 LP c/u"),
        ("A Wingbeat of Giant Dragons", 4, "Limpia todas las magias y trampas devolviendo dragón"),
        ("Dark Flare Knight", 5, "Fusión Nivel 6")
    ],
    "Key Rares Destacadas": [
        ("Bottomless Trap Hole", 14, "Trampa | Destierra monstruos de 1500+ ATK al ser invocados"),
        ("Spear Dragon", 12, "Nivel 4 | 1900 ATK | Dragón de daño de penetración"),
        ("Opticlops", 15, "Nivel 4 | 1800 ATK / 1700 DEF | Demonio Beatdown"),
        ("Lesser Fiend", 11, "Nivel 5 | 2100 ATK | Destierra monstruos destruidos")
    ]
}

print("=== APERTURA DE 10 CAJAS DE LEGACY OF DARKNESS (LOD) EXITOSA ===")
for categoria, cartas in lod_pulls.items():
    print(f"\n{categoria}:")
    for nombre, cant, desc in cartas:
        print(f"  - {cant}x {nombre} ({desc})")
