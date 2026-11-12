# -*- coding: utf-8 -*-
"""Question bank for the interactive Topic 5 page (manoeuvres). In every question the FIRST option is the
correct one (the page shuffles options when it shows them). Ids must be unique and must not start with "ai"."""

BANK = []


def Q(qid, tag, en, es, opts, why_en, why_es):
    BANK.append({
        "id": qid, "tag": tag,
        "q": {"en": en, "es": es},
        "o": [{"en": a, "es": b} for a, b in opts],
        "why": {"en": why_en, "es": why_es},
    })


def S(*pairs):
    """Shorthand for options that are the same in both languages."""
    return [(p, p) for p in pairs]


# tag -> section number, names, recap bullets, typical confusion
TAGS = {
    "basics": dict(sec=1, en="What a manoeuvre is", es="Qué es una maniobra",
        recap=[("A manoeuvre is a noticeable change the driver makes that the road layout does not impose.", "Maniobra: alteración sensible que hace el conductor y que no impone el trazado de la vía."),
               ("Before any manoeuvre: RSM (mirror, signal, manoeuvre) and PVO (position, speed, observation).", "Antes de cualquier maniobra: RSM (retrovisor, señalizar, maniobra) y PVO (posición, velocidad, observación)."),
               ("Basic manoeuvres: joining, moving sideways, overtaking, turning, turning round, stopping or parking.", "Básicas: incorporación, desplazamiento lateral, adelantamiento, cambio de dirección, cambio de sentido, parada o estacionamiento."),
               ("Not manoeuvres: imposed detention, following a curve or roundabout, reversing.", "No son maniobras: la detención impuesta, la trayectoria curva y la marcha atrás.")],
        trap=("Counting reversing as a basic manoeuvre.", "Contar la marcha atrás como maniobra básica.")),
    "optical": dict(sec=2, en="Light and arm signals", es="Advertencias ópticas",
        recap=[("Announce every manoeuvre clearly and in good time.", "Advertir toda maniobra de forma clara y con antelación."),
               ("Lights stay on for the whole manoeuvre; the arm (usually the left) only if done properly and visible to all.", "Las luces, durante toda la maniobra; el brazo (normalmente el izquierdo), bien hecho y visible."),
               ("Left: arm straight out. Right: forearm up, palm open. Reversing: arm out, palm back. Slowing: arm up and down.", "Izquierda: brazo horizontal. Derecha: antebrazo arriba. Marcha atrás: palma hacia atrás. Frenar: brazo de arriba abajo."),
               ("If lights and arm disagree, the arm prevails.", "Si luces y brazo se contradicen, prevalece el brazo.")],
        trap=("Thinking the indicator beats the arm signal.", "Pensar que el intermitente prevalece sobre el brazo.")),
    "horn": dict(sec=2, en="Horn and flashes", es="Claxon y ráfagas",
        recap=[("The horn is exceptional: to avoid an accident or running someone over, on an emergency trip, and out of town to announce an overtaking.",
                "El claxon es excepcional: evitar accidente o atropello, servicio de urgencia y, fuera de poblado, avisar del adelantamiento."),
               ("In town, an overtaking is announced only with flashes.", "En poblado, el adelantamiento solo se avisa con ráfagas."),
               ("Continuous, steady, not shrill, no musical notes; never to greet, tell off or warn of police.", "Continuo, uniforme, no estridente, sin notas musicales; nunca para saludar, recriminar o avisar de agentes."),
               ("Flashes: dipped or main beam, very short, never to dazzle; same uses as the horn or instead of it.", "Ráfagas: cruce o carretera, muy cortas, sin deslumbrar; mismos usos que el claxon o en su lugar.")],
        trap=("Using the horn in town to announce an overtaking.", "Usar el claxon en poblado para avisar de un adelantamiento.")),
    "joining": dict(sec=3, en="Joining traffic", es="Incorporación a la circulación",
        recap=[("Joining = starting to drive or entering another road; moving off after a red light or agent is not joining.", "Incorporarse = empezar a circular o entrar en otra vía; reanudar tras semáforo o agente no lo es."),
               ("Observe (mirrors and directly), signal (indicator, or briefly if going straight), join giving way.", "Observar (directamente y por espejos), señalizar (intermitente, o momentáneamente si es de frente), incorporarse cediendo el paso."),
               ("From a private road or building: speed to stop at once, giving way to both sides, pedestrians too.", "Desde inmueble o camino privado: velocidad para detenerse en el acto, cediendo a ambos lados, también a peatones."),
               ("Acceleration lane: check at its start (stop there if needed), reach the right speed by its end.", "Carril de aceleración: comprobar al principio (detenerse si hace falta), alcanzar la velocidad adecuada al final.")],
        trap=("Thinking you join at the end of the acceleration lane without checking at its start.", "Pensar que se comprueba al final del carril de aceleración en vez de al principio.")),
    "facilitate": dict(sec=3, en="Helping others join", es="Facilitar la incorporación",
        recap=[("Help anyone joining as far as you can, above all a bus leaving a signed stop.", "Facilitar la incorporación en lo posible, sobre todo a un autobús que sale de una parada señalizada."),
               ("In town: move sideways, or slow down safely and signalled, even stop.", "En poblado: desplazarse lateralmente, o reducir la velocidad con seguridad y señalizando, incluso detenerse."),
               ("The bus driver signals with the indicators and still takes every precaution.", "El conductor del autobús señaliza con los intermitentes y sigue extremando la precaución."),
               ("If dense traffic stops you joining, you may signal so that others help you.", "Si la densidad del tráfico impide incorporarse, se puede señalizar para que te la faciliten.")],
        trap=("Thinking the bus simply has priority and need not take care.", "Pensar que el autobús tiene prioridad sin más y no debe tomar precauciones.")),
    "lateral": dict(sec=4, en="Moving sideways", es="Desplazamiento lateral",
        recap=[("Any change of position that takes you partly or fully into another lane; a correction within your lane is not one.", "Todo cambio de posición que invade parcial o totalmente otro carril; corregir dentro del carril no lo es."),
               ("Reasons: turning, passing an immobilised vehicle, overtaking, stopping or parking, joining, signs.", "Motivos: girar, rebasar a un inmovilizado, adelantar, parar o estacionar, incorporarse, señalización."),
               ("Observe, signal until it is over, move early, gradually and smoothly.", "Observar, señalizar hasta terminar, desplazarse con antelación, de forma gradual y progresiva."),
               ("The vehicle already in the lane you move into has priority.", "Tiene prioridad el que circula por el carril que se quiere ocupar.")],
        trap=("Switching the indicator off before the move is finished.", "Quitar el intermitente antes de terminar el desplazamiento.")),
    "overtake": dict(sec=5, en="How to overtake", es="Cómo adelantar",
        recap=[("Not overtaking: faster lane in congested traffic, special lanes (bus, acceleration, shoulder), cyclists within a group.", "No es adelantamiento: carril más rápido en tráfico congestionado, carriles especiales, ciclistas del mismo grupo."),
               ("Before: suitable distance, room to pass and to return, the vehicle ahead has not signalled the same way, nobody overtaking you.", "Antes: distancia adecuada, espacio para pasar y volver, que el de delante no haya señalizado el mismo lado y que nadie te adelante."),
               ("On the left; on the right only past a vehicle turning left, trams in the centre, or in town with 2+ marked lanes.", "Por la izquierda; por la derecha solo al que gira a la izquierda, al tranvía central o en poblado con 2 o más carriles delimitados."),
               ("Return gradually when you see the overtaken vehicle in the mirror; if it goes wrong, slow down and pull back in.", "Volver gradualmente al ver al adelantado en el espejo; si surge peligro, frenar y regresar.")],
        trap=("Changing lanes to overtake in a congested queue.", "Cambiar de carril para adelantar en una cola congestionada.")),
    "gap": dict(sec=5, en="Side gap and −20 km/h", es="Separación lateral y −20 km/h",
        recap=[("Vulnerable users, immobilised and assistance vehicles: move partly or fully into the next lane, gap ≥ 1.5 m.", "Usuarios vulnerables, inmovilizados y vehículos de auxilio: ocupar parcial o totalmente el carril contiguo, separación ≥ 1,5 m."),
               ("With more than one lane your way: a full lane change.", "Con más de un carril por sentido: cambio completo de carril."),
               ("Out of town, overtaking vulnerable users: 20 km/h below the limit. Immobilised or assistance vehicles: −20 km/h in and out of town.", "Fuera de poblado, a vulnerables: 20 km/h menos. A inmovilizados o de auxilio: −20 km/h dentro y fuera."),
               ("Never overtake if it endangers cyclists coming the other way, even on the shoulder.", "Nunca adelantar poniendo en peligro a ciclistas que vienen de frente, aunque vayan por el arcén.")],
        trap=("Applying the −20 km/h for cyclists inside towns too.", "Aplicar los −20 km/h por ciclistas también dentro de poblado.")),
    "overtaken": dict(sec=5, en="The vehicle being overtaken", es="El vehículo adelantado",
        recap=[("Keep to the right edge (not on the shoulder); to turn left, keep left.", "Ceñirse al borde derecho (sin pisar el arcén); para girar a la izquierda, ceñirse a la izquierda."),
               ("Never speed up or make it harder; slow down if a danger appears.", "Prohibido acelerar o dificultar el adelantamiento; frenar si surge un peligro."),
               ("If the overtaker gives up and brakes, let them back in.", "Si el que adelanta desiste y frena, facilitarle la vuelta."),
               ("Heavy and large vehicles: arm moved back to front or right indicator to say ‘you can pass’; slow down or use a usable shoulder if needed.",
                "Pesados y grandes: brazo de atrás hacia delante o intermitente derecho para indicar que se puede adelantar; aminorar o apartarse al arcén si hace falta.")],
        trap=("Thinking the overtaken vehicle should move onto the shoulder as a rule.", "Pensar que el adelantado debe meterse en el arcén como norma.")),
    "noovertake": dict(sec=5, en="Where overtaking is forbidden", es="Dónde está prohibido adelantar",
        recap=[("Signs, a line you may not cross, poor visibility (bends, brows, weather, behind a large vehicle overtaking).", "Señales, marca que no se puede atravesar, falta de visibilidad (curvas, rasantes, meteorología, tras un vehículo grande que adelanta)."),
               ("Junctions, except roundabouts, overtaking on the right, signed priority, and two-wheelers.", "Intersecciones, salvo glorietas, por la derecha, prioridad señalizada y vehículos de dos ruedas."),
               ("Level crossings, pedestrian crossings, junctions with cycle routes; tunnels with one lane your way; a vehicle already overtaking.", "Pasos a nivel, pasos de peatones, cruces con vías ciclistas; túneles con un carril por sentido; al que ya adelanta."),
               ("Even across a continuous line: an obstacle or broken-down vehicle, or slow users (cycles, pedestrians, animals, farm vehicles) if safe; not a vehicle stopped by traffic.",
                "Incluso con línea continua: obstáculo o averiado, o usuarios lentos (ciclos, peatones, animales, agrícolas) si es seguro; no al detenido por el tráfico.")],
        trap=("Thinking overtaking a motorcycle at a junction is forbidden.", "Pensar que adelantar a una moto en una intersección está prohibido.")),
    "turning": dict(sec=6, en="Turning", es="Cambio de dirección",
        recap=[("Turning to use another road, another carriageway, or leave the road; following a bend is not one.", "Girar para usar otra vía, otra calzada o salir de la vía; seguir una curva no lo es."),
               ("Right: keep to the right edge. Left, one-way: keep to the left edge.", "Derecha: ceñirse al borde derecho. Izquierda en sentido único: al borde izquierdo."),
               ("Left, two-way: next to the centre marking or centre of the road; three lanes with broken lines: centre lane.", "Izquierda en doble sentido: junto a la marca o al eje; tres carriles con discontinuas: carril central."),
               ("Roundabouts: centre on your left. Deceleration lane: enter early, slow down inside. Cyclists and mopeds out of town turn left from the right shoulder.",
                "Glorietas: centro a la izquierda. Carril de deceleración: entrar pronto y frenar dentro. Ciclos y ciclomotores en interurbana giran a la izquierda desde el arcén derecho.")],
        trap=("Turning left from the left lane of a two-way three-lane road.", "Girar a la izquierda desde el carril izquierdo de una vía de doble sentido con tres carriles.")),
    "uturn": dict(sec=7, en="Turning round", es="Cambio de sentido",
        recap=[("A 180° half turn to continue the other way on the same road.", "Media vuelta de 180° para seguir por la misma vía en sentido contrario."),
               ("Observe, signal (braking and moving sideways), choose a suitable place, one go, no reversing.", "Observar, señalizar (frenar y desplazarse), lugar adecuado, un solo giro, sin marcha atrás."),
               ("If waiting holds others up, pull off to the right and wait.", "Si al esperar se retiene a los de detrás, salir por la derecha y esperar."),
               ("Forbidden: signs or continuous line, where overtaking is forbidden (but near a level crossing it is allowed), junctions (except signed priority and roundabouts), motorways except grade-separated points.",
                "Prohibido: señales o línea continua, donde se prohíbe adelantar (pero junto a un paso a nivel sí), intersecciones (salvo prioridad señalizada y glorietas), autopistas salvo a distinto nivel.")],
        trap=("Crossing an open gap in a motorway median to turn round.", "Cruzar el paso abierto de la mediana de una autopista para cambiar de sentido.")),
    "reverse": dict(sec=8, en="Reversing", es="Marcha atrás",
        recap=[("Driving in reverse is forbidden as a rule; only when you cannot go forward, turn or turn round, for the minimum distance.", "Prohibido como norma; solo si no se puede ir hacia delante, girar ni cambiar de sentido, con el recorrido mínimo."),
               ("As part of stopping, parking or joining: at most 15 m and never into a junction.", "Como complemento de parada, estacionamiento o incorporación: máximo 15 m y sin invadir intersecciones."),
               ("Forbidden on autopistas and autovías.", "Prohibida en autopistas y autovías."),
               ("Observe (get out if needed, or follow someone’s directions), reversing light or arm palm back, slowly; without total safety, give up.",
                "Observar (bajándose si hace falta o con ayuda), luz de marcha atrás o brazo con la palma hacia atrás, despacio; sin seguridad total, desistir.")],
        trap=("Thinking 15 m is the limit for any reversing, even on a motorway.", "Pensar que los 15 m valen para cualquier marcha atrás, incluso en autopista.")),
    "stops": dict(sec=9, en="Detentions, breakdowns and the V-16", es="Detenciones, averías y V-16",
        recap=[("Detention: imposed. Stop: voluntary, under 2 minutes, driver stays. Parking: everything else.", "Detención: impuesta. Parada: voluntaria, menos de 2 minutos, sin abandonar. Estacionamiento: el resto."),
               ("Breakdown: off the carriageway and usable shoulder; if it can move, carry on or head to the first exit on the right shoulder.", "Avería: fuera de calzada y arcén transitable; si puede seguir, continuar o ir a la primera salida por el arcén derecho."),
               ("Occupants out on the side away from traffic to a safe place off the platform; otherwise inside with belts on.", "Ocupantes fuera por el lado contrario al tráfico hacia un lugar seguro; si no, dentro con el cinturón."),
               ("Hazard lights + connected V-16 on the roof (+ position lights at night). Vest on interurban roads. No accident report on the road.",
                "Luz de emergencia + V-16 conectada en el techo (+ luz de posición de noche). Chaleco en interurbanas. Sin parte de accidente en la vía.")],
        trap=("Believing the triangle still replaces the V-16.", "Creer que el triángulo aún sustituye a la V-16.")),
    "tunnel": dict(sec=9, en="Emergencies in tunnels", es="Emergencias en túneles",
        recap=[("Breakdown: drive out if you can, or to an emergency lay-by, or as far right as possible.", "Avería: salir si se puede, o al apartadero de emergencia, o lo más a la derecha posible."),
               ("Engine off, position and hazard lights, V-16, SOS post, everyone to the nearest refuge or exit.", "Motor parado, luces de posición y emergencia, V-16, poste S.O.S., todos al refugio o salida más próximos."),
               ("Fire: pull right, engine off, key in, doors open, walk away from the fire.", "Incendio: a la derecha, motor apagado, llave puesta, puertas abiertas, alejarse del fuego."),
               ("Held up by traffic: keep well back, engine off after 2 minutes, position lights and brief hazard lights.", "Detenido por el tráfico: separarse del de delante, motor apagado pasados 2 minutos, posición y emergencia temporal.")],
        trap=("Taking the key and locking the car in a tunnel fire.", "Llevarse la llave y cerrar el coche en un incendio en túnel.")),
    "parking": dict(sec=9, en="How and where to stop and park", es="Cómo y dónde parar y estacionar",
        recap=[("Parallel to the edge, one behind another; oblique or side by side only if the road advises it; never take two spaces.", "En paralelo y en línea; oblicuo o en batería solo si la vía lo aconseja; no ocupar dos plazas."),
               ("Urban: on carriageway or shoulder, close to the right edge; both sides if one-way, only the right if two-way.", "Urbanas: en calzada o arcén, junto al borde derecho; ambos lados en sentido único, solo el derecho en doble sentido."),
               ("Interurban: always off the carriageway and usable shoulder, on the right.", "Interurbanas: siempre fuera de la calzada y del arcén transitable, a la derecha."),
               ("Councils: time limits, removal over 3 × the paid time, fees by size and label, tow trucks, two-wheelers on pavements.", "Ayuntamientos: limitación horaria, retirada al rebasar el triple, tarifas, grúas, motos en aceras.")],
        trap=("Parking on the shoulder of an interurban road.", "Estacionar en el arcén de una vía interurbana.")),
    "noparking": dict(sec=9, en="Where you may not stop or park", es="Prohibiciones de parada y estacionamiento",
        recap=[("No parking: limited time without ticket, loading zones, disabled spaces, pavements, vados, double parking, broken yellow line, zig-zag.",
                "Prohibido estacionar: zona horaria sin título, carga y descarga, minusválidos, aceras, vados, doble fila, amarilla discontinua, zig-zag."),
               ("No stopping or parking: bends, brows, tunnels, level and pedestrian crossings, cycle lanes, junctions, bus lanes, motorways, tram rails, continuous yellow line.",
                "Prohibido parar y estacionar: curvas, rasantes, túneles, pasos a nivel y de peatones, carriles bici, intersecciones, carril bus, autopistas, raíles, amarilla continua."),
               ("Serious when parking: loading zone in use, double parking without driver, bus stop, emergency spaces, middle of the road.",
                "Grave al estacionar: carga y descarga en uso, doble fila sin conductor, parada de bus, espacios de urgencia, medio de la calzada."),
               ("Serious when stopping or parking: under 3 m to the opposite edge or continuous line, blocking a vado, exits, dropped kerbs, medians or islands, turns.",
                "Grave al parar o estacionar: menos de 3 m al borde opuesto o línea continua, vados, salidas, pasos rebajados, medianas o isletas, giros.")],
        trap=("Mixing up the broken yellow line (no parking) with the continuous one (no stopping either).", "Confundir la amarilla discontinua (no estacionar) con la continua (ni parar).")),
    "secure": dict(sec=9, en="Securing a parked vehicle", es="Inmovilizar correctamente",
        recap=[("Engine off, starting system disconnected, parking brake on, lights if needed, protect against unauthorised use.", "Motor apagado, arranque desconectado, freno de estacionamiento, luces si hace falta, evitar el uso sin autorización."),
               ("Slope: 1st gear uphill, reverse downhill, P for automatics.", "Pendiente: primera si sube, marcha atrás si baja, P en automáticos."),
               ("Over 3,500 kg, buses and combinations: proper chocks (never stones) or a front wheel against the kerb.", "Más de 3.500 kg, autobuses y conjuntos: calzos adecuados (nunca piedras) o rueda contra el bordillo."),
               ("Motorhomes: nothing beyond the outline, only on tyres (chocks allowed), no fluids.", "Autocaravanas: nada fuera del perímetro, solo sobre neumáticos (calzos permitidos), sin verter fluidos.")],
        trap=("Leaving reverse engaged facing uphill.", "Dejar la marcha atrás puesta cuesta arriba.")),
}


# ---------------------------------------------------------------- 1. basics
Q("bs1", "basics", "A manoeuvre is…", "Una maniobra es…",
  [("a noticeable change the driver makes that the road layout does not impose", "una alteración sensible que realiza el conductor y que no impone el trazado de la vía"),
   ("any movement of the vehicle", "cualquier movimiento del vehículo"), ("following the bends of the road", "seguir las curvas de la vía")],
  "The opposite of normal progression.", "Lo contrario de la progresión normal.")
Q("bs2", "basics", "What does RSM stand for?", "¿Qué significa RSM?",
  [("Mirror, signal, manoeuvre", "Retrovisor, señalizar, maniobra"), ("Reduce, stop, move", "Reducir, señalizar, mover"), ("Right, speed, mirror", "Derecha, señalizar, mirar")],
  "Together with PVO: position, speed, observation.", "Junto a PVO: posición, velocidad, observación.")
Q("bs3", "basics", "Which of these is NOT a manoeuvre?", "¿Cuál de estas NO es una maniobra?",
  [("Following a bend in the road", "Seguir el trazado de una curva"), ("Turning into another road", "Girar para entrar en otra vía"), ("Overtaking", "Adelantar")],
  "Nor is stopping at a red light, or reversing on its own.", "Tampoco detenerse ante un semáforo en rojo, ni la marcha atrás por sí sola.")
Q("bs4", "basics", "Reversing is…", "La marcha atrás es…",
  [("a complementary manoeuvre, not a basic one", "una maniobra complementaria, no básica"), ("a basic manoeuvre", "una maniobra básica"), ("never allowed", "algo nunca permitido")],
  "It complements parking or joining traffic.", "Complementa al estacionamiento o a la incorporación.")
Q("bs5", "basics", "In short, every manoeuvre means…", "En resumen, toda maniobra consiste en…",
  [("observe, signal and carry out", "observar, señalizar y realizar"), ("signal, carry out and observe", "señalizar, realizar y observar"), ("brake, signal and turn", "frenar, señalizar y girar")],
  "Always in that order.", "Siempre en ese orden.")
Q("bs6", "basics", "Stopping at a red light is…", "Detenerse ante un semáforo en rojo es…",
  [("a detention, not a manoeuvre", "una detención, no una maniobra"), ("a stop (parada)", "una parada"), ("a basic manoeuvre", "una maniobra básica")],
  "It is imposed, not chosen.", "Viene impuesta, no es voluntaria.")
Q("bs7", "basics", "What does PVO stand for?", "¿Qué significa PVO?",
  [("Position, speed, observation", "Posición, velocidad, observación"), ("Priority, warning, overtaking", "Prioridad, aviso, adelantamiento"), ("Pedal, gear, steering", "Pedal, velocidad, orientación")],
  "Another safety routine before any manoeuvre.", "Otra regla de seguridad antes de cualquier maniobra.")

# ---------------------------------------------------------------- 2.1 optical
Q("op1", "optical", "How long must the indicator stay on?", "¿Cuánto tiempo debe estar encendido el intermitente?",
  [("For the whole manoeuvre, off when it ends", "Todo el tiempo que dure la maniobra y apagarse al finalizar"), ("Three flashes", "Tres destellos"), ("Only before starting", "Solo antes de empezar")],
  "It must announce the manoeuvre clearly and in good time.", "Debe advertirla de forma clara y con antelación.")
Q("op2", "optical", "The driver’s arm out of the window, straight and horizontal, means…", "El brazo del conductor extendido horizontalmente por la ventanilla indica…",
  [("moving or turning left", "desplazamiento o giro a la izquierda"), ("moving or turning right", "desplazamiento o giro a la derecha"), ("slowing down", "frenar")],
  "With the palm facing backwards it means reversing.", "Con la palma hacia atrás indica marcha atrás.")
Q("op3", "optical", "Left arm out with the forearm raised and the hand open means…", "Brazo izquierdo con el antebrazo levantado y la mano abierta indica…",
  [("moving or turning right", "desplazamiento o giro a la derecha"), ("moving or turning left", "desplazamiento o giro a la izquierda"), ("stop immediately", "detención inmediata")],
  "The arm points the way you will go.", "El antebrazo señala el lado hacia el que vas.")
Q("op4", "optical", "The indicator shows left but the arm signals right. Which counts?", "El intermitente indica izquierda y el brazo indica derecha. ¿Cuál vale?",
  [("The arm signal", "La del brazo"), ("The indicator", "La del intermitente"), ("Neither: stop", "Ninguna: hay que parar")],
  "Arm signals prevail over light signals.", "Las advertencias con el brazo prevalecen sobre las luminosas.")
Q("op5", "optical", "Moving the arm up and down out of the window means…", "Mover el brazo de arriba abajo por la ventanilla indica…",
  [("I am going to slow down or brake considerably", "voy a reducir la marcha o frenar considerablemente"), ("you can overtake me", "puedes adelantarme"), ("I am turning right", "voy a girar a la derecha")],
  "The light equivalent is the brake lights.", "Su equivalente luminoso son las luces de freno.")
Q("op6", "optical", "Which arm is normally used for arm signals?", "¿Qué brazo se usa normalmente para las señales?",
  [("The left", "El izquierdo"), ("The right", "El derecho"), ("Either, it makes no difference", "Cualquiera, da igual")],
  "Through the driver’s window.", "Por la ventanilla del conductor.")
Q("op7", "optical", "For an arm signal to be valid it must be…", "Para que una señal con el brazo sea válida debe…",
  [("made correctly and visible to all road users", "hacerse correctamente y ser visible para todos"), ("held for 5 seconds", "mantenerse 5 segundos"), ("made with both arms", "hacerse con los dos brazos")],
  "Otherwise it does not count as a warning.", "Si no, no sirve como advertencia.")

# ---------------------------------------------------------------- 2.2 horn and flashes
Q("hn1", "horn", "May you use the horn in town to avoid running someone over?", "¿Se puede usar el claxon en poblado para evitar un atropello?",
  [("Yes", "Sí"), ("No, never in town", "No, nunca en poblado"), ("Only at night", "Solo de noche")],
  "Avoiding an accident or running someone over: in and out of town.", "Evitar accidente o atropello: dentro y fuera de poblado.")
Q("hn2", "horn", "To announce an overtaking in town you may use…", "Para avisar de un adelantamiento en poblado se puede usar…",
  [("headlight flashes only", "solo ráfagas"), ("the horn only", "solo el claxon"), ("the horn and flashes", "claxon y ráfagas")],
  "The horn for overtaking is only allowed out of town.", "El claxon para adelantar solo se permite fuera de poblado.")
Q("hn3", "horn", "Out of town, to tell the driver ahead you will overtake, you may use…", "Fuera de poblado, para avisar al de delante de que vas a adelantar, puedes usar…",
  [("the horn or headlight flashes", "el claxon o las ráfagas"), ("only the horn", "solo el claxon"), ("the hazard lights", "la luz de emergencia")],
  "In town, only flashes.", "En poblado, solo ráfagas.")
Q("hn4", "horn", "Which of these uses of the horn is forbidden?", "¿Cuál de estos usos del claxon está prohibido?",
  [("Greeting a friend", "Saludar a un amigo"), ("Warning of danger on a narrow winding road", "Avisar en una vía estrecha con muchas curvas"), ("Avoiding an accident", "Evitar un accidente")],
  "Also forbidden: telling someone off or warning of police.", "También prohibido: recriminar o avisar de la presencia de agentes.")
Q("hn5", "horn", "The horn’s sound must be…", "El sonido del claxon debe ser…",
  [("continuous and steady, not shrill", "continuo y uniforme, no estridente"), ("a short melody", "una melodía corta"), ("as loud as possible", "lo más fuerte posible")],
  "No varied musical notes that could confuse.", "Sin notas musicales variadas que confundan.")
Q("hn6", "horn", "Headlight flashes must be…", "Las ráfagas de luz deben ser…",
  [("very short, to avoid dazzling", "a intervalos muy cortos, para no deslumbrar"), ("long, to be clearly seen", "largas, para verse bien"), ("only with the main beam", "solo con la luz de carretera")],
  "Dipped, main beam, or both alternately.", "Con luz de cruce, de carretera o ambas alternativamente.")
Q("hn7", "horn", "Flashing your headlights to warn oncoming drivers of a police check is…", "Hacer ráfagas para avisar a los que vienen de un control policial está…",
  [("forbidden", "prohibido"), ("allowed", "permitido"), ("allowed only out of town", "permitido solo fuera de poblado")],
  "Flashes follow the same limits as the horn.", "Las ráfagas siguen las mismas limitaciones que el claxon.")
Q("hn8", "horn", "Why may flashes replace the horn?", "¿Por qué las ráfagas pueden sustituir al claxon?",
  [("They make no noise pollution", "No producen contaminación acústica"), ("They are more visible at night only", "Solo son más visibles de noche"), ("They give you priority", "Dan prioridad")],
  "Same cases, quieter.", "Mismos casos, sin ruido.")

# ---------------------------------------------------------------- 3. joining
Q("jn1", "joining", "Which of these is joining traffic (incorporación)?", "¿Cuál de estas es una incorporación a la circulación?",
  [("Leaving a parking space", "Salir de un estacionamiento"), ("Moving off when the light turns green", "Arrancar cuando el semáforo se pone verde"),
   ("Moving off after an agent’s signal", "Reanudar la marcha tras la señal de un agente")],
  "Moving off after a detention is not joining.", "Reanudar la marcha tras una detención no es incorporarse.")
Q("jn2", "joining", "The first step to join traffic is…", "El primer paso para incorporarse es…",
  [("observe, directly and in the mirrors", "observar, directamente y por los retrovisores"), ("switch on the indicator", "poner el intermitente"), ("accelerate", "acelerar")],
  "If someone could be hindered, you may not start.", "Si se puede entorpecer a alguien, no se puede iniciar.")
Q("jn3", "joining", "You leave a garage across the pavement into the street. You must…", "Sales de un garaje cruzando la acera hacia la calle. Debes…",
  [("drive slowly enough to stop at once, giving way to vehicles and pedestrians from both sides", "circular a una velocidad que permita detenerte en el acto, cediendo a vehículos y peatones de ambos lados"),
   ("give way only to vehicles from the left", "ceder solo a los vehículos de la izquierda"), ("sound the horn and go out", "tocar el claxon y salir")],
  "From a building or private road, both sides have priority.", "Desde un inmueble o camino privado, ambos lados tienen prioridad.")
Q("jn4", "joining", "On an acceleration lane, where do you check that you can join safely?", "En un carril de aceleración, ¿dónde se comprueba que se puede incorporar con seguridad?",
  [("At the start of the lane, stopping there if necessary", "Al principio del carril, deteniéndose allí si es necesario"), ("At the end of the lane", "Al final del carril"),
   ("Only on the main carriageway", "Ya en la calzada principal")],
  "Then build up speed to join safely at its end.", "Después se acelera para incorporarse al final sin peligro.")
Q("jn5", "joining", "You join a road straight ahead, with no sideways move. How do you signal?", "Te incorporas de frente, sin desplazamiento lateral. ¿Cómo señalizas?",
  [("Briefly switch on the indicator for the side you join from", "Encender momentáneamente el intermitente del lado por el que te incorporas"), ("No signal is needed", "No hace falta señalizar"),
   ("Hazard lights", "Con la luz de emergencia")],
  "Otherwise, the indicator of the side you move to.", "En otro caso, el del lado hacia el que te desplazas.")
Q("jn6", "joining", "Heavy traffic stops you from joining. May you signal anyway?", "Un tráfico denso te impide incorporarte. ¿Puedes señalizar igualmente?",
  [("Yes, so others can make room", "Sí, para que los demás te la faciliten"), ("No, only when the road is clear", "No, solo con la vía libre"), ("Only with the horn", "Solo con el claxon")],
  "Signalling does not give you priority, though.", "Aun así, señalizar no da prioridad.")
Q("jn7", "joining", "When you join traffic, those already on the road…", "Al incorporarte, los que ya circulan por la vía…",
  [("have priority", "tienen prioridad"), ("must give way to you", "deben cederte el paso"), ("must stop", "deben detenerse")],
  "Join without making them change position or speed abruptly.", "Incorpórate sin que cambien bruscamente su posición o velocidad.")
Q("jn8", "joining", "Leaving a service area onto a motorway is…", "Salir de un área de servicio a la autopista es…",
  [("joining traffic", "una incorporación a la circulación"), ("a change of direction", "un cambio de dirección"), ("not a manoeuvre", "no es una maniobra")],
  "Entering another road from a service area or access road.", "Entrar en otra vía desde zonas de servicio o vías de acceso.")

# ---------------------------------------------------------------- 3.2 facilitate
Q("fc1", "facilitate", "In town, a bus signals to leave a signed stop. You must…", "En poblado, un autobús señaliza que sale de una parada señalizada. Debes…",
  [("move sideways or slow down, and stop if necessary, to let it out", "desplazarte lateralmente o reducir, deteniéndote si es preciso, para dejarle salir"),
   ("keep going, you have priority", "seguir, tienes prioridad"), ("sound the horn", "tocar el claxon")],
  "The bus driver still takes every precaution.", "El conductor del autobús debe igualmente extremar precauciones.")
Q("fc2", "facilitate", "Does the bus driver leaving a stop have to take precautions?", "¿Debe tomar precauciones el conductor del autobús que sale de la parada?",
  [("Yes, after signalling with the indicators", "Sí, tras anunciarlo con los intermitentes"), ("No, others must stop", "No, los demás deben detenerse"), ("Only out of town", "Solo fuera de poblado")],
  "To avoid any risk of accident.", "Para evitar todo riesgo de accidente.")
Q("fc3", "facilitate", "When you see someone trying to join traffic, you should…", "Cuando ves a alguien intentando incorporarse, debes…",
  [("help them as far as possible", "facilitarle la maniobra en la medida de lo posible"), ("speed up to pass first", "acelerar para pasar antes"), ("ignore them", "ignorarlo")],
  "Above all buses leaving a signed stop.", "Sobre todo a los autobuses que salen de una parada señalizada.")
Q("fc4", "facilitate", "To let a bus out of a stop in town you may slow down…", "Para dejar salir a un autobús en poblado puedes reducir la velocidad…",
  [("if it is safe and you signal correctly", "si puedes hacerlo sin peligro y señalizando correctamente"), ("always, without signalling", "siempre, sin señalizar"), ("never", "nunca")],
  "Or move sideways when possible.", "O desplazarte lateralmente cuando sea posible.")

# ---------------------------------------------------------------- 4. lateral
Q("lt1", "lateral", "A sideways move (desplazamiento lateral) is…", "El desplazamiento lateral es…",
  [("a change of position that takes you partly or fully into another lane", "un cambio de posición que invade parcial o totalmente otro carril"),
   ("a small correction within your own lane", "una corrección de trayectoria dentro del carril"), ("following a bend", "seguir una curva")],
  "It is also called a lane change.", "También se llama cambio de carril.")
Q("lt2", "lateral", "How long do you signal a sideways move?", "¿Hasta cuándo se señaliza un desplazamiento lateral?",
  [("Until the move is finished", "Hasta la finalización del desplazamiento"), ("Only before starting", "Solo antes de empezar"), ("Three seconds", "Tres segundos")],
  "Indicator or arm.", "Con el intermitente o el brazo.")
Q("lt3", "lateral", "When you move into another lane, who has priority?", "Al desplazarte a otro carril, ¿quién tiene prioridad?",
  [("The vehicle already in that lane", "El que ya circula por ese carril"), ("You, if you signalled", "Tú, si has señalizado"), ("The faster vehicle", "El más rápido")],
  "Signalling never gives priority.", "Señalizar nunca da prioridad.")
Q("lt4", "lateral", "How should a lane change be made?", "¿Cómo se debe hacer un cambio de carril?",
  [("Early, gradually and smoothly", "Con antelación, gradual y progresivamente"), ("Quickly, to spend less time between lanes", "Rápido, para estar menos tiempo entre carriles"), ("With a sharp turn of the wheel", "Con un volantazo")],
  "No sudden swerves.", "Sin brusquedades ni volantazos.")
Q("lt5", "lateral", "Which of these is a typical reason for a sideways move?", "¿Cuál es un motivo habitual de desplazamiento lateral?",
  [("Passing an immobilised vehicle", "Rebasar a un vehículo inmovilizado"), ("Following a bend", "Seguir una curva"), ("Braking at a red light", "Frenar ante un semáforo")],
  "Also turning, overtaking, parking, joining and signs.", "También girar, adelantar, estacionar, incorporarse y la señalización.")
Q("lt6", "lateral", "Before moving sideways you must first…", "Antes de desplazarte lateralmente debes primero…",
  [("check you will not hinder or endanger anyone", "comprobar que no entorpeces ni pones en peligro a nadie"), ("move and then look", "desplazarte y después mirar"), ("sound the horn", "tocar el claxon")],
  "Observe, signal, move.", "Observar, señalizar, realizar.")

# ---------------------------------------------------------------- 5 overtaking
Q("ov1", "overtake", "Overtaking is…", "El adelantamiento es…",
  [("passing a vehicle ahead that is going more slowly", "sobrepasar a un vehículo que circula delante más lento"), ("any lane change", "cualquier cambio de carril"), ("passing a parked car", "pasar junto a un coche estacionado")],
  "Passing an immobilised vehicle is called rebasar.", "Pasar a un inmovilizado se llama rebasar.")
Q("ov2", "overtake", "In a congested queue filling the carriageway, your lane moves faster than the next. Is that overtaking?", "En una cola congestionada que ocupa toda la calzada, tu carril avanza más rápido que el contiguo. ¿Es adelantamiento?",
  [("No, and you may not change lanes to overtake", "No, y no puedes cambiar de carril para adelantar"), ("Yes, a normal one", "Sí, uno normal"), ("Yes, on the right", "Sí, por la derecha")],
  "Only lane changes to get ready to turn or leave.", "Solo cambios para prepararse a girar o salir.")
Q("ov3", "overtake", "As a general rule you overtake…", "Como norma general se adelanta…",
  [("on the left", "por la izquierda"), ("on the right", "por la derecha"), ("on whichever side is free", "por el lado que esté libre")],
  "On the right only in specific cases.", "Por la derecha solo en casos concretos.")
Q("ov4", "overtake", "You may overtake on the right…", "Se puede adelantar por la derecha…",
  [("a vehicle clearly signalling a left turn", "a un vehículo que indica claramente que gira a la izquierda"), ("any slow vehicle on a motorway", "a cualquier vehículo lento en autopista"),
   ("a lorry going uphill", "a un camión en una subida")],
  "Also trams in the centre, and in town with 2+ marked lanes.", "También tranvías por el centro y en poblado con 2 o más carriles delimitados.")
Q("ov5", "overtake", "The vehicle ahead has signalled it will move left. You wanted to overtake it. You…", "El de delante ha señalizado que se desplaza a la izquierda. Querías adelantarlo. Tú…",
  [("let it go first", "le dejas pasar primero"), ("overtake quickly before it moves", "adelantas rápido antes de que se mueva"), ("overtake on the right", "adelantas por la derecha")],
  "If it does not move after a reasonable time, you may overtake after warning it.", "Si tras un tiempo prudencial no se desplaza, puedes adelantar avisándole.")
Q("ov6", "overtake", "Halfway through an overtaking you see you cannot finish safely. You…", "A mitad de un adelantamiento ves que no puedes terminarlo con seguridad. Tú…",
  [("slow down quickly and pull back into the right lane, signalling", "reduces rápidamente la velocidad y regresas al carril derecho, señalizándolo"),
   ("accelerate hard to finish", "aceleras a fondo para terminar"), ("stay in the left lane", "sigues en el carril izquierdo")],
  "The overtaken vehicle must let you back in.", "El adelantado debe facilitarte la vuelta.")
Q("ov7", "overtake", "When do you return to the right lane after overtaking?", "¿Cuándo vuelves al carril derecho tras adelantar?",
  [("As soon as possible, gradually, when you see the overtaken vehicle in the mirror", "Tan pronto como sea posible, gradualmente, al ver al adelantado por el espejo"),
   ("Immediately after passing its front", "Justo después de rebasar su parte delantera"), ("Only at the next junction", "En la siguiente intersección")],
  "Without forcing anyone to change path or speed.", "Sin obligar a nadie a modificar su trayectoria o velocidad.")
Q("ov8", "overtake", "Two-way road with three lanes and broken lines: where do you overtake?", "Vía de doble sentido con tres carriles y líneas discontinuas: ¿por dónde se adelanta?",
  [("Only in the centre lane, if oncoming drivers are not using it", "Solo por el carril central, si no lo ocupan los que vienen de frente"), ("In the left lane", "Por el carril izquierdo"),
   ("In any lane", "Por cualquier carril")],
  "The left lane belongs to the opposite direction.", "El carril izquierdo es del sentido contrario.")
Q("ov9", "overtake", "Cyclists riding in a group pass each other. Is that overtaking?", "Ciclistas que circulan en grupo se adelantan entre sí. ¿Es adelantamiento?",
  [("No", "No"), ("Yes", "Sí"), ("Only out of town", "Solo fuera de poblado")],
  "Nor is going faster in a bus or acceleration lane.", "Tampoco circular más rápido por un carril bus o de aceleración.")
Q("ov10", "overtake", "Why should you not follow too closely before overtaking?", "¿Por qué no hay que ir demasiado pegado antes de adelantar?",
  [("It reduces your view and the room to react", "Reduce el campo de visión y hay peligro de colisión"), ("It uses more fuel", "Gasta más combustible"), ("It is only a courtesy rule", "Es solo cortesía")],
  "Too far back is no good either: you need more time and distance.", "Muy lejos tampoco: se necesita más tiempo y distancia.")
Q("ov11", "overtake", "On a one-way road with two lanes, after overtaking you want to overtake again. You may…", "En una vía de sentido único con dos carriles, tras adelantar quieres volver a adelantar. Puedes…",
  [("stay in the left lane if you do not bother faster vehicles behind", "permanecer en el carril izquierdo si no molestas a los que vienen más rápido"),
   ("never stay in the left lane", "nunca permanecer en el carril izquierdo"), ("use the shoulder", "usar el arcén")],
  "Otherwise return to the right.", "Si no, vuelve a la derecha.")

# ---------------------------------------------------------------- 5.2 gap
Q("gp1", "gap", "Minimum side gap when overtaking a cyclist", "Separación lateral mínima al adelantar a un ciclista",
  [("1.5 m", "1,5 m"), ("1 m", "1 m"), ("2 m", "2 m")], "In and out of town.", "Dentro y fuera de poblado.")
Q("gp2", "gap", "Out of town you overtake a cyclist. Besides the 1.5 m gap you must…", "Fuera de poblado adelantas a un ciclista. Además de 1,5 m de separación debes…",
  [("drive at least 20 km/h below the road’s limit", "reducir la velocidad 20 km/h respecto al límite de la vía"), ("sound the horn twice", "tocar el claxon dos veces"),
   ("switch on the hazard lights", "encender la luz de emergencia")],
  "Also for pedestrians, animals, mopeds, VMP and animal-drawn vehicles.", "También con peatones, animales, ciclomotores, VMP y tracción animal.")
Q("gp3", "gap", "Overtaking a broken-down vehicle in town, must you reduce speed by 20 km/h?", "Al adelantar a un vehículo averiado en poblado, ¿hay que reducir 20 km/h?",
  [("Yes, in and out of town", "Sí, dentro y fuera de poblado"), ("No, only out of town", "No, solo fuera de poblado"), ("No, never", "No, nunca")],
  "Same for assistance vehicles at work.", "Igual con los vehículos de auxilio trabajando.")
Q("gp4", "gap", "On a road with two lanes your way, you overtake a cyclist. You must…", "En una vía con dos carriles por tu sentido adelantas a un ciclista. Debes…",
  [("change lanes completely", "cambiar completamente de carril"), ("keep at least half the car in the right lane", "mantener medio coche en el carril derecho"), ("stay in your lane with 1 m", "seguir en tu carril con 1 m")],
  "With one lane per direction, partly or fully into the next lane.", "Con un carril por sentido, ocupando parcial o totalmente el contiguo.")
Q("gp5", "gap", "Overtaking a car (not a vulnerable user), the side gap must be…", "Al adelantar a un turismo (no vulnerable), la separación lateral debe ser…",
  [("proportional to the speed and the road", "proporcional a la velocidad y a la vía"), ("at least 1.5 m always", "de al menos 1,5 m siempre"), ("at least 3 m", "de al menos 3 m")],
  "Width and features of the carriageway.", "Anchura y características de la calzada.")
Q("gp6", "gap", "A motorcyclist overtakes a lorry out of town. Minimum side gap?", "Un motorista adelanta a un camión fuera de poblado. ¿Separación mínima?",
  [("1.5 m", "1,5 m"), ("0.5 m", "0,5 m"), ("1 m", "1 m")], "Two-wheelers overtaking out of town keep 1.5 m too.", "Los de dos ruedas que adelantan fuera de poblado también guardan 1,5 m.")
Q("gp7", "gap", "A group of cyclists comes the other way, on the shoulder. You may overtake a car if…", "Un grupo de ciclistas viene de frente por el arcén. Puedes adelantar a un turismo si…",
  [("it does not endanger or hinder the cyclists", "no pones en peligro ni entorpeces a los ciclistas"), ("they are on the shoulder, so always", "van por el arcén, así que siempre"), ("you sound the horn", "tocas el claxon")],
  "It is expressly forbidden to endanger oncoming cyclists, even on the shoulder.", "Está expresamente prohibido poner en peligro a ciclistas de frente, aunque vayan por el arcén.")

# ---------------------------------------------------------------- 5.3 overtaken
Q("od1", "overtaken", "When someone overtakes you, you must…", "Cuando alguien te adelanta, debes…",
  [("keep to the right edge, without using the shoulder", "ceñirte al borde derecho sin pisar el arcén"), ("move onto the shoulder", "meterte en el arcén"), ("speed up to finish sooner", "acelerar para que acabe antes")],
  "If you want to turn left, keep left instead.", "Si quieres girar a la izquierda, cíñete a la izquierda.")
Q("od2", "overtaken", "May the vehicle being overtaken speed up?", "¿Puede acelerar el vehículo que está siendo adelantado?",
  [("No", "No"), ("Yes, if the road allows", "Sí, si la vía lo permite"), ("Yes, out of town", "Sí, fuera de poblado")],
  "Nor make the overtaking harder in any way.", "Ni dificultar el adelantamiento de ninguna manera.")
Q("od3", "overtaken", "The overtaking driver gives up and brakes. You (being overtaken)…", "El que te adelanta desiste y frena. Tú (adelantado)…",
  [("make it easy for them to get back in", "le facilitas la vuelta al carril"), ("keep your speed", "mantienes la velocidad"), ("speed up", "aceleras")],
  "Usually by easing off.", "Normalmente levantando el pie.")
Q("od4", "overtaken", "A lorry driver moves an arm from back to front out of the window. It means…", "Un camionero mueve el brazo de atrás hacia delante por la ventanilla. Significa…",
  [("you can overtake me", "puedes adelantarme"), ("do not overtake", "no adelantes"), ("I am turning left", "voy a girar a la izquierda")],
  "It may also use the right indicator.", "También puede usar el intermitente derecho.")
Q("od5", "overtaken", "A slow, large vehicle sees heavy oncoming traffic and a queue behind it. It should…", "Un vehículo lento y grande ve mucho tráfico de frente y una cola detrás. Debe…",
  [("slow down or pull onto a usable shoulder as soon as possible", "aminorar la marcha o apartarse al arcén practicable cuanto antes"), ("keep going at the same speed", "seguir igual"),
   ("speed up", "acelerar")],
  "To let others overtake safely.", "Para que puedan adelantarlo con seguridad.")
Q("od6", "overtaken", "Once the overtaking has started, a danger appears. The vehicle being overtaken must…", "Iniciado el adelantamiento, surge un peligro. El vehículo adelantado debe…",
  [("slow down", "disminuir la velocidad"), ("speed up", "aumentar la velocidad"), ("move to the left", "desplazarse a la izquierda")],
  "So the overtaker can finish or pull back in.", "Para que el otro termine o vuelva.")

# ---------------------------------------------------------------- 5.4-5.5 where forbidden
Q("no1", "noovertake", "Overtaking is forbidden…", "Está prohibido adelantar…",
  [("on bends and brows with reduced visibility", "en curvas y cambios de rasante de visibilidad reducida"), ("on straight roads", "en rectas"), ("on motorways", "en autopistas")],
  "Unless the directions are clearly separated and you do not enter the other.", "Salvo que los sentidos estén claramente delimitados y no invadas el contrario.")
Q("no2", "noovertake", "May you overtake a motorcycle at a junction?", "¿Se puede adelantar a una motocicleta en una intersección?",
  [("Yes, two-wheelers may be overtaken there", "Sí, a los vehículos de dos ruedas se les puede adelantar"), ("No, never at junctions", "No, nunca en intersecciones"), ("Only on the right", "Solo por la derecha")],
  "Also allowed at roundabouts and where you have signed priority.", "También en glorietas y con prioridad señalizada.")
Q("no3", "noovertake", "Is overtaking allowed at a roundabout?", "¿Está permitido adelantar en una glorieta?",
  [("Yes, roundabouts are an exception", "Sí, las glorietas son una excepción"), ("No, it is a junction", "No, es una intersección"), ("Only lorries", "Solo a camiones")],
  "Roundabouts and circulating squares.", "Glorietas y plazas de circulación giratoria.")
Q("no4", "noovertake", "Overtaking near a level crossing is…", "Adelantar en las proximidades de un paso a nivel está…",
  [("forbidden", "prohibido"), ("allowed if no train is coming", "permitido si no viene el tren"), ("allowed with barriers up", "permitido con las barreras subidas")],
  "Same for pedestrian crossings and junctions with cycle routes.", "Igual en pasos de peatones e intersecciones con vías ciclistas.")
Q("no5", "noovertake", "In a tunnel with two lanes in your direction, may you overtake?", "En un túnel con dos carriles para tu sentido, ¿puedes adelantar?",
  [("Yes", "Sí"), ("No, never in tunnels", "No, nunca en túneles"), ("Only by day", "Solo de día")],
  "Forbidden only with one lane your way.", "Prohibido solo con un carril para tu sentido.")
Q("no6", "noovertake", "A broken-down car blocks your lane on a stretch with a continuous line. You may…", "Un turismo averiado bloquea tu carril en un tramo con línea continua. Puedes…",
  [("pass it using the other half of the road, after checking there is no danger", "rebasarlo ocupando el sentido contrario, tras asegurarte de que no hay peligro"),
   ("never cross the continuous line", "nunca cruzar la línea continua"), ("pass it on the shoulder", "pasarlo por el arcén")],
  "If it has stopped because of traffic, stay behind.", "Si está detenido por necesidades del tráfico, quédate detrás.")
Q("no7", "noovertake", "A car is stopped ahead because of the traffic (a queue). Continuous line. You…", "Un turismo está detenido delante por el tráfico (una cola). Línea continua. Tú…",
  [("stay behind it", "te quedas detrás"), ("pass it on the left", "lo rebasas por la izquierda"), ("pass it on the shoulder", "lo rebasas por el arcén")],
  "Only obstacles and broken-down vehicles may be passed across the line.", "Solo se rebasan obstáculos y vehículos averiados.")
Q("no8", "noovertake", "Continuous line: a tractor at 20 km/h. May you overtake it across the line?", "Línea continua: un tractor a 20 km/h. ¿Puedes adelantarlo cruzando la línea?",
  [("Yes, if it can be done without risk", "Sí, si se puede hacer sin riesgo"), ("No, never", "No, nunca"), ("Only on the right", "Solo por la derecha")],
  "Agricultural special vehicles, cycles, mopeds, VMP, pedestrians and animals.", "Especiales agrícolas, ciclos, ciclomotores, VMP, peatones y animales.")
Q("no9", "noovertake", "A large lorry ahead of you is overtaking and hides the road ahead. You…", "Un camión grande delante de ti está adelantando y te tapa la vista. Tú…",
  [("may not overtake behind it", "no puedes adelantar detrás de él"), ("may follow it closely", "puedes seguirle pegado"), ("may overtake both", "puedes adelantar a ambos")],
  "Lack of visibility.", "Falta de visibilidad.")
Q("no10", "noovertake", "May you overtake a vehicle that is already overtaking another, if you must enter the opposite direction?", "¿Puedes adelantar a un vehículo que ya está adelantando a otro, si tienes que invadir el sentido contrario?",
  [("No", "No"), ("Yes, if fast enough", "Sí, si eres más rápido"), ("Yes, out of town", "Sí, fuera de poblado")],
  "A double overtaking into the opposite lane is forbidden.", "El doble adelantamiento invadiendo el sentido contrario está prohibido.")

# ---------------------------------------------------------------- 6. turning
Q("tr1", "turning", "Before turning right, you keep…", "Antes de girar a la derecha te ciñes…",
  [("as close as possible to the right edge", "todo lo posible al borde derecho"), ("to the centre of the road", "al eje de la calzada"), ("to the left lane", "al carril izquierdo")],
  "And signal in good time.", "Y señalizas con antelación.")
Q("tr2", "turning", "Turning left from a one-way road, you keep…", "Para girar a la izquierda en una vía de sentido único te ciñes…",
  [("as close as possible to the left edge", "todo lo posible al borde izquierdo"), ("to the right edge", "al borde derecho"), ("to the centre", "al centro")],
  "On two-way roads you keep to the centre instead.", "En doble sentido, al eje o a la marca central.")
Q("tr3", "turning", "Two-way road with three lanes separated by broken lines: to turn left you position…", "Vía de doble sentido con tres carriles separados por discontinuas: para girar a la izquierda te colocas…",
  [("in the centre lane", "en el carril central"), ("in the left lane", "en el carril izquierdo"), ("in the right lane", "en el carril derecho")],
  "The left lane belongs to oncoming traffic.", "El izquierdo es del sentido contrario.")
Q("tr4", "turning", "Two-way road with no centre marking: to turn left you keep…", "Vía de doble sentido sin marca central: para girar a la izquierda te ciñes…",
  [("to the centre of the road, without entering the other half", "al eje de la calzada, sin invadir el sentido contrario"), ("to the left edge", "al borde izquierdo"), ("to the right edge", "al borde derecho")],
  "With a marking, keep next to it without crossing.", "Con marca, ceñirse a ella sin rebasarla.")
Q("tr5", "turning", "Is following the curve of a bend a change of direction?", "¿Seguir el trazado de una curva es un cambio de dirección?",
  [("No", "No"), ("Yes", "Sí"), ("Only on motorways", "Solo en autopistas")],
  "A change of direction is to use another road, carriageway, or leave the road.", "El cambio de dirección es para usar otra vía, otra calzada o salir de la vía.")
Q("tr6", "turning", "Leaving a motorway by a deceleration lane, where do you slow down?", "Al salir de una autopista por un carril de deceleración, ¿dónde reduces la velocidad?",
  [("Inside the deceleration lane, after entering it as soon as possible", "Dentro del carril de deceleración, tras entrar en él lo antes posible"),
   ("On the main carriageway before the exit", "En la calzada principal antes de la salida"), ("On the shoulder", "En el arcén")],
  "Signal early and move to the lane next to it first.", "Señaliza con antelación y colócate antes en el carril más próximo.")
Q("tr7", "turning", "Out of town, a cyclist wants to turn left and there is no special lane. They should…", "Fuera de poblado, un ciclista quiere girar a la izquierda y no hay carril especial. Debe…",
  [("wait on the right-hand shoulder if possible and start from there", "colocarse en el arcén derecho si es posible e iniciar el giro desde allí"),
   ("move to the centre of the road", "colocarse en el centro de la calzada"), ("dismount always", "bajarse siempre")],
  "Same for two-wheeled mopeds.", "Igual los ciclomotores de dos ruedas.")
Q("tr8", "turning", "At a roundabout or square you leave the centre…", "En una glorieta o plaza se deja el centro…",
  [("on your left, unless the road is designed otherwise", "a la izquierda, salvo que la vía esté acondicionada para otra cosa"), ("on your right", "a la derecha"), ("on either side", "a cualquier lado")],
  "The usual direction around a roundabout.", "Es el sentido habitual de giro.")

# ---------------------------------------------------------------- 7. U-turn
Q("ut1", "uturn", "A U-turn (cambio de sentido) must be made…", "El cambio de sentido debe hacerse…",
  [("in one go, without reversing", "de un solo giro y sin marcha atrás"), ("with as many manoeuvres as needed", "con las maniobras que hagan falta"), ("always reversing first", "siempre con marcha atrás primero")],
  "At a suitable place, in the least time possible.", "En un lugar adecuado y en el menor tiempo posible.")
Q("ut2", "uturn", "Waiting to turn round holds up the traffic behind you. You…", "Esperar para cambiar de sentido retiene a los de detrás. Tú…",
  [("leave the carriageway on the right, if possible, and wait", "sales de la calzada por la derecha, si es posible, y esperas"), ("keep waiting in the lane", "sigues esperando en el carril"),
   ("turn round quickly", "cambias de sentido rápido")],
  "Until traffic allows it.", "Hasta que la circulación lo permita.")
Q("ut3", "uturn", "Is a U-turn allowed on an autovía through an open gap in the median?", "¿Se puede cambiar de sentido en una autovía por un paso abierto en la mediana?",
  [("No, never", "No, nunca"), ("Yes, if no one is coming", "Sí, si no viene nadie"), ("Yes, at night", "Sí, de noche")],
  "Only at points built for it at a different level.", "Solo en los lugares habilitados a distinto nivel.")
Q("ut4", "uturn", "Is a U-turn allowed near a level crossing?", "¿Está permitido cambiar de sentido en las proximidades de un paso a nivel?",
  [("Yes, near it; on the crossing itself no", "Sí, en sus proximidades; en el propio paso, no"), ("No, neither on it nor near it", "No, ni en él ni cerca"), ("Only with barriers up", "Solo con las barreras subidas")],
  "A classic difference from overtaking.", "Una diferencia clásica con el adelantamiento.")
Q("ut5", "uturn", "At which junctions is a U-turn allowed?", "¿En qué intersecciones está permitido cambiar de sentido?",
  [("Where you have signed priority, and at roundabouts", "Donde se tenga prioridad señalizada y en glorietas"), ("At any junction", "En cualquier intersección"), ("Never at junctions", "Nunca en intersecciones")],
  "Otherwise, forbidden at junctions and near them.", "En otro caso, prohibido en intersecciones y sus proximidades.")
Q("ut6", "uturn", "Which of these forbids a U-turn?", "¿Cuál de estas prohíbe el cambio de sentido?",
  [("A continuous line", "Una línea continua"), ("A broken line", "Una línea discontinua"), ("A blue information sign", "Una señal azul informativa")],
  "Also no-U-turn, no-left-turn, no-overtaking and one-way signs.", "También las señales de prohibido el cambio de sentido, giro a la izquierda, adelantamiento y sentido único.")
Q("ut7", "uturn", "To turn round you signal…", "Para cambiar de sentido se señaliza…",
  [("that you will slow down a lot and move sideways", "la intención de frenar considerablemente y el desplazamiento lateral"), ("only with the horn", "solo con el claxon"),
   ("nothing, it is not needed", "nada, no es necesario")],
  "With lights or the arm.", "Con los dispositivos luminosos o el brazo.")

# ---------------------------------------------------------------- 8. reversing
Q("rv1", "reverse", "As a general rule, driving in reverse is…", "Como norma general, circular marcha atrás está…",
  [("forbidden", "prohibido"), ("allowed up to 50 m", "permitido hasta 50 m"), ("allowed in town", "permitido en poblado")],
  "Exceptionally when you cannot go forward, turn or turn round.", "Excepcionalmente cuando no se puede ir hacia delante, girar ni cambiar de sentido.")
Q("rv2", "reverse", "Reversing to park, the distance may not exceed…", "Al dar marcha atrás para estacionar, el recorrido no puede superar…",
  S("15 m", "25 m", "50 m"), "And may not enter any junction.", "Ni invadir ninguna intersección.")
Q("rv3", "reverse", "Reversing on an autovía is…", "La marcha atrás en una autovía está…",
  [("forbidden", "prohibida"), ("allowed up to 15 m", "permitida hasta 15 m"), ("allowed on the shoulder", "permitida por el arcén")],
  "Also on autopistas.", "También en autopistas.")
Q("rv4", "reverse", "The arm signal for reversing is…", "La señal con el brazo para la marcha atrás es…",
  [("arm horizontal, palm facing backwards", "brazo horizontal con la palma de la mano hacia atrás"), ("arm raised vertically", "brazo levantado en vertical"), ("arm moved up and down", "brazo de arriba abajo")],
  "Or the reversing light, which comes on by itself.", "O la luz de marcha atrás, que se enciende sola.")
Q("rv5", "reverse", "You cannot see well behind before reversing. You may…", "No ves bien detrás antes de dar marcha atrás. Puedes…",
  [("get out and look, or follow another person’s directions", "bajarte a mirar o seguir las indicaciones de otra persona"), ("reverse quickly to spend less time", "dar marcha atrás rápido para tardar menos"),
   ("sound the horn and go", "tocar el claxon y retroceder")],
  "Without total safety, do not do it.", "Sin seguridad total, hay que desistir.")
Q("rv6", "reverse", "Reversing may complement…", "La marcha atrás puede complementar…",
  [("stopping, parking and joining traffic", "la parada, el estacionamiento y la incorporación"), ("overtaking", "el adelantamiento"), ("turning round on a motorway", "el cambio de sentido en autopista")],
  "A U-turn must be done without reversing.", "El cambio de sentido se hace sin marcha atrás.")

# ---------------------------------------------------------------- 9. stops, breakdowns, V-16
Q("st1", "stops", "A stop (parada) is a voluntary immobilisation lasting…", "La parada es una inmovilización voluntaria de…",
  [("less than 2 minutes, without the driver abandoning the vehicle", "menos de 2 minutos, sin que el conductor abandone el vehículo"), ("less than 5 minutes", "menos de 5 minutos"),
   ("any time, if the driver stays inside", "cualquier duración si el conductor sigue dentro")],
  "The driver may get out if they keep watching it.", "El conductor puede bajarse si lo tiene vigilado.")
Q("st2", "stops", "Stopping because an agent tells you to is…", "Detenerse porque lo ordena un agente es…",
  [("a detention", "una detención"), ("a stop (parada)", "una parada"), ("parking", "un estacionamiento")],
  "Imposed, not voluntary; not a manoeuvre.", "Impuesta, no voluntaria; no es maniobra.")
Q("st3", "stops", "Your car breaks down but can still move slowly on an autovía and needs help. You…", "Tu turismo se avería pero puede moverse despacio por una autovía y necesita auxilio. Tú…",
  [("leave the lanes and head for the first exit on the right shoulder", "abandonas los carriles y te diriges a la primera salida por el arcén derecho"),
   ("stop in the right lane", "te detienes en el carril derecho"), ("drive on in the left lane slowly", "sigues despacio por el carril izquierdo")],
  "If that is not possible, stop on the right shoulder.", "Si no es posible, detente en el arcén derecho.")
Q("st4", "stops", "Your car is stuck on the shoulder of an autovía and there is a safe place beyond the barrier. Occupants…", "Tu turismo queda inmovilizado en el arcén de una autovía y hay un lugar seguro tras la barrera. Los ocupantes…",
  [("get out on the side away from the traffic and wait there", "salen por el lado contrario al tráfico y esperan allí"), ("stay inside with belts on", "se quedan dentro con el cinturón"),
   ("wait on the shoulder behind the car", "esperan en el arcén detrás del coche")],
  "If they cannot get out safely, they stay inside with belts fastened.", "Si no pueden salir con seguridad, se quedan dentro con el cinturón.")
Q("st5", "stops", "Where do you place the V-16 light?", "¿Dónde se coloca la señal V-16?",
  [("On the highest point of the vehicle, usually the roof", "En la parte más alta del vehículo, normalmente el techo"), ("50 m behind the car", "50 m por detrás del vehículo"),
   ("Inside, on the dashboard", "Dentro, en el salpicadero")],
  "It is magnetic and visible 360°.", "Es imantada y visible en 360°.")
Q("st6", "stops", "Is the V-16 compulsory for motorcycles?", "¿Es obligatoria la V-16 para motocicletas?",
  [("No, it is recommended", "No, es recomendable"), ("Yes", "Sí"), ("Only out of town", "Solo fuera de poblado")],
  "Compulsory for cars, vans, buses, mixed vehicles, lorries and combinations.", "Obligatoria para turismos, furgonetas, autobuses, mixtos, camiones y conjuntos.")
Q("st7", "stops", "You place a warning triangle but no V-16. Is that correct?", "Colocas un triángulo pero no la V-16. ¿Es correcto?",
  [("No: the triangle does not replace the V-16", "No: el triángulo no sustituye a la V-16"), ("Yes, either is fine", "Sí, cualquiera vale"), ("Yes, by day", "Sí, de día")],
  "The triangle may be added, never instead.", "El triángulo puede añadirse, nunca sustituirla.")
Q("st8", "stops", "When must you wear the reflective vest?", "¿Cuándo hay que ponerse el chaleco reflectante?",
  [("When you get out onto the carriageway or shoulder of an interurban road, day or night", "Al salir y ocupar la calzada o el arcén de una vía interurbana, de día o de noche"),
   ("Only at night", "Solo de noche"), ("Only on motorways", "Solo en autopistas")],
  "It must be an approved high-visibility vest.", "Chaleco homologado de alta visibilidad.")
Q("st9", "stops", "After a minor accident on a road, where do you fill in the accident report?", "Tras un accidente leve en carretera, ¿dónde se rellena el parte?",
  [("In a safe place off the road", "En un lugar seguro fuera de la vía"), ("On the shoulder next to the cars", "En el arcén junto a los coches"), ("Inside the car on the carriageway", "Dentro del coche en la calzada")],
  "Filling it in on the road platform is forbidden.", "Está prohibido hacerlo en la plataforma.")
Q("st10", "stops", "A connected V-16 sends its location to…", "Una V-16 conectada envía su ubicación a…",
  [("the national traffic access point, with no app needed", "el punto de acceso nacional de tráfico, sin necesidad de app"), ("your mobile phone only", "solo a tu móvil"), ("the nearest police car", "la patrulla más cercana")],
  "Communications are included for 12 years.", "Las comunicaciones están incluidas durante 12 años.")

# ---------------------------------------------------------------- 9.1.1 tunnels
Q("tu1", "tunnel", "Your car breaks down in a tunnel but can still move. You…", "Tu turismo se avería en un túnel pero puede seguir. Tú…",
  [("drive out of the tunnel", "sales del túnel"), ("stop at once on the right", "te detienes en el acto a la derecha"), ("turn round", "cambias de sentido")],
  "If you cannot, go to the nearest emergency lay-by.", "Si no puedes, al apartadero de emergencia más próximo.")
Q("tu2", "tunnel", "Fire in a tunnel: you leave the car…", "Incendio en un túnel: dejas el coche…",
  [("with the engine off, the key in and the doors open", "con el motor apagado, la llave puesta y las puertas abiertas"), ("locked, taking the key", "cerrado y con la llave"), ("with the engine running", "con el motor en marcha")],
  "So emergency crews can move it.", "Para que los servicios de emergencia puedan moverlo.")
Q("tu3", "tunnel", "Fire in a tunnel: occupants walk to the nearest refuge or exit…", "Incendio en un túnel: los ocupantes van al refugio o salida más próximos…",
  [("away from the fire", "en sentido contrario al fuego"), ("towards the fire, to help", "hacia el fuego, para ayudar"), ("along the carriageway", "por la calzada")],
  "Never along the carriageway if there are areas closed to traffic.", "Sin transitar por la calzada si hay zonas excluidas a la circulación.")
Q("tu4", "tunnel", "Stopped in a tunnel by traffic for more than 2 minutes, you…", "Detenido en un túnel por el tráfico más de 2 minutos, tú…",
  [("switch off the engine", "apagas el motor"), ("keep it running for the air conditioning", "lo mantienes encendido por el aire acondicionado"), ("switch off all lights", "apagas todas las luces")],
  "Keep position lights on and use hazard lights briefly.", "Mantén la luz de posición y conecta la de emergencia temporalmente.")
Q("tu5", "tunnel", "Stopped by traffic in a tunnel, you keep…", "Detenido por el tráfico en un túnel, te mantienes…",
  [("as far as possible from the vehicle ahead", "lo más lejos posible del vehículo de delante"), ("as close as possible to the vehicle ahead", "lo más cerca posible del de delante"), ("on the walkway", "en la acera de servicio")],
  "More room for manoeuvre and for emergency access.", "Más espacio para maniobrar y para los servicios de emergencia.")
Q("tu6", "tunnel", "Broken down and stopped in a tunnel, you ask for help…", "Averiado y detenido en un túnel, pides auxilio…",
  [("at the nearest SOS post, and follow its instructions", "en el poste S.O.S. más próximo y sigues sus instrucciones"), ("by sounding the horn", "tocando el claxon"), ("by walking out along the carriageway", "saliendo a pie por la calzada")],
  "Then everyone heads to the nearest refuge or exit.", "Después todos van al refugio o salida más próximos.")
Q("tu7", "tunnel", "Who may enter a tunnel when its entrance light forbids it?", "¿Quién puede entrar en un túnel cuando el semáforo de entrada no lo permite?",
  [("Emergency services, mechanical assistance and road maintenance crews", "Servicios de urgencia, asistencia mecánica y conservación de carreteras"), ("Buses", "Los autobuses"), ("Nobody, ever", "Nadie, nunca")],
  "Everyone else waits.", "Los demás esperan.")

# ---------------------------------------------------------------- 9.2 parking
Q("pk1", "parking", "As a general rule, vehicles park…", "Como norma general, los vehículos se estacionan…",
  [("parallel to the edge, one behind another", "en paralelo al borde, uno detrás de otro"), ("side by side (en batería)", "en batería"), ("at an angle", "en oblicuo")],
  "Other ways only when the road or circumstances advise it.", "Otras formas solo si la vía o las circunstancias lo aconsejan.")
Q("pk2", "parking", "In town, on a two-way street, you may park…", "En poblado, en una calle de doble sentido, puedes estacionar…",
  [("only on the right-hand side", "solo en el lado derecho"), ("on both sides", "en ambos lados"), ("on the left only", "solo en el izquierdo")],
  "On one-way streets, both sides.", "En sentido único, en ambos lados.")
Q("pk3", "parking", "On an interurban road you stop…", "En una vía interurbana te detienes…",
  [("off the carriageway and off the usable shoulder, on the right", "fuera de la calzada y de la parte transitable del arcén, a la derecha"), ("on the shoulder", "en el arcén"),
   ("on the carriageway with hazard lights", "en la calzada con la luz de emergencia")],
  "Always outside the carriageway.", "Siempre fuera de la calzada.")
Q("pk4", "parking", "In town, may you park on a usable shoulder?", "En poblado, ¿puedes estacionar en un arcén transitable?",
  [("Yes, on the carriageway or shoulder, close to the right edge", "Sí, en la calzada o el arcén, cerca del borde derecho"), ("No, never on the shoulder", "No, nunca en el arcén"), ("Only motorcycles", "Solo motocicletas")],
  "Out of town it is the opposite: never on the usable shoulder.", "Fuera de poblado es al revés: nunca en el arcén transitable.")
Q("pk5", "parking", "In a time-limited zone, the council may have your car removed when it stays more than…", "En una zona de estacionamiento limitado, el ayuntamiento puede retirar el vehículo cuando rebase…",
  [("three times the time paid", "el triple del tiempo abonado"), ("twice the time paid", "el doble del tiempo abonado"), ("10 minutes over the time paid", "10 minutos del tiempo abonado")],
  "Or if it has no ticket at all, until the driver is identified.", "O si no tiene título, hasta identificar al conductor.")
Q("pk6", "parking", "When parking, you should…", "Al estacionar, debes…",
  [("leave the best possible use of the remaining space", "permitir la mejor utilización del resto del espacio"), ("leave a full space in front", "dejar una plaza libre delante"), ("park in the middle of two spaces", "ocupar dos plazas")],
  "Never take up two spaces.", "No se deben ocupar dos plazas.")
Q("pk7", "parking", "Councils may charge parking according to…", "Los ayuntamientos pueden fijar tarifas de estacionamiento según…",
  [("the vehicle’s size and environmental label", "las dimensiones del vehículo y su clasificación ambiental"), ("the driver’s age", "la edad del conductor"), ("the car’s colour", "el color del vehículo")],
  "They may also regulate two-wheelers on pavements.", "También pueden regular las motos en aceras.")

# ---------------------------------------------------------------- 9.3 prohibitions
Q("np1", "noparking", "A broken yellow line along the kerb means…", "Una línea amarilla discontinua junto al bordillo indica…",
  [("no parking", "prohibido estacionar"), ("no stopping and no parking", "prohibido parar y estacionar"), ("loading only", "solo carga y descarga")],
  "A continuous yellow line forbids stopping too.", "La continua prohíbe también parar.")
Q("np2", "noparking", "A continuous yellow line along the kerb means…", "Una línea amarilla continua junto al bordillo indica…",
  [("no stopping and no parking", "prohibido parar y estacionar"), ("no parking only", "solo prohibido estacionar"), ("taxi rank", "parada de taxis")],
  "The broken one forbids parking only.", "La discontinua solo prohíbe estacionar.")
Q("np3", "noparking", "Double parking is…", "En doble fila…",
  [("a place where stopping is allowed but parking is not", "se permite parar pero no estacionar"), ("allowed for 5 minutes", "se permite estacionar 5 minutos"), ("always forbidden, even stopping", "está prohibido incluso parar")],
  "Double parking without the driver is a serious offence.", "Estacionar en doble fila sin conductor es infracción grave.")
Q("np4", "noparking", "Stopping on a pedestrian crossing is…", "Parar en un paso para peatones está…",
  [("forbidden", "prohibido"), ("allowed for under 2 minutes", "permitido menos de 2 minutos"), ("allowed at night", "permitido de noche")],
  "Stopping and parking are both forbidden there.", "Allí están prohibidas la parada y el estacionamiento.")
Q("np5", "noparking", "Parking that leaves less than how much space to the opposite edge or a continuous line is a serious offence?", "¿Estacionar dejando menos de cuánta distancia al borde opuesto o a una línea continua es infracción grave?",
  S("3 m", "2 m", "5 m"), "Or when other vehicles cannot pass.", "O cuando no permita el paso de otros vehículos.")
Q("np6", "noparking", "Parking in a loading zone is a serious offence when…", "Estacionar en una zona de carga y descarga es infracción grave cuando…",
  [("it is during its hours of use", "es durante las horas de utilización"), ("it is at night", "es de noche"), ("it is for more than 2 hours", "es durante más de 2 horas")],
  "Outside those hours, the general rules apply.", "Fuera de ese horario rigen las normas generales.")
Q("np7", "noparking", "Stopping at a junction in town is forbidden…", "Parar en una intersección en poblado está prohibido…",
  [("if it hinders turning", "si dificulta el giro"), ("never", "nunca"), ("only at night", "solo de noche")],
  "Out of town, also if it creates danger through lack of visibility.", "En interurbanas, también si genera peligro por falta de visibilidad.")
Q("np8", "noparking", "May you stop on an autopista?", "¿Puedes parar en una autopista?",
  [("Only in areas provided for it", "Solo en las zonas habilitadas"), ("Yes, on the shoulder for a short time", "Sí, en el arcén un momento"), ("Yes, in the right lane with hazard lights", "Sí, en el carril derecho con la luz de emergencia")],
  "Emergencies are detentions, not stops.", "Las emergencias son detenciones, no paradas.")
Q("np9", "noparking", "Which of these is a serious offence when stopping or parking?", "¿Cuál de estas es infracción grave al parar o estacionar?",
  [("Blocking a dropped kerb for disabled people", "Obstaculizar un paso rebajado para disminuidos físicos"), ("Parking parallel to the kerb", "Estacionar en paralelo al bordillo"),
   ("Stopping for 1 minute in a legal place", "Parar 1 minuto en un lugar permitido")],
  "Also medians, islands, blocking a vado or a turn.", "También medianas, isletas, vados o impedir un giro.")
Q("np10", "noparking", "Parking in front of a signed vado (driveway) is…", "Estacionar delante de un vado señalizado está…",
  [("forbidden", "prohibido"), ("allowed at night", "permitido de noche"), ("allowed for residents", "permitido a residentes")],
  "Blocking its use is a serious offence.", "Obstaculizar su uso es infracción grave.")
Q("np11", "noparking", "A yellow zig-zag marking at the kerb means…", "Una marca amarilla en zig-zag junto al bordillo indica…",
  [("no parking", "prohibido estacionar"), ("parking for motorcycles", "estacionamiento de motos"), ("a pedestrian crossing ahead", "un paso de peatones próximo")],
  "It usually marks a bus stop or a reserved space.", "Suele marcar una parada de bus u otro espacio reservado.")

# ---------------------------------------------------------------- 9.4 securing
Q("sc1", "secure", "Parking facing uphill with a manual gearbox, you leave…", "Estacionando cuesta arriba con cambio manual, dejas…",
  [("first gear engaged", "la primera velocidad engranada"), ("reverse engaged", "la marcha atrás engranada"), ("neutral", "punto muerto")],
  "Downhill: reverse. Automatic: P.", "Cuesta abajo: marcha atrás. Automático: P.")
Q("sc2", "secure", "Parking facing downhill with a manual gearbox, you leave…", "Estacionando cuesta abajo con cambio manual, dejas…",
  [("reverse engaged", "la marcha atrás engranada"), ("first gear engaged", "la primera engranada"), ("neutral", "punto muerto")],
  "The gear works against the slope.", "La marcha engranada se opone a la pendiente.")
Q("sc3", "secure", "A lorry over 3,500 kg parks on a slope. It must also…", "Un camión de más de 3.500 kg estaciona en pendiente. Además debe…",
  [("use proper chocks or rest a front wheel against the kerb", "usar calzos adecuados o apoyar una rueda directriz en el bordillo"), ("put stones under the wheels", "poner piedras bajo las ruedas"),
   ("leave the engine running", "dejar el motor en marcha")],
  "Never stones or other improvised objects.", "Nunca piedras u otros elementos no destinados a ello.")
Q("sc4", "secure", "With an automatic gearbox, the parked vehicle is left in…", "Con cambio automático, el vehículo estacionado se deja en…",
  [("P", "P"), ("N", "N"), ("D", "D")],
  "Plus the parking brake.", "Además del freno de estacionamiento.")
Q("sc5", "secure", "May a parked motorhome put out its awning and stabilisers?", "¿Puede una autocaravana estacionada desplegar el toldo y los estabilizadores?",
  [("No: nothing may stick out of its outline, and it rests only on its tyres", "No: nada puede desbordar su perímetro y se apoya solo sobre los neumáticos"),
   ("Yes, always", "Sí, siempre"), ("Yes, at night", "Sí, de noche")],
  "Chocks or wedges are allowed; spilling fluids is not.", "Se permiten calzos o cuñas; verter fluidos, no.")
Q("sc6", "secure", "Before leaving the driver’s seat you must…", "Antes de abandonar el puesto de conducción debes…",
  [("switch off the engine and apply the parking brake", "apagar el motor y accionar el freno de estacionamiento"), ("leave the engine running if it is short", "dejar el motor en marcha si es poco tiempo"),
   ("leave it in neutral", "dejarlo en punto muerto")],
  "And prevent unauthorised use if you walk away.", "Y evitar su uso sin autorización si te alejas.")
Q("sc7", "secure", "Heavy vehicle on a downhill slope, using the kerb: the front wheels point…", "Vehículo pesado en pendiente descendente usando el bordillo: las ruedas delanteras se orientan…",
  [("towards the kerb", "hacia fuera (hacia el bordillo)"), ("towards the centre of the road", "hacia el centro de la calzada"), ("straight ahead", "rectas")],
  "Uphill: towards the centre of the road.", "En subida: hacia el centro de la calzada.")
