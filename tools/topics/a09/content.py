# -*- coding: utf-8 -*-
"""Category A1/A2, Topic 9 content (documentation: licences, the motorcycle's papers, insurance, points and
liability), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the A1/A2 course's Tema 9 (Documentación). The parts that are about riders — the
motorcycle licences, the novice plate on a motorcycle, the ITV calendar of motorcycles and mopeds, plates, insurance
and the passenger, the rider's points traps — are written here. The rules that are the same for every driver
(validity and renewal, duplicates, the sale deadlines, ITV results, the points tables, the speeding table and who is
liable) are taken from Category B, Topic 9, so one correction reaches both pages. The course leaves out the B-only
licences and the Penal Code; so does this page.

The rules come from the Ley sobre Tráfico (RDL 6/2015), the Reglamento General de Conductores (RD 818/2009), the
Reglamento General de Vehículos (RD 2822/1998), the ITV decree (RD 920/2017), the motor-insurance law (RDL 8/2004) and
the reform made by RD 518/2026 (in force 1 October 2026), as they stand in November 2026.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from ..b09 import content as B9
from .diagrams import licence_ladder, a2_power, itv_timeline, points_path, insurance_grid

TWO = ("On two wheels", "Sobre dos ruedas")


# ------------------------------------------------------------------------------------------ helpers
def _under(B, start, kinds=None, skip_title=None):
    """The blocks under the heading of Topic B9 whose English title starts with `start`, up to the next heading.
    `kinds` keeps only those block kinds; `skip_title` drops boxes whose English title starts with it."""
    i = next((k for k, b in enumerate(B) if (b[0] == "h3" and b[1]["en"].startswith(start)) or (b[0] == "h2" and b[2]["en"].startswith(start))), None)
    if i is None:
        raise KeyError(f"Topic B9 has no heading starting with {start!r}")
    out = []
    for b in B[i + 1:]:
        if b[0] in ("h2", "h3"):
            break
        if kinds and b[0] not in kinds:
            continue
        if skip_title and b[0] == "box" and b[2]["en"].startswith(skip_title):
            continue
        out.append(b)
    if not out:
        raise KeyError(f"Nothing taken from Topic B9 under {start!r}")
    return out


def _table(B, start, first_head):
    """The table under `start` whose first column header (English) starts with `first_head`."""
    for b in _under(B, start, ("table",)):
        if b[1][0]["en"].startswith(first_head):
            return b
    raise KeyError(f"No table {first_head!r} under {start!r} in Topic B9")


def _box(B, start, title):
    for b in _under(B, start, ("box",)):
        if b[2]["en"].startswith(title):
            return b
    raise KeyError(f"No box {title!r} under {start!r} in Topic B9")


def blocks():
    b9 = B9.blocks()
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Three families of papers: the <b>rider’s</b> (licence and its points), the <b>motorcycle’s</b> (registration certificate, ITV card, insurance), and what happens when rules are broken "
         "(<b>points</b> and <b>who pays the fine</b>).",
         "Tres familias de documentos: los del <b>conductor</b> (permiso y sus puntos), los de la <b>motocicleta</b> (permiso de circulación, tarjeta ITV, seguro) y lo que ocurre al incumplir "
         "(<b>puntos</b> y <b>quién responde</b>)."),
        ("The exam loves <b>numbers</b>: ages (<b>15, 16, 18, 20, 21</b>), power limits (<b>11 kW, 35 kW, 0.1 and 0.2 kW/kg</b>), <b>125 cc</b>, deadlines (<b>10, 15 and 30 days</b>), points (<b>8, 12, 15</b>) "
         "and the ITV calendar (<b>3 and 4 years</b>).",
         "El examen pregunta sobre todo <b>cifras</b>: edades (<b>15, 16, 18, 20, 21</b>), potencias (<b>11 kW, 35 kW, 0,1 y 0,2 kW/kg</b>), <b>125 c.c.</b>, plazos (<b>10, 15 y 30 días</b>), puntos (<b>8, 12, 15</b>) "
         "y el calendario de la ITV (<b>3 y 4 años</b>)."),
        ("The sections follow your A1/A2 course’s Topic 9. The rules that are the same for every driver come from <b>Category B, Topic 9</b>, which also covers the car licences and the road-safety crimes of the Penal Code "
         "that your course leaves out. What changes on a motorcycle is flagged <b>“On two wheels”</b>. Spanish exam terms are in <i>italics</i>, and a glossary closes the topic.",
         "Los apartados siguen el Tema 9 de tu curso A1/A2. Las normas iguales para todos los conductores proceden del <b>Tema 9 del permiso B</b>, que trata además los permisos de turismo y los delitos contra la seguridad vial "
         "del Código Penal que tu curso no incluye. Lo propio de la moto va marcado como <b>«Sobre dos ruedas»</b>. Al final hay un glosario español–inglés."),
    ]))

    # ---------------------------------------------------------------- 1. rider
    B.append(H2("1", "The rider’s documents", "Documentación del conductor"))
    B.append(P(
        "You must carry your <b>driving licence</b> and the <b>motorcycle’s documents</b>, <b>valid and in force</b>, and <b>show them</b> to the authorities or their agents when asked: the <b>physical original</b>, "
        "a <b>certified photocopy</b>, or the <b>digital</b> version in the DGT’s <b>miDGT</b> app. The app is as valid as paper for traffic purposes, but <b>only in Spain</b>: if you ride abroad, take the physical documents.",
        "Debes llevar tu <b>permiso de conducción</b> y la <b>documentación de la motocicleta</b>, <b>válidos y vigentes</b>, y <b>mostrarlos</b> a la autoridad o a sus agentes cuando lo soliciten: el <b>original</b>, "
        "una <b>fotocopia compulsada</b> o la versión <b>digital</b> de la app <b>miDGT</b>. La app vale lo mismo que el papel a efectos de tráfico, pero <b>solo en España</b>: si sales al extranjero, lleva los documentos físicos."))
    B.append(P("Nobody may hold <b>more than one</b> driving licence issued by an EU member state. If they do, the one that applies is withdrawn. All your classes (AM, A1, A2, B…) go on <b>one single licence</b>.",
               "Nadie puede ser titular de <b>más de un</b> permiso expedido por un Estado miembro de la UE; si fuese así, se le retira el que proceda. Todas tus clases (AM, A1, A2, B…) constan en <b>un único permiso</b>."))
    B.append(_table(b9, "The driver’s documents", "To get a driving licence"))
    B.append(BOX("trap", "When your fitness changes", "Si cambian tus aptitudes", [
        ("If illness, injury or anything else takes away the required fitness, you may <b>not ride until you recover it</b>, even though your licence is still in force.",
         "Si por enfermedad, lesión u otra circunstancia pierdes las aptitudes requeridas, <b>no puedes conducir hasta recuperarlas</b>, aunque el permiso siga en vigor."),
        ("If your physical condition changes and the motorcycle has to be <b>adapted</b>, tell the Provincial Traffic Office, even though the licence is in force.",
         "Si cambian tus condiciones físicas y hay que <b>adaptar</b> la motocicleta, comunícalo a la Jefatura de Tráfico, aunque el permiso esté en vigor."),
    ]))

    # 1.1 classes
    B.append(H3("1.1 Motorcycle licences", "1.1 Clases de permisos de conducción"))
    B.append(FIG(licence_ladder, "A1 and A2 can each be taken directly at 16 and 18. The A can only be reached from the A2, after two years of experience and a training course.",
                 "El A1 y el A2 se pueden obtener directamente a los 16 y 18 años. Al A solo se llega desde el A2, tras dos años de experiencia y una formación."))
    B.append(TABLE(
        [T("Licence", "Permiso"), T("Age", "Edad"), T("Motorcycles", "Motocicletas"), T("Also lets you drive", "También permite conducir")],
        [
            [T("<b>A1</b>", "<b>A1</b>"), T("<b>16</b>", "<b>16</b>"),
             T("Up to <b>125 cc</b>, <b>11 kW</b> (a little under 15 hp) and <b>0.1 kW/kg</b>.", "Hasta <b>125 c.c.</b>, <b>11 kW</b> (algo menos de 15 CV) y <b>0,1 kW/kg</b>."),
             T("<b>Motor tricycles up to 15 kW</b>; two- and three-wheel <b>mopeds</b> and <b>light quadricycles</b> (A1 includes AM); vehicles for people with <b>reduced mobility</b>.",
               "<b>Triciclos de motor de hasta 15 kW</b>; <b>ciclomotores</b> de dos y tres ruedas y <b>cuadriciclos ligeros</b> (el A1 incluye el AM); vehículos para personas de <b>movilidad reducida</b>.")],
            [T("<b>A2</b>", "<b>A2</b>"), T("<b>18</b>", "<b>18</b>"),
             T("Up to <b>35 kW</b> and <b>0.2 kW/kg</b>, and <b>not derived</b> from a motorcycle with <b>more than twice</b> that power.",
               "Hasta <b>35 kW</b> y <b>0,2 kW/kg</b>, y <b>no derivadas</b> de una motocicleta con <b>más del doble</b> de su potencia."),
             T("Everything <b>AM</b> and <b>A1</b> allow (A2 includes A1), and reduced-mobility vehicles.", "Todo lo que autorizan el <b>AM</b> y el <b>A1</b> (el A2 incluye el A1), y vehículos para personas de movilidad reducida.")],
            [T("<b>A</b>", "<b>A</b>"), T("<b>20</b> (<b>21</b> for trikes over 15 kW)", "<b>20</b> (<b>21</b> para triciclos de más de 15 kW)"),
             T("<b>Any motorcycle</b>, and motor tricycles.", "<b>Cualquier motocicleta</b> y triciclos de motor."),
             T("Everything AM, A1 and A2 allow, and reduced-mobility vehicles.", "Todo lo de AM, A1 y A2, y vehículos para personas de movilidad reducida.")],
        ],
        widths=["10%", "16%", "36%", "38%"],
    ))
    B.append(FIG(a2_power, "Two checks for the A2: divide the power by the mass, and, if the motorcycle has been limited, compare its original power with twice the limited one.",
                 "Dos comprobaciones para el A2: dividir la potencia por la masa y, si la moto está limitada, comparar su potencia original con el doble de la limitada."))
    B.append(BOX("key", "How you get each one", "Cómo se obtiene cada uno", [
        ("<b>A1</b> and <b>A2</b>: with the <b>theory and practical exams</b> at the Traffic Office. Nobody has to hold an AM or an A1 first.",
         "<b>A1</b> y <b>A2</b>: con las <b>pruebas teóricas y prácticas</b> en la Jefatura. No hace falta tener antes el AM ni el A1."),
        ("<b>A</b>: only if you have held an <b>A2</b> with <b>at least two years of experience</b>, and you complete a <b>training course</b> (there is no new exam). "
         "That is why the minimum age is <b>20</b>: 18 for the A2 plus two years.",
         "<b>A</b>: solo si eres titular de un <b>A2</b> con <b>al menos dos años de experiencia</b> y superas una <b>formación</b> (no hay examen nuevo). "
         "Por eso la edad mínima es de <b>20 años</b>: 18 del A2 más dos años."),
        ("Beyond your course: an A1 holder with <b>two years of experience</b> may also get the A2 by passing only the <b>practical test</b> (which an official training course can replace).",
         "Más allá de tu curso: quien tenga el A1 con <b>dos años de experiencia</b> también puede obtener el A2 superando solo la <b>prueba práctica</b> (que puede sustituirse por una formación oficial)."),
    ]))
    B.append(BOX("trap", "The B licence and 125 cc motorcycles", "El permiso B y las motos de 125 c.c.", [
        ("With a <b>B held for more than three years</b> you may ride the <b>motorcycles of the A1</b> (up to 125 cc, 11 kW, 0.1 kW/kg) <b>in Spain only</b>. Abroad you need a real A1.",
         "Con un <b>permiso B de más de tres años</b> de antigüedad puedes conducir las <b>motocicletas del A1</b> (hasta 125 c.c., 11 kW, 0,1 kW/kg) <b>solo en España</b>. En el extranjero necesitas el A1."),
        ("The three-year rule is about <b>motorcycles</b>. <b>Mopeds</b> and <b>motor tricycles</b> are already in the B itself from day one (tricycles over 15 kW only from age 21).",
         "La regla de los tres años se refiere a las <b>motocicletas</b>. Los <b>ciclomotores</b> y los <b>triciclos de motor</b> ya los incluye el propio B desde el primer día (los triciclos de más de 15 kW, solo desde los 21 años)."),
    ]))

    # 1.2 validity
    B.append(H3("1.2 Validity and renewal", "1.2 Vigencia y prórroga"))
    B += _under(b9, "1.4 Validity")
    # 1.3 changes
    B.append(H3("1.3 Changes of details and duplicates", "1.3 Cambio de datos y duplicados"))
    B += _under(b9, "1.5 Changes")
    # 1.4 new riders
    B.append(H3("1.4 New riders", "1.4 Conductores noveles"))
    B.append(E(
        "The novice plate V-13 (“L”) on a motorcycle", "La señal V-13 («L») en la motocicleta",
        "Whoever gets a driving licence <b>for the first time</b> must display the <b>V-13</b> during its <b>first year</b>: <b>retroreflective, green with a white “L”</b>. "
        "On a car it goes at the <b>rear left</b>; on a <b>motorcycle</b> (and on three-wheelers) it is enough to place it <b>somewhere visible at the rear</b>. Motorcycles use a <b>smaller plate</b> (10 × 13 cm instead of 15 × 19.5 cm). "
        "If the novice’s licence is <b>withdrawn or suspended</b> during that year, the year is <b>extended</b> by the same time.",
        "Quien obtenga <b>por primera vez</b> un permiso de conducción debe llevar la <b>V-13</b> durante su <b>primer año</b>: <b>reflectante, de fondo verde con la «L» en blanco</b>. "
        "En un turismo va <b>detrás a la izquierda</b>; en una <b>motocicleta</b> (y en los vehículos de tres ruedas) basta con colocarla en un <b>sitio visible de la parte posterior</b>. En las motos la placa es <b>más pequeña</b> (10 × 13 cm en lugar de 15 × 19,5 cm). "
        "Si al novel le <b>intervienen o suspenden</b> el permiso durante ese año, el año se <b>amplía</b> en ese mismo tiempo.",
        pills_=[T("first year", "primer año"), T("rear, visible", "detrás, visible")]))
    B.append(BOX("trap", f"{TWO[0]}: is it really your first licence?", f"{TWO[1]}: ¿es de verdad tu primer permiso?", [
        ("You do <b>not</b> count as a first-time holder if you have held <b>another licence of any class for at least a year</b>. A rider with a B for years who now gets an A2 does <b>not</b> wear the “L”.",
         "<b>No</b> se considera que obtienes el permiso por primera vez si ya has sido titular de <b>otro permiso de cualquier clase durante al menos un año</b>. Quien tiene el B desde hace años y ahora saca el A2 <b>no</b> lleva la «L»."),
        ("An <b>AM</b> is a driving licence too: a moped rider who got the AM at 15 and the A1 at 16 has already done the novice year.",
         "El <b>AM</b> también es un permiso de conducción: quien sacó el AM a los 15 años y el A1 a los 16 ya ha cumplido el año de novel."),
    ]))
    # 1.5 nullity
    B.append(H3("1.5 Nullity, loss of validity and suspension", "1.5 Nulidad o lesividad y pérdida de vigencia"))
    B += _under(b9, "1.7 Nullity")

    # ---------------------------------------------------------------- 2. motorcycle
    B.append(H2("2", "The motorcycle’s documents", "Documentación del vehículo"))
    B.append(P(
        "To ride on public roads the motorcycle must carry the <b>originals or duly certified photocopies</b> of: the <b>registration certificate</b> (<i>permiso de circulación</i>); and the <b>ITV card</b> with its inspections up to date "
        "(some mopeds have a <b>certificate of characteristics</b> instead) plus the <b>last inspection report</b>, if it has already been to the ITV. On a motorcycle there is little room: a certified copy or the app saves space.",
        "Para circular, en la motocicleta deben llevarse los <b>originales o fotocopias debidamente cotejadas</b> de: el <b>permiso de circulación</b>; y la <b>tarjeta de inspección técnica</b> al corriente "
        "(algunos ciclomotores tienen <b>certificado de características</b> en su lugar) y el <b>último informe de inspección</b>, si ya ha pasado la ITV. En moto hay poco sitio: la fotocopia cotejada o la app ahorran espacio."))
    B.append(H3("2.1 The registration certificate (permiso de circulación)", "2.1 El permiso de circulación"))
    B.append(P(
        "It <b>authorises the motorcycle to be ridden</b>. The Traffic Office issues it after checking that the vehicle meets the conditions to circulate. It shows, among other data, the <b>plate number</b>, "
        "<b>registration date</b>, <b>owner’s name and address</b>, <b>make, model, MMA, number of seats</b> and the <b>use</b> it is meant for.",
        "<b>Autoriza la circulación de la motocicleta</b>. Lo expide la Jefatura de Tráfico tras comprobar que el vehículo reúne las condiciones para circular. En él figuran, entre otros, la <b>matrícula</b>, "
        "la <b>fecha de matriculación</b>, el <b>nombre y domicilio del titular</b>, <b>marca, modelo, MMA, número de plazas</b> y el <b>servicio</b> al que se destina."))
    B.append(_table(b9, "2.1 The registration", "Change"))
    B.append(TABLE(
        [T("Number plate on two wheels", "Placa de matrícula en dos ruedas")],
        [
            [T("<b>Motorcycles and mopeds</b> carry <b>one single plate, at the rear</b>.", "<b>Motocicletas y ciclomotores</b> llevan <b>una sola placa, en la parte posterior</b>.")],
            [T("The <b>rider</b> must make sure that nothing (a top case, a bag, mud, a bent bracket) <b>prevents or hinders reading it</b>.",
               "El <b>conductor</b> es responsable de que nada (un baúl, una bolsa, barro, un soporte doblado) <b>impida o dificulte su lectura</b>.")],
        ],
    ))
    # 2.2 ITV
    B.append(H3("2.2 The ITV card and inspections", "2.2 La tarjeta de inspección técnica (ITV)"))
    B.append(P(
        "The <b>ITV card</b> certifies that the motorcycle meets the <b>technical conditions</b> to be ridden; every motor vehicle needs one. Its front records the <b>inspections</b>; its back holds the <b>technical data</b> "
        "(chassis number, make, type, tare, seats, power…) and any <b>major modifications</b> (a different exhaust, extra lights, a sidecar…). The age of the motorcycle counts from the <b>registration date</b> on the registration certificate; "
        "for the 2nd and later inspections, check the <b>ITV card</b> or the <b>V-19</b> sticker.",
        "La <b>tarjeta ITV</b> acredita que la motocicleta reúne las <b>condiciones técnicas</b> para circular; es obligatoria para todo vehículo de motor. En el anverso, las <b>inspecciones</b> pasadas; en el reverso, las <b>características técnicas</b> "
        "(bastidor, marca, tipo, tara, plazas, potencia…) y las <b>reformas de importancia</b> (otro escape, faros adicionales, un sidecar…). La antigüedad se cuenta desde la <b>fecha de matriculación</b> del permiso de circulación; "
        "para la 2.ª ITV y siguientes, se consulta la <b>tarjeta ITV</b> o el distintivo <b>V-19</b>."))
    B.append(FIG(itv_timeline, "A two-wheel moped first goes at 3 years, a motorcycle at 4; after that, both go every 2 years for as long as they are on the road.",
                 "El ciclomotor de dos ruedas va por primera vez a los 3 años y la motocicleta a los 4; después, los dos cada 2 años mientras circulen."))
    B.append(TABLE(
        [T("Vehicle", "Vehículo"), T("Frequency", "Frecuencia")],
        [
            [T("Two-wheel <b>mopeds</b>", "<b>Ciclomotores</b> de dos ruedas"), T("Exempt up to <b>3 years</b>; then every <b>2 years</b>.", "Exentos hasta <b>3 años</b>; después, cada <b>2 años</b> (bienal).")],
            [T("<b>Motorcycles</b>, three-wheel mopeds, light quadricycles, three-wheelers, quadricycles and quads", "<b>Motocicletas</b>, ciclomotores de tres ruedas, cuadriciclos ligeros, vehículos de tres ruedas, cuadriciclos y quads"),
             T("Exempt up to <b>4 years</b>; then every <b>2 years</b>.", "Exentos hasta <b>4 años</b>; después, cada <b>2 años</b> (bienal).")],
        ],
        widths=["56%", "44%"],
    ))
    B.append(BOX("key", f"{TWO[0]}: the V-19 sticker", f"{TWO[1]}: el distintivo V-19", [
        ("Vehicles <b>with a windscreen</b>: in its <b>top right corner</b>, on the inside. A motorcycle <b>without a windscreen</b>: somewhere <b>clearly visible</b>.",
         "Vehículos <b>con parabrisas</b>: en su <b>ángulo superior derecho</b>, por la cara interior. Motocicleta <b>sin parabrisas</b>: en un <b>sitio bien visible</b>."),
        ("You may pass the ITV <b>up to 30 days early</b> without losing time: the next date counts from the one you were due.",
         "Se puede pasar la ITV <b>hasta 30 días antes</b> sin perder tiempo: la fecha siguiente se cuenta desde la que tocaba."),
    ]))
    B.append(_box(b9, "How often", "Major changes"))
    B.append(_table(b9, "How often", "Result of the periodic ITV"))
    B.append(next(b for b in _under(b9, "How often", ("p",)) if b[1]["en"].startswith("After an unfavourable")))
    # 2.3 insurance
    B.append(H3("2.3 Compulsory insurance", "2.3 Seguro obligatorio"))
    B.append(P(
        "The compulsory <b>third-party liability</b> insurance covers, within certain limits, the <b>rider’s civil liability</b> for <b>injuries to people</b> and <b>damage to property</b> caused in road traffic. "
        "The <b>owner</b> must take it out, <b>even if the motorcycle is not being ridden</b>; whoever signs it is the <b>policyholder</b> (<i>tomador</i>). Mopeds must be insured too.",
        "El seguro de responsabilidad civil de suscripción obligatoria cubre, dentro de ciertos límites, la <b>responsabilidad civil del conductor</b> por <b>daños a las personas</b> (corporales) <b>o a los bienes</b> (materiales) causados con motivo de la circulación. "
        "Debe concertarlo el <b>propietario</b>, <b>aunque la moto no esté circulando</b>; quien lo contrata es el <b>tomador</b>. Los ciclomotores también deben estar asegurados."))
    B.append(FIG(insurance_grid, "The guilty rider’s own injuries and own motorcycle are never paid by the compulsory insurance; other people’s injuries are, including the passenger’s.",
                 "Las lesiones del propio conductor culpable y su moto nunca las paga el seguro obligatorio; las lesiones de los demás, sí, también las del pasajero."))
    B.append(_table(b9, "2.3 Compulsory", "Covered"))
    B.append(BOX("key", f"{TWO[0]}: your passenger and your gear", f"{TWO[1]}: tu pasajero y tu equipo", [
        ("Your <b>passenger’s injuries</b> are covered by your compulsory insurance, <b>even if the passenger is your partner or a relative</b>: the exclusion for relatives is only for their <b>property</b>.",
         "Las <b>lesiones de tu pasajero</b> las cubre tu seguro obligatorio, <b>aunque sea tu pareja o un familiar</b>: la exclusión de los parientes es solo para sus <b>bienes</b>."),
        ("Your <b>own injuries</b>, your <b>motorcycle</b>, your <b>helmet and clothing</b> and what you carry are <b>not</b> covered by the compulsory insurance. Cover for them has to be added voluntarily.",
         "Tus <b>propias lesiones</b>, tu <b>moto</b>, tu <b>casco y tu ropa</b> y lo que transportas <b>no</b> los cubre el seguro obligatorio. Para eso hay que contratar coberturas voluntarias."),
    ]))
    B.append(_box(b9, "2.3 Compulsory", "Good to know"))
    B.append(_table(b9, "2.3 Compulsory", "Topic"))

    # ---------------------------------------------------------------- 3. points
    B.append(H2("3", "The points licence", "Permiso por puntos"))
    B.append(H3("3.1 How many points do I have?", "3.1 ¿Cuántos puntos tengo?"))
    B += _under(b9, "3.1 How many")
    B.append(BOX("trap", f"{TWO[0]}: one balance for all your licences", f"{TWO[1]}: un solo saldo para todos tus permisos", [
        ("The <b>8 points</b> of a new licence do <b>not</b> apply if you already held <b>another licence for more than two years</b>. A rider who has had the AM or the B for three years and gets an A2 starts with <b>12</b>.",
         "Los <b>8 puntos</b> del permiso nuevo <b>no</b> se aplican si ya eras titular de <b>otro permiso con más de dos años</b>. Quien tiene el AM o el B desde hace tres años y saca el A2 empieza con <b>12</b>."),
        ("Points lost riding a motorcycle come off the <b>same balance</b> that lets you drive a car, and the other way round.",
         "Los puntos que pierdes en moto salen del <b>mismo saldo</b> que te permite conducir un turismo, y al revés."),
    ]))
    B.append(H3("3.2 Offences and points", "3.2 Infracciones y pérdida de puntos"))
    B += _under(b9, "3.2 Offences")
    B.append(BOX("key", f"{TWO[0]}: helmet, gloves and devices", f"{TWO[1]}: casco, guantes y dispositivos", [
        ("Riding <b>without a helmet</b>, or with it unfastened: <b>4 points</b>. If it is the <b>passenger</b> who has no helmet, the <b>rider</b> answers for it and loses the points.",
         "Circular <b>sin casco</b>, o sin abrocharlo: <b>4 puntos</b>. Si quien no lo lleva es el <b>pasajero</b>, responde el <b>conductor</b> y es quien pierde los puntos."),
        ("Since <b>1 October 2026</b> the rule on helmets (art. 118 of the Reglamento General de Circulación) also lists <b>protective gloves out of town</b> and <b>closed shoes</b> on every road, for rider and passenger. "
         "Going without them is a <b>serious offence: 200 €</b>. The points table speaks of the “helmet and <b>other compulsory protective elements</b>”, but the DGT has not said clearly whether gloves and shoes also cost the 4 points.",
         "Desde el <b>1 de octubre de 2026</b> la norma de los cascos (art. 118 del Reglamento General de Circulación) incluye también <b>guantes de protección en vías interurbanas</b> y <b>calzado cerrado</b> en todas las vías, para conductor y pasajero. "
         "No llevarlos es <b>infracción grave: 200 €</b>. La tabla de puntos habla del «casco y <b>demás elementos de protección obligatorios</b>», pero la DGT no ha aclarado si guantes y calzado también restan los 4 puntos."),
        ("A <b>phone held between helmet and head</b>, or headphones connected to a sound device: <b>3 points</b>. Holding the <b>phone in your hand</b>: <b>6 points</b>. "
         "<b>Certified wireless devices built into the helmet</b> are allowed, for <b>intercom or navigation</b> only and as long as they do not affect safety.",
         "Llevar el <b>móvil sujeto entre el casco y la cabeza</b>, o auriculares conectados a un aparato de sonido: <b>3 puntos</b>. <b>Sujetar el móvil con la mano</b>: <b>6 puntos</b>. "
         "Los <b>dispositivos inalámbricos certificados u homologados integrados en el casco</b> están permitidos, solo para <b>intercomunicación o navegación</b> y siempre que no afecten a la seguridad."),
    ]))
    B.append(H3("Speeding: fine and points", "Exceso de velocidad: multa y puntos"))
    B += _under(b9, "Speeding")
    B.append(H3("3.3 Road-safety courses", "3.3 Cursos de sensibilización y reeducación vial"))
    B += _under(b9, "3.3 Road-safety")

    # ---------------------------------------------------------------- 4. liability
    B.append(H2("4", "Who is liable for an offence", "Responsabilidad de las infracciones"))
    B += _under(b9, "Who is liable")

    # ---------------------------------------------------------------- 5. traps
    B.append(H2("5", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("Ages: AM <b>15</b>, A1 <b>16</b>, A2 <b>18</b>, A <b>20</b>, trikes over 15 kW <b>21</b>.", "Edades: AM <b>15</b>, A1 <b>16</b>, A2 <b>18</b>, A <b>20</b>, triciclos de más de 15 kW <b>21</b>."),
        ("A1: <b>125 cc and 11 kW and 0.1 kW/kg</b>, all three. A2: <b>35 kW and 0.2 kW/kg</b>, and if limited, from <b>no more than twice</b> its power (35 kW → at most 70 kW).",
         "A1: <b>125 c.c. y 11 kW y 0,1 kW/kg</b>, las tres. A2: <b>35 kW y 0,2 kW/kg</b>, y si está limitada, desde <b>no más del doble</b> (35 kW → como máximo 70 kW)."),
        ("A = <b>2 years with A2 + training</b>, no new exam. There is no direct route to the A.", "A = <b>2 años con el A2 + formación</b>, sin examen nuevo. No hay acceso directo al A."),
        ("B + <b>more than 3 years</b> = A1 <b>motorcycles</b>, <b>in Spain only</b>.", "B + <b>más de 3 años</b> = <b>motocicletas</b> del A1, <b>solo en España</b>."),
        ("Renewal: every <b>10 years</b>, every <b>5</b> from age 65. An expired licence is <b>withdrawn on the spot</b>.", "Renovación: cada <b>10 años</b>; cada <b>5</b> desde los 65. Un permiso caducado se <b>interviene en el acto</b>."),
        ("V-13 “L”: <b>first year</b>, on a motorcycle <b>somewhere visible at the rear</b>; not needed if you have held another licence for a year.", "V-13 «L»: <b>primer año</b>; en moto, en un <b>sitio visible de la parte posterior</b>; no hace falta si has tenido otro permiso durante un año."),
        ("Deadlines: licence data <b>15 days</b>; owner’s address <b>15 days</b>; seller <b>10 days</b>; buyer <b>30 days</b>; overdue ITV slip <b>10 days</b>.", "Plazos: datos del permiso <b>15 días</b>; domicilio del titular <b>15 días</b>; vendedor <b>10 días</b>; comprador <b>30 días</b>; volante de ITV <b>10 días</b>."),
        ("ITV: two-wheel moped from <b>3 years</b>, motorcycle from <b>4 years</b>, then <b>every 2 years</b>. Unfavourable: <b>you may ride to the workshop</b>; negative: <b>tow truck</b> only.",
         "ITV: ciclomotor de dos ruedas desde los <b>3 años</b>, moto desde los <b>4</b>, después <b>cada 2 años</b>. Desfavorable: <b>se puede ir al taller</b>; negativa: <b>solo en grúa</b>."),
        ("One plate, <b>at the rear</b>. V-19 without a windscreen: somewhere <b>visible</b>.", "Una placa, <b>detrás</b>. V-19 sin parabrisas: en un sitio <b>visible</b>."),
        ("The compulsory insurance pays your <b>passenger’s injuries</b>, never <b>yours</b> nor your motorcycle.", "El seguro obligatorio paga las <b>lesiones de tu pasajero</b>, nunca las <b>tuyas</b> ni tu moto."),
        ("Passenger without a helmet or under the minimum age: the <b>rider</b> is liable.", "Pasajero sin casco o sin la edad mínima: responde el <b>conductor</b>."),
        ("At most <b>8 points a day</b>, unless there is a very serious offence. Phone <b>in hand</b> = 6 points; phone <b>inside the helmet</b> = 3.", "Como máximo <b>8 puntos al día</b>, salvo infracción muy grave. Móvil <b>en la mano</b> = 6 puntos; móvil <b>dentro del casco</b> = 3."),
        ("Partial course: up to <b>4 points</b>, once every <b>2 years</b>. Licence regained: <b>8 points</b>, same class and seniority.", "Curso parcial: hasta <b>4 puntos</b>, una vez cada <b>2 años</b>. Permiso recuperado: <b>8 puntos</b>, misma clase y antigüedad."),
    ]))

    # ---------------------------------------------------------------- 6. numbers
    B.append(H2("6", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Minimum age AM / A1 / A2 / A", "Edad mínima AM / A1 / A2 / A"), T("15 / 16 / 18 / 20 (trikes over 15 kW: 21)", "15 / 16 / 18 / 20 (triciclos de más de 15 kW: 21)")],
            [T("A1 motorcycle", "Moto del A1"), T("≤ 125 cc, ≤ 11 kW, ≤ 0.1 kW/kg; trikes ≤ 15 kW", "≤ 125 c.c., ≤ 11 kW, ≤ 0,1 kW/kg; triciclos ≤ 15 kW")],
            [T("A2 motorcycle", "Moto del A2"), T("≤ 35 kW, ≤ 0.2 kW/kg, original ≤ 2 × its power", "≤ 35 kW, ≤ 0,2 kW/kg, original ≤ 2 × su potencia")],
            [T("From A2 to A", "Del A2 al A"), T("2 years of experience + training", "2 años de experiencia + formación")],
            [T("B and 125 cc motorcycles", "B y motos de 125 c.c."), T("B held for more than 3 years, in Spain", "B con más de 3 años, en España")],
            [T("Validity of AM, A1, A2, A", "Vigencia de AM, A1, A2, A"), T("10 years; 5 years from 65", "10 años; 5 años desde los 65")],
            [T("Novice “L” plate", "Señal «L»"), T("first year; motorcycle plate 10 × 13 cm", "primer año; placa de moto de 10 × 13 cm")],
            [T("Change of licence data / owner’s address", "Cambio de datos del permiso / domicilio del titular"), T("15 days", "15 días")],
            [T("Sale: seller / buyer", "Venta: vendedor / comprador"), T("10 days / 30 days", "10 días / 30 días")],
            [T("First ITV: two-wheel moped / motorcycle", "Primera ITV: ciclomotor de dos ruedas / motocicleta"), T("3 years / 4 years, then every 2", "3 años / 4 años, después cada 2")],
            [T("ITV early / overdue slip / repairs", "ITV adelantada / volante / reparación"), T("up to 30 days / 10 days / up to 2 months", "hasta 30 días / 10 días / hasta 2 meses")],
            [T("Points: standard / new licence / maximum", "Puntos: normal / permiso nuevo / máximo"), T("12 / 8 / 15", "12 / 8 / 15")],
            [T("Most points lost in one day", "Máximo de puntos perdidos en un día"), T("8 (unless a very serious offence)", "8 (salvo infracción muy grave)")],
            [T("Courses: partial / licence", "Cursos: parcial / recuperación del permiso"), T("10 h, up to 4 points / 20 h + test, 8 points", "10 h, hasta 4 puntos / 20 h + test, 8 puntos")],
            [T("Gloves out of town, closed shoes (since 1-10-2026)", "Guantes en interurbanas, calzado cerrado (desde 1-10-2026)"), T("200 € fine", "200 € de multa")],
        ],
        widths=["52%", "48%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["dc2", "cl2", "cl6", "a2a", "cl9", "nv2", "vd2", "it2", "it7", "in3", "pt3", "lb2"]


def quiz():
    from .bank import BANK
    by_id = {q["id"]: q for q in BANK}
    out = []
    for i, qid in enumerate(QUIZ_IDS):
        q = by_id[qid]
        opts = [T(o["en"], o["es"]) for o in q["o"]]
        k = i % 3
        order = opts[1:]
        order.insert(k, opts[0])
        out.append((T(q["q"]["en"], q["q"]["es"]), order, k, T(q["why"]["en"], q["why"]["es"])))
    return out


SOURCES = [s for s in B9.SOURCES if "Código Penal" not in s[0] and "VMP" not in s[0] and "518/2026" not in s[0]] + [
    ("Real Decreto 518/2026 (reform of the Reglamento General de Circulación: gloves and closed shoes on motorcycles, habitual driver; in force 1 October 2026)", "https://www.boe.es/buscar/doc.php?id=BOE-A-2026-13889"),
]

GLOSSARY = [g for g in B9.GLOSSARY if g[0] not in ("delito contra la seguridad vial", "trabajos en beneficio de la comunidad")] + [
    ("relación potencia/peso", "power-to-weight ratio"),
    ("motocicleta limitada", "restricted (power-limited) motorcycle"),
    ("formación (para el permiso A)", "training course (for the A licence)"),
    ("guantes de protección · calzado cerrado", "protective gloves · closed shoes"),
    ("intercomunicador del casco", "helmet intercom"),
]
