# -*- coding: utf-8 -*-
"""Category A1/A2, Topic 2 content (use of the road), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Manual Permiso A1/A2, Tema 2: Uso de las vías). The wording and
three figures are original; one figure is shared with Category B, Topic 2. The rules come from the Ley sobre Tráfico
(RDL 6/2015) and the Reglamento General de Circulación (RD 1428/2003) as amended by RD 518/2026 (in force since
1 October 2026), and the DGT's 2026 resolution on special traffic measures (VAO lanes), as they stand in November 2026.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import lanes_moto, island_sides, moto_shoulder, distances


def rows(pairs):
    return [[T(a, b)] for a, b in pairs]


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("How to behave on the road and <b>where a motorcycle may ride</b>: which lane, which side of an island or roundabout, which lanes are reserved, "
         "when the <b>hard shoulder</b> is allowed and how much <b>distance</b> to keep.",
         "Cómo comportarse en la vía y <b>por dónde puede circular una moto</b>: qué carril, por qué lado de una isleta o una glorieta, qué carriles están reservados, "
         "cuándo se puede usar el <b>arcén</b> y qué <b>distancia</b> guardar."),
        ("New since <b>1 October 2026</b>: motorcycles may use the <b>right-hand hard shoulder</b> in a jam on signed stretches at up to <b>30 km/h</b>; helmet intercoms remain allowed. "
         "Since <b>January 2026</b>, a car with a 0 emisiones, ECO, C or B label and only the driver aboard may use a <b>VAO</b> lane only when the panels allow it; motorcycles keep their access.",
         "Novedad desde el <b>1 de octubre de 2026</b>: las motos pueden usar el <b>arcén derecho</b> en atascos en tramos señalizados, a <b>30 km/h</b> como máximo; los intercomunicadores del casco siguen permitidos. "
         "Desde <b>enero de 2026</b>, un turismo con etiqueta 0 emisiones, ECO, C o B y solo el conductor puede usar el carril <b>VAO</b> solo si los paneles lo permiten; las motos mantienen su acceso."),
        ("The sections follow the order of your A1/A2 course. <b>Category B, Topic 2</b> covers the same rules from a car driver’s point of view, plus road parts, pedestrians and animals.",
         "Los apartados siguen el orden de tu curso A1/A2. El <b>Tema 2 del permiso B</b> trata las mismas normas desde el punto de vista del turismo, más las partes de la vía, los peatones y los animales."),
    ]))

    # ---------------------------------------------------------------- 1. safe use
    B.append(H2("1", "A safe use of public roads", "Un uso seguro de las vías públicas"))
    B.append(P(
        "The public road is where <b>drivers, pedestrians and animals</b> live together. All of them have rights, duties and prohibitions aimed at the common good — everybody’s safety — "
        "so cooperation between road users is essential.",
        "La <b>vía pública</b> es el espacio donde conviven <b>conductores, peatones y animales</b>. Todos tienen derechos, obligaciones y prohibiciones que buscan el bien común, la seguridad de todos, "
        "por lo que la colaboración entre usuarios es esencial."))
    B.append(TABLE(
        [T("Principle", "Principio"), T("What it means", "Qué significa")],
        [
            [T("<b>Don’t annoy</b> (<i>no molestar</i>)", "<b>No molestar</b>"), T("Breaking rules and signs or lacking courtesy annoys others. Respect the rules; be considerate, polite and respectful.", "Se molesta incumpliendo normas y señales o faltando a la cortesía. Respetar las normas y ser solidario, educado y respetuoso.")],
            [T("<b>Don’t surprise</b> (<i>no sorprender</i>)", "<b>No sorprender</b>"), T("No sudden manoeuvres without warning. Warn early and clearly so others can react.", "Nada de maniobras súbitas sin aviso. Avisar con antelación y claridad para que los demás reaccionen.")],
            [T("<b>Warn</b> (<i>advertir</i>)", "<b>Advertir</b>"), T("Signal manoeuvres early so they are seen and understood. <b>Signalling does not give you the right</b> to make the manoeuvre: you must still do it correctly and safely.",
                                                                  "Señalizar las maniobras con antelación para que se perciban y entiendan. <b>Advertir no da derecho</b> a realizar la maniobra: hay que hacerla correctamente y sin peligro.")],
            [T("<b>Understand</b> (<i>comprender</i>)", "<b>Comprender</b>"), T("Understand others’ warnings and forgive their mistakes — without excusing your own or turning aggressive.", "Comprender las advertencias ajenas y disculpar sus errores, sin justificar los propios ni adoptar un comportamiento agresivo.")],
        ],
        widths=["28%", "72%"],
    ))
    B.append(H3("1.1 The driver’s duties", "1.1 Obligaciones del conductor"))
    B.append(TABLE(
        [T("Duty", "Obligación")],
        rows([
            ("Drive with <b>care and caution</b> to avoid any harm, to yourself or others. Riding <b>negligently or recklessly</b> is strictly prohibited, and so is riding where it is not allowed, such as <b>pavements</b>. "
             "<b>Don’t zigzag</b>, especially in heavy traffic.",
             "Conducir con <b>diligencia y precaución</b> para evitar todo daño, propio o ajeno. Prohibido conducir de modo <b>negligente o temerario</b> y circular por espacios no permitidos, como las <b>aceras</b>. "
             "<b>No se debe circular en zigzag</b>, especialmente con el tráfico saturado."),
            ("Be able to <b>control your vehicle</b> at all times and take <b>extra care</b> near other road users, especially <b>children, elderly people, blind people</b> and people with reduced mobility.",
             "Estar en condiciones de <b>controlar el vehículo</b> y adoptar las <b>precauciones necesarias</b> al acercarse a otros usuarios, sobre todo <b>niños, ancianos, invidentes</b> y personas con movilidad reducida."),
            ("Keep your own <b>freedom of movement</b>, the <b>field of vision</b> you need and <b>constant attention</b>: a proper position for you and your passenger, and objects carried properly placed.",
             "Mantener la propia <b>libertad de movimientos</b>, el <b>campo de visión</b> necesario y la <b>atención permanente</b>: posición adecuada del conductor y del pasajero, y objetos bien colocados."),
        ]),
    ))
    B.append(H3("1.2 What the driver must not do", "1.2 Prohibiciones del conductor"))
    B.append(TABLE(
        [T("Device", "Dispositivo"), T("Rule", "Norma")],
        [
            [T("<b>Screens</b>", "<b>Pantallas</b>"), T("Screens with <b>internet</b>, TV monitors and video/DVD players are incompatible with constant attention while moving. Allowed: rear manoeuvring cameras, monitors for passengers getting on and off, and the <b>GPS</b> — <b>not handled while moving</b>.",
                                                     "Incompatibles con la atención permanente, con el vehículo en movimiento, las <b>pantallas con internet</b>, monitores de TV y reproductores de vídeo o DVD. Se permiten las cámaras de maniobra traseras, los monitores de acceso de pasajeros y el <b>GPS</b>, <b>sin manipularlo en marcha</b>.")],
            [T("<b>Mobile phone</b>", "<b>Teléfono móvil</b>"), T("Using a phone or other communication device while riding is prohibited — <b>even just holding it in your hand</b>. Allowed only <b>without using your hands</b> and without headphones or similar. Traffic agents on duty are exempt.",
                                                                 "Prohibido usar el móvil u otro medio de comunicación conduciendo, <b>incluso sujetándolo con la mano aunque no se use</b>. Solo se permite <b>sin emplear las manos</b> ni usar cascos, auriculares o similares. Exentos los agentes en servicio.")],
            [T("<b>Headphones and earphones</b>", "<b>Cascos y auriculares</b>"),
             T("Prohibited when connected to sound devices. <b>Exceptions</b>: lessons and skills tests on open roads for the licence, when the rules require it (in practice, the motorcycle test with radio instructions); "
               "and <b>certified or approved wireless devices built into the helmet</b> of motorcycle and moped riders, <b>only for intercom or navigation</b>, as long as they don’t affect safety.",
               "Prohibido conducir con ellos conectados a aparatos de sonido. <b>Excepciones</b>: la enseñanza y las pruebas de aptitud en circuito abierto para obtener el permiso, cuando lo exija la norma (en la práctica, el examen de moto con instrucciones por radio); "
               "y los <b>dispositivos inalámbricos certificados u homologados integrados en el casco</b> de motoristas y ciclomotoristas, <b>solo para intercomunicación o navegación</b>, siempre que no afecten a la seguridad.")],
        ],
        widths=["22%", "78%"],
    ))
    B.append(BOX("trap", "Helmet intercom: yes. Earphones under the helmet: no", "Intercomunicador del casco: sí. Auriculares bajo el casco: no", [
        ("An approved wireless system <b>built into the helmet</b> for talking or navigation is allowed. Earphones or a phone wedged inside the helmet are not — and a phone held between helmet and head costs <b>3 points</b> (Topic 9 of category B).",
         "Un sistema inalámbrico homologado <b>integrado en el casco</b> para hablar o navegar está permitido. Auriculares o un móvil metido en el casco, no: el móvil sujeto entre el casco y la cabeza supone <b>3 puntos</b> (Tema 9 del permiso B)."),
    ]))
    B.append(H3("1.3 Other prohibitions", "1.3 Otras prohibiciones"))
    B.append(TABLE(
        [T("Prohibited", "Prohibido"), T("Detail", "Detalle")],
        [
            [T("Hindering or endangering others", "Entorpecer o poner en peligro"), T("Don’t obstruct traffic unduly or cause danger, harm or needless nuisance to people or damage to property.", "No entorpecer indebidamente la circulación ni causar peligro, perjuicios o molestias innecesarias a las personas o daños a los bienes.")],
            [T("Throwing or leaving things", "Arrojar o abandonar objetos"), T("Throwing, leaving or dumping on the road or beside it anything that can cause a <b>fire</b> or <b>pollution</b>, damage the road or make it dangerous.", "Arrojar, depositar o abandonar en la vía o sus inmediaciones objetos o materias que puedan producir <b>incendios</b> o <b>contaminación</b>, deteriorar la vía o hacerla peligrosa.")],
            [T("Leaving an obstacle you created", "Dejar un obstáculo creado"), T("Signal the vehicle or obstacle, day and night, and get it <b>removed as soon as possible</b>; take it off the carriageway and park it properly if you can.", "Señalizar el vehículo o el obstáculo, de día y de noche, y <b>retirarlo cuanto antes</b>; sacarlo de la calzada y dejarlo bien estacionado si es posible.")],
            [T("Radar <b>jammers</b> and <b>detectors</b>", "<b>Inhibidores</b> y <b>detectores</b> de radar"), T("Fitting or carrying devices that jam or detect speed cameras, or signalling to dodge them. Apps that only warn where surveillance points are <b>are allowed</b>.",
                                                                                                    "Instalar o llevar mecanismos que interfieran en los cinemómetros o los detecten, o hacer señales con esa finalidad. Los avisadores que solo informan de la posición de los sistemas de vigilancia <b>están permitidos</b>.")],
            [T("Warning others about police", "Avisar de los agentes"), T("Signalling to other road users that traffic agents are present or watching.", "Hacer señales a otros usuarios para advertir de la presencia o vigilancia de los agentes de tráfico.")],
            [T("Noise and gases over the limits", "Ruidos y gases por encima del límite"), T("Electromagnetic interference, noise or gases above the limits — especially riding with an <b>open exhaust</b> (<i>escape libre</i>), without a silencer.", "Perturbaciones electromagnéticas, ruidos, gases u otra contaminación por encima de los límites, en especial circular con <b>escape libre</b>, sin silenciador.")],
            [T("Refuelling carelessly", "Repostar sin precauciones"), T("Refuel with the <b>engine stopped</b>, ignition off, <b>lights off</b>, and radio and <b>mobile phones</b> switched off.", "Repostar con el <b>motor parado</b>, el contacto quitado, las <b>luces apagadas</b> y la radio y los <b>móviles</b> apagados.")],
        ],
        widths=["30%", "70%"],
    ))

    # ---------------------------------------------------------------- 2. lanes
    B.append(H2("2", "Using the lanes", "Utilización de carriles"))
    B.append(P(
        "A motorcycle rides <b>on the carriageway, not on the hard shoulder</b>, except in an emergency. As a rule — and above all in <b>bends and brows with poor visibility</b> — keep <b>as close as possible to the right-hand edge</b>, "
        "leave enough room to pass oncoming traffic safely, and leave the opposite half <b>completely free</b>.",
        "La motocicleta circula <b>por la calzada y no por el arcén</b>, salvo por emergencia. Como norma general, y sobre todo en <b>curvas y cambios de rasante de visibilidad reducida</b>, se circula <b>lo más cerca posible del borde derecho</b>, "
        "con separación lateral suficiente para cruzarse con seguridad y dejando <b>completamente libre</b> la parte del sentido contrario."))
    B.append(BOX("trap", "No weaving", "Nada de zigzag", [("<b>Zigzagging between vehicles</b> and <b>sudden manoeuvres</b> without warning are prohibited.", "Prohibido <b>zigzaguear entre los vehículos</b> y realizar <b>maniobras súbitas</b> sin previo aviso.")]))
    B.append(FIG(lanes_moto, "Two-way roads: right-hand lane (on three lanes, the centre one only to overtake or turn left). One-way out of town: rightmost. One-way in town with marked lanes: the one for your destination.",
                 "Doble sentido: carril derecho (con tres, el central solo para adelantar o girar a la izquierda). Sentido único fuera de poblado: el de más a la derecha. En poblado con carriles marcados: el de tu destino."))
    B.append(TABLE(
        [T("Road", "Vía"), T("Lane to use", "Carril que se usa")],
        [
            [T("<b>Two-way</b>, two lanes (marked or not), in or out of town", "<b>Doble sentido</b>, dos carriles (con o sin marcas), dentro o fuera de poblado"), T("The <b>right-hand lane</b>.", "El <b>carril derecho</b>.")],
            [T("<b>Two-way</b>, three lanes separated by <b>broken lines</b>", "<b>Doble sentido</b>, tres carriles separados por <b>discontinuas</b>"), T("The <b>right-hand lane</b>; the <b>centre lane only to overtake or turn left</b>; never the left-hand one.", "El <b>derecho</b> (nunca el izquierdo); el <b>central solo para adelantar o girar a la izquierda</b>.")],
            [T("<b>Out of town</b>, one way, more than one lane", "<b>Fuera de poblado</b>, sentido único, más de un carril"), T("Normally the <b>rightmost lane</b>; the others to overtake, without hindering anyone behind.", "Normalmente el <b>de más a la derecha</b>; el resto para adelantar, sin entorpecer a quien venga detrás.")],
            [T("<b>In town</b> (urban roads and travesías), one way, lanes <b>marked</b>", "<b>Dentro de poblado</b> (vías urbanas y travesías), sentido único, carriles <b>delimitados</b>"),
             T("The lane that <b>best suits your destination</b>, without hindering others. Leave it only to turn, overtake, stop or park.", "El que <b>mejor convenga a su destino</b>, sin obstaculizar. Solo se abandona para cambiar de dirección, adelantar, parar o estacionar.")],
            [T("<b>In town</b>, one way, lanes <b>not marked</b>", "<b>Dentro de poblado</b>, sentido único, carriles <b>no delimitados</b>"), T("The <b>right-hand lane</b>.", "El <b>carril de la derecha</b>.")],
            [T("Autopista or autovía <b>through urban land</b>", "Autopista o autovía <b>por suelo urbano</b>"), T("<b>Not</b> “best for your destination”: normally the rightmost lane, the rest to overtake.", "<b>No</b> vale el que mejor convenga: normalmente el de más a la derecha y el resto para adelantar.")],
        ],
        widths=["44%", "56%"],
        cls="small",
    ))
    B.append(P("<b>Under no circumstances</b> may motorcycles ride on <b>pavements</b> or other pedestrian areas.", "En <b>ningún caso</b> las motocicletas pueden circular por las <b>aceras</b> y demás zonas peatonales."))

    # ---------------------------------------------------------------- 3. position
    B.append(H2("3", "Position on the carriageway", "Posición en la calzada"))
    B.append(FIG(island_sides, "An island between two directions stays on your left; on a one-way road you may pass either side. In a roundabout, the centre stays on your left.",
                 "Una isleta entre dos sentidos se deja a la izquierda; en sentido único se puede pasar por cualquier lado. En una glorieta, el centro queda a la izquierda."))
    B.append(TABLE(
        [T("Situation", "Situación"), T("Rule", "Norma")],
        [
            [T("Refuges, islands or guide posts <b>separating two directions</b>", "Refugios, isletas o dispositivos de guía que <b>separan dos sentidos</b>"), T("Ride on the part of the carriageway to their <b>right</b>, leaving them on your left.", "Circular por la parte de la calzada a su <b>derecha</b>, dejándolos a la izquierda.")],
            [T("The same on a <b>one-way</b> road, or within one direction’s half", "Lo mismo en vía de <b>sentido único</b> o dentro de la parte de un sentido"), T("<b>Either side</b>.", "Por <b>ambos lados</b>.")],
            [T("Squares, roundabouts and junctions", "Plazas, glorietas e intersecciones"), T("Go round leaving the <b>centre on your left</b>.", "Se circula dejando a la <b>izquierda el centro</b>.")],
            [T("Roundabout on an <b>interurban</b> road, at least two marked lanes", "Glorieta en vía <b>interurbana</b> con al menos dos carriles delimitados"), T("The lane <b>nearest the right</b>; the others only when traffic or the road advise it, without hindering anyone.", "El <b>más próximo a la derecha</b>; el resto cuando lo aconsejen el tráfico o la vía, sin estorbar.")],
            [T("Roundabout on an <b>urban</b> road, at least two marked lanes", "Glorieta en vía <b>urbana</b> con al menos dos carriles delimitados"), T("The lane that <b>best suits your destination</b>. Never cut across a vehicle in an outer lane.", "El que <b>mejor convenga a su destino</b>. No se puede cortar la trayectoria de quien circula por un carril exterior.")],
            [T("Road with <b>two carriageways</b>", "Vía con <b>dos calzadas</b>"), T("The carriageway on the <b>right</b> for your direction.", "La calzada de la <b>derecha</b>, según el sentido de la marcha.")],
            [T("Road with <b>three carriageways</b>", "Vía con <b>tres calzadas</b>"), T("The <b>centre one</b> may carry one or two directions, permanently or at times; the <b>side ones</b>, one direction, unless signed otherwise.", "La <b>central</b> puede ser de uno o dos sentidos, permanente o temporalmente; las <b>laterales</b>, de uno solo, salvo otra señalización.")],
        ],
        widths=["42%", "58%"],
    ))

    # ---------------------------------------------------------------- 4. types of lane
    B.append(H2("4", "Types of lane", "Tipos de carriles"))
    B.append(H3("4.1 Lanes reserved for certain vehicles: VAO", "4.1 Carriles reservados: carril VAO"))
    B.append(P(
        "<b>High-occupancy vehicles</b> (VAO) are automobiles that carry only people, with an <b>MMA up to 3,500 kg</b>, and the number of occupants set for each stretch — as a rule <b>at least two, driver included</b>. "
        "Under the Reglamento, only <b>motorcycles, cars and adaptable mixed vehicles</b> may use the lane. Breaking its rules is a <b>serious</b> offence.",
        "Son <b>vehículos de alta ocupación</b> (VAO) los automóviles destinados solo al transporte de personas, de <b>MMA no superior a 3.500 kg</b>, ocupados por el número de personas fijado para cada tramo (como norma general, <b>mínimo dos, incluido el conductor</b>). "
        "Según el Reglamento, solo pueden usar el carril las <b>motocicletas, turismos y vehículos mixtos adaptables</b>. Incumplir sus normas es infracción <b>grave</b>."))
    B.append(TABLE(
        [T("May use the VAO lane", "Pueden usar el carril VAO"), T("Condition", "Condición")],
        [
            [T("<b>Motorcycles</b> (two or three wheels)", "<b>Motocicletas</b> (dos o tres ruedas)"), T("<b>No passenger needed.</b>", "<b>No es obligatorio llevar acompañante.</b>")],
            [T("Cars and adaptable mixed vehicles", "Turismos y vehículos mixtos adaptables"), T("With the occupants required. Alone only with the <b>V-15</b> sign or the disabled parking card.", "Con los ocupantes exigidos. Solo el conductor, si lleva la señal <b>V-15</b> o la tarjeta de estacionamiento para personas con movilidad reducida.")],
            [T("Buses over 3,500 kg and articulated buses", "Autobuses de más de 3.500 kg y articulados"), T("Whatever the number of occupants.", "Con independencia del número de ocupantes.")],
            [T("Taxis (your course)", "Taxis (según tu curso)"), T("Whatever the number of occupants, where the stretch allows them.", "Con independencia del número de ocupantes, donde el tramo lo permita.")],
            [T("Priority vehicles on urgent service; road-maintenance crews", "Prioritarios en servicio urgente; equipos de mantenimiento"), T("When on duty.", "En servicio.")],
            [T("Cars with a <b>0 emisiones, ECO, C or B</b> label and only the driver", "Turismos con distintivo <b>0 emisiones, ECO, C o B</b> y solo el conductor"),
             T("<b>Only when traffic allows and the variable-message panels at the entrance say so</b> (since January 2026). Your course still says zero-emission cars may always use it — that ended in 2026.",
               "<b>Solo cuando lo permitan el tráfico y los paneles de mensaje variable de acceso</b> (desde enero de 2026). Tu curso dice aún que los 0 emisiones pueden usarlo siempre: eso terminó en 2026.")],
        ],
        widths=["42%", "58%"],
        cls="small",
    ))
    B.append(P("<b>Prohibited</b> in the VAO lane: all other vehicles and combinations, including <b>cars with a trailer</b>, lorries and vans, and also pedestrians, <b>mopeds</b>, cycles, VMP and animals.",
               "<b>Prohibido</b> en el carril VAO: el resto de vehículos y conjuntos, incluidos los <b>turismos con remolque</b>, camiones y furgones, y también peatones, <b>ciclomotores</b>, ciclos, VMP y animales."))
    B.append(H3("4.2 Lanes for certain manoeuvres", "4.2 Carriles reservados a determinadas maniobras"))
    B.append(TABLE(
        [T("Lane", "Carril"), T("How to use it", "Cómo se usa")],
        [
            [T("<b>Acceleration</b> (slip road in)", "<b>Aceleración</b> (de entrada)"), T("Reach the right speed <b>by its end</b> to join safely. At its <b>start</b>, make sure you can merge without danger, given the position, path and speed of the others — <b>stopping if necessary</b>.",
                                                                                         "Alcanzar la velocidad adecuada <b>al final del carril</b> para incorporarse con seguridad. Al <b>principio</b>, cerciorarse de que puede hacerse sin peligro, según la posición, trayectoria y velocidad de los demás, <b>llegando a detenerse si es necesario</b>.")],
            [T("<b>Deceleration</b> (slip road out)", "<b>Deceleración</b> (de salida)"), T("Ride in the lane nearest the exit and enter the deceleration lane <b>as soon as possible</b>; adapt your speed <b>inside it</b>, without hindering or endangering those on the road you are leaving.",
                                                                                          "Circular por el carril más próximo a la salida y entrar en el de deceleración <b>cuanto antes</b>; adaptar la velocidad <b>ya dentro</b>, sin entorpecer ni crear peligro a quienes siguen por la vía que se abandona.")],
        ],
        widths=["28%", "72%"],
    ))
    B.append(H3("4.3 Lanes that improve traffic flow", "4.3 Carriles para mejorar la fluidez del tráfico"))
    B.append(BOX("key", "Memory trick: one rule per word of the name", "Truco: una norma por cada palabra del nombre", [
        ("<b>Reversible</b>: dipped headlights.", "<b>Reversible</b>: luz de cruce."),
        ("<b>Adicional circunstancial</b>: dipped headlights + 60–80 km/h.", "<b>Adicional circunstancial</b>: luz de cruce + 60–80 km/h."),
        ("<b>Sentido contrario al habitual</b>: dipped headlights + 60–80 km/h + only <b>motorcycles</b> and cars without trailer when opened for traffic flow (for roadworks, every vehicle allowed on the road).",
         "<b>Sentido contrario al habitual</b>: luz de cruce + 60–80 km/h + solo <b>motocicletas</b> y turismos sin remolque si es por fluidez (por obras, todos los autorizados en la vía)."),
    ]))
    B.append(TABLE(
        [T("Lane", "Carril"), T("Where", "Dónde"), T("Rules", "Normas")],
        [
            [T("<b>Reversible</b>", "<b>Reversible</b>"), T("Two-way carriageway; a lane bounded by <b>double broken lines on both sides</b>; its direction is set by square <b>lane signals</b> or other means.", "Calzada de doble sentido; carril delimitado por <b>marcas dobles discontinuas a ambos lados</b>; su sentido se regula con <b>semáforos de carril</b> (cuadrados) u otros medios."),
             T("Dipped headlights <b>day and night</b>; never move into the lane on your left.", "Luz de corto alcance <b>de día y de noche</b>; no invadir el carril de su izquierda.")],
            [T("<b>Additional</b> (<i>adicional circunstancial</i>)", "<b>Adicional circunstancial</b>"), T("Two-way carriageway with <b>hard shoulders</b>; temporary signs and cones use both shoulders to make <b>two lanes one way and one the other</b>.", "Calzada de doble sentido con <b>arcenes</b>; con señalización y balizamiento provisionales se usan ambos arcenes para tener <b>dos carriles en un sentido y uno en el otro</b>."),
             T("Lane markings <b>between the wheels</b>; dipped headlights day and night; <b>max 80, min 60 km/h</b> (or less if signed); never cross the line of cones.", "Marcas longitudinales <b>entre las ruedas</b>; luz de cruce de día y de noche; <b>máx. 80, mín. 60 km/h</b> (o menos si se señaliza); sin atravesar la línea de balizamiento.")],
            [T("<b>Contraflow</b> (<i>sentido contrario al habitual</i>)", "<b>Sentido contrario al habitual</b>"), T("Carriageway with more than one lane per direction; lanes opened the other way with temporary signs, cones and sometimes lane signals.", "Calzada con más de un carril por sentido; se habilitan carriles en sentido contrario con señalización y balizamiento provisionales y, a veces, semáforos de carril."),
             T("<b>For flow</b>: only <b>motorcycles and cars without trailer</b>. <b>For roadworks</b>: every vehicle allowed on the road. Dipped headlights; <b>60–80 km/h</b>; never move sideways into the normal-direction lanes.",
               "<b>Por fluidez</b>: solo <b>motocicletas y turismos sin remolque</b>. <b>Por obras</b>: todos los autorizados en la vía. Luz de cruce; <b>60–80 km/h</b>; sin desplazarse nunca al carril del sentido normal.")],
        ],
        widths=["20%", "40%", "40%"],
        cls="small",
    ))
    B.append(P(
        "Riders in the <b>normal-direction lanes next to a contraflow lane</b> also use dipped headlights and keep to <b>60–80 km/h</b>, unless there is more than one lane in their direction — then each road’s limits apply.",
        "Quienes circulen por los <b>carriles del sentido normal contiguos al carril en sentido contrario</b> llevarán también luz de cruce y circularán entre <b>60 y 80 km/h</b>, salvo que en su sentido haya más de un carril: entonces rigen los límites de cada vía."))
    B.append(H3("4.4 Counting lanes", "4.4 Cómputo de carriles"))
    B.append(P(
        "When a rule depends on the number of lanes (lane use, overtaking, speed), <b>don’t count</b> lanes reserved for certain vehicles (<b>bus, bicycle</b>) or for certain manoeuvres (<b>acceleration, deceleration</b>…).",
        "Para aplicar las normas que dependen del número de carriles (utilización, adelantamiento, velocidad) <b>no se cuentan</b> los reservados a determinados vehículos (<b>bus, bici</b>) ni a ciertas maniobras (<b>aceleración, deceleración</b>…)."))

    # ---------------------------------------------------------------- 5. hard shoulder
    B.append(H2("5", "Riding on the hard shoulder", "Circulación por el arcén"))
    B.append(P(
        "A motorcycle that has had an <b>accident or breakdown</b> and can carry on should do so <b>at once</b>, making sure it is safe. If it <b>needs help</b>, leave the traffic lanes as soon as possible and head for the <b>first exit using the right-hand hard shoulder</b>; "
        "if that is not possible, <b>stop on the right-hand shoulder</b> or wherever you obstruct traffic least.",
        "La motocicleta que, tras un <b>accidente o avería</b>, pueda continuar, lo hará <b>de forma inmediata</b>, asegurándose de hacerlo con seguridad. Si <b>precisa auxilio</b>, abandonará cuanto antes los carriles y se dirigirá a la <b>primera salida usando el arcén derecho</b>; "
        "si no es posible, <b>se detendrá en el arcén derecho</b> o donde cause menor obstáculo."))
    B.append(FIG(moto_shoulder, "Only on signed stretches, only when traffic is stopped by congestion, at up to 30 km/h and in single file. Weaving between the stopped lanes is still prohibited.",
                 "Solo en tramos señalizados, solo con el tráfico detenido por congestión, a 30 km/h como máximo y en columna de a uno. Zigzaguear entre los carriles detenidos sigue prohibido."))
    B.append(E(
        "Motorcycles on the shoulder in a jam (since 1 October 2026)", "Uso extraordinario del arcén por motocicletas (desde el 1 de octubre de 2026)",
        "The <b>right-hand shoulder</b> may be opened to motorcycles on <b>stretches agreed</b> between the road’s owner and the traffic authority (the DGT, or the regional or local authority), and <b>signed</b> with fixed signs and road markings. "
        "It applies <b>only when traffic in the lanes is stopped by congestion</b>; <b>30 km/h at most</b>; <b>single file</b>, with extreme care. Riders must not endanger the drivers who are obliged to use the shoulder, and must <b>leave it</b> if needed.",
        "Se puede habilitar el <b>arcén derecho</b> para motocicletas en <b>tramos acordados</b> entre el titular de la vía y la Jefatura Central de Tráfico (o la autoridad autonómica o local), <b>señalizados</b> con señales fijas y marcas viales. "
        "Solo cuando la circulación de los carriles esté <b>detenida por congestión</b>; a <b>30 km/h como máximo</b>; en <b>columna de a uno</b>, extremando la precaución. No se debe poner en riesgo a los obligados a circular por el arcén, <b>abandonándolo</b> si fuera preciso.",
        pills_=[T("signed stretches only", "solo tramos señalizados"), T("traffic stopped", "tráfico detenido"), T("≤ 30 km/h", "≤ 30 km/h"), T("single file", "columna de a uno")]))
    B.append(BOX("trap", "Rules for vehicles that must use the shoulder", "Normas de utilización del arcén", [
        ("Vehicles <b>obliged to use the shoulder</b> (mopeds, animal-drawn vehicles, light special vehicles…) may not ride <b>side by side</b>, and may not overtake each other if they would be side by side for more than <b>15 seconds</b> or <b>200 metres</b>. "
         "<b>Bicycles</b> are the exception: they may ride two abreast.",
         "Los vehículos <b>obligados a usar el arcén</b> (ciclomotores, tracción animal, especiales ligeros…) no pueden circular <b>en paralelo</b> ni adelantarse si la marcha en paralelo supera <b>15 segundos</b> o <b>200 metros</b>. "
         "La excepción son las <b>bicicletas</b>, que pueden ir en columna de a dos."),
    ]))

    # ---------------------------------------------------------------- 6. distance
    B.append(H2("6", "Safety distance", "Distancia de seguridad"))
    B.append(P(
        "Behind another vehicle — <b>even if you mean to overtake it</b> — leave enough free space to <b>stop without hitting it if it brakes hard</b>, taking into account speed, grip and braking. "
        "If you are <b>not signalling</b> that you will overtake, the gap must also let whoever follows you <b>overtake you safely</b>.",
        "Detrás de otro vehículo, <b>aunque tenga intención de adelantarlo</b>, hay que dejar un espacio libre que permita <b>detenerse sin colisionar si frena bruscamente</b>, teniendo en cuenta la velocidad, la adherencia y el frenado. "
        "Si <b>no se señala</b> el propósito de adelantar, la separación debe permitir además que el que le sigue <b>le adelante con seguridad</b>."))
    B.append(TABLE(
        [T("A gap that avoids a collision is enough…", "Basta una distancia que evite la colisión…")],
        rows([
            ("…<b>in town</b>; where <b>overtaking is prohibited</b>; where there is <b>more than one lane</b> in your direction; when traffic is so <b>dense</b> that overtaking is impossible; and when you <b>intend to overtake</b>.",
             "…<b>en poblado</b>; donde esté <b>prohibido adelantar</b>; donde haya <b>más de un carril</b> en el mismo sentido; cuando la circulación esté tan <b>saturada</b> que no permita adelantar; y cuando se tenga <b>intención de adelantar</b>."),
            ("Your course mentions “not the 50 metres”: that fixed <b>50 m</b> gap applies <b>out of town</b> to vehicles over <b>3,500 kg</b> or <b>longer than 10 m</b>, not to motorcycles.",
             "Tu curso menciona «no siendo necesarios los 50 metros»: esa separación fija de <b>50 m</b> se exige <b>fuera de poblado</b> a los vehículos de más de <b>3.500 kg</b> o de <b>más de 10 m</b>, no a las motos."),
        ]),
    ))
    B.append(FIG(distances, "In tunnels and underpasses: at least 100 m or 4 seconds when not overtaking. The 50 m and 150 m rows apply to heavy or long vehicles.",
                 "En túneles y pasos inferiores: al menos 100 m o 4 segundos si no se va a adelantar. Las filas de 50 m y 150 m son para vehículos pesados o largos."))
    B.append(BOX("key", "Tunnels and underpasses", "Túneles y pasos inferiores", [
        ("When you are not about to overtake, keep <b>at all times</b> at least <b>100 metres</b> or <b>4 seconds</b> from the vehicle in front.", "Cuando no se pretenda adelantar, hay que mantener <b>en todo momento</b> una distancia mínima de <b>100 metros</b> o un intervalo de <b>4 segundos</b> con el vehículo precedente."),
    ]))

    # ---------------------------------------------------------------- 7. traps
    B.append(H2("7", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("Signalling a manoeuvre <b>does not give you the right</b> to make it.", "Señalizar una maniobra <b>no da derecho</b> a realizarla."),
        ("Phone: prohibited <b>even just held in your hand</b>. Helmet-integrated intercom or navigation: <b>allowed</b>. Earphones connected to a sound device: <b>prohibited</b>.", "Móvil: prohibido <b>incluso solo sujetándolo</b>. Intercomunicador o navegador integrado en el casco: <b>permitido</b>. Auriculares conectados a un aparato de sonido: <b>prohibido</b>."),
        ("Radar <b>detectors</b> and <b>jammers</b>: prohibited. Apps that just say where cameras are: <b>allowed</b>.", "<b>Detectores</b> e <b>inhibidores</b> de radar: prohibidos. Avisadores que solo informan de dónde hay radares: <b>permitidos</b>."),
        ("Refuel with the engine <b>and the lights</b> off, and the phone off.", "Repostar con el motor <b>y las luces</b> apagados, y el móvil apagado."),
        ("Two-way, three lanes: the <b>centre</b> lane only to <b>overtake or turn left</b>; the left lane <b>never</b>.", "Doble sentido con tres carriles: el <b>central</b> solo para <b>adelantar o girar a la izquierda</b>; el izquierdo, <b>nunca</b>."),
        ("“Lane best for your destination” only <b>in town</b> with <b>marked</b> lanes — not on an autovía through a city.", "«El carril que mejor convenga» solo <b>en poblado</b> con carriles <b>delimitados</b>; no en una autovía que cruza la ciudad."),
        ("Island between two directions: <b>keep it on your left</b>. One-way: either side. Roundabouts: centre on your left.", "Isleta entre dos sentidos: <b>a la izquierda</b>. Sentido único: por cualquier lado. Glorietas: centro a la izquierda."),
        ("VAO: motorcycles <b>alone</b> are fine; <b>mopeds</b> are not. A zero-emission car with only the driver: <b>only if the panels allow it</b> (since 2026).", "VAO: la moto <b>sin pasajero</b> puede; el <b>ciclomotor</b>, no. Turismo 0 emisiones con solo el conductor: <b>solo si lo permiten los paneles</b> (desde 2026)."),
        ("Contraflow lane for traffic flow: only <b>motorcycles and cars without trailer</b>, 60–80 km/h, dipped headlights.", "Carril en sentido contrario por fluidez: solo <b>motos y turismos sin remolque</b>, 60–80 km/h, luz de cruce."),
        ("Bus and bicycle lanes, and acceleration and deceleration lanes, <b>don’t count</b> as lanes.", "Los carriles bus y bici, y los de aceleración y deceleración, <b>no se cuentan</b>."),
        ("Motorcycles on the shoulder: <b>signed stretches</b>, <b>traffic stopped</b>, <b>≤ 30 km/h</b>, <b>single file</b>. Otherwise only in an emergency.", "Motos por el arcén: <b>tramo señalizado</b>, <b>tráfico detenido</b>, <b>≤ 30 km/h</b>, <b>en columna de a uno</b>. Si no, solo por emergencia."),
        ("Tunnels: <b>100 m or 4 s</b>. The 50 m rule is for heavy or long vehicles out of town.", "Túneles: <b>100 m o 4 s</b>. Los 50 m son para pesados o largos fuera de poblado."),
    ]))

    # ---------------------------------------------------------------- 8. numbers
    B.append(H2("8", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("VAO: minimum occupants (as a rule) / MMA", "VAO: ocupantes mínimos (norma general) / MMA"), T("2, driver included (motorcycles: 1) / ≤ 3,500 kg", "2, incluido el conductor (motos: 1) / ≤ 3.500 kg")],
            [T("Additional and contraflow lanes", "Carril adicional y en sentido contrario"), T("60–80 km/h, dipped headlights", "60–80 km/h, luz de cruce")],
            [T("Motorcycles on the shoulder in a jam", "Motos por el arcén en atascos"), T("≤ 30 km/h, single file, signed stretches", "≤ 30 km/h, en columna de a uno, tramos señalizados")],
            [T("Vehicles obliged to use the shoulder: side by side", "Obligados a usar el arcén: marcha en paralelo"), T("no more than 15 s or 200 m", "no más de 15 s o 200 m")],
            [T("Tunnels and underpasses (not overtaking)", "Túneles y pasos inferiores (sin adelantar)"), T("≥ 100 m or 4 s", "≥ 100 m o 4 s")],
            [T("Fixed gap out of town (vehicles > 3,500 kg or > 10 m)", "Separación fija fuera de poblado (> 3.500 kg o > 10 m)"), T("50 m", "50 m")],
        ],
        widths=["56%", "44%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
QUIZ_IDS = ["pr2", "ph1", "ph4", "ln2", "ln5", "po1", "po4", "va1", "va4", "fl3", "sh2", "di3"]


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
    ("Reglamento General de Circulación (RD 1428/2003), arts. 3, 4, 10, 18, 29–36 and 54 — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Real Decreto 518/2026 (BOE 26-06-2026): helmet intercoms (art. 18), VAO lanes (art. 35), motorcycles on the hard shoulder (art. 36), in force 1 October 2026", "https://www.boe.es/boe/dias/2026/06/26/pdfs/BOE-A-2026-13889.pdf"),
    ("DGT press release, 22-01-2026: special traffic measures for 2026 — single-occupant cars in VAO lanes only when the panels allow it", "https://www.dgt.es/comunicacion/notas-de-prensa/20260122-resolucion-medidas-especiales-trafico-2026"),
    ("Ley sobre Tráfico (RDL 6/2015), art. 13: phones and headphones while driving", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722"),
]

GLOSSARY = [
    ("vía pública", "public road"),
    ("no molestar · no sorprender · advertir · comprender", "don’t annoy · don’t surprise · warn · understand"),
    ("conducción negligente / temeraria", "careless / reckless driving"),
    ("zigzaguear", "to weave (zigzag) between vehicles"),
    ("dispositivo inalámbrico integrado en el casco", "helmet-integrated wireless device (intercom)"),
    ("inhibidor · detector de radar", "radar jammer · radar detector"),
    ("escape libre", "open exhaust (no silencer)"),
    ("repostar", "to refuel"),
    ("calzada · carril · arcén", "carriageway · lane · hard shoulder"),
    ("borde derecho de la calzada", "right-hand edge of the carriageway"),
    ("cambio de rasante", "brow of a hill"),
    ("travesía", "stretch of an interurban road through a town"),
    ("refugio · isleta · dispositivo de guía", "refuge · traffic island · guide post"),
    ("glorieta · plaza", "roundabout · square"),
    ("carril VAO (vehículos de alta ocupación)", "high-occupancy vehicle lane"),
    ("panel de mensaje variable", "variable-message sign"),
    ("carril de aceleración / deceleración", "acceleration / deceleration lane (slip road)"),
    ("carril reversible", "reversible (tidal-flow) lane"),
    ("carril adicional circunstancial", "temporary additional lane"),
    ("carril en sentido contrario al habitual", "contraflow lane"),
    ("semáforo de carril", "lane-control signal"),
    ("balizamiento", "cones and markers"),
    ("cómputo de carriles", "counting lanes"),
    ("congestión · columna de a uno", "traffic jam · single file"),
    ("distancia de seguridad", "safety (following) distance"),
    ("túnel · paso inferior", "tunnel · underpass"),
]
