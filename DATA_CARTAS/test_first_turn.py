# -*- coding: utf-8 -*-
import sys

# Simulador táctico Maksu vs Paul
# Si Maksu va Primero (Turno 1):
# Mano de Maksu:
# [1] Injection Fairy Lily
# [2] Dimension Fusion
# [3] Robbin' Goblin
# [4] Book of Moon
# [5] Witch of the Black Forest

# Turno 1 (Maksu):
# Coloca Witch of the Black Forest boca abajo en DEF (1200 DEF).
# Coloca Book of Moon boca abajo.
# Coloca Robbin' Goblin boca abajo.
# Pasa turno.

# Turno 2 (Paul):
# Paul roba: Masked Dragon.
# Mano Paul (6 cartas): Armed Dragon LV5, Luster Dragon, Dragon's Rage, Snatch Steal, Mirage Dragon, Masked Dragon.
# Paul invoca Luster Dragon (1900 ATK).
# Paul coloca Dragon's Rage.
# Paul entra a Battle Phase y ataca con Luster Dragon a Witch boca abajo.
# En la declaración de ataque, Maksu activa Book of Moon:
# Selecciona a Luster Dragon: se voltea boca abajo en defensa (1600 DEF). Ataque cancelado!
# Paul pasa turno.

# Turno 3 (Maksu):
# Maksu roba: Ring of Destruction!
# Mano de Maksu: Injection Fairy Lily, Dimension Fusion, Ring of Destruction (3 cartas).
# Campo de Maksu: Witch of the Black Forest (1200 DEF boca abajo), Robbin' Goblin (Set).
# Campo de Paul: Luster Dragon (1600 DEF boca abajo), Dragon's Rage (Set).
# Main Phase 1:
# Maksu invoca de Modo Normal a Injection Fairy Lily (400 ATK / 1500 DEF)!
# Coloca Ring of Destruction boca abajo.
# Battle Phase:
# Lily ataca a Luster Dragon boca abajo (1600 DEF).
# Damage Step: Maksu activa efecto de Lily: paga 2000 LP -> 3400 ATK!
# LP Maksu: 4000 - 2000 = 2000 LP.
# 3400 ATK destruye a Luster Dragon (1600 DEF). Luster al GY de Paul.
# Witch no ataca (1100 ATK).
# End Phase.

# Turno 4 (Paul):
# Paul roba: Heavy Storm!
# Mano Paul (5 cartas): Armed Dragon LV5, Snatch Steal, Mirage Dragon, Masked Dragon, Heavy Storm.
# LP Paul: 4000 | LP Maksu: 2000.
# Paul activa Heavy Storm!
# CADENA:
# Link 1: Heavy Storm.
# Link 2: Maksu activa Ring of Destruction!
# Pero no hay monstruos en campo de Paul! Ring requiere seleccionar 1 monstruo boca arriba!
# Maksu puede seleccionar a su propia Lily (400 ATK)? Si destruye a Lily, ambos reciben 400 de daño.
# LP Maksu: 2000 - 400 = 1600. LP Paul: 4000 - 400 = 3600.
# Pero espera!

print("Calculando variantes...")
