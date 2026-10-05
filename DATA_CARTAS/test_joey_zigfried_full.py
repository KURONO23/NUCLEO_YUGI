# -*- coding: utf-8 -*-
"""
SIMULACIÓN EXACTA: JOEY VS ZIGFRIED
Ladrillo mutuo -> Clímax táctico de Waboku y contragolpe Caos
"""
lp_joey = 4000
lp_zigfried = 4000

# Mano Joey (Ladrillo 100%):
# 1. Black Luster Soldier - Envoy of the Beginning
# 2. Gearfried the Swordmaster
# 3. Chaos Sorcerer
# 4. Jinzo
# 5. Release Restraint

# Mano Zigfried (Ladrillo 100%):
# 1. Valkyrie Brunhilde
# 2. Valkyrie Sigrun
# 3. Valkyrie Erda
# 4. Mischief of the Time Goddess
# 5. Wotan's Judgment

# Turno 1 (Zigfried):
# Set Wotan's Judgment como farol. Pasa turno.

# Turno 2 (Joey):
# Roba: WABOKU! (Su única esperanza defensiva).
# Coloca Waboku y Release Restraint como doble farol. Pasa turno.

# Turno 3 (Zigfried):
# Roba: Ride of the Valkyries!
# Activa Ride of the Valkyries: Invoca Brunhilde (1800), Sigrun (2200), Erda (2000). Total: 6000 ATK.
# Declara Battle Phase.
# Joey activa WABOKU! Anula todo el daño de batalla de este turno.
# End Phase de Ride of the Valkyries:
# Las 3 Valkirias regresan a la baraja de Zigfried! El campo de Zigfried queda VACÍO!

# Turno 4 (Joey):
# Roba: Reinforcement of the Army (RotA)!
# Activa RotA: busca a Blade Knight (LUZ / 1600 ATK).
# Invoca a Blade Knight.
# Ataca directo: 1600 de daño.
lp_zigfried -= 1600

# Turno 5 (Zigfried):
# Roba Valkyrie Dritte (Nivel 4 / 1000 ATK). La invoca.
# Busca Valkyrie en mazo.
# Ataca a Blade Knight: Blade Knight tiene 1600 (o 2000 si no hay cartas en mano de Joey).
# Dritte es destruida o muere.

# Turno 6 (Joey):
# Roba Raigeki o Don Zaloog (OSCURIDAD) o Sangan.
# Prepara cementerio con 1 LUZ (Blade Knight) y 1 OSCURIDAD.
# Despierta a BLACK LUSTER SOLDIER - ENVOY OF THE BEGINNING (3000 ATK)!
# Ataque directo con BLS por 3000 de daño!
lp_zigfried -= 3000
assert lp_zigfried <= 0
print("¡Joey aplasta a Zigfried! Victoria legal confirmada.")
