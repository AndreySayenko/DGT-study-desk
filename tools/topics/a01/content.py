# -*- coding: utf-8 -*-
"""Category A1/A2, Topic 1 content (definitions and general concepts), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Manual Permiso A1/A2, Tema 1: Definiciones y conceptos
generales). The wording and the two new figures are original; three figures are shared with Category B, Topic 1.
The definitions come from the Ley sobre Tráfico (RDL 6/2015, annex I) and the Reglamento General de Vehículos
(RD 2822/1998, annex II, which defines the light and heavy quadricycle by EU Regulation 168/2013), as they stand in
November 2026.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import tree, ladder, masses, who_is_driver, wheel_layouts


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("The legal words the rest of the course uses: who is a <b>pedestrian</b> or a <b>driver</b>, who <b>owns</b> or <b>insures</b> a vehicle, and which family each vehicle belongs to — "
         "above all, where the line falls between a <b>moped</b> and a <b>motorcycle</b>.",
         "Las palabras legales que usa el resto del curso: quién es <b>peatón</b> o <b>conductor</b>, quién es <b>titular</b> o <b>tomador</b>, y a qué familia pertenece cada vehículo; "
         "sobre todo, dónde está la frontera entre <b>ciclomotor</b> y <b>motocicleta</b>."),
        ("The exam loves <b>numbers and exclusions</b>: <b>50 cm³</b> and <b>45 km/h</b>, <b>6–25 km/h</b> for a VMP, <b>350 kg</b> for a reduced-mobility vehicle, <b>750 kg</b> for a light trailer, "
         "and which vehicles are <b>not</b> motor vehicles.",
         "El examen pregunta sobre todo <b>cifras y exclusiones</b>: <b>50 cm³</b> y <b>45 km/h</b>, <b>6–25 km/h</b> para un VMP, <b>350 kg</b> para el vehículo de movilidad reducida, <b>750 kg</b> para el remolque ligero, "
         "y qué vehículos <b>no</b> son vehículos de motor."),
        ("This topic covers much of the same ground as <b>Category B, Topic 1</b>, which goes further (EU categories, environmental labels). The sections here follow the order of your A1/A2 course.",
         "Este tema comparte mucho con el <b>Tema 1 del permiso B</b>, que amplía más (categorías europeas, distintivos ambientales). Aquí los apartados siguen el orden de tu curso A1/A2."),
    ]))

    # ---------------------------------------------------------------- 1. general definitions
    B.append(H2("1", "General definitions", "Definiciones generales"))
    B.append(E(
        "Pedestrian (<i>peatón</i>)", "Peatón",
        "A person who, <b>without being a driver</b>, travels <b>on foot</b> on public roads or on private land in common use. Also pedestrians: people who <b>push or pull</b> a pram, a wheelchair or any other "
        "<b>small vehicle without a motor</b>; people who <b>walk a cycle or a two-wheeled moped</b>; and people with a disability moving <b>at walking pace in a wheelchair</b>, with or without a motor.",
        "Persona que, <b>sin ser conductor</b>, transita <b>a pie</b> por las vías o terrenos públicos o privados de uso común. También son peatones quienes <b>empujan o arrastran</b> un coche de niño, de impedido "
        "o cualquier otro <b>vehículo sin motor de pequeñas dimensiones</b>; quienes <b>conducen a pie un ciclo o un ciclomotor de dos ruedas</b>; y los impedidos que circulan <b>al paso en silla de ruedas</b>, con o sin motor.",
        tip=("Pushing your moped by hand you are a <b>pedestrian</b>; sitting on it with the engine running you are a <b>driver</b>.",
             "Empujando el ciclomotor a pie eres <b>peatón</b>; montado en él y en marcha eres <b>conductor</b>.")))
    B.append(E(
        "Driver (<i>conductor</i>)", "Conductor",
        "A person who handles the <b>steering</b> or is <b>in command of a vehicle</b>, or who is <b>in charge of one or more animals</b>. In a vehicle used for driving lessons, the driver is the person in charge of the "
        "<b>additional controls</b> — the instructor.",
        "Persona que <b>maneja el mecanismo de dirección o va al mando de un vehículo</b>, o <b>a cuyo cargo está un animal o animales</b>. En los vehículos de aprendizaje de la conducción, el conductor es quien está a cargo de los "
        "<b>mandos adicionales</b>: el profesor."))
    B.append(FIG(who_is_driver, "On foot, pushing a moped or a bicycle, or in a wheelchair at walking pace: pedestrian. Riding, in charge of an animal, or the instructor of a learner: driver.",
                 "A pie, llevando a pie un ciclomotor o una bici, o en silla de ruedas al paso: peatón. Montado, a cargo de un animal o el profesor de autoescuela: conductor."))
    B.append(TABLE(
        [T("Term", "Concepto"), T("Who it is", "Quién es")],
        [
            [T("<b>Vehicle owner</b> (<i>titular del vehículo</i>)", "<b>Titular del vehículo</b>"), T("The person in whose name the vehicle is <b>entered in the official register</b>.", "La persona <b>a cuyo nombre figura inscrito el vehículo</b> en el registro oficial.")],
            [T("<b>Policyholder</b> (<i>tomador</i>)", "<b>Tomador</b>"), T("The person who <b>takes out the third-party insurance</b> with the insurer.", "La persona que <b>contrata el seguro de responsabilidad civil</b> del vehículo con la aseguradora.")],
            [T("<b>Habitual driver</b> (<i>conductor habitual</i>)", "<b>Conductor habitual</b>"),
             T("A licence holder who, <b>with their consent</b>, is declared to the vehicle register by the owner (or long-term lessee) because they are the one who <b>drives the vehicle most often</b>.",
               "Persona con permiso de conducir que, <b>con su consentimiento</b>, es declarada al Registro de Vehículos por el titular (o el arrendatario a largo plazo) por ser quien <b>maneja el vehículo con más frecuencia</b>.")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(TABLE(
        [T("Term", "Concepto"), T("Definition", "Definición")],
        [
            [T("<b>Vehicle</b>", "<b>Vehículo</b>"), T("A machine able to travel on public roads, or on private land in common use.", "Aparato apto para circular por las vías o terrenos públicos o privados de uso común.")],
            [T("<b>Motor vehicle</b> (<i>vehículo a motor</i>)", "<b>Vehículo a motor</b>"),
             T("A vehicle with a <b>motor for its propulsion</b>. <b>Not</b> motor vehicles: <b>mopeds, trams, vehicles for people with reduced mobility</b>, pedal-assist bicycles and <b>personal mobility vehicles (VMP)</b>.",
               "Vehículo provisto de <b>motor para su propulsión</b>. <b>Se excluyen</b>: <b>ciclomotores, tranvías, vehículos para personas de movilidad reducida</b>, bicicletas de pedaleo asistido y <b>vehículos de movilidad personal (VMP)</b>.")],
            [T("<b>Automóvil</b>", "<b>Automóvil</b>"), T("A motor vehicle normally used to <b>carry people or goods</b>, or both, or to <b>tow</b> other vehicles for that purpose. <b>Special vehicles are excluded</b>.",
                                                       "Vehículo de motor que sirve, normalmente, <b>para el transporte de personas o cosas</b>, o de ambas, o para la <b>tracción</b> de otros vehículos con ese fin. <b>Se excluyen los vehículos especiales</b>.")],
            [T("<b>Special vehicle</b> (<i>vehículo especial</i>, VE)", "<b>Vehículo especial</b> (VE)"),
             T("Self-propelled or towed, built for <b>works or services</b>, and <b>farm machinery</b> and its trailers. Because of what it is, it is <b>exempt</b> from some technical requirements or <b>permanently exceeds</b> the mass or size limits.",
               "Autopropulsado o remolcado, concebido para <b>realizar obras o servicios</b>, y la <b>maquinaria agrícola</b> y sus remolques. Por sus características, está <b>exento</b> de alguna condición técnica o <b>sobrepasa permanentemente</b> los límites de masas o dimensiones.")],
        ],
        widths=["26%", "74%"],
    ))

    # ---------------------------------------------------------------- 2. users and vehicles
    B.append(H2("2", "Classifying road users", "Clasificación de usuarios"))
    B.append(P(
        "Road users are <b>pedestrians</b>, <b>animals</b> and <b>vehicles</b>. Vehicles fall into three families: <b>without a motor</b>, <b>not considered motor vehicles</b> (they may have a motor, but the law leaves them out), "
        "and <b>motor vehicles</b>, which split into <b>automóviles</b> and <b>special vehicles</b>.",
        "Los usuarios son <b>peatones</b>, <b>animales</b> y <b>vehículos</b>. Los vehículos forman tres familias: <b>sin motor</b>, <b>no considerados de motor</b> (pueden tenerlo, pero la ley los excluye) "
        "y <b>de motor</b>, que se dividen en <b>automóviles</b> y <b>vehículos especiales</b>."))
    B.append(FIG(tree, "Who is on the road, and where each vehicle family sits. The middle branch — vehicles with a motor that are not motor vehicles — is the one the exam likes to hide.",
                 "Quién circula por la vía y dónde encaja cada familia de vehículos. La rama central —vehículos con motor que no son vehículos de motor— es la que más se esconde en el examen."))
    B.append(TABLE(
        [T("Family", "Familia"), T("Vehicles", "Vehículos")],
        [
            [T("<b>Without a motor</b>", "<b>Sin motor</b>"), T("Cycles and bicycles, animal-drawn vehicles, trailers, semi-trailers, caravans.", "Ciclos y bicicletas, vehículos de tracción animal, remolques, semirremolques, caravanas.")],
            [T("<b>Not considered motor vehicles</b>", "<b>No considerados de motor</b>"), T("Two- and three-wheeled mopeds, light quadricycles (four-wheeled mopeds), vehicles for people with reduced mobility, personal mobility vehicles (VMP), trams.",
                                                                                         "Ciclomotores de dos y tres ruedas, cuatriciclos ligeros (ciclomotores de cuatro ruedas), vehículos para personas de movilidad reducida, vehículos de movilidad personal (VMP), tranvías.")],
            [T("<b>Motor vehicles: automóviles</b>", "<b>De motor: automóviles</b>"),
             T("Two-wheeled motorcycles, motorcycles with sidecar, three-wheeled vehicles, quadricycles, cars and car-derived vans, vans, lorries, adaptable mixed vehicles, motorhomes, off-road vehicles, buses and coaches, road trains and articulated vehicles.",
               "Motocicletas de dos ruedas, motocicletas con sidecar, vehículos de tres ruedas, cuatriciclos, turismos y derivados de turismo, furgones y furgonetas, camiones, vehículos mixtos adaptables, autocaravanas, todoterrenos, autobuses o autocares, trenes de carretera y vehículos articulados.")],
            [T("<b>Motor vehicles: special vehicles</b>", "<b>De motor: vehículos especiales</b>"), T("Farm tractors, works tractors, tourist trains, quad-ATVs…", "Tractores agrícolas, tractores de obras, trenes turísticos, quads-ATV…")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(H3("2.1 Vehicles without a motor", "2.1 Vehículos sin motor"))
    B.append(TABLE(
        [T("Vehicle", "Vehículo"), T("Definition", "Definición")],
        [
            [T("<b>Cycle</b> (<i>ciclo</i>)", "<b>Ciclo</b>"), T("A vehicle with <b>at least two wheels</b>, moved by the <b>muscle power</b> of the people on it, through <b>pedals or hand cranks</b>.", "Vehículo de <b>dos ruedas, como mínimo</b>, accionado por el <b>esfuerzo muscular</b> de las personas, mediante <b>pedales o manivelas</b>.")],
            [T("<b>Bicycle</b>", "<b>Bicicleta</b>"), T("A cycle with <b>two wheels</b>.", "Ciclo de <b>dos ruedas</b>.")],
            [T("<b>Animal-drawn vehicle</b>", "<b>Vehículo de tracción animal</b>"), T("A vehicle <b>pulled by animals</b>.", "Vehículo <b>arrastrado por animales</b>.")],
            [T("<b>Trailer</b> (<i>remolque</i>)", "<b>Remolque</b>"), T("A vehicle <b>without its own propulsion</b>, designed to be <b>towed by a motor vehicle</b>. A <b>light trailer</b> has an MMA of up to <b>750 kg</b>.", "Vehículo <b>no autopropulsado</b>, concebido para ser <b>remolcado por un vehículo de motor</b>. El <b>remolque ligero</b> tiene una MMA de hasta <b>750 kg</b>.")],
        ],
        widths=["26%", "74%"],
    ))
    B.append(H3("2.2 Vehicles not considered motor vehicles", "2.2 Vehículos no considerados de motor"))
    B.append(FIG(ladder, "Speed ladder. Up to 25 km/h: VMP and pedal-assisted cycles. Up to 45 km/h: mopeds. Over 45 km/h, or over 50 cm³: a motorcycle.",
                 "Escalera de velocidades. Hasta 25 km/h: VMP y ciclos asistidos. Hasta 45 km/h: ciclomotores. Más de 45 km/h, o más de 50 cm³: motocicleta."))
    B.append(E(
        "Two- or three-wheeled moped (<i>ciclomotor de 2 o 3 ruedas</i>)", "Ciclomotor de dos o tres ruedas",
        "A vehicle whose engine is <b>no larger than 50 cm³</b> if it is an internal-combustion engine, and whose <b>maximum speed by construction is no more than 45 km/h</b>.",
        "Vehículo con motor de <b>cilindrada no superior a 50 cm³</b>, si es de combustión interna, y con una <b>velocidad máxima por construcción no superior a 45 km/h</b>.",
        pills_=[T("≤ 50 cm³", "≤ 50 cm³"), T("≤ 45 km/h", "≤ 45 km/h"), T("not a motor vehicle", "no es vehículo de motor")],
        tip=("Go over <b>either</b> limit — more than 50 cm³ <b>or</b> more than 45 km/h — and it becomes a <b>motorcycle</b>.",
             "Si supera <b>cualquiera</b> de los dos límites —más de 50 cm³ <b>o</b> más de 45 km/h— pasa a ser <b>motocicleta</b>.")))
    B.append(E(
        "Four-wheeled moped / light quadricycle (<i>cuatriciclo ligero</i>)", "Ciclomotor de cuatro ruedas (cuatriciclo ligero)",
        "A four-wheeled vehicle with a <b>maximum speed by construction of 45 km/h</b> and an engine up to <b>50 cm³</b> (spark-ignition). Your course gives the older limits — <b>4 kW</b> for other engines and an <b>empty mass under 350 kg</b>, "
        "batteries excluded. Since July 2025 the rule follows EU category <b>L6e</b>: at most <b>425 kg in running order</b> and <b>two seats</b> (see Category B, Topic 1).",
        "Vehículo de cuatro ruedas con <b>velocidad máxima por construcción de 45 km/h</b> y motor de hasta <b>50 cm³</b> (encendido por chispa). Tu curso da los límites antiguos: <b>4 kW</b> para los demás motores y <b>tara inferior a 350 kg</b>, "
        "sin contar las baterías. Desde julio de 2025 se sigue la categoría europea <b>L6e</b>: como máximo <b>425 kg en orden de marcha</b> y <b>dos plazas</b> (ver Tema 1 del permiso B).",
        pills_=[T("≤ 45 km/h", "≤ 45 km/h"), T("≤ 50 cm³", "≤ 50 cm³"), T("course: tara < 350 kg", "curso: tara < 350 kg")]))
    B.append(E(
        "Personal mobility vehicle (<i>vehículo de movilidad personal</i>, VMP)", "Vehículo de movilidad personal (VMP)",
        "A vehicle with <b>one or more wheels</b> and a <b>single seat or place</b>, driven <b>only by electric motors</b>, with a <b>design speed between 6 and 25 km/h</b>. It may only have a seat or saddle if it has a <b>self-balancing system</b>.",
        "Vehículo de <b>una o más ruedas</b> dotado de una <b>única plaza</b> y propulsado <b>exclusivamente por motores eléctricos</b>, con una <b>velocidad máxima por diseño entre 6 y 25 km/h</b>. Solo puede llevar asiento o sillín si tiene <b>sistema de autoequilibrado</b>.",
        pills_=[T("6–25 km/h", "6–25 km/h"), T("1 place", "1 plaza"), T("electric only", "solo eléctrico")]))
    B.append(E(
        "Vehicle for people with reduced mobility (<i>vehículo para personas de movilidad reducida</i>)", "Vehículo para personas de movilidad reducida",
        "A vehicle <b>designed and built specially</b> — not merely adapted — for people with a physical disability, with a <b>tare of no more than 350 kg</b> and unable to exceed <b>45 km/h</b> on the flat. In its other technical features it is treated like a <b>three-wheeled moped</b>.",
        "Vehículo <b>proyectado y construido especialmente</b> (no meramente adaptado) para personas con alguna disfunción o incapacidad física, con <b>tara no superior a 350 kg</b> y que no puede superar <b>45 km/h</b> en llano. En el resto de características técnicas se equipara a los <b>ciclomotores de tres ruedas</b>.",
        pills_=[T("tara ≤ 350 kg", "tara ≤ 350 kg"), T("≤ 45 km/h", "≤ 45 km/h")]))
    B.append(E("Tram (<i>tranvía</i>)", "Tranvía", "A vehicle that runs on <b>rails laid in the road</b>.", "Vehículo que marcha por <b>raíles instalados en la vía</b>."))

    B.append(H3("2.3 Motor vehicles: motorcycles and their relatives", "2.3 Vehículos de motor (automóviles): motocicletas y similares"))
    B.append(FIG(wheel_layouts, "A sidecar makes three wheels that are not symmetrical about the long axis; a three-wheeled vehicle has three symmetrical wheels.",
                 "El sidecar da tres ruedas asimétricas respecto al eje longitudinal; el vehículo de tres ruedas tiene tres ruedas simétricas."))
    B.append(TABLE(
        [T("Automóvil", "Automóvil"), T("Definition", "Definición")],
        [
            [T("<b>Two-wheeled motorcycle</b>", "<b>Motocicleta de dos ruedas</b>"), T("Two wheels, <b>no sidecar</b>, engine <b>over 50 cm³</b> (combustion) <b>and/or</b> a design speed <b>over 45 km/h</b>.", "Automóvil de <b>2 ruedas, sin sidecar</b>, con motor de <b>más de 50 cm³</b> (combustión interna) <b>y/o</b> velocidad máxima por construcción <b>superior a 45 km/h</b>.")],
            [T("<b>Motorcycle with sidecar</b>", "<b>Motocicleta con sidecar</b>"), T("<b>Three wheels, asymmetrical</b> about the long axis; same engine/speed thresholds.", "Automóvil de <b>3 ruedas asimétricas</b> respecto a su eje medio longitudinal; mismos umbrales de cilindrada y velocidad.")],
            [T("<b>Three-wheeled vehicle</b>", "<b>Vehículo de tres ruedas</b>"), T("<b>Three symmetrical wheels</b>; engine over 50 cm³ (combustion) and/or over 45 km/h.", "Automóvil de <b>3 ruedas simétricas</b>; motor de más de 50 cm³ (combustión) y/o más de 45 km/h.")],
            [T("<b>Motor quadricycle</b> (<i>cuatriciclo de motor</i>)", "<b>Cuatriciclo de motor</b>"),
             T("Four wheels and a maximum net power of <b>15 kW</b>. Your course gives an empty mass of up to <b>400 kg</b> (<b>550 kg</b> for goods), batteries excluded, and says quadricycles are treated as <b>three-wheeled vehicles</b>. "
               "Today the regulation uses EU category <b>L7e</b>: a mass in running order of up to <b>450 kg</b> (<b>600 kg</b> for goods).",
               "Cuatro ruedas y potencia máxima neta de <b>15 kW</b>. Tu curso da una masa en vacío de hasta <b>400 kg</b> (<b>550 kg</b> si es para mercancías), sin las baterías, y dice que tienen la consideración de <b>vehículos de tres ruedas</b>. "
               "Hoy el reglamento remite a la categoría europea <b>L7e</b>: masa en orden de marcha de hasta <b>450 kg</b> (<b>600 kg</b> mercancías).")],
        ],
        widths=["28%", "72%"],
    ))
    B.append(BOX("trap", "“Quad” is not one thing", "«Quad» no es una sola cosa", [
        ("A road-approved <b>quadricycle</b> is an <b>automóvil</b>. A <b>quad-ATV</b> approved as a <b>special vehicle</b> (often for farm or off-road work) belongs to the special-vehicle branch. Check its registration papers.",
         "Un <b>cuatriciclo</b> homologado para circular es un <b>automóvil</b>. Un <b>quad-ATV</b> homologado como <b>vehículo especial</b> (a menudo para trabajos agrícolas o fuera de carretera) es de la rama de vehículos especiales. Lo dice su documentación."),
    ]))

    # ---------------------------------------------------------------- 3. masses
    B.append(H2("3", "Definitions about mass", "Definiciones relativas a la masa"))
    B.append(TABLE(
        [T("Term", "Concepto"), T("Definition", "Definición")],
        [
            [T("<b>Tare</b> (<i>tara</i>, empty mass)", "<b>Tara</b> o masa en vacío"), T("The vehicle with its fixed equipment and full supply of water, fuel, lubricant, tools and accessories — <b>without people or load</b>.", "Masa del vehículo con su equipo fijo autorizado y su dotación completa de agua, combustible, lubricante, herramientas y accesorios, <b>sin personas ni carga</b>.")],
            [T("<b>Laden mass</b> (<i>masa en carga</i>)", "<b>Masa en carga</b>"), T("The actual mass of the vehicle <b>and its load, passengers included</b> — what it weighs right now.", "Masa efectiva del vehículo <b>y de su carga, incluidos los pasajeros</b>: lo que pesa en ese momento.")],
            [T("<b>Maximum authorised mass</b> (MMA)", "<b>Masa máxima autorizada</b> (MMA)"), T("The <b>most a loaded vehicle may weigh</b> to be driven on public roads.", "Lo <b>máximo que puede pesar un vehículo con carga</b> para circular por las vías públicas.")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(FIG(masses, "Tare, mass in running order (tare + 75 kg driver) and laden mass. The MMA is the ceiling the laden mass must never exceed.",
                 "Tara, masa en orden de marcha (tara + 75 kg del conductor) y masa en carga. La MMA es el techo que la masa en carga nunca puede superar."))

    # ---------------------------------------------------------------- 4. traps
    B.append(H2("4", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("Walking a <b>two-wheeled moped</b> or a cycle = <b>pedestrian</b>. In charge of an <b>animal</b> = <b>driver</b>. In a learner vehicle, the driver is the <b>instructor</b>.", "Llevar a pie un <b>ciclomotor de dos ruedas</b> o un ciclo = <b>peatón</b>. A cargo de un <b>animal</b> = <b>conductor</b>. En autoescuela, el conductor es el <b>profesor</b>."),
        ("<b>Titular</b> = name on the register; <b>tomador</b> = who signs the insurance; <b>conductor habitual</b> = declared by the owner, with their consent.", "<b>Titular</b> = a su nombre en el registro; <b>tomador</b> = quien contrata el seguro; <b>conductor habitual</b> = lo declara el titular, con su consentimiento."),
        ("<b>Not</b> motor vehicles: mopeds, trams, reduced-mobility vehicles, pedal-assist bicycles and VMP. Special vehicles are motor vehicles but <b>not automóviles</b>.", "<b>No</b> son vehículos de motor: ciclomotores, tranvías, vehículos de movilidad reducida, bicicletas de pedaleo asistido y VMP. Los especiales son de motor pero <b>no automóviles</b>."),
        ("Moped: ≤ 50 cm³ <b>and</b> ≤ 45 km/h. Motorcycle: > 50 cm³ <b>and/or</b> > 45 km/h.", "Ciclomotor: ≤ 50 cm³ <b>y</b> ≤ 45 km/h. Motocicleta: > 50 cm³ <b>y/o</b> > 45 km/h."),
        ("Sidecar = 3 <b>asymmetric</b> wheels (still a <b>motorcycle</b>); three-wheeled vehicle = 3 <b>symmetric</b> wheels.", "Sidecar = 3 ruedas <b>asimétricas</b> (sigue siendo <b>motocicleta</b>); vehículo de tres ruedas = 3 ruedas <b>simétricas</b>."),
        ("VMP: <b>6–25 km/h</b>, one place, electric only, a seat only if self-balancing.", "VMP: <b>6–25 km/h</b>, una plaza, solo eléctrico, asiento solo si es autoequilibrado."),
        ("Reduced-mobility vehicle: <b>built</b> for it (not adapted), tare ≤ <b>350 kg</b>, ≤ 45 km/h; treated like a <b>three-wheeled moped</b>.", "Vehículo de movilidad reducida: <b>construido</b> para ello (no adaptado), tara ≤ <b>350 kg</b>, ≤ 45 km/h; se equipara al <b>ciclomotor de tres ruedas</b>."),
        ("Tare: <b>no people or load</b>. Laden mass: <b>with</b> passengers and load. MMA: the legal maximum.", "Tara: <b>sin personas ni carga</b>. Masa en carga: <b>con</b> pasajeros y carga. MMA: el máximo legal."),
    ]))

    # ---------------------------------------------------------------- 5. numbers
    B.append(H2("5", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Moped: engine / speed", "Ciclomotor: cilindrada / velocidad"), T("≤ 50 cm³ / ≤ 45 km/h", "≤ 50 cm³ / ≤ 45 km/h")],
            [T("Motorcycle: engine and/or speed", "Motocicleta: cilindrada y/o velocidad"), T("> 50 cm³ and/or > 45 km/h", "> 50 cm³ y/o > 45 km/h")],
            [T("VMP design speed", "Velocidad de diseño del VMP"), T("6–25 km/h", "6–25 km/h")],
            [T("Reduced-mobility vehicle", "Vehículo de movilidad reducida"), T("tare ≤ 350 kg; ≤ 45 km/h", "tara ≤ 350 kg; ≤ 45 km/h")],
            [T("Light quadricycle (course / since July 2025)", "Cuatriciclo ligero (curso / desde julio de 2025)"), T("tare < 350 kg, 4 kW / ≤ 425 kg in running order", "tara < 350 kg, 4 kW / ≤ 425 kg en orden de marcha")],
            [T("Motor quadricycle (course / EU L7e)", "Cuatriciclo de motor (curso / UE L7e)"), T("400 kg (550 goods) / 450 kg (600 goods); 15 kW", "400 kg (550 mercancías) / 450 kg (600 mercancías); 15 kW")],
            [T("Light trailer", "Remolque ligero"), T("MMA ≤ 750 kg", "MMA ≤ 750 kg")],
        ],
        widths=["52%", "48%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["pe2", "pe5", "ow2", "vd2", "vd5", "us2", "nm3", "mp2", "mp6", "mo2", "mo4", "ms2"]


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
    ("Ley sobre Tráfico, Circulación de Vehículos a Motor y Seguridad Vial (RDL 6/2015), annex I: definitions — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722"),
    ("Reglamento General de Vehículos (RD 2822/1998), annex II: vehicle definitions — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-1999-1826"),
    ("Orden PJC/780/2025 (BOE 23-07-2025): updates annexes II and IX of the Reglamento General de Vehículos", "https://www.boe.es/boe/dias/2025/07/23/pdfs/BOE-A-2025-15231.pdf"),
    ("Regulation (EU) No 168/2013 on two- or three-wheel vehicles and quadricycles (categories L1e–L7e)", "https://eur-lex.europa.eu/eli/reg/2013/168/oj"),
]

GLOSSARY = [
    ("peatón", "pedestrian"),
    ("conductor", "driver"),
    ("mandos adicionales", "dual controls (learner vehicle)"),
    ("titular del vehículo", "registered owner"),
    ("tomador (del seguro)", "policyholder"),
    ("conductor habitual", "regular (named) driver"),
    ("vehículo a motor · automóvil", "motor vehicle · automobile"),
    ("vehículo especial", "special vehicle"),
    ("ciclo · bicicleta", "cycle · bicycle"),
    ("vehículo de tracción animal", "animal-drawn vehicle"),
    ("remolque · semirremolque · remolque ligero", "trailer · semi-trailer · light trailer"),
    ("ciclomotor", "moped"),
    ("cuatriciclo ligero / pesado", "light / heavy quadricycle"),
    ("vehículo de movilidad personal (VMP)", "personal mobility vehicle (e-scooter)"),
    ("vehículo para personas de movilidad reducida", "vehicle for people with reduced mobility"),
    ("tranvía", "tram"),
    ("motocicleta · sidecar", "motorcycle · sidecar"),
    ("vehículo de tres ruedas", "three-wheeled vehicle (trike)"),
    ("cilindrada", "engine capacity (cc)"),
    ("velocidad máxima por construcción", "design (maximum) speed"),
    ("eje longitudinal · ruedas simétricas / asimétricas", "long axis · symmetrical / asymmetrical wheels"),
    ("tara (masa en vacío)", "tare (empty mass)"),
    ("masa en orden de marcha", "mass in running order"),
    ("masa en carga", "laden mass"),
    ("masa máxima autorizada (MMA)", "maximum authorised mass"),
]
