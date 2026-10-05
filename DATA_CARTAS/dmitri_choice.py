# -*- coding: utf-8 -*-
import secrets

# Dmitri analiza las 5 cartas:
# 1. Jinzo
# 2. Tribe-Infecting Virus
# 3. Premature Burial
# 4. Graceful Charity
# 5. Harpie's Feather Duster

# Ningún jugador sensato le da Tribe-Infecting Virus contra un mazo de Máquinas.
# Ni le da Premature Burial teniendo a Jinzo y Tribe en el cementerio.
# Por tanto, las opciones reales que un duelista de choque considera "el mal menor" son:
# - Graceful Charity (esperando que robe mal)
# - Harpie's Feather Duster (al menos no es un monstruo inmediato)
# - Jinzo (esperando que no tenga con qué tributarlo)

rng = secrets.SystemRandom()
choice = rng.choice(["GRACEFUL_CHARITY", "HARPIE_FEATHER_DUSTER", "GRACEFUL_CHARITY"])
print("Dmitri elige darte:", choice)
