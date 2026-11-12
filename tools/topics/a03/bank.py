# -*- coding: utf-8 -*-
"""Question bank for the interactive Category A1/A2, Topic 3 page (speed). In every question the FIRST option is the
correct one (the page shuffles options when it shows them). Ids must be unique and must not start with "ai"."""

BANK = []


def Q(qid, tag, en, es, opts, why_en, why_es):
    BANK.append({
        "id": qid, "tag": tag,
        "q": {"en": en, "es": es},
        "o": [{"en": a, "es": b} for a, b in opts],
        "why": {"en": why_en, "es": why_es},
    })


def K(*vals):
    """Options that are plain speeds: K(90, 120, 100) -> '90 km/h' ..."""
    return [(f"{v} km/h", f"{v} km/h".replace(".", ",")) for v in vals]


# tag -> section number, names, recap bullets, typical confusion
TAGS = {
    "concepts": dict(sec=1, en="Speed concepts", es="Conceptos de velocidad",
        recap=[("Maximum: the upper limit for your vehicle and road; above it, exceso de velocidad.", "Máxima: límite superior según vehículo y vía; por encima, exceso de velocidad."),
               ("Minimum: the lower limit for your vehicle and road.", "Mínima: límite inferior según vehículo y vía."),
               ("Adequate: adapted to the circumstances, so you can react to anything unexpected.", "Adecuada: adaptada a las circunstancias, para controlar el vehículo ante cualquier imprevisto."),
               ("Velocidad excesiva: too fast for the conditions, even inside the limit.", "Velocidad excesiva: demasiado rápida para las circunstancias, aunque esté dentro del límite.")],
        trap=("Thinking that within the limit your speed is always correct.", "Pensar que dentro del límite la velocidad siempre es correcta.")),
    "outtown": dict(sec=2, en="Limits out of town", es="Límites fuera de poblado",
        recap=[("Motorcycle: 120 (min 60) on autopistas and autovías; 90 (min 45) on the rest.", "Motocicleta: 120 (mín. 60) en autopistas y autovías; 90 (mín. 45) en las demás."),
               ("Three-wheeled vehicle and heavy quadricycle: 70 everywhere (min 60 or 35).", "Vehículo de tres ruedas y cuatriciclo pesado: 70 en todas (mín. 60 o 35)."),
               ("Cycles and mopeds: 45; bicycles only on autovías; mopeds not on vías para automóviles.", "Ciclos y ciclomotores: 45; bicicletas solo en autovías; ciclomotores no por vías para automóviles."),
               ("Separated conventional road: up to 100 for motorcycles if the owner sets it. Unpaved: 30.", "Convencional con separación física: hasta 100 para motos si lo fija el titular. Sin pavimentar: 30.")],
        trap=("Giving a motorcycle 120 on a vía para automóviles.", "Dar 120 a una moto en una vía para automóviles.")),
    "trailer": dict(sec=2, en="Towing a trailer", es="Con remolque",
        recap=[("Motorcycles, three-wheelers and mopeds may tow a trailer.", "Motos, vehículos de tres ruedas y ciclomotores pueden llevar remolque."),
               ("Trailer ≤ 50 % of the towing vehicle’s unladen mass.", "Remolque ≤ 50 % de la masa en vacío del vehículo tractor."),
               ("By day, good visibility, nobody in the trailer.", "De día, con buena visibilidad y sin personas en el remolque."),
               ("Maximum −10 %: motorcycle 108 / 81; moped 40.5.", "Máxima −10 %: moto 108 / 81; ciclomotor 40,5.")],
        trap=("Taking off 10 km/h instead of 10 %.", "Restar 10 km/h en vez del 10 %.")),
    "urban": dict(sec=2, en="Limits in town", es="Límites en poblado",
        recap=[("Single platform: 20. One lane per direction: 30.", "Plataforma única: 20. Único carril por sentido: 30."),
               ("Two or more lanes per direction: 50 (reserved lanes don’t count). Travesía: 50.", "Dos o más carriles por sentido: 50 (los reservados no cuentan). Travesía: 50."),
               ("Urban autopista or autovía: 80 max, 60 min.", "Autopista o autovía urbana: 80 máx., 60 mín."),
               ("Signs may lower them, or raise urban autopistas; travesías only lower; a one-lane street up to 50.", "Se pueden rebajar, o ampliar en autopistas urbanas; travesías solo a la baja; una vía de un carril, hasta 50.")],
        trap=("Thinking every urban street is 50.", "Pensar que todas las calles son de 50.")),
    "why": dict(sec=2, en="Why the limits matter", es="Por qué respetar los límites",
        recap=[("Limits rest on technical criteria: design speed, congestion, demand, environment.", "Los límites se basan en criterios técnicos: velocidad de diseño, congestión, demanda, medio ambiente."),
               ("Design speed: the highest that can be kept safely in good conditions; never exceed it.", "Velocidad de diseño: la máxima que puede mantenerse con seguridad en condiciones favorables; no superarla nunca."),
               ("Conventional roads are more dangerous: two directions together, junctions, no fences.", "Las convencionales son más peligrosas: dos sentidos juntos, intersecciones, sin vallas."),
               ("Pedestrian hit at 50 km/h: about 50 % die (course); at 80, practically all.", "Peatón atropellado a 50 km/h: muere cerca del 50 % (curso); a 80, prácticamente todos.")],
        trap=("Thinking autopistas are more dangerous than conventional roads.", "Pensar que las autopistas son más peligrosas que las convencionales.")),
    "adequate": dict(sec=3, en="Speed suited to the circumstances", es="Velocidad adecuada a las circunstancias",
        recap=[("Respect the limits and also adapt to yourself, the road, the vehicle, the load, the weather and the traffic.", "Respetar los límites y adaptarse además a uno mismo, la vía, el vehículo, la carga, el tiempo y el tráfico."),
               ("You must always be able to stop within your field of vision.", "Siempre hay que poder detenerse dentro del campo de visión."),
               ("Not adapting = inadequate speed; higher than needed = excessive speed.", "No adaptarse = velocidad inadecuada; superior a la necesaria = velocidad excesiva."),
               ("Excessive speed is a main cause of accidents and makes them more often fatal.", "La velocidad excesiva es una de las principales causas de accidente y los hace más mortales.")],
        trap=("Confusing exceso de velocidad with velocidad excesiva.", "Confundir exceso de velocidad con velocidad excesiva.")),
    "moderate": dict(sec=3, en="When to slow down", es="Cuándo moderar la velocidad",
        recap=[("Pedestrians or animals, especially children, elderly or blind people; markets and schools.", "Peatones o animales, sobre todo niños, ancianos o invidentes; mercados y centros docentes."),
               ("Stopped bus (school bus above all); out of town: immobilised vehicles, assistance vehicles, cycles.", "Autobús parado (sobre todo escolar); fuera de poblado: inmovilizados, vehículos de auxilio, ciclos."),
               ("Slippery surface, level crossings, roundabouts, junctions without priority, poor visibility, narrowings.", "Pavimento deslizante, pasos a nivel, glorietas, intersecciones sin prioridad, poca visibilidad, estrechamientos."),
               ("Signed junction with practically nil visibility: ≤ 50. Racing: prohibited unless authorised.", "Intersección señalizada sin visibilidad: ≤ 50. Competiciones: prohibidas salvo autorización.")],
        trap=("Thinking you need to slow down only where there is a sign.", "Pensar que solo hay que moderar donde hay señal.")),
    "minimum": dict(sec=4, en="Minimum speed", es="Velocidad mínima",
        recap=[("Autopistas and autovías: 60 for motor vehicles. Other roads: half the generic maximum.", "Autopistas y autovías: 60 para vehículos a motor. Resto: la mitad de la genérica."),
               ("It applies even with no other traffic.", "Rige aunque no circulen otros vehículos."),
               ("Exceptions: cycles, animal-drawn, special vehicles and transport, circumstances, escorts.", "Excepciones: ciclos, tracción animal, especiales y transporte especial, circunstancias, acompañamiento."),
               ("Can’t reach it with risk of being hit: hazard lights. Emergency on an autopista: first exit.", "Sin alcanzarla y con peligro de alcance: señal de emergencia. Emergencia en autopista: primera salida.")],
        trap=("Thinking the minimum doesn’t apply when the road is empty.", "Pensar que la mínima no rige si la vía está vacía.")),
}

# ---------------------------------------------------------------- concepts
Q("co1", "concepts", "The maximum speed is…", "La velocidad máxima es…",
  [("the upper limit allowed for your vehicle on that road", "el límite superior permitido según el vehículo y la vía"), ("the speed the motorcycle can reach", "la velocidad que puede alcanzar la moto"), ("the speed recommended by the manufacturer", "la velocidad recomendada por el fabricante")],
  "Going above it is speeding.", "Superarla es exceso de velocidad.")
Q("co2", "concepts", "You ride a motorcycle at 100 km/h on an autopista in heavy snow. Your speed is…", "Circulas en moto a 100 km/h por autopista con mucha nieve. Tu velocidad es…",
  [("inadequate and excessive, though within the limit", "inadecuada y excesiva, aunque esté dentro del límite"), ("correct, because it is below 120", "correcta, porque está por debajo de 120"), ("exceso de velocidad", "exceso de velocidad")],
  "Velocidad excesiva can happen inside the limit.", "La velocidad excesiva puede darse dentro del límite.")
Q("co3", "concepts", "The adequate speed is the one that…", "La velocidad adecuada es la que…",
  [("lets you control the vehicle in any unforeseen event", "permite controlar el vehículo ante cualquier imprevisto"), ("is always the road’s maximum", "es siempre la máxima de la vía"), ("lets you arrive on time", "permite llegar a tiempo")],
  "It depends on the circumstances of each moment.", "Depende de las circunstancias de cada momento.")
Q("co4", "concepts", "Riding above the signed limit is called…", "Circular por encima del límite señalizado se llama…",
  [("exceso de velocidad (speeding)", "exceso de velocidad"), ("velocidad excesiva", "velocidad excesiva"), ("velocidad inadecuada", "velocidad inadecuada")],
  "Velocidad excesiva is about the circumstances, not the limit.", "La velocidad excesiva se refiere a las circunstancias, no al límite.")
Q("co5", "concepts", "The minimum speed is…", "La velocidad mínima es…",
  [("the lower limit allowed for your vehicle on that road", "el límite inferior permitido según el vehículo y la vía"), ("the slowest the motorcycle can go upright", "la más lenta a la que la moto se mantiene en equilibrio"), ("always 60 km/h", "siempre 60 km/h")],
  "60 km/h only on autopistas and autovías.", "60 km/h solo en autopistas y autovías.")
Q("co6", "concepts", "Riding below the minimum allowed without a reason is…", "Circular por debajo de la mínima sin motivo es…",
  [("riding at an abnormally low speed", "circular a velocidad anormalmente reducida"), ("adequate speed", "velocidad adecuada"), ("allowed if you keep right", "permitido si vas por la derecha")],
  "It holds up the traffic behind.", "Entorpece a los que vienen detrás.")

# ---------------------------------------------------------------- out of town
Q("ot1", "outtown", "Generic maximum for a motorcycle on an autopista or autovía:", "Velocidad máxima genérica de una motocicleta en autopista o autovía:",
  K(120, 100, 90), "Minimum 60.", "Mínima 60.")
Q("ot2", "outtown", "Generic maximum for a motorcycle on a carretera convencional:", "Velocidad máxima genérica de una motocicleta en carretera convencional:",
  K(90, 100, 80), "Minimum 45.", "Mínima 45.")
Q("ot3", "outtown", "Generic maximum for a motorcycle on a vía para automóviles:", "Velocidad máxima genérica de una motocicleta en una vía para automóviles:",
  K(90, 120, 100), "Same group as conventional roads.", "Mismo grupo que las carreteras convencionales.")
Q("ot4", "outtown", "Generic maximum for a three-wheeled vehicle on an autopista:", "Velocidad máxima genérica de un vehículo de tres ruedas en autopista:",
  K(70, 90, 120), "70 on every road where it may circulate.", "70 en cualquier vía donde pueda circular.")
Q("ot5", "outtown", "Generic maximum for a heavy quadricycle on a carretera convencional:", "Velocidad máxima genérica de un cuatriciclo pesado en carretera convencional:",
  K(70, 90, 45), "Minimum 35, half of 70.", "Mínima 35, la mitad de 70.")
Q("ot6", "outtown", "Generic maximum for a moped on a carretera convencional:", "Velocidad máxima genérica de un ciclomotor en carretera convencional:",
  K(45, 50, 70), "Also for cycles and light quadricycles.", "También para ciclos y cuatriciclos ligeros.")
Q("ot7", "outtown", "May a moped ride on a vía para automóviles?", "¿Puede un ciclomotor circular por una vía para automóviles?",
  [("No", "No"), ("Yes, at 45 km/h", "Sí, a 45 km/h"), ("Yes, on the shoulder", "Sí, por el arcén")],
  "Nor on autopistas or autovías.", "Tampoco por autopistas ni autovías.")
Q("ot8", "outtown", "Which of these may use an autovía, at up to 45 km/h?", "¿Cuál de estos puede circular por una autovía, a 45 km/h como máximo?",
  [("A bicycle, on the shoulder", "Una bicicleta, por el arcén"), ("A moped", "Un ciclomotor"), ("A light quadricycle", "Un cuatriciclo ligero")],
  "Bicycles only, and only on autovías (riders over 14).", "Solo bicicletas y solo en autovías (mayores de 14 años).")
Q("ot9", "outtown", "On a carretera convencional with a physical barrier between the two directions, a motorcycle may ride at up to…", "En una carretera convencional con separación física de los dos sentidos, una moto puede circular hasta…",
  [("100 km/h, if the road owner sets it", "100 km/h, si lo fija el titular de la vía"), ("120 km/h, always", "120 km/h, siempre"), ("90 km/h, never more", "90 km/h, nunca más")],
  "It has to be set and signed.", "Debe fijarse y señalizarse.")
Q("ot10", "outtown", "Maximum speed on an unpaved road:", "Velocidad máxima en una vía sin pavimentar:",
  K(30, 40, 50), "For every vehicle.", "Para todos los vehículos.")
Q("ot11", "outtown", "A three-wheeled vehicle that the rules treat as a motorcycle (asimilado) has, on an autopista, a maximum of…", "Un vehículo de tres ruedas asimilado a las motocicletas tiene en autopista una máxima de…",
  K(120, 70, 90), "The same as a two-wheeled motorcycle.", "La misma que una motocicleta de dos ruedas.")
Q("ot12", "outtown", "When overtaking on a carretera convencional, may you exceed the limit by 20 km/h?", "Al adelantar en una carretera convencional, ¿puedes superar el límite en 20 km/h?",
  [("No, that allowance was removed in 2022", "No, esa posibilidad se suprimió en 2022"), ("Yes, motorcycles and cars", "Sí, motos y turismos"), ("Yes, if the vehicle overtaken is slow", "Sí, si el adelantado va despacio")],
  "The limit is the same while overtaking.", "El límite es el mismo durante el adelantamiento.")
Q("ot13", "outtown", "Out of town, overtaking a cyclist on your motorcycle (since October 2026), you must ride…", "Fuera de poblado, al adelantar en moto a un ciclista (desde octubre de 2026), debes ir…",
  [("at least 20 km/h below the road’s limit", "al menos 20 km/h por debajo del límite de la vía"), ("at the road’s limit", "al límite de la vía"), ("20 km/h above the limit", "20 km/h por encima del límite")],
  "So the cyclist’s stability is not put at risk.", "Para no comprometer la estabilidad del ciclista.")
Q("ot14", "outtown", "Out of town, the generic limit depends on…", "Fuera de poblado, el límite genérico depende…",
  [("the type of vehicle and the type of road", "del tipo de vehículo y del tipo de vía"), ("only the type of road", "solo del tipo de vía"), ("only the engine size", "solo de la cilindrada")],
  "In town it depends on the street.", "En poblado depende de la calle.")

# ---------------------------------------------------------------- trailer
Q("tr1", "trailer", "A motorcycle towing a trailer must…", "Una motocicleta que arrastra un remolque debe…",
  [("reduce its maximum speed by 10 %", "reducir un 10 % su velocidad máxima"), ("reduce its maximum by 10 km/h", "reducir 10 km/h su velocidad máxima"), ("keep the same maximum", "mantener la misma velocidad máxima")],
  "Per cent, not km/h.", "Por ciento, no km/h.")
Q("tr2", "trailer", "A motorcycle with a trailer on an autopista may ride at most at…", "Una moto con remolque en autopista puede circular como máximo a…",
  K(108, 110, 90), "120 minus 10 %.", "120 menos el 10 %.")
Q("tr3", "trailer", "A motorcycle with a trailer on a carretera convencional may ride at most at…", "Una moto con remolque en carretera convencional puede circular como máximo a…",
  K(81, 80, 90), "90 minus 10 %.", "90 menos el 10 %.")
Q("tr4", "trailer", "The trailer of a motorcycle may weigh at most…", "El remolque de una moto puede pesar como máximo…",
  [("50 % of the motorcycle’s unladen mass", "el 50 % de la masa en vacío de la moto"), ("75 % of its MMA", "el 75 % de su MMA"), ("750 kg", "750 kg")],
  "Measured against the towing vehicle.", "Respecto al vehículo tractor.")
Q("tr5", "trailer", "A motorcycle may tow a trailer…", "Una moto puede llevar remolque…",
  [("only by day and with good visibility", "solo de día y con buena visibilidad"), ("at any time, with lights on", "a cualquier hora, con las luces encendidas"), ("only at night", "solo de noche")],
  "Never in reduced visibility.", "Nunca con visibilidad reducida.")
Q("tr6", "trailer", "May a person travel in a motorcycle’s trailer?", "¿Puede viajar una persona en el remolque de una moto?",
  [("No, never", "No, nunca"), ("Yes, a child", "Sí, un niño"), ("Yes, with a helmet", "Sí, con casco")],
  "Never people in the towed vehicle.", "Nunca personas en el vehículo remolcado.")
Q("tr7", "trailer", "Which of these may tow a trailer under the motorcycle rule (−10 %)?", "¿Cuál de estos puede llevar remolque con la norma de las motos (−10 %)?",
  [("A moped", "Un ciclomotor"), ("A VMP", "Un VMP"), ("None: only cars may tow", "Ninguno: solo los turismos")],
  "Motorcycles, three-wheeled vehicles and mopeds.", "Motocicletas, vehículos de tres ruedas y ciclomotores.")
Q("tr8", "trailer", "In town, the rules for a motorcycle with a trailer are set by…", "En poblado, las normas para una moto con remolque las fijan…",
  [("the local bylaws", "las ordenanzas municipales"), ("the DGT, for each street", "la DGT, calle a calle"), ("nobody: trailers are banned in town", "nadie: en poblado están prohibidos")],
  "Out of town: −10 %.", "Fuera de poblado: −10 %.")
Q("tr9", "trailer", "A moped with a trailer may ride at most at…", "Un ciclomotor con remolque puede circular como máximo a…",
  K(40.5, 35, 45), "45 minus 10 %.", "45 menos el 10 %.")

# ---------------------------------------------------------------- urban
Q("ur1", "urban", "In town, a street with one lane per direction has a generic limit of…", "En poblado, una vía de único carril por sentido tiene un límite genérico de…",
  K(30, 50, 20), "Two or more lanes per direction: 50.", "Dos o más carriles por sentido: 50.")
Q("ur2", "urban", "A single-platform street (road and pavement at the same level) has a generic limit of…", "Una vía de plataforma única de calzada y acera tiene un límite genérico de…",
  K(20, 30, 10), "Pedestrians share the space.", "Los peatones comparten el espacio.")
Q("ur3", "urban", "In town, a street with two or more lanes per direction:", "En poblado, una vía de dos o más carriles por sentido:",
  K(50, 30, 60), "Bus and other reserved lanes don’t count.", "Los carriles bus y reservados no se cuentan.")
Q("ur4", "urban", "Generic limit in a travesía:", "Límite genérico en una travesía:",
  K(50, 30, 60), "It can only be lowered.", "Solo puede rebajarse.")
Q("ur5", "urban", "An autopista crossing a town has a generic maximum of…", "Una autopista que discurre dentro de poblado tiene una máxima genérica de…",
  K(80, 120, 50), "Minimum 60.", "Mínima 60.")
Q("ur6", "urban", "Minimum speed on an urban autovía:", "Velocidad mínima en una autovía urbana:",
  K(60, 40, 30), "The usual motorway minimum.", "La mínima habitual de autopistas y autovías.")
Q("ur7", "urban", "A street has one lane per direction plus a bus lane each way. Its generic limit is…", "Una calle tiene un carril por sentido más un carril bus en cada sentido. Su límite genérico es…",
  K(30, 50, 20), "Reserved lanes don’t count.", "Los carriles reservados no se cuentan.")
Q("ur8", "urban", "Exceptionally, the town may raise a one-lane-per-direction street, with signs, to at most…", "Excepcionalmente, el ayuntamiento puede subir una vía de único carril por sentido, con señales, hasta…",
  K(50, 60, 40), "Never above 50.", "Nunca por encima de 50.")
Q("ur9", "urban", "The limit of an urban autopista may be raised by signs, but never…", "El límite de una autopista urbana puede ampliarse con señales, pero nunca…",
  [("above the generic limit for that road out of town", "por encima del límite genérico de esa vía fuera de poblado"), ("above 80 km/h", "por encima de 80 km/h"), ("at night", "de noche")],
  "Nor above the vehicle’s own limit.", "Ni por encima del límite del tipo de vehículo.")
Q("ur10", "urban", "Today, may the 50 km/h limit of a travesía be raised by signs?", "Hoy, ¿puede ampliarse con señales el límite de 50 km/h de una travesía?",
  [("No, it can only be lowered", "No, solo puede rebajarse"), ("Yes, up to 90 km/h", "Sí, hasta 90 km/h"), ("Yes, up to 70 km/h", "Sí, hasta 70 km/h")],
  "Since May 2021. Your course still says it can be raised.", "Desde mayo de 2021. Tu curso dice aún que puede ampliarse.")

# ---------------------------------------------------------------- why
Q("wh1", "why", "The design speed of a road is…", "La velocidad de diseño de una vía es…",
  [("the highest that can be kept safely on that stretch in good conditions", "la máxima que puede mantenerse con seguridad en ese tramo en condiciones favorables"), ("the speed shown on the signs", "la que indican las señales"), ("the average speed of traffic", "la velocidad media del tráfico")],
  "Never exceed it.", "No debe superarse nunca.")
Q("wh2", "why", "According to your course, a pedestrian hit at 50 km/h has a probability of dying close to…", "Según tu curso, un peatón atropellado a 50 km/h tiene una probabilidad de morir próxima al…",
  [("50 %", "50 %"), ("10 %", "10 %"), ("100 %", "100 %")],
  "At 80 km/h practically all die. Recent DGT material gives about 80 % at 50 km/h.", "A 80 km/h mueren prácticamente todos. Material reciente de la DGT da en torno al 80 % a 50 km/h.")
Q("wh3", "why", "A pedestrian hit at 80 km/h…", "Un peatón atropellado a 80 km/h…",
  [("practically always dies", "prácticamente siempre muere"), ("usually survives", "normalmente sobrevive"), ("has a 50 % chance", "tiene un 50 % de probabilidad")],
  "Every source agrees.", "Todas las fuentes coinciden.")
Q("wh4", "why", "Which roads are more dangerous?", "¿Qué vías son más peligrosas?",
  [("Carreteras convencionales", "Las carreteras convencionales"), ("Autopistas", "Las autopistas"), ("Autovías", "Las autovías")],
  "Two directions together, junctions, no fences.", "Dos sentidos juntos, intersecciones y sin vallas.")
Q("wh5", "why", "Why must you watch for animals and pedestrians on a carretera convencional?", "¿Por qué hay que vigilar a peatones y animales en una carretera convencional?",
  [("Because it is not fenced", "Porque no está vallada"), ("Because it has a hard shoulder", "Porque tiene arcén"), ("Because it is lit", "Porque está iluminada")],
  "Someone may cross at any moment.", "Pueden cruzar en cualquier momento.")
Q("wh6", "why", "As speed increases…", "A mayor velocidad…",
  [("the motorcycle is harder to control and needs more metres to stop", "es más difícil controlar la moto y se recorren más metros antes de detenerla"), ("the stopping distance stays the same", "la distancia de detención es la misma"), ("injuries are less serious", "las lesiones son menos graves")],
  "Above 120 km/h crashes are usually fatal.", "A más de 120 km/h los accidentes suelen ser mortales.")
Q("wh7", "why", "Generic limits are set using…", "Los límites genéricos se fijan según…",
  [("technical criteria such as design speed, congestion and traffic demand", "criterios técnicos como la velocidad de diseño, la congestión y la demanda de tráfico"), ("the average speed of drivers", "la velocidad media de los conductores"), ("the most powerful vehicles", "los vehículos más potentes")],
  "Their aim is safety and flow.", "Su objetivo es la seguridad y la fluidez.")

# ---------------------------------------------------------------- adequate
Q("ad1", "adequate", "Besides respecting the limits, to adapt your speed you must take into account…", "Además de respetar los límites, para adecuar la velocidad debes tener en cuenta…",
  [("your physical and mental state, the road, the vehicle, the load, the weather and the traffic", "tus condiciones físicas y psíquicas, la vía, el vehículo, la carga, el tiempo y el tráfico"), ("only the weather", "solo el tiempo"), ("only the signs", "solo las señales")],
  "Every circumstance at that moment.", "Todas las circunstancias del momento.")
Q("ad2", "adequate", "Your speed must let you always…", "Tu velocidad debe permitirte siempre…",
  [("stop within your field of vision", "detenerte dentro de los límites de tu campo de visión"), ("overtake whoever is in front", "adelantar a quien vaya delante"), ("keep up with the traffic", "seguir el ritmo del tráfico")],
  "And before any obstacle.", "Y ante cualquier obstáculo.")
Q("ad3", "adequate", "Riding faster than the circumstances require is called…", "Circular más rápido de lo que exigen las circunstancias se llama…",
  [("velocidad excesiva", "velocidad excesiva"), ("exceso de velocidad", "exceso de velocidad"), ("velocidad de diseño", "velocidad de diseño")],
  "It can happen inside the limit.", "Puede darse dentro del límite.")
Q("ad4", "adequate", "Excessive speed…", "La velocidad excesiva…",
  [("is one of the main causes of accidents", "es una de las principales causas de accidente"), ("only matters on autopistas", "solo importa en autopistas"), ("is not an offence if under the limit", "no es infracción si se va por debajo del límite")],
  "And it makes a crash more likely to be fatal.", "Y aumenta la probabilidad de que el accidente sea mortal.")
Q("ad5", "adequate", "You are very tired. Your adequate speed…", "Estás muy cansado. Tu velocidad adecuada…",
  [("is lower than usual", "es inferior a la habitual"), ("is the road’s limit", "es el límite de la vía"), ("doesn’t change", "no cambia")],
  "Your physical state counts.", "Cuentan tus condiciones físicas.")

# ---------------------------------------------------------------- moderate
Q("md1", "moderate", "You must moderate your speed near…", "Debes moderar la velocidad cerca de…",
  [("markets, schools and places where children are likely", "mercados, centros docentes y lugares con presencia previsible de niños"), ("petrol stations only", "solo gasolineras"), ("industrial estates", "polígonos industriales")],
  "Children may step onto the road.", "Los niños pueden irrumpir en la vía.")
Q("md2", "moderate", "You approach a stopped school bus. You…", "Te acercas a un autobús escolar parado. Tú…",
  [("moderate your speed and stop if necessary", "moderas la velocidad y te detienes si es preciso"), ("sound the horn and keep your speed", "tocas el claxon y mantienes la velocidad"), ("overtake it quickly", "lo adelantas rápidamente")],
  "Children may cross in front of it.", "Pueden cruzar niños por delante.")
Q("md3", "moderate", "At a properly signed junction with practically nil visibility, your speed may not exceed…", "En una intersección debidamente señalizada con visibilidad prácticamente nula, tu velocidad no debe exceder de…",
  K(50, 30, 70), "And less if the circumstances require it.", "Y menos si lo exigen las circunstancias.")
Q("md4", "moderate", "Out of town, you approach a broken-down vehicle on the carriageway. You must…", "Fuera de poblado te acercas a un vehículo averiado en la calzada. Debes…",
  [("moderate your speed", "moderar la velocidad"), ("keep your speed: it is stopped", "mantener la velocidad: está parado"), ("speed up to pass it quickly", "acelerar para rebasarlo rápido")],
  "Also near assistance vehicles at work and cycles.", "También ante vehículos de auxilio prestando servicio y ciclos.")
Q("md5", "moderate", "Riding through a puddle next to people waiting at a bus stop, you must…", "Al pasar por un charco junto a personas en una parada de autobús, debes…",
  [("slow down so as not to splash them", "moderar la velocidad para no salpicarlas"), ("keep your speed", "mantener la velocidad"), ("sound the horn", "tocar el claxon")],
  "Also with gravel or other material.", "También con gravilla u otras materias.")
Q("md6", "moderate", "Which of these is a place where you must moderate your speed?", "¿En cuál de estos lugares debes moderar la velocidad?",
  [("A roundabout", "Una glorieta"), ("A straight autovía with light traffic", "Una autovía recta con poco tráfico"), ("An acceleration lane", "Un carril de aceleración")],
  "Also level crossings and junctions without priority.", "También pasos a nivel e intersecciones sin prioridad.")
Q("md7", "moderate", "In dense fog, heavy rain or snowfall you must…", "Con niebla densa, lluvia intensa o nevada debes…",
  [("moderate your speed and stop if necessary", "moderar la velocidad y detenerte si es preciso"), ("ride at the minimum of the road", "circular a la mínima de la vía"), ("keep the generic limit", "mantener el límite genérico")],
  "Also in clouds of dust or smoke.", "También con nubes de polvo o humo.")
Q("md8", "moderate", "You are dazzled by an oncoming vehicle. You…", "Te deslumbra un vehículo que viene de frente. Tú…",
  [("slow down, even to a stop, to avoid hitting anyone ahead", "reduces la velocidad, incluso hasta detenerte, para no alcanzar a nadie"), ("keep your speed and look at the centre line", "mantienes la velocidad y miras a la línea central"), ("speed up to get past it", "aceleras para dejarlo atrás")],
  "Dazzle is one of the cases for moderating speed.", "El deslumbramiento es uno de los casos de moderar la velocidad.")
Q("md9", "moderate", "Speed races on public roads are…", "Las competiciones de velocidad en vías públicas están…",
  [("prohibited unless authorised and the area is closed off for them", "prohibidas salvo que se autoricen y se acondicione la zona"), ("allowed at night", "permitidas de noche"), ("allowed on empty autopistas", "permitidas en autopistas vacías")],
  "A very serious offence.", "Infracción muy grave.")
Q("md10", "moderate", "You approach a pedestrian crossing without traffic lights or agents. You…", "Te acercas a un paso de peatones sin semáforo ni agentes. Tú…",
  [("moderate your speed", "moderas la velocidad"), ("keep your speed if nobody is crossing", "mantienes la velocidad si nadie cruza"), ("sound the horn", "tocas el claxon")],
  "Pedestrians may appear.", "Pueden aparecer peatones.")

# ---------------------------------------------------------------- minimum
Q("mn1", "minimum", "Minimum speed for a motorcycle on an autopista or autovía:", "Velocidad mínima de una motocicleta en autopista o autovía:",
  K(60, 45, 50), "For every motor vehicle.", "Para todos los vehículos a motor.")
Q("mn2", "minimum", "Minimum speed for a motorcycle on a carretera convencional:", "Velocidad mínima de una motocicleta en carretera convencional:",
  K(45, 60, 30), "Half of 90.", "La mitad de 90.")
Q("mn3", "minimum", "Minimum speed for a three-wheeled vehicle on a carretera convencional:", "Velocidad mínima de un vehículo de tres ruedas en carretera convencional:",
  K(35, 45, 60), "Half of 70.", "La mitad de 70.")
Q("mn4", "minimum", "The road is empty. Does the minimum speed still apply?", "La vía está vacía. ¿Rige la velocidad mínima?",
  [("Yes, even with no other traffic", "Sí, aunque no circulen otros vehículos"), ("No, only with traffic behind", "No, solo con tráfico detrás"), ("Only on autopistas", "Solo en autopistas")],
  "Unless the circumstances make it unsafe.", "Salvo que las circunstancias lo hagan peligroso.")
Q("mn5", "minimum", "Who may ride below the minimum speed?", "¿Quién puede circular por debajo de la velocidad mínima?",
  [("Cycles and animal-drawn vehicles", "Los ciclos y los vehículos de tracción animal"), ("Motorcycles in town", "Las motos en poblado"), ("Nobody", "Nadie")],
  "Also special vehicles, special transport and escort vehicles.", "También vehículos especiales, transporte especial y acompañamiento.")
Q("mn6", "minimum", "Your motorcycle can’t reach the minimum and there is a risk of being hit from behind. You…", "Tu moto no alcanza la mínima y hay peligro de alcance. Tú…",
  [("ride with the hazard warning lights on", "circulas con la señal de emergencia"), ("ride on the left lane", "vas por el carril izquierdo"), ("sound the horn", "tocas el claxon")],
  "Luz o señal de emergencia.", "Luz o señal de emergencia.")
Q("mn7", "minimum", "An emergency forces you to ride on an autovía at an abnormally low speed. You must…", "Una emergencia te obliga a circular por una autovía a velocidad anormalmente reducida. Debes…",
  [("leave it at the first exit", "abandonarla por la primera salida"), ("carry on to your destination on the shoulder", "seguir hasta tu destino por el arcén"), ("stop in the left lane", "detenerte en el carril izquierdo")],
  "With the hazard lights if there is a risk of being hit.", "Con la señal de emergencia si hay peligro de alcance.")
Q("mn8", "minimum", "Heavy traffic prevents you from going above 40 km/h on an autopista. Are you committing an offence?", "El tráfico denso te impide superar 40 km/h en autopista. ¿Cometes infracción?",
  [("No: the traffic circumstances allow it", "No: lo permiten las circunstancias del tráfico"), ("Yes: the minimum is 60", "Sí: la mínima es 60"), ("Yes, unless you use the shoulder", "Sí, salvo que uses el arcén")],
  "The minimum gives way to safety.", "La mínima cede ante la seguridad.")
Q("mn9", "minimum", "Minimum speed on other roads (not autopistas or autovías):", "Velocidad mínima en las demás vías (no autopistas ni autovías):",
  [("half the generic maximum for that vehicle", "la mitad de la máxima genérica de ese vehículo"), ("always 40 km/h", "siempre 40 km/h"), ("there is none", "no hay")],
  "Motorcycle: 45; three-wheeler: 35.", "Moto: 45; tres ruedas: 35.")
