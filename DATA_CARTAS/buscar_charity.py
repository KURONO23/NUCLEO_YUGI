# -*- coding: utf-8 -*-
with open(r'C:\projects\NUCLEO_YUGI\05_CONTINUIDAD\INVENTARIO_CARTAS.md', 'r', encoding='utf-8') as f:
    text = f.read()

found = False
for line in text.split('\n'):
    if 'graceful' in line.lower() or 'caridad' in line.lower():
        print("Encontrado:", line)
        found = True

if not found:
    print("No se encontro Graceful Charity en INVENTARIO_CARTAS.md")
