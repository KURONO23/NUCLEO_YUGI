import random
import os
from collections import Counter
from card_data import LOB_DATABASE, MRD_DATABASE

# Fijar semilla para reproducibilidad exacta de la apertura
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

lob_packs = [open_pack(LOB_DATABASE) for _ in range(24)]
mrd_packs = [open_pack(MRD_DATABASE) for _ in range(24)]

binder = {}
for p in lob_packs:
    for c, r in p:
        name = c["name"]
        if name not in binder:
            binder[name] = {"card": c, "rarity": r, "set": "LOB", "count": 0}
        binder[name]["count"] += 1

for p in mrd_packs:
    for c, r in p:
        name = c["name"]
        if name not in binder:
            binder[name] = {"card": c, "rarity": r, "set": "MRD", "count": 0}
        binder[name]["count"] += 1

# Generar Markdown
md_content = """# 05_CONTINUIDAD - Inventario y Colección de Cartas (Binder)

*Registrado por [AGENTE-1: CATALOGO] y archivado por [AGENTE-4: DECKBUILDER]*
*Resultado de la apertura de 2 cajas completas (24 sobres de LOB + 24 sobres de MRD = 48 sobres / 432 cartas)*

---

## 🌟 Joyas de la Colección (Holográficas / Foils)

### Secret Rare (SCR)
"""

for name, data in binder.items():
    if data["rarity"] == "Secret Rare":
        c = data["card"]
        md_content += f"- **{name}** ({data['set']}) x{data['count']} | {c.get('type')} / {c.get('sub')} | ATK: {c.get('atk', '-')} / DEF: {c.get('def', '-')} | *{c.get('desc')}*\n"

md_content += "\n### Ultra Rare (UR)\n"
for name, data in binder.items():
    if data["rarity"] == "Ultra Rare":
        c = data["card"]
        md_content += f"- **{name}** ({data['set']}) x{data['count']} | {c.get('type')} / {c.get('sub')} | ATK: {c.get('atk', '-')} / DEF: {c.get('def', '-')} | *{c.get('desc')}*\n"

md_content += "\n### Super Rare (SR)\n"
for name, data in binder.items():
    if data["rarity"] == "Super Rare":
        c = data["card"]
        md_content += f"- **{name}** ({data['set']}) x{data['count']} | {c.get('type')} / {c.get('sub')} | ATK: {c.get('atk', '-')} / DEF: {c.get('def', '-')} | *{c.get('desc')}*\n"

md_content += "\n### Rare (R)\n"
for name, data in binder.items():
    if data["rarity"] == "Rare":
        c = data["card"]
        md_content += f"- **{name}** ({data['set']}) x{data['count']} | {c.get('type')} / {c.get('sub')} | ATK: {c.get('atk', '-')} / DEF: {c.get('def', '-')} | *{c.get('desc')}*\n"

md_content += "\n### Common (C) - Monstruos & Recursos Destacados\n"
for name, data in sorted(binder.items()):
    if data["rarity"] == "Common":
        c = data["card"]
        md_content += f"- **{name}** ({data['set']}) x{data['count']} | {c.get('type')} | ATK: {c.get('atk', '-')} / DEF: {c.get('def', '-')} | *{c.get('desc')}*\n"

with open(r"C:\projects\NUCLEO_YUGI\05_CONTINUIDAD\INVENTARIO_CARTAS.md", "w", encoding="utf-8") as f:
    f.write(md_content)

print("INVENTARIO_CARTAS.md generado con éxito.")
