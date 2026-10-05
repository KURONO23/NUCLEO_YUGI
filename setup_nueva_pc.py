#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🛠️ INSTALADOR Y SINCRONIZADOR DE ENTORNO — NÚCLEO YUGI (KURONO)
=============================================================================
Este script configura automáticamente cualquier nueva PC para que:
1. Cree la ruta de trabajo libre: C:\\projects
2. Clone o actualice el repositorio oficial de GitHub: KURONO23/NUCLEO_YUGI
3. Configure la identidad de Git (KURONO23)
4. Instale las Reglas de Concesión Territorial (user_global) para que la IA
   actúe de forma autónoma, ágil y sin pedir permisos repetitivos.
5. Verifique el entorno de Python y la base de datos de cartas.
=============================================================================
"""

import os
import sys
import subprocess
from pathlib import Path

# --- CONFIGURACIÓN BASE ---
REPO_URL = "https://github.com/KURONO23/NUCLEO_YUGI.git"
PROJECTS_DIR = Path(r"C:\projects")
YUGI_DIR = PROJECTS_DIR / "NUCLEO_YUGI"
GIT_USER = "KURONO23"
GIT_EMAIL = "kurono23@users.noreply.github.com"

# Texto exacto de la regla de agilidad territorial
RULE_CONTENT = """# Reglas Globales de Seguridad y Ámbito (Harness Territorial)

## 1. Zona de Trabajo Libre (Taller): `C:\\projects`
- Tu área de trabajo principal y autorizada es `C:\\projects` y cualquiera de sus subdirectorios.
- Dentro de `C:\\projects`, procede con total agilidad: crea, edita, refactoriza código y ejecuta herramientas de desarrollo (Python, Node, Git, pruebas, dependencias, etc.) sin interrumpir innecesariamente.

## 2. Zona Protegida (Bóveda / Core / Sistema)
- Las siguientes rutas son **zonas reservadas**:
  - `ChatGPT\\Nucleo` y subcarpetas de ChatGPT.
  - `core_ia` (núcleos de configuración o datos de IA).
  - Rutas de configuración interna del asistente.
  - Directorios raíz del sistema operativo.
- Tienes terminantemente prohibido modificar, sobreescribir o eliminar archivos en estas zonas sin autorización explícita previa del usuario.
"""

def print_step(title):
    print(f"\n{'='*70}\n📌 {title}\n{'='*70}")

def step_1_projects_dir():
    print_step("1. Verificando Zona Libre de Trabajo (C:\\projects)")
    if not PROJECTS_DIR.exists():
        try:
            PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
            print(f"✅ Carpeta creada con éxito: {PROJECTS_DIR}")
        except Exception as e:
            print(f"❌ Error al crear {PROJECTS_DIR}: {e}")
            print("👉 Sugerencia: Ejecuta la consola como Administrador si es necesario.")
    else:
        print(f"✅ Zona Libre existente: {PROJECTS_DIR}")

def step_2_repo_sync():
    print_step("2. Sincronizando Repositorio Oficial desde GitHub")
    if not (YUGI_DIR / ".git").exists():
        print(f"Clonando {REPO_URL} en {YUGI_DIR}...")
        try:
            subprocess.run(["git", "clone", REPO_URL, str(YUGI_DIR)], check=True)
            print("✅ Clonación completada con éxito.")
        except Exception as e:
            print(f"⚠️ No se pudo clonar automáticamente: {e}")
            print(f"👉 Puedes clonarlo manualmente con: git clone {REPO_URL} {YUGI_DIR}")
    else:
        print(f"Repositorio ya presente en {YUGI_DIR}. Actualizando con 'git pull'...")
        try:
            subprocess.run(["git", "-C", str(YUGI_DIR), "pull"], check=True)
            print("✅ Repositorio actualizado a la última versión.")
        except Exception as e:
            print(f"⚠️ Aviso al actualizar: {e}")

def step_3_configure_git():
    print_step("3. Configurando Identidad Local de Git")
    if (YUGI_DIR / ".git").exists():
        try:
            subprocess.run(["git", "-C", str(YUGI_DIR), "config", "user.name", GIT_USER], check=True)
            subprocess.run(["git", "-C", str(YUGI_DIR), "config", "user.email", GIT_EMAIL], check=True)
            print(f"✅ Git configurado localmente: {GIT_USER} <{GIT_EMAIL}>")
        except Exception as e:
            print(f"⚠️ Aviso configurando git: {e}")

def step_4_install_rules():
    print_step("4. Instalando Reglas de Agilidad y Seguridad (Harness Territorial)")
    home = Path.home()
    
    # Destinos estratégicos de reglas (Globales y Locales del Workspace)
    target_locations = [
        home / ".gemini" / "antigravity" / "rules",
        home / ".gemini" / "rules",
        YUGI_DIR / ".gemini" / "rules"
    ]
    
    installed_count = 0
    for folder in target_locations:
        try:
            folder.mkdir(parents=True, exist_ok=True)
            rule_file = folder / "user_global.md"
            with open(rule_file, "w", encoding="utf-8") as f:
                f.write(RULE_CONTENT)
            print(f"✅ Regla instalada en: {rule_file}")
            installed_count += 1
        except Exception as e:
            print(f"⚠️ Aviso en {folder}: {e}")
            
    if installed_count > 0:
        print("\n🎯 Las reglas han quedado activadas. El asistente trabajará con total agilidad en C:\\projects.")

def step_5_verify_environment():
    print_step("5. Verificación de Sistemas del Núcleo")
    print(f"🐍 Python Version: {sys.version.split()[0]}")
    
    state_file = YUGI_DIR / "05_CONTINUIDAD" / "CURRENT_STATE.md"
    if state_file.exists():
        print(f"✅ Archivo de Estado Canónico detectado: {state_file.name}")
    else:
        print(f"⚠️ No se encontró {state_file}")

    audit_file = YUGI_DIR / "04_SISTEMAS" / "AUDITORIA_COMPLETA_13000_CARTAS.md"
    if audit_file.exists():
        print(f"✅ Base de Datos Auditada (13,000 cartas) detectada: {audit_file.name}")
    else:
        print(f"⚠️ No se encontró {audit_file}")

def main():
    print("""
    ===================================================================
     👑 INICIALIZADOR DEL NÚCLEO DE YU-GI-OH! — PROTOCOLO KURONO 👑
    ===================================================================
    """)
    step_1_projects_dir()
    step_2_repo_sync()
    step_3_configure_git()
    step_4_install_rules()
    step_5_verify_environment()
    
    print("\n" + "="*70)
    print("🎉 ¡TODO LISTO! La máquina está configurada con éxito.")
    print("   El asistente de IA ahora trabajará con total agilidad en C:\\projects.")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
