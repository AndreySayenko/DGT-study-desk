# -*- coding: utf-8 -*-
"""Question bank for the interactive Category A1/A2, Topic 1 page (definitions and general concepts). In every
question the FIRST option is the correct one (the page shuffles options when it shows them). Ids must be unique and
must not start with "ai"."""

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
    "people": dict(sec=1, en="Pedestrians and drivers", es="Peatones y conductores",
        recap=[("Pedestrian: travels on foot without being a driver.", "Peatón: transita a pie sin ser conductor."),
               ("Also pedestrians: pushing a pram or small motorless vehicle, walking a cycle or two-wheeled moped, in a wheelchair at walking pace.", "También peatones: quien empuja un coche de niño o vehículo pequeño sin motor, quien lleva a pie un ciclo o ciclomotor de dos ruedas, quien va en silla de ruedas al paso."),
               ("Driver: handles the steering or is in command of a vehicle, or is in charge of animals.", "Conductor: maneja la dirección o va al mando de un vehículo, o está a cargo de animales."),
               ("In a learner vehicle, the driver is whoever controls the additional controls: the instructor.", "En un vehículo de aprendizaje, el conductor es quien está a cargo de los mandos adicionales: el profesor.")],
        trap=("Calling someone who pushes a moped on foot a ‘driver’.", "Llamar «conductor» a quien lleva a pie un ciclomotor.")),
    "owner": dict(sec=1, en="Owner, policyholder, habitual driver", es="Titular, tomador, conductor habitual",
        recap=[("Owner (titular): the vehicle is registered in their name.", "Titular: el vehículo está inscrito a su nombre."),
               ("Policyholder (tomador): takes out the third-party insurance.", "Tomador: contrata el seguro de responsabilidad civil."),
               ("Habitual driver: a licence holder declared by the owner or long-term lessee, with their consent.", "Conductor habitual: persona con permiso declarada por el titular o el arrendatario a largo plazo, con su consentimiento."),
               ("They can be three different people.", "Pueden ser tres personas distintas.")],
        trap=("Thinking the policyholder must be the owner.", "Pensar que el tomador tiene que ser el titular.")),
    "vehdef": dict(sec=1, en="Vehicle, motor vehicle, automóvil, special vehicle", es="Vehículo, de motor, automóvil, especial",
        recap=[("Vehicle: a machine fit to travel on roads or land in common use.", "Vehículo: aparato apto para circular por vías o terrenos de uso común."),
               ("Motor vehicle: has a motor for propulsion — except mopeds, trams, reduced-mobility vehicles, pedal-assist bicycles and VMP.", "Vehículo a motor: tiene motor para su propulsión, salvo ciclomotores, tranvías, vehículos de movilidad reducida, bicicletas de pedaleo asistido y VMP."),
               ("Automóvil: a motor vehicle to carry people or goods or to tow; special vehicles excluded.", "Automóvil: vehículo de motor para transportar personas o cosas o remolcar; se excluyen los especiales."),
               ("Special vehicle: for works or services, and farm machinery; exempt from some rules or over the limits.", "Vehículo especial: para obras o servicios y maquinaria agrícola; exento de algunas normas o por encima de los límites.")],
        trap=("Thinking a moped is a motor vehicle in law because it has a motor.", "Pensar que el ciclomotor es vehículo de motor porque tiene motor.")),
    "users": dict(sec=2, en="Classifying users and vehicles", es="Clasificación de usuarios y vehículos",
        recap=[("Users: pedestrians, animals, vehicles.", "Usuarios: peatones, animales y vehículos."),
               ("Vehicles: without a motor, not considered motor vehicles, motor vehicles.", "Vehículos: sin motor, no considerados de motor y de motor."),
               ("Motor vehicles: automóviles and special vehicles.", "De motor: automóviles y vehículos especiales."),
               ("Motorcycles, trikes and quadricycles are automóviles; tractors and tourist trains are special vehicles.", "Motos, triciclos y cuatriciclos son automóviles; tractores y trenes turísticos son vehículos especiales.")],
        trap=("Putting mopeds in the motor-vehicle branch.", "Poner los ciclomotores en la rama de vehículos de motor.")),
    "nomotor": dict(sec=2, en="Vehicles without a motor", es="Vehículos sin motor",
        recap=[("Cycle: at least two wheels, moved by muscle power with pedals or cranks.", "Ciclo: dos ruedas como mínimo, movido por esfuerzo muscular con pedales o manivelas."),
               ("Bicycle: a two-wheeled cycle.", "Bicicleta: ciclo de dos ruedas."),
               ("Animal-drawn vehicle: pulled by animals.", "Vehículo de tracción animal: arrastrado por animales."),
               ("Trailer: not self-propelled, towed by a motor vehicle; light trailer up to 750 kg MMA.", "Remolque: no autopropulsado, remolcado por un vehículo de motor; ligero hasta 750 kg de MMA.")],
        trap=("Thinking a tricycle pedalled by hand isn’t a cycle.", "Pensar que un triciclo a manivela no es un ciclo.")),
    "notmotor": dict(sec=2, en="Mopeds, VMP, reduced-mobility vehicles, trams", es="Ciclomotores, VMP, movilidad reducida, tranvía",
        recap=[("Moped (2 or 3 wheels): ≤ 50 cm³ (combustion) and ≤ 45 km/h.", "Ciclomotor (2 o 3 ruedas): ≤ 50 cm³ (combustión) y ≤ 45 km/h."),
               ("Light quadricycle: ≤ 45 km/h; course: 50 cm³ or 4 kW, tare < 350 kg; since July 2025: ≤ 425 kg in running order.", "Cuatriciclo ligero: ≤ 45 km/h; curso: 50 cm³ o 4 kW, tara < 350 kg; desde julio de 2025: ≤ 425 kg en orden de marcha."),
               ("VMP: one or more wheels, one place, electric only, 6–25 km/h; a seat only if self-balancing.", "VMP: una o más ruedas, una plaza, solo eléctrico, 6–25 km/h; asiento solo si es autoequilibrado."),
               ("Reduced-mobility vehicle: built for it, tare ≤ 350 kg, ≤ 45 km/h, treated like a three-wheeled moped. Tram: runs on rails.", "Movilidad reducida: construido para ello, tara ≤ 350 kg, ≤ 45 km/h, se equipara al ciclomotor de tres ruedas. Tranvía: por raíles.")],
        trap=("Thinking a VMP can reach 45 km/h.", "Pensar que un VMP puede llegar a 45 km/h.")),
    "motos": dict(sec=2, en="Motorcycles, trikes and quadricycles", es="Motocicletas, triciclos y cuatriciclos",
        recap=[("Motorcycle: two wheels, no sidecar, > 50 cm³ and/or > 45 km/h.", "Motocicleta: dos ruedas, sin sidecar, > 50 cm³ y/o > 45 km/h."),
               ("With sidecar: three wheels asymmetric about the long axis — still a motorcycle.", "Con sidecar: tres ruedas asimétricas respecto al eje — sigue siendo motocicleta."),
               ("Three-wheeled vehicle: three symmetric wheels, > 50 cm³ and/or > 45 km/h.", "Vehículo de tres ruedas: tres ruedas simétricas, > 50 cm³ y/o > 45 km/h."),
               ("Motor quadricycle: 15 kW; course 400 kg (550 goods); EU L7e 450 kg (600 goods).", "Cuatriciclo de motor: 15 kW; curso 400 kg (550 mercancías); UE L7e 450 kg (600 mercancías).")],
        trap=("Calling a motorcycle with sidecar a ‘three-wheeled vehicle’.", "Llamar «vehículo de tres ruedas» a una moto con sidecar.")),
    "masses": dict(sec=3, en="Masses", es="Masas",
        recap=[("Tare: vehicle with fixed equipment, fluids, tools and accessories — no people, no load.", "Tara: vehículo con equipo fijo, líquidos, herramientas y accesorios, sin personas ni carga."),
               ("Laden mass: actual mass with load and passengers.", "Masa en carga: masa efectiva con carga y pasajeros."),
               ("MMA: the maximum mass allowed on public roads with load.", "MMA: la masa máxima permitida con carga en las vías públicas."),
               ("Mass in running order: tare plus a 75 kg driver.", "Masa en orden de marcha: tara más 75 kg del conductor.")],
        trap=("Including the passengers in the tare.", "Incluir a los pasajeros en la tara.")),
}

# ---------------------------------------------------------------- people
Q("pe1", "people", "A person who travels on foot without being a driver is a…", "La persona que transita a pie sin ser conductor es un…",
  [("pedestrian", "peatón"), ("road user without rights", "usuario sin derechos"), ("passenger", "pasajero")],
  "On public roads or private land in common use.", "Por vías o terrenos públicos o privados de uso común.")
Q("pe2", "people", "You push your broken-down moped along the road on foot. You are…", "Llevas a pie tu ciclomotor averiado por la vía. Eres…",
  [("a pedestrian", "peatón"), ("a driver", "conductor"), ("a passenger", "pasajero")],
  "Walking a cycle or a two-wheeled moped counts as a pedestrian.", "Conducir a pie un ciclo o ciclomotor de dos ruedas es ser peatón.")
Q("pe3", "people", "A person with a disability in a motorised wheelchair at walking pace is…", "Una persona con discapacidad en silla de ruedas con motor, al paso, es…",
  [("a pedestrian", "peatón"), ("a moped rider", "conductor de ciclomotor"), ("a VMP rider", "conductor de VMP")],
  "With or without a motor.", "Con o sin motor.")
Q("pe4", "people", "Someone leading a herd of cows along a road is legally…", "Quien guía un rebaño de vacas por la vía es, legalmente…",
  [("a driver", "conductor"), ("a pedestrian", "peatón"), ("nothing in particular", "nada en particular")],
  "A driver can be in charge of animals.", "El conductor puede estar a cargo de animales.")
Q("pe5", "people", "During a motorcycle lesson with an instructor in a dual-control vehicle, the driver is…", "En una clase en un vehículo con doble mando, el conductor es…",
  [("the instructor, who is in charge of the additional controls", "el profesor, a cargo de los mandos adicionales"), ("always the learner", "siempre el alumno"), ("nobody", "nadie")],
  "In learner vehicles.", "En los vehículos de aprendizaje.")
Q("pe6", "people", "Someone pushing a handcart (a small vehicle without a motor) is…", "Quien empuja un carro de mano (vehículo pequeño sin motor) es…",
  [("a pedestrian", "peatón"), ("a driver", "conductor"), ("a cyclist", "ciclista")],
  "Like pushing a pram.", "Como empujar un coche de niño.")
Q("pe7", "people", "You are riding your motorcycle. You are…", "Vas montado en tu motocicleta. Eres…",
  [("a driver", "conductor"), ("a pedestrian", "peatón"), ("a passenger", "pasajero")],
  "You handle the steering.", "Manejas la dirección.")
Q("pe8", "people", "Which of these is a pedestrian?", "¿Cuál de estos es peatón?",
  [("A person walking a bicycle", "Una persona que lleva a pie una bicicleta"), ("A person riding a moped", "Una persona montada en un ciclomotor"), ("A person on a horse", "Una persona a caballo")],
  "Riding = driver; walking it = pedestrian.", "Montado = conductor; a pie = peatón.")

# ---------------------------------------------------------------- owner
Q("ow1", "owner", "The ‘titular’ of a vehicle is…", "El titular de un vehículo es…",
  [("the person in whose name it is registered", "la persona a cuyo nombre figura inscrito"), ("whoever drives it most", "quien más lo conduce"), ("whoever pays the insurance", "quien paga el seguro")],
  "In the official register.", "En el registro oficial.")
Q("ow2", "owner", "The ‘tomador’ is…", "El tomador es…",
  [("the person who takes out the vehicle’s third-party insurance", "quien contrata el seguro de responsabilidad civil del vehículo"), ("the registered owner", "el titular"), ("the habitual driver", "el conductor habitual")],
  "They need not be the owner.", "No tiene por qué ser el titular.")
Q("ow3", "owner", "The habitual driver is declared to the vehicle register by…", "Al conductor habitual lo declara al Registro de Vehículos…",
  [("the owner (or the long-term lessee), with the driver’s consent", "el titular (o el arrendatario a largo plazo), con su consentimiento"), ("the insurer", "la aseguradora"), ("the police", "la policía")],
  "The one who drives it most often.", "Quien lo conduce con más frecuencia.")
Q("ow4", "owner", "To be declared habitual driver, a person must…", "Para ser declarado conductor habitual hay que…",
  [("hold a driving licence and consent", "tener permiso de conducir y dar su consentimiento"), ("be the owner", "ser el titular"), ("be over 25", "tener más de 25 años")],
  "And drive the vehicle most often.", "Y ser quien más lo conduce.")
Q("ow5", "owner", "Can the owner, the policyholder and the habitual driver be three different people?", "¿Pueden ser el titular, el tomador y el conductor habitual tres personas distintas?",
  [("Yes", "Sí"), ("No, they must be the same person", "No, deben ser la misma"), ("Only for company cars", "Solo en vehículos de empresa")],
  "Each term describes a different role.", "Cada término describe un papel distinto.")

# ---------------------------------------------------------------- vehicle definitions
Q("vd1", "vehdef", "A ‘vehicle’ is…", "Un vehículo es…",
  [("a machine fit to travel on roads or land in common use", "un aparato apto para circular por vías o terrenos de uso común"), ("only machines with a motor", "solo los aparatos con motor"), ("only cars", "solo los turismos")],
  "With or without a motor.", "Con o sin motor.")
Q("vd2", "vehdef", "Which of these is NOT a motor vehicle in law?", "¿Cuál NO es vehículo a motor según la ley?",
  [("A moped", "Un ciclomotor"), ("A motorcycle", "Una motocicleta"), ("A three-wheeled vehicle", "Un vehículo de tres ruedas")],
  "Also excluded: trams, reduced-mobility vehicles, pedal-assist bicycles and VMP.", "También se excluyen tranvías, vehículos de movilidad reducida, bicicletas de pedaleo asistido y VMP.")
Q("vd3", "vehdef", "Is a tram a motor vehicle?", "¿Es el tranvía un vehículo a motor?",
  [("No, the law excludes it", "No, la ley lo excluye"), ("Yes, it has an electric motor", "Sí, tiene motor eléctrico"), ("Only outside towns", "Solo fuera de poblado")],
  "It runs on rails.", "Circula por raíles.")
Q("vd4", "vehdef", "An ‘automóvil’ is…", "Un automóvil es…",
  [("a motor vehicle to carry people or goods, or to tow", "un vehículo de motor para transportar personas o cosas, o remolcar"), ("any vehicle", "cualquier vehículo"), ("only cars with four wheels", "solo los de cuatro ruedas")],
  "Special vehicles are excluded.", "Se excluyen los vehículos especiales.")
Q("vd5", "vehdef", "Is a motorcycle an automóvil?", "¿Es la motocicleta un automóvil?",
  [("Yes", "Sí"), ("No, only four-wheeled vehicles are", "No, solo los de cuatro ruedas"), ("Only with a sidecar", "Solo con sidecar")],
  "It is a motor vehicle for carrying people or goods.", "Es un vehículo de motor para transportar personas o cosas.")
Q("vd6", "vehdef", "A farm tractor is a…", "Un tractor agrícola es un…",
  [("special vehicle", "vehículo especial"), ("automóvil", "automóvil"), ("vehicle not considered a motor vehicle", "vehículo no considerado de motor")],
  "Farm machinery is a special vehicle.", "La maquinaria agrícola es vehículo especial.")
Q("vd7", "vehdef", "A special vehicle…", "Un vehículo especial…",
  [("is built for works or services and may be exempt from some technical requirements", "está concebido para obras o servicios y puede estar exento de algunas condiciones técnicas"), ("is always an automóvil", "es siempre un automóvil"), ("has no motor", "no tiene motor")],
  "Or it permanently exceeds the mass or size limits.", "O sobrepasa permanentemente los límites de masas o dimensiones.")
Q("vd8", "vehdef", "Are special vehicles automóviles?", "¿Son los vehículos especiales automóviles?",
  [("No, they are excluded from the automóvil definition", "No, se excluyen de la definición de automóvil"), ("Yes, always", "Sí, siempre"), ("Only if they carry people", "Solo si llevan personas")],
  "They are motor vehicles, but a separate branch.", "Son de motor, pero una rama aparte.")
Q("vd9", "vehdef", "A personal mobility vehicle (VMP) is…", "Un vehículo de movilidad personal (VMP) es…",
  [("not a motor vehicle", "no es vehículo a motor"), ("a motor vehicle", "un vehículo a motor"), ("a moped", "un ciclomotor")],
  "The law excludes it.", "La ley lo excluye.")

# ---------------------------------------------------------------- users and families
Q("us1", "users", "Road users are classified as…", "Los usuarios de la vía se clasifican en…",
  [("pedestrians, animals and vehicles", "peatones, animales y vehículos"), ("drivers and passengers", "conductores y pasajeros"), ("cars and motorcycles", "turismos y motos")],
  "Vehicles split further.", "Los vehículos se subdividen.")
Q("us2", "users", "Mopeds belong to the family of vehicles…", "Los ciclomotores pertenecen a la familia de vehículos…",
  [("not considered motor vehicles", "no considerados de motor"), ("without a motor", "sin motor"), ("special", "especiales")],
  "With VMP, light quadricycles, reduced-mobility vehicles and trams.", "Con los VMP, cuatriciclos ligeros, vehículos de movilidad reducida y tranvías.")
Q("us3", "users", "Motor vehicles are divided into…", "Los vehículos de motor se dividen en…",
  [("automóviles and special vehicles", "automóviles y vehículos especiales"), ("cars and lorries", "turismos y camiones"), ("mopeds and motorcycles", "ciclomotores y motocicletas")],
  "Special vehicles are not automóviles.", "Los especiales no son automóviles.")
Q("us4", "users", "A caravan belongs to the family of vehicles…", "Una caravana pertenece a la familia de vehículos…",
  [("without a motor", "sin motor"), ("not considered motor vehicles", "no considerados de motor"), ("automóviles", "automóviles")],
  "Like trailers and semi-trailers.", "Como los remolques y semirremolques.")
Q("us5", "users", "A motorhome (autocaravana) is…", "Una autocaravana es…",
  [("an automóvil", "un automóvil"), ("a vehicle without a motor", "un vehículo sin motor"), ("a special vehicle", "un vehículo especial")],
  "A caravan, which is towed, has no motor.", "La caravana, que se remolca, no tiene motor.")
Q("us6", "users", "A tourist train is…", "Un tren turístico es…",
  [("a special vehicle", "un vehículo especial"), ("a tram", "un tranvía"), ("an automóvil", "un automóvil")],
  "Like farm and works tractors.", "Como los tractores agrícolas y de obras.")

# ---------------------------------------------------------------- without a motor
Q("nm1", "nomotor", "A cycle is a vehicle…", "Un ciclo es un vehículo…",
  [("with at least two wheels, moved by muscle power through pedals or cranks", "de dos ruedas como mínimo, accionado por esfuerzo muscular mediante pedales o manivelas"), ("with an engine up to 50 cm³", "con motor de hasta 50 cm³"), ("pulled by animals", "arrastrado por animales")],
  "A bicycle is a two-wheeled cycle.", "La bicicleta es un ciclo de dos ruedas.")
Q("nm2", "nomotor", "A bicycle is…", "Una bicicleta es…",
  [("a two-wheeled cycle", "un ciclo de dos ruedas"), ("any cycle", "cualquier ciclo"), ("a moped", "un ciclomotor")],
  "Cycles can have more wheels.", "Los ciclos pueden tener más ruedas.")
Q("nm3", "nomotor", "A light trailer has a maximum authorised mass of up to…", "Un remolque ligero tiene una MMA de hasta…",
  [("750 kg", "750 kg"), ("350 kg", "350 kg"), ("3,500 kg", "3.500 kg")],
  "A trailer is towed by a motor vehicle.", "El remolque lo arrastra un vehículo de motor.")
Q("nm4", "nomotor", "A trailer is…", "Un remolque es…",
  [("a vehicle without its own propulsion, designed to be towed by a motor vehicle", "un vehículo no autopropulsado, concebido para ser remolcado por un vehículo de motor"), ("a motor vehicle", "un vehículo de motor"), ("a special vehicle", "un vehículo especial")],
  "Light trailer: MMA up to 750 kg.", "Ligero: MMA hasta 750 kg.")
Q("nm5", "nomotor", "A horse-drawn carriage is a…", "Un coche de caballos es un…",
  [("animal-drawn vehicle", "vehículo de tracción animal"), ("special vehicle", "vehículo especial"), ("cycle", "ciclo")],
  "Pulled by animals; its driver is a ‘conductor’.", "Arrastrado por animales; quien lo lleva es conductor.")

# ---------------------------------------------------------------- not considered motor vehicles
Q("mp1", "notmotor", "A two-wheeled moped has an engine of no more than…", "Un ciclomotor de dos ruedas tiene un motor de cilindrada no superior a…",
  [("50 cm³", "50 cm³"), ("125 cm³", "125 cm³"), ("250 cm³", "250 cm³")],
  "If it is an internal-combustion engine.", "Si es de combustión interna.")
Q("mp2", "notmotor", "A moped’s maximum speed by construction is no more than…", "La velocidad máxima por construcción de un ciclomotor no supera…",
  [("45 km/h", "45 km/h"), ("25 km/h", "25 km/h"), ("70 km/h", "70 km/h")],
  "Over 45 km/h it is a motorcycle.", "Por encima de 45 km/h es motocicleta.")
Q("mp3", "notmotor", "A two-wheeled vehicle with a 49 cm³ engine that can reach 60 km/h is…", "Un vehículo de dos ruedas de 49 cm³ que alcanza 60 km/h es…",
  [("a motorcycle", "una motocicleta"), ("a moped", "un ciclomotor"), ("a VMP", "un VMP")],
  "Over 45 km/h is enough: the rule is ‘and/or’.", "Basta con superar 45 km/h: la regla es «y/o».")
Q("mp4", "notmotor", "Can a moped have three wheels?", "¿Puede un ciclomotor tener tres ruedas?",
  [("Yes, two- and three-wheeled mopeds exist", "Sí, hay ciclomotores de dos y tres ruedas"), ("No, only two", "No, solo dos"), ("Only electric ones", "Solo los eléctricos")],
  "A four-wheeled one is a light quadricycle.", "El de cuatro ruedas es el cuatriciclo ligero.")
Q("mp5", "notmotor", "A light quadricycle is also called a…", "El cuatriciclo ligero también se llama…",
  [("four-wheeled moped", "ciclomotor de cuatro ruedas"), ("motor quadricycle", "cuatriciclo de motor"), ("quad-ATV", "quad-ATV")],
  "Up to 45 km/h.", "Hasta 45 km/h.")
Q("mp6", "notmotor", "A personal mobility vehicle (VMP) has a design speed of…", "Un vehículo de movilidad personal (VMP) tiene una velocidad máxima por diseño de…",
  [("between 6 and 25 km/h", "entre 6 y 25 km/h"), ("up to 45 km/h", "hasta 45 km/h"), ("between 25 and 45 km/h", "entre 25 y 45 km/h")],
  "Electric only, one place.", "Solo eléctrico, una plaza.")
Q("mp7", "notmotor", "A VMP may have a seat or saddle…", "Un VMP puede llevar asiento o sillín…",
  [("only if it has a self-balancing system", "solo si tiene sistema de autoequilibrado"), ("always", "siempre"), ("never", "nunca")],
  "Like some electric unicycles.", "Como algunos monociclos eléctricos.")
Q("mp8", "notmotor", "A VMP is driven by…", "Un VMP se propulsa…",
  [("electric motors only", "exclusivamente con motores eléctricos"), ("a petrol engine up to 50 cm³", "con motor de gasolina de hasta 50 cm³"), ("pedals", "con pedales")],
  "One or more wheels, one place.", "Una o más ruedas, una plaza.")
Q("mp9", "notmotor", "A vehicle for people with reduced mobility has a tare of no more than…", "Un vehículo para personas de movilidad reducida tiene una tara no superior a…",
  [("350 kg", "350 kg"), ("750 kg", "750 kg"), ("100 kg", "100 kg")],
  "And it cannot exceed 45 km/h on the flat.", "Y no supera 45 km/h en llano.")
Q("mp10", "notmotor", "A car merely adapted for a driver with a disability is…", "Un turismo simplemente adaptado para un conductor con discapacidad es…",
  [("still a car, not a reduced-mobility vehicle", "sigue siendo un turismo, no un vehículo de movilidad reducida"), ("a reduced-mobility vehicle", "un vehículo de movilidad reducida"), ("a special vehicle", "un vehículo especial")],
  "Reduced-mobility vehicles are built specially, not adapted.", "Los de movilidad reducida se construyen a propósito, no se adaptan.")
Q("mp11", "notmotor", "In their other technical features, reduced-mobility vehicles are treated like…", "En el resto de características técnicas, los vehículos de movilidad reducida se equiparan a…",
  [("three-wheeled mopeds", "los ciclomotores de tres ruedas"), ("motorcycles", "las motocicletas"), ("cars", "los turismos")],
  "Tare ≤ 350 kg, ≤ 45 km/h.", "Tara ≤ 350 kg, ≤ 45 km/h.")
Q("mp12", "notmotor", "A tram is a vehicle that…", "Un tranvía es un vehículo que…",
  [("runs on rails laid in the road", "marcha por raíles instalados en la vía"), ("runs on an overhead cable only", "circula solo por cable aéreo"), ("is a bus", "es un autobús")],
  "Not a motor vehicle in law.", "No es vehículo a motor para la ley.")
Q("mp13", "notmotor", "According to your course, a light quadricycle with a non-petrol engine has a maximum power of…", "Según tu curso, un cuatriciclo ligero con motor que no es de gasolina tiene una potencia máxima de…",
  [("4 kW", "4 kW"), ("15 kW", "15 kW"), ("35 kW", "35 kW")],
  "15 kW is the motor quadricycle.", "15 kW es el cuatriciclo de motor.")

# ---------------------------------------------------------------- motorcycles and relatives
Q("mo1", "motos", "A two-wheeled motorcycle has an engine…", "Una motocicleta de dos ruedas tiene un motor…",
  [("over 50 cm³ and/or a design speed over 45 km/h", "de más de 50 cm³ y/o velocidad por construcción superior a 45 km/h"), ("of up to 50 cm³ and 45 km/h", "de hasta 50 cm³ y 45 km/h"), ("of at least 125 cm³", "de al menos 125 cm³")],
  "If it is an internal-combustion engine.", "Si es de combustión interna.")
Q("mo2", "motos", "A motorcycle with sidecar has…", "Una motocicleta con sidecar tiene…",
  [("three wheels asymmetric about its long axis", "tres ruedas asimétricas respecto a su eje medio longitudinal"), ("three symmetric wheels", "tres ruedas simétricas"), ("four wheels", "cuatro ruedas")],
  "It is still a motorcycle.", "Sigue siendo una motocicleta.")
Q("mo3", "motos", "A three-wheeled vehicle has…", "Un vehículo de tres ruedas tiene…",
  [("three wheels symmetric about the long axis", "tres ruedas simétricas"), ("three asymmetric wheels", "tres ruedas asimétricas"), ("a sidecar", "sidecar")],
  "With a sidecar they are asymmetric.", "Con sidecar son asimétricas.")
Q("mo4", "motos", "A motor quadricycle has a maximum net power of…", "Un cuatriciclo de motor tiene una potencia máxima neta de…",
  [("15 kW", "15 kW"), ("4 kW", "4 kW"), ("35 kW", "35 kW")],
  "A light quadricycle: 45 km/h.", "El ligero: 45 km/h.")
Q("mo5", "motos", "According to your course, the empty mass of a motor quadricycle for passengers is no more than…", "Según tu curso, la masa en vacío de un cuatriciclo de motor de pasajeros no supera…",
  [("400 kg", "400 kg"), ("750 kg", "750 kg"), ("1,000 kg", "1.000 kg")],
  "550 kg for goods. Today’s EU category L7e: 450 kg (600 kg goods).", "550 kg mercancías. Hoy la categoría UE L7e: 450 kg (600 kg mercancías).")
Q("mo6", "motos", "A 125 cm³ scooter is a…", "Un scooter de 125 cm³ es una…",
  [("motorcycle", "motocicleta"), ("moped", "ciclomotor"), ("VMP", "VMP")],
  "Over 50 cm³.", "Más de 50 cm³.")
Q("mo7", "motos", "An electric two-wheeler with a design speed of 80 km/h is a…", "Un vehículo eléctrico de dos ruedas con velocidad de diseño de 80 km/h es una…",
  [("motorcycle", "motocicleta"), ("moped", "ciclomotor"), ("VMP", "VMP")],
  "The speed alone is enough: over 45 km/h.", "Basta con la velocidad: más de 45 km/h.")
Q("mo8", "motos", "Motorcycles, sidecar motorcycles, trikes and motor quadricycles are all…", "Motocicletas, motos con sidecar, vehículos de tres ruedas y cuatriciclos de motor son todos…",
  [("automóviles", "automóviles"), ("special vehicles", "vehículos especiales"), ("vehicles not considered motor vehicles", "vehículos no considerados de motor")],
  "Motor vehicles for carrying people or goods.", "Vehículos de motor para transportar personas o cosas.")
Q("mo9", "motos", "A quad approved as a special vehicle (quad-ATV) belongs to the branch of…", "Un quad homologado como vehículo especial (quad-ATV) pertenece a la rama de…",
  [("special vehicles", "vehículos especiales"), ("mopeds", "ciclomotores"), ("vehicles without a motor", "vehículos sin motor")],
  "A road quadricycle is an automóvil.", "Un cuatriciclo de carretera es un automóvil.")

# ---------------------------------------------------------------- masses
Q("ms1", "masses", "The tare (empty mass) of a vehicle includes…", "La tara de un vehículo incluye…",
  [("its fixed equipment, fluids, tools and accessories — no people or load", "su equipo fijo, líquidos, herramientas y accesorios, sin personas ni carga"), ("the driver", "el conductor"), ("the passengers and luggage", "los pasajeros y el equipaje")],
  "Water, fuel, lubricant, tools and accessories.", "Agua, combustible, lubricante, herramientas y accesorios.")
Q("ms2", "masses", "The laden mass (masa en carga) is…", "La masa en carga es…",
  [("the actual mass of the vehicle and its load, passengers included", "la masa efectiva del vehículo y su carga, incluidos los pasajeros"), ("the most it may weigh", "lo máximo que puede pesar"), ("the empty mass", "la masa en vacío")],
  "What it weighs at that moment.", "Lo que pesa en ese momento.")
Q("ms3", "masses", "The maximum authorised mass (MMA) is…", "La masa máxima autorizada (MMA) es…",
  [("the most a loaded vehicle may weigh to be driven on public roads", "lo máximo que puede pesar un vehículo con carga para circular por las vías públicas"), ("the empty mass", "la tara"), ("the mass with the driver only", "la masa con el conductor")],
  "The laden mass must never exceed it.", "La masa en carga nunca puede superarla.")
Q("ms4", "masses", "Your motorcycle with you and a passenger on it weighs 340 kg. That figure is the…", "Tu moto contigo y un pasajero pesa 340 kg. Esa cifra es la…",
  [("laden mass", "masa en carga"), ("tare", "tara"), ("MMA", "MMA")],
  "With people and load.", "Con personas y carga.")
Q("ms5", "masses", "Mass in running order is…", "La masa en orden de marcha es…",
  [("the tare plus a standard 75 kg driver", "la tara más un conductor estándar de 75 kg"), ("the MMA", "la MMA"), ("the tare without fuel", "la tara sin combustible")],
  "The general rule in the Reglamento General de Vehículos.", "Es la regla general del Reglamento General de Vehículos.")
