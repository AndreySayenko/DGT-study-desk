# -*- coding: utf-8 -*-
"""Question bank for the interactive Topic 8 page (signs and signals). In every question the FIRST option is the
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
    "order": dict(sec=1, en="Order of priority", es="Orden de prioridad",
        recap=[("Agents → temporary signs and beaconing → traffic lights → vertical signs → road markings.", "Agentes → señalización circunstancial y balizamiento → semáforos → señales verticales → marcas viales."),
               ("Different groups: obey the one higher in that order. Same group: the most restrictive.", "Grupos distintos: la prioritaria según ese orden. Mismo grupo: la más restrictiva."),
               ("Sign against a traffic rule: obey the sign, unless special circumstances justify otherwise.", "Señal contra norma de circulación: la señal, salvo circunstancias especiales."),
               ("Everyone must obey signs; nobody may install, move, hide or alter them, or put objects that confuse, dazzle or distract.", "Todos deben obedecer; nadie puede instalar, trasladar, ocultar o modificar señales ni poner objetos que confundan, deslumbren o distraigan.")],
        trap=("Thinking a road marking beats a vertical sign.", "Pensar que una marca vial prevalece sobre una señal vertical.")),
    "place": dict(sec=1, en="Where signs apply", es="Colocación y aplicación",
        recap=[("Right-hand sign: everyone. Left-hand sign: straight on or left. Different signs: left for straight/left, right for right turns.", "Derecha: todos. Izquierda: de frente o a la izquierda. Distintas: izquierda de frente/izquierda; derecha, giro derecha."),
               ("Above the carriageway: whole carriageway. Above a lane: that lane only.", "Encima de la calzada: toda la calzada. Encima de un carril: solo ese carril."),
               ("Signs apply to the whole usable width unless painted in a lane or limited by a panel.", "Se aplican a toda la anchura utilizable, salvo dentro de un carril o limitadas por un panel."),
               ("Roadworks: yellow markings and yellow-background signs, same meaning; signed day and night, lit at night.", "Obras: marcas amarillas y señales con fondo amarillo, mismo significado; señalizadas de día y de noche, balizadas de noche.")],
        trap=("Thinking a sign on the left also binds those turning right.", "Pensar que la señal de la izquierda obliga también a los que giran a la derecha.")),
    "arms": dict(sec=2, en="Agents’ arm signals", es="Señales de los agentes con los brazos",
        recap=[("Agents’ orders prevail over every other sign and rule, even if they contradict them.", "Las órdenes de los agentes prevalecen sobre las demás señales y normas, aunque las contradigan."),
               ("Arm raised: everyone approaching stops (at the stop line, before the agent, or before the junction); those already inside carry on.", "Brazo levantado: todos los que se acercan se detienen (línea de detención, antes del agente o antes de la intersección); los que ya están dentro siguen."),
               ("Arms out sideways: traffic crossing the arms’ line stops; the order stays while the agent keeps position.", "Brazos extendidos: se detienen los que cortan la dirección de los brazos; la orden sigue mientras no cambie de posición."),
               ("Swinging red/amber light: those it is aimed at stop. Arm moving up and down: slow down.", "Luz roja/amarilla en balanceo: se detienen aquellos a los que se dirige. Brazo arriba y abajo: reducir velocidad.")],
        trap=("Taking the up-and-down arm as an order to stop.", "Tomar el brazo arriba y abajo como orden de detenerse.")),
    "agveh": dict(sec=2, en="Whistle and agents’ vehicles", es="Silbato y señales desde el vehículo",
        recap=[("Whistle: short frequent blasts = stop; one long blast = move off.", "Silbato: toques cortos y frecuentes = detención; un toque largo = reanudar."),
               ("Red flag: road closed after the vehicle; yellow: extreme care / danger; green: road open again.", "Bandera roja: calzada cerrada tras el vehículo; amarilla: extremar la atención / peligro; verde: de nuevo abierta."),
               ("Arm held down, slanted and still, from a vehicle: stop on the right.", "Brazo extendido hacia abajo, inclinado y fijo, desde un vehículo: detenerse a la derecha."),
               ("Flashing red light forwards: stop on the right ahead of the police car and obey the loudspeaker.", "Luz roja intermitente hacia delante: detenerse a la derecha delante del vehículo policial y obedecer la megafonía.")],
        trap=("Stopping behind the police car instead of in front of it.", "Detenerse detrás del coche policial en vez de delante.")),
    "helpers": dict(sec=2, en="Agents’ helpers", es="Auxiliares de los agentes",
        recap=[("Roadworks staff and special-transport escorts regulate with paddle signs: obey them.", "Personal de obras y de acompañamiento de transportes especiales regulan con paleta: hay que obedecerles."),
               ("School patrols may “invite” users to stop with a paddle.", "Las patrullas escolares pueden «invitar» a detenerse con una paleta."),
               ("Military Police may regulate traffic; civil-protection or organisers’ staff may close routes for authorised events.", "La Policía Militar puede regular; protección civil o la organización pueden cerrar el paso en actos autorizados."),
               ("All wear bright clothing and retroreflective elements visible from at least 150 m.", "Todos llevan prendas llamativas y elementos retrorreflectantes visibles a 150 m como mínimo.")],
        trap=("Mixing up 150 m with other distances.", "Confundir 150 m con otras distancias.")),
    "beacon": dict(sec=3, en="Variable messages and delimiting devices", es="Paneles variables y dispositivos delimitadores",
        recap=[("Variable message signs adapt traffic to circumstances: inform, warn, recommend or give compulsory orders; never more than 2 alternating messages.", "Los paneles de mensaje variable adaptan la circulación: informan, advierten, recomiendan u ordenan; nunca más de 2 mensajes alternados."),
               ("Fixed barrier: no passing. Moving barrier: no passing while moving or across; queue one behind another.", "Barrera fija: prohíbe el paso. Móvil: lo prohíbe mientras se mueve o está transversal; esperar uno detrás de otro."),
               ("Cones, edge beacons and yellow lights: do not cross the real or imaginary line joining them.", "Conos, balizas de borde y luces amarillas: no atravesar la línea real o imaginaria que los une."),
               ("Steady red light: carriageway completely closed. Temporary direction panel: no passing, shows the direction.", "Luz roja fija: calzada totalmente cerrada. Panel direccional provisional: prohíbe el paso e indica el sentido.")],
        trap=("Thinking a variable message is only a recommendation.", "Pensar que un panel variable solo recomienda.")),
    "guide": dict(sec=3, en="Guide devices and barriers", es="Dispositivos de guía y contención",
        recap=[("Gore marker: where two streams separate. Edge posts: the road’s edges at night.", "Hito de vértice: donde se separan dos corrientes. Hito de arista: bordes de la vía de noche."),
               ("Permanent direction panels: single, double or triple = moderate, medium, high danger.", "Paneles direccionales permanentes: sencillo, doble o triple = peligro moderado, medio o elevado."),
               ("Edge posts and reflectors: white on the left, white or yellow on the right. Luminous studs: cross only when green.", "Hitos y captafaros: blancos a la izquierda; blancos o amarillos a la derecha. Captafaro luminoso: solo se pasa en verde."),
               ("Fog lights: amber = direction/edge, red = a vehicle passing. Parapets protect on bridges; crash cushions at forks.", "Balizamiento en niebla: ámbar = sentido/borde, rojo = paso de un vehículo. Pretiles en puentes; atenuadores en bifurcaciones.")],
        trap=("Thinking a windsock replaces the crosswind warning sign.", "Pensar que la manga de viento sustituye a la señal de viento transversal.")),
    "tlights": dict(sec=4, en="Steady traffic lights", es="Semáforos de luz fija",
        recap=[("Pedestrians: steady green = start crossing; flashing green = time running out; red = do not start.", "Peatones: verde fijo = comenzar a cruzar; verde intermitente = se acaba el tiempo; rojo = no comenzar."),
               ("Green: go with priority, unless you would be left stopped blocking a junction or crossing.", "Verde: paso con prioridad, salvo que fueras a quedar detenido obstruyendo un cruce."),
               ("Steady amber: stop as for red unless too close to stop safely.", "Amarillo fijo: detenerse como en rojo salvo que estés tan cerca que no puedas hacerlo con seguridad."),
               ("Red: stop before the light or the stop line; a light inside or beyond a junction means do not enter it.", "Rojo: detenerse antes del semáforo o de la línea; si está dentro o al otro lado de la intersección, no entrar.")],
        trap=("Entering a junction on green although you will be stuck inside it.", "Entrar con verde en un cruce donde vas a quedar detenido.")),
    "tlflash": dict(sec=4, en="Flashing lights and arrows", es="Luces intermitentes y flechas",
        recap=[("Flashing red (one, or two alternating): temporarily no passing — level crossings, bridges, fire stations, low aircraft.", "Roja intermitente (una o dos alternas): prohibido temporalmente el paso — pasos a nivel, puentes, bomberos, aeronaves."),
               ("Flashing amber: extreme care and give way if needed; other stop signs still apply.", "Ámbar intermitente: extremar la precaución y ceder si procede; las demás señales de detención siguen rigiendo."),
               ("Green arrow: go that way whatever else is lit, with care, giving way to the lane you join and to pedestrians.", "Flecha verde: se puede ir en esa dirección con cualquier otra luz, con precaución, cediendo al carril de destino y a peatones."),
               ("Black arrow on red or amber: the light applies only to that movement.", "Flecha negra sobre roja o amarilla: la luz solo afecta a ese movimiento.")],
        trap=("Thinking a flashing amber cancels a STOP sign.", "Pensar que el ámbar intermitente anula un STOP.")),
    "tllane": dict(sec=4, en="Lane lights and special lights", es="Semáforos de carril y reservados",
        recap=[("Square lane lights apply only to the lane beneath; also at motorway tolls.", "Los cuadrados afectan solo al carril sobre el que están; también en peajes."),
               ("Green down arrow: use the lane (still obey red lights and stop signs). Oblique arrow: move over, the lane closes. Red cross: leave the lane asap.", "Flecha verde abajo: usar el carril (sin eximir de rojos ni stops). Flecha oblicua: cambiarse, el carril se cierra. Aspa roja: abandonarlo cuanto antes."),
               ("White bar lights: trams and regular buses (or all users of a reserved lane). Horizontal = stop, vertical = straight, slanted = turn.", "Franja blanca: tranvías y autobuses regulares (o todos los del carril reservado). Horizontal = parar, vertical = de frente, inclinada = giro."),
               ("Flashing white bar: stop as for steady amber. Bicycle lights: cycles only.", "Franja intermitente: detenerse como ante ámbar fijo. Semáforo con bici: solo ciclos.")],
        trap=("Thinking bus lights bind cars outside the bus lane.", "Pensar que los semáforos de bus afectan a turismos fuera del carril bus.")),
    "warn": dict(sec=5, en="Warning signs", es="Señales de advertencia de peligro",
        recap=[("Red-bordered triangles: a danger hard to see in time; a panel may give the distance or the length.", "Triángulos con borde rojo: peligro difícil de percibir a tiempo; un panel puede dar la distancia o la longitud."),
               ("P-1 family: you have priority over the side road; on P-1c/d still make the merge easier. P-2: priority to the right.", "Familia P-1: tienes prioridad sobre la vía lateral; en P-1c/d facilita la incorporación. P-2: prioridad de la derecha."),
               ("P-9/P-10 posts: 3 stripes 200 m, 2 = 150 m, 1 = 100 m, always with P-5, P-7, P-8 or P-27.", "Balizas P-9/P-10: 3 franjas 200 m, 2 = 150 m, 1 = 100 m, siempre con P-5, P-7, P-8 o P-27."),
               ("P-29 crosswind does not say the side. P-35 weaving: paths cross between a merge and a fork.", "P-29 viento transversal no indica el lado. P-35 trenzado: trayectorias cruzadas entre confluencia y bifurcación.")],
        trap=("Mixing up P-14a (first bend right) and P-14b.", "Confundir P-14a (primera curva a la derecha) y P-14b.")),
    "prio": dict(sec=6, en="Priority signs and how R signs apply", es="Señales de prioridad y aplicación",
        recap=[("R-1 give way at the next junction; R-2 STOP at the line or before the junction, stop again if you cannot see.", "R-1 ceder en la próxima intersección; R-2 STOP en la línea o antes del cruce, y otra vez si no hay visibilidad."),
               ("R-3 priority road; R-4 end of priority. R-5: give way to oncoming; R-6: you have priority in the narrow passage.", "R-3 calzada con prioridad; R-4 fin. R-5: cede al que viene; R-6: tienes prioridad en el paso estrecho."),
               ("P-1 to P-1e, P-2, P-6, P-7 and P-8 are also priority signs.", "P-1 a P-1e, P-2, P-6, P-7 y P-8 también son señales de prioridad."),
               ("R signs apply from where they stand unless a panel gives a distance; beside the town sign they apply to the whole town.", "Las R rigen desde donde están salvo panel de distancia; junto a la de poblado, a todo el poblado.")],
        trap=("Confusing R-5 (red ring) with R-6 (blue square).", "Confundir R-5 (borde rojo) con R-6 (cuadrado azul).")),
    "noentry": dict(sec=6, en="No-entry and restriction signs", es="Prohibición de entrada y restricción",
        recap=[("R-100 no vehicles both ways; R-101 no entry. They bind those meeting them head-on.", "R-100 circulación prohibida en ambos sentidos; R-101 entrada prohibida. Afectan a quien se las encuentra de frente."),
               ("R-103 lets two-wheeled motorcycles in; R-105 also bans reduced-mobility vehicles; R-107 applies even empty.", "R-103 deja pasar motos de dos ruedas; R-105 prohíbe también vehículos de movilidad reducida; R-107 aunque vayan vacíos."),
               ("R-110: more than 1,000 l of water pollutants. R-120: by environmental label (S-860 panel).", "R-110: más de 1.000 l de contaminantes del agua. R-120: según distintivo ambiental (panel S-860)."),
               ("R-200 stop at customs/police/toll; R-201 actual mass; R-203–R-205 length, width, height with the load.", "R-200 detenerse en aduana/policía/peaje; R-201 masa en carga; R-203 a R-205 longitud, anchura y altura con la carga.")],
        trap=("Thinking R-107 lets an empty heavy lorry through.", "Pensar que la R-107 deja pasar a un camión pesado vacío.")),
    "other": dict(sec=6, en="Other prohibitions", es="Otras prohibiciones",
        recap=[("R-301 lasts until an end sign or another limit; with a danger sign, until the danger ends; on a minor road, until a junction with a priority road.", "R-301 rige hasta su fin u otra limitación; con señal de peligro, hasta que acaba el peligro; en vía sin prioridad, hasta el cruce con una con prioridad."),
               ("R-303 no left turn includes U-turns; R-304 no U-turn still allows turning.", "R-303 giro a la izquierda prohibido incluye el cambio de sentido; R-304 media vuelta prohibida permite girar."),
               ("R-305 no overtaking motor vehicles if you invade the other side; R-306 lorries over 3,500 kg even without invading.", "R-305 prohibido adelantar a vehículos de motor invadiendo el contrario; R-306 camiones de más de 3.500 kg aunque no invadan."),
               ("R-307 no stopping or parking; R-308 no parking (stopping OK) on that side to the next junction; R-308c/d fortnights from 9:00.", "R-307 parada y estacionamiento prohibidos; R-308 solo estacionamiento, en ese lado hasta la intersección; R-308c/d quincenas desde las 9 h.")],
        trap=("Thinking R-308 also forbids stopping.", "Pensar que la R-308 prohíbe también la parada.")),
    "oblig": dict(sec=6, en="Obligation and end signs", es="Obligación y fin de prohibición",
        recap=[("Blue circles order: direction, passing side, roundabout, only directions (no U-turn on R-403).", "Círculos azules obligan: sentido, paso obligatorio, glorieta, únicas direcciones (R-403 no permite cambio de sentido)."),
               ("Reserved tracks (cycles, mopeds, riders, pedestrians, VMP): compulsory for them and forbidden for others.", "Vías reservadas (ciclos, ciclomotores, jinetes, peatones, VMP): obligatorias para ellos y prohibidas para los demás."),
               ("R-411 minimum speed; R-412 chains on at least one wheel each side of a drive axle, or snow tyres; R-413 dipped beam.", "R-411 velocidad mínima; R-412 cadenas en al menos una rueda a cada lado del eje motor, o neumáticos de nieve; R-413 luz de cruce."),
               ("R-500 ends all specific prohibitions for moving vehicles; blue signs with a red bar end an obligation.", "R-500 termina todas las prohibiciones específicas para vehículos en movimiento; las azules con barra roja terminan una obligación.")],
        trap=("Thinking R-500 also ends a limited parking zone.", "Pensar que la R-500 termina también la zona de estacionamiento limitado.")),
    "zones": dict(sec=7, en="General indication signs", es="Indicaciones generales",
        recap=[("S-1 motorway, S-1a autovía, S-1b multi-lane road, S-1c 2+1 road (middle lane for overtaking, alternating); red bar = end.", "S-1 autopista, S-1a autovía, S-1b multicarril, S-1c 2+1 (carril central para adelantar, alterno); barra roja = fin."),
               ("S-7 and S-9 only recommend a speed; under a warning sign they refer to that danger.", "S-7 y S-9 solo recomiendan; bajo una señal de peligro se refieren a ese tramo."),
               ("S-28 play zone 10 km/h, games allowed; S-47 coexistence 20 km/h, games not allowed; parking only where marked.", "S-28 estancia y juego 10 km/h, juegos permitidos; S-47 coexistencia 20 km/h, juegos no; estacionar solo en lugares designados."),
               ("S-26 exit at 300/200/100 m; S-49 advanced stop box; S-17a parking for a specific need.", "S-26 salida a 300/200/100 m; S-49 avanza moto o bici; S-17a estacionamiento de necesidad.")],
        trap=("Taking a blue square speed sign as a compulsory limit.", "Tomar la velocidad del cuadrado azul como límite obligatorio.")),
    "lanes": dict(sec=7, en="Lane signs", es="Señales de carriles",
        recap=[("S-50: lanes with a minimum speed only for vehicles at or above it; keep right when you can.", "S-50: carriles con velocidad mínima solo para quien la alcance; si se puede, por la derecha."),
               ("S-51a bus lane: where its line is dashed, others may use it only for manoeuvres other than stop, park, U-turn or overtake.", "S-51a carril bus: con línea discontinua, los demás solo para maniobras que no sean parar, estacionar, cambiar de sentido o adelantar."),
               ("S-51b VAO: minimum number of occupants shown.", "S-51b VAO: número mínimo de ocupantes indicado."),
               ("S-52 lane ends; S-53 one lane becomes two; S-60–S-63 forks; S-70–S-73 merges (dashed arrow = the joining lane).", "S-52 fin de carril; S-53 de uno a dos; S-60 a S-63 bifurcaciones; S-70 a S-73 confluencias (flecha discontinua = carril que se une).")],
        trap=("Thinking you may overtake in a bus lane with a dashed line.", "Pensar que se puede adelantar por un carril bus con línea discontinua.")),
    "orient": dict(sec=7, en="Services, orientation, panels and others", es="Servicio, orientación, paneles y otras",
        recap=[("Orientation colours: white for conventional and multi-lane roads, blue for motorways; confirmation keeps the current road’s colour.", "Colores: blanco en convencional y multicarril, azul en autopistas; la confirmación mantiene el color de la vía actual."),
               ("Pre-signposting takes the destination road’s colour except to a lower category; the immediate exit sign always does.", "La preseñalización toma el color de la vía de destino salvo si es de inferior categoría; la de salida inmediata siempre."),
               ("Road numbers: E green, A/AP blue, State red, regional orange/brown/yellow. Exit numbers = kilometre point.", "Matrículas: E verde, A/AP azul, Estado rojo, autonómicas naranja/marrón/amarillo. Número de salida = punto kilométrico."),
               ("Panels: S-800 distance, S-810 length, S-840 STOP ahead, S-860 generic, S-891 1.5 m, S-892 automatic cameras.", "Paneles: S-800 distancia, S-810 longitud, S-840 STOP a…, S-860 genérico, S-891 1,5 m, S-892 medios automáticos.")],
        trap=("Thinking an exit panel always keeps the motorway blue.", "Pensar que el cartel de salida mantiene siempre el azul de la autopista.")),
    "mklong": dict(sec=8, en="Longitudinal markings", es="Marcas longitudinales",
        recap=[("Continuous: do not cross or drive on it, nor to its left when it separates directions; two lines mean the same.", "Continua: no atravesarla ni circular sobre ella, ni por su izquierda si separa sentidos; dos líneas igual."),
               ("Wider continuous = special lane: only its users may cross it to leave. Broken: guides; drive on it only if lanes are narrow.", "Continua más ancha = carril especial: solo sus usuarios la cruzan para salir. Discontinua: guía; pisarla solo si los carriles son estrechos."),
               ("Shorter gaps: a continuous line or special risk is coming; broken lines also announce forks and merges.", "Trazos más juntos: se acerca una continua o un riesgo especial; también anuncia bifurcaciones y confluencias."),
               ("Continuous + broken: obey your side’s line; double broken lines = reversible lane. Edge and parking lines are not counted.", "Continua + discontinua: atender a la de tu lado; dobles discontinuas = carril reversible. Bordes y estacionamientos no cuentan.")],
        trap=("Thinking an overtaking driver cannot return across a continuous line beside a broken one.", "Pensar que quien ha adelantado no puede volver por una continua adosada a discontinua.")),
    "mktrans": dict(sec=8, en="Transverse markings and painted signs", es="Marcas transversales y señales horizontales",
        recap=[("Stop line: do not cross when you must stop (STOP, R-200, crossing, light, agent, level crossing); stop again if you cannot see.", "Línea de detención: no rebasarla si hay que parar (STOP, R-200, paso, semáforo, agente, paso a nivel); volver a parar si no hay visibilidad."),
               ("Give-way line: do not cross when you must give way; if you cannot see, edge forward without stopping.", "Línea de ceda: no rebasarla si hay que ceder; sin visibilidad, avanzar hasta conseguirla sin detenerse."),
               ("Zebra: wide bands parallel to the axis, no other colours; give way to pedestrians. Cycle crossing: two dashed lines, cyclists first.", "Paso de peatones: bandas paralelas al eje, sin otros colores; ceder el paso. Paso ciclista: dos discontinuas, preferencia ciclista."),
               ("Painted signs in a lane bind that lane only; return arrow = a continuous line ahead, move right.", "Las señales pintadas en un carril solo afectan a ese carril; flecha de retorno = se acerca una continua, volver a la derecha.")],
        trap=("Thinking you must stop at a give-way line.", "Pensar que hay que detenerse siempre en la línea de ceda el paso.")),
    "mkother": dict(sec=8, en="Other markings and colours", es="Otras marcas y colores",
        recap=[("Hatched area: no entry except for those who must use the shoulder. Edge line: continuous or broken, same thing.", "Cebreado: no entrar salvo los obligados a circular por el arcén. Borde: continua o discontinua, igual."),
               ("Chevrons: keep at least 2; R-300 at the start. Avanza-motos: two lines 4 m apart, for the vehicles shown on red.", "Galones: al menos 2; R-300 al inicio. Avanza-motos: dos líneas a 4 m, para los vehículos del pictograma con rojo."),
               ("Dragon’s teeth: entering a town. Zig-zag edges: crossing ahead. Chequerboard: hidden risk ahead.", "Dientes de dragón: llegada a travesía. Bordes quebrados: paso cercano. Damero: riesgo mayor del percibido."),
               ("Yellow zig-zag and broken kerb line: no parking; continuous yellow: no stopping or parking; yellow box: don’t block; red-white: escape lane; blue: limited parking.",
                "Zigzag y discontinua amarillas: no estacionar; continua amarilla: ni parar ni estacionar; cuadrícula: no bloquear; rojo-blanco: frenado de emergencia; azul: estacionamiento limitado.")],
        trap=("Thinking the broken yellow kerb line also forbids stopping.", "Pensar que la amarilla discontinua prohíbe también la parada.")),
}

# ---------------------------------------------------------------- 1. general rules
Q("or1", "order", "A traffic light is green but an agent signals you to stop. You…", "Un semáforo está en verde pero un agente te ordena detenerte. Tú…",
  [("stop: agents come first", "te detienes: el agente es prioritario"), ("go on: the light is green", "sigues: el semáforo está en verde"), ("go on carefully", "sigues con precaución")],
  "Agents’ orders prevail over every other signal.", "Las órdenes de los agentes prevalecen sobre las demás señales.")
Q("or2", "order", "Which comes first in the order of priority?", "¿Qué va antes en el orden de prioridad?",
  [("Traffic lights", "Los semáforos"), ("Vertical signs", "Las señales verticales"), ("Road markings", "Las marcas viales")],
  "Agents, temporary signs, lights, vertical signs, markings.", "Agentes, circunstancial, semáforos, verticales, marcas.")
Q("or3", "order", "A road marking and a vertical sign contradict each other. You obey…", "Una marca vial y una señal vertical se contradicen. Obedeces…",
  [("the vertical sign", "la señal vertical"), ("the road marking", "la marca vial"), ("the less restrictive", "la menos restrictiva")],
  "Markings are last in the order.", "Las marcas van en último lugar.")
Q("or4", "order", "Two vertical signs contradict each other. You obey…", "Dos señales verticales se contradicen. Obedeces…",
  [("the most restrictive", "la más restrictiva"), ("the nearer one", "la más cercana"), ("the one on the right", "la de la derecha")],
  "Same group: the most restrictive.", "Mismo grupo: la más restrictiva.")
Q("or5", "order", "A sign contradicts a general traffic rule. You obey…", "Una señal contradice una norma de circulación. Obedeces…",
  [("the sign, unless special circumstances justify otherwise", "la señal, salvo circunstancias especiales que lo justifiquen"), ("the rule", "la norma"), ("whichever you prefer", "la que prefieras")],
  "Signs prevail over the general rules.", "La señal prevalece sobre la norma.")
Q("or6", "order", "Temporary signs and traffic lights disagree. Which prevails?", "La señalización circunstancial y un semáforo no coinciden. ¿Qué prevalece?",
  [("The temporary signs", "La señalización circunstancial"), ("The traffic light", "El semáforo"), ("Neither: stop", "Ninguno: detenerse")],
  "They are second, lights are third.", "Va segunda; los semáforos, terceros.")
Q("or7", "order", "May a shop put a poster next to a traffic sign?", "¿Puede una tienda poner un cartel junto a una señal?",
  [("No, if it can confuse, reduce visibility or distract", "No, si puede confundir, reducir su visibilidad o distraer"), ("Yes, if it is small", "Sí, si es pequeño"), ("Yes, in town", "Sí, en poblado")],
  "Nothing may be placed on or near signs that harms their effect.", "No se pueden poner objetos que perjudiquen su eficacia.")
Q("or8", "order", "Who must obey traffic signs?", "¿Quién debe obedecer las señales?",
  [("All road users", "Todos los usuarios"), ("Only drivers", "Solo los conductores"), ("Only motor vehicles", "Solo los vehículos de motor")],
  "Pedestrians and cyclists included.", "Incluidos peatones y ciclistas.")
Q("pl1", "place", "A STOP sign stands only on the left of the road. It binds…", "Una señal de STOP está solo a la izquierda. Obliga a…",
  [("those going straight on or turning left", "los que siguen de frente o giran a la izquierda"), ("everyone", "todos"), ("only those turning right", "solo a los que giran a la derecha")],
  "Left-hand signs: straight on or left.", "Señales a la izquierda: de frente o a la izquierda.")
Q("pl2", "place", "A sign placed on the right of the road applies to…", "Una señal colocada a la derecha afecta a…",
  [("everyone, straight on or turning", "todos, sigan de frente o giren"), ("only those turning right", "solo a los que giran a la derecha"), ("only those going straight on", "solo a los que siguen de frente")],
  "Right-hand signs bind everyone.", "Las de la derecha obligan a todos.")
Q("pl3", "place", "There is a STOP on the left and a give-way sign on the right. You want to turn right. You obey…", "Hay un STOP a la izquierda y un ceda el paso a la derecha. Vas a girar a la derecha. Obedeces…",
  [("the give-way sign", "el ceda el paso"), ("the STOP", "el STOP"), ("both", "las dos")],
  "The right-hand sign is for right turns.", "La de la derecha es para el giro a la derecha.")
Q("pl4", "place", "A sign hangs over one lane. It applies to…", "Una señal está sobre un carril. Afecta a…",
  [("that lane only", "solo ese carril"), ("the whole carriageway", "toda la calzada"), ("the right lane", "el carril derecho")],
  "Over the carriageway it would apply to all of it.", "Sobre la calzada afectaría a toda ella.")
Q("pl5", "place", "A “30” is painted inside your lane. It applies to…", "Hay un «30» pintado dentro de tu carril. Afecta a…",
  [("vehicles in that lane", "los vehículos de ese carril"), ("the whole carriageway", "toda la calzada"), ("only lorries", "solo a camiones")],
  "A sign inside a lane is limited to it.", "Dentro de un carril solo afecta a ese carril.")
Q("pl6", "place", "In roadworks, what colour are the road markings?", "En las obras, ¿de qué color son las marcas viales?",
  [("Yellow", "Amarillas"), ("Orange", "Naranjas"), ("White", "Blancas")],
  "Some signs also get a yellow background.", "Algunas señales llevan también fondo amarillo.")
Q("pl7", "place", "A warning sign with a yellow background means…", "Una señal de peligro con fondo amarillo significa…",
  [("the same as usual, in roadworks", "lo mismo que la normal, en obras"), ("a recommendation", "una recomendación"), ("a more serious danger", "un peligro más grave")],
  "Its meaning does not change.", "Su significado no cambia.")
Q("pl8", "place", "Works that hinder traffic must be signed…", "Las obras que dificultan la circulación deben señalizarse…",
  [("by day and by night, and lit at night", "de día y de noche, con balizamiento luminoso de noche"), ("only by day", "solo de día"), ("only on motorways", "solo en autopistas")],
  "Also lit when weather requires it.", "También si el tiempo lo exige.")

# ---------------------------------------------------------------- 2. agents
Q("ag1", "arms", "An agent raises one arm vertically. Who must stop?", "Un agente levanta un brazo verticalmente. ¿Quién debe detenerse?",
  [("Everyone approaching the agent", "Todos los que se acerquen al agente"), ("Only those in front of the agent", "Solo los que están de frente"), ("Only pedestrians", "Solo los peatones")],
  "Except drivers who cannot stop safely.", "Salvo los que no puedan hacerlo con seguridad.")
Q("ag2", "arms", "You are already inside a junction when the agent raises an arm. You…", "Ya estás dentro de la intersección cuando el agente levanta el brazo. Tú…",
  [("may carry on and clear the junction", "puedes seguir y dejar libre la intersección"), ("must stop where you are", "debes detenerte donde estás"), ("must reverse", "debes dar marcha atrás")],
  "Those already inside need not stop.", "Los que ya están dentro no están obligados a detenerse.")
Q("ag3", "arms", "With an arm raised and no stop line, you stop…", "Con el brazo levantado y sin línea de detención, te detienes…",
  [("before the agent", "antes del agente"), ("beside the agent", "a la altura del agente"), ("after the agent", "pasado el agente")],
  "At a junction, before entering it.", "En una intersección, antes de entrar en ella.")
Q("ag4", "arms", "An agent holds both arms out sideways. Who must stop?", "Un agente tiene los brazos extendidos horizontalmente. ¿Quién se detiene?",
  [("Those coming from directions that cross the line of the arms", "Los que vengan de direcciones que corten la de los brazos"), ("Those moving parallel to the arms", "Los que circulan paralelos a los brazos"), ("Nobody", "Nadie")],
  "Those facing the agent’s front or back.", "Los que vienen de frente o por la espalda del agente.")
Q("ag5", "arms", "An agent moves an outstretched arm up and down. It means…", "Un agente mueve el brazo extendido arriba y abajo. Significa…",
  [("slow down, for drivers coming at right angles to the arm", "reducir la velocidad, para los que vienen perpendiculares al brazo"), ("stop", "detenerse"), ("speed up", "acelerar")],
  "It is the only arm signal that does not mean stop.", "Es la única de brazo que no obliga a parar.")
Q("ag6", "arms", "The agent stopped you with arms out sideways and then lowers them without moving. You…", "El agente te detuvo con los brazos extendidos y los baja sin cambiar de posición. Tú…",
  [("stay stopped", "sigues detenido"), ("move off", "reanudas la marcha"), ("turn right", "giras a la derecha")],
  "The order stays in force until it changes position or signal.", "La orden sigue mientras no cambie de posición o de señal.")
Q("ag7", "arms", "At night an agent swings a red light towards you. You…", "De noche un agente balancea una luz roja hacia ti. Tú…",
  [("stop", "te detienes"), ("slow down", "reduces"), ("flash your lights", "haces ráfagas")],
  "Those the light is aimed at must stop.", "Se detienen aquellos hacia los que dirige la luz.")
Q("ag8", "arms", "Do agents’ orders prevail over a STOP sign?", "¿Prevalecen las órdenes del agente sobre un STOP?",
  [("Yes, over all signs and rules", "Sí, sobre todas las señales y normas"), ("No", "No"), ("Only in town", "Solo en poblado")],
  "Even when they contradict them.", "Aunque estén en contradicción.")
Q("vh1", "agveh", "An agent blows a series of short, frequent whistle blasts. It means…", "Un agente da una serie de toques cortos y frecuentes de silbato. Significa…",
  [("stop", "detenerse"), ("move off", "reanudar la marcha"), ("slow down", "reducir")],
  "One long blast means move off.", "Un toque largo: reanudar.")
Q("vh2", "agveh", "One long whistle blast means…", "Un toque largo de silbato significa…",
  [("move off again", "reanudar la marcha"), ("stop", "detenerse"), ("pull over", "apartarse")],
  "Short frequent blasts mean stop.", "Los cortos y frecuentes: detenerse.")
Q("vh3", "agveh", "A vehicle with a red flag goes past you. From then on the road is…", "Pasa un vehículo con bandera roja. Desde ese momento la calzada…",
  [("temporarily closed, except for those escorted by agents", "queda cerrada temporalmente, salvo los escoltados por agentes"), ("open again", "queda abierta de nuevo"), ("one-way", "es de sentido único")],
  "The green flag reopens it.", "La bandera verde la reabre.")
Q("vh4", "agveh", "A yellow flag means…", "Una bandera amarilla significa…",
  [("take extreme care, a danger is near", "extremar la atención, peligro próximo"), ("road closed", "calzada cerrada"), ("road open", "calzada abierta")],
  "Also used by staff at cycle marches.", "También la usa el personal de marchas ciclistas.")
Q("vh5", "agveh", "A green flag carried by a vehicle means…", "Una bandera verde en un vehículo significa…",
  [("the road is open again after it passes", "tras su paso, la calzada queda de nuevo abierta"), ("speed up", "acelerar"), ("pull over", "apartarse")],
  "Red closed it.", "La roja la cerró.")
Q("vh6", "agveh", "A motorcycle agent holds an arm down, slanted and still, towards you. You must…", "Un agente en moto extiende el brazo hacia abajo, inclinado y fijo, hacia ti. Debes…",
  [("stop on the right", "detenerte en el lado derecho"), ("overtake him", "adelantarle"), ("slow down only", "solo reducir")],
  "It is a stop order from a vehicle.", "Es una orden de detención desde un vehículo.")
Q("vh7", "agveh", "The police car behind you flashes a red light forwards. You must stop…", "El coche policial detrás de ti emite una luz roja intermitente hacia delante. Debes detenerte…",
  [("on the right, ahead of the police car", "a la derecha, delante del vehículo policial"), ("behind the police car", "detrás del vehículo policial"), ("in the left lane", "en el carril izquierdo")],
  "Somewhere safe, and obey the loudspeaker.", "En un lugar seguro, y obedecer la megafonía.")
Q("vh8", "agveh", "Agents may also use…", "Los agentes también pueden usar…",
  [("any other clear indication when needed", "cualquier otra indicación clara si es necesario"), ("only arms and whistle", "solo brazos y silbato"), ("only the V-1 light", "solo la luz V-1")],
  "As long as it is clear.", "Siempre que sea clara.")
Q("hp1", "helpers", "On roadworks a worker shows you a STOP paddle. You…", "En unas obras un operario te muestra una paleta de STOP. Tú…",
  [("must stop", "debes detenerte"), ("may ignore it", "puedes ignorarla"), ("stop only if an agent is there", "solo paras si hay un agente")],
  "Drivers must obey their indications.", "Hay que obedecer sus indicaciones.")
Q("hp2", "helpers", "A school patrol may…", "Una patrulla escolar puede…",
  [("“invite” users to stop with a paddle", "«invitar» a detenerse con una paleta"), ("fine drivers", "multar"), ("direct traffic with a whistle", "dirigir el tráfico con silbato")],
  "Course wording: they “invite”.", "Expresión del curso: «invitar».")
Q("hp3", "helpers", "From how far must helpers be visible thanks to their clothing?", "¿A qué distancia deben ser visibles los auxiliares por su ropa?",
  [("At least 150 m", "Al menos 150 m"), ("At least 50 m", "Al menos 50 m"), ("At least 300 m", "Al menos 300 m")],
  "Bright colours and retroreflective elements.", "Colores llamativos y elementos retrorreflectantes.")
Q("hp4", "helpers", "Who else may regulate traffic?", "¿Quién más puede regular la circulación?",
  [("The Military Police", "La Policía Militar"), ("Any driver", "Cualquier conductor"), ("Taxi drivers", "Los taxistas")],
  "And enabled civil-protection or organisers’ staff at events.", "Y protección civil u organización habilitados en eventos.")
Q("hp5", "helpers", "Who may regulate traffic with a paddle where there are no agents?", "¿Quién puede regular con paleta si no hay agentes?",
  [("Roadworks staff and special-transport escorts", "El personal de obras y de acompañamiento de transportes especiales"), ("Any pedestrian", "Cualquier peatón"), ("Petrol station staff", "El personal de gasolineras")],
  "Drivers must obey them.", "Los conductores deben obedecerles.")

# ---------------------------------------------------------------- 3. temporary signs and beaconing
Q("ha1", "beacon", "A variable message sign may show at most…", "Un panel de mensaje variable puede mostrar como máximo…",
  [("two alternating messages", "dos mensajes alternados"), ("three messages", "tres mensajes"), ("one fixed message", "un mensaje fijo")],
  "Never more than two.", "Nunca más de dos.")
Q("ha2", "beacon", "Can a variable message sign give compulsory instructions?", "¿Puede un panel de mensaje variable dar instrucciones obligatorias?",
  [("Yes", "Sí"), ("No, only advice", "No, solo recomendaciones"), ("Only about weather", "Solo sobre el tiempo")],
  "It informs, warns, recommends or orders.", "Informa, advierte, recomienda u ordena.")
Q("ha3", "beacon", "A line of cones narrows the carriageway. You may…", "Una hilera de conos estrecha la calzada. Puedes…",
  [("not cross the line joining them", "no atravesar la línea que los une"), ("pass between them carefully", "pasar entre ellos con cuidado"), ("cross only at night", "cruzarla solo de noche")],
  "The line can be real or imaginary.", "La línea puede ser real o imaginaria.")
Q("ha4", "beacon", "A steady red light on a barrier means…", "Una luz roja fija sobre una barrera significa…",
  [("the carriageway is completely closed", "la calzada está totalmente cerrada"), ("slow down", "reducir la velocidad"), ("roadworks ahead", "obras más adelante")],
  "Yellow lights forbid crossing the line between them.", "Las amarillas prohíben cruzar la línea entre ellas.")
Q("ha5", "beacon", "The level-crossing barrier is moving. You…", "La barrera del paso a nivel está en movimiento. Tú…",
  [("stop in your lane, one behind another", "te detienes en tu carril, uno detrás de otro"), ("cross quickly", "cruzas rápido"), ("overtake the queue", "adelantas a la fila")],
  "Wait until the way is clear.", "Hasta tener paso libre.")
Q("ha6", "beacon", "A temporary panel with red and white chevrons…", "Un panel provisional con chevrones rojos y blancos…",
  [("forbids passing and shows the direction", "prohíbe el paso e indica el sentido"), ("only warns of a bend", "solo advierte de una curva"), ("marks a parking area", "marca un aparcamiento")],
  "It is a delimiting device.", "Es un dispositivo delimitador.")
Q("ha7", "beacon", "Variable message changes end…", "Las modificaciones de un panel variable terminan…",
  [("when the panel says so or the causes end", "cuando lo diga el panel o cesen sus causas"), ("after 1 km", "tras 1 km"), ("at the next junction", "en la próxima intersección")],
  "Until then they apply.", "Hasta entonces rigen.")
Q("gd1", "guide", "What does a gore marker (hito de vértice) show?", "¿Qué indica un hito de vértice?",
  [("Where two traffic streams separate", "Dónde se separan dos corrientes de tráfico"), ("The kilometre point", "El punto kilométrico"), ("A bus stop", "Una parada de autobús")],
  "Half-cylinder with two opposed triangles.", "Semicilíndrico con dos triángulos opuestos.")
Q("gd2", "guide", "A triple permanent direction panel means a danger that is…", "Un panel direccional permanente triple indica un peligro…",
  [("high", "elevado"), ("moderate", "moderado"), ("medium", "medio")],
  "Single moderate, double medium, triple high.", "Sencillo moderado, doble medio, triple elevado.")
Q("gd3", "guide", "Edge posts and reflectors on the LEFT of the road are…", "Los hitos de arista y captafaros a la IZQUIERDA son…",
  [("white", "blancos"), ("yellow", "amarillos"), ("red", "rojos")],
  "On the right: white or yellow.", "A la derecha: blancos o amarillos.")
Q("gd4", "guide", "Luminous road studs may be crossed when they are…", "Los captafaros horizontales luminosos se pueden franquear cuando están en…",
  [("green", "verde"), ("orange", "naranja"), ("red", "rojo")],
  "They can be green, orange or red.", "Pueden ser verdes, naranjas o rojos.")
Q("gd5", "guide", "You may cross the line joining cylindrical bollards…", "Se puede atravesar la línea que une las balizas cilíndricas…",
  [("never", "nunca"), ("if it is imaginary", "si es imaginaria"), ("to overtake", "para adelantar")],
  "Imaginary or not, it is forbidden.", "Imaginaria o no, está prohibido.")
Q("gd6", "guide", "In fog-beacon systems, a steady red light shows…", "En el balizamiento luminoso de niebla, la luz roja fija indica…",
  [("a vehicle passing", "el paso de un vehículo"), ("the road edge", "el borde de la vía"), ("an exit", "una salida")],
  "Amber shows the direction and the edge.", "El ámbar indica sentido y borde.")
Q("gd7", "guide", "Rumble strips warn you of…", "Las guías sonoras longitudinales avisan de…",
  [("drifting off course", "desvíos involuntarios de la trayectoria"), ("a speed camera", "un radar"), ("a junction", "una intersección")],
  "Through vibration and/or noise.", "Mediante vibración y/o sonido.")
Q("gd8", "guide", "Parapets (pretiles) protect against…", "Los pretiles protegen frente a…",
  [("falling off bridges and walls", "salidas de la vía con caída en puentes y muros"), ("rear-end crashes", "alcances"), ("wild animals", "animales")],
  "Crash cushions are used at forks.", "Los atenuadores se usan en bifurcaciones.")
Q("gd9", "guide", "A height-control gantry…", "Un pórtico de control de gálibo…",
  [("warns or stops vehicles too tall for the structure ahead", "advierte o impide el paso a vehículos que superan la altura de la estructura siguiente"), ("checks speed", "controla la velocidad"), ("marks a toll", "señala un peaje")],
  "Bridge, overpass or tunnel.", "Puente, paso superior o túnel.")
Q("gd10", "guide", "A windsock beside the road…", "Una manga de viento junto a la vía…",
  [("adds to the crosswind sign: shows wind direction and strength", "complementa la señal de viento transversal: sentido e intensidad"), ("replaces the crosswind sign", "sustituye a la señal de viento transversal"), ("marks an airport", "indica un aeropuerto")],
  "Steady or gusty wind.", "Viento continuo o racheado.")

# ---------------------------------------------------------------- 4. traffic lights
Q("tl1", "tlights", "The pedestrian green figure starts flashing. It means…", "La figura verde de peatones empieza a parpadear. Significa…",
  [("time to finish crossing is running out", "se acaba el tiempo para terminar de cruzar"), ("start crossing now", "empezar a cruzar ya"), ("vehicles may go", "pueden pasar los vehículos")],
  "Red will come on next.", "Después se encenderá la roja.")
Q("tl2", "tlights", "A steady red standing figure tells pedestrians…", "Una figura roja fija de peatón inmóvil indica a los peatones…",
  [("not to start crossing", "que no deben comenzar a cruzar"), ("to run", "que corran"), ("to cross with care", "que crucen con precaución")],
  "Those already crossing finish.", "Quien ya está cruzando termina.")
Q("tl3", "tlights", "Your light is green but the junction ahead is jammed. You…", "Tu semáforo está verde, pero la intersección está atascada. Tú…",
  [("wait, so as not to block it", "esperas para no bloquearla"), ("enter: green gives priority", "entras: el verde da prioridad"), ("sound the horn", "tocas el claxon")],
  "Green does not allow blocking cross traffic.", "El verde no permite obstruir la circulación transversal.")
Q("tl4", "tlights", "The light turns amber when you are so close you cannot stop safely. You…", "El semáforo pasa a amarillo cuando estás tan cerca que no puedes parar con seguridad. Tú…",
  [("may continue", "puedes continuar"), ("must brake hard anyway", "debes frenar en seco igualmente"), ("must reverse", "debes dar marcha atrás")],
  "Otherwise steady amber means stop.", "Si no, el amarillo fijo obliga a detenerse.")
Q("tl5", "tlights", "The red light is on the far side of the junction. Where do you stop?", "El semáforo rojo está al otro lado de la intersección. ¿Dónde te detienes?",
  [("Before entering the junction", "Antes de entrar en la intersección"), ("Right under the light", "Justo debajo del semáforo"), ("In the middle of the junction", "En medio de la intersección")],
  "Do not cross the stop line before it.", "Sin rebasar la línea de detención anterior.")
Q("tl6", "tlights", "A steady amber light means…", "Una luz amarilla fija significa…",
  [("stop as for red, unless you cannot do so safely", "detenerse como en rojo, salvo que no puedas con seguridad"), ("speed up", "acelerar"), ("take care and give way", "precaución y ceder el paso")],
  "That last one is the flashing amber.", "Eso último es el ámbar intermitente.")
Q("tl7", "tlights", "What is the main job of traffic lights?", "¿Cuál es la misión principal de los semáforos?",
  [("To regulate who goes first", "Regular la prioridad de paso"), ("To limit speed", "Limitar la velocidad"), ("To light junctions", "Iluminar los cruces")],
  "They allocate priority.", "Asignan la prioridad.")
Q("tl8", "tlights", "With a steady red light you must stop…", "Con luz roja fija debes detenerte…",
  [("without passing the light or the nearest stop line before it", "sin rebasar el semáforo ni la línea de detención más próxima"), ("10 m before the light", "10 m antes del semáforo"), ("after the light", "pasado el semáforo")],
  "Red forbids passing.", "La roja prohíbe el paso.")
Q("fl1", "tlflash", "Two red lights flash alternately before a level crossing. They mean…", "Dos luces rojas intermitentes alternas antes de un paso a nivel significan…",
  [("no passing for now", "prohibido temporalmente el paso"), ("cross with care", "cruzar con precaución"), ("the train has gone", "el tren ya pasó")],
  "Also at fire-engine exits and low aircraft.", "También en salidas de bomberos y aeronaves.")
Q("fl2", "tlflash", "A flashing amber light means…", "Una luz amarilla intermitente significa…",
  [("take extreme care and give way if appropriate", "extremar la precaución y, en su caso, ceder el paso"), ("stop", "detenerse"), ("no passing", "prohibido el paso")],
  "It does not cancel other stop signs.", "No exime de otras señales de detención.")
Q("fl3", "tlflash", "A flashing amber light hangs above a STOP sign. You…", "Hay un ámbar intermitente sobre una señal de STOP. Tú…",
  [("stop at the STOP", "te detienes en el STOP"), ("only slow down", "solo reduces"), ("go: the light comes first", "pasas: el semáforo es prioritario")],
  "Flashing amber does not exempt you from other stop signs.", "El ámbar intermitente no exime de otras señales de detención.")
Q("fl4", "tlflash", "A green arrow is lit beside a red light. You may go that way…", "Una flecha verde está encendida junto a la luz roja. Puedes ir en esa dirección…",
  [("with care, giving way to the lane you join and to pedestrians", "con precaución, cediendo al carril al que te incorporas y a los peatones"), ("with priority over everyone", "con prioridad sobre todos"), ("only when red goes off", "solo cuando se apague la roja")],
  "Whatever else is lit.", "Cualquiera que sea la otra luz.")
Q("fl5", "tlflash", "You are in the lane others need for the green arrow, and it lights up. You…", "Estás en el carril que necesitan otros para la flecha verde y se enciende. Tú…",
  [("must move off in the arrow’s direction if yours is not possible", "debes avanzar en el sentido de la flecha si el tuyo no es posible"), ("stay put", "te quedas quieto"), ("reverse", "das marcha atrás")],
  "Even if it was not your intended direction.", "Aunque no fuera la dirección deseada.")
Q("fl6", "tlflash", "A black arrow on a red light…", "Una flecha negra sobre una luz roja…",
  [("limits the red to the movement of the arrow", "limita la roja al movimiento de la flecha"), ("lets you go that way", "permite ir en esa dirección"), ("means the light is broken", "indica que está averiado")],
  "Steady or flashing.", "Fija o intermitente.")
Q("fl7", "tlflash", "Where are flashing red lights typically found?", "¿Dónde suelen estar las luces rojas intermitentes?",
  [("Before level crossings and near fire-station exits", "Antes de pasos a nivel y cerca de salidas de bomberos"), ("At every junction", "En todos los cruces"), ("At school gates", "En las puertas de colegios")],
  "Also movable bridges, ferries, low aircraft.", "También puentes móviles, transbordadores, aeronaves.")
Q("ln1", "tllane", "A green arrow pointing down over your lane means…", "Una flecha verde hacia abajo sobre tu carril significa…",
  [("you may use that lane", "puedes circular por ese carril"), ("the lane ends", "el carril termina"), ("you have priority at every junction", "tienes prioridad en todos los cruces")],
  "It does not exempt you from red lights or stop signs.", "No exime de luces rojas ni señales de detención.")
Q("ln2", "tllane", "A red cross lights over your lane. You must…", "Se enciende un aspa roja sobre tu carril. Debes…",
  [("leave the lane as soon as possible", "abandonarlo en el tiempo más breve posible"), ("stop at once", "detenerte inmediatamente"), ("speed up", "acelerar")],
  "Occupying it is forbidden.", "Está prohibido ocuparlo.")
Q("ln3", "tllane", "A yellow arrow pointing down at an angle over your lane means…", "Una flecha amarilla oblicua hacia abajo sobre tu carril significa…",
  [("move safely into the lane it points to: yours is closing", "incorporarse con seguridad al carril que señala: el tuyo se cierra"), ("turn off at the next exit", "salir en la próxima salida"), ("overtake", "adelantar")],
  "Steady or flashing; white or yellow.", "Fija o intermitente; blanca o amarilla.")
Q("ln4", "tllane", "Lights with a white bar on a black lens apply to…", "Los semáforos con franja blanca sobre fondo negro afectan a…",
  [("trams and regular-line buses (or all users of a reserved lane)", "tranvías y autobuses de líneas regulares (o a todos los del carril reservado)"), ("all vehicles", "todos los vehículos"), ("cyclists", "ciclistas")],
  "Cars outside the bus lane ignore them.", "Los turismos fuera del carril bus no.")
Q("ln5", "tllane", "On a bus light, a horizontal white bar means…", "En un semáforo de autobús, una franja blanca horizontal significa…",
  [("no passing", "prohibido el paso"), ("straight on", "paso de frente"), ("turn left", "girar a la izquierda")],
  "Vertical = straight on; slanted = turn.", "Vertical = de frente; inclinada = giro.")
Q("ln6", "tllane", "If the white bar flashes, the bus must…", "Si la franja blanca es intermitente, el autobús debe…",
  [("stop as for a steady amber", "detenerse como ante un ámbar fijo"), ("go on with priority", "seguir con prioridad"), ("stop always", "detenerse siempre")],
  "Same conditions as steady amber.", "Mismas condiciones que el amarillo fijo.")
Q("ln7", "tllane", "Lights showing a bicycle apply to…", "Los semáforos con silueta de bicicleta afectan a…",
  [("cycles only", "solo a los ciclos"), ("cycles and mopeds", "ciclos y ciclomotores"), ("everyone", "todos")],
  "Exclusively cycles.", "Exclusivamente a los ciclos.")

# ---------------------------------------------------------------- 5. warning signs
Q("wn1", "warn", "What do red-bordered triangles warn of?", "¿De qué avisan los triángulos con borde rojo?",
  [("A danger that is hard to see in time", "De un peligro difícil de percibir a tiempo"), ("A prohibition", "De una prohibición"), ("A service", "De un servicio")],
  "A panel can add the distance or the length.", "Un panel puede añadir distancia o longitud.")
Q("wn2", "warn", "Sign P-1 (thick vertical bar crossed by a thin one) means…", "La señal P-1 (barra vertical gruesa cruzada por otra fina) indica…",
  [("a junction where the side road gives way to you", "una intersección donde la vía lateral te cede el paso"), ("a junction with priority to the right", "una intersección con prioridad de la derecha"), ("a crossroads with lights", "un cruce con semáforos")],
  "The thick bar is your road.", "La barra gruesa es tu vía.")
Q("wn3", "warn", "Sign P-2 (an X in a triangle) means…", "La señal P-2 (una X en un triángulo) indica…",
  [("a junction where the priority-to-the-right rule applies", "una intersección donde rige la prioridad de la derecha"), ("a level crossing", "un paso a nivel"), ("no entry", "entrada prohibida")],
  "The general priority rule.", "La regla general de prioridad.")
Q("wn4", "warn", "On P-1c (merge from the right with priority), you should…", "Con la P-1c (incorporación por la derecha con prioridad) debes…",
  [("keep priority but make the merge easier where possible", "mantener la prioridad pero facilitar la incorporación si es posible"), ("give way to the merging traffic", "ceder el paso a los que se incorporan"), ("stop", "detenerte")],
  "They give way, you help.", "Ellos ceden, tú facilitas.")
Q("wn5", "warn", "A pair of posts with two red stripes each before a level crossing means it is about…", "Un par de balizas con dos franjas rojas cada una antes de un paso a nivel indica que está a unos…",
  [("150 m away", "150 m"), ("200 m away", "200 m"), ("100 m away", "100 m")],
  "3 stripes 200 m, 2 = 150 m, 1 = 100 m.", "3 franjas 200 m, 2 = 150 m, 1 = 100 m.")
Q("wn6", "warn", "Countdown posts (P-9/P-10) always go with sign…", "Las balizas P-9/P-10 van siempre acompañadas de la señal…",
  [("P-5, P-7, P-8 or P-27", "P-5, P-7, P-8 o P-27"), ("R-2", "R-2"), ("P-50", "P-50")],
  "Movable bridge, level crossings or quay.", "Puente móvil, pasos a nivel o muelle.")
Q("wn7", "warn", "Sign P-14a warns of…", "La señal P-14a advierte de…",
  [("a series of bends, the first to the right", "curvas peligrosas, la primera hacia la derecha"), ("a single bend to the right", "una curva a la derecha"), ("a series of bends, the first to the left", "curvas, la primera a la izquierda")],
  "P-13: a single bend.", "P-13: una sola curva.")
Q("wn8", "warn", "The crosswind sign (P-29) tells you…", "La señal de viento transversal (P-29) te indica…",
  [("that strong crosswinds are frequent, not from which side", "que sopla con frecuencia viento fuerte, pero no de qué lado"), ("the wind comes from the right", "que el viento viene de la derecha"), ("the wind speed", "la velocidad del viento")],
  "It does not show the side.", "No indica el lado.")
Q("wn9", "warn", "Sign P-17 (road narrows) is NOT used when…", "La señal P-17 (estrechamiento) NO se usa cuando…",
  [("after losing a lane, the other lanes and shoulders keep their width", "tras perder un carril, los demás y los arcenes no varían su anchura"), ("the shoulders get narrower", "los arcenes se estrechan"), ("the carriageway narrows", "la calzada se estrecha")],
  "It can also be used for narrower shoulders.", "Puede usarse para arcenes más estrechos.")
Q("wn10", "warn", "Sign P-35 “Trenzado” warns of…", "La señal P-35 «Trenzado» advierte de…",
  [("a stretch between a merge and a fork where paths cross", "un tramo entre confluencia y bifurcación con trayectorias cruzadas"), ("a narrow bridge", "un puente estrecho"), ("cyclists", "ciclistas")],
  "Lane changes cross each other: collision risk.", "Cambios de carril cruzados: riesgo de colisión.")
Q("wn11", "warn", "On sign P-16a the figure “10%” is…", "En la señal P-16a la cifra «10%» indica…",
  [("the gradient of the descent", "la inclinación de la bajada"), ("the speed reduction", "la reducción de velocidad"), ("the length in km", "la longitud en km")],
  "P-16b is the ascent.", "La P-16b es la subida.")
Q("wn12", "warn", "Sign P-6 (tram) warns of a tram crossing where…", "La señal P-6 (tranvía) avisa de un cruce donde…",
  [("the tram has priority", "el tranvía tiene prioridad"), ("you have priority", "tú tienes prioridad"), ("the priority-to-the-right rule applies", "rige la prioridad de la derecha")],
  "It is also a priority sign.", "También es señal de prioridad.")
Q("wn13", "warn", "Sign P-15 (uneven road) warns of…", "La señal P-15 (perfil irregular) advierte de…",
  [("a bump or dip or a road in poor condition", "un resalte, un badén o pavimento en mal estado"), ("a steep slope", "una fuerte pendiente"), ("falling rocks", "desprendimientos")],
  "P-15a bump, P-15b dip.", "P-15a resalte, P-15b badén.")
Q("wn14", "warn", "Which warning sign has a yellow background?", "¿Qué señal de peligro tiene fondo amarillo?",
  [("P-18 roadworks", "P-18 obras"), ("P-50 other dangers", "P-50 otros peligros"), ("P-19 slippery road", "P-19 pavimento deslizante")],
  "Roadworks.", "Obras.")
Q("wn15", "warn", "Sign P-24a shows a wild boar. It warns of…", "La señal P-24a muestra un jabalí. Advierte de…",
  [("wild animals crossing, many of them wild boar", "paso de animales en libertad, en gran parte jabalíes"), ("a hunting reserve", "un coto de caza"), ("farm animals", "ganado doméstico")],
  "P-23 is for domestic animals.", "La P-23 es para animales domésticos.")
Q("wn16", "warn", "Sign P-11 (red and white cross) shows…", "La señal P-11 (aspa roja y blanca) indica…",
  [("an unbarriered level crossing right there", "la presencia inmediata de un paso a nivel sin barreras"), ("a level crossing 200 m ahead", "un paso a nivel a 200 m"), ("a junction", "una intersección")],
  "P-11a: more than one track.", "P-11a: más de una vía.")

# ---------------------------------------------------------------- 6. regulatory signs
Q("pr1", "prio", "With a STOP sign and no stop line, you stop…", "Con STOP y sin línea de detención, te detienes…",
  [("immediately before the junction", "inmediatamente antes de la intersección"), ("next to the sign", "junto a la señal"), ("in the middle of the junction", "en mitad de la intersección")],
  "Then give way.", "Y cedes el paso.")
Q("pr2", "prio", "You stopped at the STOP line but still cannot see. You…", "Te detuviste en la línea del STOP pero no ves bien. Tú…",
  [("move forward and stop again where you can see", "avanzas y te detienes de nuevo donde haya visibilidad"), ("go on: you already stopped", "sigues: ya paraste"), ("sound the horn and go", "pitas y pasas")],
  "Without endangering anyone.", "Sin poner en peligro a nadie.")
Q("pr3", "prio", "A round sign with a red border shows a black arrow down and a red arrow up. You must…", "Una señal redonda con borde rojo muestra una flecha negra hacia abajo y una roja hacia arriba. Debes…",
  [("give way to oncoming traffic in the narrow passage", "ceder el paso a los que vienen en sentido contrario en el paso estrecho"), ("go first", "pasar primero"), ("turn round", "dar la vuelta")],
  "That is R-5; R-6 (blue square) gives you priority.", "Es la R-5; la R-6 (azul) te da prioridad.")
Q("pr4", "prio", "Sign R-6 (blue square, white arrow up) tells you…", "La señal R-6 (cuadrado azul, flecha blanca arriba) te indica…",
  [("you have priority over oncoming traffic in the narrow passage", "tienes prioridad sobre los que vienen en el paso estrecho"), ("give way to oncoming traffic", "cede el paso a los que vienen"), ("one-way road", "calzada de sentido único")],
  "Your arrow is the big white one.", "Tu flecha es la blanca grande.")
Q("pr5", "prio", "Sign R-4 (yellow diamond with a black band) means…", "La señal R-4 (rombo amarillo con franja negra) significa…",
  [("end of priority", "fin de prioridad"), ("priority road", "calzada con prioridad"), ("give way", "ceda el paso")],
  "R-3 is the priority road.", "La R-3 es calzada con prioridad.")
Q("pr6", "prio", "Which of these warning signs is also a priority sign?", "¿Cuál de estas señales de peligro es también de prioridad?",
  [("P-8 level crossing without barriers", "P-8 paso a nivel sin barreras"), ("P-13a bend", "P-13a curva"), ("P-19 slippery", "P-19 deslizante")],
  "P-1 to P-1e, P-2, P-6, P-7, P-8.", "P-1 a P-1e, P-2, P-6, P-7, P-8.")
Q("pr7", "prio", "From where does a regulatory sign apply?", "¿Desde dónde rige una señal de reglamentación?",
  [("From the point where it stands, unless a panel gives a distance", "Desde donde está, salvo que un panel indique distancia"), ("100 m after it", "100 m después"), ("From the next junction", "Desde la próxima intersección")],
  "The panel goes below the sign.", "El panel va debajo de la señal.")
Q("pr8", "prio", "A 40 km/h sign stands on the same post as the town-name sign. It applies…", "Una señal de 40 km/h está en el mismo poste que la de nombre del poblado. Rige…",
  [("in the whole town, unless other signs say otherwise", "en todo el poblado, salvo otras señales"), ("only for 100 m", "solo 100 m"), ("only on the travesía", "solo en la travesía")],
  "Before or after the town sign: only the travesía.", "Antes o después de la de poblado: solo la travesía.")
Q("pr9", "prio", "The give-way sign (R-1) obliges you to give way…", "La señal de ceda el paso (R-1) obliga a ceder…",
  [("at the next junction to vehicles on the road you approach", "en la próxima intersección a los vehículos de la vía a la que te aproximas"), ("to everyone for 1 km", "a todos durante 1 km"), ("only to pedestrians", "solo a peatones")],
  "Or to the lane you want to join.", "O al carril al que te incorporas.")
Q("ne1", "noentry", "Sign R-100 (red ring, white centre) forbids…", "La señal R-100 (borde rojo, centro blanco) prohíbe…",
  [("all vehicles in both directions", "la circulación de todo vehículo en ambos sentidos"), ("entry in your direction only", "la entrada solo en tu sentido"), ("parking", "estacionar")],
  "R-101 is no entry for your direction.", "R-101 es entrada prohibida.")
Q("ne2", "noentry", "Sign R-103 (car in a red ring) lets in…", "La señal R-103 (turismo en borde rojo) permite la entrada a…",
  [("two-wheeled motorcycles", "motocicletas de dos ruedas"), ("cars with trailers", "turismos con remolque"), ("no motor vehicle", "ningún vehículo de motor")],
  "R-102 bans all motor vehicles.", "La R-102 prohíbe todos los de motor.")
Q("ne3", "noentry", "Sign R-105 (moped) also forbids…", "La señal R-105 (ciclomotor) prohíbe también…",
  [("vehicles for people with reduced mobility", "los vehículos para personas de movilidad reducida"), ("bicycles", "las bicicletas"), ("motorcycles", "las motocicletas")],
  "As the course says.", "Según el curso.")
Q("ne4", "noentry", "An empty lorry of 12 t MMA meets an R-107 sign showing 5.5 t. It…", "Un camión vacío de 12 t de MMA encuentra una R-107 de 5,5 t. Él…",
  [("may not enter, even empty", "no puede entrar, aunque vaya vacío"), ("may enter: it is empty", "puede entrar: va vacío"), ("may enter at 30 km/h", "puede entrar a 30 km/h")],
  "R-107 looks at the maximum authorised mass.", "La R-107 se fija en la masa máxima autorizada.")
Q("ne5", "noentry", "Sign R-201 “5,5t” forbids vehicles whose…", "La señal R-201 «5,5t» prohíbe el paso a vehículos cuya…",
  [("actual laden mass is over 5.5 t", "masa en carga supere 5,5 t"), ("MMA is over 5.5 t even empty", "MMA supere 5,5 t aunque vayan vacíos"), ("axle mass is over 5.5 t", "masa por eje supere 5,5 t")],
  "R-202 is per axle.", "La R-202 es por eje.")
Q("ne6", "noentry", "Height limit R-205 counts…", "La limitación de altura R-205 cuenta…",
  [("the vehicle with its load", "el vehículo incluida la carga"), ("the vehicle without load", "el vehículo sin carga"), ("only the cab", "solo la cabina")],
  "Same for length and width.", "Igual longitud y anchura.")
Q("ne7", "noentry", "Sign R-200 (red ring, black bar) means…", "La señal R-200 (borde rojo, barra negra) significa…",
  [("no passing without stopping (customs, police, toll…)", "prohibido pasar sin detenerse (aduana, policía, peaje…)"), ("no entry", "entrada prohibida"), ("end of prohibitions", "fin de prohibiciones")],
  "You go on only after doing what it requires.", "Solo se reanuda tras cumplir lo que establece.")
Q("ne8", "noentry", "Sign R-110 bans vehicles carrying water pollutants of…", "La señal R-110 prohíbe vehículos con contaminantes del agua de…",
  [("more than 1,000 litres", "más de 1.000 litros"), ("any amount", "cualquier cantidad"), ("more than 500 litres", "más de 500 litros")],
  "R-415 is the matching obligation.", "La R-415 es la obligación equivalente.")
Q("ne9", "noentry", "Sign R-120 restricts entry according to…", "La señal R-120 restringe la entrada según…",
  [("the vehicle’s environmental label", "el distintivo ambiental del vehículo"), ("the vehicle’s age only", "solo la antigüedad"), ("the number of passengers", "el número de ocupantes")],
  "Conditions on an S-860 panel or placard.", "Condiciones en un panel S-860 o cartel.")
Q("ne10", "noentry", "No-entry signs bind the users who…", "Las señales de prohibición de entrada afectan a los usuarios que…",
  [("meet them head-on in their direction of travel", "se las encuentren de frente en el sentido de su marcha"), ("see them in the mirror", "las vean por el retrovisor"), ("live in the street", "residan en la calle")],
  "From where they stand.", "Desde donde estén.")
Q("ne11", "noentry", "Sign R-112 with “2t” on the trailer bans…", "La señal R-112 con «2t» en el remolque prohíbe…",
  [("vehicles towing a trailer whose maximum mass is over 2 t (except single-axle)", "vehículos con remolque de MMA superior a 2 t (salvo de un eje)"), ("all trailers", "todos los remolques"), ("vehicles over 2 t", "vehículos de más de 2 t")],
  "Single-axle trailers are excepted.", "Se exceptúan los de un solo eje.")
Q("ot1", "other", "Sign R-300 “70 m” obliges you to…", "La señal R-300 «70 m» obliga a…",
  [("keep at least 70 m from the vehicle ahead, except to overtake", "mantener al menos 70 m con el precedente, salvo para adelantar"), ("drive at 70 km/h", "circular a 70 km/h"), ("stop in 70 m", "detenerse en 70 m")],
  "Without a figure it is a general reminder.", "Sin cifra es un recordatorio genérico.")
Q("ot2", "other", "A speed limit sign is on the same post as a bend warning. The limit ends…", "Una limitación de velocidad está en el mismo poste que una señal de curva. La limitación termina…",
  [("when the danger ends", "cuando termina el peligro"), ("at the next junction", "en la próxima intersección"), ("only with an end sign", "solo con una señal de fin")],
  "Otherwise it lasts until an end sign or another limit.", "Si no, hasta su fin u otra limitación.")
Q("ot3", "other", "A speed limit on a road without priority stops applying…", "Una limitación en una vía sin prioridad deja de regir…",
  [("after a junction with a priority road", "al salir de una intersección con una vía con prioridad"), ("after 1 km", "tras 1 km"), ("never", "nunca")],
  "Unless repeated.", "Salvo que se repita.")
Q("ot4", "other", "Sign R-303 (no left turn) also forbids…", "La señal R-303 (giro a la izquierda prohibido) prohíbe también…",
  [("U-turns", "el cambio de sentido"), ("overtaking", "adelantar"), ("parking", "estacionar")],
  "R-304 (no U-turn) still allows turning.", "La R-304 (media vuelta) permite girar.")
Q("ot5", "other", "Sign R-304 (no U-turn)…", "La señal R-304 (media vuelta prohibida)…",
  [("allows you to turn left", "permite girar a la izquierda"), ("forbids turning left", "prohíbe girar a la izquierda"), ("forbids all turns", "prohíbe todos los giros")],
  "Only the change of direction of travel is banned.", "Solo prohíbe el cambio de sentido.")
Q("ot6", "other", "Sign R-305 forbids overtaking motor vehicles…", "La señal R-305 prohíbe adelantar a vehículos de motor…",
  [("when it means using the oncoming side", "cuando implique invadir el sentido contrario"), ("always", "siempre"), ("only at night", "solo de noche")],
  "Until “end of no overtaking” or “end of prohibitions”.", "Hasta su fin o «Fin de prohibiciones».")
Q("ot7", "other", "Sign R-306 applies to lorries with an MMA over…", "La señal R-306 afecta a camiones de MMA superior a…",
  [("3,500 kg", "3.500 kg"), ("7,500 kg", "7.500 kg"), ("12,000 kg", "12.000 kg")],
  "Even if overtaking does not invade the oncoming side.", "Aunque no invadan el sentido contrario.")
Q("ot8", "other", "Sign R-308 (blue disc, one red diagonal) means…", "La señal R-308 (fondo azul, una diagonal roja) significa…",
  [("no parking, stopping allowed", "estacionamiento prohibido, parada permitida"), ("no stopping or parking", "parada y estacionamiento prohibidos"), ("parking for residents", "estacionamiento para residentes")],
  "R-307 (red X) bans stopping too.", "La R-307 (aspa) prohíbe también parar.")
Q("ot9", "other", "Sign R-308c (“1-15”) forbids parking…", "La señal R-308c («1-15») prohíbe estacionar…",
  [("from 9:00 on day 1 to 9:00 on day 16", "desde las 9 h del día 1 hasta las 9 h del día 16"), ("from 0:00 day 1 to 24:00 day 15", "de las 0 h del día 1 a las 24 h del día 15"), ("on odd days", "los días impares")],
  "R-308d: from 9:00 day 16 to 9:00 day 1.", "R-308d: de las 9 h del día 16 a las 9 h del día 1.")
Q("ot10", "other", "Unless shown otherwise, a no-parking sign applies…", "Salvo indicación, una señal de estacionamiento prohibido rige…",
  [("on its side of the road, from the sign to the next junction", "en su lado de la calzada, desde la señal hasta la intersección más próxima"), ("on both sides for 100 m", "en ambos lados 100 m"), ("in the whole street", "en toda la calle")],
  "Panels S-820/S-830 can change it.", "Los paneles S-820/S-830 pueden variarlo.")
Q("ot11", "other", "In a zone signed R-309 (limited parking) you must…", "En una zona R-309 (estacionamiento limitado) debes…",
  [("show the time you parked as required", "indicar de forma reglamentaria la hora de comienzo"), ("leave the engine running", "dejar el motor en marcha"), ("park only on even days", "estacionar solo días pares")],
  "It may also say whether you pay.", "Puede indicar si es de pago.")
Q("ot12", "other", "Sign R-310 (no horn) allows the horn…", "La señal R-310 (advertencias acústicas prohibidas) permite el claxon…",
  [("only to avoid an accident", "solo para evitar un accidente"), ("to greet people", "para saludar"), ("before overtaking", "antes de adelantar")],
  "It reminds the general prohibition.", "Recuerda la prohibición general.")
Q("ob1", "oblig", "Sign R-403 (only directions allowed)…", "La señal R-403 (únicas direcciones permitidas)…",
  [("does not allow U-turns", "no permite cambiar de sentido"), ("allows U-turns", "permite cambiar de sentido"), ("is only advice", "es solo una recomendación")],
  "Only the arrows shown.", "Solo las flechas indicadas.")
Q("ob2", "oblig", "A blue round sign with a bicycle (R-407a) means…", "Una señal azul redonda con bicicleta (R-407a) significa…",
  [("compulsory for cycles and forbidden for others", "obligatoria para ciclos y prohibida para los demás"), ("cycles may use it", "los ciclos pueden usarla"), ("no cycles", "prohibido a ciclos")],
  "R-114 (red ring) bans cycles.", "La R-114 (borde rojo) prohíbe los ciclos.")
Q("ob3", "oblig", "Sign R-411 “40” (blue) obliges you to…", "La señal R-411 «40» (azul) obliga a…",
  [("drive at least at 40 km/h", "circular al menos a 40 km/h"), ("not exceed 40 km/h", "no superar 40 km/h"), ("keep 40 m", "guardar 40 m")],
  "Until an end sign or a lower or equal maximum.", "Hasta su fin o una velocidad máxima igual o inferior.")
Q("ob4", "oblig", "With sign R-412 (chains) you need chains on…", "Con la señal R-412 (cadenas) necesitas cadenas en…",
  [("at least one wheel on each side of the same drive axle", "al menos una rueda a cada lado del mismo eje motor"), ("all four wheels", "las cuatro ruedas"), ("the front wheels only", "solo las delanteras")],
  "Or special snow tyres.", "O neumáticos especiales de nieve.")
Q("ob5", "oblig", "Sign R-413 obliges you to…", "La señal R-413 obliga a…",
  [("use at least dipped headlights", "llevar al menos la luz de corto alcance"), ("use fog lights", "llevar la antiniebla"), ("switch lights off", "apagar las luces")],
  "Whatever the visibility.", "Con independencia de la visibilidad.")
Q("ob6", "oblig", "Sign R-500 (white disc, black diagonal stripes) means…", "La señal R-500 (disco blanco con franjas negras) significa…",
  [("end of all specific prohibitions for moving vehicles", "fin de todas las prohibiciones específicas para vehículos en movimiento"), ("no entry", "entrada prohibida"), ("end of motorway", "fin de autopista")],
  "End of speed limits, overtaking bans…", "Fin de limitaciones, prohibición de adelantar…")
Q("ob7", "oblig", "Sign R-422 obliges cyclists to…", "La señal R-422 obliga a los ciclistas a…",
  [("dismount and continue on foot", "desmontar y continuar a pie"), ("use the cycle lane", "usar el carril bici"), ("ride single file", "ir en fila de uno")],
  "A panel may limit it to certain times.", "Un panel puede limitarla a ciertos periodos.")
Q("ob8", "oblig", "Sign R-406 (blue, lorry) without a tonnage applies to goods vehicles…", "La señal R-406 (azul, camión) sin tonelaje afecta a vehículos de mercancías…",
  [("whatever their mass", "independientemente de su masa"), ("over 3,500 kg", "de más de 3.500 kg"), ("only when loaded", "solo cargados")],
  "With a tonnage, only those whose MMA is over it.", "Con tonelaje, solo si su MMA lo supera.")
Q("ob9", "oblig", "A blue round sign with a red diagonal bar means…", "Una señal azul redonda con barra roja diagonal significa…",
  [("the end of an obligation", "el fin de una obligación"), ("a prohibition", "una prohibición"), ("a warning", "un peligro")],
  "R-505 to R-516.", "R-505 a R-516.")
Q("ob10", "oblig", "Sign R-418 (blue with a “TT” symbol) means…", "La señal R-418 (azul con símbolo de telepeaje) significa…",
  [("electronic toll compulsory in that lane", "telepeaje obligatorio en ese carril"), ("tunnel ahead", "túnel próximo"), ("taxi rank", "parada de taxis")],
  "S-32 only says you may pay by electronic toll.", "La S-32 solo indica que se puede pagar con telepeaje.")

# ---------------------------------------------------------------- 7. indication signs
Q("zn1", "zones", "A blue square sign showing “70” means…", "Una señal cuadrada azul con «70» significa…",
  [("recommended maximum speed", "velocidad máxima aconsejable"), ("compulsory maximum speed", "velocidad máxima obligatoria"), ("minimum speed", "velocidad mínima")],
  "S-7 only advises.", "La S-7 solo aconseja.")
Q("zn2", "zones", "In a residential play zone (S-28), the maximum speed is…", "En una zona de estancia y juego (S-28), la velocidad máxima es…",
  [("10 km/h", "10 km/h"), ("20 km/h", "20 km/h"), ("30 km/h", "30 km/h")],
  "Coexistence zone S-47: 20 km/h.", "Zona de coexistencia S-47: 20 km/h.")
Q("zn3", "zones", "In a coexistence zone (S-47)…", "En una zona de coexistencia (S-47)…",
  [("games and sports are not allowed", "no se autorizan juegos ni deportes"), ("you may park anywhere", "se puede estacionar en cualquier sitio"), ("the limit is 10 km/h", "el límite es 10 km/h")],
  "20 km/h; pedestrians may use the whole area.", "20 km/h; los peatones usan toda la zona.")
Q("zn4", "zones", "On a 2+1 road (S-1c), the middle lane is…", "En una carretera 2+1 (S-1c), el carril central…",
  [("for overtaking, given to each direction in turn", "es para adelantar, reservado de forma alterna a cada sentido"), ("for slow vehicles", "es para vehículos lentos"), ("a bus lane", "es un carril bus")],
  "Three lanes, both directions.", "Tres carriles, ambos sentidos.")
Q("zn5", "zones", "Exit countdown panels (S-26) with one diagonal bar mean the exit is about…", "Los paneles S-26 con una sola diagonal indican que la salida está a unos…",
  [("100 m away", "100 m"), ("300 m away", "300 m"), ("1 km away", "1 km")],
  "Three bars 300 m, two 200 m.", "Tres barras 300 m, dos 200 m.")
Q("zn6", "zones", "Sign S-17a (parking for a specific need) is for…", "La señal S-17a (estacionamiento de necesidad) es para…",
  [("a specific purpose shown by a pictogram, for a limited time", "un fin concreto indicado por pictograma, durante un tiempo limitado"), ("residents", "residentes"), ("lorries at night", "camiones de noche")],
  "E.g. pharmacy or hospital.", "Por ejemplo, farmacia u hospital.")
Q("zn7", "zones", "Sign S-49 (motorcycle and bicycle over a line) shows…", "La señal S-49 (moto y bici sobre una línea) indica…",
  [("an advanced waiting area before the stop line for those vehicles", "una zona de espera previa a la línea de detención para esos vehículos"), ("a motorcycle lane", "un carril para motos"), ("no motorcycles", "prohibido motos")],
  "At junctions with traffic lights.", "En intersecciones con semáforos.")
Q("zn8", "zones", "Sign S-16 shows…", "La señal S-16 indica…",
  [("an emergency escape lane for brake failure", "una zona de frenado de emergencia"), ("a lay-by", "un apartadero"), ("a steep descent", "una bajada fuerte")],
  "Red-white chequerboard marks where it starts.", "El damero rojo y blanco marca su inicio.")
Q("zn9", "zones", "In a residential play zone, cycles and VMP may go…", "En una zona de estancia y juego, ciclos y VMP pueden circular…",
  [("both ways, unless signed otherwise", "en ambos sentidos, salvo indicación"), ("never", "nunca"), ("only one way", "solo en un sentido")],
  "Same in coexistence zones.", "Igual en zonas de coexistencia.")
Q("zn10", "zones", "Sign S-33 (green, pedestrians and bicycle) is a…", "La señal S-33 (verde, peatones y bicicleta) es una…",
  [("shared foot and cycle path away from motor traffic", "senda ciclopeatonal segregada del tráfico motorizado"), ("cycle lane on the road", "carril bici en calzada"), ("park entrance", "entrada a un parque")],
  "Cycles slow down near pedestrians.", "Los ciclos reducen ante peatones.")
Q("zn11", "zones", "Sign S-24 (headlamp with “?”) reminds you that…", "La señal S-24 (faro con «?») recuerda que…",
  [("the dipped-beam obligation ends, use it if conditions require", "termina la obligación de luz de cruce; úsala si las condiciones lo exigen"), ("your lights are faulty", "tus luces fallan"), ("fog lights are allowed", "se permiten antinieblas")],
  "End of R-413.", "Fin de la R-413.")
Q("la1", "lanes", "In a bus lane with a dashed line, may a car overtake through it?", "En un carril bus con línea discontinua, ¿puede un turismo adelantar por él?",
  [("No", "No"), ("Yes, if it is free", "Sí, si está libre"), ("Yes, at night", "Sí, de noche")],
  "Other users may only make manoeuvres other than stopping, parking, U-turns or overtaking.", "Solo maniobras que no sean parar, estacionar, cambiar de sentido o adelantar.")
Q("la2", "lanes", "A lane signed with a minimum speed (S-50) may be used by…", "Un carril con velocidad mínima (S-50) pueden usarlo…",
  [("vehicles at or above that speed", "los que circulen a esa velocidad o superior"), ("any vehicle", "cualquier vehículo"), ("only lorries", "solo camiones")],
  "Keep to the right lane when you can.", "Si se puede, ir por la derecha.")
Q("la3", "lanes", "Sign S-51b “2+” marks a lane for…", "La señal S-51b «2+» indica un carril para…",
  [("vehicles with at least 2 occupants", "vehículos con al menos 2 ocupantes"), ("two-wheelers", "vehículos de dos ruedas"), ("two lanes", "dos carriles")],
  "High-occupancy (VAO) lane.", "Carril VAO.")
Q("la4", "lanes", "On a lane sign, a dashed arrow joining the others means…", "En una señal de carriles, una flecha discontinua que se une a las demás indica…",
  [("a lane merging from that side", "la confluencia de un carril por ese lado"), ("a closed lane", "un carril cerrado"), ("a bus lane", "un carril bus")],
  "S-70 to S-73.", "S-70 a S-73.")
Q("la5", "lanes", "Sign S-52 shows one lane line bending into the next. It means…", "La señal S-52 muestra una línea de carril que se une a la de al lado. Indica…",
  [("that lane ends: change lane", "que ese carril termina: hay que cambiar de carril"), ("a new lane opens", "que se abre un carril"), ("a fork", "una bifurcación")],
  "S-53 is the opposite: one lane becomes two.", "La S-53 es al revés: de uno a dos.")
Q("la6", "lanes", "Sign S-64 (cycle in a circle over one lane) means that lane is…", "La señal S-64 (bici en un círculo sobre un carril) indica que ese carril es…",
  [("compulsory for cycles and forbidden for others", "obligatorio para ciclos y prohibido a los demás"), ("forbidden for cycles", "prohibido a ciclos"), ("shared with buses", "compartido con autobuses")],
  "S-65: reserved, not compulsory.", "S-65: reservado, no obligatorio.")
Q("oi1", "orient", "Signs on motorways and autovías have…", "Las señales de orientación en autopistas y autovías tienen…",
  [("a blue background and white letters", "fondo azul y letras blancas"), ("a white background and black letters", "fondo blanco y letras negras"), ("a green background", "fondo verde")],
  "Conventional roads: white background.", "Convencionales: fondo blanco.")
Q("oi2", "orient", "Confirmation signs always have the colour of…", "Los carteles de confirmación tienen siempre el color de…",
  [("the road you are on", "la vía por la que circulas"), ("the road you will reach", "la vía a la que llegarás"), ("the province", "la provincia")],
  "Only pre-signposting changes colour.", "Solo la preseñalización cambia de color.")
Q("oi3", "orient", "On a motorway, the immediate exit sign for an exit to a conventional road is…", "En autopista, el cartel de salida inmediata hacia una carretera convencional es…",
  [("white", "blanco"), ("blue", "azul"), ("green", "verde")],
  "Immediate exit signs take the destination road’s colour.", "Toma el color de la vía de destino.")
Q("oi4", "orient", "Pre-signposting to an exit leading to a lower-category road keeps…", "La preseñalización de una salida hacia una vía de inferior categoría mantiene…",
  [("the colour of the road you are on", "el color de la vía por la que circulas"), ("the colour of the destination road", "el color de la vía de destino"), ("a yellow colour", "el color amarillo")],
  "To avoid drivers slowing before the deceleration lane.", "Para evitar reducciones antes del carril de deceleración.")
Q("oi5", "orient", "On a motorway, the exit number…", "En autopista, el número de salida…",
  [("matches the kilometre point", "coincide con el punto kilométrico"), ("counts exits from the start", "cuenta las salidas desde el inicio"), ("is the road number", "es el número de la carretera")],
  "S-341/S-342.", "S-341/S-342.")
Q("oi6", "orient", "A road number on a red plate (e.g. N-401) belongs to…", "Una matrícula sobre fondo rojo (p. ej., N-401) es…",
  [("the State network, not a motorway", "de la red del Estado, no autopista"), ("a regional first-level road", "autonómica de primer nivel"), ("a European route", "un itinerario europeo")],
  "E green; A/AP blue; regional orange, brown, yellow.", "E verde; A/AP azul; autonómicas naranja, marrón, amarillo.")
Q("oi7", "orient", "May a road that is not a motorway or autovía use the letter A?", "¿Puede llevar la letra A una carretera que no sea autopista o autovía?",
  [("No", "No"), ("Yes, if it is regional", "Sí, si es autonómica"), ("Yes, ring roads", "Sí, las rondas")],
  "Ring roads may swap the A for the city’s letters.", "Las rondas pueden sustituir la A por letras de la ciudad.")
Q("oi8", "orient", "Panel S-840 “STOP 150 m” under a give-way sign means…", "El panel S-840 «STOP 150 m» bajo un ceda el paso indica…",
  [("a STOP sign 150 m ahead at the next junction", "un STOP a 150 m en la próxima intersección"), ("stop for 150 seconds", "detenerse 150 segundos"), ("no stopping for 150 m", "prohibido parar 150 m")],
  "It pre-signals the STOP.", "Preseñaliza el STOP.")
Q("oi9", "orient", "Panel S-810 “800 m” with arrows shows…", "El panel S-810 «800 m» con flechas indica…",
  [("the length of the stretch affected", "la longitud del tramo afectado"), ("the distance to the danger", "la distancia al peligro"), ("the free width", "la anchura libre")],
  "S-800 gives the distance to the start.", "El S-800 da la distancia al comienzo.")
Q("oi10", "orient", "Panel S-892 (camera) under a sign means…", "El panel S-892 (cámara) bajo una señal indica…",
  [("compliance is checked by automatic means", "su cumplimiento se vigila con medios automáticos"), ("a tourist viewpoint", "un mirador turístico"), ("a police station", "una comisaría")],
  "Automatic capture and fines.", "Captación y denuncia automáticas.")
Q("oi11", "orient", "Panel S-891 reminds you of the side gap when overtaking cycles or mopeds:", "El panel S-891 recuerda la separación lateral al adelantar a ciclos o ciclomotores:",
  [("1.5 m", "1,5 m"), ("1 m", "1 m"), ("2 m", "2 m")],
  "With a group, measured from the one furthest left.", "En grupo, desde el más escorado a la izquierda.")
Q("oi12", "orient", "Sign S-500 (town entry) marks…", "La señal S-500 (entrada a poblado) indica…",
  [("where the town’s traffic rules begin", "dónde empiezan a regir las normas de poblado"), ("the town hall", "el ayuntamiento"), ("a 30 km/h zone", "una zona 30")],
  "S-510 ends them.", "La S-510 las termina.")
Q("oi13", "orient", "Sign S-991g (yellow, helicopter and drone) warns that…", "La señal S-991g (amarilla, helicóptero y dron) advierte de que…",
  [("speed may be checked from the air", "puede haber control de velocidad desde el aire"), ("an airport is near", "hay un aeropuerto"), ("drones are forbidden", "están prohibidos los drones")],
  "Helicopter or drone.", "Helicóptero o dron.")
Q("oi14", "orient", "In town, a yellow S-710 module points to…", "En poblado, un módulo amarillo S-710 indica…",
  [("places of interest for travellers (stations, airports, hotels)", "lugares de interés para viajeros (estaciones, aeropuertos, hoteles)"), ("streets and squares", "calles y plazas"), ("industrial zones", "zonas industriales")],
  "Green S-700 streets; brown S-730 monuments.", "Verde S-700 calles; marrón S-730 monumentos.")
Q("oi15", "orient", "Sign S-122 (blue with an empty white square) is for…", "La señal S-122 (azul con recuadro blanco vacío) es para…",
  [("other services, written in the square", "otros servicios, inscritos en el recuadro"), ("a closed service", "un servicio cerrado"), ("free parking", "estacionamiento libre")],
  "Generic service sign.", "Señal genérica de servicio.")

# ---------------------------------------------------------------- 8. road markings
Q("mk1", "mklong", "A continuous white line separating directions means…", "Una línea continua que separa sentidos significa…",
  [("do not cross it, drive on it or drive to its left", "no atravesarla, no circular sobre ella ni por su izquierda"), ("cross it only to overtake", "cruzarla solo para adelantar"), ("cross it with care", "cruzarla con precaución")],
  "Two continuous lines mean the same.", "Dos continuas adosadas, lo mismo.")
Q("mk2", "mklong", "A noticeably wider continuous line marks…", "Una línea continua sensiblemente más ancha indica…",
  [("a special lane: only its users may cross it to leave", "un carril especial: solo sus usuarios la cruzan para salir"), ("a stronger ban for everyone", "una prohibición más fuerte para todos"), ("the road edge", "el borde de la calzada")],
  "When the manoeuvre or destination requires it.", "Cuando lo exija la maniobra o el destino.")
Q("mk3", "mklong", "May you drive on a broken lane line?", "¿Se puede circular sobre una línea discontinua?",
  [("Only if lanes are narrow and it is safe", "Solo si los carriles son estrechos y es seguro"), ("Yes, always", "Sí, siempre"), ("Never", "Nunca")],
  "It guides traffic.", "Sirve para guiar.")
Q("mk4", "mklong", "Broken lines with noticeably shorter gaps announce…", "Las discontinuas con trazos más juntos anuncian…",
  [("a continuous line or a stretch of special risk", "una línea continua o un tramo de riesgo especial"), ("a bus lane", "un carril bus"), ("the end of the road", "el final de la vía")],
  "Broken lines also announce forks and merges.", "También anuncian bifurcaciones y confluencias.")
Q("mk5", "mklong", "A continuous line is next to a broken line. You heed…", "Una línea continua va adosada a una discontinua. Atiendes a…",
  [("the line on your side", "la línea de tu lado"), ("the continuous one always", "siempre la continua"), ("the broken one always", "siempre la discontinua")],
  "Each driver obeys the one on their side.", "Cada uno, la de su lado.")
Q("mk6", "mklong", "You have just overtaken; the line between directions is now continuous on your side and broken on the other. You…", "Acabas de adelantar; la línea entre sentidos es continua por tu lado y discontinua por el otro. Tú…",
  [("may return to your side", "puedes volver a tu lado"), ("must stay on the left", "debes seguir por la izquierda"), ("must stop", "debes detenerte")],
  "Between directions it does not stop you returning.", "Si separa sentidos, no impide volver.")
Q("mk7", "mklong", "A lane bounded on both sides by double broken lines is…", "Un carril delimitado por líneas dobles discontinuas a ambos lados es…",
  [("a reversible lane", "un carril reversible"), ("a bus lane", "un carril bus"), ("a hard shoulder", "un arcén")],
  "Its direction is set by lane lights or other means.", "Se regula con semáforos de carril u otros medios.")
Q("mk8", "mklong", "Are edge lines or parking-bay lines longitudinal white markings for these rules?", "¿Las líneas de borde o de estacionamiento cuentan como marcas longitudinales?",
  [("No", "No"), ("Yes", "Sí"), ("Only if continuous", "Solo si son continuas")],
  "They just make the edges more visible.", "Solo hacen más visibles los bordes.")
Q("mt1", "mktrans", "A continuous line across your lane is…", "Una línea continua transversal en tu carril es…",
  [("a stop line", "una línea de detención"), ("a give-way line", "una línea de ceda el paso"), ("a pedestrian crossing", "un paso de peatones")],
  "Don’t cross it when you must stop.", "No rebasarla cuando debas detenerte.")
Q("mt2", "mktrans", "At a give-way line you cannot see the road. You…", "En una línea de ceda el paso no ves la vía. Tú…",
  [("may move forward until you can see, without having to stop", "puedes avanzar hasta conseguir visibilidad, sin necesidad de detenerte"), ("must stop at the line first", "debes detenerte primero en la línea"), ("must turn back", "debes volver")],
  "At a stop line you would stop and then stop again.", "En una de detención pararías y volverías a parar.")
Q("mt3", "mktrans", "Pedestrian crossing bands are…", "Las bandas de un paso de peatones son…",
  [("parallel to the road’s axis, with no other colours alternating", "paralelas al eje de la calzada, sin alternar otros colores"), ("across the road, red and white", "transversales, rojas y blancas"), ("diagonal", "diagonales")],
  "They form a set across the road.", "Forman un conjunto transversal.")
Q("mt4", "mktrans", "A cycle crossing is marked by…", "Un paso para ciclistas se marca con…",
  [("two parallel broken lines across the road", "dos líneas transversales discontinuas y paralelas"), ("a zebra", "una cebra"), ("a yellow grid", "una cuadrícula amarilla")],
  "Cyclists have priority; may be painted red.", "Preferencia ciclista; puede pintarse de rojo.")
Q("mt5", "mktrans", "Three white triangles on a hump (“lomo de asno”) mean…", "Tres triángulos blancos sobre un resalto («lomo de asno») indican…",
  [("a speed hump: slow down", "un reductor de velocidad: hay que reducir"), ("give way", "ceda el paso"), ("a level crossing", "un paso a nivel")],
  "Near crossings, schools, hospitals…", "Cerca de pasos, colegios, hospitales…")
Q("mt6", "mktrans", "A STOP painted in a lane bounded by lines applies to…", "Un STOP pintado en un carril delimitado por líneas afecta a…",
  [("vehicles in that lane only", "solo a los vehículos de ese carril"), ("all lanes", "todos los carriles"), ("pedestrians", "los peatones")],
  "All painted signs in a lane work like that.", "Así funcionan las señales pintadas en un carril.")
Q("mt7", "mktrans", "A return arrow near the centre of a two-way road pointing right means…", "Una flecha de retorno en el eje de una calzada de doble sentido, apuntando a la derecha, indica…",
  [("a continuous line is coming: move right as soon as possible", "se acerca una línea continua: pasar a la derecha cuanto antes"), ("turn right at the next junction", "girar a la derecha en el próximo cruce"), ("the lane ends", "el carril termina")],
  "Driving to the left of that line will be forbidden.", "Estará prohibido circular por su izquierda.")
Q("mt8", "mktrans", "A mini-roundabout’s central island measures…", "La isleta central de una minirrotonda mide…",
  [("4 m or less across", "4 m o menos de diámetro"), ("at least 10 m", "al menos 10 m"), ("exactly 6 m", "exactamente 6 m")],
  "The arrows show the way round.", "Las flechas indican el sentido.")
Q("mt9", "mktrans", "A painted triangle with its point towards you means…", "Un triángulo pintado con el vértice hacia ti significa…",
  [("give way at the next junction", "ceder el paso en la próxima intersección"), ("road narrows", "estrechamiento"), ("danger", "peligro")],
  "Horizontal give-way sign.", "Señal horizontal de ceda el paso.")
Q("mo1", "mkother", "May a car enter a hatched area (cebreado)?", "¿Puede un turismo entrar en un cebreado?",
  [("No; only those who must use the shoulder may", "No; solo los obligados a circular por el arcén"), ("Yes, to overtake", "Sí, para adelantar"), ("Yes, to stop", "Sí, para parar")],
  "Oblique stripes framed by a continuous line.", "Franjas oblicuas enmarcadas por una continua.")
Q("mo2", "mkother", "Distance chevrons (galones): keep at least…", "Galones: hay que dejar al menos…",
  [("2 chevrons", "2 galones"), ("1 chevron", "1 galón"), ("3 chevrons", "3 galones")],
  "On any road; R-300 at the start.", "En cualquier vía; R-300 al inicio.")
Q("mo3", "mkother", "The two lines of an avanza-motos box are…", "Las dos líneas de un avanza-motos están separadas…",
  [("4 m apart", "4 m"), ("2 m apart", "2 m"), ("10 m apart", "10 m")],
  "Only the vehicles shown may wait there on red.", "Con rojo solo pueden ocuparlo los del pictograma.")
Q("mo4", "mkother", "Dragon’s teeth at the edges of the road warn you to…", "Los dientes de dragón en los bordes avisan de que debes…",
  [("slow down noticeably as you enter a town", "reducir sensiblemente la velocidad al llegar a una travesía o vía urbana"), ("give way", "ceder el paso"), ("overtake", "adelantar")],
  "Vulnerable users may be present.", "Posibles usuarios vulnerables.")
Q("mo5", "mkother", "Zig-zag edge lines warn of…", "Las líneas de borde quebradas avisan de…",
  [("a pedestrian or cycle crossing ahead", "un paso para peatones o ciclistas próximo"), ("a bend", "una curva"), ("a toll", "un peaje")],
  "Slow down and pay attention.", "Reducir y aumentar la atención.")
Q("mo6", "mkother", "A broken yellow line along the kerb means…", "Una línea amarilla discontinua junto al bordillo significa…",
  [("no parking (stopping allowed)", "estacionamiento prohibido (parada permitida)"), ("no stopping or parking", "parada y estacionamiento prohibidos"), ("loading only", "solo carga y descarga")],
  "Continuous yellow: no stopping or parking.", "Continua amarilla: ni parar ni estacionar.")
Q("mo7", "mkother", "A yellow criss-cross grid in a junction means…", "Una cuadrícula amarilla en una intersección significa…",
  [("do not enter if you may be left stopped there", "no entrar si previsiblemente quedarás detenido"), ("no entry at all", "prohibido entrar siempre"), ("parking area", "zona de estacionamiento")],
  "So as not to block cross traffic.", "Para no obstruir la circulación transversal.")
Q("mo8", "mkother", "A red and white chequerboard marks…", "Un damero rojo y blanco marca…",
  [("the start of an emergency escape lane", "el comienzo de una zona de frenado de emergencia"), ("a level crossing", "un paso a nivel"), ("a cycle lane", "un carril bici")],
  "No stopping, parking or other use.", "Prohibida la parada, el estacionamiento y otros usos.")
Q("mo9", "mkother", "Blue lines marking parking spaces mean…", "Las marcas azules de estacionamiento significan…",
  [("parking time is limited at certain times", "duración del estacionamiento limitada en ciertos periodos"), ("reserved for disabled people", "reservado a personas con discapacidad"), ("no parking", "prohibido estacionar")],
  "Instead of the usual white.", "En lugar del blanco habitual.")
Q("mo10", "mkother", "A yellow zig-zag marking means…", "Una marca amarilla en zigzag significa…",
  [("no parking: reserved for a special short-stay use", "prohibido estacionar: reservado a un uso especial sin larga permanencia"), ("no overtaking", "prohibido adelantar"), ("roadworks", "obras")],
  "Bus stops, loading zones.", "Paradas de bus, carga y descarga.")
Q("mo11", "mkother", "An edge line can be continuous or broken. The difference is…", "Una línea de borde puede ser continua o discontinua. La diferencia es…",
  [("none, it makes no difference", "ninguna, es indiferente"), ("you may cross the broken one to overtake", "la discontinua se puede cruzar para adelantar"), ("the continuous one bans stopping", "la continua prohíbe parar")],
  "It only makes the edge more visible.", "Solo hace más visible el borde.")
Q("mo12", "mkother", "A chequerboard of white squares across the road warns of…", "Un damero de cuadros blancos en la calzada avisa de…",
  [("a risk greater than it looks: slow down", "un riesgo mayor del percibido: reducir"), ("a pedestrian crossing", "un paso de peatones"), ("a parking area", "un aparcamiento")],
  "Before roundabouts, tolls…", "Antes de glorietas, peajes…")
Q("mo13", "mkother", "Yellow kerb markings can mean a temporary prohibition when…", "Las marcas amarillas pueden indicar una prohibición temporal cuando…",
  [("a vertical sign at the start of the stretch says so", "una señal vertical al principio del tramo lo especifica"), ("it is raining", "llueve"), ("it is night", "es de noche")],
  "Zig-zag, continuous and broken yellow lines.", "Zigzag, continua y discontinua amarillas.")
