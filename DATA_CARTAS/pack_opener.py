import random
from card_data import LOB_DATABASE

def open_lob_pack():
    pack = []
    # 8 Comunes
    commons = random.choices(LOB_DATABASE["Common"], k=8)
    pack.extend([(c, "Common") for c in commons])
    
    # 1 Ranura de Rara o Superior
    roll = random.random()
    if roll < (1.0 / 31.0):  # ~3.2% Secreta
        card = random.choice(LOB_DATABASE["Secret Rare"])
        rarity = "Secret Rare"
    elif roll < (1.0 / 31.0 + 1.0 / 12.0):  # ~8.3% Ultra Rara
        card = random.choice(LOB_DATABASE["Ultra Rare"])
        rarity = "Ultra Rare"
    elif roll < (1.0 / 31.0 + 1.0 / 12.0 + 1.0 / 6.0):  # ~16.6% Súper Rara
        card = random.choice(LOB_DATABASE["Super Rare"])
        rarity = "Super Rare"
    else:  # Rara estándar
        card = random.choice(LOB_DATABASE["Rare"])
        rarity = "Rare"
        
    pack.append((card, rarity))
    return pack

def open_multiple_packs(count=10):
    all_opened = []
    print(f"=== Abriendo {count} Booster Packs de Legend of Blue Eyes White Dragon ===")
    for i in range(1, count + 1):
        p = open_lob_pack()
        all_opened.append(p)
        rare_card = p[-1]
        print(f"Sobre #{i:02d}: Rara/Foil -> [{rare_card[1]}] {rare_card[0]['name']}")
    return all_opened

if __name__ == "__main__":
    open_multiple_packs(5)
