import random
import json

# Pool canónico oficial de MRD (Metal Raiders)
SECRET_ULTRA = [
    "Mirror Force (Ultra Rara)",
    "Solemn Judgment (Ultra Rara)",
    "Change of Heart (Ultra Rara)",
    "Summoned Skull (Ultra Rara - 2500 ATK)",
    "Time Wizard (Ultra Rara)",
    "Barrel Dragon (Ultra Rara - 2600 ATK)",
    "B. Skull Dragon (Ultra Rara - 3200 ATK)",
    "Heavy Storm (Super Rara)",
    "Seven Tools of the Bandit (Super Rara)",
    "Magic Jammer (Super Rara)",
    "Tribute to The Doomed (Super Rara)",
    "Kuriboh (Super Rara)",
    "Sangan (Super Rara)",
    "Witch of the Black Forest (Super Rara)"
]

RARES = [
    "Jirai Gumo (Rara - 2200 ATK)",
    "Labyrinth Wall (Rara - 3000 DEF)",
    "Suijin (Rara - 2500 ATK)",
    "Kazejin (Rara - 2400 ATK)",
    "Sanga of the Thunder (Rara - 2600 ATK)",
    "Princess of Tsurugi (Rara)",
    "White Magical Hat (Rara - 1000 ATK)",
    "Mask of Darkness (Rara)",
    "Tremendous Fire (Rara)",
    "Share the Pain (Rara)",
    "Block Attack (Rara)"
]

COMMONS = [
    "Hane-Hane", "Penguin Soldier", "Ancient Elf", "Crawling Dragon #2 (1600 ATK)",
    "Little Chimera", "Bladefly", "Hoshiningen", "Milus Radiant",
    "Star Boy", "Witch's Apprentice", "Giga-Tech Wolf", "Thunder Kid",
    "Bat", "Armored Glass", "The Cheerful Coffin", "Just Desserts"
]

def simular_caja_mrd_inka():
    caja = []
    for num in range(1, 24 + 1):
        d20 = random.randint(1, 20)
        
        cartas_sobre = []
        # Ranura principal según el d20
        if d20 == 20:
            holo = random.choice(SECRET_ULTRA[:7])
            calidad = "NATURAL 20 (CRITICO ROTUNDO)"
        elif d20 >= 15:
            holo = random.choice(SECRET_ULTRA[7:])
            calidad = "EXITO NOTABLE"
        elif d20 >= 10:
            holo = random.choice(RARES[:6])
            calidad = "EXITO ESTANDAR"
        elif d20 >= 5:
            holo = random.choice(RARES[6:])
            calidad = "REGULAR"
        else:
            holo = "Pifia: Rara menor (" + random.choice(RARES[-3:]) + ")"
            calidad = "PIFIA / MALA SUERTE"
            
        cartas_sobre.append(holo)
        # Rara secundaria o común pesada
        cartas_sobre.append(random.choice(RARES))
        # 7 comunes
        cartas_sobre.extend(random.sample(COMMONS, 7))
        
        caja.append({
            "sobre": num,
            "d20": d20,
            "calidad": calidad,
            "cartas": cartas_sobre
        })
    return caja

if __name__ == "__main__":
    res = simular_caja_mrd_inka()
    with open("C:/projects/NUCLEO_YUGI/DATA_CARTAS/mrd_pulls_inka.json", "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
    print("Caja MRD INKA_rreble generada.")
