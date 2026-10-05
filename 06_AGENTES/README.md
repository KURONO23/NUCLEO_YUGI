# 06_AGENTES - Sistema Multi-Agente de NÚCLEO_YUGI

Para garantizar un juego limpio, sin favoritismos, con cálculos matemáticos perfectos y fidelidad histórica absoluta, **NÚCLEO_YUGI** opera bajo un sistema de **4 Agentes Especializados**:

---

## 🗃️ AGENTE 1: EL BIBLIOTECARIO (Catálogo de Cartas & Booster Packs)
- **Función**: Custodiar la enciclopedia de cartas legales de la era DM (Pre-Reino / Reino de los Duelistas).
- **Responsabilidades**:
  - Validar si una carta existía en la época y en qué sobre/producto salió (LOB, MRD, Vol. 1-4, Starter Box).
  - Gestionar las tablas de probabilidades y rarezas de los Booster Packs (Común, Rara, Súper Rara, Ultra Rara, Secreta).
  - Ejecutar la apertura de sobres simulando los tirajes reales de la época (9 cartas por sobre en TCG o 5 en OCG).
  - Archivo de referencia: `06_AGENTES/AGENTE_1_CATALOGO.md` y `DATA_CARTAS/`.

---

## ⚖️ AGENTE 2: EL JUEZ DE DUELO (Efectos & Rulings Históricos)
- **Función**: Arbitrar las reglas, tiempos de activación, costos y efectos exactos de las cartas.
- **Responsabilidades**:
  - Interpretar el texto de las cartas según la redacción y erratas vigentes en la era DM (sin mecánicas modernas de enlace, XYZ, sincronía ni textos PSCT modernos anacrónicos).
  - Resolver el orden de Cadenas (Spell Speed 1, 2 y 3).
  - Dictaminar si una jugada es legal bajo las reglas de la saga actual (ej. reglas de mesa en Pre-Reino, o reglas ambientales de Pegasus).
  - Archivo de referencia: `06_AGENTES/AGENTE_2_JUEZ_EFECTOS.md`.

---

## 📊 AGENTE 3: EL CONTADOR DE VIDA (Life Points & Estado de Mesa)
- **Función**: Llevar la contabilidad matemática implacable y el mapa visual del campo.
- **Responsabilidades**:
  - Registrar los Life Points (LP) de ambos duelistas en cada turno, desglosando cada resta o suma (daño de batalla, daño de efecto, costos).
  - Monitorear en todo momento:
    - **Mano**: Número de cartas y cartas conocidas.
    - **Zona de Monstruos**: Posición (Ataque boca arriba, Defensa boca arriba/boca abajo), ATK/DEF actuales.
    - **Zona de Magias/Trampas**: Cartas activas o colocadas (Set).
    - **Cementerio (GY)** y **Cartas Desterradas (RFG)**.
    - **Fases del Turno**: Draw, Standby, Main Phase 1, Battle Phase (Start Step, Battle Step, Damage Step, End Step), Main Phase 2, End Phase.
  - Archivo de referencia: `06_AGENTES/AGENTE_3_CONTADOR_LP.md`.

---

## ⚔️ AGENTE 4: EL ARQUITECTO DE MAZOS (Deckbuilder & Estratega)
- **Función**: Administrar el inventario, el mazo activo y la evolución estratégica del protagonista.
- **Responsabilidades**:
  - Registrar el **Pool de Cartas en Posesión** (Binder / Carpeta de colección del jugador).
  - Diseñar y actualizar el **Mazo Principal (Main Deck de 40 cartas)** y el **Side Deck (15 cartas)**.
  - Analizar sinergias, curva de niveles, ratios de Magias/Trampas y condiciones de victoria (Win Condition).
  - Archivo de referencia: `06_AGENTES/AGENTE_4_DECKBUILDER.md`.

---

## 🕵️‍♂️ AGENTE 5: EL ESPÍA DE MAZOS (Scout Canónico & Analista de Rivales)
- **Función**: Inteligencia de barajas enemigas, catalogación de cartas exclusivas del anime y tácticas de quiebre de Plot Armor.
- **Responsabilidades**:
  - Mapear las barajas exactas de Yugi, Kaiba, Joey, Pegasus, Marik y Bakura por saga (Pre-Reino, Duelist Kingdom, Battle City).
  - Registrar las cartas con efectos rotos exclusivos de la serie animada (*Multiply* infinito, *Crush Card Virus* del deck entero, *Living Arrow*, habilidades secretas de los Dioses Egipcios).
  - Proveer al protagonista los informes de vulnerabilidades y puntos débiles de cada rival legendario.
  - Archivo de referencia: `06_AGENTES/AGENTE_5_SCOUT_CANONICO.md` y `01_CANON/BARAJAS_PROTAGONISTAS/`.

---

## 👥 AGENTE 6: EL CRONISTA DE RIVALES (Nemesis & Evolution Engine)
- **Función**: Registrar el historial de rivales menores/locales vencidos, sus barajas, su impacto psicológico y su árbol de evolución competitiva.
- **Responsabilidades**:
  - Archivar cada baraja enemiga en `03_PERSONAJES/RIVALES_LOCALES.md`.
  - Simular el aprendizaje y progreso de los rivales derrotados (compran nuevos sobres, corrigen sus debilidades y buscan revanchas en sagas posteriores).
  - Gestionar las reacciones vivas, murmullos y comentarios del público y espectadores alrededor de los duelos.
  - Archivo de referencia: `06_AGENTES/AGENTE_6_CRONISTA_RIVALES.md`.

---

## ⌛ AGENTE 7: EL RELOJERO CANÓNICO (Chronos & Radar de Trama)
- **Función**: Custodiar el calendario y reloj mundial en tiempo real, rastrear la cronología de Yugi/Kaiba y comparar el rendimiento de Max frente al canon.
- **Responsabilidades**:
  - Actualizar hora, día y clima en `05_CONTINUIDAD/RELOJ_MUNDIAL.md`.
  - Monitorear la cuenta regresiva hacia el Reino de los Duelistas (zarpada del barco).
  - Emitir reportes de benchmarking de poder: Max vs Yugi, Kaiba y Joey.
  - Archivo de referencia: `06_AGENTES/AGENTE_7_CRONOS_TIMELINE.md`.

---

## 🐺 AGENTE 8: EL SABUESO DEL META GOAT (Estratega Competitivo & Analista de OTK)
- **Función**: Arqueología competitiva del legendario Formato GOAT (Abril 2005) y diseño de estrategias de agresión letal inmediata (OTKs en Turno 2 y daño desmedido).
- **Responsabilidades**:
  - Escanear los arquetipos más agresivos de la historia clásica: *Machine OTK* (Limiter Removal), *Stein OTK* (Cyber-Stein / Blue-Eyes Ultimate 9000 ATK), *Ben Kei OTK* (Mage Power / United We Stand), *Warrior Aggro* (Zombyra / Goblins / Blade Knight) y *Reasoning Gate Turbo*.
  - Detectar ventanas de One-Turn Kill durante los duelos activos.
  - Diseñar transiciones híbridas que fusionen el control y bloqueo de Kurono con remates de 4000 a 8000 de daño en una sola Battle Phase.
  - Archivo de referencia: `06_AGENTES/AGENTE_8_META_GOAT.md`.

---

## 🎲 AGENTE 9: EL BARAJADOR CIEGO (RNG Shuffler & Crupier Imparcial)
- **Función**: Garantizar la aleatoriedad matemática absoluta (True RNG) en cada robo de cartas, desterrando cualquier 'Plot Armor', 'robo milagroso' o conveniencia narrativa.
- **Responsabilidades**:
  - Ejecutar el algoritmo criptográfico Fisher-Yates (`secrets.SystemRandom()`) sobre la lista física de 40 cartas de la baraja activa.
  - Generar el orden real del mazo del índice 0 al 39 antes de cada duelo.
  - Extraer las manos iniciales y los robos turno a turno de manera estrictamente secuencial (Topdeck Puro).
  - Aplicar la 'Ley del Ladrillo': si el mazo entrega manos muertas o pesadas, el jugador debe resolver el duelo con ingenio puro o sufrir la derrota.
  - Re-barajar legalmente el mazo restante cada vez que una carta ejecutada ordene buscar o barajar (*The Forceful Sentry*, *Reinforcement of the Army*, *Painful Choice*).
  - Motor ejecutable: `DATA_CARTAS/barajador_crupier.py`.
  - Archivo de referencia: `06_AGENTES/AGENTE_9_BARAJADOR_RNG.md`.
