# -*- coding: utf-8 -*-
"""Question bank for the interactive Topic 7 page (vehicle lights). In every question the FIRST option is the
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
        recap=[("Lights show the vehicle (be seen), light the road (see and be seen) and warn others.", "Las luces indican la presencia (ser vistos), alumbran (ver y ser vistos) y avisan."),
               ("Lights on from sunset to sunrise, and at any time in tunnels, underpasses and “Tunnel” stretches.", "Alumbrado entre el ocaso y la salida del sol, y a cualquier hora en túneles, pasos inferiores y tramos «Túnel»."),
               ("Poorly lit road: can’t read a plate at 10 m or see a dark car at 50 m.", "Vía mal iluminada: no se lee una matrícula a 10 m o no se distingue un vehículo oscuro a 50 m."),
               ("Paired lights match in colour and intensity; no extra or flashing lights; with a weaker light after a breakdown, slow down to stop within the lit area.",
                "Luces dobles iguales en color e intensidad; ni luces de más ni intermitentes; con una luz más débil por avería, reducir hasta poder parar en la zona iluminada.")],
        trap=("Swapping 10 m (plate) and 50 m (dark vehicle).", "Intercambiar 10 m (matrícula) y 50 m (vehículo oscuro).")),
    "position": dict(sec=2, en="Position lights", es="Luces de posición",
        recap=[("Front white, rear red: presence and width. Side amber (red next to the rear ones): presence.", "Delanteras blancas, traseras rojas: presencia y anchura. Laterales amarillo auto (rojas junto a las traseras): presencia."),
               ("Cars 2 + 2; motorcycles 1 or 2; trailers 2 front if wider than 1.60 m, 2 side if longer than 6 m.", "Turismos 2 + 2; motos 1 o 2; remolques 2 delante si miden más de 1,60 m de ancho, 2 laterales si más de 6 m de largo."),
               ("At night or poor visibility: on when stopped on carriageway or shoulder, parked on a non-usable interurban shoulder, in a dark travesía, or on a dark urban street.",
                "De noche o con poca visibilidad: detenido en calzada o arcén, estacionado en arcén no transitable de interurbana, en travesía o vía urbana mal iluminadas."),
               ("They come on automatically with dipped, main or fog lights.", "Se encienden automáticamente con las de cruce, carretera o antiniebla.")],
        trap=("Thinking position lights light the road.", "Pensar que la luz de posición alumbra la vía.")),
    "parking": dict(sec=2, en="Parking lights", es="Luz de estacionamiento",
        recap=[("May replace position lights when parked in a poorly lit travesía.", "Puede sustituir a la de posición estacionado en travesía mal iluminada."),
               ("Two white in front, two red behind, where the position lights are.", "Dos blancas delante y dos rojas detrás, coincidiendo con las de posición."),
               ("Usually only the pair on the traffic side is lit.", "Normalmente solo se enciende la pareja del lado de la calzada."),
               ("Optional up to 6 m long and 2 m wide; forbidden on bigger vehicles.", "Opcional hasta 6 m de largo y 2 m de ancho; prohibida en vehículos mayores.")],
        trap=("Thinking lorries may use parking lights.", "Pensar que los camiones pueden usar luz de estacionamiento.")),
    "reflectors": dict(sec=2, en="Reflectors", es="Catadióptricos",
        recap=[("No light of their own: they reflect light from another source.", "Sin luz propia: reflejan la luz de otra fuente."),
               ("Front white, rear red, side amber (red if next to the rear one); never triangular, except…", "Delanteros blancos, traseros rojos, laterales amarillo auto (rojos junto al trasero); nunca triangulares, salvo…"),
               ("…the rear reflectors of trailers and semitrailers, which are triangular.", "…los traseros de remolques y semirremolques, que son triangulares."),
               ("Rear compulsory for VMP, mopeds, automobiles; front and side for VMP, trailers, semitrailers.", "Traseros obligatorios en VMP, ciclomotores y automóviles; delanteros y laterales en VMP, remolques y semirremolques.")],
        trap=("Putting triangular reflectors on a car.", "Poner catadióptricos triangulares en un turismo.")),
    "galibo": dict(sec=2, en="Clearance lights", es="Luz de gálibo",
        recap=[("Show the vehicle’s width and, with the position lights, its size.", "Indica la anchura y, con la de posición, el volumen del vehículo."),
               ("Two white in front, two red behind.", "Dos blancas delante, dos rojas detrás."),
               ("Compulsory over 2.10 m wide.", "Obligatoria a más de 2,10 m de ancho."),
               ("Optional between 1.80 and 2.10 m.", "Opcional entre 1,80 y 2,10 m.")],
        trap=("Mixing up 2.10 m (clearance lights) with 2 m (parking light).", "Confundir 2,10 m (gálibo) con 2 m (estacionamiento).")),
    "dipped": dict(sec=3, en="Dipped beam", es="Luz de cruce",
        recap=[("White; lights the road ahead without dazzling. The light for meeting other users.", "Blanca; alumbra delante sin deslumbrar. Es la luz para cruzarse."),
               ("Night: every road in town, however lit; out of town if well lit.", "De noche: toda vía en poblado, con independencia de su iluminación; en interurbana, si está bien iluminada."),
               ("Any time: well-lit tunnels and underpasses. Motorcycles: always, day and night.", "A cualquier hora: túneles y pasos inferiores bien iluminados. Motos: siempre, de día y de noche."),
               ("Always together with the position lights. Cars 2; two-wheelers 1 or 2.", "Siempre con la de posición. Automóviles 2; motos 1 o 2.")],
        trap=("Using main beam in a dark town street.", "Usar la luz larga en una calle oscura de un poblado.")),
    "main": dict(sec=3, en="Main beam", es="Luz de carretera",
        recap=[("White and stronger; lights far ahead.", "Blanca y más intensa; alumbra a larga distancia."),
               ("Compulsory above 40 km/h on dark interurban roads at night, and in dark tunnels at any time.", "Obligatoria a más de 40 km/h en interurbanas oscuras de noche y en túneles oscuros a cualquier hora."),
               ("Dipped instead if it could dazzle; at 40 km/h or less, either.", "La de cruce si puede deslumbrar; a 40 km/h o menos, cualquiera."),
               ("Forbidden when stopped or parked, and in town. Cars carry an even number.", "Prohibida parado o estacionado y en poblado. Los automóviles llevan un número par.")],
        trap=("Thinking main beam is compulsory at any speed on dark roads.", "Pensar que la luz larga es obligatoria a cualquier velocidad en vías oscuras.")),
    "fog": dict(sec=3, en="Fog lights", es="Luces antiniebla",
        recap=[("Front: optional, white or selective yellow, only with position lights on; MAY be used in bad weather and on narrow winding roads (≤ 6.50 m with bends sign).",
                "Delantera: opcional, blanca o amarillo selectivo, solo con la de posición; se PUEDE usar con mal tiempo y en vías estrechas con curvas (≤ 6,50 m con señal)."),
               ("Rear: compulsory (not motorcycles or three-wheelers), red, only with dipped, main or front fog on.", "Trasera: obligatoria (salvo motos y tres ruedas), roja, solo con cruce, carretera o antiniebla delantera."),
               ("Rear MUST be used only in especially bad conditions: thick fog, very heavy rain, heavy snow, dense dust or smoke.", "La trasera se DEBE usar solo con condiciones especialmente adversas: niebla espesa, lluvia muy intensa, nevada fuerte, nubes densas."),
               ("Tell-tales: rear amber (compulsory), front green (optional). Bad-weather minimum: day position + any; night position + dipped.",
                "Testigos: trasera amarillo auto (obligatorio), delantera verde (opcional). Mínimo con mal tiempo: de día posición + cualquiera; de noche posición + cruce.")],
        trap=("Switching on the rear fog light in light rain or on a winding road.", "Encender la antiniebla trasera con lluvia ligera o en una vía con curvas.")),
    "special": dict(sec=3, en="Lanes where lights are always on", es="Situaciones especiales",
        recap=[("At least dipped beam, day and night, on a reversible lane.", "Al menos luz de cruce, de día y de noche, en carril reversible."),
               ("Also on roads with a temporary additional lane.", "También en vías con carril adicional circunstancial."),
               ("And on a contraflow lane and the normal lane next to it.", "Y en el carril en sentido contrario y en el normal contiguo."),
               ("Cyclists on interurban roads when lights are compulsory: a luminous or reflective element visible at 150 m.", "Ciclistas en interurbanas con alumbrado obligatorio: un elemento luminoso o reflectante visible a 150 m.")],
        trap=("Thinking these lights are only needed at night.", "Pensar que estas luces solo hacen falta de noche.")),
    "dazzle": dict(sec=3, en="Not dazzling others", es="Evitar deslumbrar",
        recap=[("Dip as soon as you could dazzle anyone: oncoming drivers (even if they don’t) and drivers ahead via mirrors.", "Poner la de cruce en cuanto se pueda deslumbrar: a los de frente (aunque ellos no lo hagan) y a los de delante por los espejos."),
               ("Overtaking: main beam only once level; then the overtaken car dips.", "Al adelantar: luz larga solo en paralelo; entonces el adelantado pone la de cruce."),
               ("Bends: the driver whose road turns right dips first.", "Curvas: cambia primero quien toma la curva a la derecha."),
               ("Aim the headlights and place the load well, or even dipped beams dazzle.", "Faros bien reglados y carga bien colocada, o deslumbra incluso la de cruce.")],
        trap=("Keeping main beam on because the oncoming driver did not dip.", "Mantener la luz larga porque el de enfrente no la ha quitado.")),
    "dazzled": dict(sec=3, en="When you are dazzled", es="Cuando te deslumbran",
        recap=[("Dazzle is a temporary blindness.", "El deslumbramiento es una ceguera temporal."),
               ("Oncoming: look right, along the line between carriageway and shoulder; close the left eye.", "De frente: mirar a la derecha, guiándose por la línea entre calzada y arcén; cerrar el ojo izquierdo."),
               ("From behind: adjust the mirror or change position.", "Por detrás: cambiar la orientación del espejo o la posición."),
               ("Slow down, even stop, without moving onto the shoulder.", "Reducir, incluso parar, sin salir al arcén.")],
        trap=("Pulling onto the shoulder when dazzled.", "Salir al arcén al ser deslumbrado.")),
    "hazard": dict(sec=4, en="Indicators and hazard lights", es="Intermitentes y luz de emergencia",
        recap=[("Indicators: amber, any sideways manoeuvre; compulsory on motor vehicles and trailers.", "Intermitentes: amarillo auto, toda maniobra con desplazamiento lateral; obligatorios en vehículos de motor y remolques."),
               ("Hazard lights: all indicators together; compulsory on automobiles, optional on motorcycles; flashing red tell-tale.", "Emergencia: todos los intermitentes a la vez; obligatoria en automóviles, opcional en motos; testigo rojo intermitente."),
               ("Use: immobilised on motorways or in poor visibility, in tunnels, below the minimum speed, any emergency, school transport stops, non-priority emergency trips.",
                "Uso: inmovilizado en autopista o con poca visibilidad, en túneles, sin alcanzar la mínima, emergencias, paradas de transporte escolar, urgencias no prioritarias."),
               ("Not a substitute for the V-16; not for double parking.", "No sustituye a la V-16; no vale para la doble fila.")],
        trap=("Using hazard lights to park in a double row.", "Usar la luz de emergencia para parar en doble fila.")),
    "brake": dict(sec=4, en="Brake and reversing lights", es="Luz de freno y de marcha atrás",
        recap=[("Brake lights: show the service brake is used; most cars add a high third brake light.", "Freno: indica que se usa el freno de servicio; la mayoría lleva una tercera luz más alta."),
               ("Use them repeatedly to warn you will stop or brake hard.", "Usarla de forma reiterada para avisar de que se va a parar o frenar mucho."),
               ("Reversing light: white, comes on with reverse and the ignition on, even with the engine off.", "Marcha atrás: blanca, se enciende con la marcha atrás y el contacto, aun con el motor parado."),
               ("Compulsory on automobiles (not motorcycles), optional on trailers.", "Obligatoria en automóviles (no motos), opcional en remolques.")],
        trap=("Thinking the reversing light only works with the engine running.", "Pensar que la luz de marcha atrás solo funciona con el motor en marcha.")),
    "other": dict(sec=5, en="Other lights", es="Otras luces",
        recap=[("Interior lighting compulsory in public passenger vehicles and hire cars with driver.", "Alumbrado interior obligatorio en vehículos de servicio público de viajeros y de alquiler con conductor."),
               ("It must not dazzle or bother other road users.", "No debe deslumbrar ni molestar a los demás usuarios."),
               ("Rear number-plate light comes on automatically with the position lights.", "La luz de la matrícula trasera se enciende automáticamente con la de posición."),
               ("So does the SP plate light, if the vehicle has one.", "También la de la placa SP, si la lleva.")],
        trap=("Thinking the plate light has its own switch.", "Pensar que la luz de la matrícula tiene interruptor propio.")),
}


# ---------------------------------------------------------------- 1. purpose
Q("pu1", "purpose", "Vehicle lights are for…", "Las luces del vehículo sirven para…",
  [("showing the vehicle, lighting the road and warning others", "indicar la presencia, alumbrar la vía y avisar a los demás"), ("lighting the road only", "solo alumbrar la vía"), ("decoration", "decorar")],
  "Be seen; see and be seen; signal and be seen.", "Ser vistos; ver y ser vistos; señalizar y ser vistos.")
Q("pu2", "purpose", "A road is considered poorly lit when you cannot…", "Una vía se considera insuficientemente iluminada cuando no se puede…",
  [("read a number plate at 10 m or make out a dark car at 50 m", "leer una matrícula a 10 m o distinguir un vehículo oscuro a 50 m"), ("see a pedestrian at 100 m", "ver a un peatón a 100 m"),
   ("read a road sign at 50 m", "leer una señal a 50 m")],
  "Both measures are in the definition.", "Las dos medidas forman parte de la definición.")
Q("pu3", "purpose", "In a tunnel at midday you must…", "En un túnel a mediodía debes…",
  [("have the right lights on", "llevar encendido el alumbrado correspondiente"), ("drive without lights, it is daytime", "circular sin luces, es de día"), ("use only the hazard lights", "usar solo la luz de emergencia")],
  "At any time of day in tunnels, underpasses and “Tunnel” stretches.", "A cualquier hora en túneles, pasos inferiores y tramos «Túnel».")
Q("pu4", "purpose", "A headlight fails beyond repair and you must drive with a weaker light. You…", "Se avería un faro sin arreglo y debes circular con una luz más débil. Tú…",
  [("slow down until you can stop within the lit area", "reduces la velocidad hasta poder detenerte en la zona iluminada"), ("keep your speed", "mantienes la velocidad"), ("switch on the hazard lights and carry on", "pones la emergencia y sigues")],
  "Your speed must match what you can see.", "La velocidad debe ajustarse a lo que se ve.")
Q("pu5", "purpose", "Paired lights with the same purpose must be…", "Las luces dobles con la misma finalidad deben ser…",
  [("the same colour and intensity, placed symmetrically", "del mismo color e intensidad y simétricas"), ("different colours, to tell them apart", "de colores distintos, para diferenciarlas"), ("one fixed, one flashing", "una fija y otra intermitente")],
  "If possible at the same distance from the edges.", "A ser posible a la misma distancia de los bordes.")
Q("pu6", "purpose", "Fitting extra lights or reflective paint not authorised is…", "Instalar luces de más o pinturas reflectantes no autorizadas está…",
  [("forbidden", "prohibido"), ("allowed if they are white", "permitido si son blancas"), ("allowed on trailers", "permitido en remolques")],
  "Only the lights the rules allow.", "Solo las luces autorizadas reglamentariamente.")

# ---------------------------------------------------------------- 2.1 position
Q("ps1", "position", "Front position lights are…", "Las luces de posición delanteras son…",
  [("white", "blancas"), ("amber", "amarillo auto"), ("red", "rojas")],
  "Rear ones are red.", "Las traseras son rojas.")
Q("ps2", "position", "Front and rear position lights show…", "Las luces de posición delanteras y traseras indican…",
  [("the vehicle’s presence and width", "la presencia y la anchura del vehículo"), ("its speed", "su velocidad"), ("that it is braking", "que está frenando")],
  "Side position lights show its presence.", "Las laterales indican su presencia.")
Q("ps3", "position", "Side position lights are…", "Las luces de posición laterales son…",
  [("amber, or red when next to the rear lights", "amarillo auto, o rojas si están junto a las traseras"), ("white", "blancas"), ("blue", "azules")],
  "Compulsory on trailers longer than 6 m (at least 2).", "Obligatorias en remolques de más de 6 m (al menos 2).")
Q("ps4", "position", "At night you park on the non-usable shoulder of an interurban road. You leave on…", "De noche estacionas en el arcén no transitable de una vía interurbana. Dejas encendidas…",
  [("the position lights", "las luces de posición"), ("the dipped beam", "la luz de cruce"), ("no lights", "ninguna luz")],
  "So others can see you.", "Para que te vean los demás.")
Q("ps5", "position", "Front position lights on a trailer are compulsory when it is wider than…", "La luz de posición delantera es obligatoria en remolques de anchura superior a…",
  [("1.60 m", "1,60 m"), ("2.10 m", "2,10 m"), ("2.55 m", "2,55 m")],
  "Optional for narrower ones.", "Opcional en los más estrechos.")
Q("ps6", "position", "When you switch on the dipped beam, the position lights…", "Al encender la luz de cruce, las luces de posición…",
  [("come on automatically", "se encienden automáticamente"), ("must be switched on separately", "deben encenderse aparte"), ("switch off", "se apagan")],
  "Also with main beam or fog lights.", "También con la de carretera o la antiniebla.")
Q("ps7", "position", "How many rear position lights must a car have?", "¿Cuántas luces de posición traseras debe tener un turismo?",
  [("2", "2"), ("1 or 2", "1 o 2"), ("4", "4")],
  "Motorcycles: 1 or 2.", "Motocicletas: 1 o 2.")

# ---------------------------------------------------------------- 2.2 parking
Q("pk1", "parking", "Parking lights may replace position lights when the vehicle is…", "La luz de estacionamiento puede sustituir a la de posición cuando el vehículo está…",
  [("parked in a poorly lit travesía", "estacionado en una travesía insuficientemente iluminada"), ("moving slowly", "circulando despacio"), ("stopped on a motorway", "detenido en una autopista")],
  "Usually only the pair on the traffic side is lit.", "Normalmente solo se enciende la pareja del lado de la calzada.")
Q("pk2", "parking", "Parking lights are allowed on vehicles up to…", "La luz de estacionamiento se permite en vehículos de hasta…",
  [("6 m long and 2 m wide", "6 m de largo y 2 m de ancho"), ("12 m long and 2.55 m wide", "12 m de largo y 2,55 m de ancho"), ("3,500 kg", "3.500 kg")],
  "Forbidden on larger vehicles.", "Prohibida en los demás.")
Q("pk3", "parking", "Parking lights are…", "La luz de estacionamiento son…",
  [("two white in front and two red behind", "dos blancas delante y dos rojas detrás"), ("two amber on each side", "dos amarillas a cada lado"), ("one red on the roof", "una roja en el techo")],
  "In the same place as the position lights.", "Coincidiendo con las de posición.")

# ---------------------------------------------------------------- 2.3 reflectors
Q("rf1", "reflectors", "Reflectors (catadióptricos)…", "Los catadióptricos…",
  [("have no light of their own; they reflect other light", "no tienen luz propia; reflejan la de otra fuente"), ("light up when the engine runs", "se iluminan con el motor en marcha"), ("flash when braking", "parpadean al frenar")],
  "The observer is near the light source.", "El observador está cerca de la fuente de luz.")
Q("rf2", "reflectors", "Triangular reflectors are reserved for…", "Los catadióptricos triangulares están reservados a…",
  [("the rear of trailers and semitrailers", "la parte trasera de remolques y semirremolques"), ("the rear of cars", "la parte trasera de los turismos"), ("motorcycles", "las motocicletas")],
  "On any other vehicle, never triangular.", "En cualquier otro vehículo, nunca triangulares.")
Q("rf3", "reflectors", "Front reflectors are…", "Los catadióptricos delanteros son…",
  [("white", "blancos"), ("red", "rojos"), ("amber", "amarillo auto")],
  "Compulsory for VMP, trailers and semitrailers.", "Obligatorios para VMP, remolques y semirremolques.")
Q("rf4", "reflectors", "Rear reflectors are compulsory for…", "Los catadióptricos traseros son obligatorios para…",
  [("VMP, mopeds and automobiles", "VMP, ciclomotores y automóviles"), ("trailers only", "solo remolques"), ("no vehicle", "ningún vehículo")],
  "Red, never triangular on these vehicles.", "Rojos, nunca triangulares en estos vehículos.")
Q("rf5", "reflectors", "Side reflectors are…", "Los catadióptricos laterales son…",
  [("amber, not triangular (red if next to the rear one)", "amarillo auto, no triangulares (rojos junto al trasero)"), ("white", "blancos"), ("blue", "azules")],
  "Compulsory for VMP, trailers and semitrailers.", "Obligatorios para VMP, remolques y semirremolques.")
Q("rf6", "reflectors", "Are other retroreflective plates on a vehicle (V-6, V-20…) reflectors?", "¿Las demás placas retrorreflectantes del vehículo (V-6, V-20…) son catadióptricos?",
  [("No", "No"), ("Yes", "Sí"), ("Only at night", "Solo de noche")],
  "Reflectors are specific devices.", "Los catadióptricos son dispositivos específicos.")

# ---------------------------------------------------------------- 2.4 clearance
Q("gb1", "galibo", "Clearance lights (luz de gálibo) are compulsory for vehicles wider than…", "La luz de gálibo es obligatoria en vehículos de anchura superior a…",
  [("2.10 m", "2,10 m"), ("1.80 m", "1,80 m"), ("2.55 m", "2,55 m")],
  "Optional between 1.80 and 2.10 m.", "Opcional entre 1,80 y 2,10 m.")
Q("gb2", "galibo", "Clearance lights show…", "La luz de gálibo indica…",
  [("the vehicle’s width", "la anchura del vehículo"), ("its speed", "su velocidad"), ("that it is reversing", "que va marcha atrás")],
  "With the position lights, its size.", "Con la de posición, su volumen.")
Q("gb3", "galibo", "Clearance lights are…", "Las luces de gálibo son…",
  [("two white in front and two red behind", "dos blancas delante y dos rojas detrás"), ("amber all round", "amarillas en todo el contorno"), ("one blue on the roof", "una azul en el techo")],
  "Placed high, at the corners.", "En la parte alta, en las esquinas.")
Q("gb4", "galibo", "A van 1.95 m wide: clearance lights are…", "Una furgoneta de 1,95 m de ancho: la luz de gálibo es…",
  [("optional", "opcional"), ("compulsory", "obligatoria"), ("forbidden", "prohibida")],
  "Between 1.80 and 2.10 m.", "Entre 1,80 y 2,10 m.")

# ---------------------------------------------------------------- 3.1 dipped
Q("dp1", "dipped", "At night on a well-lit town street you use…", "De noche en una calle bien iluminada de un poblado usas…",
  [("dipped beam and position lights", "luz de cruce y de posición"), ("position lights only", "solo la de posición"), ("no lights, the street is lit", "ninguna, la calle está iluminada")],
  "In town, whatever the lighting.", "En poblado, con independencia de su iluminación.")
Q("dp2", "dipped", "A motorcycle on a public road by day must use…", "Una motocicleta por una vía pública de día debe llevar…",
  [("the dipped beam", "la luz de cruce"), ("no lights", "ninguna luz"), ("the main beam", "la luz de carretera")],
  "Motorcycles: dipped beam at any time of day.", "Motocicletas: luz de cruce a cualquier hora.")
Q("dp3", "dipped", "At night on a well-lit interurban road you use…", "De noche en una vía interurbana suficientemente iluminada usas…",
  [("the dipped beam", "la luz de cruce"), ("the main beam", "la luz de carretera"), ("the fog lights", "las antiniebla")],
  "Main beam is for poorly lit roads above 40 km/h.", "La larga es para vías mal iluminadas a más de 40 km/h.")
Q("dp4", "dipped", "In a well-lit tunnel by day you use…", "En un túnel bien iluminado de día usas…",
  [("the dipped beam", "la luz de cruce"), ("the position lights only", "solo la de posición"), ("the main beam", "la luz de carretera")],
  "At any time of day.", "A cualquier hora del día.")
Q("dp5", "dipped", "When you meet another road user at night, you use…", "Cuando te cruzas con otro usuario de noche, usas…",
  [("the dipped beam", "la luz de cruce"), ("the main beam", "la luz de carretera"), ("the hazard lights", "la luz de emergencia")],
  "So as not to dazzle.", "Para no deslumbrar.")
Q("dp6", "dipped", "How many dipped-beam headlights must a car have?", "¿Cuántas luces de cruce debe tener un turismo?",
  [("2", "2"), ("1 or 2", "1 o 2"), ("an even number", "un número par")],
  "Mopeds, motorcycles, three-wheelers and quadricycles: 1 or 2.", "Ciclomotores, motos, tres ruedas y cuadriciclos: 1 o 2.")

# ---------------------------------------------------------------- 3.2 main
Q("mb1", "main", "On a dark interurban road at night, the main beam is compulsory above…", "En una interurbana oscura de noche, la luz de carretera es obligatoria a más de…",
  [("40 km/h", "40 km/h"), ("60 km/h", "60 km/h"), ("90 km/h", "90 km/h")],
  "At 40 km/h or less, either beam.", "A 40 km/h o menos, cualquiera.")
Q("mb2", "main", "Is main beam allowed in town?", "¿Se permite la luz de carretera en poblado?",
  [("No, it is forbidden", "No, está prohibida"), ("Yes, on dark streets", "Sí, en calles oscuras"), ("Yes, above 40 km/h", "Sí, a más de 40 km/h")],
  "Also forbidden with the vehicle stopped or parked.", "También prohibida parado o estacionado.")
Q("mb3", "main", "On a dark road at 30 km/h at night, you may use…", "En una vía oscura a 30 km/h de noche, puedes usar…",
  [("either the dipped or the main beam", "la luz de cruce o la de carretera"), ("only the main beam", "solo la de carretera"), ("only the position lights", "solo la de posición")],
  "At 40 km/h or less, you choose.", "A 40 km/h o menos, a elección.")
Q("mb4", "main", "In a poorly lit tunnel at 80 km/h by day, you use…", "En un túnel mal iluminado a 80 km/h de día usas…",
  [("the main beam, dipping if you could dazzle", "la luz de carretera, cambiando a la de cruce si puedes deslumbrar"), ("position lights only", "solo la de posición"), ("no lights", "ninguna luz")],
  "At any time of day in poorly lit tunnels.", "A cualquier hora en túneles mal iluminados.")
Q("mb5", "main", "A car must carry main-beam headlights in…", "Un automóvil debe llevar luces de carretera en…",
  [("an even number", "número par"), ("any number", "cualquier número"), ("exactly one", "una sola")],
  "Motorcycles, three-wheelers and quadricycles: 1 or 2.", "Motos, tres ruedas y cuadriciclos: 1 o 2.")
Q("mb6", "main", "With the vehicle parked, the main beam is…", "Con el vehículo estacionado, la luz de carretera está…",
  [("forbidden", "prohibida"), ("allowed to light the area", "permitida para alumbrar la zona"), ("compulsory at night", "obligatoria de noche")],
  "Stopped or parked: never main beam.", "Parado o estacionado: nunca luz larga.")

# ---------------------------------------------------------------- 3.3 fog
Q("fg1", "fog", "Front fog lights can only be switched on when…", "La antiniebla delantera solo se puede encender si…",
  [("the position lights are on", "está encendida la luz de posición"), ("the main beam is on", "está encendida la de carretera"), ("it is night", "es de noche")],
  "Alone or with dipped or even main beam.", "Sola o con la de cruce o incluso la de carretera.")
Q("fg2", "fog", "The rear fog light can only be switched on when…", "La antiniebla trasera solo se puede encender si…",
  [("the dipped, main or front fog lights are on", "está encendida la de cruce, carretera o antiniebla delantera"), ("the position lights alone are on", "solo está la de posición"), ("the engine is off", "el motor está apagado")],
  "Its tell-tale is amber and compulsory.", "Su testigo es amarillo auto y obligatorio.")
Q("fg3", "fog", "On a narrow winding road (≤ 6.50 m, “dangerous bends” sign) in clear weather, you may use…", "En una vía estrecha con curvas (≤ 6,50 m, señal «curvas peligrosas») con buen tiempo, puedes usar…",
  [("the front fog lights, but not the rear one", "la antiniebla delantera, pero no la trasera"), ("both fog lights", "las dos antiniebla"), ("the rear fog light only", "solo la antiniebla trasera")],
  "The rear one is only for especially bad weather.", "La trasera es solo para condiciones especialmente adversas.")
Q("fg4", "fog", "You must switch on the rear fog light in…", "Debes encender la antiniebla trasera con…",
  [("thick fog", "niebla espesa"), ("light rain", "lluvia ligera"), ("a cloudy day", "un día nublado")],
  "Also very heavy rain, heavy snow, dense dust or smoke.", "También lluvia muy intensa, nevada fuerte, nubes densas de polvo o humo.")
Q("fg5", "fog", "Front fog lights are…", "La antiniebla delantera es…",
  [("optional on all motor vehicles", "opcional en todos los vehículos de motor"), ("compulsory on cars", "obligatoria en turismos"), ("forbidden on motorcycles", "prohibida en motocicletas")],
  "White or selective yellow.", "Blanca o amarillo selectivo.")
Q("fg6", "fog", "The rear fog light is compulsory on…", "La antiniebla trasera es obligatoria en…",
  [("motor vehicles (not motorcycles or three-wheelers), trailers and semitrailers", "vehículos de motor (salvo motos y tres ruedas), remolques y semirremolques"),
   ("motorcycles only", "solo motocicletas"), ("no vehicle", "ningún vehículo")],
  "One or two, red.", "Una o dos, rojas.")
Q("fg7", "fog", "In heavy rain by day, the minimum lighting is…", "Con lluvia intensa de día, el alumbrado mínimo es…",
  [("position lights plus any lighting light (fog, dipped or main)", "la de posición más cualquier luz de alumbrado (antiniebla, cruce o carretera)"), ("no lights, it is daytime", "ninguna, es de día"), ("hazard lights", "la de emergencia")],
  "At night: at least position and dipped.", "De noche: al menos posición y cruce.")
Q("fg8", "fog", "The dashboard light for the rear fog light is…", "El testigo de la antiniebla trasera es…",
  [("amber, not flashing, and compulsory", "amarillo auto, no intermitente y obligatorio"), ("green and optional", "verde y opcional"), ("flashing red", "rojo intermitente")],
  "Front fog: green, optional.", "Antiniebla delantera: verde, opcional.")

# ---------------------------------------------------------------- 3.4 special
Q("sp1", "special", "Driving on a reversible lane at midday, you must have on at least…", "Circulando por un carril reversible a mediodía, debes llevar al menos…",
  [("the dipped beam", "la luz de cruce"), ("no lights, it is daytime", "ninguna, es de día"), ("the hazard lights", "la de emergencia")],
  "Day and night.", "De día y de noche.")
Q("sp2", "special", "Driving in the normal lane next to a contraflow lane by day, you…", "Por el carril normal contiguo a uno en sentido contrario, de día, tú…",
  [("must have at least the dipped beam on", "debes llevar al menos la luz de cruce"), ("need no lights", "no necesitas luces"), ("must use the main beam", "debes usar la de carretera")],
  "Same on the contraflow lane itself and on temporary additional lanes.", "Igual en el propio carril en sentido contrario y en el adicional circunstancial.")
Q("sp3", "special", "A cyclist on an interurban road at night must also use…", "Un ciclista por una interurbana de noche debe usar además…",
  [("at least one luminous or reflective element visible from 150 m", "al menos un elemento luminoso o reflectante visible a 150 m"), ("a reflective element visible from 50 m", "un elemento reflectante visible a 50 m"), ("a V-16", "una V-16")],
  "Whenever lights are compulsory (art. 118.2 since October 2026): a light or a reflective item, as long as it is visible from 150 m.",
  "Siempre que el alumbrado sea obligatorio (art. 118.2 desde octubre de 2026): una luz o un elemento reflectante, siempre que sea visible a 150 m.")
Q("sp4", "special", "On a road with a temporary additional lane, lights are needed…", "En una vía con carril adicional circunstancial, el alumbrado es necesario…",
  [("day and night: at least dipped beam", "de día y de noche: al menos la de cruce"), ("only at night", "solo de noche"), ("never", "nunca")],
  "Because traffic flows unusually close.", "Porque el tráfico circula de forma excepcional.")

# ---------------------------------------------------------------- 3.5 dazzle (avoid)
Q("dz1", "dazzle", "An oncoming driver keeps their main beam on. You…", "Un conductor que viene de frente no quita la luz larga. Tú…",
  [("switch to dipped beam anyway", "pones la luz de cruce igualmente"), ("keep your main beam on too", "mantienes también la larga"), ("flash your lights repeatedly", "le das ráfagas repetidas")],
  "Even if they do not dip.", "Aunque ellos no cumplan.")
Q("dz2", "dazzle", "Following a car closely at night, you should…", "Siguiendo de cerca a un coche de noche, debes…",
  [("use the dipped beam so as not to dazzle via the mirrors", "usar la luz de cruce para no deslumbrar por los espejos"), ("use the main beam to see better", "usar la larga para ver mejor"), ("switch off the lights", "apagar las luces")],
  "Mirrors reflect your main beam into the driver’s eyes.", "Los espejos reflejan tu luz larga en sus ojos.")
Q("dz3", "dazzle", "Overtaking at night, when may you switch on the main beam?", "Adelantando de noche, ¿cuándo puedes poner la luz larga?",
  [("Once you are level with the overtaken vehicle", "Al estar en paralelo con el adelantado"), ("As soon as you pull out", "En cuanto sales a adelantar"), ("Never while overtaking", "Nunca durante el adelantamiento")],
  "At that moment the overtaken driver dips.", "En ese momento el adelantado pone la de cruce.")
Q("dz4", "dazzle", "While being overtaken at night, you switch to dipped beam…", "Mientras te adelantan de noche, pones la luz de cruce…",
  [("when the overtaking car is level with you", "cuando el que adelanta está en paralelo contigo"), ("never", "nunca"), ("only after they have gone", "solo cuando ya se ha ido")],
  "Your main beam would dazzle them through their mirrors.", "Tu luz larga le deslumbraría por sus espejos.")
Q("dz5", "dazzle", "On a bend, who must dip first?", "En una curva, ¿quién debe cambiar primero a la luz de cruce?",
  [("The driver whose road turns right", "El que toma la curva hacia la derecha"), ("The driver whose road turns left", "El que la toma hacia la izquierda"), ("The faster driver", "El más rápido")],
  "Their beam sweeps across the oncoming lane.", "Su haz barre el carril contrario.")
Q("dz6", "dazzle", "Even dipped beams can dazzle if…", "Incluso la luz de cruce puede deslumbrar si…",
  [("the headlights are badly aimed or the load is badly placed", "los faros están mal reglados o la carga mal colocada"), ("it is raining", "llueve"), ("the car is new", "el coche es nuevo")],
  "Keep the headlights properly adjusted.", "Hay que mantener bien reglados los faros.")
Q("dz7", "dazzle", "When may you switch the main beam back on after meeting a car?", "¿Cuándo puedes volver a poner la luz larga tras cruzarte con un coche?",
  [("When you are sure you cannot dazzle anyone", "Cuando estés seguro de no deslumbrar a nadie"), ("Right when it reaches you", "Justo cuando llega a tu altura"), ("After 100 m", "A los 100 m")],
  "Not before.", "Nunca antes.")

# ---------------------------------------------------------------- 3.5 dazzled
Q("dd1", "dazzled", "Oncoming lights dazzle you. To see, you look…", "Te deslumbran las luces de frente. Para ver, miras…",
  [("to the right, along the line between carriageway and shoulder", "a la derecha, guiándote por la línea entre calzada y arcén"), ("straight at the lights", "directamente a las luces"),
   ("to the centre line", "a la línea central")],
  "And close the left eye.", "Y cierras el ojo izquierdo.")
Q("dd2", "dazzled", "Which eye do you close when dazzled by oncoming traffic?", "¿Qué ojo cierras si te deslumbra el que viene de frente?",
  [("The left", "El izquierdo"), ("The right", "El derecho"), ("Neither", "Ninguno")],
  "It receives most of the light.", "Es el que más luz recibe.")
Q("dd3", "dazzled", "If you are dazzled, you must…", "Si te deslumbran, debes…",
  [("slow down, even to a stop, without moving onto the shoulder", "reducir la velocidad, incluso parar, sin salir al arcén"), ("pull onto the shoulder at once", "salir al arcén inmediatamente"),
   ("keep your speed and look away", "mantener la velocidad y apartar la vista")],
  "On the shoulder you could leave the road or hit someone.", "En el arcén podrías salirte o encontrar a otros usuarios.")
Q("dd4", "dazzled", "A car behind dazzles you through the mirror. You may…", "Un coche de detrás te deslumbra por el espejo. Puedes…",
  [("tilt the mirror or change your position", "cambiar la orientación del espejo o tu posición"), ("brake hard to warn them", "frenar en seco para avisarle"), ("switch on your rear fog light", "encender la antiniebla trasera")],
  "Most mirrors have a night setting.", "Muchos espejos tienen posición nocturna.")
Q("dd5", "dazzled", "Dazzle is…", "El deslumbramiento es…",
  [("a temporary blindness", "una ceguera temporal"), ("permanent eye damage", "una lesión permanente"), ("tiredness", "cansancio")],
  "The eyes get more light than they can take.", "Los ojos reciben más luz de la que soportan.")

# ---------------------------------------------------------------- 4.1-4.2 indicators and hazard
Q("hz1", "hazard", "Indicators are…", "Los intermitentes son…",
  [("amber, for any manoeuvre with a sideways move", "amarillo auto, para toda maniobra con desplazamiento lateral"), ("white, for turning only", "blancos, solo para girar"), ("red, for braking", "rojos, para frenar")],
  "Compulsory on motor vehicles, trailers and semitrailers.", "Obligatorios en vehículos de motor, remolques y semirremolques.")
Q("hz2", "hazard", "Hazard warning lights are…", "La luz de emergencia es…",
  [("all the indicators flashing at the same time", "el funcionamiento simultáneo de todos los intermitentes"), ("the brake lights flashing", "las luces de freno parpadeando"), ("the fog lights on", "las antiniebla encendidas")],
  "Compulsory on automobiles, optional on motorcycles.", "Obligatoria en automóviles, opcional en motos.")
Q("hz3", "hazard", "May you use the hazard lights to stop in a double row?", "¿Puedes usar la luz de emergencia para parar en doble fila?",
  [("No, that is not an emergency", "No, eso no es una emergencia"), ("Yes, for 2 minutes", "Sí, 2 minutos"), ("Yes, in town", "Sí, en poblado")],
  "Hazard lights are for real emergencies.", "La emergencia es para emergencias reales.")
Q("hz4", "hazard", "A school bus is stopped while children get off. It uses…", "Un autobús escolar está parado mientras bajan los niños. Usa…",
  [("the hazard lights", "la luz de emergencia"), ("the indicators of one side", "el intermitente de un lado"), ("the main beam", "la luz de carretera")],
  "During stops of school or minors’ transport.", "En las paradas de transporte escolar o de menores.")
Q("hz5", "hazard", "Do the hazard lights replace the V-16?", "¿Sustituye la luz de emergencia a la V-16?",
  [("No", "No"), ("Yes", "Sí"), ("Only by day", "Solo de día")],
  "Use both when immobilised on the road.", "Se usan ambas si se queda inmovilizado en la vía.")
Q("hz6", "hazard", "You cannot reach the minimum speed and could be hit from behind. You switch on…", "No alcanzas la velocidad mínima y hay peligro de alcance. Enciendes…",
  [("the hazard lights", "la luz de emergencia"), ("the rear fog light", "la antiniebla trasera"), ("the main beam", "la luz de carretera")],
  "As seen in the speed topic.", "Como en el tema de la velocidad.")
Q("hz7", "hazard", "The hazard lights’ dashboard tell-tale is…", "El testigo de la luz de emergencia es…",
  [("flashing red", "rojo intermitente"), ("steady green", "verde fijo"), ("steady blue", "azul fijo")],
  "Rear fog: amber; front fog: green.", "Antiniebla trasera: amarillo; delantera: verde.")

# ---------------------------------------------------------------- 4.3-4.4 brake and reversing
Q("br1", "brake", "The brake lights show that…", "La luz de frenado indica que…",
  [("the service (foot) brake is being used", "se está usando el freno de servicio (de pie)"), ("the parking brake is on", "está puesto el freno de estacionamiento"), ("the car is reversing", "el coche va marcha atrás")],
  "Most cars add a higher third brake light.", "La mayoría lleva una tercera luz más alta.")
Q("br2", "brake", "Pressing the brake pedal several times before stopping…", "Pisar el freno varias veces antes de parar…",
  [("warns those behind that you will stop or brake hard", "avisa a los de detrás de que vas a parar o frenar mucho"), ("is forbidden", "está prohibido"), ("wears the brakes", "desgasta los frenos")],
  "Use brake lights repeatedly whenever possible.", "Usar la luz de freno de forma reiterada siempre que se pueda.")
Q("br3", "brake", "The reversing light comes on…", "La luz de marcha atrás se enciende…",
  [("by itself when reverse is selected with the ignition on, even with the engine off", "sola al poner la marcha atrás con el contacto, aun con el motor parado"),
   ("only with the engine running", "solo con el motor en marcha"), ("with a separate switch", "con un interruptor propio")],
  "It is white.", "Es blanca.")
Q("br4", "brake", "The reversing light is compulsory on…", "La luz de marcha atrás es obligatoria en…",
  [("automobiles, except motorcycles", "los automóviles, salvo motocicletas"), ("all vehicles, motorcycles included", "todos los vehículos, motos incluidas"), ("trailers only", "solo remolques")],
  "Optional on trailers and semitrailers.", "Opcional en remolques y semirremolques.")
Q("br5", "brake", "What colour is the reversing light?", "¿De qué color es la luz de marcha atrás?",
  [("White", "Blanca"), ("Red", "Roja"), ("Amber", "Amarilla")],
  "It also lights the road behind.", "También alumbra la vía por detrás.")

# ---------------------------------------------------------------- 5. other
Q("ot1", "other", "Interior lighting is compulsory in…", "El alumbrado interior es obligatorio en…",
  [("public passenger vehicles and hire cars with driver", "vehículos de servicio público de viajeros y de alquiler con conductor"), ("every car", "todos los turismos"), ("no vehicle", "ningún vehículo")],
  "Without dazzling other road users.", "Sin deslumbrar a los demás.")
Q("ot2", "other", "The rear number-plate light comes on…", "La luz de la placa de matrícula trasera se enciende…",
  [("automatically with the position lights", "automáticamente con las luces de posición"), ("only with the main beam", "solo con la luz de carretera"), ("with its own switch", "con su propio interruptor")],
  "And the SP plate light, if there is one.", "Y la de la placa SP, si la hay.")
Q("ot3", "other", "A taxi’s interior light must…", "La luz interior de un taxi debe…",
  [("not dazzle or bother other road users", "no deslumbrar ni molestar a los demás usuarios"), ("always be on", "estar siempre encendida"), ("be red", "ser roja")],
  "It is compulsory in public passenger vehicles.", "Es obligatoria en servicio público de viajeros.")
