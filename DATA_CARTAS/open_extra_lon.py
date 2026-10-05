import random
from card_data import LON_DATABASE

random.seed(7771)

def open_pack(db):
    pack = []
    commons = random.choices(db["Common"], k=7)
    pack.extend([(c, "Common") for c in commons])
    rare = random.choice(db["Rare"])
    pack.append((rare, "Rare"))
    roll = random.random()
    if roll < (1.0 / 31.0):
        foil = random.choice(db["Secret Rare"])
        rarity = "Secret Rare"
    elif roll < (1.0 / 31.0 + 1.0 / 12.0):
        foil = random.choice(db["Ultra Rare"])
        rarity = "Ultra Rare"
    elif roll < (1.0 / 31.0 + 1.0 / 12.0 + 1.0 / 6.0):
        foil = random.choice(db["Super Rare"])
        rarity = "Super Rare"
    else:
        foil = None
    if foil:
        pack.append((foil, rarity))
    else:
        pack.append((random.choice(db["Common"]), "Common"))
    return pack

# 2 cajas adicionales = 48 sobres
packs_extra = [open_pack(LON_DATABASE) for _ in range(48)]
extra_foils = [p[-1] for p in packs_extra if p[-1][1] in ["Secret Rare", "Ultra Rare", "Super Rare"]]
print("Foils en 2 cajas extra:")
for f in extra_foils:
    print(f[1], ":", f[0]["name"])
