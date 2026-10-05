import secrets
rng = secrets.SystemRandom()
# Klaus tiene 3700 LP, Magician of Faith vuelve a atacar con 300 ATK.
# Klaus tiene 0 cartas en mano, 0 monstruos.
# Sus dos trampas son Mirror Force e Imperial Order.
decision = rng.choice(["ACTIVA_MIRROR_FORCE", "AGUANTA_OTRA_VEZ"])
print("Decision de Klaus T10:", decision)
