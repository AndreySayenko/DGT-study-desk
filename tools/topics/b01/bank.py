# -*- coding: utf-8 -*-
"""Question bank for the interactive Topic 1 page. In every question the FIRST option is the correct one
(the page shuffles options when it shows them)."""

BANK = []


def Q(qid, tag, en, es, opts, why_en, why_es):
    BANK.append({
        "id": qid, "tag": tag,
        "q": {"en": en, "es": es},
        "o": [{"en": a, "es": b} for a, b in opts],
        "why": {"en": why_en, "es": why_es},
    })


# tag -> section number, names, recap bullets, typical confusion
TAGS = {
    "roads": dict(sec=1, en="Roads and where the law applies", es="Vías y ámbito de la ley",
        recap=[("The law covers public roads, roads in common use, and private roads used by an undetermined group of users.",
                "La ley se aplica a vías públicas, vías de uso común y vías privadas usadas por una colectividad indeterminada."),
               ("Vía urbana = inside a built-up area (except travesías). Vía interurbana = outside it.",
                "Vía urbana = dentro de poblado (excepto travesías). Vía interurbana = fuera de poblado."),
               ("Travesía = stretch of a carretera that runs through a built-up area.",
                "Travesía = tramo de carretera que discurre por poblado."),
               ("Arcén = paved strip beside the carriageway, not for cars except in exceptional circumstances.",
                "Arcén = franja pavimentada junto a la calzada, no destinada a automóviles salvo circunstancias excepcionales.")],
        trap=("Mixing up travesía with an ordinary street, and assuming private always means outside the law.",
              "Confundir travesía con una calle cualquiera y creer que lo privado siempre queda fuera de la ley.")),
    "users": dict(sec=2, en="Drivers, pedestrians and animals", es="Conductores, peatones y animales",
        recap=[("Driver = whoever steers a vehicle or is in charge of animals.",
                "Conductor = quien maneja un vehículo o está a cargo de animales."),
               ("In a driving lesson the legal driver is the person at the additional controls.",
                "En el aprendizaje, el conductor legal es quien va a cargo de los mandos adicionales."),
               ("Pedestrian = on foot, pushing a pram or small unpowered vehicle, walking a cycle or two-wheel moped, or in a wheelchair at walking pace.",
                "Peatón = a pie, empujando un cochecito o vehículo pequeño sin motor, llevando a pie un ciclo o ciclomotor de dos ruedas, o en silla de ruedas al paso.")],
        trap=("Forgetting that the same person changes category: riding a bike is driving, pushing it is walking.",
              "Olvidar que la misma persona cambia de categoría: montar en bici es conducir, empujarla es caminar.")),
    "motordef": dict(sec=3, en="What counts as a motor vehicle", es="Qué es un vehículo de motor",
        recap=[("Motor vehicle = vehicle with an engine for propulsion, EXCEPT mopeds, trams, vehicles for people with reduced mobility, EPAC and VMP.",
                "Vehículo de motor = vehículo con motor para su propulsión, EXCEPTO ciclomotores, tranvías, vehículos para personas de movilidad reducida, EPAC y VMP."),
               ("Automóvil = motor vehicle for carrying people or goods or towing. Special vehicles are not automóviles.",
                "Automóvil = vehículo de motor para transportar personas o cosas o para la tracción. Los vehículos especiales no son automóviles.")],
        trap=("Thinking “it has a motor, so it is a motor vehicle”. The law lists five exceptions.",
              "Pensar «tiene motor, luego es vehículo de motor». La ley enumera cinco excepciones.")),
    "nomotor": dict(sec=4, en="Cycles, trailers and combinations", es="Ciclos, remolques y conjuntos",
        recap=[("Cycle = at least two wheels, moved only by the riders' muscle power.",
                "Ciclo = al menos dos ruedas, movido solo por la fuerza muscular de sus ocupantes."),
               ("Light trailer = MMA up to 750 kg.", "Remolque ligero = MMA de hasta 750 kg."),
               ("Semi-trailer = part of its weight rests on the towing vehicle.",
                "Semirremolque = parte de su peso descansa sobre el vehículo tractor."),
               ("Road train = motor vehicle + trailer. Articulated vehicle = tractor unit + semi-trailer.",
                "Tren de carretera = automóvil + remolque. Vehículo articulado = tractocamión + semirremolque.")],
        trap=("Swapping road train and articulated vehicle.", "Intercambiar tren de carretera y vehículo articulado.")),
    "light25": dict(sec=5, en="VMP, EPAC and ciclo de motor (25 km/h group)", es="VMP, EPAC y ciclo de motor (grupo de 25 km/h)",
        recap=[("VMP = one place, electric only, design speed 6–25 km/h. Not a motor vehicle.",
                "VMP = una plaza, solo eléctrico, velocidad de diseño de 6 a 25 km/h. No es vehículo de motor."),
               ("EPAC = up to 250 W, assistance cuts off before 25 km/h or when you stop pedalling. Not a motor vehicle.",
                "EPAC = hasta 250 W, la ayuda se corta antes de 25 km/h o al dejar de pedalear. No es vehículo de motor."),
               ("Ciclo de motor (L1e-A) = up to 1,000 W, assistance cuts off at 25 km/h or less, must be registered (code 07).",
                "Ciclo de motor (L1e-A) = hasta 1.000 W, la ayuda se corta a 25 km/h o menos, hay que matricularlo (código 07)."),
               ("A vehicle for people with reduced mobility is never a VMP.",
                "Un vehículo para personas de movilidad reducida nunca es un VMP.")],
        trap=("Mixing the three power figures (250 W, 1,000 W) and using 45 km/h where the limit is 25.",
              "Mezclar las potencias (250 W, 1.000 W) y usar 45 km/h donde el límite es 25.")),
    "moped": dict(sec=5, en="Mopeds and light quadricycles (45 km/h group)", es="Ciclomotores y cuatriciclos ligeros (grupo de 45 km/h)",
        recap=[("Moped, 2 or 3 wheels = up to 45 km/h and up to 50 cm³ (4 kW if electric).",
                "Ciclomotor de 2 o 3 ruedas = hasta 45 km/h y hasta 50 cm³ (4 kW si es eléctrico)."),
               ("Four-wheel moped = at most 2 seats with the driver, up to 425 kg in running order, up to 45 km/h.",
                "Ciclomotor de 4 ruedas = máximo 2 plazas con el conductor, hasta 425 kg en orden de marcha, hasta 45 km/h."),
               ("Vehicle for people with reduced mobility = tara up to 350 kg, up to 45 km/h, purpose-built.",
                "Vehículo para personas de movilidad reducida = tara de hasta 350 kg, hasta 45 km/h, construido a propósito."),
               ("Break either moped limit (speed or engine size) and it is a motorcycle.",
                "Si supera cualquiera de los dos límites (velocidad o cilindrada) es una motocicleta.")],
        trap=("Using the old 350 kg figure for the four-wheel moped; 350 kg now belongs only to the reduced-mobility vehicle.",
              "Usar los antiguos 350 kg para el ciclomotor de cuatro ruedas; los 350 kg son ahora solo del vehículo para movilidad reducida.")),
    "motos": dict(sec=6, en="Motorcycles and heavy quadricycles", es="Motocicletas y cuatriciclos pesados",
        recap=[("Motorcycle = two wheels, with or without sidecar, over 50 cm³ and/or over 45 km/h.",
                "Motocicleta = dos ruedas, con o sin sidecar, más de 50 cm³ y/o más de 45 km/h."),
               ("Three-wheeled vehicle = three symmetrical wheels, over 50 cm³ and/or over 45 km/h.",
                "Vehículo de tres ruedas = tres ruedas simétricas, más de 50 cm³ y/o más de 45 km/h."),
               ("Heavy quadricycle (L7e) = mass in running order up to 450 kg (people) or 600 kg (goods), up to 15 kW.",
                "Cuatriciclo pesado (L7e) = masa en orden de marcha de hasta 450 kg (personas) o 600 kg (mercancías), hasta 15 kW.")],
        trap=("Confusing the light quadricycle numbers (425 kg, 4 or 6 kW) with the heavy ones (450/600 kg, 15 kW).",
              "Confundir las cifras del cuatriciclo ligero (425 kg, 4 o 6 kW) con las del pesado (450/600 kg, 15 kW).")),
    "carbus": dict(sec=6, en="Cars, buses and mixed vehicles", es="Turismos, autobuses y vehículos mixtos",
        recap=[("Turismo = for people, at most 9 seats including the driver.",
                "Turismo = para personas, máximo 9 plazas incluida la del conductor."),
               ("Autobús = for people, more than 9 seats including the driver.",
                "Autobús = para personas, más de 9 plazas incluida la del conductor."),
               ("Mixto adaptable = people and goods; load can be replaced by people by adding seats.",
                "Mixto adaptable = personas y mercancías; la carga puede sustituirse por personas añadiendo asientos.")],
        trap=("Counting the driver wrongly: 9 with the driver is a car, 10 is a bus.",
              "Contar mal al conductor: 9 con conductor es turismo, 10 es autobús.")),
    "goods": dict(sec=6, en="Trucks, vans, pick-ups and special vehicles", es="Camiones, furgonetas, pick-up y vehículos especiales",
        recap=[("Camión = goods, cab not integrated, at most 9 seats with the driver; any MMA.",
                "Camión = mercancías, cabina no integrada, máximo 9 plazas con el conductor; cualquier MMA."),
               ("Furgoneta = goods, cab integrated, at most 9 seats with the driver; any MMA. The cab, not the mass, tells them apart.",
                "Furgoneta = mercancías, cabina integrada, máximo 9 plazas con el conductor; cualquier MMA. Los distingue la cabina, no la masa."),
               ("Pick-up = up to 3,500 kg, seats and cargo not in one compartment, height up to 2 m. Follows car rules.",
                "Pick-up = hasta 3.500 kg, asientos y carga no en un único compartimento, altura de hasta 2 m. Sigue las normas del turismo."),
               ("Special vehicle = built for specific works or services (tractor, crane). Motor vehicle, but not an automóvil.",
                "Vehículo especial = construido para obras o servicios determinados (tractor, grúa). Es vehículo de motor, pero no automóvil.")],
        trap=("Forgetting one of the three pick-up conditions, or telling a truck from a van by its mass instead of its cab.",
              "Olvidar una de las tres condiciones del pick-up o distinguir el camión de la furgoneta por la masa en vez de por la cabina.")),
    "masses": dict(sec=7, en="Masses and weights", es="Masas y pesos",
        recap=[("Tara = empty vehicle with fixed equipment; no driver, passengers or load.",
                "Tara = vehículo vacío con su equipo fijo; sin conductor, pasajeros ni carga."),
               ("Mass in running order = tara + 75 kg driver (+ 75 kg crew member on buses).",
                "Masa en orden de marcha = tara + 75 kg del conductor (+ 75 kg del acompañante en autobuses)."),
               ("Laden mass = what the vehicle really weighs right now.",
                "Masa en carga = lo que pesa realmente el vehículo en ese momento."),
               ("MMA = the ceiling for a loaded vehicle on public roads. Never exceeded.",
                "MMA = el techo para circular cargado por las vías públicas. Nunca se supera.")],
        trap=("Treating MMA as the real weight, or forgetting the 75 kg driver in running order.",
              "Tomar la MMA por el peso real u olvidar los 75 kg del conductor en la masa en orden de marcha.")),
    "cats": dict(sec=8, en="EU categories M, N, O and L", es="Categorías europeas M, N, O y L",
        recap=[("M = people. M1 up to 8 seats besides the driver; M2 more, MMA up to 5 t; M3 more, MMA over 5 t.",
                "M = personas. M1 hasta 8 plazas además del conductor; M2 más, MMA de hasta 5 t; M3 más, MMA superior a 5 t."),
               ("N = goods. N1 up to 3.5 t; N2 over 3.5 t up to 12 t; N3 over 12 t.",
                "N = mercancías. N1 hasta 3,5 t; N2 más de 3,5 t y hasta 12 t; N3 más de 12 t."),
               ("O = trailers. O1 up to 0.75 t; O2 up to 3.5 t; O3 up to 10 t; O4 over 10 t.",
                "O = remolques. O1 hasta 0,75 t; O2 hasta 3,5 t; O3 hasta 10 t; O4 más de 10 t."),
               ("L = light. L1e-A ciclo de motor, L1e-B moped, L3e motorcycle, L6e light quadricycle, L7e heavy quadricycle.",
                "L = ligeros. L1e-A ciclo de motor, L1e-B ciclomotor, L3e motocicleta, L6e cuatriciclo ligero, L7e cuatriciclo pesado.")],
        trap=("Mixing the borders: 5 t belongs to M, 12 t to N, 10 t to O.",
              "Mezclar las fronteras: 5 t es de M, 12 t de N y 10 t de O.")),
    "eco": dict(sec=9, en="Propulsion, environmental labels and shared use", es="Propulsión, distintivos ambientales y uso compartido",
        recap=[("0 emisiones = BEV, REEV, fuel cell, and PHEV with at least 40 km electric range.",
                "0 emisiones = BEV, REEV, pila de combustible y PHEV con al menos 40 km de autonomía eléctrica."),
               ("ECO = PHEV under 40 km, non-plug-in hybrids, gas vehicles that meet label C.",
                "ECO = PHEV con menos de 40 km, híbridos no enchufables y vehículos de gas que cumplan los criterios del C."),
               ("V-25 = environmental label. V-26 = shared-use vehicle sticker.",
                "V-25 = distintivo ambiental. V-26 = distintivo de vehículo de uso compartido."),
               ("REEV = wheels driven electrically; the small combustion engine only generates electricity.",
                "REEV = las ruedas las mueve el motor eléctrico; el pequeño motor de combustión solo genera electricidad.")],
        trap=("Forgetting that the 40 km line splits plug-in hybrids between 0 emisiones and ECO.",
              "Olvidar que los 40 km reparten a los híbridos enchufables entre 0 emisiones y ECO.")),
}

# ---------------------------------------------------------------- roads
Q("r1", "roads", "A <i>travesía</i> is…", "Una travesía es…",
  [("a stretch of a <i>carretera</i> that runs through a built-up area", "un tramo de carretera que discurre por poblado"),
   ("any street inside a town", "cualquier calle dentro de un poblado"),
   ("a road that joins two motorways", "una vía que une dos autopistas")],
  "A travesía is the part of a carretera that passes through a built-up area.",
  "La travesía es el tramo de carretera que discurre por poblado.")
Q("r2", "roads", "A private car park that any driver may enter. Does the traffic law apply inside?",
  "Un aparcamiento privado en el que puede entrar cualquier conductor. ¿Se aplica dentro la ley de tráfico?",
  [("Yes, because an undetermined group of users uses it", "Sí, porque lo utiliza una colectividad indeterminada de usuarios"),
   ("No, because it is private property", "No, porque es propiedad privada"),
   ("Only if the owner has put up traffic signs", "Solo si el dueño ha colocado señales de tráfico")],
  "Private roads and terrain used by an undetermined group of users fall under the law when no other rule applies.",
  "Las vías y terrenos privados utilizados por una colectividad indeterminada de usuarios quedan dentro de la ley si no hay otra norma.")
Q("r3", "roads", "The <i>arcén</i> (hard shoulder) is…", "El arcén es…",
  [("a paved strip beside the carriageway, not meant for cars except in exceptional circumstances",
    "una franja pavimentada contigua a la calzada, no destinada a automóviles salvo circunstancias excepcionales"),
   ("an extra lane for slow vehicles", "un carril adicional para vehículos lentos"),
   ("the part of the carriageway used for overtaking", "la parte de la calzada que se usa para adelantar")],
  "The hard shoulder is beside the carriageway, not part of it, and cars use it only exceptionally.",
  "El arcén está junto a la calzada, no forma parte de ella, y los automóviles solo lo usan excepcionalmente.")
Q("r4", "roads", "An interurban road (<i>vía interurbana</i>) is…", "Una vía interurbana es…",
  [("a public road outside built-up areas", "una vía pública situada fuera de poblado"),
   ("any road with more than one lane each way", "cualquier vía con más de un carril por sentido"),
   ("a road between two towns, including the stretches inside them", "una vía entre dos poblaciones, incluidos los tramos dentro de ellas")],
  "Interurban means outside built-up areas; the stretch inside a town is a travesía or an urban road.",
  "Interurbana significa fuera de poblado; el tramo dentro de una población es travesía o vía urbana.")

# ---------------------------------------------------------------- users
Q("u1", "users", "Someone walks beside the bicycle they are pushing. Legally they are a…",
  "Una persona camina empujando su bicicleta. Legalmente es…",
  [("pedestrian", "peatón"), ("cyclist (driver)", "ciclista (conductor)"), ("passenger", "pasajero")],
  "People who walk a cycle or a two-wheel moped by hand are treated as pedestrians.",
  "Quienes conducen a pie un ciclo o ciclomotor de dos ruedas se consideran peatones.")
Q("u2", "users", "A person leading a herd of animals along the road is legally a…",
  "La persona que conduce un rebaño por la vía es legalmente…",
  [("driver (<i>conductor</i>)", "conductor"), ("pedestrian", "peatón"), ("neither driver nor pedestrian", "ni conductor ni peatón")],
  "The definition of driver includes whoever is in charge of one or more animals.",
  "La definición de conductor incluye a quien está a cargo de uno o más animales.")
Q("u3", "users", "During a driving lesson in a driving-school car, who is the driver in law?",
  "Durante una clase en un coche de autoescuela, ¿quién es el conductor para la ley?",
  [("The person in charge of the additional controls", "Quien está a cargo de los mandos adicionales"),
   ("The learner at the steering wheel", "El alumno que lleva el volante"),
   ("Both, in equal parts", "Los dos a partes iguales")],
  "In vehicles used for driving instruction, the driver is the person at the additional controls.",
  "En los vehículos en función de aprendizaje, el conductor es quien va a cargo de los mandos adicionales.")
Q("u4", "users", "A person with reduced mobility moves at walking pace in a motorised wheelchair. They are a…",
  "Una persona con movilidad reducida circula al paso en una silla de ruedas con motor. Es…",
  [("pedestrian", "peatón"), ("driver of a VMP", "conductor de un VMP"), ("driver of a motor vehicle", "conductor de un vehículo de motor")],
  "Wheelchair users moving at walking pace are pedestrians, with or without a motor.",
  "Quien circula al paso en silla de ruedas es peatón, con o sin motor.")

# ---------------------------------------------------------------- motordef
Q("m1", "motordef", "Which of these is legally a <b>motor vehicle</b>?", "¿Cuál de estos es legalmente un <b>vehículo de motor</b>?",
  [("A motorcycle", "Una motocicleta"), ("A moped", "Un ciclomotor"), ("A tram", "Un tranvía")],
  "Mopeds and trams are excluded by name; the motorcycle is a motor vehicle.",
  "Ciclomotores y tranvías están excluidos expresamente; la motocicleta es vehículo de motor.")
Q("m2", "motordef", "Which of these is <b>not</b> a motor vehicle in law?", "¿Cuál de estos <b>no</b> es vehículo de motor para la ley?",
  [("A moped", "Un ciclomotor"), ("A car", "Un turismo"), ("A truck", "Un camión")],
  "The moped has an engine but is on the list of exclusions.",
  "El ciclomotor tiene motor, pero está en la lista de exclusiones.")
Q("m3", "motordef", "Which vehicles are left out of the term <i>automóvil</i>?", "¿Qué vehículos quedan fuera del término «automóvil»?",
  [("Special vehicles", "Los vehículos especiales"), ("Trucks", "Los camiones"), ("Motorcycles", "Las motocicletas")],
  "Special vehicles are motor vehicles but are excluded from the definition of automóvil.",
  "Los vehículos especiales son vehículos de motor, pero están excluidos de la definición de automóvil.")
Q("m4", "motordef", "A pedal-assist bicycle (EPAC) has an electric motor. In law it is…",
  "Una bicicleta de pedaleo asistido (EPAC) tiene motor eléctrico. Para la ley es…",
  [("not a motor vehicle", "un vehículo que no es de motor"), ("a motor vehicle, because it has a motor", "un vehículo de motor, porque tiene motor"),
   ("an <i>automóvil</i>", "un automóvil")],
  "Pedal-assist cycles are one of the five groups excluded from the motor-vehicle definition.",
  "Los ciclos de pedaleo asistido son uno de los cinco grupos excluidos de la definición de vehículo de motor.")

# ---------------------------------------------------------------- nomotor
Q("n1", "nomotor", "A tractor unit coupled to a semi-trailer is…", "Un tractocamión acoplado a un semirremolque es…",
  [("an articulated vehicle", "un vehículo articulado"), ("a road train", "un tren de carretera"), ("a light trailer", "un remolque ligero")],
  "Tractor unit + semi-trailer = articulated vehicle.", "Tractocamión + semirremolque = vehículo articulado.")
Q("n2", "nomotor", "A road train (<i>tren de carretera</i>) is made of…", "Un tren de carretera está formado por…",
  [("a motor vehicle hitched to a trailer", "un vehículo de motor enganchado a un remolque"),
   ("a tractor unit coupled to a semi-trailer", "un tractocamión acoplado a un semirremolque"),
   ("two semi-trailers", "dos semirremolques")],
  "Motor vehicle + trailer = road train.", "Vehículo de motor + remolque = tren de carretera.")
Q("n3", "nomotor", "What sets a semi-trailer apart from a trailer?", "¿Qué distingue a un semirremolque de un remolque?",
  [("Part of its weight rests on the towing vehicle", "Parte de su peso descansa sobre el vehículo tractor"),
   ("It has its own engine", "Tiene motor propio"),
   ("Its MMA never exceeds 750 kg", "Su MMA nunca supera los 750 kg")],
  "The semi-trailer's coupling passes vertical forces to the tractor unit, so the tractor carries part of its weight.",
  "El acoplamiento del semirremolque transmite esfuerzos verticales al tractocamión, que soporta parte de su peso.")
Q("n4", "nomotor", "A light trailer (<i>remolque ligero</i>) has an MMA…", "Un remolque ligero tiene una MMA…",
  [("of up to 750 kg", "de hasta 750 kg"), ("of up to 3,500 kg", "de hasta 3.500 kg"), ("above 750 kg", "superior a 750 kg")],
  "Light trailer: MMA not over 750 kg.", "Remolque ligero: MMA no superior a 750 kg.")
Q("n5", "nomotor", "A cycle (<i>ciclo</i>) is propelled…", "Un ciclo se propulsa…",
  [("only by the muscular effort of the people on it", "solo con el esfuerzo muscular de quienes lo ocupan"),
   ("by muscle power or by a motor of up to 250 W", "con esfuerzo muscular o con un motor de hasta 250 W"),
   ("by any motor that cuts off at 25 km/h", "con cualquier motor que se corte a 25 km/h")],
  "A plain cycle has no motor at all; with an auxiliary motor it becomes an EPAC or a ciclo de motor.",
  "Un ciclo no lleva motor; con motor auxiliar pasa a ser EPAC o ciclo de motor.")

# ---------------------------------------------------------------- light25
Q("l1", "light25", "A VMP is…", "Un VMP es…",
  [("single-place, electric, 6–25 km/h", "monoplaza, eléctrico, de 6 a 25 km/h"),
   ("two-place, petrol, up to 45 km/h", "biplaza, de gasolina, hasta 45 km/h"),
   ("any scooter up to 40 km/h", "cualquier patinete de hasta 40 km/h")],
  "One place, electric motors only, design speed between 6 and 25 km/h.",
  "Una plaza, solo motores eléctricos, velocidad de diseño entre 6 y 25 km/h.")
Q("l2", "light25", "An EPAC's electric assistance must cut off…", "La asistencia eléctrica de una EPAC debe cortarse…",
  [("before 25 km/h", "antes de 25 km/h"), ("at 45 km/h", "a 45 km/h"), ("at 40 km/h", "a 40 km/h")],
  "The assistance fades out and stops before 25 km/h, or when the rider stops pedalling.",
  "La ayuda disminuye y se corta antes de 25 km/h, o cuando se deja de pedalear.")
Q("l3", "light25", "The maximum continuous rated power of an EPAC motor is…", "La potencia nominal continua máxima del motor de una EPAC es…",
  [("250 W", "250 W"), ("500 W", "500 W"), ("1,000 W", "1.000 W")],
  "EPAC: 250 W at most. Up to 1,000 W it is a ciclo de motor.",
  "EPAC: 250 W como máximo. Hasta 1.000 W es un ciclo de motor.")
Q("l4", "light25", "A <i>ciclo de motor</i> (L1e-A) may have a continuous power of up to…", "Un ciclo de motor (L1e-A) puede tener una potencia continua de hasta…",
  [("1,000 W", "1.000 W"), ("250 W", "250 W"), ("4 kW", "4 kW")],
  "L1e-A: up to 1,000 W, with assistance cutting off at 25 km/h or less.",
  "L1e-A: hasta 1.000 W, con asistencia que se corta a 25 km/h o menos.")
Q("l5", "light25", "An electric scooter designed to reach 35 km/h is…", "Un patinete eléctrico diseñado para alcanzar 35 km/h es…",
  [("not a VMP", "un vehículo que no es VMP"), ("a VMP", "un VMP"), ("an EPAC", "una EPAC")],
  "The VMP design speed must stay between 6 and 25 km/h.",
  "La velocidad de diseño de un VMP debe estar entre 6 y 25 km/h.")
Q("l6", "light25", "Can a vehicle for people with reduced mobility be a VMP?", "¿Puede un vehículo para personas de movilidad reducida ser un VMP?",
  [("No, the VMP definition excludes it", "No, la definición de VMP lo excluye"),
   ("Yes, if it is electric", "Sí, si es eléctrico"),
   ("Yes, if it stays under 25 km/h", "Sí, si no pasa de 25 km/h")],
  "Vehicles for people with reduced mobility are expressly left out of the VMP category.",
  "Los vehículos para personas con movilidad reducida están expresamente fuera de la categoría de VMP.")

# ---------------------------------------------------------------- moped
Q("p1", "moped", "Which one is a two-wheel <b>moped</b>?", "¿Cuál es un <b>ciclomotor</b> de dos ruedas?",
  [("50 cm³ and 45 km/h", "50 cm³ y 45 km/h"), ("60 cm³ and 50 km/h", "60 cm³ y 50 km/h"), ("125 cm³ and 90 km/h", "125 cm³ y 90 km/h")],
  "Moped: up to 50 cm³ and up to 45 km/h by construction.", "Ciclomotor: hasta 50 cm³ y hasta 45 km/h por construcción.")
Q("p2", "moped", "The maximum mass in running order of a four-wheel moped is…", "La masa en orden de marcha máxima de un ciclomotor de cuatro ruedas es…",
  [("425 kg", "425 kg"), ("350 kg", "350 kg"), ("600 kg", "600 kg")],
  "425 kg, batteries of electric vehicles not counted. The old 350 kg tara is out of date.",
  "425 kg, sin contar las baterías de los eléctricos. Los antiguos 350 kg de tara están desfasados.")
Q("p3", "moped", "How many seats may a four-wheel moped have?", "¿Cuántas plazas puede tener un ciclomotor de cuatro ruedas?",
  [("At most two, driver included", "Dos como máximo, incluida la del conductor"),
   ("At most four, driver included", "Cuatro como máximo, incluida la del conductor"),
   ("Only one", "Solo una")],
  "Maximum two seats including the driver's.", "Máximo dos plazas incluida la del conductor.")
Q("p4", "moped", "A vehicle for people with reduced mobility has…", "Un vehículo para personas de movilidad reducida tiene…",
  [("tara up to 350 kg and a top speed of 45 km/h", "tara de hasta 350 kg y velocidad máxima de 45 km/h"),
   ("tara up to 425 kg and a top speed of 25 km/h", "tara de hasta 425 kg y velocidad máxima de 25 km/h"),
   ("tara up to 750 kg and a top speed of 45 km/h", "tara de hasta 750 kg y velocidad máxima de 45 km/h")],
  "Tara not over 350 kg, not over 45 km/h on level ground, and built specially for the purpose.",
  "Tara no superior a 350 kg, no más de 45 km/h en llano y construido especialmente para ese uso.")
Q("p5", "moped", "A two-wheeler with a 49 cm³ engine that reaches 60 km/h is a…", "Un vehículo de dos ruedas con motor de 49 cm³ que alcanza 60 km/h es…",
  [("motorcycle", "una motocicleta"), ("moped", "un ciclomotor"), ("<i>ciclo de motor</i>", "un ciclo de motor")],
  "Breaking either limit is enough: over 45 km/h makes it a motorcycle even under 50 cm³.",
  "Basta superar uno de los límites: más de 45 km/h lo convierte en motocicleta aunque tenga menos de 50 cm³.")

# ---------------------------------------------------------------- motos
Q("t1", "motos", "A motorcycle is a two-wheeled motor vehicle with…", "Una motocicleta es un automóvil de dos ruedas con…",
  [("more than 50 cm³ and/or more than 45 km/h", "más de 50 cm³ y/o más de 45 km/h"),
   ("more than 50 cm³ and also more than 45 km/h, both together", "más de 50 cm³ y además más de 45 km/h, las dos cosas"),
   ("more than 125 cm³", "más de 125 cm³")],
  "“And/or”: one of the two is enough.", "«Y/o»: basta una de las dos condiciones.")
Q("t2", "motos", "The maximum power of a heavy quadricycle is…", "La potencia máxima de un cuatriciclo pesado es…",
  [("15 kW", "15 kW"), ("6 kW", "6 kW"), ("4 kW", "4 kW")],
  "Heavy quadricycle: up to 15 kW. The 4 or 6 kW figures belong to the light one.",
  "Cuatriciclo pesado: hasta 15 kW. Los 4 o 6 kW son del ligero.")
Q("t3", "motos", "The limit on the mass in running order of a heavy quadricycle for carrying people is…", "El límite de masa en orden de marcha de un cuatriciclo pesado para personas es…",
  [("450 kg", "450 kg"), ("425 kg", "425 kg"), ("600 kg", "600 kg")],
  "450 kg for people, 600 kg for goods, batteries excluded (EU category L7e). Older manuals give 400 kg of empty mass.",
  "450 kg para personas y 600 kg para mercancías, sin contar baterías (categoría europea L7e). Los manuales antiguos dan 400 kg de masa en vacío.")
Q("t4", "motos", "A two-wheeled motorcycle fitted with a sidecar is…", "Una motocicleta de dos ruedas a la que se acopla un sidecar es…",
  [("still a motorcycle", "sigue siendo una motocicleta"), ("a three-wheeled vehicle", "un vehículo de tres ruedas"), ("a car", "un turismo")],
  "The motorcycle definition says “with or without sidecar”.", "La definición de motocicleta dice «con o sin sidecar».")

# ---------------------------------------------------------------- carbus
Q("c1", "carbus", "A vehicle for people has nine seats including the driver. It is a…", "Un vehículo para personas tiene nueve plazas incluida la del conductor. Es…",
  [("car (<i>turismo</i>)", "un turismo"), ("bus", "un autobús"), ("truck", "un camión")],
  "Turismo: up to nine seats, driver included.", "Turismo: hasta nueve plazas, incluida la del conductor.")
Q("c2", "carbus", "A vehicle for people has ten seats including the driver. It is a…", "Un vehículo para personas tiene diez plazas incluida la del conductor. Es…",
  [("bus", "un autobús"), ("car (<i>turismo</i>)", "un turismo"), ("adaptable mixed vehicle", "un vehículo mixto adaptable")],
  "More than nine seats with the driver makes it a bus.", "Más de nueve plazas con el conductor lo convierte en autobús.")
Q("c3", "carbus", "In an adaptable mixed vehicle (<i>mixto adaptable</i>)…", "En un vehículo mixto adaptable…",
  [("the load can be replaced by people by adding seats", "la carga puede sustituirse por personas añadiendo asientos"),
   ("only goods may be carried", "solo se pueden transportar mercancías"),
   ("there are always more than nine seats", "siempre hay más de nueve plazas")],
  "It carries people and goods, and seats can be added in place of load.",
  "Transporta personas y mercancías, y se pueden añadir asientos en lugar de carga.")
Q("c4", "carbus", "A <i>turismo</i> is intended for carrying…", "Un turismo está destinado al transporte de…",
  [("people", "personas"), ("goods", "mercancías"), ("people and goods at the same time", "personas y mercancías a la vez")],
  "A turismo is a motor vehicle for carrying people, with at most nine seats.",
  "El turismo es un automóvil destinado al transporte de personas, con un máximo de nueve plazas.")

# ---------------------------------------------------------------- goods
Q("g1", "goods", "A pick-up is treated as a car for traffic rules if…", "Un pick-up se trata como turismo a efectos de circulación si…",
  [("MMA ≤ 3,500 kg, height ≤ 2 m and cargo area separate from the seats", "MMA ≤ 3.500 kg, altura ≤ 2 m y zona de carga separada de los asientos"),
   ("it has a tow bar", "lleva bola de remolque"),
   ("its engine is under 2 litres", "su motor es de menos de 2 litros")],
  "Three conditions together: mass up to 3,500 kg, seats and cargo not in one compartment, total height up to 2 m.",
  "Tres condiciones a la vez: masa de hasta 3.500 kg, asientos y carga no en un único compartimento y altura total de hasta 2 m.")
Q("g2", "goods", "A <i>furgoneta</i> (van) is a goods vehicle with…", "Una furgoneta es un vehículo de mercancías con…",
  [("the cab integrated in the rest of the bodywork", "la cabina integrada en el resto de la carrocería"),
   ("the cab separate from the rest of the bodywork", "la cabina separada del resto de la carrocería"),
   ("more than nine seats", "más de nueve plazas")],
  "Integrated cab = furgoneta; cab not integrated = camión. Neither definition sets a mass.",
  "Cabina integrada = furgoneta; cabina no integrada = camión. Ninguna de las dos definiciones fija una masa.")
Q("g3", "goods", "What sets a <i>camión</i> (truck) apart from a <i>furgoneta</i> (van)?", "¿Qué distingue un camión de una furgoneta?",
  [("Its cab is not integrated in the rest of the bodywork", "Su cabina no está integrada en el resto de la carrocería"),
   ("Its MMA is over 3,500 kg", "Su MMA es superior a 3.500 kg"),
   ("It may carry more than nine people", "Puede llevar más de nueve personas")],
  "Both carry goods, with at most nine seats and any MMA; only the cab differs. 3,500 kg is the line for the B licence and category N1.",
  "Los dos llevan mercancías, con un máximo de nueve plazas y cualquier MMA; solo cambia la cabina. 3.500 kg es la frontera del permiso B y de la categoría N1.")
Q("g4", "goods", "An agricultural tractor is…", "Un tractor agrícola es…",
  [("a special vehicle", "un vehículo especial"), ("an <i>automóvil</i>", "un automóvil"), ("a vehicle that is not a motor vehicle", "un vehículo que no es de motor")],
  "Special vehicles are built for specific works or services. They are motor vehicles but not automóviles.",
  "Los vehículos especiales se construyen para obras o servicios determinados. Son vehículos de motor, pero no automóviles.")
Q("g5", "goods", "A pick-up that meets the three conditions follows the traffic rules of a…", "Un pick-up que cumple las tres condiciones sigue las normas de circulación de…",
  [("car (<i>turismo</i>)", "un turismo"), ("truck", "un camión"), ("bus", "un autobús")],
  "For traffic rules such as speed limits it is treated like a car, not a truck.",
  "A efectos de normas de circulación, como los límites de velocidad, se trata como un turismo y no como un camión.")

# ---------------------------------------------------------------- masses
Q("ma1", "masses", "Mass in running order =", "Masa en orden de marcha =",
  [("tara + 75 kg", "tara + 75 kg"), ("tara + passengers", "tara + pasajeros"), ("MMA − load", "MMA − carga")],
  "Tara plus the standard 75 kg driver.", "Tara más el conductor estándar de 75 kg.")
Q("ma2", "masses", "The maximum authorised mass (MMA) is…", "La masa máxima autorizada (MMA) es…",
  [("the most a loaded vehicle may weigh on public roads", "la masa máxima con la que puede circular cargado por las vías públicas"),
   ("what the vehicle weighs empty", "lo que pesa el vehículo vacío"),
   ("what the vehicle weighs at this moment", "lo que pesa el vehículo en este momento")],
  "MMA is a ceiling. The empty weight is the tara and the current weight is the laden mass.",
  "La MMA es un techo. El peso en vacío es la tara y el peso actual es la masa en carga.")
Q("ma3", "masses", "The <i>tara</i> of a vehicle…", "La tara de un vehículo…",
  [("includes neither driver, passengers nor load", "no incluye conductor, pasajeros ni carga"),
   ("includes the driver", "incluye al conductor"),
   ("includes the driver and the passengers", "incluye al conductor y a los pasajeros")],
  "Tara is the empty vehicle with its fixed equipment. The driver first appears in the mass in running order.",
  "La tara es el vehículo vacío con su equipo fijo. El conductor aparece en la masa en orden de marcha.")
Q("ma4", "masses", "May the laden mass exceed the MMA?", "¿Puede la masa en carga superar la MMA?",
  [("Never", "Nunca"), ("By up to 10 %", "Hasta un 10 %"), ("Only on motorways", "Solo en autopista")],
  "The MMA is the limit for the loaded vehicle.", "La MMA es el límite del vehículo cargado.")
Q("ma5", "masses", "A coach carries a crew member. Its mass in running order is tara +", "Un autocar lleva acompañante. Su masa en orden de marcha es la tara +",
  [("150 kg", "150 kg"), ("75 kg", "75 kg"), ("225 kg", "225 kg")],
  "75 kg for the driver plus 75 kg for the crew member.", "75 kg del conductor más 75 kg del acompañante.")

# ---------------------------------------------------------------- cats
Q("k1", "cats", "Category N2 covers goods vehicles with an MMA…", "La categoría N2 abarca vehículos de mercancías con una MMA…",
  [("above 3.5 t and up to 12 t", "superior a 3,5 t y de hasta 12 t"), ("above 12 t", "superior a 12 t"), ("of up to 3.5 t", "de hasta 3,5 t")],
  "N1 up to 3.5 t, N2 above 3.5 t up to 12 t, N3 above 12 t.", "N1 hasta 3,5 t, N2 más de 3,5 t y hasta 12 t, N3 más de 12 t.")
Q("k2", "cats", "A goods vehicle with an MMA of 3,000 kg is category…", "Un vehículo de mercancías con una MMA de 3.000 kg es de la categoría…",
  [("N1", "N1"), ("N2", "N2"), ("M1", "M1")],
  "N is goods; N1 goes up to 3.5 t.", "N es mercancías; N1 llega hasta 3,5 t.")
Q("k3", "cats", "Category O1 covers trailers with an MMA of up to…", "La categoría O1 abarca remolques con una MMA de hasta…",
  [("0.75 t", "0,75 t"), ("3.5 t", "3,5 t"), ("10 t", "10 t")],
  "O1 up to 0.75 t, O2 up to 3.5 t, O3 up to 10 t, O4 above 10 t.", "O1 hasta 0,75 t, O2 hasta 3,5 t, O3 hasta 10 t, O4 más de 10 t.")
Q("k4", "cats", "A passenger vehicle with 20 seats and an MMA of 4.5 t is category…", "Un vehículo de personas con 20 plazas y una MMA de 4,5 t es de la categoría…",
  [("M2", "M2"), ("M1", "M1"), ("M3", "M3")],
  "More than 8 seats besides the driver's and not over 5 t is M2.", "Más de 8 plazas además de la del conductor y no más de 5 t es M2.")
Q("k5", "cats", "EU class L6e is the…", "La clase europea L6e es…",
  [("light quadricycle", "el cuatriciclo ligero"), ("heavy quadricycle", "el cuatriciclo pesado"), ("two-wheel moped", "el ciclomotor de dos ruedas")],
  "L6e light quadricycle, L7e heavy quadricycle, L1e-B two-wheel moped.", "L6e cuatriciclo ligero, L7e cuatriciclo pesado, L1e-B ciclomotor de dos ruedas.")
Q("k6", "cats", "Category M1 allows, besides the driver's seat, up to…", "La categoría M1 admite, además de la plaza del conductor, hasta…",
  [("8 seats", "8 plazas"), ("9 seats", "9 plazas"), ("5 seats", "5 plazas")],
  "Eight besides the driver, which is the same border as the turismo's nine in total.",
  "Ocho además del conductor, la misma frontera que las nueve en total del turismo.")

# ---------------------------------------------------------------- eco
Q("e1", "eco", "A battery electric vehicle (BEV) gets the label…", "Un vehículo eléctrico de batería (BEV) recibe el distintivo…",
  [("0 emisiones", "0 emisiones"), ("ECO", "ECO"), ("C", "C")],
  "BEV, REEV, fuel-cell vehicles and PHEV with at least 40 km get 0 emisiones.",
  "BEV, REEV, pila de combustible y PHEV con al menos 40 km reciben 0 emisiones.")
Q("e2", "eco", "A plug-in hybrid with 50 km of electric range gets the label…", "Un híbrido enchufable con 50 km de autonomía eléctrica recibe el distintivo…",
  [("0 emisiones", "0 emisiones"), ("ECO", "ECO"), ("B", "B")],
  "The line is 40 km: at or above it 0 emisiones, below it ECO.", "La frontera son 40 km: con 40 o más 0 emisiones, con menos ECO.")
Q("e3", "eco", "A hybrid that cannot be plugged in (HEV) gets the label…", "Un híbrido no enchufable (HEV) recibe el distintivo…",
  [("ECO", "ECO"), ("0 emisiones", "0 emisiones"), ("none", "ninguno")],
  "Non-plug-in hybrids are ECO.", "Los híbridos no enchufables son ECO.")
Q("e4", "eco", "Vehicle sign V-26 identifies…", "La señal V-26 en un vehículo identifica…",
  [("a shared-use vehicle", "un vehículo de uso compartido"), ("the environmental label", "el distintivo ambiental"), ("a novice driver", "a un conductor novel")],
  "V-26 is the shared-use sticker; V-25 is the environmental label.", "La V-26 es el distintivo de uso compartido; la V-25 es el distintivo ambiental.")
Q("e5", "eco", "Vehicle sign V-25 is…", "La señal V-25 en un vehículo es…",
  [("the environmental label", "el distintivo ambiental"), ("the shared-use sticker", "el distintivo de uso compartido"), ("the registration plate", "la placa de matrícula")],
  "V-25 = environmental label.", "V-25 = distintivo ambiental.")
Q("e6", "eco", "In a range-extended electric vehicle (REEV), the combustion engine…", "En un eléctrico de autonomía extendida (REEV), el motor de combustión…",
  [("only generates electricity", "solo genera electricidad"), ("drives the wheels on the motorway", "mueve las ruedas en autopista"), ("does not exist", "no existe")],
  "The wheels are always driven by the electric motor.", "Las ruedas las mueve siempre el motor eléctrico.")
