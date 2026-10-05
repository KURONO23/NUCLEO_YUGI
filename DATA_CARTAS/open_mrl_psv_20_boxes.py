# -*- coding: utf-8 -*-
import random
import os
from collections import Counter

# Semilla reproducible para el gran tiraje de 20 cajas
random.seed(777)

MRL_DATABASE = {
    "Secret Rare": [
        {"name": "Blue-Eyes Toon Dragon", "type": "Monster", "sub": "Toon", "attr": "LIGHT", "lvl": 8, "atk": 3000, "def": 2500, "desc": "Dragón Toon definitivo de Pegasus."},
        {"name": "Serpent Night Dragon", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 7, "atk": 2350, "def": 2400, "desc": "Dragón oscuro del caballero de las sombras."}
    ],
    "Ultra Rare": [
        {"name": "Snatch Steal", "type": "Spell", "sub": "Equip", "desc": "Toma el control permanente de un monstruo del adversario. El adversario gana 1000 LP en cada una de sus Standby Phases."},
        {"name": "Delinquent Duo", "type": "Spell", "sub": "Normal", "desc": "Paga 1000 LP; tu adversario descarta 1 carta al azar y luego selecciona y descarta otra carta de su mano."},
        {"name": "The Forceful Sentry", "type": "Spell", "sub": "Normal", "desc": "Mira la mano de tu adversario, selecciona 1 carta de ella y devuélvela al Deck."},
        {"name": "Confiscation", "type": "Spell", "sub": "Normal", "desc": "Paga 1000 LP; mira la mano de tu adversario, selecciona 1 carta de ella y descártala."},
        {"name": "Relinquished", "type": "Monster", "sub": "Ritual/Effect", "attr": "DARK", "lvl": 1, "atk": 0, "def": 0, "desc": "Absorbe 1 monstruo del adversario como monstruo de equipo y gana su ATK/DEF."},
        {"name": "Black Illusion Ritual", "type": "Spell", "sub": "Ritual", "desc": "Magia de Ritual necesaria para Invocar a Relinquished."},
        {"name": "Spellbinding Circle", "type": "Trap", "sub": "Continuous", "desc": "Selecciona 1 monstruo; no puede atacar ni cambiar de posición, y pierde 700 ATK."},
        {"name": "Axe of Despair", "type": "Spell", "sub": "Equip", "desc": "Aumenta el ATK del monstruo equipado en 1000 puntos."},
        {"name": "Maha Vailo", "type": "Monster", "sub": "Effect", "attr": "LIGHT", "lvl": 4, "atk": 1550, "def": 1400, "desc": "Gana 500 ATK por cada Carta de Equipo equipada a esta carta."},
        {"name": "Toon Summoned Skull", "type": "Monster", "sub": "Toon", "attr": "DARK", "lvl": 6, "atk": 2500, "def": 1200, "desc": "Calavera Convocada versión Toon; ataca directamente si no hay Toons enemigos."}
    ],
    "Super Rare": [
        {"name": "Mystical Space Typhoon", "type": "Spell", "sub": "Quick-Play", "desc": "Selecciona 1 Magia o Trampa en el campo; destrúyela."},
        {"name": "Giant Trunade", "type": "Spell", "sub": "Normal", "desc": "Devuelve al mazo/mano todas las cartas Mágicas y de Trampa en el campo."},
        {"name": "Painful Choice", "type": "Spell", "sub": "Normal", "desc": "Selecciona 5 cartas de tu Deck; tu rival elige 1 para tu mano y las otras 4 van al Cementerio."},
        {"name": "Messenger of Peace", "type": "Spell", "sub": "Continuous", "desc": "Los monstruos con 1500 o más ATK no pueden declarar ataques."},
        {"name": "Megamorph", "type": "Spell", "sub": "Equip", "desc": "Si tus LP son menores, duplica el ATK original del monstruo equipado. Si son mayores, córtalo a la mitad."},
        {"name": "Toon World", "type": "Spell", "sub": "Continuous", "desc": "Paga 1000 LP para activar el mundo de caricaturas."},
        {"name": "Toon Mermaid", "type": "Monster", "sub": "Toon", "attr": "WATER", "lvl": 4, "atk": 1400, "def": 1500, "desc": "Sirena Toon invocable con Toon World."},
        {"name": "Flash Assailant", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 4, "atk": 2000, "def": 2000, "desc": "Pierde 400 ATK/DEF por cada carta en tu mano."}
    ],
    "Rare": [
        {"name": "Cyber Jar", "type": "Monster", "sub": "Flip", "attr": "DARK", "lvl": 3, "atk": 900, "def": 900, "desc": "VOLTEO: Destruye todos los monstruos en el campo. Ambos jugadores revelan las 5 cartas superiores de su Deck e Invocan los monstruos de Nivel 4 o menor."},
        {"name": "Nimble Momonga", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 2, "atk": 1000, "def": 1000, "desc": "Destruido en batalla: gana 1000 LP e Invoca de Modo Especial cualquier número de 'Nimble Momonga' desde tu Deck."},
        {"name": "Gradius", "type": "Monster", "sub": "Normal", "attr": "LIGHT", "lvl": 4, "atk": 1200, "def": 800, "desc": "Una nave espacial de combate legendaria."},
        {"name": "Mystic Tomato", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 4, "atk": 1400, "def": 1100, "desc": "Destruido en batalla: Invoca 1 monstruo de OSCURIDAD con 1500 o menos ATK desde tu Deck."},
        {"name": "Shining Angel", "type": "Monster", "sub": "Effect", "attr": "LIGHT", "lvl": 4, "atk": 1400, "def": 800, "desc": "Destruido en batalla: Invoca 1 monstruo de LUZ con 1500 o menos ATK desde tu Deck."},
        {"name": "Mother Grizzly", "type": "Monster", "sub": "Effect", "attr": "WATER", "lvl": 4, "atk": 1400, "def": 1000, "desc": "Destruido en batalla: Invoca 1 monstruo de AGUA con 1500 o menos ATK desde tu Deck."},
        {"name": "Giant Rat", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 4, "atk": 1400, "def": 1450, "desc": "Destruido en batalla: Invoca 1 monstruo de TIERRA con 1500 o menos ATK desde tu Deck."},
        {"name": "Flying Kamakiri #1", "type": "Monster", "sub": "Effect", "attr": "WIND", "lvl": 4, "atk": 1400, "def": 900, "desc": "Destruido en batalla: Invoca 1 monstruo de VIENTO con 1500 o menos ATK desde tu Deck."},
        {"name": "UFO Turtle", "type": "Monster", "sub": "Effect", "attr": "FIRE", "lvl": 4, "atk": 1400, "def": 1200, "desc": "Destruido en batalla: Invoca 1 monstruo de FUEGO con 1500 o menos ATK desde tu Deck."},
        {"name": "Toll", "type": "Spell", "sub": "Continuous", "desc": "Cualquier jugador debe pagar 500 LP para declarar un ataque."}
    ],
    "Common": [
        {"name": "Sonic Bird", "type": "Monster", "sub": "Effect", "attr": "WIND", "lvl": 4, "atk": 1400, "def": 1000, "desc": "Al ser Invocado: añade 1 Magia de Ritual desde tu Deck a tu mano."},
        {"name": "Senju of the Thousand Hands", "type": "Monster", "sub": "Effect", "attr": "LIGHT", "lvl": 4, "atk": 1400, "def": 1000, "desc": "Al ser Invocado: añade 1 Monstruo de Ritual desde tu Deck a tu mano."},
        {"name": "Upstart Goblin", "type": "Spell", "sub": "Normal", "desc": "Roba 1 carta; tu adversario gana 1000 LP."},
        {"name": "Spear Cretin", "type": "Monster", "sub": "Flip", "attr": "DARK", "lvl": 2, "atk": 500, "def": 500, "desc": "VOLTEO: Al ser mandado al Cementerio, ambos jugadores reviven 1 monstruo."},
        {"name": "Dark Zebra", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 4, "atk": 1800, "def": 400, "desc": "Bestia agresiva con alto ataque."},
        {"name": "Boar Soldier", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 4, "atk": 2000, "def": 500, "desc": "Pierde 1000 ATK al ser Invocado de Modo Normal."},
        {"name": "High Tide Gyojin", "type": "Monster", "sub": "Normal", "attr": "WATER", "lvl": 4, "atk": 1650, "def": 1300, "desc": "Guerrero anfibio de las mareas."},
        {"name": "Ameba", "type": "Monster", "sub": "Effect", "attr": "WATER", "lvl": 1, "atk": 300, "def": 350, "desc": "Inflige 2000 LP si cambia de control al campo rival."}
    ]
}

PSV_DATABASE = {
    "Secret Rare": [
        {"name": "Jinzo", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 6, "atk": 2400, "def": 1500, "desc": "Las Cartas de Trampa, y sus efectos en el campo, no se pueden activar. Niega los efectos de todas las Trampas en el campo."},
        {"name": "Imperial Order", "type": "Trap", "sub": "Continuous", "desc": "Niega todos los efectos de Magia en el campo. Paga 700 LP en cada una de tus Standby Phases para mantenerla."}
    ],
    "Ultra Rare": [
        {"name": "Buster Blader", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 7, "atk": 2600, "def": 2300, "desc": "Gana 500 ATK por cada monstruo Dragón que controle tu adversario o esté en su Cementerio."},
        {"name": "Call of the Haunted", "type": "Trap", "sub": "Continuous", "desc": "Selecciona 1 monstruo en tu Cementerio; Invócalo de Modo Especial en Posición de Ataque."},
        {"name": "Premature Burial", "type": "Spell", "sub": "Equip", "desc": "Paga 800 LP; selecciona 1 monstruo en tu Cementerio; Invócalo de Modo Especial y equípalo con esta carta."},
        {"name": "Ceasefire", "type": "Trap", "sub": "Normal", "desc": "Voltea todos los monstruos boca abajo a boca arriba (sin activar efectos de volteo). Inflige 500 de daño por cada monstruo de efecto en el campo."},
        {"name": "Nobleman of Crossout", "type": "Spell", "sub": "Normal", "desc": "Selecciona 1 monstruo boca abajo en el campo; destrúyelo y destiérralo. Si era un monstruo de Volteo, ambos jugadores destierran todas las copias de sus Decks."},
        {"name": "Nobleman of Extermination", "type": "Spell", "sub": "Normal", "desc": "Selecciona 1 Trampa boca abajo; destrúyela y destiérrala junto a todas las copias de los Decks."},
        {"name": "Gearfried the Iron Knight", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 4, "atk": 1800, "def": 1600, "desc": "Cualquier Carta de Equipo equipada a esta carta es destruida de inmediato."},
        {"name": "The Fiend Megacyber", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 6, "atk": 2200, "def": 1200, "desc": "Si tu adversario controla al menos 2 monstruos más que tú, puedes Invocarlo de Modo Especial desde la mano."},
        {"name": "Beast of Talwar", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 6, "atk": 2400, "def": 2150, "desc": "Un maestro espadachín demonio con imponente poder."},
        {"name": "Mirror Wall", "type": "Trap", "sub": "Continuous", "desc": "Corta a la mitad el ATK de cualquier monstruo del adversario que declare un ataque."}
    ],
    "Super Rare": [
        {"name": "Chain Destruction", "type": "Trap", "sub": "Normal", "desc": "Cuando es Invocado un monstruo con 2000 o menos ATK: destruye todas las copias de ese monstruo en la mano y Deck de su controlador."},
        {"name": "Gravity Bind", "type": "Trap", "sub": "Continuous", "desc": "Todos los monstruos de Nivel 4 o superior no pueden declarar ataques."},
        {"name": "Limiter Removal", "type": "Spell", "sub": "Quick-Play", "desc": "Duplica el ATK de todos los monstruos Máquina que controles actualmente hasta el final del turno."},
        {"name": "Dust Tornado", "type": "Trap", "sub": "Normal", "desc": "Selecciona 1 Magia o Trampa que controle tu adversario; destrúyela, y luego puedes Colocar 1 Trampa desde tu mano."},
        {"name": "Michizure", "type": "Trap", "sub": "Normal", "desc": "Cuando tu monstruo es destruido y mandado al Cementerio: destruye 1 monstruo en el campo."},
        {"name": "Shift", "type": "Trap", "sub": "Normal", "desc": "Redirige el objetivo de una carta mágica o trampa enemiga a otro monstruo válido."},
        {"name": "Appropriate", "type": "Trap", "sub": "Continuous", "desc": "Cada vez que tu adversario robe cartas fuera de su Draw Phase: roba 2 cartas."}
    ],
    "Rare": [
        {"name": "Goblin Attack Force", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 4, "atk": 2300, "def": 0, "desc": "Si esta carta ataca, cambia a Posición de Defensa al final de la Battle Phase, y su posición no se puede cambiar hasta tu próximo turno."},
        {"name": "Hayabusa Knight", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 3, "atk": 1000, "def": 700, "desc": "Esta carta puede hacer un segundo ataque durante cada Battle Phase."},
        {"name": "Cyber Falcon", "type": "Monster", "sub": "Normal", "attr": "WIND", "lvl": 4, "atk": 1400, "def": 1200, "desc": "Un halcón robótico con alas afiladas."},
        {"name": "Seven Tools of the Bandit", "type": "Trap", "sub": "Counter", "desc": "Paga 1000 LP; niega la activación de 1 Carta de Trampa y destrúyela."},
        {"name": "Enchanted Javelin", "type": "Trap", "sub": "Normal", "desc": "Gana LP iguales al ATK del monstruo atacante."},
        {"name": "Prohibition", "type": "Spell", "sub": "Continuous", "desc": "Declara 1 nombre de carta. Esa carta no puede ser jugada ni sus efectos activados."}
    ],
    "Common": [
        {"name": "Mad Dog of Darkness", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 4, "atk": 1900, "def": 1400, "desc": "Un perro furioso con enorme poder ofensivo."},
        {"name": "Solomon's Lawbook", "type": "Trap", "sub": "Normal", "desc": "Sáltate tu próxima Standby Phase."},
        {"name": "Dimension Hole", "type": "Spell", "sub": "Normal", "desc": "Destierra 1 monstruo propio hasta tu próxima Standby Phase."},
        {"name": "Lightforce Sword", "type": "Trap", "sub": "Normal", "desc": "Destierra 1 carta al azar de la mano del adversario, boca abajo, por 3 turnos."},
        {"name": "Goddess with the Third Eye", "type": "Monster", "sub": "Effect", "attr": "LIGHT", "lvl": 4, "atk": 1200, "def": 1000, "desc": "Sustituto de Fusión."},
        {"name": "The Bistro Butcher", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 4, "atk": 1800, "def": 1000, "desc": "Al infligir daño de batalla: tu rival roba 2 cartas."},
        {"name": "Spikebot", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 5, "atk": 1800, "def": 1700, "desc": "Un robot cubierto de púas metálicas."}
    ]
}

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

def open_boxes(db, set_name, count=10):
    all_foils = []
    all_rares = []
    all_commons = []
    for box_idx in range(count):
        for pack_idx in range(24):
            pack = open_pack(db)
            for c, r in pack[:-1]:
                all_commons.append(c["name"])
            rare_slot = pack[-1]
            card_obj, rarity = rare_slot
            if rarity in ["Secret Rare", "Ultra Rare", "Super Rare"]:
                all_foils.append((card_obj["name"], rarity, set_name))
            else:
                all_rares.append((card_obj["name"], rarity, set_name))
    return all_foils, all_rares, all_commons

mrl_foils, mrl_rares, mrl_commons = open_boxes(MRL_DATABASE, "MRL", 10)
psv_foils, psv_rares, psv_commons = open_boxes(PSV_DATABASE, "PSV", 10)

with open("C:/projects/NUCLEO_YUGI/DATA_CARTAS/HITS_MRL_PSV_20_CAJAS.txt", "w", encoding="utf-8") as f:
    f.write("=============================================================================\n")
    f.write("      RESULTADOS OFICIALES DE APERTURA: 10 CAJAS MRL + 10 CAJAS PSV\n")
    f.write("=============================================================================\n\n")
    
    f.write("--- 1. FOILS DE MAGIC RULER (MRL) - 10 CAJAS (240 SOBRES) ---\n")
    mrl_counter = Counter([f"{r}: {name}" for name, r, s in mrl_foils])
    for item, qty in sorted(mrl_counter.items()):
        f.write(f"  [{qty}x] {item}\n")
        
    f.write("\n--- RARES DESTACADAS DE MAGIC RULER (MRL) ---\n")
    mrl_rare_counter = Counter([name for name, r, s in mrl_rares])
    for name in ["Cyber Jar", "Nimble Momonga", "Mystic Tomato", "Shining Angel", "Giant Rat"]:
        if name in mrl_rare_counter:
            f.write(f"  [{mrl_rare_counter[name]}x] {name} (Rare Clave)\n")

    f.write("\n-----------------------------------------------------------------------------\n")
    f.write("--- 2. FOILS DE PHARAOH'S SERVANT (PSV) - 10 CAJAS (240 SOBRES) ---\n")
    psv_counter = Counter([f"{r}: {name}" for name, r, s in psv_foils])
    for item, qty in sorted(psv_counter.items()):
        f.write(f"  [{qty}x] {item}\n")
        
    f.write("\n--- RARES DESTACADAS DE PHARAOH'S SERVANT (PSV) ---\n")
    psv_rare_counter = Counter([name for name, r, s in psv_rares])
    for name in ["Goblin Attack Force", "Hayabusa Knight", "Prohibition", "Seven Tools of the Bandit"]:
        if name in psv_rare_counter:
            f.write(f"  [{psv_rare_counter[name]}x] {name} (Rare Clave)\n")
            
print("Tiraje de 20 cajas completado con éxito. Archivo de reporte generado.")
