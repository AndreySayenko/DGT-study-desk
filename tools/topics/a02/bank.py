# -*- coding: utf-8 -*-
"""Question bank for the interactive Category A1/A2, Topic 2 page (use of the road). In every question the FIRST
option is the correct one (the page shuffles options when it shows them). Ids must be unique and must not start
with "ai"."""

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
    "prin": dict(sec=1, en="Principles and the driver’s duties", es="Principios y obligaciones del conductor",
        recap=[("Four principles: don’t annoy, don’t surprise, warn, understand.", "Cuatro principios: no molestar, no sorprender, advertir y comprender."),
               ("Signalling a manoeuvre does not give you the right to make it.", "Advertir una maniobra no da derecho a realizarla."),
               ("Ride with care; no negligent or reckless riding, no pavements, no zigzag.", "Conducir con diligencia; nada de conducción negligente o temeraria, ni aceras, ni zigzag."),
               ("Keep freedom of movement, field of vision and constant attention; extra care near children, elderly and blind people.", "Mantener libertad de movimientos, campo de visión y atención permanente; precaución con niños, ancianos e invidentes.")],
        trap=("Thinking that signalling in time gives you priority.", "Pensar que señalizar a tiempo da prioridad.")),
    "dev": dict(sec=1, en="Phones, screens and headphones", es="Móvil, pantallas y auriculares",
        recap=[("Phone: prohibited even just held in your hand; only hands-free without headphones.", "Móvil: prohibido incluso solo sujetándolo; solo sin manos y sin auriculares."),
               ("Approved wireless device built into the helmet: allowed, only for intercom or navigation.", "Dispositivo inalámbrico homologado integrado en el casco: permitido, solo para intercomunicación o navegación."),
               ("Headphones connected to sound devices: prohibited, except lessons and tests on open roads when required.", "Auriculares conectados a aparatos de sonido: prohibidos, salvo enseñanza y pruebas en circuito abierto cuando se exija."),
               ("Screens with internet or TV: no. GPS and manoeuvring cameras: yes — the GPS not handled while moving.", "Pantallas con internet o TV: no. GPS y cámaras de maniobra: sí; el GPS sin manipularlo en marcha.")],
        trap=("Thinking earphones under the helmet count as the allowed intercom.", "Pensar que unos auriculares bajo el casco equivalen al intercomunicador permitido.")),
    "proh": dict(sec=1, en="Other prohibitions", es="Otras prohibiciones",
        recap=[("Don’t throw or leave objects that can cause fires, pollution or danger.", "No arrojar ni abandonar objetos que puedan causar incendios, contaminación o peligro."),
               ("Radar jammers and detectors: prohibited. Apps that only show where cameras are: allowed.", "Inhibidores y detectores de radar: prohibidos. Avisadores que solo informan de dónde hay radares: permitidos."),
               ("Don’t warn others that traffic agents are present.", "No avisar a otros de la presencia de agentes."),
               ("No open exhaust; refuel with engine, lights, radio and phone off.", "Nada de escape libre; repostar con motor, luces, radio y móvil apagados.")],
        trap=("Mixing up a radar detector (prohibited) with a camera-location app (allowed).", "Confundir un detector de radar (prohibido) con un avisador de radares (permitido).")),
    "lanes": dict(sec=2, en="Which lane", es="Qué carril",
        recap=[("Ride on the carriageway, as close to the right edge as possible.", "Circular por la calzada, lo más cerca posible del borde derecho."),
               ("Two-way, three lanes: right lane; centre only to overtake or turn left; left never.", "Doble sentido con tres carriles: el derecho; el central solo para adelantar o girar a la izquierda; el izquierdo nunca."),
               ("Out of town, one way: normally the rightmost; the others to overtake.", "Fuera de poblado, sentido único: normalmente el de la derecha; los demás para adelantar."),
               ("In town, one way, marked lanes: the one best for your destination (not on autopistas or autovías).", "En poblado, sentido único, carriles marcados: el que mejor convenga al destino (no en autopistas ni autovías).")],
        trap=("Using the centre lane of a three-lane two-way road as a normal lane.", "Usar el carril central de una vía de tres carriles y doble sentido como carril normal.")),
    "pos": dict(sec=3, en="Islands, roundabouts, carriageways", es="Isletas, glorietas y calzadas",
        recap=[("Island separating two directions: keep it on your left.", "Isleta que separa dos sentidos: dejarla a la izquierda."),
               ("One-way road or within one direction: either side.", "Vía de sentido único o dentro de un mismo sentido: por ambos lados."),
               ("Roundabouts: centre on your left; interurban: rightmost lane; urban: best for destination.", "Glorietas: centro a la izquierda; interurbana: carril derecho; urbana: el que convenga."),
               ("Two carriageways: the right one. Three: side ones one way, centre one or two ways.", "Dos calzadas: la de la derecha. Tres: laterales de un sentido, central de uno o dos.")],
        trap=("Passing an island between two directions on its left.", "Pasar una isleta entre dos sentidos por su izquierda.")),
    "vao": dict(sec=4, en="VAO lanes", es="Carril VAO",
        recap=[("VAO: automóviles for people, MMA ≤ 3,500 kg, occupants set per stretch (usually 2).", "VAO: automóviles de personas, MMA ≤ 3.500 kg, ocupantes fijados por tramo (normalmente 2)."),
               ("Motorcycles may use it alone; mopeds may not.", "Las motos pueden usarlo solas; los ciclomotores no."),
               ("Alone: V-15 or disabled card; buses > 3,500 kg any occupancy; priority vehicles on duty.", "Solo el conductor: V-15 o tarjeta de discapacidad; autobuses > 3.500 kg con cualquier ocupación; prioritarios en servicio."),
               ("Since 2026, cars with a label and one occupant only when the panels allow it. Breaking the rules: serious.", "Desde 2026, turismos con etiqueta y un ocupante solo si lo permiten los paneles. Infringirlo: grave.")],
        trap=("Thinking a zero-emission car may always use the VAO lane alone.", "Pensar que un 0 emisiones puede usar siempre el VAO con un solo ocupante.")),
    "slip": dict(sec=4, en="Acceleration and deceleration lanes", es="Carriles de aceleración y deceleración",
        recap=[("Acceleration lane: reach the right speed by its end.", "Aceleración: alcanzar la velocidad adecuada al final del carril."),
               ("At its start, check you can merge — stopping if necessary.", "Al principio, cerciorarse de poder incorporarse, deteniéndose si es necesario."),
               ("Deceleration lane: move to the lane nearest the exit, enter as soon as possible.", "Deceleración: situarse en el carril más próximo a la salida y entrar cuanto antes."),
               ("Slow down inside the deceleration lane, not on the main road.", "Reducir la velocidad dentro del carril de deceleración, no en la vía principal.")],
        trap=("Braking on the main carriageway before reaching the exit lane.", "Frenar en la calzada principal antes de llegar al carril de salida.")),
    "flow": dict(sec=4, en="Reversible, additional and contraflow lanes", es="Carriles reversible, adicional y en sentido contrario",
        recap=[("Reversible: double broken lines both sides; dipped headlights day and night.", "Reversible: doble línea discontinua a ambos lados; luz de cruce de día y de noche."),
               ("Additional: uses both shoulders; dipped headlights; 60–80 km/h.", "Adicional circunstancial: usa ambos arcenes; luz de cruce; 60–80 km/h."),
               ("Contraflow for flow: only motorcycles and cars without trailer; 60–80 km/h; never move into the normal lanes.", "Sentido contrario por fluidez: solo motos y turismos sin remolque; 60–80 km/h; sin invadir el sentido normal."),
               ("Reserved and slip lanes don’t count when counting lanes.", "Los carriles reservados y los de aceleración o deceleración no se cuentan.")],
        trap=("Thinking any vehicle may use a contraflow lane opened for traffic flow.", "Pensar que cualquier vehículo puede usar un carril en sentido contrario abierto por fluidez.")),
    "shoulder": dict(sec=5, en="The hard shoulder", es="El arcén",
        recap=[("Motorcycles ride on the carriageway; the shoulder only in an emergency or the new jam rule.", "La moto circula por la calzada; el arcén solo por emergencia o en el nuevo supuesto de atasco."),
               ("Jam rule (1-10-2026): signed stretches, lanes stopped by congestion, ≤ 30 km/h, single file.", "Atascos (1-10-2026): tramos señalizados, carriles detenidos por congestión, ≤ 30 km/h, en columna de a uno."),
               ("Don’t endanger those obliged to use the shoulder; leave it if needed.", "No poner en riesgo a los obligados a usar el arcén; abandonarlo si es preciso."),
               ("Broken down but able to go on: continue at once; needing help: first exit along the right shoulder.", "Averiada pero puede seguir: continuar enseguida; si necesita auxilio: primera salida por el arcén derecho.")],
        trap=("Thinking slow traffic is enough to use the shoulder — it must be stopped.", "Pensar que basta con tráfico lento: debe estar detenido.")),
    "dist": dict(sec=6, en="Safety distance", es="Distancia de seguridad",
        recap=[("Enough space to stop without hitting the vehicle in front if it brakes hard.", "Espacio para detenerse sin chocar si el de delante frena bruscamente."),
               ("Not signalling an overtake: also leave room for others to overtake you.", "Sin señalizar adelantamiento: dejar también sitio para que le adelanten."),
               ("A collision-avoiding gap is enough in town, where overtaking is banned, with several lanes, in dense traffic or when about to overtake.", "Basta la que evite la colisión en poblado, con adelantamiento prohibido, con varios carriles, con tráfico saturado o al ir a adelantar."),
               ("Tunnels: 100 m or 4 s. Fixed 50 m: heavy or long vehicles out of town.", "Túneles: 100 m o 4 s. 50 m fijos: pesados o largos fuera de poblado.")],
        trap=("Applying the 50 m rule to motorcycles.", "Aplicar la regla de los 50 m a las motos.")),
}

# ---------------------------------------------------------------- principles and duties
Q("pr1", "prin", "Which four principles should guide your behaviour on the road?", "¿Qué cuatro principios deben guiar el comportamiento en la vía?",
  [("Don’t annoy, don’t surprise, warn and understand", "No molestar, no sorprender, advertir y comprender"), ("Speed, priority, signalling and braking", "Velocidad, prioridad, señalización y frenado"), ("Look, accelerate, overtake and return", "Mirar, acelerar, adelantar y volver")],
  "They are the basis of living together on the road.", "Son la base de la convivencia en la vía.")
Q("pr2", "prin", "You signal a lane change in good time. Does that give you the right to make it?", "Señalizas con antelación un cambio de carril. ¿Te da derecho a realizarlo?",
  [("No: you must still make sure it can be done without danger", "No: hay que asegurarse de que puede hacerse sin peligro"), ("Yes: the others must let you in", "Sí: los demás deben dejarte pasar"), ("Yes, if you signal for at least 3 seconds", "Sí, si señalizas al menos 3 segundos")],
  "Warning others is a duty, not a priority.", "Advertir es una obligación, no una prioridad.")
Q("pr3", "prin", "The principle of “understanding” (comprender) means…", "El principio de «comprender» significa…",
  [("understanding others’ warnings and forgiving their mistakes, without excusing your own", "comprender las advertencias de los demás y disculpar sus errores, sin justificar los propios"), ("expecting others to understand your mistakes", "esperar que los demás comprendan tus errores"), ("answering others’ mistakes with the horn", "responder con el claxon a los errores ajenos")],
  "Without turning aggressive.", "Sin adoptar un comportamiento agresivo.")
Q("pr4", "prin", "Changing lanes suddenly without any warning breaks above all the principle of…", "Cambiar de carril de forma súbita sin avisar incumple sobre todo el principio de…",
  [("not surprising others", "no sorprender"), ("understanding", "comprender"), ("none, if the lane is free", "ninguno, si el carril está libre")],
  "Others need time to react.", "Los demás necesitan tiempo para reaccionar.")
Q("pr5", "prin", "Who shares the public road and has rights and duties on it?", "¿Quiénes conviven en la vía pública con derechos y obligaciones?",
  [("Drivers, pedestrians and animals", "Conductores, peatones y animales"), ("Only drivers", "Solo los conductores"), ("Only drivers and pedestrians", "Solo conductores y peatones")],
  "Cooperation between all of them is essential.", "La colaboración entre todos es esencial.")
Q("pr6", "prin", "To get past a queue, may you ride a short stretch on the pavement?", "Para salir de una cola, ¿puedes circular un tramo corto por la acera?",
  [("No, never", "No, nunca"), ("Yes, at walking pace", "Sí, al paso"), ("Yes, if there are no pedestrians", "Sí, si no hay peatones")],
  "Motorcycles may not ride on pavements or other pedestrian areas.", "Las motos no pueden circular por aceras ni zonas peatonales.")
Q("pr7", "prin", "You approach a group of children near the edge of the road. You must…", "Te acercas a un grupo de niños junto al borde de la vía. Debes…",
  [("take extra precautions", "adoptar las precauciones necesarias"), ("keep your speed: they are off the carriageway", "mantener la velocidad: no están en la calzada"), ("sound the horn and carry on", "tocar el claxon y seguir")],
  "Children, elderly people, blind people and people with reduced mobility need special care.", "Niños, ancianos, invidentes y personas con movilidad reducida requieren especial cuidado.")
Q("pr8", "prin", "Weaving (zigzagging) between cars in heavy traffic on a motorcycle is…", "Circular en zigzag entre los coches con tráfico denso en moto está…",
  [("prohibited", "prohibido"), ("allowed for motorcycles", "permitido para motocicletas"), ("allowed below 30 km/h", "permitido por debajo de 30 km/h")],
  "It is especially dangerous when traffic is saturated.", "Es especialmente peligroso con el tráfico saturado.")
Q("pr9", "prin", "While riding you must keep…", "Durante la conducción debes mantener…",
  [("your freedom of movement, the field of vision you need and constant attention", "la libertad de movimientos, el campo de visión necesario y la atención permanente"), ("constant attention only when overtaking", "la atención permanente solo al adelantar"), ("only a clear view to the front", "solo la visión hacia delante")],
  "Your position, your passenger’s and the load all count.", "Cuentan tu posición, la del pasajero y la de la carga.")
Q("pr10", "prin", "Riding in a way that shows clear contempt for others’ lives is called…", "Conducir con manifiesto desprecio por la vida de los demás se llama…",
  [("reckless driving (conducción temeraria)", "conducción temeraria"), ("negligent driving", "conducción negligente"), ("defensive driving", "conducción defensiva")],
  "Both reckless and negligent driving are prohibited.", "Tanto la conducción temeraria como la negligente están prohibidas.")

# ---------------------------------------------------------------- devices
Q("ph1", "dev", "You ride holding your phone in your hand, but you are not using it. This is…", "Circulas con el móvil sujeto en la mano, aunque no lo usas. Esto está…",
  [("prohibited", "prohibido"), ("allowed, because you aren’t using it", "permitido, porque no lo usas"), ("allowed only in town", "permitido solo en poblado")],
  "Holding it is enough to break the rule.", "Basta con sujetarlo para incumplir la norma.")
Q("ph2", "dev", "You may talk on the phone while riding only if…", "Solo puedes hablar por teléfono conduciendo si…",
  [("you don’t use your hands, headphones or similar", "no empleas las manos ni usas cascos, auriculares o similares"), ("you hold it with one hand below 50 km/h", "lo sujetas con una mano por debajo de 50 km/h"), ("the call lasts less than a minute", "la llamada dura menos de un minuto")],
  "For motorcyclists, the usual way is an approved helmet intercom.", "En moto, lo habitual es un intercomunicador homologado en el casco.")
Q("ph3", "dev", "Who is exempt from the ban on using a phone while driving?", "¿Quién está exento de la prohibición de usar el móvil conduciendo?",
  [("Traffic agents performing their duties", "Los agentes de la autoridad en el ejercicio de sus funciones"), ("Delivery riders", "Los repartidores"), ("Professional drivers", "Los conductores profesionales")],
  "Nobody else is.", "Nadie más.")
Q("ph4", "dev", "A certified wireless intercom built into your helmet, used to talk to your passenger, is…", "Un intercomunicador inalámbrico certificado integrado en el casco, para hablar con tu pasajero, está…",
  [("allowed, if it doesn’t affect safety", "permitido, si no afecta a la seguridad"), ("prohibited", "prohibido"), ("allowed only when stopped", "permitido solo con la moto parada")],
  "Only for intercom or navigation.", "Solo para intercomunicación o navegación.")
Q("ph5", "dev", "Earphones under your helmet connected to a music player are…", "Unos auriculares bajo el casco conectados a un reproductor de música están…",
  [("prohibited", "prohibidos"), ("allowed at low volume", "permitidos a bajo volumen"), ("allowed on autopistas and autovías", "permitidos en autopistas y autovías")],
  "They reduce the constant attention you need.", "Disminuyen la atención permanente a la conducción.")
Q("ph6", "dev", "Riding with your phone wedged between your helmet and your head costs…", "Circular con el móvil ajustado entre el casco y la cabeza supone…",
  [("3 points", "3 puntos"), ("no penalty: your hands are free", "ninguna sanción: tienes las manos libres"), ("1 point", "1 punto")],
  "Annex II of the Ley sobre Tráfico; holding it in your hand costs 6.", "Anexo II de la Ley sobre Tráfico; sujetarlo con la mano supone 6.")
Q("ph7", "dev", "A sat-nav (GPS) on the motorcycle…", "Un navegador (GPS) en la moto…",
  [("may be used, but not handled while moving", "puede usarse, pero sin manipularlo en marcha"), ("is prohibited", "está prohibido"), ("may be programmed while moving at low speed", "puede programarse en marcha a baja velocidad")],
  "Set the route before setting off or when stopped safely.", "Programa la ruta antes de salir o parado en lugar seguro.")
Q("ph8", "dev", "Which of these is allowed in view while moving?", "¿Cuál de estas pantallas se permite con el vehículo en movimiento?",
  [("The GPS screen", "La pantalla del GPS"), ("A screen with internet access", "Una pantalla con acceso a internet"), ("A video player", "Un reproductor de vídeo")],
  "Rear manoeuvring cameras are also allowed.", "También las cámaras traseras de maniobra.")
Q("ph9", "dev", "During the skills test on open roads, the examiner gives you instructions through an earpiece. This is…", "En la prueba de circulación en vías abiertas, el examinador te da instrucciones por un auricular. Esto está…",
  [("allowed: it is an exception to the ban", "permitido: es una excepción a la prohibición"), ("prohibited", "prohibido"), ("allowed only on a closed circuit", "permitido solo en circuito cerrado")],
  "Lessons and tests on open roads, when the rules require it.", "Enseñanza y pruebas en circuito abierto, cuando lo exija la norma.")
Q("ph10", "dev", "A helmet-integrated wireless device may be used for…", "Un dispositivo inalámbrico integrado en el casco puede usarse para…",
  [("intercom or navigation", "intercomunicación o navegación"), ("watching videos", "ver vídeos"), ("anything, if it is approved", "cualquier cosa, si está homologado")],
  "And only if it doesn’t affect safety.", "Y solo si no afecta a la seguridad.")

# ---------------------------------------------------------------- other prohibitions
Q("ot1", "proh", "Throwing a lit cigarette from your motorcycle is…", "Arrojar una colilla encendida desde la moto está…",
  [("prohibited: it can cause a fire", "prohibido: puede provocar un incendio"), ("allowed if nobody is behind you", "permitido si no viene nadie detrás"), ("allowed in town", "permitido en poblado")],
  "Nothing that can cause fires or pollution may be thrown.", "No se puede arrojar nada que pueda causar incendios o contaminación.")
Q("ot2", "proh", "Carrying a radar detector on the motorcycle is…", "Llevar un detector de radar en la moto está…",
  [("prohibited", "prohibido"), ("allowed if it is switched off", "permitido si va apagado"), ("allowed", "permitido")],
  "Fitting or carrying it is enough.", "Basta con instalarlo o llevarlo.")
Q("ot3", "proh", "A phone app that only tells you where the speed cameras are is…", "Una aplicación que solo indica dónde están los radares está…",
  [("allowed", "permitida"), ("prohibited, like a detector", "prohibida, como un detector"), ("allowed only for professionals", "permitida solo a profesionales")],
  "It doesn’t detect or jam anything.", "No detecta ni interfiere nada.")
Q("ot4", "proh", "Flashing your lights to warn oncoming drivers of a police check is…", "Hacer ráfagas para avisar a los que vienen de un control policial está…",
  [("prohibited", "prohibido"), ("allowed", "permitido"), ("recommended", "recomendado")],
  "Warning of the presence or surveillance of agents is prohibited.", "Está prohibido advertir de la presencia o vigilancia de los agentes.")
Q("ot5", "proh", "Riding a motorcycle with an open exhaust (no silencer) is…", "Circular en moto con escape libre (sin silenciador) está…",
  [("prohibited", "prohibido"), ("allowed out of town", "permitido fuera de poblado"), ("allowed above 500 cm³", "permitido a partir de 500 cm³")],
  "Noise above the limits is prohibited.", "Se prohíben los ruidos por encima de los límites.")
Q("ot6", "proh", "When refuelling your motorcycle you must…", "Al repostar la moto debes…",
  [("stop the engine and switch off the lights, the radio and the phone", "parar el motor y apagar las luces, la radio y el móvil"), ("keep the engine running for a quick refill", "mantener el motor en marcha para repostar rápido"), ("only stop the engine", "solo parar el motor")],
  "Lights off too.", "También con las luces apagadas.")
Q("ot7", "proh", "Part of your load falls onto the carriageway. You must…", "Parte de tu carga cae a la calzada. Debes…",
  [("signal it and have it removed as soon as possible", "señalizarla y retirarla cuanto antes"), ("carry on: the road service will remove it", "seguir: la retirará el servicio de carreteras"), ("only signal it at night", "señalizarla solo de noche")],
  "Day and night.", "De día y de noche.")
Q("ot8", "proh", "A device that interferes with speed cameras (a jammer) is…", "Un dispositivo que interfiere en los radares (inhibidor) está…",
  [("prohibited", "prohibido"), ("allowed if it is approved", "permitido si está homologado"), ("allowed out of town", "permitido fuera de poblado")],
  "Fitting or carrying one is prohibited.", "Está prohibido instalarlo o llevarlo.")

# ---------------------------------------------------------------- lanes
Q("ln1", "lanes", "On a two-way road with one lane in each direction, you ride…", "En una vía de doble sentido con un carril para cada sentido, circulas…",
  [("in the right-hand lane, as close as possible to the right edge", "por el carril derecho, lo más cerca posible del borde derecho"), ("in the centre of the road", "por el centro de la vía"), ("on the hard shoulder", "por el arcén")],
  "Especially in bends and brows with poor visibility.", "Sobre todo en curvas y cambios de rasante de visibilidad reducida.")
Q("ln2", "lanes", "On a two-way road with three lanes separated by broken lines, the centre lane may be used…", "En una vía de doble sentido con tres carriles separados por líneas discontinuas, el carril central puede usarse…",
  [("only to overtake or to turn left", "solo para adelantar o girar a la izquierda"), ("as a normal lane", "como carril normal"), ("never", "nunca")],
  "Ride normally in the right-hand lane.", "Normalmente se circula por el derecho.")
Q("ln3", "lanes", "On that same two-way road with three lanes, the left-hand lane…", "En esa misma vía de doble sentido con tres carriles, el carril izquierdo…",
  [("may never be used", "no puede utilizarse nunca"), ("may be used to overtake", "puede usarse para adelantar"), ("may be used to turn left", "puede usarse para girar a la izquierda")],
  "It belongs to the opposite direction.", "Pertenece al sentido contrario.")
Q("ln4", "lanes", "Out of town, on a one-way carriageway with three lanes, you normally ride…", "Fuera de poblado, en una calzada de sentido único con tres carriles, circulas normalmente…",
  [("in the rightmost lane; the others are for overtaking", "por el carril de la derecha; los demás son para adelantar"), ("in any lane", "por cualquier carril"), ("in the centre lane", "por el carril central")],
  "Without hindering anyone coming behind.", "Sin entorpecer a quien venga detrás.")
Q("ln5", "lanes", "In town, on a one-way street with marked lanes, you may use…", "En poblado, en una calle de sentido único con carriles marcados, puedes usar…",
  [("the lane that best suits your destination", "el carril que mejor convenga a tu destino"), ("only the right-hand lane", "solo el carril derecho"), ("only the left-hand lane", "solo el carril izquierdo")],
  "Without hindering others.", "Sin obstaculizar a los demás.")
Q("ln6", "lanes", "In town, on a one-way street whose lanes are not marked, you ride…", "En poblado, en una calle de sentido único sin carriles marcados, circulas…",
  [("on the right", "por la derecha"), ("wherever suits your destination", "por donde convenga a tu destino"), ("in the centre", "por el centro")],
  "“Best for your destination” requires marked lanes.", "«El que mejor convenga» exige carriles delimitados.")
Q("ln7", "lanes", "On an autovía that crosses a city with marked lanes, may you use whichever lane best suits your destination?", "En una autovía que cruza una ciudad con carriles marcados, ¿puedes usar el carril que mejor convenga a tu destino?",
  [("No: normally the rightmost; the others to overtake", "No: normalmente el de la derecha; los demás para adelantar"), ("Yes, because it is in town", "Sí, porque es en poblado"), ("Yes, if traffic is light", "Sí, si hay poco tráfico")],
  "The urban exception doesn’t apply to autopistas and autovías.", "La excepción urbana no vale en autopistas y autovías.")
Q("ln8", "lanes", "As a rule, may a motorcycle ride on the hard shoulder?", "Como norma general, ¿puede una moto circular por el arcén?",
  [("No: only in an emergency or on signed stretches when traffic is stopped", "No: solo por emergencia o en tramos señalizados con el tráfico detenido"), ("Yes, always", "Sí, siempre"), ("Yes, below 45 km/h", "Sí, por debajo de 45 km/h")],
  "Motorcycles ride on the carriageway.", "La moto circula por la calzada.")
Q("ln9", "lanes", "In town, in a marked lane, you may leave it only to…", "En poblado, en un carril marcado, solo puedes abandonarlo para…",
  [("turn, overtake, stop or park", "cambiar de dirección, adelantar, parar o estacionar"), ("ride faster than the others", "circular más rápido que los demás"), ("ride between two lanes", "circular entre dos carriles")],
  "Otherwise, stay in it.", "Si no, se permanece en él.")
Q("ln10", "lanes", "In a bend with poor visibility on a two-way road, you should ride…", "En una curva de visibilidad reducida en una vía de doble sentido, debes circular…",
  [("as close as possible to the right-hand edge", "lo más cerca posible del borde derecho"), ("near the centre line to see better", "cerca de la línea central para ver mejor"), ("in the centre of your lane", "por el centro de tu carril")],
  "Leave the opposite half completely free.", "Dejando completamente libre la mitad contraria.")

# ---------------------------------------------------------------- position
Q("po1", "pos", "An island separates the two directions of traffic. You pass it…", "Una isleta separa los dos sentidos de circulación. La rebasas…",
  [("on its right, leaving it on your left", "por su derecha, dejándola a la izquierda"), ("on either side", "por cualquier lado"), ("on its left", "por su izquierda")],
  "Otherwise you would enter the opposite direction.", "Si no, entrarías en el sentido contrario.")
Q("po2", "pos", "An island on a one-way road may be passed…", "Una isleta en una vía de sentido único se puede rebasar…",
  [("on either side", "por ambos lados"), ("only on its right", "solo por su derecha"), ("only on its left", "solo por su izquierda")],
  "The same within one direction’s half of a two-way road.", "Lo mismo dentro de la parte de un sentido en una vía de doble sentido.")
Q("po3", "pos", "In squares, roundabouts and junctions you go round…", "En plazas, glorietas e intersecciones se circula…",
  [("leaving the centre on your left", "dejando el centro a la izquierda"), ("leaving the centre on your right", "dejando el centro a la derecha"), ("whichever way is shorter", "por el lado más corto")],
  "Anticlockwise in Spain.", "En sentido antihorario en España.")
Q("po4", "pos", "In a roundabout on an interurban road with two marked lanes, you normally use…", "En una glorieta de vía interurbana con dos carriles marcados, normalmente usas…",
  [("the lane nearest the right", "el carril más próximo a la derecha"), ("the inner lane", "el carril interior"), ("whichever suits your exit", "el que convenga a tu salida")],
  "The others only when traffic or the road advise it.", "Los demás solo cuando lo aconsejen el tráfico o la vía.")
Q("po5", "pos", "In a roundabout on an urban road with two marked lanes, you may use…", "En una glorieta de vía urbana con dos carriles marcados, puedes usar…",
  [("the lane that best suits your destination", "el carril que mejor convenga a tu destino"), ("only the outer lane", "solo el carril exterior"), ("only the inner lane", "solo el carril interior")],
  "Without cutting across vehicles in an outer lane.", "Sin cortar la trayectoria de quien va por un carril exterior.")
Q("po6", "pos", "Leaving a roundabout from the inner lane, you must not…", "Al salir de una glorieta desde el carril interior, no debes…",
  [("cut across a vehicle in an outer lane", "cortar la trayectoria de un vehículo que va por un carril exterior"), ("signal to the right", "señalizar a la derecha"), ("slow down", "reducir la velocidad")],
  "Move out in good time.", "Hay que desplazarse con antelación.")
Q("po7", "pos", "On a road with two carriageways you use…", "En una vía con dos calzadas utilizas…",
  [("the one on the right for your direction", "la de la derecha según el sentido de la marcha"), ("either one", "cualquiera de las dos"), ("the one on the left", "la de la izquierda")],
  "Each carriageway carries one direction.", "Cada calzada lleva un sentido.")
Q("po8", "pos", "On a road with three carriageways…", "En una vía con tres calzadas…",
  [("the centre one may carry one or two directions; the side ones, one direction", "la central puede ser de uno o dos sentidos; las laterales, de uno solo"), ("all three carry both directions", "las tres son de doble sentido"), ("the centre one is only for motorcycles", "la central es solo para motos")],
  "Unless signs say otherwise.", "Salvo otra señalización.")

# ---------------------------------------------------------------- VAO
Q("va1", "vao", "May you use a VAO lane riding your motorcycle alone?", "¿Puedes usar un carril VAO circulando solo en tu moto?",
  [("Yes: motorcycles need no passenger", "Sí: las motos no necesitan acompañante"), ("No: at least two people are needed", "No: se necesitan al menos dos personas"), ("Only with an ECO label", "Solo con etiqueta ECO")],
  "Motorcycles are among the vehicles allowed to use it.", "Las motos están entre los vehículos autorizados.")
Q("va2", "vao", "May a moped use a VAO lane?", "¿Puede un ciclomotor usar un carril VAO?",
  [("No, never", "No, nunca"), ("Yes, with a passenger", "Sí, con pasajero"), ("Yes, like a motorcycle", "Sí, como una moto")],
  "Mopeds, cycles, VMP and pedestrians are excluded.", "Ciclomotores, ciclos, VMP y peatones están excluidos.")
Q("va3", "vao", "A high-occupancy vehicle (VAO) has an MMA of no more than…", "Un vehículo de alta ocupación (VAO) tiene una MMA no superior a…",
  [("3,500 kg", "3.500 kg"), ("2,500 kg", "2.500 kg"), ("7,500 kg", "7.500 kg")],
  "And carries only people.", "Y transporta solo personas.")
Q("va4", "vao", "Since 2026, may a zero-emission car with only the driver aboard use a VAO lane?", "Desde 2026, ¿puede un turismo 0 emisiones con solo el conductor usar el carril VAO?",
  [("Only when traffic allows it and the entrance panels say so", "Solo cuando lo permita el tráfico y lo indiquen los paneles de acceso"), ("Yes, always", "Sí, siempre"), ("No, never", "No, nunca")],
  "Your course still says “always”: that changed in January 2026.", "Tu curso aún dice «siempre»: eso cambió en enero de 2026.")
Q("va5", "vao", "A car towing a trailer, with three people aboard, may use a VAO lane?", "Un turismo con remolque y tres ocupantes, ¿puede usar el carril VAO?",
  [("No: cars with a trailer are excluded", "No: los turismos con remolque están excluidos"), ("Yes: it has enough occupants", "Sí: tiene ocupantes suficientes"), ("Yes, if the trailer is light", "Sí, si el remolque es ligero")],
  "Only motorcycles, cars and adaptable mixed vehicles — without trailers.", "Solo motos, turismos y mixtos adaptables, sin remolque.")
Q("va6", "vao", "A bus with an MMA over 3,500 kg carrying only its driver…", "Un autobús de MMA superior a 3.500 kg con solo el conductor…",
  [("may use the VAO lane", "puede usar el carril VAO"), ("needs at least two occupants", "necesita al menos dos ocupantes"), ("may not use it", "no puede usarlo")],
  "Buses over 3,500 kg and articulated buses, whatever the occupancy.", "Autobuses de más de 3.500 kg y articulados, con independencia de los ocupantes.")
Q("va7", "vao", "Breaking the rules on using a VAO lane is an offence classed as…", "Incumplir las normas de uso del carril VAO es una infracción…",
  [("serious", "grave"), ("minor", "leve"), ("very serious", "muy grave")],
  "Art. 35.3 of the Reglamento General de Circulación.", "Art. 35.3 del Reglamento General de Circulación.")
Q("va8", "vao", "A car carrying only its driver and showing the V-15 sign (disabled driver)…", "Un turismo con solo el conductor y la señal V-15 (persona con discapacidad)…",
  [("may use the VAO lane", "puede usar el carril VAO"), ("needs a passenger", "necesita un acompañante"), ("may use it only at night", "solo puede usarlo de noche")],
  "The disabled parking card also allows it.", "También la tarjeta de estacionamiento para personas con movilidad reducida.")
Q("va9", "vao", "An ambulance on urgent service may use the VAO lane…", "Una ambulancia en servicio de urgencia puede usar el carril VAO…",
  [("yes, like other priority vehicles", "sí, como el resto de prioritarios"), ("only with two occupants", "solo con dos ocupantes"), ("no", "no")],
  "Road-maintenance crews may too.", "También los equipos de mantenimiento de la vía.")
Q("va10", "vao", "As a rule, the minimum occupancy for a car in a VAO lane is…", "Como norma general, la ocupación mínima de un turismo en el carril VAO es…",
  [("two people, driver included", "dos personas, incluido el conductor"), ("two people plus the driver", "dos personas más el conductor"), ("four people", "cuatro personas")],
  "The number is set for each stretch.", "El número se fija para cada tramo.")
Q("va11", "vao", "A lorry with two people aboard may use the VAO lane?", "Un camión con dos ocupantes, ¿puede usar el carril VAO?",
  [("No", "No"), ("Yes", "Sí"), ("Yes, if its MMA is over 3,500 kg", "Sí, si su MMA supera 3.500 kg")],
  "VAO is for vehicles carrying people.", "El VAO es para vehículos de transporte de personas.")

# ---------------------------------------------------------------- slip roads
Q("ac1", "slip", "In an acceleration lane, you should reach a suitable speed…", "En un carril de aceleración, debes alcanzar la velocidad adecuada…",
  [("by the end of the lane", "al final del carril"), ("at its start", "al principio del carril"), ("after joining the main road", "tras incorporarte a la vía principal")],
  "So that you can join safely.", "Para incorporarte con seguridad.")
Q("ac2", "slip", "At the start of the acceleration lane you see you can’t join safely. You…", "Al principio del carril de aceleración ves que no puedes incorporarte con seguridad. Tú…",
  [("may even have to stop", "puedes llegar a tener que detenerte"), ("accelerate: the others must let you in", "aceleras: los demás deben dejarte pasar"), ("carry on along the hard shoulder", "continúas por el arcén")],
  "Joining depends on the position, path and speed of the others.", "La incorporación depende de la posición, trayectoria y velocidad de los demás.")
Q("ac3", "slip", "To leave by a deceleration lane, you…", "Para salir por un carril de deceleración…",
  [("enter it as soon as possible and slow down inside it", "entras en él cuanto antes y reduces la velocidad dentro"), ("brake on the main carriageway before entering", "frenas en la calzada principal antes de entrar"), ("enter at its very end", "entras al final del carril")],
  "Without hindering those staying on the main road.", "Sin entorpecer a quienes siguen por la vía principal.")
Q("ac4", "slip", "Before taking an exit, you should ride…", "Antes de tomar una salida, debes circular…",
  [("in the lane nearest the exit", "por el carril más próximo a la salida"), ("in the left-hand lane", "por el carril izquierdo"), ("in any lane", "por cualquier carril")],
  "Then into the deceleration lane.", "Y luego al carril de deceleración.")

# ---------------------------------------------------------------- reversible, additional, contraflow, counting
Q("fl1", "flow", "A reversible lane is marked by…", "Un carril reversible está delimitado por…",
  [("double broken lines on both sides", "marcas dobles discontinuas a ambos lados"), ("a single continuous line", "una línea continua sencilla"), ("yellow zigzag lines", "líneas amarillas en zigzag")],
  "Its direction is set by lane-control signals.", "Su sentido se regula con semáforos de carril.")
Q("fl2", "flow", "In a reversible lane, which lights must you use?", "En un carril reversible, ¿qué alumbrado debes llevar?",
  [("Dipped headlights, day and night", "Luz de cruce, de día y de noche"), ("Only at night", "Solo de noche"), ("Position lights", "Luces de posición")],
  "Motorcycles use dipped headlights by day anyway.", "Las motos ya llevan la luz de cruce de día.")
Q("fl3", "flow", "A contraflow lane opened to ease traffic flow may be used by…", "Un carril en sentido contrario al habitual habilitado por fluidez puede ser usado por…",
  [("only motorcycles and cars without a trailer", "solo motocicletas y turismos sin remolque"), ("every vehicle", "todos los vehículos"), ("only buses and taxis", "solo autobuses y taxis")],
  "If opened for roadworks, every vehicle allowed on the road.", "Si es por obras, todos los autorizados en la vía.")
Q("fl4", "flow", "Speed in a temporary additional lane (carril adicional circunstancial)…", "Velocidad en un carril adicional circunstancial…",
  [("maximum 80, minimum 60 km/h", "máxima 80, mínima 60 km/h"), ("maximum 70, minimum 50 km/h", "máxima 70, mínima 50 km/h"), ("maximum 100 km/h", "máxima 100 km/h")],
  "Or lower if signed.", "O inferiores si se señaliza.")
Q("fl5", "flow", "A temporary additional lane is created by using…", "Un carril adicional circunstancial se crea utilizando…",
  [("both hard shoulders", "ambos arcenes"), ("the central reservation", "la mediana"), ("a cycle lane", "un carril bici")],
  "Two lanes one way and one the other.", "Dos carriles en un sentido y uno en el otro.")
Q("fl6", "flow", "In a contraflow lane, may you move into the normal-direction lane to overtake?", "En un carril en sentido contrario al habitual, ¿puedes pasar al carril del sentido normal para adelantar?",
  [("No, never", "No, nunca"), ("Yes, if it is clear", "Sí, si está libre"), ("Yes, after signalling", "Sí, señalizándolo")],
  "Never move sideways across the cones.", "Nunca se desplaza lateralmente atravesando el balizamiento.")
Q("fl7", "flow", "A contraflow lane opened because of roadworks may be used by…", "Un carril en sentido contrario habilitado por obras puede ser usado por…",
  [("every vehicle allowed on that road, unless prohibited", "todos los vehículos autorizados en esa vía, salvo prohibición"), ("only motorcycles and cars", "solo motos y turismos"), ("only works vehicles", "solo vehículos de obras")],
  "Under the same conditions: dipped lights, 60–80 km/h.", "En las mismas condiciones: luz de cruce, 60–80 km/h.")
Q("fl8", "flow", "You ride in the only normal-direction lane next to a contraflow lane. You must…", "Circulas por el único carril del sentido normal contiguo a un carril en sentido contrario. Debes…",
  [("use dipped headlights and keep to 60–80 km/h", "llevar luz de cruce y circular entre 60 y 80 km/h"), ("keep to the road’s usual limits", "respetar los límites habituales de la vía"), ("ride on the hard shoulder", "circular por el arcén")],
  "With more than one lane in your direction, the road’s limits apply.", "Con más de un carril en tu sentido, rigen los límites de la vía.")
Q("fl9", "flow", "When counting lanes to apply the rules, bus lanes…", "Al contar los carriles para aplicar las normas, los carriles bus…",
  [("are not counted", "no se cuentan"), ("are counted", "se cuentan"), ("are counted only at night", "se cuentan solo de noche")],
  "Nor bicycle, acceleration or deceleration lanes.", "Tampoco los carriles bici, de aceleración o de deceleración.")
Q("fl10", "flow", "Your carriageway has two lanes plus a deceleration lane. For the lane rules, it has…", "Tu calzada tiene dos carriles más uno de deceleración. A efectos de las normas, tiene…",
  [("two lanes", "dos carriles"), ("three lanes", "tres carriles"), ("one lane", "un carril")],
  "Lanes for certain manoeuvres don’t count.", "Los carriles para ciertas maniobras no se cuentan.")
Q("fl11", "flow", "The direction of a reversible lane is controlled by…", "El sentido de un carril reversible se regula con…",
  [("lane-control signals or other means", "semáforos de carril u otros medios"), ("the time of day only", "solo la hora del día"), ("a yellow line", "una línea amarilla")],
  "Square signals over each lane.", "Semáforos cuadrados sobre cada carril.")

# ---------------------------------------------------------------- hard shoulder
Q("sh1", "shoulder", "After a minor breakdown on an autovía, your motorcycle can carry on. You should…", "Tras una avería leve en una autovía, tu moto puede continuar. Debes…",
  [("carry on at once, making sure it is safe", "continuar de inmediato, asegurándote de hacerlo con seguridad"), ("stop on the shoulder and wait for help", "parar en el arcén y esperar auxilio"), ("ride on the shoulder to the next town", "circular por el arcén hasta el próximo pueblo")],
  "Don’t stop if you don’t need to.", "No se detenga si no lo necesita.")
Q("sh2", "shoulder", "When may motorcycles use the right-hand hard shoulder in a jam?", "¿Cuándo pueden las motos usar el arcén derecho en un atasco?",
  [("On signed stretches, when traffic in the lanes is stopped by congestion", "En tramos señalizados, cuando la circulación de los carriles esté detenida por congestión"), ("In any jam on any road", "En cualquier atasco y en cualquier vía"), ("Never", "Nunca")],
  "In force since 1 October 2026.", "En vigor desde el 1 de octubre de 2026.")
Q("sh3", "shoulder", "On a signed stretch, riding on the hard shoulder in a jam, your maximum speed is…", "En un tramo señalizado, circulando por el arcén en un atasco, tu velocidad máxima es…",
  [("30 km/h", "30 km/h"), ("45 km/h", "45 km/h"), ("50 km/h", "50 km/h")],
  "In single file and with extreme care.", "En columna de a uno y extremando la precaución.")
Q("sh4", "shoulder", "Several motorcycles use the hard shoulder on a signed stretch in a jam. They ride…", "Varias motos usan el arcén en un tramo señalizado en un atasco. Circulan…",
  [("in single file", "en columna de a uno"), ("two abreast", "en paralelo de dos en dos"), ("however they like", "como quieran")],
  "Extreme care.", "Extremando la precaución.")
Q("sh5", "shoulder", "On that shoulder you come up behind a moped. You…", "En ese arcén alcanzas a un ciclomotor. Tú…",
  [("must not endanger it, leaving the shoulder if necessary", "no debes ponerlo en riesgo, abandonando el arcén si es preciso"), ("have priority: it must let you pass", "tienes preferencia: debe dejarte pasar"), ("may overtake it on the shoulder at 30 km/h", "puedes adelantarlo por el arcén a 30 km/h")],
  "Mopeds are obliged to use the shoulder; you are not.", "El ciclomotor está obligado a usar el arcén; tú no.")
Q("sh6", "shoulder", "On a signed stretch, traffic is moving slowly at 40 km/h. May you use the hard shoulder?", "En un tramo señalizado, el tráfico avanza despacio a 40 km/h. ¿Puedes usar el arcén?",
  [("No: traffic must be stopped", "No: el tráfico debe estar detenido"), ("Yes, at up to 30 km/h", "Sí, a 30 km/h como máximo"), ("Yes, if you stay below 40 km/h", "Sí, si vas a menos de 40 km/h")],
  "Only when the lanes are stopped by congestion.", "Solo cuando los carriles estén detenidos por congestión.")
Q("sh7", "shoulder", "Your motorcycle breaks down and needs help. You should…", "Tu moto se avería y necesita auxilio. Debes…",
  [("leave the lanes and head for the first exit along the right shoulder", "abandonar los carriles y dirigirte a la primera salida por el arcén derecho"), ("stop in your lane with the hazard lights on", "detenerte en tu carril con la señal de emergencia"), ("use the left-hand shoulder", "usar el arcén izquierdo")],
  "If you can’t, stop on the right shoulder or where you obstruct least.", "Si no es posible, detenerse en el arcén derecho o donde menos estorbe.")
Q("sh8", "shoulder", "Two mopeds on the hard shoulder may ride side by side?", "Dos ciclomotores por el arcén, ¿pueden circular en paralelo?",
  [("No", "No"), ("Yes, always", "Sí, siempre"), ("Yes, in single file", "Sí, en columna de a uno")],
  "Only bicycles may ride two abreast.", "Solo las bicicletas pueden ir en columna de a dos.")
Q("sh9", "shoulder", "A moped on the shoulder may not overtake another if they stay side by side for more than…", "Un ciclomotor en el arcén no puede adelantar a otro si la marcha en paralelo supera…",
  [("15 seconds or 200 metres", "15 segundos o 200 metros"), ("30 seconds or 500 metres", "30 segundos o 500 metros"), ("10 seconds or 100 metres", "10 segundos o 100 metros")],
  "Bicycles are exempt.", "Las bicicletas están exentas.")
Q("sh10", "shoulder", "In a stopped jam with no signed stretch, may you ride between the two stopped lanes?", "En un atasco detenido sin tramo señalizado, ¿puedes circular entre los dos carriles parados?",
  [("No: weaving between vehicles is prohibited", "No: zigzaguear entre los vehículos está prohibido"), ("Yes, at up to 30 km/h", "Sí, a 30 km/h como máximo"), ("Yes, if you are on a motorcycle", "Sí, si vas en moto")],
  "The new rule only opens the signed right-hand shoulder.", "La nueva norma solo habilita el arcén derecho señalizado.")

# ---------------------------------------------------------------- safety distance
Q("di1", "dist", "Behind another vehicle, the gap you leave must let you…", "Detrás de otro vehículo, la separación que dejas debe permitirte…",
  [("stop without hitting it if it brakes hard", "detenerte sin chocar si frena bruscamente"), ("read its number plate", "leer su matrícula"), ("overtake it at any moment", "adelantarlo en cualquier momento")],
  "Taking speed, grip and braking into account.", "Teniendo en cuenta la velocidad, la adherencia y el frenado.")
Q("di2", "dist", "If you are not signalling that you will overtake, the gap must also…", "Si no señalizas que vas a adelantar, la separación debe además…",
  [("let the vehicle behind overtake you safely", "permitir que el que te sigue te adelante con seguridad"), ("be at least 100 metres", "ser de al menos 100 metros"), ("be nothing more", "nada más")],
  "So that others can slot in.", "Para que otros puedan meterse.")
Q("di3", "dist", "In a tunnel, when you are not going to overtake, keep at least…", "En un túnel, si no vas a adelantar, mantén al menos…",
  [("100 metres or 4 seconds", "100 metros o 4 segundos"), ("50 metres or 2 seconds", "50 metros o 2 segundos"), ("150 metres", "150 metros")],
  "At all times, also in underpasses.", "En todo momento, también en pasos inferiores.")
Q("di4", "dist", "The fixed 50 m gap out of town is required of…", "La separación fija de 50 m fuera de poblado se exige a…",
  [("vehicles over 3,500 kg or longer than 10 m", "vehículos de más de 3.500 kg o de más de 10 m"), ("motorcycles", "motocicletas"), ("all vehicles at night", "todos los vehículos de noche")],
  "Not to motorcycles.", "No a las motos.")
Q("di5", "dist", "In town, the gap to the vehicle in front must be…", "En poblado, la separación con el vehículo de delante debe ser…",
  [("enough to avoid a collision", "la suficiente para evitar una colisión"), ("at least 50 metres", "de al menos 50 metros"), ("at least 100 metres", "de al menos 100 metros")],
  "No room for overtakers is needed in town.", "En poblado no hace falta dejar hueco para que te adelanten.")
Q("di6", "dist", "You intend to overtake the vehicle in front. While you wait, the gap must…", "Vas a adelantar al vehículo de delante. Mientras esperas, la separación debe…",
  [("still let you stop without hitting it", "seguir permitiéndote detenerte sin chocar"), ("be as short as possible", "ser lo más corta posible"), ("be at least 50 metres", "ser de al menos 50 metros")],
  "Even if you mean to overtake.", "Aunque tengas intención de adelantar.")
Q("di7", "dist", "The safety distance depends above all on…", "La distancia de seguridad depende sobre todo de…",
  [("speed, grip and braking", "la velocidad, la adherencia y el frenado"), ("only the type of vehicle", "solo el tipo de vehículo"), ("only the time of day", "solo la hora del día")],
  "Wet roads need a longer gap.", "Con el firme mojado hace falta más separación.")
