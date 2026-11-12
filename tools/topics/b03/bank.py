# -*- coding: utf-8 -*-
"""Question bank for the interactive Topic 3 page (speed). In every question the FIRST option is the
correct one (the page shuffles options when it shows them). Ids must be unique and must not start with "ai"."""

BANK = []


def Q(qid, tag, en, es, opts, why_en, why_es):
    BANK.append({
        "id": qid, "tag": tag,
        "q": {"en": en, "es": es},
        "o": [{"en": a, "es": b} for a, b in opts],
        "why": {"en": why_en, "es": why_es},
    })


def K(*nums):
    """Options that are plain speeds, the same in both languages."""
    return [(f"{n} km/h", f"{n} km/h") for n in nums]


# tag -> section number, names, recap bullets, typical confusion
TAGS = {
    "concepts": dict(sec=1, en="Speed concepts", es="Conceptos de velocidad",
        recap=[("Maximum = upper limit for that vehicle on that road; going above it is exceso de velocidad.",
                "Máxima = límite superior para ese vehículo en esa vía; superarla es exceso de velocidad."),
               ("Minimum = lower limit; below it the speed is abnormally low (anormalmente reducida).",
                "Mínima = límite inferior; por debajo, la velocidad es anormalmente reducida."),
               ("Adequate = adapted to the circumstances, so you control the vehicle in any unforeseen event.",
                "Adecuada = adaptada a las circunstancias, para controlar el vehículo ante cualquier imprevisto."),
               ("Inadequate = not taking all the factors into account; excessive = faster than the circumstances allow, even inside the limit.",
                "Inadecuada = no tener en cuenta todos los factores; excesiva = más rápida de lo que permiten las circunstancias, aunque sea dentro del límite.")],
        trap=("Treating exceso de velocidad (over the limit) and velocidad excesiva (too fast for the conditions) as the same thing.",
              "Tratar como lo mismo el exceso de velocidad (sobre el límite) y la velocidad excesiva (demasiado rápida para las circunstancias).")),
    "generic": dict(sec=2, en="Generic limits out of town", es="Límites genéricos fuera de poblado",
        recap=[("Cars, motorcycles, motorhomes up to 3,500 kg and pick-ups: 120 on motorways, 90 on other roads.",
                "Turismos, motos, autocaravanas hasta 3.500 kg y pick-up: 120 en autopista y autovía, 90 en las demás."),
               ("Buses, car-derived vans and adaptable mixed vehicles: 100 and 90.",
                "Autobuses, derivados de turismo y mixtos adaptables: 100 y 90."),
               ("Lorries, vans, motorhomes over 3,500 kg, vehicles with a trailer and the rest: 90 and 80.",
                "Camiones, furgonetas, autocaravanas de más de 3.500 kg, vehículos con remolque y resto: 90 y 80."),
               ("Up to 100 on conventional roads with physical separation if the road owner sets it; 30 on unpaved roads.",
                "Hasta 100 en convencionales con separación física si lo fija el titular; 30 en vías sin pavimentar.")],
        trap=("Giving a car towing a trailer, or a heavy motorhome, the car limits.",
              "Aplicar a un turismo con remolque, o a una autocaravana pesada, los límites del turismo.")),
    "urban": dict(sec=2, en="Limits in built-up areas", es="Límites en poblado",
        recap=[("Single platform (road and pavement level): 20. One lane per direction: 30.",
                "Plataforma única de calzada y acera: 20. Único carril por sentido: 30."),
               ("Two or more lanes per direction: 50. Travesía: 50.", "Dos o más carriles por sentido: 50. Travesía: 50."),
               ("Urban autopista or autovía: 80 maximum, 60 minimum.", "Autopista o autovía urbana: 80 de máxima y 60 de mínima."),
               ("Signs may lower them, or raise them on urban motorways, never above the out-of-town generic limit; travesías only lower; a one-lane street up to 50 at most.",
                "Las señales pueden rebajarlos, o ampliarlos en autopistas urbanas, nunca por encima del genérico fuera de poblado; travesías solo a la baja; una vía de un carril, hasta 50 como máximo.")],
        trap=("Thinking every urban street is 50, or that a one-lane street can be raised above 50.",
              "Pensar que toda calle es de 50, o que una vía de un carril puede subir por encima de 50.")),
    "others": dict(sec=2, en="Limits for other vehicles", es="Velocidades de otros vehículos",
        recap=[("Dangerous goods and school transport: 10 km/h less out of town; 40 and 50 in town. The minimum does not change.",
                "Mercancías peligrosas y transporte escolar: 10 km/h menos fuera de poblado; 40 y 50 en poblado. La mínima no cambia."),
               ("Cycles, mopeds and reduced-mobility vehicles: 45 (on autovías, bicycles only).",
                "Ciclos, ciclomotores y vehículos de movilidad reducida: 45 (en autovías, solo bicicletas)."),
               ("Three-wheeled vehicles and heavy quadricycles: 70, 70 and 50 in town.",
                "Vehículos de tres ruedas y cuadriciclos pesados: 70, 70 y 50 en poblado."),
               ("Special vehicles: 25 (no brake lights, trailer, motocultor), 40 (the rest), 70 if they can exceed 60 km/h on the flat.",
                "Especiales: 25 (sin señal de frenado, con remolque, motocultores), 40 (resto), 70 si superan 60 km/h en llano.")],
        trap=("Mixing up − 10 km/h (dangerous goods, school transport) with − 10 % (vehicles towing a trailer).",
              "Confundir − 10 km/h (mercancías peligrosas, escolar) con − 10 % (vehículos con remolque).")),
    "extra": dict(sec=2, en="Trailers, buses, bicycles and overtaking", es="Remolques, autobuses, bicicletas y adelantamiento",
        recap=[("Motorcycles, three-wheelers and mopeds towing a trailer: − 10 % of their maximum.",
                "Motos, tres ruedas y ciclomotores con remolque: − 10 % de su máxima."),
               ("Bus with standing passengers or without seat belts: 80 on any road out of town.",
                "Autobús con pasajeros de pie o sin cinturones: 80 en cualquier vía fuera de poblado."),
               ("Cyclists may exceed their generic maximum where the road allows a higher speed.",
                "Los ciclistas pueden superar su máxima genérica donde la vía permita una velocidad superior."),
               ("No extra 20 km/h for overtaking (since March 2022). Since October 2026, overtaking cyclists out of town: at least 20 km/h below the limit.",
                "No hay 20 km/h extra para adelantar (desde marzo de 2022). Desde octubre de 2026, al adelantar ciclistas en interurbana: al menos 20 km/h por debajo del límite.")],
        trap=("Remembering the old +20 km/h for overtaking, which no longer exists.",
              "Recordar el antiguo +20 km/h para adelantar, que ya no existe.")),
    "why": dict(sec=2, en="Why the limits matter", es="Por qué respetar los límites",
        recap=[("Limits rest on technical criteria: design speed, congestion, traffic demand, environmental impact.",
                "Los límites se basan en criterios técnicos: velocidad de diseño, congestión, demanda de tráfico, impacto ambiental."),
               ("Design speed = the highest speed that can be kept safely on a stretch in good conditions; never exceed it.",
                "Velocidad de diseño = la máxima que puede mantenerse con seguridad en un tramo en condiciones favorables; nunca se supera."),
               ("Faster = harder to control, longer to stop, worse injuries (above 120 km/h usually fatal).",
                "Más rápido = más difícil de controlar, más metros para parar, lesiones más graves (a más de 120 km/h suelen ser mortales)."),
               ("Conventional roads: oncoming traffic, junctions, no fences. Pedestrian hit at 80 km/h: almost certain death.",
                "Convencionales: tráfico de frente, intersecciones, sin vallas. Peatón atropellado a 80 km/h: muerte casi segura.")],
        trap=("Thinking motorways are the most dangerous roads because they are the fastest.",
              "Pensar que las autopistas son las vías más peligrosas por ser las más rápidas.")),
    "prevail": dict(sec=3, en="Speeds that take precedence", es="Velocidades prevalentes",
        recap=[("Signed limits, limits for certain drivers and limits for certain vehicles prevail over the generic maximums.",
                "Prevalecen sobre las máximas genéricas las fijadas por señales, a determinados conductores y a determinados vehículos."),
               ("Driver limits (personal circumstances) and vehicle limits (features or load) are shown with the V-4 plate.",
                "Los límites del conductor (circunstancias personales) y del vehículo (características o carga) se indican con la señal V-4."),
               ("The V-4 goes at the rear, always visible, and shows the speed the vehicle must not exceed.",
                "La V-4 va en la parte posterior, siempre visible, e indica la velocidad que el vehículo no debe rebasar."),
               ("The lowest applicable limit always wins.", "Siempre rige el límite aplicable más bajo.")],
        trap=("Following the road’s higher limit when the vehicle carries a lower V-4.",
              "Seguir el límite más alto de la vía cuando el vehículo lleva una V-4 más baja.")),
    "adapt": dict(sec=4, en="Speed suited to the circumstances", es="Velocidad adecuada a las circunstancias",
        recap=[("Respect the limits and also adapt to your own state, the road, the vehicle, the load, the weather and the traffic.",
                "Respetar los límites y además adaptarse al propio estado, la vía, el vehículo, la carga, la meteorología y la circulación."),
               ("Always be able to stop within your field of vision and before any obstacle.",
                "Poder detenerse siempre dentro del campo de visión y ante cualquier obstáculo."),
               ("Not adapting = inadequate speed; faster than the circumstances require = excessive speed.",
                "No adaptarse = velocidad inadecuada; más rápida de lo que requieren las circunstancias = velocidad excesiva."),
               ("Excessive speed is one of the main causes of accidents and makes them more often fatal.",
                "La velocidad excesiva es una de las principales causas de accidente y los hace más a menudo mortales.")],
        trap=("Believing that staying under the signed limit is always enough.", "Creer que ir por debajo del límite señalizado siempre basta.")),
    "moderate": dict(sec=4, en="When to slow down", es="Cuándo moderar la velocidad",
        recap=[("People: pedestrians and animals, children, elderly and blind people; schools and markets; cycles; uncontrolled crossings; buildings opening onto the road.",
                "Personas: peatones y animales, niños, ancianos e invidentes; colegios y mercados; ciclos; pasos no regulados; edificios con acceso a la vía."),
               ("Vehicles: stopped bus (above all school buses); out of town, immobilised vehicles, assistance vehicles and cycles.",
                "Vehículos: autobús parado (sobre todo escolar); fuera de poblado, vehículos inmovilizados, de auxilio y ciclos."),
               ("Road: slippery or splashing, level crossings, movable bridges, roundabouts, junctions without priority, poor visibility, narrowings, danger signs.",
                "Vía: deslizante o con salpicaduras, pasos a nivel, puentes móviles, glorietas, intersecciones sin prioridad, poca visibilidad, estrechamientos, señales de peligro."),
               ("Visibility: dazzle, dense fog, heavy rain, snow, dust or smoke. Signed junction with nil visibility: 50 km/h at most.",
                "Visibilidad: deslumbramiento, niebla densa, lluvia intensa, nevada, polvo o humo. Intersección señalizada con visibilidad nula: 50 km/h como máximo.")],
        trap=("Moderating only at crossings with traffic lights, when the rule targets the ones without.",
              "Moderar solo en los pasos con semáforo, cuando la norma se refiere a los que no lo tienen.")),
    "races": dict(sec=4, en="Races and cycling events", es="Competiciones y marchas ciclistas",
        recap=[("Speed competitions on public roads are forbidden unless authorised and the area is prepared.",
                "Las competiciones de velocidad en vías públicas están prohibidas salvo autorización y acondicionamiento de la zona."),
               ("Cycling events with more than 50 cyclists need prior authorisation.", "Las marchas ciclistas de más de 50 ciclistas necesitan autorización previa."),
               ("Holiday or not, urban or interurban: the rule is the same.", "Sea festivo o no, urbana o interurbana: la norma es la misma."),
               ("Agents or authorised staff keep order; the staff’s instructions count as an agent’s.",
                "El orden lo mantienen agentes o personal habilitado; las órdenes de ese personal valen como las de los agentes.")],
        trap=("Thinking that a holiday or an urban route removes the need for authorisation.",
              "Pensar que un festivo o un recorrido urbano evitan la autorización.")),
    "minimum": dict(sec=5, en="Minimum speed", es="Velocidad mínima",
        recap=[("Autopistas and autovías: 60 km/h minimum for motor vehicles. Other roads: half the generic maximum.",
                "Autopistas y autovías: 60 km/h de mínima para vehículos a motor. Demás vías: la mitad de la genérica."),
               ("It applies even when there is no other traffic.", "Se aplica aunque no circulen otros vehículos."),
               ("Exempt: cycles, animal-drawn vehicles, special vehicles and special transport, escort vehicles, and anyone when conditions make a higher speed unsafe.",
                "Exentos: ciclos, tracción animal, especiales y transporte especial, vehículos de acompañamiento y cualquiera cuando las circunstancias impidan ir más rápido sin riesgo."),
               ("Cannot reach the minimum and risk being hit: hazard lights. Emergency on a motorway: leave at the first exit.",
                "Sin alcanzar la mínima y con peligro de alcance: luz de emergencia. Emergencia en autopista: salir por la primera salida.")],
        trap=("Using 60 km/h as the minimum on every road, or thinking the minimum lapses when the road is empty.",
              "Usar 60 km/h como mínima en todas las vías, o pensar que la mínima no rige si la vía está vacía.")),
    "slowing": dict(sec=5, en="Slowing down", es="Reducción de la velocidad",
        recap=[("Except in imminent danger, before slowing down sharply check the mirrors: distance and speed of those behind.",
                "Salvo peligro inminente, antes de reducir mucho la velocidad hay que mirar los espejos: distancia y velocidad de los de detrás."),
               ("Warn whenever possible: repeated brake lights, or the arm moved up and down in short, quick movements.",
                "Avisar siempre que sea posible: luces de freno reiteradas o el brazo de arriba abajo con movimientos cortos y rápidos."),
               ("Reduce smoothly, never abruptly, so nobody runs into you.", "Reducir sin brusquedades para que nadie te alcance."),
               ("The hazard lights are for when you cannot reach the minimum, not the usual way to warn of braking.",
                "La luz de emergencia es para cuando no se alcanza la mínima, no la forma habitual de avisar de una frenada.")],
        trap=("Answering “hazard lights” or “indicator” when the rule is brake lights or the arm.",
              "Responder «luz de emergencia» o «intermitente» cuando la norma dice luces de freno o el brazo.")),
}


# ---------------------------------------------------------------- 1. concepts
Q("cn1", "concepts", "The maximum speed (velocidad máxima) is…", "La velocidad máxima es…",
  [("the upper limit allowed for your vehicle on the road you are on", "el límite superior permitido para tu vehículo en la vía por la que circulas"),
   ("the highest speed your vehicle can reach", "la mayor velocidad que puede alcanzar tu vehículo"),
   ("the speed the road was designed for", "la velocidad para la que se diseñó la vía")],
  "Going above it is exceso de velocidad.", "Superarla es circular con exceso de velocidad.")
Q("cn2", "concepts", "Driving below the minimum speed allowed is called…", "Circular por debajo de la velocidad mínima permitida se llama…",
  [("abnormally low speed (velocidad anormalmente reducida)", "velocidad anormalmente reducida"), ("adequate speed", "velocidad adecuada"), ("moderate speed", "velocidad moderada")],
  "It can hold up the traffic and cause accidents.", "Puede entorpecer la circulación y causar accidentes.")
Q("cn3", "concepts", "The adequate speed (velocidad adecuada) is the one that…", "La velocidad adecuada es la que…",
  [("suits the circumstances of each moment and lets you control the vehicle in any unforeseen event", "se adapta a las circunstancias de cada momento y permite controlar el vehículo ante cualquier imprevisto"),
   ("matches exactly the maximum on the signs", "coincide exactamente con la máxima señalizada"),
   ("is halfway between the minimum and the maximum", "está a medio camino entre la mínima y la máxima")],
  "Limits, weather and the driver’s state all count.", "Cuentan los límites, la meteorología y el estado del conductor.")
Q("cn4", "concepts", "You drive at an inadequate speed (velocidad inadecuada) when…", "Se circula a velocidad inadecuada cuando…",
  [("you do not take into account all the factors that affect driving", "no se tienen en cuenta todos los factores que afectan a la conducción"),
   ("only when you exceed the signed limit", "solo cuando se supera el límite señalizado"),
   ("you drive below the minimum", "se circula por debajo de la mínima")],
  "It raises the risk of an accident, even within the limits.", "Aumenta el riesgo de accidente, incluso dentro de los límites.")
Q("cn5", "concepts", "You drive a car at 100 km/h on a motorway in heavy snow. Your speed is…", "Conduces un turismo a 100 km/h por una autopista con mucha nieve. Tu velocidad es…",
  [("within the limit, but excessive for the conditions", "dentro del límite, pero excesiva para las circunstancias"),
   ("correct, because the limit is 120 km/h", "correcta, porque el límite es 120 km/h"), ("abnormally low", "anormalmente reducida")],
  "Respecting the limit is not enough: the speed must fit the conditions.", "Respetar el límite no basta: la velocidad debe ajustarse a las circunstancias.")
Q("cn6", "concepts", "What is the difference between exceso de velocidad and velocidad excesiva?", "¿Qué diferencia hay entre exceso de velocidad y velocidad excesiva?",
  [("The first is going over the limit; the second is going too fast for the conditions, even within the limit", "La primera es superar el límite; la segunda, ir demasiado rápido para las circunstancias, aunque sea dentro del límite"),
   ("None, they mean the same", "Ninguna, significan lo mismo"),
   ("The first applies only in town, the second only out of town", "La primera solo rige en poblado y la segunda fuera de poblado")],
  "You can drive at a velocidad excesiva without any exceso de velocidad.", "Se puede circular a velocidad excesiva sin exceso de velocidad.")

# ---------------------------------------------------------------- 2. generic limits
Q("gn1", "generic", "What is the generic maximum speed for a car on an autopista or autovía?", "¿Cuál es la velocidad máxima genérica de un turismo en autopista o autovía?",
  K(120, 100, 130), "Also motorcycles, motorhomes up to 3,500 kg and pick-ups.", "También motos, autocaravanas hasta 3.500 kg y pick-up.")
Q("gn2", "generic", "What is the generic maximum speed for a car on a carretera convencional?", "¿Cuál es la velocidad máxima genérica de un turismo en carretera convencional?",
  K(90, 100, 80), "Up to 100 only where the directions are physically separated and the road owner sets it.", "Hasta 100 solo con separación física de sentidos y si lo fija el titular.")
Q("gn3", "generic", "What is the generic maximum speed for a bus on an autovía?", "¿Cuál es la velocidad máxima genérica de un autobús en autovía?",
  K(100, 90, 120), "Buses, car-derived vans and adaptable mixed vehicles: 100 on motorways, 90 on other roads.", "Autobuses, derivados de turismo y mixtos adaptables: 100 en autopista y autovía, 90 en las demás.")
Q("gn4", "generic", "A lorry on a carretera convencional may drive at most at…", "Un camión por una carretera convencional puede circular como máximo a…",
  K(80, 90, 70), "Lorries: 90 on motorways, 80 on other roads.", "Camiones: 90 en autopista y autovía, 80 en las demás.")
Q("gn5", "generic", "A car-derived van (vehículo derivado de turismo) on a motorway: what is its maximum?", "Un vehículo derivado de turismo en autopista: ¿cuál es su máxima?",
  K(100, 120, 90), "It goes with buses and adaptable mixed vehicles. A furgoneta goes with lorries (90).", "Va con autobuses y mixtos adaptables. La furgoneta va con los camiones (90).")
Q("gn6", "generic", "A motorhome with an MMA of 3,500 kg on an autopista may drive at most at…", "Una autocaravana de 3.500 kg de MMA por autopista puede circular como máximo a…",
  K(120, 100, 90), "Up to 3,500 kg it has the car limits; above, the lorry limits.", "Hasta 3.500 kg tiene los límites del turismo; por encima, los del camión.")
Q("gn7", "generic", "A car towing a trailer on an autopista may drive at most at…", "Un turismo con remolque por autopista puede circular como máximo a…",
  K(90, 120, 100), "Vehicles with a trailer go in the lorry group: 90 on motorways, 80 on other roads.", "Los vehículos con remolque van en el grupo de los camiones: 90 en autopista, 80 en las demás.")
Q("gn8", "generic", "On a carretera convencional with the two directions physically separated, the road owner may set a maximum for cars of…",
  "En una carretera convencional con separación física de los dos sentidos, el titular puede fijar para turismos una máxima de…",
  K(100, 110, 120), "Only for cars, motorcycles and motorhomes up to 3,500 kg.", "Solo para turismos, motos y autocaravanas de hasta 3.500 kg.")
Q("gn9", "generic", "What is the maximum speed on an unpaved road?", "¿Cuál es la velocidad máxima en una vía sin pavimentar?",
  K(30, 40, 50), "Whatever the vehicle.", "Sea cual sea el vehículo.")
Q("gn10", "generic", "A pick-up on an autovía may drive at most at…", "Un pick-up por autovía puede circular como máximo a…",
  K(120, 100, 90), "Pick-ups share the car limits.", "Los pick-up comparten los límites del turismo.")

# ---------------------------------------------------------------- 2.1 urban
Q("ur1", "urban", "What is the generic limit on a street where road and pavement are at the same level (plataforma única)?", "¿Cuál es el límite genérico en una vía de plataforma única de calzada y acera?",
  K(20, 30, 10), "Pedestrians and vehicles share the same surface.", "Peatones y vehículos comparten la misma superficie.")
Q("ur2", "urban", "What is the generic limit on an urban street with a single lane per direction?", "¿Cuál es el límite genérico en una vía urbana de único carril por sentido?",
  K(30, 50, 40), "With two or more lanes per direction it is 50.", "Con dos o más carriles por sentido es 50.")
Q("ur3", "urban", "What is the generic limit on an urban road with two or more lanes per direction?", "¿Cuál es el límite genérico en una vía urbana con dos o más carriles por sentido?",
  K(50, 30, 60), "One lane per direction: 30.", "Un carril por sentido: 30.")
Q("ur4", "urban", "What is the generic limit in a travesía?", "¿Cuál es el límite genérico en una travesía?",
  K(50, 30, 90), "Signs may lower it or raise it, never above the road’s out-of-town limit.", "Las señales pueden rebajarlo o ampliarlo, nunca por encima del límite de esa vía fuera de poblado.")
Q("ur5", "urban", "On an autopista or autovía inside a built-up area, the generic limits are…", "En una autopista o autovía dentro de poblado, los límites genéricos son…",
  [("80 maximum and 60 minimum", "80 de máxima y 60 de mínima"), ("120 maximum and 60 minimum", "120 de máxima y 60 de mínima"), ("50 maximum and 25 minimum", "50 de máxima y 25 de mínima")],
  "They may be raised by signs, never above the out-of-town generic limit.", "Pueden ampliarse con señales, nunca por encima del genérico fuera de poblado.")
Q("ur6", "urban", "Exceptionally, the authority may raise the limit of a one-lane-per-direction urban street, with specific signs, to at most…",
  "Excepcionalmente, la autoridad puede subir el límite de una vía urbana de único carril por sentido, con señalización específica, hasta…",
  K(50, 60, 40), "Never above 50.", "Nunca por encima de 50.")
Q("ur7", "urban", "The limit of an urban autopista or autovía may be raised by signs, but never…", "El límite de una autopista o autovía urbana puede ampliarse con señales, pero nunca…",
  [("above the generic limit for that kind of road out of town", "por encima del límite genérico de esa vía fuera de poblado"), ("above 50 km/h", "por encima de 50 km/h"), ("at night", "de noche")],
  "The travesía limit can only be lowered.", "El límite de las travesías solo puede rebajarse.")

# ---------------------------------------------------------------- 2.2 other vehicles
Q("ov1", "others", "Out of town, a vehicle carrying dangerous goods has a maximum speed of…", "Fuera de poblado, un vehículo que transporta mercancías peligrosas tiene una velocidad máxima de…",
  [("10 km/h less than the generic one for its type and road", "10 km/h menos que la genérica de su tipo y vía"), ("the same as other vehicles of its type", "la misma que los demás vehículos de su tipo"),
   ("60 km/h on any road", "60 km/h en cualquier vía")],
  "Its minimum stays the general one. In town: 40.", "Su mínima sigue siendo la general. En poblado: 40.")
Q("ov2", "others", "In town, the maximum for a vehicle carrying dangerous goods is…", "En poblado, la máxima de un vehículo de mercancías peligrosas es…",
  K(40, 50, 30), "School transport in town: 50.", "Transporte escolar en poblado: 50.")
Q("ov3", "others", "In town, the maximum for school transport is…", "En poblado, la máxima del transporte escolar es…",
  K(50, 40, 30), "Out of town: 10 km/h less than the generic limit.", "Fuera de poblado: 10 km/h menos que la genérica.")
Q("ov4", "others", "Out of town, school and minors transport may drive…", "Fuera de poblado, el transporte escolar y de menores puede circular…",
  [("10 km/h below the generic maximum for that vehicle and road", "10 km/h por debajo de la máxima genérica para ese vehículo y vía"), ("at 80 km/h on any road", "a 80 km/h en cualquier vía"),
   ("at the same speed as other buses", "a la misma velocidad que los demás autobuses")],
  "The minimum is the general one for each class of vehicle and road.", "La mínima es la general para cada clase de vehículo y vía.")
Q("ov5", "others", "What is the generic maximum speed of a moped?", "¿Cuál es la velocidad máxima genérica de un ciclomotor?",
  K(45, 50, 25), "Same for cycles and vehicles for people with reduced mobility.", "Igual para ciclos y vehículos para personas de movilidad reducida.")
Q("ov6", "others", "Which of these may NOT drive on a vía para automóviles?", "¿Cuál de estos NO puede circular por una vía para automóviles?",
  [("A moped", "Un ciclomotor"), ("A car", "Un turismo"), ("A bus", "Un autobús")],
  "Cycles, mopeds, reduced-mobility vehicles and slow special vehicles: conventional roads only.", "Ciclos, ciclomotores, vehículos de movilidad reducida y especiales lentos: solo carreteras convencionales.")
Q("ov7", "others", "What is the maximum for a three-wheeled vehicle on a carretera convencional?", "¿Cuál es la máxima de un vehículo de tres ruedas en carretera convencional?",
  K(70, 90, 45), "Also heavy quadricycles. In town: 50.", "También los cuadriciclos pesados. En poblado: 50.")
Q("ov8", "others", "A special vehicle without brake lights, or towing a trailer, on a conventional road may drive at most at…",
  "Un vehículo especial sin señalización de frenado, o con remolque, por una carretera convencional puede circular como máximo a…",
  K(25, 40, 45), "Same for motocultores. They may not use autopistas or autovías.", "Igual los motocultores. No pueden circular por autopistas ni autovías.")
Q("ov9", "others", "Special vehicles that cannot exceed 60 km/h on the flat (and have brake lights and no trailer) may drive on a conventional road at most at…",
  "Los vehículos especiales que no superan 60 km/h en llano (con señal de frenado y sin remolque) pueden circular por carretera convencional como máximo a…",
  K(40, 25, 70), "They may not use autopistas or autovías.", "No pueden circular por autopistas ni autovías.")
Q("ov10", "others", "A special vehicle able to exceed 60 km/h on the flat that meets the vehicle regulations may drive on an autovía at most at…",
  "Un vehículo especial que supera 60 km/h en llano y cumple las normas reguladoras de los vehículos puede circular por autovía como máximo a…",
  K(70, 60, 90), "In town: 50.", "En poblado: 50.")
Q("ov11", "others", "On autovías, the 45 km/h limit for cycles applies to…", "En las autovías, el límite de 45 km/h de los ciclos se aplica a…",
  [("bicycles only (mopeds may not use autovías)", "solo bicicletas (los ciclomotores no pueden circular por autovías)"), ("bicycles and mopeds", "bicicletas y ciclomotores"),
   ("all cycles, on autopistas too", "todos los ciclos, también en autopistas")],
  "Cyclists over 14 may use the shoulder of an autovía, never of an autopista.", "Los ciclistas mayores de 14 años pueden ir por el arcén de la autovía, nunca de la autopista.")

# ---------------------------------------------------------------- 2.2 extras
Q("ex1", "extra", "A motorcycle towing a trailer must…", "Una motocicleta que arrastra un remolque debe…",
  [("reduce its maximum speed by 10 %", "reducir un 10 % su velocidad máxima"), ("reduce its maximum by 10 km/h", "reducir 10 km/h su velocidad máxima"), ("keep the same maximum", "mantener la misma velocidad máxima")],
  "Also three-wheeled vehicles and mopeds towing a trailer or semitrailer.", "También vehículos de tres ruedas y ciclomotores con remolque o semirremolque.")
Q("ex2", "extra", "A bus carrying authorised standing passengers may drive out of town at most at…", "Un autobús con pasajeros de pie autorizados puede circular fuera de poblado como máximo a…",
  K(80, 90, 100), "On any type of road out of town.", "En cualquier tipo de vía fuera de poblado.")
Q("ex3", "extra", "A bus without seat belts on an autopista may drive at most at…", "Un autobús sin cinturones de seguridad por autopista puede circular como máximo a…",
  K(80, 100, 90), "Same as with standing passengers.", "Igual que con pasajeros de pie.")
Q("ex4", "extra", "May a cyclist go faster than the generic maximum for bicycles?", "¿Puede un ciclista superar la velocidad máxima genérica de las bicicletas?",
  [("Yes, on stretches where the road allows a higher speed", "Sí, en los tramos en que las circunstancias de la vía permitan una velocidad superior"), ("No, never", "No, nunca"),
   ("Only when overtaking", "Solo al adelantar")],
  "It depends on the road, not on overtaking.", "Depende de la vía, no del adelantamiento.")
Q("ex5", "extra", "Since 1 October 2026, when you overtake a cyclist on an interurban road you must drive…", "Desde el 1 de octubre de 2026, al adelantar a un ciclista en vía interurbana debes circular…",
  [("at least 20 km/h below the road’s limit", "al menos 20 km/h por debajo del límite de la vía"), ("up to 20 km/h above the limit, to overtake quickly", "hasta 20 km/h por encima del límite, para adelantar rápido"),
   ("at the road’s limit, never less", "al límite de la vía, nunca menos")],
  "The overtaking topic covers the side gap and the lane change.", "El tema de adelantamientos trata la separación lateral y el cambio de carril.")
Q("ex6", "extra", "When overtaking on a carretera convencional, may you exceed the limit by 20 km/h?", "Al adelantar en una carretera convencional, ¿puedes superar el límite en 20 km/h?",
  [("No, that allowance was removed in 2022", "No, esa posibilidad se suprimió en 2022"), ("Yes, cars and motorcycles", "Sí, turismos y motocicletas"),
   ("Yes, if the overtaken vehicle is below the limit", "Sí, si el adelantado va por debajo del límite")],
  "The limit is the same while overtaking.", "El límite es el mismo durante el adelantamiento.")

# ---------------------------------------------------------------- 2.3 why
Q("wy1", "why", "The design speed of a road is…", "La velocidad de diseño de una vía es…",
  [("the highest speed that can be kept safely on a stretch in good conditions", "la máxima velocidad que puede mantenerse con seguridad en un tramo en condiciones favorables"),
   ("the minimum speed for that road", "la velocidad mínima de esa vía"), ("the speed most drivers actually use", "la velocidad a la que circula la mayoría")],
  "Never exceed it: the road’s safety was calculated for it.", "No debe superarse nunca: la seguridad de la vía se calculó para ella.")
Q("wy2", "why", "The generic speed limits are based on…", "Los límites genéricos de velocidad se basan en…",
  [("technical criteria such as design speed, congestion, traffic demand and environmental impact", "criterios técnicos como la velocidad de diseño, la congestión, la demanda de tráfico y el impacto ambiental"),
   ("the power of the vehicles", "la potencia de los vehículos"), ("only the previous year’s accidents", "solo los accidentes del año anterior")],
  "Their aim: safety and traffic flow.", "Su objetivo: seguridad y fluidez.")
Q("wy3", "why", "At a higher speed…", "A mayor velocidad…",
  [("the vehicle is harder to control and needs more metres to stop", "es más difícil controlar el vehículo y se recorren más metros antes de detenerse"),
   ("the stopping distance stays the same", "la distancia de detención no cambia"), ("injuries are less serious thanks to modern cars", "las lesiones son menos graves gracias a los coches modernos")],
  "Injuries are also more serious: above 120 km/h crashes are usually fatal.", "Las lesiones también son más graves: a más de 120 km/h los accidentes suelen ser mortales.")
Q("wy4", "why", "Why are conventional roads more dangerous than autopistas and autovías?", "¿Por qué las carreteras convencionales son más peligrosas que las autopistas y autovías?",
  [("Both directions share the road, there are junctions and they are not fenced", "Los dos sentidos van juntos, hay intersecciones y no están valladas"),
   ("Their limits are higher", "Sus límites son más altos"), ("They have more lanes", "Tienen más carriles")],
  "So you can meet oncoming vehicles, crossing traffic, pedestrians and animals.", "Por eso puede haber vehículos de frente, cruces, peatones y animales.")
Q("wy5", "why", "A pedestrian hit by a car at 80 km/h…", "Un peatón atropellado a 80 km/h…",
  [("will almost certainly die", "morirá casi con seguridad"), ("has about a 15 % chance of dying", "tiene alrededor de un 15 % de probabilidades de morir"), ("will usually survive", "normalmente sobrevivirá")],
  "At 30 km/h most pedestrians survive.", "A 30 km/h la mayoría de los peatones sobrevive.")
Q("wy6", "why", "Lowering speed in town from 50 to 30 km/h…", "Bajar la velocidad en ciudad de 50 a 30 km/h…",
  [("greatly reduces the chance that a pedestrian who is hit dies", "reduce mucho la probabilidad de que muera un peatón atropellado"),
   ("makes no difference to pedestrians", "no cambia nada para los peatones"), ("only reduces noise", "solo reduce el ruido")],
  "From roughly half or more at 50 km/h to 10–15 % at 30 km/h.", "De la mitad o más a 50 km/h a un 10–15 % a 30 km/h.")
Q("wy7", "why", "According to your course, above which speed are crashes usually fatal?", "Según tu curso, ¿a partir de qué velocidad los accidentes suelen ser mortales?",
  K(120, 60, 200), "Higher speed means more serious injuries.", "A mayor velocidad, lesiones más graves.")

# ---------------------------------------------------------------- 3. prevailing speeds
Q("pv1", "prevail", "Which speeds prevail over the generic maximums?", "¿Qué velocidades prevalecen sobre las máximas genéricas?",
  [("those set by signs, for certain drivers and for certain vehicles", "las fijadas por señales, a determinados conductores y a determinados vehículos"),
   ("those the driver chooses", "las que elija el conductor"), ("those the speedometer shows", "las que marque el velocímetro")],
  "Drivers for personal circumstances; vehicles for their features or load.", "Conductores por circunstancias personales; vehículos por sus características o su carga.")
Q("pv2", "prevail", "A sign shows 70 on a carretera convencional, where the generic limit for cars is 90. In a car you may drive at most at…",
  "Una señal marca 70 en una carretera convencional donde el genérico para turismos es 90. Con un turismo puedes circular como máximo a…",
  K(70, 90, 80), "Signed limits prevail.", "Prevalecen los límites señalizados.")
Q("pv3", "prevail", "The V-4 plate shows…", "La señal V-4 indica…",
  [("the speed the vehicle must not exceed", "la velocidad que el vehículo no debe rebasar"), ("the vehicle’s minimum speed", "la velocidad mínima del vehículo"),
   ("the recommended speed for the road", "la velocidad recomendada en la vía")],
  "It is a speed-limitation plate.", "Es una señal de limitación de velocidad.")
Q("pv4", "prevail", "Where does the V-4 plate go?", "¿Dónde se coloca la señal V-4?",
  [("At the rear of the vehicle, always visible", "En la parte posterior del vehículo, siempre visible"), ("On the windscreen", "En el parabrisas"), ("On the dashboard", "En el salpicadero")],
  "Drivers behind need to see it.", "Deben verla los que circulan detrás.")
Q("pv5", "prevail", "Which vehicles carry the V-4 plate?", "¿Qué vehículos llevan la señal V-4?",
  [("those limited because of the driver’s personal circumstances or the vehicle’s features or load", "los limitados por circunstancias personales del conductor o por las características o la carga del vehículo"),
   ("every heavy vehicle", "todos los vehículos pesados"), ("every vehicle on a motorway", "todos los que circulan por autopista")],
  "The plate shows their own maximum.", "La señal indica su propia máxima.")
Q("pv6", "prevail", "On an autovía signed at 100 km/h, your vehicle carries a V-4 plate showing 80. You may drive at most at…",
  "En una autovía señalizada a 100 km/h, tu vehículo lleva una señal V-4 de 80. Puedes circular como máximo a…",
  K(80, 100, 90), "The lowest applicable limit wins.", "Rige el límite aplicable más bajo.")

# ---------------------------------------------------------------- 4. adequate speed
Q("ad1", "adapt", "Besides respecting the limits, every driver must take into account…", "Además de respetar los límites, todo conductor debe tener en cuenta…",
  [("their physical and mental condition, the road, the vehicle, its load, the weather and the traffic", "sus condiciones físicas y psíquicas, la vía, el vehículo, su carga, la meteorología y la circulación"),
   ("only the signs", "solo las señales"), ("only the weather", "solo la meteorología")],
  "The more circumstances there are at once, the more you adapt.", "Cuantas más circunstancias concurran, más hay que adaptarse.")
Q("ad2", "adapt", "Adapting your speed means you can always stop…", "Adecuar la velocidad significa poder detenerse siempre…",
  [("within your field of vision and before any obstacle", "dentro de los límites de tu campo de visión y ante cualquier obstáculo"), ("within 100 metres", "en 100 metros"),
   ("before the next sign", "antes de la siguiente señal")],
  "If you cannot see far, you must be able to stop in less.", "Si ves poco, tienes que poder parar en menos.")
Q("ad3", "adapt", "Velocidad excesiva is…", "La velocidad excesiva es…",
  [("a speed higher than the circumstances require", "una velocidad superior a la que requieren las circunstancias"), ("only a speed above the signed limit", "solo una velocidad superior al límite señalizado"),
   ("a speed below the minimum", "una velocidad inferior a la mínima")],
  "It is one of the main causes of accidents.", "Es una de las principales causas de accidente.")
Q("ad4", "adapt", "Velocidad excesiva makes an accident…", "La velocidad excesiva hace que un accidente sea…",
  [("more likely, and more likely to be fatal", "más probable, y con más probabilidad de ser mortal"), ("less likely if the road is good", "menos probable si la vía es buena"), ("no more serious", "igual de grave")],
  "It is a kind of inadequate speed.", "Es una forma de velocidad inadecuada.")
Q("ad5", "adapt", "If you do not adapt your speed to the circumstances, you are driving at…", "Si no adaptas la velocidad a las circunstancias, circulas a…",
  [("an inadequate speed", "velocidad inadecuada"), ("an abnormally low speed", "velocidad anormalmente reducida"), ("the design speed", "velocidad de diseño")],
  "It can happen even within the limits.", "Puede ocurrir incluso dentro de los límites.")

# ---------------------------------------------------------------- 4.1 moderate
Q("md1", "moderate", "You must drive at a moderate speed, and stop if necessary, when…", "Debes circular a velocidad moderada, y detenerte si es preciso, cuando…",
  [("children may step onto the road near a school", "pueden irrumpir niños en la vía cerca de un colegio"), ("the road is wide and empty", "la vía es ancha y está despejada"),
   ("you are on a motorway with good visibility", "vas por una autopista con buena visibilidad")],
  "Also near markets and other places where children are likely.", "También cerca de mercados y otros lugares con presencia previsible de niños.")
Q("md2", "moderate", "At a properly signed junction where visibility is practically nil, the speed may not exceed…", "En una intersección debidamente señalizada con visibilidad prácticamente nula, la velocidad no deberá exceder de…",
  K(50, 30, 40), "Even if you have priority.", "Aunque se tenga prioridad.")
Q("md3", "moderate", "Approaching a stopped bus, especially a school bus, you must…", "Al aproximarte a un autobús en situación de parada, sobre todo escolar, debes…",
  [("moderate your speed", "moderar la velocidad"), ("sound the horn and keep your speed", "tocar el claxon y mantener la velocidad"), ("overtake it quickly", "adelantarlo rápidamente")],
  "Passengers, often children, may cross in front of or behind it.", "Los pasajeros, a menudo niños, pueden cruzar por delante o por detrás.")
Q("md4", "moderate", "Out of town, approaching a vehicle immobilised on the carriageway or a recovery vehicle at work, you must…",
  "Fuera de poblado, al acercarte a un vehículo inmovilizado en la calzada o a un vehículo de auxilio prestando servicio, debes…",
  [("moderate your speed", "moderar la velocidad"), ("flash your headlights and keep going", "dar ráfagas y seguir"), ("always stop", "detenerte siempre")],
  "Same for cycles on the carriageway or its shoulder.", "Igual con los ciclos que circulan por la calzada o su arcén.")
Q("md5", "moderate", "At which pedestrian crossings must you moderate your speed?", "¿En qué pasos de peatones debes moderar la velocidad?",
  [("Those not controlled by traffic lights or agents", "En los no regulados por semáforo o agentes"), ("Only those with traffic lights", "Solo en los regulados por semáforo"),
   ("None: pedestrians must wait", "En ninguno: los peatones deben esperar")],
  "Nothing stops pedestrians there, so you must be ready.", "Allí nada detiene a los peatones, así que hay que estar preparado.")
Q("md6", "moderate", "On a wet road where you could splash pedestrians, you must…", "En una vía mojada donde podrías salpicar a los peatones, debes…",
  [("moderate your speed", "moderar la velocidad"), ("sound the horn to warn them", "tocar el claxon para avisarles"), ("move to the left lane", "pasarte al carril izquierdo")],
  "Same with gravel or other material that could be thrown up.", "Igual con gravilla u otras materias que puedan proyectarse.")
Q("md7", "moderate", "If you are dazzled, you must…", "Si sufres un deslumbramiento, debes…",
  [("reduce your speed, stopping if necessary, so as not to hit vehicles or pedestrians", "reducir la velocidad, e incluso detenerte, para no alcanzar a vehículos o peatones"),
   ("switch on your main beam", "encender la luz de carretera"), ("keep your speed and look at the centre line", "mantener la velocidad y mirar a la línea central")],
  "You cannot see what is ahead, so you must be able to stop.", "No ves lo que hay delante, así que debes poder detenerte.")
Q("md8", "moderate", "Which of these is NOT one of the listed reasons to moderate speed?", "¿Cuál de estas NO es una de las situaciones en las que hay que moderar la velocidad?",
  [("A straight, dry autovía with light traffic", "Una autovía recta, seca y con poco tráfico"), ("Approaching a roundabout", "Acercarse a una glorieta"),
   ("Approaching a level crossing", "Acercarse a un paso a nivel")],
  "Roundabouts, level crossings and movable bridges are on the list.", "Glorietas, pasos a nivel y puentes móviles están en la lista.")
Q("md9", "moderate", "You must moderate your speed on stretches with buildings that…", "Hay que moderar la velocidad en tramos con edificios que…",
  [("open directly onto the road", "tienen acceso inmediato a la vía"), ("are more than three storeys high", "tienen más de tres plantas"), ("are industrial", "son industriales")],
  "People and vehicles may come out suddenly.", "Pueden salir personas o vehículos de repente.")

# ---------------------------------------------------------------- 4.2 races
Q("rc1", "races", "Speed competitions on public roads are…", "Las competiciones de velocidad en vías públicas están…",
  [("forbidden unless authorised and the area is prepared", "prohibidas salvo autorización y acondicionamiento de la zona"), ("allowed at night", "permitidas de noche"),
   ("allowed on autopistas", "permitidas en autopistas")],
  "The competent authority must authorise them.", "Debe autorizarlas la autoridad competente.")
Q("rc2", "races", "An organised cycling event on public roads needs prior authorisation when it has more than…", "Una marcha ciclista organizada por vías públicas necesita autorización previa cuando tiene más de…",
  [("50 cyclists", "50 ciclistas"), ("20 cyclists", "20 ciclistas"), ("100 cyclists", "100 ciclistas")],
  "Holiday or not, urban or interurban.", "Sea festivo o no, en vía urbana o interurbana.")
Q("rc3", "races", "Does a cycling event with 80 cyclists on an urban road on a public holiday need authorisation?", "¿Necesita autorización una marcha de 80 ciclistas por vía urbana en día festivo?",
  [("Yes, whatever the day or the type of road", "Sí, sea festivo o no y en vía urbana o interurbana"), ("No, not on holidays", "No, en festivos no"), ("Only on interurban roads", "Solo en vías interurbanas")],
  "The threshold is more than 50 cyclists.", "El umbral es de más de 50 ciclistas.")
Q("rc4", "races", "Who keeps control and order during a cycling event?", "¿Quién se encarga del control y orden de una marcha ciclista?",
  [("Traffic agents or the organisation’s authorised staff", "Los agentes de la autoridad o el personal habilitado de la organización"), ("The cyclist at the front", "El ciclista que va en cabeza"),
   ("Any volunteer", "Cualquier voluntario")],
  "Both for the participants and for the other road users.", "Tanto respecto a los participantes como al resto de usuarios.")
Q("rc5", "races", "Instructions given by the authorised staff of a cycling event…", "Las órdenes del personal habilitado de una marcha ciclista…",
  [("must be obeyed like those of traffic agents", "se obedecen como las de los agentes"), ("are only recommendations", "son solo recomendaciones"), ("apply only to the cyclists", "solo afectan a los ciclistas")],
  "They act as the agents’ auxiliaries, following their guidelines.", "Actúan como auxiliares de los agentes, siguiendo sus directrices.")

# ---------------------------------------------------------------- 5. minimum speed
Q("mn1", "minimum", "What is the minimum speed for motor vehicles on autopistas and autovías?", "¿Cuál es la velocidad mínima de los vehículos a motor en autopistas y autovías?",
  K(60, 50, 70), "On other roads: half the generic maximum.", "En las demás vías: la mitad de la máxima genérica.")
Q("mn2", "minimum", "On a carretera convencional, the minimum speed is…", "En una carretera convencional, la velocidad mínima es…",
  [("half the generic maximum for that vehicle", "la mitad de la máxima genérica para ese vehículo"), ("60 km/h for everyone", "60 km/h para todos"), ("there is no minimum", "no hay mínima")],
  "Car 45, lorry 40.", "Turismo 45, camión 40.")
Q("mn3", "minimum", "What is the minimum speed for a car on a carretera convencional?", "¿Cuál es la velocidad mínima de un turismo en carretera convencional?",
  K(45, 60, 40), "Half of 90.", "La mitad de 90.")
Q("mn4", "minimum", "What is the minimum speed for a lorry on a carretera convencional?", "¿Cuál es la velocidad mínima de un camión en carretera convencional?",
  K(40, 45, 60), "Half of 80.", "La mitad de 80.")
Q("mn5", "minimum", "Does the minimum speed apply when there is no other traffic?", "¿Rige la velocidad mínima cuando no circulan otros vehículos?",
  [("Yes, even with no other vehicles", "Sí, aunque no circulen otros vehículos"), ("No, only when someone is behind", "No, solo si hay alguien detrás"), ("Only on motorways", "Solo en autopistas")],
  "Without a justified cause you may not drive below it.", "Sin causa justificada no se puede circular por debajo.")
Q("mn6", "minimum", "Which of these may drive below the minimum speed?", "¿Cuál de estos puede circular por debajo de la velocidad mínima?",
  [("An escort vehicle matching the speed of the vehicle it accompanies", "Un vehículo de acompañamiento que adecua su velocidad a la del acompañado"),
   ("A car whose driver is in no hurry", "Un turismo cuyo conductor no tiene prisa"), ("A lorry trying to save fuel", "Un camión que quiere ahorrar combustible")],
  "Also cycles, animal-drawn vehicles, special vehicles and special transport.", "También ciclos, tracción animal, vehículos especiales y transporte especial.")
Q("mn7", "minimum", "A vehicle that cannot reach the minimum speed, with a risk of being hit from behind, must…", "Un vehículo que no puede alcanzar la velocidad mínima, con peligro de alcance, debe…",
  [("drive with its hazard warning lights on", "circular con la luz de emergencia"), ("drive with its main beam on", "circular con la luz de carretera"),
   ("sound the horn from time to time", "tocar el claxon de vez en cuando")],
  "The hazard lights warn those coming from behind.", "La luz de emergencia avisa a los que vienen detrás.")
Q("mn8", "minimum", "If an emergency forces you to drive on an autovía at an abnormally low speed, you must…", "Si por una emergencia tienes que circular por una autovía a velocidad anormalmente reducida, debes…",
  [("leave it at the first exit", "abandonarla por la primera salida"), ("stop on the shoulder and wait", "detenerte en el arcén y esperar"), ("carry on in the left lane", "seguir por el carril izquierdo")],
  "Same on autopistas.", "Igual en autopistas.")
Q("mn9", "minimum", "Dense traffic only lets you drive at 40 km/h on an autovía. Are you breaking the minimum-speed rule?", "Un tráfico denso solo te permite ir a 40 km/h por una autovía. ¿Incumples la velocidad mínima?",
  [("No: the traffic conditions justify it", "No: lo justifican las circunstancias del tráfico"), ("Yes, 60 km/h is always compulsory", "Sí, 60 km/h es siempre obligatorio"),
   ("Yes, unless you switch on the hazard lights", "Sí, salvo que lleves la luz de emergencia")],
  "Traffic, vehicle or road conditions can justify going slower.", "Las circunstancias del tráfico, del vehículo o de la vía pueden justificar ir más despacio.")
Q("mn10", "minimum", "Which of these may also drive below the minimum?", "¿Cuáles de estos también pueden circular por debajo de la mínima?",
  [("Special vehicles and vehicles under special-transport rules", "Los vehículos especiales y los vehículos en régimen de transporte especial"), ("Taxis", "Los taxis"),
   ("Any vehicle carrying a V-4 plate", "Cualquier vehículo con señal V-4")],
  "Also cycles and animal-drawn vehicles.", "También los ciclos y los vehículos de tracción animal.")

# ---------------------------------------------------------------- 5.1 slowing down
Q("sl1", "slowing", "Before reducing speed considerably (with no imminent danger), you must first…", "Antes de reducir considerablemente la velocidad (sin peligro inminente), primero debes…",
  [("make sure it is safe for those behind, checking the mirrors", "cerciorarte de que no hay riesgo para los de detrás, mirando los espejos"),
   ("switch on the hazard lights", "encender la luz de emergencia"), ("sound the horn", "tocar el claxon")],
  "Look at the distance and speed of the vehicles behind.", "Hay que observar la distancia y velocidad de los que vienen detrás.")
Q("sl2", "slowing", "How do you warn that you are going to slow down considerably?", "¿Cómo se advierte que se va a reducir considerablemente la velocidad?",
  [("With repeated use of the brake lights, or moving the arm up and down", "Con el empleo reiterado de las luces de frenado o moviendo el brazo de arriba abajo"),
   ("With the left indicator", "Con el intermitente izquierdo"), ("By flashing the headlights", "Con ráfagas de luz")],
  "Whenever possible, in advance.", "Siempre que sea posible, con antelación.")
Q("sl3", "slowing", "The arm signal for slowing down is…", "La señal con el brazo para reducir la velocidad es…",
  [("the arm out, moved up and down in short, quick movements", "el brazo extendido, movido de arriba abajo con movimientos cortos y rápidos"),
   ("the arm raised vertically and held still", "el brazo levantado en vertical y quieto"), ("the arm pointing to the right", "el brazo señalando a la derecha")],
  "It replaces or adds to the brake lights.", "Sustituye o complementa a las luces de frenado.")
Q("sl4", "slowing", "Do you have to warn before braking hard because of an imminent danger?", "¿Hay que advertir antes de frenar fuerte por un peligro inminente?",
  [("No: you warn whenever possible, and imminent danger is the exception", "No: se advierte siempre que sea posible, y el peligro inminente es la excepción"),
   ("Yes, always", "Sí, siempre"), ("Only on motorways", "Solo en autopistas")],
  "In an imminent danger there is no time to check and warn.", "Ante un peligro inminente no hay tiempo para comprobar y avisar.")
Q("sl5", "slowing", "How must you reduce speed?", "¿Cómo se debe reducir la velocidad?",
  [("Smoothly, avoiding sudden braking that could make someone hit you", "Sin brusquedades, para no provocar que te alcancen"), ("As quickly as possible", "Lo más rápido posible"),
   ("By switching off the engine", "Apagando el motor")],
  "The goal is no risk of collision with the vehicles behind.", "El objetivo es que no haya riesgo de colisión con los de detrás.")
Q("sl6", "slowing", "When you check before slowing down, you look at…", "Al comprobar antes de reducir la velocidad, miras…",
  [("the distance and speed of the vehicles behind", "la distancia y velocidad de los vehículos que vienen detrás"), ("the oncoming vehicles", "los vehículos que vienen de frente"),
   ("only your speedometer", "solo el velocímetro")],
  "Using the rear-view mirrors.", "Por los espejos retrovisores.")
