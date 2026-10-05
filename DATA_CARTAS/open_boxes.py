import random
import os
from collections import Counter
from card_data import LOB_DATABASE, MRD_DATABASE

def open_pack(db):
    pack = []
    # 8 Comunes
    commons = random.choices(db["Common"], k=8)
    pack.extend([(c, "Common") for c in commons])
    
    # 1 Ranura de Rara / Foil
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

def run_box_openings():
    lob_packs = [open_pack(LOB_DATABASE) for _ in range(24)]
    mrd_packs = [open_pack(MRD_DATABASE) for _ in range(24)]
    
    all_cards = []
    for p in lob_packs:
        for c, r in p:
            all_cards.append((c, r, "LOB"))
            
    for p in mrd_packs:
        for c, r in p:
            all_cards.append((c, r, "MRD"))
            
    return lob_packs, mrd_packs, all_cards

if __name__ == "__main__":
    lob_packs, mrd_packs, all_cards = run_box_openings()
    print(f"Total cartas abiertas: {len(all_cards)}")
    
    foils_lob = [p[-1] for p in lob_packs if p[-1][1] != "Rare"]
    foils_mrd = [p[-1] for p in mrd_packs if p[-1][1] != "Rare"]
    
    print("\n--- FOILS DE LOB (Legend of Blue Eyes) ---")
    for c, r in foils_lob:
        print(f"[{r}] {c['name']}")
        
    print("\n--- FOILS DE MRD (Metal Raiders) ---")
    for c, r in foils_mrd:
        print(f"[{r}] {c['name']}")
