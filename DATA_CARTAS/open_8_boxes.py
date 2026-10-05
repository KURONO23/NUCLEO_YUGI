import random
import os
from card_data import LOB_DATABASE, MRD_DATABASE

# Fijamos semilla para que el tiraje sea consistente, emocionante y verificable
random.seed(101)

def open_pack(db):
    pack = []
    # 8 Comunes
    commons = random.choices(db["Common"], k=8)
    pack.extend([(c, "Common") for c in commons])
    
    # 1 Ranura de Rara / Foil según probabilidades oficiales
    roll = random.random()
    if roll < (1.0 / 31.0):  # ~3.2% Secreta
        card = random.choice(db["Secret Rare"])
        rarity = "Secret Rare"
    elif roll < (1.0 / 31.0 + 1.0 / 12.0):  # ~8.3% Ultra Rara
        card = random.choice(db["Ultra Rare"])
        rarity = "Ultra Rare"
    elif roll < (1.0 / 31.0 + 1.0 / 12.0 + 1.0 / 6.0):  # ~16.6% Super Rara
        card = random.choice(db["Super Rare"])
        rarity = "Super Rare"
    else:  # Rara
        card = random.choice(db["Rare"])
        rarity = "Rare"
        
    pack.append((card, rarity))
    return pack

def open_box(db, set_name):
    box_packs = [open_pack(db) for _ in range(24)]
    foils = []
    rares = []
    all_cards = []
    for p in box_packs:
        for c, r in p:
            all_cards.append((c, r, set_name))
        foil_slot = p[-1]
        if foil_slot[1] in ["Secret Rare", "Ultra Rare", "Super Rare"]:
            foils.append((foil_slot[0]["name"], foil_slot[1]))
        else:
            rares.append((foil_slot[0]["name"], foil_slot[1]))
    return box_packs, foils, rares, all_cards

# Abrir 4 Cajas de LOB y 4 Cajas de MRD
lob_boxes = [open_box(LOB_DATABASE, "LOB") for i in range(4)]
mrd_boxes = [open_box(MRD_DATABASE, "MRD") for i in range(4)]

print("=== APERTURA DE 4 CAJAS DE LEGEND OF BLUE EYES WHITE DRAGON (LOB) ===")
for i, b in enumerate(lob_boxes, 1):
    print(f"\n--- CAJA LOB #{i} ---")
    print(f"Foils extraídas ({len(b[1])}):")
    for name, rarity in b[1]:
        print(f"  [{rarity}] {name}")

print("\n=== APERTURA DE 4 CAJAS DE METAL RAIDERS (MRD) ===")
for i, b in enumerate(mrd_boxes, 1):
    print(f"\n--- CAJA MRD #{i} ---")
    print(f"Foils extraídas ({len(b[1])}):")
    for name, rarity in b[1]:
        print(f"  [{rarity}] {name}")

# Consolidar todo el inventario
# Cargar inventario previo si existe
all_opened = []
for b in lob_boxes:
    all_opened.extend(b[3])
for b in mrd_boxes:
    all_opened.extend(b[3])

with open(r"C:\projects\NUCLEO_YUGI\DATA_CARTAS\opened_cards_summary.txt", "w", encoding="utf-8") as out:
    out.write(f"Total cartas abiertas en 8 cajas: {len(all_opened)}\n")
    for i, b in enumerate(lob_boxes, 1):
        out.write(f"\n[CAJA LOB #{i}]:\n")
        for name, rarity in b[1]:
            out.write(f"  [{rarity}] {name}\n")
    for i, b in enumerate(mrd_boxes, 1):
        out.write(f"\n[CAJA MRD #{i}]:\n")
        for name, rarity in b[1]:
            out.write(f"  [{rarity}] {name}\n")

print("\nSimulacion completada exitosamente.")
