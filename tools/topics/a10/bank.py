# -*- coding: utf-8 -*-
"""Question bank for the interactive Category A1/A2, Topic 10 page (accidents and their factors). In every question
the FIRST option is the correct one (the page shuffles options when it shows them). Ids must be unique and must not
start with "ai"."""

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
    "impact": dict(sec=1, en="Social impact", es="Impacto social",
        recap=[("Road accidents: a serious public-health problem; speed is the leading cause.", "Accidentes de tráfico: problema grave de salud pública; la velocidad es la causa principal."),
               ("More accidents in towns, more deaths on interurban roads.", "Más accidentes en vías urbanas, más muertos en carretera."),
               ("Motorways and autovías are the safest roads.", "Autopistas y autovías son las vías más seguras."),
               ("Riskiest times: evening return from work; weekends and holidays in the early hours.", "Momentos de más riesgo: salida del trabajo por la tarde; fines de semana y festivos de madrugada.")],
        trap=("Thinking most deaths happen in towns because there are more accidents there.", "Pensar que hay más muertos en ciudad porque hay más accidentes.")),
    "human": dict(sec=2, en="The human factor", es="Factor humano",
        recap=[("The human factor causes 70–90 % of accidents.", "El factor humano causa el 70–90 % de los accidentes."),
               ("Motorcycle accidents are easily fatal; not wearing the helmet is a main reason.", "Los accidentes de moto son fácilmente letales; no usar el casco es un motivo principal."),
               ("Ability depends on training and experience.", "La capacidad depende de la formación y la experiencia."),
               ("No weaving between vehicles or sudden manoeuvres without warning.", "Prohibido zigzaguear entre vehículos y las maniobras súbitas sin aviso.")],
        trap=("Thinking the vehicle causes most accidents.", "Pensar que el vehículo causa la mayoría de los accidentes.")),
    "falls": dict(sec=2, en="Falls and guardrails", es="Caídas y guardarraíles",
        recap=[("After any accident, check handlebar, wheels, lights, fluids and oil on brakes or tyres.", "Tras cualquier accidente, revisar manillar, ruedas, luces, niveles y aceite en frenos o neumáticos."),
               ("Let go of the controls so the bike does not drag you.", "Soltar los mandos para no ser arrastrado por la moto."),
               ("Slide, don’t roll; don’t get up until you stop.", "Deslizarse, no rodar; no levantarse hasta detenerse."),
               ("“H” posts cut; “C” posts and lower rails protect.", "Los postes en «H» cortan; los de «C» y las bandas inferiores protegen.")],
        trap=("Trying to stand up while still sliding.", "Intentar levantarse mientras aún se desliza.")),
    "speed": dict(sec=2, en="Speed and stopping distance", es="Velocidad y distancia de detención",
        recap=[("More speed: less time to see and analyse, worse reactions, worse injuries.", "Más velocidad: menos capacidad de ver y analizar, peores reacciones, lesiones más graves."),
               ("Reaction time about 0.75 s; longer with age, fatigue, alcohol, drugs, medicines, heat.", "Tiempo de reacción unos 0,75 s; mayor con edad, fatiga, alcohol, drogas, medicamentos, calor."),
               ("Stopping distance = reaction distance + braking distance.", "Distancia de detención = distancia de reacción + distancia de frenado."),
               ("Braking distance: rain ×2, snow or ice ×10; longer with a passenger.", "Distancia de frenado: lluvia ×2, nieve o hielo ×10; mayor con pasajero.")],
        trap=("Thinking the reaction distance depends on the brakes.", "Pensar que la distancia de reacción depende de los frenos.")),
    "fatigue": dict(sec=2, en="Fatigue, sleep and distractions", es="Fatiga, sueño y distracciones",
        recap=[("Main cause of fatigue: riding long periods without proper breaks.", "Principal causa de fatiga: conducir largos periodos sin descansar bien."),
               ("Fatigue: stiffness, imprecise movements, irritability, slower reactions.", "Fatiga: agarrotamiento, imprecisión, irritabilidad, más tiempo de reacción."),
               ("Sleep: microsleeps, distractions, worse decisions; rest every 2 h or 200 km for 20–30 min.", "Sueño: microsueños, distracciones, peores decisiones; descansar cada 2 h o 200 km, 20–30 min."),
               ("Distractions: stress, anxiety, medicines, sat-nav, phone even hands-free.", "Distracciones: estrés, ansiedad, fármacos, GPS, móvil incluso con manos libres.")],
        trap=("Thinking coffee is a substitute for a rest.", "Pensar que el café sustituye al descanso.")),
    "alcohol": dict(sec=2, en="Alcohol and drugs", es="Alcohol y drogas",
        recap=[("Depressant with an initial euphoric phase; false sense of safety, tunnel vision.", "Depresor con una fase euforizante inicial; falsa seguridad, visión túnel."),
               ("Limits: 0.25 mg/l air (0.5 g/l blood); first 2 years and professionals 0.15 (0.3); under 18: 0.", "Tasas: 0,25 mg/l aire (0,5 g/l sangre); 2 primeros años y profesionales 0,15 (0,3); menores: 0."),
               ("Peak 30–90 minutes after drinking; nothing fools the breathalyser.", "Pico entre 30 y 90 minutos; nada engaña al etilómetro."),
               ("Drugs forbidden, except prescribed medicines that don’t affect riding.", "Drogas prohibidas, salvo medicamentos con receta que no afecten a la conducción.")],
        trap=("Thinking a 17-year-old A1 rider may reach 0.15 mg/l.", "Pensar que un motorista de 17 años con el A1 puede llegar a 0,15 mg/l.")),
    "law": dict(sec=2, en="Tests and immobilisation", es="Pruebas e inmovilización",
        recap=[("Any driver can be tested, including at a preventive check.", "Cualquier conductor puede ser sometido a las pruebas, también en un control preventivo."),
               ("Alcohol: breathalyser; drugs: saliva test and lab analysis.", "Alcohol: etilómetro; drogas: prueba salival y análisis."),
               ("Second test at least 10 minutes later; contrast analysis paid in advance, refunded if negative.", "Segunda prueba al menos 10 minutos después; contraste pagado antes y devuelto si es negativo."),
               ("Positive or refusal: vehicle immobilised, unless another licensed person can ride it.", "Positivo o negativa: inmovilización, salvo que pueda conducir otra persona habilitada.")],
        trap=("Thinking the contrast blood test is always free.", "Pensar que el análisis de sangre de contraste es siempre gratuito.")),
    "tyres": dict(sec=3, en="Tyres", es="Neumáticos",
        recap=[("The only contact with the ground; the tread gives grip and clears water.", "El único contacto con el suelo; la banda de rodamiento da agarre y evacua agua."),
               ("Pressure as the manufacturer says, checked cold; don’t let air out when hot.", "Presión del fabricante, comprobada en frío; no quitar aire en caliente."),
               ("Same sizes as the manufacturer’s; fit in the direction of the arrow.", "Mismas medidas que el fabricante; montar en el sentido de la flecha."),
               ("No cuts or deformations; worn tyres lose grip.", "Sin cortes ni deformaciones; los gastados pierden adherencia.")],
        trap=("Letting air out of a hot tyre to reach the cold pressure.", "Quitar aire a un neumático caliente para dejar la presión en frío.")),
    "brakes": dict(sec=3, en="Brakes and electronic aids", es="Frenos y ayudas electrónicas",
        recap=[("Two braking devices: one on the rear wheel, one on the front; none needed on the sidecar wheel.", "Dos dispositivos: uno en la rueda trasera y otro en la delantera; no en la del sidecar."),
               ("Front disc: fewer metres, less locking, better cooling (less fading).", "Disco delantero: menos metros, menos bloqueo, mejor refrigeración (menos fading)."),
               ("ABS stops the wheels locking under hard braking.", "El ABS evita el bloqueo de las ruedas en una frenada brusca."),
               ("Traction control can be switched off; anti-wheelie stops the front lifting.", "El control de tracción se puede desconectar; el anti-wheelie evita levantar la delantera.")],
        trap=("Thinking ABS shortens the braking distance in every case.", "Pensar que el ABS acorta siempre la distancia de frenado.")),
    "helmet": dict(sec=3, en="Helmet", es="El casco",
        recap=[("Not wearing it: main cause of death in motorcycle and moped accidents.", "No usarlo: principal causa de mortalidad en accidentes de moto y ciclomotor."),
               ("Compulsory for rider and passenger, approved UNECE R22, fastened.", "Obligatorio para conductor y pasajero, homologado UNECE R22, abrochado."),
               ("Full-face recommended; modular only with the chin bar closed; jet leaves the chin bare.", "Integral recomendable; modular solo con la mentonera cerrada; el jet deja la barbilla al aire."),
               ("Replace after an accident or a hard knock.", "Sustituir tras un accidente o un golpe fuerte.")],
        trap=("Keeping a helmet that fell hard because it looks fine.", "Seguir usando un casco que recibió un golpe fuerte porque parece intacto.")),
    "gear": dict(sec=3, en="Rider’s gear", es="Equipamiento motorista",
        recap=[("Abrasion-resistant suit with protectors, bright colours.", "Traje resistente a la abrasión con protecciones, colores llamativos."),
               ("Gloves compulsory on interurban roads; closed shoes on every road.", "Guantes obligatorios en vías interurbanas; calzado cerrado en todas."),
               ("Vest: carried on the motorcycle, worn when you get off on an interurban road.", "Chaleco: lo lleva la moto, se usa al bajarse en una interurbana."),
               ("Professional riders wear the vest on every road.", "Los profesionales llevan el chaleco en todas las vías.")],
        trap=("Thinking gloves are compulsory in town too.", "Pensar que los guantes son obligatorios también en ciudad.")),
    "weather": dict(sec=4, en="Road and weather", es="Vía y climatología",
        recap=[("Low grip: slow down before, cross upright.", "Baja adherencia: reducir antes y pasar enderezado."),
               ("Rain: first drops worst; brake early, less front pressure; avoid markings and puddles.", "Lluvia: primeras gotas lo peor; frenar antes, menos presión delante; evitar marcas y charcos."),
               ("Snow on motorways: no overtaking, right-hand lane; ice ×10, don’t ride.", "Nieve en autopista: no adelantar, carril derecho; hielo ×10, no circular."),
               ("Fog: no main beam, fog light if fitted; wind: firm grip, screen effect; sun: no dark visor at night.", "Niebla: sin largas, antiniebla si la hay; viento: manillar firme, efecto pantalla; sol: nada de visera oscura de noche.")],
        trap=("Using main beam in fog or heavy rain to see further.", "Usar las largas con niebla o lluvia intensa para ver más.")),
}

# ---------------------------------------------------------------- 1 social impact
Q("im1", "impact", "According to your course, what is the leading cause of road accidents in Spain?", "Según tu curso, ¿cuál es la causa principal de los accidentes en España?",
  [("Excessive speed", "El exceso de velocidad"), ("Bad weather", "La mala climatología"), ("Mechanical failure", "Los fallos mecánicos")],
  "Road accidents are a priority public-health problem, and excessive speed is the main cause.", "Los accidentes son un problema prioritario de salud pública, y el exceso de velocidad es la causa principal.")
Q("im2", "impact", "Where are there more accidents with victims, and where more deaths?", "¿Dónde hay más accidentes con víctimas y dónde más víctimas mortales?",
  [("More accidents in towns; more deaths on interurban roads", "Más accidentes en vías urbanas; más muertos en carretera"), ("More of both in towns", "Más de las dos cosas en ciudad"), ("More accidents on interurban roads; more deaths in towns", "Más accidentes en carretera; más muertos en ciudad")],
  "Out of town speeds are higher, so accidents there are more often fatal.", "En carretera se circula más deprisa, así que los accidentes son más a menudo mortales.")
Q("im3", "impact", "Which roads are considered the safest?", "¿Qué vías se consideran más seguras?",
  [("Autopistas and autovías", "Autopistas y autovías"), ("Conventional roads", "Carreteras convencionales"), ("Urban streets", "Calles urbanas")],
  "Separate directions, no intersections and a gentler layout.", "Sentidos separados, sin intersecciones y trazado menos sinuoso.")
Q("im4", "impact", "When is the risk of an accident highest on a working day?", "¿Cuándo es mayor el riesgo de accidente en un día laborable?",
  [("Going to and from work, above all the evening return", "Al ir y volver del trabajo, sobre todo al salir por la tarde"), ("Mid-morning", "A media mañana"), ("At lunchtime", "A mediodía")],
  "Commuting hours are the most dangerous, especially at the end of the working day.", "Las horas de entrada y salida del trabajo son las más peligrosas, sobre todo al terminar la jornada.")
Q("im5", "impact", "And during holidays and weekends?", "¿Y durante las vacaciones y los fines de semana?",
  [("Above all in the early hours", "Sobre todo de madrugada"), ("Above all at midday", "Sobre todo a mediodía"), ("The risk is the same all day", "El riesgo es igual todo el día")],
  "Holidays, bank holidays and weekends are risky, especially in the early hours.", "Vacaciones, festivos y fines de semana son peligrosos, especialmente de madrugada.")

# ---------------------------------------------------------------- 2 human factor
Q("hu1", "human", "What share of accidents is due to the human factor?", "¿Qué parte de los accidentes se debe al factor humano?",
  [("70–90 %", "Entre el 70 y el 90 %"), ("About 30 %", "Alrededor del 30 %"), ("Less than 10 %", "Menos del 10 %")],
  "The human factor is the main cause: most accidents come from the rider’s unsuitable behaviour.", "El factor humano es el principal responsable: la mayoría se deben a comportamientos inadecuados del conductor.")
Q("hu2", "human", "Why are motorcycle accidents so often fatal?", "¿Por qué los accidentes de moto son tan a menudo mortales?",
  [("The rider has no bodywork around them, and many don’t wear the helmet or don’t fasten it", "El motorista no tiene carrocería, y muchos no usan el casco o no lo abrochan"),
   ("Because motorcycles are faster than cars", "Porque las motos son más rápidas que los coches"), ("Because they happen at night", "Porque ocurren de noche")],
  "They often end in death or multiple injuries; not wearing the helmet, or wearing it unfastened, is a main reason.", "Suelen acabar en muerte o traumatismos múltiples; no usar el casco, o llevarlo sin abrochar, es uno de los principales motivos.")
Q("hu3", "human", "On what does a rider’s ability to adapt to traffic depend?", "¿De qué depende la capacidad del motorista para adaptarse a la circulación?",
  [("Training and experience", "De la formación y la experiencia"), ("Only the motorcycle’s power", "Solo de la potencia de la moto"), ("Only age", "Solo de la edad")],
  "The level of ability depends on training while learning and on experience.", "El nivel de capacidad depende de la formación en el aprendizaje y de la experiencia.")
Q("hu4", "human", "Is it allowed to weave between vehicles in slow traffic?", "¿Está permitido zigzaguear entre los vehículos en circulación lenta?",
  [("No: weaving and sudden manoeuvres without warning are forbidden", "No: zigzaguear y las maniobras súbitas sin aviso están prohibidos"), ("Yes, on a motorcycle", "Sí, en moto"), ("Yes, below 30 km/h", "Sí, por debajo de 30 km/h")],
  "Every sideways move must be checked and signalled in advance.", "Todo desplazamiento lateral debe comprobarse y señalizarse con antelación.")
Q("hu5", "human", "Which age group do motorcycle accidents hit hardest, according to your course?", "¿A qué grupo de edad afectan más los accidentes de moto, según tu curso?",
  [("Young people: they are a leading cause of death among them", "A los jóvenes: son una de sus principales causas de muerte"), ("People over 65", "A los mayores de 65"), ("Children under 12", "A los menores de 12")],
  "Your course links motorcycle accidents, many of them at weekends, with youth mortality.", "Tu curso relaciona los accidentes de moto, muchos de fin de semana, con la mortalidad juvenil.")

# ---------------------------------------------------------------- 2.1 falls
Q("fl1", "falls", "A fall cannot be avoided. What should you do first?", "La caída es inevitable. ¿Qué debes hacer primero?",
  [("Let go of the controls so the motorcycle does not drag you", "Soltar los mandos para que la moto no te arrastre"), ("Hold the handlebar tight", "Agarrar fuerte el manillar"), ("Brake hard with the front brake", "Frenar fuerte con el freno delantero")],
  "Letting go at once avoids being dragged along by the motorcycle.", "Soltar los mandos inmediatamente evita ser arrastrado por la moto.")
Q("fl2", "falls", "Once on the ground after a fall, how should you move?", "Una vez en el suelo tras una caída, ¿cómo debes moverte?",
  [("Stay calm and slide, without rolling, until you stop", "Mantener la calma y deslizarse, sin rodar, hasta detenerse"), ("Roll to stop sooner", "Rodar para detenerse antes"), ("Get up at once", "Levantarse enseguida")],
  "Slide, don’t roll, and don’t try to get up before your body has stopped.", "Deslizarse, no rodar, y no intentar levantarse antes de que el cuerpo se haya detenido.")
Q("fl3", "falls", "After a minor accident, what should you check before riding on?", "Tras un accidente leve, ¿qué debes comprobar antes de seguir?",
  [("Handlebar, wheels, lights, fluid levels, and that there is no oil on brakes or tyres", "Manillar, ruedas, luces, niveles y que no haya aceite en frenos ni neumáticos"), ("Only the paintwork", "Solo la pintura"), ("Nothing, if the motorcycle starts", "Nada, si la moto arranca")],
  "A careless check can lead to a later mechanical failure.", "Una comprobación incorrecta puede provocar después un fallo mecánico.")
Q("fl4", "falls", "Which guardrail posts are most dangerous for a fallen rider?", "¿Qué postes de guardarraíl son más peligrosos para un motorista caído?",
  [("Posts with a cutting “H” profile", "Los de perfil cortante en «H»"), ("Posts with a rounded “C” profile", "Los de perfil redondeado en «C»"), ("Posts covered by a lower rail", "Los tapados por una banda inferior")],
  "A cutting profile causes very serious injuries; a rounded one, or a motorcyclist protection rail, much less.", "Un perfil cortante causa lesiones muy graves; uno redondeado, o un sistema de protección para motoristas, mucho menos.")
Q("fl5", "falls", "What clothing is recommended to limit injuries in a fall?", "¿Qué ropa se recomienda para reducir las lesiones en una caída?",
  [("A full-face helmet and leather or special fabrics with protectors", "Casco integral y ropa de cuero o tejidos especiales con protectores"), ("Light cotton clothing so you can move", "Ropa ligera de algodón para moverse"), ("Any clothing, if you wear the helmet", "Cualquier ropa, si llevas casco")],
  "The helmet and suitable clothing make a great difference.", "El casco y la ropa adecuada son de gran importancia para reducir los daños.")

# ---------------------------------------------------------------- 2.2 speed
Q("sp1", "speed", "What happens to your ability to anticipate and react as speed rises?", "¿Qué ocurre con tu capacidad de anticipación y reacción al aumentar la velocidad?",
  [("It decreases, and injuries are more serious", "Disminuye, y las lesiones son más graves"), ("It improves, because you concentrate more", "Mejora, porque te concentras más"), ("It does not change", "No cambia")],
  "At higher speed you have less time to see and analyse what happens around you.", "A más velocidad hay menos capacidad para ver y analizar lo que ocurre alrededor.")
Q("sp2", "speed", "What is the usual reaction time of a rider in normal conditions?", "¿Cuál es el tiempo de reacción habitual de un conductor en condiciones normales?",
  [("About 0.75 seconds", "Unos 0,75 segundos"), ("About 2 seconds", "Unos 2 segundos"), ("About 0.1 seconds", "Unos 0,1 segundos")],
  "Normally between half a second and one second, typically 0.75 s.", "Normalmente entre medio y un segundo, habitualmente 0,75 s.")
Q("sp3", "speed", "What is the stopping distance (parada técnica)?", "¿Qué es la distancia de detención (parada técnica)?",
  [("The reaction distance plus the braking distance", "La distancia de reacción más la de frenado"), ("Only the braking distance", "Solo la distancia de frenado"), ("The distance to the vehicle in front", "La distancia al vehículo de delante")],
  "From seeing the obstacle until stopping: reaction plus braking.", "Desde que se ve el obstáculo hasta detenerse: reacción más frenado.")
Q("sp4", "speed", "How does rain change the braking distance?", "¿Cómo cambia la lluvia la distancia de frenado?",
  [("It can double it", "Puede duplicarla"), ("It multiplies it by ten", "La multiplica por diez"), ("It does not change it", "No la cambia")],
  "Rain ×2; snow or ice ×10.", "Lluvia ×2; nieve o hielo ×10.")
Q("sp5", "speed", "What does the reaction distance depend on?", "¿De qué depende la distancia de reacción?",
  [("The rider’s reaction time and the speed", "Del tiempo de reacción del conductor y de la velocidad"), ("The condition of the brakes", "Del estado de los frenos"), ("The type of tyres", "Del tipo de neumáticos")],
  "It is what you cover before braking: faster or slower to react, more metres.", "Es lo que se recorre antes de frenar: a más velocidad o más lentitud en reaccionar, más metros.")
Q("sp6", "speed", "You carry a passenger. What happens to your braking distance?", "Llevas un pasajero. ¿Qué pasa con tu distancia de frenado?",
  [("It gets longer", "Aumenta"), ("It gets shorter, because there is more grip", "Disminuye, porque hay más agarre"), ("It stays the same", "No cambia")],
  "The braking distance depends on the mass, the load and how it is placed.", "La distancia de frenado depende de la masa, la carga y su colocación.")
Q("sp7", "speed", "Which of these makes the reaction time longer?", "¿Cuál de estos factores aumenta el tiempo de reacción?",
  [("Fatigue, alcohol or some medicines", "La fatiga, el alcohol o algunos medicamentos"), ("New tyres", "Unos neumáticos nuevos"), ("A dry road", "Una calzada seca")],
  "Age, fatigue and sleepiness, alcohol, drugs, medicines, mood, illness, stress and heat lengthen it.", "La edad, la fatiga y la somnolencia, el alcohol, las drogas, los medicamentos, el estado de ánimo, las enfermedades, el estrés y el calor la alargan.")

# ---------------------------------------------------------------- 2.3–2.4 fatigue, sleep, distractions
Q("fa1", "fatigue", "What is the main cause of fatigue?", "¿Cuál es la principal causa de la fatiga?",
  [("Riding for long periods without proper breaks", "Conducir largos periodos sin descansar o descansando mal"), ("Riding in town", "Circular por ciudad"), ("Riding with a passenger", "Llevar pasajero")],
  "Long periods without stopping, or inadequate breaks, are the main cause.", "Los largos periodos sin parar, o los descansos inadecuados, son la principal causa.")
Q("fa2", "fatigue", "How often should you rest on a long trip?", "¿Cada cuánto debes descansar en un viaje largo?",
  [("At least every 2 hours or 200 km, for 20–30 minutes", "Como máximo cada 2 horas o 200 km, de 20 a 30 minutos"), ("Every 4 hours or 400 km, for 10 minutes", "Cada 4 horas o 400 km, 10 minutos"), ("Only when you feel tired", "Solo cuando notes cansancio")],
  "Stop every 2 hours or 200 km for 20–30 minutes, and sooner if tired or sleepy.", "Parar cada 2 horas o 200 km de 20 a 30 minutos, y antes si hay cansancio o sueño.")
Q("fa3", "fatigue", "Which is an effect of fatigue?", "¿Cuál es un efecto de la fatiga?",
  [("Slow, imprecise movements and a longer reaction time", "Movimientos lentos e imprecisos y más tiempo de reacción"), ("Sharper attention", "Más atención"), ("Shorter reaction time", "Menor tiempo de reacción")],
  "Muscle stiffness, imprecision, behaviour changes, less attention and slower reactions.", "Agarrotamiento, imprecisión, cambios de comportamiento, menos atención y reacciones más lentas.")
Q("fa4", "fatigue", "What is a microsleep?", "¿Qué es un microsueño?",
  [("A few seconds asleep without realising it", "Unos segundos dormido sin darse cuenta"), ("A short rest at a service area", "Un descanso corto en un área de servicio"), ("A mild headache", "Un dolor de cabeza leve")],
  "Microsleeps are short periods in which the rider falls slightly asleep without noticing.", "Son periodos de unos segundos en que el conductor queda ligeramente dormido sin darse cuenta.")
Q("fa5", "fatigue", "You feel sleepy on an interurban road. What is the right thing to do?", "Tienes sueño en una carretera. ¿Qué es lo correcto?",
  [("Stop somewhere suitable and sleep a little", "Parar en un lugar adecuado y dormir un poco"), ("Ride faster to arrive sooner", "Ir más deprisa para llegar antes"), ("Open the visor and carry on", "Abrir la visera y seguir")],
  "If you are tired or sleepy, stop to rest in a suitable place and sleep a little.", "Si estás cansado o tienes sueño, para a descansar en un lugar adecuado y duerme un poco.")
Q("fa6", "fatigue", "Which road conditions bring on fatigue sooner?", "¿Qué condiciones de la vía adelantan la aparición de la fatiga?",
  [("Heavy traffic, a poor surface, unfamiliar roads and bad weather", "Mucho tráfico, firme en mal estado, vías poco conocidas y mal tiempo"), ("A motorway with little traffic in good weather", "Una autovía con poco tráfico y buen tiempo"), ("A road you know well", "Una vía que conoces bien")],
  "They demand more concentration or make riding uncomfortable.", "Exigen más concentración o hacen la conducción más incómoda.")
Q("fa7", "fatigue", "Is talking on a hands-free phone a distraction?", "¿Hablar por el móvil con manos libres es una distracción?",
  [("Yes, even hands-free", "Sí, incluso con manos libres"), ("No, if your hands are on the handlebar", "No, si las manos están en el manillar"), ("Only in town", "Solo en ciudad")],
  "Your course lists the phone, even hands-free, and the sat-nav among the causes of distraction.", "Tu curso incluye el móvil, incluso con manos libres, y el GPS entre las causas de distracción.")
Q("fa8", "fatigue", "A rider with a chronic illness takes medicines. What should they avoid?", "Un conductor con una enfermedad crónica toma medicamentos. ¿Qué debe evitar?",
  [("Drinking alcohol while taking the medicines", "Tomar alcohol mientras toma los medicamentos"), ("Asking the doctor about riding", "Consultar al médico sobre la conducción"), ("Reading the leaflet", "Leer el prospecto")],
  "Know the illness and side effects, recognise a crisis, avoid triggers, no alcohol with medicines, ask the doctor.", "Conocer la enfermedad y los efectos secundarios, reconocer una crisis, evitar desencadenantes, no tomar alcohol con medicamentos, consultar al médico.")

# ---------------------------------------------------------------- 2.5 alcohol and drugs
Q("al1", "alcohol", "What kind of substance is alcohol?", "¿Qué tipo de sustancia es el alcohol?",
  [("A depressant of the central nervous system, with an initial euphoric phase", "Un depresor del sistema nervioso central, con una fase euforizante al principio"), ("A stimulant", "Un estimulante"), ("A harmless substance in small amounts", "Una sustancia inocua en pequeñas cantidades")],
  "It depresses the nervous system although at first it seems to excite.", "Deprime el sistema nervioso aunque al principio parezca excitar.")
Q("al2", "alcohol", "Which perception change can alcohol cause?", "¿Qué alteración de la percepción puede causar el alcohol?",
  [("Tunnel vision and misjudging distances", "Visión túnel y cálculo erróneo de las distancias"), ("Better night vision", "Mejor visión nocturna"), ("Less sensitivity to dazzle", "Menos sensibilidad al deslumbramiento")],
  "You perceive worse, misjudge distances, are more sensitive to dazzle and may suffer tunnel vision.", "Se percibe peor, se calculan mal las distancias, hay más sensibilidad al deslumbramiento y puede aparecer la visión túnel.")
Q("al3", "alcohol", "Your A2 licence is one year old. What is your alcohol limit in exhaled air?", "Tu permiso A2 tiene un año. ¿Cuál es tu tasa máxima de alcohol en aire espirado?",
  [("0.15 mg/l", "0,15 mg/l"), ("0.25 mg/l", "0,25 mg/l"), ("0.30 mg/l", "0,30 mg/l")],
  "During the first two years of the licence the limit is 0.15 mg/l in air (0.3 g/l in blood).", "Durante los dos primeros años del permiso la tasa es de 0,15 mg/l en aire (0,3 g/l en sangre).")
Q("al4", "alcohol", "And after more than two years with the licence?", "¿Y con más de dos años de permiso?",
  [("0.25 mg/l in air, 0.5 g/l in blood", "0,25 mg/l en aire, 0,5 g/l en sangre"), ("0.5 mg/l in air, 0.25 g/l in blood", "0,5 mg/l en aire, 0,25 g/l en sangre"), ("0.15 mg/l in air, 0.3 g/l in blood", "0,15 mg/l en aire, 0,3 g/l en sangre")],
  "The general limit: 0.25 mg/l in exhaled air or 0.5 g/l in blood.", "La tasa general: 0,25 mg/l en aire espirado o 0,5 g/l en sangre.")
Q("al5", "alcohol", "You are 17 and ride an A1 motorcycle. What is your alcohol limit?", "Tienes 17 años y conduces una moto del A1. ¿Cuál es tu tasa máxima de alcohol?",
  [("0.0: none at all", "0,0: nada de alcohol"), ("0.15 mg/l, as a new rider", "0,15 mg/l, como novel"), ("0.25 mg/l", "0,25 mg/l")],
  "The Traffic Law sets 0 for any driver under 18, below the new-licence limit.", "La Ley de Tráfico fija 0 para cualquier conductor menor de edad, por debajo de la tasa de los noveles.")
Q("al6", "alcohol", "How long after drinking is the blood alcohol level at its highest?", "¿Cuánto tiempo después de beber se alcanza la tasa máxima de alcohol?",
  [("30 to 90 minutes", "Entre 30 y 90 minutos"), ("5 minutes", "5 minutos"), ("6 hours", "6 horas")],
  "It peaks 30–90 minutes after drinking and then falls very slowly over several hours.", "Alcanza el pico entre 30 y 90 minutos y después baja muy lentamente durante varias horas.")
Q("al7", "alcohol", "Can coffee, chewing gum or drinking lots of water lower the breathalyser result?", "¿El café, los chicles o beber mucha agua pueden bajar el resultado del etilómetro?",
  [("No: there are no tricks", "No: no hay trucos"), ("Yes, coffee", "Sí, el café"), ("Yes, water", "Sí, el agua")],
  "Exercise, gum, sweets, coffee, oil, smoking, sprays, a nap or water — none of them works.", "Ejercicio, chicles, caramelos, café, aceite, fumar, sprays, dormir un poco o agua: nada funciona.")
Q("al8", "alcohol", "What is the only truly safe blood alcohol level for riding?", "¿Cuál es la única tasa de alcohol realmente segura para conducir?",
  [("0.0 g/l", "0,0 g/l"), ("Anything below the legal limit", "Cualquiera por debajo de la permitida"), ("0.2 g/l", "0,2 g/l")],
  "Even below the limit, alcohol can cause an accident.", "Aun por debajo de la tasa máxima, el alcohol puede causar un accidente.")
Q("al9", "alcohol", "May you ride after taking a medicine prescribed by your doctor that contains a drug?", "¿Puedes conducir tras tomar un medicamento recetado por tu médico que contiene una droga?",
  [("Yes, if it is for treatment on prescription and does not affect your riding", "Sí, si es con prescripción y finalidad terapéutica y no afecta a la conducción"), ("Never", "Nunca"), ("Yes, always", "Sí, siempre")],
  "Prescribed substances used for treatment are excluded, provided they don’t affect driving.", "Quedan excluidas las sustancias usadas bajo prescripción médica y con finalidad terapéutica, siempre que no afecten a la conducción.")

# ---------------------------------------------------------------- 2.6 the law
Q("lw1", "law", "Can you be breath-tested at a preventive check without having committed any offence?", "¿Pueden someterte a la prueba de alcohol en un control preventivo sin haber cometido ninguna infracción?",
  [("Yes", "Sí"), ("No: only after an accident", "No: solo tras un accidente"), ("Only if you show symptoms", "Solo si presentas síntomas")],
  "Any driver can be tested when simply required at a preventive check.", "Cualquier conductor puede ser sometido a la prueba si es requerido en un control preventivo.")
Q("lw2", "law", "Your first breath test is positive. How long must pass before the second?", "Tu primera prueba de alcohol da positivo. ¿Cuánto tiempo debe pasar hasta la segunda?",
  [("At least 10 minutes", "Al menos 10 minutos"), ("At least 30 minutes", "Al menos 30 minutos"), ("No time: it is immediate", "Ninguno: es inmediata")],
  "You, your companions or witnesses may check that at least 10 minutes pass between the tests.", "El examinado, sus acompañantes o testigos pueden controlar que pasen al menos 10 minutos.")
Q("lw3", "law", "How is the presence of drugs tested at the roadside?", "¿Cómo se comprueba la presencia de drogas en un control?",
  [("With a saliva test and later analysis", "Con una prueba salival y su posterior análisis"), ("With a breathalyser", "Con un etilómetro"), ("With a blood test on the spot", "Con un análisis de sangre en el acto")],
  "Alcohol: exhaled air. Drugs: an approved saliva device and a later lab analysis.", "Alcohol: aire espirado. Drogas: un dispositivo salival autorizado y posterior análisis.")
Q("lw4", "law", "You ask for a blood test to contrast the result. Who pays for it?", "Pides un análisis de sangre para contrastar el resultado. ¿Quién lo paga?",
  [("You pay in advance; it is refunded if the result is negative", "Lo pagas tú por adelantado; se devuelve si el resultado es negativo"), ("Always the administration", "Siempre la Administración"), ("Always you, whatever the result", "Siempre tú, sea cual sea el resultado")],
  "It is charged to you if positive and refunded if negative.", "Corre a tu cargo si es positivo y se te devuelve si es negativo.")
Q("lw5", "law", "Your alcohol test is positive and nobody with you can ride the motorcycle. What happens to it?", "Tu prueba da positivo y nadie de los que te acompañan puede conducir la moto. ¿Qué pasa con ella?",
  [("It is immobilised, and you pay the costs", "Se inmoviliza, y los gastos corren de tu cuenta"), ("You may push it home", "Puedes empujarla hasta casa"), ("You may ride it slowly", "Puedes conducirla despacio")],
  "Positive result or refusal: immobilisation, unless another properly licensed person can ride it.", "Resultado positivo o negativa: inmovilización, salvo que pueda conducirla otra persona habilitada.")
Q("lw6", "law", "What does it cost to ride with 0.40 mg/l of alcohol in exhaled air, licence held for five years?", "¿Qué supone circular con 0,40 mg/l en aire espirado, con un permiso de cinco años?",
  [("500 € and 4 points", "500 € y 4 puntos"), ("1,000 € and 6 points", "1.000 € y 6 puntos"), ("A warning", "Un aviso")],
  "Over the limit but not over twice it (0.25–0.50 mg/l): 500 € and 4 points.", "Por encima de la tasa sin superar el doble (0,25–0,50 mg/l): 500 € y 4 puntos.")
Q("lw7", "law", "From what alcohol level in exhaled air does riding become a crime?", "¿A partir de qué tasa de alcohol en aire espirado conducir es delito?",
  [("Over 0.60 mg/l", "Más de 0,60 mg/l"), ("Over 0.25 mg/l", "Más de 0,25 mg/l"), ("Over 0.50 mg/l", "Más de 0,50 mg/l")],
  "Over 0.60 mg/l in air (1.2 g/l in blood) is a crime, as is refusing the tests.", "Más de 0,60 mg/l en aire (1,2 g/l en sangre) es delito, igual que negarse a las pruebas.")

# ---------------------------------------------------------------- 3.1 tyres
Q("ty1", "tyres", "When should you check the tyre pressure?", "¿Cuándo debes comprobar la presión de los neumáticos?",
  [("Regularly, with the tyres cold", "Periódicamente, con los neumáticos fríos"), ("Only at the ITV", "Solo en la ITV"), ("Right after a long ride", "Justo después de un viaje largo")],
  "Check it cold with a gauge in good condition, at the pressure the manufacturer gives.", "Se comprueba en frío con un manómetro en buen estado, a la presión del fabricante.")
Q("ty2", "tyres", "You check the pressure after riding and it is above the cold figure. What do you do?", "Compruebas la presión tras circular y está por encima de la de frío. ¿Qué haces?",
  [("Leave it: the rise is normal and the manufacturer counts on it", "Dejarla: el aumento es normal y el fabricante lo prevé"), ("Let air out to the cold figure", "Quitar aire hasta la presión de frío"), ("Add more air", "Añadir más aire")],
  "If you check hot tyres, don’t remove the increase.", "Si los compruebas calientes, no debes quitar el aumento producido.")
Q("ty3", "tyres", "Which part of the tyre gives grip and clears the water?", "¿Qué parte del neumático da el agarre y evacua el agua?",
  [("The tread", "La banda de rodamiento"), ("The sidewall", "El flanco"), ("The valve", "La válvula")],
  "The tread has channels and grooves for grip and to clear water.", "La banda de rodamiento tiene canales y ranuras para el agarre y para evacuar el agua.")
Q("ty4", "tyres", "How must a new tyre be fitted?", "¿Cómo debe montarse un neumático nuevo?",
  [("In the direction of rotation shown by the arrow on the sidewall", "En el sentido de giro que marca la flecha del flanco"), ("Either way round", "En cualquier sentido"), ("Opposite to the arrow on the front wheel", "Al contrario que la flecha en la rueda delantera")],
  "Fit it in the right direction of rotation, and in the manufacturer’s sizes.", "Hay que montarlo en el sentido de giro correcto y con las medidas del fabricante.")
Q("ty5", "tyres", "A tyre has a cut on its sidewall. What can happen?", "Un neumático tiene un corte en el flanco. ¿Qué puede ocurrir?",
  [("Dangerous steering movements, especially at speed", "Movimientos peligrosos en la dirección, sobre todo a alta velocidad"), ("Nothing, if the pressure is right", "Nada, si la presión es correcta"), ("Only more noise", "Solo más ruido")],
  "A tyre must have no cuts or deformations.", "El neumático no debe presentar cortes ni deformaciones.")

# ---------------------------------------------------------------- 3.2–3.3 brakes and aids
Q("br1", "brakes", "How many braking devices must a motorcycle have?", "¿Cuántos dispositivos de frenado debe tener una motocicleta?",
  [("Two: one acting at least on the rear wheel and the other on the front", "Dos: uno que actúe al menos sobre la rueda trasera y otro sobre la delantera"), ("One, on the rear wheel", "Uno, en la rueda trasera"), ("Three, if it has a sidecar", "Tres, si lleva sidecar")],
  "With a sidecar, its wheel need not be braked.", "Con sidecar, no se exige frenar la rueda de este.")
Q("br2", "brakes", "Why is a disc usually used on the front wheel?", "¿Por qué se suele usar freno de disco en la rueda delantera?",
  [("It stops in fewer metres, locks less and cools better", "Frena en menos metros, se bloquea menos y se refrigera mejor"), ("It is cheaper", "Es más barato"), ("It never wears", "No se desgasta nunca")],
  "Better cooling also delays fading.", "Al refrigerarse mejor, también retrasa el fading.")
Q("br3", "brakes", "What is fading?", "¿Qué es el fading?",
  [("Loss of braking power because the brakes overheat", "La pérdida de eficacia del freno por calentamiento excesivo"), ("A worn tyre", "Un neumático desgastado"), ("A locked wheel", "Una rueda bloqueada")],
  "Disc brakes cool better and delay it.", "Los frenos de disco se refrigeran mejor y lo retrasan.")
Q("br4", "brakes", "What does ABS do?", "¿Qué hace el ABS?",
  [("Prevents the wheels locking under hard braking, so you keep control", "Evita el bloqueo de las ruedas en una frenada brusca y permite controlar la trayectoria"), ("Accelerates when the rear wheel slips", "Acelera cuando la rueda trasera patina"), ("Brakes automatically before an obstacle", "Frena solo ante un obstáculo")],
  "It adjusts the braking force to the available grip.", "Regula la potencia de frenado según la adherencia.")
Q("br5", "brakes", "Your motorcycle has spent several days outside in damp weather. What should you check?", "Tu moto ha pasado varios días a la intemperie con humedad. ¿Qué debes revisar?",
  [("The brakes: pads or shoes and discs or drums", "Los frenos: pastillas o zapatas y discos o tambores"), ("Only the tyre pressure", "Solo la presión de los neumáticos"), ("Nothing: damp does not affect it", "Nada: la humedad no le afecta")],
  "Check the fixed and moving parts of the brakes and that they work properly.", "Hay que comprobar los elementos fijos y móviles de los frenos y su funcionamiento.")
Q("br6", "brakes", "Which system lets you change gear without the clutch lever?", "¿Qué sistema permite cambiar de marcha sin usar la maneta de embrague?",
  [("The quickshifter", "El quickshifter"), ("The hill holder", "El hill holder"), ("The IMU", "La IMU")],
  "It cuts the power for an instant so the gears engage smoothly.", "Corta un instante la potencia para que las marchas engranen con suavidad.")
Q("br7", "brakes", "What does the anti-wheelie system do?", "¿Qué hace el sistema anti-wheelie?",
  [("Stops the front wheel lifting under hard acceleration", "Evita que la rueda delantera se levante al acelerar fuerte"), ("Stops the rear wheel locking", "Evita que la rueda trasera se bloquee"), ("Keeps the distance to the vehicle ahead", "Mantiene la distancia con el vehículo de delante")],
  "It reduces engine power or brakes gently to keep the front wheel down.", "Reduce la potencia o frena suavemente para mantener la rueda delantera en el suelo.")
Q("br8", "brakes", "What does the emergency brake signal do?", "¿Qué hace la señal de frenada de emergencia?",
  [("Makes the indicators flash under hard braking, to warn whoever is behind", "Hace parpadear los intermitentes en una frenada enérgica para avisar al de detrás"), ("Sounds the horn", "Hace sonar el claxon"), ("Brakes both wheels", "Frena las dos ruedas")],
  "It warns the vehicle behind so it can stop in time.", "Avisa al vehículo de detrás para que pueda detenerse a tiempo.")
Q("br9", "brakes", "Which of these aids can the rider switch off?", "¿Cuál de estas ayudas puede desconectar el conductor?",
  [("Traction control", "El control de tracción"), ("The brakes", "Los frenos"), ("The suspension", "La suspensión")],
  "Traction control doses the power to the grip and can be disconnected.", "El control de tracción dosifica la potencia según la adherencia y se puede desconectar.")
Q("br10", "brakes", "What does the suspension do?", "¿Qué hace la suspensión?",
  [("Keeps the wheels on the ground for grip and control, and absorbs bumps", "Mantiene las ruedas apoyadas para conservar la adherencia y el control, y absorbe las irregularidades"), ("Points the front wheel", "Orienta la rueda delantera"), ("Stops the wheels locking", "Evita el bloqueo de las ruedas")],
  "It reduces the chance of skidding or locking and makes the ride more comfortable.", "Reduce la posibilidad de derrapar o bloquear las ruedas y aumenta la comodidad.")

# ---------------------------------------------------------------- 3.4 helmet and gear
Q("hm1", "helmet", "What is the main cause of death in motorcycle and moped accidents?", "¿Cuál es la principal causa de mortalidad en los accidentes de moto y ciclomotor?",
  [("Not wearing the helmet", "No usar el casco"), ("Riding in the rain", "Circular con lluvia"), ("Worn tyres", "Los neumáticos gastados")],
  "The helmet absorbs much of the energy of an impact and protects against abrasion.", "El casco absorbe gran parte de la energía del impacto y protege de la abrasión.")
Q("hm2", "helmet", "Which helmet type is recommended?", "¿Qué tipo de casco es recomendable?",
  [("Full-face (integral)", "El integral"), ("Open-face (jet)", "El jet"), ("Any, if it is light", "Cualquiera, si es ligero")],
  "It covers the whole head and face; the jet leaves the chin bare.", "Cubre toda la cabeza y la cara; el jet deja la barbilla al descubierto.")
Q("hm3", "helmet", "Your helmet hit the ground hard when the parked motorcycle fell over, but you see no damage. What do you do?", "Tu casco se golpeó fuerte contra el suelo al caerse la moto aparcada, pero no ves daños. ¿Qué haces?",
  [("Replace it", "Sustituirlo"), ("Keep using it if the visor still closes", "Seguir usándolo si la pantalla cierra"), ("Use it only in town", "Usarlo solo en ciudad")],
  "A helmet must be replaced after an accident or a hard knock.", "El casco se debe sustituir después de un accidente o de un golpe fuerte.")
Q("hm4", "helmet", "What must the helmet label show?", "¿Qué debe acreditar la etiqueta del casco?",
  [("Approval to UNECE Regulation 22", "La homologación conforme al Reglamento UNECE R22"), ("The colour code", "El código de color"), ("The owner’s name", "El nombre del propietario")],
  "Approval guarantees it has passed the safety tests.", "La homologación garantiza que ha superado las pruebas de seguridad.")
Q("hm5", "helmet", "How should a modular helmet be used while riding?", "¿Cómo debe usarse un casco modular al circular?",
  [("With the chin bar closed", "Con la mentonera cerrada"), ("With the chin bar raised, for ventilation", "Con la mentonera levantada, para ventilar"), ("Either way", "De cualquier forma")],
  "The chin bar can be lifted, but it only protects like a full-face helmet when closed.", "La mentonera se puede levantar, pero solo protege como un integral si está cerrada.")
Q("hm6", "helmet", "Who must wear a helmet on a motorcycle?", "¿Quién debe llevar casco en una moto?",
  [("Rider and passenger, on every road", "Conductor y pasajero, en todo tipo de vías"), ("Only the rider", "Solo el conductor"), ("Only out of town", "Solo fuera de poblado")],
  "It is compulsory for rider and passenger, properly fastened.", "Es obligatorio para conductor y pasajero, adecuadamente abrochado.")
Q("hm7", "helmet", "Which helmet colours are safer?", "¿Qué colores de casco son más seguros?",
  [("Light, bright and reflective ones", "Los claros, brillantes y reflectantes"), ("Dark ones", "Los oscuros"), ("Colour makes no difference", "El color no influye")],
  "They make you more visible.", "Te hacen más visible.")
Q("ge1", "gear", "Where are protective gloves compulsory?", "¿Dónde son obligatorios los guantes de protección?",
  [("On interurban roads", "En vías interurbanas"), ("On every road", "En todo tipo de vías"), ("Only on motorways", "Solo en autopistas")],
  "Since 1 October 2026, gloves are compulsory for rider and passenger on interurban roads.", "Desde el 1 de octubre de 2026, los guantes son obligatorios para conductor y pasajero en vías interurbanas.")
Q("ge2", "gear", "Where must you wear closed shoes covering the whole foot?", "¿Dónde debes llevar calzado cerrado que cubra todo el pie?",
  [("On every road", "En todo tipo de vías"), ("Only on interurban roads", "Solo en vías interurbanas"), ("It is only recommended", "Solo es recomendable")],
  "Closed shoes are compulsory on every road; gloves only on interurban roads.", "El calzado cerrado es obligatorio en todas las vías; los guantes, solo en las interurbanas.")
Q("ge3", "gear", "When must you wear the reflective vest that your motorcycle carries?", "¿Cuándo debes ponerte el chaleco reflectante que lleva tu moto?",
  [("When you get off and stand on the carriageway or shoulder of an interurban road", "Al bajarte y ocupar la calzada o el arcén de una vía interurbana"), ("Always while riding", "Siempre al circular"), ("Only at night", "Solo de noche")],
  "Since October 2026 motorcycles must carry the vest; it is worn when you get off on an interurban road.", "Desde octubre de 2026 las motos deben llevar el chaleco; se usa al bajarse en una vía interurbana.")
Q("ge4", "gear", "A courier works on a moped. When must they wear a reflective vest?", "Un repartidor trabaja en ciclomotor. ¿Cuándo debe llevar chaleco reflectante?",
  [("On every road, while riding", "En todo tipo de vías, al circular"), ("Only on interurban roads", "Solo en vías interurbanas"), ("Never", "Nunca")],
  "Those who work riding motorcycles, mopeds, bicycles or VMP must wear it on every road.", "Quienes trabajan circulando en moto, ciclomotor, bicicleta o VMP deben llevarlo en todas las vías.")
Q("ge5", "gear", "What does an airbag jacket or vest do?", "¿Qué hace una chaqueta o chaleco airbag?",
  [("Inflates when you are thrown off, protecting chest, neck and spine", "Se activa al salir despedido y protege tórax, cervicales y columna"), ("Keeps you warm", "Te protege del frío"), ("Makes you visible at night", "Te hace visible de noche")],
  "It is one of the recommended extra garments.", "Es una de las prendas complementarias recomendadas.")
Q("ge6", "gear", "What should a rider’s suit or jacket be like?", "¿Cómo debe ser el traje o la chaqueta del motorista?",
  [("Abrasion-resistant, with protectors, in bright colours", "Resistente a la abrasión, con protecciones y de colores llamativos"), ("Light and dark, to stay cool", "Ligera y oscura, para no pasar calor"), ("Any, if you wear gloves", "Cualquiera, si llevas guantes")],
  "Preferably leather or another abrasion-resistant material, with protectors at the back, knees and elbows.", "Preferiblemente de piel u otro material resistente a la abrasión, con protecciones en espalda, rodillas y codos.")

# ---------------------------------------------------------------- 4 road and weather
Q("wt1", "weather", "You have to cross a painted marking in a bend. How do you do it?", "Tienes que pasar sobre una marca vial pintada en una curva. ¿Cómo lo haces?",
  [("Slow down before and cross it with the motorcycle as upright as possible", "Reducir antes y pasar con la moto lo más enderezada posible"), ("Lean more to get past quickly", "Inclinarte más para pasar rápido"), ("Brake hard on the marking", "Frenar fuerte sobre la marca")],
  "With low grip, slow down beforehand and keep the motorcycle at right angles to the surface.", "Con baja adherencia, reducir antes y pasar con la moto en ángulo recto con el pavimento.")
Q("wt2", "weather", "When is rain most dangerous?", "¿Cuándo es más peligrosa la lluvia?",
  [("With the first drops, which make a slippery film with the dirt", "Con las primeras gotas, que forman con la suciedad un barrillo deslizante"), ("After an hour of heavy rain", "Tras una hora de lluvia intensa"), ("When it stops", "Cuando para")],
  "The first drops mix with the dirt on the road and make it very slippery.", "Las primeras gotas forman con la suciedad un barrillo altamente deslizante.")
Q("wt3", "weather", "How does your course advise braking in the rain on a motorcycle?", "¿Cómo aconseja tu curso frenar en moto con lluvia?",
  [("Early and gently, shared between both wheels with less pressure on the front", "Con antelación y suavidad, repartiendo entre las dos ruedas con menos presión en la delantera"),
   ("Only with the front brake", "Solo con el freno delantero"), ("Hard and late, to dry the brakes", "Fuerte y tarde, para secar los frenos")],
  "A locked rear wheel is easier to control than a locked front one; if a wheel locks, release and brake again.", "El bloqueo de la trasera se controla mejor que el de la delantera; si se bloquea una rueda, soltar y volver a frenar.")
Q("wt4", "weather", "Why is main beam a bad idea in the rain?", "¿Por qué no conviene la luz de carretera con lluvia?",
  [("Its reflection on the water dazzles you", "Su reflejo en el agua te deslumbra"), ("It uses more battery", "Gasta más batería"), ("It is forbidden in the rain", "Está prohibida con lluvia")],
  "Water on the road reflects the light and hides the markings.", "El agua en la calzada refleja la luz y dificulta ver las marcas viales.")
Q("wt5", "weather", "What is aquaplaning?", "¿Qué es el aquaplaning?",
  [("The tyre slides on a layer of water it cannot clear, and the motorcycle ignores steering and brakes", "El neumático se desliza sobre una capa de agua que no puede desalojar y la moto no obedece a la dirección ni al freno"),
   ("Riding through a deep puddle", "Pasar por un charco profundo"), ("The visor misting up", "El empañamiento de la visera")],
  "It happens at too high a speed and is worse with worn tyres and on two-wheelers.", "Se produce a velocidad excesiva y es peor con neumáticos gastados y en vehículos de dos ruedas.")
Q("wt6", "weather", "You are caught in a very heavy storm. What is best?", "Te sorprende una tormenta muy intensa. ¿Qué es lo mejor?",
  [("Stop and take shelter away from the motorcycle", "Detener la marcha y resguardarse apartado de la moto"), ("Ride faster to get out of it", "Acelerar para salir de ella"), ("Shelter right next to the motorcycle", "Resguardarse junto a la moto")],
  "In a torrential storm, stop and shelter away from the motorcycle.", "Con lluvia torrencial, detener la marcha y resguardarse apartado de la moto.")
Q("wt7", "weather", "On an autovía, snow makes driving difficult. What is the rule?", "En una autovía la nieve dificulta la circulación. ¿Qué norma se aplica?",
  [("No overtaking, and ride in the right-hand lane", "Prohibido adelantar y circular por el carril de la derecha"), ("Ride in the left-hand lane, which is cleaner", "Circular por el carril izquierdo, que está más limpio"), ("Nothing special", "Nada especial")],
  "The left lanes stay free for emergency vehicles and snowploughs.", "Los carriles de la izquierda quedan libres para emergencias y quitanieves.")
Q("wt8", "weather", "Which is the most dangerous situation on the road?", "¿Cuál es la situación más peligrosa en la vía?",
  [("Ice: grip is almost nil and the stopping distance ×10", "El hielo: adherencia casi nula y distancia de detención ×10"), ("Light rain", "La lluvia ligera"), ("Strong sun", "El sol fuerte")],
  "The best advice is not to ride on icy roads.", "Lo recomendable es no circular con hielo en la calzada.")
Q("wt9", "weather", "On hard snow or ice, what must you avoid?", "Sobre nieve endurecida o hielo, ¿qué debes evitar?",
  [("Braking or accelerating", "Frenar o acelerar"), ("Keeping a steady speed", "Mantener una velocidad constante"), ("Using a high gear", "Usar una marcha larga")],
  "Don’t brake or accelerate on hard snow or ice.", "Sobre placas de nieve endurecida o hielo, no frenes ni aceleres.")
Q("wt10", "weather", "Riding in snow, which gear should you use?", "Circulando con nieve, ¿qué marcha debes usar?",
  [("The highest gear possible, with smooth, steady throttle", "La marcha más alta posible, con aceleración suave y constante"), ("First gear all the time", "Primera todo el tiempo"), ("Neutral downhill", "Punto muerto en las bajadas")],
  "Uphill long gears; downhill short gears for engine braking.", "Subiendo, marchas largas; bajando, marchas cortas para usar el freno motor.")
Q("wt11", "weather", "In fog, which lights should you use?", "Con niebla, ¿qué alumbrado debes usar?",
  [("The compulsory lights and the fog light if fitted, not main beam", "El alumbrado obligatorio y la antiniebla si la hay, sin luz de carretera"), ("Main beam, to see further", "La luz de carretera, para ver más"), ("Only the position light", "Solo la luz de posición")],
  "Main beam reflects back off the fog and dazzles you (mirror effect).", "La luz de carretera se refleja en la niebla y deslumbra (efecto espejo).")
Q("wt12", "weather", "Strong gusts of crosswind. What do you do?", "Fuertes rachas de viento lateral. ¿Qué haces?",
  [("Slow down, hold the handlebar firmly and watch for the screen effect", "Reducir la velocidad, sujetar el manillar con firmeza y cuidado con el efecto pantalla"), ("Speed up to get through quickly", "Acelerar para pasar rápido"), ("Ride close to lorries for shelter", "Ir pegado a los camiones para resguardarte")],
  "Motorcycles, especially with a passenger, are among the most affected.", "Las motos, sobre todo con pasajero, están entre los vehículos más afectados.")
Q("wt13", "weather", "What does a windsock beside the road tell you?", "¿Qué te indica una manga de viento junto a la vía?",
  [("The side the wind blows from and its strength", "El lado del que sopla el viento y su intensidad"), ("That an airport is near", "Que hay un aeropuerto cerca"), ("Only that there is wind", "Solo que hay viento")],
  "The P-29 sign does not show the side; the windsock does.", "La señal P-29 no indica el lado; la manga sí.")
Q("wt14", "weather", "Riding at night or through a tunnel, may you use a dark visor or sunglasses?", "De noche o en un túnel, ¿puedes usar visera oscura o gafas de sol?",
  [("No, never", "No, nunca"), ("Yes, if there is dazzle", "Sí, si hay deslumbramiento"), ("Yes, in tunnels", "Sí, en los túneles")],
  "They reduce visibility; use them only by day against the sun.", "Restan visibilidad; solo de día y contra el sol.")
Q("wt15", "weather", "Which road surfaces call for special care on a motorcycle?", "¿Qué superficies exigen especial cuidado en moto?",
  [("Loose gravel or sand, rails, painted markings and oil patches", "Gravilla suelta o arena, raíles, marcas viales pintadas y manchas de aceite"), ("New asphalt in dry weather", "Asfalto nuevo y seco"), ("Concrete in a car park", "Hormigón en un aparcamiento")],
  "Adapt to the road: all of these reduce grip.", "Hay que adaptarse a la vía: todas ellas reducen la adherencia.")
