# Klaus tiene 4000 LP.
# Maga de la Fe ataca con 300 ATK.
# Klaus tiene 1 carta boca abajo: Mirror Force.
# Mano de Klaus: 0 cartas. Campo: 0 monstruos.
# Si activa Mirror Force: se queda sin trampas, pero destruye a Magician of Faith.
# Si no la activa: recibe 300 de daño (baja a 3700 LP) y conserva Mirror Force para un atacante mayor.
import secrets
rng = secrets.SystemRandom()
decision = rng.choice(["ACTIVA_MIRROR_FORCE", "AGUANTA_EL_GOLPE"])
print("Decision de Klaus:", decision)
