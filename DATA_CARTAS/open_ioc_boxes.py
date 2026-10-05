# -*- coding: utf-8 -*-
import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Lista de cartas destacadas de Invasion of Chaos (IOC):
secret_rares = [
    "Black Luster Soldier - Envoy of the Beginning",
    "Chaos Emperor Dragon - Envoy of the End",
    "Invader of Darkness"
]

ultra_rares = [
    "Dark Magician of Chaos",
    "Dimension Fusion",
    "Chaos Sorcerer",
    "Levia-Dragon - Daedalus",
    "Manticore of Darkness",
    "Freed the Brave Wanderer",
    "Strike Ninja",
    "D.D. Scout Plane",
    "Orca Mega-Fortress of Darkness",
    "Insect Princess"
]

super_rares = [
    "Compulsory Evacuation Device",
    "Smashing Ground",
    "Reload",
    "Stealth Bird",
    "Enraged Battle Ox",
    "Stumbling",
    "Wild Nature's Release",
    "Big Burn",
    "Granadora",
    "Gradius' Option"
]

rares_commons_key = [
    "Manju of the Ten Thousand Hands",
    "Giga Gagagigo",
    "Fenrir",
    "Trap Jammer",
    "Begone, Knave!",
    "Chiron the Mage",
    "Mad Dog of Darkness",
    "Blazing Inpachi",
    "Burning Beast"
]

rng = secrets.SystemRandom()

def open_boxes(owner_name, num_boxes=4):
    print(f"==================================================")
    print(f"📦 APERTURA OFICIAL IOC: {owner_name} ({num_boxes} Cajas)")
    print(f"==================================================")
    
    # En cajas de IOC vintage:
    # 1 Secret Rare cada 1-2 cajas (o garantizada en casos maestros)
    # 2 Ultra Rares por caja
    # 4-6 Super Rares por caja
    
    pulls_secret = []
    pulls_ultra = []
    pulls_super = []
    pulls_rares = {}
    
    for b in range(1, num_boxes + 1):
        # Secret check (alta probabilidad en master cases)
        sec = rng.choice(secret_rares)
        pulls_secret.append(sec)
        
        # 2 Ultras por caja
        u1 = rng.choice(ultra_rares)
        u2 = rng.choice(ultra_rares)
        pulls_ultra.extend([u1, u2])
        
        # 5 Supers por caja
        for _ in range(5):
            s = rng.choice(super_rares)
            pulls_super.append(s)
            
        # Key Rares
        for _ in range(10):
            r = rng.choice(rares_commons_key)
            pulls_rares[r] = pulls_rares.get(r, 0) + 1
            
    print("\n✨ SECRET RARES EXTRAÍDAS:")
    for s in set(pulls_secret):
        print(f"  🌟 {s} x{pulls_secret.count(s)}")
        
    print("\n🔥 ULTRA RARES EXTRAÍDAS:")
    for u in set(pulls_ultra):
        print(f"  ⭐ {u} x{pulls_ultra.count(u)}")
        
    print("\n⚡ SUPER RARES CLAVE:")
    for sp in set(pulls_super):
        print(f"  💎 {sp} x{pulls_super.count(sp)}")
        
    print("\n🔍 RARES / COMMONS DE IMPACTO:")
    for r, count in pulls_rares.items():
        print(f"  📘 {r} x{count}")
        
    return {
        "secrets": pulls_secret,
        "ultras": pulls_ultra,
        "supers": pulls_super,
        "rares": pulls_rares
    }

print("--- APERTURA DE SOBRES EN LA SUITE IMPERIAL ---")
res_maksu = open_boxes("MAKSU", num_boxes=4)
print("\n")
res_yugi = open_boxes("YUGI MUTO / ATEM", num_boxes=4)
