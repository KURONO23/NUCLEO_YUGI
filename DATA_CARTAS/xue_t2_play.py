# -*- coding: utf-8 -*-
import secrets

# Madame Xue tiene:
# Des Koala, Lava Golem, Level Limit - Area B, Swords of Revealing Light, Scapegoat, Just Desserts.
# Maksu tiene: 1 Monstruo boca abajo (Witch of the Black Forest, 1200 DEF).
# Mano de Maksu: 5 cartas.

# Si Des Koala se voltea, hace 400 por cada carta en mano de Maksu (5 x 400 = 2000 daño!).
# Madame Xue juega defensivo y de quemadura (Stall/Burn):
# 1. Bajar a Des Koala boca abajo (1800 DEF).
# 2. Setear cartas de protección o daño (Scapegoat, Just Desserts).
# 3. ¿Activa Swords of Revealing Light o Level Limit?

rng = secrets.SystemRandom()
play = rng.choice(["SET_KOALA_AND_SET_TRAPS", "SET_KOALA_AND_ACTIVATE_LEVEL_LIMIT"])
print("Jugada de Madame Xue T2:", play)
