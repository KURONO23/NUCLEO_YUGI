# Base de datos canónica de cartas para LOB y MRD
# REGLA DE ORO CANÓNICA: Blue-Eyes White Dragon está EXCLUIDO del pool comercial (solo existen 4 en el lore de DM y 3 son de Kaiba).

LOB_DATABASE = {
    "Secret Rare": [
        {"name": "Tri-Horned Dragon", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 8, "atk": 2850, "def": 2350, "desc": "Un dragón indigno de confianza con tres cuernos afilados."},
        {"name": "Gaia the Dragon Champion", "type": "Monster", "sub": "Fusion", "attr": "WIND", "lvl": 7, "atk": 2600, "def": 2100, "desc": "Gaia The Fierce Knight + Curse of Dragon"}
    ],
    "Ultra Rare": [
        # Blue-Eyes EXCLUIDO por mandato canónico.
        {"name": "Dark Magician", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 7, "atk": 2500, "def": 2100, "desc": "El mago definitivo en términos de ataque y defensa."},
        {"name": "Red-Eyes B. Dragon", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 7, "atk": 2400, "def": 2000, "desc": "Un dragón feroz con un ataque letal."},
        {"name": "Exodia the Forbidden One", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 3, "atk": 1000, "def": 1000, "desc": "Si tienes las 5 piezas en la mano, ganas el duelo automáticamente."},
        {"name": "Gaia The Fierce Knight", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 7, "atk": 2300, "def": 2100, "desc": "Un caballero cuyo caballo corre más rápido que el viento."},
        {"name": "Monster Reborn", "type": "Spell", "sub": "Normal", "desc": "Selecciona 1 monstruo en cualquier Cementerio; Invócalo de Modo Especial a tu campo."},
        {"name": "Raigeki", "type": "Spell", "sub": "Normal", "desc": "Destruye todos los monstruos que controle tu adversario."},
        {"name": "Dark Hole", "type": "Spell", "sub": "Normal", "desc": "Destruye todos los monstruos en el campo."},
        {"name": "Polymerization", "type": "Spell", "sub": "Normal", "desc": "Manda al Cementerio Materiales de Fusión listados en tu mano o campo, e Invoca de Modo Especial ese Monstruo de Fusión."},
        {"name": "Swords of Revealing Light", "type": "Spell", "sub": "Normal", "desc": "Los monstruos del adversario no pueden declarar ataques durante 3 turnos. Voltea todos sus monstruos boca arriba."}
    ],
    "Super Rare": [
        {"name": "Right Arm of the Forbidden One", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 1, "atk": 200, "def": 300, "desc": "Brazo derecho sellado."},
        {"name": "Left Arm of the Forbidden One", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 1, "atk": 200, "def": 300, "desc": "Brazo izquierdo sellado."},
        {"name": "Right Leg of the Forbidden One", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 1, "atk": 200, "def": 300, "desc": "Pierna derecha sellada."},
        {"name": "Left Leg of the Forbidden One", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 1, "atk": 200, "def": 300, "desc": "Pierna izquierda sellada."},
        {"name": "Celtic Guardian", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 4, "atk": 1400, "def": 1200, "desc": "Un elfo guerrero que blande una espada plateada."},
        {"name": "Curse of Dragon", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 5, "atk": 2000, "def": 1500, "desc": "Un dragón maligno con poderosos ataques de fuego."},
        {"name": "Flame Swordsman", "type": "Monster", "sub": "Fusion", "attr": "FIRE", "lvl": 5, "atk": 1800, "def": 1600, "desc": "Flame Manipulator + Masaki the Legendary Swordsman"},
        {"name": "Trap Hole", "type": "Trap", "sub": "Normal", "desc": "Cuando tu adversario Invoca de Modo Normal o por Volteo un monstruo con 1000 ATK o más: selecciona ese monstruo; destrúyelo."},
        {"name": "Pot of Greed", "type": "Spell", "sub": "Normal", "desc": "Roba 2 cartas de tu Deck."},
        {"name": "Fissure", "type": "Spell", "sub": "Normal", "desc": "Destruye 1 monstruo boca arriba con el menor ATK en el campo de tu adversario."},
        {"name": "Man-Eater Bug", "type": "Monster", "sub": "Flip", "attr": "EARTH", "lvl": 2, "atk": 450, "def": 600, "desc": "VOLTEO: Selecciona 1 monstruo en el campo; destrúyelo."}
    ],
    "Rare": [
        {"name": "Mystical Elf", "type": "Monster", "sub": "Normal", "attr": "LIGHT", "lvl": 4, "atk": 800, "def": 2000, "desc": "Una elfa que canta cánticos de protección divina."},
        {"name": "Giant Soldier of Stone", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 3, "atk": 1300, "def": 2000, "desc": "Un guerrero de roca maciza con gran defensa."},
        {"name": "Silver Fang", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 3, "atk": 1200, "def": 800, "desc": "Un lobo de pelo blanco y colmillos brillantes."},
        {"name": "Beaver Warrior", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 4, "atk": 1200, "def": 1500, "desc": "Un castor que domina la espada y el escudo."},
        {"name": "Stop Defense", "type": "Spell", "sub": "Normal", "desc": "Cambia 1 monstruo en defensa del adversario a posición de ataque."},
        {"name": "Remove Trap", "type": "Spell", "sub": "Normal", "desc": "Destruye 1 trampa boca arriba en el campo."},
        {"name": "Dragon Capture Jar", "type": "Trap", "sub": "Continuous", "desc": "Todos los monstruos Dragón se cambian a Posición de Defensa."},
        {"name": "Two-Pronged Attack", "type": "Trap", "sub": "Normal", "desc": "Destruye 2 monstruos propios para destruir 1 monstruo del adversario."},
        {"name": "Mountain", "type": "Spell", "sub": "Field", "desc": "Aumenta ATK/DEF de Dragón, Bestia Alada y Trueno en 200."},
        {"name": "Sogen", "type": "Spell", "sub": "Field", "desc": "Aumenta ATK/DEF de Guerrero y Bestia-Guerrero en 200."},
        {"name": "Umi", "type": "Spell", "sub": "Field", "desc": "Aumenta ATK/DEF de Pez, Serpiente Marina, Trueno y Aqua en 200."},
        {"name": "Yami", "type": "Spell", "sub": "Field", "desc": "Aumenta ATK/DEF de Lanzador de Conjuros y Demonio en 200."},
        {"name": "Wasteland", "type": "Spell", "sub": "Field", "desc": "Aumenta ATK/DEF de Dinosaurio, Zombi y Roca en 200."},
        {"name": "Forest", "type": "Spell", "sub": "Field", "desc": "Aumenta ATK/DEF de Insecto, Bestia, Planta y Bestia-Guerrero en 200."},
        {"name": "Dragon Treasure", "type": "Spell", "sub": "Equip", "desc": "Equipa a Dragón. +300 ATK/DEF."},
        {"name": "Sword of Dark Destruction", "type": "Spell", "sub": "Equip", "desc": "Equipa a Oscuridad. +400 ATK, -200 DEF."}
    ],
    "Common": [
        {"name": "Uraby", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 4, "atk": 1500, "def": 800, "desc": "Un dinosaurio veloz con garras implacables."},
        {"name": "Mammoth Graveyard", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 3, "atk": 1200, "def": 800, "desc": "Un mamut que custodia los restos de sus ancestros."},
        {"name": "Hitotsu-Me Giant", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 4, "atk": 1200, "def": 1000, "desc": "Un gigante cíclope con gruesa masa muscular."},
        {"name": "Skull Servant", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 1, "atk": 300, "def": 200, "desc": "Un esqueleto andante que se deshace al menor golpe."},
        {"name": "Basic Insect", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 2, "atk": 500, "def": 700, "desc": "Un escarabajo común que viaja en enjambre."},
        {"name": "Armored Lizard", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 4, "atk": 1500, "def": 1200, "desc": "Un reptil acorazado con piel dura como el metal."},
        {"name": "Petite Dragon", "type": "Monster", "sub": "Normal", "attr": "WIND", "lvl": 2, "atk": 600, "def": 700, "desc": "Un dragón pequeño y juguetón."},
        {"name": "Dark Gray", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 3, "atk": 800, "def": 900, "desc": "Una bestia peluda con aspecto fiero."},
        {"name": "Nemuriko", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 3, "atk": 800, "def": 700, "desc": "Un pequeño demonio infantil."},
        {"name": "Hard-Armor", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 3, "atk": 300, "def": 1200, "desc": "Un guerrero protegido por una pesada armadura."},
        {"name": "Kagemusha of the Blue Flame", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 2, "atk": 800, "def": 400, "desc": "El doble del señor samurái."},
        {"name": "Meda Bat", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 2, "atk": 800, "def": 400, "desc": "Un murciélago sombrío con ojos saltones."},
        {"name": "Skull Red Bird", "type": "Monster", "sub": "Normal", "attr": "WIND", "lvl": 4, "atk": 1550, "def": 1200, "desc": "Un ave rojiza monstruosa."},
        {"name": "Firegrass", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 2, "atk": 700, "def": 600, "desc": "Hierba seca que arde espontáneamente."},
        {"name": "Sparks", "type": "Spell", "sub": "Normal", "desc": "Inflige 50 de daño a los LP del adversario."},
        {"name": "Hinotama", "type": "Spell", "sub": "Normal", "desc": "Inflige 500 de daño a los LP del adversario."},
        {"name": "Final Flame", "type": "Spell", "sub": "Normal", "desc": "Inflige 600 de daño a los LP del adversario."}
    ]
}

MRD_DATABASE = {
    "Secret Rare": [
        {"name": "Gate Guardian", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 11, "atk": 3750, "def": 3400, "desc": "Solo puede ser Invocado Especialmente tributando a Sanga of the Thunder, Kazejin y Suijin."},
        {"name": "Thousand Dragon", "type": "Monster", "sub": "Fusion", "attr": "WIND", "lvl": 7, "atk": 2400, "def": 2000, "desc": "Time Wizard + Baby Dragon"}
    ],
    "Ultra Rare": [
        {"name": "Mirror Force", "type": "Trap", "sub": "Normal", "desc": "Cuando un monstruo del adversario declara un ataque: destruye todos los monstruos en Posición de Ataque que controle tu adversario."},
        {"name": "Solemn Judgment", "type": "Trap", "sub": "Counter", "desc": "Paga la mitad de tus LP: Niega la Invocación de un monstruo O la activación de una Carta Mágica/Trampa y destrúyela."},
        {"name": "Heavy Storm", "type": "Spell", "sub": "Normal", "desc": "Destruye todas las Cartas Mágicas y de Trampa en el campo."},
        {"name": "Change of Heart", "type": "Spell", "sub": "Normal", "desc": "Toma el control de 1 monstruo que controle tu adversario hasta la End Phase."},
        {"name": "Summoned Skull", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 6, "atk": 2500, "def": 1200, "desc": "Un demonio con poderes oscuros para confundir al enemigo."},
        {"name": "Time Wizard", "type": "Monster", "sub": "Effect", "attr": "LIGHT", "lvl": 2, "atk": 500, "def": 400, "desc": "Gira la ruleta: Si aciertas destruyes todos los monstruos del adversario; si fallas destruyes los tuyos y recibes daño."},
        {"name": "Tribute to The Doomed", "type": "Spell", "sub": "Normal", "desc": "Descarta 1 carta de tu mano: destruye 1 monstruo en el campo."},
        {"name": "Barrel Dragon", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 7, "atk": 2600, "def": 2200, "desc": "Lanza 3 monedas: si 2 o más caen cara, destruye 1 monstruo en el campo."},
        {"name": "Harpie Lady Sisters", "type": "Monster", "sub": "Effect", "attr": "WIND", "lvl": 6, "atk": 1950, "def": 2100, "desc": "Solo puede ser Invocada Especialmente con Elegant Egotist."},
        {"name": "B. Skull Dragon", "type": "Monster", "sub": "Fusion", "attr": "DARK", "lvl": 9, "atk": 3200, "def": 2500, "desc": "Summoned Skull + Red-Eyes B. Dragon"}
    ],
    "Super Rare": [
        {"name": "Sangan", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 3, "atk": 1000, "def": 600, "desc": "Si esta carta es enviada del campo al Cementerio: añade a tu mano 1 monstruo con 1500 ATK o menos en tu Deck."},
        {"name": "Witch of the Black Forest", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 4, "atk": 1100, "def": 1200, "desc": "Si esta carta es enviada del campo al Cementerio: añade a tu mano 1 monstruo con 1500 DEF o menos en tu Deck."},
        {"name": "Magician of Faith", "type": "Monster", "sub": "Flip", "attr": "LIGHT", "lvl": 1, "atk": 300, "def": 400, "desc": "VOLTEO: Selecciona 1 Carta Mágica en tu Cementerio; añádela a tu mano."},
        {"name": "Seven Tools of the Bandit", "type": "Trap", "sub": "Counter", "desc": "Paga 1000 LP: Niega la activación de una Carta de Trampa y destrúyela."},
        {"name": "Magic Jammer", "type": "Trap", "sub": "Counter", "desc": "Descarta 1 carta: Niega la activación de una Carta Mágica y destrúyela."},
        {"name": "Kuriboh", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 1, "atk": 300, "def": 200, "desc": "Durante el cálculo de daño, descarta esta carta: el daño de batalla recibido se reduce a 0."},
        {"name": "Robbin' Goblin", "type": "Trap", "sub": "Continuous", "desc": "Cada vez que un monstruo propio inflige daño de batalla al adversario, el adversario descarta 1 carta al azar de su mano."},
        {"name": "Mask of Darkness", "type": "Monster", "sub": "Flip", "attr": "DARK", "lvl": 2, "atk": 900, "def": 400, "desc": "VOLTEO: Selecciona 1 Carta de Trampa en tu Cementerio; añádela a tu mano."},
        {"name": "Catapult Turtle", "type": "Monster", "sub": "Effect", "attr": "WATER", "lvl": 5, "atk": 1000, "def": 2000, "desc": "Tributa 1 monstruo: inflige daño al adversario igual a la mitad del ATK del monstruo tributado."}
    ],
    "Rare": [
        {"name": "White Magical Hat", "type": "Monster", "sub": "Effect", "attr": "LIGHT", "lvl": 3, "atk": 1000, "def": 700, "desc": "Cuando inflige daño de batalla al adversario: descarta 1 carta al azar de su mano."},
        {"name": "Cannon Soldier", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 4, "atk": 1400, "def": 1300, "desc": "Tributa 1 monstruo: inflige 500 de daño al adversario."},
        {"name": "Jirai Gumo", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 4, "atk": 2200, "def": 100, "desc": "Cuando declara un ataque: lanza una moneda. Si fallas, pierdes la mitad de tus LP."},
        {"name": "Princess of Tsurugi", "type": "Monster", "sub": "Flip", "attr": "WIND", "lvl": 3, "atk": 900, "def": 700, "desc": "VOLTEO: Inflige 500 de daño al adversario por cada Mágica/Trampa que controle."},
        {"name": "Just Desserts", "type": "Trap", "sub": "Normal", "desc": "Inflige 500 de daño a tu adversario por cada monstruo que controle."},
        {"name": "Tremendous Fire", "type": "Spell", "sub": "Normal", "desc": "Inflige 1000 de daño al adversario y 500 de daño a ti mismo."},
        {"name": "Share the Pain", "type": "Spell", "sub": "Normal", "desc": "Tributa 1 monstruo propio; tu adversario debe tributar 1 monstruo suyo."},
        {"name": "Wall of Illusion", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 4, "atk": 1000, "def": 1850, "desc": "Si esta carta es atacada por un monstruo, después del cálculo de daño devuelve ese monstruo a la mano de su dueño."},
        {"name": "Waboku", "type": "Trap", "sub": "Normal", "desc": "Cualquier daño infligido por los monstruos del adversario este turno se convierte en 0. Tus monstruos no pueden ser destruidos en batalla este turno."},
        {"name": "Block Attack", "type": "Spell", "sub": "Normal", "desc": "Cambia 1 monstruo en ataque del adversario a posición de defensa boca arriba."},
        {"name": "Soul of the Pure", "type": "Spell", "sub": "Normal", "desc": "Aumenta tus LP en 800."}
    ],
    "Common": [
        {"name": "7 Colored Fish", "type": "Monster", "sub": "Normal", "attr": "WATER", "lvl": 4, "atk": 1800, "def": 800, "desc": "Un pez arcoíris con un ataque tremendo."},
        {"name": "Harpie Lady", "type": "Monster", "sub": "Normal", "attr": "WIND", "lvl": 4, "atk": 1300, "def": 1400, "desc": "Una mujer alada de aspecto fiero y garras letales."},
        {"name": "Whiptail Crow", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 4, "atk": 1650, "def": 1600, "desc": "Un cuervo con cola en forma de látigo y gran fuerza."},
        {"name": "Ancient Lizard Warrior", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 4, "atk": 1400, "def": 1100, "desc": "Un lagarto guerrero que sobrevivió desde eras arcaicas."},
        {"name": "Crawling Dragon #2", "type": "Monster", "sub": "Normal", "attr": "FIRE", "lvl": 4, "atk": 1600, "def": 1200, "desc": "Un dragón de fuego que repta por el suelo calcinándolo todo."},
        {"name": "Ryu-Kishin Powered", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 4, "atk": 1600, "def": 1200, "desc": "Una gárgola fortalecida con magia oscura."},
        {"name": "Armored Zombie", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 3, "atk": 1500, "def": 0, "desc": "Un guerrero zombi protegido con armadura."},
        {"name": "The Bistro Butcher", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 4, "atk": 1600, "def": 1200, "desc": "Cuando inflige daño de batalla, el rival roba 2 cartas."},
        {"name": "Trap Master", "type": "Monster", "sub": "Flip", "attr": "EARTH", "lvl": 3, "atk": 500, "def": 1100, "desc": "VOLTEO: Destruye 1 trampa en el campo."},
        {"name": "Cocoon of Evolution", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 3, "atk": 0, "def": 2000, "desc": "Un capullo de defensa impenetrable."},
        {"name": "Petit Moth", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 1, "atk": 300, "def": 200, "desc": "Una pequeña oruga indefensa."},
        {"name": "Bottom Dweller", "type": "Monster", "sub": "Normal", "attr": "WATER", "lvl": 5, "atk": 1650, "def": 1700, "desc": "Una criatura acuática de las profundidades."},
        {"name": "Fake Trap", "type": "Trap", "sub": "Normal", "desc": "Si una trampa propia fuera a ser destruida, destruye esta carta en su lugar."}
    ]
}


MRL_DATABASE = {
    "Secret Rare": [
        {"name": "Blue-Eyes Toon Dragon", "type": "Monster", "sub": "Toon", "attr": "LIGHT", "lvl": 8, "atk": 3000, "def": 2500, "desc": "Dragón Toon legendario."},
        {"name": "Serpent Night Dragon", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 7, "atk": 2350, "def": 2400, "desc": "Un dragón oscuro creado por un caballero malvado."}
    ],
    "Ultra Rare": [
        {"name": "Snatch Steal", "type": "Spell", "sub": "Equip", "desc": "Toma el control de 1 monstruo del adversario. Durante cada una de sus Standby Phases, tu adversario gana 1000 LP."},
        {"name": "Delinquent Duo", "type": "Spell", "sub": "Normal", "desc": "Paga 1000 LP: tu adversario descarta 1 carta al azar de su mano y luego descarta otra carta a su elección."},
        {"name": "The Forceful Sentry", "type": "Spell", "sub": "Normal", "desc": "Mira la mano de tu adversario, selecciona 1 carta en ella y devuélvela a su Deck."},
        {"name": "Confiscation", "type": "Spell", "sub": "Normal", "desc": "Paga 1000 LP: mira la mano de tu adversario, selecciona 1 carta en ella y mándala al Cementerio."},
        {"name": "Relinquished", "type": "Monster", "sub": "Ritual", "attr": "DARK", "lvl": 1, "atk": 0, "def": 0, "desc": "Una vez por turno: equipa 1 monstruo del adversario a esta carta. Gana su ATK/DEF."},
        {"name": "Black Illusion Ritual", "type": "Spell", "sub": "Ritual", "desc": "Usada para Invocar por Ritual a Relinquished."},
        {"name": "Axe of Despair", "type": "Spell", "sub": "Equip", "desc": "Equipa a un monstruo: gana 1000 ATK."},
        {"name": "Maha Vailo", "type": "Monster", "sub": "Effect", "attr": "LIGHT", "lvl": 4, "atk": 1550, "def": 1400, "desc": "Gana 500 ATK por cada Carta de Equipo equipada a esta carta."},
        {"name": "Spellbinding Circle", "type": "Trap", "sub": "Continuous", "desc": "Selecciona 1 monstruo del adversario: no puede atacar ni cambiar su posición de batalla. Pierde 700 ATK."},
        {"name": "Toon Summoned Skull", "type": "Monster", "sub": "Toon", "attr": "DARK", "lvl": 6, "atk": 2500, "def": 1200, "desc": "Versión Toon de Summoned Skull."}
    ],
    "Super Rare": [
        {"name": "Mystical Space Typhoon", "type": "Spell", "sub": "Quick-Play", "desc": "Selecciona 1 Carta Mágica/Trampa en el campo; destrúyela."},
        {"name": "Giant Trunade", "type": "Spell", "sub": "Normal", "desc": "Devuelve a la mano todas las Cartas Mágicas y de Trampa en el campo."},
        {"name": "Painful Choice", "type": "Spell", "sub": "Normal", "desc": "Selecciona 5 cartas de tu Deck y muéstralas a tu adversario. Tu adversario elige 1 para tu mano y manda el resto al Cementerio."},
        {"name": "Messenger of Peace", "type": "Spell", "sub": "Continuous", "desc": "Ningún monstruo con 1500 ATK o más puede declarar un ataque. Paga 100 LP en cada Standby Phase para mantenerla."},
        {"name": "Megamorph", "type": "Spell", "sub": "Equip", "desc": "Si tus LP son menores que los de tu adversario, el ATK original del monstruo equipado se duplica."},
        {"name": "Cyber Jar", "type": "Monster", "sub": "Flip", "attr": "DARK", "lvl": 3, "atk": 900, "def": 900, "desc": "VOLTEO: Destruye todos los monstruos en el campo. Ambos jugadores revelan las 5 cartas superiores de su Deck e Invocan de Modo Especial todos los monstruos de Nivel 4 o menor."},
        {"name": "Toon World", "type": "Spell", "sub": "Continuous", "desc": "Paga 1000 LP para activar esta carta."},
        {"name": "Toll", "type": "Spell", "sub": "Continuous", "desc": "Cada jugador debe pagar 500 LP para declarar un ataque."},
        {"name": "Banisher of the Light", "type": "Monster", "sub": "Effect", "attr": "LIGHT", "lvl": 3, "atk": 100, "def": 2000, "desc": "Cualquier carta mandada al Cementerio es desterrada en su lugar."},
        {"name": "Gradius", "type": "Monster", "sub": "Normal", "attr": "LIGHT", "lvl": 4, "atk": 1200, "def": 800, "desc": "Una nave espacial de alta tecnología."}
    ],
    "Rare": [
        {"name": "Nimble Momonga", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 2, "atk": 1000, "def": 100, "desc": "Si es destruida en batalla: gana 1000 LP e Invoca de Modo Especial cualquier número de Nimble Momonga de tu Deck."},
        {"name": "Upstart Goblin", "type": "Spell", "sub": "Normal", "desc": "Roba 1 carta de tu Deck; tu adversario gana 1000 LP."},
        {"name": "Sonic Bird", "type": "Monster", "sub": "Effect", "attr": "WIND", "lvl": 4, "atk": 1400, "def": 1000, "desc": "Cuando es Invocada de Modo Normal: añade 1 Carta Mágica de Ritual de tu Deck a tu mano."},
        {"name": "Senju of the Thousand Hands", "type": "Monster", "sub": "Effect", "attr": "LIGHT", "lvl": 4, "atk": 1400, "def": 1000, "desc": "Cuando es Invocado de Modo Normal: añade 1 Monstruo de Ritual de tu Deck a tu mano."},
        {"name": "Shining Angel", "type": "Monster", "sub": "Effect", "attr": "LIGHT", "lvl": 4, "atk": 1400, "def": 800, "desc": "Si es destruido en batalla: Invoca de Modo Especial 1 monstruo de LUZ con 1500 ATK o menos de tu Deck."},
        {"name": "Mystic Tomato", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 4, "atk": 1400, "def": 1100, "desc": "Si es destruido en batalla: Invoca de Modo Especial 1 monstruo de OSCURIDAD con 1500 ATK o menos de tu Deck."},
        {"name": "Giant Rat", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 4, "atk": 1400, "def": 1450, "desc": "Si es destruido en batalla: Invoca de Modo Especial 1 monstruo de TIERRA con 1500 ATK o menos de tu Deck."},
        {"name": "Mother Grizzly", "type": "Monster", "sub": "Effect", "attr": "WATER", "lvl": 4, "atk": 1400, "def": 1000, "desc": "Si es destruido en batalla: Invoca de Modo Especial 1 monstruo de AGUA con 1500 ATK o menos de tu Deck."},
        {"name": "Flying Kamakiri #1", "type": "Monster", "sub": "Effect", "attr": "WIND", "lvl": 4, "atk": 1400, "def": 900, "desc": "Si es destruido en batalla: Invoca de Modo Especial 1 monstruo de VIENTO con 1500 ATK o menos de tu Deck."},
        {"name": "UFO Turtle", "type": "Monster", "sub": "Effect", "attr": "FIRE", "lvl": 4, "atk": 1400, "def": 1200, "desc": "Si es destruido en batalla: Invoca de Modo Especial 1 monstruo de FUEGO con 1500 ATK o menos de tu Deck."}
    ],
    "Common": [
        {"name": "Kotodama", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 3, "atk": 0, "def": 1600, "desc": "Monstruos con el mismo nombre no pueden existir boca arriba en el campo."},
        {"name": "Giant Germ", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 2, "atk": 1000, "def": 100, "desc": "Si esta carta es destruida en batalla y enviada al Cementerio: inflige 500 de daño al adversario, y luego puedes Invocar de Modo Especial cualquier número de 'Giant Germ' de tu Deck en Posición de Ataque boca arriba."},
        {"name": "Tailor of the Fickle", "type": "Spell", "sub": "Quick-Play", "desc": "Cambia 1 Carta de Equipo a otro blanco correcto."},
        {"name": "Rush Recklessly", "type": "Spell", "sub": "Quick-Play", "desc": "Aumenta el ATK de 1 monstruo boca arriba en 700 hasta el final del turno."},
        {"name": "The Cheerful Coffin", "type": "Spell", "sub": "Normal", "desc": "Descarta hasta 3 cartas de monstruo de tu mano al Cementerio."}
    ]
}

PSV_DATABASE = {
    "Secret Rare": [
        {"name": "Jinzo", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 6, "atk": 2400, "def": 1500, "desc": "Las Cartas de Trampa no pueden ser activadas. Los efectos de todas las Cartas de Trampa en el campo se niegan."},
        {"name": "Imperial Order", "type": "Trap", "sub": "Continuous", "desc": "Niega todos los efectos de Cartas Mágicas en el campo. Paga 700 LP en cada Standby Phase para mantenerla activa."}
    ],
    "Ultra Rare": [
        {"name": "Buster Blader", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 7, "atk": 2600, "def": 2300, "desc": "Gana 500 ATK por cada monstruo Dragón que tu adversario controle o esté en su Cementerio."},
        {"name": "Call of the Haunted", "type": "Trap", "sub": "Continuous", "desc": "Selecciona 1 monstruo en tu Cementerio; Invócalo de Modo Especial en Posición de Ataque."},
        {"name": "Premature Burial", "type": "Spell", "sub": "Equip", "desc": "Paga 800 LP: selecciona 1 monstruo en tu Cementerio; Invócalo de Modo Especial boca arriba en Posición de Ataque y equípalo con esta carta."},
        {"name": "Nobleman of Crossout", "type": "Spell", "sub": "Normal", "desc": "Destruye 1 monstruo en Posición de Defensa boca abajo y destiérralo. Si era de Volteo, ambos jugadores destierran todas las copias de sus Decks."},
        {"name": "Gearfried the Iron Knight", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 4, "atk": 1800, "def": 1600, "desc": "Si una Carta de Equipo es equipada a esta carta: destrúyela de inmediato."},
        {"name": "The Fiend Megacyber", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 6, "atk": 2200, "def": 1200, "desc": "Si tu adversario controla al menos 2 monstruos más que tú, puedes Invocar esta carta de Modo Especial desde tu mano."},
        {"name": "Beast of Talwar", "type": "Monster", "sub": "Normal", "attr": "DARK", "lvl": 6, "atk": 2400, "def": 2150, "desc": "Solo requiere 1 Tributo: un demonio espadachín con poder colosal."},
        {"name": "Ceasefire", "type": "Trap", "sub": "Normal", "desc": "Cambia todos los monstruos boca abajo a Posición de Defensa boca arriba (no se activan Volteos). Inflige 500 de daño al rival por cada Monstruo de Efecto en el campo."}
    ],
    "Super Rare": [
        {"name": "Gravity Bind", "type": "Trap", "sub": "Continuous", "desc": "Los monstruos de Nivel 4 o superior no pueden declarar ataques."},
        {"name": "Hayabusa Knight", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 3, "atk": 1000, "def": 700, "desc": "Esta carta puede realizar un segundo ataque durante cada Battle Phase."},
        {"name": "Goblin Attack Force", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 4, "atk": 2300, "def": 0, "desc": "Si ataca, cambia a Posición de Defensa al final de la Battle Phase y no puede cambiar de posición hasta el final de tu próximo turno."},
        {"name": "Limiter Removal", "type": "Spell", "sub": "Quick-Play", "desc": "Duplica el ATK de todos los monstruos Máquina en tu campo hasta el final del turno. Se destruyen en la End Phase."},
        {"name": "Mirror Wall", "type": "Trap", "sub": "Continuous", "desc": "El ATK de los monstruos atacantes del adversario se corta a la mitad. Paga 2000 LP en cada Standby Phase para mantenerla."},
        {"name": "Enchanted Javelin", "type": "Trap", "sub": "Normal", "desc": "Cuando un monstruo rival ataca: gana LP iguales al ATK del monstruo atacante."}
    ],
    "Rare": [
        {"name": "Morphing Jar #2", "type": "Monster", "sub": "Flip", "attr": "EARTH", "lvl": 3, "atk": 800, "def": 700, "desc": "VOLTEO: Baraja todos los monstruos en los Decks y excava hasta Invocar monstruos de Nivel 4 o menor."},
        {"name": "Prohibition", "type": "Spell", "sub": "Continuous", "desc": "Declara 1 nombre de carta. Mientras esta carta permanezca en el campo, esa carta no puede ser jugada."},
        {"name": "Lightforce Sword", "type": "Trap", "sub": "Normal", "desc": "Destierra 1 carta al azar de la mano de tu adversario boca abajo por 3 turnos."},
        {"name": "Appropriate", "type": "Trap", "sub": "Continuous", "desc": "Cada vez que tu adversario robe cartas fuera de su Draw Phase: roba 2 cartas."},
        {"name": "Major Riot", "type": "Trap", "sub": "Normal", "desc": "Cuando 1 monstruo vuelve a la mano: ambos jugadores pueden Invocar de Modo Especial monstruos de Nivel 4 o menor desde la mano en defensa boca abajo."}
    ],
    "Common": [
        {"name": "7 Completed", "type": "Spell", "sub": "Equip", "desc": "Equipa solo a una Máquina. +700 ATK o +700 DEF."},
        {"name": "DNA Surgery", "type": "Trap", "sub": "Continuous", "desc": "Declara 1 Tipo de monstruo. Todos los monstruos boca arriba en el campo se convierten en ese Tipo."},
        {"name": "Attack and Receive", "type": "Trap", "sub": "Normal", "desc": "Cuando recibes daño de batalla o efecto: inflige 700 de daño al adversario más 300 por cada copia en el Cementerio."}
    ]
}

LON_DATABASE = {
    "Secret Rare": [
        {"name": "Gemini Elf", "type": "Monster", "sub": "Normal", "attr": "EARTH", "lvl": 4, "atk": 1900, "def": 900, "desc": "Elfas gemelas que alternan sus ataques. La cúspide de 1900 ATK en Nivel 4."},
        {"name": "Magic Cylinder", "type": "Trap", "sub": "Normal", "desc": "Cuando un monstruo del adversario declara un ataque: selecciona ese monstruo; niega el ataque y, si lo haces, inflige daño a tu adversario igual a su ATK."}
    ],
    "Ultra Rare": [
        {"name": "Torrential Tribute", "type": "Trap", "sub": "Normal", "desc": "Cuando uno o más monstruos son Invocados: destruye todos los monstruos en el campo."},
        {"name": "United We Stand", "type": "Spell", "sub": "Equip", "desc": "El monstruo equipado gana 800 ATK/DEF por cada monstruo boca arriba que controles."},
        {"name": "Mage Power", "type": "Spell", "sub": "Equip", "desc": "El monstruo equipado gana 500 ATK/DEF por cada Carta Mágica/Trampa que controles."},
        {"name": "Dark Necrofear", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 8, "atk": 2200, "def": 2800, "desc": "Destierra 3 Demonios de tu Cementerio para Invocarla. Al morir, toma el control de un monstruo rival en la End Phase."},
        {"name": "Destiny Board", "type": "Trap", "sub": "Continuous", "desc": "Si completas el mensaje F-I-N-A-L en tu zona de Magias/Trampas, ganas el duelo automáticamente."},
        {"name": "Mask of Restrict", "type": "Trap", "sub": "Continuous", "desc": "Ningún jugador puede tributar cartas bajo ninguna circunstancia."},
        {"name": "Card of Safe Return", "type": "Spell", "sub": "Continuous", "desc": "Cada vez que un monstruo sea Invocado de Modo Especial desde tu Cementerio: roba 1 carta."},
        {"name": "Spiritualism", "type": "Spell", "sub": "Normal", "desc": "Devuelve 1 Carta Mágica o de Trampa que controle tu adversario a la mano. La activación y efecto de esta carta no pueden ser negados."}
    ],
    "Super Rare": [
        {"name": "Kycoo the Ghost Destroyer", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 4, "atk": 1800, "def": 700, "desc": "Cada vez que inflige daño de batalla: destierra hasta 2 monstruos en el Cementerio rival. Tu adversario no puede desterrar cartas de ningún Cementerio."},
        {"name": "Bazoo the Soul-Eater", "type": "Monster", "sub": "Effect", "attr": "EARTH", "lvl": 4, "atk": 1600, "def": 900, "desc": "Una vez por turno: puedes desterrar hasta 3 monstruos en tu Cementerio; esta carta gana 300 ATK por cada uno hasta el final del turno del adversario (hasta 2500 ATK)."},
        {"name": "Dark Spirit of the Silent", "type": "Trap", "sub": "Normal", "desc": "Fuerza a 1 monstruo del adversario a declarar un ataque inmediatamente."},
        {"name": "Fusion Gate", "type": "Spell", "sub": "Field", "desc": "Permite Invocar por Fusión desterrando los materiales de la mano o campo sin usar Polymerization."},
        {"name": "Ryu-Senshi", "type": "Monster", "sub": "Fusion", "attr": "EARTH", "lvl": 6, "atk": 2000, "def": 1200, "desc": "Niega Cartas Mágicas que lo seleccionen y niega Trampas pagando 1000 LP."},
        {"name": "Fiend Skull Dragon", "type": "Monster", "sub": "Fusion", "attr": "WIND", "lvl": 5, "atk": 2000, "def": 1200, "desc": "Niega los efectos de monstruos de Volteo y niega Trampas que lo seleccionen."}
    ],
    "Rare": [
        {"name": "Zombyra the Dark", "type": "Monster", "sub": "Effect", "attr": "DARK", "lvl": 4, "atk": 2100, "def": 500, "desc": "No puede atacar directamente al adversario. Si destruye un monstruo en batalla, pierde 200 ATK permanentemente."},
        {"name": "The Shallow Grave", "type": "Spell", "sub": "Normal", "desc": "Cada jugador selecciona 1 monstruo en su Cementerio; Invocan esos monstruos en Posición de Defensa boca abajo."},
        {"name": "Bait Doll", "type": "Spell", "sub": "Normal", "desc": "Fuerza la activación de 1 trampa colocada rival; si el tiempo es incorrecto, se destruye."},
        {"name": "Cyclon Laser", "type": "Spell", "sub": "Equip", "desc": "Equipa a Gradius. +300 ATK y perfora defensas."}
    ],
    "Common": [
        {"name": "Jowgen the Anarchist", "type": "Monster", "sub": "Effect", "attr": "LIGHT", "lvl": 3, "atk": 200, "def": 1300, "desc": "Ningún jugador puede Invocar de Modo Especial. Descarta 1 carta al azar para destruir todos los monstruos Invocados Especialmente."},
        {"name": "Tornado Bird", "type": "Monster", "sub": "Flip", "attr": "WIND", "lvl": 4, "atk": 1100, "def": 1000, "desc": "VOLTEO: Devuelve 2 Cartas Mágicas o de Trampa en el campo a la mano de sus dueños."},
        {"name": "Dancing Fairy", "type": "Monster", "sub": "Effect", "attr": "WIND", "lvl": 4, "atk": 1700, "def": 1000, "desc": "Gana 1000 LP en cada una de tus Standby Phases si está en Defensa."},
        {"name": "Supply", "type": "Spell", "sub": "Normal", "desc": "Recupera 2 cartas de equipo de tu cementerio a la mano."}
    ]
}
