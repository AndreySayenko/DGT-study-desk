# -*- coding: utf-8 -*-
"""Question bank for the interactive Topic 4 page (priority). In every question the FIRST option is the
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
    "signed": dict(sec=1, en="Junctions with signs", es="Intersecciones señalizadas",
        recap=[("Priority follows the signs: agents, traffic lights, vertical signs, road markings (in that order if they disagree, after temporary signs).",
                "La prioridad la marcan las señales: agentes, semáforos, señales verticales y marcas viales (en ese orden si se contradicen, tras las circunstanciales)."),
               ("Give way or STOP: give way to vehicles on the priority road from either side; STOP always means a full stop.",
                "Ceda el paso o stop: se cede a los de la vía preferente vengan por donde vengan; el stop obliga siempre a detenerse."),
               ("Stop at the stop line or, if there is none, immediately before the junction.",
                "La detención, ante la línea de detención o, si no la hay, inmediatamente antes de la intersección."),
               ("Not enough visibility from there? Stop again where you can see, without endangering anyone.",
                "¿Sin visibilidad suficiente? Detenerse de nuevo donde se tenga, sin poner en peligro a nadie.")],
        trap=("Thinking that at a give-way sign you only yield to vehicles from the right.",
              "Pensar que en un ceda el paso solo se cede a los que vienen por la derecha.")),
    "unsigned": dict(sec=1, en="Junctions without signs", es="Intersecciones sin señalizar",
        recap=[("General rule: give way to vehicles approaching from your right.", "Norma general: ceder el paso a los que se aproximan por la derecha."),
               ("Exceptions: paved over unpaved; rail vehicles over everyone; inside a roundabout over those entering; on a motorway over those joining.",
                "Excepciones: pavimentada sobre sin pavimentar; raíles sobre todos; dentro de la glorieta sobre los que entran; en la autopista sobre los que acceden."),
               ("The P-2 sign changes nothing: it reminds you of these rules.", "La señal P-2 no cambia nada: recuerda estas normas."),
               ("A vehicle on your left gives way to you, unless an exception favours it.", "El que viene por tu izquierda te cede el paso, salvo que una excepción le favorezca.")],
        trap=("Applying the right-hand rule to a car coming out of an unpaved track or into a roundabout.",
              "Aplicar la regla de la derecha a quien sale de un camino de tierra o entra en una glorieta.")),
    "conduct": dict(sec=1, en="How to act at junctions", es="Normas de actuación",
        recap=[("Giving way: do not start or carry on if you would force the other driver to brake or swerve.",
                "Al ceder el paso: no iniciar ni continuar si obligas al otro a frenar o desviarse bruscamente."),
               ("Show early that you will give way, above all by slowing down gradually.",
                "Demostrar con antelación que se va a ceder, sobre todo reduciendo la velocidad paulatinamente."),
               ("With priority: still do not enter a junction or a pedestrian or cycle crossing if you may get stuck there.",
                "Con prioridad: tampoco se entra en una intersección o paso para peatones o ciclistas si se puede quedar detenido."),
               ("Stuck inside a junction with lights: leave without waiting for your green, without hindering anyone.",
                "Detenido dentro de una intersección con semáforo: salir sin esperar al verde, sin entorpecer.")],
        trap=("Believing that a green light means you may enter even when the exit is blocked.",
              "Creer que el verde permite entrar aunque la salida esté bloqueada.")),
    "rail": dict(sec=2, en="Level crossings, bridges and rail vehicles", es="Pasos a nivel, puentes móviles y raíles",
        recap=[("Approaching a level crossing or movable bridge: extreme care and slow down below the limit.",
                "Al acercarse a un paso a nivel o puente móvil: extremar la prudencia y bajar de la velocidad máxima."),
               ("Never enter with barriers down or moving, or lights showing stop; queue one behind another.",
                "No entrar con barreras bajadas o en movimiento, o semáforo de detención; esperar uno detrás de otro."),
               ("No barriers or lights: make sure no train is coming; stopping to look is not compulsory. Cross without delay.",
                "Sin barreras ni semáforos: asegurarse de que no viene ningún tren; detenerse no es obligatorio. Cruzar sin demora."),
               ("Stuck: get people out, clear the crossing; if impossible, warn train drivers and other drivers. Trains always first; trams from right and left except over priority vehicles.",
                "Detenido: desalojar, dejar libre el paso; si no, avisar a maquinistas y conductores. El tren siempre; el tranvía por derecha e izquierda salvo ante prioritarios.")],
        trap=("Thinking you must always stop at a level crossing without barriers, or that trams beat ambulances.",
              "Creer que siempre hay que detenerse en un paso sin barreras, o que el tranvía pasa antes que una ambulancia.")),
    "tunnels": dict(sec=2, en="Tunnels and underpasses", es="Túneles y pasos inferiores",
        recap=[("Tunnels of any length and underpasses over 200 m are signed.", "Se señalizan los túneles de cualquier longitud y los pasos inferiores de más de 200 m."),
               ("Obey the lights, the variable-message panels and loudspeaker instructions.", "Obedecer semáforos, paneles de mensaje variable e instrucciones por megafonía."),
               ("Forbidden: stopping, parking, turning round, reversing; overtaking in two-way tunnels unless 2+ lanes your way. Lights on.",
                "Prohibido: parar, estacionar, cambiar de sentido, marcha atrás; adelantar en doble sentido salvo 2 o más carriles para tu sentido. Alumbrado encendido."),
               ("Distance: 100 m or 4 s; over 3,500 kg: 150 m or 6 s.", "Distancia: 100 m o 4 s; más de 3.500 kg: 150 m o 6 s.")],
        trap=("Mixing up 100 m / 4 s (cars) with 150 m / 6 s (over 3,500 kg).", "Confundir 100 m / 4 s (turismos) con 150 m / 6 s (más de 3.500 kg).")),
    "peds": dict(sec=3, en="Pedestrians", es="Peatones",
        recap=[("Pedestrian crossings, pavements and pedestrian zones; and since October 2026, single-platform streets.",
                "Pasos para peatones, aceras y zonas peatonales; y desde octubre de 2026, calles de plataforma única."),
               ("A vehicle turning into another road gives way to pedestrians crossing it, even with no crossing.",
                "El vehículo que gira para entrar en otra vía cede a los peatones que la cruzan, aunque no haya paso."),
               ("Crossing a shoulder used by pedestrians, or a pedestrian zone through its passage (garage), pedestrians go first.",
                "Al cruzar un arcén con peatones, o una zona peatonal por su paso habilitado (garaje), pasan primero los peatones."),
               ("Bus passengers between the bus and the pavement at a signed stop; troops, school rows and processions.",
                "Viajeros entre el autobús y la acera en una parada señalizada; tropas, filas escolares y comitivas organizadas.")],
        trap=("Thinking pedestrians only have priority on a marked crossing.", "Pensar que los peatones solo tienen prioridad en un paso señalizado.")),
    "cyclists": dict(sec=3, en="Cyclists", es="Ciclistas",
        recap=[("On a signed cycle lane, cycle crossing or hard shoulder.", "En carril bici, paso para ciclistas o arcén debidamente señalizados."),
               ("When a motor vehicle or moped turns right or left into another road and a cyclist is close by.",
                "Cuando un vehículo de motor o ciclomotor gira a derecha o izquierda para entrar en otra vía y hay un ciclista próximo."),
               ("A group is one moving unit once the first has started crossing or entered a roundabout.",
                "Un grupo es una unidad móvil cuando el primero ha iniciado el cruce o entrado en la glorieta."),
               ("Every other case: the general rules between vehicles.", "En los demás casos, las normas generales entre vehículos.")],
        trap=("Cutting into a group of cyclists after the leader has entered the roundabout.", "Meterse en un grupo de ciclistas cuando el primero ya ha entrado en la glorieta.")),
    "animals": dict(sec=3, en="Animals", es="Animales",
        recap=[("Drivers have priority over animals, with three exceptions.", "Los conductores tienen prioridad sobre los animales, con tres excepciones."),
               ("Signed cañadas: the animals go first.", "En cañadas señalizadas, pasan primero los animales."),
               ("Turning into a road that animals are crossing, even without a cañada; crossing a shoulder they walk along.",
                "Al girar para entrar en una vía que cruzan animales, aunque no haya cañada; al cruzar un arcén por el que circulan."),
               ("A cañada is signed with a «cañada» panel under the domestic animals sign, plus speed limits.",
                "La cañada se señaliza con un panel «cañada» bajo la señal de animales domésticos, más limitación de velocidad.")],
        trap=("Thinking animals always have priority, or never.", "Pensar que los animales tienen siempre prioridad, o nunca.")),
    "narrow": dict(sec=4, en="Narrow stretches", es="Estrechamientos",
        recap=[("Signs first: agents, lights, R-6 (blue square: you go first), R-5 (red circle: you give way).",
                "Primero las señales: agentes, semáforos, R-6 (cuadrado azul: pasas tú), R-5 (círculo rojo: cedes)."),
               ("No signs: whoever entered first. In doubt: the harder to manoeuvre, by the 10-step list.",
                "Sin señales: el que entró primero. En duda: el de mayor dificultad de maniobra, según la lista de 10."),
               ("Order: oversize specials, combinations, animal-drawn, car + trailer ≤ 750 kg and motorhomes, buses, lorries, cars, small specials and quads, 3 wheels, 2 wheels.",
                "Orden: especiales que exceden, conjuntos, tracción animal, turismo + remolque ≤ 750 kg y autocaravanas, autobuses, camiones, turismos, especiales pequeños y cuadriciclos, 3 ruedas, 2 ruedas."),
               ("Same type: longer reverse, then width, length or MMA. Gradient ≥ 7 %: uphill first, unless it can reach a lay-by first.",
                "Mismo tipo: mayor marcha atrás, después anchura, longitud o MMA. Pendiente ≥ 7 %: el que sube, salvo que llegue antes a un apartadero.")],
        trap=("Using the vehicle list when it is clear who entered first.", "Usar la lista de vehículos cuando está claro quién entró primero.")),
    "bridges": dict(sec=4, en="Narrow bridges", es="Puentes y obras de paso",
        recap=[("Signs decide the order on a narrow bridge.", "La señalización decide el orden en un puente estrecho."),
               ("Meeting on it: the one who came in by the end with R-5 or give way reverses.", "Si se encuentran, retrocede el que entró por el extremo con R-5 o ceda el paso."),
               ("No signs: the order of vehicles for narrow stretches.", "Sin señales: el orden de vehículos de los estrechamientos."),
               ("Vehicles with a special permit may not pass each other on bridges under 6 m wide.", "Los vehículos con autorización especial no se cruzan en puentes de menos de 6 m.")],
        trap=("Thinking the bigger vehicle always has the right to stay on the bridge.", "Pensar que el vehículo más grande siempre tiene derecho a quedarse en el puente.")),
    "priority": dict(sec=5, en="Priority vehicles", es="Vehículos prioritarios",
        recap=[("Police, fire, civil protection and ambulances, public or private, on urgent service; also maintenance crews and roadside assistance.",
                "Policía, bomberos, protección civil y asistencia sanitaria, públicos o privados, en servicio urgente; también mantenimiento y auxilio en carretera."),
               ("Light (V-1, blue, visible at 50 m) and siren together; the light alone only if that is no danger.",
                "Luz (V-1, azul, visible a 50 m) y sirena a la vez; solo la luz si no entraña peligro."),
               ("May exceed limits and ignore rules and signs on their own responsibility, never agents’ instructions.",
                "Pueden superar los límites y no cumplir normas o señales bajo su responsabilidad, nunca las órdenes de los agentes."),
               ("At junctions and lights they make sure others have stopped; on motorways they may exceptionally turn, reverse, go against traffic on the shoulder or cross the median.",
                "En intersecciones y semáforos se aseguran de que los demás han parado; en autopista pueden excepcionalmente dar la vuelta, retroceder, ir en sentido contrario por el arcén o cruzar la mediana.")],
        trap=("Thinking priority vehicles may also ignore agents’ instructions.", "Pensar que los prioritarios pueden ignorar también las órdenes de los agentes.")),
    "nonprio": dict(sec=5, en="Non-priority vehicles in an emergency", es="No prioritarios en servicio de urgencia",
        recap=[("Only in especially serious circumstances and with no other means.", "Solo en circunstancias especialmente graves y sin otro medio."),
               ("Horn on and off plus hazard lights, or a handkerchief waved.", "Claxon intermitente y luz de emergencia, o un pañuelo agitado."),
               ("No priority: every traffic rule applies, above all at junctions.", "Sin prioridad: todas las normas, sobre todo en las intersecciones."),
               ("Agents may ask for justification at any time.", "Los agentes pueden exigir la justificación en cualquier momento.")],
        trap=("Thinking hazard lights and the horn give an ordinary car the right to skip red lights.",
              "Pensar que la luz de emergencia y el claxon permiten a un turismo saltarse los semáforos.")),
    "yield": dict(sec=5, en="Making way for emergencies", es="Facilitar el paso a los vehículos de urgencia",
        recap=[("Make way for any vehicle on emergency service, priority or not.", "Facilitar el paso a todo vehículo en servicio de urgencia, prioritario o no."),
               ("Normally move to your right, and stop if necessary.", "Normalmente apartarse a la derecha y detenerse si es preciso."),
               ("Queue at walking pace or stopped on a motorway: open the emergency corridor.", "Retención a paso de peatón o detenida en autopista: abrir el carril de emergencia."),
               ("2 lanes: centre. 3+: between the left lane and the next.", "2 carriles: centro. 3 o más: entre el izquierdo y su contiguo.")],
        trap=("Opening the corridor on the hard shoulder, or waiting for the siren before opening it.",
              "Abrir el hueco en el arcén, o esperar a oír la sirena para abrirlo.")),
}


# ---------------------------------------------------------------- 1.1 signed junctions
Q("sg1", "signed", "Priority (preferencia de paso) is…", "La prioridad o preferencia de paso es…",
  [("the right to go before another road user at a junction or where your paths cross", "el derecho a pasar antes que otro usuario en las intersecciones o cuando se cruzan sus trayectorias"),
   ("the duty to stop at every junction", "la obligación de detenerse en todas las intersecciones"), ("the right to drive faster than others", "el derecho a circular más rápido que los demás")],
  "A junction is where vehicle paths cross at the same level.", "Una intersección es donde las trayectorias se cruzan a nivel.")
Q("sg2", "signed", "At a give-way sign, you give way to vehicles on the priority road coming from…", "Ante una señal de ceda el paso, se cede a los vehículos de la vía preferente que vienen…",
  [("either side", "por cualquiera de los dos lados"), ("the right only", "solo por la derecha"), ("the left only", "solo por la izquierda")],
  "Whichever side they approach from.", "Cualquiera que sea el lado por el que se aproximen.")
Q("sg3", "signed", "Where do you stop at a STOP sign if there is no stop line?", "¿Dónde te detienes en un stop si no hay línea de detención?",
  [("Immediately before the junction", "Inmediatamente antes de la intersección"), ("Next to the sign, wherever it is", "Junto a la señal, esté donde esté"),
   ("Inside the junction, where you can see", "Dentro de la intersección, donde se vea")],
  "With a line, you stop at the line.", "Si hay línea, ante la línea.")
Q("sg4", "signed", "You have stopped at a STOP line but cannot see the priority road well. What do you do?", "Te has detenido en la línea de un stop pero no ves bien la vía preferente. ¿Qué haces?",
  [("Stop again where you can see, without endangering anyone", "Detenerme de nuevo donde tenga visibilidad, sin poner en peligro a nadie"),
   ("Carry on slowly without stopping again", "Seguir despacio sin volver a detenerme"), ("Sound the horn and cross", "Tocar el claxon y cruzar")],
  "The second stop is part of the rule when visibility is poor.", "La segunda detención forma parte de la norma cuando falta visibilidad.")
Q("sg5", "signed", "At a give-way sign, must you always come to a complete stop?", "Ante un ceda el paso, ¿hay que detenerse siempre por completo?",
  [("Only when necessary to give way", "Solo cuando sea preciso para ceder el paso"), ("Yes, always", "Sí, siempre"), ("Never", "Nunca")],
  "STOP is the sign that always requires a full stop.", "La señal que obliga siempre a detenerse es el stop.")
Q("sg6", "signed", "Which of these gives you priority?", "¿Cuál de estas te da prioridad?",
  [("A triangular P-1 sign whose thick line is your road", "Una señal triangular P-1 cuya línea gruesa es tu vía"), ("An inverted-triangle R-1 sign", "Una señal R-1 de triángulo invertido"),
   ("A steady amber light", "Una luz ámbar fija")],
  "The yellow diamond (priority road) and a green light also give priority.", "El rombo amarillo (calzada con prioridad) y la luz verde también la dan.")
Q("sg7", "signed", "Which of these takes priority away from you?", "¿Cuál de estas te quita la prioridad?",
  [("A sign announcing a roundabout ahead", "Una señal que anuncia una glorieta próxima"), ("A green light", "Una luz verde"), ("The yellow diamond sign", "La señal del rombo amarillo")],
  "At the roundabout you will give way to those already inside.", "En la glorieta cederás el paso a los que ya están dentro.")
Q("sg8", "signed", "An agent signals you to go, but the traffic light is red. You obey…", "Un agente te indica que pases, pero el semáforo está en rojo. Obedeces…",
  [("the agent", "al agente"), ("the traffic light", "al semáforo"), ("whichever is more restrictive", "a la indicación más restrictiva")],
  "Agents’ signals come first, then temporary signs, lights, vertical signs and markings.", "Primero los agentes; después la señalización circunstancial, semáforos, señales verticales y marcas viales.")
Q("sg9", "signed", "A STOP sign obliges you to…", "La señal de stop obliga a…",
  [("stop completely, even if nobody is coming", "detenerse por completo, aunque no venga nadie"), ("stop only if vehicles are coming", "detenerse solo si vienen vehículos"),
   ("slow down without stopping", "reducir la velocidad sin detenerse")],
  "Then give way to vehicles on the road you approach.", "Después se cede el paso a los vehículos de la vía a la que se accede.")

# ---------------------------------------------------------------- 1.2 unsigned junctions
Q("us1", "unsigned", "At a junction with no signs, the general rule is to give way to vehicles…", "En una intersección sin señalizar, la norma general es ceder el paso a los vehículos…",
  [("approaching from your right", "que se aproximen por la derecha"), ("approaching from your left", "que se aproximen por la izquierda"), ("on the wider road", "de la vía más ancha")],
  "Unless one of the four exceptions applies.", "Salvo que se dé alguna de las cuatro excepciones.")
Q("us2", "unsigned", "Unsigned junction: you are on a paved road and a car comes out of an unpaved track on your right. Who goes first?",
  "Intersección sin señalizar: vas por una vía pavimentada y un turismo sale por tu derecha de un camino sin pavimentar. ¿Quién pasa primero?",
  [("You", "Tú"), ("The car on your right", "El turismo de tu derecha"), ("Whoever arrives first", "El que llegue primero")],
  "Paved road beats unpaved road, whatever the side.", "La vía pavimentada pasa antes que la no pavimentada, sea cual sea el lado.")
Q("us3", "unsigned", "Unsigned junction: a tram comes from your left. Who goes first?", "Intersección sin señalizar: un tranvía viene por tu izquierda. ¿Quién pasa primero?",
  [("The tram", "El tranvía"), ("You, because it is on your left", "Tú, porque viene por tu izquierda"), ("Whoever arrives first", "El que llegue primero")],
  "Vehicles on rails have priority over the other road users.", "Los vehículos que circulan por raíles tienen prioridad sobre los demás usuarios.")
Q("us4", "unsigned", "At a roundabout with no signs, who has priority?", "En una glorieta sin señalizar, ¿quién tiene prioridad?",
  [("Those already inside the ring", "Los que ya circulan por el anillo"), ("Those entering from the right", "Los que entran por la derecha"), ("The larger vehicle", "El vehículo más grande")],
  "Those inside have priority over those who want to enter.", "Los de dentro tienen prioridad sobre los que pretenden acceder.")
Q("us5", "unsigned", "The P-2 sign “Junction with priority to the right”…", "La señal P-2 «Intersección con prioridad de la derecha»…",
  [("does not change priority: it reminds you that the general rules apply", "no modifica la prioridad: recuerda que se aplican las normas generales"),
   ("gives priority to whoever comes from the right in every case, even from an unpaved track", "da prioridad al que viene por la derecha en todo caso, incluso desde un camino sin pavimentar"),
   ("means vehicles from the right must stop", "indica que los de la derecha deben detenerse")],
  "The four exceptions still apply.", "Las cuatro excepciones siguen aplicándose.")
Q("us6", "unsigned", "You are on an autovía and a car is joining from the slip road on your right. Who goes first?", "Circulas por una autovía y un turismo se incorpora desde el carril de la derecha. ¿Quién pasa primero?",
  [("You, already on the autovía", "Tú, que ya circulas por la autovía"), ("The joining car, since it is on your right", "El que se incorpora, por venir por la derecha"), ("Whoever is faster", "El más rápido")],
  "Vehicles on an autopista or autovía have priority over those joining it.", "Los que circulan por autopista o autovía tienen prioridad sobre los que acceden.")
Q("us7", "unsigned", "Unsigned junction: a car comes from your left on an ordinary paved road. Who goes first?", "Intersección sin señalizar: un turismo viene por tu izquierda por una vía pavimentada normal. ¿Quién pasa primero?",
  [("You, unless someone is coming from your right", "Tú, salvo que venga alguien por tu derecha"), ("The car on your left", "El de tu izquierda"), ("The larger vehicle", "El vehículo más grande")],
  "You are the one on its right.", "Tú eres el que viene por su derecha.")

# ---------------------------------------------------------------- 1.3 how to act
Q("co1", "conduct", "If you must give way, you may not start or carry on until…", "Si debes ceder el paso, no puedes iniciar ni continuar la marcha hasta…",
  [("you are sure you will not force the driver with priority to change path or speed abruptly", "asegurarte de que no obligas al que tiene prioridad a modificar bruscamente su trayectoria o velocidad"),
   ("the other vehicle is 10 m away", "que el otro esté a 10 m"), ("you have signalled your manoeuvre", "haber señalizado la maniobra")],
  "Signalling never gives you the right to go.", "Señalizar nunca da derecho a pasar.")
Q("co2", "conduct", "Your light is green but the exit beyond the junction is full of stopped cars. You…", "Tu semáforo está en verde, pero la salida de la intersección está llena de vehículos detenidos. Tú…",
  [("wait before the junction", "esperas antes de la intersección"), ("enter, because you have priority", "entras, porque tienes prioridad"), ("enter halfway and wait", "entras hasta la mitad y esperas")],
  "Never enter if you will probably stop inside and block the cross traffic.", "No se entra si previsiblemente se va a quedar detenido obstruyendo la circulación transversal.")
Q("co3", "conduct", "How do you show early that you will give way?", "¿Cómo se demuestra con antelación que se va a ceder el paso?",
  [("By slowing down gradually", "Reduciendo paulatinamente la velocidad"), ("By flashing your headlights", "Con ráfagas de luz"), ("By sounding the horn", "Tocando el claxon")],
  "Your way of driving must make it clear.", "La forma de circular debe dejarlo claro.")
Q("co4", "conduct", "You are stuck inside a junction with traffic lights and your light turns red. You…", "Te has quedado detenido dentro de una intersección con semáforo y tu semáforo se pone en rojo. Tú…",
  [("leave it without waiting for green, without hindering those who now have green", "sales sin esperar al verde, sin entorpecer a quienes ahora lo tienen"),
   ("stay until your light turns green again", "esperas a que tu semáforo vuelva a ponerse verde"), ("reverse to the stop line", "retrocedes hasta la línea de detención")],
  "You are an obstacle there, so you get out.", "Ahí eres un obstáculo, así que debes salir.")
Q("co5", "conduct", "Even with priority, you must not enter a pedestrian crossing if…", "Aun teniendo prioridad, no debes entrar en un paso para peatones si…",
  [("you may be left stopped on it, blocking the cross traffic", "puedes quedar detenido en él obstruyendo la circulación transversal"), ("it has no traffic lights", "no tiene semáforo"),
   ("it is night", "es de noche")],
  "Same for junctions and cycle crossings.", "Igual en intersecciones y pasos para ciclistas.")
Q("co6", "conduct", "A yellow criss-cross grid painted on a junction means…", "Una cuadrícula amarilla pintada en una intersección indica…",
  [("do not enter if you may have to stop inside", "no entrar si se puede quedar detenido dentro"), ("a taxi rank", "una parada de taxis"),
   ("a place to stop and wait for a gap", "un lugar para detenerse a esperar un hueco")],
  "It keeps the junction clear for cross traffic.", "Mantiene libre la intersección para el tráfico transversal.")

# ---------------------------------------------------------------- 2.1 level crossings and rails
Q("rl1", "rail", "Approaching a level crossing, you must…", "Al aproximarte a un paso a nivel, debes…",
  [("take extreme care and slow down below the maximum allowed", "extremar la prudencia y reducir la velocidad por debajo de la máxima permitida"),
   ("keep your speed to cross quickly", "mantener la velocidad para cruzar rápido"), ("always stop", "detenerte siempre")],
  "Same for movable bridges.", "Igual ante un puente móvil.")
Q("rl2", "rail", "The half-barriers of a level crossing are rising. You…", "Las semibarreras de un paso a nivel están subiendo. Tú…",
  [("may not enter while they are moving", "no puedes entrar mientras estén en movimiento"), ("may enter: they are opening", "puedes entrar: se están abriendo"),
   ("may enter if no train is in sight", "puedes entrar si no se ve ningún tren")],
  "Not while they are going up or down.", "Ni subiendo ni bajando.")
Q("rl3", "rail", "At a level crossing without barriers or lights, you…", "En un paso a nivel sin barreras ni semáforos, tú…",
  [("make sure no train is coming; stopping is not compulsory", "te aseguras de que no se acerca ningún tren; no es obligatorio detenerse"),
   ("must always stop before crossing", "debes detenerte siempre antes de cruzar"), ("cross quickly: the train will see you", "cruzas rápido: el tren te verá")],
  "Unless a STOP sign tells you to stop.", "Salvo que una señal de stop obligue a detenerse.")
Q("rl4", "rail", "Your car breaks down on a level crossing. First you…", "Tu turismo se avería en un paso a nivel. Lo primero es…",
  [("get the occupants out quickly and try to clear the crossing", "desalojar rápidamente a los ocupantes e intentar dejar el paso libre"),
   ("stay inside and wait for help", "quedarse dentro y esperar ayuda"), ("switch on the hazard lights and wait", "encender la luz de emergencia y esperar")],
  "Same if your load falls onto the crossing.", "Igual si se cae la carga dentro del paso.")
Q("rl5", "rail", "If you cannot clear the level crossing, you must…", "Si no consigues dejar libre el paso a nivel, debes…",
  [("make sure train drivers and other drivers are warned of the danger in good time", "conseguir que los maquinistas y los demás conductores sean advertidos del peligro con antelación"),
   ("leave without doing anything else", "marcharte sin hacer nada más"), ("wait inside the vehicle", "esperar dentro del vehículo")],
  "Using every means you have.", "Con todas las medidas a tu alcance.")
Q("rl6", "rail", "At a junction without priority signs, a tram and an ambulance on urgent service meet. Who goes first?",
  "En una intersección sin señal de preferencia coinciden un tranvía y una ambulancia en servicio urgente. ¿Quién pasa primero?",
  [("The ambulance", "La ambulancia"), ("The tram, which always has priority", "El tranvía, que siempre tiene prioridad"), ("Whoever comes from the right", "El que venga por la derecha")],
  "Trams have priority from right and left, except over priority vehicles on urgent service.", "El tranvía tiene prioridad por la derecha y por la izquierda, salvo sobre los prioritarios en servicio de urgencia.")
Q("rl7", "rail", "Do trains have priority?", "¿Tienen prioridad los trenes?",
  [("Yes, always", "Sí, siempre"), ("Only at crossings without barriers", "Solo en pasos sin barreras"), ("Only at night", "Solo de noche")],
  "Because of their characteristics.", "Por sus características particulares.")
Q("rl8", "rail", "How do you cross a level crossing?", "¿Cómo se cruza un paso a nivel?",
  [("Without delay, once sure you will not get stuck inside", "Sin demora, tras asegurarse de que no se va a quedar inmovilizado dentro"),
   ("Slowly, stopping on the rails to look", "Despacio, deteniéndose sobre las vías para mirar"), ("Only in first gear", "Solo en primera velocidad")],
  "Check the exit is clear before you go onto the tracks.", "Comprueba que la salida está libre antes de entrar en las vías.")
Q("rl9", "rail", "May signs give drivers priority over trams?", "¿Pueden las señales dar prioridad a los conductores sobre los tranvías?",
  [("Yes", "Sí"), ("No, trams always go first", "No, el tranvía pasa siempre primero"), ("Only in town centres", "Solo en el centro de las ciudades")],
  "The tram’s general priority applies at junctions without priority signs.", "La prioridad general del tranvía rige en intersecciones sin señal de preferencia.")

# ---------------------------------------------------------------- 2.2 tunnels
Q("tn1", "tunnels", "Which underpasses must be signed?", "¿Qué pasos inferiores deben estar señalizados?",
  [("Those longer than 200 m", "Los de más de 200 m"), ("All of them", "Todos"), ("Those longer than 500 m", "Los de más de 500 m")],
  "Tunnels are signed whatever their length.", "Los túneles, sea cual sea su longitud.")
Q("tn2", "tunnels", "Inside a tunnel it is forbidden to…", "Dentro de un túnel está prohibido…",
  [("stop, park, turn round and reverse", "parar, estacionar, cambiar de sentido y dar marcha atrás"), ("use dipped headlights", "usar la luz de cruce"), ("drive at the speed limit", "circular al límite de velocidad")],
  "Overtaking is restricted too.", "El adelantamiento también está restringido.")
Q("tn3", "tunnels", "Overtaking in a two-way tunnel is…", "Adelantar en un túnel de doble sentido está…",
  [("forbidden, unless there is more than one lane for your direction", "prohibido, salvo que haya más de un carril para tu sentido"), ("allowed if visibility is good", "permitido si hay buena visibilidad"),
   ("allowed for motorcycles", "permitido a las motocicletas")],
  "With 2+ lanes your way, without entering the opposite direction.", "Con 2 o más carriles en tu sentido, sin invadir el contrario.")
Q("tn4", "tunnels", "In a tunnel, when not overtaking, a car keeps at least…", "En un túnel, cuando no adelanta, un turismo mantiene al menos…",
  [("100 m or 4 seconds", "100 m o 4 segundos"), ("50 m or 2 seconds", "50 m o 2 segundos"), ("150 m or 6 seconds", "150 m o 6 segundos")],
  "Vehicles over 3,500 kg: 150 m or 6 s.", "Más de 3.500 kg: 150 m o 6 s.")
Q("tn5", "tunnels", "In a tunnel, a vehicle with an MMA over 3,500 kg keeps at least…", "En un túnel, un vehículo de MMA superior a 3.500 kg mantiene al menos…",
  [("150 m or 6 seconds", "150 m o 6 segundos"), ("100 m or 4 seconds", "100 m o 4 segundos"), ("200 m or 8 seconds", "200 m o 8 segundos")],
  "Or three chevrons in sight.", "O la visión de tres galones.")
Q("tn6", "tunnels", "The traffic light at a tunnel entrance is red. You…", "El semáforo a la entrada de un túnel está en rojo. Tú…",
  [("do not enter", "no entras"), ("enter slowly", "entras despacio"), ("enter if there is no one inside", "entras si no hay nadie dentro")],
  "Tunnel lights and message panels must always be obeyed.", "Los semáforos y paneles del túnel se obedecen siempre.")
Q("tn7", "tunnels", "In a tunnel you hear instructions over the loudspeakers. You…", "En un túnel oyes instrucciones por megafonía. Tú…",
  [("follow them", "las sigues"), ("ignore them if the light is green", "las ignoras si el semáforo está en verde"), ("only follow agents in person", "solo obedeces a agentes en persona")],
  "Or any other means the tunnel uses to reach you.", "O cualquier otro medio que use el túnel.")

# ---------------------------------------------------------------- 3.1 pedestrians
Q("pe1", "peds", "Pedestrians have priority on…", "Los peatones tienen prioridad en…",
  [("signed pedestrian crossings, pavements and pedestrian zones", "los pasos para peatones señalizados, las aceras y las zonas peatonales"), ("any part of the road", "cualquier parte de la vía"),
   ("only crossings with traffic lights", "solo los pasos con semáforo")],
  "Plus the other listed cases.", "Además de los demás casos de la lista.")
Q("pe2", "peds", "You turn right into another street and pedestrians are crossing it where there is no crossing. Who goes first?",
  "Giras a la derecha para entrar en otra calle y hay peatones cruzándola donde no hay paso. ¿Quién pasa primero?",
  [("The pedestrians", "Los peatones"), ("You, since there is no crossing", "Tú, porque no hay paso"), ("Whoever arrives first", "El que llegue primero")],
  "Even without a pedestrian crossing.", "Aunque no exista paso para peatones.")
Q("pe3", "peds", "You cross a hard shoulder to turn off, and pedestrians are walking along it (there is no pavement). Who goes first?",
  "Cruzas un arcén para salir de la vía y por él caminan peatones (no hay acera). ¿Quién pasa primero?",
  [("The pedestrians", "Los peatones"), ("You", "Tú"), ("Whoever is faster", "El más rápido")],
  "They have no pedestrian zone, so the shoulder is theirs.", "No disponen de zona peatonal, así que el arcén es suyo.")
Q("pe4", "peds", "Pedestrians who have just got off a bus at a signed stop are between the bus and the pavement. They…",
  "Unos peatones acaban de bajar de un autobús en una parada señalizada y están entre el autobús y la acera. Ellos…",
  [("have priority", "tienen prioridad"), ("must wait for a gap in the traffic", "deben esperar un hueco en el tráfico"), ("only have priority if they are children", "solo tienen prioridad si son niños")],
  "Also those about to get on.", "También los que van a subir.")
Q("pe5", "peds", "A school row is crossing the road on foot. It…", "Una fila escolar cruza la calzada a pie. Tiene…",
  [("has priority over vehicles", "prioridad sobre los vehículos"), ("must give way to vehicles", "que ceder el paso a los vehículos"), ("has priority only with an agent present", "prioridad solo si hay un agente")],
  "So do troops and organised processions.", "Igual las unidades militares y las comitivas organizadas.")
Q("pe6", "peds", "Leaving a garage across the pavement, who goes first?", "Al salir de un garaje cruzando la acera, ¿quién pasa primero?",
  [("The pedestrians on the pavement", "Los peatones de la acera"), ("You, if you signal", "Tú, si señalizas"), ("Whoever is on the right", "El que esté a la derecha")],
  "Vehicles crossing a pedestrian zone through its passage give way to pedestrians.", "Los vehículos que cruzan una zona peatonal por su paso habilitado ceden a los peatones.")
Q("pe7", "peds", "Since October 2026, on a single-platform street (road and pavement at the same level)…", "Desde octubre de 2026, en una calle de plataforma única (calzada y acera al mismo nivel)…",
  [("pedestrians have priority", "los peatones tienen prioridad"), ("vehicles have priority", "los vehículos tienen prioridad"), ("whoever comes from the right goes first", "pasa primero quien venga por la derecha")],
  "Its generic speed limit is also the lowest: 20 km/h.", "Su límite genérico de velocidad es además el más bajo: 20 km/h.")
Q("pe8", "peds", "Which of these counts as a vulnerable road user under the 2026 reform?", "¿Cuál de estos es un usuario vulnerable según la reforma de 2026?",
  [("A motorcyclist", "Un motorista"), ("A lorry driver", "Un camionero"), ("A bus driver", "Un conductor de autobús")],
  "Also pedestrians, cyclists, personal mobility vehicle users and moped riders.", "También peatones, ciclistas, usuarios de vehículos de movilidad personal y de ciclomotores.")

# ---------------------------------------------------------------- 3.2 cyclists
Q("cy1", "cyclists", "Cyclists have priority over vehicles when riding on…", "Los ciclistas tienen prioridad sobre los vehículos cuando circulan por…",
  [("a signed cycle lane, cycle crossing or hard shoulder", "un carril bici, paso para ciclistas o arcén señalizados"), ("any lane of a motorway", "cualquier carril de una autopista"),
   ("any pavement", "cualquier acera")],
  "Properly signed.", "Debidamente señalizados.")
Q("cy2", "cyclists", "You turn left into a side road and a cyclist close by is going straight on. Who goes first?", "Giras a la izquierda para entrar en una vía lateral y un ciclista próximo sigue recto. ¿Quién pasa primero?",
  [("The cyclist", "El ciclista"), ("You", "Tú"), ("Whoever is on the right", "El que esté a la derecha")],
  "Turning right or left, the nearby cyclist goes first.", "Gires a la derecha o a la izquierda, pasa primero el ciclista próximo.")
Q("cy3", "cyclists", "The first rider of a group of cyclists has already entered a roundabout. You…", "El primero de un grupo de ciclistas ya ha entrado en una glorieta. Tú…",
  [("give way to the whole group", "cedes el paso a todo el grupo"), ("may cut in after the first rider", "puedes meterte después del primero"),
   ("have priority over the rest of the group", "tienes prioridad sobre el resto del grupo")],
  "The group counts as one moving unit.", "El grupo se considera una unidad móvil.")
Q("cy4", "cyclists", "Outside the listed cases, priority between cyclists and other vehicles follows…", "Fuera de los casos enumerados, la prioridad entre ciclistas y demás vehículos sigue…",
  [("the general priority rules between vehicles", "las normas generales de prioridad entre vehículos"), ("always the cyclist", "siempre al ciclista"), ("always the motor vehicle", "siempre al vehículo de motor")],
  "For example, give way to the right at unsigned junctions.", "Por ejemplo, ceder a la derecha en intersecciones sin señalizar.")
Q("cy5", "cyclists", "Who must give way to a nearby cyclist when turning into another road?", "¿Quién debe ceder el paso al ciclista próximo al girar para entrar en otra vía?",
  [("Motor vehicles and mopeds", "Los vehículos de motor y los ciclomotores"), ("Only lorries", "Solo los camiones"), ("Only cars turning right", "Solo los turismos que giran a la derecha")],
  "Whichever way they turn.", "Giren hacia donde giren.")
Q("cy6", "cyclists", "Unsigned junction on an ordinary road: a cyclist comes from your left, and you go straight on. Who goes first?",
  "Intersección sin señalizar en una vía normal: un ciclista viene por tu izquierda y tú sigues recto. ¿Quién pasa primero?",
  [("You, under the general rules", "Tú, por las normas generales"), ("The cyclist, always", "El ciclista, siempre"), ("Whoever is slower", "El más lento")],
  "No cycle lane, no turn, no group: general rules apply.", "Sin carril bici, sin giro y sin grupo: rigen las normas generales.")

# ---------------------------------------------------------------- 3.3 animals
Q("am1", "animals", "As a general rule, between vehicles and animals…", "Como norma general, entre vehículos y animales…",
  [("drivers have priority, with some exceptions", "los conductores tienen prioridad, con algunas excepciones"), ("animals always have priority", "los animales tienen siempre prioridad"),
   ("whoever arrives first goes first", "pasa el que llega primero")],
  "Three exceptions: signed cañadas, turning, crossing a shoulder.", "Tres excepciones: cañadas señalizadas, giros y cruce de arcén.")
Q("am2", "animals", "On a signed cañada, who goes first?", "En una cañada señalizada, ¿quién pasa primero?",
  [("The animals", "Los animales"), ("The vehicles", "Los vehículos"), ("The larger one", "El más grande")],
  "It is the animals’ route.", "Es el itinerario de los animales.")
Q("am3", "animals", "You turn into another road and a flock is crossing it where there is no cañada. You…", "Giras para entrar en otra vía y un rebaño la está cruzando donde no hay cañada. Tú…",
  [("give way to the animals", "cedes el paso a los animales"), ("have priority", "tienes prioridad"), ("sound the horn and go on", "tocas el claxon y sigues")],
  "Even though there is no crossing for them.", "Aunque no exista paso para ellos.")
Q("am4", "animals", "How is a cañada signed?", "¿Cómo se señaliza una cañada?",
  [("A «cañada» panel under the domestic animals warning sign, plus speed limits", "Un panel «cañada» bajo la señal de animales domésticos, más limitación de velocidad"),
   ("With a green information sign only", "Solo con una señal verde informativa"), ("With road markings only", "Solo con marcas viales")],
  "The speed-limit signs complement it.", "Las señales de limitación de velocidad la complementan.")
Q("am5", "animals", "You cross a hard shoulder along which animals are walking (no cañada). Who goes first?", "Cruzas un arcén por el que caminan animales (no hay cañada). ¿Quién pasa primero?",
  [("The animals", "Los animales"), ("You", "Tú"), ("Whoever is faster", "El más rápido")],
  "Same logic as pedestrians on a shoulder.", "La misma lógica que con los peatones en el arcén.")

# ---------------------------------------------------------------- 4.1 narrow stretches
Q("nr1", "narrow", "A narrow stretch (estrechamiento) is a part of the road where…", "Un estrechamiento es un tramo de la vía en el que…",
  [("two vehicles in opposite directions cannot pass, or only with great difficulty", "es imposible o muy difícil el paso simultáneo de dos vehículos en sentidos opuestos"),
   ("the road is under 6 m wide", "la calzada mide menos de 6 m"), ("there is only one lane per direction", "solo hay un carril por sentido")],
  "Because of its narrowness.", "Por su estrechez.")
Q("nr2", "narrow", "A blue square sign with a large white arrow up and a small red arrow down (R-6) means…", "Una señal cuadrada azul con flecha blanca grande hacia arriba y flecha roja pequeña hacia abajo (R-6) indica…",
  [("you have priority over oncoming vehicles", "prioridad respecto al sentido contrario: pasas tú"), ("give way to oncoming vehicles", "debes ceder el paso al sentido contrario"), ("a one-way road", "una calle de sentido único")],
  "The round red one (R-5) means the opposite.", "La redonda roja (R-5) indica lo contrario.")
Q("nr3", "narrow", "In a narrow stretch with no signs, who goes first?", "En un estrechamiento sin señalizar, ¿quién pasa primero?",
  [("The vehicle that entered first", "El vehículo que hubiera entrado primero"), ("The larger vehicle", "El vehículo más grande"), ("The one going uphill, always", "El que sube, siempre")],
  "The list of vehicles is only for doubtful cases.", "La lista de vehículos solo se usa en caso de duda.")
Q("nr4", "narrow", "Narrow stretch, no signs, unclear who entered first: a bus meets a lorry. Who goes first?", "Estrechamiento sin señales, sin saber quién entró primero: se encuentran un autobús y un camión. ¿Quién pasa?",
  [("The bus", "El autobús"), ("The lorry", "El camión"), ("The one with less distance to reverse", "El que tenga menos marcha atrás")],
  "Buses are 5th, lorries 6th.", "Autobuses 5.º, camiones 6.º.")
Q("nr5", "narrow", "In doubt: a car towing a 600 kg trailer meets a bus. Who goes first?", "En caso de duda: un turismo con remolque de 600 kg se encuentra con un autobús. ¿Quién pasa?",
  [("The car with the trailer", "El turismo con remolque"), ("The bus", "El autobús"), ("The one coming from the right", "El que viene por la derecha")],
  "Cars with a trailer up to 750 kg, and motorhomes, are 4th; buses 5th.", "Turismos con remolque de hasta 750 kg y autocaravanas, 4.º; autobuses, 5.º.")
Q("nr6", "narrow", "In doubt: a motorcycle without sidecar meets a car. Who goes first?", "En caso de duda: una motocicleta sin sidecar se encuentra con un turismo. ¿Quién pasa?",
  [("The car", "El turismo"), ("The motorcycle", "La motocicleta"), ("The one going downhill", "El que baja")],
  "Two-wheelers are last on the list.", "Las de dos ruedas son las últimas de la lista.")
Q("nr7", "narrow", "Two cars meet in a narrow stretch and it is unclear who entered first. Who goes first?", "Dos turismos se encuentran en un estrechamiento y no está claro quién entró primero. ¿Quién pasa?",
  [("The one that would have to reverse further", "El que tuviera que dar marcha atrás mayor distancia"), ("The faster one", "El más rápido"), ("The one on the right", "El de la derecha")],
  "If that is equal: the wider, longer or heavier.", "Si es igual: el de mayor anchura, longitud o MMA.")
Q("nr8", "narrow", "Narrow stretch on a gradient of 7 % or more, no signs. Who goes first?", "Estrechamiento en pendiente del 7 % o más, sin señales. ¿Quién pasa primero?",
  [("The vehicle going uphill, unless it could reach a lay-by first", "El que sube, salvo que pudiera llegar antes a un apartadero"), ("The vehicle going downhill", "El que baja"),
   ("The heavier vehicle", "El más pesado")],
  "In doubt about the gradient or the lay-by, the general rules apply.", "En caso de duda sobre la pendiente o el apartadero, rigen las normas generales.")
Q("nr9", "narrow", "In doubt: an oversize special vehicle meets a combination of vehicles. Who goes first?", "En caso de duda: un vehículo especial que excede de las dimensiones se encuentra con un conjunto de vehículos. ¿Quién pasa?",
  [("The oversize special vehicle", "El vehículo especial que excede"), ("The combination", "El conjunto de vehículos"), ("The one that entered last", "El que entró el último")],
  "It is first on the list.", "Es el primero de la lista.")
Q("nr10", "narrow", "In doubt: an animal-drawn cart meets a lorry. Who goes first?", "En caso de duda: un carro de tracción animal se encuentra con un camión. ¿Quién pasa?",
  [("The animal-drawn cart", "El vehículo de tracción animal"), ("The lorry", "El camión"), ("The one on the right", "El de la derecha")],
  "Animal-drawn vehicles are 3rd; lorries 6th.", "Tracción animal, 3.º; camiones, 6.º.")
Q("nr11", "narrow", "A round sign with a red rim, a black arrow down and a red arrow up (R-5) means…", "Una señal redonda con borde rojo, flecha negra hacia abajo y flecha roja hacia arriba (R-5) indica…",
  [("give way to oncoming vehicles", "prioridad en sentido contrario: cedes el paso"), ("you have priority over oncoming vehicles", "tienes prioridad sobre el sentido contrario"), ("no entry", "entrada prohibida")],
  "Red, round = you give way.", "Roja y redonda = cedes.")

# ---------------------------------------------------------------- 4.2 bridges
Q("br1", "bridges", "A narrow bridge has an R-5 sign at your end. You meet a car on the bridge. You…", "Un puente estrecho tiene una señal R-5 en tu extremo. Te encuentras con un turismo en el puente. Tú…",
  [("reverse to let it pass", "retrocedes para dejarle paso"), ("wait for it to reverse", "esperas a que retroceda él"), ("the smaller one reverses", "retrocede el más pequeño")],
  "Same with a give-way sign at your end.", "Igual con un ceda el paso en tu extremo.")
Q("br2", "bridges", "On a narrow bridge with no signs, who goes first?", "En un puente estrecho sin señalizar, ¿quién pasa primero?",
  [("As in narrow stretches: first in; in doubt, the vehicle list", "Como en los estrechamientos: el que entró primero; en duda, la lista"),
   ("Whoever comes from the right", "El que viene por la derecha"), ("Always the heavier vehicle", "Siempre el más pesado")],
  "Section 4.1 applies.", "Se aplica el apartado 4.1.")
Q("br3", "bridges", "Vehicles that need a special permit may not pass each other on bridges whose carriageway is narrower than…", "Los vehículos que necesitan autorización especial no pueden cruzarse en puentes cuya calzada mida menos de…",
  [("6 m", "6 m"), ("4 m", "4 m"), ("8 m", "8 m")],
  "If they meet, the narrow-stretch rules apply.", "Si se encuentran, rigen las normas de los estrechamientos.")
Q("br4", "bridges", "On a bridge too narrow to pass, the order of priority is set first by…", "En un puente que no permite el cruce, el orden de preferencia lo marca en primer lugar…",
  [("the signs that regulate it", "la señalización que lo regule"), ("the size of the vehicles", "el tamaño de los vehículos"), ("the time of day", "la hora del día")],
  "Without signs, the vehicle list.", "Sin señales, la lista de vehículos.")

# ---------------------------------------------------------------- 5.1 priority vehicles
Q("pr1", "priority", "Which vehicles are emergency-service priority vehicles?", "¿Qué vehículos son prioritarios de servicios de urgencia?",
  [("Police, fire brigade, civil protection and ambulances on urgent service", "Policía, bomberos, protección civil y asistencia sanitaria en servicio urgente"),
   ("All buses", "Todos los autobuses"), ("Taxis carrying passengers", "Los taxis con pasajeros")],
  "Public or private.", "Públicos o privados.")
Q("pr2", "priority", "To be a priority vehicle, an ambulance on urgent service normally uses…", "Para ser prioritaria, una ambulancia en servicio urgente utiliza normalmente…",
  [("the blue light and the siren at the same time", "la señal luminosa y la acústica a la vez"), ("only the siren", "solo la sirena"), ("the hazard lights", "la luz de emergencia")],
  "The light alone only when omitting the siren is no danger.", "Solo la luz cuando omitir la sirena no entrañe peligro.")
Q("pr3", "priority", "The V-1 light of a priority vehicle is…", "La señal luminosa V-1 de un vehículo prioritario es…",
  [("blue, visible from at least 50 m in all directions", "azul, visible a 50 m como mínimo en todas las direcciones"), ("amber, visible from 100 m", "ámbar, visible a 100 m"),
   ("red, visible from 150 m to the front", "roja, visible a 150 m por delante")],
  "One or more blue lights.", "Uno o varios destellos azules.")
Q("pr4", "priority", "When may a priority vehicle use only the light, without the siren?", "¿Cuándo puede un vehículo prioritario usar solo la señal luminosa, sin la acústica?",
  [("Exceptionally, when leaving out the siren is no danger", "Excepcionalmente, cuando omitir la acústica no entrañe peligro"), ("Never", "Nunca"), ("Always at night", "Siempre de noche")],
  "For example on an empty road at night, if that is safe.", "Por ejemplo en una vía vacía de noche, si es seguro.")
Q("pr5", "priority", "On urgent service and signalling correctly, a priority vehicle may…", "En servicio urgente y señalizándolo correctamente, un vehículo prioritario puede…",
  [("exceed the speed limits, on its own responsibility", "superar los límites de velocidad, bajo su exclusiva responsabilidad"),
   ("ignore agents’ instructions", "ignorar las órdenes de los agentes"), ("never cross a red light", "no cruzar nunca un semáforo en rojo")],
  "Agents’ instructions must always be obeyed.", "Las órdenes de los agentes son siempre de obligado cumplimiento.")
Q("pr6", "priority", "Before going through a red light, a priority vehicle must…", "Antes de pasar un semáforo en rojo, un vehículo prioritario debe…",
  [("make sure there is no risk of hitting pedestrians and that other drivers have stopped", "cerciorarse de que no hay riesgo de atropello y de que los demás han detenido su marcha"),
   ("just switch on the siren", "solo activar la sirena"), ("slow down to 20 km/h", "reducir a 20 km/h")],
  "Same at junctions where it would otherwise have to give way.", "Igual en las intersecciones donde tendría que ceder.")
Q("pr7", "priority", "On an autovía, exceptionally and without endangering anyone, a priority vehicle may…", "En una autovía, excepcionalmente y sin comprometer la seguridad, un vehículo prioritario puede…",
  [("drive against the traffic on the hard shoulder", "circular en sentido contrario por el arcén"), ("drive against the traffic in the left lane", "circular en sentido contrario por el carril izquierdo"),
   ("park in the right lane", "estacionar en el carril derecho")],
  "Also turn round, reverse, or enter the median and its crossing points.", "También dar media vuelta, marcha atrás o penetrar en la mediana y sus pasos transversales.")
Q("pr8", "priority", "Which instructions must a priority vehicle always obey?", "¿Qué indicaciones debe obedecer siempre un vehículo prioritario?",
  [("Those of traffic agents", "Las de los agentes"), ("Traffic lights", "Los semáforos"), ("All vertical signs", "Todas las señales verticales")],
  "It may skip other rules and signs on its own responsibility.", "Puede no cumplir otras normas y señales bajo su responsabilidad.")
Q("pr9", "priority", "Besides emergency services, who else has priority under the law?", "Además de los servicios de urgencia, ¿quién más tiene prioridad según la ley?",
  [("Road maintenance crews and vehicles going to provide roadside assistance", "Los equipos de mantenimiento de la vía y los vehículos que acuden a un auxilio en carretera"),
   ("Driving school cars", "Los vehículos de autoescuela"), ("Taxis", "Los taxis")],
  "Your course includes them with the priority vehicles.", "Tu curso los incluye con los prioritarios.")

# ---------------------------------------------------------------- 5.2 non-priority vehicles
Q("np1", "nonprio", "With no other option, you drive a seriously injured person to hospital in your own car. How do you make others notice?",
  "Sin otra opción, llevas a un herido grave al hospital en tu turismo. ¿Cómo te haces notar?",
  [("Horn on and off and hazard lights, or waving a handkerchief", "Claxon intermitente y luz de emergencia, o agitando un pañuelo"), ("With blue lights", "Con luces azules"),
   ("With the horn held down continuously", "Con el claxon de forma continua")],
  "Hazard lights if the vehicle has them.", "La luz de emergencia, si se dispone de ella.")
Q("np2", "nonprio", "Does a non-priority vehicle on emergency service have priority?", "¿Tiene prioridad un vehículo no prioritario en servicio de urgencia?",
  [("No: it must obey every traffic rule", "No: debe respetar todas las normas de circulación"), ("Yes, like an ambulance", "Sí, como una ambulancia"), ("Only at junctions", "Solo en las intersecciones")],
  "Especially at junctions.", "Especialmente en las intersecciones.")
Q("np3", "nonprio", "May an ordinary car on an emergency trip exceed the speed limit?", "¿Puede un turismo en un servicio de urgencia superar el límite de velocidad?",
  [("No", "No"), ("Yes, by up to 20 km/h", "Sí, hasta 20 km/h"), ("Yes, with the hazard lights on", "Sí, con la luz de emergencia encendida")],
  "It must respect every rule.", "Debe respetar todas las normas.")
Q("np4", "nonprio", "Agents may ask the driver of a non-priority vehicle on emergency service to…", "Los agentes pueden exigir al conductor de un vehículo no prioritario en servicio de urgencia…",
  [("justify the emergency, at any time", "la justificación de la urgencia, en cualquier momento"), ("pay an escort fee", "el pago de una escolta"), ("follow them to the hospital", "que les siga hasta el hospital")],
  "The emergency must be real and especially serious.", "La urgencia debe ser real y especialmente grave.")

# ---------------------------------------------------------------- 5.3 everyone else
Q("yd1", "yield", "When you notice a vehicle on emergency service, you normally…", "Cuando percibes un vehículo en servicio de urgencia, normalmente…",
  [("move to your right, and stop if necessary", "te apartas a la derecha y te detienes si es preciso"), ("speed up to clear the way", "aceleras para dejar libre el camino"),
   ("stop in the middle of your lane", "te detienes en mitad de tu carril")],
  "Whatever the circumstances allow.", "Según las circunstancias del momento y lugar.")
Q("yd2", "yield", "Must you also make way for a non-priority vehicle on emergency service?", "¿Hay que facilitar el paso también a un vehículo no prioritario en servicio de urgencia?",
  [("Yes", "Sí"), ("No, only for priority vehicles", "No, solo a los prioritarios"), ("Only on motorways", "Solo en autopistas")],
  "The duty covers both, priority or not.", "La obligación incluye a ambos, prioritarios o no.")
Q("yd3", "yield", "On a motorway with two lanes in your direction, the emergency corridor opens…", "En una autopista con dos carriles en tu sentido, el carril de emergencia se forma…",
  [("in the centre, between the two lanes", "en el centro, entre ambos carriles"), ("on the right shoulder", "en el arcén derecho"), ("on the left shoulder", "en el arcén izquierdo")],
  "Left lane moves left, right lane moves right.", "El carril izquierdo se orilla a la izquierda y el derecho a la derecha.")
Q("yd4", "yield", "With three or more lanes in your direction, the emergency corridor opens…", "Con tres o más carriles en tu sentido, el carril de emergencia se forma…",
  [("between the leftmost lane and the next one", "entre el carril de más a la izquierda y su contiguo"), ("between the right lane and the next one", "entre el carril derecho y su contiguo"),
   ("in the centre lane", "en el carril central")],
  "Left lane as far left as possible; the rest as far right as possible.", "El izquierdo, lo más a la izquierda posible; el resto, lo más a la derecha posible.")
Q("yd5", "yield", "When must you open the emergency corridor?", "¿Cuándo hay que formar el carril de emergencia?",
  [("When the queue moves at walking pace or stops", "Cuando la retención avanza a paso de peatón o se detiene"), ("Only when you hear a siren", "Solo cuando oyes una sirena"),
   ("Only inside tunnels", "Solo en los túneles")],
  "Before the emergency vehicle arrives.", "Antes de que llegue el vehículo de urgencia.")
Q("yd6", "yield", "A police car behind you, with blue light and siren, switches on a red light flashing forward. You must…", "Un coche de policía detrás de ti, con luz azul y sirena, activa una luz roja intermitente hacia delante. Debes…",
  [("stop on the right, in front of the police vehicle, and stay inside", "detenerte a la derecha, delante del vehículo policial, y permanecer en el interior"), ("move aside and let it pass", "apartarte y dejarle pasar"),
   ("get out and walk to the police car", "bajarte e ir andando al coche policial")],
  "It is an order to stop, in force since July 2025.", "Es una orden de detención, en vigor desde julio de 2025.")
