# -*- coding: utf-8 -*-
"""
Análisis de líneas de juego óptimas para Maksu vs Paul
"""
import sys

# Si Maksu va Primero (Turn 1):
# Mano Maksu (5 cartas):
# 1. Injection Fairy Lily
# 2. Dimension Fusion
# 3. Robbin' Goblin
# 4. Book of Moon
# 5. Witch of the Black Forest

# Turn 1 (Maksu):
# Coloca Witch of the Black Forest boca abajo en DEF (1200 DEF).
# Coloca Book of Moon boca abajo.
# Coloca Robbin' Goblin boca abajo.
# Pasa turno.

# Turn 2 (Paul):
# Paul roba: Armed Dragon LV5, Luster Dragon, Dragon's Rage, Snatch Steal, Mirage Dragon + Topdeck: Masked Dragon (6 cartas).
# Paul invoca Luster Dragon (1900 ATK).
# Paul coloca Dragon's Rage.
# Paul ataca con Luster Dragon a Witch boca abajo.
# Maksu encadena Book of Moon: voltea a Luster Dragon boca abajo! Ataque cancelado.
# Paul termina turno con Luster Dragon en defensa boca abajo y 1 trampa.

# Turn 3 (Maksu):
# Maksu roba: Ring of Destruction!
# Mano de Maksu: Ring of Destruction, Injection Fairy Lily, Dimension Fusion, Robbin' Goblin (en campo).
# En campo: Witch of the Black Forest (1200 DEF boca abajo), Book of Moon (usada/GY).
# Maksu puede colocar Ring of Destruction.
# O Maksu puede voltear a Witch (1100 ATK) o invocar a Lily (3400 ATK).
# Si Lily ataca a Luster Dragon en DEF (1600 DEF):
# Lily paga 2000 LP -> 3400 ATK. Destruye a Luster Dragon.
# Pero espera!

print("Simulacion iniciada...")
