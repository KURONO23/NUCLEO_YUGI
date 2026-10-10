import random
import json

# Simulación completa MRD (Metal Raiders) - 24 sobres x 9 cartas = 216 cartas
# Pools de cartas reales de MRD:
SECRET_ULTRA = [
    "Mirror Force (Ultra Rara)",
    "Solemn Judgment (Ultra Rara)",
    "Change of Heart (Ultra Rara)",
    "Summoned Skull (Ultra Rara)",
    "Time Wizard (Ultra Rara)",
    "Barrel Dragon (Ultra Rara)",
    "B. Skull Dragon (Ultra Rara)",
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
    "Suijin (Rara)", "Kazejin (Rara)", "Sanga of the Thunder (Rara)",
    "Princess of Tsurugi (Rara)",
    "White Magical Hat (Rara)",
    "Mask of Darkness (Rara)",
    "Tremendous Fire (Rara)",
    "Share the Pain (Rara)",
    "Block Attack (Rara)"
]

COMMONS = [
    "Hane-Hane", "Penguin Soldier", "Ancient Elf", "Crawling Dragon #2",
    "Little Chimera", "Bladefly", "Hoshiningen", "Milus Radiant",
    "Star Boy", "Witch's Apprentice", "Giga-Tech Wolf", "Thunder Kid",
    "Bat", "Armored Glass", "The Cheerful Coffin", "Just Desserts"
]

def abrir_caja_mrd():
    caja = []
    for num in range(1, 25):
        d20 = random.randint(1, 20)
        
        # Generar 9 cartas para el sobre según el d20
        cartas_sobre = []
        
        # 1 ranura especial / rara principal
        if d20 == 20:
            holo = random.choice(SECRET_ULTRA[:7]) # Ultra / Secreta top
            calidad = "NATURAL 20 (CRITICO ROTUNDO)"
        elif d20 >= 15:
            holo = random.choice(SECRET_ULTRA[7:]) # Super / Ultra
            calidad = "EXITO NOTABLE"
        elif d20 >= 10:
            holo = random.choice(RARES[:6])
            calidad = "EXITO ESTANDAR"
        elif d20 >= 5:
            holo = random.choice(RARES[6:])
            calidad = "REGULAR"
        else: # 1 a 4
            holo = "Pifia: Rara menor inservible (" + random.choice(RARES[-3:]) + ")"
            calidad = "PIFIA / MALA SUERTE"
            
        cartas_sobre.append(holo)
        
        # 1 Rara adicional o común fuerte
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
    res = abrir_caja_mrd()
    with open("C:/projects/NUCLEO_YUGI/DATA_CARTAS/mrd_pulls_fabio.json", "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
    print("Simulacion MRD completada.")
