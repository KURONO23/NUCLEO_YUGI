# -*- coding: utf-8 -*-
"""
SIMULACIÓN OFICIAL - DUELO DE CUARTOS DE FINAL
Maksu (KURONO) vs Paul McGregor
Reglas Oficiales Konami DM (4000 LP)
"""

# ESTADO INICIAL
# Maksu LP: 4000 | Paul LP: 4000
# Moneda: Paul gana el volado y decide ir PRIMERO para activar su Flauta de Dragón.

# TURNO 1 (Paul McGregor):
# Mano Paul (5 cartas): The Flute of Summoning Dragon, Luster Dragon, Mirage Dragon, Stamping Destruction, Lord of D.
# Normal Summon: Lord of D. (Nivel 4 | OSCURIDAD | Lanzador | 1200 ATK / 900 DEF).
# Efecto de Lord of D.: Mientras esté boca arriba, todos los monstruos Dragón en el campo no pueden ser seleccionados por Magias, Trampas ni efectos de monstruos.
# Magic Activation: The Flute of Summoning Dragon (Magia Normal).
# Efecto: Invoca de Modo Especial hasta 2 monstruos Dragón de tu mano mientras Lord of D. esté en el campo.
# Special Summon 1: Luster Dragon (Nivel 4 | VIENTO | Dragón | 1900 ATK / 1600 DEF) en Posición de Ataque.
# Special Summon 2: Mirage Dragon (Nivel 4 | LUZ | Dragón | 1600 ATK / 600 DEF) en Posición de Ataque.
# Set 1 carta: Paul coloca Stamping Destruction boca abajo (o la guarda en mano porque requiere que el rival tenga magias/trampas para activarse).
# Mano Paul restante: Stamping Destruction (1 carta).
# Campo Paul: Lord of D. (1200 ATK), Luster Dragon (1900 ATK), Mirage Dragon (1600 ATK). Total ATK en campo: 4700 ATK!
# Paul pasa turno (en Turno 1 no se ataca).

# TURNO 2 (Maksu):
# Maksu roba su 6ta carta: M[5] = POT OF GREED!
# Mano Maksu (6 cartas):
# 1. Nobleman of Crossout
# 2. Pot of Greed (M[1])
# 3. Magician of Faith (M[2])
# 4. Book of Moon (M[3])
# 5. Breaker the Magical Warrior (M[4])
# 6. Pot of Greed (M[5])

# Standby Phase.
# Main Phase 1:
# Maksu activa Pot of Greed #1 (M[1]):
# Roba 2 cartas: M[6] = Dark Hole, M[7] = Reinforcement of the Army!
# Mano de Maksu: 7 cartas!
# Maksu activa Pot of Greed #2 (M[5]):
# Roba 2 cartas: M[8] = Yata-Garasu, M[9] = Jinzo!
# Mano de Maksu: 8 cartas!
# [AGENTE-2: JUEZ DE REGLAS INTERVIENE]:
# Lord of D. protege a los Dragones contra cartas que SELECCIONEN (Target).
# Pero DARK HOLE no selecciona! ("Destroy all monsters on the field").
# Maksu activa DARK HOLE!
# Cadena Link 1: Dark Hole.
# Se resuelve: Todos los monstruos en el campo son destruidos.
# Lord of D. (1200), Luster Dragon (1900) y Mirage Dragon (1600) son enviados al Cementerio de Paul!
# Paul queda con el campo TOTALMENTE LIMPIO!
# Maksu aún tiene su Normal Summon!
# Maksu invoca de Modo Normal a: BREAKER THE MAGICAL WARRIOR (1600 ATK / 1000 DEF).
# Efecto de Breaker: Gana 1 Spell Counter al ser invocado con éxito -> Sube a 1900 ATK!
# Battle Phase:
# Breaker the Magical Warrior ataca DIRECTO a los Puntos de Vida de Paul!
# Daño: 1900 puntos!
# [AGENTE-3: CONTADOR LP]:
# Paul LP: 4000 - 1900 = 2100 LP.
# Maksu LP: 4000.
# Main Phase 2:
# Maksu activa Reinforcement of the Army (RotA):
# Busca a Don Zaloog (Guerrero Nivel 4) a la mano. Baraja su mazo con Agente 9.
# Maksu coloca Book of Moon boca abajo.
# End Phase. Mano de Maksu: 5 cartas (Nobleman of Crossout, Magician of Faith, Yata-Garasu, Jinzo, Don Zaloog).

print("Turno 1 y 2 calculados con precision matematica.")
