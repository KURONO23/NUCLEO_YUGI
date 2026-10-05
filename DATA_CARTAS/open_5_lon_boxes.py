import random
import os
from collections import Counter
from card_data import LON_DATABASE

random.seed(555)

def open_pack(db):
    pack = []
    commons = random.choices(db["Common"], k=7)
    pack.extend([(c, "Common") for c in commons])
    
    # 1 Rara garantizada
    rare = random.choice(db["Rare"])
    pack.append((rare, "Rare"))
    
    # Probabilidad de Foil en el sobre:
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
        pack.append((foil, "Foil-" + rarity))
    else:
        extra_c = random.choice(db["Common"])
        pack.append((extra_c, "Common"))
        
    return pack

# 5 cajas = 120 sobres
total_packs = [open_pack(LON_DATABASE) for _ in range(120)]

foils = []
rares = Counter()
commons = Counter()

for p in total_packs:
    for card, r in p:
        name = card["name"]
        if r.startswith("Foil-"):
            foils.append((name, r.replace("Foil-", ""), card))
        elif r == "Rare":
            rares[name] += 1
        elif r == "Common":
            commons[name] += 1

print(f"=== RESULTADOS DE 5 CAJAS DE LON (120 SOBRES / 1,080 CARTAS) ===")
foil_counts = Counter([f"{r}: {name}" for name, r, c in foils])
for item, count in sorted(foil_counts.items()):
    print(f"  [{count}x] {item}")

print("\n--- RARES DESTACADAS ---")
for name, count in rares.most_common():
    print(f"  [{count}x] {name}")
