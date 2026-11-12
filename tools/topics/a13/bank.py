# -*- coding: utf-8 -*-
"""Question bank for the interactive Category A1/A2, Topic 13 page (maintenance and accessories). In every question the
FIRST option is the correct one (the page shuffles options when it shows them). Ids must be unique and must not start
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
    "engine": dict(sec=1, en="Chassis, engine and transmission", es="Chasis, motor y transmisión",
        recap=[("Frame: steel or aluminium, strong and light; carries everything.", "Bastidor: acero o aluminio, resistente y ligero; soporta todo."),
               ("Engine: turns energy into mechanical energy; two-stroke or four-stroke.", "Motor: transforma la energía en mecánica; de dos o de cuatro tiempos."),
               ("Two-stroke: four phases in two piston movements; oil mixed with the petrol.", "Dos tiempos: cuatro fases en dos movimientos; aceite con la gasolina."),
               ("Four-stroke: four movements; oil in the crankcase. Transmission drives the rear wheel.", "Cuatro tiempos: cuatro movimientos; aceite en el cárter. La transmisión mueve la rueda trasera.")],
        trap=("Thinking a two-stroke engine uses no oil.", "Pensar que el motor de dos tiempos no lleva aceite.")),
    "fuel": dict(sec=1, en="Fuel system", es="Alimentación",
        recap=[("Delivers the right amount of air and fuel to the cylinders.", "Hace llegar a los cilindros la cantidad de aire y combustible necesaria."),
               ("Air filter: clean air; dirty = more fuel and pollution; change more often in summer and on dust.", "Filtro de aire: aire limpio; sucio = más consumo y contaminación; cambiarlo más en verano y con polvo."),
               ("Carburettor makes the mixture; being replaced by electronic injection.", "El carburador hace la mezcla; en desuso frente a la inyección electrónica."),
               ("Clean the carburettor, clean or change the filter, adjust the idle.", "Limpiar el carburador, limpiar o cambiar el filtro, regular el ralentí.")],
        trap=("Thinking a dirty air filter only affects power, not fuel use.", "Pensar que un filtro sucio solo afecta a la potencia, no al consumo.")),
    "lube": dict(sec=1, en="Lubrication and cooling", es="Lubricación y refrigeración",
        recap=[("Oil film between metal parts: less friction, less wear.", "Película de aceite entre piezas metálicas: menos rozamiento y desgaste."),
               ("Four-stroke: check cold, upright, dipstick between MIN and MAX; change warm; filter as the maker says.", "Cuatro tiempos: comprobar en frío, vertical, varilla entre MIN y MAX; cambiar en caliente; filtro según fabricante."),
               ("Used oil to a collection point, never down the drain.", "Aceite usado a un punto de recogida, nunca a la alcantarilla."),
               ("Cooling: air (fins, fan) or liquid (pump, radiator, coolant level).", "Refrigeración: aire (aletas, ventilador) o líquido (bomba, radiador, nivel).")],
        trap=("Checking the oil with a hot engine, just after riding.", "Comprobar el aceite con el motor caliente, recién llegado.")),
    "elec": dict(sec=1, en="Electrical system", es="Sistema eléctrico",
        recap=[("The battery powers the motorcycle while the engine is stopped.", "La batería da energía mientras el motor está parado."),
               ("Starting circuit: an electric motor gives the first turns.", "Circuito de arranque: un motor eléctrico da los primeros giros."),
               ("Ignition: the spark plug makes the spark in a petrol engine.", "Encendido: la bujía hace la chispa en el motor de gasolina."),
               ("Electrolyte: sulphuric acid and distilled water; top up with distilled water only.", "Electrolito: ácido sulfúrico y agua destilada; reponer solo con agua destilada.")],
        trap=("Topping up a battery with tap water.", "Rellenar la batería con agua del grifo.")),
    "trans": dict(sec=1, en="Transmission, steering and suspension", es="Transmisión, dirección y suspensión",
        recap=[("Clutch, gearbox, and chain, belt or shaft to the rear wheel.", "Embrague, caja de cambios y cadena, correa o cardan a la rueda trasera."),
               ("Chain: tension and grease regularly, especially after rain.", "Cadena: tensar y engrasar periódicamente, sobre todo tras la lluvia."),
               ("Shaft: little maintenance, oil every 10,000–15,000 km (course).", "Cardan: poco mantenimiento, aceite cada 10.000–15.000 km (curso)."),
               ("Steering bearings without play or stiffness; check the shock absorbers.", "Rodamientos de la dirección sin holgura ni agarrotamiento; revisar los amortiguadores.")],
        trap=("Thinking a shaft drive needs greasing like a chain after rain.", "Pensar que el cardan hay que engrasarlo como la cadena tras la lluvia.")),
    "access": dict(sec=1, en="Accessories, spares and maintenance", es="Accesorios, repuestos y mantenimiento",
        recap=[("Every accessory must be approved; major modifications need an ITV.", "Todo accesorio debe estar homologado; las reformas de importancia, ITV."),
               ("No spare part is compulsory; spare bulbs recommended.", "Ningún repuesto es obligatorio; lámparas de repuesto recomendables."),
               ("Since 1-10-2026 a motorcycle must carry a high-visibility vest.", "Desde el 1-10-2026 la moto debe llevar chaleco de alta visibilidad."),
               ("After rain grease: chain, cables, levers, pedals, cable ends, stands.", "Tras la lluvia engrasar: cadena, cables, manetas, pedales, extremos de cables, caballetes.")],
        trap=("Thinking a motorcycle must carry spare bulbs.", "Pensar que la moto debe llevar lámparas de repuesto obligatoriamente.")),
    "faults": dict(sec=1, en="Breakdowns", es="Averías",
        recap=[("Won’t start: battery, spark plug, no fuel, starter button or key.", "No arranca: batería, bujía, no llega combustible, pulsador o llave."),
               ("Clutch drags: oil in poor condition, too thick or too much.", "Problemas al desembragar: aceite en mal estado, muy viscoso o exceso."),
               ("Smoke: black fuel, bluish white oil, white condensed water.", "Humo: negro combustible, blanco azulado aceite, blanco agua condensada."),
               ("Unstable: tyres, wheel alignment, rim, steering head too tight. Overheating: plug, filter, coolant, lubrication.", "Inestable: neumáticos, alineación, llanta, tija apretada. Recalentamiento: bujía, filtro, refrigerante, lubricación.")],
        trap=("Thinking bluish-white smoke means too much fuel.", "Pensar que el humo blanco azulado indica exceso de combustible.")),
}

# ---------------------------------------------------------------- 1 chassis, engine, transmission
Q("en1", "engine", "What are the three main parts of a motorcycle?", "¿Cuáles son las tres partes principales de una moto?",
  [("Chassis, engine and transmission", "Chasis, motor y transmisión"), ("Tank, seat and handlebar", "Depósito, asiento y manillar"), ("Wheels, brakes and lights", "Ruedas, frenos y luces")],
  "Other systems are added to these.", "A ellos se suman otros sistemas.")
Q("en2", "engine", "What is a motorcycle’s chassis (frame) usually made of?", "¿De qué suele estar hecho el chasis o bastidor de una moto?",
  [("Steel or aluminium: strong and light", "Acero o aluminio: resistente y ligero"), ("Plastic", "Plástico"), ("Wood and carbon", "Madera y carbono")],
  "It supports all the systems and parts.", "Es el soporte de todos los sistemas y elementos.")
Q("en3", "engine", "What does the engine do?", "¿Qué hace el motor?",
  [("Turns energy into mechanical energy to move the motorcycle", "Transforma la energía en energía mecánica para desplazar la moto"), ("Stores electricity", "Almacena electricidad"), ("Cools the motorcycle", "Refrigera la moto")],
  "It can be two-stroke or four-stroke.", "Puede ser de dos o de cuatro tiempos.")
Q("en4", "engine", "In a two-stroke engine, how many piston movements does it take to complete intake, compression, explosion and exhaust?", "En un motor de dos tiempos, ¿en cuántos movimientos del pistón se hacen la admisión, compresión, explosión y escape?",
  [("Two", "Dos"), ("Four", "Cuatro"), ("One", "Uno")],
  "A four-stroke needs four.", "El de cuatro tiempos necesita cuatro.")
Q("en5", "engine", "How is a two-stroke engine lubricated?", "¿Cómo se lubrica un motor de dos tiempos?",
  [("Oil is mixed with the petrol, or comes from a separate oil tank", "El aceite se mezcla con la gasolina o va en un depósito aparte"), ("It needs no oil", "No necesita aceite"), ("Oil in the crankcase, checked with a dipstick", "Con aceite en el cárter, comprobado con varilla")],
  "Your course’s introduction swaps this with the four-stroke; its lubrication section has it right.", "La introducción de tu curso lo intercambia con el de cuatro tiempos; su apartado de lubricación lo dice bien.")
Q("en6", "engine", "How is a four-stroke engine lubricated?", "¿Cómo se lubrica un motor de cuatro tiempos?",
  [("With oil in the crankcase, kept between MIN and MAX", "Con aceite en el cárter, entre el mínimo y el máximo"), ("By mixing oil into the petrol", "Mezclando aceite con la gasolina"), ("It needs no lubrication", "No necesita lubricación")],
  "Check the level regularly with the dipstick.", "El nivel se comprueba periódicamente con la varilla.")
Q("en7", "engine", "Which wheel does the transmission drive on a motorcycle?", "¿A qué rueda lleva el movimiento la transmisión en una moto?",
  [("The rear wheel", "A la rueda trasera"), ("The front wheel", "A la rueda delantera"), ("Both", "A las dos")],
  "The rear wheel is the driving wheel.", "La rueda trasera es la motriz.")

# ---------------------------------------------------------------- 1.1 fuel
Q("fu1", "fuel", "What does the fuel system do?", "¿Qué hace el sistema de alimentación?",
  [("Delivers the right amount of air and fuel to the cylinders", "Hace llegar a los cilindros la cantidad de aire y combustible necesaria"), ("Cools the engine", "Refrigera el motor"), ("Charges the battery", "Carga la batería")],
  "Its main parts: air filter and carburettor or injection.", "Sus componentes principales: filtro de aire y carburador o inyección.")
Q("fu2", "fuel", "What happens if the air filter is dirty?", "¿Qué ocurre si el filtro del aire está sucio?",
  [("The engine uses more fuel and pollutes more", "El motor consume más combustible y contamina más"), ("Nothing important", "Nada importante"), ("The engine uses less fuel", "El motor consume menos")],
  "Change it as the manufacturer says, more often in summer and on dusty tracks.", "Hay que cambiarlo según el fabricante, más a menudo en verano y por caminos polvorientos.")
Q("fu3", "fuel", "When should the air filter be changed more often?", "¿Cuándo hay que cambiar el filtro del aire con más frecuencia?",
  [("In summer and when riding on dusty tracks", "En verano y si se circula por caminos polvorientos"), ("In winter", "En invierno"), ("Only in town", "Solo en ciudad")],
  "Dust clogs it sooner.", "El polvo lo obstruye antes.")
Q("fu4", "fuel", "What does the carburettor do?", "¿Qué hace el carburador?",
  [("Makes the air and petrol mixture in the right proportion", "Elabora la mezcla de aire y gasolina en la proporción adecuada"), ("Filters the oil", "Filtra el aceite"), ("Cools the engine", "Refrigera el motor")],
  "Today it is giving way to electronic injection.", "Hoy está en desuso frente a la inyección electrónica.")
Q("fu5", "fuel", "How does fuel injection work?", "¿Cómo funciona la inyección?",
  [("A pump injects fuel under pressure, and sensors give each cylinder the exact amount", "Una bomba inyecta combustible a presión y unos sensores dan a cada cilindro la cantidad precisa"), ("The fuel falls by gravity", "El combustible cae por gravedad"), ("It mixes oil and petrol", "Mezcla aceite y gasolina")],
  "The fuel goes into the intake.", "El combustible se inyecta en la conducción de admisión.")
Q("fu6", "fuel", "Which is a maintenance task of the fuel system?", "¿Cuál es una tarea de mantenimiento del sistema de alimentación?",
  [("Clean the carburettor, clean or change the air filter, adjust the idle", "Limpiar el carburador, limpiar o cambiar el filtro del aire y regular el ralentí"), ("Top up the electrolyte", "Reponer el electrolito"), ("Grease the stands", "Engrasar los caballetes")],
  "It avoids excessive fuel use.", "Evita un consumo excesivo.")

# ---------------------------------------------------------------- 1.2–1.3 lubrication and cooling
Q("lu1", "lube", "What is the job of the lubrication system?", "¿Cuál es la misión del sistema de lubricación?",
  [("To put a film of oil between metal parts, reducing friction and wear", "Interponer una película de aceite entre las piezas metálicas para reducir rozamiento y desgaste"), ("To cool the tyres", "Refrigerar los neumáticos"), ("To clean the air", "Limpiar el aire")],
  "It prevents premature wear.", "Evita un desgaste prematuro.")
Q("lu2", "lube", "How should you check the oil level of a four-stroke motorcycle?", "¿Cómo compruebas el nivel de aceite de una moto de cuatro tiempos?",
  [("Engine stopped and cold, motorcycle upright, dipstick between MIN and MAX", "Motor parado y frío, moto en posición horizontal, varilla entre mínimo y máximo"), ("Engine running", "Con el motor en marcha"), ("Right after a long ride, on the side stand", "Recién llegado de un viaje, sobre la pata de cabra")],
  "On the side stand the motorcycle leans and the reading is wrong.", "Sobre la pata de cabra la moto se inclina y la lectura no es fiable.")
Q("lu3", "lube", "When should the oil be changed?", "¿Cuándo debe cambiarse el aceite?",
  [("With the engine warm and the motorcycle upright", "Con el motor caliente y la moto en posición horizontal"), ("With the engine cold and leaning", "Con el motor frío e inclinada"), ("Never: you only top it up", "Nunca: solo se repone")],
  "Warm oil flows out better. Change the filter as the manufacturer says.", "El aceite caliente sale mejor. El filtro, según el fabricante.")
Q("lu4", "lube", "What should you do with the used oil?", "¿Qué debes hacer con el aceite usado?",
  [("Take it to a recycling or collection point", "Llevarlo a un centro de reciclaje o recogida"), ("Pour it down the drain", "Echarlo a la alcantarilla"), ("Pour it on the ground in the countryside", "Verterlo en el campo")],
  "It is highly polluting.", "Es altamente contaminante.")
Q("lu5", "lube", "On a two-stroke motorcycle with a separate oil tank, what must you do?", "En una moto de dos tiempos con depósito de aceite aparte, ¿qué debes hacer?",
  [("Top up the oil tank regularly", "Reponer periódicamente el depósito de aceite"), ("Nothing: it never needs oil", "Nada: nunca necesita aceite"), ("Change the crankcase oil with a dipstick", "Cambiar el aceite del cárter con la varilla")],
  "A pump or dosing device mixes it with the petrol.", "Una bomba o dosificador lo mezcla con la gasolina.")
Q("co1", "lube", "What are the two cooling systems of a motorcycle?", "¿Cuáles son los dos sistemas de refrigeración de una moto?",
  [("By air (direct or forced by a fan) and by liquid", "Por aire (directo o forzado por ventilador) y por líquido"), ("By oil and by water spray", "Por aceite y por pulverización de agua"), ("Only by liquid", "Solo por líquido")],
  "Liquid cooling uses a pump to move the coolant through the engine block.", "La refrigeración por líquido usa una bomba que mueve el líquido por el bloque motor.")
Q("co2", "lube", "What maintenance does air cooling need?", "¿Qué mantenimiento necesita la refrigeración por aire?",
  [("Keep the fins and the turbine’s protective slots clean and in good condition", "Limpiar y mantener las aletas exteriores y las ranuras de la turbina"), ("Top up the coolant", "Reponer el refrigerante"), ("None", "Ninguno")],
  "Dirty fins cool badly.", "Unas aletas sucias refrigeran mal.")
Q("co3", "lube", "What maintenance does liquid cooling need?", "¿Qué mantenimiento necesita la refrigeración por líquido?",
  [("Check the coolant level, and top up or change it as the manufacturer says", "Comprobar el nivel del refrigerante y añadir o cambiar según el fabricante"), ("Clean the fins only", "Solo limpiar las aletas"), ("Grease the radiator", "Engrasar el radiador")],
  "Low coolant is one cause of overheating.", "El refrigerante bajo es una causa de recalentamiento.")

# ---------------------------------------------------------------- 1.4 electrical
Q("el1", "elec", "When does the battery supply the motorcycle’s electrical energy?", "¿Cuándo proporciona la batería la energía eléctrica de la moto?",
  [("While the engine is stopped", "Mientras el motor está parado"), ("Only at high speed", "Solo a alta velocidad"), ("Never: it only stores it", "Nunca: solo la almacena")],
  "With the engine running, the charging system takes over.", "Con el motor en marcha, se encarga el sistema de carga.")
Q("el2", "elec", "What should you add if the battery electrolyte is low?", "¿Qué debes añadir si el electrolito de la batería está bajo?",
  [("Distilled water only", "Solo agua destilada"), ("Sulphuric acid", "Ácido sulfúrico"), ("Tap water", "Agua del grifo")],
  "The electrolyte is sulphuric acid and distilled water. Many batteries today need no maintenance.", "El electrolito es ácido sulfúrico y agua destilada. Hoy muchas baterías no requieren mantenimiento.")
Q("el3", "elec", "What does the starting circuit do?", "¿Qué hace el circuito de arranque?",
  [("A switch turns an electric motor that gives the engine its first turns", "Un interruptor hace girar un motor eléctrico que da los primeros giros al motor"), ("It makes the spark in the cylinder", "Provoca la chispa en el cilindro"), ("It charges the battery", "Carga la batería")],
  "The switch is a button or the ignition key.", "El interruptor es un pulsador o la llave de contacto.")
Q("el4", "elec", "What makes the spark in the cylinder of a petrol engine?", "¿Qué provoca la chispa en el cilindro de un motor de gasolina?",
  [("The spark plug, in the ignition circuit", "La bujía, en el circuito de encendido"), ("The battery directly", "La batería directamente"), ("The carburettor", "El carburador")],
  "The spark ignites the air–fuel mixture.", "La chispa enciende la mezcla de aire y carburante.")
Q("el5", "elec", "What should be kept clean on a battery?", "¿Qué hay que mantener limpio en la batería?",
  [("The terminals and the gas vents", "Los bornes y los orificios de salida de gases"), ("The label", "La etiqueta"), ("Nothing", "Nada")],
  "Also check the spark plugs and the engine tuning.", "También hay que verificar las bujías y la puesta a punto del motor.")

# ---------------------------------------------------------------- 1.5–1.6 transmission, steering, suspension
Q("tr1", "trans", "What does the clutch do?", "¿Qué hace el embrague?",
  [("Connects or cuts the engine’s movement to the gearbox", "Transmite o interrumpe el movimiento del motor a la caja de velocidades"), ("Stops the motorcycle", "Detiene la moto"), ("Changes gear by itself", "Cambia de marcha por sí solo")],
  "The gearbox adapts the pace; the chain, belt or shaft drives the rear wheel.", "La caja adapta la marcha; la cadena, correa o cardan mueve la rueda trasera.")
Q("tr2", "trans", "When is it especially important to grease and tension the chain?", "¿Cuándo es especialmente importante engrasar y tensar la cadena?",
  [("After riding in the rain", "Después de circular con lluvia"), ("After riding at night", "Después de circular de noche"), ("Only at the ITV", "Solo en la ITV")],
  "Water washes the grease away.", "El agua elimina la grasa.")
Q("tr3", "trans", "Which elements can link the gearbox with the rear wheel?", "¿Qué elementos pueden unir la caja de cambios con la rueda trasera?",
  [("Chain, belt or shaft (cardan)", "Cadena, correa o cardan"), ("Only a chain", "Solo una cadena"), ("Gears on the front wheel", "Engranajes en la rueda delantera")],
  "Each needs its own maintenance.", "Cada uno requiere su mantenimiento.")
Q("tr4", "trans", "What maintenance does a shaft drive need, according to your course?", "¿Qué mantenimiento necesita el cardan, según tu curso?",
  [("Minimal: an oil change every 10,000 or 15,000 km", "Mínimo: un cambio de aceite cada 10.000 o 15.000 km"), ("Greasing after every rain", "Engrasarlo tras cada lluvia"), ("Tensioning every week", "Tensarlo cada semana")],
  "Follow the manufacturer’s figure.", "Sigue la cifra del fabricante.")
Q("tr5", "trans", "Where is the chain slack measured?", "¿Dónde se mide la holgura de la cadena?",
  [("In the middle of the lower run, with the wheel on the ground", "En el centro del tramo inferior, con la rueda en el suelo"), ("On the rear sprocket", "En la corona"), ("At the front sprocket, with the engine running", "En el piñón, con el motor en marcha")],
  "Follow the owner’s manual for the figure (usually about 20–30 mm).", "La cifra la da el manual (lo habitual, unos 20–30 mm).")
Q("tr6", "trans", "How should the handlebar be held, and why?", "¿Cómo se maneja el manillar y por qué?",
  [("Firmly but not rigidly: a small movement changes the front wheel’s angle at once", "Con firmeza pero sin rigidez: un pequeño movimiento cambia al instante el ángulo de la rueda delantera"), ("Very tightly, to avoid vibration", "Muy apretado, para evitar vibraciones"), ("With one hand on straights", "Con una mano en las rectas")],
  "The steering-head bearings must have no play and no stiffness.", "Los rodamientos de la tija no deben tener holguras ni agarrotamiento.")
Q("tr7", "trans", "What is the job of the suspension?", "¿Cuál es la misión de la suspensión?",
  [("To keep even contact with the ground and give some comfort", "Asegurar un contacto uniforme con el suelo y dar cierto confort"), ("To brake the rear wheel", "Frenar la rueda trasera"), ("To steer the motorcycle", "Dirigir la moto")],
  "Check the shock absorbers: they affect control.", "Hay que revisar los amortiguadores: afectan al control.")
Q("tr8", "trans", "What does the rear suspension usually use?", "¿Qué suele usar la suspensión trasera?",
  [("A swingarm with shock absorbers", "Una horquilla oscilante (basculante) con amortiguadores"), ("A telescopic fork", "Una horquilla telescópica"), ("Nothing: only the tyre", "Nada: solo el neumático")],
  "The telescopic fork is the front suspension.", "La horquilla telescópica es la suspensión delantera.")

# ---------------------------------------------------------------- 1.7–1.8 accessories, spares, maintenance
Q("ac1", "access", "You fit a new exhaust from another brand. What must it be?", "Instalas un escape nuevo de otra marca. ¿Cómo debe ser?",
  [("Approved (homologado)", "Homologado"), ("From the same manufacturer only", "Solo del mismo fabricante"), ("Anything, if it is quieter", "Cualquiera, si es más silencioso")],
  "Any accessory must be approved, from the manufacturer or another make.", "Cualquier accesorio debe estar homologado, sea del fabricante o de otro.")
Q("ac2", "access", "Which spare parts must a motorcycle carry?", "¿Qué repuestos debe llevar obligatoriamente una moto?",
  [("None", "Ninguno"), ("Spare bulbs", "Lámparas de repuesto"), ("A spare tyre", "Una rueda de repuesto")],
  "Spare bulbs are recommended, not compulsory.", "Las lámparas de repuesto son recomendables, no obligatorias.")
Q("ac3", "access", "Why is it advisable to carry spare bulbs?", "¿Por qué conviene llevar lámparas de repuesto?",
  [("Agents may immobilise the motorcycle if a light is blown", "Los agentes pueden inmovilizar la moto si lleva una luz fundida"), ("They are compulsory", "Son obligatorias"), ("They improve fuel use", "Mejoran el consumo")],
  "It lets you replace a blown bulb at once.", "Permite sustituir enseguida una lámpara fundida.")
Q("ac4", "access", "Since 1 October 2026, what must every motorcycle carry?", "Desde el 1 de octubre de 2026, ¿qué debe llevar toda motocicleta?",
  [("A high-visibility reflective vest", "Un chaleco reflectante de alta visibilidad"), ("A V-16 light", "Una luz V-16"), ("A fire extinguisher", "Un extintor")],
  "Reglamento General de Vehículos, Anexo XII, as amended by RD 518/2026. The V-16 is recommended on motorcycles.", "Reglamento General de Vehículos, anexo XII, reformado por el RD 518/2026. La V-16 es recomendable en moto.")
Q("ac5", "access", "After a major modification such as fitting a sidecar, what is needed?", "Tras una reforma de importancia, como montar un sidecar, ¿qué hace falta?",
  [("An extraordinary ITV inspection before riding again", "Una ITV extraordinaria antes de volver a circular"), ("Nothing, if the parts are approved", "Nada, si las piezas están homologadas"), ("Only tell the insurer", "Solo comunicarlo a la aseguradora")],
  "Topic 9.", "Tema 9.")
Q("ac6", "access", "Which of these can you do yourself with general mechanical knowledge?", "¿Cuál de estas tareas puedes hacer tú con conocimientos mecánicos generales?",
  [("Adjust the chain and clean the air filter", "Ajustar la cadena y limpiar el filtro del aire"), ("Rebuild the gearbox", "Reconstruir la caja de cambios"), ("Reprogram the injection", "Reprogramar la inyección")],
  "Also adjust the pedals, tighten some nuts and bolts and grease the main parts.", "También ajustar los pedales, apretar algunas tuercas y tornillos y engrasar las piezas fundamentales.")
Q("ac7", "access", "After riding in the rain, which of these should you grease?", "Tras circular con lluvia, ¿cuál de estos elementos debes engrasar?",
  [("The chain, the clutch and brake levers, and the stands", "La cadena, las manetas de embrague y frenos y los caballetes"), ("The brake discs", "Los discos de freno"), ("The tyres", "Los neumáticos")],
  "Also the throttle and starter cables, the pedals and the cable ends. Never grease brake discs or tyres.", "También los cables del acelerador y del estárter, los pedales y los extremos de los cables. Nunca se engrasan discos ni neumáticos.")

# ---------------------------------------------------------------- breakdowns
Q("br1", "faults", "The engine won’t start. Which is a possible cause?", "El motor no arranca. ¿Cuál es una posible causa?",
  [("A flat battery or bad connections", "Batería descargada o problema en las conexiones"), ("Worn tyres", "Neumáticos gastados"), ("A loose mirror", "Un espejo suelto")],
  "Also a spark plug in poor condition, no fuel, or a faulty starter button or key.", "También bujía en malas condiciones, que no llegue combustible o fallo en el pulsador o la llave.")
Q("br2", "faults", "The clutch is hard to disengage. What may be the cause?", "Cuesta desembragar. ¿Cuál puede ser la causa?",
  [("Oil in poor condition, too thick, or too much oil", "Aceite en mal estado, muy viscoso o exceso de nivel"), ("Low tyre pressure", "Poca presión en los neumáticos"), ("A dirty visor", "Una visera sucia")],
  "On many motorcycles the clutch works in the engine oil.", "En muchas motos el embrague trabaja en el aceite del motor.")
Q("br3", "faults", "The exhaust gives off bluish-white smoke. What does it mean?", "El escape echa humo blanco azulado. ¿Qué indica?",
  [("The engine is burning too much oil", "Consumo excesivo de aceite"), ("Too much fuel", "Consumo excesivo de combustible"), ("Condensed water evaporating", "Evaporación del agua condensada")],
  "Black smoke: too much fuel. White: condensed water.", "Humo negro: exceso de combustible. Blanco: agua condensada.")
Q("br4", "faults", "What does black exhaust smoke indicate?", "¿Qué indica el humo negro del escape?",
  [("Excessive fuel consumption", "Consumo excesivo de combustible"), ("Excessive oil consumption", "Consumo excesivo de aceite"), ("A cold morning", "Una mañana fría")],
  "Too much fuel or too little air.", "Exceso de combustible o falta de aire.")
Q("br5", "faults", "White smoke when you start on a cold morning. What is it?", "Humo blanco al arrancar una mañana fría. ¿Qué es?",
  [("Condensed water in the exhaust evaporating", "Evaporación del agua condensada en el tubo de escape"), ("A serious oil leak", "Una fuga grave de aceite"), ("Too much fuel", "Exceso de combustible")],
  "If it goes on with the engine warm, have it checked.", "Si sigue con el motor caliente, hay que revisarlo.")
Q("br6", "faults", "The motorcycle feels unstable. Which is a possible cause?", "La moto va inestable. ¿Cuál es una posible causa?",
  [("Low tyre pressure, a misaligned wheel, a bent rim or a steering head too tight", "Poca presión, rueda desalineada, llanta torcida o tija de dirección demasiado apretada"), ("A dirty air filter", "Un filtro del aire sucio"), ("A flat battery", "Una batería descargada")],
  "Also uneven tyre wear.", "También un desgaste desigual de los neumáticos.")
Q("br7", "faults", "The engine overheats. Which is a possible cause?", "El motor se recalienta. ¿Cuál es una posible causa?",
  [("Low coolant level", "Nivel de refrigerante bajo"), ("New tyres", "Neumáticos nuevos"), ("A full fuel tank", "El depósito lleno")],
  "Also a wrong or dirty spark plug, a dirty air filter, lubrication problems or a low float-bowl level.", "También bujía inapropiada o sucia, filtro del aire en mal estado, problemas de lubricación o nivel bajo en la cuba del carburador.")
Q("br8", "faults", "The engine runs badly at low speed. What may be wrong?", "El motor falla a baja velocidad. ¿Qué puede ocurrir?",
  [("The air filter is blocked or the carburettor is dirty", "El filtro del aire está obstruido o el carburador sucio"), ("The tyres are too hard", "Los neumáticos están muy duros"), ("The chain is too greased", "La cadena tiene demasiada grasa")],
  "Or the air–petrol mixture is wrong.", "O la mezcla de aire y gasolina es incorrecta.")
Q("br9", "faults", "The motorcycle loses power at high speed. Which is a possible cause?", "La moto pierde potencia a alta velocidad. ¿Cuál es una posible causa?",
  [("A dragging brake or a dirty spark plug", "Rozamiento del freno o una bujía sucia"), ("A loose mirror", "Un espejo suelto"), ("A new battery", "Una batería nueva")],
  "Also a dirty air filter, blocked jets, a wrong fuel level in the carburettor, or pre-ignition.", "También filtro del aire en mal estado, surtidor atascado, nivel inadecuado en el carburador o autoencendido.")

# ---------------------------------------------------------------- more questions
Q("en8", "engine", "What are the four phases of the engine cycle?", "¿Cuáles son las cuatro fases del ciclo del motor?",
  [("Intake, compression, explosion and exhaust", "Admisión, compresión, explosión y escape"), ("Start, run, brake and stop", "Arranque, marcha, frenada y parada"), ("Fuel, oil, water and air", "Combustible, aceite, agua y aire")],
  "A two-stroke does them in two piston movements, a four-stroke in four.", "El de dos tiempos las hace en dos movimientos del pistón; el de cuatro, en cuatro.")
Q("en9", "engine", "In a four-stroke engine, what is the fuel mixture made of?", "En un motor de cuatro tiempos, ¿de qué se compone la mezcla de combustible?",
  [("Air and petrol", "Aire y gasolina"), ("Air, petrol and oil", "Aire, gasolina y aceite"), ("Petrol and water", "Gasolina y agua")],
  "Its oil stays in the crankcase. Your course’s introduction has this the wrong way round.", "Su aceite se queda en el cárter. La introducción de tu curso lo dice al revés.")
Q("fu7", "fuel", "Which system is replacing the carburettor on modern motorcycles?", "¿Qué sistema está sustituyendo al carburador en las motos modernas?",
  [("Electronic injection", "La inyección electrónica"), ("The turbine", "La turbina"), ("The cardan", "El cardan")],
  "Sensors give each cylinder the exact amount of fuel.", "Unos sensores dan a cada cilindro la cantidad precisa de combustible.")
Q("lu6", "lube", "Why check the oil with the motorcycle upright rather than on its side stand?", "¿Por qué comprobar el aceite con la moto vertical y no sobre la pata de cabra?",
  [("Leaning, the level reads wrong", "Inclinada, el nivel se lee mal"), ("The engine could start", "El motor podría arrancar"), ("It makes no difference", "Da igual")],
  "Your course says ‘horizontal position’: the motorcycle upright, for example on the centre stand.", "Tu curso dice «posición horizontal»: la moto vertical, por ejemplo sobre el caballete.")
Q("co4", "lube", "In forced-air cooling, what moves the air?", "En la refrigeración por aire forzado, ¿qué mueve el aire?",
  [("A fan or turbine driven by the engine", "Un ventilador o turbina que recibe el movimiento del motor"), ("The coolant pump", "La bomba del refrigerante"), ("The rider’s body", "El cuerpo del conductor")],
  "Direct air cooling relies on the motorcycle’s movement.", "La refrigeración por aire directo se basa en el movimiento de la moto.")
Q("el6", "elec", "What is battery electrolyte made of?", "¿De qué se compone el electrolito de la batería?",
  [("Sulphuric acid and distilled water", "Ácido sulfúrico y agua destilada"), ("Engine oil", "Aceite de motor"), ("Coolant", "Líquido refrigerante")],
  "Top it up with distilled water only.", "Se repone solo con agua destilada.")
Q("el7", "elec", "Do all batteries need their electrolyte checked?", "¿Hay que comprobar el electrolito de todas las baterías?",
  [("No: many batteries today are maintenance-free", "No: hoy muchas baterías no requieren mantenimiento"), ("Yes, every week", "Sí, cada semana"), ("Only electric motorcycles have batteries", "Solo las motos eléctricas tienen batería")],
  "Where it is needed, check the level regularly.", "Cuando haga falta, se comprueba periódicamente.")
Q("tr9", "trans", "What does the gearbox do?", "¿Qué hace la caja de cambios?",
  [("Adapts the motorcycle’s pace to what is needed", "Permite adaptar la marcha del vehículo según convenga"), ("Cuts the engine off from the wheel", "Desconecta el motor de la rueda"), ("Cools the clutch", "Refrigera el embrague")],
  "Check its lubrication regularly.", "Hay que verificar su lubricado periódicamente.")
Q("tr10", "trans", "What can a chain that is too tight do?", "¿Qué puede provocar una cadena demasiado tensa?",
  [("Wear the chain, sprockets and bearings", "Desgastar la cadena, los piñones y los rodamientos"), ("Improve braking", "Mejorar la frenada"), ("Nothing", "Nada")],
  "That is why the slack follows the owner’s manual (usually about 20–30 mm).", "Por eso la holgura se ajusta según el manual (lo habitual, unos 20–30 mm).")
Q("ac8", "access", "Which of these accessories must be approved if you fit it?", "¿Cuál de estos accesorios debe estar homologado si lo instalas?",
  [("All of them: racks, fairings, mirrors, exhausts, shock absorbers…", "Todos: portaequipajes, carenados, retrovisores, escapes, amortiguadores…"), ("Only the exhaust", "Solo el escape"), ("None, if the manufacturer made it", "Ninguno, si es del fabricante")],
  "Whether it is the manufacturer’s or another make.", "Sea del propio fabricante u otro.")
Q("ac9", "access", "Which nuts and bolts can you check yourself?", "¿Qué tuercas y tornillos puedes revisar tú mismo?",
  [("The axle fixings, the steering head, the rear shock and the footrests", "Las fijaciones de los ejes, la tija de dirección, el amortiguador trasero y las estriberas"), ("The cylinder head bolts", "Los tornillos de la culata"), ("None: only a workshop can", "Ninguno: solo un taller")],
  "With general mechanical knowledge, without a specialist workshop.", "Con conocimientos mecánicos generales, sin acudir a un taller especializado.")
Q("br10", "faults", "Which fault can cause both loss of power and overheating?", "¿Qué fallo puede causar a la vez falta de potencia y recalentamiento?",
  [("A wrong, dirty, broken or badly gapped spark plug", "Una bujía inapropiada, sucia, rota o mal ajustada"), ("Low tyre pressure", "Poca presión en los neumáticos"), ("A loose mirror", "Un espejo suelto")],
  "A dirty air filter also appears in both lists.", "El filtro del aire en mal estado también aparece en las dos listas.")
Q("br11", "faults", "Which of these can make the steering feel heavy and the motorcycle unstable?", "¿Cuál de estos fallos puede hacer la dirección pesada y la moto inestable?",
  [("A steering head that is too tight", "Una tija de dirección demasiado apretada"), ("A full fuel tank", "Un depósito lleno"), ("New brake pads", "Pastillas de freno nuevas")],
  "The steering bearings must have no play and no stiffness.", "Los rodamientos de la dirección no deben tener holguras ni agarrotamiento.")
