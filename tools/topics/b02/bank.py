# -*- coding: utf-8 -*-
"""Question bank for the interactive Topic 2 page (use of the road). In every question the FIRST option is the
correct one (the page shuffles options when it shows them). Ids must be unique and must not start with "ai"."""

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
    "duties": dict(sec=1, en="Principles and driver duties", es="Principios y obligaciones del conductor",
        recap=[("Four principles: do not annoy, do not surprise, warn, understand. Warning does not give you the right to manoeuvre.",
                "Cuatro principios: no molestar, no sorprender, advertir y comprender. Advertir no da derecho a realizar la maniobra."),
               ("Drive with care and caution; negligent or reckless driving is strictly forbidden.",
                "Conducir con diligencia y precaución; está prohibido conducir de modo negligente o temerario."),
               ("Take extra care near children, elderly people, blind people and people with reduced mobility.",
                "Extremar la precaución con niños, ancianos, invidentes y personas con movilidad reducida."),
               ("Keep freedom of movement, field of vision and permanent attention; passengers, objects and animals well placed.",
                "Mantener libertad de movimientos, campo de visión y atención permanente; pasajeros, objetos y animales bien colocados.")],
        trap=("Believing that once you have signalled, the manoeuvre is yours by right.",
              "Creer que, una vez señalizada, la maniobra es tuya por derecho.")),
    "bans": dict(sec=1, en="Phones, screens and other prohibitions", es="Móvil, pantallas y otras prohibiciones",
        recap=[("Holding a phone while driving is an offence even if you do not use it. Only hands-free, without headphones.",
                "Sujetar el móvil conduciendo es infracción aunque no se use. Solo manos libres, sin cascos ni auriculares."),
               ("Headphones are forbidden; certified intercoms built into a motorcycle helmet are allowed.",
                "Los auriculares están prohibidos; los intercomunicadores homologados integrados en el casco de moto, permitidos."),
               ("Allowed screens: parking camera, GPS (not handled while moving), passenger-boarding monitors. Not internet, TV or DVD.",
                "Pantallas permitidas: cámara de maniobra, GPS (sin manipularlo en marcha) y monitores de subida y bajada. No internet, TV ni DVD."),
               ("Radar jammers and detectors are forbidden; warning devices are allowed. Refuel with engine, lights, radio and phone off.",
                "Inhibidores y detectores de radar prohibidos; avisadores permitidos. Se reposta con motor, luces, radio y móvil apagados.")],
        trap=("Mixing up radar warning devices (legal) with detectors (illegal).",
              "Confundir los avisadores de radar (legales) con los detectores (ilegales).")),
    "parts": dict(sec=2, en="Parts and elements of the road", es="Partes y elementos de la vía",
        recap=[("Plataforma = calzada + arcenes. Calzada = the part for vehicles. Carril = room for one line of cars (not motorcycles).",
                "Plataforma = calzada + arcenes. Calzada = parte para vehículos. Carril = una fila de automóviles que no sean motos."),
               ("Mediana = strip between two separate plataformas. Arcén = next to the calzada, not for motor vehicles.",
                "Mediana = franja entre dos plataformas separadas. Arcén = contiguo a la calzada, no para automóviles."),
               ("Refugio = pedestrian zone on the calzada. Isleta = channels traffic. Apartadero = widening to stop.",
                "Refugio = zona peatonal en la calzada. Isleta = canaliza el tráfico. Apartadero = ensanchamiento para detenerse."),
               ("Intersección = paths cross at the same level. Glorieta = ring around a central island.",
                "Intersección = las trayectorias se cruzan a nivel. Glorieta = anillo alrededor de una isleta central.")],
        trap=("Swapping plataforma and calzada, or refugio and isleta.", "Intercambiar plataforma y calzada, o refugio e isleta.")),
    "cycleways": dict(sec=2, en="Cycle infrastructure", es="Vías ciclistas",
        recap=[("Carril bici = alongside the carriageway; protegido = physically separated.",
                "Carril bici = adosado a la calzada; protegido = separado físicamente."),
               ("Acera bici = on the pavement. Pista bici = segregated, on its own route.",
                "Acera bici = sobre la acera. Pista bici = segregada, con trazado independiente."),
               ("Senda ciclable = shared by pedestrians and cycles through parks and open spaces.",
                "Senda ciclable = compartida por peatones y ciclos, por parques y espacios abiertos."),
               ("Other vehicles need the authority’s permission and signs.", "Otros vehículos necesitan autorización y señalización.")],
        trap=("Confusing pista bici (own route) with carril bici (next to the carriageway).",
              "Confundir pista bici (trazado propio) con carril bici (junto a la calzada).")),
    "types": dict(sec=3, en="Types of road", es="Tipos de vía",
        recap=[("Carretera = paved public road outside towns, except travesías. Travesía = a carretera through a town.",
                "Carretera = vía pública pavimentada fuera de poblado, salvo travesías. Travesía = carretera que cruza un poblado."),
               ("Autopista: automobiles only, no access, no level crossings. Autovía: limited access, no level crossings.",
                "Autopista: solo automóviles, sin accesos, sin cruces a nivel. Autovía: accesos limitados, sin cruces a nivel."),
               ("Motorways and dual carriageways: automobiles able to exceed 60 km/h on the flat. No pedestrians, cycles, mopeds, VMP or animals.",
                "Autopistas y autovías: automóviles que superen 60 km/h en llano. Sin peatones, ciclos, ciclomotores, VMP ni animales."),
               ("Cyclists over 14 may ride on the shoulder of an autovía.", "Los ciclistas mayores de 14 años pueden circular por el arcén de la autovía.")],
        trap=("Autopista vs autovía: “no access” vs “limited access”.", "Autopista frente a autovía: «sin accesos» frente a «accesos limitados».")),
    "lanes": dict(sec=4, en="Which lane to use", es="Utilización de carriles",
        recap=[("Two-way, two lanes: right lane. Two-way, three lanes (broken lines): right; centre only to overtake or turn left; left never.",
                "Doble sentido, dos carriles: el derecho. Tres carriles (discontinuas): el derecho; central solo para adelantar o girar a la izquierda; izquierdo nunca."),
               ("One way, out of town: rightmost lane, the rest to overtake.", "Sentido único, interurbana: el de más a la derecha; el resto para adelantar."),
               ("3+ lanes out of town: trucks, vans and specials over 3,500 kg and combinations over 7 m: right lane and, exceptionally, the next one.",
                "3 o más carriles en interurbana: camiones, furgones y especiales de más de 3.500 kg y conjuntos de más de 7 m: el derecho y excepcionalmente el contiguo."),
               ("In town: marked lanes → best for your destination; unmarked → right lane. Not on an autopista or autovía through the town.",
                "En poblado: carriles delimitados → el que convenga al destino; sin delimitar → el derecho. No en autopistas o autovías urbanas.")],
        trap=("Using the left lane on a two-way three-lane road, or 10 m instead of 7 m for combinations.",
              "Usar el carril izquierdo en doble sentido con tres carriles, o 10 m en lugar de 7 m para los conjuntos.")),
    "position": dict(sec=5, en="Islands, roundabouts and carriageways", es="Isletas, glorietas y calzadas",
        recap=[("Islands separating two directions: pass on their right. On one-way roads: either side.",
                "Isletas que separan dos sentidos: por su derecha. En sentido único: por cualquier lado."),
               ("Squares, roundabouts and junctions: centre on your left.", "Plazas, glorietas e intersecciones: el centro a la izquierda."),
               ("Interurban roundabout with 2+ lanes: the outer (right) lane. Urban: the lane that suits your destination.",
                "Glorieta interurbana con 2 o más carriles: el más próximo a la derecha. Urbana: el que convenga al destino."),
               ("Two carriageways: the right one. Three: centre one or two directions, sides one direction.",
                "Dos calzadas: la de la derecha. Tres: la central de uno o dos sentidos, las laterales de uno.")],
        trap=("Thinking the inner lane of an interurban roundabout is the normal one.",
              "Creer que el carril interior de una glorieta interurbana es el normal.")),
    "reserved": dict(sec=6, en="Reserved lanes and lane counting", es="Carriles reservados y cómputo de carriles",
        recap=[("Minimum-speed lane: only for vehicles at or above the signed speed; it counts as a lane.",
                "Carril de velocidad mínima: solo para quien circula a esa velocidad o más; sí se computa."),
               ("Bus lane: buses (and taxis if signed). Others cross only at broken stretches, never to stop, park, turn round or overtake.",
                "Carril bus: autobuses (y taxis si se indica). Los demás lo cruzan solo en tramos discontinuos, nunca para parar, estacionar, cambiar de sentido o adelantar."),
               ("VAO: MMA ≤ 3,500 kg, usually ≥ 2 occupants incl. driver. Motorcycles, taxis and buses always; labelled cars only when the panels allow it.",
                "VAO: MMA ≤ 3.500 kg, normalmente ≥ 2 ocupantes con el conductor. Motos, taxis y autobuses siempre; turismos con distintivo solo si lo permiten los paneles."),
               ("Not counted: bus, bike, acceleration, deceleration and waiting lanes.",
                "No se computan: bus, bici, aceleración, deceleración y espera.")],
        trap=("Thinking minimum-speed lanes do not count, or slowing down on the main carriageway before an exit.",
              "Creer que los carriles de velocidad mínima no cuentan, o frenar en la calzada principal antes de la salida.")),
    "flow": dict(sec=6, en="Flow lanes, emergency corridor and snow", es="Carriles de fluidez, carril de emergencia y nieve",
        recap=[("Reversible: double broken lines on both sides; dipped headlights day and night.",
                "Reversible: dobles líneas discontinuas a ambos lados; luz de cruce de día y de noche."),
               ("Additional and contraflow lanes: dipped headlights and 60–80 km/h.", "Adicional circunstancial y sentido contrario: luz de cruce y 60–80 km/h."),
               ("Contraflow for traffic flow: only motorcycles and cars without trailer. For roadworks: all vehicles allowed on the road.",
                "Sentido contrario por fluidez: solo motos y turismos sin remolque. Por obras: todos los autorizados."),
               ("Emergency corridor: 2 lanes → centre; 3+ → between the left lane and the next. Snow: no overtaking, right lane.",
                "Carril de emergencia: 2 carriles → centro; 3 o más → entre el izquierdo y su contiguo. Nieve: no adelantar, carril derecho.")],
        trap=("Putting the emergency corridor in the middle of a three-lane road.", "Abrir el carril de emergencia en el centro de una vía de tres carriles.")),
    "shoulder": dict(sec=7, en="Driving on the hard shoulder", es="Circulación por el arcén",
        recap=[("Must use the shoulder: cycles, mopeds, reduced-mobility vehicles, animal-drawn vehicles, special vehicles ≤ 3,500 kg, vehicles escorting cyclists.",
                "Obligados al arcén: ciclos, ciclomotores, vehículos de movilidad reducida, de tracción animal, especiales ≤ 3.500 kg y vehículos que siguen a ciclistas."),
               ("Bicycles may ride two abreast; single file without visibility or when bunched. On long descents with bends they may use the carriageway, not on autovías.",
                "Las bicis pueden ir en columna de a dos; en hilera sin visibilidad o con aglomeraciones. En descensos con curvas pueden usar la calzada, salvo en autovía."),
               ("The others may not overtake each other if side by side more than 15 s or 200 m.",
                "Los demás no pueden adelantarse si la marcha en paralelo supera 15 s o 200 m."),
               ("Breakdown (≤ 3,500 kg): to the first exit by the right shoulder. Service vehicles and motorcycles in jams: ≤ 30 km/h.",
                "Avería (≤ 3.500 kg): a la primera salida por el arcén derecho. Vehículos de servicio y motos en atascos: ≤ 30 km/h.")],
        trap=("Applying the 15 s / 200 m rule to bicycles.", "Aplicar la regla de 15 s / 200 m a las bicicletas.")),
    "distance": dict(sec=8, en="Safety distance", es="Distancia de seguridad",
        recap=[("Leave room to stop without hitting the vehicle in front; if you are not signalling to overtake, also room to be overtaken.",
                "Espacio para detenerse sin chocar; si no se señaliza el adelantamiento, también para que nos adelanten."),
               ("Out of town, MMA over 3,500 kg or over 10 m long: at least 50 m.", "Fuera de poblado, MMA de más de 3.500 kg o más de 10 m: al menos 50 m."),
               ("No 50 m in town, where overtaking is forbidden, with more than one lane, in saturated traffic or when about to overtake.",
                "No hacen falta 50 m en poblado, donde se prohíbe adelantar, con más de un carril, con tráfico saturado o al ir a adelantar."),
               ("Chevrons: at least two (sign R-300). Tunnels: 100 m or 4 s; over 3,500 kg 150 m or 6 s.",
                "Galones: al menos dos (señal R-300). Túneles: 100 m o 4 s; más de 3.500 kg, 150 m o 6 s.")],
        trap=("Using 7 m for the 50 m rule: it is 10 m.", "Usar 7 m para la regla de los 50 m: son 10 m.")),
    "saturated": dict(sec=9, en="Congested roads", es="Vías saturadas",
        recap=[("Saturated = vehicles fill every lane.", "Saturada = los vehículos ocupan todos los carriles."),
               ("Going faster in the right lane is not overtaking.", "Ir más rápido por el carril derecho no es adelantar."),
               ("No lane changes except to turn, leave or take a direction; never use the shoulder, not even for the next exit.",
                "No cambiar de carril salvo para girar, salir o tomar una dirección; nunca usar el arcén, ni para la salida más próxima."),
               ("Colours: white > 90 %, green 75–90 %, yellow 25–75 %, red < 25 %, black = closed.",
                "Colores: blanco > 90 %, verde 75–90 %, amarillo 25–75 %, rojo < 25 %, negro = cortada.")],
        trap=("Mixing up green (conditioned) and yellow (discontinuous).", "Confundir verde (condicionada) con amarillo (discontinua).")),
    "peds": dict(sec=10, en="Pedestrians", es="Peatones",
        recap=[("No usable pedestrian zone: left shoulder, facing the traffic, in single file.",
                "Sin zona peatonal practicable: por el arcén izquierdo, de cara al tráfico, en fila."),
               ("On the right: pushing a cycle, moped or VMP; groups led by one person; safety reasons.",
                "Por la derecha: quien empuja un ciclo, ciclomotor o VMP; grupos dirigidos por una persona; razones de seguridad."),
               ("Cross at crossings, at right angles, without stopping. Never across the carriageway of a roundabout.",
                "Cruzar por los pasos, perpendicularmente y sin detenerse. Nunca por la calzada de una glorieta."),
               ("Motorways: only in emergencies; no hitch-hiking. At night out of town: reflective item visible at 150 m.",
                "Autopistas: solo en emergencias; prohibido el autostop. De noche fuera de poblado: elemento reflectante visible a 150 m.")],
        trap=("Forgetting that pushing a bicycle moves you to the right-hand side.", "Olvidar que empujar una bicicleta te lleva al lado derecho.")),
    "animals": dict(sec=11, en="Animals on the road", es="Animales en la vía",
        recap=[("Only when there is no usable livestock track; always with a keeper over 18.",
                "Solo si no hay vía pecuaria practicable; siempre con un conductor mayor de 18 años."),
               ("Right-hand shoulder; one single animal may go on the left for safety.", "Por el arcén derecho; un solo animal puede ir por la izquierda por seguridad."),
               ("Herds at walking pace, never more than the right half of the carriageway.", "Rebaños al paso, nunca más de la mitad derecha de la calzada."),
               ("Never on motorways or dual carriageways; give way to vehicles at narrow points; at night white or yellow light in front, red behind.",
                "Nunca por autopistas o autovías; ceden el paso a los vehículos en estrechamientos; de noche, luz blanca o amarilla delante y roja detrás.")],
        trap=("Thinking a 16-year-old may lead a herd, or that a herd may use the whole road when it is empty.",
              "Creer que un menor de 16 años puede conducir un rebaño, o que puede ocupar toda la calzada si está vacía.")),
}

# ---------------------------------------------------------------- 1. principles and duties
Q("du1", "duties", "Signalling a manoeuvre in good time…", "Señalizar una maniobra con antelación…",
  [("does not give you the right to make it if it is not safe", "no da derecho a realizarla si no es segura"),
   ("gives you priority over the other road users", "da prioridad sobre los demás usuarios"),
   ("makes the manoeuvre legal in every case", "hace que la maniobra sea legal en todo caso")],
  "Warning is a duty, not a right: the manoeuvre still has to be done correctly and without danger.",
  "Advertir es una obligación, no un derecho: la maniobra hay que hacerla correctamente y sin peligro.")
Q("du2", "duties", "Driving recklessly (<i>de modo temerario</i>) is…", "Conducir de modo temerario está…",
  [("strictly forbidden", "terminantemente prohibido"), ("allowed on empty roads", "permitido en vías vacías"), ("only an offence in town", "prohibido solo en poblado")],
  "The law forbids negligent or reckless driving everywhere.", "La ley prohíbe conducir de modo negligente o temerario en cualquier vía.")
Q("du3", "duties", "When approaching other road users, the law asks for extra care especially with…",
  "Al aproximarse a otros usuarios, la ley exige extremar la precaución especialmente con…",
  [("children, elderly people, blind people and people with reduced mobility", "niños, ancianos, invidentes y personas con movilidad reducida"),
   ("drivers of heavy vehicles", "conductores de vehículos pesados"), ("other car drivers", "otros conductores de turismos")],
  "These are the vulnerable users the law names.", "Son los usuarios vulnerables que cita la norma.")
Q("du4", "duties", "The principle “understand” (<i>comprender</i>) means…", "El principio de «comprender» significa…",
  [("forgiving other people’s mistakes without using them to excuse your own or to turn aggressive", "disculpar los errores ajenos sin usarlos para justificar los propios ni para ponerse agresivo"),
   ("always giving way to everyone", "ceder siempre el paso a todos"), ("knowing how your engine works", "saber cómo funciona el motor")],
  "Understand others’ warnings and mistakes; never copy them or answer aggressively.", "Comprender las advertencias y errores de los demás, sin imitarlos ni responder con agresividad.")

# ---------------------------------------------------------------- 1. prohibitions
Q("bn1", "bans", "Is it an offence to drive holding your mobile phone in your hand, even if you are not using it?",
  "¿Es infracción conducir sujetando el móvil con la mano, aunque no se esté usando?",
  [("Yes", "Sí"), ("No, only if you are talking", "No, solo si se está hablando"), ("Only in town", "Solo en poblado")],
  "Even holding it without using it is forbidden.", "Está prohibido incluso sujetarlo con la mano aunque no se utilice.")
Q("bn2", "bans", "May you use a mobile phone while driving?", "¿Se puede usar el móvil mientras se conduce?",
  [("Only without using your hands and without headsets or earphones", "Solo sin emplear las manos y sin cascos ni auriculares"),
   ("Yes, with a single earphone", "Sí, con un solo auricular"), ("Yes, if you hold it only for a moment", "Sí, si se sujeta solo un momento")],
  "Hands-free only, and no headsets, earphones or similar.", "Solo manos libres y sin cascos, auriculares ni similares.")
Q("bn3", "bans", "Which screen may be used while the vehicle is moving?", "¿Qué pantalla se puede usar con el vehículo en movimiento?",
  [("A rear-view parking camera", "Una cámara de maniobra trasera"), ("A DVD player in the driver’s view", "Un reproductor de DVD a la vista del conductor"),
   ("A screen with internet access", "Una pantalla con acceso a internet")],
  "Parking cameras, GPS and passenger-boarding monitors are the exceptions.", "Las excepciones son las cámaras de maniobra, el GPS y los monitores de subida y bajada de pasajeros.")
Q("bn4", "bans", "The GPS navigator…", "El navegador GPS…",
  [("is allowed, but must not be handled while the vehicle is moving", "está permitido, pero no se puede manipular con el vehículo en movimiento"),
   ("is forbidden", "está prohibido"), ("may be handled freely", "se puede manipular libremente")],
  "GPS is allowed; touching it while moving is not.", "El GPS está permitido; manipularlo en marcha, no.")
Q("bn5", "bans", "A motorcyclist may ride using…", "Un motorista puede circular usando…",
  [("a certified wireless intercom built into the helmet, for communication or navigation", "un dispositivo inalámbrico homologado integrado en el casco, para comunicación o navegación"),
   ("earphones under the helmet to listen to music", "auriculares bajo el casco para escuchar música"),
   ("a phone held between the helmet and the shoulder", "el móvil sujeto entre el casco y el hombro")],
  "Certified helmet devices are the one exception to the headphone ban, if they do not affect safety.",
  "Los dispositivos homologados del casco son la excepción a la prohibición de auriculares, si no afectan a la seguridad.")
Q("bn6", "bans", "Which device is allowed in the vehicle?", "¿Qué dispositivo está permitido en el vehículo?",
  [("One that warns where the traffic surveillance points are", "Uno que avisa de dónde están los sistemas de vigilancia"),
   ("A radar detector", "Un detector de radares"), ("A radar jammer (<i>inhibidor</i>)", "Un inhibidor de radares")],
  "Warning devices are legal; detectors and jammers are not.", "Los avisadores son legales; los detectores e inhibidores, no.")
Q("bn7", "bans", "When refuelling you must…", "Al repostar combustible hay que…",
  [("stop the engine and switch off the lights, the radio and the mobile phone", "parar el motor y apagar las luces, la radio y el móvil"),
   ("keep the engine running if it is cold", "mantener el motor en marcha si está frío"), ("only switch off the engine", "solo apagar el motor")],
  "Engine stopped, ignition off, lights off, electrical systems such as the radio off, and phones off.",
  "Motor parado, contacto cortado, luces apagadas, sistemas eléctricos como la radio y móviles apagados.")
Q("bn8", "bans", "May you fit approved tinted films on the rear windows?", "¿Se pueden poner láminas adhesivas reglamentarias en las ventanillas posteriores?",
  [("Yes, if the vehicle has two exterior mirrors", "Sí, si el vehículo lleva dos espejos retrovisores exteriores"),
   ("No, never", "No, nunca"), ("Yes, and also on the windscreen", "Sí, y también en el parabrisas")],
  "Films or sun blinds are allowed only on the rear windows, and only with two exterior mirrors.",
  "Las láminas o cortinillas solo se permiten en las ventanillas posteriores y con dos espejos exteriores.")

# ---------------------------------------------------------------- 2. parts of the road
Q("pt1", "parts", "The road platform (<i>plataforma</i>) is made up of…", "La plataforma está formada por…",
  [("the carriageway and the hard shoulders", "la calzada y los arcenes"), ("the carriageway only", "solo la calzada"),
   ("the carriageway, the shoulders and the median", "la calzada, los arcenes y la mediana")],
  "Plataforma = calzada + arcenes. The median lies between two plataformas.", "Plataforma = calzada + arcenes. La mediana está entre dos plataformas.")
Q("pt2", "parts", "The part of the road intended for vehicles is the…", "La parte de la vía destinada a la circulación de vehículos es la…",
  [("carriageway (<i>calzada</i>)", "calzada"), ("road platform (<i>plataforma</i>)", "plataforma"), ("hard shoulder (<i>arcén</i>)", "arcén")],
  "The calzada is for vehicles; the arcén is not, except in exceptional cases.", "La calzada es para vehículos; el arcén no, salvo casos excepcionales.")
Q("pt3", "parts", "A lane (<i>carril</i>) is wide enough for…", "Un carril permite el paso de…",
  [("one line of automobiles that are not motorcycles", "una fila de automóviles que no sean motocicletas"),
   ("one line of motorcycles", "una fila de motocicletas"), ("two lines of cars", "dos filas de turismos")],
  "That is the legal definition, whether or not it has lane markings.", "Es la definición legal, esté o no delimitado por marcas longitudinales.")
Q("pt4", "parts", "The median (<i>mediana</i>) is a strip…", "La mediana es una franja…",
  [("between two separate plataformas, not for traffic", "entre dos plataformas separadas, no destinada a la circulación"),
   ("between two lanes in the same direction", "entre dos carriles del mismo sentido"), ("next to the carriageway for broken-down vehicles", "junto a la calzada para vehículos averiados")],
  "It separates the two plataformas of a dual road.", "Separa las dos plataformas de una vía desdoblada.")
Q("pt5", "parts", "A <i>refugio</i> is…", "Un refugio es…",
  [("a pedestrian zone on the carriageway, protected from traffic", "una zona peatonal situada en la calzada y protegida del tráfico"),
   ("a raised area that channels traffic at a junction", "una zona elevada que canaliza el tráfico en una intersección"),
   ("a lay-by to stop without blocking traffic", "un ensanchamiento para detenerse sin estorbar")],
  "Refugio is for pedestrians; isleta channels traffic; apartadero is the lay-by.", "El refugio es para peatones; la isleta canaliza el tráfico; el apartadero es para detenerse.")
Q("pt6", "parts", "A widening of the carriageway where vehicles stop without blocking traffic is a…",
  "Un ensanchamiento de la calzada para detenerse sin interceptar la circulación es un…",
  [("lay-by (<i>apartadero</i>)", "apartadero"), ("emergency escape lane", "zona de frenado de emergencia"), ("service road", "vía de servicio")],
  "The escape lane is for brake failure; the service road runs parallel to the main road.", "La zona de frenado es para fallos de frenos; la vía de servicio va paralela a la carretera.")
Q("pt7", "parts", "Is a “split roundabout”, where traffic crosses the central island directly, a true <i>glorieta</i>?",
  "¿Una glorieta partida, en la que el tráfico atraviesa la isleta central, es una glorieta propiamente dicha?",
  [("No", "No"), ("Yes", "Sí"), ("Only if it has traffic lights", "Solo si tiene semáforos")],
  "In a true glorieta traffic goes round the central island.", "En una glorieta el tráfico rodea la isleta central.")

# ---------------------------------------------------------------- 2. cycle infrastructure
Q("cy1", "cycleways", "A cycle route marked on the pavement is a…", "Una vía ciclista señalizada sobre la acera es una…",
  [("<i>acera bici</i>", "acera bici"), ("<i>pista bici</i>", "pista bici"), ("<i>carril bici</i>", "carril bici")],
  "Acera bici = on the pavement.", "Acera bici = sobre la acera.")
Q("cy2", "cycleways", "A <i>pista bici</i> is a cycle route…", "Una pista bici es una vía ciclista…",
  [("segregated from motor traffic, on its own route away from the roads", "segregada del tráfico motorizado, con trazado independiente de las carreteras"),
   ("alongside the carriageway", "adosada a la calzada"), ("shared with pedestrians through parks", "compartida con peatones por parques")],
  "The carril bici runs alongside the carriageway; the senda ciclable is shared with pedestrians.", "El carril bici va junto a la calzada; la senda ciclable se comparte con peatones.")
Q("cy3", "cycleways", "A <i>senda ciclable</i> is for…", "Una senda ciclable es para…",
  [("pedestrians and cycles, through parks, gardens or open spaces", "peatones y ciclos, por parques, jardines o espacios abiertos"),
   ("cycles only, alongside the carriageway", "solo ciclos, junto a la calzada"), ("cycles and mopeds", "ciclos y ciclomotores")],
  "It is segregated from motor traffic and shared with people on foot.", "Está segregada del tráfico motorizado y se comparte con los peatones.")
Q("cy4", "cycleways", "What makes a <i>carril bici</i> “protegido”?", "¿Qué hace que un carril bici sea «protegido»?",
  [("Side elements that physically separate it from the carriageway and the pavement", "Elementos laterales que lo separan físicamente de la calzada y de la acera"),
   ("Being painted green", "Estar pintado de verde"), ("Being one-way", "Ser de un solo sentido")],
  "The protection is physical, not just paint.", "La protección es física, no solo pintura.")

# ---------------------------------------------------------------- 3. types of road
Q("ty1", "types", "A <i>travesía</i> is…", "Una travesía es…",
  [("a stretch of carretera that runs through a town", "un tramo de carretera que discurre por poblado"), ("any street in a town", "cualquier calle de una población"),
   ("a road outside built-up areas", "una vía fuera de poblado")],
  "Urban roads are all the town’s roads except the travesías.", "Las vías urbanas son todas las de la población excepto las travesías.")
Q("ty2", "types", "What distinguishes an <i>autopista</i> from an <i>autovía</i>?", "¿Qué diferencia una autopista de una autovía?",
  [("The autopista has no access from neighbouring properties; the autovía has limited access", "La autopista no tiene accesos desde las propiedades colindantes; la autovía los tiene limitados"),
   ("The autovía has level crossings", "La autovía tiene cruces a nivel"), ("Only the autopista has separate carriageways", "Solo la autopista tiene calzadas separadas")],
  "Both have separate carriageways and no level crossings.", "Las dos tienen calzadas separadas y ninguna tiene cruces a nivel.")
Q("ty3", "types", "To use an autopista or autovía, an automobile must be able to exceed…", "Para circular por autopista o autovía, un automóvil debe poder superar…",
  [("60 km/h on the flat", "60 km/h en llano"), ("80 km/h on the flat", "80 km/h en llano"), ("45 km/h", "45 km/h")],
  "The threshold is 60 km/h on level ground.", "El umbral es 60 km/h en llano.")
Q("ty4", "types", "May a 16-year-old cyclist ride on an <i>autovía</i>?", "¿Puede un ciclista de 16 años circular por una autovía?",
  [("Yes, on the hard shoulder, unless signs forbid it", "Sí, por el arcén, salvo prohibición señalizada"),
   ("No, cycles are always forbidden", "No, los ciclos están siempre prohibidos"), ("Yes, in the right-hand lane", "Sí, por el carril derecho")],
  "Cyclists over 14 may use the shoulder of an autovía, never of an autopista.", "Los ciclistas mayores de 14 años pueden usar el arcén de la autovía, nunca el de la autopista.")
Q("ty5", "types", "Which of these may never use an autopista?", "¿Cuál de estos no puede circular nunca por autopista?",
  [("A moped", "Un ciclomotor"), ("A car towing a light trailer", "Un turismo con remolque ligero"), ("A motorcycle", "Una motocicleta")],
  "Mopeds are on the forbidden list with pedestrians, cycles, VMP and animals.", "Los ciclomotores están en la lista de prohibidos junto a peatones, ciclos, VMP y animales.")
Q("ty6", "types", "A road reserved for automobiles, with a single carriageway and no access to neighbouring properties, is a…",
  "Una vía reservada a automóviles, con una sola calzada y sin accesos a las propiedades colindantes, es una…",
  [("<i>vía para automóviles</i>", "vía para automóviles"), ("<i>autovía</i>", "autovía"), ("<i>carretera convencional</i>", "carretera convencional")],
  "Single carriageway is the key: autovías have separate carriageways.", "La clave es la calzada única: las autovías tienen calzadas separadas.")

# ---------------------------------------------------------------- 4. lanes
Q("ln1", "lanes", "On a two-way road with two lanes, you normally drive…", "En una calzada de doble sentido con dos carriles se circula normalmente…",
  [("in the right-hand lane", "por el carril derecho"), ("in either lane", "por cualquiera de los dos"), ("in the left-hand lane if it is free", "por el izquierdo si está libre")],
  "Whether or not the lanes are marked, in or out of town.", "Estén o no delimitados, dentro o fuera de poblado.")
Q("ln2", "lanes", "Two-way road with three lanes separated by broken lines. The centre lane may be used…",
  "Calzada de doble sentido con tres carriles separados por líneas discontinuas. El carril central se puede usar…",
  [("only to overtake or to turn left", "solo para adelantar o girar a la izquierda"), ("freely in both directions", "libremente en ambos sentidos"), ("never", "nunca")],
  "You drive in the right-hand lane; the centre one is for overtaking or turning left.", "Se circula por el derecho; el central es para adelantar o girar a la izquierda.")
Q("ln3", "lanes", "On that same road (two-way, three lanes), may you drive in the left-hand lane?", "En esa misma calzada (doble sentido, tres carriles), ¿se puede circular por el carril izquierdo?",
  [("No, never", "No, nunca"), ("Yes, to overtake", "Sí, para adelantar"), ("Yes, if the centre lane is busy", "Sí, si el central está ocupado")],
  "The left-hand lane belongs to the opposite direction.", "El carril izquierdo corresponde al sentido contrario.")
Q("ln4", "lanes", "Interurban one-way carriageway with three lanes. A truck with an MMA over 3,500 kg uses…",
  "Calzada interurbana de sentido único con tres carriles. Un camión de más de 3.500 kg de MMA circula por…",
  [("the right-hand lane, and exceptionally the next one", "el carril derecho y, excepcionalmente, el inmediato"), ("any lane", "cualquier carril"),
   ("the left-hand lane to overtake", "el izquierdo para adelantar")],
  "Never the remaining lanes.", "Nunca por los restantes.")
Q("ln5", "lanes", "On an interurban carriageway with three lanes in its direction, which combination is limited to the right lane and the next one?",
  "En una calzada interurbana con tres carriles en su sentido, ¿qué conjunto está limitado al carril derecho y su contiguo?",
  [("A combination over 7 m long", "Un conjunto de más de 7 m de longitud"), ("Only a combination over 10 m long", "Solo un conjunto de más de 10 m"),
   ("Only a combination over 12 m long", "Solo un conjunto de más de 12 m")],
  "7 m for lane use; 10 m is the threshold for the 50 m safety distance.", "7 m para la utilización de carriles; 10 m es el umbral de la distancia de 50 m.")
Q("ln6", "lanes", "In town, on a one-way street with marked lanes, a car uses…", "En poblado, en una calzada de sentido único con carriles delimitados, un turismo circula por…",
  [("the lane that best suits its destination", "el carril que mejor convenga a su destino"), ("always the right-hand lane", "siempre el carril derecho"),
   ("always the left-hand lane", "siempre el carril izquierdo")],
  "Without hindering others, and leaving it only to turn, overtake, stop or park.", "Sin estorbar, y abandonándolo solo para girar, adelantar, parar o estacionar.")
Q("ln7", "lanes", "On an autovía that runs through urban land, you normally drive…", "En una autovía que discurre por suelo urbano se circula normalmente…",
  [("in the rightmost lane, using the others to overtake", "por el carril de más a la derecha, usando los demás para adelantar"),
   ("in the lane that best suits your destination", "por el carril que mejor convenga al destino"), ("in any lane", "por cualquier carril")],
  "The “best for your destination” rule does not apply on autopistas and autovías.", "La regla del carril que mejor convenga no se aplica en autopistas y autovías.")

# ---------------------------------------------------------------- 5. position
Q("po1", "position", "Islands that separate the two directions of traffic are passed…", "Las isletas que separan los dos sentidos de circulación se rebasan…",
  [("on their right, leaving them on your left", "por su derecha, dejándolas a la izquierda"), ("on either side", "por cualquier lado"), ("on their left", "por su izquierda")],
  "Passing on their left would put you in the opposite direction.", "Pasar por su izquierda sería invadir el sentido contrario.")
Q("po2", "position", "An island on a one-way road may be passed…", "Una isleta en una vía de sentido único se puede rebasar…",
  [("on either side", "por cualquiera de los dos lados"), ("only on the right", "solo por la derecha"), ("only on the left", "solo por la izquierda")],
  "With a single direction, both sides are allowed.", "Con un solo sentido se permiten ambos lados.")
Q("po3", "position", "In squares, roundabouts and junctions you go round leaving the centre…", "En plazas, glorietas e intersecciones se circula dejando el centro…",
  [("on your left", "a la izquierda"), ("on your right", "a la derecha"), ("on either side depending on your exit", "a un lado u otro según la salida")],
  "The centre always stays on the left.", "El centro siempre queda a la izquierda.")
Q("po4", "position", "Roundabout on an interurban road with two marked lanes. Normally you use…", "Glorieta en vía interurbana con dos carriles delimitados. Normalmente se circula por…",
  [("the lane nearest the right (the outer lane)", "el carril más próximo a la derecha (exterior)"), ("the inner lane", "el carril interior"),
   ("whichever suits your exit", "el que convenga a la salida")],
  "The others only when traffic or the road advise it, without hindering anyone.", "Los demás solo cuando lo aconsejen el tráfico o la vía, sin estorbar.")
Q("po5", "position", "Roundabout in town with two marked lanes:", "Glorieta en vía urbana con dos carriles delimitados:",
  [("the lane that best suits your destination, never cutting across a vehicle in an outer lane", "el carril que mejor convenga al destino, sin cortar la trayectoria de quien va por un carril exterior"),
   ("always the outer lane", "siempre el exterior"), ("always the inner lane", "siempre el interior")],
  "In urban roundabouts you choose by destination.", "En glorietas urbanas se elige según el destino.")

# ---------------------------------------------------------------- 6. reserved lanes
Q("rs1", "reserved", "On an uphill stretch with a minimum-speed lane, who may use the lane carrying the minimum-speed sign?",
  "En una subida con carril de velocidad mínima, ¿quién puede usar el carril con la señal de velocidad mínima?",
  [("Only vehicles going at or above the signed speed", "Solo los que circulen a esa velocidad o superior"), ("Only slow vehicles", "Solo los vehículos lentos"),
   ("Any vehicle", "Cualquier vehículo")],
  "And even they should keep right when circumstances allow.", "Y aun así deben ir por la derecha si las circunstancias lo permiten.")
Q("rs2", "reserved", "Do minimum-speed lanes count when counting lanes?", "¿Se computan los carriles de velocidad mínima?",
  [("Yes", "Sí"), ("No", "No"), ("Only for trucks", "Solo para camiones")],
  "They count; bus, bike, acceleration, deceleration and waiting lanes do not.", "Sí cuentan; los de bus, bici, aceleración, deceleración y espera no.")
Q("rs3", "reserved", "A bus lane whose sign also says TAXI may be used by…", "Un carril bus cuya señal incluye la palabra TAXI lo pueden usar…",
  [("buses and taxis", "autobuses y taxis"), ("only taxis", "solo los taxis"), ("any car with passengers", "cualquier turismo con pasajeros")],
  "The word TAXI adds taxis to the buses.", "La palabra TAXI añade los taxis a los autobuses.")
Q("rs4", "reserved", "At a broken-line stretch of a bus lane, a car may cross it to…", "En un tramo discontinuo del carril bus, un turismo puede cruzarlo para…",
  [("turn right", "girar a la derecha"), ("park", "estacionar"), ("overtake", "adelantar")],
  "Not to stop, park, turn round or overtake; and giving way to buses and taxis.", "No para parar, estacionar, cambiar de sentido o adelantar; y cediendo el paso a autobuses y taxis.")
Q("rs5", "reserved", "As a general rule, the minimum number of occupants in a VAO lane is…", "Como norma general, el número mínimo de ocupantes en un carril VAO es…",
  [("two, driver included", "dos, incluido el conductor"), ("three, driver included", "tres, incluido el conductor"), ("two besides the driver", "dos además del conductor")],
  "Each stretch may set its own number, but the general minimum is two.", "Cada tramo puede fijar el suyo, pero el mínimo general es dos.")
Q("rs6", "reserved", "Which vehicle may use a VAO lane whatever its number of occupants?", "¿Qué vehículo puede usar el carril VAO con independencia de sus ocupantes?",
  [("A taxi", "Un taxi"), ("A car towing a trailer", "Un turismo con remolque"), ("A van", "Una furgoneta")],
  "Taxis and buses over 3.5 t may use it whatever their occupancy; cars with trailers and vans are forbidden.",
  "Taxis y autobuses de más de 3,5 t pueden usarlo sea cual sea su ocupación; turismos con remolque y furgonetas, no.")
Q("rs7", "reserved", "A car with the ECO label and only the driver on board may use a VAO lane…", "Un turismo con distintivo ECO y solo el conductor puede usar el carril VAO…",
  [("only when the variable-message panels allow it", "solo cuando lo indiquen los paneles de mensaje variable"), ("always", "siempre"), ("never", "nunca")],
  "Since 2026 cars with environmental labels depend on what the panels say.", "Desde 2026 los turismos con distintivo dependen de lo que indiquen los paneles.")
Q("rs8", "reserved", "On an acceleration lane you must…", "En un carril de aceleración hay que…",
  [("check at its start that you can merge safely, stopping if necessary", "cerciorarse al principio de que se puede entrar sin peligro, llegando a detenerse si es necesario"),
   ("merge at the start of the lane at any speed", "incorporarse al principio del carril a cualquier velocidad"),
   ("take priority over the main carriageway", "tener prioridad sobre la calzada principal")],
  "Those already on the main carriageway have priority.", "La prioridad es de quienes circulan por la calzada principal.")
Q("rs9", "reserved", "To leave a motorway with a deceleration lane, you slow down…", "Para salir de una autopista con carril de deceleración, se reduce la velocidad…",
  [("inside the deceleration lane, after entering it as soon as possible", "dentro del carril de deceleración, tras entrar en él cuanto antes"),
   ("on the main carriageway before the exit", "en la calzada principal antes de la salida"), ("on the hard shoulder", "en el arcén")],
  "Slowing on the main carriageway would hinder the traffic behind you.", "Frenar en la calzada principal entorpecería a los que vienen detrás.")
Q("rs10", "reserved", "Which lane is NOT counted when counting lanes?", "¿Qué carril NO se computa?",
  [("An acceleration lane", "Un carril de aceleración"), ("A minimum-speed lane", "Un carril de velocidad mínima"), ("An ordinary lane", "Un carril normal")],
  "Lanes reserved for certain vehicles or manoeuvres are left out.", "Se excluyen los reservados a determinados vehículos o maniobras.")

# ---------------------------------------------------------------- 6. flow lanes, corridor, snow
Q("fl1", "flow", "A reversible lane is marked by…", "Un carril reversible se identifica por…",
  [("double broken lines on both sides", "dobles líneas discontinuas a ambos lados"), ("a single continuous line", "una línea continua"), ("traffic cones", "conos")],
  "Lane-control lights or other means set its direction.", "Su sentido se regula con semáforos de carril u otros medios.")
Q("fl2", "flow", "In a reversible lane you must use…", "Por un carril reversible hay que llevar…",
  [("dipped headlights, day and night", "la luz de corto alcance o de cruce, de día y de noche"), ("hazard warning lights", "las luces de emergencia"),
   ("no special lights in daytime", "ninguna luz especial de día")],
  "Dipped beam day and night, and never move into the lane on its left.", "Luz de cruce de día y de noche, sin invadir el carril de su izquierda.")
Q("fl3", "flow", "Speed in a temporary additional lane (<i>carril adicional circunstancial</i>):", "Velocidad en un carril adicional circunstancial:",
  [("maximum 80 and minimum 60 km/h, unless lower is signed", "máxima 80 y mínima 60 km/h, salvo que se señalice otra inferior"),
   ("maximum 100 km/h", "máxima 100 km/h"), ("maximum 50 km/h", "máxima 50 km/h")],
  "Also with dipped headlights and lane markings between the wheels.", "Además, con luz de cruce y las marcas longitudinales entre las ruedas.")
Q("fl4", "flow", "A contraflow lane opened to improve traffic flow may be used by…", "Un carril en sentido contrario al habitual habilitado por fluidez lo pueden usar…",
  [("motorcycles and cars without trailer", "motocicletas y turismos sin remolque"), ("every vehicle", "todos los vehículos"), ("trucks only", "solo camiones")],
  "When it is opened for roadworks, every vehicle allowed on that road may use it.", "Cuando se habilita por obras, lo pueden usar todos los autorizados en esa vía.")
Q("fl5", "flow", "Queue on an autovía with three lanes in your direction. Where does the emergency corridor go?",
  "Retención en una autovía con tres carriles en su sentido. ¿Dónde se forma el carril de emergencia?",
  [("Between the left-hand lane and the next one", "Entre el carril izquierdo y su contiguo"), ("In the centre of the middle lane", "En el centro del carril central"),
   ("On the hard shoulder", "Por el arcén")],
  "The left lane moves left; all the others move right.", "Los del carril izquierdo se van a la izquierda; el resto, a la derecha.")
Q("fl6", "flow", "Queue on an autopista with two lanes in your direction. Who moves where?", "Retención en una autopista con dos carriles en su sentido. ¿Cómo se colocan?",
  [("The left lane moves left and the right lane moves right, leaving the gap in the centre", "Los del carril izquierdo a la izquierda y los del derecho a la derecha, dejando el hueco en el centro"),
   ("Everyone moves right", "Todos a la derecha"), ("Everyone moves onto the shoulder", "Todos al arcén")],
  "With two lanes the corridor is in the middle.", "Con dos carriles el hueco queda en el centro.")
Q("fl7", "flow", "Snow is making driving difficult on a two-lane autovía. You must…", "La nieve dificulta la circulación en una autovía de dos carriles. Hay que…",
  [("not overtake and keep to the right-hand lane", "no adelantar y circular por el carril derecho"), ("use the left-hand lane, which is clearer", "usar el carril izquierdo, que está más limpio"),
   ("overtake only snowploughs", "adelantar solo a los quitanieves")],
  "The left lanes stay free for emergency vehicles and snowploughs.", "Los carriles de la izquierda quedan libres para emergencias y quitanieves.")

# ---------------------------------------------------------------- 7. hard shoulder
Q("sh1", "shoulder", "Which of these must use the hard shoulder if it is passable and wide enough?", "¿Cuál de estos debe circular por el arcén si es transitable y suficiente?",
  [("A moped", "Un ciclomotor"), ("A car", "Un turismo"), ("A special vehicle with an MMA of 5,000 kg", "Un vehículo especial de 5.000 kg de MMA")],
  "Special vehicles go on the shoulder only up to 3,500 kg.", "Los vehículos especiales van por el arcén solo hasta 3.500 kg.")
Q("sh2", "shoulder", "Cyclists on the hard shoulder may ride…", "Los ciclistas por el arcén pueden ir…",
  [("two abreast, as far right as possible", "en columna de a dos, lo más a la derecha posible"), ("three abreast", "de tres en tres"), ("only in single file, always", "siempre en fila de a uno")],
  "Single file without visibility or when they bunch up.", "En hilera en tramos sin visibilidad o con aglomeraciones.")
Q("sh3", "shoulder", "Two mopeds on the shoulder. One wants to overtake the other. It is forbidden if they would be side by side for more than…",
  "Dos ciclomotores por el arcén. Uno quiere adelantar al otro. Está prohibido si la marcha en paralelo supera…",
  [("15 seconds or 200 metres", "15 segundos o 200 metros"), ("30 seconds or 500 metres", "30 segundos o 500 metros"), ("10 seconds or 100 metres", "10 segundos o 100 metros")],
  "Serious offence. Bicycles are exempt from this rule.", "Es infracción grave. Las bicicletas quedan exceptuadas.")
Q("sh4", "shoulder", "On a long descent with bends, may a cyclist leave the shoulder?", "En un descenso prolongado con curvas, ¿puede un ciclista abandonar el arcén?",
  [("Yes, if safety allows, but not on an autovía", "Sí, si la seguridad lo permite, pero no en autovía"), ("No, never", "No, nunca"), ("Yes, also on an autovía", "Sí, también en autovía")],
  "On autovías cyclists must stay on the shoulder.", "En autovía los ciclistas no pueden abandonar el arcén.")
Q("sh5", "shoulder", "A car breaks down on a motorway but can still move. If it needs assistance it should…", "Un turismo se avería en autopista pero puede moverse. Si necesita auxilio debe…",
  [("head for the first exit using the right-hand shoulder", "dirigirse a la primera salida usando el arcén derecho"), ("stop in the left-hand lane", "detenerse en el carril izquierdo"),
   ("reverse to the previous exit", "volver marcha atrás a la salida anterior")],
  "If that is impossible, stop on the right-hand shoulder or where it obstructs least.", "Si no es posible, detenerse en el arcén derecho o donde menos estorbe.")
Q("sh6", "shoulder", "A road maintenance vehicle using the shoulder to reach its work must not exceed…", "Un vehículo de mantenimiento que usa el arcén para ir a su trabajo no puede superar…",
  [("30 km/h", "30 km/h"), ("50 km/h", "50 km/h"), ("60 km/h", "60 km/h")],
  "Only priority vehicles on urgent service are exempt from the 30 km/h limit.", "Solo los prioritarios en servicio de urgencia están exentos del límite de 30 km/h.")
Q("sh7", "shoulder", "Since 1 October 2026, a motorcycle may ride on the hard shoulder…", "Desde el 1 de octubre de 2026, una motocicleta puede circular por el arcén…",
  [("only on signed stretches, when traffic is stopped by congestion, at up to 30 km/h", "solo en tramos señalizados, con el tráfico detenido por congestión y a 30 km/h como máximo"),
   ("on any road when traffic is slow, at up to 50 km/h", "en cualquier vía con tráfico lento, a 50 km/h como máximo"), ("whenever the shoulder is empty", "siempre que el arcén esté libre")],
  "In single file and without endangering those who must use the shoulder.", "En columna de a uno y sin poner en riesgo a los obligados a usar el arcén.")

# ---------------------------------------------------------------- 8. safety distance
Q("ds1", "distance", "Following another vehicle without signalling that you will overtake, your distance must also let…",
  "Detrás de otro vehículo y sin señalizar que se va a adelantar, la separación debe permitir además…",
  [("the vehicle behind you overtake you safely", "que el que viene detrás nos adelante con seguridad"), ("you brake gently", "frenar suavemente"),
   ("a car park between you", "que un turismo estacione entre ambos")],
  "Besides room to stop without colliding.", "Además del espacio para detenerse sin colisionar.")
Q("ds2", "distance", "Outside towns, a truck with an MMA over 3,500 kg keeps behind another vehicle at least…", "Fuera de poblado, un camión de más de 3.500 kg de MMA guarda detrás de otro vehículo al menos…",
  [("50 m", "50 m"), ("100 m", "100 m"), ("25 m", "25 m")],
  "Also vehicles and combinations over 10 m long.", "También los vehículos y conjuntos de más de 10 m de longitud.")
Q("ds3", "distance", "Which of these must keep the 50 m gap outside towns?", "¿Cuál de estos debe guardar la separación de 50 m fuera de poblado?",
  [("A combination 12 m long", "Un conjunto de 12 m de longitud"), ("A car towing a caravan, 9 m in total", "Un turismo con caravana de 9 m en total"), ("A 4.5 m car", "Un turismo de 4,5 m")],
  "The length threshold is over 10 m.", "El umbral de longitud es de más de 10 m.")
Q("ds4", "distance", "Where is the 50 m gap NOT required?", "¿Dónde NO es obligatoria la separación de 50 m?",
  [("Where overtaking is forbidden", "Donde esté prohibido adelantar"), ("On a two-way road with one lane each way where overtaking is allowed", "En una vía de doble sentido con un carril por sentido donde se puede adelantar"),
   ("At night", "De noche")],
  "Also in town, with more than one lane, in saturated traffic and when about to overtake.", "Tampoco en poblado, con más de un carril, con tráfico saturado ni al ir a adelantar.")
Q("ds5", "distance", "Chevrons are painted on the lane. How many should you keep between you and the vehicle in front?", "En el carril hay galones pintados. ¿Cuántos hay que dejar con el vehículo de delante?",
  [("At least two", "Al menos dos"), ("At least one", "Al menos uno"), ("At least four", "Al menos cuatro")],
  "Sign R-300 “Minimum distance” marks the start of the stretch.", "La señal R-300 «Separación mínima» marca el inicio del tramo.")
Q("ds6", "distance", "In a tunnel, a car not intending to overtake keeps at least…", "En un túnel, un turismo que no pretende adelantar mantiene al menos…",
  [("100 m or 4 seconds", "100 m o 4 segundos"), ("50 m or 2 seconds", "50 m o 2 segundos"), ("150 m or 6 seconds", "150 m o 6 segundos")],
  "150 m or 6 s is for vehicles over 3,500 kg.", "150 m o 6 s es para los de más de 3.500 kg.")
Q("ds7", "distance", "Cyclists riding in a group…", "Los ciclistas que circulan en grupo…",
  [("may ride without the minimum gap, taking extra care", "pueden circular sin esa separación, extremando la atención"), ("must keep 50 m between them", "deben guardar 50 m entre ellos"),
   ("must ride 10 m apart", "deben ir a 10 m unos de otros")],
  "The law exempts groups of cyclists, asking them to avoid rear-end collisions among themselves.", "La norma exceptúa a los grupos de ciclistas, que deben evitar alcances entre ellos.")

# ---------------------------------------------------------------- 9. congested roads
Q("st1", "saturated", "Traffic is saturated when…", "La circulación está saturada cuando…",
  [("vehicles fill the whole width of the carriageway", "los vehículos ocupan todo el ancho de la calzada"), ("there is a vehicle every 50 m", "hay un vehículo cada 50 m"),
   ("the traffic lights are red", "los semáforos están en rojo")],
  "Every lane is occupied.", "Todos los carriles están ocupados.")
Q("st2", "saturated", "In saturated traffic the right-hand lane moves faster than the left. Is that overtaking on the right?",
  "Con la circulación saturada, el carril derecho avanza más rápido que el izquierdo. ¿Es un adelantamiento por la derecha?",
  [("No, it is not considered overtaking", "No, no se considera adelantamiento"), ("Yes, and it is forbidden", "Sí, y está prohibido"), ("Yes, but it is allowed", "Sí, pero está permitido")],
  "Different speeds in different lanes are normal when traffic is saturated.", "Distintas velocidades por carril son normales con la circulación saturada.")
Q("st3", "saturated", "On a saturated road, may you drive on the hard shoulder to reach the next exit?", "En una vía saturada, ¿se puede circular por el arcén para tomar la salida más próxima?",
  [("No", "No"), ("Yes, slowly", "Sí, despacio"), ("Yes, with the hazard lights on", "Sí, con las luces de emergencia")],
  "Overtaking on the shoulder or driving on it is forbidden, even for the next exit.", "Se prohíbe adelantar por el arcén o circular por él, ni para la salida más próxima.")
Q("st4", "saturated", "On a saturated road, changing lanes is allowed…", "En una vía saturada se puede cambiar de carril…",
  [("only to get ready to turn, leave the carriageway or take a particular direction", "solo para prepararse a girar, salir de la calzada o tomar una dirección determinada"),
   ("whenever the other lane moves faster", "siempre que el otro carril vaya más rápido"), ("never in any case", "nunca, en ningún caso")],
  "Switching lanes to gain a few metres is forbidden.", "Cambiar de carril para ganar unos metros está prohibido.")
Q("st5", "saturated", "In DGT traffic information, red means…", "En la información de tráfico de la DGT, el rojo significa…",
  [("saturated traffic, under 25 % of normal speed", "circulación saturada, por debajo del 25 % de la velocidad"), ("road closed", "carretera cortada"),
   ("heavy traffic, 75–90 %", "circulación intensa, 75–90 %")],
  "White > 90 %, green 75–90 %, yellow 25–75 %, red < 25 %, black = interrupted.", "Blanco > 90 %, verde 75–90 %, amarillo 25–75 %, rojo < 25 %, negro = interrumpida.")

# ---------------------------------------------------------------- 10. pedestrians
Q("pd1", "peds", "May any vehicle drive along the pavement (<i>acera</i>)?", "¿Puede algún vehículo circular por la acera?",
  [("No, pavements are reserved for pedestrians", "No, las aceras están reservadas a los peatones"), ("Yes, mopeds at walking pace", "Sí, los ciclomotores al paso"), ("Yes, at night", "Sí, de noche")],
  "Only a municipal bylaw can allow children up to 12 on bicycles, with an adult on foot.", "Solo una ordenanza puede permitir niños de hasta 12 años en bici acompañados de un adulto a pie.")
Q("pd2", "peds", "With no usable pedestrian zone, a pedestrian walking alone uses…", "Sin zona peatonal practicable, un peatón solo circula…",
  [("the left-hand shoulder, facing the traffic", "por el arcén izquierdo, de cara al tráfico"), ("the right-hand shoulder, with the traffic", "por el arcén derecho, en el sentido del tráfico"),
   ("the middle of the carriageway", "por el centro de la calzada")],
  "Facing the traffic lets the pedestrian see what is coming.", "De cara al tráfico, el peatón ve lo que se le acerca.")
Q("pd3", "peds", "Someone pushing a bicycle along a road without a pavement walks…", "Quien empuja una bicicleta por una vía sin acera circula…",
  [("on the right", "por la derecha"), ("on the left", "por la izquierda"), ("on whichever side has less traffic", "por el lado con menos tráfico")],
  "Same for a moped or VMP pushed by hand, and for groups led by one person.", "Igual con un ciclomotor o VMP a pie, y los grupos dirigidos por una persona.")
Q("pd4", "peds", "At a zebra crossing without lights, the pedestrian…", "En un paso de peatones sin semáforo, el peatón…",
  [("has preference, but should step out only when it is safe", "tiene preferencia, pero solo debe entrar cuando sea seguro"),
   ("may step out at any moment", "puede entrar en cualquier momento"), ("must wait until no vehicle is in sight", "debe esperar a que no se vea ningún vehículo")],
  "Distance and speed of the approaching vehicles must allow it.", "La distancia y velocidad de los vehículos deben permitirlo.")
Q("pd5", "peds", "May pedestrians cross the carriageway of a roundabout?", "¿Pueden los peatones atravesar la calzada de una glorieta?",
  [("No, they must walk round it unless there is a crossing", "No, deben rodearla salvo que haya paso para peatones"), ("Yes, through the centre", "Sí, por el centro"),
   ("Yes, if there is no traffic", "Sí, si no hay tráfico")],
  "Squares and roundabouts are walked round, not across.", "Plazas y glorietas se rodean, no se atraviesan.")
Q("pd6", "peds", "Your car breaks down on an autovía and you can get out safely. You should…", "Tu coche se avería en una autovía y puedes salir con seguridad. Debes…",
  [("get out on the side away from the traffic and go to a safe place outside the platform", "salir por el lado contrario al tráfico e ir a un lugar seguro fuera de la plataforma"),
   ("wait on the shoulder behind the car", "esperar en el arcén detrás del coche"), ("walk along the shoulder to the next exit", "caminar por el arcén hasta la salida")],
  "If you cannot get out safely, stay inside with your seat belt fastened.", "Si no se puede salir con seguridad, se permanece dentro con el cinturón abrochado.")
Q("pd7", "peds", "Hitch-hiking on an autopista or autovía…", "El autostop en autopistas y autovías…",
  [("is forbidden anywhere, including the areas around toll booths", "está prohibido en cualquier tramo, incluidas las explanadas de peaje"),
   ("is allowed at toll booths", "está permitido en los peajes"), ("is allowed on the hard shoulder", "está permitido en el arcén")],
  "No requests for a lift anywhere on these roads.", "No se puede pedir que te lleven en ningún punto de estas vías.")
Q("pd8", "peds", "At night outside towns, a pedestrian on the shoulder must wear an approved reflective item visible from at least…",
  "De noche fuera de poblado, el peatón que va por el arcén debe llevar un elemento reflectante homologado visible al menos a…",
  [("150 m", "150 m"), ("50 m", "50 m"), ("300 m", "300 m")],
  "Also by day when weather reduces visibility.", "También de día si las condiciones reducen la visibilidad.")
Q("pd9", "peds", "When a priority vehicle with its signals on approaches, pedestrians…", "Ante un vehículo prioritario con sus señales, los peatones…",
  [("clear the carriageway and stay in refuges or pedestrian zones", "despejan la calzada y permanecen en refugios o zonas peatonales"),
   ("may finish crossing slowly", "pueden terminar de cruzar despacio"), ("must stop in the middle of the road", "deben detenerse en medio de la calzada")],
  "If there are none, they move away from the traffic.", "Si no los hay, se alejan de la circulación.")

# ---------------------------------------------------------------- 11. animals
Q("an1", "animals", "The person leading animals on a public road must be…", "La persona que conduce animales por una vía pública debe ser…",
  [("over 18", "mayor de 18 años"), ("over 16", "mayor de 16 años"), ("over 14", "mayor de 14 años")],
  "And able to control them at all times.", "Y capaz de dominarlos en todo momento.")
Q("an2", "animals", "A flock of sheep on the carriageway may occupy…", "Un rebaño de ovejas en la calzada puede ocupar…",
  [("never more than the right-hand half", "nunca más de la mitad derecha"), ("the whole carriageway if there is no traffic", "toda la calzada si no hay tráfico"),
   ("the left-hand half", "la mitad izquierda")],
  "At walking pace, as far right as possible, in moderate groups.", "Al paso, lo más a la derecha posible y en grupos moderados.")
Q("an3", "animals", "Animals on a road normally go along…", "Los animales en una vía circulan normalmente por…",
  [("the right-hand shoulder", "el arcén derecho"), ("the left-hand shoulder", "el arcén izquierdo"), ("the centre of the carriageway", "el centro de la calzada")],
  "Exceptionally, one single animal may be led on the left for safety.", "Excepcionalmente, un solo animal puede ir por la izquierda por seguridad.")
Q("an4", "animals", "At a narrow point where the paths of animals and vehicles cross…", "En un estrechamiento donde se cruzan las trayectorias de animales y vehículos…",
  [("the animals give way to the vehicles", "los animales ceden el paso a los vehículos"), ("the vehicles give way to the animals", "los vehículos ceden el paso a los animales"),
   ("whoever arrives first goes first", "pasa quien llegue primero")],
  "Same at junctions.", "Igual en las intersecciones.")
Q("an5", "animals", "Animals on a poorly lit road at night carry lights on the side nearest the centre:", "Los animales de noche en vía mal iluminada llevan luces en el lado más próximo al centro:",
  [("white or yellow in front, red behind", "blanca o amarilla delante y roja detrás"), ("red in front, white behind", "roja delante y blanca detrás"),
   ("flashing yellow on both sides", "amarilla intermitente a ambos lados")],
  "Same as groups of pedestrians led by one person.", "Igual que los grupos de peatones dirigidos por una persona.")
Q("an6", "animals", "May livestock use an autovía when there is no other route?", "¿Puede el ganado circular por una autovía si no hay otro itinerario?",
  [("No, animals are forbidden on autopistas and autovías", "No, los animales tienen prohibidas las autopistas y autovías"), ("Yes, on the shoulder", "Sí, por el arcén"),
   ("Yes, at night", "Sí, de noche")],
  "Animal-drawn vehicles are forbidden there too.", "También están prohibidos los vehículos de tracción animal.")
