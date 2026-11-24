# -*- coding: utf-8 -*-
"""Question bank for the interactive Topic 10 page (accidents and their factors). In every question the FIRST option
is the correct one (the page shuffles options when it shows them). Ids must be unique and must not start with "ai"."""

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
        recap=[("For the WHO, road accidents are a serious, priority public-health problem; in Spain, a main cause of death and injury.", "Para la OMS, un problema grave y prioritario de salud pública; en España, una de las principales causas de muerte y lesiones."),
               ("Each death affects about 100 people. Costs: human, material, health and administrative.", "Cada víctima mortal afecta a unas 100 personas. Costes: humanos, materiales, sanitarios y administrativos."),
               ("Most accidents can be avoided: they are predictable, caused by risk factors.", "La mayoría son evitables: son sucesos predecibles, debidos a factores de riesgo."),
               ("Avoid above all the risk factors that depend on the driver.", "Hay que evitar sobre todo los factores que dependen del conductor.")],
        trap=("Thinking accidents are mostly bad luck.", "Pensar que los accidentes se deben sobre todo a la mala suerte.")),
    "whenwhere": dict(sec=2, en="Where and when", es="Dónde y cuándo",
        recap=[("More accidents with victims in towns; more deaths on interurban roads (higher speeds).", "Más accidentes con víctimas en vías urbanas; más muertos en carretera (más velocidad)."),
               ("Most interurban accidents: straight roads with good visibility, running off the road. Autovías and autopistas are the safest.", "La mayoría en carretera: rectas con buena visibilidad, salidas de la vía. Autovías y autopistas, las más seguras."),
               ("Worst times: commuting (above all leaving work in the afternoon); holidays and weekends, above all in the early hours.", "Peores momentos: ir y volver del trabajo (sobre todo al salir por la tarde); vacaciones y fines de semana, sobre todo de madrugada."),
               ("Vans: worst hour 15–16 h, worst day Friday then Monday; main factor distraction.", "Furgonetas: peor hora 15–16 h, peor día el viernes y luego el lunes; factor principal, la distracción.")],
        trap=("Thinking most road accidents happen in sharp bends.", "Pensar que la mayoría de los accidentes en carretera son en curvas cerradas.")),
    "elderly": dict(sec=3, en="Older drivers", es="Conductores mayores",
        recap=[("Main problem: the decline of physical and mental abilities.", "Principal problema: el deterioro de las capacidades psicofísicas."),
               ("Narrower field of vision (worse at night, dazzle); hearing loss.", "Menor campo visual (peor de noche, deslumbramientos); pérdida de audición."),
               ("Slower in complex situations: longer reaction time. Medicines; less attention; less strength.", "Más lentos en situaciones complejas: más tiempo de reacción. Medicamentos; menos atención; menos fuerza."),
               ("Be respectful and patient with them.", "Ser respetuosos y tolerantes con ellos.")],
        trap=("Thinking older drivers mainly fail through speeding.", "Pensar que el problema de los mayores es sobre todo la velocidad.")),
    "peds": dict(sec=3, en="Pedestrians", es="Peatones",
        recap=[("More pedestrian accidents in towns; more serious on interurban roads. More than half of pedestrians killed die in towns.", "Más atropellos en ciudad; más graves en carretera. Más de la mitad de los peatones fallecidos mueren en ciudad."),
               ("Older pedestrians: more accidents alone than with children; noise, speeds, light colours, wide streets.", "Mayores: más accidentes solos que con niños; ruido, velocidades, colores de semáforos, calles anchas."),
               ("Children: hit on the head; most at the end of the school day; under 7 can’t place sounds; 40 % less field of vision; confuse seeing with being seen.", "Niños: impacto en la cabeza; sobre todo a la salida del colegio; menores de 7 no localizan sonidos; 40 % menos de campo visual; confunden ver con ser visto."),
               ("Slow down near stopped (school) buses, garages, phones, leisure areas; don’t wave pedestrians across or park on the pavement.", "Reducir ante autobuses (escolares) parados, garajes, móviles, zonas de ocio; no hacer señales para que crucen ni aparcar en la acera.")],
        trap=("Waving a pedestrian across to be polite.", "Hacer señales a un peatón para que cruce, por cortesía.")),
    "cyclists": dict(sec=3, en="Cyclists", es="Ciclistas",
        recap=[("Mostly weekends and good weather, on conventional roads; mostly head-on or front-side collisions.", "Sobre todo en fin de semana y con buen tiempo, en carreteras convencionales; sobre todo choques frontales o frontolaterales."),
               ("Carriageway if there is no bike lane; no pavements except under 12 with an adult on foot, if the town allows.", "Por la calzada si no hay carril bici; nunca por aceras salvo menores de 12 con un adulto a pie, si lo permite el ayuntamiento."),
               ("In town: centre of the lane, 5 m behind. Overtaking: 1.5 m, out of town 20 km/h below the limit, change lane fully if there are two.", "En ciudad: centro del carril, 5 m detrás. Adelantar: 1,5 m, en interurbana 20 km/h menos, cambiar de carril del todo si hay dos."),
               ("Helmet: every cyclist out of town; under 16 and delivery riders everywhere. 150 m reflective element at night out of town.", "Casco: todos en interurbanas; menores de 16 y repartidores en todas. Elemento reflectante a 150 m de noche en interurbana.")],
        trap=("Using the horn to warn a cyclist.", "Usar el claxon para avisar a un ciclista.")),
    "motos": dict(sec=3, en="Mopeds and motorcycles", es="Ciclomotores y motocicletas",
        recap=[("Less visible, less stable, more fragile; accidents easily fatal — not wearing a helmet is a main cause of death.", "Menos visibles, estables y más frágiles; accidentes muy letales: no usar el casco es una causa principal de muerte."),
               ("Most common accident: head-on or front-side collision when overtaking, especially in town.", "Accidente más común: colisión frontal o frontolateral al adelantar, sobre todo en ciudad."),
               ("Passenger: harder to lock the rear wheel, longer stopping distance. Very slowly in a bend: no front brake.", "Con pasajero: más difícil bloquear la rueda trasera, mayor distancia de detención. Muy despacio en curva: no frenar delante."),
               ("Since 1 Oct 2026: gloves out of town, closed shoes everywhere; the bike carries a vest; delivery riders wear it always.", "Desde el 1-10-2026: guantes en interurbanas, calzado cerrado en todas; la moto lleva chaleco; los profesionales lo llevan siempre.")],
        trap=("Thinking a vest is compulsory while riding.", "Pensar que el chaleco es obligatorio al circular.")),
    "vmp": dict(sec=3, en="E-scooters (VMP)", es="Patinetes y VMP",
        recap=[("Minimum age 15; helmet compulsory; rider only; arm signals; max 25 km/h.", "Edad mínima 15; casco obligatorio; solo el conductor; señales con el brazo; máximo 25 km/h."),
               ("Never on pavements, autopistas/autovías, travesías, interurban roads or urban tunnels (except bike lanes and roads closed to motor traffic).", "Nunca por aceras, autopistas/autovías, travesías, interurbanas ni túneles urbanos (salvo vías ciclistas y vías cerradas a motor)."),
               ("Two brakes, white front and red rear lights, reflectors, bell; lights always on (by day from Oct 2027).", "Dos frenos, luz blanca delante y roja detrás, catadióptricos, timbre; alumbrado siempre (de día desde octubre de 2027)."),
               ("Registered, certified (uncertified until 21 Jan 2027), labelled and insured. Reduced mobility at walking pace = pedestrian.", "Inscrito, certificado (sin certificado hasta el 21-1-2027), con etiqueta y asegurado. Movilidad reducida al paso = peatón.")],
        trap=("Riding an e-scooter on the pavement at low speed.", "Circular en patinete por la acera despacio.")),
    "young": dict(sec=3, en="Young drivers", es="Conductores jóvenes",
        recap=[("A risk group, not vulnerable users.", "Grupo de riesgo, no usuarios vulnerables."),
               ("Main cause of injury and death between 15 and 29 (almost 35 % of deaths); rises from 14–15.", "Principal causa de lesiones y muerte entre 15 y 29 años (casi el 35 %); aumenta desde los 14–15."),
               ("When: fun, alcohol, several occupants, nights, weekends, Christmas, summer.", "Cuándo: diversión, alcohol, varios ocupantes, noches, fines de semana, Navidad, verano."),
               ("Why: inexperience, speed, rule-breaking, alcohol and drugs; low risk perception, overconfidence.", "Por qué: inexperiencia, velocidad, incumplir normas, alcohol y drogas; baja percepción del riesgo, exceso de confianza.")],
        trap=("Calling young drivers ‘vulnerable users’.", "Llamar «usuarios vulnerables» a los jóvenes.")),
    "factors": dict(sec=4, en="The three factors", es="Los tres factores",
        recap=[("Human factor 70–90 %: the main one.", "Factor humano 70–90 %: el principal."),
               ("Road and surroundings 10–35 %: the second.", "Vía y entorno 10–35 %: el segundo."),
               ("Vehicle 4–13 %: the least; worse with poor maintenance (tyres, brakes).", "Vehículo 4–13 %: el que menos; aumenta con mal mantenimiento (neumáticos, frenos)."),
               ("Driver’s top causes: distraction, no safety distance, speed, priority, wrong turns, illegal overtaking.", "Causas del conductor: distracciones, distancia de seguridad, velocidad, prioridad, giros, adelantamientos.")],
        trap=("Ranking the vehicle above the road.", "Poner el vehículo por delante de la vía.")),
    "speed": dict(sec=4, en="Speed and stopping distance", es="Velocidad y distancia de detención",
        recap=[("More speed: tunnel vision, less time to analyse and react, more serious injuries. 90 % of information is visual.", "Más velocidad: efecto túnel, menos capacidad de análisis y reacción, lesiones más graves. El 90 % de la información es visual."),
               ("Reaction time 0.5–1 s, typically 0.75 s; longer with age, fatigue, alcohol, drugs, medicines, heat.", "Tiempo de reacción 0,5–1 s, habitual 0,75 s; más con la edad, fatiga, alcohol, drogas, medicamentos, calor."),
               ("Stopping distance = reaction distance + braking distance.", "Distancia de detención = distancia de reacción + distancia de frenado."),
               ("Braking distance: speed, mass, technique, vehicle, road; rain ×2, snow or ice ×10.", "Distancia de frenado: velocidad, masa, técnica, vehículo, vía; lluvia ×2, nieve o hielo ×10.")],
        trap=("Thinking the reaction distance is covered while braking.", "Pensar que la distancia de reacción se recorre frenando.")),
    "fatigue": dict(sec=4, en="Fatigue and sleep", es="Fatiga y sueño",
        recap=[("Fatigue: main cause is driving long periods without proper rest; recommended 20–23 °C inside.", "Fatiga: la principal causa es conducir mucho tiempo sin descansar bien; habitáculo a 20–23 °C."),
               ("Sleep causes 15–30 % of accidents; you don’t need to fall asleep; microsleeps.", "El sueño causa el 15–30 % de los accidentes; no hace falta dormirse; microsueños."),
               ("Worst hours 3–5 and 14–16; sleep 7–9 h; coffee has a rebound effect; narcolepsy prevents a licence.", "Peores horas 3–5 y 14–16; dormir 7–9 h; el café tiene efecto rebote; la narcolepsia impide el permiso."),
               ("Stop at least every 2 h or 200 km for 20–30 min. Rumble strips warn by noise and vibration.", "Parar como mínimo cada 2 h o 200 km, 20–30 min. Las guías sonoras avisan con ruido y vibración.")],
        trap=("Trusting coffee to keep you awake for the whole trip.", "Confiar en el café para aguantar todo el viaje.")),
    "health": dict(sec=4, en="Illness, medicines and heat", es="Enfermedades, medicamentos y calor",
        recap=[("Chronic illness: know the medicines’ side effects, spot the first symptoms, no alcohol with medicines, ask the doctor.", "Enfermedad crónica: conocer los efectos secundarios, reconocer los síntomas, sin alcohol con medicamentos, consultar al médico."),
               ("Allergies: first-generation antihistamines cause strong drowsiness; keep windows closed.", "Alergias: los antihistamínicos de primera generación dan mucha somnolencia; ventanillas cerradas."),
               ("Stress: more aggression and risk; depression: more distraction; some psychotropics forbid driving.", "Estrés: más agresividad y riesgo; depresión: más distracciones; algunos psicofármacos impiden conducir."),
               ("The ‘see leaflet’ pictogram warns, it doesn’t forbid. Heat: longer reaction time — stops, water, 20–23 °C.", "El pictograma «ver prospecto» advierte, no prohíbe. Calor: más tiempo de reacción; paradas, agua, 20–23 °C.")],
        trap=("Thinking the medicine pictogram forbids driving.", "Pensar que el pictograma del medicamento prohíbe conducir.")),
    "distract": dict(sec=4, en="Distractions", es="Distracciones",
        recap=[("The fastest-growing risk factor: one in three fatal accidents; worst among 18–25 and over 70.", "El factor que más ha aumentado: uno de cada tres accidentes mortales; sobre todo de 18 a 25 y mayores de 70."),
               ("Phone: most dangerous when answering, dialling, talking and hanging up; after 1.5 min, 40 % of signs missed.", "Móvil: lo más peligroso es recibir, marcar, hablar y colgar; al minuto y medio no se percibe el 40 % de las señales."),
               ("Most frequent phone accident: running off the road; like 1 g/l of alcohol. In hand: 6 points and 200 €, even at a red light.", "Accidente más frecuente por el móvil: salida de vía; como 1 g/l de alcohol. En la mano: 6 puntos y 200 €, incluso en un semáforo."),
               ("GPS: plan before, voice guidance, never near the airbag. Smoking: not prohibited, not recommended.", "GPS: planificar antes, instrucciones de voz, nunca cerca del airbag. Fumar: no prohibido, no recomendable.")],
        trap=("Thinking hands-free makes the phone harmless.", "Pensar que el manos libres hace el móvil inofensivo.")),
    "alcohol": dict(sec=4, en="Alcohol", es="Alcohol",
        recap=[("A depressant with an initial euphoric phase: false sense of control, tunnel vision, worse coordination.", "Depresor con una fase euforizante inicial: falsa sensación de control, visión túnel, peor coordinación."),
               ("Limits in air: 0.25 general (cyclists and VMP too), 0.15 first two years and professionals, 0.0 under 18.", "Tasas en aire: 0,25 general (también bici y VMP), 0,15 dos primeros años y profesionales, 0,0 menores de edad."),
               ("In the blood after 5 min, peak 30–90 min, slow elimination; empty stomach and fizzy drinks speed it up; fermented slower than distilled.", "En sangre a los 5 min, pico a los 30–90 min, eliminación lenta; en ayunas y con gas, más rápido; fermentadas más lentas que destiladas."),
               ("More effect on slim people, women, under 18 and over 65, the inexperienced. No tricks fool the breathalyser.", "Afecta más a delgados, mujeres, menores de 18 y mayores de 65, inexpertos. No hay trucos contra el etilómetro.")],
        trap=("Thinking coffee or water lowers the reading.", "Pensar que el café o el agua bajan la tasa.")),
    "drugslaw": dict(sec=4, en="Drugs and the law", es="Drogas y tratamiento legal",
        recap=[("Drugs forbidden for all drivers (cyclists and VMP too), except prescribed treatment that doesn’t affect driving.", "Drogas prohibidas a todos los conductores (también bici y VMP), salvo tratamiento prescrito que no afecte."),
               ("Alcohol: breathalyser; drugs: saliva test plus analysis; contrast test (blood) on request or court order.", "Alcohol: etilómetro; drogas: prueba salival y análisis; contraste (sangre) a petición o por orden judicial."),
               ("Second test at least 10 min later; contrast paid first, refunded if negative. Immobilisation if positive or if you refuse.", "Segunda prueba al menos 10 min después; contraste pagado antes, se devuelve si es negativo. Inmovilización si es positivo o si se niega."),
               ("Fines 500–1,000 € for alcohol, 1,000 € for drugs; 4 or 6 points; serious cases are crimes.", "Multas de 500–1.000 € por alcohol, 1.000 € por drogas; 4 o 6 puntos; los casos graves son delito.")],
        trap=("Thinking a cyclist can’t be tested.", "Pensar que a un ciclista no se le puede hacer la prueba.")),
    "controls": dict(sec=4, en="Driving position and controls", es="Puesto del conductor y mandos",
        recap=[("Seat: press the pedals fully with legs slightly bent. Backrest and wheel: reach the top with arms bent, back on the seat.", "Asiento: pisar a fondo con las piernas algo flexionadas. Respaldo y volante: llegar arriba con los brazos flexionados, sin separar la espalda."),
               ("Too close: fatigue and airbag danger. Too far: slow reactions, passive safety works worse.", "Muy cerca: fatiga y peligro por el airbag. Muy lejos: reacciones lentas, la seguridad pasiva actúa peor."),
               ("Wheel at ten to two or quarter to three, hands outside, never crossed. Low gears: more force, less speed.", "Volante a las 2 menos 10 o 3 menos cuarto, manos por fuera, sin cruzarlas. Marchas cortas: más fuerza, menos velocidad."),
               ("Clutch released = engaged. Motorcycle: right hand throttle + front brake; left hand clutch; right foot rear brake; left foot gears.", "Embrague sin pisar = embragado. Moto: mano derecha acelerador + freno delantero; izquierda embrague; pie derecho freno trasero; izquierdo marchas.")],
        trap=("Mixing up ‘engaged’ and ‘pressed’ for the clutch.", "Confundir embragado con pisado.")),
    "tyres": dict(sec=4, en="Tyres", es="Neumáticos",
        recap=[("Tyres: the main cause of accidents from mechanical failure. Parts: tread, shoulders, carcass, beads, sidewalls.", "Neumáticos: principal causa de accidente por fallo mecánico. Partes: banda, hombros, carcasa, talones, flancos."),
               ("225/70 R16 110S: width mm, profile %, radial, rim inches, load index, speed symbol. DOT 3221 = week 32 of 2021.", "225/70 R16 110S: anchura mm, perfil %, radial, pulgadas, índice de carga, código de velocidad. DOT 3221 = semana 32 de 2021."),
               ("Pressure: every ~15 days, cold; spare at the highest; low wears edges, high wears centre; unequal on an axle is worst.", "Presión: cada ~15 días, en frío; repuesto a la más alta; baja gasta los bordes, alta el centro; descompensada en un eje, lo peor."),
               ("Change at 1.6 mm (2 recommended); best tyres on the rear axle; blow-out: hold firm, don’t lift off suddenly, brake minimally.", "Cambiar a 1,6 mm (recomendable 2); los mejores detrás; reventón: sujetar fuerte, no soltar el acelerador de golpe, frenar lo mínimo.")],
        trap=("Letting air out of hot tyres.", "Quitar aire a los neumáticos calientes.")),
    "brakes": dict(sec=4, en="Brakes", es="Frenos",
        recap=[("Service brake on all wheels; emergency brake = last part of the travel, one wheel each side; parking brake usually rear.", "Servicio en todas las ruedas; socorro = último recorrido, una rueda de cada lado; estacionamiento normalmente detrás."),
               ("Servo brake works only with the engine running. Engine brake on long descents; fading from overheating.", "El servofreno solo funciona con el motor en marcha. Freno motor en descensos largos; fading por calentamiento."),
               ("Emergency: press fully; without ABS release and press again if wheels lock; with ABS keep pressing; clutch just before stopping.", "Emergencia: pisar a fondo; sin ABS soltar y volver a pisar si bloquea; con ABS seguir pisando; embrague justo antes de parar."),
               ("Spongy pedal = air; long travel = fluid loss; harder pedal = worn pads; pulls = unequal pressure. Brakes: first cause of ITV failure.", "Pedal esponjoso = aire; recorrido excesivo = pérdida de líquido; más fuerza = pastillas gastadas; se desvía = presión desigual. Frenos: primera causa de ITV no superada.")],
        trap=("Pumping the pedal in an emergency stop with ABS.", "Bombear el pedal en una frenada de emergencia con ABS.")),
    "chassis": dict(sec=4, en="Suspension, steering, lights, ESP", es="Suspensión, dirección, luces, ESP",
        recap=[("Suspension joins wheels and body, absorbs bumps, controls roll. Smart suspension: hard or soft.", "La suspensión une ruedas y vehículo, absorbe irregularidades y compensa el balanceo. Inteligente: dura o blanda."),
               ("Bounces: shock absorbers or high pressure; leans: shock absorbers or low pressure.", "Rebota: amortiguadores o mucha presión; se inclina: amortiguadores o poca presión."),
               ("Heavy steering: low pressure or alignment; play: worn part. Speed-sensitive steering stiffens with speed.", "Dirección dura: poca presión o alineación; holgura: pieza desgastada. La asistida progresiva se endurece con la velocidad."),
               ("Lights: see, be seen, signal; check the aim after loading. ESP corrects a skid before it happens.", "Luces: ver, ser vistos y señalizar; revisar el reglaje tras cargar. El ESP corrige el derrape antes de que ocurra.")],
        trap=("Thinking ESP only works after the car has spun.", "Pensar que el ESP actúa cuando el coche ya ha trompeado.")),
    "passive": dict(sec=4, en="Passive safety", es="Seguridad pasiva",
        recap=[("Rigid central cell, crumple zones; don’t modify the bodywork. Laminated windscreen, tempered side and rear glass.", "Habitáculo rígido, deformación programada; no modificar la carrocería. Parabrisas laminado; laterales y trasera templados."),
               ("Belt: over the collarbone and low on the hips; no clips, no thick coats, no cushions (submarining). Replace after a strong crash.", "Cinturón: sobre la clavícula y bajo en la cadera; sin pinzas, ropa gruesa ni cojines (efecto submarino). Cambiarlo tras un fuerte accidente."),
               ("Children ≤ 135 cm in approved seats, rear-facing as long as possible, rear centre safest; never rear-facing with an active airbag.", "Menores ≤ 135 cm en SRI homologado, de espaldas el mayor tiempo posible, centro trasero el más seguro; nunca hacia atrás con airbag activo."),
               ("Airbag 25 cm (never under 10), inflates at 300 km/h, always with the belt. Head restraint: top with head, middle at eyes, ≤ 4 cm.", "Airbag a 25 cm (nunca menos de 10), se infla a 300 km/h, siempre con cinturón. Reposacabezas: arriba con la cabeza, centro a los ojos, ≤ 4 cm.")],
        trap=("Thinking the airbag replaces the belt.", "Pensar que el airbag sustituye al cinturón.")),
    "helmet": dict(sec=4, en="Helmets and rider gear", es="Casco y equipamiento",
        recap=[("Not wearing a helmet is the main cause of death in motorcycle accidents; compulsory for rider and passenger.", "No usar casco es la principal causa de muerte en accidentes de moto; obligatorio para conductor y pasajero."),
               ("Full-face recommended; modular lifts; jet leaves the chin open. Approved to UNECE R22.", "Integral recomendable; modular se levanta; jet no cubre la barbilla. Homologado UNECE R22."),
               ("Light, bright colours; anti-fog visor; replace after an accident or a hard knock.", "Colores claros y brillantes; pantalla antivaho; sustituir tras un accidente o golpe fuerte."),
               ("Gloves compulsory out of town; closed shoes everywhere; the bike must carry a vest, worn when you get off on an interurban road.", "Guantes obligatorios en interurbanas; calzado cerrado en todas; la moto debe llevar chaleco, que te pones al bajarte en una vía interurbana.")],
        trap=("Keeping a helmet that has had a hard knock because it ‘looks fine’.", "Seguir usando un casco que ha sufrido un golpe porque «parece bien».")),
    "adas": dict(sec=4, en="Driver-assistance systems", es="Sistemas ADAS",
        recap=[("ADAS help with cameras and sensors, warn or act; most can be switched off; the driver keeps an active role.", "Los ADAS ayudan con cámaras y sensores, avisan o actúan; la mayoría se pueden desconectar; el conductor mantiene un papel activo."),
               ("ISA reduces engine revs, never brakes; AEB brakes by itself; LDW off when you signal; RCTA up to 30 m.", "El ISA reduce revoluciones, nunca frena; el AEB frena solo; el LDW no actúa con intermitente; el RCTA hasta 30 m."),
               ("eCall calls 112 when airbags fire; EDR can’t be switched off; aftermarket ADAS only as warning systems.", "eCall llama al 112 al saltar los airbags; el EDR no se puede desactivar; los aftermarket, solo como sistemas de aviso."),
               ("Driving test: full self-parking not allowed; ISA only with automatic speed control off; unlisted systems off.", "Examen: no se admite el estacionamiento total; ISA solo con el control automático de velocidad desconectado; los no recogidos, desactivados.")],
        trap=("Trusting the systems and taking more risks.", "Confiar en los sistemas y asumir más riesgos.")),
    "grip": dict(sec=4, en="Grip, bends and skids", es="Adherencia, curvas y derrapes",
        recap=[("Good grip: rough, dry, clean asphalt. Poor: smooth, cobbles, wet, gravel, leaves, snow, painted markings.", "Buena adherencia: asfalto rugoso, seco y limpio. Mala: liso, adoquines, mojado, gravilla, hojas, nieve, marcas viales."),
               ("Centrifugal force pushes outward: more with speed, tighter bends and weight.", "La fuerza centrífuga empuja hacia fuera: más con velocidad, curvas cerradas y peso."),
               ("Bend: brake before, gentle throttle during, accelerate and straighten on the way out.", "Curva: frenar antes, acelerar suave durante, acelerar y enderezar a la salida."),
               ("Skid: too much braking → release; front → straighten; rear → steer towards the skid.", "Derrape: exceso de frenada → soltar; delantero → enderezar; trasero → girar hacia el lado del derrape.")],
        trap=("Braking hard in the middle of a bend.", "Frenar fuerte en mitad de la curva.")),
    "weather": dict(sec=4, en="Weather", es="Climatología",
        recap=[("Rain: first drops are the worst; braking distance can double; aquaplaning with speed and worn tyres.", "Lluvia: las primeras gotas, lo peor; la frenada puede duplicarse; aquaplaning con velocidad y neumáticos gastados."),
               ("Snow: second gear, highest gear possible; thick in the ruts, thin outside them; motorway: no overtaking, right lane.", "Nieve: arrancar en segunda, la marcha más alta posible; gruesa por las rodaduras, fina fuera; autovía: no adelantar, carril derecho."),
               ("Ice: the most dangerous, stopping ×10; near 0 °C, night, bridges and shade. Chains can be compulsory — sprays don’t count.", "Hielo: lo más peligroso, detención ×10; cerca de 0 °C, de noche, puentes y sombra. Cadenas obligatorias si lo exigen; los sprays no valen."),
               ("Fog: lights, markings, slow down, no overtaking. Wind: steer into it, watch the screen effect. Sun: no sunglasses at night or in tunnels.", "Niebla: luces, marcas viales, reducir, no adelantar. Viento: girar contra él, efecto pantalla. Sol: sin gafas de sol de noche ni en túneles.")],
        trap=("Driving outside the ruts in thick snow.", "Circular fuera de las rodaduras con nieve gruesa.")),
}

# ---------------------------------------------------------------- 1. impact
Q("im1", "impact", "For the WHO, road accidents are…", "Para la OMS, los accidentes de circulación son…",
  [("a serious, priority public-health problem", "un problema grave y prioritario de salud pública"), ("a minor problem compared with other causes", "un problema menor frente a otras causas"), ("only a problem in poor countries", "un problema solo de países pobres")],
  "In Spain they are one of the main causes of death and injury.", "En España son una de las principales causas de muerte y lesiones.")
Q("im2", "impact", "On average, how many people are affected by each road death?", "¿A cuántas personas afecta de media cada víctima mortal?",
  [("About 100", "A unas 100"), ("About 10", "A unas 10"), ("About 1,000", "A unas 1.000")],
  "Family, friends, colleagues…", "Familiares, amigos, compañeros…")
Q("im3", "impact", "First aid, treatment and rehabilitation of the injured are…", "Los primeros auxilios, el tratamiento y la rehabilitación de los heridos son costes…",
  [("health costs", "sanitarios"), ("administrative costs", "administrativos"), ("material costs", "materiales")],
  "Administrative: police, fire services, insurance, legal costs.", "Administrativos: policía, bomberos, seguros, costes legales.")
Q("im4", "impact", "Most road accidents…", "La mayoría de los accidentes de tráfico…",
  [("can be avoided: they are predictable", "se pueden evitar: son predecibles"), ("are due to chance", "se deben al azar"), ("are due to the road", "se deben a la vía")],
  "They come from risk factors that can be avoided.", "Se deben a factores de riesgo que se pueden evitar.")
Q("im5", "impact", "Which risk factors matter most to avoid?", "¿Qué factores de riesgo es más importante evitar?",
  [("Those that depend on the driver", "Los que dependen del propio conductor"), ("Those that depend on the weather", "Los que dependen del tiempo"), ("Those that depend on other drivers", "Los que dependen de los demás")],
  "Speed, distraction, fatigue, sleep, illness, medicines, alcohol, drugs.", "Velocidad, distracciones, fatiga, sueño, enfermedades, fármacos, alcohol, drogas.")
Q("im6", "impact", "Following the manufacturer’s maintenance and passing the ITV reduces risks that depend on…", "Hacer los mantenimientos del fabricante y pasar la ITV reduce los riesgos que dependen…",
  [("the vehicle", "del vehículo"), ("the road", "de la vía"), ("the weather", "de la climatología")],
  "It avoids mechanical failures.", "Evita fallos mecánicos.")

# ---------------------------------------------------------------- 2. where and when
Q("wh1", "whenwhere", "Where are there more accidents with victims?", "¿Dónde hay más accidentes con víctimas?",
  [("On urban roads", "En vías urbanas"), ("On autopistas", "En autopistas"), ("On interurban roads", "En carretera")],
  "But more deaths on interurban roads.", "Pero más víctimas mortales en carretera.")
Q("wh2", "whenwhere", "Where are there more road deaths, and why?", "¿Dónde hay más víctimas mortales y por qué?",
  [("On interurban roads, because speeds are higher", "En carretera, porque se circula a mayor velocidad"), ("In towns, because there is more traffic", "En ciudad, porque hay más tráfico"), ("On autovías, because they are longer", "En autovías, porque son más largas")],
  "More accidents in towns, more deaths on the road.", "Más accidentes en ciudad, más muertos en carretera.")
Q("wh3", "whenwhere", "Most accidents on interurban roads happen…", "La mayoría de los accidentes en carretera se producen…",
  [("on straight stretches with good visibility, by running off the road", "en rectas con buena visibilidad, por salidas de la vía"), ("in sharp bends at night", "en curvas cerradas de noche"), ("at roundabouts", "en las glorietas")],
  "Single-vehicle accidents, often from distraction.", "Accidentes en solitario, a menudo por distracción.")
Q("wh4", "whenwhere", "Which roads are considered the safest?", "¿Qué vías se consideran más seguras?",
  [("Autovías and autopistas", "Autovías y autopistas"), ("Conventional roads", "Carreteras convencionales"), ("Town streets", "Calles urbanas")],
  "Separate directions, no intersections, gentler layout.", "Sentidos separados, sin intersecciones, trazado menos sinuoso.")
Q("wh5", "whenwhere", "On working days, the most dangerous time is…", "En días laborables, el momento más peligroso es…",
  [("leaving work in the afternoon", "al terminar la jornada por la tarde"), ("mid-morning", "a media mañana"), ("lunchtime", "a mediodía")],
  "Going to and leaving work, especially in the afternoon.", "Entrada y salida del trabajo, sobre todo por la tarde.")
Q("wh6", "whenwhere", "On holidays and weekends, the most dangerous time is…", "En vacaciones y fines de semana, el momento más peligroso es…",
  [("the early hours (madrugada)", "la madrugada"), ("the morning", "la mañana"), ("the afternoon", "la tarde")],
  "Night, fatigue, alcohol and leisure trips.", "Noche, fatiga, alcohol y trayectos de ocio.")
Q("wh7", "whenwhere", "Vans: the hour with most accidents is…", "Furgonetas: la hora de más siniestralidad es…",
  [("15:00 to 16:00", "de 15:00 a 16:00"), ("8:00 to 9:00", "de 8:00 a 9:00"), ("midnight to 1:00", "de 0:00 a 1:00")],
  "Most happen between 7:00 and 23:59.", "La mayoría entre las 7:00 y las 23:59.")
Q("wh8", "whenwhere", "Vans: the day with most accidents is…", "Furgonetas: el día con más siniestros es…",
  [("Friday, then Monday", "el viernes, seguido del lunes"), ("Sunday", "el domingo"), ("Wednesday", "el miércoles")],
  "Most common factor: driver distraction.", "Factor más habitual: las distracciones.")
Q("wh9", "whenwhere", "Vans on interurban roads are most often involved in…", "En vías interurbanas, las furgonetas sufren sobre todo…",
  [("rear-end and multiple collisions", "colisiones traseras y múltiples"), ("pedestrian accidents", "atropellos"), ("rollovers only", "solo vuelcos")],
  "In towns: side and front-side collisions.", "En ciudad: laterales y frontolaterales.")

# ---------------------------------------------------------------- 3. elderly
Q("el1", "elderly", "The main problem of older drivers is…", "El principal problema de los conductores mayores es…",
  [("the decline of their physical and mental abilities", "el deterioro de sus capacidades psicofísicas"), ("their lack of experience", "su falta de experiencia"), ("speeding", "el exceso de velocidad")],
  "Vision, hearing, reaction time, attention, strength.", "Visión, audición, tiempo de reacción, atención, fuerza.")
Q("el2", "elderly", "With age, the field of vision…", "Con la edad, el campo visual…",
  [("narrows, especially at night", "se estrecha, sobre todo de noche"), ("widens", "se amplía"), ("does not change", "no cambia")],
  "And dazzle becomes more likely.", "Y hay más deslumbramientos.")
Q("el3", "elderly", "Older drivers find it hardest to…", "A los conductores mayores les cuesta más…",
  [("respond in complex situations such as intersections", "responder en situaciones complejas, como intersecciones"), ("drive on a straight road", "circular por una recta"), ("park in a garage", "aparcar en un garaje")],
  "Their reaction time is longer.", "Aumenta su tiempo de reacción.")
Q("el4", "elderly", "Hearing loss in older drivers makes it harder to…", "La pérdida de audición en los mayores dificulta…",
  [("tell where a sound comes from", "localizar la procedencia de los sonidos"), ("see traffic lights", "ver los semáforos"), ("brake", "frenar")],
  "Also distinguishing sounds.", "También distinguir los sonidos.")
Q("el5", "elderly", "With older drivers, other drivers should…", "Con los conductores mayores, los demás deben…",
  [("be respectful and patient, especially in complex situations", "ser respetuosos y tolerantes, sobre todo en situaciones complejas"), ("use the horn to hurry them", "pitarles para que se den prisa"), ("overtake them quickly", "adelantarles rápido")],
  "Their reactions are slower.", "Sus reacciones son más lentas.")

# ---------------------------------------------------------------- 3. pedestrians
Q("pd1", "peds", "Where do most pedestrian accidents happen?", "¿Dónde se producen más atropellos?",
  [("In towns", "En ciudad"), ("On autopistas", "En autopistas"), ("On interurban roads", "En carretera")],
  "But on interurban roads they are more serious.", "Pero en carretera son más graves.")
Q("pd2", "peds", "Of the pedestrians killed, more than half die…", "De los peatones fallecidos, más de la mitad mueren…",
  [("in towns", "en ciudad"), ("on interurban roads", "en carretera"), ("on autovías", "en autovías")],
  "Even though the chance of dying is lower there, there are many more accidents.", "Aunque allí la probabilidad de morir es menor, hay muchos más atropellos.")
Q("pd3", "peds", "Pedestrians are hard to anticipate because they…", "Es difícil prever a los peatones porque…",
  [("have a larger zone of uncertainty", "tienen una zona de incertidumbre mayor"), ("always walk slowly", "siempre caminan despacio"), ("never cross", "nunca cruzan")],
  "They can change direction at any moment.", "Pueden cambiar de dirección en cualquier momento.")
Q("pd4", "peds", "Older pedestrians have more accidents…", "Las personas mayores tienen más atropellos…",
  [("when they are alone", "cuando van solas"), ("when they are with children", "cuando van con niños"), ("only at night", "solo de noche")],
  "When looking after children they take more care.", "Con niños a su cargo tienen más cuidado.")
Q("pd5", "peds", "A child hit by a car usually takes the impact on…", "Un niño atropellado suele recibir el impacto en…",
  [("the head or vital organs", "la cabeza o partes vitales"), ("the legs only", "solo las piernas"), ("the arms", "los brazos")],
  "Because they are shorter.", "Por su menor estatura.")
Q("pd6", "peds", "Most child pedestrians are hit…", "La mayoría de los atropellos a niños se producen…",
  [("when school ends", "al finalizar la jornada escolar"), ("early in the morning", "a primera hora de la mañana"), ("at night", "de noche")],
  "At the school exit.", "A la salida del colegio.")
Q("pd7", "peds", "Children under what age can’t tell where the noise of a vehicle comes from?", "¿Hasta qué edad los niños no distinguen de dónde viene el ruido de un vehículo?",
  [("7", "7 años"), ("12", "12 años"), ("3", "3 años")],
  "Under seven.", "Los menores de siete años.")
Q("pd8", "peds", "Between parked cars, a child’s field of vision can be smaller than an adult’s by up to…", "Entre coches aparcados, el campo visual de un niño puede ser menor que el de un adulto hasta en…",
  [("40 %", "un 40 %"), ("10 %", "un 10 %"), ("80 %", "un 80 %")],
  "And drivers find it harder to see them.", "Y a los conductores les cuesta más verlos.")
Q("pd9", "peds", "Children often confuse…", "Los niños suelen confundir…",
  [("seeing with being seen", "«ver» con «ser visto»"), ("red with green", "el rojo con el verde"), ("left with right", "la izquierda con la derecha")],
  "If they see a car they think the driver sees them.", "Si ven un coche creen que el conductor les ve.")
Q("pd10", "peds", "To avoid hitting pedestrians, you should NOT…", "Para evitar atropellos, NO se debe…",
  [("wave pedestrians across the road", "hacer señales a los peatones para que crucen"), ("slow down near a stopped school bus", "reducir la velocidad junto a un autobús escolar parado"), ("take care when reversing", "tener cuidado con la marcha atrás")],
  "It can lead them into danger from other vehicles.", "Puede llevarles a un peligro con otros vehículos.")
Q("pd11", "peds", "Why shouldn’t you modify the front of your car?", "¿Por qué no se deben modificar las partes delanteras del coche?",
  [("They are designed to reduce injuries to pedestrians", "Están diseñadas para reducir las lesiones a los peatones"), ("It is only an aesthetic rule", "Es solo una norma estética"), ("It raises fuel consumption", "Aumenta el consumo")],
  "Also: don’t park on the pavement.", "Tampoco aparcar sobre la acera.")
Q("pd12", "peds", "A pedestrian walks along an interurban road at night. They must wear…", "Un peatón camina de noche por una vía interurbana. Debe llevar…",
  [("a luminous or reflective element visible from 150 m", "un elemento luminoso o reflectante visible a 150 m"), ("nothing special", "nada especial"), ("a helmet", "un casco")],
  "On the carriageway or shoulder, or in poor visibility.", "Por la calzada o el arcén, o con poca visibilidad.")

# ---------------------------------------------------------------- 3. cyclists
Q("cy1", "cyclists", "Cyclist accidents happen mostly…", "Los accidentes de ciclistas ocurren sobre todo…",
  [("at weekends, especially in good weather", "en fin de semana, sobre todo con buen tiempo"), ("on rainy weekdays", "los días laborables de lluvia"), ("at night in winter", "de noche en invierno")],
  "On conventional roads, on straights and at intersections.", "En carreteras convencionales, en rectas e intersecciones.")
Q("cy2", "cyclists", "The most common cyclist accident is…", "El accidente más habitual de los ciclistas es…",
  [("a head-on or front-side collision with another vehicle", "el choque frontal o frontolateral con otro vehículo"), ("a fall on their own", "la caída en solitario"), ("hitting a pedestrian", "atropellar a un peatón")],
  "Then rear-end and side collisions.", "Seguido de alcances y choques laterales.")
Q("cy3", "cyclists", "In town, how far behind a cyclist in the same lane must a motor vehicle keep?", "En vía urbana, ¿qué distancia debe dejar un vehículo a motor con el ciclista que le precede en el mismo carril?",
  [("At least 5 m", "Al menos 5 m"), ("At least 1.5 m", "Al menos 1,5 m"), ("At least 50 m", "Al menos 50 m")],
  "1.5 m is the lateral gap when overtaking.", "1,5 m es la separación lateral al adelantar.")
Q("cy4", "cyclists", "Where should a cyclist ride in a town lane?", "¿Por dónde circulan preferentemente los ciclistas en un carril urbano?",
  [("Preferably in the centre of the lane", "Preferentemente por el centro del carril"), ("Always at the right edge", "Siempre por el borde derecho"), ("On the pavement", "Por la acera")],
  "As far as safety allows.", "En la medida en que lo permita su seguridad.")
Q("cy5", "cyclists", "May a cyclist ride on the pavement?", "¿Puede un ciclista circular por la acera?",
  [("No, except children under 12 with an adult on foot, if the town allows it", "No, salvo menores de 12 con un adulto a pie, si lo permite el ayuntamiento"), ("Yes, at walking pace", "Sí, al paso"), ("Yes, if there is no bike lane", "Sí, si no hay carril bici")],
  "Without a bike lane, cyclists use the carriageway.", "Sin carril bici, por la calzada.")
Q("cy6", "cyclists", "Overtaking a cyclist on an interurban road, you must slow down…", "Al adelantar a un ciclista en una vía interurbana hay que reducir la velocidad…",
  [("by at least 20 km/h below the limit", "al menos 20 km/h respecto al límite"), ("by 10 km/h", "en 10 km/h"), ("you may go 20 km/h above the limit", "se puede superar el límite en 20 km/h")],
  "And leave at least 1.5 m.", "Y dejar al menos 1,5 m.")
Q("cy7", "cyclists", "On a road with two lanes in your direction, to overtake a cyclist you must…", "En una calzada con dos carriles por sentido, para adelantar a un ciclista hay que…",
  [("change lane completely", "cambiar completamente de carril"), ("stay in the lane, 1.5 m away", "quedarse en el carril a 1,5 m"), ("sound the horn", "tocar el claxon")],
  "Plus the 1.5 m lateral gap.", "Además de la separación de 1,5 m.")
Q("cy8", "cyclists", "Since October 2026, the bicycle helmet on interurban roads is…", "Desde octubre de 2026, el casco en bicicleta en vías interurbanas es…",
  [("compulsory for every cyclist, with no exceptions", "obligatorio para todos, sin exenciones"), ("compulsory only for under-16s", "obligatorio solo para menores de 16"), ("recommended", "recomendable")],
  "The old exceptions (long climbs, heat) were removed.", "Se suprimieron las exenciones (rampas, calor).")
Q("cy9", "cyclists", "A delivery rider on a bicycle in town must wear…", "Un repartidor en bicicleta por ciudad debe llevar…",
  [("a helmet and a high-visibility vest", "casco y chaleco de alta visibilidad"), ("only a helmet out of town", "solo casco fuera de poblado"), ("nothing compulsory in town", "nada obligatorio en ciudad")],
  "Under-16s also need a helmet on all roads.", "Los menores de 16 también llevan casco en todas las vías.")
Q("cy10", "cyclists", "A cyclist on an interurban road at night must use…", "Un ciclista de noche por vía interurbana debe usar…",
  [("a luminous or reflective element visible from 150 m", "un elemento luminoso o reflectante visible a 150 m"), ("hazard lights", "luces de emergencia"), ("nothing extra", "nada más")],
  "Also in poor visibility.", "También con poca visibilidad.")
Q("cy11", "cyclists", "Near cyclists you should avoid…", "Cerca de ciclistas hay que evitar…",
  [("using the horn", "las señales acústicas"), ("slowing down", "reducir la velocidad"), ("keeping your distance", "guardar la distancia")],
  "It can startle them.", "Les puede asustar.")

# ---------------------------------------------------------------- 3. motorcycles
Q("mo1", "motos", "Compared with other vehicles, motorcycles and mopeds are…", "Frente a otros vehículos, motos y ciclomotores son…",
  [("less visible, less stable and more fragile", "menos visibles, menos estables y más frágiles"), ("more visible", "más visibles"), ("more stable", "más estables")],
  "Their accidents are easily fatal.", "Sus accidentes son fácilmente letales.")
Q("mo2", "motos", "One of the main reasons for the high death rate of motorcyclists is…", "Uno de los principales motivos de la alta mortalidad de los motoristas es…",
  [("not wearing a helmet", "no usar el casco"), ("riding in town", "circular por ciudad"), ("riding by day", "circular de día")],
  "It protects head and face.", "Protege cabeza y cara.")
Q("mo3", "motos", "The most common motorcycle accident is…", "El accidente más común de las motos es…",
  [("a head-on or front-side collision when overtaking", "la colisión frontal o frontolateral al adelantar"), ("a rear-end collision on the motorway", "el alcance en autopista"), ("hitting a pedestrian", "el atropello")],
  "Especially in towns.", "Sobre todo en vías urbanas.")
Q("mo4", "motos", "With a passenger, when the motorcycle brakes…", "Con pasajero, al frenar la moto…",
  [("the rear wheel is harder to lock and the stopping distance is longer", "es más difícil que se bloquee la rueda trasera y la detención es mayor"), ("it stops sooner", "se detiene antes"), ("nothing changes", "no cambia nada")],
  "The centre of gravity shifts.", "Se desplaza el centro de gravedad.")
Q("mo5", "motos", "Riding very slowly round a bend with the handlebar turned, you should not…", "Circulando muy despacio en curva con el manillar girado, no se debe…",
  [("use the front brake", "accionar el freno delantero"), ("use the rear brake", "accionar el freno trasero"), ("look ahead", "mirar hacia delante")],
  "You could fall.", "Posible caída.")
Q("mo6", "motos", "Since October 2026, motorcycle gloves are compulsory…", "Desde octubre de 2026, los guantes en moto son obligatorios…",
  [("on interurban roads, for rider and passenger", "en vías interurbanas, para conductor y pasajero"), ("only in winter", "solo en invierno"), ("only for the rider in town", "solo para el conductor en ciudad")],
  "Fine: 200 €.", "Multa: 200 €.")
Q("mo7", "motos", "Closed footwear on a motorcycle or moped is compulsory…", "El calzado cerrado en moto o ciclomotor es obligatorio…",
  [("on all roads", "en todo tipo de vías"), ("only on interurban roads", "solo en vías interurbanas"), ("never", "nunca")],
  "No sandals or flip-flops.", "Nada de sandalias ni chanclas.")
Q("mo8", "motos", "For an ordinary (non-professional) motorcyclist, the reflective vest while riding is…", "Para un motorista particular, el chaleco reflectante al circular es…",
  [("recommended, not compulsory", "recomendable, no obligatorio"), ("compulsory day and night", "obligatorio de día y de noche"), ("prohibited", "prohibido")],
  "But the bike must carry one, and delivery riders always wear it.", "Pero la moto debe llevarlo, y los profesionales lo usan siempre.")
Q("mo9", "motos", "If you fall off a motorcycle, you should try to…", "En caso de caída de la moto, hay que procurar…",
  [("slide along the ground as relaxed as possible", "deslizarse por el suelo lo más relajadamente posible"), ("get up immediately", "levantarse inmediatamente"), ("hold on to the motorcycle", "agarrarse a la moto")],
  "Until you stop.", "Hasta quedar detenido.")
Q("mo10", "motos", "The right posture on a motorcycle is…", "La postura correcta en moto es…",
  [("relaxed, arms slightly bent, gentle but firm grip", "suelta, con los brazos algo flexionados y agarre suave y firme"), ("leaning well forward with stiff arms", "muy inclinado con los brazos rígidos"), ("one hand on the handlebar", "una mano en el manillar")],
  "Avoid tension and stiffness.", "Evitar la fuerza y el agarrotamiento.")

# ---------------------------------------------------------------- 3. VMP
Q("vm1", "vmp", "The minimum age to ride an e-scooter (VMP) is…", "La edad mínima para conducir un patinete eléctrico (VMP) es…",
  [("15", "15 años"), ("14", "14 años"), ("18", "18 años")],
  "Since 1 October 2026.", "Desde el 1 de octubre de 2026.")
Q("vm2", "vmp", "A VMP rider must wear a helmet…", "El conductor de un VMP debe llevar casco…",
  [("always", "siempre"), ("only on interurban roads", "solo en vías interurbanas"), ("only if under 16", "solo si es menor de 16")],
  "Approved or certified, fastened.", "Homologado o certificado y abrochado.")
Q("vm3", "vmp", "May an e-scooter carry a passenger?", "¿Puede un patinete eléctrico llevar acompañante?",
  [("No, only the rider", "No, solo el conductor"), ("Yes, one child", "Sí, un niño"), ("Yes, with a helmet", "Sí, con casco")],
  "Solo conductor.", "Solo conductor.")
Q("vm4", "vmp", "The maximum speed of a VMP is…", "La velocidad máxima de un VMP es…",
  [("25 km/h", "25 km/h"), ("30 km/h", "30 km/h"), ("45 km/h", "45 km/h")],
  "A moped goes up to 45 km/h.", "Un ciclomotor llega a 45 km/h.")
Q("vm5", "vmp", "May a VMP ride on the pavement?", "¿Puede un VMP circular por la acera?",
  [("No, never", "No, nunca"), ("Yes, at walking pace", "Sí, al paso"), ("Yes, if the street is busy", "Sí, si hay mucho tráfico")],
  "Except a person with reduced mobility at walking pace, who counts as a pedestrian.", "Salvo la persona con movilidad reducida al paso, que es peatón.")
Q("vm6", "vmp", "VMP may not ride on…", "Los VMP no pueden circular por…",
  [("autovías, travesías and interurban roads", "autovías, travesías y vías interurbanas"), ("bike lanes", "carriles bici"), ("30 km/h streets", "calles a 30 km/h")],
  "Except cycle tracks and roads closed to motor traffic.", "Salvo vías ciclistas y vías cerradas a vehículos de motor.")
Q("vm7", "vmp", "How must a VMP rider warn of a manoeuvre?", "¿Cómo debe advertir un conductor de VMP de sus maniobras?",
  [("Always with the arm", "Siempre con el brazo"), ("With the horn", "Con el claxon"), ("They don’t need to", "No hace falta")],
  "As cyclists do.", "Como los ciclistas.")
Q("vm8", "vmp", "Which equipment must a VMP have?", "¿Qué equipamiento debe llevar un VMP?",
  [("Two independent brakes, lights, reflectors and a bell", "Dos frenos independientes, luces, catadióptricos y timbre"), ("Only a front light", "Solo luz delantera"), ("Indicators and a horn", "Intermitentes y bocina")],
  "White front light, red rear light.", "Luz blanca delante, roja detrás.")
Q("vm9", "vmp", "A person with reduced mobility rides a VMP at walking pace. They count as…", "Una persona con movilidad reducida va en VMP al paso de persona. Se considera…",
  [("a pedestrian", "peatón"), ("a cyclist", "ciclista"), ("a moped rider", "conductor de ciclomotor")],
  "So they may use the pavement.", "Por eso puede ir por la acera.")
Q("vm10", "vmp", "To ride a VMP you need…", "Para circular con un VMP hace falta…",
  [("registration, a certificate, the label and insurance", "inscripción, certificado, etiqueta y seguro"), ("only a licence", "solo un permiso"), ("nothing", "nada")],
  "Insurance has been compulsory since January 2026.", "El seguro es obligatorio desde enero de 2026.")
Q("vm11", "vmp", "A VMP sold in 2023 without a circulation certificate may be used…", "Un VMP vendido en 2023 sin certificado de circulación puede usarse…",
  [("until 21 January 2027, registered and insured", "hasta el 21 de enero de 2027, inscrito y asegurado"), ("forever", "para siempre"), ("not at all", "en ningún caso")],
  "From 22 January 2027 only certified VMP.", "Desde el 22 de enero de 2027, solo los certificados.")

# ---------------------------------------------------------------- 3. young drivers
Q("yg1", "young", "Young drivers are considered…", "Los conductores jóvenes se consideran…",
  [("a risk group, not vulnerable users", "grupo de riesgo, no usuarios vulnerables"), ("vulnerable users", "usuarios vulnerables"), ("the safest group", "el grupo más seguro")],
  "Because of their high accident rate.", "Por su alta siniestralidad.")
Q("yg2", "young", "Road accidents are the main cause of injury and death for people aged…", "Los accidentes son la principal causa de lesiones y muerte entre los…",
  [("15 to 29", "15 y 29 años"), ("30 to 45", "30 y 45 años"), ("over 65", "mayores de 65")],
  "Almost 35 % of deaths.", "Casi el 35 % de las víctimas mortales.")
Q("yg3", "young", "The risk for young people rises from age 14–15 because…", "El riesgo de los jóvenes aumenta a partir de los 14–15 años porque…",
  [("that is when the first moped riders appear", "aparecen los primeros conductores de ciclomotores"), ("they start school", "empiezan el colegio"), ("they get the B licence", "obtienen el permiso B")],
  "AM licence from 15.", "Permiso AM desde los 15.")
Q("yg4", "young", "Young drivers’ accidents happen above all…", "Los accidentes de los jóvenes se producen sobre todo…",
  [("at night, at weekends, going out with alcohol and several occupants", "de noche, en fin de semana, en ocio con alcohol y varios ocupantes"), ("on weekday mornings", "las mañanas laborables"), ("alone, in good weather", "solos y con buen tiempo")],
  "Also Christmas and summer.", "También en Navidad y verano.")
Q("yg5", "young", "Which is NOT one of the causes of young drivers’ accidents in your course?", "¿Cuál NO es una de las causas de los accidentes de jóvenes según tu curso?",
  [("Their slow reaction time", "Su lento tiempo de reacción"), ("Lack of experience", "Falta de experiencia"), ("Alcohol and drugs", "Alcohol y drogas")],
  "Causes: inexperience, speed, rule-breaking, alcohol and drugs.", "Causas: falta de experiencia, velocidad, incumplir normas, alcohol y drogas.")
Q("yg6", "young", "In a group, young drivers tend to…", "En grupo, los conductores jóvenes tienden a…",
  [("show off and take more risks", "exhibirse y arriesgar más"), ("drive more slowly", "conducir más despacio"), ("be more careful", "ser más prudentes")],
  "They risk more when accompanied.", "Arriesgan más cuando van acompañados.")
Q("yg7", "young", "Young drivers often think that mistakes…", "Los jóvenes suelen pensar que los errores…",
  [("are always made by others", "siempre los cometen los demás"), ("are always their own", "siempre son suyos"), ("don’t matter", "no importan")],
  "And they overestimate their ability.", "Y sobrevaloran su capacidad.")

# ---------------------------------------------------------------- 4. factors
Q("fa1", "factors", "The human factor is involved in…", "El factor humano interviene en…",
  [("70–90 % of accidents", "el 70–90 % de los accidentes"), ("10–35 %", "el 10–35 %"), ("4–13 %", "el 4–13 %")],
  "It is the main cause.", "Es el principal responsable.")
Q("fa2", "factors", "The road factor is involved in…", "El factor vía interviene en…",
  [("10–35 % of accidents", "el 10–35 % de los accidentes"), ("70–90 %", "el 70–90 %"), ("4–13 %", "el 4–13 %")],
  "The second factor.", "El segundo factor.")
Q("fa3", "factors", "Which factor has the least influence on accidents?", "¿Qué factor influye menos en los accidentes?",
  [("The vehicle (4–13 %)", "El vehículo (4–13 %)"), ("The road", "La vía"), ("The driver", "El conductor")],
  "It rises with poor maintenance.", "Aumenta con un mantenimiento deficiente.")
Q("fa4", "factors", "Which is a frequent cause of accidents due to the driver?", "¿Cuál es una causa frecuente de accidentes por el conductor?",
  [("Distraction or lack of attention", "Distracciones o falta de atención"), ("A worn tyre", "Un neumático gastado"), ("Fog", "La niebla")],
  "Also safety distance, speed, priority, turns, overtaking.", "También distancia, velocidad, prioridad, giros, adelantamientos.")
Q("fa5", "factors", "A driver’s ability depends on…", "La capacidad del conductor depende de…",
  [("training and experience", "la formación y la experiencia"), ("the car’s power", "la potencia del coche"), ("the time of day", "la hora del día")],
  "And you must adapt to what driving demands.", "Y hay que adaptarse al nivel exigido.")

# ---------------------------------------------------------------- 4. speed
Q("sp1", "speed", "As speed increases, the field of vision…", "Al aumentar la velocidad, el campo visual…",
  [("narrows: the tunnel effect", "disminuye: efecto túnel"), ("widens", "aumenta"), ("does not change", "no cambia")],
  "Only the centre of the road is seen sharply.", "Solo se ve con nitidez el centro de la vía.")
Q("sp2", "speed", "The tunnel effect is especially dangerous…", "El efecto túnel es especialmente peligroso…",
  [("at intersections and with sideways movements", "en intersecciones y desplazamientos laterales"), ("on long straights", "en rectas largas"), ("when stopped", "parado")],
  "Side images pass too fast.", "Las imágenes laterales pasan muy rápido.")
Q("sp3", "speed", "The stopping distance is…", "La distancia de detención es…",
  [("the reaction distance plus the braking distance", "la distancia de reacción más la de frenado"), ("the braking distance only", "solo la distancia de frenado"), ("the safety distance", "la distancia de seguridad")],
  "From seeing the obstacle to stopping.", "Desde que se ve el obstáculo hasta que se para.")
Q("sp4", "speed", "In normal conditions, a typical reaction time is…", "En condiciones normales, el tiempo de reacción habitual es…",
  [("0.75 seconds", "0,75 segundos"), ("3 seconds", "3 segundos"), ("0.1 seconds", "0,1 segundos")],
  "Between half a second and one second.", "Entre medio y un segundo.")
Q("sp5", "speed", "Which of these does NOT lengthen the reaction time?", "¿Cuál de estos NO aumenta el tiempo de reacción?",
  [("A dry road", "Una calzada seca"), ("Fatigue", "La fatiga"), ("Heat or too much heating", "El calor o exceso de calefacción")],
  "Also age, alcohol, drugs, medicines, stress.", "También edad, alcohol, drogas, medicamentos, estrés.")
Q("sp6", "speed", "The reaction distance is what the vehicle travels…", "La distancia de reacción es la que recorre el vehículo…",
  [("during the reaction time", "durante el tiempo de reacción"), ("while braking", "mientras frena"), ("after stopping", "después de parar")],
  "It grows with speed.", "Aumenta con la velocidad.")
Q("sp7", "speed", "On a wet road, the braking distance can…", "Con lluvia, la distancia de frenado puede…",
  [("double", "duplicarse"), ("halve", "reducirse a la mitad"), ("stay the same", "seguir igual")],
  "On snow or ice, ×10.", "Con nieve o hielo, ×10.")
Q("sp8", "speed", "On snow or ice the braking distance is multiplied by about…", "Con nieve o hielo, la distancia de frenado se multiplica por…",
  [("10", "10"), ("2", "2"), ("4", "4")],
  "Rain ×2.", "Lluvia ×2.")
Q("sp9", "speed", "Carrying a passenger on a motorcycle makes the braking distance…", "Llevar un pasajero en la moto hace que la distancia de frenado…",
  [("longer", "aumente"), ("shorter", "disminuya"), ("the same", "sea la misma")],
  "More mass.", "Más masa.")
Q("sp10", "speed", "Driving fast for a long time on a wide road, you tend to feel…", "Conduciendo mucho tiempo deprisa por una vía amplia, se tiene la sensación de…",
  [("you are going slower than you are", "ir más despacio de lo que se va"), ("you are going faster than you are", "ir más deprisa de lo que se va"), ("more rested", "estar más descansado")],
  "Take care when entering towns.", "Cuidado en los accesos a las ciudades.")
Q("sp11", "speed", "What share of the information needed to drive is visual?", "¿Qué parte de la información necesaria para conducir es visual?",
  [("90 %", "El 90 %"), ("50 %", "El 50 %"), ("25 %", "El 25 %")],
  "So anything that harms vision is dangerous.", "Por eso todo lo que afecta a la vista es peligroso.")
Q("sp12", "speed", "To avoid an accident, your speed must let you stop…", "Para evitar un accidente, la velocidad debe permitir detenerse…",
  [("in less distance than there is to the obstacle", "en menos distancia de la que hay hasta el obstáculo"), ("in exactly 2 seconds", "en exactamente 2 segundos"), ("within 100 m", "en 100 m")],
  "Stopping distance < distance to the obstacle.", "Distancia de detención < distancia al obstáculo.")

# ---------------------------------------------------------------- 4. fatigue and sleep
Q("ft1", "fatigue", "The main cause of fatigue at the wheel is…", "La principal causa de fatiga al volante es…",
  [("driving for long periods without proper breaks", "conducir largos periodos sin descansar o descansando mal"), ("driving in the city", "conducir en ciudad"), ("driving a new car", "conducir un coche nuevo")],
  "Also bad posture, speed, illness, stress.", "También postura, velocidad, enfermedad, estrés.")
Q("ft2", "fatigue", "The recommended temperature inside the car is…", "La temperatura recomendada en el habitáculo es…",
  [("20–23 °C", "20–23 °C"), ("15–17 °C", "15–17 °C"), ("25–28 °C", "25–28 °C")],
  "Without blowing air at the eyes.", "Sin dirigir el aire a los ojos.")
Q("ft3", "fatigue", "Fatigue makes the reaction time…", "La fatiga hace que el tiempo de reacción…",
  [("longer", "aumente"), ("shorter", "disminuya"), ("the same", "no cambie")],
  "And driving more passive and automatic.", "Y la conducción más pasiva y automatizada.")
Q("ft4", "fatigue", "To reduce fatigue on a trip, stop…", "Para reducir la fatiga en un viaje, hay que parar…",
  [("at least every 2 hours or 200 km, for 20–30 minutes", "como mínimo cada 2 horas o 200 km, 20–30 minutos"), ("every 5 hours", "cada 5 horas"), ("only when you feel sleepy", "solo al tener sueño")],
  "More often if you feel tired.", "Más a menudo si hay cansancio.")
Q("ft5", "fatigue", "Driving while sleepy causes about what share of accidents?", "¿Qué parte de los accidentes causa la conducción con sueño?",
  [("15–30 %", "Entre el 15 y el 30 %"), ("1–2 %", "El 1–2 %"), ("50–60 %", "El 50–60 %")],
  "And they tend to be serious.", "Y suelen ser graves.")
Q("ft6", "fatigue", "To have an accident caused by sleep, you…", "Para tener un accidente por sueño…",
  [("don’t need to fall asleep", "no hace falta llegar a dormirse"), ("must fall asleep", "hay que dormirse"), ("must be driving at night", "hay que conducir de noche")],
  "Drowsiness risks start much earlier, by day too.", "Los riesgos aparecen mucho antes, también de día.")
Q("ft7", "fatigue", "A ‘microsleep’ is…", "Un «microsueño» es…",
  [("a few seconds asleep without realising it", "unos segundos dormido sin darse cuenta"), ("a 20-minute nap", "una siesta de 20 minutos"), ("a yawn", "un bostezo")],
  "Very dangerous at the wheel.", "Muy peligroso al volante.")
Q("ft8", "fatigue", "The times of day with most drowsiness are…", "Las horas del día de más somnolencia son…",
  [("3–5 h and 14–16 h", "de 3 a 5 y de 14 a 16"), ("8–10 h and 18–20 h", "de 8 a 10 y de 18 a 20"), ("12–13 h only", "solo de 12 a 13")],
  "Early hours and early afternoon.", "Madrugada y primeras horas de la tarde.")
Q("ft9", "fatigue", "How much sleep is considered right?", "¿Cuánto sueño se considera adecuado?",
  [("7–9 hours of deep sleep", "7–9 horas de sueño profundo"), ("4–5 hours", "4–5 horas"), ("12 hours", "12 horas")],
  "Sleeping badly is as dangerous as sleeping little.", "Dormir mal es tan peligroso como dormir poco.")
Q("ft10", "fatigue", "Tea or coffee to stay awake…", "El té o el café para no dormirse…",
  [("have a rebound effect: sleep comes suddenly when they wear off", "tienen efecto rebote: el sueño aparece de golpe al pasar su efecto"), ("remove sleepiness for the whole trip", "eliminan el sueño todo el viaje"), ("are the best solution", "son la mejor solución")],
  "The real solution is to stop and rest.", "La solución es parar y descansar.")
Q("ft11", "fatigue", "Which sleep disorder legally prevents getting a driving licence?", "¿Qué trastorno del sueño impide legalmente obtener el permiso?",
  [("Narcolepsy", "La narcolepsia"), ("Occasional insomnia", "El insomnio ocasional"), ("Snoring", "Roncar")],
  "Insomnia can cause daytime sleepiness.", "El insomnio puede causar somnolencia diurna.")
Q("ft12", "fatigue", "Rumble strips (GSLF) warn the driver by…", "Las guías sonoras (GSLF) avisan al conductor mediante…",
  [("noise and vibration", "sonido y vibración"), ("flashing lights", "luces intermitentes"), ("a message on the dashboard", "un mensaje en el salpicadero")],
  "Of an unintended lane departure.", "Del abandono involuntario del carril.")
Q("ft13", "fatigue", "Which situation most favours drowsiness?", "¿Qué situación favorece más la somnolencia?",
  [("Driving at night on an empty motorway", "Conducir de noche por autovía sin tráfico"), ("Driving in town traffic", "Conducir en tráfico urbano"), ("Driving a short trip in the morning", "Un trayecto corto por la mañana")],
  "Monotony brings on sleep.", "La monotonía favorece el sueño.")

# ---------------------------------------------------------------- 4. illness, medicines, heat
Q("hl1", "health", "A driver with a chronic illness should…", "Un conductor con una enfermedad crónica debe…",
  [("know the side effects of their medicines and not drink alcohol with them", "conocer los efectos secundarios de sus medicamentos y no tomar alcohol con ellos"), ("stop taking their medicines to drive", "dejar la medicación para conducir"), ("drive only at night", "conducir solo de noche")],
  "And recognise the first symptoms of a crisis.", "Y reconocer los primeros síntomas de una crisis.")
Q("hl2", "health", "Which antihistamines cause the most drowsiness?", "¿Qué antihistamínicos producen más somnolencia?",
  [("First-generation ones", "Los de primera generación"), ("Third-generation ones", "Los de tercera generación"), ("None", "Ninguno")],
  "Third generation: safer, but never with alcohol.", "Tercera generación: más seguros, pero nunca con alcohol.")
Q("hl3", "health", "A driver with an allergy should…", "Un conductor con alergia debe…",
  [("keep the windows closed and not self-medicate", "no abrir las ventanillas y no automedicarse"), ("drive at dawn", "conducir al amanecer"), ("turn the air conditioning to maximum", "poner el aire acondicionado al máximo")],
  "Also sunglasses and a clean interior.", "También gafas de sol y habitáculo limpio.")
Q("hl4", "health", "Stress at the wheel tends to…", "El estrés al volante tiende a…",
  [("increase aggression and acceptance of risk", "aumentar la agresividad y la aceptación del riesgo"), ("improve concentration", "mejorar la concentración"), ("shorten the reaction time", "reducir el tiempo de reacción")],
  "And more distractions and fatigue.", "Y más distracciones y fatiga.")
Q("hl5", "health", "A driver with depression should…", "Un conductor con depresión debe…",
  [("see a specialist before driving and avoid the most acute phase", "consultar a un especialista antes de conducir y evitar la fase más aguda"), ("drive more to distract themselves", "conducir más para distraerse"), ("take alcohol to relax", "tomar alcohol para relajarse")],
  "Some psychotropics forbid driving.", "Algunos psicofármacos impiden conducir.")
Q("hl6", "health", "The pictogram “Conducción: ver prospecto” on a medicine box…", "El pictograma «Conducción: ver prospecto» en la caja de un medicamento…",
  [("warns you to read the leaflet; it does not forbid driving", "advierte de leer el prospecto; no prohíbe conducir"), ("forbids driving", "prohíbe conducir"), ("means the medicine is safe to drive", "indica que es seguro para conducir")],
  "The leaflet lists effects that may affect driving.", "El prospecto describe los efectos que pueden afectar a la conducción.")
Q("hl7", "health", "When is it most advisable not to drive (or be very careful) with a medicine?", "¿Cuándo es más aconsejable no conducir (o extremar la prudencia) con un medicamento?",
  [("At the start of the treatment", "Al inicio del tratamiento"), ("After a month", "Al cabo de un mes"), ("Never", "Nunca")],
  "Not everyone reacts the same.", "No todas las personas reaccionan igual.")
Q("hl8", "health", "Natural or alternative remedies…", "Las medicinas naturales o alternativas…",
  [("can also have negative effects on driving", "también pueden tener efectos negativos en la conducción"), ("never affect driving", "nunca afectan a la conducción"), ("cancel alcohol’s effects", "anulan los efectos del alcohol")],
  "Read the leaflet and ask.", "Consultar el prospecto y preguntar.")
Q("hl9", "health", "Heat makes the reaction time…", "El calor hace que el tiempo de reacción…",
  [("longer", "aumente"), ("shorter", "disminuya"), ("unchanged", "no varíe")],
  "More mistakes, fatigue and aggression.", "Más errores, fatiga y agresividad.")
Q("hl10", "health", "To reduce the risks of heat you should…", "Para reducir los riesgos del calor hay que…",
  [("stop more often and drink water or juice", "hacer más paradas y beber agua o zumos"), ("eat a big hot meal before leaving", "comer caliente y abundante antes de salir"), ("park in the sun", "aparcar al sol")],
  "And air conditioning at 20–23 °C.", "Y climatización a 20–23 °C.")
Q("hl11", "health", "Mixing medicines with alcohol…", "Mezclar medicamentos y alcohol…",
  [("must be avoided", "debe evitarse"), ("is safe in small amounts", "es seguro en poca cantidad"), ("reduces side effects", "reduce los efectos secundarios")],
  "Also don’t mix medicines without medical advice.", "Tampoco mezclar medicamentos sin indicación médica.")

# ---------------------------------------------------------------- 4. distractions
Q("ph1", "distract", "Which risk factor has grown the most in the last decade?", "¿Qué factor de riesgo más ha aumentado en la última década?",
  [("Distractions", "Las distracciones"), ("Alcohol", "El alcohol"), ("Worn tyres", "Los neumáticos gastados")],
  "Behind one in three fatal accidents.", "Causa uno de cada tres accidentes mortales.")
Q("ph2", "distract", "Using the phone at the wheel, the most frequent accident is…", "Por el uso del móvil, el accidente más frecuente es…",
  [("running off the road", "la salida de la vía"), ("a pedestrian accident", "el atropello"), ("a collision at a roundabout", "la colisión en una glorieta")],
  "Swerving and poor handling.", "Desviaciones de la trayectoria.")
Q("ph3", "distract", "After a minute and a half on the phone, how many signs are missed?", "Al minuto y medio de usar el móvil, ¿qué parte de las señales se deja de percibir?",
  [("40 %", "El 40 %"), ("10 %", "El 10 %"), ("90 %", "El 90 %")],
  "And the average speed drops 12 %.", "Y la velocidad media baja un 12 %.")
Q("ph4", "distract", "Talking on the phone while driving is compared to driving with…", "Hablar por el móvil conduciendo se compara con conducir con…",
  [("1 g/l of alcohol in the blood", "1 g/l de alcohol en sangre"), ("0.1 g/l of alcohol", "0,1 g/l de alcohol"), ("no effect at all", "ningún efecto")],
  "Even hands-free reduces attention.", "Incluso con manos libres se reduce la atención.")
Q("ph5", "distract", "Which moment of a phone call is NOT among the most dangerous?", "¿Qué momento NO está entre los más peligrosos de una llamada?",
  [("When the phone is switched off in the glovebox", "Con el móvil apagado en la guantera"), ("Answering", "Al recibir la llamada"), ("Hanging up", "Al colgar")],
  "Also dialling or texting, and talking.", "También marcar o escribir y mientras se habla.")
Q("ph6", "distract", "Using the phone by hand while stopped at a red light is…", "Usar el móvil con la mano detenido en un semáforo en rojo…",
  [("prohibited", "está prohibido"), ("allowed", "está permitido"), ("allowed for under a minute", "se permite menos de un minuto")],
  "Held in the hand: 6 points and 200 €.", "Sujetándolo con la mano: 6 puntos y 200 €.")
Q("ph7", "distract", "With a hands-free kit, your course recommends…", "Con manos libres, tu curso recomienda…",
  [("telling the caller you are driving and not talking for over a minute", "decir que conduces y no hablar más de un minuto"), ("long calls only on motorways", "llamadas largas solo en autovía"), ("nothing: it is completely safe", "nada: es totalmente seguro")],
  "Better: stop somewhere safe.", "Mejor: parar en un lugar seguro.")
Q("ph8", "distract", "Distractions are more frequent among…", "Las distracciones son más frecuentes entre…",
  [("drivers aged 18–25 and over 70", "los jóvenes de 18 a 25 años y los mayores de 70"), ("drivers aged 40–50", "los de 40 a 50 años"), ("professional drivers only", "solo los profesionales")],
  "Also with company and on leisure trips.", "También acompañados y en trayectos de ocio.")
Q("ph9", "distract", "When using a sat-nav, which takes priority?", "Usando un navegador, ¿qué debe prevalecer?",
  [("The driver’s own judgement", "El juicio del conductor"), ("The sat-nav’s route", "La ruta del navegador"), ("The fastest route", "La ruta más rápida")],
  "Plan before leaving and use voice guidance.", "Planificar antes y usar las instrucciones de voz.")
Q("ph10", "distract", "A portable sat-nav must never be placed…", "Un navegador portátil nunca debe colocarse…",
  [("near the airbag", "cerca del airbag"), ("on a proper mount", "en un soporte adecuado"), ("where it doesn’t block the view", "donde no entorpezca la visión")],
  "Very dangerous for driver and passenger.", "Muy peligroso para conductor y acompañante.")
Q("ph11", "distract", "The main reference for your speed should be…", "La principal fuente de información de la velocidad debe ser…",
  [("the speedometer", "el velocímetro"), ("the sat-nav", "el navegador"), ("the traffic around you", "el tráfico de alrededor")],
  "The sat-nav can help, but the speedometer comes first.", "El navegador ayuda, pero manda el velocímetro.")
Q("ph12", "distract", "Smoking while driving is…", "Fumar mientras se conduce…",
  [("not prohibited, but not recommended", "no está prohibido, pero no se recomienda"), ("prohibited", "está prohibido"), ("recommended to stay alert", "se recomienda para estar alerta")],
  "CO lowers attention and you lose one hand.", "El CO disminuye la atención y se pierde una mano.")

# ---------------------------------------------------------------- 4. alcohol
Q("al1", "alcohol", "Alcohol acts on the central nervous system as…", "El alcohol actúa sobre el sistema nervioso central como…",
  [("a depressant, after an initial euphoric phase", "depresor, tras una fase euforizante inicial"), ("a stimulant", "estimulante"), ("it has no effect", "no le afecta")],
  "False sense of safety and control.", "Falsa sensación de seguridad y control.")
Q("al2", "alcohol", "The general alcohol limit in exhaled air (cyclists and VMP included) is…", "La tasa general en aire espirado (también ciclistas y VMP) es…",
  [("0.25 mg/l", "0,25 mg/l"), ("0.15 mg/l", "0,15 mg/l"), ("0.50 mg/l", "0,50 mg/l")],
  "In blood: 0.5 g/l.", "En sangre: 0,5 g/l.")
Q("al3", "alcohol", "A driver who got their licence a year ago may have at most…", "Un conductor con el permiso desde hace un año puede tener como máximo…",
  [("0.15 mg/l in air (0.3 g/l in blood)", "0,15 mg/l en aire (0,3 g/l en sangre)"), ("0.25 mg/l in air", "0,25 mg/l en aire"), ("0.0 mg/l", "0,0 mg/l")],
  "Same for professional drivers.", "Igual que los profesionales.")
Q("al4", "alcohol", "A 17-year-old moped rider may have…", "Un conductor de ciclomotor de 17 años puede tener…",
  [("no alcohol at all (0.0)", "ninguna tasa (0,0)"), ("up to 0.15 mg/l", "hasta 0,15 mg/l"), ("up to 0.25 mg/l", "hasta 0,25 mg/l")],
  "Under-18 drivers: 0.0, on any vehicle.", "Menores de edad: 0,0, en cualquier vehículo.")
Q("al5", "alcohol", "The only truly safe blood alcohol level is…", "La única tasa realmente segura es…",
  [("0.0 g/l", "0,0 g/l"), ("0.3 g/l", "0,3 g/l"), ("0.5 g/l", "0,5 g/l")],
  "Below the limit you can still crash.", "Por debajo del límite también se puede tener un accidente.")
Q("al6", "alcohol", "Which trick lowers the breathalyser reading?", "¿Qué truco baja el resultado del etilómetro?",
  [("None of them", "Ninguno"), ("Drinking a lot of water", "Beber mucha agua"), ("Chewing gum or coffee", "Chicle o café")],
  "Exercise, oil, sprays, a nap… nothing works.", "Ejercicio, aceite, sprays, dormir… nada funciona.")
Q("al7", "alcohol", "Blood alcohol reaches its highest level…", "La tasa de alcohol alcanza su máximo…",
  [("30–90 minutes after drinking", "entre 30 y 90 minutos después de beber"), ("5 minutes after drinking", "a los 5 minutos"), ("the next day", "al día siguiente")],
  "It appears after 5 min and falls slowly.", "Aparece a los 5 min y baja despacio.")
Q("al8", "alcohol", "The most important factor in the alcohol level reached is…", "El factor más importante en la tasa alcanzada es…",
  [("the quantity drunk", "la cantidad que se toma"), ("the colour of the drink", "el color de la bebida"), ("the time of year", "la época del año")],
  "Then time, speed, type, food.", "Después tiempo, rapidez, tipo, comida.")
Q("al9", "alcohol", "Compared with distilled drinks, fermented ones (beer, wine) are absorbed…", "Frente a las destiladas, las bebidas fermentadas (cerveza, vino) se absorben…",
  [("more slowly", "más lentamente"), ("faster", "más rápido"), ("the same", "igual")],
  "Fizzy or hot drinks act faster.", "Las gaseosas o calientes, más rápido.")
Q("al10", "alcohol", "Drinking on an empty stomach makes alcohol pass into the blood…", "En ayunas, el alcohol pasa a la sangre…",
  [("faster, giving a higher level", "más rápido, con mayor tasa"), ("more slowly", "más despacio"), ("not at all", "no pasa")],
  "Food slows absorption.", "La comida frena la absorción.")
Q("al11", "alcohol", "Alcohol affects more…", "El alcohol afecta más…",
  [("slim people, women, the young and the elderly", "a delgados, mujeres, jóvenes y mayores"), ("heavier people", "a las personas corpulentas"), ("experienced drivers", "a los conductores con experiencia")],
  "Under 18 and over 65; inexperienced drivers.", "Menores de 18 y mayores de 65; conductores con poca experiencia.")
Q("al12", "alcohol", "During sleep, alcohol is eliminated…", "Durante el sueño, el alcohol se elimina…",
  [("more slowly", "más lentamente"), ("faster", "más deprisa"), ("completely in an hour", "por completo en una hora")],
  "A night’s sleep may not be enough.", "Una noche de sueño puede no bastar.")
Q("al13", "alcohol", "Alcohol can cause…", "El alcohol puede provocar…",
  [("tunnel vision and more sensitivity to dazzle", "visión túnel y más sensibilidad al deslumbramiento"), ("better coordination", "mejor coordinación"), ("longer attention span", "más atención")],
  "And misjudged distances.", "Y errores al calcular distancias.")

# ---------------------------------------------------------------- 4. drugs and the law
Q("dg1", "drugslaw", "Driving with drugs in the body is prohibited…", "Conducir con drogas en el organismo está prohibido…",
  [("for all drivers, cyclists and VMP riders included", "a todos los conductores, incluidos ciclistas y VMP"), ("only for car drivers", "solo a los conductores de coche"), ("only above a certain level", "solo por encima de una tasa")],
  "Except prescribed treatment that doesn’t affect driving.", "Salvo tratamiento prescrito que no afecte a la conducción.")
Q("dg2", "drugslaw", "Which drug typically causes aggressive, competitive behaviour and overconfidence?", "¿Qué droga provoca típicamente conductas agresivas, competitivas y sobrevaloración?",
  [("Cocaine", "La cocaína"), ("Cannabis", "El cannabis"), ("LSD", "El LSD")],
  "Amphetamines too.", "También las anfetaminas.")
Q("dg3", "drugslaw", "Cannabis typically…", "El cannabis típicamente…",
  [("distorts time and space and lengthens the reaction time", "altera el tiempo y el espacio y aumenta el tiempo de reacción"), ("improves concentration", "mejora la concentración"), ("has no effect on driving", "no afecta a la conducción")],
  "Also drowsiness.", "También somnolencia.")
Q("dg4", "drugslaw", "Amphetamines hide fatigue, but then…", "Las anfetaminas ocultan la fatiga, pero después…",
  [("sleep returns with a rebound effect", "el sueño reaparece con efecto rebote"), ("you never feel tired again", "ya no se siente cansancio"), ("you become calmer", "uno se tranquiliza")],
  "False security and impulsive behaviour.", "Falsa seguridad y comportamientos impulsivos.")
Q("dg5", "drugslaw", "LSD effects can last…", "Los efectos del LSD pueden durar…",
  [("10–12 hours", "10 o 12 horas"), ("10 minutes", "10 minutos"), ("1 hour", "1 hora")],
  "Flashbacks are possible.", "Puede haber flashbacks.")
Q("dg6", "drugslaw", "Who can be asked to take an alcohol test at a preventive check?", "¿A quién se le puede pedir la prueba de alcoholemia en un control preventivo?",
  [("Any driver, including cyclists and VMP riders", "A cualquier conductor, incluidos ciclistas y VMP"), ("Only drivers who commit an offence", "Solo a quien comete una infracción"), ("Only professional drivers", "Solo a los profesionales")],
  "Also anyone involved in an accident or with symptoms.", "También a implicados en accidentes o con síntomas.")
Q("dg7", "drugslaw", "Drug tests at the roadside are done with…", "Las pruebas de drogas en carretera se hacen con…",
  [("a saliva test, then a lab analysis", "una prueba salival y su posterior análisis"), ("a breathalyser", "un etilómetro"), ("a blood sample on the spot", "una extracción de sangre in situ")],
  "Alcohol: exhaled air with breathalysers.", "Alcohol: aire espirado con etilómetros.")
Q("dg8", "drugslaw", "Between the first and the second breath test there must be at least…", "Entre la primera y la segunda prueba debe haber al menos…",
  [("10 minutes", "10 minutos"), ("1 minute", "1 minuto"), ("1 hour", "1 hora")],
  "The person, companions or witnesses may check it.", "Lo puede controlar el examinado, sus acompañantes o testigos.")
Q("dg9", "drugslaw", "A contrast blood test requested by the driver is…", "El análisis de sangre de contraste que pide el conductor…",
  [("paid in advance by them, refunded if negative", "lo paga antes el interesado y se le devuelve si es negativo"), ("always free", "es siempre gratuito"), ("always paid by the police", "lo paga siempre la policía")],
  "Charged to them if positive.", "Corre a su cargo si es positivo.")
Q("dg10", "drugslaw", "Agents may immobilise the vehicle when…", "Los agentes pueden inmovilizar el vehículo cuando…",
  [("the test is positive or the driver refuses it", "la prueba es positiva o el conductor se niega"), ("the driver is tired", "el conductor está cansado"), ("the test is negative", "la prueba es negativa")],
  "Unless another qualified person can drive.", "Salvo que pueda conducir otra persona habilitada.")
Q("dg11", "drugslaw", "Who pays the costs of immobilising and towing the vehicle?", "¿Quién paga los gastos de inmovilización y traslado?",
  [("The driver, or whoever is legally responsible", "El conductor o quien deba responder por él"), ("The police", "La policía"), ("The insurer always", "Siempre el seguro")],
  "Also the storage.", "También el depósito.")
Q("dg12", "drugslaw", "A positive drug test carries…", "Un positivo en drogas conlleva…",
  [("a 1,000 € fine and 6 points", "multa de 1.000 € y 6 puntos"), ("a 200 € fine and no points", "multa de 200 € sin puntos"), ("only a warning", "solo un aviso")],
  "Alcohol: 500 € and 4 points, or 1,000 € and 6 points.", "Alcohol: 500 € y 4 puntos, o 1.000 € y 6 puntos.")

# ---------------------------------------------------------------- 4. position and controls
Q("ct1", "controls", "The seat is well adjusted when you can press the pedals all the way down with…", "El asiento está bien regulado si se pisan a fondo los pedales con…",
  [("your legs slightly bent", "las piernas ligeramente flexionadas"), ("your legs straight", "las piernas estiradas"), ("your body leaning forward", "el cuerpo inclinado hacia delante")],
  "Without moving the body forward.", "Sin desplazar el cuerpo.")
Q("ct2", "controls", "Sitting too close to the steering wheel…", "Ir demasiado cerca del volante…",
  [("causes fatigue and can be dangerous with the airbag", "produce fatiga y puede ser peligroso por el airbag"), ("improves control", "mejora el control"), ("is recommended in town", "se recomienda en ciudad")],
  "Too far: slow reactions, passive safety works worse.", "Muy lejos: reacciones lentas y peor seguridad pasiva.")
Q("ct3", "controls", "After adjusting the seat and backrest, you adjust…", "Tras regular el asiento y el respaldo, se regulan…",
  [("the head restraint, mirrors and seat belt", "el reposacabezas, los espejos y el cinturón"), ("the radio", "la radio"), ("nothing else", "nada más")],
  "Before starting the engine.", "Antes de arrancar.")
Q("ct4", "controls", "The hands on the steering wheel go…", "Las manos en el volante van…",
  [("on the outside, at ten to two or quarter to three", "por el exterior, a las 2 menos 10 o las 3 menos cuarto"), ("both at the top", "las dos arriba"), ("one at the bottom", "una abajo")],
  "Never cross your hands to turn.", "Para girar, no cruzarlas.")
Q("ct5", "controls", "Low (short) gears give…", "Las marchas cortas tienen…",
  [("more force but less speed", "más fuerza pero menos velocidad"), ("more speed and less force", "más velocidad y menos fuerza"), ("the same as long gears", "lo mismo que las largas")],
  "Useful uphill and as engine brake.", "Útiles en subida y como freno motor.")
Q("ct6", "controls", "When the clutch pedal is NOT pressed, the car is…", "Con el pedal de embrague SIN pisar, el coche está…",
  [("engaged (embragado): the engine’s turn reaches the wheels if in gear", "embragado: el giro llega a las ruedas si hay marcha"), ("disengaged", "desembragado"), ("in neutral automatically", "en punto muerto automáticamente")],
  "Pressed = disengaged, so you can change gear.", "Pisado = desembragado, para cambiar de marcha.")
Q("ct7", "controls", "On the usual motorcycle layout, the front brake is worked with…", "En la disposición habitual de la moto, el freno delantero se acciona con…",
  [("the right hand", "la mano derecha"), ("the left hand", "la mano izquierda"), ("the right foot", "el pie derecho")],
  "The right hand also works the throttle.", "La mano derecha también acelera.")
Q("ct8", "controls", "On the usual motorcycle layout, gears are changed with…", "En la disposición habitual de la moto, las marchas se cambian con…",
  [("the left foot", "el pie izquierdo"), ("the right foot", "el pie derecho"), ("the left hand", "la mano izquierda")],
  "Left hand: clutch; right foot: rear brake.", "Mano izquierda: embrague; pie derecho: freno trasero.")

# ---------------------------------------------------------------- 4. tyres
Q("ty1", "tyres", "The main cause of accidents from mechanical failure is…", "La principal causa de accidente por fallo mecánico son…",
  [("the tyres", "los neumáticos"), ("the lights", "las luces"), ("the steering", "la dirección")],
  "They are the only part touching the ground.", "Son el único elemento en contacto con el suelo.")
Q("ty2", "tyres", "The part of the tyre that touches the road is the…", "La parte del neumático en contacto con el suelo es…",
  [("tread", "la banda de rodadura"), ("bead", "el talón"), ("carcass", "la carcasa")],
  "Its grooves clear the water.", "Sus ranuras evacuan el agua.")
Q("ty3", "tyres", "The bead (talón) is the part that…", "El talón es la parte que…",
  [("joins the tyre to the rim", "une el neumático a la llanta"), ("touches the road", "toca el suelo"), ("forms the side", "forma el costado")],
  "The sidewall is the flanco.", "El costado es el flanco.")
Q("ty4", "tyres", "In “225/70 R16 110S”, the number 70 means…", "En «225/70 R16 110S», el número 70 indica…",
  [("the sidewall height is 70 % of the width", "que la altura del flanco es el 70 % de la anchura"), ("70 km/h maximum", "70 km/h como máximo"), ("70 kg of load", "70 kg de carga")],
  "225 = width in mm; 16 = rim in inches.", "225 = anchura en mm; 16 = llanta en pulgadas.")
Q("ty5", "tyres", "In “225/70 R16 110S”, the 110 is…", "En «225/70 R16 110S», el 110 es…",
  [("the load index (110 = 1,060 kg per tyre)", "el índice de carga (110 = 1.060 kg por neumático)"), ("the maximum speed", "la velocidad máxima"), ("the width", "la anchura")],
  "S is the speed symbol (180 km/h).", "La S es el código de velocidad (180 km/h).")
Q("ty6", "tyres", "“DOT 3221” on a tyre means it was made…", "«DOT 3221» en un neumático indica que se fabricó…",
  [("in week 32 of 2021", "la semana 32 de 2021"), ("on 3 February 2021", "el 3 de febrero de 2021"), ("in March 2022", "en marzo de 2022")],
  "Week, then year.", "Semana y después año.")
Q("ty7", "tyres", "May you fit tyres with a higher load index and speed code than the manufacturer’s?", "¿Se pueden montar neumáticos con índice de carga y código de velocidad superiores a los del fabricante?",
  [("Yes, equal or higher is allowed", "Sí, iguales o superiores"), ("No, they must be identical", "No, deben ser idénticos"), ("Only lower ones", "Solo inferiores")],
  "Lower ones are prohibited.", "Inferiores está prohibido.")
Q("ty8", "tyres", "Which tyres are safer in a puncture?", "¿Qué neumáticos son más seguros en un pinchazo?",
  [("Tubeless tyres: they lose air slowly", "Los sin cámara: pierden el aire lentamente"), ("Tyres with an inner tube", "Los de cámara"), ("Both the same", "Igual los dos")],
  "Tubeless = without inner tube.", "Tubeless = sin cámara.")
Q("ty9", "tyres", "Tyre pressure should be checked…", "La presión de los neumáticos se debe comprobar…",
  [("about every 15 days, with the tyres cold", "cada 15 días aproximadamente, en frío"), ("once a year, hot", "una vez al año, en caliente"), ("only at the ITV", "solo en la ITV")],
  "With a gauge in good condition.", "Con un manómetro en buen estado.")
Q("ty10", "tyres", "You check the pressure with hot tyres and it is above the recommended figure. You should…", "Compruebas la presión con los neumáticos calientes y está por encima de la recomendada. Debes…",
  [("leave it: the manufacturer allows for the rise", "dejarla: el fabricante prevé el aumento"), ("let air out", "quitar aire"), ("add more air", "añadir más aire")],
  "Better to check them cold.", "Mejor comprobarla en frío.")
Q("ty11", "tyres", "The spare wheel should be inflated to…", "La rueda de repuesto debe ir a…",
  [("the highest recommended pressure", "la más alta de las presiones recomendadas"), ("the lowest", "la más baja"), ("half the normal pressure", "la mitad de la normal")],
  "And don’t change pressures between winter and summer.", "Y no variar la presión entre invierno y verano.")
Q("ty12", "tyres", "A tyre that is worn mainly on its edges has been driven with…", "Un neumático gastado sobre todo por los bordes ha circulado con…",
  [("too little pressure", "presión escasa"), ("too much pressure", "presión excesiva"), ("the right pressure", "la presión correcta")],
  "Too much pressure wears the centre.", "La excesiva gasta el centro.")
Q("ty13", "tyres", "The most dangerous pressure fault is…", "La anomalía de presión más peligrosa es…",
  [("different pressures on the same axle", "la descompensada entre ruedas del mismo eje"), ("slightly high pressure in all four", "una presión algo alta en las cuatro"), ("checking every 15 days", "comprobarla cada 15 días")],
  "The car pulls to one side and brakes unevenly.", "Se desvía y frena de forma irregular.")
Q("ty14", "tyres", "Tyres must be changed when the tread depth reaches…", "Hay que cambiar los neumáticos cuando la profundidad del dibujo llega a…",
  [("1.6 mm (2 mm recommended)", "1,6 mm (recomendable 2 mm)"), ("4 mm", "4 mm"), ("0.5 mm", "0,5 mm")],
  "Also with cuts, cracks, bulges or old age.", "También con cortes, grietas, bultos o caducados.")
Q("ty15", "tyres", "The tyres in the best condition should go…", "Los neumáticos en mejor estado deben ir…",
  [("on the rear axle", "en el eje trasero"), ("on the front axle", "en el eje delantero"), ("anywhere", "en cualquier eje")],
  "New tyres: the same on each axle at least.", "Los nuevos: al menos iguales en cada eje.")
Q("ty16", "tyres", "When changing a wheel, you loosen the nuts…", "Al cambiar una rueda, las tuercas se aflojan…",
  [("before lifting the car with the jack", "antes de levantar el vehículo con el gato"), ("after lifting it", "después de levantarlo"), ("with the wheel in the air", "con la rueda en el aire")],
  "And tighten them with the car on the ground.", "Y se aprietan con el vehículo en el suelo.")
Q("ty17", "tyres", "After changing a wheel, check the nuts after…", "Tras cambiar una rueda, hay que comprobar el apriete a los…",
  [("20–30 km", "20–30 km"), ("500 km", "500 km"), ("5 km", "5 km")],
  "Recommended again at 150–250 km.", "Recomendable repetir a los 150–250 km.")
Q("ty18", "tyres", "If a tyre blows out, you should…", "Si revienta un neumático, hay que…",
  [("hold the wheel firmly and brake as little and as gently as possible", "sujetar el volante con fuerza y frenar lo mínimo y con suavidad"), ("brake hard at once", "frenar a fondo inmediatamente"), ("take your foot off the accelerator suddenly", "soltar bruscamente el acelerador")],
  "Keep calm and your line.", "Mantener la calma y la trayectoria.")

# ---------------------------------------------------------------- 4. brakes
Q("br1", "brakes", "The servo brake…", "El servofreno…",
  [("only works with the engine running", "solo funciona con el motor en marcha"), ("works better with the engine off", "funciona mejor con el motor parado"), ("is the parking brake", "es el freno de estacionamiento")],
  "With the engine off you must press much harder.", "Con el motor parado hay que hacer más fuerza.")
Q("br2", "brakes", "The service (foot) brake acts on…", "El freno de servicio (de pie) actúa sobre…",
  [("all the wheels", "todas las ruedas"), ("the rear wheels only", "solo las traseras"), ("one wheel on each side", "una rueda de cada lado")],
  "The emergency brake: at least one on each side.", "El de socorro: al menos una de cada lado.")
Q("br3", "brakes", "In an emergency stop in a car with ABS, you should…", "En una frenada de emergencia con ABS hay que…",
  [("keep pressing hard even if the pedal vibrates", "seguir pisando a fondo aunque vibre el pedal"), ("pump the pedal", "bombear el pedal"), ("release the brake when it vibrates", "soltar el freno cuando vibre")],
  "Without ABS: ease off if the wheels lock and press again.", "Sin ABS: soltar si se bloquean y volver a pisar.")
Q("br4", "brakes", "In an emergency stop, when should you press the clutch?", "En una frenada de emergencia, ¿cuándo se pisa el embrague?",
  [("Just before the vehicle stops", "Justo antes de que el vehículo se detenga"), ("At the same time as the brake", "A la vez que el freno"), ("Never", "Nunca")],
  "First press the brake fully.", "Primero, pisar a fondo el freno.")
Q("br5", "brakes", "The emergency brake (freno de socorro) is…", "El freno de socorro es…",
  [("the last part of the foot brake’s travel, for when the service brake fails", "el último recorrido del freno de pie, por si falla el de servicio"), ("the handbrake", "el freno de mano"), ("the engine brake", "el freno motor")],
  "Acts on at least one wheel on each side.", "Actúa al menos sobre una rueda de cada lado.")
Q("br6", "brakes", "Which is an advantage of the engine brake?", "¿Cuál es una ventaja del freno motor?",
  [("Less brake wear and no fading", "Menos desgaste de frenos y evita el fading"), ("Higher fuel use", "Más consumo"), ("Shorter stopping distance on ice", "Menos distancia de detención en hielo")],
  "And it doesn’t surprise drivers behind.", "Y no sorprende a los de detrás.")
Q("br7", "brakes", "“Fading” is…", "El «fading» es…",
  [("brakes losing effect from overheating", "la pérdida de eficacia de los frenos por calentamiento"), ("a worn tyre", "un neumático gastado"), ("a type of ABS", "un tipo de ABS")],
  "Use the engine brake on long descents.", "Freno motor en los descensos largos.")
Q("br8", "brakes", "The brake pedal feels soft and spongy. The likely cause is…", "El pedal de freno está blando y esponjoso. La causa probable es…",
  [("air in the hydraulic circuit", "aire en el circuito hidráulico"), ("worn pads", "pastillas gastadas"), ("high tyre pressure", "mucha presión en los neumáticos")],
  "Workshop: bleed the system.", "Taller: purgar el sistema.")
Q("br9", "brakes", "The brake pedal goes almost to the floor. The likely cause is…", "El pedal de freno llega casi hasta el fondo. La causa probable es…",
  [("a loss of brake fluid", "una pérdida de líquido de frenos"), ("air in the tyres", "aire en los neumáticos"), ("a hot engine", "el motor caliente")],
  "Fix the leak and refill.", "Reparar la fuga y rellenar.")
Q("br10", "brakes", "After crossing a deep puddle the brakes work worse. You should…", "Tras pasar un charco profundo los frenos van peor. Debes…",
  [("press them several times to dry them", "pisar varias veces para secarlos"), ("go straight to the workshop", "ir directamente al taller"), ("drive faster", "acelerar")],
  "Moisture is the cause.", "La causa es la humedad.")
Q("br11", "brakes", "If the brakes fail, the first thing to do is…", "Si fallan los frenos, lo primero es…",
  [("pump the brake pedal", "pisar y soltar el pedal (bombear)"), ("pull the handbrake hard", "tirar fuerte del freno de mano"), ("switch off the engine", "apagar el motor")],
  "Then shift down, gentle handbrake, escape lane or uphill slope.", "Luego reducir marchas, freno de mano suave, lecho de frenado o subida.")
Q("br12", "brakes", "Which brake is the most used and fades less?", "¿Qué freno es el más utilizado y tiene menos fading?",
  [("The disc brake", "El de disco"), ("The drum brake", "El de tambor"), ("The handbrake", "El de mano")],
  "Pads squeeze the disc; drums use shoes.", "Las pastillas comprimen el disco; el tambor usa zapatas.")
Q("br13", "brakes", "The first reason vehicles fail the ITV is…", "La primera causa por la que los vehículos no superan la ITV es…",
  [("bad brakes", "el mal estado de los frenos"), ("dirty lights", "las luces sucias"), ("missing documents", "la falta de documentos")],
  "Check the brake fluid level between min and max.", "Comprobar el líquido de frenos entre mínimo y máximo.")
Q("br14", "brakes", "The BAS system…", "El sistema BAS…",
  [("detects emergency braking and raises the pressure without locking the wheels", "detecta la frenada de emergencia y aumenta la presión sin bloquear las ruedas"), ("is the parking brake", "es el freno de estacionamiento"), ("prevents skids in bends", "evita derrapes en curva")],
  "ABS keeps the wheels from locking so you can steer.", "El ABS evita el bloqueo y permite dirigir.")

# ---------------------------------------------------------------- 4. suspension, steering, lights, ESP
Q("ch1", "chassis", "Which is NOT a job of the suspension?", "¿Cuál NO es una función de la suspensión?",
  [("Slowing the car down", "Frenar el vehículo"), ("Absorbing bumps", "Absorber las irregularidades"), ("Controlling body roll", "Compensar el balanceo")],
  "It also joins the wheels to the vehicle.", "También une las ruedas al vehículo.")
Q("ch2", "chassis", "The car bounces too much over bumps. Likely causes:", "El vehículo rebota demasiado en los baches. Causas probables:",
  [("worn shock absorbers or too much tyre pressure", "amortiguadores en mal estado o exceso de presión"), ("too little fuel", "poco combustible"), ("wrong headlight aim", "mal reglaje de luces")],
  "Leans too much: shock absorbers or low pressure.", "Se inclina demasiado: amortiguadores o poca presión.")
Q("ch3", "chassis", "The car bounces when braking and takes longer to stop. The cause is…", "Al frenar rebota y tarda más en detenerse. La causa es…",
  [("worn shock absorbers", "amortiguadores en mal estado"), ("worn tyres only", "solo neumáticos gastados"), ("a dirty air filter", "el filtro de aire sucio")],
  "Replace the shock absorbers.", "Sustituir los amortiguadores.")
Q("ch4", "chassis", "Heavy steering can be caused by…", "Una dirección dura puede deberse a…",
  [("low tyre pressure or wrong alignment", "poca presión o una alineación incorrecta"), ("too much fuel", "mucho combustible"), ("new brakes", "frenos nuevos")],
  "Play in the steering: a worn part.", "Holgura: algún elemento desgastado.")
Q("ch5", "chassis", "Speed-sensitive power steering…", "La dirección asistida progresiva…",
  [("gets stiffer as speed rises", "se endurece con la velocidad"), ("gets softer as speed rises", "se ablanda con la velocidad"), ("only works when parked", "solo funciona al aparcar")],
  "For better control at speed.", "Para un mejor control a velocidad.")
Q("ch6", "chassis", "The headlight aim should be checked especially…", "El reglaje de los faros se debe comprobar sobre todo…",
  [("after loading or unloading the vehicle", "después de cargar o descargar el vehículo"), ("after refuelling", "tras repostar"), ("in summer", "en verano")],
  "Too low: obstacles seen later; too high: dazzle.", "Bajo: obstáculos más tarde; alto: deslumbra.")
Q("ch7", "chassis", "Lights are for…", "Las luces sirven para…",
  [("seeing, being seen and signalling", "ver, ser vistos y señalizar"), ("decoration only", "solo decorar"), ("seeing only", "solo ver")],
  "Check the fuses if one fails.", "Revisar los fusibles si alguna falla.")
Q("ch8", "chassis", "The ESP…", "El ESP…",
  [("corrects a skid before it happens, braking individual wheels", "corrige el derrape antes de que se produzca, frenando ruedas concretas"), ("only works once the car has spun", "solo actúa cuando el coche ya ha trompeado"), ("is a parking aid", "es una ayuda al aparcamiento")],
  "And acts on the traction.", "Y actúa sobre la tracción.")
Q("ch9", "chassis", "Traction control acts when…", "El control de tracción actúa cuando…",
  [("a driving wheel spins faster than it should", "una rueda motriz gira más rápido de lo debido"), ("the car is parked", "el coche está aparcado"), ("the lights are off", "las luces están apagadas")],
  "On slippery ground or in bends.", "En suelos deslizantes o en curva.")

# ---------------------------------------------------------------- 4. passive safety
Q("ps1", "passive", "Passive safety aims to…", "La seguridad pasiva trata de…",
  [("reduce the consequences of an accident", "reducir las consecuencias de un accidente"), ("prevent the accident happening", "evitar que se produzca el accidente"), ("improve fuel use", "mejorar el consumo")],
  "Active safety prevents the accident.", "La activa evita el accidente.")
Q("ps2", "passive", "Which is an element of passive safety?", "¿Cuál es un elemento de seguridad pasiva?",
  [("The seat belt", "El cinturón de seguridad"), ("The brakes", "Los frenos"), ("The tyres", "Los neumáticos")],
  "Also airbags, head restraints, child seats, body, glass.", "También airbags, reposacabezas, sillitas, carrocería, cristales.")
Q("ps3", "passive", "In a crash, the body around the passenger compartment…", "En un choque, la carrocería fuera del habitáculo…",
  [("deforms progressively and absorbs the energy", "se deforma progresivamente y absorbe la energía"), ("stays completely rigid", "permanece totalmente rígida"), ("breaks into pieces", "se rompe en trozos")],
  "The central cell stays rigid.", "La estructura central se mantiene rígida.")
Q("ps4", "passive", "The windscreen is usually made of…", "El parabrisas suele ser de cristal…",
  [("laminated glass: it cracks but stays in one piece", "laminado: se agrieta pero sigue unido"), ("tempered glass", "templado"), ("plastic", "plástico")],
  "Side and rear windows: tempered.", "Laterales y luneta: templados.")
Q("ps5", "passive", "The diagonal strap of the seat belt should cross…", "La banda torácica del cinturón debe pasar…",
  [("over the collarbone, between shoulder and neck", "sobre la clavícula, entre el hombro y el cuello"), ("against the neck", "pegada al cuello"), ("under the arm", "por debajo del brazo")],
  "The lap strap goes low, over the hip bones.", "La abdominal, baja, sobre los huesos de la cadera.")
Q("ps6", "passive", "The “submarining effect” happens when…", "El «efecto submarino» se produce cuando…",
  [("the body slides under the lap strap in a crash", "el cuerpo se desliza por debajo de la banda abdominal en un choque"), ("the car falls into water", "el coche cae al agua"), ("the airbag doesn’t open", "no se abre el airbag")],
  "Caused by cushions, reclined seats or a high lap belt.", "Por cojines, respaldo inclinado o banda alta.")
Q("ps7", "passive", "Belt clips that slacken the belt are…", "Las pinzas que reducen la tensión del cinturón…",
  [("prohibited", "están prohibidas"), ("recommended for comfort", "se recomiendan para ir cómodo"), ("allowed in town", "se permiten en ciudad")],
  "They reduce its effect.", "Reducen su eficacia.")
Q("ps8", "passive", "After a serious crash, the seat belt…", "Después de un fuerte accidente, el cinturón…",
  [("should be replaced", "es recomendable cambiarlo"), ("is as good as new", "queda como nuevo"), ("only needs cleaning", "solo hay que limpiarlo")],
  "Pretensioners and anchorages may be damaged.", "Los pretensores y anclajes pueden estar dañados.")
Q("ps9", "passive", "Children must use a child restraint if they are…", "Los menores deben usar un sistema de retención infantil si miden…",
  [("135 cm tall or less", "135 cm o menos"), ("under 10 years old only", "solo si tienen menos de 10 años"), ("150 cm or less", "150 cm o menos")],
  "Approved and suited to their size and weight.", "Homologado y adaptado a su talla y peso.")
Q("ps10", "passive", "The safest seat for a child is generally…", "El asiento más seguro para un niño es, en general…",
  [("the rear centre seat", "el trasero central"), ("the front passenger seat", "el del acompañante"), ("behind the driver", "detrás del conductor")],
  "Least affected by side impacts.", "Menos afectado en impactos laterales.")
Q("ps11", "passive", "With ISOFIX, a child can travel rear-facing at least until…", "Con ISOFIX, el niño puede viajar de espaldas al menos hasta…",
  [("15 months or 83 cm", "los 15 meses o 83 cm"), ("6 months", "los 6 meses"), ("4 years", "los 4 años")],
  "Some models up to 105 cm.", "Algunos hasta 105 cm.")
Q("ps12", "passive", "Can you fit a rear-facing child seat on the front passenger seat?", "¿Se puede colocar una sillita orientada hacia atrás en el asiento del acompañante?",
  [("Only if the airbag has been switched off", "Solo si se ha desactivado el airbag"), ("Yes, always", "Sí, siempre"), ("Yes, if the child is asleep", "Sí, si el niño va dormido")],
  "An active airbag would hit the seat.", "El airbag activo golpearía la sillita.")
Q("ps13", "passive", "You should sit about how far from the airbag?", "¿A qué distancia del airbag hay que sentarse?",
  [("25 cm, never less than 10 cm", "25 cm, nunca menos de 10 cm"), ("5 cm", "5 cm"), ("50 cm minimum", "50 cm como mínimo")],
  "It inflates at about 300 km/h.", "Se infla a unos 300 km/h.")
Q("ps14", "passive", "The airbag and the seat belt…", "El airbag y el cinturón…",
  [("complement each other", "se complementan"), ("replace each other", "se sustituyen"), ("shouldn’t be used together", "no deben usarse juntos")],
  "Always wear the belt.", "Siempre con el cinturón.")
Q("ps15", "passive", "The head restraint is correctly adjusted when…", "El reposacabezas está bien regulado cuando…",
  [("its top is level with the top of the head and its middle at eye level", "su parte superior está a la altura de la cabeza y la central a la de los ojos"), ("it is at neck level", "está a la altura del cuello"), ("it is removed", "se quita")],
  "And no more than 4 cm from the head.", "Y a no más de 4 cm de la cabeza.")
Q("ps16", "passive", "The head restraint mainly protects against…", "El reposacabezas protege sobre todo de…",
  [("whiplash in rear-end crashes", "el latigazo cervical en los alcances"), ("side impacts", "los impactos laterales"), ("rollovers", "los vuelcos")],
  "Compulsory in the front seats.", "Obligatorio en los delanteros.")

# ---------------------------------------------------------------- 4. helmets and gear
Q("hm1", "helmet", "Which helmet type is recommended?", "¿Qué tipo de casco se recomienda?",
  [("Full-face (integral)", "El integral"), ("Open-face (jet)", "El jet"), ("Any, they are the same", "Cualquiera, son iguales")],
  "It covers the whole head and face.", "Cubre toda la cabeza y la cara.")
Q("hm2", "helmet", "The jet helmet…", "El casco jet…",
  [("does not cover the chin", "no cubre la barbilla"), ("covers the whole face", "cubre toda la cara"), ("is not allowed", "no está permitido")],
  "The modular one can lift its chin bar.", "El modular permite levantar la parte inferior.")
Q("hm3", "helmet", "A motorcycle helmet must be approved according to…", "Un casco de moto debe estar homologado conforme a…",
  [("UNECE Regulation 22", "el Reglamento UNECE R22"), ("the ITV", "la ITV"), ("no standard", "ninguna norma")],
  "Label inside.", "Etiqueta interior.")
Q("hm4", "helmet", "After a hard knock, the helmet…", "Tras un fuerte golpe, el casco…",
  [("must be replaced", "se debe sustituir"), ("can be used if it looks fine", "se puede usar si parece bien"), ("must be repainted", "hay que repintarlo")],
  "Also after any accident.", "También tras cualquier accidente.")
Q("hm5", "helmet", "The safest helmet colours are…", "Los colores más seguros para el casco son…",
  [("light, bright and reflective", "claros, brillantes y reflectantes"), ("black and matt", "negros y mates"), ("dark blue", "azul oscuro")],
  "More visible.", "Más visibles.")
Q("hm6", "helmet", "The best material for a riding suit is…", "El mejor material para el traje del motorista es…",
  [("leather or another abrasion-resistant material", "piel u otro material resistente a la abrasión"), ("cotton", "algodón"), ("nylon swimwear", "lycra")],
  "With protection on back, knees and elbows.", "Con protecciones en espalda, rodillas y codos.")

# ---------------------------------------------------------------- 4. ADAS
Q("ad1", "adas", "ADAS systems…", "Los sistemas ADAS…",
  [("help the driver, but the driver keeps an active role", "ayudan al conductor, pero este mantiene un papel activo"), ("drive the car for you", "conducen por ti"), ("let you take more risks", "permiten asumir más riesgos")],
  "Keep full attention and control.", "Mantener total atención y control.")
Q("ad2", "adas", "Most ADAS…", "La mayoría de los ADAS…",
  [("can be switched off by the driver", "pueden ser desconectados por el conductor"), ("can never be switched off", "no se pueden desconectar nunca"), ("only work at night", "solo funcionan de noche")],
  "Temporarily or permanently.", "Temporal o permanentemente.")
Q("ad3", "adas", "The ISA system adapts the speed by…", "El sistema ISA adapta la velocidad…",
  [("reducing engine revs — it never brakes", "reduciendo las revoluciones del motor, nunca frena"), ("braking hard", "frenando fuerte"), ("steering", "girando el volante")],
  "It reads the signs with a camera.", "Lee las señales con una cámara.")
Q("ad4", "adas", "Ordinary cruise control switches off when…", "El control de crucero se desconecta cuando…",
  [("you press the brake", "se pisa el freno"), ("you turn on the radio", "se enciende la radio"), ("you overtake", "se adelanta")],
  "The adaptive one also keeps the safety distance.", "El adaptativo además mantiene la distancia.")
Q("ad5", "adas", "The AEB system…", "El sistema AEB…",
  [("brakes by itself if the driver ignores the warnings", "frena solo si el conductor ignora los avisos"), ("only beeps", "solo pita"), ("parks the car", "aparca el coche")],
  "To avoid or reduce a collision.", "Para evitar o mitigar la colisión.")
Q("ad6", "adas", "The lane departure warning (LDW) stays inactive when…", "El aviso de cambio de carril (LDW) permanece desactivado cuando…",
  [("you have the indicator on", "se lleva el intermitente puesto"), ("it is raining", "llueve"), ("you are on a motorway", "se circula por autopista")],
  "Also in an evasive manoeuvre; usually active from 60–80 km/h.", "También al esquivar; suele activarse desde 60–80 km/h.")
Q("ad7", "adas", "The rear cross-traffic alert (RCTA) warns of what is behind up to…", "La alerta de tráfico cruzado (RCTA) avisa de lo que hay detrás hasta…",
  [("30 m", "30 m"), ("3 m", "3 m"), ("300 m", "300 m")],
  "Some brake by themselves below 15 km/h.", "Algunos frenan solos por debajo de 15 km/h.")
Q("ad8", "adas", "eCall…", "El eCall…",
  [("calls 112 automatically when the airbags go off", "llama al 112 automáticamente al saltar los airbags"), ("calls a tow truck", "llama a una grúa"), ("only works in Spain", "solo funciona en España")],
  "Operators answer in the caller’s language.", "Responden en el idioma de quien llama.")
Q("ad9", "adas", "The event data recorder (EDR, “black box”)…", "El registrador de datos (EDR, «caja negra»)…",
  [("cannot be switched off", "no se puede desactivar"), ("can be switched off with a button", "se desactiva con un botón"), ("records conversations", "graba las conversaciones")],
  "It records data around a collision.", "Registra datos de una colisión.")
Q("ad10", "adas", "An already-registered car can be fitted with an aftermarket ADAS if it…", "Un coche ya matriculado puede instalar un ADAS aftermarket si…",
  [("only warns and doesn’t act on the driving controls", "solo avisa y no actúa sobre los sistemas de conducción"), ("steers the car", "mueve el volante"), ("brakes the car", "frena el coche")],
  "Warning systems only.", "Solo sistemas de aviso.")
Q("ad11", "adas", "In the practical driving test, which system is NOT allowed?", "En el examen práctico, ¿qué sistema NO está permitido?",
  [("Full self-parking", "La ayuda de estacionamiento total"), ("Start-Stop", "El Start-Stop"), ("Hill holder", "La ayuda de salida en pendiente")],
  "Rear camera, 360° and sensors are allowed.", "Cámara trasera, 360° y sensores sí se admiten.")
Q("ad12", "adas", "In the driving test, the ISA may be used…", "En el examen práctico, el ISA se puede usar…",
  [("with its automatic speed control switched off", "con el control automático de velocidad desconectado"), ("fully on", "totalmente conectado"), ("never", "nunca")],
  "Systems not listed must be switched off.", "Los sistemas no recogidos deben desactivarse.")
Q("ad13", "adas", "If the AEB brakes during the driving test to avoid an accident, the examiner treats it…", "Si en el examen el AEB frena para evitar un accidente, el examinador lo valora…",
  [("like an intervention by the instructor", "como una intervención del profesor"), ("as nothing", "como nada"), ("as a merit", "como un mérito")],
  "It counts against the candidate.", "Cuenta en contra del aspirante.")
Q("ad14", "adas", "The hill holder…", "La ayuda de salida en pendiente (hill holder)…",
  [("stops the car rolling back when you lift off the brake on a slope", "impide que el coche vaya hacia atrás al soltar el freno en pendiente"), ("switches the engine off at idle", "apaga el motor al ralentí"), ("keeps the lane", "mantiene el carril")],
  "Start-Stop switches the engine off at idle.", "El Start-Stop apaga el motor al ralentí.")

# ---------------------------------------------------------------- 4. grip, bends, skids
Q("gr1", "grip", "Which surface gives the best grip?", "¿Qué pavimento da mejor adherencia?",
  [("Rough, dry, clean asphalt", "Asfalto rugoso, seco y limpio"), ("Cobbles", "Adoquines"), ("A shiny smooth surface", "Un pavimento liso y brillante")],
  "Wet, gravel, leaves and markings reduce grip.", "Mojado, gravilla, hojas y marcas viales reducen la adherencia.")
Q("gr2", "grip", "On two wheels in bad weather, a painted road marking should be crossed…", "En dos ruedas con mal tiempo, una marca vial se debe pasar…",
  [("slowing down before it and keeping the vehicle upright", "reduciendo antes de llegar y con el vehículo vertical"), ("braking on it", "frenando sobre ella"), ("leaning hard", "muy inclinado")],
  "Markings are very slippery.", "Las marcas son muy resbaladizas.")
Q("gr3", "grip", "The most dangerous force in a bend is…", "La fuerza más peligrosa en una curva es…",
  [("centrifugal force", "la fuerza centrífuga"), ("centripetal force", "la fuerza centrípeta"), ("gravity", "la gravedad")],
  "It pushes the vehicle outwards.", "Empuja el vehículo hacia el exterior.")
Q("gr4", "grip", "Centrifugal force increases with…", "La fuerza centrífuga aumenta con…",
  [("more speed, a tighter bend and more weight", "más velocidad, curva más cerrada y más peso"), ("a wider bend", "una curva más abierta"), ("less speed", "menos velocidad")],
  "Double the speed: four times the force.", "Al doble de velocidad, cuatro veces la fuerza.")
Q("gr5", "grip", "When should you slow down for a bend?", "¿Cuándo se debe reducir la velocidad para una curva?",
  [("Before entering it, on the straight", "Antes de entrar, en la recta"), ("In the middle of the bend", "En mitad de la curva"), ("At the exit", "A la salida")],
  "Avoid braking inside the bend.", "Evitar frenar dentro de la curva.")
Q("gr6", "grip", "Inside the bend you should…", "Durante la curva hay que…",
  [("accelerate gently and steadily", "acelerar suave y progresivamente"), ("brake hard", "frenar fuerte"), ("press the clutch", "pisar el embrague")],
  "It improves grip.", "Mejora la adherencia.")
Q("gr7", "grip", "If the rear axle skids, you should…", "Si derrapa el eje trasero, hay que…",
  [("turn the wheel towards the same side as the skid", "girar el volante hacia el mismo lado del derrape"), ("turn the wheel the other way", "girar hacia el lado contrario"), ("brake hard", "frenar fuerte")],
  "Countersteer.", "Contravolante.")
Q("gr8", "grip", "If the front axle skids, you should…", "Si derrapa el eje delantero, hay que…",
  [("straighten the steering", "enderezar la dirección"), ("turn the wheel more", "girar más el volante"), ("accelerate hard", "acelerar fuerte")],
  "So the front tyres grip again.", "Para que las ruedas recuperen agarre.")
Q("gr9", "grip", "A skid caused by too much braking is corrected by…", "Un derrape por exceso de frenada se corrige…",
  [("releasing the brake", "soltando el freno"), ("braking harder", "frenando más"), ("pulling the handbrake", "tirando del freno de mano")],
  "Then steer gently.", "Después, dirigir con suavidad.")
Q("gr10", "grip", "Which is a cause of skidding?", "¿Cuál es una causa de derrape?",
  [("Sudden use of the accelerator, brake or steering", "El uso brusco del acelerador, el freno o el volante"), ("Smooth driving", "Una conducción suave"), ("Correct tyre pressure", "La presión correcta")],
  "Also too much speed with a vehicle in poor condition.", "También velocidad excesiva con mal estado del vehículo.")

# ---------------------------------------------------------------- 4. weather
Q("wx1", "weather", "Rain is most dangerous…", "La lluvia es más peligrosa…",
  [("when the first drops fall", "al caer las primeras gotas"), ("after an hour of rain", "tras una hora lloviendo"), ("when it stops", "cuando para")],
  "Dirt and oil make the road slippery.", "La suciedad hace la calzada deslizante.")
Q("wx2", "weather", "Aquaplaning happens when…", "El aquaplaning se produce cuando…",
  [("the tread can’t clear the water and the tyre floats", "el dibujo no puede desalojar el agua y el neumático flota"), ("the road is dry", "la calzada está seca"), ("you drive slowly", "se circula despacio")],
  "The car ignores steering and brakes.", "No obedece a la dirección ni al freno.")
Q("wx3", "weather", "A large puddle should be crossed…", "Un charco grande se debe atravesar…",
  [("slowly, even in first gear", "lentamente, incluso en primera"), ("fast to avoid getting stuck", "rápido para no quedarse"), ("with the wheels of one side only, fast", "solo con las ruedas de un lado, deprisa")],
  "Small ones: between the wheels or with all of them.", "Pequeños: entre las ruedas o con todas.")
Q("wx4", "weather", "On snow, you should move off…", "Con nieve hay que iniciar la marcha…",
  [("gently, preferably in second gear", "suavemente, mejor en segunda"), ("in first gear with lots of throttle", "en primera y acelerando mucho"), ("in reverse", "marcha atrás")],
  "With the wheels straight.", "Con las ruedas rectas.")
Q("wx5", "weather", "With a thick layer of snow, you should drive…", "Con una capa de nieve gruesa hay que circular…",
  [("in the ruts of other vehicles", "por las rodaduras de otros vehículos"), ("where there are no ruts", "donde no haya rodaduras"), ("on the shoulder", "por el arcén")],
  "Thin layer: where there are no ruts.", "Capa fina: donde no haya rodaduras.")
Q("wx6", "weather", "On snow, which gear should you use?", "Con nieve, ¿qué marcha conviene?",
  [("The highest gear possible for the circumstances", "La más alta posible según las circunstancias"), ("Always first", "Siempre la primera"), ("Neutral", "Punto muerto")],
  "Downhill: low gears (engine brake).", "En bajada: marchas cortas (freno motor).")
Q("wx7", "weather", "On an autovía with snow making driving difficult…", "En una autovía con nieve que dificulta la circulación…",
  [("overtaking is prohibited and you use the right-hand lane", "está prohibido adelantar y se circula por el carril derecho"), ("you may overtake on the left", "se puede adelantar por la izquierda"), ("you use the left lane", "se circula por el carril izquierdo")],
  "With three or more lanes, also the next one; the left ones stay free for snowploughs.", "Con tres o más carriles, también su contiguo; los de la izquierda, libres para quitanieves.")
Q("wx8", "weather", "On ice, the stopping distance is multiplied by…", "Con hielo, la distancia de detención se multiplica por…",
  [("10", "10"), ("2", "2"), ("4", "4")],
  "Grip is almost nil.", "La adherencia es casi nula.")
Q("wx9", "weather", "Ice is most likely…", "El hielo es más frecuente…",
  [("on bridges and in shady places, at night or at dawn", "en puentes y zonas sombrías, de noche o al amanecer"), ("on sunny afternoons", "las tardes soleadas"), ("in tunnels at midday", "en túneles a mediodía")],
  "Near or below 0 °C.", "Con temperaturas cercanas o inferiores a 0 °C.")
Q("wx10", "weather", "Agents require chains. Can you use a snow spray instead?", "Los agentes obligan a usar cadenas. ¿Sirve un spray para nieve?",
  [("No; if you don’t fit chains you are fined and immobilised", "No; si no las pones, te sancionan e inmovilizan el vehículo"), ("Yes, it is the same", "Sí, es lo mismo"), ("Yes, on the motorway", "Sí, en autovía")],
  "Chains at least on the driving wheels.", "Cadenas al menos en las ruedas motrices.")
Q("wx11", "weather", "In fog you should…", "Con niebla hay que…",
  [("slow down, keep more distance and avoid overtaking", "reducir la velocidad, aumentar la distancia y evitar adelantar"), ("use high beams", "usar las luces largas"), ("follow the car ahead closely", "seguir de cerca al de delante")],
  "Guide yourself by the road markings.", "Guiarse por las marcas viales.")
Q("wx12", "weather", "Strong crosswind from the right: as you overtake a lorry and are alongside it, you should…", "Viento lateral fuerte desde la derecha: al adelantar a un camión y ponerte a su altura, debes…",
  [("straighten the wheel, because it shields you", "enderezar el volante, porque hace de pantalla"), ("turn more to the right", "girar más a la derecha"), ("brake hard", "frenar fuerte")],
  "Once past it, correct to the right again.", "Al dejarlo atrás, vuelve a corregir a la derecha.")
Q("wx13", "weather", "Which vehicles are most affected by wind?", "¿Qué vehículos son más afectados por el viento?",
  [("Bicycles, mopeds, motorcycles and bulky vehicles", "Bicicletas, ciclomotores, motos y vehículos voluminosos"), ("Small cars", "Turismos pequeños"), ("Buses only", "Solo autobuses")],
  "Vans, lorries, trailers.", "Furgonetas, camiones, remolques.")
Q("wx14", "weather", "Sunglasses should never be worn…", "Las gafas de sol nunca deben usarse…",
  [("at night or in tunnels", "de noche o en túneles"), ("on snowy days", "en días de nieve"), ("at sunset", "a la puesta de sol")],
  "Also avoid driving into the rising or setting sun.", "Evita conducir con el sol de cara al amanecer o atardecer.")
Q("wx15", "weather", "If snow is forecast, you should take…", "Si hay previsión de nevada hay que llevar…",
  [("a full tank, warm clothes, water and food, a torch and a charged phone", "depósito lleno, ropa de abrigo, agua y comida, linterna y móvil cargado"), ("only sunglasses", "solo gafas de sol"), ("nothing special", "nada especial")],
  "Even blankets.", "Incluso mantas.")
