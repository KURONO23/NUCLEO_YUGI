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

random.seed(999)
random.shuffle(deck)

# Mano inicial (5) + Robo Turno 1 (1):
hand = deck[:6]
rem = deck[6:]

# Painful choice targets:
pc_targets = ['Jinzo', 'Monster Reborn', 'Pot of Greed', 'Call of the Haunted', 'Delinquent Duo']
for t in pc_targets:
    rem.remove(t)

# Barajar tras Painful Choice:
random.seed(1234)
random.shuffle(rem)

# Robo Turno 3:
draw_t3 = rem.pop(0)
# Robo Turno 5:
draw_t5 = rem.pop(0)

print(f"Robo Turno 3: {draw_t3}")
print(f"Robo Turno 5: {draw_t5}")
print(f"Cartas restantes: {len(rem)}")
