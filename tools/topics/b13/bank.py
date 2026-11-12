# -*- coding: utf-8 -*-
"""Question bank for the interactive Topic 13 page (vehicle maintenance and accessories). In every question the FIRST
option is the correct one (the page shuffles options when it shows them). Ids must be unique and must not start with "ai"."""

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
    "engine": dict(sec=1, en="Maintenance and the engine", es="Mantenimiento y motor",
        recap=[("Good maintenance makes the car last, prevents failures, saves fuel and cuts pollution.", "Un buen mantenimiento alarga la vida útil, previene averías, ahorra combustible y reduce la contaminación."),
               ("Many breakdowns come from no, poor or wrong maintenance. Vehicle factor: 4–13 % of accidents.", "Muchas averías vienen de un mantenimiento nulo, deficiente o equivocado. Factor vehículo: 4–13 % de los accidentes."),
               ("White smoke on a cold start: water vapour, no fault. Bluish: burning oil.", "Humo blanco al arrancar en frío: vapor de agua, no es avería. Azulado: consume aceite."),
               ("Black smoke: too much fuel or too little air — more consumption and pollution.", "Humo negro: exceso de carburante o falta de aire; más consumo y contaminación.")],
        trap=("Thinking white smoke on a cold morning means a breakdown.", "Pensar que el humo blanco una mañana fría indica avería.")),
    "fuel": dict(sec=2, en="Fuel and air supply", es="Alimentación",
        recap=[("Delivers air and fuel to the cylinders.", "Hace llegar aire y combustible a los cilindros."),
               ("A clogged air filter raises fuel use and pollution; it gets dirtier in summer.", "Un filtro de aire obstruido aumenta consumo y contaminación; se ensucia más en verano."),
               ("Replace air and fuel filters as the maker says.", "Sustituir los filtros de aire y combustible según el fabricante."),
               ("Idle too high: more fuel; too low: the engine stalls.", "Ralentí demasiado alto: más consumo; demasiado bajo: el motor se cala.")],
        trap=("Thinking a low idle saves fuel without any problem.", "Pensar que un ralentí bajo ahorra sin ningún problema.")),
    "exhaust": dict(sec=2, en="Exhaust", es="Escape",
        recap=[("Takes the combustion gases to the rear of the car.", "Lleva los gases de la combustión a la parte trasera."),
               ("Silencer: less noise and cooler gases. Catalyst: cuts toxic gases almost completely.", "Silenciador: menos ruido y gases menos calientes. Catalizador: reduce casi por completo los gases tóxicos."),
               ("Catalyst about every 150,000 km; damaged by burning oil, running the tank empty, knocks underneath.", "Catalizador cada 150.000 km aprox.; lo dañan el consumo de aceite, apurar el depósito y los golpes en los bajos."),
               ("No silencer or a faulty one: driving prohibited, in and out of town (except electric vehicles).", "Sin silenciador o defectuoso: prohibido circular, en poblado y fuera (salvo eléctricos).")],
        trap=("Thinking driving without a silencer is allowed out of town.", "Pensar que sin silenciador se puede circular fuera de poblado.")),
    "lube": dict(sec=2, en="Lubrication and oil", es="Lubricación y aceite",
        recap=[("An oil film reduces friction and wear between metal parts.", "Una película de aceite reduce el rozamiento y el desgaste entre piezas metálicas."),
               ("Red oil-pressure light: pressure below minimum — stop the engine quickly.", "Testigo rojo de presión de aceite: por debajo del mínimo; parar el motor rápidamente."),
               ("Check the level cold and level, between MIN and MAX; change it warm, through the sump plug.", "Comprobar el nivel en frío y en llano, entre MIN y MAX; cambiarlo en caliente, por el tapón del cárter."),
               ("SAE 10W-60: 10W winter (cold), 60 hot. Never change oil on the street.", "SAE 10W-60: 10W invierno (frío), 60 caliente. Nunca cambiar el aceite en la vía pública.")],
        trap=("Checking the oil with the engine hot.", "Comprobar el aceite con el motor caliente.")),
    "cooling": dict(sec=2, en="Cooling", es="Refrigeración",
        recap=[("Coolant (distilled water with antifreeze) carries the engine’s heat to the radiator.", "El refrigerante (agua destilada con anticongelante) lleva el calor del motor al radiador."),
               ("Check cold, between MIN and MAX on the expansion tank; course: top up with distilled water.", "Comprobar en frío, entre MIN y MAX del vaso de expansión; curso: rellenar con agua destilada."),
               ("Change about every 2 years; watch for leaks; antifreeze for very low temperatures.", "Cambiar cada 2 años aprox.; vigilar fugas; anticongelante para temperaturas muy bajas."),
               ("Never open the expansion tank with the engine hot.", "Nunca abrir el vaso de expansión con el motor caliente.")],
        trap=("Opening the expansion tank to check it right after a drive.", "Abrir el vaso de expansión justo después de un viaje.")),
    "battery": dict(sec=3, en="The battery", es="La batería",
        recap=[("Gives electricity with the engine stopped.", "Proporciona energía con el motor parado."),
               ("Cells with lead plates in distilled water and sulphuric acid (electrolyte); terminals outside.", "Vasos con placas de plomo en agua destilada y ácido sulfúrico (electrolito); bornes fuera."),
               ("The electrolyte must cover the plates; top up with distilled water only.", "El electrolito debe cubrir las placas; añadir solo agua destilada."),
               ("Terminals tight, clean and greased; low-maintenance: check every 6 months; maintenance-free: no need.", "Bornes apretados, limpios y engrasados; bajo mantenimiento: cada 6 meses; sin mantenimiento: no hace falta.")],
        trap=("Topping up a battery with acid or tap water.", "Rellenar la batería con ácido o agua del grifo.")),
    "electric": dict(sec=3, en="Charging, starting, ignition and lights", es="Carga, arranque, encendido y luces",
        recap=[("The alternator, driven by a belt, recharges the battery with the engine running.", "El alternador, movido por una correa, recarga la batería con el motor en marcha."),
               ("Charge light on: broken belt or worn brushes. Irregular charging: low electrolyte.", "Testigo de carga encendido: correa rota o escobillas gastadas. Carga irregular: electrolito bajo."),
               ("Starter: don’t keep trying. Doesn’t turn and lights go out: flat battery; turns slowly: low battery or bad connections.", "Arranque: no insistir. No gira y se apagan las luces: batería descargada; gira despacio: batería baja o malas conexiones."),
               ("Spark plugs (petrol): a bad one wastes fuel and pollutes. Pair of lamps out: bulbs, fuse or switch. Xenon: specialists.", "Bujías (gasolina): una en mal estado gasta y contamina. Un par de lámparas apagadas: lámparas, fusible o interruptor. Xenón: especialistas.")],
        trap=("Thinking diesel engines have spark plugs.", "Pensar que los motores diésel llevan bujías.")),
    "trans": dict(sec=4, en="Transmission", es="Transmisión",
        recap=[("Takes the engine’s force to the driving wheels: front (traction), rear (propulsion), all (4×4).", "Lleva la fuerza del motor a las ruedas motrices: delanteras (tracción), traseras (propulsión), todas (4×4)."),
               ("Clutch between engine and gearbox; gearbox; differential lets the wheels turn at different speeds.", "Embrague entre motor y caja de cambios; caja de cambios; el diferencial permite que las ruedas giren a distinta velocidad."),
               ("Riding the clutch damages it. Speed not rising with revs: slipping clutch (worn linings).", "Ir a medio embrague lo daña. La velocidad no sube con las revoluciones: patina el embrague (forros gastados)."),
               ("Gears hard to engage: gearbox fault, maybe wrong oil level. Press the clutch fully to change gear.", "Marchas que entran con dificultad: avería de la caja, quizá nivel de aceite. Pisar el embrague a fondo para cambiar.")],
        trap=("Calling a rear-wheel-drive car a ‘traction’ vehicle.", "Llamar «de tracción» a un vehículo con las ruedas traseras motrices.")),
    "equip": dict(sec=5, en="Compulsory equipment", es="Dotación obligatoria",
        recap=[("Cars and goods/mixed up to 3,500 kg: V-16, certified vest, spare or temporary wheel + tools, or an alternative system.", "Turismos y mixtos/mercancías hasta 3.500 kg: V-16, chaleco certificado, rueda de repuesto o temporal + herramientas, o sistema alternativo."),
               ("Buses, heavy over 3,500 kg and combinations: V-16, vest and an approved extinguisher.", "Autobuses, pesados de más de 3.500 kg y conjuntos: V-16, chaleco y extintor homologado."),
               ("Motorcycles: a vest (since 1 October 2026). Professional riders wear it on all roads.", "Motocicletas: chaleco (desde el 1 de octubre de 2026). Los profesionales lo llevan en todas las vías."),
               ("Vest: yellow, orange-red or red; worn on interurban carriageway or shoulder; kept out of the light but within reach.", "Chaleco: amarillo, rojo anaranjado o rojo; en calzada o arcén de interurbanas; guardado sin luz pero accesible.")],
        trap=("Thinking lorries must carry a spare wheel by law.", "Pensar que los camiones deben llevar por ley rueda de repuesto.")),
}

# ---------------------------------------------------------------- 1. engine and maintenance
Q("en1", "engine", "Correct maintenance of the vehicle…", "Un correcto mantenimiento del vehículo…",
  [("makes it last longer, prevents failures, saves fuel and pollutes less", "alarga su vida, previene averías, ahorra combustible y contamina menos"), ("only matters for the ITV", "solo importa para la ITV"), ("increases fuel use", "aumenta el consumo")],
  "Above all the maintenance the manufacturer sets.", "Sobre todo el establecido por el fabricante.")
Q("en2", "engine", "On a cold morning, white smoke comes out of the exhaust when you start. It is…", "Una mañana fría sale humo blanco del escape al arrancar. Es…",
  [("water vapour — not a fault", "vapor de agua, no es avería"), ("burning oil", "aceite quemado"), ("too much fuel", "exceso de carburante")],
  "If it goes on with the engine warm, have it checked.", "Si sigue con el motor caliente, hay que revisarlo.")
Q("en3", "engine", "Bluish-white smoke from the exhaust means…", "El humo blanco azulado por el escape indica…",
  [("the engine is burning too much oil", "que el motor consume demasiado aceite"), ("water vapour", "vapor de agua"), ("a dirty air filter only", "solo un filtro de aire sucio")],
  "Excess oil can also damage the catalyst.", "El exceso de aceite también puede dañar el catalizador.")
Q("en4", "engine", "Black smoke from the exhaust means…", "El humo negro por el escape indica…",
  [("too much fuel or too little air", "exceso de carburante o falta de aire"), ("burning oil", "consumo de aceite"), ("a cold engine", "motor frío")],
  "Unbalanced combustion: more fuel use and pollution.", "Combustión desequilibrada: más consumo y contaminación.")
Q("en5", "engine", "Many breakdowns are due to…", "Gran parte de las averías se deben a…",
  [("no, poor or wrong maintenance by the driver", "un mantenimiento nulo, deficiente o equivocado del conductor"), ("bad luck", "la mala suerte"), ("the weather", "el clima")],
  "And they can be avoided.", "Y se pueden evitar.")
Q("en6", "engine", "Most vehicles today use…", "La mayoría de los vehículos actuales usan…",
  [("heat engines burning petrol or diesel", "motores térmicos de gasolina o gasóleo"), ("only electric motors", "solo motores eléctricos"), ("hydrogen only", "solo hidrógeno")],
  "Electric, hybrid and hydrogen are growing.", "Crecen los eléctricos, híbridos y de hidrógeno.")
Q("en7", "engine", "In what share of accidents is the vehicle the cause?", "¿En qué porcentaje de accidentes el vehículo es la causa?",
  [("4–13 %", "4–13 %"), ("70–90 %", "70–90 %"), ("50 %", "50 %")],
  "The driver: 70–90 %.", "El conductor: 70–90 %.")

# ---------------------------------------------------------------- 2.1 fuel and air
Q("fu1", "fuel", "The fuel-supply system…", "El sistema de alimentación…",
  [("delivers air and fuel to the cylinders", "hace llegar aire y combustible a los cilindros"), ("cools the engine", "refrigera el motor"), ("charges the battery", "carga la batería")],
  "Air circuit and fuel circuit.", "Circuito de aire y de carburante.")
Q("fu2", "fuel", "A clogged air filter causes…", "Un filtro de aire obstruido provoca…",
  [("more fuel use and more pollution", "más consumo y más contaminación"), ("less fuel use", "menos consumo"), ("nothing", "nada")],
  "Replace it as the maker says.", "Sustituirlo según el fabricante.")
Q("fu3", "fuel", "The air filter usually gets dirtier in…", "El filtro de aire suele ensuciarse más en…",
  [("summer", "verano"), ("winter", "invierno"), ("rainy weather", "tiempo lluvioso")],
  "More dust.", "Más polvo.")
Q("fu4", "fuel", "The ‘idle’ (ralentí) is…", "El ralentí es…",
  [("the engine running with the car stopped, in neutral or with the clutch pressed", "el motor en marcha con el coche parado, en punto muerto o con el embrague pisado"), ("the top speed", "la velocidad máxima"), ("the engine switched off", "el motor apagado")],
  "Check it if fuel use rises.", "Revisarlo si sube el consumo.")
Q("fu5", "fuel", "If the idle speed is too low…", "Si el ralentí está demasiado bajo…",
  [("the engine can stall", "el motor se puede calar"), ("fuel use rises a lot", "el consumo sube mucho"), ("the battery overcharges", "la batería se sobrecarga")],
  "Too high: more fuel.", "Demasiado alto: más consumo.")
Q("fu6", "fuel", "Fuel use has gone up. One thing to check is…", "Ha aumentado el consumo. Algo que conviene revisar es…",
  [("the idle speed, which may be too high", "el ralentí, que puede estar demasiado alto"), ("the horn", "la bocina"), ("the seat belts", "los cinturones")],
  "And the air filter.", "Y el filtro de aire.")
Q("fu7", "fuel", "When should the fuel filter be replaced?", "¿Cuándo se sustituye el filtro de combustible?",
  [("When the manufacturer says", "Cuando lo indique el fabricante"), ("Never", "Nunca"), ("Every month", "Cada mes")],
  "Follow the maintenance plan.", "Según el plan de mantenimiento.")

# ---------------------------------------------------------------- 2.2 exhaust
Q("ex1", "exhaust", "The exhaust system…", "El sistema de escape…",
  [("takes the combustion gases to the rear of the vehicle", "lleva los gases de la combustión a la parte trasera"), ("brings fresh air into the engine", "introduce aire en el motor"), ("cools the brakes", "refrigera los frenos")],
  "And reduces their harm.", "Y reduce sus daños.")
Q("ex2", "exhaust", "The silencer…", "El silenciador…",
  [("lowers the noise and keeps gases from coming out too hot", "disminuye el ruido y evita que los gases salgan muy calientes"), ("cuts toxic gases", "reduce los gases tóxicos"), ("filters the fuel", "filtra el combustible")],
  "The catalyst cuts toxic gases.", "El catalizador reduce los gases tóxicos.")
Q("ex3", "exhaust", "The catalytic converter…", "El catalizador…",
  [("cuts the toxic gases almost completely", "reduce los gases tóxicos casi por completo"), ("lowers the noise", "disminuye el ruido"), ("cools the engine", "refrigera el motor")],
  "Replace it about every 150,000 km.", "Sustituirlo cada 150.000 km aprox.")
Q("ex4", "exhaust", "According to your course, the catalyst should be replaced about every…", "Según tu curso, el catalizador se sustituye aproximadamente cada…",
  [("150,000 km", "150.000 km"), ("15,000 km", "15.000 km"), ("500,000 km", "500.000 km")],
  "Avoid knocks underneath.", "Evitar golpes en los bajos.")
Q("ex5", "exhaust", "What can damage the catalyst?", "¿Qué puede dañar el catalizador?",
  [("Burning too much oil, or regularly running the tank almost empty", "Un consumo excesivo de aceite o apurar regularmente el depósito"), ("Washing the car", "Lavar el coche"), ("Using the air conditioning", "Usar el aire acondicionado")],
  "Also knocks underneath.", "También los golpes en los bajos.")
Q("ex6", "exhaust", "Driving with no silencer, or a faulty one, is…", "Circular sin silenciador o con uno defectuoso…",
  [("prohibited in town and out of town", "está prohibido en poblado y fuera"), ("allowed out of town", "se permite fuera de poblado"), ("allowed at night", "se permite de noche")],
  "Except electric vehicles.", "Salvo vehículos eléctricos.")
Q("ex7", "exhaust", "Which vehicles do not need a silencer?", "¿Qué vehículos no necesitan silenciador?",
  [("Electric vehicles", "Los eléctricos"), ("Mopeds", "Los ciclomotores"), ("Diesel cars", "Los turismos diésel")],
  "They have no combustion explosions.", "No tienen explosiones de combustión.")

# ---------------------------------------------------------------- 2.3 lubrication
Q("lu1", "lube", "The lubrication system…", "El sistema de lubricación…",
  [("puts a film of oil between metal parts to reduce friction and wear", "interpone una película de aceite entre las piezas para reducir rozamiento y desgaste"), ("cools the coolant", "enfría el refrigerante"), ("feeds the spark plugs", "alimenta las bujías")],
  "Avoids early wear.", "Evita un desgaste prematuro.")
Q("lu2", "lube", "The red oil-pressure light comes on while driving. You should…", "Se enciende el testigo rojo de presión de aceite. Hay que…",
  [("stop the engine quickly", "detener el motor rápidamente"), ("carry on to the next service", "seguir hasta la próxima revisión"), ("speed up", "acelerar")],
  "The pressure is below the minimum.", "La presión está por debajo del mínimo.")
Q("lu3", "lube", "To check the oil level, the engine should be…", "Para comprobar el nivel de aceite, el motor debe estar…",
  [("stopped and cold, with the car level", "parado y frío, con el coche en llano"), ("running and hot", "en marcha y caliente"), ("running at idle", "al ralentí")],
  "Use the dipstick.", "Con la varilla indicadora.")
Q("lu4", "lube", "On the dipstick, the oil should be…", "En la varilla, el aceite debe estar…",
  [("between the MIN and MAX marks", "entre las marcas de mínimo y máximo"), ("above MAX", "por encima del máximo"), ("below MIN", "por debajo del mínimo")],
  "Pull out, wipe, put back, pull out again and read.", "Sacar, limpiar, volver a meter, sacar y leer.")
Q("lu5", "lube", "The oil is best changed with the engine…", "El cambio de aceite se hace mejor con el motor…",
  [("warm, because the oil flows better", "caliente, porque el aceite es más fluido"), ("cold", "frío"), ("running", "en marcha")],
  "With the car level.", "Con el coche en llano.")
Q("lu6", "lube", "Used engine oil is drained through…", "El aceite usado se vacía por…",
  [("the drain plug at the bottom of the sump", "el tapón de vaciado de la parte inferior del cárter"), ("the dipstick tube", "el tubo de la varilla"), ("the radiator", "el radiador")],
  "Refill through the cap on top.", "Se rellena por el tapón superior.")
Q("lu7", "lube", "In an oil marked SAE 10W-60, the ‘W’ means…", "En un aceite SAE 10W-60, la «W» significa…",
  [("winter: the first number is for the cold", "winter (invierno): el primer número es para frío"), ("weight", "peso"), ("water", "agua")],
  "The second number is for hot temperatures.", "El segundo número, para temperaturas altas.")
Q("lu8", "lube", "A multigrade oil…", "Un aceite multigrado…",
  [("has two viscosity grades, one for cold and one for hot", "tiene dos grados de viscosidad, para frío y para caliente"), ("only works in winter", "solo sirve en invierno"), ("never needs changing", "no hay que cambiarlo nunca")],
  "Low number = fluid, high = viscous.", "Número bajo = fluido; alto = viscoso.")
Q("lu9", "lube", "May you change your car’s oil in the street?", "¿Puedes cambiar el aceite de tu coche en la calle?",
  [("No: it is very polluting; take the oil to a recovery container", "No: es muy contaminante; se entrega en un contenedor de recuperación"), ("Yes, if you are careful", "Sí, con cuidado"), ("Yes, at night", "Sí, de noche")],
  "Never on the public road.", "Nunca en la vía pública.")
Q("lu10", "lube", "The oil filter should be replaced…", "El filtro de aceite se sustituye…",
  [("as the manufacturer says", "según indique el fabricante"), ("never", "nunca"), ("only at the ITV", "solo en la ITV")],
  "Usually with the oil change.", "Normalmente con el cambio de aceite.")

# ---------------------------------------------------------------- 2.4 cooling
Q("co1", "cooling", "The cooling system…", "El sistema de refrigeración…",
  [("gets rid of part of the heat the engine produces", "expulsa parte del calor que produce el motor"), ("lubricates the engine", "lubrica el motor"), ("supplies fuel", "aporta combustible")],
  "With a coolant flowing through the engine and radiator.", "Con un refrigerante que circula por el motor y el radiador.")
Q("co2", "cooling", "The coolant level is checked…", "El nivel del refrigerante se comprueba…",
  [("with the engine cold, on the expansion tank, between MIN and MAX", "con el motor frío, en el vaso de expansión, entre MIN y MAX"), ("with the engine hot, opening the radiator", "con el motor caliente, abriendo el radiador"), ("on the dipstick", "en la varilla del aceite")],
  "Never open the tank hot.", "Nunca abrir el vaso en caliente.")
Q("co3", "cooling", "Can you open the expansion tank with the engine hot?", "¿Se puede abrir el vaso de expansión con el motor caliente?",
  [("Never", "Nunca"), ("Yes, slowly", "Sí, despacio"), ("Yes, if the level is low", "Sí, si el nivel está bajo")],
  "The hot coolant is under pressure.", "El refrigerante caliente está a presión.")
Q("co4", "cooling", "Engine coolant is made of…", "El líquido refrigerante está formado por…",
  [("distilled water mixed with antifreeze additives", "agua destilada mezclada con aditivos anticongelantes"), ("engine oil", "aceite de motor"), ("brake fluid", "líquido de frenos")],
  "Add antifreeze for very low temperatures.", "Añadir anticongelante para temperaturas muy bajas.")
Q("co5", "cooling", "According to your course, the coolant should be changed about every…", "Según tu curso, el refrigerante se cambia aproximadamente cada…",
  [("2 years", "2 años"), ("month", "mes"), ("10 years", "10 años")],
  "As the manufacturer says.", "Según el fabricante.")
Q("co6", "cooling", "According to your course, if the coolant level is low you top it up with…", "Según tu curso, si el nivel de refrigerante está bajo se rellena con…",
  [("distilled water", "agua destilada"), ("engine oil", "aceite de motor"), ("sea water", "agua de mar")],
  "Many makers ask for the same coolant mixture.", "Muchos fabricantes piden la misma mezcla de refrigerante.")
Q("co7", "cooling", "Before very cold weather it is advisable to…", "Antes de un periodo de mucho frío conviene…",
  [("add antifreeze", "añadir anticongelante"), ("empty the radiator", "vaciar el radiador"), ("remove the thermostat", "quitar el termostato")],
  "And check for leaks.", "Y revisar posibles fugas.")

# ---------------------------------------------------------------- 3.1 battery
Q("ba1", "battery", "The battery supplies electricity…", "La batería proporciona energía eléctrica…",
  [("while the engine is stopped", "mientras el motor está parado"), ("only while driving", "solo en marcha"), ("only to the radio", "solo a la radio")],
  "With the engine running, the alternator does it.", "Con el motor en marcha, lo hace el alternador.")
Q("ba2", "battery", "To top up a battery’s electrolyte you add…", "Para reponer el electrolito de la batería se añade…",
  [("distilled water only", "exclusivamente agua destilada"), ("sulphuric acid", "ácido sulfúrico"), ("tap water", "agua del grifo")],
  "The liquid must cover the plates.", "El líquido debe cubrir las placas.")
Q("ba3", "battery", "The battery’s electrolyte is…", "El electrolito de la batería es…",
  [("distilled water mixed with sulphuric acid", "agua destilada con ácido sulfúrico"), ("engine oil", "aceite de motor"), ("antifreeze", "anticongelante")],
  "In cells with lead plates.", "En vasos con placas de plomo.")
Q("ba4", "battery", "The battery terminals should be…", "Los bornes de la batería deben estar…",
  [("tight, clean and greased", "apretados, limpios y engrasados"), ("loose", "flojos"), ("painted", "pintados")],
  "Petroleum jelly or soft grease against sulphation.", "Vaselina o grasa blanda contra la sulfatación.")
Q("ba5", "battery", "A low-maintenance battery’s liquid level should be checked about every…", "En una batería de bajo mantenimiento, el nivel se revisa aproximadamente cada…",
  [("6 months", "6 meses"), ("week", "semana"), ("5 years", "5 años")],
  "Maintenance-free batteries don’t need it.", "Las sin mantenimiento no lo necesitan.")
Q("ba6", "battery", "Inside the battery, the electrolyte must always…", "Dentro de la batería, el electrolito debe siempre…",
  [("cover the plates", "cubrir las placas"), ("be below the plates", "estar por debajo de las placas"), ("be empty", "estar vacío")],
  "Check the level.", "Comprobar el nivel.")

# ---------------------------------------------------------------- 3.2–3.5 electrics
Q("el1", "electric", "The alternator…", "El alternador…",
  [("turns the engine’s movement into electricity and recharges the battery", "transforma el movimiento del motor en electricidad y recarga la batería"), ("starts the engine", "arranca el motor"), ("makes the spark", "produce la chispa")],
  "Driven by a belt.", "Movido por una correa.")
Q("el2", "electric", "The battery-charge warning light comes on. The likely cause is…", "Se enciende el testigo de carga de la batería. La causa probable es…",
  [("a broken belt or worn brushes in the alternator", "correa rota o escobillas desgastadas del alternador"), ("low oil", "poco aceite"), ("a blown headlight bulb", "una lámpara fundida")],
  "The alternator isn’t charging enough.", "El alternador no carga lo suficiente.")
Q("el3", "electric", "When you turn the key the engine doesn’t turn, or very slowly, and the lights go out. The cause is…", "Al accionar el arranque el motor no gira, o muy despacio, y las luces se apagan. La causa es…",
  [("a flat or nearly flat battery", "la batería descargada o con muy poca carga"), ("too much oil", "exceso de aceite"), ("a dirty air filter", "el filtro de aire sucio")],
  "Check the terminals, recharge or replace it.", "Comprobar los bornes, recargarla o sustituirla.")
Q("el4", "electric", "When starting, you should not…", "Al arrancar no se debe…",
  [("keep the starter running too long", "insistir demasiado con el arranque"), ("press the clutch", "pisar el embrague"), ("check the lights", "mirar los testigos")],
  "It can flatten the battery.", "Podría descargar la batería.")
Q("el5", "electric", "The starter motor is fed by…", "El motor de arranque recibe la corriente de…",
  [("the battery, directly", "la batería, directamente"), ("the alternator", "el alternador"), ("the spark plugs", "las bujías")],
  "Worked by the key or start button.", "Se acciona con la llave o el pulsador.")
Q("el6", "electric", "Spark plugs are found in…", "Las bujías se encuentran en…",
  [("petrol engines", "los motores de gasolina"), ("diesel engines", "los motores diésel"), ("electric motors", "los motores eléctricos")],
  "They ignite the air–fuel mixture.", "Inflaman la mezcla de aire y carburante.")
Q("el7", "electric", "A spark plug in bad condition…", "Una bujía en mal estado…",
  [("raises fuel use and makes the exhaust dirtier", "aumenta el consumo y los gases contaminantes"), ("saves fuel", "ahorra combustible"), ("has no effect", "no tiene efecto")],
  "Part of the mixture doesn’t burn.", "No se quema toda la mezcla.")
Q("el8", "electric", "A pair of lamps or a whole set of lights doesn’t come on. The cause may be…", "No enciende un par de lámparas o un juego completo. Puede deberse a…",
  [("blown bulbs, a blown fuse or a faulty switch", "lámparas fundidas, un fusible dañado o un interruptor defectuoso"), ("low oil", "poco aceite"), ("the alternator belt only", "solo la correa del alternador")],
  "Check the fuses.", "Revisar los fusibles.")
Q("el9", "electric", "Xenon and bi-xenon lamps should be handled…", "Las lámparas de xenón y bixenón deben manipularlas…",
  [("only by specialists: they work at very high voltage", "solo personal especializado: funcionan con tensión muy alta"), ("by anyone", "cualquiera"), ("only with the engine running", "solo con el motor en marcha")],
  "Danger of electric shock.", "Peligro de descarga.")
Q("el10", "electric", "Using the lights, radio or air conditioning a lot with the engine off can…", "Abusar de luces, radio o aire acondicionado con el motor apagado puede…",
  [("flatten the battery", "descargar la batería"), ("damage the catalyst", "dañar el catalizador"), ("overheat the engine", "calentar el motor")],
  "The alternator only charges with the engine running.", "El alternador solo carga con el motor en marcha.")
Q("el11", "electric", "Charging is irregular. According to your course, it may be because…", "La carga es irregular. Según tu curso, puede deberse a que…",
  [("the electrolyte level is very low", "el nivel del electrolito es muy bajo"), ("the tyres are under-inflated", "los neumáticos tienen poca presión"), ("the air filter is new", "el filtro de aire es nuevo")],
  "Check the battery.", "Revisar la batería.")
Q("el12", "electric", "After loading the car heavily, the headlight beam may…", "Tras cargar mucho el coche, el haz de luz puede…",
  [("point too high and dazzle others", "quedar demasiado alto y deslumbrar"), ("switch off", "apagarse"), ("change colour", "cambiar de color")],
  "Check the aim after loading or unloading.", "Comprobar el reglaje tras cargar o descargar.")

# ---------------------------------------------------------------- 4. transmission
Q("tr1", "trans", "The transmission…", "El sistema de transmisión…",
  [("takes the engine’s force to the driving wheels", "transmite la fuerza del motor a las ruedas motrices"), ("cools the engine", "refrigera el motor"), ("brakes the car", "frena el coche")],
  "Front, rear or all wheels.", "Delanteras, traseras o todas.")
Q("tr2", "trans", "A vehicle whose driving wheels are the rear ones is called a…", "Un vehículo cuyas ruedas motrices son las traseras se llama de…",
  [("propulsion vehicle (rear-wheel drive)", "propulsión"), ("traction vehicle", "tracción"), ("integral traction vehicle", "tracción integral")],
  "Front wheels: traction; all wheels: 4×4.", "Delanteras: tracción; todas: 4×4.")
Q("tr3", "trans", "A vehicle with the front wheels as driving wheels is a…", "Un vehículo con las ruedas delanteras motrices es de…",
  [("traction vehicle", "tracción"), ("propulsion vehicle", "propulsión"), ("4×4", "4×4")],
  "The front wheels pull.", "Las ruedas delanteras tiran.")
Q("tr4", "trans", "The clutch is located…", "El embrague está situado…",
  [("between the engine and the gearbox", "entre el motor y la caja de cambios"), ("between the wheels", "entre las ruedas"), ("in the exhaust", "en el escape")],
  "It connects and disconnects the engine’s turn.", "Acopla y desacopla el giro del motor.")
Q("tr5", "trans", "The car’s speed doesn’t increase when the revs go up. The cause is…", "La velocidad no aumenta al subir las revoluciones. La causa es…",
  [("a slipping clutch with worn linings", "que patina el embrague, con los forros desgastados"), ("a flat battery", "la batería descargada"), ("a dirty air filter", "el filtro de aire sucio")],
  "Take it to a workshop.", "Hay que repararlo en un taller.")
Q("tr6", "trans", "Riding the clutch or resting your foot on the pedal…", "Ir a medio embrague o con el pie apoyado en el pedal…",
  [("can damage the clutch or shorten its life", "puede averiar el embrague o reducir su vida útil"), ("is recommended", "es recomendable"), ("saves fuel", "ahorra combustible")],
  "Take your foot off when not using it.", "Retirar el pie cuando no se use.")
Q("tr7", "trans", "Gears go in or out with great difficulty. The likely cause is…", "Las marchas entran o salen con mucha dificultad. La causa probable es…",
  [("an internal gearbox fault, possibly the wrong oil level", "una avería interna de la caja de cambios, quizá nivel de aceite incorrecto"), ("low tyre pressure", "poca presión en los neumáticos"), ("a blown fuse", "un fusible fundido")],
  "Workshop.", "Taller.")
Q("tr8", "trans", "Which part lets the driving wheels turn at different speeds in a bend?", "¿Qué elemento permite que las ruedas motrices giren a distinta velocidad en una curva?",
  [("The differential", "El diferencial"), ("The clutch", "El embrague"), ("The alternator", "El alternador")],
  "Part of the transmission.", "Forma parte de la transmisión.")
Q("tr9", "trans", "To change gear you should press the clutch…", "Para cambiar de marcha hay que pisar el embrague…",
  [("all the way down", "hasta el fondo"), ("halfway", "hasta la mitad"), ("slightly", "ligeramente")],
  "Without the engine revving high.", "Sin el motor revolucionado.")

# ---------------------------------------------------------------- 5. equipment
Q("eq1", "equip", "Which of these must a car carry?", "¿Qué debe llevar un turismo?",
  [("A V-16 light, a high-visibility vest and a spare wheel (or temporary wheel or alternative system)", "Un dispositivo V-16, un chaleco de alta visibilidad y una rueda de repuesto (o temporal o sistema alternativo)"), ("A fire extinguisher", "Un extintor"), ("A first-aid kit", "Un botiquín")],
  "Extinguisher: buses and heavy vehicles.", "Extintor: autobuses y pesados.")
Q("eq2", "equip", "Instead of a spare wheel, a car may carry…", "En lugar de rueda de repuesto, un turismo puede llevar…",
  [("a temporary-use wheel or an alternative system such as a repair kit", "una rueda de uso temporal o un sistema alternativo, como un kit reparapinchazos"), ("nothing", "nada"), ("a second V-16", "una segunda V-16")],
  "Respecting its limits.", "Respetando sus limitaciones.")
Q("eq3", "equip", "A lorry of more than 3,500 kg must carry…", "Un camión de más de 3.500 kg debe llevar…",
  [("a V-16 light, a vest and an approved fire extinguisher", "un dispositivo V-16, un chaleco y un extintor homologado"), ("only a vest", "solo un chaleco"), ("a spare wheel and a jack", "una rueda de repuesto y un gato")],
  "Like buses and non-special combinations.", "Como los autobuses y los conjuntos no especiales.")
Q("eq4", "equip", "Since 1 October 2026, a motorcycle must carry…", "Desde el 1 de octubre de 2026, una motocicleta debe llevar…",
  [("a high-visibility vest", "un chaleco de alta visibilidad"), ("a V-16 light", "un dispositivo V-16"), ("a fire extinguisher", "un extintor")],
  "The V-16 is recommended, not compulsory, on a motorcycle.", "La V-16 es recomendable, no obligatoria, en la moto.")
Q("eq5", "equip", "When must you wear the reflective vest?", "¿Cuándo hay que usar el chaleco reflectante?",
  [("When you get out and stand on the carriageway or shoulder of an interurban road", "Al salir y ocupar la calzada o el arcén de una vía interurbana"), ("Always while driving", "Siempre al conducir"), ("Only in town", "Solo en ciudad")],
  "Put it on before getting out.", "Ponérselo antes de salir.")
Q("eq6", "equip", "Where should the vest be kept?", "¿Dónde se debe guardar el chaleco?",
  [("Out of the light, but within reach so you can put it on before getting out", "Sin exponerlo a la luz, pero accesible para salir con él puesto"), ("In the boot, under the luggage", "En el maletero, bajo el equipaje"), ("On the dashboard in the sun", "En el salpicadero, al sol")],
  "Light spoils its reflective properties.", "La luz le hace perder las propiedades reflectantes.")
Q("eq7", "equip", "The high-visibility vest may be…", "El chaleco de alta visibilidad puede ser…",
  [("yellow, orange-red or red", "amarillo, rojo anaranjado o rojo"), ("any colour", "de cualquier color"), ("white or black", "blanco o negro")],
  "It must be certified.", "Debe estar certificado.")
Q("eq8", "equip", "An escort (pilot) vehicle must carry vests for…", "Un vehículo piloto de protección y acompañamiento debe llevar chalecos para…",
  [("the driver and each assistant", "el conductor y cada miembro del personal auxiliar"), ("the driver only", "solo el conductor"), ("nobody", "nadie")],
  "One each.", "Uno para cada uno.")
Q("eq9", "equip", "A delivery rider on a moped must wear a high-visibility vest…", "Un repartidor en ciclomotor debe llevar chaleco de alta visibilidad…",
  [("on all roads, at all times", "en todo tipo de vías"), ("only out of town", "solo fuera de poblado"), ("only at night", "solo de noche")],
  "Also on bicycles, VMP, motorcycles, quads…", "También en bicicletas, VMP, motos, quads…")
Q("eq10", "equip", "A temporary-use spare wheel is usually limited to…", "Una rueda de uso temporal suele estar limitada a…",
  [("about 80 km/h and 50–200 km, as the maker states", "unos 80 km/h y 50–200 km, según el fabricante"), ("120 km/h, no distance limit", "120 km/h, sin límite de distancia"), ("no limits", "ningún límite")],
  "The limits are marked on it.", "Las limitaciones vienen indicadas.")
Q("eq11", "equip", "Must a van of 3,000 kg MMA carry a fire extinguisher?", "¿Una furgoneta de 3.000 kg de MMA debe llevar extintor?",
  [("No: it carries the car equipment (V-16, vest and spare wheel or alternative)", "No: lleva la dotación de turismo (V-16, chaleco y rueda o alternativa)"), ("Yes, always", "Sí, siempre"), ("Only on motorways", "Solo en autopistas")],
  "Extinguisher above 3,500 kg.", "Extintor a partir de más de 3.500 kg.")
Q("eq12", "equip", "Since 1 January 2026, the V-16 warning light must be…", "Desde el 1 de enero de 2026, la señal V-16 debe ser…",
  [("an approved, connected model", "un modelo homologado y conectado"), ("any yellow light", "cualquier luz amarilla"), ("replaced by two triangles", "sustituida por dos triángulos")],
  "Topic 5.", "Tema 5.")
