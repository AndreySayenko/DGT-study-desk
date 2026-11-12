# -*- coding: utf-8 -*-
"""Question bank for the interactive Category A1/A2, Topic 12 page (riding techniques). In every question the FIRST
option is the correct one (the page shuffles options when it shows them). Ids must be unique and must not start with
"ai"."""

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
    "features": dict(sec=1, en="The motorcycle and its types", es="La moto y sus tipos",
        recap=[("Less stable, more fragile, less visible, powerful for their mass.", "Menos estables, más frágiles, menos visibles, más potentes respecto a su masa."),
               ("Hard acceleration: centre of gravity back, front wheel loses grip, wobble.", "Aceleración fuerte: centro de gravedad atrás, la delantera pierde agarre, fluctuación."),
               ("Scooter: town, automatic. Tourer: long trips, less manoeuvrable. Sports: high speed, tiring posture.", "Scooter: ciudad, automática. Rutera: viajes largos, menos maniobrable. Deportiva: velocidad, postura incómoda."),
               ("Short, low handlebar: less resistance but less steering angle.", "Manillar corto y bajo: menos resistencia pero menor ángulo de giro.")],
        trap=("Thinking a high, wide handlebar is more aerodynamic.", "Pensar que un manillar alto y ancho es más aerodinámico.")),
    "controls": dict(sec=1, en="Controls and mirrors", es="Mandos y espejos",
        recap=[("Right hand: throttle and front brake. Left hand: clutch, lights, horn.", "Mano derecha: acelerador y freno delantero. Izquierda: embrague, luces, claxon."),
               ("Right foot: rear brake. Left foot: gear lever.", "Pie derecho: freno trasero. Pie izquierdo: selector de marchas."),
               ("Mirrors: up to 100 km/h left compulsory; over 100 km/h left and right.", "Espejos: hasta 100 km/h, izquierdo obligatorio; más de 100 km/h, izquierdo y derecho."),
               ("Adjust before moving off, stopped, on level ground; turn your head for the blind spot.", "Regular antes de salir, parado y en llano; girar la cabeza para el ángulo muerto.")],
        trap=("Thinking the rear brake is a hand lever on most motorcycles.", "Pensar que el freno trasero es una maneta en la mayoría de las motos.")),
    "start": dict(sec=2, en="Stands and moving off", es="Soportes y puesta en marcha",
        recap=[("Engine off: handlebar with both hands, no sharp front braking, feel the weight.", "Motor parado: manillar con las dos manos, sin frenar bruscamente delante, notar el peso."),
               ("Side stand: lean it on; to take it off, brake and bring the bike upright.", "Pata de cabra: inclinarla sobre ella; para quitarla, frenar y enderezar la moto."),
               ("Centre stand: foot on it, pull back and slightly up; off by pushing forward, front brake ready.", "Caballete: pie encima, tirar hacia atrás y algo arriba; quitarlo empujando adelante con el freno delantero listo."),
               ("Right foot down, left selects first (lever down); throttle and clutch out gently.", "Pie derecho al suelo, el izquierdo mete primera (palanca abajo); acelerar y soltar embrague con suavidad.")],
        trap=("Letting the clutch out sharply and doing a wheelie.", "Soltar el embrague de golpe y hacer un caballito.")),
    "posture": dict(sec=2, en="Posture and the passenger", es="Postura y acompañante",
        recap=[("Astride, relaxed, looking well ahead; arms slightly bent; knees on the tank in bends and braking.", "A horcajadas, suelto, mirando a lo lejos; brazos flexionados; rodillas al depósito en curvas y frenadas."),
               ("Passenger behind, astride, feet on footrests; never between rider and handlebar.", "Pasajero detrás, a horcajadas, pies en reposapiés; nunca entre conductor y manillar."),
               ("The passenger holds on and leans like the rider.", "El pasajero se agarra y se inclina como el conductor."),
               ("With a passenger: longer braking, less acceleration, rear locks less, more rear tyre pressure.", "Con pasajero: frenadas más largas, menos aceleración, la trasera se bloquea menos, más presión detrás.")],
        trap=("Thinking the passenger should lean the other way to balance.", "Pensar que el pasajero debe inclinarse al revés para compensar.")),
    "curves": dict(sec=2, en="Balance and bends", es="Equilibrio y curvas",
        recap=[("Balance is hardest at low speed; gyroscopic help from about 30 km/h.", "El equilibrio es más difícil despacio; ayuda giroscópica desde unos 30 km/h."),
               ("Brake before the bend, not in it; a leaning bike takes more width.", "Frenar antes de la curva, no dentro; inclinada, la moto ocupa más anchura."),
               ("Inside: accelerate progressively; if you must brake, very gently.", "Dentro: acelerar progresivamente; si hay que frenar, muy suave."),
               ("Emergency in a bend: both brakes, look at the exit. Centrifugal force: weight, speed, tighter bend.", "Emergencia en curva: los dos frenos y mirar a la salida. Fuerza centrífuga: peso, velocidad, curva cerrada.")],
        trap=("Looking at the obstacle during an emergency in a bend.", "Mirar al obstáculo en una emergencia en curva.")),
    "braking": dict(sec=2, en="Braking", es="Frenada",
        recap=[("The front wheel matters most; brake progressively; locked wheel → release and brake again.", "La rueda delantera es la más importante; frenar progresivo; rueda bloqueada → soltar y volver a frenar."),
               ("Emergency: upright, 60–70 % front, 30–40 % rear, clutch in, both brakes hard.", "Emergencia: recto, 60–70 % delante, 30–40 % detrás, desembragar, los dos frenos a fondo."),
               ("Rigid body: arms straight, knees on the tank, heels on the footrests.", "Cuerpo rígido: brazos estirados, rodillas al depósito, talones en los reposapiés."),
               ("Engine brake: change down carefully; downhill to spare the brakes; clutch only near the stop.", "Freno motor: reducir con cuidado; en bajadas para no calentar frenos; embrague solo al final.")],
        trap=("Braking hard with the front brake while leaned over.", "Frenar fuerte con el delantero con la moto inclinada.")),
    "town": dict(sec=2, en="Town and groups", es="Ciudad y grupo",
        recap=[("Town: defensive riding, feet on the footrests, rear brake at very low speed, look ahead.", "Ciudad: conducción defensiva, pies en los estribos, freno trasero muy despacio, mirar lejos."),
               ("Groups: subgroups of 3–4, with gaps between them.", "Grupo: subgrupos de 3–4, separados entre sí."),
               ("Least experienced and least powerful in the front groups.", "Los menos experimentados y menos potentes en los grupos de cabeza."),
               ("Single file, slightly offset, never side by side; responsibility is individual.", "En hilera, algo desviados, nunca en paralelo; la responsabilidad es individual.")],
        trap=("Putting the most experienced riders at the front of the group.", "Poner a los más experimentados en cabeza del grupo.")),
    "sidecar": dict(sec=2, en="The sidecar", es="El sidecar",
        recap=[("Weight not symmetrical; centre of gravity shifted towards the motorcycle.", "Peso no simétrico; centro de gravedad desplazado hacia la moto."),
               ("Turning away from the sidecar or swerving: risk of losing grip or tipping towards the sidecar.", "Girar hacia el lado contrario al sidecar o esquivar: riesgo de perder adherencia o volcar hacia el sidecar."),
               ("Up to three people, if the registration certificate allows it.", "Hasta tres personas, si lo autoriza el permiso de circulación."),
               ("Course: the heaviest in the sidecar; a single passenger in the sidecar.", "Curso: el de más peso en el sidecar; un solo pasajero, en el sidecar.")],
        trap=("Seating a single passenger behind the rider instead of in the sidecar.", "Sentar a un único pasajero detrás del conductor en lugar de en el sidecar.")),
    "load": dict(sec=2, en="Luggage and fuel use", es="Carga y consumo",
        recap=[("Only what you need, low and close to the centre of gravity, strapped down.", "Solo lo necesario, bajo y cerca del centro de gravedad, amarrado."),
               ("Front rack (tank): heavy; rear rack: light; side cases: equal weight.", "Delantero (depósito): pesado; trasero: ligero; laterales: mismo peso."),
               ("Nothing near handlebar, wheels, suspension, pedals or transmission; adjust the suspension.", "Nada cerca de manillar, ruedas, suspensión, pedales o transmisión; ajustar la amortiguación."),
               ("Fuel use: speed above all, air resistance, aggressive riding, town, poor maintenance, overload.", "Consumo: sobre todo la velocidad, el aire, la conducción agresiva, la ciudad, el mal mantenimiento, el exceso de carga.")],
        trap=("Putting heavy items in the top case.", "Llevar objetos pesados en el baúl.")),
}

# ---------------------------------------------------------------- 1 features and types
Q("ft1", "features", "Why do motorcycles need special preparation compared with cars?", "¿Por qué la moto exige una preparación especial frente al turismo?",
  [("They are less stable, more fragile, less visible and powerful for their mass", "Son menos estables, más frágiles, menos visibles y más potentes respecto a su masa"), ("They are slower", "Son más lentas"), ("They have more safety systems", "Tienen más sistemas de seguridad")],
  "Each of these features changes how you must ride.", "Cada una de esas características cambia la forma de conducir.")
Q("ft2", "features", "What can happen under very hard acceleration on a motorcycle?", "¿Qué puede ocurrir al acelerar muy fuerte en moto?",
  [("The centre of gravity shifts back, the front wheel loses grip and the bike can wobble", "El centro de gravedad se desplaza atrás, la delantera pierde adherencia y se favorece la fluctuación"),
   ("The rear wheel locks", "Se bloquea la rueda trasera"), ("Nothing: power is always an advantage", "Nada: la potencia siempre es una ventaja")],
  "Strong acceleration can also surprise others and the rider.", "Las grandes aceleraciones también pueden sorprender a los demás y al propio conductor.")
Q("ft3", "features", "Why are motorcycles less visible to other road users?", "¿Por qué las motos son menos visibles para los demás?",
  [("Their small size, quick movements and speed", "Por su menor tamaño, la agilidad de sus movimientos y su velocidad"), ("Because they have fewer lights", "Porque llevan menos luces"), ("Because they are usually dark", "Porque suelen ser oscuras")],
  "That is why riders must make themselves visible.", "Por eso el motorista debe hacerse visible.")
Q("ft4", "features", "Which type of motorcycle is ideal for town: automatic, easy and economical?", "¿Qué tipo de moto es ideal para la ciudad: automática, manejable y económica?",
  [("Scooter", "Scooter"), ("Tourer", "Rutera"), ("Trial", "Trial")],
  "Scooters are easy to ride, automatic, economical and clean.", "Los scooter son manejables, automáticos, de bajo consumo y limpios.")
Q("ft5", "features", "Which type suits long trips with a passenger but is less manoeuvrable?", "¿Qué tipo es idóneo para viajes largos con acompañante pero menos maniobrable?",
  [("Tourer (gran turismo)", "Rutera (gran turismo)"), ("Scooter", "Scooter"), ("Cross", "Cross")],
  "Large, heavy, with big fairings against rain and wind.", "Grande, pesada y con amplios carenados contra lluvia y viento.")
Q("ft6", "features", "What is the drawback of a sports motorcycle on long trips?", "¿Qué inconveniente tiene la moto deportiva en viajes largos?",
  [("An uncomfortable riding position", "Una postura incómoda"), ("Too little power", "Poca potencia"), ("No fairing", "No tiene carenado")],
  "Very aerodynamic fairings force a tiring posture; they need training and experience.", "Sus carenados aerodinámicos obligan a una postura incómoda; requiere formación y experiencia.")
Q("ft7", "features", "What does the fairing do?", "¿Para qué sirve el carenado?",
  [("Improves safety and aerodynamics: protection, less fuel, fatigue later", "Mejora la seguridad y la aerodinámica: protección, menos consumo, la fatiga tarda más"), ("Only decorates the motorcycle", "Solo decora la moto"), ("Covers the front wheel to keep it clean", "Cubre la rueda delantera para que no se ensucie")],
  "It leaves the front wheel free, keeping manoeuvrability and cooling.", "Deja libre la rueda delantera, conservando la maniobrabilidad y la refrigeración.")
Q("ft8", "features", "What is the drawback of a short, low handlebar?", "¿Qué inconveniente tiene un manillar corto y bajo?",
  [("Less steering angle to avoid obstacles", "Menor ángulo de giro para esquivar obstáculos"), ("More wind resistance", "Más resistencia aerodinámica"), ("It is not allowed", "No está permitido")],
  "It has less wind resistance and suits high speed, but steers less.", "Tiene menos resistencia y va mejor a velocidad alta, pero gira menos.")
Q("ft9", "features", "Is the seat height of a motorcycle usually adjustable?", "¿Suele ser regulable la altura del asiento de una moto?",
  [("No, except on a few motorcycles", "No, salvo casos excepcionales"), ("Yes, always", "Sí, siempre"), ("Only on scooters", "Solo en los scooter")],
  "The handlebar, on the other hand, is usually adjustable within limits.", "El manillar, en cambio, suele ser ajustable dentro de ciertos límites.")
Q("ft10", "features", "A motorcycle has a self-protection structure and seat belts, as its ITV card states. What must its occupants wear?", "Una moto tiene estructura de autoprotección y cinturones, y así consta en su tarjeta ITV. ¿Qué deben llevar sus ocupantes?",
  [("The seat belt; they are exempt from helmet, gloves and closed shoes", "El cinturón; quedan exentos de casco, guantes y calzado cerrado"), ("Helmet and seat belt", "Casco y cinturón"), ("Only the helmet", "Solo el casco")],
  "Art. 118 of the Reglamento General de Circulación.", "Art. 118 del Reglamento General de Circulación.")

# ---------------------------------------------------------------- 1.2–1.3 controls and mirrors
Q("ct1", "controls", "On most motorcycles, which controls does the right hand work?", "En la mayoría de las motos, ¿qué mandos acciona la mano derecha?",
  [("Throttle and front brake", "El acelerador y el freno delantero"), ("Clutch and horn", "El embrague y el claxon"), ("Rear brake", "El freno trasero")],
  "Throttle gently; front brake gently and progressively.", "El acelerador, suavemente; el freno delantero, suave y progresivamente.")
Q("ct2", "controls", "Which control does the left hand work?", "¿Qué mando acciona la mano izquierda?",
  [("The clutch (and the lights and horn switches)", "El embrague (y también las luces y el claxon)"), ("The front brake", "El freno delantero"), ("The throttle", "El acelerador")],
  "The left side of the motorcycle: clutch and gears.", "En el lado izquierdo de la moto: embrague y marchas.")
Q("ct3", "controls", "What does the right foot operate?", "¿Qué acciona el pie derecho?",
  [("The rear brake", "El freno trasero"), ("The gear lever", "El selector de marchas"), ("The side stand only", "Solo la pata de cabra")],
  "Right side: throttle and both brakes.", "Lado derecho: acelerador y los dos frenos.")
Q("ct4", "controls", "What does the left foot operate?", "¿Qué acciona el pie izquierdo?",
  [("The gear lever", "El selector de marchas"), ("The rear brake", "El freno trasero"), ("The front brake", "El freno delantero")],
  "Lever down for first; up to change up, down to change down.", "Abajo para la primera; arriba para subir y abajo para bajar.")
Q("mr1", "controls", "Which mirror is compulsory on a motorcycle whose top speed is not over 100 km/h?", "¿Qué espejo es obligatorio en una moto cuya velocidad máxima no supera los 100 km/h?",
  [("The left one; the right one is optional", "El izquierdo; el derecho es optativo"), ("The right one only", "Solo el derecho"), ("Both", "Los dos")],
  "Reglamento General de Vehículos, Anexo III.", "Reglamento General de Vehículos, anexo III.")
Q("mr2", "controls", "And on a motorcycle whose top speed is over 100 km/h?", "¿Y en una moto cuya velocidad máxima supera los 100 km/h?",
  [("Left and right", "Izquierdo y derecho"), ("Left only", "Solo el izquierdo"), ("None is compulsory", "Ninguno es obligatorio")],
  "Over 100 km/h both outside mirrors are compulsory.", "A más de 100 km/h, los dos retrovisores exteriores son obligatorios.")
Q("mr3", "controls", "Which mirrors must a three-wheeler with a closed body carry?", "¿Qué espejos debe llevar un vehículo de tres ruedas con carrocería cerrada?",
  [("One inside and one on the left (two outside if the inside one can’t give the view)", "Uno interior y otro izquierdo (dos exteriores si por el interior no se ve lo exigido)"), ("Only one on the left", "Solo uno izquierdo"), ("None", "Ninguno")],
  "If the interior mirror cannot meet the visibility requirements, the right outside mirror becomes compulsory.", "Si el interior no cumple la visibilidad exigida, es obligatorio el exterior derecho.")
Q("mr4", "controls", "When and how should you adjust the mirrors?", "¿Cuándo y cómo debes regular los espejos?",
  [("Before moving off, with the motorcycle still, preferably on level ground", "Antes de iniciar la marcha, con la moto inmovilizada, preferiblemente en llano"), ("While riding, at the first straight", "Circulando, en la primera recta"), ("Only at the ITV", "Solo en la ITV")],
  "Or at least check that their adjustment is right.", "O, al menos, comprobar que su reglaje es correcto.")
Q("mr5", "controls", "What is the blind spot?", "¿Qué es el ángulo muerto?",
  [("The area at the sides and behind that the mirrors don’t show", "La zona lateral y trasera que no se ve por los espejos"), ("The area right in front of the front wheel", "La zona justo delante de la rueda delantera"), ("A dark stretch of road", "Un tramo oscuro de la vía")],
  "A good adjustment reduces it; turn your head before any manoeuvre to complete your view.", "Un buen reglaje lo reduce; hay que girar la cabeza antes de cualquier maniobra.")
Q("mr6", "controls", "You want to change lanes. Your mirrors show nothing. What else must you do?", "Quieres cambiar de carril. Los espejos no muestran nada. ¿Qué más debes hacer?",
  [("Turn your head to check the blind spot", "Girar la cabeza para comprobar el ángulo muerto"), ("Nothing: the mirrors are enough", "Nada: los espejos bastan"), ("Sound the horn", "Tocar el claxon")],
  "A car can hide beside and slightly behind you.", "Un coche puede ocultarse a tu lado y algo por detrás.")

# ---------------------------------------------------------------- 2.1–2.2 stands and moving off
Q("st1", "start", "Pushing the motorcycle with the engine off, what should you avoid?", "Moviendo la moto con el motor parado, ¿qué debes evitar?",
  [("Braking sharply with the front brake", "Frenar bruscamente con el freno delantero"), ("Holding the handlebar with both hands", "Sujetar el manillar con las dos manos"), ("Leaning it slightly", "Inclinarla ligeramente")],
  "It can destabilise the motorcycle and make it fall.", "Puede desestabilizarla y provocar una caída.")
Q("st2", "start", "How do you take a motorcycle off its side stand?", "¿Cómo se quita la pata de cabra?",
  [("Hold the handlebar with both hands, braking, bring the bike upright and push the stand back with your foot", "Sujetar el manillar con ambas manos, frenando, enderezar la moto y empujar el soporte con el pie"),
   ("Kick the stand while the motorcycle leans on it", "Golpear el soporte con la moto apoyada"), ("Ride off and it folds by itself", "Arrancar y se pliega solo")],
  "Practise it on flat, firm ground, first standing, then sitting on the bike.", "Se practica en terreno llano y compacto, primero a pie y después subido.")
Q("st3", "start", "How do you put a motorcycle on its centre stand?", "¿Cómo se pone la moto sobre el caballete?",
  [("Foot on the stand and, putting your weight on it, pull the bike back and slightly up", "Pie sobre el soporte y, cargando el peso en él, tirar de la moto hacia atrás y algo hacia arriba"),
   ("Push the motorcycle forwards onto it", "Empujar la moto hacia delante sobre él"), ("Lift the front wheel", "Levantar la rueda delantera")],
  "One hand on the handlebar and the other on the rear.", "Una mano en el manillar y la otra en la parte trasera.")
Q("st4", "start", "How do you take a motorcycle off its centre stand?", "¿Cómo se quita el caballete?",
  [("Sitting on it, feet on the ground, push it forwards with the front brake ready", "Subido, con los pies en el suelo, empujarla hacia delante con el freno delantero preparado"),
   ("Pull it backwards", "Tirar de ella hacia atrás"), ("Start the engine and accelerate", "Arrancar y acelerar")],
  "The front brake stops it rolling away.", "El freno delantero evita que se vaya hacia delante.")
Q("st5", "start", "To move off, which foot do you put on the ground?", "Para iniciar la marcha, ¿qué pie apoyas en el suelo?",
  [("The right one: the left one selects first gear", "El derecho: el izquierdo mete la primera"), ("The left one", "El izquierdo"), ("Both", "Los dos")],
  "First gear is selected by pushing the lever down.", "La primera se selecciona empujando la palanca hacia abajo.")
Q("st6", "start", "How do you select first gear on most motorcycles?", "¿Cómo se mete la primera en la mayoría de las motos?",
  [("Pushing the gear lever down with the left foot", "Empujando el selector hacia abajo con el pie izquierdo"), ("Pulling the lever up", "Subiendo la palanca"), ("With the right foot", "Con el pie derecho")],
  "Then up to change up, down to change down.", "Después, hacia arriba para subir y hacia abajo para bajar.")
Q("st7", "start", "What can happen if you let the clutch out sharply when moving off?", "¿Qué puede ocurrir si sueltas el embrague de golpe al salir?",
  [("A wheelie: the mass moves back and the front wheel lifts", "Un caballito: la masa se desplaza atrás y la rueda delantera se levanta"), ("The rear brake locks", "Se bloquea el freno trasero"), ("Nothing", "Nada")],
  "Throttle and clutch must be worked gently and progressively.", "Hay que acelerar y soltar el embrague suave y progresivamente.")
Q("st8", "start", "Where do you put your feet once the motorcycle is moving?", "¿Dónde pones los pies una vez en movimiento?",
  [("On the footrests", "En los estribos (reposapiés)"), ("Near the ground, ready to stop", "Cerca del suelo, por si hay que parar"), ("On the engine guard", "En el protector del motor")],
  "Keep them there, even at low speed in town.", "Se mantienen ahí incluso despacio en ciudad.")

# ---------------------------------------------------------------- 2.3 posture and passenger
Q("ps1", "posture", "Where must the passenger sit on a motorcycle?", "¿Dónde debe ir el pasajero en una moto?",
  [("Behind the rider, astride, feet on the footrests", "Detrás del conductor, a horcajadas, con los pies en los reposapiés"), ("Between the rider and the handlebar", "Entre el conductor y el manillar"), ("Sideways, on the seat", "De lado, en el asiento")],
  "Never between the rider and the handlebar (art. 12).", "Nunca entre el conductor y el manillar (art. 12).")
Q("ps2", "posture", "Where should the rider look while riding?", "¿Hacia dónde debe mirar el motorista al circular?",
  [("Well ahead, at the vehicles beyond the one in front", "A lo lejos, a los vehículos que van más adelante"), ("At the vehicle right in front", "Al vehículo que va delante"), ("At the front wheel", "A la rueda delantera")],
  "Looking far ahead lets you anticipate.", "Mirar a lo lejos permite anticiparse.")
Q("ps3", "posture", "How should the rider hold the handlebar?", "¿Cómo debe agarrar el manillar el motorista?",
  [("Gently but firmly, arms slightly bent", "Con suavidad y firmeza, brazos ligeramente flexionados"), ("As tight as possible, arms locked", "Lo más fuerte posible, brazos rígidos"), ("With one hand on long straights", "Con una mano en las rectas largas")],
  "Avoid tension and stiffness.", "Hay que evitar la fuerza y el agarrotamiento.")
Q("ps4", "posture", "When should your knees press against the tank?", "¿Cuándo deben ir las rodillas contra el depósito?",
  [("When riding, especially in bends and when braking", "Al circular, sobre todo en las curvas y en las frenadas"), ("Only when stopped", "Solo parado"), ("Never: it tires you", "Nunca: cansa")],
  "Better control of the weight in bends; no sliding forward when braking.", "Más control del peso en curvas; evita deslizarse hacia delante al frenar.")
Q("ps5", "posture", "What is wrong with a very high, upright riding position?", "¿Qué inconveniente tiene una postura muy alta y erguida?",
  [("It raises the centre of gravity: more fatigue and more wind resistance", "Eleva el centro de gravedad: más fatiga y más resistencia al avance"), ("It improves stability", "Mejora la estabilidad"), ("Nothing", "Ninguno")],
  "The posture should be relaxed, without leaning forward more than needed.", "La postura debe ser suelta, sin inclinarse más de lo necesario.")
Q("ps6", "posture", "How should a passenger behave in bends?", "¿Cómo debe comportarse el pasajero en las curvas?",
  [("Hold on to the rider and lean exactly as the rider does", "Agarrarse al conductor y adoptar la misma inclinación"), ("Lean the opposite way to balance", "Inclinarse al lado contrario para compensar"), ("Stay rigidly upright", "Mantenerse rígido y vertical")],
  "Otherwise they unbalance the motorcycle.", "Si no, desequilibra la moto o dificulta la conducción.")
Q("ps7", "posture", "With a passenger, how does braking change?", "Con pasajero, ¿cómo cambia la frenada?",
  [("It takes longer, but the rear wheel locks less easily", "Es más prolongada, pero la rueda trasera se bloquea con más dificultad"), ("It is shorter", "Es más corta"), ("The front wheel locks less", "La delantera se bloquea menos")],
  "So the rear brake can be used harder.", "Por eso el freno trasero puede usarse con más fuerza.")
Q("ps8", "posture", "With a passenger, what should you do with the rear tyre pressure?", "Con pasajero, ¿qué haces con la presión del neumático trasero?",
  [("Raise it, as the manufacturer says", "Aumentarla, según el fabricante"), ("Lower it for more grip", "Bajarla para tener más agarre"), ("Leave it", "Dejarla igual")],
  "It helps avoid wobble (fluctuación).", "Ayuda a evitar la fluctuación.")
Q("ps9", "posture", "What is wobble (fluctuación)?", "¿Qué es la fluctuación?",
  [("A swaying of the tyres that harms grip and stability", "Un oscilamiento o vaivén de los neumáticos que perjudica la adherencia y la estabilidad"), ("A puncture", "Un pinchazo"), ("An engine vibration at idle", "Una vibración del motor al ralentí")],
  "It comes from the centre of gravity moving back, badly placed luggage or a poor road or bike.", "Se debe al desplazamiento del centro de gravedad hacia atrás, al equipaje mal colocado o al mal estado de la vía o la moto.")
Q("ps10", "posture", "With a passenger, what happens to acceleration?", "Con pasajero, ¿qué ocurre con la aceleración?",
  [("It is weaker, and the mass shifts back when accelerating", "Es menor, y al acelerar la masa se desplaza hacia atrás"), ("It is stronger", "Es mayor"), ("It does not change", "No cambia")],
  "The centre of gravity changes with a passenger.", "Con acompañante varía el centro de gravedad.")

# ---------------------------------------------------------------- 2.4 bends
Q("cv1", "curves", "When is it hardest to keep a motorcycle balanced?", "¿Cuándo es más difícil mantener el equilibrio en moto?",
  [("At low speed", "A baja velocidad"), ("At high speed", "A alta velocidad"), ("On a motorway", "En autopista")],
  "At low speed the rider must use the handlebar and the body to avoid falling.", "A baja velocidad hay que corregir con el manillar y el cuerpo para no caer.")
Q("cv2", "curves", "From about what speed does the gyroscopic effect help to keep the balance, according to your course?", "¿A partir de qué velocidad el efecto giroscópico ayuda al equilibrio, según tu curso?",
  [("About 30 km/h", "Unos 30 km/h"), ("About 10 km/h", "Unos 10 km/h"), ("About 80 km/h", "Unos 80 km/h")],
  "The spinning wheels make the motorcycle more stable.", "La rotación de las ruedas estabiliza la moto.")
Q("cv3", "curves", "Where should you brake for a bend?", "¿Dónde debes frenar para tomar una curva?",
  [("Before entering it, on the straight", "Antes de entrar, en la recta"), ("In the middle of the bend", "En mitad de la curva"), ("At the exit", "A la salida")],
  "Braking in the bend can make you lose grip.", "Frenar durante la curva puede hacer perder adherencia.")
Q("cv4", "curves", "Why must you keep away from the centre line in a left-hand bend?", "¿Por qué debes alejarte del eje en una curva a la izquierda?",
  [("A leaning motorcycle takes up more width and you could invade the opposite lane", "Inclinada, la moto ocupa más anchura y podrías invadir el sentido contrario"), ("To see the road signs", "Para ver las señales"), ("To use less fuel", "Para gastar menos")],
  "Your body hangs over the inside of the bend.", "El cuerpo sobresale hacia el interior de la curva.")
Q("cv5", "curves", "Once inside the bend, what should you do with the throttle?", "Una vez dentro de la curva, ¿qué haces con el acelerador?",
  [("Accelerate progressively to bring the bike back upright", "Acelerar progresivamente para recobrar la verticalidad"), ("Close it completely", "Cerrarlo del todo"), ("Accelerate hard", "Acelerar a fondo")],
  "If braking is essential, do it very gently.", "Si fuese imprescindible frenar, hacerlo muy suavemente.")
Q("cv6", "curves", "You must brake hard in the middle of a bend. What do you do?", "Tienes que frenar de emergencia en mitad de una curva. ¿Qué haces?",
  [("Use both brakes and look at the exit of the bend", "Accionar los dos frenos y mirar hacia la salida de la curva"), ("Look at the obstacle and use the front brake only", "Mirar el obstáculo y usar solo el delantero"), ("Close your eyes and brake", "Cerrar los ojos y frenar")],
  "If you look at the obstacle you instinctively steer towards it.", "Si se mira el obstáculo, instintivamente se dirige la moto hacia él.")
Q("cv7", "curves", "Which of these increases the centrifugal force in a bend?", "¿Cuál de estos factores aumenta la fuerza centrífuga en una curva?",
  [("More speed", "Más velocidad"), ("A wider bend", "Una curva más abierta"), ("Less weight", "Menos peso")],
  "More weight, more speed, and a tighter bend (smaller radius) all increase it.", "Más peso, más velocidad y una curva más cerrada (menor radio) la aumentan.")
Q("cv8", "curves", "How should you enter a bend?", "¿Cómo debes entrar en una curva?",
  [("With the motorcycle fully under control, so you won’t need to brake in it", "Con la moto totalmente dominada, para no tener que frenar dentro"), ("Fast, and brake if needed", "Rápido, y frenar si hace falta"), ("In neutral", "En punto muerto")],
  "Judge the line and adapt the speed before arriving.", "Hay que valorar la trayectoria y adaptar la velocidad antes de llegar.")
Q("cv9", "curves", "Which bend produces the most centrifugal force at the same speed?", "¿Qué curva produce más fuerza centrífuga a la misma velocidad?",
  [("The tighter one, with the smaller radius", "La más cerrada, de menor radio"), ("The wider one", "La más abierta"), ("Both the same", "Las dos igual")],
  "The smaller the radius, the greater the force.", "Cuanto menor es el radio, mayor es la fuerza.")

# ---------------------------------------------------------------- 2.5 braking
Q("bk1", "braking", "Which wheel matters most for a motorcycle’s stability when braking?", "¿Qué rueda es la más importante para estabilizar la moto al frenar?",
  [("The front wheel", "La rueda delantera"), ("The rear wheel", "La rueda trasera"), ("Both the same", "Las dos igual")],
  "Braking must be progressive: too hard on the front can lock it and throw you off.", "La frenada debe ser progresiva: demasiado fuerte delante puede bloquearla y provocar la caída.")
Q("bk2", "braking", "According to your course, how do you share an emergency braking?", "Según tu curso, ¿cómo repartes una frenada de emergencia?",
  [("60–70 % on the front, 30–40 % on the rear", "60–70 % en la delantera y 30–40 % en la trasera"), ("50 % on each", "50 % en cada una"), ("Only the rear brake", "Solo el freno trasero")],
  "Upright, clutch in, both brakes used hard.", "Recto, desembragado y con uso intensivo de ambos frenos.")
Q("bk3", "braking", "A wheel locks while you brake. What do you do?", "Se bloquea una rueda al frenar. ¿Qué haces?",
  [("Release that brake at once and apply it again once the wheel turns", "Soltar inmediatamente ese freno y volver a accionarlo una vez desbloqueada"), ("Brake harder", "Frenar más fuerte"), ("Keep the brake on until you stop", "Mantener el freno hasta parar")],
  "A locked front wheel especially can make you fall.", "Una rueda delantera bloqueada, sobre todo, puede provocar la caída.")
Q("bk4", "braking", "When should you brake in an emergency?", "¿Cuándo debes frenar en una emergencia?",
  [("With the motorcycle upright, before it leans", "Con la moto recta, antes de inclinarla"), ("While leaning hard", "Muy inclinado"), ("Only after the bend", "Solo después de la curva")],
  "Brake when there is no lean, or before it.", "Frenar cuando no exista inclinación lateral o antes de ella.")
Q("bk5", "braking", "In an emergency braking, what happens to the weight?", "En una frenada de emergencia, ¿qué pasa con el peso?",
  [("It moves forward: the rear wheel loses traction and can lock and skid", "Se desplaza hacia delante: la rueda trasera pierde tracción y puede bloquearse y derrapar"), ("It moves back", "Se desplaza hacia atrás"), ("It does not move", "No se desplaza")],
  "With a passenger the rear wheel locks less easily.", "Con pasajero es más difícil que se bloquee la trasera.")
Q("bk6", "braking", "What body position helps in an emergency braking?", "¿Qué postura ayuda en una frenada de emergencia?",
  [("Rigid: arms straight, knees against the tank, heels pressing the footrests", "Rígida: brazos estirados, rodillas contra el depósito y talones presionando los reposapiés"), ("Relaxed, leaning forward", "Relajada, inclinada adelante"), ("Standing on the footrests", "De pie sobre los estribos")],
  "It stops the rider sliding forward.", "Evita el deslizamiento hacia delante del conductor.")
Q("bk7", "braking", "In an emergency braking, what does your course advise doing with the clutch?", "En una frenada de emergencia, ¿qué aconseja tu curso hacer con el embrague?",
  [("Pull it in and use both brakes hard", "Desembragar y hacer un uso intensivo de ambos frenos"), ("Keep it out to use the engine brake", "No tocarlo, para usar el freno motor"), ("Change up a gear", "Subir una marcha")],
  "Hard use of both brakes is only for this kind of braking.", "El uso intensivo de ambos frenos es solo para este tipo de frenadas.")
Q("bk8", "braking", "In normal braking, when should you pull the clutch in?", "En una frenada normal, ¿cuándo accionas el embrague?",
  [("When the motorcycle has almost stopped", "Cuando la moto esté prácticamente detenida"), ("As soon as you start braking", "En cuanto empiezas a frenar"), ("Never", "Nunca")],
  "Until then the engine brake helps; except in emergency braking.", "Hasta entonces ayuda el freno motor; salvo en las frenadas de emergencia.")
Q("bk9", "braking", "Why use the engine brake on a long descent?", "¿Por qué usar el freno motor en una bajada larga?",
  [("So the service brakes don’t overheat", "Para no calentar el freno de servicio"), ("To use less fuel only", "Solo para gastar menos"), ("It is compulsory", "Es obligatorio")],
  "Change down carefully, with no jolt or locked wheel.", "Reducir con cuidado, sin sacudidas ni bloqueo de rueda.")
Q("bk10", "braking", "On a shaft-drive motorcycle, what happens if you select a lower gear by mistake and let the clutch out sharply?", "En una moto con cardan, ¿qué pasa si metes una marcha inferior por error y sueltas el embrague de golpe?",
  [("The rear wheel bounces hard and the transmission can be damaged", "Un rebote acusado de la rueda trasera y una posible avería de la transmisión"), ("Nothing", "Nada"), ("The front wheel locks", "Se bloquea la rueda delantera")],
  "Change down carefully.", "Hay que reducir con cuidado.")

# ---------------------------------------------------------------- 2.6–2.7 town and groups
Q("tw1", "town", "In town, at very low speed, which brake does your course recommend for stability?", "En ciudad, a muy poca velocidad, ¿qué freno recomienda tu curso para mantener la estabilidad?",
  [("The rear brake", "El freno trasero"), ("The front brake", "El freno delantero"), ("Neither: use your feet", "Ninguno: los pies")],
  "And look far ahead, not at the front wheel.", "Y mirar a lo lejos, no cerca de la rueda delantera.")
Q("tw2", "town", "Riding slowly in town, may you take your feet off the footrests?", "Circulando despacio en ciudad, ¿puedes quitar los pies de los estribos?",
  [("No: keep them there to avoid losing balance", "No: mantenerlos para evitar desequilibrios"), ("Yes, below 20 km/h", "Sí, por debajo de 20 km/h"), ("Yes, always in town", "Sí, siempre en ciudad")],
  "Even at low speed.", "Incluso aunque se circule a poca velocidad.")
Q("tw3", "town", "What kind of riding suits town traffic?", "¿Qué tipo de conducción conviene en ciudad?",
  [("Defensive riding: more attention, because motorcycles are more vulnerable", "Conducción defensiva: más atención, porque la moto es más vulnerable"), ("Fast, to get through junctions quickly", "Rápida, para pasar pronto las intersecciones"), ("Weaving to avoid queues", "Zigzagueando para evitar colas")],
  "Pedestrians, junctions and traffic make motorcycles more vulnerable.", "Peatones, intersecciones y la propia circulación hacen la moto más vulnerable.")
Q("gr1", "town", "How should a large group of motorcyclists ride?", "¿Cómo debe circular un grupo numeroso de motoristas?",
  [("In subgroups of three or four, with gaps between them", "En subgrupos de tres o cuatro, distanciados entre sí"), ("All together, close to each other", "Todos juntos y pegados"), ("In pairs side by side", "De dos en dos en paralelo")],
  "Group riding is influenced by the others: competitiveness can appear.", "En grupo influye el comportamiento de los demás: puede aparecer el afán competitivo.")
Q("gr2", "town", "Where should the least experienced riders and least powerful motorcycles go?", "¿Dónde deben ir los conductores con menos experiencia y las motos de menor potencia?",
  [("In the front groups", "En los grupos de cabeza"), ("At the back", "Al final"), ("In the middle of the largest group", "En medio del grupo más numeroso")],
  "So the group adapts to them and nobody is left behind.", "Así el grupo se adapta a ellos.")
Q("gr3", "town", "In a group, how should the motorcycles be placed?", "En grupo, ¿cómo se colocan las motos?",
  [("In single file, slightly offset to see ahead", "En hilera, algo desviados para ver hacia delante"), ("Side by side", "En paralelo"), ("All on the same line", "Todos en la misma línea")],
  "Never side by side.", "Nunca en paralelo.")
Q("gr4", "town", "In a group, who is responsible for each rider’s riding?", "En grupo, ¿quién responde de la conducción de cada motorista?",
  [("Each rider individually", "Cada conductor, individualmente"), ("The leader", "El que va en cabeza"), ("The organiser", "El organizador")],
  "Responsibility is individual.", "La responsabilidad es individual.")
Q("gr5", "town", "May two mopeds ride side by side on the shoulder?", "¿Pueden circular dos ciclomotores en paralelo por el arcén?",
  [("No: the law forbids it for vehicles that must use the shoulder", "No: la ley lo prohíbe a los vehículos obligados a usar el arcén"), ("Yes, like bicycles", "Sí, como las bicicletas"), ("Yes, in town", "Sí, en poblado")],
  "Only bicycles may ride two abreast (art. 36).", "Solo las bicicletas pueden ir en columna de a dos (art. 36).")

# ---------------------------------------------------------------- 2.8 sidecar
Q("sc1", "sidecar", "Why does a motorcycle with a sidecar handle differently?", "¿Por qué una moto con sidecar se conduce de forma diferente?",
  [("The weight is not symmetrical and the centre of gravity is shifted towards the motorcycle", "El peso no está repartido simétricamente y el centro de gravedad está desplazado hacia la moto"),
   ("It has more power", "Tiene más potencia"), ("It has no rear brake", "No tiene freno trasero")],
  "Riding must be more moderate.", "La conducción debe ser más moderada.")
Q("sc2", "sidecar", "When is there a risk of tipping over towards the sidecar?", "¿Cuándo hay riesgo de volcar hacia el lado del sidecar?",
  [("When turning towards the side away from the sidecar, or swerving", "Al girar hacia el lado contrario al sidecar o al esquivar un obstáculo"), ("When braking in a straight line", "Al frenar en recta"), ("When moving off", "Al arrancar")],
  "The centrifugal force pushes the outfit towards the sidecar.", "La fuerza centrífuga empuja el conjunto hacia el sidecar.")
Q("sc3", "sidecar", "How many people may travel on a motorcycle with a sidecar?", "¿Cuántas personas pueden viajar en una moto con sidecar?",
  [("Up to three, if the registration certificate allows it", "Hasta tres, si lo autoriza el permiso de circulación"), ("Two", "Dos"), ("Four", "Cuatro")],
  "The rider and a passenger on the motorcycle, and one in the sidecar.", "Conductor y pasajero en la moto, y otro en el sidecar.")
Q("sc4", "sidecar", "With a single passenger, where does your course say they should ride?", "Con un solo pasajero, ¿dónde dice tu curso que debe ir?",
  [("In the sidecar", "En el sidecar"), ("Behind the rider", "Detrás del conductor"), ("Either", "Indistintamente")],
  "For the outfit’s stability, especially in turns.", "Por la estabilidad del conjunto, sobre todo en los giros.")
Q("sc5", "sidecar", "With two passengers, who goes in the sidecar, according to your course?", "Con dos pasajeros, ¿quién va en el sidecar, según tu curso?",
  [("The heavier one", "El de mayor peso"), ("The lighter one", "El de menor peso"), ("The younger one", "El más joven")],
  "It helps balance the outfit.", "Ayuda a equilibrar el conjunto.")
Q("sc6", "sidecar", "Must the sidecar wheel have a brake?", "¿Debe tener freno la rueda del sidecar?",
  [("No, it is not required", "No, no se exige"), ("Yes, always", "Sí, siempre"), ("Only if a passenger travels in it", "Solo si va un pasajero")],
  "The motorcycle needs two brakes, one front and one rear; the sidecar wheel need not have one.", "La moto necesita dos frenos, delantero y trasero; no se exige frenar la rueda del sidecar.")

# ---------------------------------------------------------------- 2.9–2.10 load and fuel
Q("ld1", "load", "Where should heavy luggage go?", "¿Dónde debe ir el equipaje pesado?",
  [("Low and close to the centre of gravity, at the bottom of the cases", "Bajo y cerca del centro de gravedad, en el fondo de las maletas"), ("High, in the top case", "Arriba, en el baúl"), ("On the handlebar", "En el manillar")],
  "And spread the weight evenly on both sides.", "Y repartir el peso de forma equilibrada a ambos lados.")
Q("ld2", "load", "What should the rear rack (top case) carry?", "¿Qué debe llevar el portaequipajes trasero (baúl)?",
  [("Light items only", "Solo objetos ligeros"), ("The heaviest items", "Los objetos más pesados"), ("Fuel cans", "Bidones de combustible")],
  "Heavy items there cause wobble.", "Los objetos pesados ahí provocan fluctuación.")
Q("ld3", "load", "What is the front rack, on the tank, good for?", "¿Para qué es adecuado el portaequipajes delantero, sobre el depósito?",
  [("Heavy items, because it doesn’t change the centre of gravity", "Objetos pesados, porque no modifica el centro de gravedad"), ("Only light items", "Solo objetos ligeros"), ("Nothing: it is forbidden", "Para nada: está prohibido")],
  "It keeps the weight near the centre of the motorcycle.", "Mantiene el peso cerca del centro de la moto.")
Q("ld4", "load", "How should side cases be loaded?", "¿Cómo se cargan las maletas laterales?",
  [("The same weight on each side, without overloading", "El mismo peso a cada lado, sin sobrecargar"), ("All the weight on the right side", "Todo el peso en el lado derecho"), ("Heaviest on top", "Lo más pesado arriba")],
  "Unbalanced or overloaded cases are dangerous at speed.", "Unas maletas desequilibradas o sobrecargadas son peligrosas a velocidad elevada.")
Q("ld5", "load", "Where should you never place luggage?", "¿Dónde no debes colocar nunca la carga?",
  [("Near the handlebar, wheels, suspension, pedals or transmission", "Cerca del manillar, las ruedas, la suspensión, los pedales o la transmisión"), ("In the side cases", "En las maletas laterales"), ("In a tank bag", "En una bolsa sobre el depósito")],
  "It could interfere with them.", "Podría interferir con ellos.")
Q("ld6", "load", "With a heavy load, what should you adjust on the motorcycle?", "Con mucha carga, ¿qué debes ajustar en la moto?",
  [("The suspension, to compensate for the load", "La amortiguación, para compensar la carga"), ("The mirrors only", "Solo los espejos"), ("Nothing", "Nada")],
  "Strap down everything that has no fixing.", "Y amarrar todo lo que no tenga anclaje.")
Q("ld7", "load", "What is the main factor in fuel consumption and pollution?", "¿Cuál es el principal factor del consumo y la contaminación?",
  [("High speed", "La velocidad elevada"), ("The colour of the motorcycle", "El color de la moto"), ("Riding with gloves", "Llevar guantes")],
  "Also air resistance, aggressive riding, town riding, poor maintenance and overloading.", "También la resistencia al aire, la conducción agresiva, la ciudad, el mal mantenimiento y el exceso de carga.")
Q("ld8", "load", "Where does a motorcycle use more fuel: in town or on the open road?", "¿Dónde consume más una moto: en poblado o en carretera?",
  [("In town", "En poblado"), ("On the open road", "En carretera"), ("The same", "Igual")],
  "Stopping and starting raises consumption.", "Las paradas y arrancadas aumentan el consumo.")
Q("ld9", "load", "Why shouldn’t you modify the motorcycle’s fairing?", "¿Por qué no se debe modificar el carenado de la moto?",
  [("It changes the aerodynamics and raises fuel use", "Cambia la aerodinámica y aumenta el consumo"), ("It is only for looks", "Es solo estético"), ("It voids the helmet approval", "Anula la homologación del casco")],
  "Air resistance is one of the factors in consumption.", "La resistencia al aire es uno de los factores del consumo.")
Q("ld10", "load", "Besides fuel use, what else do aggressive riding and overloading increase?", "Además del consumo, ¿qué más aumentan la conducción agresiva y el exceso de carga?",
  [("Tyre wear, through friction and heat", "El desgaste de los neumáticos, por rozamiento y calentamiento"), ("The motorcycle’s top speed", "La velocidad máxima de la moto"), ("Nothing else", "Nada más")],
  "The same factors wear the tyres.", "Los mismos factores desgastan los neumáticos.")
