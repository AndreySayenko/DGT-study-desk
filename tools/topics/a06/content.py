# -*- coding: utf-8 -*-
"""Category A1/A2, Topic 6 content (carrying people and goods), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Manual Permiso A1/A2, Tema 6: Transporte de personas y
mercancías). The wording and two figures are original; one figure is shared with Category B, Topic 6 and one with
A1/A2, Topic 3. The rules come from the Reglamento General de Circulación (RD 1428/2003, arts. 9, 12, 14, 15 and 118)
and the Reglamento General de Vehículos (annexes XI and XII) as amended by RD 518/2026, as they stand in November 2026.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import moto_passenger, moto_load, trailer_rule, moto_plates


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Who may ride <b>behind you</b> (one passenger, 12 years old, or 7 with a parent), what you both must <b>wear</b>, how a <b>load</b> goes on a motorcycle "
         "(0.25 m behind, 0.50 m each side of the axis, nothing in front), the <b>trailer</b> rule and the <b>signs</b> carried on vehicles.",
         "Quién puede ir <b>detrás de ti</b> (un pasajero, de 12 años, o de 7 con su padre o madre), qué debéis <b>llevar puesto</b>, cómo va la <b>carga</b> en la moto "
         "(0,25 m detrás, 0,50 m a cada lado del eje, nada delante), la norma del <b>remolque</b> y las <b>señales</b> en los vehículos."),
        ("New since <b>1 October 2026</b>: riders and passengers need, besides the helmet, <b>protective gloves</b> on interurban roads and <b>closed shoes</b> on every road, "
         "and every motorcycle carries a <b>high-visibility vest</b>. Your course only mentions the helmet.",
         "Novedad desde el <b>1 de octubre de 2026</b>: conductor y pasajero necesitan, además del casco, <b>guantes de protección</b> en vías interurbanas y <b>calzado cerrado</b> en todas las vías, "
         "y toda moto lleva un <b>chaleco de alta visibilidad</b>. Tu curso solo menciona el casco."),
    ]))

    # ---------------------------------------------------------------- 1. people
    B.append(H2("1", "Carrying people", "Transporte de personas"))
    B.append(P(
        "You may not carry <b>more people than there are seats</b>, nor exceed the vehicle’s <b>MMA</b>, so count the weight of the people too. "
        "The number of seats and the MMA are shown on the <b>inspection card</b> (<i>tarjeta ITV</i>) or the <b>registration certificate</b> (<i>permiso de circulación</i>).",
        "El número de personas transportadas no puede superar el <b>número de plazas</b>, ni se puede superar la <b>MMA</b> del vehículo, por lo que cuenta también el peso de las personas. "
        "Las plazas y la MMA se consultan en la <b>tarjeta de inspección técnica</b> o en el <b>permiso de circulación</b>."))
    B.append(FIG(moto_passenger, "Besides the rider (and the sidecar passenger, if any), at most one passenger, and only on these conditions.",
                 "Además del conductor (y del ocupante del sidecar, en su caso), como máximo un pasajero, y solo con estas condiciones."))
    B.append(TABLE(
        [T("Motorcycles and mopeds: one passenger, if…", "Motocicletas y ciclomotores: un pasajero, si…")],
        [
            [T("The <b>registration document</b> (licence or permiso de circulación) allows it.", "<b>Consta</b> en la licencia o el permiso de circulación del vehículo.")],
            [T("The passenger is <b>over 12</b>. <b>Exceptionally</b>, <b>over 7</b> if the rider is their <b>father, mother, guardian</b> or an <b>adult authorised</b> by them.",
               "El pasajero es <b>mayor de 12 años</b>. <b>Excepcionalmente</b>, <b>mayor de 7</b> si conduce su <b>padre, madre, tutor</b> o una <b>persona mayor de edad autorizada</b> por ellos.")],
            [T("They sit on the seat <b>behind the rider</b> — <b>never</b> between the rider and the handlebar, <b>not even a child</b>.", "Utiliza el asiento <b>detrás del conductor</b>; <b>nunca</b> entre el conductor y el manillar, <b>ni siquiera un niño</b>.")],
            [T("They ride <b>astride</b> (one leg each side), with their <b>feet on the side footrests</b>, and wear an approved <b>helmet</b>.", "Va <b>a horcajadas</b> (una pierna a cada lado), con los <b>pies en los reposapiés laterales</b>, y lleva <b>casco homologado</b>.")],
        ],
    ))
    B.append(BOX("key", "What riders and passengers must wear (since 1 October 2026)", "Qué deben llevar conductor y pasajero (desde el 1 de octubre de 2026)", [
        ("Who: riders and passengers of <b>motorcycles</b> (with or without sidecar), <b>three-wheelers and quadricycles</b>, <b>mopeds</b> and special vehicles of the <b>quad</b> type.",
         "Quiénes: conductores y pasajeros de <b>motocicletas</b> (con o sin sidecar), <b>vehículos de tres ruedas y cuadriciclos</b>, <b>ciclomotores</b> y vehículos especiales tipo <b>quad</b>."),
        ("<b>Helmet</b> approved to <b>UNECE R22</b>, properly <b>fastened</b>, on <b>every road</b>. Moped users may keep using <b>certified</b> helmets until <b>1 October 2027</b>.",
         "<b>Casco</b> homologado según el <b>Reglamento UNECE R22</b>, correctamente <b>abrochado</b>, en <b>todas las vías</b>. En ciclomotor se pueden seguir usando cascos <b>certificados</b> hasta el <b>1 de octubre de 2027</b>."),
        ("<b>Protective gloves</b> on <b>interurban roads</b>, and <b>closed shoes</b> covering the whole foot on <b>every road</b>.",
         "<b>Guantes de protección</b> en <b>vías interurbanas</b>, y <b>calzado cerrado</b> que cubra todo el pie en <b>todas las vías</b>."),
        ("If the vehicle has a <b>protective structure</b> and <b>seat belts</b>, and the inspection card (or the moped’s certificate) says so, occupants are exempt from the helmet, gloves and shoes rule and <b>wear the seat belt</b> instead.",
         "Si el vehículo tiene <b>estructura de autoprotección</b> y <b>cinturones</b>, y así consta en la tarjeta ITV (o en el certificado de características del ciclomotor), sus ocupantes quedan exentos de casco, guantes y calzado y deben <b>usar el cinturón</b>."),
    ]))
    B.append(E(
        "The high-visibility vest", "El chaleco de alta visibilidad",
        "Every motorcycle must <b>carry</b> a certified high-visibility vest. Wear it when you <b>get off</b> and walk on the carriageway or shoulder of an <b>interurban road</b>. "
        "Riders who <b>work</b> on a motorcycle, moped, three-wheeler, quadricycle, quad, bicycle or VMP (deliveries, for example) wear it <b>at all times, on every road</b>.",
        "Toda motocicleta debe <b>llevar</b> un chaleco reflectante de alta visibilidad certificado. Se usa al <b>bajarse</b> y ocupar la calzada o el arcén de una <b>vía interurbana</b>. "
        "Quien <b>trabaja</b> circulando en moto, ciclomotor, tres ruedas, cuadriciclo, quad, bicicleta o VMP (repartidores, por ejemplo) lo lleva <b>siempre, en todas las vías</b>.",
        pills_=[T("carry it", "llevarlo siempre"), T("wear it off the bike, interurban", "ponérselo al bajar, en interurbana")]))

    # ---------------------------------------------------------------- 2. goods
    B.append(H2("2", "Carrying goods", "Transporte de mercancías"))
    B.append(H3("2.1 How to place the load", "2.1 ¿Cómo se coloca la carga?"))
    B.append(TABLE(
        [T("The load and its accessories must be placed (and tied down if needed) so that they cannot…", "La carga y los accesorios para su acondicionamiento deben colocarse (y sujetarse si es necesario) de forma que no puedan…")],
        [
            [T("<b>compromise the stability</b> of the vehicle;", "<b>comprometer la estabilidad</b> del vehículo;")],
            [T("<b>hide</b> the lights, the number plates or compulsory badges, or the rider’s <b>arm signals</b>;", "<b>ocultar</b> los dispositivos luminosos, las placas o distintivos y las <b>advertencias manuales</b> del conductor;")],
            [T("<b>drag, fall</b> or <b>shift</b> dangerously;", "<b>arrastrar, caer</b> o <b>desplazarse</b> de forma peligrosa;")],
            [T("make <b>noise, dust</b> or other avoidable nuisance (a load that makes dust or may fall must be <b>fully covered</b>).", "producir <b>ruido, polvo</b> u otras molestias evitables (si produce polvo o puede caer, debe <b>cubrirse total y eficazmente</b>).")],
        ],
    ))
    B.append(FIG(moto_load, "On a two-wheeled motorcycle the load goes on the central rear rack or in two side cases fixed to the frame.",
                 "En la moto de dos ruedas la carga va en el portaequipajes central o en dos maletas laterales fijadas al chasis."))
    B.append(H3("2.2 How far the load may stick out", "2.2 ¿Cuánto puede sobresalir la carga?"))
    B.append(TABLE(
        [T("Vehicle", "Vehículo"), T("Limit", "Límite")],
        [
            [T("<b>Less than 1 m wide</b> (motorcycles, mopeds)", "<b>Anchura inferior a 1 m</b> (motos, ciclomotores)"),
             T("<b>Rear</b>: 0.25 m · <b>each side</b> of the long axis: 0.50 m (so the total width, load included, stays within 1 m) · <b>front</b>: nothing.",
               "<b>Detrás</b>: 0,25 m · a <b>cada lado</b> del eje longitudinal: 0,50 m (la anchura total con la carga no supera 1 m) · <b>delante</b>: nada.")],
            [T("Not built only for goods (wider)", "No destinados exclusivamente a mercancías (más anchos)"),
             T("<b>Rear</b> only: <b>10 %</b> of the vehicle’s length if the load is divisible, <b>15 %</b> if it is indivisible.",
               "Solo <b>por detrás</b>: <b>10 %</b> de la longitud del vehículo si la carga es divisible, <b>15 %</b> si es indivisible.")],
        ],
        widths=["34%", "66%"],
    ))
    B.append(H3("2.3 What to do if the load sticks out", "2.3 ¿Qué hacer si la carga sobresale?"))
    B.append(P(
        "Take every precaution to avoid harm to others: <b>protect the end</b> that sticks out to soften any rub or knock, and <b>signal</b> it: "
        "by day in clear weather, a <b>V-20 panel</b> at the rear; at night or in poor visibility, the panel <b>plus a red light</b>.",
        "Hay que adoptar las precauciones necesarias para evitar daños o peligros: <b>resguardar la extremidad saliente</b> para aminorar los efectos de un roce o choque, y <b>señalizarla</b>: "
        "de día y con tiempo claro, un <b>panel V-20</b> en la parte trasera; de noche o con poca visibilidad, además del panel, <b>una luz roja</b>."))
    B.append(BOX("trap", "Motorcycles don’t need the V-20", "La moto no necesita la V-20", [
        ("On vehicles <b>less than 1 m wide</b> a load sticking out at the rear does <b>not</b> need to be signalled.", "En los vehículos de <b>anchura inferior a 1 m</b> <b>no</b> es necesario señalizar la carga que sobresale por detrás."),
    ]))
    B.append(H3("2.4 Towing a trailer", "2.4 Arrastrar un remolque"))
    B.append(E(
        "Motorcycles, three-wheelers and mopeds", "Motocicletas, vehículos de tres ruedas y ciclomotores",
        "They may tow a trailer or semitrailer whose mass is <b>no more than 50 %</b> of the towing vehicle’s <b>unladen mass</b>, if: they travel <b>by day</b> with good visibility; "
        "their generic out-of-town speed is <b>reduced by 10 %</b>; and <b>nobody</b> rides in the trailer. In towns, local bylaws apply.",
        "Pueden arrastrar un remolque o semirremolque cuya masa <b>no supere el 50 %</b> de la <b>masa en vacío</b> del vehículo tractor, si: circulan <b>de día</b> y sin visibilidad reducida; "
        "<b>reducen un 10 %</b> sus velocidades genéricas fuera de poblado; y <b>en ningún caso</b> transportan personas en el remolque. En poblado, lo que digan las ordenanzas municipales.",
        pills_=[T("≤ 50 % unladen mass", "≤ 50 % de la masa en vacío"), T("−10 % speed", "−10 % de velocidad")],
        tip=("Your course also lists cycles. Since 1 October 2026 bicycles have their own trailer rules and are no longer in this list.",
             "Tu curso incluye también los ciclos. Desde el 1 de octubre de 2026 las bicicletas tienen sus propias normas de remolque y ya no figuran en esta lista.")))
    B.append(FIG(trailer_rule, "The 10 % comes off the generic maximum for that vehicle on that road (Topic 3).",
                 "El 10 % se resta de la máxima genérica de ese vehículo en esa vía (Tema 3)."))

    # ---------------------------------------------------------------- 3. signs on vehicles
    B.append(H2("3", "Signs on vehicles", "Señales en los vehículos"))
    B.append(P("These signs tell other road users something about the vehicle, the service it provides, its load or its driver, so they can take the right precautions.",
               "Estas señales informan a los demás usuarios de circunstancias o características del vehículo, del servicio que presta, de su carga o de su conductor, para que adopten las precauciones necesarias."))
    B.append(FIG(moto_plates, "Simplified drawings of the ten signs in your course.", "Dibujos simplificados de las diez señales de tu curso."))
    B.append(TABLE(
        [T("Sign", "Señal"), T("What it means · where it goes", "Qué indica · dónde se coloca")],
        [
            [T("<b>V-1</b> Priority vehicle", "<b>V-1</b> Vehículo prioritario"), T("Police, fire, civil protection and rescue, or medical assistance on <b>urgent service</b>. One or more <b>blue</b> lights.",
                                                                                  "Policía, extinción de incendios, protección civil y salvamento o asistencia sanitaria en <b>servicio urgente</b>. Una o varias luces <b>azules</b>.")],
            [T("<b>V-2</b> Vehicle-obstacle", "<b>V-2</b> Vehículo-obstáculo en la vía"), T("<b>Amber</b> light(s): a vehicle doing a service or work on or by the road, <b>stopped, parked</b> or at <b>≤ 40 km/h</b>; also special transport and its escorts, "
                                                                                        "escorts of sports events, cycling marches and other events, and military columns. They may add red-and-white reflective strips on their outline.",
                                                                                        "Luz o luces <b>amarillo auto</b>: vehículo que presta un servicio, actividad u operación de trabajo, <b>parado, estacionado</b> o a <b>≤ 40 km/h</b>; también transporte especial y sus vehículos piloto, "
                                                                                        "acompañamiento de pruebas deportivas, marchas ciclistas y otros eventos, y columnas militares. Pueden llevar distintivos de franjas rojas y blancas en su contorno.")],
            [T("<b>V-6</b> Long vehicle", "<b>V-6</b> Vehículo largo"), T("Vehicle or combination longer than <b>12 m</b>.", "Vehículo o conjunto de longitud superior a <b>12 m</b>.")],
            [T("<b>V-13</b> Novice driver", "<b>V-13</b> Conductor novel"), T("Licence held for <b>less than a year</b>. At the <b>rear left</b>, visible (13 × 10 cm on motorcycles).",
                                                                            "Permiso con <b>menos de un año</b> de antigüedad. En la <b>parte posterior izquierda</b>, visible (13 × 10 cm en motocicletas).")],
            [T("<b>V-16</b> Warning device", "<b>V-16</b> Dispositivo de preseñalización de peligro"), T("The vehicle is <b>immobilised on the carriageway</b>, or its load has fallen onto it. Since <b>1 January 2026</b> only the connected V-16 is valid; the <b>triangles</b> no longer count. "
                                                                                                      "Compulsory for cars, vans, buses and lorries; <b>recommended, not compulsory</b>, for motorcycles.",
                                                                                                      "El vehículo ha quedado <b>inmovilizado en la calzada</b> o su carga está sobre ella. Desde el <b>1 de enero de 2026</b> solo vale la V-16 conectada; los <b>triángulos</b> ya no sirven. "
                                                                                                      "Obligatoria en turismos, furgonetas, autobuses y camiones; en motocicletas, <b>recomendable, no obligatoria</b>.")],
            [T("<b>V-19</b> ITV badge", "<b>V-19</b> Distintivo de ITV"), T("The vehicle has passed its periodic <b>inspection</b>; shows when the next one is due.", "Ha superado la <b>inspección técnica periódica</b>; indica la fecha de la próxima.")],
            [T("<b>V-20</b> Overhanging load panel", "<b>V-20</b> Panel para cargas que sobresalen"), T("The load sticks out <b>at the rear</b> (not needed on vehicles under 1 m wide).", "La carga <b>sobresale por detrás</b> (no hace falta en vehículos de menos de 1 m de ancho).")],
            [T("<b>V-25</b> Environmental label", "<b>V-25</b> Distintivo ambiental"), T("<b>0 emisiones, ECO, C or B</b>. With a windscreen: lower right corner, inside; otherwise somewhere clearly visible. "
                                                                                    "On <b>motorcycles</b> it is <b>recommended</b> on the screen or another visible place, <b>not compulsory</b>.",
                                                                                    "<b>0 emisiones, ECO, C o B</b>. Con parabrisas: ángulo inferior derecho, por dentro; si no, en sitio bien visible. "
                                                                                    "En <b>motocicletas</b> se <b>recomienda</b> en la cúpula o en otro lugar visible; <b>no es obligatorio</b>.")],
            [T("<b>V-26</b> Shared use", "<b>V-26</b> Distintivo de uso compartido"), T("Self-drive rental vehicle used one after another by many users within a set zone. Same place as the V-25.",
                                                                                    "Vehículo de alquiler sin conductor de uso concatenado por un número indeterminado de usuarios en una zona delimitada. Mismo lugar que la V-25.")],
            [T("<b>VEH 21/05</b> Blind-spot sticker", "<b>VEH 21/05</b> Advertencia de ángulos muertos"), T("<b>Voluntary</b> sticker warning <b>vulnerable users</b> — pedestrians, cyclists and also <b>motorcyclists</b> — of the blind spots of large vehicles. "
                                                                                                     "Three per vehicle: one each side within the first metre from the front, one at the rear right (refuse trucks: two at the rear).",
                                                                                                     "Señal adhesiva <b>voluntaria</b> que advierte a los <b>usuarios vulnerables</b> (peatones, ciclistas y también <b>motoristas</b>) de los ángulos muertos de los vehículos grandes. "
                                                                                                     "Tres por vehículo: una a cada lado en el primer metro desde la parte delantera y una detrás a la derecha (vehículos de residuos: dos detrás).")],
        ],
        widths=["28%", "72%"],
        cls="small",
    ))

    # ---------------------------------------------------------------- 4. traps
    B.append(H2("4", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("Passenger: <b>over 12</b>; <b>over 7</b> only with father, mother, guardian or an authorised adult.", "Pasajero: <b>mayor de 12</b>; <b>mayor de 7</b> solo con padre, madre, tutor o adulto autorizado."),
        ("A child may <b>never</b> sit between the rider and the handlebar.", "Un niño <b>nunca</b> puede ir entre el conductor y el manillar."),
        ("Astride, feet on the footrests — riding side-saddle is not allowed.", "A horcajadas y con los pies en los reposapiés: no se puede ir de lado."),
        ("Helmet everywhere; <b>gloves only on interurban roads</b>; closed shoes everywhere.", "Casco en todas las vías; <b>guantes solo en interurbanas</b>; calzado cerrado en todas."),
        ("A quadricycle with a protective structure and belts on its ITV card: <b>seat belt</b> instead of helmet.", "Cuadriciclo con estructura de autoprotección y cinturones en la ITV: <b>cinturón</b> en lugar de casco."),
        ("Under 1 m wide: <b>0.25 m</b> rear, <b>0.50 m</b> each side of the axis, <b>0</b> in front, and <b>no V-20</b>.", "Menos de 1 m de ancho: <b>0,25 m</b> detrás, <b>0,50 m</b> a cada lado del eje, <b>0</b> delante y <b>sin V-20</b>."),
        ("10 % / 15 % rear overhang is for wider vehicles not built only for goods.", "El 10 % / 15 % por detrás es para vehículos más anchos no destinados solo a mercancías."),
        ("Trailer: ≤ 50 % of the <b>unladen</b> mass, by day, <b>−10 %</b> (not −10 km/h), nobody in it.", "Remolque: ≤ 50 % de la masa <b>en vacío</b>, de día, <b>−10 %</b> (no −10 km/h) y sin personas."),
        ("V-1 blue = priority; V-2 amber = obstacle or slow work vehicle (≤ 40 km/h).", "V-1 azul = prioritario; V-2 amarillo auto = obstáculo o vehículo de trabajo lento (≤ 40 km/h)."),
        ("V-13 at the <b>rear left</b>; licence held under a year.", "V-13 en la <b>parte posterior izquierda</b>; permiso de menos de un año."),
        ("Triangles no longer count since 1 January 2026; the V-16 is not compulsory on motorcycles.", "Los triángulos ya no valen desde el 1 de enero de 2026; la V-16 no es obligatoria en moto."),
    ]))

    # ---------------------------------------------------------------- 5. numbers
    B.append(H2("5", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Passengers on a motorcycle or moped", "Pasajeros en moto o ciclomotor"), T("1 (plus the sidecar occupant)", "1 (más el ocupante del sidecar)")],
            [T("Passenger’s minimum age", "Edad mínima del pasajero"), T("over 12 · over 7 with parent, guardian or authorised adult", "mayor de 12 · mayor de 7 con padre, madre, tutor o adulto autorizado")],
            [T("Helmet standard", "Norma del casco"), T("UNECE R22", "UNECE R22")],
            [T("Certified helmets on mopeds allowed until", "Cascos certificados en ciclomotor hasta"), T("1 October 2027", "1 de octubre de 2027")],
            [T("Load on vehicles under 1 m wide", "Carga en vehículos de menos de 1 m"), T("rear 0.25 m · side 0.50 m from the axis · front 0", "detrás 0,25 m · lateral 0,50 m del eje · delante 0")],
            [T("Rear overhang, other vehicles not only for goods", "Voladizo trasero, otros no exclusivos de mercancías"), T("10 % divisible · 15 % indivisible", "10 % divisible · 15 % indivisible")],
            [T("Trailer", "Remolque"), T("≤ 50 % unladen mass · −10 % speed", "≤ 50 % de la masa en vacío · −10 % de velocidad")],
            [T("V-2 slow work vehicle", "V-2 vehículo de trabajo lento"), T("≤ 40 km/h", "≤ 40 km/h")],
            [T("V-6 long vehicle", "V-6 vehículo largo"), T("&gt; 12 m", "&gt; 12 m")],
            [T("V-13 novice", "V-13 novel"), T("licence &lt; 1 year · 13 × 10 cm on motorcycles", "permiso &lt; 1 año · 13 × 10 cm en motos")],
        ],
        widths=["50%", "50%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
QUIZ_IDS = ["pp1", "pp3", "eq1", "eq3", "ld1", "oh1", "oh3", "tr1", "tr3", "vp1", "vp4", "vp6"]


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


SOURCES = [
    ("Reglamento General de Circulación (RD 1428/2003), arts. 12 (passengers and trailers), 14–15 (loads) and 118 (helmet, gloves, shoes, vest) — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Real Decreto 518/2026 (BOE 26-06-2026): gloves and closed shoes, vest on motorcycles, trailer rule, transitional period for certified moped helmets; in force 1 October 2026", "https://www.boe.es/boe/dias/2026/06/26/pdfs/BOE-A-2026-13889.pdf"),
    ("Reglamento General de Vehículos (RD 2822/1998), annex XI (signs on vehicles) and annex XII (equipment) — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-1999-1826"),
]

GLOSSARY = [
    ("plaza · número de plazas", "seat · seating capacity"),
    ("tarjeta de inspección técnica (ITV)", "vehicle inspection card"),
    ("permiso / licencia de circulación", "registration certificate"),
    ("pasajero · ocupante del sidecar", "passenger · sidecar occupant"),
    ("a horcajadas", "astride"),
    ("reposapiés", "footrests"),
    ("manillar", "handlebar"),
    ("casco homologado / certificado", "approved / certified helmet"),
    ("guantes de protección", "protective gloves"),
    ("calzado cerrado", "closed shoes"),
    ("estructura de autoprotección", "protective (roll-over) structure"),
    ("chaleco reflectante de alta visibilidad", "high-visibility vest"),
    ("carga divisible / indivisible", "divisible / indivisible load"),
    ("proyección en planta", "outline seen from above"),
    ("eje longitudinal", "long axis"),
    ("portaequipajes · baúl · maletas laterales", "luggage rack · top case · side cases"),
    ("sobresalir", "to stick out"),
    ("resguardar la extremidad saliente", "to protect the end that sticks out"),
    ("remolque · semirremolque", "trailer · semitrailer"),
    ("masa en vacío", "unladen mass"),
    ("vehículo-obstáculo", "vehicle that is an obstacle on the road"),
    ("conductor novel", "novice driver"),
    ("dispositivo de preseñalización de peligro", "warning device (V-16)"),
    ("distintivo ambiental", "environmental label"),
    ("uso compartido", "shared use (car sharing)"),
    ("ángulo muerto", "blind spot"),
]
