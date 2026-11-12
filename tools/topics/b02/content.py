# -*- coding: utf-8 -*-
"""Topic 2 content (use of the road), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Tema 2: Uso de las vías). The wording and the figures are
original; the rules come from the Ley sobre Tráfico (RDL 6/2015, Anexo I and arts. 10, 13, 14), the Reglamento
General de Circulación (RD 1428/2003) as amended up to RD 518/2026 (in force 1 October 2026), and DGT notes.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import road_parts, lane_choice, corridor, distances, levels, walkers


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Most questions ask <b>where</b> you may drive: which lane, which side of an island, when the hard shoulder is allowed, "
         "and who may use a motorway at all.",
         "Casi todas las preguntas preguntan <b>por dónde</b> se circula: qué carril, por qué lado de una isleta, cuándo se puede usar el arcén "
         "y quién puede entrar en una autopista."),
        ("The traps are <b>numbers</b> (60 km/h, 3,500 kg, 7 m, 10 m, 50 m, 100 m, 150 m, 4 s, 6 s, 15 s, 200 m, 30 km/h, 60–80 km/h) "
         "and <b>exceptions</b> (bicycles in pairs, cyclists over 14 on dual carriageways, the emergency corridor).",
         "Las trampas son los <b>números</b> (60 km/h, 3.500 kg, 7 m, 10 m, 50 m, 100 m, 150 m, 4 s, 6 s, 15 s, 200 m, 30 km/h, 60–80 km/h) "
         "y las <b>excepciones</b> (bicicletas en columna de a dos, ciclistas mayores de 14 años en autovía, el carril de emergencia)."),
        ("The sections follow the order of your course’s Topic 2. Spanish exam terms are in <i>italics</i> in the English text, "
         "and a glossary closes the topic.",
         "Los apartados siguen el orden del Tema 2 de tu curso. Al final hay un glosario español–inglés."),
    ]))

    # ---------------------------------------------------------------- 1. safe use
    B.append(H2("1", "A safe use of public roads", "Un uso seguro de las vías públicas"))
    B.append(P(
        "The public road (<i>vía pública</i>) is shared by drivers, pedestrians and animals. Everyone on it has rights, duties and prohibitions, "
        "all aimed at the same thing: everybody’s safety. Four principles sum up the attitude the exam expects.",
        "La vía pública la comparten conductores, peatones y animales. Todos tienen derechos, obligaciones y prohibiciones con un mismo fin: "
        "la seguridad de todos. Cuatro principios resumen la actitud que espera el examen."))
    B.append(TABLE(
        [T("Principle", "Principio"), T("What it means", "Qué significa")],
        [
            [T("<b>Do not annoy</b> (<i>no molestar</i>)", "<b>No molestar</b>"),
             T("Breaking traffic rules, signs or plain courtesy annoys others. Respect the rules and be considerate.",
               "Se molesta incumpliendo normas y señales o faltando a la cortesía. Hay que respetar las normas y ser educado y solidario.")],
            [T("<b>Do not surprise</b> (<i>no sorprender</i>)", "<b>No sorprender</b>"),
             T("No sudden manoeuvres without warning. Signal clearly and early so others have time to react.",
               "Nada de maniobras bruscas sin aviso. Hay que avisar con claridad y antelación para que los demás puedan reaccionar.")],
            [T("<b>Warn</b> (<i>advertir</i>)", "<b>Advertir</b>"),
             T("Signal every manoeuvre in good time. Signalling does <b>not</b> give you the right to make it: you still have to do it correctly and safely.",
               "Señalizar cada maniobra con antelación. Avisar <b>no</b> da derecho a realizarla: hay que hacerla correctamente y sin peligro.")],
            [T("<b>Understand</b> (<i>comprender</i>)", "<b>Comprender</b>"),
             T("Read other people’s signals and forgive their mistakes, without using them to excuse your own or to turn aggressive.",
               "Entender las advertencias de los demás y disculpar sus errores, sin usarlos para justificar los propios ni para ponerse agresivo.")],
        ],
        widths=["28%", "72%"],
    ))

    B.append(H3("1.1 What a driver must do", "1.1 Obligaciones del conductor"))
    B.append(E(
        "Drive with care and caution", "Conducir con diligencia y precaución",
        "Drive with the care needed to avoid <b>any harm</b>, to yourself or to others. Driving <b>negligently</b> or <b>recklessly</b> "
        "(<i>de modo negligente o temerario</i>) is strictly forbidden.",
        "Hay que conducir con la diligencia necesaria para evitar <b>todo daño</b>, propio o ajeno. Está terminantemente prohibido conducir de modo "
        "<b>negligente</b> o <b>temerario</b>."))
    B.append(E(
        "Stay in control and take care near vulnerable people", "Controlar el vehículo y extremar la precaución con los más vulnerables",
        "Be able to control your vehicle (or animals) at all times. When you approach other road users, take extra care with <b>children, elderly people, "
        "blind people</b> and anyone with <b>reduced mobility</b> or visibly impaired.",
        "Hay que estar en condiciones de controlar el vehículo (o los animales) en todo momento. Al acercarse a otros usuarios se extremarán las precauciones con "
        "<b>niños, ancianos, invidentes</b> y personas con <b>movilidad reducida</b> o manifiestamente impedidas."))
    B.append(E(
        "Freedom of movement, field of vision and constant attention", "Libertad de movimientos, campo de visión y atención permanente",
        "Keep your own freedom of movement, the field of vision you need and <b>permanent attention</b> to driving. Sit properly, make sure passengers do too, "
        "and place objects and animals so that nothing gets between you and the controls.",
        "Hay que mantener la propia libertad de movimientos, el campo de visión necesario y la <b>atención permanente</b> a la conducción. Para ello, posición adecuada del "
        "conductor y de los pasajeros, y colocación adecuada de los objetos y animales transportados para que nada interfiera."))
    B.append(E(
        "Cooperate in emission tests", "Colaborar en las pruebas de emisiones",
        "Drivers must cooperate in tests that measure the vehicle’s <b>noise</b> and <b>polluting gases</b>.",
        "Los conductores deben colaborar en las pruebas de detección de <b>ruidos</b> y <b>gases contaminantes</b> del vehículo."))

    B.append(H3("1.2 What a driver must not do", "1.2 Prohibiciones del conductor"))
    B.append(E(
        "Screens in the vehicle", "Pantallas en el vehículo",
        "While the vehicle moves, using screens with <b>internet access, TV monitors or video/DVD players</b> is incompatible with permanent attention. "
        "Allowed: <b>rear-view parking cameras</b>, <b>GPS</b> (not handled while moving) and monitors needed to watch passengers getting on and off.",
        "Con el vehículo en movimiento es incompatible con la atención permanente usar <b>pantallas con acceso a internet, monitores de televisión y reproductores de vídeo o DVD</b>. "
        "Se permiten las <b>cámaras de maniobra traseras</b>, el <b>GPS</b> (sin manipularlo en marcha) y los monitores necesarios para ver la subida y bajada de pasajeros.",
        tip=("The GPS is allowed, but touching it while driving is not.",
             "El GPS está permitido, pero manipularlo en marcha no.")))
    B.append(E(
        "Mobile phone", "Teléfono móvil",
        "You may not drive using a mobile phone or any other communication device, <b>not even holding it in your hand without using it</b>. "
        "Only allowed when it works <b>without hands</b> and without headsets, earphones or similar. "
        "Exempt: police and other traffic agents doing their job, and drivers of Armed Forces vehicles in convoy.",
        "No se puede conducir utilizando el móvil u otro medio de comunicación, <b>ni siquiera sujetándolo con la mano aunque no se use</b>. "
        "Solo se permite si se usa <b>sin emplear las manos</b> y sin cascos, auriculares o similares. "
        "Exentos: los agentes de la autoridad en el ejercicio de sus funciones y los conductores de vehículos de las Fuerzas Armadas que circulen en convoy.",
        pills_=[T("holding it = offence", "sujetarlo = infracción"), T("hands-free OK", "manos libres sí")]))
    B.append(E(
        "Headphones and earphones", "Cascos y auriculares",
        "Driving with any <b>audio headset, earphones</b> or similar connected to a sound device is forbidden. "
        "Exceptions: during lessons and the skills tests <b>on open roads</b> (<i>circuito abierto</i>) for the licence, when the Reglamento General de Conductores requires it, and <b>certified wireless devices built into a motorcycle or moped helmet</b> "
        "for communication or navigation, as long as they do not affect safety.",
        "Está prohibido conducir con <b>cascos de audio, auriculares</b> o similares conectados a aparatos de sonido. "
        "Excepciones: durante la enseñanza y las pruebas de aptitud <b>en circuito abierto</b> para obtener el permiso, cuando lo exija el Reglamento General de Conductores, y los <b>dispositivos inalámbricos homologados integrados en el casco</b> "
        "de motos y ciclomotores para comunicación o navegación, siempre que no afecten a la seguridad."))

    B.append(H3("1.3 Other prohibitions", "1.3 Otras prohibiciones"))
    B.append(TABLE(
        [T("Forbidden", "Prohibido"), T("Detail", "Detalle")],
        [
            [T("Hindering or endangering others", "Entorpecer o poner en peligro"),
             T("Behave so as not to obstruct traffic unduly or cause danger, harm or unnecessary nuisance to people, property or the environment.",
               "Comportarse sin entorpecer indebidamente la circulación ni causar peligro, perjuicios o molestias innecesarias a personas, bienes o medio ambiente.")],
            [T("Throwing or leaving things", "Arrojar o abandonar objetos"),
             T("Throwing, leaving or dumping on the road or beside it anything that can start a <b>fire</b> or <b>pollute</b>, damage the road, or change the conditions for driving, stopping or parking. Washing the car on a public road is also forbidden.",
               "Arrojar, depositar o abandonar en la vía o sus inmediaciones objetos que puedan producir <b>incendios</b> o <b>contaminación</b>, deteriorar la vía o modificar las condiciones para circular, parar o estacionar. También está prohibido lavar el vehículo en la vía pública.")],
            [T("Leaving an obstacle you created", "Dejar un obstáculo creado"),
             T("Signal it (and your vehicle), day and night, and get it removed as soon as possible. Speed humps at pedestrian crossings and rumble strips that meet the rules are <b>not</b> obstacles.",
               "Hay que señalizarlo (y señalizar el vehículo), de día y de noche, y retirarlo cuanto antes. Los resaltos en pasos de peatones y las bandas transversales reglamentarias <b>no</b> son obstáculos.")],
            [T("Radar <b>inhibitors</b> and <b>detectors</b>", "<b>Inhibidores</b> y <b>detectores</b> de radar"),
             T("Fitting or carrying devices that jam speed cameras (<i>cinemómetros</i>) or detect them. <b>Warning apps/devices</b> that only say where the surveillance points are <b>are allowed</b>.",
               "Instalar o llevar mecanismos que interfieran en los cinemómetros o que los detecten. Los <b>avisadores</b> que solo informan de dónde están los sistemas de vigilancia <b>están permitidos</b>.")],
            [T("Warning others about police", "Avisar de la presencia de agentes"),
             T("Making signals to other road users to warn them that traffic agents are present or watching.",
               "Hacer señales a otros usuarios para advertir de la presencia o vigilancia de los agentes de tráfico.")],
            [T("Noise and fumes over the limits", "Ruidos y humos por encima del límite"),
             T("Electromagnetic interference, noise or gases above the limits, especially riding with an <b>open exhaust</b> (no silencer).",
               "Perturbaciones electromagnéticas, ruidos o gases por encima de los límites, especialmente circular con <b>escape libre</b> (sin silenciador).")],
            [T("Refuelling carelessly", "Repostar sin precauciones"),
             T("Refuel with the <b>engine stopped</b>, the ignition off, the <b>lights off</b>, and the radio and <b>mobile phones</b> switched off.",
               "Se reposta con el <b>motor parado</b>, el contacto quitado, las <b>luces apagadas</b> y la radio y los <b>móviles</b> apagados.")],
            [T("Sharp ornaments", "Adornos con aristas"),
             T("Ornaments or objects with protruding sharp edges, inside or outside the vehicle.",
               "Adornos u objetos con aristas salientes peligrosas, dentro o fuera del vehículo.")],
            [T("Covering the windows", "Tapar las lunas"),
             T("Non-approved tinted glass, films or stickers that reduce the driver’s view. <b>Exception:</b> approved films or sun blinds on the <b>rear windows</b> if the vehicle has <b>two exterior mirrors</b>.",
               "Vidrios tintados no homologados, láminas o adhesivos que reduzcan la visibilidad. <b>Excepción:</b> láminas o cortinillas reglamentarias en las <b>ventanillas posteriores</b> si se llevan <b>dos espejos exteriores</b>.")],
        ],
        widths=["30%", "70%"],
    ))

    # ---------------------------------------------------------------- 2. parts of the road
    B.append(H2("2", "Parts of the road", "Partes de la vía"))
    B.append(FIG(road_parts, "A dual carriageway seen in cross-section. Each <i>plataforma</i> is a carriageway plus its two hard shoulders; the median separates the two plataformas.",
                 "Una autovía vista en sección. Cada plataforma es una calzada con sus dos arcenes; la mediana separa las dos plataformas."))
    B.append(TABLE(
        [T("Term", "Término"), T("Meaning", "Significado")],
        [
            [T("<b>Plataforma</b> (road platform)", "<b>Plataforma</b>"), T("The area made up of the <b>carriageway and the hard shoulders</b>.", "Zona formada por la <b>calzada y los arcenes</b>.")],
            [T("<b>Calzada</b> (carriageway)", "<b>Calzada</b>"), T("Part of the road <b>for vehicles</b>.", "Parte de la vía <b>destinada a la circulación de vehículos</b>.")],
            [T("<b>Carril</b> (lane)", "<b>Carril</b>"), T("Subdivision of the carriageway wide enough for <b>one line of cars</b> (not motorcycles), with or without lane markings.",
                                                          "Subdivisión de la calzada que permite el paso de <b>una fila de automóviles</b> que no sean motocicletas, delimitada o no por marcas longitudinales.")],
            [T("<b>Mediana</b> (median)", "<b>Mediana</b>"), T("Strip <b>between two separate plataformas</b>, not for traffic.", "Franja longitudinal <b>entre dos plataformas separadas</b>, no destinada a la circulación.")],
            [T("<b>Arcén</b> (hard shoulder)", "<b>Arcén</b>"), T("Paved strip <b>next to the carriageway</b>, not for motor vehicles except in exceptional cases.",
                                                               "Parte afirmada <b>contigua a la calzada</b>, no destinada a vehículos automóviles salvo en casos excepcionales.")],
        ],
        widths=["28%", "72%"],
    ))
    B.append(H3("2.1 Other elements of the road", "2.1 Otros elementos de la vía"))
    B.append(TABLE(
        [T("Element", "Elemento"), T("Meaning", "Significado")],
        [
            [T("<i>Zona peatonal</i> (pedestrian zone)", "Zona peatonal"), T("Part of the road, raised or marked off, <b>reserved for pedestrians</b>: pavements, squares, boulevards, promenades, platforms and the like.",
                                                                            "Parte de la vía, elevada o delimitada, <b>reservada a los peatones</b>: aceras, plazas, bulevares, paseos, andenes y similares.")],
            [T("<i>Acera</i> (pavement)", "Acera"), T("Strip along the road, raised or not, <b>for people on foot</b>.", "Zona longitudinal, elevada o no, <b>destinada al tránsito de peatones</b>.")],
            [T("<i>Refugio</i> (pedestrian refuge)", "Refugio"), T("Pedestrian zone <b>on the carriageway</b>, protected from traffic.", "Zona peatonal <b>situada en la calzada</b> y protegida del tráfico rodado.")],
            [T("<i>Isleta</i> (traffic island)", "Isleta"), T("Raised or marked-off area of the carriageway, usually at junctions, that <b>channels traffic</b>.",
                                                            "Zona elevada o delimitada de la calzada, normalmente en intersecciones, que sirve para <b>canalizar el tráfico</b>.")],
            [T("<i>Curva</i> (bend)", "Curva"), T("Stretch where the road changes direction. It has <b>reduced visibility</b> when you cannot see the whole width of the carriageway or oncoming vehicles.",
                                                 "Tramo en el que la vía cambia de dirección. Es de <b>visibilidad reducida</b> cuando no se ve toda la anchura de la calzada o los vehículos que vienen de frente.")],
            [T("<i>Rasante</i> (gradient)", "Rasante"), T("The slope of a stretch of road.", "Inclinación de un tramo de la vía.")],
            [T("<i>Cambio de rasante</i> (brow / change of gradient)", "Cambio de rasante"), T("Where two stretches with different gradients meet. Reduced visibility when it hides vehicles on the other side.",
                                                                                               "Lugar donde se unen dos tramos de distinta inclinación. Es de visibilidad reducida cuando impide ver los vehículos del otro lado.")],
            [T("<i>Apartadero</i> (lay-by)", "Apartadero"), T("Widening of the carriageway to <b>stop</b> without blocking traffic.", "Ensanchamiento de la calzada para <b>detenerse</b> sin interceptar la circulación.")],
            [T("<i>Zona de frenado de emergencia</i> (escape lane)", "Zona de frenado de emergencia"), T("Escape area off the carriageway where a vehicle whose <b>brakes fail</b> can stop.",
                                                                                                       "Zona de escape de la calzada donde puede detenerse un vehículo cuyos <b>frenos fallan</b>.")],
            [T("<i>Vía de servicio</i> (service road)", "Vía o calzada de servicio"), T("Road roughly parallel to a main road, secondary to it, joined to it at some points, serving the buildings and properties alongside.",
                                                                                   "Camino sensiblemente paralelo a una carretera, secundario respecto a ella, conectado en algunos puntos y que da servicio a las propiedades o edificios contiguos.")],
            [T("<i>Intersección</i> (junction)", "Intersección"), T("Node where all the vehicle paths cross <b>at the same level</b>.", "Nudo de la red viaria en el que todos los cruces de trayectorias se hacen <b>a nivel</b>.")],
            [T("<i>Glorieta</i> (roundabout)", "Glorieta"), T("Junction where the roads meet through a <b>ring</b> that traffic travels round a <b>central island</b>. A “split roundabout”, where traffic goes straight <b>through</b> the island, is not a true glorieta.",
                                                            "Intersección en la que los tramos se comunican a través de un <b>anillo</b> con circulación rotatoria alrededor de una <b>isleta central</b>. Las glorietas partidas, en las que el tráfico <b>atraviesa</b> la isleta, no son glorietas propiamente dichas.")],
        ],
        widths=["30%", "70%"],
        cls="small",
    ))
    B.append(H3("2.2 Cycle infrastructure", "2.2 Vías para ciclos"))
    B.append(TABLE(
        [T("Type", "Tipo"), T("Where it runs", "Por dónde discurre")],
        [
            [T("<i>Vía ciclista</i> (cycle route)", "Vía ciclista"), T("Any road specifically prepared for cycles, with its own signs and markings, wide enough for them to pass safely. All the types below are cycle routes.",
                                                                     "Vía específicamente acondicionada para ciclos, con su señalización y anchura suficiente para su paso seguro. Todas las siguientes son vías ciclistas.")],
            [T("<i>Carril bici</i>", "Carril bici"), T("<b>Alongside the carriageway</b>, one-way or two-way.", "<b>Adosado a la calzada</b>, en un sentido o en doble sentido.")],
            [T("<i>Carril bici protegido</i>", "Carril bici protegido"), T("A carril bici with <b>physical side elements</b> separating it from the carriageway and the pavement.", "Carril bici con <b>elementos laterales</b> que lo separan físicamente de la calzada y de la acera.")],
            [T("<i>Acera bici</i>", "Acera bici"), T("Cycle route marked <b>on the pavement</b>.", "Vía ciclista señalizada <b>sobre la acera</b>.")],
            [T("<i>Pista bici</i>", "Pista bici"), T("<b>Segregated</b> from motor traffic, on its own route independent of the roads.", "<b>Segregada</b> del tráfico motorizado, con trazado independiente de las carreteras.")],
            [T("<i>Senda ciclable</i>", "Senda ciclable"), T("For <b>pedestrians and cycles</b>, segregated from motor traffic, through parks, gardens, forests and open spaces.",
                                                           "Para <b>peatones y ciclos</b>, segregada del tráfico motorizado, por espacios abiertos, parques, jardines o bosques.")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(P("Other vehicles may use a cycle route only when the traffic authority has authorised it and signs say so.",
               "Otros vehículos solo pueden circular por una vía ciclista si lo autoriza la autoridad de tráfico competente y lo indica la señalización."))

    # ---------------------------------------------------------------- 3. types of road
    B.append(H2("3", "Types of road", "Tipos de vía"))
    B.append(H3("3.1 By location", "3.1 Según su ubicación"))
    B.append(TABLE(
        [T("Term", "Término"), T("Meaning", "Significado")],
        [
            [T("<i>Vía interurbana</i> (outside built-up areas)", "Vía interurbana (fuera de poblado)"), T("Any public road <b>outside</b> a built-up area.", "Toda vía pública situada <b>fuera de poblado</b>.")],
            [T("<i>Carretera</i> (road)", "Carretera"), T("Any <b>paved</b> public road outside built-up areas, <b>except travesías</b>.", "Toda vía pública <b>pavimentada</b> situada fuera de poblado, <b>salvo las travesías</b>.")],
            [T("<i>Vía urbana</i> (inside built-up areas)", "Vía urbana (dentro de poblado)"), T("Every road of a town <b>except the travesías</b>.", "Todas las vías de una población <b>excepto las travesías</b>.")],
            [T("<i>Travesía</i>", "Travesía"), T("Stretch of a <b>carretera</b> that runs <b>through a town</b>. It stops being a travesía if there is a bypass the driver can take instead.",
                                               "Tramo de <b>carretera</b> que discurre <b>por poblado</b>. No lo es si existe una variante o alternativa a la que se tiene acceso.")],
        ],
        widths=["32%", "68%"],
    ))
    B.append(H3("3.2 By characteristics", "3.2 Según sus características"))
    B.append(E(
        "<i>Autopista</i> (motorway) · sign S-1", "Autopista · señal S-1",
        "Built and signed <b>only for automobiles</b>. Separate carriageways for each direction (median or other means), <b>no access</b> from neighbouring properties, "
        "and it does <b>not cross any other road at the same level</b>. It may be free or a toll road, and may run through towns.",
        "Proyectada, construida y señalizada para la <b>exclusiva circulación de automóviles</b>. Calzadas separadas para cada sentido (mediana u otros medios), "
        "<b>sin acceso</b> desde las propiedades colindantes y <b>sin cruces a nivel</b> con ninguna otra vía. Puede ser libre o de peaje y puede discurrir por poblado.",
        pills_=[T("no access from properties", "sin accesos"), T("automobiles only", "solo automóviles")]))
    B.append(E(
        "<i>Autovía</i> (dual carriageway) · sign S-1a", "Autovía · señal S-1a",
        "Separate carriageways for each direction, <b>no level crossings</b>, and <b>limited access</b> from neighbouring properties. May run through towns.",
        "Calzadas separadas para cada sentido, <b>sin cruces a nivel</b> y con <b>limitación de accesos</b> desde las propiedades colindantes. Puede discurrir por poblado.",
        pills_=[T("limited access", "accesos limitados")],
        tip=("Autopista = no access at all. Autovía = limited access. That single word is the usual trap.",
             "Autopista = sin accesos. Autovía = accesos limitados. Esa palabra es la trampa habitual.")))
    B.append(BOX("key", "Who may use motorways and dual carriageways", "Quién puede circular por autopistas y autovías", [
        ("<b>Allowed:</b> automobiles able to exceed <b>60 km/h on the flat</b>. Special vehicles: if they exceed the standard masses or dimensions, as their complementary permit says; if not, only if they can exceed 60 km/h on the flat.",
         "<b>Pueden:</b> los automóviles capaces de superar <b>60 km/h en llano</b>. Vehículos especiales: si superan masas o dimensiones, según su autorización complementaria; si no, solo si superan 60 km/h en llano."),
        ("<b>Forbidden:</b> pedestrians, cycles, mopeds, vehicles for people with reduced mobility, personal mobility vehicles (VMP), animals and animal-drawn vehicles.",
         "<b>Prohibido:</b> peatones, ciclos, ciclomotores, vehículos para personas de movilidad reducida, vehículos de movilidad personal (VMP), animales y vehículos de tracción animal."),
        ("<b>Exception:</b> cyclists <b>over 14</b> may ride on the <b>hard shoulder of an autovía</b> (never of an autopista), unless signs forbid it.",
         "<b>Excepción:</b> los ciclistas <b>mayores de 14 años</b> pueden circular por el <b>arcén de las autovías</b> (nunca de las autopistas), salvo prohibición señalizada."),
    ]))
    B.append(E(
        "<i>Vía para automóviles</i> (road for automobiles) · sign S-1b", "Vía para automóviles · señal S-1b",
        "Reserved <b>only for automobiles</b> and signed as such, with a <b>single carriageway</b> and no access to neighbouring properties.",
        "Vía reservada <b>exclusivamente a automóviles</b>, señalizada como tal, con <b>una sola calzada</b> y sin accesos a las propiedades colindantes."))
    B.append(E(
        "<i>Carretera convencional</i> (ordinary road)", "Carretera convencional",
        "Any carretera that is <b>not</b> an autopista, autovía or vía para automóviles. There is no restriction on who may use it.",
        "Toda carretera que <b>no</b> reúne las características de autopista, autovía o vía para automóviles. No tiene limitaciones de uso."))

    # ---------------------------------------------------------------- 4. lanes
    B.append(H2("4", "Using the lanes", "Utilización de carriles"))
    B.append(P(
        "Drivers of automobiles, and of special vehicles over <b>3,500 kg</b> MMA, use the <b>carriageway, not the hard shoulder</b>, except in an emergency. "
        "As a general rule, and above all on bends and brows with reduced visibility, drive <b>as close as possible to the right-hand edge</b>, leave enough "
        "side room to pass oncoming traffic safely, and leave the opposite half completely free.",
        "Los conductores de automóviles, y de vehículos especiales de más de <b>3.500 kg</b> de MMA, circulan por la <b>calzada y no por el arcén</b>, salvo por emergencia. "
        "Como norma general, y sobre todo en curvas y cambios de rasante de visibilidad reducida, se circula <b>lo más cerca posible del borde derecho</b>, con separación lateral "
        "suficiente para cruzarse con seguridad y dejando completamente libre la parte del sentido contrario."))
    B.append(FIG(lane_choice, "Which lane to use: two-way roads (left and centre) and an interurban one-way carriageway with three or more lanes (right).",
                 "Qué carril usar: calzadas de doble sentido (izquierda y centro) y calzada interurbana de sentido único con tres o más carriles (derecha)."))
    B.append(TABLE(
        [T("Road", "Vía"), T("Lane to use", "Carril que se usa")],
        [
            [T("<b>Two-way</b>, two lanes (marked or not), in or out of town", "<b>Doble sentido</b>, dos carriles (con o sin marcas), dentro o fuera de poblado"),
             T("The <b>right-hand lane</b>.", "El <b>carril derecho</b>.")],
            [T("<b>Two-way</b>, three lanes separated by <b>broken lines</b>", "<b>Doble sentido</b>, tres carriles separados por <b>discontinuas</b>"),
             T("The <b>right-hand lane</b>; the <b>centre lane only to overtake or to turn left</b>. Never the left-hand lane.",
               "El <b>carril derecho</b>; el <b>central solo para adelantar o girar a la izquierda</b>. Nunca el izquierdo.")],
            [T("<b>Out of town, one way</b>, more than one lane", "<b>Fuera de poblado, sentido único</b>, más de un carril"),
             T("Normally the <b>rightmost lane</b>; the others for overtaking.", "Normalmente el <b>carril de más a la derecha</b>; el resto para adelantar.")],
            [T("<b>Out of town, one way</b>, three or more lanes: trucks and vans over 3,500 kg, special vehicles over 3,500 kg, and combinations over <b>7 m</b>",
               "<b>Fuera de poblado, sentido único</b>, tres o más carriles: camiones y furgones de más de 3.500 kg, especiales de más de 3.500 kg y conjuntos de más de <b>7 m</b>"),
             T("The rightmost lane; <b>exceptionally the one next to it, never the rest</b>.", "El de la derecha; <b>excepcionalmente el inmediato, nunca los restantes</b>.")],
            [T("<b>In town</b> (urban roads and travesías), one way, lanes <b>marked</b>", "<b>Dentro de poblado</b> (vías urbanas y travesías), sentido único, carriles <b>delimitados</b>"),
             T("The lane that <b>best suits your destination</b>, without hindering others. Leave it only to turn, overtake, stop or park.",
               "El que <b>mejor convenga a su destino</b>, sin estorbar. Solo se abandona para cambiar de dirección, adelantar, parar o estacionar.")],
            [T("<b>In town</b>, one way, lanes <b>not marked</b>", "<b>Dentro de poblado</b>, sentido único, carriles <b>no delimitados</b>"),
             T("The <b>right-hand lane</b>.", "El <b>carril de la derecha</b>.")],
            [T("Autopista or autovía <b>through urban land</b>", "Autopista o autovía <b>por suelo urbano</b>"),
             T("<b>Not</b> “best for your destination”: normally the rightmost lane, the rest to overtake.", "<b>No</b> vale el que mejor convenga: normalmente el de más a la derecha y el resto para adelantar.")],
        ],
        widths=["44%", "56%"],
        cls="small",
    ))
    B.append(P(
        "Out of town you leave the right-hand lane only when traffic or the road make it advisable, and never if it hinders someone behind you. "
        "No vehicle may drive on pavements or pedestrian zones; regulations make exceptions for VMP, bicycles and cycles.",
        "Fuera de poblado solo se abandona el carril derecho cuando lo aconsejen el tráfico o la vía y sin entorpecer al que viene detrás. "
        "En ningún caso se circula por aceras o zonas peatonales; las normas prevén excepciones para VMP, bicicletas y ciclos."))

    # ---------------------------------------------------------------- 5. position
    B.append(H2("5", "Position on the carriageway", "Posición en la calzada"))
    B.append(TABLE(
        [T("Situation", "Situación"), T("Rule", "Norma")],
        [
            [T("Refuges, islands or guide posts <b>separating two directions</b>", "Refugios, isletas o dispositivos de guía que <b>separan dos sentidos</b>"),
             T("Pass on the part of the carriageway to their <b>right</b> (leave them on your left).", "Se circula por la parte de la calzada a su <b>derecha</b> (dejándolos a la izquierda).")],
            [T("The same on a <b>one-way</b> road, or inside the half of one direction", "Lo mismo en vía de <b>sentido único</b> o dentro de la parte de un sentido"),
             T("<b>Either side</b>.", "Por <b>cualquiera de los dos lados</b>.")],
            [T("Squares, roundabouts and junctions", "Plazas, glorietas e intersecciones"),
             T("Go round leaving the <b>centre on your left</b>.", "Se circula dejando el <b>centro a la izquierda</b>.")],
            [T("Roundabout on an <b>interurban</b> road, at least two marked lanes", "Glorieta en vía <b>interurbana</b> con al menos dos carriles delimitados"),
             T("Use the lane <b>nearest the right</b> (outer lane); the others only when traffic or the road advise it, without hindering anyone.",
               "Se circula por el <b>más próximo a la derecha</b> (exterior); los demás solo cuando lo aconsejen el tráfico o la vía, sin estorbar.")],
            [T("Roundabout on an <b>urban</b> road, at least two marked lanes", "Glorieta en vía <b>urbana</b> con al menos dos carriles delimitados"),
             T("The lane that <b>best suits your destination</b>. Never cut across a vehicle in an outer lane.", "El que <b>mejor convenga a su destino</b>. Nunca se corta la trayectoria de quien va por un carril exterior.")],
            [T("Road with <b>two carriageways</b>", "Vía con <b>dos calzadas</b>"),
             T("Use the carriageway on the <b>right</b> for your direction.", "Se usa la calzada de la <b>derecha</b> según el sentido de la marcha.")],
            [T("Road with <b>three carriageways</b>", "Vía con <b>tres calzadas</b>"),
             T("The <b>centre one</b> may carry one or both directions, permanently or at times; the <b>side ones</b> carry one direction, unless signed otherwise.",
               "La <b>central</b> puede ser de uno o dos sentidos, de forma permanente o temporal; las <b>laterales</b>, de un solo sentido, salvo que se señalice otra cosa.")],
        ],
        widths=["42%", "58%"],
    ))

    # ---------------------------------------------------------------- 6. types of lane
    B.append(H2("6", "Types of lane", "Tipos de carriles"))
    B.append(H3("6.1 Lanes by signed speed", "6.1 Carriles en función de la velocidad señalizada"))
    B.append(P(
        "On steep uphill stretches of interurban roads there may be a lane for vehicles that <b>cannot reach a given speed</b>. The lane with the "
        "<b>minimum-speed</b> sign may only be used by vehicles going at that speed or faster, and even they should keep to the right-hand lane when they can. "
        "The obligation ends at the <b>“End of lane”</b> or <b>“End of minimum speed”</b> sign. These lanes <b>do count</b> when counting lanes.",
        "En subidas pronunciadas de vías interurbanas puede haber un carril para los vehículos que <b>no alcanzan una velocidad determinada</b>. El carril con la señal de "
        "<b>velocidad mínima</b> solo pueden usarlo quienes circulen a esa velocidad o más, y aun así deben ir por el derecho si las circunstancias lo permiten. "
        "La obligación termina con la señal de <b>«Fin de carril»</b> o <b>«Fin de velocidad mínima»</b>. Estos carriles <b>sí se computan</b>."))
    B.append(H3("6.2 Lanes reserved for certain vehicles", "6.2 Carriles reservados a determinados vehículos"))
    B.append(E(
        "Bus lane (<i>carril bus</i>) and bus-taxi lane", "Carril bus y carril bus-taxi",
        "Only public-transport buses may use it; if the sign also says <b>TAXI</b>, taxis may too. It is marked with a <b>continuous line</b>, "
        "with short <b>broken</b> stretches where other vehicles may cross it for a manoeuvre <b>other than stopping, parking, turning round or overtaking</b> "
        "(for example to turn right), giving way to buses and taxis.",
        "Solo pueden usarlo los autobuses de transporte colectivo; si la señal dice además <b>TAXI</b>, también los taxis. Se delimita con <b>línea continua</b>, "
        "con pequeños tramos <b>discontinuos</b> para que otros vehículos lo crucen en maniobras <b>que no sean parar, estacionar, cambiar de sentido o adelantar</b> "
        "(por ejemplo, girar a la derecha), cediendo el paso a autobuses y taxis."))
    B.append(E(
        "High-occupancy lane (<i>carril VAO</i>)", "Carril VAO (vehículos de alta ocupación)",
        "For automobiles that carry only people, <b>MMA up to 3,500 kg</b>, with the number of occupants set for that stretch (as a rule <b>at least two, driver included</b>). "
        "Using it wrongly is a <b>serious</b> offence. It may be open permanently or at set times.",
        "Para automóviles destinados solo al transporte de personas, de <b>MMA no superior a 3.500 kg</b>, con el número de ocupantes fijado para cada tramo "
        "(como norma general, <b>mínimo dos, incluido el conductor</b>). Incumplir sus normas es infracción <b>grave</b>. Puede habilitarse de forma permanente o temporal.",
        pills_=[T("≥ 2 occupants", "≥ 2 ocupantes"), T("MMA ≤ 3,500 kg", "MMA ≤ 3.500 kg"), T("serious offence", "infracción grave")]))
    B.append(TABLE(
        [T("May use the VAO lane", "Pueden usar el carril VAO"), T("Condition", "Condición")],
        [
            [T("Cars and adaptable mixed vehicles", "Turismos y vehículos mixtos adaptables"), T("With the occupants required. The driver may be alone with the <b>V-15</b> reduced-mobility sign or the disabled parking card.",
                                                                                                  "Con los ocupantes exigidos. El conductor puede ir solo con la señal <b>V-15</b> o la tarjeta de estacionamiento para personas con movilidad reducida.")],
            [T("Motorcycles (two or three wheels)", "Motocicletas de dos o tres ruedas"), T("No passenger needed.", "No es obligatorio llevar acompañante.")],
            [T("Buses over 3.5 t and articulated buses", "Autobuses de más de 3,5 t y articulados"), T("Whatever the number of occupants.", "Con independencia del número de ocupantes.")],
            [T("Taxis", "Taxis"), T("Whatever the number of occupants.", "Con independencia del número de ocupantes.")],
            [T("Priority vehicles on urgent service and road maintenance crews", "Vehículos prioritarios en servicio urgente y equipos de mantenimiento"), T("When on duty.", "En servicio.")],
            [T("Cars with the environmental label (V-25) <b>0 emisiones, ECO, C or B</b>", "Turismos con distintivo ambiental (V-25) <b>0 emisiones, ECO, C o B</b>"),
             T("<b>Only when the variable-message panels say so</b>; then the number of occupants does not matter.", "<b>Solo cuando lo indiquen los paneles de mensaje variable</b>; entonces da igual el número de ocupantes.")],
        ],
        widths=["44%", "56%"],
        cls="small",
    ))
    B.append(P(
        "<b>Forbidden</b> in the VAO lane: every other vehicle or combination, including cars towing a trailer, trucks and vans, and also pedestrians, mopeds, cycles and VMP.",
        "<b>Prohibido</b> en el carril VAO: el resto de vehículos y conjuntos, incluidos los turismos con remolque, camiones y furgones, y también peatones, ciclomotores, ciclos y VMP."))
    B.append(H3("6.3 Lanes for certain manoeuvres", "6.3 Carriles reservados a determinadas maniobras"))
    B.append(TABLE(
        [T("Lane", "Carril"), T("What it is for", "Para qué sirve")],
        [
            [T("<b>Acceleration</b> (slip road in)", "<b>Aceleración</b> (de entrada)"),
             T("To <b>join</b> the main carriageway. Accelerate to the right speed by its end. At its start, check you can merge safely given the position, path and speed of the others, <b>stopping if necessary</b>.",
               "Para <b>incorporarse</b> a la calzada principal. Se acelera hasta la velocidad adecuada al final del carril. Al principio hay que cerciorarse de que se puede hacer sin peligro, <b>llegando a detenerse si es necesario</b>.")],
            [T("<b>Deceleration</b> (slip road out)", "<b>Deceleración</b> (de salida)"),
             T("To <b>leave</b>. Move to the lane nearest the exit and enter the deceleration lane <b>as soon as possible</b>; slow down <b>inside</b> it, not on the main carriageway.",
               "Para <b>salir</b>. Hay que ir por el carril más próximo a la salida y entrar en él <b>cuanto antes</b>; la velocidad se adapta <b>dentro</b> del carril, no en la calzada principal.")],
            [T("<b>Weaving lane</b> (<i>carril trenzado</i>)", "<b>Trenzado</b>"),
             T("An acceleration lane joined to the next deceleration lane: some vehicles come in while others leave.",
               "Unión de un carril de aceleración con otro de deceleración consecutivo: unos entran mientras otros salen.")],
            [T("<b>Waiting lane</b> (<i>carril de espera</i>)", "<b>Espera</b>"),
             T("At a junction with a <b>left turn</b>, lets you <b>stop and wait</b> for the right moment without blocking others.",
               "En una intersección con <b>giro a la izquierda</b>, permite <b>detenerse a esperar</b> el momento adecuado sin obstaculizar a los demás.")],
        ],
        widths=["28%", "72%"],
    ))
    B.append(H3("6.4 Lanes that improve traffic flow", "6.4 Carriles para mejorar la fluidez del tráfico"))
    B.append(BOX("key", "Memory trick: one rule per word of the name", "Truco: una norma por cada palabra del nombre", [
        ("<b>Reversible</b> (one word): dipped headlights.", "<b>Reversible</b> (una palabra): luz de cruce."),
        ("<b>Adicional circunstancial</b> (two words): dipped headlights + 60–80 km/h.", "<b>Adicional circunstancial</b> (dos palabras): luz de cruce + 60–80 km/h."),
        ("<b>Sentido contrario al habitual</b> (three ideas): dipped headlights + 60–80 km/h + only cars without trailer and motorcycles when it is for traffic flow (for roadworks, any vehicle allowed on the road).",
         "<b>Sentido contrario al habitual</b> (tres ideas): luz de cruce + 60–80 km/h + solo turismos sin remolque y motocicletas si es por fluidez (por obras, cualquiera autorizado en la vía)."),
    ]))
    B.append(TABLE(
        [T("", ""), T("Reversible", "Reversible"), T("Additional (<i>adicional circunstancial</i>)", "Adicional circunstancial"), T("Contraflow (<i>sentido contrario al habitual</i>)", "Sentido contrario al habitual")],
        [
            [T("<b>Where</b>", "<b>Dónde</b>"),
             T("Two-way carriageway; lane marked by <b>double broken lines on both sides</b>", "Calzada de doble sentido; carril con <b>dobles líneas discontinuas a ambos lados</b>"),
             T("Two-way carriageway <b>with hard shoulders</b>; both shoulders are used to make <b>2 lanes one way, 1 the other</b>", "Calzada de doble sentido <b>con arcenes</b>; se usan ambos arcenes para tener <b>2 carriles en un sentido y 1 en el otro</b>"),
             T("Carriageway with more than one lane in the same direction; lanes opened the other way", "Calzada con más de un carril en el mismo sentido; se habilitan carriles en sentido contrario")],
            [T("<b>How it is set up</b>", "<b>Cómo se regula</b>"),
             T("Direction changes; lane-control lights (square signals) or other means", "Cambia de sentido; semáforos de carril (cuadrados) u otros medios"),
             T("Temporary signs and cones", "Señalización y balizamiento provisionales"),
             T("Temporary signs and cones, sometimes lane-control lights", "Señalización y balizamiento provisionales, a veces semáforos de carril")],
            [T("<b>Lights</b>", "<b>Luces</b>"), T("Dipped beam, day and night", "Corto alcance, de día y de noche"),
             T("Dipped beam, day and night", "Corto alcance, de día y de noche"), T("Dipped beam, day and night", "Corto alcance, de día y de noche")],
            [T("<b>Speed</b>", "<b>Velocidad</b>"), T("No special limit", "Sin límite especial"),
             T("<b>Max 80, min 60 km/h</b> (or lower if signed)", "<b>Máx. 80, mín. 60 km/h</b> (o inferior si se señaliza)"),
             T("<b>Max 80, min 60 km/h</b> (or lower if signed)", "<b>Máx. 80, mín. 60 km/h</b> (o inferior si se señaliza)")],
            [T("<b>Other rules</b>", "<b>Otras normas</b>"),
             T("Never move into the lane on its left", "No invadir el carril de su izquierda"),
             T("Lane markings between the wheels; never cross the line of cones", "Marcas longitudinales entre las ruedas; no atravesar la línea de conos"),
             T("<b>For flow:</b> only <b>motorcycles and cars without trailer</b>. <b>For roadworks:</b> every vehicle allowed on that road. Never move into the normal-direction lanes.",
               "<b>Por fluidez:</b> solo <b>motocicletas y turismos sin remolque</b>. <b>Por obras:</b> todos los autorizados en la vía. No invadir los carriles del sentido normal.")],
        ],
        widths=["16%", "26%", "29%", "29%"],
        cls="small",
    ))
    B.append(P(
        "Drivers in the <b>normal-direction lanes next to a contraflow lane</b> must also use dipped headlights and keep to <b>60–80 km/h</b>, "
        "unless their direction has more than one lane, in which case each road’s usual limits apply.",
        "Quienes circulen por los <b>carriles del sentido normal contiguos a un carril en sentido contrario</b> llevarán también luz de cruce y circularán entre <b>60 y 80 km/h</b>, "
        "salvo que en su sentido haya más de un carril, en cuyo caso rigen los límites de cada vía."))
    B.append(H3("6.5 Counting lanes", "6.5 Cómputo de carriles"))
    B.append(P(
        "When rules depend on the number of lanes (which lane to use, overtaking, speed), <b>do not count</b> lanes reserved for certain vehicles (<b>bus, bicycle</b>) "
        "or for certain manoeuvres (<b>acceleration, deceleration, waiting</b>). Minimum-speed lanes <b>do count</b>.",
        "Para aplicar las normas que dependen del número de carriles (utilización, adelantamiento, velocidad) <b>no se cuentan</b> los carriles reservados a determinados vehículos "
        "(<b>bus, bici</b>) ni a determinadas maniobras (<b>aceleración, deceleración, espera</b>). Los de velocidad mínima <b>sí cuentan</b>."))
    B.append(H3("6.6 Emergency corridor and snow on motorways and dual carriageways", "6.6 Carril de emergencia y nieve en autopistas y autovías"))
    B.append(FIG(corridor, "Emergency corridor in a queue. Two lanes: the gap opens in the middle. Three or more lanes: between the left-hand lane and the next one.",
                 "Carril de emergencia en una retención. Dos carriles: el hueco se abre en el centro. Tres o más: entre el carril izquierdo y su contiguo."))
    B.append(E(
        "Emergency corridor (<i>carril de emergencia</i>)", "Carril de emergencia",
        "On autopistas and autovías, when a queue moves at <b>walking pace or stops</b>, vehicles move aside to leave a free gap for <b>priority vehicles</b>. "
        "<b>Two lanes</b>: the gap goes in the <b>centre</b>, between them. <b>Three or more</b>: between the <b>left-hand lane and the one next to it</b>: "
        "the left-hand lane moves as far left as possible and all the others as far right as possible.",
        "En autopistas y autovías, cuando por una retención se circula <b>a paso de peatón o se detiene</b>, los vehículos se orillan para dejar un espacio libre a los "
        "<b>vehículos prioritarios</b>. <b>Dos carriles</b>: el hueco se forma en el <b>centro</b>. <b>Tres o más</b>: entre el <b>carril izquierdo y su contiguo</b>: "
        "los del izquierdo lo más a la izquierda posible y el resto lo más a la derecha posible."))
    B.append(E(
        "Snow on the carriageway", "Calzada con nieve",
        "On autopistas and autovías, when snow makes driving difficult: <b>overtaking is forbidden</b> and you must keep to the <b>right-hand lane</b> "
        "(on stretches with three or more lanes, the one next to it as well), leaving the left lanes free for emergency vehicles and <b>snowploughs</b>.",
        "En autopistas y autovías, con la circulación dificultada por nieve: <b>prohibido adelantar</b> y obligatorio circular por el <b>carril de la derecha</b> "
        "(en tramos de tres o más carriles, también por su contiguo), dejando libres los de la izquierda para vehículos de emergencia y <b>quitanieves</b>."))

    # ---------------------------------------------------------------- 7. hard shoulder
    B.append(H2("7", "Driving on the hard shoulder", "Circulación por el arcén"))
    B.append(P(
        "When there is no lane or road made for them, these drivers must use the <b>right-hand hard shoulder</b> if it is passable and wide enough, "
        "and otherwise the <b>bare minimum of the carriageway</b>:",
        "Si no existe vía o parte de ella especialmente destinada a ellos, estos conductores deben circular por el <b>arcén de la derecha</b> si es transitable y suficiente "
        "y, si no lo es, por la <b>parte imprescindible de la calzada</b>:"))
    B.append(TABLE(
        [T("Must use the hard shoulder", "Obligados a usar el arcén")],
        [
            [T("Cycles", "Ciclos")], [T("Mopeds", "Ciclomotores")], [T("Vehicles for people with reduced mobility", "Vehículos para personas de movilidad reducida")],
            [T("Animal-drawn vehicles", "Vehículos de tracción animal")], [T("Special vehicles with MMA up to 3,500 kg", "Vehículos especiales con MMA de hasta 3.500 kg")],
            [T("Vehicles escorting cyclists", "Vehículos en seguimiento de ciclistas")],
        ],
    ))
    B.append(P(
        "On <b>long descents with bends</b>, when safety allows, cyclists may leave the shoulder and use the right-hand part of the carriageway they need. "
        "<b>Not on autovías</b>: there they must stay on the shoulder.",
        "En <b>descensos prolongados con curvas</b>, si la seguridad lo permite, los ciclistas pueden abandonar el arcén y circular por la parte derecha de la calzada que necesiten. "
        "<b>En autovías no</b>: allí no pueden abandonar el arcén."))
    B.append(E(
        "Accident or breakdown", "Accidente o avería",
        "Vehicles with MMA up to <b>3,500 kg</b> that can still move after an accident or breakdown must carry on at once, safely. If they need help, they leave the lanes as soon as possible "
        "and head for the <b>first exit using the right-hand shoulder</b>. If that is impossible, they stop on the right-hand shoulder or wherever they obstruct least.",
        "Los vehículos de MMA no superior a <b>3.500 kg</b> que tras un accidente o avería puedan seguir, lo harán de inmediato y con seguridad. Si necesitan auxilio, abandonarán cuanto antes "
        "los carriles y se dirigirán a la <b>primera salida usando el arcén derecho</b>. Si no es posible, se detendrán en el arcén derecho o donde menos obstáculo causen."))
    B.append(E(
        "Service vehicles on the shoulder", "Vehículos de servicio por el arcén",
        "Police, fire, civil protection, rescue and ambulance vehicles on urgent service, road maintenance crews and roadside assistance vehicles may use the shoulder to reach "
        "an emergency or do maintenance, provided they show the required signs (<b>V-1, V-2, V-23, V-24</b>) and do <b>not exceed 30 km/h</b>. "
        "Priority vehicles on urgent service are exempt from that limit.",
        "Policía, bomberos, protección civil, salvamento y ambulancias en servicio de urgencia, los equipos de mantenimiento y los vehículos de auxilio en vías públicas pueden "
        "usar el arcén para acudir a una urgencia o hacer mantenimiento, siempre que lleven las señales exigidas (<b>V-1, V-2, V-23, V-24</b>) y <b>no superen 30 km/h</b>. "
        "Los prioritarios en servicio de urgencia quedan exentos de ese límite."))
    B.append(E(
        "Motorcycles on the shoulder in traffic jams (new from 1 October 2026)", "Motocicletas por el arcén en atascos (novedad desde el 1 de octubre de 2026)",
        "Motorcycles may use the <b>right-hand shoulder</b> only on stretches agreed by the road owner and the traffic authority and <b>signed</b> with fixed signs and road markings; "
        "only when traffic is <b>stopped by congestion</b>; at <b>30 km/h at most</b>; in <b>single file</b>, taking extreme care; and without endangering the people who must use the shoulder, "
        "leaving it if necessary.",
        "Las motocicletas pueden usar el <b>arcén derecho</b> solo en tramos acordados entre el titular de la vía y la autoridad de tráfico y <b>señalizados</b> con señales fijas y marcas viales; "
        "solo cuando la circulación esté <b>detenida por congestión</b>; a <b>30 km/h como máximo</b>; en <b>columna de a uno</b>, extremando la precaución; y sin poner en riesgo a quienes "
        "están obligados a ir por el arcén, abandonándolo si es preciso.",
        pills_=[T("signed stretches only", "solo tramos señalizados"), T("traffic stopped", "tráfico detenido"), T("≤ 30 km/h", "≤ 30 km/h")]))
    B.append(BOX("key", "Rules for vehicles on the shoulder", "Normas de utilización del arcén", [
        ("They may <b>not ride side by side</b>, except <b>bicycles, which may ride two abreast</b>, as far to the right as possible. "
         "On stretches without visibility, or when they bunch up, they must go in <b>single file</b>.",
         "No pueden circular <b>en paralelo</b>, salvo las <b>bicicletas, que pueden ir en columna de a dos</b>, lo más a la derecha posible. "
         "En tramos sin visibilidad o cuando formen aglomeraciones, deben ir <b>en hilera</b>."),
        ("On <b>autovías</b> cyclists ride <b>only on the shoulder</b>, never on the carriageway.",
         "En <b>autovías</b> los ciclistas circulan <b>solo por el arcén</b>, sin invadir nunca la calzada."),
        ("Vehicles that must use the shoulder, <b>except bicycles</b>, may not overtake each other if they would be side by side for more than <b>15 seconds</b> or <b>200 metres</b> (serious offence).",
         "Los obligados a usar el arcén, <b>excepto las bicicletas</b>, no pueden adelantarse si la marcha en paralelo supera <b>15 segundos</b> o <b>200 metros</b> (infracción grave)."),
    ]))

    # ---------------------------------------------------------------- 8. distance
    B.append(H2("8", "Safety distance", "Distancia de seguridad"))
    B.append(P(
        "Behind another vehicle, even if you mean to overtake it, leave enough space to <b>stop without hitting it if it brakes hard</b>, allowing for speed, grip and brakes. "
        "If you are <b>not signalling</b> that you will overtake, also leave enough room for whoever is behind you to overtake you safely.",
        "Detrás de otro vehículo, aunque se tenga intención de adelantarlo, hay que dejar espacio para <b>detenerse sin colisionar si frena bruscamente</b>, teniendo en cuenta velocidad, adherencia y frenos. "
        "Si <b>no se señaliza</b> el propósito de adelantar, la separación debe permitir además que el que viene detrás nos adelante con seguridad."))
    B.append(FIG(distances, "Minimum gaps: 50 m for heavy or long vehicles out of town; in tunnels, 100 m or 4 seconds (150 m or 6 seconds if over 3,500 kg).",
                 "Separaciones mínimas: 50 m para vehículos pesados o largos fuera de poblado; en túneles, 100 m o 4 segundos (150 m o 6 segundos si superan 3.500 kg)."))
    B.append(E(
        "Minimum 50 metres", "Separación mínima de 50 metros",
        "Out of town, drivers of vehicles with <b>MMA over 3,500 kg</b> and of vehicles or combinations <b>over 10 m long</b> keep at least <b>50 m</b>. "
        "Groups of <b>cyclists</b> may ride without that gap, taking extra care.",
        "Fuera de poblado, los vehículos de <b>MMA superior a 3.500 kg</b> y los vehículos o conjuntos de <b>más de 10 m de longitud</b> guardan al menos <b>50 m</b>. "
        "Los <b>ciclistas</b> en grupo pueden circular sin esa separación, extremando la atención.",
        tip=("10 m here, 7 m for lane use. Don’t swap them.", "Aquí 10 m; para la utilización de carriles, 7 m. No los cambies.")))
    B.append(P(
        "The 50 m are <b>not</b> needed (a gap that avoids a collision is enough): <b>in town</b>, where <b>overtaking is forbidden</b>, where there is <b>more than one lane</b> in your direction, "
        "when traffic is so <b>dense</b> that overtaking is impossible, and when you <b>intend to overtake</b>.",
        "<b>No</b> hacen falta los 50 m (basta una distancia que evite la colisión): <b>en poblado</b>, donde esté <b>prohibido adelantar</b>, donde haya <b>más de un carril</b> en el mismo sentido, "
        "cuando la circulación esté tan <b>saturada</b> que no permita adelantar y cuando se tenga la <b>intención de adelantar</b>."))
    B.append(E(
        "Chevrons (<i>galones</i>)", "Galones",
        "Arrow-shaped markings painted in the middle of the lane on some stretches, to prevent rear-end crashes. Keep at least <b>two chevrons</b> between you and the vehicle in front, on any road. "
        "Sign <b>R-300 “Minimum distance”</b> marks the start of the stretch, and information panels may remind you.",
        "Marcas viales con forma de ángulo o punta de flecha pintadas en el centro del carril en algunos tramos, para evitar alcances. La separación mínima es de <b>dos galones</b>, en cualquier vía. "
        "Al inicio del tramo se coloca la señal <b>R-300 «Separación mínima»</b> y puede haber carteles informativos."))
    B.append(E(
        "Tunnels and underpasses", "Túneles y pasos inferiores",
        "When not overtaking, keep at all times at least <b>100 m or 4 seconds</b> (or the sight of two chevrons). Vehicles over <b>3,500 kg</b>: <b>150 m or 6 seconds</b> (or three chevrons).",
        "Cuando no se pretenda adelantar, hay que mantener en todo momento al menos <b>100 m o 4 segundos</b> (o la visión de dos galones). Los de más de <b>3.500 kg</b>: <b>150 m o 6 segundos</b> (o tres galones).",
        pills_=[T("100 m / 4 s", "100 m / 4 s"), T("&gt; 3,500 kg: 150 m / 6 s", "&gt; 3.500 kg: 150 m / 6 s")]))

    # ---------------------------------------------------------------- 9. congested roads
    B.append(H2("9", "Congested roads", "Circulación en vías saturadas"))
    B.append(P(
        "Traffic is <b>saturated</b> when vehicles fill the whole width of the carriageway (every lane).",
        "La circulación está <b>saturada</b> cuando los vehículos ocupan todo el ancho de la calzada (todos los carriles)."))
    B.append(TABLE(
        [T("You must", "Se debe"), T("You must not", "Se prohíbe")],
        [
            [T("Match your speed to the vehicle in front. Going faster in one lane than in another is <b>not overtaking</b>, so the right-hand lane may move faster than the left.",
               "Adecuar la velocidad a la del vehículo de delante. Que un carril vaya más rápido que otro <b>no se considera adelantamiento</b>, así que el derecho puede ir más rápido que el izquierdo."),
             T("Change lanes, except to get ready to turn, to leave the carriageway or to take a particular direction.",
               "Cambiar de carril, salvo para prepararse a girar, salir de la calzada o tomar una dirección determinada.")],
            [T("Keep a safe distance, in front and to the sides.", "Mantener la distancia de seguridad, frontal y lateral."),
             T("Overtake on the shoulder or drive on it, <b>not even to reach the next exit</b>.", "Adelantar por el arcén o circular por él, <b>ni siquiera para tomar la salida más próxima</b>.")],
            [T("Watch your speedometer: in a moving queue you lose your sense of speed.", "Vigilar la velocidad: se pierde la percepción de la propia velocidad."), T("", "")],
        ],
        widths=["50%", "50%"],
    ))
    B.append(H3("9.1 Traffic level colour code", "9.1 Código de colores del nivel de circulación"))
    B.append(FIG(levels, "Colours the DGT uses to report traffic, with the speed of traffic as a share of the normal speed.",
                 "Colores con los que la DGT informa del nivel de circulación, con la velocidad respecto a la normal."))

    # ---------------------------------------------------------------- 10. pedestrians
    B.append(H2("10", "Pedestrians", "Peatones"))
    B.append(H3("10.1 Where pedestrians walk", "10.1 Por dónde deben circular"))
    B.append(P(
        "Pedestrians, especially those with reduced mobility or a disability, children and the elderly, have <b>priority of passage and of stay</b> on public roads, "
        "and drivers must take special care not to endanger them. <b>Pavements</b> are reserved for them: <b>no vehicle</b> may use them. "
        "In other pedestrian zones a municipal bylaw may let cyclists and VMP share the space, always giving pedestrians priority, and may allow "
        "<b>children up to 12 on bicycles</b> on the pavement if an <b>adult walks with them</b>.",
        "Los peatones, en especial los de movilidad reducida o con discapacidad, los niños y las personas mayores, <b>gozan de prioridad de paso y estancia</b> en las vías públicas, "
        "y los conductores deben extremar el cuidado para no ponerlos en riesgo. Las <b>aceras</b> son suyas: <b>ningún vehículo</b> puede circular por ellas. "
        "En el resto de zonas peatonales, una ordenanza municipal puede autorizar la coexistencia con ciclistas y VMP, respetando la prioridad del peatón, y la circulación por la acera de "
        "<b>niños de hasta doce años en bicicleta</b> si los acompaña <b>un adulto a pie</b>."))
    B.append(FIG(walkers, "Without a usable pedestrian zone: walk on the left, facing the traffic. People pushing a bicycle, moped or VMP, and groups led by someone, walk on the right.",
                 "Sin zona peatonal practicable: por la izquierda, de cara al tráfico. Quien empuja una bicicleta, ciclomotor o VMP y los grupos dirigidos por una persona, por la derecha."))
    B.append(E(
        "No usable pedestrian zone", "Sin zona peatonal practicable",
        "Walk on the <b>left-hand shoulder</b> in your direction of travel (facing the traffic) if there is one and it is passable; if not, on the carriageway. "
        "Either way, keep as far from the traffic as possible, close to the outer edge and in single file. Walk on the right only when safety requires it.",
        "Se circula por el <b>arcén izquierdo</b> en el sentido de la marcha (de cara al tráfico) si existe y es transitable; si no, por la calzada. "
        "En ambos casos, lo más alejado posible del tráfico, junto al borde exterior y unos detrás de otros. Por la derecha, solo por razones de seguridad.",
        tip=("Drivers must also adapt their speed and distance when pedestrians walk on the carriageway.",
             "Los conductores, a su vez, adecuarán velocidad y distancia cuando haya peatones por la calzada.")))
    B.append(E(
        "Who always walks on the right", "Quién circula siempre por la derecha",
        "People <b>pushing or pulling a cycle, a two-wheeled moped, a VMP</b> or something similar; any <b>group led by one person</b>; and pedestrians who for safety reasons cannot use the left. "
        "They must also obey traffic agents and signs.",
        "Quienes <b>empujen o arrastren un ciclo, un ciclomotor de dos ruedas, un VMP</b> o similar; todo <b>grupo de peatones dirigido por una persona</b>; y los que por seguridad no puedan ir por la izquierda. "
        "Deben cumplir además las órdenes de los agentes y las señales."))
    B.append(E(
        "Stopping and waiting", "Parada y espera",
        "Where there is a refuge, pedestrian zone or similar, no pedestrian may wait on the carriageway or shoulder, not even for a vehicle. To board a vehicle, step onto the carriageway "
        "only when it is already alongside. When a <b>priority vehicle</b> signals, clear the carriageway and wait in a refuge or pedestrian zone, or move away from the traffic.",
        "Si existe refugio, zona peatonal u otro espacio adecuado, ningún peatón esperará en la calzada ni en el arcén, ni siquiera a un vehículo. Para subir a él solo se invade la calzada "
        "cuando ya está a su altura. Ante las señales de un <b>vehículo prioritario</b>, hay que despejar la calzada y quedarse en los refugios o zonas peatonales, o alejarse de la circulación."))
    B.append(H3("10.2 Crossing the road", "10.2 Pasos para peatones y cruces de calzada"))
    B.append(TABLE(
        [T("Situation", "Situación"), T("Rule", "Norma")],
        [
            [T("Crossing exists", "Hay paso de peatones"), T("Cross <b>there</b>, not nearby.", "Se cruza <b>por él</b>, no por sus proximidades.")],
            [T("Pedestrian lights", "Semáforo de peatones"), T("Obey them.", "Se obedecen.")],
            [T("No pedestrian lights", "Sin semáforo de peatones"), T("Do not step out while an agent or the vehicle lights let vehicles through.", "No se entra en la calzada mientras agentes o semáforos den paso a los vehículos.")],
            [T("Zebra crossing with markings only", "Paso señalizado solo con marca vial"), T("Pedestrians have <b>preference</b>, but step out only when the distance and speed of approaching vehicles make it <b>safe</b>.",
                                                                                               "El peatón tiene <b>preferencia</b>, pero solo entra cuando la distancia y velocidad de los vehículos permiten hacerlo <b>con seguridad</b>.")],
            [T("No crossing nearby", "Fuera de un paso"), T("Make sure you can cross without risk or undue obstruction.", "Asegurarse de poder cruzar sin riesgo ni entorpecimiento indebido.")],
            [T("While crossing", "Al cruzar"), T("Walk <b>at right angles</b> to the road, without lingering or stopping.", "Caminar <b>perpendicularmente</b> al eje, sin demorarse ni detenerse.")],
            [T("Squares and roundabouts", "Plazas y glorietas"), T("Do <b>not</b> cross their carriageway: walk round them, unless there is a crossing.", "<b>Prohibido</b> atravesar su calzada: hay que rodearlas, salvo que haya paso para peatones.")],
        ],
        widths=["32%", "68%"],
    ))
    B.append(H3("10.3 Motorways, hitch-hiking and visibility", "10.3 Autopistas, autostop y visibilidad"))
    B.append(E(
        "On autopistas and autovías", "En autopistas y autovías",
        "Pedestrians may not walk on them, except: after an <b>accident, breakdown, illness or other emergency</b> that leaves the vehicle stuck, when occupants leave it if there is a safe place "
        "<b>outside the platform</b>, getting out on the side <b>away from the traffic</b> and never staying on the lanes or shoulders (if they cannot get out safely, they stay inside "
        "<b>with seat belts fastened</b>); and staff of emergency, maintenance, assistance and special vehicles when strictly needed for the job.",
        "Los peatones no pueden circular por ellas, salvo: por <b>accidente, avería, malestar u otra emergencia</b> que inmovilice el vehículo, cuando los ocupantes lo abandonan si hay un lugar seguro "
        "<b>fuera de la plataforma</b>, saliendo por el lado <b>contrario al tráfico</b> y sin permanecer en carriles ni arcenes (si no pueden salir con seguridad, se quedan dentro "
        "<b>con el cinturón abrochado</b>); y los ocupantes o trabajadores de vehículos de urgencia, mantenimiento, auxilio y especiales cuando sea estrictamente indispensable."))
    B.append(E(
        "Hitch-hiking (<i>autostop</i>)", "Autostop",
        "Forbidden <b>anywhere on autopistas or autovías</b>, including the areas around toll booths.",
        "Prohibido en <b>cualquier tramo de autopistas o autovías</b>, incluidas las explanadas de las estaciones de peaje."))
    B.append(E(
        "Being seen", "Visibilidad del peatón",
        "Out of town, on the carriageway or shoulder, <b>between sunset and sunrise</b> or when weather reduces visibility, pedestrians wear an approved <b>luminous or reflective</b> item "
        "visible from at least <b>150 m</b>. Groups led by one person also carry lights on the side nearest the centre of the road: <b>white or yellow in front, red behind</b>.",
        "Fuera de poblado, por la calzada o el arcén, <b>entre la puesta y la salida del sol</b> o cuando las condiciones reduzcan la visibilidad, el peatón lleva un elemento <b>luminoso o reflectante</b> "
        "homologado visible a <b>150 m</b> como mínimo. Los grupos dirigidos por una persona llevan además luces en el lado más próximo al centro: <b>blanca o amarilla delante, roja detrás</b>.",
        pills_=[T("visible at 150 m", "visible a 150 m")]))

    # ---------------------------------------------------------------- 11. animals
    B.append(H2("11", "Animals", "Animales"))
    B.append(P(
        "Draught, pack and saddle animals and livestock (single, in a herd or flock) may use public roads only when there is <b>no usable livestock track</b> (<i>vía pecuaria</i>).",
        "Los animales de tiro, carga o silla y el ganado (suelto, en manada o en rebaño) solo pueden transitar por las vías públicas cuando <b>no exista itinerario practicable por vía pecuaria</b>."))
    B.append(TABLE(
        [T("Rule", "Norma"), T("Detail", "Detalle")],
        [
            [T("Who leads them", "Quién los guía"), T("Always a person <b>over 18</b>, able to control them, who follows the rules for drivers that apply to them. Take the route with the least traffic.",
                                                     "Siempre una persona <b>mayor de 18 años</b>, capaz de dominarlos y que cumpla las normas de los conductores que les afecten. Por la vía alternativa con menos tráfico.")],
            [T("Where", "Por dónde"), T("The <b>right-hand shoulder</b>; if they must use the carriageway, as close as possible to its right edge. Exceptionally, <b>one single animal</b> may be led on the <b>left</b> for safety.",
                                       "Por el <b>arcén derecho</b>; si han de usar la calzada, lo más cerca posible de su borde derecho. Excepcionalmente, <b>un solo animal</b> por el borde <b>izquierdo</b> por seguridad.")],
            [T("Herds and flocks", "Manadas y rebaños"), T("<b>At walking pace</b>, as far right as possible, <b>never taking more than the right half</b> of the carriageway, split into moderate groups each with at least one person in charge.",
                                                          "<b>Al paso</b>, lo más a la derecha posible, <b>sin ocupar nunca más de la mitad derecha</b> de la calzada, en grupos de longitud moderada con al menos un conductor cada uno.")],
            [T("Meeting another herd", "Cruce con otro ganado"), T("Pass as quickly as possible where visibility is good; if not, warn approaching drivers so they can slow down or stop.",
                                                                  "Se cruzan con rapidez y donde haya visibilidad; si no es posible, se avisa a los conductores que se acerquen para que reduzcan o se detengan.")],
            [T("Crossing the road", "Cruzar la calzada"), T("Only at authorised, signed crossings (warning sign for livestock, “cañada”), or other places that are safe.",
                                                           "Solo por pasos autorizados y señalizados (señal de animales, «cañada») o por otros lugares seguros.")],
            [T("Forbidden", "Prohibido"), T("Entering pedestrian zones; leaving animals <b>unattended</b> where they could get onto the road; taking them on <b>autopistas or autovías</b> (animal-drawn vehicles too); "
                                           "making them <b>run</b> near others of their kind or near pedestrians, or letting them roam.",
                                           "Invadir zonas peatonales; dejarlos <b>sin custodia</b> donde puedan invadir la vía; circular por <b>autopistas o autovías</b> (también vehículos de tracción animal); "
                                           "llevarlos <b>corriendo</b> cerca de otros de su especie o de peatones, o abandonarlos.")],
            [T("Narrow points and junctions", "Estrechamientos e intersecciones"), T("Where their path meets that of vehicles, <b>animals give way to vehicles</b>.", "Donde se crucen las trayectorias, <b>ceden el paso a los vehículos</b>.")],
            [T("At night", "De noche"), T("On a poorly lit road or with poor visibility, carry lights on the side nearest the centre: <b>white or yellow in front, red behind</b>.",
                                         "En vía insuficientemente iluminada o con poca visibilidad, luces en el lado más próximo al centro: <b>blanca o amarilla delante, roja detrás</b>.")],
        ],
        widths=["26%", "74%"],
    ))

    # ---------------------------------------------------------------- 12. traps
    B.append(H2("12", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("Signalling a manoeuvre does <b>not</b> give you the right to make it.", "Señalizar una maniobra <b>no</b> da derecho a realizarla."),
        ("<b>Holding</b> the phone is already an offence, even if you are not using it.", "<b>Sujetar</b> el móvil ya es infracción, aunque no se use."),
        ("Radar <b>warning</b> apps are legal; radar <b>detectors</b> and <b>jammers</b> are not.", "Los <b>avisadores</b> de radar son legales; los <b>detectores</b> e <b>inhibidores</b>, no."),
        ("<b>Autopista</b>: no access from properties. <b>Autovía</b>: limited access. Both: no level crossings.",
         "<b>Autopista</b>: sin accesos. <b>Autovía</b>: accesos limitados. Ambas: sin cruces a nivel."),
        ("Cyclists <b>over 14</b> may use the shoulder of an <b>autovía</b>, never of an autopista.", "Los ciclistas <b>mayores de 14 años</b> pueden ir por el arcén de la <b>autovía</b>, nunca de la autopista."),
        ("Two-way road with three lanes: the <b>left</b> lane is never used; the <b>centre</b> one only to overtake or turn left.",
         "Doble sentido con tres carriles: el <b>izquierdo</b> nunca; el <b>central</b> solo para adelantar o girar a la izquierda."),
        ("Heavy vehicles on 3+ lanes: right lane and, exceptionally, the next one: threshold <b>7 m</b>. The 50 m gap: threshold <b>10 m</b>.",
         "Pesados en 3 o más carriles: el derecho y excepcionalmente el contiguo: umbral de <b>7 m</b>. Distancia de 50 m: umbral de <b>10 m</b>."),
        ("In town with marked lanes you choose the lane for your destination, but <b>not</b> on an autopista or autovía through the town.",
         "En poblado con carriles delimitados se elige el que convenga al destino, pero <b>no</b> en una autopista o autovía que cruce el poblado."),
        ("Minimum-speed lanes <b>count</b> as lanes; bus, bike, acceleration, deceleration and waiting lanes <b>do not</b>.",
         "Los carriles de velocidad mínima <b>cuentan</b>; los de bus, bici, aceleración, deceleración y espera <b>no</b>."),
        ("Emergency corridor: <b>2 lanes</b> → in the centre; <b>3 or more</b> → between the left lane and the next one.",
         "Carril de emergencia: <b>2 carriles</b> → en el centro; <b>3 o más</b> → entre el izquierdo y su contiguo."),
        ("Bicycles <b>may</b> ride two abreast on the shoulder, and the 15 s / 200 m overtaking limit does <b>not</b> apply to them: it is for the <b>other</b> shoulder vehicles.",
         "Las bicicletas <b>pueden</b> ir en columna de a dos por el arcén y el límite de 15 s / 200 m para adelantar <b>no</b> va con ellas: es para los <b>demás</b> obligados a usar el arcén."),
        ("In a saturated queue, going faster in the right lane is <b>not</b> overtaking; using the shoulder to reach an exit is still forbidden.",
         "En una vía saturada, ir más rápido por el carril derecho <b>no</b> es adelantar; usar el arcén para llegar a la salida sigue prohibido."),
        ("Pedestrians walk on the <b>left</b>; pushing a bicycle or leading a group puts them on the <b>right</b>.",
         "El peatón va por la <b>izquierda</b>; si empuja una bicicleta o dirige un grupo, por la <b>derecha</b>."),
        ("A herd may never take more than the <b>right half</b> of the carriageway, and its keeper must be <b>over 18</b>.",
         "Un rebaño nunca ocupa más de la <b>mitad derecha</b> de la calzada, y su conductor debe ser <b>mayor de 18 años</b>."),
    ]))

    # ---------------------------------------------------------------- 13. key numbers
    B.append(H2("13", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Minimum ability to use autopista / autovía", "Capacidad mínima para autopista / autovía"), T("&gt; 60 km/h on the flat", "&gt; 60 km/h en llano")],
            [T("Cyclists on an autovía shoulder", "Ciclistas por el arcén de autovía"), T("over 14 years old", "mayores de 14 años")],
            [T("Must use the carriageway, not the shoulder", "Obligados a la calzada, no al arcén"), T("automobiles; special vehicles &gt; 3,500 kg", "automóviles; especiales &gt; 3.500 kg")],
            [T("Restricted to right lane + next one (3+ lanes, out of town)", "Solo carril derecho + contiguo (3 o más carriles, interurbana)"),
             T("trucks, vans, special vehicles &gt; 3,500 kg; combinations &gt; 7 m", "camiones, furgones, especiales &gt; 3.500 kg; conjuntos &gt; 7 m")],
            [T("VAO lane", "Carril VAO"), T("MMA ≤ 3,500 kg; usually ≥ 2 occupants incl. driver", "MMA ≤ 3.500 kg; normalmente ≥ 2 ocupantes con el conductor")],
            [T("Additional and contraflow lanes", "Carril adicional y en sentido contrario"), T("dipped beam; 60 – 80 km/h", "luz de cruce; 60 – 80 km/h")],
            [T("Shoulder: service vehicles / motorcycles in jams", "Arcén: vehículos de servicio / motos en atascos"), T("≤ 30 km/h / ≤ 30 km/h", "≤ 30 km/h / ≤ 30 km/h")],
            [T("Shoulder vehicles overtaking each other (not bicycles)", "Adelantamiento entre obligados al arcén (no bicis)"), T("forbidden if &gt; 15 s or &gt; 200 m side by side", "prohibido si &gt; 15 s o &gt; 200 m en paralelo")],
            [T("Breakdown: drive on to the exit on the shoulder", "Avería: seguir hasta la salida por el arcén"), T("vehicles ≤ 3,500 kg", "vehículos ≤ 3.500 kg")],
            [T("Minimum gap out of town", "Separación mínima fuera de poblado"), T("50 m for MMA &gt; 3,500 kg or length &gt; 10 m", "50 m para MMA &gt; 3.500 kg o longitud &gt; 10 m")],
            [T("Chevrons", "Galones"), T("at least 2", "al menos 2")],
            [T("Tunnels", "Túneles"), T("100 m or 4 s (2 chevrons); &gt; 3,500 kg: 150 m or 6 s (3 chevrons)", "100 m o 4 s (2 galones); &gt; 3.500 kg: 150 m o 6 s (3 galones)")],
            [T("Traffic levels (share of normal speed)", "Niveles de circulación (velocidad respecto a la normal)"),
             T("white &gt; 90 % · green 75–90 % · yellow 25–75 % · red &lt; 25 % · black = closed", "blanco &gt; 90 % · verde 75–90 % · amarillo 25–75 % · rojo &lt; 25 % · negro = cortada")],
            [T("Children cycling on the pavement (if allowed)", "Niños en bici por la acera (si se autoriza)"), T("up to 12, with an adult on foot", "hasta 12 años, con un adulto a pie")],
            [T("Pedestrian reflective item", "Elemento reflectante del peatón"), T("visible from 150 m", "visible a 150 m")],
            [T("Person leading animals", "Conductor de animales"), T("over 18", "mayor de 18 años")],
        ],
        widths=["46%", "54%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["bn1", "ty2", "ln2", "ln4", "rs5", "fl2", "fl5", "sh3", "ds2", "ds4", "pd2", "an1"]


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
    ("Ley sobre Tráfico, Circulación de Vehículos a Motor y Seguridad Vial (RDL 6/2015): Anexo I definitions and arts. 10, 13, 14", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722"),
    ("Reglamento General de Circulación (RD 1428/2003) — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Ley 18/2021: mobile phone held in the hand", "https://www.boe.es/eli/es/l/2021/12/20/18"),
    ("Real Decreto 970/2020: urban roads, VMP and related changes to the Reglamento General de Circulación", "https://www.boe.es/eli/es/rd/2020/11/10/970"),
    ("DGT press release, 23-06-2026: Real Decreto 518/2026 (motorcycles on the shoulder, emergency corridor, snow), in force 1 October 2026",
     "https://www.dgt.es/comunicacion/notas-de-prensa/20260623-RD-usuarios-vulnerables"),
    ("DGT press release, 22-01-2026: VAO lanes and cars with environmental labels", "https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/nota_prensa/2026/20260122_Nota_de_prensa.pdf"),
    ("DGT, carriles BUS-VAO", "https://www.dgt.es/conoce-el-estado-del-trafico/carriles-bus-vao/index.html"),
]

GLOSSARY = [
    ("vía pública", "public road"),
    ("plataforma · calzada · carril", "road platform · carriageway · lane"),
    ("arcén · mediana", "hard shoulder · median (central reservation)"),
    ("zona peatonal · acera · refugio", "pedestrian zone · pavement · pedestrian refuge"),
    ("isleta", "traffic island"),
    ("rasante · cambio de rasante", "gradient · brow (change of gradient)"),
    ("apartadero", "lay-by"),
    ("zona de frenado de emergencia", "emergency escape lane"),
    ("vía (calzada) de servicio", "service road"),
    ("intersección · glorieta", "junction · roundabout"),
    ("carril bici · acera bici · pista bici · senda ciclable", "cycle lane · pavement cycle track · segregated cycle track · shared path"),
    ("vía interurbana · vía urbana · travesía", "interurban road · urban road · road through a town"),
    ("autopista · autovía", "motorway · dual carriageway"),
    ("vía para automóviles · carretera convencional", "road for automobiles · ordinary road"),
    ("variante", "bypass"),
    ("carril de aceleración / deceleración", "acceleration / deceleration lane"),
    ("carril trenzado · carril de espera", "weaving lane · waiting (turning) lane"),
    ("carril VAO", "high-occupancy vehicle lane"),
    ("carril reversible", "reversible lane"),
    ("carril adicional circunstancial", "temporary additional lane"),
    ("carril en sentido contrario al habitual", "contraflow lane"),
    ("carril de emergencia", "emergency corridor"),
    ("retención · vía saturada", "queue · congested road"),
    ("quitanieves", "snowplough"),
    ("distancia de seguridad · galones", "safety distance · chevrons"),
    ("cinemómetro · inhibidor · detector · avisador", "speed camera · jammer · detector · (legal) warning device"),
    ("escape libre", "open exhaust (no silencer)"),
    ("luz de corto alcance o de cruce", "dipped headlights"),
    ("paso para peatones", "pedestrian crossing"),
    ("autostop", "hitch-hiking"),
    ("vía pecuaria · cañada", "livestock track · drove road"),
    ("ganado · manada · rebaño", "livestock · herd · flock"),
    ("animales de tiro, carga o silla", "draught, pack or saddle animals"),
]
