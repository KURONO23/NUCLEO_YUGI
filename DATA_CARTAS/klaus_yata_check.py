import secrets
rng = secrets.SystemRandom()
# Klaus ve a Yata-Garasu ser invocado.
# Sabe que si Yata conecta, se acabó la partida (Yata-Lock infinito con 0 cartas en mano).
# Klaus tiene Solemn Judgment boca abajo (cuesta la mitad de sus LP: 1850 LP).
# ¿Klaus activa Solemn Judgment para salvarse del Yata-Lock?
# La probabilidad de que un banquero competitivo active Solemn Judgment para no perder instantáneamente es altísima, pero veamos qué decide el RNG:
decision = rng.choice(["ACTIVA_SOLEMN", "PARALIZADO_NO_ACTIVA", "ACTIVA_SOLEMN"])
print("Decision Klaus vs Yata:", decision)
