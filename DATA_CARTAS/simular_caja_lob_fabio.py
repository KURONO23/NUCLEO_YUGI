import random
import json

# Simulación de probabilidades LOB (Legend of Blue Eyes White Dragon)
# 9 cartas por sobre: 7 Comunes, 1 Rara fija, 1 slot variable (Común/Super/Ultra/Secret)

def abrir_caja_lob_con_iniciativa():
    sobres_resultado = []
    
    # Pool de cartas icónicas de LOB (excluyendo Dragón Blanco)
    secretas_ultra = [
        "Gaia the Fierce Knight (Ultra Rara)",
        "Dark Magician (Ultra Rara)",
        "Monster Reborn (Ultra Rara)",
        "Polymerization (Super Rara)",
        "Dark Hole (Super Rara)",
        "Raigeki (Super Rara)",
        "Swords of Revealing Light (Super Rara)",
        "Trap Hole (Super Rara)",
        "Flame Swordsman (Super Rara)",
        "Celtic Guardian (Super Rara)",
        "Man-Eater Bug (Super Rara)"
    ]
    
    raras_buenas = [
        "Fissure (Rara)", "Trap Hole (Rara)", "Curse of Dragon (Rara)", 
        "Mystical Elf (Rara)", "Silver Fang (Rara)", "Stop Defense (Rara)"
    ]
    
    comunes_buenas = [
        "Basic Insect", "Mammoth Graveyard", "Kagemusha of the Blue Flame",
        "Armored Lizard", "Dragon Statue", "Dark Gray", "Petit Dragon",
        "Hinotama", "Sparks", "Red Medicine", "Final Flame"
    ]

    for i in range(1, 25):
        d20 = random.randint(1, 20)
        
        # Lógica del D20 según el Agente del Caos
        if d20 == 20:
            loot = f"¡NATURAL 20! HITS LEGENDARIO: {random.choice(secretas_ultra)} + Rara Brillante"
            calidad = "CRITICO ROTUNDO"
        elif d20 >= 15:
            loot = f"Éxito Notable: {random.choice(secretas_ultra[:5])} o Super Rara"
            calidad = "MUY BUENO"
        elif d20 >= 10:
            loot = f"Éxito Estándar: {random.choice(raras_buenas)} + Comunes sólidas"
            calidad = "DECENTE"
        elif d20 >= 5:
            loot = f"Bajo: Rara menor ({random.choice(raras_buenas[-2:])}) y comunes relleno"
            calidad = "REGULAR"
        else: # 1 a 4
            loot = "Pifia / Mala Suerte: Monstruos normales débiles de 400-800 ATK y magias inútiles"
            calidad = "PIFIA / BASURA"

        sobres_resultado.append({
            "sobre": i,
            "d20": d20,
            "calidad": calidad,
            "loot": loot
        })
        
    return sobres_resultado

if __name__ == "__main__":
    resultado = abrir_caja_lob_con_iniciativa()
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
