# -*- coding: utf-8 -*-
"""Question bank for the interactive Category A1/A2, Topic 8 page (signs and signals). In every question the FIRST
option is the correct one (the page shuffles options when it shows them). Ids must be unique and must not start with
"ai". The questions are written from the rider's seat; the facts are those of the shared sign catalogue."""

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
    "order": dict(sec=1, en="Order of priority", es="Orden de prioridad",
        recap=[("Agents → temporary signs and beaconing → traffic lights → vertical signs → road markings.", "Agentes → señalización circunstancial y balizamiento → semáforos → señales verticales → marcas viales."),
               ("Different groups: the one higher in that order. Same group: the most restrictive.", "Grupos distintos: la prioritaria según ese orden. Mismo grupo: la más restrictiva."),
               ("A sign against a traffic rule: obey the sign, unless special circumstances justify otherwise.", "Señal contra norma de circulación: la señal, salvo circunstancias especiales."),
               ("Everyone must obey signs; nobody may install, move, hide or alter them without permission.", "Todos deben obedecer las señales; nadie puede instalarlas, trasladarlas, ocultarlas o modificarlas sin permiso.")],
        trap=("Thinking a road marking beats a vertical sign.", "Pensar que una marca vial prevalece sobre una señal vertical.")),
    "place": dict(sec=1, en="Where signs apply", es="Colocación y aplicación",
        recap=[("Right-hand sign: everyone. Left-hand sign: straight on or turning left.", "Derecha: todos. Izquierda: los que siguen de frente o giran a la izquierda."),
               ("Different signs each side: left one for straight on or left, right one for right turns.", "Distintas a cada lado: la izquierda para de frente o izquierda; la derecha para el giro a la derecha."),
               ("Above the carriageway: all of it. Above or inside one lane: that lane only.", "Encima de la calzada: toda. Encima o dentro de un carril: solo ese carril."),
               ("Roadworks: yellow markings and yellow-background signs with the same meaning; signed day and night.", "Obras: marcas amarillas y señales de fondo amarillo con el mismo significado; señalizadas de día y de noche.")],
        trap=("Thinking a sign on the left also binds those turning right.", "Pensar que la señal de la izquierda obliga también a quien gira a la derecha.")),
    "arms": dict(sec=2, en="Agents’ arms and whistle", es="Brazos y silbato de los agentes",
        recap=[("Arm raised: everyone approaching stops; those already inside the junction go on.", "Brazo levantado: se detienen todos los que se acercan; los que ya están dentro de la intersección siguen."),
               ("Arm(s) held out: stop if your direction crosses the line of the arm.", "Brazo(s) extendido(s): se detiene quien venga de direcciones que corten la del brazo."),
               ("Arm up and down: slow down. Swinging red or amber light: stop.", "Brazo arriba y abajo: reducir. Balanceo de luz roja o amarilla: detenerse."),
               ("Whistle: short frequent blasts stop; one long blast, move off.", "Silbato: toques cortos y frecuentes, detención; un toque largo, reanudar.")],
        trap=("Stopping inside the junction when the agent raises an arm.", "Detenerse dentro de la intersección cuando el agente levanta el brazo.")),
    "agveh": dict(sec=2, en="Agents’ vehicles and helpers", es="Vehículos de los agentes y auxiliares",
        recap=[("Red flag: road closed. Green flag: open again. Yellow flag: extreme care or danger near.", "Bandera roja: calzada cerrada. Verde: de nuevo abierta. Amarilla: extremar la atención o peligro próximo."),
               ("Arm out, slanted down and still: stop on the right.", "Brazo extendido hacia abajo, inclinado y fijo: detenerse en el lado derecho."),
               ("Flashing red light facing forwards: stop on the right, ahead of the police vehicle, and obey the loudspeaker.", "Luz roja intermitente hacia delante: detenerse a la derecha, delante del vehículo policial, y obedecer la megafonía."),
               ("Works staff and escorts regulate with a paddle; school patrols invite you to stop; all visible from 150 m.", "Personal de obras y de acompañamiento regulan con paleta; las patrullas escolares invitan a detenerse; visibles a 150 m.")],
        trap=("Taking the yellow flag for a closed road.", "Confundir la bandera amarilla con el cierre de la calzada.")),
    "beacon": dict(sec=3, en="Variable signs, beaconing and barriers", es="Paneles, balizamiento y contención",
        recap=[("Variable message signs: never more than two alternating messages.", "Paneles de mensaje variable: nunca más de dos mensajes alternados."),
               ("Cones, edge beacons, yellow lights and bollards: do not cross the line that joins them.", "Conos, balizas de borde, luces amarillas y balizas cilíndricas: no se cruza la línea que los une."),
               ("Edge posts and reflectors: white on the left; white or yellow on the right.", "Hitos de arista y captafaros: blancos a la izquierda; blancos o amarillos a la derecha."),
               ("Direction panels: single moderate, double medium, triple high danger.", "Paneles direccionales: sencillo moderada, doble media, triple elevada.")],
        trap=("Slipping between two cones because a motorcycle fits.", "Colarse entre dos conos porque la moto cabe.")),
    "lights": dict(sec=4, en="Round traffic lights", es="Semáforos circulares",
        recap=[("Green: go with priority, unless you would be left blocking the junction or a crossing.", "Verde: paso con prioridad, salvo que vayas a quedar detenido obstruyendo la intersección o un paso."),
               ("Amber: stop as for red, unless you cannot stop safely before the light.", "Amarillo: detenerse como en rojo, salvo que no puedas hacerlo con seguridad antes del semáforo."),
               ("Flashing amber: extreme care and give way if needed; it does not cancel a STOP.", "Ámbar intermitente: extremar la precaución y ceder si procede; no anula un STOP."),
               ("Green arrow: go with care, giving way; black arrow on red or amber: only that movement.", "Flecha verde: pasar con precaución y cediendo; flecha negra sobre rojo o amarillo: solo ese movimiento.")],
        trap=("Thinking the green arrow gives you priority.", "Pensar que la flecha verde da prioridad.")),
    "lanelights": dict(sec=4, en="Lane lights and special lights", es="Semáforos de carril y reservados",
        recap=[("Red cross: leave the lane as soon as possible. Green down arrow: lane open.", "Aspa roja: abandonar el carril cuanto antes. Flecha verde hacia abajo: carril permitido."),
               ("Slanted white or yellow arrow: move into the lane it points to.", "Flecha oblicua blanca o amarilla: incorporarse al carril al que apunta."),
               ("White bars: trams and regular buses (or everyone in the reserved lane); flashing bar = steady amber.", "Franjas blancas: tranvías y autobuses regulares (o todos los del carril reservado); intermitente = amarillo fijo."),
               ("Bicycle silhouette: cycles only.", "Silueta de ciclo: solo ciclos.")],
        trap=("Riding a moped through on a green bicycle light.", "Pasar en ciclomotor con el semáforo verde de bicicletas.")),
    "warn": dict(sec=5, en="Warning signs", es="Señales de advertencia de peligro",
        recap=[("They announce a danger that is hard to see in time; a panel may give the distance and the length.", "Avisan de un peligro difícil de percibir a tiempo; un panel puede dar la distancia y la longitud."),
               ("P-1 family: the others give way. P-2: the general rule (priority to the right).", "Familia P-1: ceden los otros. P-2: rige la regla general (prioridad a la derecha)."),
               ("Approach posts: 3 stripes 200 m, 2 stripes 150 m, 1 stripe 100 m.", "Balizas de aproximación: 3 franjas 200 m, 2 franjas 150 m, 1 franja 100 m."),
               ("P-19 slippery for any reason; P-29 never shows the side of the wind.", "P-19: deslizante por cualquier motivo; P-29: nunca indica el lado del viento.")],
        trap=("Reading P-2 as ‘you have priority’.", "Leer la P-2 como «tienes prioridad».")),
    "prio": dict(sec=6, en="Priority signs and how R signs apply", es="Señales de prioridad y aplicación",
        recap=[("Regulatory signs apply from where they stand, unless a panel gives a distance.", "Las de reglamentación rigen desde donde están, salvo que un panel indique la distancia."),
               ("Beside or above the town-name sign: the whole town.", "Al lado o en la vertical de la señal de poblado: todo el poblado."),
               ("STOP: at the stop line or just before the junction; stop again if you cannot see.", "STOP: ante la línea de detención o justo antes de la intersección; nueva detención si no hay visibilidad."),
               ("R-5 red ring: wait at the narrow passage. R-6 blue square: you go first.", "R-5, borde rojo: esperar en el paso estrecho. R-6, cuadrado azul: pasas primero.")],
        trap=("Rolling through a STOP because nobody is coming.", "Pasar un STOP sin detenerse porque no viene nadie.")),
    "noentry": dict(sec=6, en="No-entry and restriction signs", es="Prohibición de entrada y restricción de paso",
        recap=[("R-100: no vehicles, both directions. R-101: no entry for any vehicle.", "R-100: ningún vehículo, ambos sentidos. R-101: entrada prohibida a todo vehículo."),
               ("R-102 stops motorcycles but not mopeds: a moped is not a motor vehicle.", "La R-102 detiene a las motocicletas pero no a los ciclomotores: el ciclomotor no es vehículo de motor."),
               ("R-103 lets two-wheeled motorcycles through; R-104 stops motorcycles; R-105 stops mopeds.", "La R-103 deja pasar a las motocicletas de dos ruedas; la R-104 detiene a las motocicletas; la R-105, a los ciclomotores."),
               ("Length, width and height limits count the load.", "Los límites de longitud, anchura y altura incluyen la carga.")],
        trap=("Thinking R-102 also stops a moped.", "Pensar que la R-102 detiene también a un ciclomotor.")),
    "other": dict(sec=6, en="Other prohibitions", es="Otras prohibiciones",
        recap=[("R-303 (no left turn) also bans U-turns; R-304 (no U-turn) still lets you turn left.", "R-303 (giro a la izquierda) prohíbe también el cambio de sentido; R-304 (media vuelta) sí permite girar."),
               ("R-305: no overtaking motor vehicles by using the oncoming side, also on a motorcycle.", "R-305: no adelantar a vehículos de motor invadiendo el sentido contrario, también en moto."),
               ("R-307: no stopping or parking. R-308: no parking, stopping allowed.", "R-307: ni parar ni estacionar. R-308: no estacionar; la parada sí."),
               ("R-301 on a warning sign’s post ends with the danger.", "La R-301 en el poste de una señal de peligro termina con el peligro.")],
        trap=("Thinking motorcycles are exempt from R-305.", "Pensar que las motos están exentas de la R-305.")),
    "oblig": dict(sec=6, en="Obligation and end signs", es="Obligación y fin de prohibición",
        recap=[("R-404 obliges automobiles except two-wheeled motorcycles; R-405 obliges motorcycles.", "La R-404 obliga a los automóviles excepto motocicletas de dos ruedas; la R-405 obliga a las motocicletas."),
               ("R-407b: compulsory for mopeds, closed to everyone else.", "R-407b: obligatoria para ciclomotores, cerrada a los demás."),
               ("R-403: only those directions; U-turns are not allowed.", "R-403: solo esas direcciones; no permite el cambio de sentido."),
               ("R-500 ends all specific prohibitions for moving vehicles.", "La R-500 pone fin a todas las prohibiciones específicas para vehículos en movimiento.")],
        trap=("Thinking the white car on blue obliges a motorcycle.", "Pensar que el turismo blanco sobre azul obliga a una motocicleta.")),
    "info": dict(sec=7, en="Indication signs", es="Señales de indicación",
        recap=[("S-7 advises a speed; R-301 limits it.", "La S-7 aconseja una velocidad; la R-301 la limita."),
               ("S-28: 10 km/h, games allowed. S-47: 20 km/h, games not allowed.", "S-28: 10 km/h, juegos permitidos. S-47: 20 km/h, juegos no."),
               ("Reserved lane with a broken line: enter only for a manoeuvre that is not stopping, parking, turning round or overtaking.", "Carril reservado con línea discontinua: solo para maniobras que no sean parar, estacionar, cambiar de sentido o adelantar."),
               ("Motorway pre-signposting to a lower-category road stays blue; the exit sign itself changes colour.", "La preseñalización en autopista hacia una vía inferior sigue azul; el cartel de salida inmediata sí cambia.")],
        trap=("Taking the blue square with a figure for a speed limit.", "Tomar el cuadrado azul con una cifra por un límite de velocidad.")),
    "mklines": dict(sec=8, en="Lines along and across the road", es="Marcas longitudinales y transversales",
        recap=[("Continuous line: do not cross it or ride on it, nor ride to its left when it divides the two directions.", "Continua: no se atraviesa ni se circula sobre ella, ni por su izquierda si separa sentidos."),
               ("Continuous beside broken: only the one on your side counts.", "Continua adosada a discontinua: solo cuenta la de tu lado."),
               ("Stop line: stop, and stop again where you can see. Give-way line: you may move forward to see.", "Línea de detención: parar y volver a parar donde haya visibilidad. Línea de ceda: se puede avanzar hasta ver."),
               ("Shorter gaps: a continuous line or special risk is near. Much wider line: a special lane.", "Trazos más juntos: se acerca una continua o un riesgo. Línea mucho más ancha: carril especial.")],
        trap=("Riding along the line itself to filter past traffic.", "Circular sobre la línea para avanzar entre el tráfico.")),
    "mkother": dict(sec=8, en="Painted signs and other markings", es="Señales horizontales y otras marcas",
        recap=[("Hatched area: only those obliged to use the shoulder may enter.", "Cebreado: solo entran los obligados a circular por el arcén."),
               ("Chevrons: keep at least two between you and the vehicle ahead.", "Galones: al menos dos entre tú y el vehículo de delante."),
               ("Yellow continuous kerb line: no stopping or parking. Yellow broken: no parking. Blue: limited time.", "Amarilla continua: ni parar ni estacionar. Amarilla discontinua: no estacionar. Azul: tiempo limitado."),
               ("Yellow box: do not enter if you would be left stopped inside.", "Cuadrícula amarilla: no entrar si vas a quedar detenido dentro.")],
        trap=("Parking the motorcycle on a yellow zig-zag ‘because it is small’.", "Estacionar la moto sobre el zigzag amarillo «porque ocupa poco».")),
    "twowheels": dict(sec=9, en="On two wheels", es="Sobre dos ruedas",
        recap=[("Advanced stop box: two lines 4 m apart; on red, only the vehicles painted in it.", "Avanza-motos: dos líneas separadas 4 m; en rojo, solo los vehículos pintados."),
               ("S-49’s motorcycle pictogram covers motorcycles, three-wheelers treated as them and mopeds.", "El pictograma de moto de la S-49 incluye motocicletas, tres ruedas asimilados y ciclomotores."),
               ("Reserved lane: only if the motorcycle is drawn on the sign.", "Carril reservado: solo si la motocicleta figura en la señal."),
               ("Guidance marks: a bend of special risk and the strip better not to ride on.", "Marcas de guiado: curva de especial riesgo y franja que se recomienda no pisar.")],
        trap=("Rolling into a box painted only with a bicycle.", "Adelantarse a una zona pintada solo con una bicicleta.")),
}

# ---------------------------------------------------------------- 1 order of priority
Q("or1", "order", "At a junction an agent waves you on while the traffic light in front of you is red. What do you do?",
  "En una intersección un agente te indica que pases mientras tu semáforo está en rojo. ¿Qué haces?",
  [("Go on: the agent’s order comes first", "Paso: la orden del agente prevalece"), ("Wait for the green light", "Espero a la luz verde"), ("Stop and ask the agent to repeat the signal", "Me detengo y pido al agente que repita la señal")],
  "Agents’ signals and orders rank first and prevail over every other sign and rule.", "Las señales y órdenes de los agentes ocupan el primer lugar y prevalecen sobre las demás señales y normas.")
Q("or2", "order", "Which is the correct order of priority among signals?",
  "¿Cuál es el orden de prioridad correcto entre las señales?",
  [("Agents, temporary signs and beaconing, traffic lights, vertical signs, road markings", "Agentes, señalización circunstancial y balizamiento, semáforos, señales verticales, marcas viales"),
   ("Agents, traffic lights, temporary signs and beaconing, vertical signs, road markings", "Agentes, semáforos, señalización circunstancial y balizamiento, señales verticales, marcas viales"),
   ("Traffic lights, agents, vertical signs, temporary signs and beaconing, road markings", "Semáforos, agentes, señales verticales, señalización circunstancial y balizamiento, marcas viales")],
  "First agents, then temporary signs with beaconing, then traffic lights, vertical signs and, last, road markings.", "Primero los agentes, después la señalización circunstancial y el balizamiento, los semáforos, las señales verticales y, por último, las marcas viales.")
Q("or3", "order", "A vertical STOP sign stands at a junction where the line painted across the road is a give-way line. Which do you obey?",
  "En una intersección hay una señal vertical de STOP y en el suelo una línea de ceda el paso. ¿Cuál obedeces?",
  [("The STOP sign: vertical signs rank above road markings", "El STOP: las señales verticales prevalecen sobre las marcas viales"), ("The marking, because it is the nearest to you", "La marca, porque es la más próxima"), ("Whichever is less restrictive", "La menos restrictiva")],
  "Signs of different groups: the one higher in the order prevails. Vertical signs are fourth, markings fifth.", "Entre grupos distintos prevalece la prioritaria: las verticales son las cuartas y las marcas, las quintas.")
Q("or4", "order", "Two vertical signs of the same kind contradict each other. Which one do you obey?",
  "Dos señales verticales del mismo tipo se contradicen. ¿Cuál obedeces?",
  [("The most restrictive one", "La más restrictiva"), ("The one placed higher", "La colocada más arriba"), ("The one on the right", "La de la derecha")],
  "Within the same group, the most restrictive sign prevails.", "Dentro del mismo grupo prevalece la señal más restrictiva.")
Q("or5", "order", "A sign orders something different from the general traffic rules. As a rule, what do you follow?",
  "Una señal ordena algo distinto de las normas generales de circulación. Por norma, ¿qué sigues?",
  [("The sign, unless special circumstances justify otherwise", "La señal, salvo circunstancias especiales que lo justifiquen"), ("The general rule, always", "La norma general, siempre"), ("Whichever suits a motorcycle better", "Lo que más convenga a una motocicleta")],
  "When a sign contradicts the traffic rules, the sign is obeyed unless special circumstances justify otherwise.", "Si una señal contradice las normas de circulación, se obedece la señal, salvo circunstancias especiales.")
Q("or6", "order", "Roadworks have set up temporary signs and beacons that change the normal use of the road, and the traffic light there shows green. Which prevails?",
  "Unas obras han colocado señalización circunstancial y balizas que modifican el uso normal de la vía, y el semáforo del tramo está en verde. ¿Qué prevalece?",
  [("The temporary signs and the beaconing", "La señalización circunstancial y el balizamiento"), ("The traffic light", "El semáforo"), ("Neither: they rank the same", "Ninguno: tienen el mismo rango")],
  "Temporary signs and beaconing rank second, above traffic lights (third).", "La señalización circunstancial y el balizamiento ocupan el segundo lugar, por encima de los semáforos (tercero).")
Q("or7", "order", "Who may put up, remove, move, hide or alter the signs of a road?",
  "¿Quién puede instalar, retirar, trasladar, ocultar o modificar la señalización de una vía?",
  [("Nobody without permission from the road’s owner or the competent authority, unless there is a justified reason", "Nadie sin permiso del titular de la vía o de la autoridad competente, salvo causa justificada"),
   ("Any neighbour, if the sign is in front of their property", "Cualquier vecino, si la señal está delante de su propiedad"), ("Any driver who finds it confusing", "Cualquier conductor al que le resulte confusa")],
  "Without a justified reason nobody may tamper with signs without permission, nor put objects on or near them that confuse, dazzle or distract.", "Salvo causa justificada, nadie puede manipular la señalización sin permiso ni colocar objetos que confundan, deslumbren o distraigan.")

# ---------------------------------------------------------------- 1 placement
Q("pl1", "place", "A give-way sign stands only on the left of your carriageway. Who must obey it?",
  "Hay una señal de ceda el paso solo a la izquierda de tu calzada. ¿A quién obliga?",
  [("Those going straight on or turning left", "A los que siguen de frente o giran a la izquierda"), ("Everyone, whichever way they go", "A todos, vayan hacia donde vayan"), ("Only those turning right", "Solo a los que giran a la derecha")],
  "A sign on the left binds those going straight on or turning left.", "La señal de la izquierda obliga a los que siguen de frente o giran a la izquierda.")
Q("pl2", "place", "A sign stands on the right-hand side of the carriageway. Who must obey it?",
  "Una señal está colocada a la derecha de la calzada. ¿A quién obliga?",
  [("Everyone, whether they go straight on or turn", "A todos, sigan de frente o giren"), ("Only those turning right", "Solo a los que giran a la derecha"), ("Only those going straight on", "Solo a los que siguen de frente")],
  "Signs on the right bind everyone.", "Las señales de la derecha deben obedecerlas todos.")
Q("pl3", "place", "At a junction there is a STOP on the left and a give-way sign on the right. You are going to turn right. Which applies to you?",
  "En una intersección hay un STOP a la izquierda y un ceda el paso a la derecha. Vas a girar a la derecha. ¿Cuál te afecta?",
  [("The give-way sign on the right", "El ceda el paso de la derecha"), ("The STOP on the left", "El STOP de la izquierda"), ("Both: you obey the stricter one", "Las dos: se obedece la más restrictiva")],
  "With different signs on each side, the right-hand one is for those turning right; the left-hand one for straight on or left.", "Con señales distintas a cada lado, la de la derecha es para quien gira a la derecha y la de la izquierda para quien sigue de frente o gira a la izquierda.")
Q("pl4", "place", "A sign hangs above a single lane. Which part of the road does it apply to?",
  "Una señal está situada encima de un solo carril. ¿A qué parte de la vía se aplica?",
  [("Only to that lane", "Solo a ese carril"), ("To the whole carriageway", "A toda la calzada"), ("To that lane and those to its right", "A ese carril y a los de su derecha")],
  "Signs above the carriageway apply to all of it; signs above one lane apply to that lane only.", "Las señales encima de la calzada afectan a toda ella; las situadas encima de un carril, solo a ese carril.")
Q("pl5", "place", "A “30” is painted inside one lane of a carriageway with three lanes. Whom does it bind?",
  "Hay un «30» pintado dentro de un carril de una calzada de tres carriles. ¿A quién obliga?",
  [("Only vehicles using that lane", "Solo a los vehículos que circulan por ese carril"), ("The whole carriageway", "A toda la calzada"), ("Only cars; motorcycles are exempt", "Solo a los turismos; las motos están exentas")],
  "A sign applies to the whole usable width unless it is inside a lane or a panel limits its message.", "Las señales se aplican a toda la anchura de la calzada salvo que estén dentro de un carril o un panel limite su mensaje.")
Q("pl6", "place", "On a stretch with roadworks, what colour are the road markings?",
  "En un tramo de obras, ¿de qué color son las marcas viales?",
  [("Yellow", "Amarillo"), ("Orange", "Naranja"), ("White with a yellow edge", "Blanco con borde amarillo")],
  "In roadworks the road markings are yellow.", "En las obras las marcas viales son de color amarillo.")
Q("pl7", "place", "A warning sign in roadworks has a yellow background. What does that change in its meaning?",
  "Una señal de peligro en obras tiene el fondo amarillo. ¿Qué cambia en su significado?",
  [("Nothing: it means the same as without works", "Nada: significa lo mismo que sin obras"), ("It becomes only advisory", "Pasa a ser solo una recomendación"), ("It applies only to lorries", "Se aplica solo a los camiones")],
  "Yellow-background signs keep the meaning they have when there are no works.", "Las señales con fondo amarillo tienen el mismo significado que las que se usan cuando no hay obras.")

# ---------------------------------------------------------------- 2 arms and whistle
Q("ag1", "arms", "An agent raises one arm vertically. Who must stop?",
  "Un agente levanta un brazo verticalmente. ¿Quién debe detenerse?",
  [("Every road user approaching the agent, except those who cannot stop safely", "Todos los usuarios que se acerquen al agente, salvo los que no puedan hacerlo con seguridad"),
   ("Only those facing the agent", "Solo los que están de frente al agente"), ("Only those behind the agent", "Solo los que están a su espalda")],
  "The raised arm stops everyone approaching the agent, from every direction.", "El brazo levantado obliga a detenerse a todos los que se acerquen al agente, desde cualquier dirección.")
Q("ag2", "arms", "You are already inside the junction when the agent raises an arm vertically. What do you do?",
  "Ya estás dentro de la intersección cuando el agente levanta el brazo verticalmente. ¿Qué haces?",
  [("Carry on: those already inside need not stop", "Continúo: los que ya están dentro no están obligados a detenerse"), ("Stop at once where I am", "Me detengo de inmediato donde estoy"), ("Stop and push the motorcycle back", "Me detengo y retrocedo con la moto")],
  "At a junction you stop before entering it; drivers already inside are not obliged to stop.", "En una intersección la detención se hace antes de entrar; los que ya están dentro no están obligados a detenerse.")
Q("ag3", "arms", "An agent holds one arm out horizontally. Who must stop?",
  "Un agente extiende un brazo horizontalmente. ¿Quién debe detenerse?",
  [("Those approaching from directions that cross the line of the arm", "Los que se acerquen desde direcciones que corten la indicada por el brazo"), ("Everyone, from every direction", "Todos, desde cualquier dirección"), ("Those moving parallel to the arm", "Los que circulan en paralelo al brazo")],
  "Arm or arms held out stop the users whose direction crosses the one shown by the arm, whichever way they travel.", "El brazo o brazos extendidos detienen a quienes vengan de direcciones que corten la indicada, cualquiera que sea su sentido.")
Q("ag4", "arms", "The agent who stopped you lowers the arms but does not change position. Is the stop order still in force?",
  "El agente que te ha detenido baja los brazos, pero no cambia de posición. ¿Sigue en vigor la orden?",
  [("Yes, until the agent changes position or makes another signal", "Sí, hasta que cambie de posición o haga otra señal"), ("No, lowering the arms ends it", "No, al bajar los brazos termina"), ("Only for the next ten seconds", "Solo durante los diez segundos siguientes")],
  "Agents’ signals stay in force although they lower their arms, as long as they keep the same position and make no other signal.", "Las señales permanecen en vigor aunque el agente baje los brazos, siempre que no cambie de posición ni realice otra señal.")
Q("ag5", "arms", "An agent moves an outstretched arm up and down. You are approaching at right angles to that arm. What must you do?",
  "Un agente mueve un brazo extendido alternativamente arriba y abajo. Te acercas perpendicularmente a ese brazo. ¿Qué debes hacer?",
  [("Slow down", "Disminuir la velocidad"), ("Stop", "Detenerme"), ("Speed up to clear the area", "Acelerar para despejar la zona")],
  "The arm moving up and down orders drivers approaching at right angles to it to slow down.", "El brazo moviéndose arriba y abajo obliga a disminuir la velocidad a quienes se acerquen perpendicularmente.")
Q("ag6", "arms", "At night an agent swings a red light in your direction. What does it order?",
  "De noche un agente balancea una luz roja hacia ti. ¿Qué ordena?",
  [("Stop", "Detenerme"), ("Slow down and continue", "Reducir y continuar"), ("Change lane", "Cambiar de carril")],
  "Swinging a red or amber light stops the users towards whom the agent aims it.", "El balanceo de una luz roja o amarilla obliga a detenerse a los usuarios hacia los que se dirige.")
Q("ag7", "arms", "Stopped by an agent, you hear one long blast of the whistle. What does it mean?",
  "Detenido por un agente, oyes un toque largo de silbato. ¿Qué significa?",
  [("Move off again", "Reanudar la marcha"), ("Stop the engine", "Parar el motor"), ("Danger: stay where you are", "Peligro: permanece donde estás")],
  "Short, frequent blasts order vehicles to stop; one long blast orders them to move off.", "Los toques cortos y frecuentes ordenan la detención; un toque largo, reanudar la marcha.")

# ---------------------------------------------------------------- 2 vehicles and helpers
Q("av1", "agveh", "A police vehicle carrying a red flag passes. What does that mean from that moment?",
  "Pasa un vehículo policial con una bandera roja. ¿Qué significa a partir de ese momento?",
  [("The carriageway is temporarily closed to everyone except those accompanied or escorted by agents", "La calzada queda temporalmente cerrada a todos, excepto a los acompañados o escoltados por los agentes"),
   ("The road is closed only to heavy vehicles", "La vía queda cerrada solo a los vehículos pesados"), ("You must take extreme care but may continue", "Hay que extremar la atención, pero se puede continuar")],
  "Red flag: the carriageway is temporarily closed to all users, except those escorted by the agents.", "Bandera roja: la calzada queda temporalmente cerrada a todos los usuarios, salvo los escoltados por los agentes.")
Q("av2", "agveh", "And a green flag on the agents’ vehicle?",
  "¿Y una bandera verde en el vehículo de los agentes?",
  [("The carriageway is open to traffic again", "La calzada queda de nuevo abierta al tráfico"), ("You have priority at the next junction", "Tienes prioridad en la próxima intersección"), ("You may exceed the speed limit to keep up", "Puedes superar el límite para seguir al vehículo")],
  "Green flag: from the moment the vehicle carrying it passes, the road is open again.", "Bandera verde: a partir del paso del vehículo que la lleva, la calzada queda de nuevo abierta.")
Q("av3", "agveh", "What does a yellow flag shown from a vehicle or by staff at a cycling event tell you?",
  "¿Qué te indica una bandera amarilla mostrada desde un vehículo o por el personal de una marcha ciclista?",
  [("Take extreme care, or a danger is near", "Necesidad de extremar la atención o proximidad de un peligro"), ("The road is closed", "La calzada está cerrada"), ("The road is open again", "La calzada vuelve a estar abierta")],
  "Yellow flag: extreme care or a danger nearby. Staff controlling cycle marches and similar events may use it too.", "Bandera amarilla: extremar la atención o peligro próximo. También puede usarla el personal de marchas ciclistas y otras actividades.")
Q("av4", "agveh", "From a police motorcycle an agent holds an arm out towards you, slanted downwards and still. What must you do?",
  "Desde una moto policial un agente extiende hacia ti el brazo, inclinado hacia abajo y fijo. ¿Qué debes hacer?",
  [("Stop on the right-hand side", "Detenerme en el lado derecho"), ("Slow down and keep behind", "Reducir y mantenerme detrás"), ("Overtake the police vehicle", "Adelantar al vehículo policial")],
  "Arm held out, slanted down and still: the users it is aimed at must stop on the right.", "Brazo extendido hacia abajo, inclinado y fijo: obligación de detenerse en el lado derecho.")
Q("av5", "agveh", "A police car behind you switches on a flashing red light facing forwards. What must you do?",
  "Un coche policial detrás de ti enciende una luz roja intermitente hacia delante. ¿Qué debes hacer?",
  [("Stop on the right, ahead of the police vehicle, where it causes no risk, and obey the loudspeaker", "Detenerme en el lado derecho, delante del vehículo policial, donde no genere riesgo, y obedecer la megafonía"),
   ("Stop at once in my lane", "Detenerme de inmediato en mi carril"), ("Let it overtake and follow it", "Dejar que me adelante y seguirlo")],
  "The vehicle in front must stop on the right ahead of the police vehicle, in a place without greater risk, and obey the instructions given over the loudspeaker.", "El vehículo que circula delante debe detenerse a la derecha, delante del vehículo policial, en un lugar sin mayores riesgos, y obedecer las instrucciones de megafonía.")
Q("av6", "agveh", "Roadworks staff regulate the traffic with a sign on a paddle. Must you obey them?",
  "El personal de unas obras regula el paso con una señal en una paleta. ¿Debes obedecer?",
  [("Yes", "Sí"), ("Only when an agent is present", "Solo si hay un agente presente"), ("No: the paddle only informs", "No: la paleta solo informa")],
  "Where there are no agents, or to help them, works staff and special-transport escorts may regulate traffic with a paddle, and drivers must obey.", "A falta de agentes o para ayudarles, el personal de obras y de acompañamiento puede regular el paso con una paleta y los conductores deben obedecer.")
Q("av7", "agveh", "From what distance must the people who help the agents be distinguishable thanks to their clothing and reflective elements?",
  "¿A qué distancia mínima deben poder distinguirse los auxiliares de los agentes gracias a sus prendas y elementos retrorreflectantes?",
  [("150 metres", "150 metros"), ("50 metres", "50 metros"), ("100 metres", "100 metros")],
  "They must wear bright clothing and retroreflective elements that let others distinguish them from at least 150 m.", "Deben llevar prendas llamativas y elementos retrorreflectantes que permitan distinguirlos a 150 m como mínimo.")

# ---------------------------------------------------------------- 3 beaconing
Q("be1", "beacon", "How many alternating messages may a variable message sign show at most?",
  "¿Cuántos mensajes alternados puede mostrar como máximo un panel de mensaje variable?",
  [("Two", "Dos"), ("Three", "Tres"), ("There is no limit", "No hay límite")],
  "Variable message signs never use more than two alternating messages.", "En los paneles de mensaje variable nunca se usan más de dos mensajes alternados.")
Q("be2", "beacon", "A row of cones closes off part of the road. Your motorcycle would fit between two of them. May you ride through?",
  "Una fila de conos cierra parte de la vía. Tu moto cabría entre dos de ellos. ¿Puedes pasar?",
  [("No: the real or imaginary line joining them may not be crossed", "No: está prohibido atravesar la línea real o imaginaria que los une"), ("Yes, at walking pace", "Sí, a paso de persona"), ("Yes, if nobody is working there", "Sí, si no hay nadie trabajando")],
  "Cones and temporary edge beacons forbid passing through the real or imaginary line that joins them.", "Los conos y balizas de borde provisionales prohíben el paso a través de la línea real o imaginaria que los une.")
Q("be3", "beacon", "What does a steady red light on a barrier mean?",
  "¿Qué indica una luz roja fija en una barrera?",
  [("The carriageway is completely closed", "Que la calzada está totalmente cerrada al tránsito"), ("You must take care but may pass", "Que hay que tener precaución, pero se puede pasar"), ("It is closed to heavy vehicles only", "Que está cerrada solo a los vehículos pesados")],
  "A steady red light shows that the carriageway is completely closed.", "La luz roja fija indica que la calzada está totalmente cerrada al tránsito.")
Q("be4", "beacon", "The barrier of a level crossing is coming down and cars are already waiting. Where do you wait on your motorcycle?",
  "La barrera de un paso a nivel está bajando y ya hay turismos esperando. ¿Dónde esperas con tu moto?",
  [("Behind the last vehicle, in your lane", "Detrás del último vehículo, en mi carril"), ("At the front, between the cars", "Delante, entre los turismos"), ("In the oncoming lane, to be first", "En el carril contrario, para salir el primero")],
  "At a level crossing or movable bridge that is closed or closing, users stop one behind the other in their lane until the way is clear.", "En un paso a nivel o puente móvil cerrado o con la barrera en movimiento, hay que detenerse uno detrás de otro en el carril correspondiente.")
Q("be5", "beacon", "At night, what colour are the edge posts and reflectors on your left?",
  "De noche, ¿de qué color son los hitos de arista y captafaros situados a tu izquierda?",
  [("White", "Blanco"), ("Yellow", "Amarillo"), ("Red", "Rojo")],
  "On the left they are white; on the right, white or yellow.", "A la izquierda son blancos; a la derecha, blancos o amarillos.")
Q("be6", "beacon", "A bend is marked with a triple permanent direction panel. What does it tell you?",
  "Una curva está señalizada con un panel direccional permanente triple. ¿Qué te indica?",
  [("A high level of danger", "Un nivel de peligrosidad elevado"), ("A moderate level of danger", "Un nivel de peligrosidad moderado"), ("That three bends follow", "Que siguen tres curvas")],
  "Single panel: moderate danger; double: medium; triple: high.", "Panel sencillo: peligrosidad moderada; doble: media; triple: elevada.")
Q("be7", "beacon", "Luminous studs set in the carriageway mark off a lane. When may you cross them?",
  "Unas balizas luminosas colocadas en la calzada delimitan un carril. ¿Cuándo puedes franquearlas?",
  [("Only when they are green", "Solo cuando están en verde"), ("Also when orange, with care", "También en naranja, con precaución"), ("In any colour, on a motorcycle", "Con cualquier color, en moto")],
  "Their light can be green, orange or red, and they may only be crossed when green.", "Su luz puede ser verde, naranja o roja, y solo se pueden franquear cuando es verde.")
Q("be8", "beacon", "A windsock stands beside the road. What does it tell you?",
  "Hay una manga de viento junto a la vía. ¿De qué te informa?",
  [("That there is wind, and its direction and strength", "De la existencia, el sentido y la intensidad del viento"), ("Only that an airfield is near", "Solo de que hay un aeródromo cerca"), ("The speed you must keep", "De la velocidad que debes mantener")],
  "It complements the crosswind sign, showing that a steady or gusty wind exists, its direction and its strength.", "Complementa la señal de viento transversal informando de la existencia, sentido e intensidad de un viento continuo o racheado.")

# ---------------------------------------------------------------- 4 round lights
Q("li1", "lights", "Your light is green, but traffic ahead is so slow that you would be left stopped on the pedestrian crossing. What do you do?",
  "Tu semáforo está en verde, pero el tráfico va tan lento que quedarías detenido sobre el paso de peatones. ¿Qué haces?",
  [("Wait: do not go on if you would foreseeably block the crossing", "Espero: no debo pasar si previsiblemente voy a obstruir el paso"), ("Go on: green always lets me pass", "Paso: el verde siempre permite pasar"), ("Go on and stop astride the crossing", "Paso y me detengo sobre el paso")],
  "Green allows you to go with priority, unless you would foreseeably be left stopped in a junction or on a crossing, obstructing cross traffic.", "El verde permite el paso con prioridad, salvo que previsiblemente vayas a quedar detenido en una intersección o paso, obstruyendo la circulación transversal.")
Q("li2", "lights", "The light turns to steady amber as you approach. What must you do?",
  "El semáforo cambia a amarillo fijo cuando te acercas. ¿Qué debes hacer?",
  [("Stop as for a red light, unless you are so close that you cannot stop safely before it", "Detenerme como ante el rojo, salvo que esté tan cerca que no pueda hacerlo con seguridad antes del semáforo"),
   ("Accelerate to clear the junction", "Acelerar para despejar la intersección"), ("Always continue with care", "Continuar siempre con precaución")],
  "Steady amber means stop in the same conditions as a red light, with that single exception.", "El amarillo fijo obliga a detenerse en las mismas condiciones que el rojo, con esa única excepción.")
Q("li3", "lights", "The red light is on the far side of the junction. Where do you stop?",
  "El semáforo en rojo está al otro lado de la intersección. ¿Dónde te detienes?",
  [("Before entering the junction, at the stop line before it if there is one", "Antes de entrar en la intersección, ante la línea de detención anterior si existe"), ("Under the light itself", "Bajo el propio semáforo"), ("In the middle of the junction", "En el centro de la intersección")],
  "If the light is inside or on the far side of a junction, vehicles must not enter it nor pass the stop line before it.", "Si el semáforo está dentro o al lado opuesto de la intersección, no se debe entrar en ella ni rebasar la línea de detención anterior.")
Q("li4", "lights", "A junction has a flashing amber light and a STOP sign. What do you do?",
  "En una intersección hay un semáforo en ámbar intermitente y una señal de STOP. ¿Qué haces?",
  [("Stop: flashing amber does not exempt you from signs that make you stop", "Me detengo: el ámbar intermitente no exime de las señales que obligan a detenerse"), ("Go through with care: the light outranks the sign", "Paso con precaución: el semáforo prevalece sobre la señal"), ("Give way without stopping", "Cedo el paso sin detenerme")],
  "Flashing amber orders extreme care and giving way where appropriate, and does not exempt you from other signs that make you stop.", "El ámbar intermitente obliga a extremar la precaución y, en su caso, ceder el paso, y no exime de otras señales que obliguen a detenerse.")
Q("li5", "lights", "Where do you find a red light flashing, or two red lights flashing alternately?",
  "¿Dónde se encuentra una luz roja intermitente o dos luces rojas alternativamente intermitentes?",
  [("Before level crossings, movable bridges, ferry landings or fire-engine exits", "Antes de pasos a nivel, puentes móviles, pontones transbordadores o salidas de vehículos de bomberos"),
   ("At every junction at night", "En todas las intersecciones por la noche"), ("At the entrance to motorways", "A la entrada de las autopistas")],
  "They temporarily forbid passing, at those places or when an aircraft is approaching at low height.", "Prohíben temporalmente el paso en esos lugares o por la aproximación de una aeronave a escasa altura.")
Q("li6", "lights", "A green arrow lights up next to a red light. How may you go?",
  "Se enciende una flecha verde junto a una luz roja. ¿Cómo puedes pasar?",
  [("In the arrow’s direction, with care, giving way to vehicles in the lane you join and to pedestrians crossing", "En el sentido de la flecha, con precaución, cediendo a los vehículos del carril al que me incorporo y a los peatones que crucen"),
   ("In the arrow’s direction, with priority over everyone", "En el sentido de la flecha, con prioridad sobre todos"), ("I may not: red comes first", "No puedo: manda la luz roja")],
  "The green arrow lets you take that direction whatever other light is on, but with care and giving way.", "La flecha verde permite tomar esa dirección cualquiera que sea la otra luz encendida, pero con precaución y cediendo el paso.")
Q("li7", "lights", "You wait in the lane others need for the turn when the green arrow lights up, but you wanted to go straight on. What must you do?",
  "Esperas en el carril que otros necesitan para girar cuando se enciende la flecha verde, pero tú querías seguir de frente. ¿Qué debes hacer?",
  [("Move off in the arrow’s direction", "Avanzar en el sentido de la flecha"), ("Stay until my own light is green", "Esperar a que mi semáforo esté en verde"), ("Push the motorcycle back to free the lane", "Retroceder con la moto para liberar el carril")],
  "A vehicle in the lane others must use for that movement has to move off in that direction, even if it was not the one it wanted.", "El vehículo que esté en el carril que otros deben utilizar para ese movimiento debe avanzar en ese sentido, aunque no fuera el que deseaba.")
Q("li8", "lights", "A red light carries a black arrow. What does the arrow change?",
  "Una luz roja lleva una flecha negra. ¿Qué cambia la flecha?",
  [("Nothing in its meaning: the red applies only to the movement shown by the arrow", "Nada en su significado: la roja se limita al movimiento indicado por la flecha"), ("It allows that movement", "Permite ese movimiento"), ("It turns the red into a give-way", "Convierte la roja en un ceda el paso")],
  "A black arrow on a red or amber light does not change its meaning, but limits it to the movement shown.", "La flecha negra sobre una luz roja o amarilla no cambia su significado, pero lo limita al movimiento indicado.")

# ---------------------------------------------------------------- 4 lane lights and special lights
Q("ll1", "lanelights", "A red cross lights up above the lane you are riding in. What must you do?",
  "Se enciende un aspa roja sobre el carril por el que circulas. ¿Qué debes hacer?",
  [("Leave that lane as soon as possible", "Abandonarlo en el tiempo más breve posible"), ("Stop under the cross", "Detenerme bajo el aspa"), ("Continue more slowly", "Continuar más despacio")],
  "The red cross forbids using the lane; those in it must leave it as soon as possible.", "El aspa roja prohíbe ocupar el carril; quien circule por él debe abandonarlo cuanto antes.")
Q("ll2", "lanelights", "A green arrow pointing down is lit above your lane, and further on there is a round red light. What do you do at the red light?",
  "Sobre tu carril hay una flecha verde hacia abajo y, más adelante, una luz roja circular. ¿Qué haces ante la luz roja?",
  [("Stop: the green arrow does not exempt you from it", "Me detengo: la flecha verde no exime de ella"), ("Continue: the lane light prevails", "Continúo: prevalece el semáforo de carril"), ("Continue if no one is crossing", "Continúo si no cruza nadie")],
  "The green lane arrow allows the use of the lane, but you must still stop at a round red light and obey signs and markings that make you stop or give way.", "La flecha verde de carril permite circular por él, pero no exime de detenerse ante una luz roja circular ni de obedecer señales y marcas de detención o ceda.")
Q("ll3", "lanelights", "A white or yellow arrow pointing down at an angle is lit above your lane. What does it mean?",
  "Sobre tu carril hay una flecha blanca o amarilla que apunta hacia abajo y en oblicuo. ¿Qué significa?",
  [("Move safely into the lane it points to: yours is about to close", "Debo ir incorporándome con seguridad al carril al que apunta: el mío va a quedar cerrado"), ("The lane it points to is closed", "El carril al que apunta está cerrado"), ("Take the next exit", "Debo tomar la próxima salida")],
  "It shows the need to move over, in safe conditions, to the lane it points to, because yours will be closed shortly.", "Indica la necesidad de irse incorporando con seguridad al carril hacia el que apunta, porque el propio va a quedar cerrado en corto espacio.")
Q("ll4", "lanelights", "Whom do the traffic lights with an illuminated white bar on a black lens apply to?",
  "¿A quién afectan los semáforos con una franja blanca iluminada sobre fondo negro?",
  [("Trams and regular-line buses or, if there is a reserved lane, everyone using that lane", "A tranvías y autobuses de líneas regulares o, si hay carril reservado, a todos los que circulen por él"),
   ("All two-wheeled vehicles", "A todos los vehículos de dos ruedas"), ("Taxis only", "Solo a los taxis")],
  "They apply only to trams and regular buses, unless a reserved lane exists: then they apply to everyone in it.", "Afectan solo a tranvías y autobuses regulares, salvo que exista un carril reservado: entonces afectan a todos los que circulen por él.")
Q("ll5", "lanelights", "You ride in a reserved lane you are allowed to use and its white-bar light is flashing. What do you do?",
  "Circulas por un carril reservado que puedes usar y su semáforo de franja blanca está intermitente. ¿Qué haces?",
  [("Stop as for a steady amber light", "Me detengo como ante una luz amarilla fija"), ("Continue with priority", "Continúo con prioridad"), ("Continue: it only concerns buses", "Continúo: solo afecta a los autobuses")],
  "A flashing white bar means stopping in the same conditions as for a steady amber light.", "Si la franja blanca es intermitente, hay que detenerse en las mismas condiciones que ante una luz amarilla fija.")
Q("ll6", "lanelights", "You ride a moped and a light with the silhouette of a bicycle turns green while the round light stays red. May you go?",
  "Vas en ciclomotor y un semáforo con la silueta de una bicicleta se pone en verde mientras el circular sigue en rojo. ¿Puedes pasar?",
  [("No: those lights apply only to cycles", "No: esos semáforos afectan exclusivamente a los ciclos"), ("Yes: it is for all two-wheelers", "Sí: es para todos los vehículos de dos ruedas"), ("Yes, but only mopeds, not motorcycles", "Sí, pero solo los ciclomotores, no las motos")],
  "Lights showing the silhouette of a cycle apply only to cycles.", "Los semáforos con la silueta de un ciclo afectan exclusivamente a los ciclos.")

# ---------------------------------------------------------------- 5 warning signs
Q("wn1", "warn", "A warning triangle shows a thick vertical arrow crossed by a thin line (P-1). What does it announce?",
  "Un triángulo de peligro muestra una flecha vertical gruesa cruzada por un trazo fino (P-1). ¿Qué anuncia?",
  [("A junction with a road whose users must give way to you", "Una intersección con una vía cuyos usuarios deben cederte el paso"), ("A junction where you must give way", "Una intersección en la que debes ceder el paso"), ("A junction where the general rule applies", "Una intersección en la que rige la regla general")],
  "P-1 announces a junction with priority: those on the other road must give way.", "La P-1 anuncia una intersección con prioridad: deben ceder los usuarios de la otra vía.")
Q("wn2", "warn", "And the triangle with an X-shaped cross (P-2)?",
  "¿Y el triángulo con un aspa (P-2)?",
  [("A junction where the general priority rule applies", "Una intersección en la que rige la regla general de prioridad"), ("A junction where you have priority", "Una intersección en la que tienes prioridad"), ("A level crossing without barriers", "Un paso a nivel sin barreras")],
  "P-2: junction with priority to the right, that is, the general rule.", "P-2: intersección con prioridad de la derecha, es decir, la regla general.")
Q("wn3", "warn", "Sign P-1c tells you that traffic merging from the right must give way to you. What else are you expected to do?",
  "La señal P-1c te indica que quienes se incorporan por la derecha deben cederte el paso. ¿Qué más se espera de ti?",
  [("Make the merge easier as far as possible", "Facilitar la incorporación en la medida de lo posible"), ("Stop to let them in", "Detenerte para dejarles entrar"), ("Sound the horn to warn them", "Tocar el claxon para avisarles")],
  "Those who meet P-1c or P-1d keep their priority but must make the merge easier as far as possible.", "Quienes encuentran la P-1c o la P-1d mantienen la prioridad, pero deben facilitar la incorporación en lo posible.")
Q("wn4", "warn", "The crosswind sign (P-29) shows a windsock. Does it tell you from which side the wind blows?",
  "La señal de viento transversal (P-29) muestra una manga de viento. ¿Indica de qué lado sopla?",
  [("No", "No"), ("Yes: the side the sock points to", "Sí: el lado hacia el que apunta la manga"), ("Yes, always from the right", "Sí, siempre de la derecha")],
  "P-29 warns of frequent strong crosswind but does not show the side it comes from.", "La P-29 avisa de viento fuerte transversal frecuente, pero no indica el lado de donde sopla.")
Q("wn5", "warn", "Sign P-19 warns of a slippery road surface. For what reason may it be slippery?",
  "La señal P-19 avisa de pavimento deslizante. ¿Por qué motivo puede serlo?",
  [("For any reason", "Por cualquier motivo"), ("Only because of rain", "Solo por la lluvia"), ("Only because of ice or snow", "Solo por hielo o nieve")],
  "P-19: the surface may be very slippery for any reason. Ice or snow has its own sign, P-34.", "P-19: el pavimento puede resultar muy deslizante por cualquier motivo. El hielo o la nieve tienen su propia señal, la P-34.")
Q("wn6", "warn", "Beside the road stands a post with three red diagonal stripes. How far away is the level crossing?",
  "Junto a la vía hay una baliza con tres franjas rojas oblicuas. ¿A qué distancia está el paso a nivel?",
  [("200 m", "200 m"), ("150 m", "150 m"), ("100 m", "100 m")],
  "Three stripes 200 m, two stripes 150 m, one stripe 100 m.", "Tres franjas, 200 m; dos franjas, 150 m; una franja, 100 m.")
Q("wn7", "warn", "What does the sign showing a car throwing up stones (P-28) warn of?",
  "¿De qué avisa la señal que muestra un vehículo proyectando piedras (P-28)?",
  [("A stretch where passing vehicles may throw up loose chippings", "De un tramo donde puede proyectarse gravilla al pasar los vehículos"), ("Falling rocks from a slope", "De desprendimientos de una ladera"), ("An unpaved road", "De una vía sin asfaltar")],
  "P-28: risk of gravel being thrown up. Falling rocks are P-26.", "P-28: riesgo de proyección de gravilla. Los desprendimientos son la P-26.")
Q("wn8", "warn", "Which of these warning signs is also a priority sign?",
  "¿Cuál de estas señales de peligro es también una señal de prioridad?",
  [("P-6, tram crossing", "P-6, cruce de tranvía"), ("P-13a, dangerous bend", "P-13a, curva peligrosa"), ("P-19, slippery road", "P-19, pavimento deslizante")],
  "The P-1 family, P-2, P-6, P-7 and P-8 are also priority signs. At P-6 the tram has priority.", "La familia P-1, la P-2, la P-6, la P-7 y la P-8 son también señales de prioridad. En la P-6 el tranvía tiene prioridad.")

# ---------------------------------------------------------------- 6 priority signs and application
Q("pr1", "prio", "From where must you obey a regulatory sign, as a rule?",
  "Por norma, ¿desde dónde debes cumplir una señal de reglamentación?",
  [("From the point where it stands, unless a panel below it gives a distance", "Desde el lugar donde está colocada, salvo que un panel debajo indique la distancia"), ("From 150 m before the sign", "Desde 150 m antes de la señal"), ("From the next junction", "Desde la próxima intersección")],
  "Regulatory signs apply from the cross-section where they stand, unless a complementary panel gives the distance.", "Las señales de reglamentación se cumplen desde la sección donde están colocadas, salvo que un panel complementario indique la distancia.")
Q("pr2", "prio", "A regulatory sign stands beside the sign with the name of the town. Where does it apply?",
  "Una señal de reglamentación está al lado de la señal con el nombre del poblado. ¿Dónde se aplica?",
  [("In the whole town, unless other signs say otherwise on certain stretches", "En todo el poblado, salvo que otras señales indiquen otra cosa en ciertos tramos"), ("Only in the first street", "Solo en la primera calle"), ("Only up to the first junction", "Solo hasta la primera intersección")],
  "Beside or above the town-name sign, a regulatory sign applies to the whole town.", "Colocada al lado o en la vertical de la señal de poblado, la señal de reglamentación se aplica a todo el poblado.")
Q("pr3", "prio", "Where must you stop at a STOP sign (R-2)?",
  "¿Dónde debes detenerte ante una señal de STOP (R-2)?",
  [("At the next stop line or, if there is none, immediately before the junction", "Ante la próxima línea de detención o, si no existe, inmediatamente antes de la intersección"), ("Level with the sign itself", "A la altura de la propia señal"), ("Anywhere, provided I give way", "Donde sea, siempre que ceda el paso")],
  "R-2 obliges you to stop at the next stop line or, failing that, just before the junction, and give way.", "La R-2 obliga a detenerse ante la próxima línea de detención o, si no existe, inmediatamente antes de la intersección, y ceder el paso.")
Q("pr4", "prio", "You have stopped at the STOP line but cannot see the road you are joining. What do you do?",
  "Te has detenido en la línea del STOP, pero no ves la vía a la que te incorporas. ¿Qué haces?",
  [("Move forward and stop again where I can see", "Avanzo y me detengo de nuevo donde tenga visibilidad"), ("Go on slowly without stopping again", "Sigo despacio sin volver a detenerme"), ("Sound the horn and go", "Toco el claxon y paso")],
  "If there is not enough visibility from the place where you stopped, you must stop again where you can see, without endangering anyone.", "Si desde el lugar de la detención no hay visibilidad suficiente, hay que detenerse de nuevo donde la haya, sin poner en peligro a nadie.")
Q("pr5", "prio", "A round sign with a red ring shows a black arrow pointing down and a red arrow pointing up (R-5). What does it order?",
  "Una señal circular con borde rojo muestra una flecha negra hacia abajo y una roja hacia arriba (R-5). ¿Qué ordena?",
  [("Not to enter the narrow passage if that would make oncoming vehicles stop", "No entrar en el paso estrecho si eso obliga a detenerse a los que vienen de frente"), ("That you have priority in the narrow passage", "Que tienes prioridad en el paso estrecho"), ("That the road is two-way", "Que la vía es de doble sentido")],
  "R-5: priority for oncoming traffic. The blue square R-6 gives the priority to you.", "R-5: prioridad en sentido contrario. El cuadrado azul R-6 te da la prioridad a ti.")
Q("pr6", "prio", "What does the yellow diamond with a white border (R-3) tell you?",
  "¿Qué te indica el rombo amarillo con borde blanco (R-3)?",
  [("Your carriageway has priority at junctions", "Que tu calzada tiene prioridad en las intersecciones"), ("You must give way at the next junction", "Que debes ceder el paso en la próxima intersección"), ("Priority to the right applies", "Que rige la prioridad de la derecha")],
  "R-3: carriageway with priority. R-4, the same diamond crossed out, announces that it is about to lose it.", "R-3: calzada con prioridad. La R-4, el mismo rombo tachado, anuncia que va a perderla.")

# ---------------------------------------------------------------- 6 no entry and restriction
Q("ne1", "noentry", "On your motorcycle you meet a red-ringed sign showing a car above a motorcycle (R-102). May you enter?",
  "En tu motocicleta encuentras una señal de borde rojo con un turismo sobre una motocicleta (R-102). ¿Puedes entrar?",
  [("No: it bans motor vehicles", "No: prohíbe la entrada a los vehículos de motor"), ("Yes: it only bans cars", "Sí: solo prohíbe los turismos"), ("Yes, if I ride alone", "Sí, si voy sin pasajero")],
  "R-102 forbids entry to motor vehicles, and a motorcycle is one.", "La R-102 prohíbe el acceso a los vehículos de motor, y la motocicleta lo es.")
Q("ne2", "noentry", "And if you meet that same sign (R-102) riding a moped?",
  "¿Y si encuentras esa misma señal (R-102) conduciendo un ciclomotor?",
  [("You may enter: in the Traffic Law a moped is not a motor vehicle", "Puedes entrar: en la Ley de Tráfico el ciclomotor no es vehículo de motor"), ("You may not enter", "No puedes entrar"), ("You may enter only pushing it", "Solo puedes entrar empujándolo")],
  "The legal definition of motor vehicle leaves out mopeds, so R-102 does not stop them. The sign that stops a moped is R-105.", "La definición legal de vehículo de motor excluye a los ciclomotores, así que la R-102 no los detiene. La señal que los detiene es la R-105.")
Q("ne3", "noentry", "A red-ringed sign shows only a car seen from the front (R-103). You ride a two-wheeled motorcycle. May you enter?",
  "Una señal de borde rojo muestra solo un turismo visto de frente (R-103). Conduces una motocicleta de dos ruedas. ¿Puedes entrar?",
  [("Yes: two-wheeled motorcycles are the exception", "Sí: las motocicletas de dos ruedas son la excepción"), ("No: it bans all motor vehicles", "No: prohíbe todos los vehículos de motor"), ("Only residents may", "Solo pueden los residentes")],
  "R-103 bans motor vehicles but not two-wheeled motorcycles nor three-wheelers treated as motorcycles.", "La R-103 prohíbe los vehículos de motor, pero no las motocicletas de dos ruedas ni los vehículos de tres ruedas asimilados.")
Q("ne4", "noentry", "Which vehicles does the red-ringed sign with a motorcycle (R-104) stop?",
  "¿A qué vehículos detiene la señal de borde rojo con una motocicleta (R-104)?",
  [("Motorcycles and three-wheelers treated as motorcycles", "A las motocicletas y a los vehículos de tres ruedas asimilados a motocicletas"), ("Motorcycles, mopeds and cycles", "A motocicletas, ciclomotores y ciclos"), ("Every two-wheeled vehicle", "A todos los vehículos de dos ruedas")],
  "R-104 forbids entry to motorcycles and to three-wheelers treated as motorcycles. Mopeds have their own sign.", "La R-104 prohíbe el acceso a motocicletas y a vehículos de tres ruedas asimilados. Los ciclomotores tienen su propia señal.")
Q("ne5", "noentry", "Besides mopeds, which vehicles does sign R-105 stop?",
  "Además de a los ciclomotores, ¿a qué vehículos detiene la señal R-105?",
  [("Vehicles for people with reduced mobility", "A los vehículos para personas de movilidad reducida"), ("Motorcycles", "A las motocicletas"), ("Cycles", "A los ciclos")],
  "R-105 forbids entry to mopeds and also to vehicles for people with reduced mobility.", "La R-105 prohíbe el acceso a los ciclomotores e igualmente a los vehículos para personas de movilidad reducida.")
Q("ne6", "noentry", "What is the difference between the empty red ring (R-100) and the red disc with a white bar (R-101)?",
  "¿En qué se diferencian el círculo blanco de borde rojo (R-100) y el disco rojo con franja blanca (R-101)?",
  [("R-100 bans all vehicles in both directions; R-101 bans entry to all vehicles", "La R-100 prohíbe la circulación de todo vehículo en ambos sentidos; la R-101, el acceso de todo vehículo"),
   ("R-100 bans only motor vehicles; R-101 everyone", "La R-100 prohíbe solo los vehículos de motor; la R-101, a todos"), ("They mean the same", "Significan lo mismo")],
  "R-100: no vehicles of any kind, in both directions. R-101: no entry for any vehicle.", "R-100: circulación prohibida a toda clase de vehículos en ambos sentidos. R-101: entrada prohibida a toda clase de vehículos.")
Q("ne7", "noentry", "A round sign with a red ring and a horizontal black bar (R-200) stands before a toll booth. What does it order?",
  "Antes de un peaje hay una señal circular de borde rojo con una barra negra horizontal (R-200). ¿Qué ordena?",
  [("To stop, and not to go on until you have done what the sign requires", "Detenerse y no reanudar la marcha hasta haber cumplido lo que la señal establece"), ("To slow down to walking pace", "Reducir a paso de persona"), ("No entry for motorcycles", "Entrada prohibida a las motocicletas")],
  "R-200, no passing without stopping: at a customs, police, toll or other post.", "R-200, prohibición de pasar sin detenerse: ante un puesto de aduana, de policía, de peaje u otro.")
Q("ne8", "noentry", "A width-limit sign (R-204) shows 2 m. Your motorcycle carries side cases. What counts?",
  "Una señal de limitación de anchura (R-204) indica 2 m. Tu moto lleva maletas laterales. ¿Qué anchura cuenta?",
  [("The vehicle’s width including its load", "La anchura del vehículo incluida la carga"), ("Only the width stated in the papers", "Solo la que figura en la documentación"), ("The handlebar width", "La del manillar")],
  "The length, width and height limits (R-203, R-204, R-205) refer to the vehicle including its load.", "Las limitaciones de longitud, anchura y altura (R-203, R-204, R-205) se refieren al vehículo incluida la carga.")

# ---------------------------------------------------------------- 6 other prohibitions
Q("ot1", "other", "Besides turning left, what does the “no left turn” sign (R-303) forbid?",
  "Además de girar a la izquierda, ¿qué prohíbe la señal de giro a la izquierda prohibido (R-303)?",
  [("Making a U-turn", "El cambio de sentido de la marcha"), ("Overtaking", "Adelantar"), ("Turning right", "Girar a la derecha")],
  "R-303 forbids turning left and includes the prohibition of the U-turn.", "La R-303 prohíbe girar a la izquierda e incluye la prohibición del cambio de sentido.")
Q("ot2", "other", "At a junction there is a “no U-turn” sign (R-304). May you turn left?",
  "En una intersección hay una señal de media vuelta prohibida (R-304). ¿Puedes girar a la izquierda?",
  [("Yes", "Sí"), ("No", "No"), ("Only on a motorcycle", "Solo en moto")],
  "R-304 forbids the U-turn but still allows a change of direction.", "La R-304 prohíbe el cambio de sentido, pero sí permite cambiar de dirección.")
Q("ot3", "other", "After a “no overtaking” sign (R-305), may you overtake a car on your motorcycle by using the oncoming side?",
  "Tras una señal de adelantamiento prohibido (R-305), ¿puedes adelantar en moto a un turismo invadiendo el sentido contrario?",
  [("No: the sign binds motorcycles too", "No: la señal obliga también a las motocicletas"), ("Yes: motorcycles need little room", "Sí: las motos necesitan poco espacio"), ("Yes, if the car is going slowly", "Sí, si el turismo va despacio")],
  "R-305 forbids every vehicle to overtake motor vehicles when that means using the side reserved for oncoming traffic.", "La R-305 prohíbe a todos los vehículos adelantar a vehículos de motor cuando la maniobra implique invadir la zona del sentido contrario.")
Q("ot4", "other", "A speed-limit sign (R-301) stands on the same post as a warning sign. Until where does the limit apply?",
  "Una señal de velocidad máxima (R-301) está en el mismo poste que una señal de peligro. ¿Hasta dónde rige el límite?",
  [("Until the danger that is signed ends", "Hasta que termine el peligro señalado"), ("Until the next junction", "Hasta la próxima intersección"), ("For one kilometre", "Durante un kilómetro")],
  "On the same post or panel as a warning sign, the limit ends when the signed danger ends.", "Colocada en el mismo poste o panel que una señal de peligro, la prohibición termina cuando termina el peligro señalado.")
Q("ot5", "other", "On which side of the carriageway does a “no stopping or parking” sign (R-307) apply, and how far?",
  "¿En qué lado de la calzada se aplica una señal de parada y estacionamiento prohibido (R-307) y hasta dónde?",
  [("On the side where it stands, from the sign to the nearest junction", "En el lado en que está situada, desde la señal hasta la intersección más próxima"), ("On both sides, for 100 m", "En ambos lados, durante 100 m"), ("On the side where it stands, for the whole street", "En el lado en que está, en toda la calle")],
  "Unless stated otherwise, it starts level with the sign and ends at the nearest junction in the direction of travel, on that side.", "Salvo indicación en contrario, comienza en la vertical de la señal y termina en la intersección más próxima en el sentido de la marcha, en ese lado.")
Q("ot6", "other", "You want to drop your passenger off where a “no parking” sign (R-308) stands. May you stop?",
  "Quieres dejar a tu pasajero donde hay una señal de estacionamiento prohibido (R-308). ¿Puedes parar?",
  [("Yes: it does not forbid stopping", "Sí: no prohíbe la parada"), ("No: it forbids stopping and parking", "No: prohíbe parar y estacionar"), ("Only at night", "Solo de noche")],
  "R-308 forbids parking on that side but does not forbid stopping.", "La R-308 prohíbe el estacionamiento en ese lado, pero no la parada.")
Q("ot7", "other", "A “no parking” sign shows “1-15” (R-308c). When may you not park there?",
  "Una señal de estacionamiento prohibido lleva «1-15» (R-308c). ¿Cuándo no puedes estacionar ahí?",
  [("From 9:00 on day 1 to 9:00 on day 16", "Desde las 9 h del día 1 hasta las 9 h del día 16"), ("From midnight on day 1 to midnight on day 15", "Desde las 0 h del día 1 hasta las 24 h del día 15"), ("On odd days of the month", "Los días impares del mes")],
  "First fortnight: from 9:00 on the 1st to 9:00 on the 16th. The second (R-308d) runs from 9:00 on the 16th to 9:00 on the 1st.", "Primera quincena: desde las 9 h del día 1 hasta las 9 h del día 16. La segunda (R-308d), desde las 9 h del día 16 hasta las 9 h del día 1.")
Q("ot8", "other", "The “minimum distance” sign (R-300) shows 70 m. In which case may you get closer to the vehicle ahead?",
  "La señal de separación mínima (R-300) indica 70 m. ¿En qué caso puedes acercarte más al vehículo que te precede?",
  [("To overtake it", "Para adelantarlo"), ("When riding a motorcycle", "Cuando conduces una moto"), ("In no case", "En ningún caso")],
  "R-300 forbids driving without keeping at least that gap, except to overtake. Without a figure it is a general reminder of the safety distance.", "La R-300 prohíbe circular sin mantener al menos esa separación, excepto para adelantar. Sin cifra, recuerda de forma genérica la distancia de seguridad.")

# ---------------------------------------------------------------- 6 obligation and end signs
Q("ob1", "oblig", "A blue round sign shows a white car (R-404). You ride a two-wheeled motorcycle. Are you obliged to use that carriageway?",
  "Una señal circular azul muestra un turismo blanco (R-404). Conduces una motocicleta de dos ruedas. ¿Estás obligado a circular por esa calzada?",
  [("No: two-wheeled motorcycles are the exception", "No: las motocicletas de dos ruedas son la excepción"), ("Yes, like every automobile", "Sí, como todo automóvil"), ("Yes, but only out of town", "Sí, pero solo fuera de poblado")],
  "R-404: compulsory carriageway for automobiles, except two-wheeled motorcycles and three-wheelers treated as motorcycles.", "R-404: calzada obligatoria para automóviles, excepto motocicletas de dos ruedas y vehículos de tres ruedas asimilados.")
Q("ob2", "oblig", "Whom does the blue round sign with a white motorcycle (R-405) oblige to use that carriageway?",
  "¿A quién obliga a circular por esa calzada la señal circular azul con una motocicleta blanca (R-405)?",
  [("Two-wheeled motorcycles and three-wheelers treated as motorcycles", "A las motocicletas de dos ruedas y a los vehículos de tres ruedas asimilados"), ("Motorcycles, mopeds and cycles", "A motocicletas, ciclomotores y ciclos"), ("Nobody: it only recommends", "A nadie: es una recomendación")],
  "R-405: compulsory carriageway for two-wheeled motorcycles and three-wheelers treated as them.", "R-405: calzada obligatoria para motocicletas de dos ruedas y vehículos de tres ruedas asimilados.")
Q("ob3", "oblig", "A blue round sign with a white moped (R-407b) stands at the entrance to a track. May you use it on your motorcycle?",
  "A la entrada de una vía hay una señal circular azul con un ciclomotor blanco (R-407b). ¿Puedes usarla con tu motocicleta?",
  [("No: it is compulsory for mopeds and forbidden to everyone else", "No: es obligatoria para ciclomotores y está prohibida a los demás usuarios"), ("Yes: it is for all two-wheelers", "Sí: es para todos los vehículos de dos ruedas"), ("Yes, if I ride slowly", "Sí, si circulo despacio")],
  "R-407b: track reserved and compulsory for mopeds; other users may not use it.", "R-407b: vía reservada y obligatoria para ciclomotores; los demás usuarios no pueden utilizarla.")
Q("ob4", "oblig", "A blue sign shows arrows for straight on and right only (R-403a). May you make a U-turn there?",
  "Una señal azul muestra flechas solo de frente y a la derecha (R-403a). ¿Puedes cambiar de sentido ahí?",
  [("No", "No"), ("Yes, if there is no oncoming traffic", "Sí, si no viene nadie de frente"), ("Yes, on a motorcycle", "Sí, en moto")],
  "The arrows show the only directions allowed, and these signs do not allow a U-turn.", "Las flechas señalan las únicas direcciones permitidas, y estas señales no permiten el cambio de sentido.")
Q("ob5", "oblig", "What does the “dipped beam” obligation sign (R-413) require?",
  "¿Qué exige la señal de obligación de alumbrado de corto alcance (R-413)?",
  [("At least dipped beam, whatever the visibility, until the sign that ends the obligation", "Al menos la luz de cruce, con independencia de la visibilidad, hasta la señal de fin de la obligación"), ("Dipped beam only at night", "La luz de cruce solo de noche"), ("Main beam in the tunnel", "La luz de carretera en el túnel")],
  "R-413 obliges everyone to use at least dipped beam regardless of visibility and lighting, until another sign ends it.", "La R-413 obliga a circular al menos con luz de cruce, con independencia de la visibilidad e iluminación, hasta otra señal de fin.")
Q("ob6", "oblig", "What ends at the white round sign with a black diagonal band and nothing else (R-500)?",
  "¿Qué termina en la señal circular blanca con una franja diagonal negra y nada más (R-500)?",
  [("All the specific prohibitions that earlier signs set for moving vehicles", "Todas las prohibiciones específicas indicadas por señales anteriores para vehículos en movimiento"), ("Only the speed limit", "Solo la limitación de velocidad"), ("The priority of your road", "La prioridad de tu vía")],
  "R-500, end of prohibitions: every specific prohibition for moving vehicles stops applying.", "R-500, fin de prohibiciones: dejan de aplicarse todas las prohibiciones específicas para vehículos en movimiento.")
Q("ob7", "oblig", "A minimum-speed sign (R-411) shows 40. Until where must you keep at least that speed?",
  "Una señal de velocidad mínima (R-411) indica 40. ¿Hasta dónde debes circular al menos a esa velocidad?",
  [("Until a different minimum-speed sign, its end sign, or a speed limit of equal or lower value", "Hasta otra de velocidad mínima diferente, la de fin de velocidad mínima o una de velocidad máxima de valor igual o inferior"),
   ("Until the next junction", "Hasta la próxima intersección"), ("For one kilometre", "Durante un kilómetro")],
  "R-411 applies from the sign to another minimum speed, the end of minimum speed or a maximum speed that is equal or lower.", "La R-411 obliga desde la señal hasta otra de velocidad mínima, la de fin o una de velocidad máxima igual o inferior.")

# ---------------------------------------------------------------- 7 indication signs
Q("in1", "info", "A blue square sign shows the figure 70 (S-7). What is it?",
  "Una señal cuadrada azul muestra la cifra 70 (S-7). ¿Qué es?",
  [("An advised maximum speed", "Una velocidad máxima aconsejable"), ("A compulsory minimum speed", "Una velocidad mínima obligatoria"), ("A speed limit", "Un límite de velocidad")],
  "S-7 recommends not exceeding about that speed. The limit is the red-ringed R-301; the minimum is the blue round R-411.", "La S-7 recomienda no sobrepasar esa velocidad. El límite es la R-301, de borde rojo; la mínima es la R-411, circular azul.")
Q("in2", "info", "What is the maximum speed in a residential play zone signed with S-28?",
  "¿Cuál es la velocidad máxima en una zona de estancia y juego señalizada con S-28?",
  [("10 km/h", "10 km/h"), ("20 km/h", "20 km/h"), ("30 km/h", "30 km/h")],
  "S-28: 10 km/h, and pedestrians may use the whole zone. The coexistence zone S-47 is 20 km/h.", "S-28: 10 km/h, y los peatones pueden usar toda la zona. La zona de coexistencia S-47 es de 20 km/h.")
Q("in3", "info", "In a coexistence zone (S-47), which is true?",
  "En una zona de coexistencia (S-47), ¿qué es cierto?",
  [("The limit is 20 km/h and games are not allowed", "El límite es 20 km/h y los juegos no están autorizados"), ("The limit is 10 km/h and games are allowed", "El límite es 10 km/h y los juegos están autorizados"), ("Vehicles may park anywhere", "Los vehículos pueden estacionar en cualquier lugar")],
  "S-47: 20 km/h, pedestrians may use the whole zone but games and sports are not authorised, and parking only in marked places.", "S-47: 20 km/h, los peatones pueden usar toda la zona pero los juegos y deportes no están autorizados, y solo se estaciona en los lugares designados.")
Q("in4", "info", "On a motorway you pass panels with three, two and one diagonal bars (S-26). What do they tell you?",
  "En una autopista pasas junto a paneles con tres, dos y una franja oblicua (S-26). ¿Qué te indican?",
  [("The next exit is about 300, 200 and 100 m away", "Que la próxima salida está aproximadamente a 300, 200 y 100 m"), ("A level crossing in 200, 150 and 100 m", "Un paso a nivel a 200, 150 y 100 m"), ("The end of the motorway", "El final de la autopista")],
  "S-26: exit countdown markers on motorways and autovías, at 300, 200 and 100 m.", "S-26: paneles de aproximación a salida en autopistas y autovías, a 300, 200 y 100 m.")
Q("in5", "info", "Lane signs show a minimum-speed figure over the left lane (S-50). Who may use that lane?",
  "Unas señales de carriles muestran una velocidad mínima sobre el carril izquierdo (S-50). ¿Quién puede usar ese carril?",
  [("Only vehicles going at that speed or faster, though they should keep right when they can", "Solo los que circulen a esa velocidad o superior, aunque deben ir por la derecha si las circunstancias lo permiten"), ("Only cars", "Solo los turismos"), ("Only vehicles that are overtaking", "Solo los que estén adelantando")],
  "The lane under the minimum-speed figure is only for vehicles at or above it; even so, they must use the right-hand lane if circumstances allow.", "El carril bajo la cifra de velocidad mínima solo puede ser utilizado por quienes circulen a esa velocidad o más; aun así, deben ir por la derecha si es posible.")
Q("in6", "info", "A reserved lane signed with S-51 does not show your vehicle, and its line is broken. When may you enter it?",
  "Un carril reservado señalizado con S-51 no incluye tu vehículo y su línea es discontinua. ¿Cuándo puedes entrar en él?",
  [("Only for a manoeuvre that is not stopping, parking, turning round or overtaking, giving preference to authorised vehicles", "Solo para una maniobra que no sea parar, estacionar, cambiar de sentido o adelantar, dejando preferencia a los autorizados"),
   ("Whenever it is empty", "Siempre que esté vacío"), ("Never", "Nunca")],
  "Where the lane’s line is broken, other vehicles may use it only for such a manoeuvre and always giving preference to the authorised vehicles.", "En tramos con línea discontinua, el resto de vehículos puede utilizarlo únicamente para esas maniobras y dejando siempre preferencia a los autorizados.")
Q("in7", "info", "On a motorway, the exit leads to a conventional road. What colour is the pre-signposting sign before the exit?",
  "En una autopista, la salida conduce a una carretera convencional. ¿De qué color es el cartel de preseñalización anterior a la salida?",
  [("Blue: it keeps the colour of the road you are on", "Azul: mantiene el color de la vía por la que circulas"), ("White: the colour of the road you are going to", "Blanco: el color de la vía a la que vas"), ("Green", "Verde")],
  "Pre-signposting takes the colour of the road the exit leads to, except when that road is of a lower category. The sign at the exit itself does change.", "La preseñalización toma el color de la vía a la que se dirige la salida, salvo que sea de inferior categoría. El cartel de salida inmediata sí cambia.")
Q("in8", "info", "Below a “road narrows” warning sign there is a panel with a figure in metres (S-800). What may it show?",
  "Bajo una señal de estrechamiento de calzada hay un panel con una cifra en metros (S-800). ¿Qué puede indicar?",
  [("The free width available", "La anchura libre disponible"), ("The maximum speed", "La velocidad máxima"), ("The maximum weight", "La masa máxima")],
  "S-800 gives the distance to where the danger or rule starts; under the narrowing sign it may give the free width.", "La S-800 indica la distancia al comienzo del peligro o prescripción; bajo la señal de estrechamiento puede indicar la anchura libre disponible.")

# ---------------------------------------------------------------- 8 lines along and across
Q("mk1", "mklines", "A continuous white line divides the two directions of the road. What does it forbid?",
  "Una línea blanca continua separa los dos sentidos de la vía. ¿Qué prohíbe?",
  [("Crossing it, riding on it and riding to its left", "Atravesarla, circular sobre ella y circular por su izquierda"), ("Only overtaking cars", "Solo adelantar a turismos"), ("Only riding on it", "Solo circular sobre ella")],
  "No driver may cross it or drive on it nor, when it divides the two directions, drive to its left.", "Ningún conductor debe atravesarla ni circular sobre ella ni, cuando separe los dos sentidos, circular por su izquierda.")
Q("mk2", "mklines", "The centre marking is a continuous line beside a broken line. Which one counts for you?",
  "La marca central es una línea continua adosada a una discontinua. ¿Cuál cuenta para ti?",
  [("The one on the side where you are riding", "La situada en el lado por el que circulas"), ("Always the continuous one", "Siempre la continua"), ("Always the broken one", "Siempre la discontinua")],
  "Drivers only take into account the line on their own side.", "Los conductores solo deben tener en cuenta la línea situada en el lado por el que circulan.")
Q("mk3", "mklines", "You started an overtake where the line was broken; now a continuous line beside a broken one separates the two directions, with the continuous on your side. May you return to your lane?",
  "Empezaste a adelantar con línea discontinua; ahora una continua adosada a discontinua separa los dos sentidos, con la continua de tu lado. ¿Puedes volver a tu carril?",
  [("Yes: it does not stop those who have overtaken from returning to their place", "Sí: no impide que quien ha adelantado vuelva a su lugar"), ("No: I must wait until it ends", "No: debo esperar a que termine"), ("Only if no agent is watching", "Solo si no hay ningún agente")],
  "When these markings separate the two directions, they do not prevent drivers who have overtaken from returning to their normal place.", "Cuando separan sentidos distintos, no impiden que los conductores que han adelantado vuelvan a ocupar su lugar normal.")
Q("mk4", "mklines", "The dashes of the broken centre line become noticeably closer together. What does that announce?",
  "Los trazos de la línea discontinua central están sensiblemente más juntos. ¿Qué anuncia?",
  [("A continuous line or a stretch of special risk is near", "La proximidad de una línea continua o de un tramo de riesgo especial"), ("A reversible lane", "Un carril reversible"), ("The start of a motorway", "El comienzo de una autopista")],
  "A noticeably shorter gap between dashes warns that a continuous line or a special risk is coming.", "Una separación sensiblemente más corta entre trazos avisa de que se aproxima una línea continua o un riesgo especial.")
Q("mk5", "mklines", "A lane is bounded on both sides by double broken lines. What kind of lane is it?",
  "Un carril está delimitado a ambos lados por líneas dobles discontinuas. ¿Qué carril es?",
  [("A reversible lane", "Un carril reversible"), ("A bus lane", "Un carril bus"), ("A deceleration lane", "Un carril de deceleración")],
  "Double broken lines on both sides mark a reversible lane, whose direction is set by lane lights or other means.", "Las líneas dobles discontinuas a ambos lados delimitan un carril reversible, regulado por semáforos de carril u otros medios.")
Q("mk6", "mklines", "A broken line across your lane marks where to give way, but from it you cannot see the other road. What may you do?",
  "Una línea discontinua transversal marca dónde ceder el paso, pero desde ella no ves la otra vía. ¿Qué puedes hacer?",
  [("Move forward until you can see, without having to stop at the line", "Avanzar hasta conseguir visibilidad, sin necesidad de detenerte ante ella"), ("You must always stop at the line first", "Debes detenerte siempre antes en la línea"), ("Go on without looking: you are on a motorcycle", "Pasar sin mirar: vas en moto")],
  "At a give-way line without visibility you may move forward until you can see, with no need to stop at it.", "En una línea de ceda el paso sin visibilidad se puede avanzar hasta conseguirla, sin necesidad de detenerse ante ella.")
Q("mk7", "mklines", "Which marking shows a cycle crossing?",
  "¿Qué marca vial señala un paso para ciclistas?",
  [("Two broken parallel lines across the carriageway", "Dos líneas transversales discontinuas y paralelas sobre la calzada"), ("Wide bands parallel to the road’s axis", "Bandas anchas paralelas al eje de la calzada"), ("A continuous line across the lane", "Una línea continua transversal")],
  "The cycle crossing is formed by two broken parallel transverse lines, and cyclists have priority on it.", "El paso para ciclistas está formado por dos líneas transversales discontinuas y paralelas, y en él los ciclistas tienen preferencia.")
Q("mk8", "mklines", "For the rules on continuous and broken lines, do the edge lines of the carriageway count as longitudinal markings?",
  "A efectos de las normas sobre líneas continuas y discontinuas, ¿cuentan las líneas de borde de la calzada como marcas longitudinales?",
  [("No", "No"), ("Yes, always", "Sí, siempre"), ("Only when they are continuous", "Solo cuando son continuas")],
  "The lines that mark the edges of the carriageway or the parking places are not considered white longitudinal markings for those rules.", "A esos efectos no se consideran marcas blancas longitudinales las líneas que delimitan los bordes de la calzada o los lugares de estacionamiento.")

# ---------------------------------------------------------------- 8 painted signs and other markings
Q("mo1", "mkother", "A white triangle is painted on your lane with its point towards you. What does it mean?",
  "En tu carril hay pintado un triángulo blanco con un vértice hacia ti. ¿Qué significa?",
  [("Give way at the next junction", "Obligación de ceder el paso en la próxima intersección"), ("Danger ahead", "Peligro próximo"), ("Your lane ends", "Tu carril termina")],
  "A painted triangle with one point towards the approaching vehicle means give way at the next junction.", "Un triángulo marcado con un vértice dirigido hacia el vehículo que se acerca indica la obligación de ceder el paso en la próxima intersección.")
Q("mo2", "mkother", "Traffic is queuing and beside you there is a hatched area framed by a continuous line. May you ride your motorcycle across it?",
  "Hay retención y junto a ti hay un cebreado enmarcado por una línea continua. ¿Puedes cruzarlo con tu motocicleta?",
  [("No: only those obliged to use the shoulder may enter it", "No: solo pueden entrar los obligados a circular por el arcén"), ("Yes: motorcycles may use it to filter", "Sí: las motos pueden usarlo para avanzar"), ("Yes, at walking pace", "Sí, a paso de persona")],
  "No driver may enter a hatched area, except those obliged to ride on the shoulder, and a motorcycle is not one of them.", "Ningún conductor debe entrar en el cebreado, excepto los obligados a circular por el arcén, y la motocicleta no lo está.")
Q("mo3", "mkother", "An arrow near the centre of a two-way road points to the right. What does it announce?",
  "Una flecha situada cerca del eje de una vía de doble sentido apunta hacia la derecha. ¿Qué anuncia?",
  [("A continuous line is coming: get into the lane it points to as soon as possible", "La proximidad de una línea continua: hay que circular cuanto antes por el carril al que apunta"), ("A compulsory right turn", "Un giro obligatorio a la derecha"), ("An exit to the right", "Una salida a la derecha")],
  "It is the return arrow: it announces a continuous line that forbids riding on its left.", "Es la flecha de retorno: anuncia una línea continua que prohíbe circular por su izquierda.")
Q("mo4", "mkother", "Chevrons are painted in the middle of your lane. How many must you leave, at least, between you and the vehicle ahead?",
  "En el centro de tu carril hay pintados galones. ¿Cuántos debes dejar, como mínimo, con el vehículo que te precede?",
  [("Two", "Dos"), ("One", "Uno"), ("Three", "Tres")],
  "The minimum distance is two chevrons on any type of road.", "La distancia mínima debe ser de dos galones en cualquier tipo de vía.")
Q("mo5", "mkother", "White triangles (“dragon’s teeth”) are painted along the edges of your lane. What do they tell you?",
  "A los lados de tu carril hay pintados triángulos blancos («dientes de dragón»). ¿Qué te indican?",
  [("Slow down noticeably: you are approaching a town street", "Reducir sensiblemente la velocidad: te aproximas a una travesía o vía urbana"), ("A cycle lane begins", "Empieza un carril bici"), ("Parking is forbidden", "Estacionamiento prohibido")],
  "Dragon’s teeth warn that you must slow down noticeably on approaching a travesía or urban road and take extreme care.", "Los dientes de dragón advierten de que hay que reducir sensiblemente la velocidad por la aproximación a una travesía o vía urbana y extremar la precaución.")
Q("mo6", "mkother", "A yellow zig-zag is painted beside the kerb. May you park your motorcycle on it?",
  "Junto al bordillo hay pintada una marca amarilla en zigzag. ¿Puedes estacionar la moto sobre ella?",
  [("No: parking is forbidden there for vehicles in general", "No: ahí está prohibido estacionar a los vehículos en general"), ("Yes: motorcycles take little room", "Sí: las motos ocupan poco"), ("Yes, for a few minutes", "Sí, unos minutos")],
  "The yellow zig-zag marks a place reserved for a special use, such as a bus stop or loading, where parking is forbidden.", "El zigzag amarillo indica un lugar reservado para un uso especial, como parada de autobús o carga y descarga, donde está prohibido estacionar.")
Q("mo7", "mkother", "What is the difference between a continuous and a broken yellow line along the kerb?",
  "¿Qué diferencia hay entre una línea amarilla continua y una discontinua junto al bordillo?",
  [("Continuous: no stopping or parking. Broken: no parking", "Continua: prohibidas la parada y el estacionamiento. Discontinua: prohibido el estacionamiento"), ("Continuous: no parking. Broken: no stopping", "Continua: prohibido estacionar. Discontinua: prohibido parar"), ("None: both forbid only parking", "Ninguna: ambas prohíben solo estacionar")],
  "Continuous yellow: stopping and parking forbidden along the line. Broken yellow: parking forbidden.", "Amarilla continua: parada y estacionamiento prohibidos en toda la línea. Amarilla discontinua: estacionamiento prohibido.")
Q("mo8", "mkother", "A junction is painted with a yellow criss-cross grid. What does it remind you of?",
  "Una intersección tiene pintada una cuadrícula amarilla. ¿Qué te recuerda?",
  [("Not to enter if you would foreseeably be left stopped inside, blocking cross traffic", "No entrar si previsiblemente vas a quedar detenido dentro, obstruyendo la circulación transversal"), ("That stopping there is allowed briefly", "Que ahí se permite una parada breve"), ("That motorcycles have priority", "Que las motos tienen prioridad")],
  "The yellow grid reminds drivers of the ban on entering a junction when they are likely to be left stopped in it.", "La cuadrícula amarilla recuerda la prohibición de entrar en la intersección cuando previsiblemente se vaya a quedar detenido en ella.")

# ---------------------------------------------------------------- 9 on two wheels
Q("tw1", "twowheels", "How far apart are the two continuous lines that mark an advanced stop box?",
  "¿Qué distancia separa las dos marcas transversales continuas que delimitan un avanza-motos?",
  [("4 m", "4 m"), ("2 m", "2 m"), ("10 m", "10 m")],
  "The reserved space is bounded by two parallel continuous transverse lines 4 m apart.", "El espacio reservado está delimitado por dos marcas transversales continuas paralelas y separadas 4 m.")
Q("tw2", "twowheels", "When is the advanced stop box reserved, and for whom?",
  "¿Cuándo está reservado el avanza-motos y para quién?",
  [("While the light is red, for the vehicles painted in it", "Con el semáforo en rojo, para los vehículos pintados en él"), ("At all times, for every two-wheeler", "En todo momento, para todos los vehículos de dos ruedas"), ("While the light is green, for motorcycles", "Con el semáforo en verde, para las motos")],
  "When the light is red, the space may only be occupied by the vehicles shown by its pictograms.", "Cuando el semáforo está en rojo, el espacio solo puede ser ocupado por los vehículos indicados por sus pictogramas.")
Q("tw3", "twowheels", "In the sign that announces the box (S-49), which vehicles does the motorcycle pictogram stand for?",
  "En la señal que anuncia la zona (S-49), ¿a qué vehículos representa el pictograma de la motocicleta?",
  [("Motorcycles, three-wheelers treated as motorcycles and mopeds", "A motocicletas, vehículos de tres ruedas asimilados y ciclomotores"), ("Two-wheeled motorcycles only", "Solo a las motocicletas de dos ruedas"), ("Motorcycles and cycles", "A motocicletas y ciclos")],
  "The three types are represented by the motorcycle pictogram; cycles have their own.", "Los tres tipos están representados por el pictograma de la motocicleta; los ciclos tienen el suyo.")
Q("tw4", "twowheels", "May you ride your motorcycle in a bus lane signed with S-51?",
  "¿Puedes circular con tu moto por un carril bus señalizado con S-51?",
  [("Only if the motorcycle pictogram is on the sign", "Solo si en la señal figura el pictograma de la motocicleta"), ("Always: motorcycles may use every bus lane", "Siempre: las motos pueden usar cualquier carril bus"), ("Only at night", "Solo de noche")],
  "The sign carries the pictogram of the vehicle types that are authorised; the lane is exclusively for them.", "La señal incluye el pictograma de los tipos de vehículos autorizados; el carril es exclusivo para ellos.")
Q("tw5", "twowheels", "What do the motorcyclist guidance marks painted on the road tell you?",
  "¿Qué te indican las marcas de guiado para motoristas pintadas en la calzada?",
  [("That a bend of special risk is coming, and which part of the lane it is better not to ride on", "La aproximación a una curva de especial riesgo y la zona del carril que se recomienda evitar pisar"), ("The lane reserved for motorcycles", "El carril reservado a las motos"), ("Where motorcycles must stop", "Dónde deben detenerse las motos")],
  "They show motorcyclists and cyclists the approach to bends of special risk and the area of the lane they are advised to avoid.", "Indican a motoristas y ciclistas la aproximación a curvas de especial riesgo y la zona del carril que se recomienda evitar pisar.")
Q("tw6", "twowheels", "At a red light the box before the stop line is painted only with a bicycle. May you wait in it on your motorcycle?",
  "Ante un semáforo en rojo, la zona anterior a la línea de detención lleva pintada solo una bicicleta. ¿Puedes esperar en ella con tu moto?",
  [("No: it is only for the vehicles painted in it", "No: es solo para los vehículos pintados en ella"), ("Yes: it is for all two-wheelers", "Sí: es para todos los vehículos de dos ruedas"), ("Yes, if no cyclist is there", "Sí, si no hay ningún ciclista")],
  "The pictograms show which vehicles may enter; a box with only a bicycle is an avanza-bici.", "Los pictogramas indican qué vehículos pueden acceder; una zona con solo una bicicleta es un avanza-bici.")
Q("tw7", "twowheels", "A panel under a sign shows a car, the figure 1.5 m and two cyclists (S-891). What does it remind you of?",
  "Un panel bajo una señal muestra un turismo, «1,5 m» y dos ciclistas (S-891). ¿Qué te recuerda?",
  [("The minimum side gap when overtaking a cycle or a moped", "La anchura mínima de seguridad al adelantar a un ciclo o a un ciclomotor"), ("The minimum gap from the vehicle ahead", "La separación mínima con el vehículo de delante"), ("The width of the cycle lane", "La anchura del carril bici")],
  "S-891 recalls the minimum 1.5 m when overtaking a cycle or a moped; for a group, measured from the one furthest to the left.", "La S-891 recuerda los 1,5 m mínimos al adelantar a un ciclo o ciclomotor; en un grupo, respecto al que circula más a la izquierda.")
Q("tw8", "twowheels", "Which of these may enter a hatched area (cebreado)?",
  "¿Cuál de estos puede entrar en un cebreado?",
  [("A moped, as a vehicle obliged to use the shoulder", "Un ciclomotor, como vehículo obligado a circular por el arcén"), ("A motorcycle, to pass a queue", "Una motocicleta, para rebasar una retención"), ("Any two-wheeled vehicle", "Cualquier vehículo de dos ruedas")],
  "Only those obliged to ride on the shoulder may enter a hatched area; mopeds are among them, motorcycles are not.", "Solo pueden entrar en el cebreado los obligados a circular por el arcén; los ciclomotores lo están, las motocicletas no.")
Q("tw9", "twowheels", "What are the “motorcyclist protection systems” listed among the vehicle restraint systems?",
  "¿Qué son los «sistemas de protección para motoristas» incluidos entre los sistemas de contención de vehículos?",
  [("Barriers designed specifically to protect two-wheeled vehicles", "Barreras diseñadas específicamente para proteger a los vehículos de dos ruedas"), ("Lanes reserved for motorcycles", "Carriles reservados a las motos"), ("Compulsory clothing for riders", "Prendas obligatorias para motoristas")],
  "They are barriers specifically designed for the protection of two-wheeled vehicles.", "Son barreras específicamente diseñadas para la protección de los vehículos de dos ruedas.")
