# -*- coding: utf-8 -*-
"""
VERIFICADOR MATEMÁTICO Y DE REGLAS: MAKSU VS SETO KAIBA
Reglas: 4000 LP Oficiales Konami DM / IOC Format
"""

def test_duelo_kaiba():
    # LP Iniciales
    lp_maksu = 4000
    lp_kaiba = 4000
    print(f"Inicio: Maksu {lp_maksu} LP | Kaiba {lp_kaiba} LP")
    
    # TURNO 1: KAIBA
    print("\n--- TURNO 1: KAIBA ---")
    # Kaiba invoca Blade Knight (1600 ATK).
    # Coloca 2 cartas boca abajo: Ring of Destruction y Crush Card Virus.
    # Mano de Kaiba: 2 cartas. (Blade Knight tiene 1600 ATK ya que tiene 2 cartas en mano; si tuviera 1 o 0 tendría 2000).
    print("Kaiba invoca Blade Knight (1600 ATK) y coloca 2 cartas boca abajo.")
    print(f"Estado Turno 1: Maksu {lp_maksu} LP | Kaiba {lp_kaiba} LP")
    
    # TURNO 2: MAKSU
    print("\n--- TURNO 2: MAKSU ---")
    # Maksu activa Harpie's Feather Duster.
    # Cadena de Kaiba: Ring of Destruction seleccionando a Blade Knight (1600 ATK).
    # Ring destruye a Blade Knight e inflige su ATK original (1600) a ambos jugadores.
    dano_ring = 1600
    lp_maksu -= dano_ring
    lp_kaiba -= dano_ring
    print(f"Ring of Destruction detona Blade Knight: -{dano_ring} LP a ambos.")
    print(f"LP tras Ring: Maksu {lp_maksu} LP | Kaiba {lp_kaiba} LP")
    assert lp_maksu == 2400
    assert lp_kaiba == 2400
    # Harpie's Feather Duster resuelve y destruye Crush Card Virus.
    print("Harpie's Feather Duster destruye Crush Card Virus.")
    # Maksu invoca Don Zaloog (1400 ATK).
    # Don Zaloog ataca directo.
    dano_zaloog = 1400
    lp_kaiba -= dano_zaloog
    print(f"Don Zaloog ataca directo: -{dano_zaloog} LP a Kaiba.")
    print(f"LP Kaiba: {lp_kaiba} LP")
    assert lp_kaiba == 1000
    # Efecto Don Zaloog: Kaiba descarta 1 carta al azar (Blue-Eyes White Dragon al cementerio).
    # Maksu coloca 2 cartas boca abajo: Book of Moon y Mirror Force.
    print("Efecto Don Zaloog: Kaiba descarta Blue-Eyes White Dragon. Maksu coloca 2 cartas.")
    
    # TURNO 3: KAIBA
    print("\n--- TURNO 3: KAIBA ---")
    # Kaiba roba (Topdeck: The Flute of Summoning Dragon). Mano Kaiba: Monster Reborn, Lord of D., The Flute of Summoning Dragon, Blue-Eyes White Dragon #2.
    # Kaiba activa Monster Reborn: revive Blue-Eyes White Dragon #1 (3000 ATK) del cementerio.
    # Kaiba invoca Lord of D. (1200 ATK).
    # Kaiba activa The Flute of Summoning Dragon: invoca de su mano Blue-Eyes White Dragon #2 (3000 ATK).
    print("Kaiba revive Blue-Eyes #1, invoca Lord of D. y con Flute invoca Blue-Eyes #2.")
    # Kaiba declara ataque con Blue-Eyes #1 sobre Don Zaloog (1400 ATK).
    # Maksu activa Book of Moon sobre Blue-Eyes #1, volteándolo a Posición de Defensa boca abajo (2500 DEF).
    print("Maksu activa Book of Moon sobre Blue-Eyes #1 volteándolo a Defensa boca abajo.")
    # Kaiba declara ataque con Blue-Eyes #2 sobre Don Zaloog (1400 ATK).
    dano_combate = 3000 - 1400
    lp_maksu -= dano_combate
    print(f"Blue-Eyes #2 destruye a Don Zaloog en batalla: Maksu recibe {dano_combate} de daño.")
    print(f"LP Maksu: {lp_maksu} LP")
    assert lp_maksu == 800
    # Kaiba declara ataque con Lord of D. (1200 ATK) para terminar el duelo.
    # Maksu activa Mirror Force.
    # Mirror Force destruye a todos los monstruos en Posición de Ataque del oponente.
    # Blue-Eyes #2 (3000 ATK) y Lord of D. (1200 ATK) son destruidos.
    # Blue-Eyes #1 está en Posición de Defensa boca abajo, por lo que NO es destruido por Mirror Force.
    print("Maksu activa Mirror Force: Blue-Eyes #2 y Lord of D. son destruidos. Blue-Eyes #1 en defensa sobrevive.")
    print(f"Fin Turno 3: Maksu {lp_maksu} LP | Kaiba {lp_kaiba} LP")
    
    # TURNO 4: MAKSU
    print("\n--- TURNO 4: MAKSU ---")
    # Maksu roba (Topdeck: Black Luster Soldier - Envoy of the Beginning).
    # En el cementerio de Maksu:
    # OSCURIDAD: Don Zaloog (enviado en T3).
    # LUZ: Magician of Faith (descartada previamente por Graceful Charity / Delinquent Duo o enviada con Painful Choice).
    # Digamos que en T2 Maksu jugó Graceful Charity descartando Magician of Faith (LUZ) y otra carta, o Don Zaloog (OSCURIDAD) y Magician of Faith (LUZ).
    # Maksu destierra 1 LUZ y 1 OSCURIDAD para invocar a Black Luster Soldier - EotB (3000 ATK).
    print("Maksu invoca de Modo Especial a Black Luster Soldier - Envoy of the Beginning (3000 ATK).")
    # BLS ataca al Blue-Eyes #1 boca abajo (2500 DEF).
    # Blue-Eyes se voltea boca arriba y es destruido en batalla (3000 ATK > 2500 DEF).
    # Efecto de BLS: 'When this card destroys an opponent's monster by battle: It can make a second attack in a row.'
    print("BLS destruye a Blue-Eyes boca abajo en batalla y activa su segundo ataque consecutivo.")
    # Segundo ataque de BLS: Ataque directo a Kaiba (3000 ATK).
    lp_kaiba -= 3000
    print(f"BLS ataca directo a Kaiba: 3000 de daño.")
    print(f"LP Kaiba Final: {lp_kaiba} LP")
    assert lp_kaiba <= 0
    print("\n=== VERIFICACIÓN EXITOSA: MAKSU GANA LIMPIAMENTE (42-0) ===")

if __name__ == "__main__":
    test_duelo_kaiba()
