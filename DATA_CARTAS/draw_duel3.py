import random

deck = [
    'Jinzo', 'Jinzo', 'Summoned Skull',
    'Giant Germ', 'Giant Germ', 'Giant Germ',
    'Mystic Tomato', 'Mystic Tomato',
    'Wall of Illusion', 'Wall of Illusion',
    'Goblin Attack Force', 'Witch of the Black Forest',
    'Sangan', 'Mechanicalchaser', 'Cyber Jar', 'Morphing Jar',
    'Magician of Faith', 'Magician of Faith', 'Kuriboh',
    'Painful Choice', 'Giant Trunade', 'Card Destruction',
    'Delinquent Duo', 'Delinquent Duo',
    'The Forceful Sentry', 'The Forceful Sentry',
    'Snatch Steal', 'Nobleman of Crossout',
    'Pot of Greed', 'Pot of Greed',
    'Raigeki', 'Dark Hole', 'Harpie\'s Feather Duster',
    'Mystical Space Typhoon', 'Monster Reborn', 'Change of Heart',
    'Imperial Order', 'Call of the Haunted', 'Waboku',
    'Dust Tornado', 'Robbin\' Goblin', 'Mirror Force', 'Solemn Judgment'
]

# Semilla reproducible para el Duelo #3
random.seed(333)
random.shuffle(deck)

print("Mano Inicial Duelo #3 (5 cartas):")
for i, c in enumerate(deck[:5], 1):
    print(f" {i}. {c}")

print(f"Robo Turno 1 (6ta carta): {deck[5]}")
print(f"Robo Turno 3: {deck[6]}")
print(f"Robo Turno 5: {deck[7]}")
