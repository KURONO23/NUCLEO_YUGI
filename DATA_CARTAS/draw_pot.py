import random

deck = [
    'Jinzo', 'Jinzo', 'Summoned Skull',
    'Giant Germ', 'Giant Germ', 'Giant Germ',
    'Mystic Tomato', 'Mystic Tomato',
    'Wall of Illusion', 'Wall of Illusion',
    'Goblin Attack Force', 'Witch of the Black Forest',
    'Sangan', 'Sangan', 'Cyber Jar', 'Morphing Jar',
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

random.seed(777)
random.shuffle(deck)

# Mano inicial:
hand = deck[:5]
remaining = deck[5:]

# Painful choice busca 5 cartas:
# 1 Pot of Greed (a mano)
# 4 al cementerio (Delinquent Duo, The Forceful Sentry, Monster Reborn, Call of the Haunted)
painful_targets = ['Pot of Greed', 'Delinquent Duo', 'The Forceful Sentry', 'Monster Reborn', 'Call of the Haunted']
for t in painful_targets:
    remaining.remove(t)

# Barajar tras Painful Choice
random.seed(888)
random.shuffle(remaining)

# Robo de Pot of Greed (2 cartas):
draw_1 = remaining.pop(0)
draw_2 = remaining.pop(0)

print(f"Robo 1 de Pot of Greed: {draw_1}")
print(f"Robo 2 de Pot of Greed: {draw_2}")
print(f"Robo Turno 3 de Kurono: {remaining.pop(0)}")
print(f"Robo Turno 5 de Kurono: {remaining.pop(0)}")
draw_t7 = remaining.pop(0)
print(f"Robo Turno 7 de Kurono: {draw_t7}")
draw_t9 = remaining.pop(0)
print(f"Robo Turno 9 de Kurono: {draw_t9}")
print(f"Cartas restantes en deck: {len(remaining)}")
