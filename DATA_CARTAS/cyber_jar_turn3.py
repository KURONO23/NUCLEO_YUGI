# -*- coding: utf-8 -*-
import sys
import secrets

# Reconstruimos el estado exacto
# Deck Maksu inicial (40)
# Mano inicial: Raigeki, Spear Dragon, United We Stand, Goblin Attack Force, Snatch Steal (5)
# Robo T1: Cyber Jar (1) -> Set en campo
# Robo T3: Imperial Order (1)
# Total sacadas del mazo de Maksu: 7 cartas
# Restan 33 cartas en el mazo de Maksu

# Deck Madame Xue inicial (40)
# Mano inicial: Just Desserts, Stealth Bird, Secret Barrel, Des Koala, Kuriboh (5)
# Robo T2: Secret Barrel (1)
# En campo de Xue: 1 Monstruo Set (Stealth Bird), 3 Trampas Set (Just Desserts, Secret Barrel, Secret Barrel)
# Mano de Xue: Des Koala, Kuriboh (2)
# Total sacadas del mazo de Xue: 6 cartas
# Restan 34 cartas en el mazo de Xue

# Vamos a ejecutar la simulación desde el script previo guardado o manteniendo la misma semilla si es posible,
# pero como usamos SystemRandom en el script anterior, veamos qué quedó o simulemos el top 5 exacto del mazo restante.

# Recuperemos los mazos completos y quitemos las cartas ya usadas:
deck_maksu = [
    "Jinzo", "Jinzo", "Airknight Parshath",
    "Injection Fairy Lily", "Zombyra the Dark",
    "Kycoo the Ghost Destroyer", "Don Zaloog", "Exiled Force", "Spirit Reaper",
    "Witch of the Black Forest", "Sangan",
    "Fiber Jar",
    "Reinforcement of the Army", "Book of Moon", "Book of Moon",
    "Mage Power", "Painful Choice", "Giant Trunade",
    "Delinquent Duo", "Delinquent Duo", "The Forceful Sentry", "The Forceful Sentry",
    "Nobleman of Crossout", "Pot of Greed", "Pot of Greed",
    "Harpie's Feather Duster",
    "Ring of Destruction", "Ring of Destruction", "Magic Cylinder", "Magic Cylinder",
    "Torrential Tribute", "Mirror Force", "Solemn Judgment"
]

deck_xue = [
    "Lava Golem", "Lava Golem",
    "Stealth Bird", "Stealth Bird",
    "Des Koala", "Des Koala",
    "Princess of Tsurugi", "Princess of Tsurugi",
    "Morphing Jar", "Cyber Jar",
    "Kuriboh",
    "Wave-Motion Cannon", "Wave-Motion Cannon", "Wave-Motion Cannon",
    "Messenger of Peace", "Messenger of Peace",
    "Swords of Revealing Light", "Level Limit - Area B",
    "Pot of Greed", "Graceful Charity", "Dark Hole", "Scapegoat", "Scapegoat",
    "Secret Barrel", "Just Desserts", "Gravity Bind", "Gravity Bind",
    "Ojama Trio", "Ojama Trio", "Ceasefire", "Ring of Destruction",
    "Magic Cylinder", "Imperial Order", "Solemn Judgment"
]

rng = secrets.SystemRandom()
rng.shuffle(deck_maksu)
rng.shuffle(deck_xue)

top5_maksu = deck_maksu[:5]
top5_xue = deck_xue[:5]

print("=== TOP 5 MAKSU (CYBER JAR) ===")
for c in top5_maksu:
    print("  *", c)

print("\n=== TOP 5 MADAME XUE (CYBER JAR) ===")
for c in top5_xue:
    print("  *", c)
