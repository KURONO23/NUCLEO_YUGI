# -*- coding: utf-8 -*-
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import os

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_summary_doc():
    doc = Document()

    # Configurar márgenes de página (1 pulgada)
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Estilos de color
    COLOR_PRIMARY = RGBColor(15, 32, 67)       # Azul Noche / KaibaCorp
    COLOR_SECONDARY = RGBColor(155, 30, 30)   # Rojo Escarlata / Kurono
    COLOR_DARK = RGBColor(40, 40, 40)          # Gris Carbón
    COLOR_MUTED = RGBColor(100, 100, 100)      # Gris Medio

    # PORTADA / TÍTULO PRINCIPAL
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title_p.add_run("CRÓNICA DE UNA REVOLUCIÓN TÁCTICA")
    title_run.font.name = "Arial"
    title_run.font.size = Pt(26)
    title_run.font.bold = True
    title_run.font.color.rgb = COLOR_PRIMARY

    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_run = sub_p.add_run("De Estudiante Invisible a la Leyenda de 'KURONO'\nResumen Integral de Campaña: Era Pre-Reino & Duelist Kingdom")
    sub_run.font.name = "Arial"
    sub_run.font.size = Pt(14)
    sub_run.font.italic = True
    sub_run.font.color.rgb = COLOR_SECONDARY

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # TABLA DE METADATOS EJECUTIVOS
    meta_table = doc.add_table(rows=6, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False

    metadata = [
        ("Protagonista / Reencarnación", "Maksu (Estudiante Domino High 1-A) / Max de Sawardo"),
        ("Identidad de Torneo (Alter Ego)", "KURONO (クロノ) — El Estratega del Vórtice"),
        ("Estado Temporal Canónico", "Fin del Reino de los Duelistas -> Vísperas de Ciudad Batallas (Battle City)"),
        ("Récord Oficial de Duelos", "22 Victorias - 0 Derrotas (100% Invicto en Tiempo Real)"),
        ("Capital Financiero Acumulado", "425,000 ¥ en efectivo líquido (225k previos + 200k del pacto de Joey)"),
        ("Próximo Objetivo Maestro", "Conquistar Ciudad Batallas bajo las nuevas reglas de sacrificios y Duel Disks")
    ]

    for i, (k, v) in enumerate(metadata):
        row = meta_table.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(2.5)
        c1.width = Inches(4.0)
        set_cell_background(c0, "1A2B4C")
        set_cell_background(c1, "F2F4F8")
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.font.name = "Arial"
        r0.font.size = Pt(10)
        r0.font.bold = True
        r0.font.color.rgb = RGBColor(255, 255, 255)
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(v)
        r1.font.name = "Arial"
        r1.font.size = Pt(10)
        r1.font.color.rgb = COLOR_DARK
        
        set_cell_margins(c0, 60, 60, 100, 100)
        set_cell_margins(c1, 60, 60, 100, 100)

    doc.add_paragraph().paragraph_format.space_after = Pt(15)

    def add_section_header(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(18)
        h.paragraph_format.space_after = Pt(6)
        r = h.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(16)
        r.font.bold = True
        r.font.color.rgb = COLOR_PRIMARY
        return h

    def add_sub_header(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(12)
        h.paragraph_format.space_after = Pt(4)
        r = h.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = COLOR_SECONDARY
        return h

    def add_body_p(text, bold_prefix=None, italic=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.font.name = "Arial"
            rb.font.size = Pt(10.5)
            rb.font.bold = True
            rb.font.color.rgb = COLOR_DARK
        r = p.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(10.5)
        r.font.italic = italic
        r.font.color.rgb = COLOR_DARK
        return p

    # --- ACTO I ---
    add_section_header("ACTO I: EL DESPERTAR DEL ANÓNIMO Y LA TESIS MATEMÁTICA")
    add_body_p(
        "La historia comienza en la Preparatoria Domino, en el salón 1-A. Max, un individuo con la conciencia analítica, cínica y desapasionada de Sawardo, despierta en el cuerpo de Maksu, un adolescente completamente invisible para sus compañeros y profesores. Mientras en los pasillos Katsuya Jonouchi presume cartas de monstruos sin protección y Yugi Muto custodia el Rompecabezas del Milenio, Maksu comprende la naturaleza de este nuevo mundo: una realidad gobernada por un juego de cartas coleccionables donde los protagonistas dependen ciegamente de milagros, destino y 'el corazón de las cartas'."
    )
    add_body_p(
        "Frente a este sentimentalismo irracional, Maksu formula su tesis fundamental: el duelo no es magia ni destino; es un sistema finito cerrado regido por la teoría de probabilidades, la ventaja de recursos (card advantage), el tempo y la negación absoluta. Quien controle las matemáticas del mazo, controlará el destino sin necesidad de artefactos milenarios."
    )
    add_body_p(
        "Con los ahorros de trabajos matutinos, Maksu compra cajas selladas completas de 'Legend of Blue Eyes White Dragon' (LOB) y 'Metal Raiders' (MRD). Entiende que comprar sobres sueltos es un error de aficionados. Respeta la ley canónica inquebrantable: el Dragón Blanco de Ojos Azules no se encuentra en el mercado minorista (las únicas cuatro copias están en poder de Seto Kaiba y Solomon Muto). De sus cajas extrae el armamento de control más letal de la historia: Raigeki, Dark Hole, Monster Reborn, Change of Heart, Pot of Greed, Solemn Judgment y Mirror Force. Nace así el 'Protocolo Silencio V1.0': exactamente 40 cartas, cero manos muertas, 93.8% de probabilidad de salida óptima."
    )

    # --- ACTO II ---
    add_section_header("ACTO II: LA CONQUISTA DE DOMINO CITY Y EL BURLA-METAS")
    add_body_p(
        "Maksu sale a poner a prueba su baraja en los circuitos locales, manteniendo un perfil bajo y sin revelar su verdadero potencial:"
    )
    add_body_p(" Demuele a Ryuto 'El Triturador' (Turno 3 KO), anula a Katsuya 'El Chispazo' (Turno 2 KO) y doblega a Takuma 'El Titán' en la final de la Copa Hobby Shop. Obtiene su primer gran trofeo: la legendaria carta Summoned Skull (2500 ATK).", bold_prefix="• La Copa Hobby Shop:")
    add_body_p(" Desciende a los almacenes del puerto y barre a Kuroda 'El Tiburón de los Muelles', arrebatándole 10,000 ¥ en efectivo.", bold_prefix="• Duelo de Apuestas en el Muelle:")
    add_body_p(" En la azotea escolar, humilla el mazo refinado de Julian Tachibana, cobrando 20,000 ¥ de recompensa.", bold_prefix="• Academia Privada Meisei:")
    add_body_p(" En alianza temporal con Katsuya, barren el torneo por equipos de Arcade Central. Maksu se asegura 40,000 ¥ de los 50,000 ¥ del pozo total.", bold_prefix="• Torneo Tag-Team de Arcade Central:")

    add_sub_header("El Domino Duel Dome y el Paquete de Pegasus")
    add_body_p(
        "El clímax local ocurre en el Domino Duel Dome Wildcard Tournament, donde está en juego la última plaza oficial de la ciudad para el torneo de Maximillion Pegasus. Maksu arrasa en tres rondas implacables: en semifinales humilla a Kenji 'La Garra de Acero' encadenando un bucle infinito con Pot of Greed, Magician of Faith, Heavy Storm y Dark Hole; y en la Gran Final desintegra a Leon 'El Noble' en el Turno 2 con Raigeki y Barrel Dragon (2600 ATK)."
    )
    add_body_p(
        "Premio Oficial: El Guantelete del Reino de los Duelistas, 2 Chips Estrella y el Boleto de Primera Clase del Crucero. Además, en la apuesta ante, Maksu captura el dragón Seiyaryu (2500 ATK) de Leon, pero con fría practicidad mercantil decide devolvérselo a cambio de un rescate de 20,000 ¥ en efectivo."
    )

    # --- ACTO III ---
    add_section_header("ACTO III: LA CREACIÓN DE 'KURONO' Y LA CACERÍA METROPOLITANA")
    add_body_p(
        "Consciente de que un colegial ordinario de Domino High llamaría demasiado la atención de los espías de Pegasus y KaibaCorp si empezaba a ganar cifras millonarias, Maksu diseña un alter ego teatral: KURONO (クロノ)."
    )
    add_body_p(
        "La Estética de Kurono: Cabello en puntas afiladas que desafían la gravedad con dos mechones frontales teñidos de blanco plateado, gabardina militar negra con forro escarlata, guantes oscuros y gafas de sol ahumadas. Un personaje excéntrico y melodramático por fuera que hace que los rivales lo juzguen como un payaso arrogante, mientras por dentro opera un ordenador matemático que castiga cada error de juego."
    )
    add_body_p(
        "El Huracán de Akihabara (The Vault): Kurono desciende al club de duelos subterráneo más prestigioso de Tokio. Paga 10,000 ¥ de inscripción y destroza a cuatro duelistas de élite. En la final, derrota a Kageyama 'El Coleccionista', cobrando 150,000 ¥ de torneo, 50,000 ¥ de apuesta personal y despojándolo de una de las cartas mágicas más codiciadas de Japón: Harpie's Feather Duster (Ultra Rare Promo de importación)."
    )
    add_body_p(
        "Incursión Nocturna en Shinjuku: Tres duelos ante adicionales añaden otros 80,000 ¥. Con las ganancias, Maksu adquiere 4 cajas selladas más de Metal Raiders (MRD), raciones de supervivencia y funda su Side Deck (Banquillo Táctico) de 15 cartas especializadas."
    )

    # --- ACTO IV ---
    add_section_header("ACTO IV: EL CRUCERO DE PEGASUS Y EL GRAN ARBITRAJE")
    add_body_p(
        "El domingo por la mañana, el transatlántico de lujo de Industrial Illusions zarpa de Domino City. Maksu sube a bordo como Kurono con trato VIP, guardando 225,000 ¥ en su cinturón táctico y dos Chips Estrella en su guantelete."
    )
    add_body_p(
        "El Incidente Canónico de Exodia: Kurono se apoya en la barandilla superior y observa en silencio cómo Weevil Underwood engaña a Yugi Muto y arroja las cinco piezas de Exodia por la borda. Joey salta al mar y solo recupera dos piezas; el resto se pierde en el océano. Fiel a su filosofía, Kurono no interviene: celebra internamente que la condición de victoria más absurda del guion haya quedado erradicada sin esfuerzo."
    )
    add_body_p(
        "El Arbitraje en el Salón de Intercambios: Mientras los duelistas entran en pánico, Kurono abre su carpeta de más de 3,000 cartas comunes y raras de catorce cajas. Aprovecha la fijación infantil del anime por monstruos de alto ataque estéticamente llamativos (Gaia The Fierce Knight, Curse of Dragon, monstruos de 1800 ATK) y los intercambia por cartas de control 'aburridas' que los novatos desprecian. Kurono consigue: Morphing Jar, Card Destruction, dos copias de Waboku, Acid Trap Hole y Stop Defense. Cambió cartón vistoso por supremacía táctica pura."
    )

    # --- ACTO V ---
    add_section_header("ACTO V: LA CACERÍA EN LA ISLA Y LA HUMILLACIÓN DE KAIBA")
    add_body_p(
        "Al desembarcar en el Reino de los Duelistas, Kurono elude el drama de los protagonistas y cosecha estrellas con frialdad quirúrgica:"
    )
    add_body_p(" Despedaza a Ryoji 'El Avaricioso' en el cañón de piedra en Turno 2 (OTK) encadenando Harpie's Feather Duster, Raigeki, Tremendous Fire y Summoned Skull, ganando 4 Chips Estrella de golpe (6/10).", bold_prefix="• La Masacre del Páramo:")
    add_body_p(" Descansa toda la noche en una cueva protegida mientras Yugi resuelve el duelo contra el Falso Kaiba y el juego de las sombras de Bakura. Al amanecer, sube a la terraza del castillo y derrota al aristócrata Jean-Louis Moreau, ganando exactamente 2 estrellas para quedar en 8/10.", bold_prefix="• Los Jardines de Mármol:")
    add_body_p(" En el claro de pinos, intercepta a Mai Valentine. Con teatralidad galante y seductora, destruye su Mirror Wall con Harpie's Feather Duster, quema sus puntos de vida con Tremendous Fire y la remata con Barrel Dragon, ganando las últimas 2 estrellas para completar sus 10/10 Chips Estrella.", bold_prefix="• El Baile con Mai Valentine:")
    add_body_p(" En el puente exterior, intercepta a Seto Kaiba antes de que comience su chantaje de suicidio ante Yugi. Kurono toma el desafío de Kaiba: en Turno 2 pulveriza su Crush Card Virus con Harpie's Feather Duster, quema 1000 LP con Tremendous Fire y remata con Summoned Skull (2500 ATK) sobre Saggi (1900 de daño de batalla residual). Kaiba cae de rodillas en 0 LP con su Duel Disk apagado. Kurono sentencia con frialdad: 'Eres nada, Kaiba... tu baraja es basura... es basura. Yo me encargo de rescatar a tu hermanito; mira cómo lo hace un hombre'.", bold_prefix="• El Juicio del Parapeto:")

    # --- ACTO VI ---
    add_section_header("ACTO VI: LA SEMIFINAL, LA RENUNCIA DEL REY Y EL PACTO DE HONOR")
    add_body_p(
        "En el banquete de gala de los cuatro finalistas, Kurono declama ante Pegasus que las manecillas del tiempo se le están agotando. En el sorteo oficial queda emparejada la Semifinal 1: Kurono vs. Joey Wheeler."
    )
    add_body_p(
        "En los pasillos, Joey le revela con angustia la fotografía de su hermana Serenity (Shizuka), quien necesita tres millones de yenes para una cirugía ocular urgente en Alemania antes de perder la vista para siempre. Kurono, con su filosofía de maestro riguroso pero humano, le enseña que la determinación no reemplaza al cálculo."
    )
    add_body_p(
        "La Semifinal 1 es una clase magistral didáctica: Kurono castiga el ataque ciego de Axe Raider con Man-Eater Bug, encierra el campo de Joey con Swords of Revealing Light y aguanta el milagro de Thousand Dragon con Waboku. En el clímax, Kurono le roba el dragón con Change of Heart demostrándole que las cartas de cualquier origen son herramientas útiles, y remata el duelo con Summoned Skull. Joey cae con honor. En la arena, Kurono le asegura que la operación se realizará y le deja una advertencia de por vida: 'No pongas ladrillos en tu baraja'."
    )
    add_body_p(
        "En la Semifinal 2, Kurono expone a gritos desde el balcón las cartas trampa ocultas en las muñequeras de Bandit Keith. Pegasus descalifica y arroja a Keith por una trampilla al mar, clasificando a Yugi Muto a la Gran Final."
    )
    add_body_p(
        "El Gesto Magistral en la Gran Final: Frente a Yugi Muto y el Faraón Atem, Kurono baja los brazos y anuncia su rendición voluntaria ante el asombro del castillo. Declara que salvar a Solomon Muto y Mokuba de las garras del Ojo del Milenio es una deuda de sangre y almas que le pertenece exclusivamente al Faraón. Kurono se marcha invicto (22-0), negándole a Pegasus el placer de leer su mente."
    )
    add_body_p(
        "El Cobro del Pacto y el Futuro: Yugi vence a Pegasus con el 'Mind Shuffle' y le entrega los tres millones de yenes a Joey. Joey paga los 2.8 millones de la clínica de Serenity y busca a Maksu en Domino City para entregarle religiosamente los 200,000 ¥ restantes pactados. Con 425,000 ¥ en efectivo y una baraja legendaria, Maksu contempla el anuncio televisivo de Seto Kaiba: la inauguración de Ciudad Batallas (Battle City), el nuevo sistema Duel Disk y la regla obligatoria de sacrificios.", bold_prefix="• El Retorno a Domino:")

    # TABLA DEL MAZO PROTOCOLO SILENCIO V2.2
    add_section_header("APÉNDICE: REGISTRO DEL ARSENAL (PROTOCOLO SILENCIO V2.2)")
    
    deck_table = doc.add_table(rows=7, cols=3)
    deck_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    deck_table.autofit = False

    headers = ["Categoría", "Cartas Clave en el Mazo Principal (40 exactas)", "Función Estratégica"]
    for j, h in enumerate(headers):
        cell = deck_table.rows[0].cells[j]
        set_cell_background(cell, "0F2043")
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        set_cell_margins(cell, 80, 80, 100, 100)

    rows_data = [
        ("Monstruos Jefe (3)", "Barrel Dragon (2600), Summoned Skull (2500), Dark Magician (2500)", "Invocables sin tributo en Turno 1 (Reglas Pre-Reino). Presión letal de OTK en 2000 LP."),
        ("Atacantes de Línea (4)", "3x 7 Colored Fish (1800 ATK), Jirai Gumo (2200 ATK)", "Control de campo. En formato de 2000 LP, un ataque directo de Jirai Gumo es victoria inmediata."),
        ("Búsqueda y Flujo (5)", "Witch of the Black Forest, 3x Sangan, Morphing Jar (NUEVA)", "Morphing Jar descarta y roba 5 cartas nuevas por volteo; recarga total tras vaciar la mano."),
        ("Volteo y Reciclaje (6)", "3x Magician of Faith, 3x Man-Eater Bug", "Reciclan magias devastadoras (Pot of Greed, Raigeki) y destruyen amenazas ignorando terrenos."),
        ("Magias de Control y Quemadura (14)", "2x Pot of Greed, Raigeki, Dark Hole, Harpie's Feather Duster, Card Destruction, Tremendous Fire, Stop Defense, 1x Swords", "Limpieza asimétrica, manipulación de mano y Tremendous Fire (1000 de daño directo = 50% de los LP del rival en este formato)."),
        ("Trampas de Negación y Muro (6)", "Mirror Force, 1x Solemn Judgment, 2x Waboku, Acid Trap Hole, Trap Hole", "Doble Waboku para inmunidad total al daño de batalla, 1 Solemn quirúrgico y destrucción de atacantes/volteos.")
    ]

    for i, data in enumerate(rows_data):
        row = deck_table.rows[i+1]
        for j in range(3):
            cell = row.cells[j]
            if j == 0:
                cell.width = Inches(1.8)
                set_cell_background(cell, "EAEFF8")
            elif j == 1:
                cell.width = Inches(2.7)
                set_cell_background(cell, "FFFFFF" if i % 2 == 0 else "F7F9FC")
            else:
                cell.width = Inches(2.2)
                set_cell_background(cell, "FFFFFF" if i % 2 == 0 else "F7F9FC")
            
            p = cell.paragraphs[0]
            r = p.add_run(data[j])
            r.font.name = "Arial"
            r.font.size = Pt(9.5)
            if j == 0:
                r.font.bold = True
                r.font.color.rgb = COLOR_PRIMARY
            else:
                r.font.color.rgb = COLOR_DARK
            set_cell_margins(cell, 60, 60, 80, 80)

    # Guardar documento
    output_path1 = "C:/projects/NUCLEO_YUGI/RESUMEN_HISTORIA_COMPLETA.docx"
    output_path2 = "C:/projects/NUCLEO_YUGI/08_NOVELA/CRONICA_COMPLETA_MAKSU_KURONO.docx"
    doc.save(output_path1)
    doc.save(output_path2)
    print(f"Documento Word guardado exitosamente en:\n1. {output_path1}\n2. {output_path2}")

if __name__ == "__main__":
    create_summary_doc()
