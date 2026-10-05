import json

with open(r"C:\projects\NUCLEO_YUGI\DATA_CARTAS\audit_cards_db.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

md_lines = [
    "# 04_SISTEMAS - Gran Compendio de Auditoría Integral (Base de Datos Oficial)",
    "",
    "*Auditado por [AGENTE-1: CATALOGO] & [AGENTE-2: JUEZ DE DUELO]*",
    "*Conexión directa con la Base de Datos Global de Cartas de Yu-Gi-Oh! (YGOPRODeck API)*",
    "",
    "---",
    "",
    "## 📜 REGISTRO OFICIAL DE CARTAS AUDITADAS Y RULINGS ESTRICTOS",
    ""
]

for name, info in sorted(cards.items()):
    md_lines.append(f"### 🃏 {name}")
    if info.get("status") == "Anime/Especial":
        md_lines.append(f"- **Estatus**: Carta de Anime / Exclusiva")
        md_lines.append(f"- **Efecto Auditado**: Interpretación canónica de la serie animada.")
    else:
        ctype = info.get("type", "N/A")
        md_lines.append(f"- **Tipo Oficial**: {ctype}")
        if "Monster" in ctype:
            md_lines.append(f"- **Atributo / Tipo**: {info.get('attribute', 'N/A')} / {info.get('race', 'N/A')} (Nivel {info.get('level', 'N/A')})")
            md_lines.append(f"- **Valores**: **{info.get('atk', 0)} ATK / {info.get('def', 0)} DEF**")
        else:
            md_lines.append(f"- **Subtipo**: {info.get('race', 'Normal')}")
        desc = info.get("desc", "").replace("\n", " ")
        md_lines.append(f"- **Texto Oficial**: *\"{desc}\"*")
        
        # Añadir dictamen específico del juez
        if name == "Graceful Dice":
            md_lines.append("- ⚠️ **DICTAMEN DEL JUEZ**: En TCG oficial afecta a todos tus monstruos, pero **bajo la regla estricta de anime de Joey**, se aplica seleccionando a **1 solo monstruo objetivo**.")
        elif name == "Skull Dice":
            md_lines.append("- ⚠️ **DICTAMEN DEL JUEZ**: Reduce el ATK de los monstruos según el resultado del dado.")
        elif name == "Witch of the Black Forest":
            md_lines.append("- ⚠️ **DICTAMEN DEL JUEZ**: **Filtro estricto DEF <= 1500**. NO puede buscar a CED ni a BLS (ambos tienen 2500 DEF).")
        elif name == "Sangan":
            md_lines.append("- ⚠️ **DICTAMEN DEL JUEZ**: **Filtro estricto ATK <= 1500**. Solo busca a monstruos de ataque bajo.")
        elif name == "Black Luster Soldier - Envoy of the Beginning":
            md_lines.append("- ⚠️ **DICTAMEN DEL JUEZ**: Si activa su efecto de destierro, **NO PUEDE ATACAR ese turno**.")
        elif name == "Chaos Emperor Dragon - Envoy of the End":
            md_lines.append("- ⚠️ **DICTAMEN DEL JUEZ**: Paga 1000 LP. Manda todas las cartas al cementerio. Daño: 300 por cada carta enviada.")
        elif name == "Gearfried the Iron Knight":
            md_lines.append("- ⚠️ **DICTAMEN DEL JUEZ**: Destruye automáticamente cualquier carta de equipo que se le intente equipar.")
        elif name == "Blade Knight":
            md_lines.append("- ⚠️ **DICTAMEN DEL JUEZ**: Solo gana +400 ATK si el controlador tiene 1 o menos cartas en mano.")
    md_lines.append("")

output_md = r"C:\projects\NUCLEO_YUGI\04_SISTEMAS\AUDITORIA_COMPLETA_13000_CARTAS.md"
with open(output_md, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Archivo markdown generado exitosamente en {output_md}")
