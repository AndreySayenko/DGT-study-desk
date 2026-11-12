# -*- coding: utf-8 -*-
"""Question bank for the interactive Category A1/A2, Topic 7 page (lights). In every question the FIRST option is the
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
    "purpose": dict(sec=1, en="What lights are for", es="Finalidad de las luces",
        recap=[("Show the vehicle is there, light the road, warn others.", "Indicar la presencia, alumbrar la vía y avisar."),
               ("Lights on from sunset to sunrise, and at any time in tunnels and underpasses.", "Luces del ocaso a la salida del sol y a cualquier hora en túneles y pasos inferiores."),
               ("Poorly lit: plate unreadable at 10 m, dark vehicle unseen at 50 m.", "Insuficientemente iluminada: matrícula ilegible a 10 m, vehículo oscuro no visible a 50 m."),
               ("Weaker lights after a breakdown: slow down to stop within the lit area.", "Alumbrado más débil por avería: reducir hasta poder detenerse en la zona iluminada.")],
        trap=("Thinking a road with street lamps is always ‘well lit’.", "Pensar que una vía con farolas está siempre «suficientemente iluminada».")),
    "position": dict(sec=2, en="Position lights", es="Luces de posición",
        recap=[("Presence and width: white front, red rear.", "Presencia y anchura: blanca delante, roja detrás."),
               ("Motorcycles: 1 or 2 front and rear; three-wheelers over 1,300 mm: 2 each end.", "Motos: 1 o 2 delante y detrás; tres ruedas de más de 1.300 mm: 2, en los extremos."),
               ("On when stopped on carriageway or shoulder at night, and parked in some places.", "Encendidas al estar detenido en calzada o arcén de noche y al estacionar en ciertos lugares."),
               ("Come on automatically with dipped, main or fog; never ride with position lights only.", "Se encienden solas con cruce, carretera o antiniebla; prohibido circular solo con ellas.")],
        trap=("Riding at dusk with only the position lights.", "Circular al anochecer solo con la luz de posición.")),
    "reflect": dict(sec=2, en="Reflectors", es="Catadióptricos",
        recap=[("No light of their own: they reflect.", "No tienen luz propia: reflejan."),
               ("Motorcycle rear: compulsory, red, not triangular (two with sidecar).", "Moto, detrás: obligatorio, rojo, no triangular (dos con sidecar)."),
               ("Sides: optional, amber, one or two per side.", "Laterales: opcionales, amarillo auto, uno o dos por lado."),
               ("Three-wheelers over 1 m wide: two rear reflectors.", "Tres ruedas de más de 1 m: dos traseros.")],
        trap=("Thinking the rear reflector may be triangular.", "Pensar que el catadióptrico trasero puede ser triangular.")),
    "dipped": dict(sec=3, en="Dipped beam", es="Luz de cruce",
        recap=[("White; lights the road ahead without dazzling.", "Blanca; alumbra por delante sin deslumbrar."),
               ("Motorcycles: dipped + position lights at any time of day.", "Motos: cruce + posición a cualquier hora del día."),
               ("Even after an ‘end of dipped beam’ sign.", "Aunque aparezca la señal «Fin de alumbrado de corto alcance»."),
               ("It is the light for meeting other road users.", "Es la luz para cruzarse con otros usuarios.")],
        trap=("Switching the dipped beam off by day on a motorcycle.", "Apagar la luz de cruce de día en moto.")),
    "main": dict(sec=3, en="Main beam", es="Luz de carretera",
        recap=[("White, more intense, lights far ahead.", "Blanca, más intensa, alumbra a larga distancia."),
               ("Compulsory above 40 km/h: night on poorly lit roads out of town; any time in poorly lit tunnels.", "Obligatoria a más de 40 km/h: de noche en interurbanas mal iluminadas; a cualquier hora en túneles mal iluminados."),
               ("At 40 km/h or less: either. Dipped if it could dazzle.", "A 40 km/h o menos: cualquiera. Cruce si puede deslumbrar."),
               ("Forbidden stopped, parked or in town.", "Prohibida parado, estacionado o en poblado.")],
        trap=("Using the main beam in a poorly lit town street.", "Usar la luz larga en una calle de poblado mal iluminada.")),
    "fog": dict(sec=3, en="Fog lights", es="Antiniebla",
        recap=[("Optional on motorcycles: front 1–2 white or selective yellow; rear 1–2 red.", "Opcionales en moto: delante 1–2 blancas o amarillo selectivo; detrás 1–2 rojas."),
               ("Front: fog, heavy rain, snow, dust or smoke; narrow roads ≤ 6.50 m with bends sign.", "Delantera: niebla, lluvia intensa, nevada, polvo o humo; vías ≤ 6,50 m con señal de curvas."),
               ("Rear: only especially bad conditions (thick fog, very heavy rain, heavy snow, dense dust).", "Trasera: solo condiciones especialmente adversas (niebla espesa, lluvia muy intensa, nevada fuerte, polvo denso)."),
               ("Bad visibility by day: position + any light; at night: position + dipped at least.", "Mala visibilidad de día: posición + cualquier alumbrado; de noche: al menos posición + cruce.")],
        trap=("Switching on the rear fog light in light rain.", "Encender la antiniebla trasera con lluvia ligera.")),
    "special": dict(sec=3, en="Lanes with lights always on", es="Carriles con luz siempre",
        recap=[("Reversible lane: dipped, day and night.", "Carril reversible: cruce, de día y de noche."),
               ("Roads with a temporary additional lane: dipped, day and night.", "Vías con carril adicional circunstancial: cruce, de día y de noche."),
               ("Contraflow lane and the adjacent normal lane: dipped, day and night.", "Carril en sentido contrario y el contiguo del sentido normal: cruce, de día y de noche."),
               ("For every vehicle, not only motorcycles.", "Para todos los vehículos, no solo motos.")],
        trap=("Thinking only the contraflow lane itself needs lights.", "Pensar que solo el carril en sentido contrario necesita luces.")),
    "dazzle": dict(sec=3, en="Dazzle", es="Deslumbramientos",
        recap=[("Dip as soon as you could dazzle anyone, even if the oncoming driver doesn’t.", "Poner la de cruce en cuanto puedas deslumbrar, aunque el otro no lo haga."),
               ("Overtaking: main beam only when level; the overtaken then dips.", "Adelantamiento: larga solo en paralelo; entonces el adelantado pone la de cruce."),
               ("Bends: the one turning right dips first. Keep the headlight aimed (passenger, load).", "Curvas: cambia primero el que gira a la derecha. Faro bien reglado (pasajero, carga)."),
               ("Dazzled: look right, close left eye; slow down, even stop, without moving onto the shoulder.", "Deslumbrado: mirar a la derecha, cerrar el ojo izquierdo; reducir, incluso parar, sin salir al arcén.")],
        trap=("Moving onto the shoulder when dazzled.", "Salir al arcén cuando te deslumbran.")),
    "warn": dict(sec=4, en="Warning lights", es="Luces de aviso",
        recap=[("Indicators: amber, compulsory, for lateral moves.", "Intermitentes: amarillo auto, obligatorios, para desplazamientos laterales."),
               ("Hazard lights: all indicators together; optional on motorcycles; flashing red tell-tale.", "Emergencia: todos los intermitentes a la vez; opcional en moto; testigo rojo intermitente."),
               ("Brake light: repeated use to warn of stopping or braking hard.", "Freno: uso reiterado para avisar de que vas a parar o frenar mucho."),
               ("Reversing light white, optional on motorcycles. Plate light on with position lights.", "Marcha atrás blanca, opcional en moto. Matrícula: se enciende con la de posición.")],
        trap=("Thinking hazard lights are compulsory on every motorcycle.", "Pensar que la luz de emergencia es obligatoria en toda moto.")),
}

# ---------------------------------------------------------------- purpose
Q("pu1", "purpose", "What are vehicle lights for?", "¿Para qué sirven las luces del vehículo?",
  [("To show the vehicle is there, light the road and warn others", "Para indicar su presencia, alumbrar la vía y avisar a los demás"), ("Only to see at night", "Solo para ver de noche"), ("Only to signal manoeuvres", "Solo para señalizar maniobras")],
  "Be seen, see, and warn.", "Ser visto, ver y avisar.")
Q("pu2", "purpose", "A road is poorly lit if you cannot read another vehicle’s number plate at…", "Una vía está insuficientemente iluminada si no puedes leer la matrícula de otro vehículo a…",
  [("10 m", "10 m"), ("50 m", "50 m"), ("25 m", "25 m")],
  "Or cannot make out a dark-painted vehicle at 50 m.", "O no distingues un vehículo pintado de oscuro a 50 m.")
Q("pu3", "purpose", "At midday you ride into a tunnel. Must you have lights on?", "A mediodía entras en un túnel. ¿Debes llevar luces?",
  [("Yes, at any time of day", "Sí, a cualquier hora del día"), ("Only if it is poorly lit", "Solo si está mal iluminado"), ("No, by day it isn’t needed", "No, de día no hace falta")],
  "On a motorcycle you have the dipped beam on anyway.", "En moto ya llevas la de cruce de todos modos.")
Q("pu4", "purpose", "Your headlight fails on the way and you must ride with a weaker light. You…", "El faro se avería en ruta y debes circular con una luz más débil. Tú…",
  [("slow down so you can stop within the lit area", "reduces la velocidad para poder detenerte dentro de la zona iluminada"), ("keep your speed using the hazard lights", "mantienes la velocidad con la luz de emergencia"), ("ride behind another vehicle", "circulas detrás de otro vehículo")],
  "An irreparable breakdown on the way.", "Avería irreparable en ruta.")
Q("pu5", "purpose", "A road is also poorly lit if you cannot make out a dark-painted vehicle at…", "Una vía también está insuficientemente iluminada si no distingues un vehículo oscuro a…",
  [("50 m", "50 m"), ("10 m", "10 m"), ("100 m", "100 m")],
  "Plate at 10 m, dark vehicle at 50 m.", "Matrícula a 10 m, vehículo oscuro a 50 m.")

# ---------------------------------------------------------------- position
Q("ps1", "position", "Position lights show the vehicle’s…", "Las luces de posición indican…",
  [("presence and width", "la presencia y la anchura del vehículo"), ("speed", "la velocidad"), ("braking", "el frenado")],
  "White at the front, red at the rear.", "Blanca delante, roja detrás.")
Q("ps2", "position", "May you ride at night with only the position lights on?", "¿Puedes circular de noche solo con las luces de posición?",
  [("No, it is forbidden", "No, está prohibido"), ("Yes, in a well-lit town", "Sí, en poblado bien iluminado"), ("Yes, below 40 km/h", "Sí, por debajo de 40 km/h")],
  "They don’t light the road.", "No alumbran la vía.")
Q("ps3", "position", "How many front position lights may a two-wheeled motorcycle have?", "¿Cuántas luces de posición delanteras puede tener una motocicleta de dos ruedas?",
  [("1 or 2", "1 o 2"), ("Exactly 2", "Exactamente 2"), ("None", "Ninguna")],
  "Same at the rear.", "Igual detrás.")
Q("ps4", "position", "A three-wheeler 1,400 mm wide must have front position lights…", "Un vehículo de tres ruedas de 1.400 mm de ancho debe llevar luces de posición delanteras…",
  [("two, one at each end", "dos, una en cada extremo"), ("one in the centre", "una en el centro"), ("one or two anywhere", "una o dos en cualquier lugar")],
  "Wider than 1,300 mm.", "Más de 1.300 mm.")
Q("ps5", "position", "At night you stop on the shoulder of an interurban road. You must have on…", "De noche te detienes en el arcén de una vía interurbana. Debes llevar encendidas…",
  [("the position lights", "las luces de posición"), ("the main beam", "la luz de carretera"), ("no lights", "ninguna luz")],
  "Stopped on carriageway or shoulder of any road.", "Detenido en calzada o arcén de cualquier vía.")
Q("ps6", "position", "When you switch on the dipped beam, the position lights…", "Al encender la luz de cruce, las luces de posición…",
  [("come on automatically", "se encienden automáticamente"), ("must be switched off", "deben apagarse"), ("are optional", "son opcionales")],
  "Also with main beam or fog lights.", "También con la de carretera o la antiniebla.")
Q("ps7", "position", "Parked at night on a well-lit urban street, must your motorcycle have its position lights on?", "Estacionada de noche en una calle urbana bien iluminada, ¿debe tu moto llevar la luz de posición?",
  [("No, if others can see it from far enough away", "No, si los demás pueden distinguirla a suficiente distancia"), ("Yes, always", "Sí, siempre"), ("Yes, and the hazard lights", "Sí, y la luz de emergencia")],
  "Only if the lighting doesn’t let others see it.", "Solo si la iluminación no permite distinguirla.")

# ---------------------------------------------------------------- reflectors
Q("rf1", "reflect", "At the rear, a motorcycle must have…", "En la parte trasera, una motocicleta debe llevar…",
  [("a red, non-triangular reflector", "un catadióptrico rojo no triangular"), ("a red triangular reflector", "un catadióptrico rojo triangular"), ("an amber reflector", "un catadióptrico amarillo auto")],
  "Two symmetrical ones with a sidecar.", "Dos simétricos con sidecar.")
Q("rf2", "reflect", "Side reflectors on a motorcycle are…", "Los catadióptricos laterales de una moto son…",
  [("optional, amber, one or two per side", "opcionales, amarillo auto, uno o dos por lado"), ("compulsory and red", "obligatorios y rojos"), ("forbidden", "prohibidos")],
  "Optional.", "Opcionales.")
Q("rf3", "reflect", "A reflector…", "Un catadióptrico…",
  [("has no light of its own: it reflects light", "no tiene luz propia: refleja la luz"), ("is a small lamp", "es una pequeña lámpara"), ("works only with the engine on", "solo funciona con el motor encendido")],
  "It shows the vehicle is there.", "Indica la presencia del vehículo.")
Q("rf4", "reflect", "A three-wheeler 1.2 m wide must have at the rear…", "Un vehículo de tres ruedas de 1,2 m de ancho debe llevar detrás…",
  [("two red non-triangular reflectors", "dos catadióptricos rojos no triangulares"), ("one triangular reflector", "un catadióptrico triangular"), ("no reflector", "ningún catadióptrico")],
  "One if up to 1 m wide.", "Uno si mide hasta 1 m.")

# ---------------------------------------------------------------- dipped
Q("dp1", "dipped", "On a motorcycle, the dipped beam must be on…", "En moto, la luz de cruce debe ir encendida…",
  [("at any time of day, on every public road", "a cualquier hora del día, en todas las vías públicas"), ("only at night", "solo de noche"), ("only out of town", "solo fuera de poblado")],
  "Together with the position lights.", "Junto con la de posición.")
Q("dp2", "dipped", "Riding your motorcycle by day, you pass an “end of dipped beam” sign. You…", "Circulando de día en moto, pasas una señal «Fin de alumbrado de corto alcance». Tú…",
  [("keep the dipped beam on", "mantienes la luz de cruce"), ("switch it off", "la apagas"), ("switch to position lights", "pones solo la de posición")],
  "Motorcycles keep it on all day.", "Las motos la llevan todo el día.")
Q("dp3", "dipped", "Which light do you use when meeting oncoming traffic at night?", "¿Qué luz usas al cruzarte de noche con otro vehículo?",
  [("The dipped beam", "La de cruce"), ("The main beam", "La de carretera"), ("The front fog light", "La antiniebla delantera")],
  "So as not to dazzle.", "Para no deslumbrar.")
Q("dp4", "dipped", "What colour is the dipped beam?", "¿De qué color es la luz de cruce?",
  [("White", "Blanca"), ("Selective yellow", "Amarillo selectivo"), ("Amber", "Amarillo auto")],
  "Main beam is white too.", "La de carretera también es blanca.")
Q("dp5", "dipped", "Which vehicles must have a dipped beam (1 or 2)?", "¿Qué vehículos deben llevar luz de cruce (1 o 2)?",
  [("Mopeds, motorcycles, three-wheelers and quadricycles", "Ciclomotores, motocicletas, tres ruedas y cuadriciclos"), ("Only motorcycles over 125 cm³", "Solo motos de más de 125 cm³"), ("Only quadricycles", "Solo cuadriciclos")],
  "1 or 2 lamps.", "1 o 2 luces.")

# ---------------------------------------------------------------- main beam
Q("mb1", "main", "At night, on a poorly lit interurban road at 80 km/h, with no one ahead or oncoming, you use…", "De noche, por una interurbana mal iluminada a 80 km/h, sin nadie delante ni de frente, usas…",
  [("the main beam", "la luz de carretera"), ("the dipped beam", "la luz de cruce"), ("the front fog light", "la antiniebla delantera")],
  "Compulsory above 40 km/h.", "Obligatoria a más de 40 km/h.")
Q("mb2", "main", "At 40 km/h or less, on a poorly lit road out of town at night, you may use…", "A 40 km/h o menos, de noche por una vía interurbana mal iluminada, puedes usar…",
  [("either the dipped or the main beam", "la de cruce o la de carretera"), ("only the main beam", "solo la de carretera"), ("only the position lights", "solo la de posición")],
  "Either of the two.", "Cualquiera de las dos.")
Q("mb3", "main", "May you use the main beam in town?", "¿Puedes usar la luz de carretera en poblado?",
  [("No", "No"), ("Yes, if poorly lit", "Sí, si está mal iluminado"), ("Yes, above 40 km/h", "Sí, a más de 40 km/h")],
  "Forbidden in town, and when stopped or parked.", "Prohibida en poblado y parado o estacionado.")
Q("mb4", "main", "In a poorly lit tunnel at midday, at 70 km/h, a motorcycle with main beam must use…", "En un túnel mal iluminado a mediodía, a 70 km/h, una moto con luz larga debe usar…",
  [("the main beam, unless it could dazzle someone", "la luz de carretera, salvo que pueda deslumbrar"), ("the dipped beam only", "solo la de cruce"), ("no lights", "ninguna luz")],
  "At any time of day in poorly lit tunnels.", "A cualquier hora en túneles mal iluminados.")
Q("mb5", "main", "Your motorcycle is stopped on the shoulder at night. May the main beam be on?", "Tu moto está detenida en el arcén de noche. ¿Puede estar encendida la luz larga?",
  [("No, it is forbidden stopped or parked", "No, está prohibida parado o estacionado"), ("Yes, to be seen", "Sí, para ser visto"), ("Yes, with the hazard lights", "Sí, con la luz de emergencia")],
  "Position lights instead.", "Luces de posición.")
Q("mb6", "main", "An oncoming car approaches while you use main beam. You…", "Se acerca un turismo de frente mientras llevas la larga. Tú…",
  [("switch to dipped beam", "cambias a la de cruce"), ("keep the main beam if it doesn’t dip", "mantienes la larga si él no cambia"), ("flash it repeatedly", "le haces ráfagas")],
  "Even if the other driver doesn’t dip.", "Aunque el otro no lo haga.")

# ---------------------------------------------------------------- fog
Q("fg1", "fog", "Are front fog lights compulsory on a motorcycle?", "¿Son obligatorias las antiniebla delanteras en una moto?",
  [("No, optional", "No, son opcionales"), ("Yes", "Sí"), ("Only on A2 motorcycles", "Solo en motos A2")],
  "1 or 2, white or selective yellow.", "1 o 2, blancas o amarillo selectivo.")
Q("fg2", "fog", "In heavy (not very heavy) rain, may you switch on the rear fog light?", "Con lluvia intensa (no muy intensa), ¿puedes encender la antiniebla trasera?",
  [("No, only in especially bad conditions", "No, solo con condiciones especialmente adversas"), ("Yes", "Sí"), ("Yes, in town", "Sí, en poblado")],
  "Very heavy rain, thick fog, heavy snow, dense dust.", "Lluvia muy intensa, niebla espesa, nevada fuerte, polvo denso.")
Q("fg3", "fog", "The front fog light may only be switched on with…", "La antiniebla delantera solo puede encenderse con…",
  [("the position lights on", "la luz de posición encendida"), ("the main beam on", "la luz de carretera encendida"), ("the hazard lights on", "la luz de emergencia")],
  "Alone or with dipped or main beam.", "Sola o con la de cruce o carretera.")
Q("fg4", "fog", "The rear fog light may only be switched on with…", "La antiniebla trasera solo puede encenderse con…",
  [("the dipped, main or front fog light on", "la de cruce, carretera o antiniebla delantera encendida"), ("the position lights only", "solo la de posición"), ("the brake light", "la luz de freno")],
  "It does not light the road.", "No alumbra la vía.")
Q("fg5", "fog", "On a narrow road (6 m) with the “dangerous bends” sign, in clear weather, you may use…", "En una vía estrecha (6 m) con la señal «curvas peligrosas», con buen tiempo, puedes usar…",
  [("the front fog light", "la antiniebla delantera"), ("the rear fog light", "la antiniebla trasera"), ("both fog lights", "las dos antiniebla")],
  "The rear one never for bends.", "La trasera nunca por las curvas.")
Q("fg6", "fog", "In fog by day, at least which lights must you have on?", "Con niebla de día, ¿qué luces debes llevar como mínimo?",
  [("Position lights plus any lighting light (fog, dipped or main)", "Posición más cualquier luz de alumbrado (antiniebla, cruce o carretera)"), ("Only position lights", "Solo las de posición"), ("Only the rear fog light", "Solo la antiniebla trasera")],
  "At night: position and dipped at least.", "De noche: al menos posición y cruce.")
Q("fg7", "fog", "Using the front fog light together with the main beam is…", "Usar la antiniebla delantera junto con la luz de carretera…",
  [("allowed but not advisable: it can reflect and dazzle you", "se permite pero no es aconsejable: puede reflejarse y deslumbrarte"), ("forbidden", "está prohibido"), ("compulsory in fog", "es obligatorio con niebla")],
  "In fog the light bounces back.", "Con niebla la luz rebota.")
Q("fg8", "fog", "What colour may a motorcycle’s rear fog light be?", "¿De qué color puede ser la antiniebla trasera de una moto?",
  [("Red", "Roja"), ("White", "Blanca"), ("Selective yellow", "Amarillo selectivo")],
  "Optional, 1 or 2.", "Opcional, 1 o 2.")
Q("fg9", "fog", "Heavy snow at night. At least which lights?", "Nevada fuerte de noche. ¿Qué luces como mínimo?",
  [("Position and dipped beam (others may be added)", "Posición y cruce (pueden añadirse las demás)"), ("Only the front fog light", "Solo la antiniebla delantera"), ("Only position lights", "Solo las de posición")],
  "The rear fog light is allowed too: heavy snow.", "La antiniebla trasera también se permite: nevada fuerte.")

# ---------------------------------------------------------------- special lanes
Q("sp1", "special", "Riding on a reversible lane by day, you must have on at least…", "Circulando de día por un carril reversible, debes llevar al menos…",
  [("the dipped beam", "la luz de cruce"), ("only position lights", "solo las de posición"), ("the hazard lights", "la luz de emergencia")],
  "Day and night.", "De día y de noche.")
Q("sp2", "special", "You ride in the normal-direction lane next to a contraflow lane. Lights?", "Circulas por el carril del sentido normal contiguo a un carril en sentido contrario. ¿Luces?",
  [("At least dipped, day and night", "Al menos la de cruce, de día y de noche"), ("None by day", "Ninguna de día"), ("Main beam", "La de carretera")],
  "The adjacent lane too.", "También el carril contiguo.")
Q("sp3", "special", "On a road with a temporary additional lane, who must have the dipped beam on by day?", "En una vía con carril adicional circunstancial, ¿quién debe llevar de día la luz de cruce?",
  [("Every vehicle using it", "Todos los vehículos que circulen por ella"), ("Only motorcycles", "Solo las motos"), ("Only lorries", "Solo los camiones")],
  "Motorcycles have it on anyway.", "Las motos ya la llevan.")

# ---------------------------------------------------------------- dazzle
Q("dz1", "dazzle", "Dazzle is…", "El deslumbramiento es…",
  [("a temporary blindness caused by more light than the eyes can take", "una ceguera temporal por recibir más luz de la que los ojos soportan"), ("a fault in the headlight", "una avería del faro"), ("a type of fog light", "un tipo de antiniebla")],
  "It lasts a few seconds.", "Dura unos segundos.")
Q("dz2", "dazzle", "At night you overtake a car. When may you switch on your main beam?", "De noche adelantas a un turismo. ¿Cuándo puedes poner la luz larga?",
  [("When you are level with it", "Cuando estés en paralelo con él"), ("Before starting to overtake", "Antes de empezar a adelantar"), ("Never while overtaking", "Nunca durante el adelantamiento")],
  "At that moment the overtaken driver dips.", "En ese momento el adelantado pone la de cruce.")
Q("dz3", "dazzle", "On a bend, who should switch to dipped beam first?", "En una curva, ¿quién debe cambiar primero a la luz de cruce?",
  [("The one for whom the bend turns right", "Aquel para quien la curva va hacia la derecha"), ("The one for whom it turns left", "Aquel para quien va hacia la izquierda"), ("Both at the same time", "Ambos a la vez")],
  "Its beam falls on oncoming drivers.", "Su haz incide sobre los que vienen de frente.")
Q("dz4", "dazzle", "You carry a passenger and a loaded top case at night. You should…", "Llevas de noche pasajero y un baúl cargado. Deberías…",
  [("check the headlight aim: the rear sinks and the beam rises", "comprobar el reglaje del faro: la parte trasera baja y el haz sube"), ("use the main beam", "usar la luz larga"), ("switch on the rear fog light", "encender la antiniebla trasera")],
  "To avoid dazzling others.", "Para no deslumbrar a los demás.")
Q("dz5", "dazzle", "An oncoming vehicle dazzles you. You…", "Un vehículo que viene de frente te deslumbra. Tú…",
  [("slow down, even stop, without changing your position", "reduces la velocidad, incluso te detienes, sin variar tu posición"), ("move onto the shoulder", "sales al arcén"), ("flash your main beam at it", "le das la luz larga")],
  "Leaving for the shoulder risks running off the road or hitting someone.", "Salir al arcén es arriesgado: puedes salirte o encontrar a alguien.")
Q("dz6", "dazzle", "To reduce the chance of being dazzled by oncoming vehicles, you…", "Para reducir la posibilidad de ser deslumbrado por los que vienen de frente…",
  [("look right, following the edge line, and close the left eye", "miras a la derecha guiándote por la línea del borde y cierras el ojo izquierdo"), ("look straight at their lights", "miras directamente a sus luces"), ("close both eyes briefly", "cierras los dos ojos un instante")],
  "The left eye gets the most light.", "El ojo izquierdo es el que más luz recibe.")
Q("dz7", "dazzle", "The vehicle behind dazzles you through the mirrors. You may…", "El vehículo de detrás te deslumbra por los espejos. Puedes…",
  [("change the angle of the mirrors or your position", "cambiar la orientación de los retrovisores o tu posición"), ("brake suddenly", "frenar bruscamente"), ("switch on the rear fog light", "encender la antiniebla trasera")],
  "So the light doesn’t reach your eyes.", "Para que la luz no se refleje en tus ojos.")
Q("dz8", "dazzle", "When may you switch the main beam back on after meeting a vehicle?", "¿Cuándo puedes volver a poner la luz larga tras cruzarte con un vehículo?",
  [("When you are sure you won’t dazzle anyone", "Cuando estés seguro de no deslumbrar a nadie"), ("Immediately", "Inmediatamente"), ("After 10 seconds", "A los 10 segundos")],
  "Including drivers ahead through their mirrors.", "Incluidos los de delante por sus retrovisores.")

# ---------------------------------------------------------------- warning
Q("wr1", "warn", "What colour are the indicators?", "¿De qué color son los intermitentes?",
  [("Amber", "Amarillo auto"), ("White", "Blanco"), ("Red", "Rojo")],
  "Compulsory.", "Obligatorios.")
Q("wr2", "warn", "Are hazard warning lights compulsory on a motorcycle?", "¿Es obligatoria la luz de emergencia en una motocicleta?",
  [("No, optional", "No, opcional"), ("Yes, as on all automobiles", "Sí, como en todos los automóviles"), ("Only above 125 cm³", "Solo de más de 125 cm³")],
  "Compulsory on other automobiles.", "Obligatoria en los demás automóviles.")
Q("wr3", "warn", "The hazard warning lights consist of…", "La luz de emergencia consiste en…",
  [("all indicators flashing at the same time", "el funcionamiento simultáneo de todos los intermitentes"), ("the brake light flashing", "la luz de freno intermitente"), ("the main beam flashing", "ráfagas de la luz larga")],
  "With a flashing red tell-tale.", "Con un testigo rojo intermitente.")
Q("wr4", "warn", "To warn that you are going to brake hard, you…", "Para avisar de que vas a frenar considerablemente…",
  [("use the brake light repeatedly, when possible", "usas la luz de freno de forma reiterada, si es posible"), ("switch on the rear fog light", "enciendes la antiniebla trasera"), ("sound the horn", "tocas el claxon")],
  "Or move your arm up and down.", "O mueves el brazo de arriba abajo.")
Q("wr5", "warn", "Is a reversing light compulsory on a motorcycle?", "¿Es obligatoria la luz de marcha atrás en una moto?",
  [("No, optional", "No, opcional"), ("Yes", "Sí"), ("Only with sidecar", "Solo con sidecar")],
  "White, at the rear.", "Blanca, en la parte trasera.")
Q("wr6", "warn", "The rear number-plate light comes on…", "La luz de la placa de matrícula se enciende…",
  [("automatically with the position lights", "automáticamente con las luces de posición"), ("only with the main beam", "solo con la luz larga"), ("only when braking", "solo al frenar")],
  "So the plate can be read at night.", "Para que la placa se lea de noche.")
Q("wr7", "warn", "The brake light lights up when you use…", "La luz de freno se enciende al usar…",
  [("the front brake, the rear brake or both", "el freno delantero, el trasero o ambos"), ("only the rear brake", "solo el freno trasero"), ("only the engine brake", "solo el freno motor")],
  "It tells those behind you are braking.", "Indica a los de detrás que estás frenando.")

# ---------------------------------------------------------------- more practice
Q("pu6", "purpose", "Between sunset and sunrise, must every vehicle on the road have its lights on?", "Entre el ocaso y la salida del sol, ¿deben llevar las luces encendidas todos los vehículos que circulen?",
  [("Yes, the lights that correspond", "Sí, el alumbrado que corresponda"), ("Only out of town", "Solo fuera de poblado"), ("Only on poorly lit roads", "Solo en vías mal iluminadas")],
  "And at any time in tunnels.", "Y a cualquier hora en túneles.")
Q("ps8", "position", "What colour is a motorcycle’s rear position light?", "¿De qué color es la luz de posición trasera de una moto?",
  [("Red", "Roja"), ("White", "Blanca"), ("Amber", "Amarillo auto")],
  "Front: white.", "Delante: blanca.")
Q("rf5", "reflect", "A motorcycle with a sidecar may have at the rear…", "Una motocicleta con sidecar puede llevar detrás…",
  [("two symmetrical red reflectors", "dos catadióptricos rojos simétricos"), ("one amber reflector", "un catadióptrico amarillo auto"), ("no reflectors", "ningún catadióptrico")],
  "Without sidecar: one.", "Sin sidecar: uno.")
Q("dp6", "dipped", "In town at night, on a well-lit street, your motorcycle has on…", "En poblado de noche, por una calle bien iluminada, tu moto lleva…",
  [("dipped beam and position lights", "luz de cruce y de posición"), ("only position lights", "solo la de posición"), ("main beam", "la luz de carretera")],
  "Main beam is forbidden in town.", "La larga está prohibida en poblado.")
Q("mb7", "main", "What colour is the main beam?", "¿De qué color es la luz de carretera?",
  [("White", "Blanca"), ("Selective yellow", "Amarillo selectivo"), ("Blue", "Azul")],
  "More intense than the dipped beam.", "Más intensa que la de cruce.")
Q("sp4", "special", "A reversible lane at night, a contraflow lane by day: which light in both cases?", "Carril reversible de noche y carril en sentido contrario de día: ¿qué luz en ambos casos?",
  [("At least the dipped beam", "Al menos la de cruce"), ("Hazard lights", "La luz de emergencia"), ("Front fog lights", "La antiniebla delantera")],
  "Day and night.", "De día y de noche.")
Q("sp5", "special", "Is a two-way road with three lanes separated by broken lines one of the cases requiring dipped beam by day for every vehicle?", "¿Una vía de doble sentido con tres carriles separados por discontinuas obliga a todos a llevar cruce de día?",
  [("No, only reversible, additional and contraflow lanes", "No, solo carriles reversibles, adicionales y en sentido contrario"), ("Yes", "Sí"), ("Only in the centre lane", "Solo en el carril central")],
  "On a motorcycle you have it on anyway.", "En moto ya la llevas igualmente.")
Q("wr8", "warn", "The hazard lights warn of…", "La luz de emergencia advierte del…",
  [("the danger of the vehicle, stopped or moving, because of an emergency", "peligro del vehículo, inmovilizado o en movimiento, por una emergencia"), ("a turn", "un giro"), ("braking", "un frenado")],
  "Breakdown, accident…", "Avería, accidente…")
