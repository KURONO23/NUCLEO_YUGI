import os
from collections import Counter
from card_data import LOB_DATABASE, MRD_DATABASE
from open_8_boxes import lob_boxes, mrd_boxes

# Cargar todas las cajas abiertas (las 2 iniciales + las 8 de hoy)
spells = Counter()
traps = Counter()

# Datos de cartas
all_boxes = lob_boxes + mrd_boxes

for b in all_boxes:
    for c, r, s in b[3]:
        t = c.get("type", "")
        name = c.get("name", "")
        if t == "Spell":
            spells[name] += 1
        elif t == "Trap":
            traps[name] += 1

# Incluir las 2 cajas iniciales de generate_inventory.py (semilla 42)
import random
random.seed(42)
def open_pack(db):
    pack = []
    commons = random.choices(db["Common"], k=8)
    pack.extend([(c, "Common") for c in commons])
    roll = random.random()
    if roll < (1.0 / 31.0):
        card = random.choice(db["Secret Rare"])
        rarity = "Secret Rare"
    elif roll < (1.0 / 31.0 + 1.0 / 12.0):
        card = random.choice(db["Ultra Rare"])
        rarity = "Ultra Rare"
    elif roll < (1.0 / 31.0 + 1.0 / 12.0 + 1.0 / 6.0):
        card = random.choice(db["Super Rare"])
        rarity = "Super Rare"
    else:
        card = random.choice(db["Rare"])
        rarity = "Rare"
    pack.append((card, rarity))
    return pack

init_lob = [open_pack(LOB_DATABASE) for _ in range(24)]
init_mrd = [open_pack(MRD_DATABASE) for _ in range(24)]

for p in init_lob + init_mrd:
    for c, r in p:
        t = c.get("type", "")
        name = c.get("name", "")
        if t == "Spell":
            spells[name] += 1
        elif t == "Trap":
            traps[name] += 1

print("--- MAGIAS ---")
for k, v in sorted(spells.items()):
    print(f"{k}: x{v}")

print("\n--- TRAMPAS ---")
for k, v in sorted(traps.items()):
    print(f"{k}: x{v}")
