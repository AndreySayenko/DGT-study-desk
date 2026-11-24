# -*- coding: utf-8 -*-
"""Topic 1 content, bilingual. Every text is a (EN, ES) pair.

Original wording based on: Ley sobre Tráfico (RDL 6/2015, Anexo I), Reglamento General de Vehículos
(RD 2822/1998, Anexos II and IX, as amended by Orden PJC/780/2025 and Orden PJC/528/2026), RD 970/2020,
RD 52/2026, Reglamento (UE) 168/2013, DGT Instruction 17/TV-97.
"""

from blocks import T, pills, H2, H3, P, E, FIG, TABLE, BOX, BR  # noqa: F401
from .diagrams import tree, ladder, masses, categories, coupling


# ------------------------------------------------------------------------------------------
def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(
        BOX(
            "key",
            "What this topic is really about",
            "De qué va realmente este tema",
            [
                (
                    "Almost every exam question here is a <b>classification question</b>: “is this a motor vehicle?”, “is this a "
                    "<i>turismo</i> or a <i>camión</i>?”, “which mass can never be exceeded?”.",
                    "Casi todas las preguntas de este tema son de <b>clasificación</b>: «¿es un vehículo de motor?», «¿es un "
                    "turismo o un camión?», «¿qué masa no se puede superar nunca?».",
                ),
                (
                    "The traps are <b>numbers</b> (25 km/h, 250 W, 45 km/h, 50 cm³, 425 kg, 750 kg, 3,500 kg, 9 seats) and "
                    "<b>exceptions</b> (mopeds, pedal-assist bicycles and personal-mobility vehicles are <i>not</i> “motor vehicles” in law).",
                    "Las trampas son los <b>números</b> (25 km/h, 250 W, 45 km/h, 50 cm³, 425 kg, 750 kg, 3.500 kg, 9 plazas) y "
                    "las <b>excepciones</b> (ciclomotores, bicicletas de pedaleo asistido y VMP <i>no</i> son «vehículos de motor» para la ley).",
                ),
                (
                    "The exam is in Spanish. In this English edition the Spanish term appears in <i>italics</i> beside each English "
                    "term; a Spanish–English glossary closes the document.",
                    "Para repasar, los términos clave llevan su equivalente en inglés en el glosario final (ES–EN).",
                ),
            ],
        )
    )

    # ---------------------------------------------------------------- 1. general definitions
    B.append(H2("1", "General definitions: the road and the people on it", "Definiciones generales: la vía y quienes la usan"))
    B.append(
        P(
            "Traffic law applies to the places listed first below. Learn what counts as a road before you learn who is on it.",
            "La ley de tráfico se aplica a los lugares que se citan primero. Primero hay que saber qué es una vía y después quién la usa.",
        )
    )
    B.append(
        E(
            "Roads and terrain covered by the law (<i>vías o terrenos aptos para la circulación</i>)",
            "Vías y terrenos a los que se aplica la ley",
            "The law applies to <b>(1)</b> public roads and terrain suitable for traffic, <b>(2)</b> roads and terrain not suitable for "
            "traffic but in common use, and <b>(3)</b>, where no other rule applies, <b>private</b> roads used by an undetermined group of users "
            "(for example a car park open to anyone, or a private road open to the general public).",
            "La ley se aplica a <b>(1)</b> las vías y terrenos públicos aptos para la circulación, <b>(2)</b> las vías y terrenos que, sin "
            "serlo, son de uso común y <b>(3)</b>, si no hay otra norma, las vías y terrenos <b>privados</b> que utiliza una colectividad "
            "indeterminada de usuarios (por ejemplo, un aparcamiento abierto a cualquiera).",
            tip=(
                "A private road used only by its owners is outside the law; the same road open to the public is inside it.",
                "Una vía privada que solo usan sus dueños queda fuera de la ley; la misma vía abierta al público queda dentro.",
            ),
        )
    )
    B.append(
        TABLE(
            [T("Term", "Término"), T("Meaning", "Significado")],
            [
                [
                    T("Urban road (<i>vía urbana</i>)", "Vía urbana"),
                    T("Public road <b>inside a built-up area</b> (<i>poblado</i>), except <i>travesías</i>.",
                      "Vía pública situada <b>dentro de poblado</b>, excepto travesías."),
                ],
                [
                    T("Interurban road (<i>vía interurbana</i>)", "Vía interurbana"),
                    T("Public road <b>outside built-up areas</b>.", "Vía pública situada <b>fuera de poblado</b>."),
                ],
                [
                    T("Built-up area (<i>poblado</i>)", "Poblado"),
                    T("Space containing buildings, with the entry and exit signs of the town placed on the roads that lead in and out.",
                      "Espacio con edificios cuyas vías de entrada y salida llevan colocadas las señales de entrada y salida de poblado."),
                ],
                [
                    T("<i>Travesía</i> (road through a town)", "Travesía"),
                    T("Stretch of a <b>road</b> (carretera) that runs through a built-up area.",
                      "Tramo de <b>carretera</b> que discurre por poblado."),
                ],
                [
                    T("Carriageway (<i>calzada</i>)", "Calzada"),
                    T("Part of the road intended for vehicles; it is made up of lanes.",
                      "Parte de la carretera destinada a la circulación de vehículos; se compone de carriles."),
                ],
                [
                    T("Hard shoulder (<i>arcén</i>)", "Arcén"),
                    T("Paved strip beside the carriageway, not meant for motor vehicles except in exceptional circumstances.",
                      "Franja longitudinal pavimentada contigua a la calzada, no destinada al uso de automóviles más que en circunstancias excepcionales."),
                ],
                [
                    T("Lane (<i>carril</i>)", "Carril"),
                    T("Longitudinal band of the carriageway, marked or not, wide enough for one line of cars (not motorcycles).",
                      "Banda longitudinal en que puede subdividirse la calzada, delimitada o no por marcas viales, con anchura suficiente para una fila de automóviles que no sean motocicletas."),
                ],
            ],
            widths=["30%", "70%"],
        )
    )

    # ---------------------------------------------------------------- 2. road users
    B.append(H2("2", "Road users", "Los usuarios de la vía"))
    B.append(
        FIG(
            tree,
            "Figure 1. Who is on the road, and where each vehicle family sits. The yellow branch is the one the exam likes to hide.",
            "Figura 1. Quién circula por la vía y dónde encaja cada familia de vehículos. La rama amarilla es la que más se esconde en el examen.",
        )
    )
    B.append(
        E(
            "Driver (<i>conductor</i>)",
            "Conductor",
            "The person who handles the steering mechanism or is in command of a vehicle, <b>or who is in charge of an animal or animals</b>. "
            "When a vehicle is used for driving instruction, the driver is the person in charge of the <b>additional controls</b> (the instructor).",
            "La persona que maneja el mecanismo de dirección o va al mando de un vehículo, <b>o que está a cargo de uno o más animales</b>. "
            "En un vehículo que circula en función de aprendizaje de la conducción, es conductor quien está a cargo de los <b>mandos adicionales</b> (el profesor).",
            tip=(
                "So someone leading a horse on the road is, legally, a <i>conductor</i>.",
                "Así, quien conduce un caballo por la vía es, legalmente, <i>conductor</i>.",
            ),
        )
    )
    B.append(
        E(
            "Pedestrian (<i>peatón</i>)",
            "Peatón",
            "A person who, without being a driver, travels <b>on foot</b>. Also treated as pedestrians: people <b>pushing or pulling</b> a pram, a "
            "wheelchair or another small vehicle without a motor; people <b>walking beside a bicycle or a two-wheeled moped</b> they are "
            "pushing; and people with reduced mobility moving <b>at walking pace in a wheelchair</b>, motorised or not.",
            "La persona que, sin ser conductor, transita <b>a pie</b>. También se consideran peatones: quienes <b>empujan o arrastran</b> un coche de niño, "
            "una silla de ruedas u otro vehículo pequeño sin motor; quienes <b>conducen a pie un ciclo o un ciclomotor de dos ruedas</b>; y las "
            "personas con movilidad reducida que circulan <b>al paso en silla de ruedas</b>, con o sin motor.",
            tip=(
                "Riding a bicycle = driver. Pushing the same bicycle by hand = pedestrian.",
                "Montado en la bicicleta = conductor. Empujándola a mano = peatón.",
            ),
        )
    )
    B.append(
        E(
            "Animals (<i>animales</i>)",
            "Animales",
            "Animals ridden, herded or pulling a vehicle are also on the road. The person in charge of them is the <i>conductor</i> (see above) and "
            "has to follow the traffic rules that apply to the animal's position on the road.",
            "Los animales montados, conducidos o que tiran de un vehículo también circulan por la vía. La persona a su cargo es el <i>conductor</i> "
            "(véase arriba) y debe cumplir las normas de circulación que le correspondan.",
        )
    )

    # ---------------------------------------------------------------- 3. vehicles overview
    B.append(H2("3", "Vehicles: the big picture", "Los vehículos: visión de conjunto"))
    B.append(
        P(
            "Legally, a vehicle (<i>vehículo</i>) is any apparatus able to travel on the roads and terrain covered by the law (section 1). "
            "The whole of this topic is a sorting exercise with three bins:",
            "Legalmente, vehículo es todo aparato apto para circular por las vías y terrenos a los que se aplica la ley (apartado 1). "
            "Todo este tema consiste en clasificar los vehículos en tres grupos:",
        )
    )
    B.append(
        TABLE(
            [T("Bin", "Grupo"), T("What goes in it", "Qué incluye"), T("Is it a “motor vehicle” in law?", "¿Es «vehículo de motor» para la ley?")],
            [
                [
                    T("<b>Without a motor</b> (<i>sin motor</i>)", "<b>Sin motor</b>"),
                    T("Cycles, trailers, semi-trailers, caravans, animal-drawn carts.",
                      "Ciclos, remolques, semirremolques, caravanas, vehículos de tracción animal."),
                    T("No", "No"),
                ],
                [
                    T("<b>With a motor but not counted as a motor vehicle</b>", "<b>Con motor pero «no considerados de motor»</b>"),
                    T("Mopeds (<i>ciclomotores</i>), pedal-assist cycles (<i>EPAC</i>), personal-mobility vehicles (<i>VMP</i>), "
                      "vehicles for people with reduced mobility, trams.",
                      "Ciclomotores, bicicletas de pedaleo asistido (EPAC), vehículos de movilidad personal (VMP), vehículos para personas "
                      "de movilidad reducida, tranvías."),
                    T("<b>No</b> — the law excludes them by name", "<b>No</b>: la ley los excluye expresamente"),
                ],
                [
                    T("<b>Motor vehicles</b> (<i>vehículos de motor</i>)", "<b>Vehículos de motor</b>"),
                    T("<i>Automóviles</i> (cars, buses, trucks, motorcycles…) and <i>vehículos especiales</i>.",
                      "Automóviles (turismos, autobuses, camiones, motocicletas…) y vehículos especiales."),
                    T("Yes", "Sí"),
                ],
            ],
            widths=["26%", "50%", "24%"],
        )
    )
    B.append(
        BOX(
            "trap",
            "The sentence to memorise",
            "La frase que hay que memorizar",
            [
                (
                    "<b>Motor vehicle</b> (<i>vehículo de motor</i>) = a vehicle fitted with an engine for propulsion, <b>excluding</b> mopeds, trams, "
                    "vehicles for people with reduced mobility, pedal-assist cycles (EPAC) and personal-mobility vehicles (VMP).",
                    "<b>Vehículo de motor</b> = vehículo provisto de motor para su propulsión, <b>excluidos</b> los ciclomotores, los tranvías, los "
                    "vehículos para personas de movilidad reducida, los ciclos de pedales con pedaleo asistido (EPAC) y los VMP.",
                ),
                (
                    "<b>Automóvil</b> = a motor vehicle that normally carries people or goods (or both) or tows other vehicles for that purpose. "
                    "<i>Vehículos especiales</i> are excluded from the word “automóvil”.",
                    "<b>Automóvil</b> = vehículo de motor que sirve normalmente para el transporte de personas o cosas, o de ambas a la vez, "
                    "o para la tracción de otros vehículos con ese fin. Los vehículos especiales quedan excluidos de este término.",
                ),
            ],
        )
    )

    # ---------------------------------------------------------------- 4. vehicles without motor
    B.append(H2("4", "Vehicles without a motor", "Vehículos sin motor"))
    B.append(
        E(
            "Cycle (<i>ciclo</i>) and bicycle (<i>bicicleta</i>)",
            "Ciclo y bicicleta",
            "A cycle has <b>at least two wheels</b> and is propelled <b>only by the muscular effort of the people riding it</b>, mainly through pedals or "
            "cranks. A bicycle is the two-wheeled cycle; a tricycle has three wheels.",
            "Un ciclo tiene <b>al menos dos ruedas</b> y se propulsa <b>solo con el esfuerzo muscular de quienes lo ocupan</b>, sobre todo mediante "
            "pedales o manivelas. La bicicleta es el ciclo de dos ruedas; el triciclo tiene tres.",
            pills_=[T("≥ 2 wheels", "≥ 2 ruedas"), T("muscle power only", "solo fuerza muscular")],
        )
    )
    B.append(
        E(
            "Trailer (<i>remolque</i>)",
            "Remolque",
            "A vehicle <b>without its own propulsion</b>, designed and built to be towed by a motor vehicle. It carries its own weight on its own axles.",
            "Vehículo <b>no autopropulsado</b>, proyectado y construido para ser remolcado por un vehículo de motor. Soporta su peso sobre sus propios ejes.",
            pills_=[T("light trailer (<i>remolque ligero</i>): MMA ≤ 750 kg", "remolque ligero: MMA ≤ 750 kg")],
            tip=(
                "The 750 kg limit refers to the <b>maximum authorised mass (MMA)</b>, not to the empty weight.",
                "Los 750 kg se refieren a la <b>masa máxima autorizada (MMA)</b>, no al peso en vacío.",
            ),
        )
    )
    B.append(
        E(
            "Semi-trailer (<i>semirremolque</i>)",
            "Semirremolque",
            "A towed vehicle whose axle(s) sit <b>behind the centre of gravity</b> (with an even load) and which has a coupling device that "
            "transmits <b>horizontal and vertical forces</b> to the towing vehicle: part of its weight rests on the tractor unit.",
            "Vehículo remolcado cuyo eje o ejes están <b>detrás del centro de gravedad</b> (con carga uniforme) y que lleva un dispositivo de acoplamiento "
            "que transmite <b>esfuerzos horizontales y verticales</b> al vehículo tractor: parte de su peso descansa sobre el tractocamión.",
        )
    )
    B.append(
        E(
            "Caravan (<i>caravana</i> / <i>remolque vivienda</i>)",
            "Caravana (remolque vivienda)",
            "A trailer built to be lived in. It is a trailer first: it has no engine and follows the trailer rules.",
            "Remolque construido para servir de vivienda. Es ante todo un remolque: no tiene motor y sigue las normas de los remolques.",
        )
    )
    B.append(
        FIG(
            coupling,
            "Figure 2. Same truck, two different legal names: <i>tren de carretera</i> (truck + trailer) and <i>vehículo articulado</i> (tractor unit + semi-trailer).",
            "Figura 2. Dos conjuntos distintos con nombre legal distinto: tren de carretera (camión + remolque) y vehículo articulado (tractocamión + semirremolque).",
        )
    )
    B.append(
        TABLE(
            [T("Combination", "Conjunto"), T("Made of", "Formado por"), T("Key idea", "Idea clave")],
            [
                [
                    T("Road train (<i>tren de carretera</i>)", "Tren de carretera"),
                    T("motor vehicle + <b>trailer</b>", "vehículo de motor + <b>remolque</b>"),
                    T("Trailer is <b>hitched</b> and bears its own weight.", "El remolque se <b>engancha</b> y soporta su propio peso."),
                ],
                [
                    T("Articulated vehicle (<i>vehículo articulado</i>)", "Vehículo articulado"),
                    T("tractor unit (<i>tractocamión</i>) + <b>semi-trailer</b>", "tractocamión + <b>semirremolque</b>"),
                    T("Semi-trailer is <b>coupled</b> and leans on the tractor.", "El semirremolque se <b>acopla</b> y se apoya en el tractocamión."),
                ],
            ],
            widths=["30%", "34%", "36%"],
        )
    )

    # ---------------------------------------------------------------- 5. light vehicles
    B.append(H2("5", "Light vehicles: from the kick-scooter to the moped", "Vehículos ligeros: del patinete al ciclomotor"))
    B.append(
        P(
            "This is the part of the topic with the most numbers. Figure 3 lines the vehicles up by speed; the cards below give the exact limits.",
            "Es la parte del tema con más números. La figura 3 ordena los vehículos por velocidad; las fichas siguientes dan los límites exactos.",
        )
    )
    B.append(
        FIG(
            ladder,
            "Figure 3. Speed ladder. Everything left of 25 km/h is pedal- or electric-assist; 45 km/h is the border between moped and motorcycle.",
            "Figura 3. Escalera de velocidades. A la izquierda de 25 km/h está lo asistido; los 45 km/h separan el ciclomotor de la motocicleta.",
        )
    )
    B.append(
        E(
            "Personal-mobility vehicle (<i>vehículo de movilidad personal, VMP</i>)",
            "Vehículo de movilidad personal (VMP)",
            "A vehicle with <b>one or more wheels</b>, a <b>single place</b>, propelled <b>exclusively by electric motors</b>, whose design speed is <b>between 6 and 25 km/h</b> "
            "(electric scooters, self-balancing boards and unicycles). It may have a seat only if it is self-balancing. "
            "It is <b>not</b> a VMP if it is a competition vehicle, a vehicle for people with reduced mobility, a pedal-assist cycle, or a vehicle with a working "
            "voltage above 100 V DC / 240 V AC. VMPs must carry an official <b>certificate</b>, be <b>entered in the DGT register</b> "
            "(light personal vehicles register, created by Royal Decree 52/2026), show an <b>identification label</b> and have <b>civil-liability insurance</b>.",
            "Vehículo de <b>una o más ruedas</b>, con <b>una única plaza</b>, propulsado <b>exclusivamente por motores eléctricos</b>, cuya velocidad máxima por diseño está "
            "<b>entre 6 y 25 km/h</b> (patinetes eléctricos, monociclos, plataformas autoequilibradas). Solo puede llevar asiento si es autoequilibrado. "
            "<b>No</b> es VMP si es un vehículo de competición, un vehículo para personas con movilidad reducida, una bicicleta de pedaleo asistido o si "
            "su tensión de trabajo supera 100 V CC / 240 V CA. Los VMP deben tener <b>certificado</b>, estar <b>inscritos en el registro de la DGT</b> "
            "(registro de vehículos personales ligeros, creado por el Real Decreto 52/2026), llevar <b>distintivo</b> y tener <b>seguro de responsabilidad civil</b>.",
            pills_=[T("6 – 25 km/h", "6 – 25 km/h"), T("1 place", "1 plaza"), T("electric only", "solo eléctrico"), T("not a motor vehicle", "no es vehículo de motor")],
            tip=(
                "VMPs sold before 22 January 2024 may keep circulating without a certificate until <b>22 January 2027</b>; after that date only certified VMPs may circulate.",
                "Los VMP comercializados antes del 22 de enero de 2024 pueden circular sin certificado hasta el <b>22 de enero de 2027</b>; después solo podrán circular los VMP certificados.",
            ),
        )
    )
    B.append(
        E(
            "Pedal-assist bicycle (<i>bicicleta de pedaleo asistido, EPAC</i>)",
            "Bicicleta de pedaleo asistido (EPAC)",
            "A cycle with pedals and an <b>auxiliary electric motor</b> whose <b>continuous rated power is at most 250 W</b>. The assistance <b>fades out and finally cuts off before the "
            "vehicle reaches 25 km/h</b>, and also whenever the rider <b>stops pedalling</b>. It needs no licence, registration or compulsory insurance, and it is <b>not</b> a motor vehicle in law.",
            "Ciclo con pedales y <b>motor eléctrico auxiliar</b> de <b>potencia nominal continua máxima de 250 W</b>. La ayuda <b>disminuye progresivamente y se interrumpe antes de que "
            "el vehículo alcance los 25 km/h</b> y también cuando el ciclista <b>deja de pedalear</b>. No requiere permiso, matrícula ni seguro obligatorio y <b>no</b> es vehículo de motor para la ley.",
            pills_=[T("≤ 250 W", "≤ 250 W"), T("cuts off before 25 km/h", "se corta antes de 25 km/h"), T("must pedal", "hay que pedalear")],
        )
    )
    B.append(
        E(
            "Motor cycle (<i>ciclo de motor</i>, EU class L1e-A)",
            "Ciclo de motor (clase UE L1e-A)",
            "A bicycle-type vehicle designed to be pedalled, with an auxiliary motor <b>stronger than an EPAC</b>: <b>continuous power up to 1,000 W</b>, assistance cutting out at "
            "<b>25 km/h or less</b>. Unlike the EPAC it is <b>not</b> on the law’s list of exclusions, so it is a motor vehicle that has to be <b>registered</b>. "
            "Since <b>30 May 2026</b> it has its own classification code, <b>07</b>, in the DGT registry.",
            "Vehículo tipo bicicleta, concebido para pedalear, con un motor auxiliar <b>más potente que el de una EPAC</b>: <b>potencia continua de hasta 1.000 W</b> y asistencia que se corta a "
            "<b>25 km/h o menos</b>. A diferencia de la EPAC <b>no</b> está en la lista de exclusiones de la ley, así que es un vehículo de motor y hay que <b>matricularlo</b>. "
            "Desde el <b>30 de mayo de 2026</b> tiene su propio código de clasificación, el <b>07</b>, en el registro de la DGT.",
            pills_=[T("≤ 1,000 W", "≤ 1.000 W"), T("cuts off at ≤ 25 km/h", "se corta a ≤ 25 km/h"), T("code 07", "código 07")],
        )
    )
    B.append(
        E(
            "Moped, 2 or 3 wheels (<i>ciclomotor de dos o tres ruedas</i>)",
            "Ciclomotor de dos o tres ruedas",
            "A two- or three-wheeled vehicle whose <b>maximum speed by construction is no more than 45 km/h</b> and whose engine is <b>no larger than 50 cm³</b> if it is an internal-combustion "
            "engine (or no more than 4 kW if electric). Mopeds are registered and carry a plate, but the law does <b>not</b> count them as motor vehicles.",
            "Vehículo de dos o tres ruedas cuya <b>velocidad máxima por construcción no supera los 45 km/h</b> y cuyo motor es de <b>cilindrada no superior a 50 cm³</b> si es de combustión interna "
            "(o de potencia no superior a 4 kW si es eléctrico). Los ciclomotores se matriculan y llevan placa, pero la ley <b>no</b> los considera vehículos de motor.",
            pills_=[T("≤ 45 km/h", "≤ 45 km/h"), T("≤ 50 cm³", "≤ 50 cm³"), T("electric: ≤ 4 kW", "eléctrico: ≤ 4 kW")],
            tip=(
                "Exceed either limit (more than 45 km/h <b>or</b> more than 50 cm³) and it is a <b>motorcycle</b>.",
                "Si supera cualquiera de los dos límites (más de 45 km/h <b>o</b> más de 50 cm³) es una <b>motocicleta</b>.",
            ),
        )
    )
    B.append(
        E(
            "Four-wheel moped / light quadricycle (<i>ciclomotor de cuatro ruedas, cuatriciclo ligero</i>)",
            "Ciclomotor de cuatro ruedas (cuatriciclo ligero)",
            "A four-wheeled vehicle with <b>at most two seats, driver included</b>; <b>mass in running order of 425 kg or less</b> (batteries of electric vehicles not counted); "
            "maximum speed by construction <b>45 km/h</b>; engine up to <b>50 cm³ if spark-ignition</b> or <b>500 cm³ for other combustion engines</b>; "
            "maximum power <b>4 kW or 6 kW</b>, depending on its EU approval category.",
            "Vehículo de cuatro ruedas con <b>un máximo de dos plazas, incluida la del conductor</b>; <b>masa en orden de marcha de 425 kg o menos</b> (sin contar las baterías de los eléctricos); "
            "velocidad máxima por construcción de <b>45 km/h</b>; motor de hasta <b>50 cm³ si es de encendido por chispa</b> o de <b>500 cm³ en los demás motores de combustión</b>; "
            "potencia máxima de <b>4 kW o 6 kW</b>, según su categoría de homologación europea.",
            pills_=[T("2 seats max", "máx. 2 plazas"), T("≤ 425 kg running order", "≤ 425 kg en orden de marcha"), T("≤ 45 km/h", "≤ 45 km/h")],
            tip=(
                "Older manuals say “empty weight 350 kg and 4 kW”. That was replaced in July 2025: the figure now is <b>425 kg mass in running order</b>.",
                "Los manuales antiguos dicen «350 kg de tara y 4 kW». Se cambió en julio de 2025: ahora es <b>425 kg de masa en orden de marcha</b>.",
            ),
        )
    )
    B.append(
        E(
            "Vehicle for people with reduced mobility (<i>vehículo para personas de movilidad reducida</i>)",
            "Vehículo para personas de movilidad reducida",
            "A vehicle with an <b>empty weight (tara) of no more than 350 kg</b> that <b>cannot exceed 45 km/h on level ground</b> by construction, "
            "<b>designed and built specially</b> (not merely adapted) for people with a physical disability. It is not a motor vehicle in law and it is <b>not a VMP</b>.",
            "Vehículo cuya <b>tara no es superior a 350 kg</b> y que, por construcción, <b>no puede superar los 45 km/h en llano</b>, "
            "<b>proyectado y construido especialmente</b> (no meramente adaptado) para el uso de personas con alguna discapacidad física. No es vehículo de motor para la ley y <b>no es un VMP</b>.",
            pills_=[T("tara ≤ 350 kg", "tara ≤ 350 kg"), T("≤ 45 km/h", "≤ 45 km/h"), T("built for the purpose", "construido a propósito")],
        )
    )
    B.append(
        E(
            "Tram (<i>tranvía</i>)",
            "Tranvía",
            "A vehicle that runs on <b>rails laid in the road</b>. Excluded from the motor-vehicle definition.",
            "Vehículo que circula por <b>raíles instalados en la vía</b>. Excluido de la definición de vehículo de motor.",
        )
    )

    # ---------------------------------------------------------------- 6. motor vehicles
    B.append(H2("6", "Motor vehicles", "Vehículos de motor"))
    B.append(
        P(
            "Once you have removed the five excluded groups, what is left is a motor vehicle. There are two branches: <i>automóviles</i> and <i>vehículos especiales</i>.",
            "Si se quitan los cinco grupos excluidos, lo que queda es un vehículo de motor. Tiene dos ramas: automóviles y vehículos especiales.",
        )
    )
    B.append(H3("Two- and three-wheeled automóviles", "Automóviles de dos y tres ruedas"))
    B.append(
        E(
            "Motorcycle (<i>motocicleta</i>)",
            "Motocicleta",
            "A two-wheeled motor vehicle, with or without sidecar, whose engine is <b>over 50 cm³</b> (if internal combustion) <b>and/or</b> whose maximum speed by construction is <b>over 45 km/h</b>.",
            "Automóvil de dos ruedas, con o sin sidecar, con motor de cilindrada <b>superior a 50 cm³</b> (si es de combustión interna) <b>y/o</b> velocidad máxima por construcción <b>superior a 45 km/h</b>.",
            pills_=[T("> 50 cm³ and/or > 45 km/h", "> 50 cm³ y/o > 45 km/h")],
        )
    )
    B.append(
        E(
            "Three-wheeled vehicle (<i>vehículo de tres ruedas</i>)",
            "Vehículo de tres ruedas",
            "A motor vehicle with <b>three symmetrical wheels</b> and an engine over 50 cm³ (combustion) and/or a speed over 45 km/h.",
            "Automóvil de <b>tres ruedas simétricas</b> con motor de más de 50 cm³ (combustión) y/o velocidad superior a 45 km/h.",
        )
    )
    B.append(
        E(
            "Heavy quadricycle (<i>cuatriciclo pesado</i>)",
            "Cuatriciclo pesado",
            "A four-wheeled vehicle that is beyond the light-quadricycle limits but still small: <b>mass in running order up to 450 kg</b> (passenger version) or <b>600 kg</b> (goods version), "
            "batteries excluded, and <b>maximum power 15 kW</b> (EU category L7e).",
            "Vehículo de cuatro ruedas que supera los límites del ligero pero sigue siendo pequeño: <b>masa en orden de marcha de hasta 450 kg</b> (transporte de personas) o <b>600 kg</b> (mercancías), "
            "sin contar las baterías, y <b>potencia máxima de 15 kW</b> (categoría europea L7e).",
            pills_=[T("450 kg / 600 kg", "450 kg / 600 kg"), T("≤ 15 kW", "≤ 15 kW")],
            tip=("Older manuals give an empty mass of 400 kg (550 kg for goods). The Reglamento now refers to EU category L7e, which uses mass in running order.",
                 "Los manuales antiguos dan una masa en vacío de 400 kg (550 kg para mercancías). El Reglamento remite hoy a la categoría europea L7e, que usa la masa en orden de marcha."),
        )
    )
    B.append(H3("Cars, buses and trucks", "Turismos, autobuses y camiones"))
    B.append(
        E(
            "Passenger car (<i>turismo</i>)",
            "Turismo",
            "A motor vehicle for carrying people with <b>at most nine seats, driver included</b>.",
            "Automóvil destinado al transporte de personas con <b>un máximo de nueve plazas, incluida la del conductor</b>.",
            pills_=[T("≤ 9 seats incl. driver", "≤ 9 plazas con conductor")],
        )
    )
    B.append(
        E(
            "Bus / coach (<i>autobús</i>)",
            "Autobús",
            "A motor vehicle for carrying people with <b>more than nine seats, driver included</b>.",
            "Automóvil destinado al transporte de personas con <b>más de nueve plazas, incluida la del conductor</b>.",
            pills_=[T("> 9 seats incl. driver", "> 9 plazas con conductor")],
        )
    )
    B.append(
        E(
            "Truck (<i>camión</i>)",
            "Camión",
            "A motor vehicle with four or more wheels, built to carry goods, whose <b>cab is not integrated</b> in the rest of the bodywork, with at most nine seats including the driver. "
            "The definition sets <b>no mass</b>: there are trucks of any MMA (the register classifies them up to 3,500 kg, from 3,500 to 12,000 kg and over 12,000 kg).",
            "Automóvil de cuatro o más ruedas, concebido y construido para el transporte de mercancías, cuya <b>cabina no está integrada</b> en el resto de la carrocería y con un máximo de nueve plazas, incluido el conductor. "
            "La definición <b>no fija ninguna masa</b>: hay camiones de cualquier MMA (el registro los clasifica hasta 3.500 kg, de 3.500 a 12.000 kg y de más de 12.000 kg).",
            pills_=[T("separate cab", "cabina independiente"), T("any MMA", "cualquier MMA")],
        )
    )
    B.append(
        E(
            "Van (<i>furgoneta</i>)",
            "Furgoneta",
            "A motor vehicle with four or more wheels, built to carry goods, whose <b>cab is integrated</b> in the rest of the bodywork, with at most nine seats including the driver. "
            "Like the truck, it can have <b>any MMA</b>: the cab, not the mass, tells a van from a truck.",
            "Automóvil de cuatro o más ruedas, concebido y construido para el transporte de mercancías, cuya <b>cabina está integrada</b> en el resto de la carrocería y con un máximo de nueve plazas, incluido el conductor. "
            "Como el camión, puede tener <b>cualquier MMA</b>: lo que distingue la furgoneta del camión es la cabina, no la masa.",
            pills_=[T("integrated cab", "cabina integrada"), T("any MMA", "cualquier MMA")],
            tip=("3,500 kg is the line for the B licence and for category N1, not the line between a van and a truck.",
                 "3.500 kg es la frontera del permiso B y de la categoría N1, no la que separa la furgoneta del camión."),
        )
    )
    B.append(
        E(
            "Adaptable mixed vehicle (<i>vehículo mixto adaptable</i>)",
            "Vehículo mixto adaptable",
            "A motor vehicle arranged to carry <b>people and goods</b> (together or not), in which the load can be replaced, wholly or in part, by people by <b>adding seats</b>.",
            "Automóvil dispuesto para transportar <b>personas y mercancías</b> (a la vez o no), en el que la carga puede sustituirse total o parcialmente por personas <b>añadiendo asientos</b>.",
        )
    )
    B.append(
        E(
            "Pick-up (<i>pick-up</i>)",
            "Pick-up",
            "A vehicle of <b>no more than 3,500 kg</b> whose seats and cargo area are <b>not in a single compartment</b> and whose <b>total height does not exceed 2 m</b> (DGT Instruction 17/TV-97). "
            "For traffic rules (for example speed limits) it is treated <b>like a car (<i>turismo</i>)</b>, not like a truck. It has its own classification code, 17.",
            "Vehículo de <b>no más de 3.500 kg</b> cuyas plazas de asiento y zona de carga <b>no están en un compartimento único</b> y cuya <b>altura total no supera los 2 m</b> (Instrucción 17/TV-97 de la DGT). "
            "A efectos de las normas de circulación (por ejemplo, límites de velocidad) se trata <b>como un turismo</b>, no como un camión. Tiene su propio código de clasificación, el 17.",
            pills_=[T("MMA ≤ 3,500 kg", "MMA ≤ 3.500 kg"), T("height ≤ 2 m", "altura ≤ 2 m"), T("treated as a car", "como un turismo")],
        )
    )
    B.append(
        E(
            "Motorhome (<i>autocaravana</i>) and tractor unit (<i>tractocamión</i>)",
            "Autocaravana y tractocamión",
            "A <b>motorhome</b> is a motor vehicle built for a special purpose that includes living accommodation. A <b>tractor unit</b> is a motor vehicle designed mainly to tow a semi-trailer.",
            "La <b>autocaravana</b> es un vehículo construido con propósito especial que incluye alojamiento vivienda. El <b>tractocamión</b> es un automóvil concebido para arrastrar principalmente un semirremolque.",
        )
    )
    B.append(H3("Special vehicles", "Vehículos especiales"))
    B.append(
        E(
            "Special vehicle (<i>vehículo especial</i>)",
            "Vehículo especial",
            "A self-propelled or towed vehicle <b>built for specific works or services</b> which, because of its features, is <b>exempt from some technical requirements</b> or "
            "<b>permanently exceeds the limits</b> for mass or dimensions. Typical examples: agricultural tractors, mobile cranes, building-site machinery. "
            "They are motor vehicles but <b>not</b> “<i>automóviles</i>”.",
            "Vehículo autopropulsado o remolcado, <b>concebido y construido para realizar obras o servicios determinados</b>, que por sus características está <b>exceptuado de alguna condición técnica</b> "
            "o <b>sobrepasa permanentemente los límites</b> de masas o dimensiones. Ejemplos: tractores agrícolas, grúas móviles, maquinaria de obras. "
            "Son vehículos de motor pero <b>no</b> «automóviles».",
        )
    )

    # ---------------------------------------------------------------- 7. masses
    B.append(H2("7", "Masses and weights", "Masas y pesos"))
    B.append(
        FIG(
            masses,
            "Figure 4. How the masses stack up. The MMA is a ceiling set on paper; the real load must stay below it.",
            "Figura 4. Cómo se suman las masas. La MMA es un techo fijado por la administración; la carga real debe quedar por debajo.",
        )
    )
    B.append(
        TABLE(
            [T("Term", "Término"), T("What it is", "Qué es")],
            [
                [
                    T("Tara (<i>unladen mass</i>)", "Tara"),
                    T("Mass of the empty vehicle in working order with its fixed equipment: no driver, no passengers, no load.",
                      "Masa del vehículo vacío, en orden de funcionamiento y con su equipo fijo: sin conductor, pasajeros ni carga."),
                ],
                [
                    T("Mass in running order (<i>masa en orden de marcha</i>)", "Masa en orden de marcha"),
                    T("<b>Tara + 75 kg</b> (standard driver). For buses and coaches add <b>another 75 kg</b> if a crew member rides along.",
                      "<b>Tara + 75 kg</b> (conductor estándar). En autobuses y autocares se suman <b>otros 75 kg</b> si lleva acompañante."),
                ],
                [
                    T("Laden mass (<i>masa en carga</i>)", "Masa en carga"),
                    T("Real mass of the vehicle with whatever it is carrying at that moment.",
                      "Masa real del vehículo con lo que transporta en ese momento."),
                ],
                [
                    T("Maximum authorised mass (<i>masa máxima autorizada, MMA</i>)", "Masa máxima autorizada (MMA)"),
                    T("Maximum mass the vehicle may have <b>when loaded on public roads</b>. It is a <b>limit</b>; the laden mass must never exceed it.",
                      "Masa máxima con que puede circular el vehículo <b>cargado por las vías públicas</b>. Es un <b>límite</b>: la masa en carga nunca debe superarlo."),
                ],
                [
                    T("Maximum technically permissible mass (<i>MMTA</i>)", "Masa máxima técnicamente admisible (MMTA)"),
                    T("Maximum mass the manufacturer declares for the vehicle’s construction. The authorised mass (MMA) cannot exceed it.",
                      "Masa máxima que declara el fabricante por construcción. La MMA no puede superarla."),
                ],
                [
                    T("Axle mass (<i>masa por eje</i>)", "Masa por eje"),
                    T("Weight that rests on the road through the wheels of one axle. Each axle has its own limit.",
                      "Peso que gravita sobre la calzada a través de las ruedas de un eje. Cada eje tiene su propio límite."),
                ],
                [
                    T("Combination MMA (<i>MMA del conjunto</i>)", "MMA del conjunto"),
                    T("Maximum mass of a motor vehicle <b>plus its trailer</b>, both loaded.",
                      "Masa máxima del vehículo de motor <b>más su remolque</b>, ambos cargados."),
                ],
            ],
            widths=["30%", "70%"],
        )
    )
    B.append(
        BOX(
            "trap",
            "Mass traps",
            "Trampas con las masas",
            [
                (
                    "“Running order” already includes a <b>75 kg driver</b>. Passengers and luggage are not in it.",
                    "La «masa en orden de marcha» ya incluye un <b>conductor de 75 kg</b>. Los pasajeros y el equipaje no están en ella.",
                ),
                (
                    "Light trailer = <b>MMA</b> up to 750 kg (not tara). Pick-up, the B licence and category N1 = <b>MMA</b> up to 3,500 kg.",
                    "Remolque ligero = <b>MMA</b> de hasta 750 kg (no tara). Pick-up, permiso B y categoría N1 = <b>MMA</b> de hasta 3.500 kg.",
                ),
            ],
        )
    )

    # ---------------------------------------------------------------- 8. categories
    B.append(H2("8", "Vehicle categories (EU classification)", "Categorías de vehículos (clasificación europea)"))
    B.append(
        P(
            "Europe sorts vehicles into letter categories. In Spain they appear on the vehicle documents. The mass limits below are on the <b>maximum authorised mass</b>.",
            "Europa clasifica los vehículos por letras. En España aparecen en la documentación del vehículo. Los límites de masa son de la <b>masa máxima autorizada</b>.",
        )
    )
    B.append(
        FIG(
            categories,
            "Figure 5. Categories M (people), N (goods) and O (trailers) by maximum authorised mass in tonnes.",
            "Figura 5. Categorías M (personas), N (mercancías) y O (remolques) por masa máxima autorizada en toneladas.",
        )
    )
    B.append(
        TABLE(
            [T("Category", "Categoría"), T("Designed for", "Destinado a"), T("Limit", "Límite")],
            [
                [T("<b>M1</b>", "<b>M1</b>"), T("People", "Personas"), T("Up to 8 seats besides the driver’s (= 9 with the driver)", "Hasta 8 plazas además de la del conductor (= 9 con conductor)")],
                [T("<b>M2</b>", "<b>M2</b>"), T("People", "Personas"), T("More than 8 seats besides the driver’s; MMA ≤ 5 t", "Más de 8 plazas además de la del conductor; MMA ≤ 5 t")],
                [T("<b>M3</b>", "<b>M3</b>"), T("People", "Personas"), T("More than 8 seats besides the driver’s; MMA &gt; 5 t", "Más de 8 plazas además de la del conductor; MMA &gt; 5 t")],
                [T("<b>N1</b>", "<b>N1</b>"), T("Goods", "Mercancías"), T("MMA ≤ 3.5 t", "MMA ≤ 3,5 t")],
                [T("<b>N2</b>", "<b>N2</b>"), T("Goods", "Mercancías"), T("MMA &gt; 3.5 t and ≤ 12 t", "MMA &gt; 3,5 t y ≤ 12 t")],
                [T("<b>N3</b>", "<b>N3</b>"), T("Goods", "Mercancías"), T("MMA &gt; 12 t", "MMA &gt; 12 t")],
                [T("<b>O1</b>", "<b>O1</b>"), T("Trailers", "Remolques"), T("MMA ≤ 0.75 t", "MMA ≤ 0,75 t")],
                [T("<b>O2</b>", "<b>O2</b>"), T("Trailers", "Remolques"), T("MMA &gt; 0.75 t and ≤ 3.5 t", "MMA &gt; 0,75 t y ≤ 3,5 t")],
                [T("<b>O3</b>", "<b>O3</b>"), T("Trailers", "Remolques"), T("MMA &gt; 3.5 t and ≤ 10 t", "MMA &gt; 3,5 t y ≤ 10 t")],
                [T("<b>O4</b>", "<b>O4</b>"), T("Trailers", "Remolques"), T("MMA &gt; 10 t", "MMA &gt; 10 t")],
            ],
            widths=["14%", "20%", "66%"],
        )
    )
    B.append(H3("Category L: light powered vehicles", "Categoría L: vehículos ligeros de motor"))
    B.append(
        TABLE(
            [T("EU class", "Clase UE"), T("Vehicle", "Vehículo")],
            [
                [T("<b>L1e-A</b>", "<b>L1e-A</b>"), T("Motor cycle (<i>ciclo de motor</i>)", "Ciclo de motor")],
                [T("<b>L1e-B</b>", "<b>L1e-B</b>"), T("Two-wheel moped (<i>ciclomotor de dos ruedas</i>)", "Ciclomotor de dos ruedas")],
                [T("<b>L2e</b>", "<b>L2e</b>"), T("Three-wheel moped", "Ciclomotor de tres ruedas")],
                [T("<b>L3e</b>", "<b>L3e</b>"), T("Two-wheel motorcycle", "Motocicleta de dos ruedas")],
                [T("<b>L4e</b>", "<b>L4e</b>"), T("Motorcycle with sidecar", "Motocicleta con sidecar")],
                [T("<b>L5e</b>", "<b>L5e</b>"), T("Powered tricycle (three-wheeled vehicle)", "Vehículo de tres ruedas (triciclo de motor)")],
                [T("<b>L6e</b>", "<b>L6e</b>"), T("Light quadricycle", "Cuatriciclo ligero")],
                [T("<b>L7e</b>", "<b>L7e</b>"), T("Heavy quadricycle", "Cuatriciclo pesado")],
            ],
            widths=["20%", "80%"],
        )
    )

    # ---------------------------------------------------------------- 9. eco
    B.append(H2("9", "Types of propulsion and environmental labels", "Tipos de propulsión y distintivos ambientales"))
    B.append(
        TABLE(
            [T("Abbreviation", "Siglas"), T("Type", "Tipo"), T("How it works", "Cómo funciona")],
            [
                [T("<b>EV / BEV</b>", "<b>EV / BEV</b>"), T("Battery electric vehicle", "Vehículo eléctrico de batería"),
                 T("Only an electric motor, fed by a battery charged from the grid.", "Solo motor eléctrico, alimentado por una batería que se carga en la red.")],
                [T("<b>REEV</b>", "<b>REEV</b>"), T("Range-extended electric vehicle", "Eléctrico de autonomía extendida"),
                 T("Wheels driven by an electric motor; a small combustion engine on board only generates electricity.", "Las ruedas las mueve un motor eléctrico; un pequeño motor de combustión solo genera electricidad.")],
                [T("<b>FCV / FCHV</b>", "<b>FCV / FCHV</b>"), T("Fuel-cell vehicle / fuel-cell hybrid", "Pila de combustible / híbrido de pila de combustible"),
                 T("Electric motor powered by hydrogen in a fuel cell (the hybrid also has a battery).", "Motor eléctrico alimentado por hidrógeno en una pila de combustible (el híbrido lleva además batería).")],
                [T("<b>HEV / HV</b>", "<b>HEV / HV</b>"), T("Hybrid (not plug-in)", "Híbrido no enchufable"),
                 T("Combustion engine + electric motor; the battery is charged by the engine and by braking.", "Motor de combustión + motor eléctrico; la batería se carga con el motor y al frenar.")],
                [T("<b>PHEV</b>", "<b>PHEV</b>"), T("Plug-in hybrid", "Híbrido enchufable"),
                 T("Hybrid with a battery that can also be charged from the grid; its electric range decides its label.", "Híbrido con batería que también se carga en la red; su autonomía eléctrica decide el distintivo.")],
                [T("<b>HICEV</b>", "<b>HICEV</b>"), T("Hydrogen combustion engine vehicle", "Vehículo de motor de combustión de hidrógeno"),
                 T("Internal-combustion engine that burns hydrogen.", "Motor de combustión interna que quema hidrógeno.")],
            ],
            widths=["16%", "30%", "54%"],
        )
    )
    B.append(
        TABLE(
            [T("Label", "Distintivo"), T("Who gets it", "A quién se concede"), T("Roughly", "Aproximadamente")],
            [
                [T("<b>0 emisiones</b> (blue)", "<b>0 emisiones</b> (azul)"),
                 T("BEV, REEV, PHEV with <b>at least 40 km</b> of electric range, fuel-cell vehicles.", "BEV, REEV, PHEV con <b>al menos 40 km</b> de autonomía eléctrica, vehículos de pila de combustible."),
                 T("Cleanest", "Los más limpios")],
                [T("<b>ECO</b> (blue-green)", "<b>ECO</b> (azul y verde)"),
                 T("PHEV with <b>under 40 km</b>, non-plug-in hybrids (HEV), natural-gas or LPG vehicles that meet label C.", "PHEV con <b>menos de 40 km</b>, híbridos no enchufables (HEV), vehículos de gas natural o GLP que cumplan los criterios del C."),
                 T("Low emissions", "Bajas emisiones")],
                [T("<b>C</b> (green)", "<b>C</b> (verde)"),
                 T("Petrol Euro 4, 5, 6 (registered from about 2006); diesel Euro 6 (from about 2015).", "Gasolina Euro 4, 5 y 6 (matriculados desde 2006 aprox.); diésel Euro 6 (desde 2015 aprox.)."),
                 T("Recent", "Recientes")],
                [T("<b>B</b> (yellow)", "<b>B</b> (amarillo)"),
                 T("Petrol Euro 3 (from about 2000); diesel Euro 4 and 5 (from about 2006).", "Gasolina Euro 3 (desde 2000 aprox.); diésel Euro 4 y 5 (desde 2006 aprox.)."),
                 T("Older", "Más antiguos")],
                [T("<b>No label</b>", "<b>Sin distintivo</b>"),
                 T("Older petrol and diesel vehicles that do not meet label B.", "Gasolina y diésel más antiguos que no cumplen el B."),
                 T("Oldest", "Los más antiguos")],
            ],
            widths=["22%", "56%", "22%"],
        )
    )
    B.append(
        P(
            "The environmental label is vehicle sign <b>V-25</b> (<i>distintivo ambiental</i>), an adhesive on the vehicle. It decides access to low-emission zones and parking rules in many cities. "
            "Always check the registration date and fuel when a question asks “which label?”.",
            "El distintivo ambiental es la señal de vehículo <b>V-25</b>, un adhesivo en el vehículo. Decide el acceso a las zonas de bajas emisiones y la regulación del aparcamiento en muchas ciudades. "
            "Conviene fijarse siempre en la fecha de matriculación y el combustible.",
        )
    )

    # ---------------------------------------------------------------- 10. shared
    B.append(H2("10", "Shared-use vehicles", "Vehículos de uso compartido"))
    B.append(
        E(
            "Shared-use vehicle (<i>vehículo de uso compartido</i>)",
            "Vehículo de uso compartido",
            "A vehicle <b>rented without a driver</b> and used in a chained, intensive way by an <b>indeterminate number of users</b> within a delimited service area, available through "
            "mobile apps (car-sharing). It is identified by the <b>V-26 “shared-use distinctive”</b>, an adhesive sticker; where it is required it goes in the upper-left corner of the windscreen.",
            "Vehículo <b>destinado al alquiler sin conductor</b> y dedicado a un uso concatenado e intensivo por un <b>número indeterminado de usuarios</b> dentro de una zona de servicio delimitada, "
            "disponible mediante aplicaciones móviles (carsharing). Se identifica con la señal <b>V-26 «Distintivo de uso compartido»</b>, un adhesivo que, cuando es exigible, va en el ángulo superior izquierdo del parabrisas.",
            pills_=[T("V-26 sticker", "adhesivo V-26"), T("rented without driver", "alquiler sin conductor")],
        )
    )

    # ---------------------------------------------------------------- 11. tell-apart
    B.append(H2("11", "Tell them apart", "Cómo distinguirlos"))
    B.append(
        TABLE(
            [T("", ""), T("EPAC", "EPAC"), T("Motor cycle (L1e-A)", "Ciclo de motor (L1e-A)"), T("Moped", "Ciclomotor"), T("Motorcycle", "Motocicleta")],
            [
                [T("<b>Power / engine</b>", "<b>Potencia / motor</b>"), T("≤ 250 W", "≤ 250 W"), T("≤ 1,000 W", "≤ 1.000 W"), T("≤ 50 cm³ (≤ 4 kW electric)", "≤ 50 cm³ (≤ 4 kW eléctrico)"), T("&gt; 50 cm³", "&gt; 50 cm³")],
                [T("<b>Speed</b>", "<b>Velocidad</b>"), T("assist cuts off before 25 km/h", "la ayuda se corta antes de 25 km/h"), T("assist cuts off at ≤ 25 km/h", "la ayuda se corta a ≤ 25 km/h"), T("≤ 45 km/h", "≤ 45 km/h"), T("&gt; 45 km/h (or &gt; 50 cm³)", "&gt; 45 km/h (o &gt; 50 cm³)")],
                [T("<b>Counts as motor vehicle?</b>", "<b>¿Vehículo de motor?</b>"), T("No", "No"), T("Yes", "Sí"), T("No", "No"), T("Yes", "Sí")],
                [T("<b>Registration</b>", "<b>Matrícula</b>"), T("No", "No"), T("Yes (code 07)", "Sí (código 07)"), T("Yes", "Sí"), T("Yes", "Sí")],
            ],
            widths=["24%", "17%", "20%", "20%", "19%"],
            cls="small",
        )
    )
    B.append(
        TABLE(
            [T("Vehicle", "Vehículo"), T("People", "Personas"), T("Mass (MMA)", "Masa (MMA)"), T("Key trait", "Rasgo clave")],
            [
                [T("<i>Turismo</i>", "Turismo"), T("≤ 9 incl. driver", "≤ 9 con conductor"), T("—", "—"), T("For people", "Para personas")],
                [T("<i>Autobús</i>", "Autobús"), T("&gt; 9 incl. driver", "&gt; 9 con conductor"), T("—", "—"), T("For people", "Para personas")],
                [T("<i>Furgoneta</i>", "Furgoneta"), T("—", "—"), T("any", "cualquiera"), T("Integrated cab; goods", "Cabina integrada; mercancías")],
                [T("<i>Pick-up</i>", "Pick-up"), T("—", "—"), T("≤ 3,500 kg", "≤ 3.500 kg"), T("Separate cargo area; height ≤ 2 m; treated as a car", "Zona de carga separada; altura ≤ 2 m; se trata como turismo")],
                [T("<i>Camión</i>", "Camión"), T("—", "—"), T("any", "cualquiera"), T("Cab not integrated; goods", "Cabina no integrada; mercancías")],
                [T("<i>Mixto adaptable</i>", "Mixto adaptable"), T("seats can be added", "se pueden añadir asientos"), T("—", "—"), T("People and goods, load swappable for seats", "Personas y mercancías; la carga se puede sustituir por asientos")],
            ],
            widths=["20%", "22%", "18%", "40%"],
            cls="small",
        )
    )

    # ---------------------------------------------------------------- 12. traps
    B.append(H2("12", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(
        BOX(
            "trap",
            "Read twice",
            "Lee dos veces",
            [
                ("A <b>moped</b> has an engine, yet it is <b>not</b> a “motor vehicle” in the law. Same for the EPAC and the VMP.",
                 "Un <b>ciclomotor</b> tiene motor, pero <b>no</b> es «vehículo de motor» para la ley. Igual que la EPAC y el VMP."),
                ("The EPAC’s motor must <b>cut off before 25 km/h</b>. Not 40, not 45.",
                 "El motor de la EPAC debe <b>cortarse antes de 25 km/h</b>. No 40, no 45."),
                ("Pushing a bicycle by hand makes you a <b>pedestrian</b>. Riding it makes you a <b>driver</b>.",
                 "Empujar una bicicleta a mano te hace <b>peatón</b>. Montar en ella te hace <b>conductor</b>."),
                ("Nine seats <b>including the driver</b> is still a car. Ten is a bus. (Same border as M1’s “8 besides the driver”.)",
                 "Nueve plazas <b>con el conductor</b> sigue siendo turismo. Diez es autobús. (Misma frontera que «8 además del conductor» de M1.)"),
                ("A <b>pick-up</b> is treated as a car <b>only if</b> MMA ≤ 3,500 kg, height ≤ 2 m and cargo area separate from the seats.",
                 "Un <b>pick-up</b> se trata como turismo <b>solo si</b> MMA ≤ 3.500 kg, altura ≤ 2 m y zona de carga separada de los asientos."),
                ("Four-wheel moped: <b>425 kg in running order</b>, at most <b>two seats including the driver</b>. Old manuals (350 kg tara) are out of date.",
                 "Ciclomotor de cuatro ruedas: <b>425 kg en orden de marcha</b> y como mucho <b>dos plazas con el conductor</b>. Los manuales antiguos (350 kg de tara) están desfasados."),
                ("<b>N2</b> stops at 12 t; <b>N3</b> starts above it. <b>O3</b> stops at 10 t.",
                 "<b>N2</b> llega hasta 12 t; <b>N3</b> empieza por encima. <b>O3</b> llega hasta 10 t."),
                ("<b>Road train</b> = trailer. <b>Articulated vehicle</b> = semi-trailer.",
                 "<b>Tren de carretera</b> = remolque. <b>Vehículo articulado</b> = semirremolque."),
                ("<b>MMA</b> is a ceiling, not the actual weight. A <b>light trailer</b> is defined by MMA (750 kg).",
                 "La <b>MMA</b> es un techo, no el peso real. El <b>remolque ligero</b> se define por la MMA (750 kg)."),
            ],
        )
    )

    # ---------------------------------------------------------------- 13. key numbers
    B.append(H2("13", "Key numbers on one page", "Números clave en una página"))
    B.append(
        TABLE(
            [T("Item", "Concepto"), T("Number", "Cifra")],
            [
                [T("VMP design speed", "VMP: velocidad de diseño"), T("6 – 25 km/h", "6 – 25 km/h")],
                [T("EPAC", "EPAC"), T("≤ 250 W; assist cuts off before 25 km/h", "≤ 250 W; ayuda cortada antes de 25 km/h")],
                [T("Motor cycle (L1e-A)", "Ciclo de motor (L1e-A)"), T("≤ 1,000 W; assist cuts off at ≤ 25 km/h; code 07", "≤ 1.000 W; ayuda cortada a ≤ 25 km/h; código 07")],
                [T("Moped, 2/3 wheels", "Ciclomotor 2/3 ruedas"), T("≤ 45 km/h; ≤ 50 cm³ (≤ 4 kW electric)", "≤ 45 km/h; ≤ 50 cm³ (≤ 4 kW eléctrico)")],
                [T("Four-wheel moped", "Ciclomotor 4 ruedas"), T("≤ 2 seats; ≤ 425 kg running order; ≤ 45 km/h; ≤ 50 cm³ (spark) / ≤ 500 cm³ (other); ≤ 4 or 6 kW",
                                                                  "≤ 2 plazas; ≤ 425 kg en orden de marcha; ≤ 45 km/h; ≤ 50 cm³ (chispa) / ≤ 500 cm³ (otros); ≤ 4 o 6 kW")],
                [T("Heavy quadricycle", "Cuatriciclo pesado"), T("450 kg (people) / 600 kg (goods); ≤ 15 kW", "450 kg (personas) / 600 kg (mercancías); ≤ 15 kW")],
                [T("Vehicle for reduced mobility", "Vehículo para movilidad reducida"), T("tara ≤ 350 kg; ≤ 45 km/h", "tara ≤ 350 kg; ≤ 45 km/h")],
                [T("Motorcycle", "Motocicleta"), T("&gt; 50 cm³ and/or &gt; 45 km/h", "&gt; 50 cm³ y/o &gt; 45 km/h")],
                [T("Car / bus", "Turismo / autobús"), T("≤ 9 seats / &gt; 9 seats (driver included)", "≤ 9 plazas / &gt; 9 plazas (con conductor)")],
                [T("Truck / van / pick-up", "Camión / furgoneta / pick-up"), T("cab not integrated / cab integrated (both any MMA) / ≤ 3,500 kg and ≤ 2 m high", "cabina no integrada / cabina integrada (ambos con cualquier MMA) / ≤ 3.500 kg y ≤ 2 m de altura")],
                [T("Light trailer", "Remolque ligero"), T("MMA ≤ 750 kg", "MMA ≤ 750 kg")],
                [T("Mass in running order", "Masa en orden de marcha"), T("tara + 75 kg (+ 75 kg crew on buses)", "tara + 75 kg (+ 75 kg acompañante en autobuses)")],
                [T("Categories M2 / M3", "Categorías M2 / M3"), T("&gt; 8 seats besides driver; ≤ 5 t / &gt; 5 t", "&gt; 8 plazas además del conductor; ≤ 5 t / &gt; 5 t")],
                [T("N1 / N2 / N3", "N1 / N2 / N3"), T("≤ 3.5 t / 3.5 – 12 t / &gt; 12 t", "≤ 3,5 t / 3,5 – 12 t / &gt; 12 t")],
                [T("O1 / O2 / O3 / O4", "O1 / O2 / O3 / O4"), T("≤ 0.75 t / ≤ 3.5 t / ≤ 10 t / &gt; 10 t", "≤ 0,75 t / ≤ 3,5 t / ≤ 10 t / &gt; 10 t")],
                [T("Label 0 emisiones (PHEV)", "Distintivo 0 emisiones (PHEV)"), T("≥ 40 km electric range", "≥ 40 km de autonomía eléctrica")],
            ],
            widths=["34%", "66%"],
            cls="small",
        )
    )

    return B


# ------------------------------------------------------------------------------------------
def quiz():
    """12 questions: (question, [A,B,C], correct index, explanation)."""
    Q = []

    def q(en, ena, es, esa, correct, ex_en, ex_es):
        Q.append((T(en, es), [T(a, b) for a, b in zip(ena, esa)], correct, T(ex_en, ex_es)))

    q(
        "Which of these is legally a <b>motor vehicle</b>?",
        ["A moped", "A tram", "A motorcycle"],
        "¿Cuál de estos es legalmente un <b>vehículo de motor</b>?",
        ["Un ciclomotor", "Un tranvía", "Una motocicleta"],
        2,
        "Mopeds and trams are excluded by name; the motorcycle is a motor vehicle.",
        "Ciclomotores y tranvías están excluidos expresamente; la motocicleta es vehículo de motor.",
    )
    q(
        "An EPAC’s electric assistance must cut off…",
        ["before 25 km/h", "at 45 km/h", "at 40 km/h"],
        "La asistencia eléctrica de una EPAC debe cortarse…",
        ["antes de 25 km/h", "a 45 km/h", "a 40 km/h"],
        0,
        "Maximum 250 W; the assist fades out and cuts off before 25 km/h or when the rider stops pedalling.",
        "Máximo 250 W; la ayuda disminuye y se corta antes de 25 km/h o si se deja de pedalear.",
    )
    q(
        "Someone walks beside the bicycle they are pushing. Legally they are a…",
        ["cyclist (driver)", "pedestrian", "passenger"],
        "Una persona camina empujando su bicicleta. Legalmente es…",
        ["ciclista (conductor)", "peatón", "pasajero"],
        1,
        "People who push a cycle or a two-wheeled moped on foot are treated as pedestrians.",
        "Quienes conducen a pie un ciclo o ciclomotor de dos ruedas se consideran peatones.",
    )
    q(
        "A VMP is…",
        ["single-place, electric, 6–25 km/h", "two-place, petrol, up to 45 km/h", "any scooter up to 40 km/h"],
        "Un VMP es…",
        ["monoplaza, eléctrico, de 6 a 25 km/h", "biplaza, de gasolina, hasta 45 km/h", "cualquier patinete de hasta 40 km/h"],
        0,
        "A personal-mobility vehicle has one place and electric propulsion only, and a design speed from 6 to 25 km/h.",
        "El VMP tiene una plaza, propulsión solo eléctrica y velocidad de diseño de 6 a 25 km/h.",
    )
    q(
        "Which one is a <b>moped</b> (<i>ciclomotor</i>) of two wheels?",
        ["60 cm³ and 50 km/h", "50 cm³ and 45 km/h", "125 cm³ and 90 km/h"],
        "¿Cuál es un <b>ciclomotor</b> de dos ruedas?",
        ["60 cm³ y 50 km/h", "50 cm³ y 45 km/h", "125 cm³ y 90 km/h"],
        1,
        "Moped: up to 50 cm³ and 45 km/h by construction. The others are motorcycles.",
        "Ciclomotor: hasta 50 cm³ y 45 km/h por construcción. Los otros son motocicletas.",
    )
    q(
        "The maximum mass in running order of a four-wheel moped is…",
        ["350 kg", "425 kg", "600 kg"],
        "La masa en orden de marcha máxima de un ciclomotor de cuatro ruedas es…",
        ["350 kg", "425 kg", "600 kg"],
        1,
        "Current rule: 425 kg (batteries excluded). The 350 kg tara of older manuals is outdated.",
        "Norma vigente: 425 kg (sin baterías). Los 350 kg de tara de los manuales antiguos están desfasados.",
    )
    q(
        "A vehicle has nine seats including the driver. It is a…",
        ["bus", "car (<i>turismo</i>)", "truck"],
        "Un vehículo tiene nueve plazas incluida la del conductor. Es un…",
        ["autobús", "turismo", "camión"],
        1,
        "Turismo: up to nine seats, driver included. A bus has more than nine.",
        "Turismo: hasta nueve plazas, incluida la del conductor. El autobús tiene más de nueve.",
    )
    q(
        "A pick-up counts as a car for traffic rules if…",
        ["MMA ≤ 3,500 kg, height ≤ 2 m, separate cargo area", "it has a tow bar", "its engine is under 2 litres"],
        "Un pick-up se trata como turismo a efectos de circulación si…",
        ["MMA ≤ 3.500 kg, altura ≤ 2 m y zona de carga separada", "lleva bola de remolque", "su motor es de menos de 2 litros"],
        0,
        "Instruction 17/TV-97: maximum mass up to 3,500 kg, seats and cargo not in one compartment, height up to 2 m.",
        "Instrucción 17/TV-97: masa máxima de hasta 3.500 kg, asientos y carga no en un único compartimento y altura de hasta 2 m.",
    )
    q(
        "A light trailer (<i>remolque ligero</i>) has an MMA of…",
        ["up to 750 kg", "up to 3,500 kg", "over 750 kg"],
        "Un remolque ligero tiene una MMA…",
        ["de hasta 750 kg", "de hasta 3.500 kg", "superior a 750 kg"],
        0,
        "Light trailer: MMA not over 750 kg.",
        "Remolque ligero: MMA no superior a 750 kg.",
    )
    q(
        "Mass in running order =",
        ["tara + 75 kg", "tara + passengers", "MMA − load"],
        "Masa en orden de marcha =",
        ["tara + 75 kg", "tara + pasajeros", "MMA − carga"],
        0,
        "Tara plus the standard driver of 75 kg (and 75 kg more for a bus crew member).",
        "Tara más el conductor estándar de 75 kg (y 75 kg más del acompañante en autobuses).",
    )
    q(
        "Category N2 covers goods vehicles with an MMA…",
        ["above 3.5 t and up to 12 t", "above 12 t", "up to 3.5 t"],
        "La categoría N2 abarca vehículos de mercancías con una MMA…",
        ["superior a 3,5 t y de hasta 12 t", "superior a 12 t", "de hasta 3,5 t"],
        0,
        "N1 up to 3.5 t, N2 above 3.5 t up to 12 t, N3 above 12 t.",
        "N1 hasta 3,5 t, N2 más de 3,5 t y hasta 12 t, N3 más de 12 t.",
    )
    q(
        "A tractor unit coupled to a semi-trailer is a…",
        ["road train", "articulated vehicle", "light trailer"],
        "Un tractocamión acoplado a un semirremolque es un…",
        ["tren de carretera", "vehículo articulado", "remolque ligero"],
        1,
        "Motor vehicle + trailer = road train; tractor unit + semi-trailer = articulated vehicle.",
        "Vehículo de motor + remolque = tren de carretera; tractocamión + semirremolque = vehículo articulado.",
    )
    return Q


SOURCES = [
    ("Ley sobre Tráfico, Circulación de Vehículos a Motor y Seguridad Vial (RDL 6/2015), Anexo I", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722"),
    ("Reglamento General de Vehículos (RD 2822/1998), Anexos II and IX — consolidated", "https://www.boe.es/eli/es/rd/1998/12/23/2822/con"),
    ("Orden PJC/780/2025 (BOE 23-07-2025): updates Anexos II and IX of the Reglamento General de Vehículos", "https://www.boe.es/boe/dias/2025/07/23/pdfs/BOE-A-2025-15231.pdf"),
    ("Orden PCI/810/2018: environmental labels (V-25), shared-use vehicles (V-26) and pick-up classification", "https://www.boe.es/eli/es/o/2018/07/27/pci810"),
    ("DGT, Inscripción de un Vehículo de Movilidad Personal (VMP)", "https://www.dgt.es/nuestros-servicios/tu-vehiculo/matricular-un-vehiculo/inscripcion-vmp/index.html"),
    ("Orden PJC/528/2026 (BOE 29-05-2026): code 07 for “ciclo de motor”", "https://www.boe.es/boe/dias/2026/05/29/pdfs/BOE-A-2026-11580.pdf"),
    ("Real Decreto 52/2026: register of light personal vehicles", "https://www.boe.es/eli/es/rd/2026/01/28/52"),
    ("DGT Instruction 17/TV-97: pick-up vehicles", "https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/muevete-con-seguridad/normas-de-trafico/TV-circulacion/17_TV_97_Vehiculos_pick_up.pdf"),
    ("DGT Instruction 19/V-134: registration of L1e-A vehicles", "https://www.dgt.es/export/sites/web-DGT/.galleries/downloads/muevete-con-seguridad/normas-de-trafico/VEH-vehiculos/19.V-134-Matriculacion-de-vehiculos-L1e-A.pdf"),
    ("Reglamento (UE) 168/2013 (L-category vehicles) and Reglamento (UE) 2018/858 (M, N, O categories)", "https://eur-lex.europa.eu/"),
]

GLOSSARY = [
    ("vía urbana / interurbana", "urban road / interurban road"),
    ("travesía", "stretch of road through a town"),
    ("calzada · arcén · carril", "carriageway · hard shoulder · lane"),
    ("conductor · peatón", "driver · pedestrian"),
    ("ciclo · bicicleta", "cycle · bicycle"),
    ("remolque · semirremolque", "trailer · semi-trailer"),
    ("tren de carretera", "road train (vehicle + trailer)"),
    ("vehículo articulado", "articulated vehicle (tractor unit + semi-trailer)"),
    ("tractocamión", "tractor unit"),
    ("ciclomotor", "moped"),
    ("cuatriciclo ligero / pesado", "light / heavy quadricycle"),
    ("motocicleta", "motorcycle"),
    ("turismo · autobús · camión", "car · bus · truck"),
    ("furgoneta · pick-up", "van · pick-up"),
    ("vehículo mixto adaptable", "adaptable mixed vehicle"),
    ("vehículo especial", "special vehicle"),
    ("vehículo de motor · automóvil", "motor vehicle · automobile (road motor vehicle)"),
    ("bicicleta de pedaleo asistido (EPAC)", "pedal-assist bicycle"),
    ("vehículo de movilidad personal (VMP)", "personal-mobility vehicle"),
    ("vehículo para personas de movilidad reducida", "vehicle for people with reduced mobility"),
    ("tara", "unladen mass (empty weight)"),
    ("masa en orden de marcha", "mass in running order"),
    ("masa en carga", "laden mass"),
    ("masa máxima autorizada (MMA)", "maximum authorised mass"),
    ("masa máxima técnicamente admisible", "maximum technically permissible mass"),
    ("distintivo ambiental", "environmental label"),
    ("vehículo de uso compartido", "shared-use vehicle"),
    ("plaza", "seat / place"),
]
