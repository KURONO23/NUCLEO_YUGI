import random
import sys

# Definir pool de Cybernetic Revolution (CRV)
CRV_POOL = {
    "Ultimate/Secret": ["Cyber End Dragon", "UFOroid Fighter", "Power Bond", "Cyber Twin Dragon"],
    "Ultra Rare": ["Cyber Dragon", "UFOroid", "Miracle Fusion", "Cyber End Dragon", "Power Bond", "Winged Kuriboh LV10"],
    "Super Rare": ["Steamroid", "Drillroid", "System Down", "Skyscraper", "Goblin Elite Attack Force"],
    "Rare": ["Gyroid", "Jetroid", "Patroid", "Cybernetic Magician", "Jerry Beans Man", "Spark Blaster", "Fusion Recovery", "Dimension Wall"],
    "Common": ["Wroughtweiler", "Bubble Shuffle", "Des Frog", "Frog the Jam"]
}

def open_crv_box():
    pulls = {
        "Ultra Rare": [],
        "Super Rare": [],
        "Rare": []
    }
    
    for i in range(24):
        roll = random.random()
        if roll < 0.10:
            pulls["Ultra Rare"].append(random.choice(CRV_POOL["Ultra Rare"]))
        elif roll < 0.30:
            pulls["Super Rare"].append(random.choice(CRV_POOL["Super Rare"]))
        else:
            pulls["Rare"].append(random.choice(CRV_POOL["Rare"]))
            
    if not pulls["Ultra Rare"]:
        pulls["Ultra Rare"].append("Power Bond")
    if "Drillroid" not in pulls["Super Rare"]:
        pulls["Super Rare"].append("Drillroid")
    if "Steamroid" not in pulls["Super Rare"]:
        pulls["Super Rare"].append("Steamroid")
        
    return pulls

def open_sandwiches(count=20):
    sandwiches = []
    has_golden = False
    golden_index = -1
    
    types = [
        "Sandwich de Huevo y Mayonesa",
        "Sandwich de Tofu Picante",
        "Sandwich de Fideos Yakisoba",
        "Sandwich de Atun Dulce",
        "Sandwich de Jamon y Queso Ahumado",
        "Sandwich de Eucalipto (Favorito de Chumley)",
        "Sandwich de Salmon con Salsa Tartara",
        "Sandwich de Pollo Teriyaki",
        "Sandwich de Carne Asada"
    ]
    
    for i in range(1, count + 1):
        if i == 17: # El sobre #17 es el dorado
            has_golden = True
            golden_index = i
            sandwiches.append((f"Sandwich #{i:02d}", "EL LEGENDARIO SANDWICH DE HUEVO DORADO", "Carta Secreta: Cyber Jar (Vintage Foil Edicion Limitada Dorothy)"))
        else:
            s_type = random.choice(types)
            sandwiches.append((f"Sandwich #{i:02d}", s_type, "Comun / Delicioso"))
            
    return sandwiches, has_golden, golden_index

if __name__ == "__main__":
    print("=== APERTURA DE 1 CAJA CRV PARA SYRUS ===")
    crv = open_crv_box()
    print("Ultra Rares:", crv["Ultra Rare"])
    print("Super Rares:", crv["Super Rare"])
    print("Rares:", list(set(crv["Rare"])))
    
    print("\n=== APERTURA DE 20 SANDWICHES DE LA TIENDA ===")
    sands, gold, idx = open_sandwiches(20)
    for s in sands:
        print(f"{s[0]}: {s[1]} -> {s[2]}")
