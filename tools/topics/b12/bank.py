# -*- coding: utf-8 -*-
"""Question bank for the interactive Topic 12 page (driving techniques). In every question the FIRST option is the
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
    "vision": dict(sec=1, en="Vision", es="Técnicas de visión",
        recap=[("Preventive driving rests on vision, anticipation and space control.", "La conducción preventiva se basa en visión, anticipación y control del espacio."),
               ("Look far ahead (where you’ll be in a few seconds), to the sides often, and in the mirrors often.", "Mirar a lo lejos (donde estaremos en unos segundos), a los lados y por los retrovisores con frecuencia."),
               ("Mirrors every 5–10 s in town and heavy traffic; every 10–15 s on motorways and empty roads.", "Retrovisores cada 5–10 s en ciudad y tráfico denso; cada 10–15 s en autovía y vías sin tráfico."),
               ("There is always a blind spot: turn your head about 45° before moving sideways.", "Siempre queda un ángulo muerto: girar la cabeza unos 45° antes de desplazarse lateralmente.")],
        trap=("Thinking well-adjusted mirrors leave no blind spot.", "Pensar que con los espejos bien reglados no hay ángulo muerto.")),
    "anticip": dict(sec=1, en="Anticipation", es="Anticipación",
        recap=[("Don’t trust others: anyone can make a mistake or be distracted.", "Desconfiar de los demás: cualquiera puede equivocarse o distraerse."),
               ("Adapt your speed to the circumstances; cover the brake when you sense a risk.", "Adaptar la velocidad a las circunstancias; preparar el pie sobre el freno ante un riesgo."),
               ("Be seen and understood: signal early and until the end; use lights well (sun in their eyes, tunnel exits).", "Hacerse ver y entender: señalizar con antelación y hasta el final; buen uso del alumbrado (sol de frente, salida de túneles)."),
               ("Avoid other vehicles’ blind spots, especially heavy ones and when on a motorcycle.", "Evitar los ángulos muertos de otros, sobre todo de los pesados y si vas en moto.")],
        trap=("Assuming others will always follow the rules.", "Suponer que los demás siempre cumplirán las normas.")),
    "space": dict(sec=1, en="Space control", es="Control del espacio",
        recap=[("Front gap: 2 s in town, 3 s on the road, at least 1 s more in worse conditions or with a tailgater.", "Distancia delantera: 2 s en ciudad, 3 s en carretera, al menos 1 s más con malas condiciones o si nos siguen muy cerca."),
               ("Tailgater: more front gap, signal early, brake gently; if stopped and a crash is unavoidable, keep braking.", "Si nos siguen muy cerca: más distancia delantera, señalizar antes, frenar suave; detenidos y sin evitar el alcance, mantener frenado."),
               ("Zone of uncertainty: large to the side for cyclists and vehicles; smaller for pedestrians except children.", "Zona de incertidumbre: grande lateral en ciclistas y vehículos; menor en peatones salvo niños."),
               ("Stopped: 2–3 m (see the rear tyres). Last in an unexpected queue: hazard lights, 5–6 m, mirrors, first gear ready.", "Detenido: 2–3 m (ver las ruedas traseras). Último de una cola imprevista: emergencia, 5–6 m, espejos, 1.ª lista.")],
        trap=("Stopping right up against the car in front.", "Detenerse pegado al vehículo de delante.")),
    "devices": dict(sec=1, en="Glass, wipers and demisters", es="Cristales, limpiaparabrisas y antivaho",
        recap=[("Glass must not distort, must be clean and safety glass; unapproved tinted glass is prohibited.", "Los cristales no deben deformar, deben estar limpios y ser de seguridad; prohibido el tintado no homologado."),
               ("Any car with wipers must have a windscreen washer; a rear washer is not compulsory.", "Todo automóvil con limpiaparabrisas debe tener lavaparabrisas; el lavalunetas no es obligatorio."),
               ("Replace cracked blades; never wipe a dry screen with an empty tank; use the slowest speed; distilled water and soap.", "Cambiar escobillas cuarteadas; nunca limpiar en seco con el depósito vacío; la velocidad más lenta; agua destilada y jabón."),
               ("Heated rear window and front demister clear mist and frost.", "La luneta térmica y el antivaho delantero eliminan vaho y hielo.")],
        trap=("Thinking the rear washer is compulsory.", "Pensar que el lavalunetas es obligatorio.")),
    "mirrors": dict(sec=1, en="Mirrors", es="Espejos retrovisores",
        recap=[("Cars: outside left mirror and an interior mirror (60 m behind, 20 m wide); right mirror compulsory if the interior one can’t see.", "Turismos: exterior izquierdo e interior (60 m por detrás, 20 m de ancho); el derecho, obligatorio si el interior no permite ver."),
               ("Motorcycles: left if top speed ≤ 100 km/h, left and right above. Two-wheel mopeds: at least left.", "Motos: izquierdo si no superan 100 km/h, izquierdo y derecho si los superan. Ciclomotores de dos ruedas: al menos el izquierdo."),
               ("Adjust before setting off, stopped, on flat ground: interior shows 3 of 4 sides of the rear window; door mirrors 50 % road, 50 % sky.", "Regular antes de salir, parado, en llano: el interior muestra 3 de los 4 lados de la luneta; los exteriores, 50 % asfalto y 50 % cielo."),
               ("Convex: wider view, objects look smaller and further; flat: true image; panoramic doesn’t replace the door mirrors.", "Convexo: más ángulo, empequeñece y aleja; plano: imagen real; el panorámico no sustituye a los exteriores.")],
        trap=("Thinking a convex mirror shows true distances.", "Pensar que un espejo convexo muestra las distancias reales.")),
    "ecostart": dict(sec=2, en="Efficient driving and moving off", es="Conducción eficiente y arranque",
        recap=[("Efficient driving: 10–25 % less fuel; course: 50–80 % less CO₂; less wear, noise and stress.", "Conducción eficiente: 10–25 % menos combustible; curso: 50–80 % menos CO₂; menos desgaste, ruido y estrés."),
               ("Start the engine without accelerating.", "Arrancar el motor sin acelerar."),
               ("Petrol: move off at once. Diesel: wait a few seconds for lubrication.", "Gasolina: salir enseguida. Diésel: esperar unos segundos por la lubricación."),
               ("First gear only to move off; second after 2 s or 6 m; no hard revving when cold.", "1.ª solo para iniciar la marcha; 2.ª a los 2 s o 6 m; sin acelerones en frío.")],
        trap=("Warming the engine up by revving it while stopped.", "Calentar el motor acelerando en parado.")),
    "gears": dict(sec=2, en="Gears", es="Uso de las marchas",
        recap=[("Highest gear possible: fewer revs, less fuel, less pollution.", "La marcha más alta posible: menos revoluciones, menos consumo y contaminación."),
               ("Change up at 1,500–2,000 rpm (diesel) or 2,000–2,500 rpm (petrol); accelerate smoothly.", "Cambiar a 1.500–2.000 rpm (diésel) o 2.000–2.500 rpm (gasolina); acelerar suave."),
               ("You can skip gears: 3rd at 30, 4th at 40, 5th at 50 km/h.", "Se pueden saltar marchas: 3.ª a 30, 4.ª a 40, 5.ª a 50 km/h."),
               ("Slow down with the engine brake (in gear, off the throttle: zero fuel); change down as late as possible.", "Reducir con el freno motor (con marcha y sin acelerar: consumo nulo); reducir de marcha lo más tarde posible.")],
        trap=("Going through every gear in order.", "Pasar por todas las marchas en orden.")),
    "savings": dict(sec=2, en="Saving fuel — and what not to do", es="Ahorro y lo que no hay que hacer",
        recap=[("Moderate, steady speed; engine off for stops over 60 s; maintenance and correct tyre pressure.", "Velocidad moderada y uniforme; apagar el motor en paradas de más de 60 s; mantenimiento y presión correcta."),
               ("No excess weight; boot rather than roof rack; don’t spoil aerodynamics; air conditioning at about 23 °C; ECO mode.", "Sin peso de más; maletero mejor que baca; no alterar la aerodinámica; aire acondicionado a unos 23 °C; modo ECO."),
               ("Don’t coast in neutral or with the engine off; don’t use lower-octane fuel; no windows down at speed.", "No circular en punto muerto ni con el motor apagado; no usar gasolina de menor octanaje; no ventanillas bajadas a velocidad."),
               ("Don’t climb in low gears with high revs; don’t save on lights; don’t switch off for a few seconds.", "No subir con marchas cortas y el motor revolucionado; no ahorrar en luces; no apagar el motor unos segundos.")],
        trap=("Coasting downhill in neutral to save fuel.", "Bajar en punto muerto para ahorrar.")),
    "pollution": dict(sec=2, en="Pollution", es="Contaminación",
        recap=[("CO: very toxic (colourless); CO₂: greenhouse effect; NOx: breathing problems; HC: toxic; SO₂: acid rain.", "CO: muy tóxico (incoloro); CO₂: efecto invernadero; NOx: problemas respiratorios; HC: tóxicos; SO₂: lluvia ácida."),
               ("Throwing objects onto the road is not allowed.", "No se permite arrojar objetos a la vía."),
               ("Noise or gases above limits: fines and immobilisation (open exhausts, loud music, revving, smoke).", "Ruidos o gases por encima de los límites: sanción e inmovilización (escape libre, música alta, acelerones, humo)."),
               ("Never change the oil on the street; take it to a recovery container.", "Nunca cambiar el aceite en la vía pública; llevarlo a un contenedor de recuperación.")],
        trap=("Thinking CO₂ causes acid rain.", "Pensar que el CO₂ causa la lluvia ácida.")),
    "zbe": dict(sec=2, en="Low-emission zones and urban access", es="ZBE y acceso urbano",
        recap=[("Municipalities over 50,000 people, island territories, and over 20,000 exceeding pollution limits: mobility plans with ZBE.", "Municipios de más de 50.000 habitantes, territorios insulares y de más de 20.000 que superen los límites: PMUS con ZBE."),
               ("A ZBE restricts access, driving and parking by emissions classification; its entrance must be signed.", "La ZBE restringe acceso, circulación y estacionamiento según la clasificación por emisiones; su entrada debe señalizarse."),
               ("R-120: entry prohibited according to the environmental label; conditions on a panel.", "R-120: entrada prohibida según el distintivo ambiental; las condiciones, en un panel."),
               ("Also residential priority zones, safe school routes and traffic calming near schools and hospitals.", "También zonas de prioridad residencial, caminos escolares seguros y calmado del tráfico junto a colegios y hospitales.")],
        trap=("Thinking only Madrid and Barcelona must have low-emission zones.", "Pensar que solo Madrid y Barcelona deben tener ZBE.")),
    "labels": dict(sec=2, en="Environmental labels", es="Distintivos ambientales",
        recap=[("Four labels, most to least efficient: 0 (blue), ECO, C (green), B (yellow).", "Cuatro distintivos, de más a menos eficiente: 0 (azul), ECO, C (verde), B (amarillo)."),
               ("0: BEV, REEV, PHEV ≥ 40 km, fuel cell. ECO: PHEV < 40 km, HEV, gas; must meet C.", "0: BEV, REEV, PHEV ≥ 40 km, pila de combustible. ECO: PHEV < 40 km, HEV, gas; deben cumplir la C."),
               ("C: petrol from Jan 2006, diesel from Sep 2015 (heavy from 2014). B: petrol from Jan 2001, diesel from 2006.", "C: gasolina desde enero 2006, diésel desde sept. 2015 (pesados desde 2014). B: gasolina desde enero 2001, diésel desde 2006."),
               ("No label: the 50 % most polluting. Display is voluntary; bottom right of the windscreen.", "Sin distintivo: el 50 % más contaminante. Colocación voluntaria; abajo a la derecha del parabrisas.")],
        trap=("Thinking any plug-in hybrid gets the 0 label.", "Pensar que cualquier híbrido enchufable tiene la etiqueta 0.")),
}

# ---------------------------------------------------------------- 1. vision
Q("vi1", "vision", "Preventive driving rests on three principles. Which?", "La conducción preventiva se basa en tres principios. ¿Cuáles?",
  [("Vision, anticipation and space control", "Visión, anticipación y control del espacio"), ("Speed, braking and steering", "Velocidad, frenada y dirección"), ("Lights, horn and mirrors", "Luces, claxon y espejos")],
  "So you can react faster to anything unexpected.", "Para reaccionar con mayor rapidez ante cualquier imprevisto.")
Q("vi2", "vision", "In town, how often should you check the mirrors?", "En vía urbana, ¿cada cuánto conviene mirar los retrovisores?",
  [("Every 5–10 seconds", "Cada 5–10 segundos"), ("Every 30 seconds", "Cada 30 segundos"), ("Only before a manoeuvre", "Solo antes de una maniobra")],
  "Also on roads with heavy traffic.", "También en carreteras con tráfico denso.")
Q("vi3", "vision", "On an autovía with little traffic, check the mirrors every…", "En una autovía con poco tráfico, mira los retrovisores cada…",
  [("10–15 seconds", "10–15 segundos"), ("5 seconds", "5 segundos"), ("minute", "minuto")],
  "Town and heavy traffic: 5–10 s.", "Ciudad y tráfico denso: 5–10 s.")
Q("vi4", "vision", "Should you check the mirrors when you are not going to manoeuvre?", "¿Hay que mirar los retrovisores aunque no vayas a hacer ninguna maniobra?",
  [("Yes, often, to keep track of the vehicles behind and beside you", "Sí, con frecuencia, para controlar a los de detrás y a los lados"), ("No, only before manoeuvres", "No, solo antes de maniobrar"), ("Only at night", "Solo de noche")],
  "Especially in stressful or heavy traffic.", "Sobre todo con estrés o tráfico denso.")
Q("vi5", "vision", "To check the blind spot before moving sideways you should…", "Para comprobar el ángulo muerto antes de un desplazamiento lateral hay que…",
  [("turn your head about 45° and look directly", "girar la cabeza unos 45° y mirar directamente"), ("look in the interior mirror", "mirar por el retrovisor interior"), ("sound the horn", "tocar el claxon")],
  "The mirrors can’t show it.", "Los espejos no lo muestran.")
Q("vi6", "vision", "With well-adjusted mirrors…", "Con los espejos bien reglados…",
  [("there is still a blind spot", "sigue quedando un ángulo muerto"), ("there is no blind spot", "no hay ángulo muerto"), ("you never need to turn your head", "nunca hace falta girar la cabeza")],
  "A place where you can’t see another road user.", "Un lugar donde no se percibe a otro usuario.")
Q("vi7", "vision", "Where should you look, especially at higher speeds?", "¿Dónde hay que mirar, sobre todo a mayor velocidad?",
  [("Far ahead, where you will be in a few seconds", "A lo lejos, al punto donde estaremos en unos segundos"), ("Only at the car in front", "Solo al coche de delante"), ("At the dashboard", "Al salpicadero")],
  "Not only at the vehicle in front.", "No solo al vehículo de delante.")
Q("vi8", "vision", "Looking to the sides often helps you…", "Mirar a los lados con frecuencia ayuda a…",
  [("spot sudden movements, such as a lane change", "percibir movimientos imprevistos, como un cambio de carril"), ("save fuel", "ahorrar combustible"), ("read the signs better", "leer mejor las señales")],
  "On both sides.", "A ambos lados.")

# ---------------------------------------------------------------- 1. anticipation
Q("an1", "anticip", "Defensive driving means…", "La conducción defensiva consiste en…",
  [("anticipating risks and not trusting that others will always do the right thing", "anticiparse a los riesgos y desconfiar de que los demás actúen siempre bien"), ("driving aggressively to stay safe", "conducir de forma agresiva para estar seguro"), ("driving always very slowly", "circular siempre muy despacio")],
  "Anyone can make a mistake or be distracted.", "Cualquiera puede cometer un error o distraerse.")
Q("an2", "anticip", "You see a situation that could become risky. It is advisable to…", "Ves una situación de posible riesgo. Conviene…",
  [("cover the brake pedal with your foot", "preparar el pie sobre el pedal del freno"), ("speed up to get past", "acelerar para pasar"), ("look away", "apartar la vista")],
  "So you can stop sooner.", "Para poder detenerse antes.")
Q("an3", "anticip", "To ‘be seen and understood’ you should…", "Para «hacerse ver y entender» hay que…",
  [("signal early and keep signalling until the manoeuvre is finished", "señalizar con antelación y mantenerlo hasta terminar la maniobra"), ("signal only at the last moment", "señalizar en el último momento"), ("use the horn often", "usar el claxon a menudo")],
  "And use your lights well.", "Y hacer un uso adecuado del alumbrado.")
Q("an4", "anticip", "When should you take extra care that others can see you?", "¿Cuándo hay que cuidar especialmente que los demás te vean?",
  [("When oncoming drivers have the sun in their eyes or leave a tunnel", "Cuando los que vienen de frente tienen el sol de cara o salen de un túnel"), ("On a sunny morning with the sun behind them", "Con sol a su espalda"), ("Never", "Nunca")],
  "Unfavourable light.", "Condiciones de luminosidad desfavorables.")
Q("an5", "anticip", "Why avoid staying in a lorry’s blind spot?", "¿Por qué evitar quedarse en el ángulo muerto de un camión?",
  [("Its driver may not see you", "Su conductor puede no detectarte"), ("It uses more fuel", "Consume más combustible"), ("It is forbidden to overtake lorries", "Está prohibido adelantar a camiones")],
  "Even more so on a motorcycle.", "Más aún si vas en moto.")
Q("an6", "anticip", "Adapting your driving means a speed suited to…", "Adaptar la conducción supone una velocidad adecuada a…",
  [("the weather, the traffic, the road, the vehicle and your own state", "la meteorología, el tráfico, la vía, el vehículo y el propio conductor"), ("the speed limit only", "solo el límite de velocidad"), ("the car in front", "el coche de delante")],
  "So you can stop safely.", "Para poder detenerse con seguridad.")

# ---------------------------------------------------------------- 1. space
Q("sp1", "space", "In town, the front safety gap should be at least…", "En zona urbana, la distancia de seguridad delantera debe ser al menos de…",
  [("2 seconds", "2 segundos"), ("1 second", "1 segundo"), ("5 seconds", "5 segundos")],
  "3 seconds on the open road.", "3 segundos en carretera.")
Q("sp2", "space", "On the open road, the front safety gap should be at least…", "En carretera, la distancia de seguridad delantera debe ser al menos de…",
  [("3 seconds", "3 segundos"), ("2 seconds", "2 segundos"), ("1 second", "1 segundo")],
  "At least one more second in worse conditions.", "Al menos un segundo más en peores condiciones.")
Q("sp3", "space", "When should you add at least one more second to your gap?", "¿Cuándo hay que aumentar la distancia al menos un segundo más?",
  [("In bad weather, when tired, on a poor surface, or when someone follows too close", "Con mal tiempo, cansancio, mal firme o si te siguen muy cerca"), ("Only at night", "Solo de noche"), ("Only on motorways", "Solo en autopista")],
  "Adverse conditions.", "Condiciones adversas.")
Q("sp4", "space", "A vehicle is following you too closely. You should…", "Un vehículo te sigue demasiado cerca. Debes…",
  [("increase your front gap, signal early and brake gently", "aumentar tu distancia delantera, señalizar antes y frenar suave"), ("brake hard to warn them", "frenar fuerte para avisarle"), ("speed up a lot", "acelerar mucho")],
  "So you won’t need to brake suddenly.", "Para no tener que frenar bruscamente.")
Q("sp5", "space", "You are stopped and a rear-end crash can’t be avoided. You should…", "Estás detenido y no se puede evitar un alcance. Conviene…",
  [("keep the vehicle braked", "mantener el vehículo frenado"), ("release the brake", "soltar el freno"), ("put it in neutral", "ponerlo en punto muerto")],
  "If you are moving and a crash looks likely, try to move aside.", "Si estás en marcha, intenta apartarte.")
Q("sp6", "space", "Which road user has the largest side zone of uncertainty?", "¿Qué usuario tiene una gran zona lateral de incertidumbre?",
  [("A cyclist, especially on long climbs", "El ciclista, sobre todo en ascensos prolongados"), ("An adult pedestrian", "Un peatón adulto"), ("A parked lorry", "Un camión aparcado")],
  "They sway with the effort of pedalling.", "Oscilan por el esfuerzo del pedaleo.")
Q("sp7", "space", "When you stop behind another vehicle you should leave…", "Al detenerte detrás de otro vehículo debes dejar…",
  [("2–3 metres, enough to see its rear tyres on the road", "2–3 metros, viendo sus ruedas traseras sobre el suelo"), ("50 cm", "50 cm"), ("10 metres", "10 metros")],
  "To react if it rolls back or breaks down.", "Para reaccionar si va hacia atrás o se avería.")
Q("sp8", "space", "You are the last vehicle in an unexpected queue. You should…", "Eres el último vehículo de una retención imprevista. Debes…",
  [("switch on the hazard lights and leave 5–6 m to the vehicle in front", "encender la emergencia y dejar 5–6 m con el de delante"), ("switch off the engine", "apagar el motor"), ("get out of the car", "salir del coche")],
  "Watch the mirrors, ready to move aside.", "Vigilar los espejos, listo para apartarte.")
Q("sp9", "space", "How long do you keep the ‘last in the queue’ measures up?", "¿Hasta cuándo se mantienen las medidas de «último de la cola»?",
  [("Until several vehicles have stopped behind you", "Hasta que se detengan varios vehículos por detrás"), ("For 10 seconds", "Durante 10 segundos"), ("Until the police arrive", "Hasta que llegue la policía")],
  "Then the risk of being hit falls.", "Entonces baja el riesgo de alcance.")
Q("sp10", "space", "Why leave space when you stop uphill behind another car?", "¿Por qué dejar espacio al detenerse en subida detrás de otro coche?",
  [("It may roll back when it moves off", "Puede ir hacia atrás al arrancar"), ("To save fuel", "Para ahorrar combustible"), ("It isn’t needed uphill", "En subida no hace falta")],
  "Also to get round it if it breaks down.", "También para esquivarlo si se avería.")
Q("sp11", "space", "A parked car’s zone of uncertainty includes…", "La zona de incertidumbre de un coche aparcado incluye…",
  [("a door that may open", "una puerta que se puede abrir"), ("nothing", "nada"), ("only its boot", "solo el maletero")],
  "Also a sudden move or turn.", "También una salida o giro imprevisto.")

# ---------------------------------------------------------------- 1. devices
Q("dv1", "devices", "Tinted or coloured glass that is not approved is…", "Los vidrios tintados o coloreados no homologados…",
  [("prohibited", "están prohibidos"), ("allowed on rear windows", "se permiten en las ventanillas traseras"), ("recommended in summer", "se recomiendan en verano")],
  "Glass must not distort what you see.", "Los cristales no deben deformar la visión.")
Q("dv2", "devices", "A car with windscreen wipers must also have…", "Un automóvil con limpiaparabrisas debe tener además…",
  [("a windscreen washer", "lavaparabrisas"), ("a rear washer", "lavalunetas"), ("a heated windscreen", "parabrisas térmico")],
  "The rear washer is not compulsory.", "El lavalunetas no es obligatorio.")
Q("dv3", "devices", "The rear window washer is…", "El lavalunetas es…",
  [("not compulsory, but recommended", "no obligatorio, pero sí recomendable"), ("compulsory", "obligatorio"), ("prohibited", "prohibido")],
  "It sits at the rear window.", "Se sitúa en la luneta trasera.")
Q("dv4", "devices", "Using the wipers on a dry windscreen with the washer tank empty…", "Usar el limpiaparabrisas con el cristal seco y el depósito vacío…",
  [("scratches the glass and damages the blade", "raya el cristal y daña la escobilla"), ("cleans better", "limpia mejor"), ("saves water", "ahorra agua")],
  "It drags dust across the glass.", "Arrastra polvo y suciedad.")
Q("dv5", "devices", "Which wiper speed is recommended?", "¿Qué velocidad del limpiaparabrisas se recomienda?",
  [("The slowest one that works", "La más lenta posible"), ("Always the fastest", "Siempre la más rápida"), ("Intermittent only", "Solo intermitente")],
  "Less distraction and wear.", "Menos molestia visual y desgaste.")
Q("dv6", "devices", "The washer tank should be filled with…", "El depósito del lavaparabrisas se recomienda rellenarlo con…",
  [("distilled water and a cleaning agent", "agua destilada y un agente limpiador"), ("tap water only", "solo agua del grifo"), ("oil", "aceite")],
  "Keep the jets clean.", "Y mantener limpios los orificios.")
Q("dv7", "devices", "The heated rear window works by…", "La luneta térmica funciona mediante…",
  [("filaments in the rear glass", "unos filamentos en el cristal trasero"), ("a fan in the boot", "un ventilador en el maletero"), ("the wipers", "el limpiaparabrisas")],
  "It clears frost and mist.", "Elimina la escarcha y el vaho.")
Q("dv8", "devices", "Wiper blades should be replaced when they…", "Las escobillas se deben sustituir cuando…",
  [("are cracked, don’t clean well or scratch the glass", "están cuarteadas, no limpian bien o arañan el cristal"), ("are a year old, always", "tienen un año, siempre"), ("get wet", "se mojan")],
  "Visibility comes first.", "La visibilidad es lo primero.")

# ---------------------------------------------------------------- 1. mirrors
Q("mi1", "mirrors", "In a car, which mirrors are always compulsory?", "En un turismo, ¿qué espejos son siempre obligatorios?",
  [("The outside left mirror and the interior mirror", "El exterior izquierdo y el interior"), ("Only the interior mirror", "Solo el interior"), ("Both outside mirrors only", "Solo los dos exteriores")],
  "The right one if the interior mirror can’t see behind.", "El derecho, si el interior no permite ver.")
Q("mi2", "mirrors", "When does the outside right mirror become compulsory in a car?", "¿Cuándo es obligatorio el espejo exterior derecho en un turismo?",
  [("When the interior mirror can’t give the view behind (trailer, luggage…)", "Cuando el interior no permite la visión trasera (remolque, equipaje…)"), ("Always", "Siempre"), ("Never", "Nunca")],
  "Otherwise it is optional.", "En el resto de casos es opcional.")
Q("mi3", "mirrors", "A motorcycle with a top speed over 100 km/h must have…", "Una motocicleta de más de 100 km/h debe llevar…",
  [("mirrors on the left and right", "espejo izquierdo y derecho"), ("only a left mirror", "solo el izquierdo"), ("no mirrors", "ningún espejo")],
  "Up to 100 km/h: at least the left one.", "Hasta 100 km/h: al menos el izquierdo.")
Q("mi4", "mirrors", "A two-wheeled moped must have at least…", "Un ciclomotor de dos ruedas debe llevar al menos…",
  [("a left mirror", "un espejo en la izquierda"), ("two mirrors", "dos espejos"), ("an interior mirror", "un espejo interior")],
  "Other mopeds depend on their body.", "Los demás, según su carrocería.")
Q("mi5", "mirrors", "When should the mirrors be adjusted?", "¿Cuándo se deben regular los espejos?",
  [("Before setting off, with the vehicle still", "Antes de iniciar la marcha, con el vehículo parado"), ("While driving on the motorway", "Circulando por la autopista"), ("Only at the ITV", "Solo en la ITV")],
  "Preferably on flat, level ground.", "Preferiblemente en terreno recto y llano.")
Q("mi6", "mirrors", "A well-adjusted interior mirror shows…", "Un retrovisor interior bien reglado muestra…",
  [("at least three of the four sides of the rear window", "al menos tres de los cuatro lados de la luneta trasera"), ("only the rear seats", "solo los asientos traseros"), ("the driver’s face", "la cara del conductor")],
  "With a slight movement of the eyes.", "Con un leve movimiento de ojos.")
Q("mi7", "mirrors", "A well-adjusted door mirror shows…", "Un retrovisor exterior bien reglado muestra…",
  [("as little of your car and as much road as possible, about 50 % road and 50 % sky", "lo mínimo del vehículo y lo máximo de la calzada, 50 % asfalto y 50 % cielo"), ("mostly your own car", "sobre todo tu coche"), ("only the sky", "solo el cielo")],
  "Horizon in the middle.", "Horizonte en medio.")
Q("mi8", "mirrors", "Convex mirrors…", "Los espejos convexos…",
  [("give a wider view but make things look smaller and further away", "dan más ángulo pero empequeñecen y alejan la imagen"), ("give a true-size image", "dan una imagen real"), ("make things look closer", "acercan los objetos")],
  "Door mirrors are convex.", "Los exteriores son convexos.")
Q("mi9", "mirrors", "The panoramic interior mirror…", "El espejo interior panorámico…",
  [("gives a wider view but doesn’t replace the door mirrors", "da más ángulo pero no sustituye a los exteriores"), ("replaces the door mirrors", "sustituye a los exteriores"), ("is prohibited", "está prohibido")],
  "Flat mirrors give a true image.", "El plano da imagen real.")
Q("mi10", "mirrors", "The interior mirror must let you see behind the car up to…", "El espejo interior debe permitir ver por detrás del vehículo hasta…",
  [("60 m, 20 m wide", "60 m, en 20 m de anchura"), ("10 m", "10 m"), ("200 m", "200 m")],
  "From the horizon on a flat road.", "Desde el horizonte, en carretera plana.")

# ---------------------------------------------------------------- 2. efficient start
Q("ef1", "ecostart", "According to your course, efficient driving reduces fuel use by…", "Según tu curso, la conducción eficiente reduce el consumo entre…",
  [("10 % and 25 %", "el 10 % y el 25 %"), ("1 % and 2 %", "el 1 % y el 2 %"), ("50 % and 80 %", "el 50 % y el 80 %")],
  "The course gives 50–80 % for CO₂.", "El curso da 50–80 % para el CO₂.")
Q("ef2", "ecostart", "According to your course, efficient driving reduces CO₂ emissions by…", "Según tu curso, la conducción eficiente reduce las emisiones de CO₂ entre…",
  [("50 % and 80 %", "el 50 % y el 80 %"), ("1 % and 5 %", "el 1 % y el 5 %"), ("nothing", "nada")],
  "In reality CO₂ falls with the fuel saved (about 15 %, IDAE).", "En realidad, el CO₂ baja con el combustible ahorrado (en torno al 15 %, IDAE).")
Q("ef3", "ecostart", "To start a modern car’s engine you should…", "Para arrancar el motor de un coche actual hay que…",
  [("not press the accelerator", "no pisar el acelerador"), ("press the accelerator fully", "pisar a fondo el acelerador"), ("rev it several times", "acelerar varias veces")],
  "It isn’t needed.", "No es necesario.")
Q("ef4", "ecostart", "With a petrol engine, after starting you should…", "Con un motor de gasolina, tras arrancar hay que…",
  [("move off straight away", "iniciar la marcha inmediatamente"), ("wait 5 minutes", "esperar 5 minutos"), ("rev it to warm it up", "acelerar para calentarlo")],
  "Diesel: wait a few seconds.", "Diésel: esperar unos segundos.")
Q("ef5", "ecostart", "With a diesel engine, after starting…", "Con un motor diésel, tras arrancar…",
  [("wait a few seconds so it is lubricated", "esperar unos segundos para que se lubrique"), ("move off at once", "salir inmediatamente"), ("wait 10 minutes", "esperar 10 minutos")],
  "Petrol: move off at once.", "Gasolina: salir enseguida.")
Q("ef6", "ecostart", "When should you change from first to second gear?", "¿Cuándo hay que pasar de 1.ª a 2.ª?",
  [("After about 2 seconds or 6 metres", "A los 2 segundos o 6 metros"), ("At 40 km/h", "A 40 km/h"), ("After 100 metres", "A los 100 metros")],
  "First gear is only for moving off.", "La 1.ª solo para iniciar la marcha.")
Q("ef7", "ecostart", "Revving hard with a cold engine…", "Acelerar fuerte con el motor en frío…",
  [("harms it: it isn’t well lubricated yet", "lo perjudica: aún no está bien lubricado"), ("warms it up faster and is good", "lo calienta antes y es bueno"), ("has no effect", "no tiene efecto")],
  "Drive gently at first.", "Conducir con suavidad al principio.")
Q("ef8", "ecostart", "Which is an advantage of efficient driving?", "¿Cuál es una ventaja de la conducción eficiente?",
  [("More comfort and less stress", "Más confort y menos estrés"), ("Shorter journey times always", "Siempre trayectos más cortos"), ("More engine wear", "Más desgaste del motor")],
  "Also longer life for brakes and gearbox, and less noise.", "También más vida útil de frenos y caja de cambios, y menos ruido.")

# ---------------------------------------------------------------- 2. gears
Q("ge1", "gears", "Fewer engine revs mean…", "Menos revoluciones del motor suponen…",
  [("less fuel and less pollution", "menos consumo y menos contaminación"), ("more fuel", "más consumo"), ("less safety", "menos seguridad")],
  "Use the highest gear possible.", "Usar la marcha más alta posible.")
Q("ge2", "gears", "With a diesel engine, change up between…", "Con un motor diésel, hay que cambiar de marcha entre…",
  [("1,500 and 2,000 rpm", "1.500 y 2.000 rpm"), ("3,000 and 4,000 rpm", "3.000 y 4.000 rpm"), ("500 and 1,000 rpm", "500 y 1.000 rpm")],
  "Petrol: 2,000–2,500 rpm.", "Gasolina: 2.000–2.500 rpm.")
Q("ge3", "gears", "With a petrol engine, change up between…", "Con un motor de gasolina, hay que cambiar de marcha entre…",
  [("2,000 and 2,500 rpm", "2.000 y 2.500 rpm"), ("1,000 and 1,500 rpm", "1.000 y 1.500 rpm"), ("4,000 and 5,000 rpm", "4.000 y 5.000 rpm")],
  "Diesel: 1,500–2,000 rpm.", "Diésel: 1.500–2.000 rpm.")
Q("ge4", "gears", "Is it possible to skip gears when accelerating?", "¿Se pueden saltar marchas al acelerar?",
  [("Yes, for example third at 30, fourth at 40, fifth at 50 km/h", "Sí, por ejemplo 3.ª a 30, 4.ª a 40, 5.ª a 50 km/h"), ("No, never", "No, nunca"), ("Only in automatic cars", "Solo en los automáticos")],
  "It saves fuel.", "Ahorra combustible.")
Q("ge5", "gears", "In gear, with your foot off the accelerator, fuel use is…", "Con una marcha engranada y sin acelerar, el consumo es…",
  [("zero", "nulo"), ("the same as idling", "el mismo que al ralentí"), ("higher", "mayor")],
  "That is the engine brake.", "Es el freno motor.")
Q("ge6", "gears", "To slow down efficiently you should…", "Para reducir la velocidad de forma eficiente hay que…",
  [("use the engine brake and change down as late as possible", "usar el freno motor y reducir de marcha lo más tarde posible"), ("change down through every gear at once", "reducir todas las marchas enseguida"), ("put it in neutral", "ponerlo en punto muerto")],
  "You can skip gears when changing down too.", "También se pueden saltar marchas al reducir.")
Q("ge7", "gears", "Efficient acceleration should be…", "La aceleración eficiente debe ser…",
  [("smooth and progressive", "suave y progresiva"), ("hard and short", "fuerte y corta"), ("always with the pedal fully down", "siempre a fondo")],
  "Don’t over-rev the engine.", "No forzar el motor.")
Q("ge8", "gears", "You are at 50 km/h in a car. The efficient gear is usually…", "Circulas a 50 km/h en un turismo. La marcha eficiente suele ser…",
  [("fifth", "la 5.ª"), ("second", "la 2.ª"), ("first", "la 1.ª")],
  "Fifth from 50 km/h, according to your course.", "5.ª desde 50 km/h, según tu curso.")

# ---------------------------------------------------------------- 2. savings and don'ts
Q("sv1", "savings", "Higher speed means…", "A mayor velocidad…",
  [("more fuel use", "mayor consumo"), ("less fuel use", "menor consumo"), ("no change", "ningún cambio")],
  "Moderate, steady speed.", "Velocidad moderada y uniforme.")
Q("sv2", "savings", "It is advisable to switch the engine off for stops longer than…", "Es recomendable apagar el motor en detenciones de más de…",
  [("60 seconds", "60 segundos"), ("5 seconds", "5 segundos"), ("10 minutes", "10 minutos")],
  "Not for stops of a few seconds.", "No en detenciones momentáneas.")
Q("sv3", "savings", "A roof rack…", "La baca…",
  [("increases fuel use even when empty", "aumenta el consumo incluso sin carga"), ("only increases it when loaded", "solo aumenta el consumo cargada"), ("saves fuel", "ahorra combustible")],
  "Use it only when there is no other option.", "Solo si no hay otra opción.")
Q("sv4", "savings", "The recommended air-conditioning temperature is about…", "La temperatura recomendada del climatizador es de unos…",
  [("23 °C", "23 °C"), ("16 °C", "16 °C"), ("30 °C", "30 °C")],
  "It has a big effect on fuel use.", "Tiene gran incidencia en el consumo.")
Q("sv5", "savings", "At high speed on the road, it is better to…", "A velocidad alta en carretera es mejor…",
  [("use the vents or moderate air conditioning than open the windows", "usar las rejillas o el aire moderado que bajar las ventanillas"), ("drive with the windows down", "circular con las ventanillas bajadas"), ("open the sunroof", "abrir el techo")],
  "Open windows spoil the aerodynamics.", "Las ventanillas abiertas empeoran la aerodinámica.")
Q("sv6", "savings", "Coasting downhill in neutral…", "Bajar una pendiente en punto muerto…",
  [("should not be done", "no se debe hacer"), ("saves fuel and is recommended", "ahorra combustible y se recomienda"), ("is only allowed on motorways", "solo se permite en autopistas")],
  "In gear and off the throttle, fuel use is zero — and you keep control.", "Con marcha y sin acelerar el consumo es nulo, y se mantiene el control.")
Q("sv7", "savings", "Under-inflated tyres…", "Los neumáticos con menos presión de la recomendada…",
  [("increase fuel use and wear out sooner", "aumentan el consumo y duran menos"), ("save fuel", "ahorran combustible"), ("improve grip on dry roads", "mejoran la adherencia en seco")],
  "Use the manufacturer’s pressure.", "Usar la presión del fabricante.")
Q("sv8", "savings", "Using petrol with a lower octane than recommended…", "Usar gasolina de menor octanaje que el recomendado…",
  [("should not be done", "no se debe hacer"), ("saves money and fuel", "ahorra dinero y combustible"), ("is required in winter", "es obligatorio en invierno")],
  "Follow the manufacturer.", "Seguir al fabricante.")
Q("sv9", "savings", "Switching the lights on later at dusk to save fuel is…", "Retrasar el encendido de las luces al anochecer para ahorrar…",
  [("something you should not do", "es algo que no se debe hacer"), ("a recommended saving", "es un ahorro recomendado"), ("only allowed in town", "solo se permite en ciudad")],
  "Safety comes first.", "La seguridad es lo primero.")
Q("sv10", "savings", "The ECO driving mode…", "El modo ECO…",
  [("limits acceleration and climate control to save fuel", "limita la aceleración y la climatización para ahorrar"), ("disables the brakes", "desactiva los frenos"), ("is always on and can’t be switched off", "está siempre activo y no se puede desconectar")],
  "The driver can switch it on and off.", "El conductor lo conecta y desconecta.")
Q("sv11", "savings", "On a motorcycle, to save fuel you should not…", "En una moto, para ahorrar no se debe…",
  [("alter the fairing", "alterar el carenado"), ("keep the right tyre pressure", "llevar la presión correcta"), ("ride smoothly", "conducir con suavidad")],
  "It changes the aerodynamics.", "Afecta a la aerodinámica.")
Q("sv12", "savings", "Climbing a hill in a low gear with high revs…", "Subir una pendiente con marchas cortas y el motor revolucionado…",
  [("wastes fuel and should be avoided", "gasta más y se debe evitar"), ("is the most efficient way", "es lo más eficiente"), ("is compulsory", "es obligatorio")],
  "Use the highest gear that pulls well.", "Usar la marcha más alta posible.")

# ---------------------------------------------------------------- 2. pollution
Q("po1", "pollution", "The gas mainly responsible for the greenhouse effect is…", "El gas mayor responsable del efecto invernadero es…",
  [("CO₂ (carbon dioxide)", "el CO₂ (dióxido de carbono)"), ("SO₂ (sulphur dioxide)", "el SO₂ (dióxido de azufre)"), ("NOx", "los NOx")],
  "SO₂: acid rain.", "SO₂: lluvia ácida.")
Q("po2", "pollution", "Acid rain is caused mainly by…", "La lluvia ácida se debe sobre todo al…",
  [("sulphur dioxide (SO₂)", "dióxido de azufre (SO₂)"), ("carbon dioxide (CO₂)", "dióxido de carbono (CO₂)"), ("water vapour", "vapor de agua")],
  "CO₂: greenhouse effect.", "CO₂: efecto invernadero.")
Q("po3", "pollution", "Nitrogen oxides (NOx) mainly cause…", "Los óxidos de nitrógeno (NOx) causan sobre todo…",
  [("breathing problems", "problemas respiratorios"), ("acid rain only", "solo lluvia ácida"), ("nothing", "nada")],
  "HC: toxic unburnt hydrocarbons.", "HC: hidrocarburos sin quemar, tóxicos.")
Q("po4", "pollution", "Carbon monoxide (CO) is…", "El monóxido de carbono (CO) es…",
  [("very toxic and can kill", "muy tóxico y puede ser mortal"), ("harmless", "inofensivo"), ("the cause of acid rain", "la causa de la lluvia ácida")],
  "It is colourless and odourless.", "Es incoloro e inodoro.")
Q("po5", "pollution", "Changing the engine oil on the public road is…", "Cambiar el aceite del motor en la vía pública…",
  [("prohibited", "no está permitido"), ("allowed if you clean up", "se permite si se limpia"), ("allowed on the shoulder", "se permite en el arcén")],
  "Take the oil to a recovery container.", "Hay que entregarlo en un contenedor de recuperación.")
Q("po6", "pollution", "A vehicle makes noise above the limits. Agents can…", "Un vehículo emite ruido por encima de los límites. Los agentes pueden…",
  [("fine you and immobilise the vehicle", "sancionar e inmovilizar el vehículo"), ("only warn you", "solo avisar"), ("do nothing", "no hacer nada")],
  "Open exhausts, loud music, revving…", "Escape libre, música alta, acelerones…")
Q("po7", "pollution", "Which is ‘needless noise’?", "¿Cuál es un «ruido innecesario»?",
  [("An exhaust without a silencer", "Un escape libre sin silenciador"), ("The indicator click", "El clic del intermitente"), ("Normal engine noise", "El ruido normal del motor")],
  "Also resonator exhausts, horn, loud music, revving.", "También tubos resonadores, claxon, música alta, acelerones.")
Q("po8", "pollution", "Throwing a cigarette end onto the road is…", "Arrojar una colilla a la vía…",
  [("not allowed", "no está permitido"), ("allowed in towns", "está permitido en poblado"), ("allowed if it is out", "está permitido si está apagada")],
  "Also food waste and other objects.", "Tampoco restos de comida u otros objetos.")

# ---------------------------------------------------------------- 2. ZBE and urban access
Q("zb1", "zbe", "Which municipalities must have sustainable mobility plans with low-emission zones?", "¿Qué municipios deben tener planes de movilidad sostenible con zonas de bajas emisiones?",
  [("Over 50,000 people, island territories, and over 20,000 that exceed pollution limits", "Los de más de 50.000 habitantes, los territorios insulares y los de más de 20.000 que superen los límites"), ("Only Madrid and Barcelona", "Solo Madrid y Barcelona"), ("All municipalities", "Todos los municipios")],
  "Ley 7/2021 on climate change.", "Ley 7/2021 de cambio climático.")
Q("zb2", "zbe", "A low-emission zone (ZBE) restricts…", "Una zona de bajas emisiones (ZBE) restringe…",
  [("access, driving and parking according to each vehicle’s emissions classification", "el acceso, la circulación y el estacionamiento según la clasificación por emisiones"), ("only parking", "solo el estacionamiento"), ("only lorries", "solo los camiones")],
  "To improve air quality.", "Para mejorar la calidad del aire.")
Q("zb3", "zbe", "Sign R-120 means…", "La señal R-120 significa…",
  [("entry prohibited to vehicles according to their environmental label or other criteria", "entrada prohibida a vehículos en función de su distintivo ambiental u otros criterios"), ("no entry for lorries", "entrada prohibida a camiones"), ("end of the low-emission zone", "fin de la zona de bajas emisiones")],
  "The conditions are on an additional panel.", "Las condiciones, en un panel complementario.")
Q("zb4", "zbe", "Where are the conditions of an R-120 sign shown?", "¿Dónde se indican las condiciones de la señal R-120?",
  [("On an additional panel or a board that includes the sign", "En un panel complementario o en un cartel que incluya la señal"), ("Nowhere", "En ningún sitio"), ("Only online", "Solo en internet")],
  "For example, which labels may enter.", "Por ejemplo, qué distintivos pueden entrar.")
Q("zb5", "zbe", "A residential priority zone…", "Una zona de prioridad residencial…",
  [("restricts access or traffic for non-residents’ vehicles", "restringe el acceso o la circulación a vehículos de no residentes"), ("is only for buses", "es solo para autobuses"), ("allows any vehicle", "permite cualquier vehículo")],
  "Regulated by the town council.", "La regula la Autoridad municipal.")
Q("zb6", "zbe", "A safe school route is…", "Un camino escolar seguro es…",
  [("roads adapted so children can get to school on foot, by public transport or by non-motorised means", "un conjunto de vías acondicionadas para que los niños vayan al colegio a pie, en transporte público o en medios no motorizados"), ("a bus lane", "un carril bus"), ("a car park at the school", "un aparcamiento junto al colegio")],
  "It can have its own signs and speed limits.", "Puede tener señales y límites propios.")
Q("zb7", "zbe", "Near schools and hospitals, the authorities apply…", "Cerca de colegios y hospitales, las autoridades aplican…",
  [("speed limits, parking rules and traffic calming", "limitación de velocidad, estacionamiento y calmado del tráfico"), ("higher speed limits", "límites de velocidad más altos"), ("nothing special", "nada especial")],
  "To protect vulnerable users.", "Para proteger a los usuarios vulnerables.")
Q("zb8", "zbe", "Local authorities send information on their low-emission zones to…", "Las entidades locales comunican sus zonas de bajas emisiones al…",
  [("the National Access Point for traffic information", "Punto de Acceso Nacional de información de tráfico"), ("the ITV station", "la estación ITV"), ("the insurers", "las aseguradoras")],
  "Areas, criteria, hours and restrictions.", "Áreas, criterios, horarios y restricciones.")

# ---------------------------------------------------------------- 2. labels
Q("lb1", "labels", "How many DGT environmental labels are there?", "¿Cuántos distintivos ambientales de la DGT existen?",
  [("Four: 0, ECO, C and B", "Cuatro: 0, ECO, C y B"), ("Three", "Tres"), ("Six", "Seis")],
  "From most to least efficient.", "De mayor a menor eficiencia.")
Q("lb2", "labels", "Which label is the most efficient?", "¿Qué distintivo es el más eficiente?",
  [("0 (zero emissions)", "El 0 (cero emisiones)"), ("ECO", "El ECO"), ("C", "El C")],
  "Then ECO, C and B.", "Después ECO, C y B.")
Q("lb3", "labels", "A plug-in hybrid gets the 0 label if its electric range is at least…", "Un híbrido enchufable tiene el distintivo 0 si su autonomía eléctrica es de al menos…",
  [("40 km", "40 km"), ("10 km", "10 km"), ("90 km", "90 km")],
  "Under 40 km: ECO. The 90 km plan was dropped.", "Con menos de 40 km: ECO. La propuesta de 90 km se retiró.")
Q("lb4", "labels", "A non-plug-in hybrid (HEV) gets the label…", "Un híbrido no enchufable (HEV) tiene el distintivo…",
  [("ECO", "ECO"), ("0", "0"), ("B", "B")],
  "Also gas vehicles (CNG, LNG, LPG).", "También los de gas (GNC, GNL, GLP).")
Q("lb5", "labels", "To get the ECO label, a vehicle must also meet the criteria of label…", "Para tener el distintivo ECO, el vehículo debe cumplir además los criterios del…",
  [("C", "C"), ("B", "B"), ("0", "0")],
  "Latest Euro standards.", "Últimas normas Euro.")
Q("lb6", "labels", "A diesel car gets label C if it was registered from…", "Un turismo diésel tiene distintivo C si se matriculó desde…",
  [("September 2015", "septiembre de 2015"), ("January 2006", "enero de 2006"), ("2001", "2001")],
  "Petrol: from January 2006.", "Gasolina: desde enero de 2006.")
Q("lb7", "labels", "A petrol car gets label C if it was registered from…", "Un turismo de gasolina tiene distintivo C si se matriculó desde…",
  [("January 2006", "enero de 2006"), ("September 2015", "septiembre de 2015"), ("2001", "2001")],
  "Diesel: from September 2015.", "Diésel: desde septiembre de 2015.")
Q("lb8", "labels", "A petrol car registered in 2003 gets label…", "Un turismo de gasolina matriculado en 2003 tiene distintivo…",
  [("B", "B"), ("C", "C"), ("none", "ninguno")],
  "B: petrol from 1 January 2001.", "B: gasolina desde el 1 de enero de 2001.")
Q("lb9", "labels", "What colour is label B?", "¿De qué color es el distintivo B?",
  [("Yellow", "Amarillo"), ("Blue", "Azul"), ("Green", "Verde")],
  "0 blue, ECO blue and green, C green.", "0 azul, ECO azul y verde, C verde.")
Q("lb10", "labels", "Which vehicles get no environmental label?", "¿Qué vehículos no tienen distintivo ambiental?",
  [("The remaining 50 % most polluting", "El 50 % restante, el más contaminante"), ("Electric cars", "Los eléctricos"), ("Motorcycles", "Las motocicletas")],
  "They don’t meet the requirements.", "No cumplen los requisitos.")
Q("lb11", "labels", "Where should the label be stuck, if you display it?", "¿Dónde se coloca el distintivo, si se pone?",
  [("Bottom right corner of the windscreen", "En el ángulo inferior derecho del parabrisas"), ("Top left of the rear window", "Arriba a la izquierda de la luneta"), ("On the number plate", "En la matrícula")],
  "Motorcycles: anywhere visible.", "Motocicletas: en cualquier sitio visible.")
Q("lb12", "labels", "According to the DGT, displaying the environmental label is…", "Según la DGT, colocar el distintivo ambiental es…",
  [("voluntary, although some towns require it in their low-emission zones", "voluntario, aunque algunas ciudades lo exigen en sus ZBE"), ("always compulsory", "siempre obligatorio"), ("prohibited", "prohibido")],
  "If displayed, bottom right of the windscreen.", "Si se pone, abajo a la derecha del parabrisas.")
