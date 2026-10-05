# -*- coding: utf-8 -*-
import sys
import secrets

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

secret_rares = [
    "Black Luster Soldier - Envoy of the Beginning",
    "Chaos Emperor Dragon - Envoy of the End",
    "Invader of Darkness"
]

ultra_rares = [
    "Dark Magician of Chaos",
    "Dimension Fusion",
    "Chaos Sorcerer",
    "Levia-Dragon - Daedalus",
    "Manticore of Darkness",
    "Freed the Brave Wanderer",
    "Strike Ninja",
    "D.D. Scout Plane",
    "Orca Mega-Fortress of Darkness",
    "Insect Princess"
]

super_rares = [
    "Compulsory Evacuation Device",
    "Smashing Ground",
    "Reload",
    "Stealth Bird",
    "Enraged Battle Ox",
    "Stumbling",
    "Wild Nature's Release",
    "Big Burn",
    "Granadora",
    "Gradius' Option"
]

rares_commons_key = [
    "Manju of the Ten Thousand Hands",
    "Giga Gagagigo",
    "Fenrir",
    "Trap Jammer",
    "Begone, Knave!",
    "Chiron the Mage",
    "Mad Dog of Darkness",
    "Blazing Inpachi",
    "Burning Beast"
]

rng = secrets.SystemRandom()

# Abrir 1 caja de IOC (24 sobres)
pull_secret = rng.choice(secret_rares)
pull_ultras = [rng.choice(ultra_rares), rng.choice(ultra_rares)]
pull_supers = [rng.choice(super_rares) for _ in range(5)]
pull_rares = [rng.choice(rares_commons_key) for _ in range(12)]

print("=== APERTURA DE 1 CAJA DE IOC EN KAME GAME ===")
print(f"🌟 SECRET RARE: {pull_secret}")
print(f"⭐ ULTRA RARES: {pull_ultras[0]}, {pull_ultras[1]}")
print("💎 SUPER RARES:")
for s in set(pull_supers):
    print(f"   * {s} x{pull_supers.count(s)}")
print("📘 RARES / COMMONS DESTACADAS:")
for r in set(pull_rares):
    print(f"   * {r} x{pull_rares.count(r)}")
