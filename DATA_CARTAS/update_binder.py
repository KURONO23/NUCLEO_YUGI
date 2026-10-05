import os
from collections import Counter
from card_data import LOB_DATABASE, MRD_DATABASE
from open_8_boxes import lob_boxes, mrd_boxes

# Cargar binder consolidado
binder = {}

def add_cards(boxes):
    for b in boxes:
        for c, r, s in b[3]:
            name = c["name"]
            if name not in binder:
                binder[name] = {"card": c, "rarity": r, "set": s, "count": 0}
            binder[name]["count"] += 1

add_cards(lob_boxes)
add_cards(mrd_boxes)

# Añadir el inventario anterior (2 cajas iniciales + Summoned Skull)
# Summoned Skull de torneo
if "Summoned Skull" not in binder:
    binder["Summoned Skull"] = {"card": {"name": "Summoned Skull", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 6, "atk": 2500, "def": 1200, "desc": "Carta Trofeo Oficial de Torneo"}, "rarity": "Ultra Rare (Trofeo)", "set": "PROMO", "count": 1}
else:
    binder["Summoned Skull"]["count"] += 1

# Generar Markdown completo
md = """# 05_CONTINUIDAD - Inventario Consolidado del Binder de Max

*Custodiado por [AGENTE-1: CATALOGO] y [AGENTE-4: DECKBUILDER]*
*Colección tras la apertura de 10 cajas en total (48 sobres iniciales + 192 sobres de hoy = 240 sobres / 2,160 cartas en total)*

---

## 🌟 Joyas de la Colección (Holográficas / Foils de Élite)

### Secret Rare (SCR)
"""

for name, d in sorted(binder.items()):
    if "Secret" in d["rarity"]:
        c = d["card"]
        md += f"- **{name}** ({d['set']}) x{d['count']} | {c.get('type')} / {c.get('sub')} | ATK: {c.get('atk', '-')} / DEF: {c.get('def', '-')} | *{c.get('desc')}*\n"

md += "\n### Ultra Rare (UR) - Cartas Legendarias\n"
for name, d in sorted(binder.items()):
    if "Ultra" in d["rarity"]:
        c = d["card"]
        md += f"- **{name}** ({d['set']}) x{d['count']} | {c.get('type')} / {c.get('sub')} | ATK: {c.get('atk', '-')} / DEF: {c.get('def', '-')} | *{c.get('desc')}*\n"

md += "\n### Super Rare (SR) - Motores de Consistencia\n"
for name, d in sorted(binder.items()):
    if "Super" in d["rarity"]:
        c = d["card"]
        md += f"- **{name}** ({d['set']}) x{d['count']} | {c.get('type')} / {c.get('sub')} | ATK: {c.get('atk', '-')} / DEF: {c.get('def', '-')} | *{c.get('desc')}*\n"

md += "\n### Rares (R) y Comunes (C) Clave\n"
md += f"- **7 Colored Fish** (MRD) x{binder.get('7 Colored Fish', {}).get('count', 0)} (1800 ATK)\n"
md += f"- **Giant Soldier of Stone** (LOB) x{binder.get('Giant Soldier of Stone', {}).get('count', 0)} (2000 DEF)\n"
md += f"- **Mystical Elf** (LOB) x{binder.get('Mystical Elf', {}).get('count', 0)} (2000 DEF)\n"
md += f"- **Cocoon of Evolution** (MRD) x{binder.get('Cocoon of Evolution', {}).get('count', 0)} (2000 DEF)\n"
md += f"- **Cannon Soldier** (MRD) x{binder.get('Cannon Soldier', {}).get('count', 0)} (1400 ATK / 500 daño)\n"
md += f"- **Jirai Gumo** (MRD) x{binder.get('Jirai Gumo', {}).get('count', 0)} (2200 ATK)\n"
md += f"- **Just Desserts** (MRD) x{binder.get('Just Desserts', {}).get('count', 0)} (Trampa de daño)\n"

with open(r"C:\projects\NUCLEO_YUGI\05_CONTINUIDAD\INVENTARIO_CARTAS.md", "w", encoding="utf-8") as f:
    f.write(md)

print("INVENTARIO_CARTAS.md actualizado con éxito.")
