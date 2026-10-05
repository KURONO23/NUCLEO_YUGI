import urllib.request
import json
import urllib.parse
import os
import time

cards_to_audit = [
    # Mazo Maksu Chaos-Yata Control
    "Chaos Emperor Dragon - Envoy of the End",
    "Black Luster Soldier - Envoy of the Beginning",
    "Jinzo",
    "Yata-Garasu",
    "Breaker the Magical Warrior",
    "Tribe-Infecting Virus",
    "Injection Fairy Lily",
    "Spirit Reaper",
    "Don Zaloog",
    "Sangan",
    "Witch of the Black Forest",
    "Magician of Faith",
    "Cyber Jar",
    "Fiber Jar",
    "Painful Choice",
    "Graceful Charity",
    "Pot of Greed",
    "Delinquent Duo",
    "The Forceful Sentry",
    "Harpie's Feather Duster",
    "Raigeki",
    "Dark Hole",
    "Dimension Fusion",
    "Snatch Steal",
    "Change of Heart",
    "Premature Burial",
    "Book of Moon",
    "Reinforcement of the Army",
    "United We Stand",
    "Nobleman of Crossout",
    "Ring of Destruction",
    "Mirror Force",
    "Torrential Tribute",
    "Imperial Order",
    "Solemn Judgment",
    "Magic Cylinder",
    "Robbin' Goblin",
    # Mazo Joey Wheeler
    "Graceful Dice",
    "Skull Dice",
    "Time Wizard",
    "Baby Dragon",
    "Thousand Dragon",
    "Gearfried the Iron Knight",
    "Marauding Captain",
    "Blade Knight",
    "Gilford the Lightning",
    "Roulette Spider",
    "Rocket Warrior",
    "Alligator's Sword",
    "Panther Warrior",
    "Kunai with Chain",
    "Fairy Box",
    # Mazo Maksu Fun Mill
    "Needle Worm",
    "Morphing Jar",
    "Morphing Jar #2",
    "Hiro's Shadow Scout",
    "Tsukuyomi",
    "The Bistro Butcher",
    "Spear Cretan",
    "Night Assailant",
    "Book of Taiyou",
    "Card Destruction",
    "The Shallow Grave",
    "Swords of Revealing Light",
    "Messenger of Peace",
    "Level Limit - Area B",
    "Gravity Bind",
    "Desert Sunlight",
    "Waboku",
    "Threatening Roar",
    # Rivales KC Grand Championship (Vivian, Zigfried, Leon)
    "Luster Dragon",
    "Twin-Headed Behemoth",
    "Dragon Lady",
    "Super Rejuvenation",
    "Dragon's Rage",
    "Ride of the Valkyries",
    "Valkyrie Dritte",
    "Valkyrie Erste",
    "Valkyrie Zweite",
    "Mischief of the Time Goddess",
    "Golden Castle of Stromberg"
]

print(f"Iniciando auditoria de {len(cards_to_audit)} cartas clave...")
audit_results = {}

for name in cards_to_audit:
    try:
        encoded = urllib.parse.quote(name)
        url = f"https://db.ygoprodeck.com/api/v7/cardinfo.php?name={encoded}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            card = data['data'][0]
            audit_results[name] = {
                "name": card.get("name"),
                "type": card.get("type"),
                "desc": card.get("desc"),
                "atk": card.get("atk"),
                "def": card.get("def"),
                "level": card.get("level"),
                "race": card.get("race"),
                "attribute": card.get("attribute")
            }
            print(f" [OK] {name}")
    except Exception as e:
        print(f" [ERROR / ESPECIAL] {name}: {e}")
        audit_results[name] = {"name": name, "status": "Anime/Especial", "desc": "Carta exclusiva o con nombre de anime"}
    time.sleep(0.05)

output_file = r"C:\projects\NUCLEO_YUGI\DATA_CARTAS\audit_cards_db.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(audit_results, f, ensure_ascii=False, indent=2)

print(f"Auditoria finalizada. Guardada en {output_file}")
