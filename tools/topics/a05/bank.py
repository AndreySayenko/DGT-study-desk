# -*- coding: utf-8 -*-
"""Question bank for the interactive Category A1/A2, Topic 5 page (manoeuvres). In every question the FIRST option is
the correct one (the page shuffles options when it shows them). Ids must be unique and must not start with "ai"."""

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
    "basics": dict(sec=1, en="What a manoeuvre is", es="Qué es una maniobra",
        recap=[("A noticeable change in the vehicle’s position on the carriageway.", "Variación sensible de la posición del vehículo en la calzada."),
               ("Signal it in good time; make it only if there is no danger.", "Señalizarla con antelación; hacerla solo si no hay peligro."),
               ("Observe, signal, carry out.", "Observar, señalizar y realizar."),
               ("Joining, lateral move, overtaking, turning, turning round, stopping or parking.", "Incorporación, desplazamiento lateral, adelantamiento, cambio de dirección, cambio de sentido, parada o estacionamiento.")],
        trap=("Signalling first and looking afterwards.", "Señalizar primero y mirar después.")),
    "warnings": dict(sec=2, en="Light and arm signals", es="Advertencias ópticas",
        recap=[("Lights kept on for the whole manoeuvre; failing that, the arm (usually the left).", "Luces durante toda la maniobra; en su defecto, el brazo (normalmente el izquierdo)."),
               ("Left: arm horizontal. Right: arm bent upwards. Slowing: arm up and down.", "Izquierda: brazo horizontal. Derecha: brazo doblado hacia arriba. Frenar: brazo de arriba abajo."),
               ("Reversing: arm horizontal, palm backwards.", "Marcha atrás: brazo horizontal, palma hacia atrás."),
               ("Contradiction: the arm prevails (your course).", "Contradicción: prevalece el brazo (tu curso).")],
        trap=("Signalling a right turn with the left arm horizontal.", "Señalizar un giro a la derecha con el brazo izquierdo horizontal.")),
    "horn": dict(sec=2, en="Horn and flashes", es="Claxon y ráfagas",
        recap=[("Horn exceptional: avoid an accident or running someone over; emergency trip.", "Claxon excepcional: evitar un accidente o atropello; servicio de urgencia."),
               ("To announce overtaking: horn only out of town; flashes in and out of town.", "Para avisar del adelantamiento: claxon solo fuera de poblado; ráfagas dentro y fuera."),
               ("Continuous, steady, not shrill; no musical notes.", "Continuo, uniforme, no estridente; sin notas musicales."),
               ("Never to greet, protest or warn of police.", "Nunca para saludar, recriminar o avisar de los agentes.")],
        trap=("Using the horn in town to announce an overtaking.", "Usar el claxon en poblado para avisar de un adelantamiento.")),
    "joining": dict(sec=3, en="Joining traffic", es="Incorporación",
        recap=[("Start riding or enter another road; not after a detention.", "Comenzar a circular o entrar en otra vía; no tras una detención."),
               ("Observe, signal, join giving way to those already on the road.", "Observar, señalizar e incorporarse cediendo el paso a los que circulan."),
               ("From a building or private road: speed to stop at once; give way both sides.", "Desde inmueble o camino privado: velocidad para detenerse en el acto; ceder a ambos lados."),
               ("Help others join, above all buses leaving a signed stop.", "Facilitar la incorporación, sobre todo a autobuses desde una parada señalizada.")],
        trap=("Thinking moving off at a green light is joining traffic.", "Pensar que arrancar con el verde es una incorporación.")),
    "lateral": dict(sec=4, en="Moving sideways", es="Desplazamiento lateral",
        recap=[("Moving partly or fully into another lane.", "Invadir parcial o totalmente otro carril."),
               ("A correction within your lane is not a lateral move.", "Una corrección dentro del carril no lo es."),
               ("Observe, signal until it ends, move early and gradually.", "Observar, señalizar hasta el final y hacerlo con antelación y progresivamente."),
               ("Respect the priority of whoever is in the lane you want.", "Respetar la prioridad de quien circula por el carril que quieres ocupar.")],
        trap=("Thinking you have priority because you signalled.", "Pensar que tienes prioridad porque señalizaste.")),
    "overtake": dict(sec=5, en="How to overtake", es="Cómo adelantar",
        recap=[("Only with 100 % safety; room to overtake and to return.", "Solo con seguridad total; espacio para adelantar y para volver."),
               ("If the one ahead signals the same side, it goes first.", "Si el de delante señaliza al mismo lado, tiene preferencia."),
               ("Overtake on the left; on the right only in the listed cases.", "Por la izquierda; por la derecha solo en los casos previstos."),
               ("Can’t finish safely: slow down quickly and return.", "Si no puedes terminar con seguridad: reduce rápido y vuelve.")],
        trap=("Overtaking on the right a vehicle that is simply slow.", "Adelantar por la derecha a un vehículo que solo va despacio.")),
    "gap": dict(sec=5, en="Side gap and −20 km/h", es="Separación lateral y −20 km/h",
        recap=[("Vulnerable users, immobilised and assistance vehicles: ≥ 1.5 m, using the next lane.", "Vulnerables, inmovilizados y de auxilio: ≥ 1,5 m ocupando el carril contiguo."),
               ("More than one lane your way: full lane change.", "Más de un carril por sentido: cambio completo de carril."),
               ("A two-wheeler overtaking anything out of town: ≥ 1.5 m.", "Vehículo de dos ruedas que adelanta fuera de poblado: ≥ 1,5 m."),
               ("−20 km/h: vulnerable users out of town; immobilised and assistance vehicles everywhere.", "−20 km/h: vulnerables fuera de poblado; inmovilizados y auxilio siempre.")],
        trap=("Applying the −20 km/h to cyclists in town.", "Aplicar los −20 km/h a ciclistas en poblado.")),
    "overtaken": dict(sec=5, en="The vehicle being overtaken", es="El vehículo adelantado",
        recap=[("Keep to the right edge, without using the shoulder.", "Ceñirse al borde derecho, sin pisar el arcén."),
               ("Turning or stopping on the left: keep left.", "Si va a girar o parar a la izquierda: ceñirse a la izquierda."),
               ("Never speed up or make it harder.", "Nunca aumentar la velocidad ni dificultarlo."),
               ("Slow down if danger arises; let a giving-up overtaker back in.", "Reducir si surge peligro; facilitar la vuelta al que desiste.")],
        trap=("Speeding up so the overtaker finishes sooner.", "Acelerar para que el que adelanta termine antes.")),
    "noover": dict(sec=5, en="Where overtaking is forbidden", es="Dónde está prohibido adelantar",
        recap=[("Signs and markings; bends and brows; poor visibility; behind an overtaking vehicle that hides the road.", "Señales y marcas; curvas y rasantes; poca visibilidad; detrás de otro que adelanta y tapa."),
               ("Junctions, except roundabouts, on the right, signed priority and two-wheelers.", "Intersecciones, salvo glorietas, por la derecha, prioridad señalizada y vehículos de dos ruedas."),
               ("Level crossings, pedestrian crossings, cycle junctions and near them — no exceptions since 2026.", "Pasos a nivel, pasos de peatones, cruces con vías ciclistas y proximidades: sin excepciones desde 2026."),
               ("Tunnels with one lane your way; a vehicle already overtaking if you must invade.", "Túneles con un carril por sentido; al que ya adelanta si hay que invadir.")],
        trap=("Thinking two-wheelers may still be overtaken at a level crossing.", "Pensar que aún se puede adelantar a los de dos ruedas en un paso a nivel.")),
    "turning": dict(sec=6, en="Turning", es="Cambio de dirección",
        recap=[("Following a bend is not a turn.", "Seguir una curva no es cambio de dirección."),
               ("Right: keep to the right edge.", "Derecha: ceñirse al borde derecho."),
               ("Left: one-way, left edge; two-way, next to the centre line without crossing; three lanes, centre lane.", "Izquierda: sentido único, borde izquierdo; doble sentido, junto a la marca sin rebasarla; tres carriles, el central."),
               ("Roundabouts: centre on the left. Deceleration lane: enter early, slow down inside.", "Glorietas: centro a la izquierda. Deceleración: entrar pronto y frenar dentro.")],
        trap=("Turning left on a two-way road from the right-hand edge.", "Girar a la izquierda en doble sentido desde el borde derecho.")),
    "uturn": dict(sec=7, en="Turning round", es="Cambio de sentido",
        recap=[("180° to continue the other way on the same road.", "180° para seguir por la misma vía en sentido contrario."),
               ("Signal braking and the lateral move; one go, no reversing.", "Señalizar el frenado y el desplazamiento; un solo giro, sin marcha atrás."),
               ("If you hold up others while waiting, pull off to the right.", "Si al esperar entorpeces, sal por la derecha."),
               ("Forbidden where overtaking is; on motorways only at grade-separated points; never via the median.", "Prohibido donde se prohíbe adelantar; en autopistas solo a distinto nivel; nunca por la mediana.")],
        trap=("Turning round through a gap in the median of an autovía.", "Cambiar de sentido por un paso de la mediana de la autovía.")),
    "immob": dict(sec=8, en="Detention, stop and parking", es="Detención, parada y estacionamiento",
        recap=[("Detention: imposed, not a manoeuvre. Stop: < 2 min, not abandoning. Parking: the rest.", "Detención: impuesta, no es maniobra. Parada: < 2 min sin abandonar. Estacionamiento: el resto."),
               ("Tunnel detention over 2 min: engine off, position lights on.", "Detención en túnel de más de 2 min: motor apagado, luces de posición."),
               ("Urban: right edge; both sides only on one-way streets. Interurban: off the carriageway.", "Urbana: borde derecho; ambos lados solo en sentido único. Interurbana: fuera de la calzada."),
               ("Two-wheelers on pavements only if a bylaw allows it.", "Motos en aceras solo si una ordenanza lo permite.")],
        trap=("Calling a stop at a red light a ‘parada’.", "Llamar «parada» a detenerse en un semáforo.")),
    "noparking": dict(sec=8, en="Where you may not stop or park", es="Prohibiciones de parada y estacionamiento",
        recap=[("No parking: time zones without ticket, loading zones, disabled spaces, pavements, vados, double parking.", "No estacionar: zona horaria sin título, carga y descarga, minusválidos, aceras, vados, doble fila."),
               ("No stopping or parking: bends, brows, tunnels, level and pedestrian crossings, cycle lanes, junctions, bus lanes, motorways.", "Ni parar ni estacionar: curvas, rasantes, túneles, pasos a nivel y de peatones, carril bici, intersecciones, carril bus, autopistas."),
               ("Broken yellow line: no parking; continuous: no stopping either.", "Línea amarilla discontinua: no estacionar; continua: tampoco parar."),
               ("Serious: < 3 m to the opposite edge, double parking without driver, bus stop, middle of the road…", "Grave: < 3 m al borde opuesto, doble fila sin conductor, parada de bus, medio de la calzada…")],
        trap=("Thinking you may stop on a pedestrian crossing for a moment.", "Pensar que se puede parar un momento en un paso de peatones.")),
}

# ---------------------------------------------------------------- basics
Q("bs1", "basics", "In short, every manoeuvre consists of…", "En resumen, toda maniobra consiste en…",
  [("observing, signalling and carrying it out", "observar, señalizar y realizar"), ("signalling, accelerating and turning", "señalizar, acelerar y girar"), ("braking, signalling and observing", "frenar, señalizar y observar")],
  "In that order.", "En ese orden.")
Q("bs2", "basics", "A manoeuvre is…", "Una maniobra es…",
  [("a noticeable change in the vehicle’s position on the carriageway", "una variación sensible de la posición del vehículo en la calzada"), ("any movement of the vehicle", "cualquier movimiento del vehículo"), ("only overtaking", "solo el adelantamiento")],
  "To be signalled in good time.", "Que debe señalizarse con antelación.")
Q("bs3", "basics", "Which of these is a basic traffic manoeuvre?", "¿Cuál de estas es una maniobra básica de la circulación?",
  [("Turning round (cambio de sentido)", "El cambio de sentido"), ("Stopping at a red light", "Detenerse en un semáforo en rojo"), ("Following a bend", "Seguir una curva")],
  "A red light imposes a detention, not a manoeuvre.", "El semáforo impone una detención, no una maniobra.")
Q("bs4", "basics", "A manoeuvre may only be made when…", "Una maniobra solo puede realizarse cuando…",
  [("it causes no danger and the rules are followed", "no represente ningún peligro y se respeten las normas"), ("you have signalled it", "la hayas señalizado"), ("nobody is behind you", "no venga nadie detrás")],
  "Signalling alone gives no right to make it.", "Señalizar no da por sí solo derecho a realizarla.")

# ---------------------------------------------------------------- warnings
Q("wn1", "warnings", "How long must the indicator stay on?", "¿Cuánto tiempo debe estar encendido el intermitente?",
  [("For the whole manoeuvre, switched off when it ends", "Todo el tiempo que dure la maniobra, apagándolo al terminar"), ("Three flashes", "Tres destellos"), ("Only before starting", "Solo antes de empezar")],
  "Then switch it off.", "Después se quita.")
Q("wn2", "warnings", "On your motorcycle, how do you signal with your arm that you will move to the right?", "En moto, ¿cómo indicas con el brazo que vas a desplazarte a la derecha?",
  [("Left arm bent upwards, palm extended", "Brazo izquierdo doblado hacia arriba, palma extendida"), ("Left arm horizontal", "Brazo izquierdo horizontal"), ("Left arm moved up and down", "Brazo izquierdo de arriba abajo")],
  "Horizontal is for the left.", "Horizontal es para la izquierda.")
Q("wn3", "warnings", "Left arm extended horizontally, palm down, means…", "El brazo izquierdo extendido horizontalmente, con la palma hacia abajo, indica…",
  [("a move or turn to the left", "desplazamiento o giro a la izquierda"), ("a move to the right", "desplazamiento a la derecha"), ("that you will stop", "que vas a detenerte")],
  "The side the hand points to.", "Hacia el lado que indica la mano.")
Q("wn4", "warnings", "Moving the arm up and down with short, quick movements means…", "Mover el brazo de arriba abajo con movimientos cortos y rápidos indica…",
  [("you are going to slow down a lot or stop", "que vas a frenar considerablemente o detenerte"), ("you are going to overtake", "que vas a adelantar"), ("let me pass", "que te dejen pasar")],
  "Equivalent to repeated use of the brake light.", "Equivale al uso reiterado de la luz de freno.")
Q("wn5", "warnings", "According to your course, if the indicator and the arm signal contradict each other…", "Según tu curso, si el intermitente y el brazo se contradicen…",
  [("the arm signal prevails", "prevalece el brazo"), ("the indicator prevails", "prevalece el intermitente"), ("both are ignored", "se ignoran ambos")],
  "Arm signals prevail over light ones.", "Las del brazo prevalecen sobre las luminosas.")
Q("wn6", "warnings", "The arm signal for reversing is…", "La señal con el brazo para la marcha atrás es…",
  [("arm horizontal with the palm facing backwards", "brazo horizontal con la palma hacia atrás"), ("arm bent upwards", "brazo doblado hacia arriba"), ("arm moved up and down", "brazo de arriba abajo")],
  "Used when there is no reversing light.", "Se usa si no hay luz de marcha atrás.")
Q("wn7", "warnings", "Which arm is normally used for arm signals?", "¿Qué brazo se usa normalmente para las señales?",
  [("The left", "El izquierdo"), ("The right", "El derecho"), ("Either", "Cualquiera")],
  "On a motorcycle the right hand stays on the throttle.", "En moto la mano derecha va en el acelerador.")
Q("wn8", "warnings", "For arm signals to be valid they must be…", "Para que las señales con el brazo sean válidas deben…",
  [("made correctly and visible to everyone", "hacerse correctamente y ser visibles para todos"), ("held for 5 seconds", "mantenerse 5 segundos"), ("made with both arms", "hacerse con ambos brazos")],
  "Otherwise they don’t count.", "Si no, no sirven.")

# ---------------------------------------------------------------- horn
Q("hn1", "horn", "As a rule, the horn may be used…", "Como norma, el claxon puede usarse…",
  [("exceptionally, to warn others of your presence", "excepcionalmente, para advertir de la presencia del vehículo"), ("whenever you like", "siempre que se quiera"), ("only at night", "solo de noche")],
  "Never for no reason.", "Nunca de forma inmotivada.")
Q("hn2", "horn", "In town, may you use the horn to avoid running someone over?", "En poblado, ¿puedes usar el claxon para evitar un atropello?",
  [("Yes", "Sí"), ("No, only flashes", "No, solo ráfagas"), ("No, never in town", "No, nunca en poblado")],
  "In and out of town.", "Dentro y fuera de poblado.")
Q("hn3", "horn", "In town, how do you tell the vehicle ahead that you want to overtake?", "En poblado, ¿cómo avisas al de delante de que quieres adelantarle?",
  [("With headlight flashes", "Con ráfagas de luz"), ("With the horn", "Con el claxon"), ("With the hazard lights", "Con la luz de emergencia")],
  "The horn for overtaking only out of town.", "El claxon para adelantar, solo fuera de poblado.")
Q("hn4", "horn", "Using the horn to greet a friend is…", "Usar el claxon para saludar a un amigo está…",
  [("forbidden", "prohibido"), ("allowed in town", "permitido en poblado"), ("allowed if short", "permitido si es breve")],
  "It causes noise pollution.", "Produce contaminación acústica.")
Q("hn5", "horn", "The horn of your motorcycle must produce a sound that is…", "El claxon de tu moto debe producir un sonido…",
  [("continuous, steady and not shrill", "continuo, uniforme y no estridente"), ("musical, to be friendly", "musical, para ser amable"), ("as loud as possible", "lo más fuerte posible")],
  "No varied notes.", "Sin notas variadas.")
Q("hn6", "horn", "Headlight flashes must be given…", "Las ráfagas deben hacerse…",
  [("at very short intervals, avoiding dazzle", "a intervalos muy cortos, evitando deslumbrar"), ("for 10 seconds", "durante 10 segundos"), ("only with main beam", "solo con luz de carretera")],
  "Dipped, main or both alternately.", "Cruce, carretera o ambas alternativamente.")
Q("hn7", "horn", "Flashing your lights to warn others of a police check is…", "Hacer ráfagas para avisar de un control policial está…",
  [("forbidden", "prohibido"), ("allowed", "permitido"), ("recommended", "recomendado")],
  "Also forbidden to greet or protest.", "También para saludar o recriminar.")
Q("hn8", "horn", "On a narrow road with many bends, out of town, the horn may be used…", "En una vía estrecha con muchas curvas, fuera de poblado, el claxon puede usarse…",
  [("to avoid a possible accident", "para evitar un posible accidente"), ("never", "nunca"), ("only at night", "solo de noche")],
  "That is the typical case.", "Es el caso típico.")

# ---------------------------------------------------------------- joining
Q("jn1", "joining", "Which of these is NOT joining traffic?", "¿Cuál de estas NO es una incorporación a la circulación?",
  [("Moving off when the light turns green", "Reanudar la marcha cuando el semáforo se pone en verde"), ("Leaving a parking space", "Salir de un estacionamiento"), ("Leaving a garage", "Salir de un garaje")],
  "Resuming after a detention.", "Es reanudar la marcha tras una detención.")
Q("jn2", "joining", "Coming out of a private road onto a public one, you must ride at a speed that lets you…", "Al salir de un camino privado a una vía pública, debes circular a una velocidad que te permita…",
  [("stop at once to give way to vehicles and pedestrians from both sides", "detenerte en el acto para ceder el paso a vehículos y peatones de ambos lados"), ("join quickly", "incorporarte rápido"), ("give way only to the right", "ceder solo a la derecha")],
  "From the right and from the left.", "Tanto por la derecha como por la izquierda.")
Q("jn3", "joining", "On an acceleration lane, where must you make sure you can join safely?", "En un carril de aceleración, ¿dónde debes asegurarte de que puedes incorporarte con seguridad?",
  [("At the start of the lane, stopping there if necessary", "Al principio del carril, deteniéndote allí si es necesario"), ("At the end of the lane", "Al final del carril"), ("Already on the main road", "Ya en la vía principal")],
  "Then speed up to the right speed by the end.", "Después acelera hasta la velocidad adecuada al final.")
Q("jn4", "joining", "When joining traffic, who has priority?", "Al incorporarte a la circulación, ¿quién tiene prioridad?",
  [("Those already on the road", "Los que ya circulan"), ("You, if you signal", "Tú, si señalizas"), ("Whoever is bigger", "El más grande")],
  "Give way to them.", "Hay que cederles el paso.")
Q("jn5", "joining", "In town, a bus signals that it is leaving a signed stop. You must…", "En poblado, un autobús señaliza que sale de una parada señalizada. Debes…",
  [("move aside or slow down, stopping if necessary, to let it out", "desplazarte o reducir la velocidad, deteniéndote si es preciso, para facilitarle la salida"), ("speed up to pass it first", "acelerar para pasar antes"), ("sound the horn", "tocar el claxon")],
  "The bus driver must still take precautions.", "El conductor del autobús debe igualmente adoptar precauciones.")
Q("jn6", "joining", "To join traffic, which indicator do you use?", "Para incorporarte, ¿qué intermitente usas?",
  [("The one for the side you move to", "El del lado hacia el que te desplazas"), ("The hazard lights", "La luz de emergencia"), ("None if nobody is coming", "Ninguno si no viene nadie")],
  "Or the arm.", "O, en su defecto, el brazo.")

# ---------------------------------------------------------------- lateral
Q("lt1", "lateral", "Is a small correction of your path within your own lane a lateral move?", "¿Es desplazamiento lateral una pequeña corrección de trayectoria dentro de tu carril?",
  [("No", "No"), ("Yes", "Sí"), ("Only out of town", "Solo fuera de poblado")],
  "It must move you into another lane.", "Debe implicar la invasión de otro carril.")
Q("lt2", "lateral", "When you move sideways into another lane, who has priority?", "Al desplazarte lateralmente a otro carril, ¿quién tiene prioridad?",
  [("Whoever is already in that lane", "Quien ya circula por ese carril"), ("You, after signalling", "Tú, tras señalizar"), ("The faster one", "El más rápido")],
  "Respect their priority.", "Hay que respetar su prioridad.")
Q("lt3", "lateral", "How must a lateral move be made?", "¿Cómo debe hacerse un desplazamiento lateral?",
  [("Early, gradually and smoothly", "Con antelación, de forma gradual y progresiva"), ("Quickly, to spend less time", "Rápido, para estar menos tiempo"), ("Sharply, so everyone notices", "Bruscamente, para que todos lo vean")],
  "No sudden swerves.", "Sin brusquedades.")
Q("lt4", "lateral", "Until when must you signal a lateral move?", "¿Hasta cuándo debes señalizar un desplazamiento lateral?",
  [("Until the move is finished", "Hasta la finalización del desplazamiento"), ("Only before starting", "Solo antes de empezar"), ("Until the next junction", "Hasta la siguiente intersección")],
  "Then switch the indicator off.", "Después se quita el intermitente.")
Q("lt5", "lateral", "Which of these is a reason for a lateral move?", "¿Cuál de estas es un motivo de desplazamiento lateral?",
  [("Passing a broken-down vehicle", "Rebasar un vehículo averiado"), ("Following a bend", "Seguir una curva"), ("Braking", "Frenar")],
  "Also turning, overtaking, stopping, joining…", "También cambiar de dirección, adelantar, parar, incorporarse…")

# ---------------------------------------------------------------- overtaking
Q("ov1", "overtake", "As a general rule you overtake…", "Como norma general se adelanta…",
  [("on the left", "por la izquierda"), ("on the right", "por la derecha"), ("on whichever side is free", "por el lado que esté libre")],
  "On the right only in some cases.", "Por la derecha solo en algunos casos.")
Q("ov2", "overtake", "The vehicle ahead signals that it will move to the left, the side you wanted to overtake on. You…", "El de delante señaliza que se desplaza a la izquierda, el lado por el que querías adelantar. Tú…",
  [("let it go first", "le dejas preferencia"), ("overtake quickly before it moves", "adelantas rápido antes de que se mueva"), ("overtake on the right", "adelantas por la derecha")],
  "If after a reasonable time it doesn’t move, you may overtake after warning it.", "Si tras un tiempo prudencial no lo hace, puedes adelantar avisando.")
Q("ov3", "overtake", "In town, on a carriageway with two marked lanes in your direction, may you overtake on the right?", "En poblado, en una calzada con dos carriles delimitados en tu sentido, ¿puedes adelantar por la derecha?",
  [("Yes", "Sí"), ("No, never", "No, nunca"), ("Only buses", "Solo a autobuses")],
  "One of the exceptions.", "Es una de las excepciones.")
Q("ov4", "overtake", "Once you have started overtaking, you realise you can’t finish safely. You…", "Una vez iniciado el adelantamiento, ves que no puedes terminarlo con seguridad. Tú…",
  [("slow down quickly and return to the right lane, signalling it", "reduces rápidamente la velocidad y vuelves al carril derecho, señalizándolo"), ("accelerate hard to finish", "aceleras al máximo para terminar"), ("stay alongside", "te quedas en paralelo")],
  "Giving up is the safe choice.", "Desistir es lo seguro.")
Q("ov5", "overtake", "May you overtake on the right a vehicle clearly signalling a left turn?", "¿Puedes adelantar por la derecha a un vehículo que indica claramente que va a girar a la izquierda?",
  [("Yes, with room and maximum care", "Sí, con espacio y máxima precaución"), ("No, never", "No, nunca"), ("Only in town", "Solo en poblado")],
  "Also when it is going to stop on the left.", "También si va a inmovilizarse a la izquierda.")
Q("ov6", "overtake", "When should you return to the right lane after overtaking?", "¿Cuándo debes volver al carril derecho tras adelantar?",
  [("As soon as possible, gradually, when you see the overtaken vehicle in your mirrors", "Cuanto antes, gradualmente, cuando veas al adelantado por los espejos"), ("Immediately in front of it", "Inmediatamente delante de él"), ("At the next junction", "En la siguiente intersección")],
  "Without forcing anyone to change path or speed.", "Sin obligar a nadie a cambiar de trayectoria o velocidad.")
Q("ov7", "overtake", "With two lanes in your direction, after overtaking you want to overtake again. You may…", "Con dos carriles en tu sentido, tras adelantar quieres volver a adelantar. Puedes…",
  [("stay in the left lane if you don’t bother faster vehicles behind", "permanecer en el carril izquierdo si no molestas a los que vienen más rápido"), ("never stay in the left lane", "nunca permanecer en el izquierdo"), ("stay in it as long as you like", "permanecer en él todo lo que quieras")],
  "Making sure you don’t bother anyone behind.", "Asegurándote de no molestar a los de detrás.")
Q("ov8", "overtake", "May you overtake a tram on the right on a two-way road?", "¿Puedes adelantar por la derecha a un tranvía en una vía de doble sentido?",
  [("Yes, if it runs in the central zone", "Sí, si marcha por la zona central"), ("No", "No"), ("Only at night", "Solo de noche")],
  "With room and maximum care.", "Con espacio y máxima precaución.")

# ---------------------------------------------------------------- gap
Q("gp1", "gap", "On your motorcycle, out of town, you overtake a car. Minimum side gap?", "En moto, fuera de poblado, adelantas a un turismo. ¿Separación lateral mínima?",
  [("1.5 m", "1,5 m"), ("1 m", "1 m"), ("0.5 m", "0,5 m")],
  "A two-wheeler overtaking any vehicle out of town.", "Vehículo de dos ruedas que adelanta a cualquiera fuera de poblado.")
Q("gp2", "gap", "Out of town you overtake a cyclist. Besides the 1.5 m, you must…", "Fuera de poblado adelantas a un ciclista. Además de los 1,5 m, debes…",
  [("ride at least 20 km/h below the road’s limit", "ir al menos 20 km/h por debajo del límite de la vía"), ("sound the horn", "tocar el claxon"), ("exceed the limit to finish sooner", "superar el límite para terminar antes")],
  "Since 1 October 2026.", "Desde el 1 de octubre de 2026.")
Q("gp3", "gap", "In town, overtaking a moped, the side gap must be…", "En poblado, al adelantar a un ciclomotor, la separación lateral debe ser…",
  [("at least 1.5 m", "al menos 1,5 m"), ("at least 1 m", "al menos 1 m"), ("whatever you judge", "la que consideres")],
  "In and out of town.", "Dentro y fuera de poblado.")
Q("gp4", "gap", "You overtake a cyclist on an autovía with two lanes in your direction. You must…", "Adelantas a un ciclista en una autovía con dos carriles en tu sentido. Debes…",
  [("change lanes completely", "cambiar completamente de carril"), ("keep 1.5 m without leaving your lane", "dejar 1,5 m sin salir de tu carril"), ("sound the horn first", "tocar antes el claxon")],
  "With more than one lane your way, a full lane change.", "Con más de un carril por sentido, cambio completo de carril.")
Q("gp5", "gap", "In town, you pass a car broken down in your lane. You must reduce your speed…", "En poblado, rebasas un turismo averiado en tu carril. Debes reducir la velocidad…",
  [("at least 20 km/h below the limit", "al menos 20 km/h por debajo del límite"), ("only out of town", "solo fuera de poblado"), ("no, the limit is enough", "no, basta el límite")],
  "Immobilised and assistance vehicles: in and out of town.", "Inmovilizados y vehículos de auxilio: dentro y fuera de poblado.")
Q("gp6", "gap", "Overtaking a group of cyclists out of town, they count as…", "Al adelantar a un grupo de ciclistas fuera de poblado, se consideran…",
  [("one single moving unit", "una única unidad móvil"), ("separate vehicles", "vehículos separados"), ("pedestrians", "peatones")],
  "Overtake the whole group at once.", "Se adelanta al grupo entero.")
Q("gp7", "gap", "May you overtake if a cyclist coming the other way on the shoulder would be put at risk?", "¿Puedes adelantar si pondrías en peligro a un ciclista que viene de frente por el arcén?",
  [("No, it is expressly forbidden", "No, está expresamente prohibido"), ("Yes, he is on the shoulder", "Sí, va por el arcén"), ("Yes, at reduced speed", "Sí, a velocidad reducida")],
  "Even if the cyclist rides on the shoulder.", "Incluso si circula por el arcén.")
Q("gp8", "gap", "Overtaking a lorry, what side gap do you leave?", "Al adelantar a un camión, ¿qué separación lateral dejas?",
  [("Out of town at least 1.5 m on a motorcycle; in general, proportional to speed and road", "Fuera de poblado, al menos 1,5 m en moto; en general, proporcional a la velocidad y la vía"), ("Always 0.5 m", "Siempre 0,5 m"), ("None is required", "No se exige ninguna")],
  "Two-wheelers out of town: 1.5 m from anything.", "Dos ruedas fuera de poblado: 1,5 m con cualquiera.")

# ---------------------------------------------------------------- overtaken
Q("od1", "overtaken", "A car is overtaking you. You must…", "Un turismo te está adelantando. Debes…",
  [("keep to the right edge and not speed up", "ceñirte al borde derecho y no aumentar la velocidad"), ("speed up to make it quicker", "acelerar para que sea más rápido"), ("move onto the shoulder", "circular por el arcén")],
  "Without using the shoulder.", "Sin pisar el arcén.")
Q("od2", "overtaken", "You are being overtaken and a danger appears. You must…", "Te están adelantando y surge un peligro. Debes…",
  [("slow down", "disminuir la velocidad"), ("speed up", "acelerar"), ("keep your speed", "mantener la velocidad")],
  "Once the overtaking has started.", "Una vez iniciado el adelantamiento.")
Q("od3", "overtaken", "The vehicle overtaking you gives up and slows down. You…", "El que te adelanta desiste y reduce la velocidad. Tú…",
  [("help it get back into the lane", "le facilitas la vuelta al carril"), ("speed up", "aceleras"), ("brake hard", "frenas bruscamente")],
  "Let it back in.", "Déjale volver.")
Q("od4", "overtaken", "You want to turn left and someone is about to overtake you. You position yourself…", "Quieres girar a la izquierda y alguien va a adelantarte. Te colocas…",
  [("as far left as possible, without hindering oncoming traffic", "lo más a la izquierda posible, sin interferir al sentido contrario"), ("on the right edge", "en el borde derecho"), ("in the centre of the lane", "en el centro del carril")],
  "So it can overtake you on the right.", "Para que pueda adelantarte por la derecha.")

# ---------------------------------------------------------------- forbidden
Q("no1", "noover", "Overtaking is forbidden…", "Está prohibido adelantar…",
  [("in bends and brows with reduced visibility", "en curvas y cambios de rasante de visibilidad reducida"), ("on straight roads", "en rectas"), ("on autovías", "en autovías")],
  "Unless the directions are clearly separated and you don’t invade.", "Salvo sentidos claramente delimitados y sin invadir.")
Q("no2", "noover", "May you overtake a moped near a junction?", "¿Puedes adelantar a un ciclomotor en las proximidades de una intersección?",
  [("Yes, two-wheelers are an exception", "Sí, los vehículos de dos ruedas son una excepción"), ("No", "No"), ("Only on the right", "Solo por la derecha")],
  "Also roundabouts, on the right, and signed priority.", "También glorietas, por la derecha y prioridad señalizada.")
Q("no3", "noover", "Since October 2026, may you overtake a motorcycle at a level crossing?", "Desde octubre de 2026, ¿puedes adelantar a una moto en un paso a nivel?",
  [("No, there are no exceptions", "No, no hay excepciones"), ("Yes, two-wheelers are an exception", "Sí, los de dos ruedas son una excepción"), ("Yes, after sounding the horn", "Sí, avisando con el claxon")],
  "The two-wheeler exception was deleted.", "Se suprimió la excepción de los vehículos de dos ruedas.")
Q("no4", "noover", "May you overtake at a pedestrian crossing if you go slowly enough to stop?", "¿Puedes adelantar en un paso de peatones si vas tan despacio que puedes detenerte?",
  [("No, it is forbidden without exceptions since October 2026", "No, está prohibido sin excepciones desde octubre de 2026"), ("Yes", "Sí"), ("Only in town", "Solo en poblado")],
  "Your course still shows the old exception.", "Tu curso aún muestra la excepción antigua.")
Q("no5", "noover", "In a tunnel with two lanes in your direction, may you overtake?", "En un túnel con dos carriles en tu sentido, ¿puedes adelantar?",
  [("Yes, if nothing else forbids it", "Sí, si nada más lo prohíbe"), ("No, never in tunnels", "No, nunca en túneles"), ("Only motorcycles", "Solo las motos")],
  "Forbidden only with one lane your way.", "Solo se prohíbe con un carril por sentido.")
Q("no6", "noover", "A lorry ahead is overtaking and hides the road. May you overtake behind it?", "Un camión de delante está adelantando y tapa la vía. ¿Puedes adelantar detrás de él?",
  [("No", "No"), ("Yes, following it closely", "Sí, siguiéndolo de cerca"), ("Yes, on a motorcycle", "Sí, en moto")],
  "Its size prevents you from seeing ahead.", "Sus dimensiones impiden ver.")
Q("no7", "noover", "May you overtake at a roundabout?", "¿Puedes adelantar en una glorieta?",
  [("Yes, roundabouts are an exception", "Sí, las glorietas son una excepción"), ("No", "No"), ("Only on the left", "Solo por la izquierda")],
  "One of the junction exceptions.", "Es una excepción de las intersecciones.")
Q("no8", "noover", "A car has stopped because of the traffic on a no-overtaking stretch. You…", "Un turismo se ha detenido por necesidades del tráfico en un tramo de adelantamiento prohibido. Tú…",
  [("stay behind it", "te quedas detrás"), ("pass it using the opposite lane", "lo rebasas por el carril contrario"), ("pass it on the shoulder", "lo rebasas por el arcén")],
  "Only an obstacle or a breakdown may be passed.", "Solo se rebasa un obstáculo o un inmovilizado por avería.")
Q("no9", "noover", "On a stretch with a continuous line, you come up behind a slow bicycle. You…", "En un tramo con línea continua alcanzas a una bicicleta lenta. Tú…",
  [("may overtake it if its speed allows it without risk", "puedes adelantarla si su velocidad permite hacerlo sin riesgo"), ("must stay behind", "debes quedarte detrás"), ("may overtake at any speed", "puedes adelantarla a cualquier velocidad")],
  "A special case, after checking there is no danger.", "Es un supuesto especial, tras cerciorarte de que no hay peligro.")

# ---------------------------------------------------------------- turning
Q("tr1", "turning", "Is leaning into a bend to follow the road a turn (cambio de dirección)?", "¿Es un cambio de dirección inclinarse en una curva para seguir la carretera?",
  [("No", "No"), ("Yes", "Sí"), ("Only if you signal", "Solo si señalizas")],
  "Following the road is not a manoeuvre.", "Seguir el trazado no es maniobra.")
Q("tr2", "turning", "To turn left on a two-way road without a centre line, you position yourself…", "Para girar a la izquierda en una vía de doble sentido sin marca central, te colocas…",
  [("next to the centre of the carriageway, without invading the opposite side", "junto al eje de la calzada, sin invadir el sentido contrario"), ("on the right edge", "en el borde derecho"), ("in the opposite lane", "en el carril contrario")],
  "With a centre line: next to it without crossing.", "Con marca: junto a ella sin rebasarla.")
Q("tr3", "turning", "To turn left on a one-way street you position yourself…", "Para girar a la izquierda en una calle de sentido único te colocas…",
  [("as close as possible to the left edge", "lo más cerca posible del borde izquierdo"), ("in the centre", "en el centro"), ("on the right edge", "en el borde derecho")],
  "As close as possible.", "Ceñirse todo lo posible.")
Q("tr4", "turning", "On a two-way road with three lanes separated by broken lines, to turn left you use…", "En una vía de doble sentido con tres carriles separados por discontinuas, para girar a la izquierda usas…",
  [("the centre lane", "el carril central"), ("the left lane", "el carril izquierdo"), ("the right lane", "el carril derecho")],
  "Never the left one.", "Nunca el izquierdo.")
Q("tr5", "turning", "To turn right you position yourself…", "Para girar a la derecha te colocas…",
  [("as close as possible to the right edge", "lo más cerca posible del borde derecho"), ("in the centre of the road", "en el centro de la vía"), ("on the left", "a la izquierda")],
  "As close as possible.", "Ceñirse todo lo posible.")
Q("tr6", "turning", "To leave an autovía by a deceleration lane, you…", "Para salir de una autovía por un carril de deceleración…",
  [("signal early, enter it as soon as possible and slow down inside it", "señalizas con antelación, entras lo antes posible y frenas ya dentro"), ("brake on the main road first", "frenas antes en la vía principal"), ("enter at the last moment", "entras en el último momento")],
  "From the lane next to it.", "Desde el carril contiguo.")
Q("tr7", "turning", "On an interurban road, which vehicles wait on the right shoulder before turning left (when there is no special lane)?", "En vía interurbana, ¿qué vehículos esperan en el arcén derecho antes de girar a la izquierda (sin carril acondicionado)?",
  [("Cycles and two-wheeled mopeds", "Ciclos y ciclomotores de dos ruedas"), ("Motorcycles", "Motocicletas"), ("All two-wheelers", "Todos los de dos ruedas")],
  "Motorcycles turn from the centre like cars.", "Las motos giran desde el eje como los turismos.")

# ---------------------------------------------------------------- U-turn
Q("ut1", "uturn", "A U-turn (cambio de sentido) must be made…", "El cambio de sentido debe hacerse…",
  [("in one go and without reversing", "de un solo giro y sin marcha atrás"), ("in three movements", "en tres maniobras"), ("reversing if needed", "con marcha atrás si hace falta")],
  "At a suitable place, as quickly as possible.", "En un lugar adecuado y en el menor tiempo posible.")
Q("ut2", "uturn", "You wait in the carriageway to turn round and hold up those behind. You…", "Esperas en la calzada para cambiar de sentido y entorpeces a los de detrás. Tú…",
  [("leave the carriageway on the right if possible and wait there", "sales de la calzada por la derecha si es posible y esperas allí"), ("stay and use the hazard lights", "te quedas con la luz de emergencia"), ("turn round at once", "cambias de sentido enseguida")],
  "Until traffic lets you turn.", "Hasta que el tráfico lo permita.")
Q("ut3", "uturn", "On an autovía, may you turn round through an open gap in the median?", "En una autovía, ¿puedes cambiar de sentido por un paso abierto de la mediana?",
  [("No, never", "No, nunca"), ("Yes, if no one is coming", "Sí, si no viene nadie"), ("Yes, on a motorcycle", "Sí, en moto")],
  "Only at the places built for it, at a different level.", "Solo en lugares habilitados, a distinto nivel.")
Q("ut4", "uturn", "Turning round is forbidden…", "El cambio de sentido está prohibido…",
  [("wherever overtaking is forbidden, as a rule", "donde está prohibido adelantar, como norma general"), ("on all urban roads", "en todas las vías urbanas"), ("at roundabouts", "en glorietas")],
  "Roundabouts are an exception.", "Las glorietas son una excepción.")
Q("ut5", "uturn", "According to your course, may you turn round near (not on) a level crossing?", "Según tu curso, ¿puedes cambiar de sentido en las proximidades (no encima) de un paso a nivel?",
  [("Yes", "Sí"), ("No", "No"), ("Only in town", "Solo en poblado")],
  "On the level crossing itself, no.", "En el propio paso a nivel, no.")
Q("ut6", "uturn", "To turn round, what do you signal?", "Para cambiar de sentido, ¿qué señalizas?",
  [("That you will slow down a lot and move sideways", "Que vas a frenar considerablemente y a desplazarte lateralmente"), ("Only the hazard lights", "Solo la luz de emergencia"), ("Nothing, if nobody is behind", "Nada, si no viene nadie")],
  "With lights or the arm.", "Con luces o con el brazo.")
Q("ut7", "uturn", "May you turn round at a junction where you have signed priority?", "¿Puedes cambiar de sentido en una intersección donde tienes prioridad señalizada?",
  [("Yes, it is an exception", "Sí, es una excepción"), ("No", "No"), ("Only at night", "Solo de noche")],
  "Also at roundabouts.", "También en glorietas.")

# ---------------------------------------------------------------- immobilisations
Q("im1", "immob", "A stop (parada) lasts…", "Una parada dura…",
  [("less than two minutes, without abandoning the vehicle", "menos de dos minutos, sin abandonar el vehículo"), ("less than five minutes", "menos de cinco minutos"), ("as long as you like if you stay nearby", "lo que quieras si te quedas cerca")],
  "You may get off if you keep watching it.", "Puedes bajarte si lo vigilas.")
Q("im2", "immob", "Stopping at a red light is…", "Detenerse ante un semáforo en rojo es…",
  [("a detention", "una detención"), ("a stop (parada)", "una parada"), ("parking", "un estacionamiento")],
  "Imposed, not voluntary.", "Impuesta, no voluntaria.")
Q("im3", "immob", "Held up in a tunnel for more than two minutes, you must…", "Detenido en un túnel durante más de dos minutos, debes…",
  [("switch off the engine and keep the position lights on", "apagar el motor y mantener las luces de posición"), ("keep the engine running", "mantener el motor encendido"), ("switch off all lights", "apagar todas las luces")],
  "In any enclosed place.", "En cualquier lugar cerrado.")
Q("im4", "immob", "In town, on a two-way street, you park your motorcycle…", "En poblado, en una calle de doble sentido, estacionas tu moto…",
  [("on the right-hand side", "en el lado derecho"), ("on either side", "en cualquier lado"), ("on the left-hand side", "en el lado izquierdo")],
  "Both sides only on one-way streets.", "Ambos lados solo en sentido único.")
Q("im5", "immob", "On an interurban road you stop or park…", "En vía interurbana se para o estaciona…",
  [("off the carriageway, on the right, leaving the usable shoulder free", "fuera de la calzada, a la derecha, dejando libre la parte transitable del arcén"), ("on the shoulder", "en el arcén"), ("on the carriageway with hazard lights", "en la calzada con la luz de emergencia")],
  "Always off the carriageway.", "Siempre fuera de la calzada.")
Q("im6", "immob", "May you park your motorcycle on the pavement?", "¿Puedes estacionar tu moto en la acera?",
  [("Only if a municipal bylaw allows it and pedestrians aren’t hindered", "Solo si una ordenanza municipal lo permite y no se entorpece a los peatones"), ("Yes, always", "Sí, siempre"), ("Yes, if it is wide", "Sí, si es ancha")],
  "As a rule it is forbidden.", "Como norma está prohibido.")
Q("im7", "immob", "As a rule, vehicles are parked…", "Como norma general, los vehículos se estacionan…",
  [("parallel to the edge, one behind another", "en paralelo al borde, uno detrás de otro"), ("at an angle", "en oblicuo"), ("side by side (en batería)", "en batería")],
  "Other positions only if the road advises it.", "Otra colocación solo si la vía lo aconseja.")
Q("im8", "immob", "Before leaving your motorcycle parked, you must…", "Antes de dejar tu moto estacionada, debes…",
  [("switch off the engine, take the key and prevent unauthorised use", "apagar el motor, quitar la llave e impedir su uso sin autorización"), ("leave the engine running", "dejarla en marcha"), ("only put it on the stand", "solo ponerle la pata")],
  "And switch on any lights needed.", "Y encender las luces necesarias.")
Q("im9", "immob", "Since 1 October 2026, what must every motorcycle carry?", "Desde el 1 de octubre de 2026, ¿qué debe llevar toda motocicleta?",
  [("A high-visibility vest", "Un chaleco de alta visibilidad"), ("A V-16 warning light", "Una señal V-16"), ("Two warning triangles", "Dos triángulos")],
  "The V-16 is recommended, not compulsory, for motorcycles.", "La V-16 es recomendable, no obligatoria, en motos.")

# ---------------------------------------------------------------- no parking
Q("np1", "noparking", "Double parking is…", "La doble fila…",
  [("forbidden for parking, allowed for stopping", "está prohibida para estacionar; la parada sí se permite"), ("always allowed", "siempre se permite"), ("forbidden for both", "está prohibida para ambas")],
  "Double parking without the driver is serious.", "Sin conductor es grave.")
Q("np2", "noparking", "A broken yellow line along the kerb means…", "Una línea amarilla discontinua junto al bordillo significa…",
  [("no parking", "prohibido estacionar"), ("no stopping or parking", "prohibido parar y estacionar"), ("parking for motorcycles", "estacionamiento para motos")],
  "Continuous yellow: no stopping either.", "Continua: tampoco parar.")
Q("np3", "noparking", "Leaving less than 3 m between your parked vehicle and a continuous line is…", "Dejar menos de 3 m entre tu vehículo estacionado y una línea continua es…",
  [("a serious offence", "una infracción grave"), ("allowed for motorcycles", "permitido para motos"), ("a minor offence", "una infracción leve")],
  "It obstructs traffic seriously.", "Obstaculiza gravemente la circulación.")
Q("np4", "noparking", "May you stop for a moment on a pedestrian crossing?", "¿Puedes parar un momento en un paso de peatones?",
  [("No", "No"), ("Yes, under two minutes", "Sí, menos de dos minutos"), ("Yes, at night", "Sí, de noche")],
  "Stopping and parking are both forbidden.", "Están prohibidas la parada y el estacionamiento.")
Q("np5", "noparking", "May you stop on an autovía?", "¿Puedes parar en una autovía?",
  [("Only in the areas enabled for it", "Solo en las zonas habilitadas"), ("Yes, on the shoulder", "Sí, en el arcén"), ("Yes, under two minutes", "Sí, menos de dos minutos")],
  "Except emergencies.", "Salvo emergencias.")
Q("np6", "noparking", "In a time-limited parking zone, the council may remove your vehicle if you exceed…", "En zona de estacionamiento limitado, el ayuntamiento puede retirar tu vehículo si rebasas…",
  [("three times the time paid", "el triple del tiempo abonado"), ("twice the time paid", "el doble del tiempo abonado"), ("15 minutes", "15 minutos")],
  "Or if you have no ticket.", "O si no tienes título.")
Q("np7", "noparking", "Parking in a loading zone during its hours is…", "Estacionar en una zona de carga y descarga en horas de utilización es…",
  [("a serious offence", "una infracción grave"), ("allowed for motorcycles", "permitido para motos"), ("allowed under 10 minutes", "permitido menos de 10 minutos")],
  "It obstructs seriously.", "Obstaculiza gravemente.")
Q("np8", "noparking", "Stopping in a cycle lane is…", "Parar en un carril bici está…",
  [("forbidden", "prohibido"), ("allowed under two minutes", "permitido menos de dos minutos"), ("allowed for two-wheelers", "permitido a los de dos ruedas")],
  "Also cycle crossings.", "También en pasos para ciclistas.")
Q("np9", "noparking", "May you park in front of a properly signed dropped kerb (vado)?", "¿Puedes estacionar delante de un vado correctamente señalizado?",
  [("No", "No"), ("Yes, a motorcycle", "Sí, una moto"), ("Yes, at night", "Sí, de noche")],
  "Blocking it is serious.", "Obstaculizarlo es grave.")
Q("np10", "noparking", "Stopping near a junction is forbidden if…", "Parar cerca de una intersección está prohibido si…",
  [("it hinders others turning (out of town, if it creates danger through lack of visibility)", "dificulta el giro (en interurbanas, si genera peligro por falta de visibilidad)"), ("always", "siempre"), ("never", "nunca")],
  "Otherwise it may be allowed.", "Si no, puede estar permitido.")
