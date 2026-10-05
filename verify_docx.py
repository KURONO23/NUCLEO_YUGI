import os
for path in ["C:/projects/NUCLEO_YUGI/RESUMEN_HISTORIA_COMPLETA.docx", "C:/projects/NUCLEO_YUGI/08_NOVELA/CRONICA_COMPLETA_MAKSU_KURONO.docx"]:
    size = os.path.getsize(path)
    print(f"{path}: {size} bytes")
