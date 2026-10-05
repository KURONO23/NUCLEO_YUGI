# -*- coding: utf-8 -*-
import secrets

# Dmitri tiene:
# Mechanicalchaser (1850), Cannon Soldier (1400), Dark Hole, Mirror Force, Imperial Order, Magic Jammer.
# Maksu tiene: 1 Monstruo boca abajo (Fiber Jar), 1 Trampa boca abajo (Ring of Destruction).

# Dmitri es agresivo. Ve 1 monstruo y 1 trampa.
# Opciones de apertura de Dmitri:
# 1. Bajar Mechanicalchaser (1850 ATK) y setear 2 trampas (Mirror Force / Imperial Order).
# 2. Activar Dark Hole para limpiar antes de invocar.
# En la cultura de juego de Ciudad Batallas / GOAT, un jugador agresivo que guarda Dark Hole para cuando el rival tenga varios monstruos invoca a su golpeador de 1850 ATK para testear la defensa.

rng = secrets.SystemRandom()
play = rng.choice(["SUMMON_MECHANICALCHASER_AND_SET_TRAPS", "SUMMON_MECHANICALCHASER_AND_SET_TRAPS", "DARK_HOLE_FIRST"])
print("Jugada de Dmitri:", play)
