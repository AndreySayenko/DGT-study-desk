# -*- coding: utf-8 -*-
"""Topic 13 content (vehicle maintenance and accessories), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Tema 13: Mantenimiento del vehículo y accesorios). The wording
and the figures are original. The compulsory equipment comes from the Reglamento General de Vehículos (RD 2822/1998,
art. 19 and annex XII, as amended by RD 159/2021 and RD 518/2026) and the professional riders' vest from the
Reglamento General de Circulación (art. 118, as amended by RD 518/2026), as they stand in November 2026.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import exhaust_smoke, maintenance_map, oil, cooling, battery, drivetrain, equipment


def rows(pairs):
    """[(en, es), ...] -> one-column table rows."""
    return [[T(a, b)] for a, b in pairs]


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("How the car’s main systems work and how to <b>look after them</b>: fuel and air, exhaust, oil, cooling, electrics and transmission — and the <b>equipment you must carry</b>.",
         "Cómo funcionan los principales sistemas del vehículo y cómo <b>mantenerlos</b>: alimentación, escape, lubricación, refrigeración, sistema eléctrico y transmisión, y la <b>dotación obligatoria</b>."),
        ("The exam asks about <b>symptoms and their cause</b> (smoke colour, warning lights, a slipping clutch, a slow starter), <b>when to check things</b> (oil cold and level, coolant cold, never open the tank hot) "
         "and <b>what each vehicle must carry</b>.",
         "El examen pregunta por <b>síntomas y su causa</b> (color del humo, testigos, embrague que patina, arranque lento), <b>cuándo comprobar</b> (aceite en frío y en llano, refrigerante en frío, nunca abrir el vaso en caliente) "
         "y <b>qué debe llevar cada vehículo</b>."),
        ("The sections follow the order of your course’s Topic 13. Spanish exam terms are in <i>italics</i> in the English text, and a glossary closes the topic.",
         "Los apartados siguen el orden del Tema 13 de tu curso. Al final hay un glosario español–inglés."),
    ]))

    # ---------------------------------------------------------------- 1. engine
    B.append(H2("1", "The engine", "El motor"))
    B.append(P(
        "<b>Correct maintenance</b> — above all the manufacturer’s — and knowing how the vehicle works <b>make it last longer</b>, <b>prevent accidents from mechanical failure</b>, <b>save fuel</b>, <b>reduce pollution</b> and avoid needless repair bills. "
        "Many breakdowns come from <b>no maintenance, poor maintenance or the wrong maintenance</b> by the driver. The <b>vehicle factor</b> causes <b>4–13 %</b> of road accidents (Topic 10).",
        "Con un <b>correcto mantenimiento</b> (sobre todo el del fabricante) y conociendo cómo funciona el vehículo se puede <b>alargar su vida útil</b>, <b>prevenir accidentes por fallos mecánicos</b>, <b>ahorrar combustible</b>, <b>reducir la contaminación</b> y evitar gastos innecesarios. "
        "Gran parte de las averías se deben a un <b>mantenimiento nulo, deficiente o equivocado</b> por parte del conductor. El <b>factor vehículo</b> causa entre el <b>4 % y el 13 %</b> de los accidentes (Tema 10)."))
    B.append(P(
        "The engine <b>turns energy into movement</b>. Most vehicles still use <b>heat engines</b> that burn fuel (<b>petrol or diesel</b>), but less-polluting engines are growing: <b>electric</b>, <b>hybrid</b>, <b>hydrogen</b>…",
        "El motor <b>transforma energía para conseguir el desplazamiento</b> del vehículo. La mayoría usan <b>motores térmicos</b> que aprovechan la energía del carburante (<b>gasolina o gasóleo</b>), aunque crece la cuota de motores <b>menos contaminantes</b>: <b>eléctricos</b>, <b>híbridos</b>, <b>hidrógeno</b>…"))
    B.append(FIG(exhaust_smoke, "White smoke on a cold start is water vapour; bluish smoke means the engine burns oil; black smoke means too much fuel or too little air.",
                 "El humo blanco al arrancar en frío es vapor de agua; el azulado indica que el motor quema aceite; el negro, exceso de carburante o falta de aire."))
    B.append(FIG(maintenance_map, "Where the parts you check and maintain are, grouped by system.",
                 "Dónde están las piezas que se comprueban y mantienen, agrupadas por sistema."))

    # ---------------------------------------------------------------- 2. engine systems
    B.append(H2("2", "Systems the engine needs", "Sistemas necesarios para el motor"))
    B.append(H3("2.1 Fuel and air supply", "2.1 Sistema de alimentación"))
    B.append(P("It delivers to the <b>cylinders</b> the <b>air and fuel</b> the engine needs. It has an <b>air circuit</b> and a <b>fuel circuit</b>.",
               "Hace llegar a los <b>cilindros</b> la cantidad de <b>aire y combustible</b> necesaria. Está formado por el circuito de alimentación de <b>aire</b> y el de <b>carburante</b>."))
    B.append(TABLE(
        [T("Part", "Elemento"), T("Care", "Mantenimiento")],
        [
            [T("<b>Air filter</b>", "<b>Filtro de aire</b>"), T("Check it so dirt doesn’t <b>clog</b> it (it gets dirtier in <b>summer</b>) — a clogged filter means <b>more fuel and more pollution</b>. Replace it as the manufacturer says.",
                                                               "Revisarlo para que la suciedad no lo <b>obstruya</b> (se ensucia más en <b>verano</b>): provocaría <b>más consumo y contaminación</b>. Sustituirlo según el fabricante.")],
            [T("<b>Fuel filter</b>", "<b>Filtro de combustible</b>"), T("Replace it when the manufacturer says.", "Sustituirlo cuando lo indique el fabricante.")],
            [T("<b>Idle speed</b> (<i>ralentí</i>)", "<b>Ralentí</b>"),
             T("The engine running with the car <b>stopped</b>, in <b>neutral</b> or with the <b>clutch pressed</b>. If fuel use goes up, it may be set <b>too high</b>; <b>too low</b>, and the engine <b>stalls</b>.",
               "Motor en marcha con el coche <b>parado</b>, en <b>punto muerto</b> o con el <b>embrague pisado</b>. Si aumenta el consumo, puede estar <b>demasiado alto</b>; si está <b>demasiado bajo</b>, el motor <b>se cala</b> o se para.")],
        ],
        widths=["26%", "74%"],
    ))
    B.append(H3("2.2 Exhaust", "2.2 Sistema de escape"))
    B.append(P(
        "It collects the <b>combustion gases</b> leaving the cylinders and takes them to the <b>rear</b> of the vehicle. On the way it reduces their harm: the <b>silencer</b> (<i>silenciador</i> or <i>silencioso</i>) <b>lowers the noise</b> and keeps the gases from coming out <b>too hot</b>; "
        "the <b>catalytic converter</b> (<i>catalizador</i>) <b>cuts the toxic gases</b> almost completely.",
        "<b>Recoge los gases</b> de la combustión a la salida de los cilindros y los lleva a la <b>parte trasera</b>. Además reduce sus daños: el <b>silenciador</b> o silencioso <b>disminuye el ruido</b> y evita que los gases salgan <b>muy calientes</b>; "
        "el <b>catalizador</b> <b>reduce los gases tóxicos</b> casi por completo."))
    B.append(BOX("key", "Looking after the exhaust", "Mantenimiento del escape", [
        ("Replace the <b>catalytic converter</b> about every <b>150,000 km</b>. <b>Burning too much oil</b> can damage it, and so can regularly <b>running the tank almost empty</b>. Avoid knocks underneath the car.",
         "Sustituir el <b>catalizador</b> aproximadamente cada <b>150.000 km</b>. Un <b>consumo excesivo de aceite</b> puede dañarlo, igual que <b>apurar regularmente el depósito</b>. Evitar golpes en los bajos."),
    ]))
    B.append(BOX("trap", "The silencer is compulsory", "El silenciador es obligatorio", [
        ("Motor vehicles must have a <b>silencer</b>. Without one, or with a faulty one, the noise goes up (<b>noise pollution</b>) and <b>driving is prohibited</b> — in town and out of town. The exception is <b>electric vehicles</b>.",
         "Los vehículos de motor deben llevar <b>silenciador</b>. Sin él, o si funciona mal, aumentan los decibelios (<b>contaminación acústica</b>) y <b>está prohibido circular</b>, en poblado y fuera. Excepto los <b>vehículos eléctricos</b>."),
    ]))
    B.append(H3("2.3 Lubrication", "2.3 Sistema de lubricación"))
    B.append(P(
        "It puts a <b>film of oil</b> between the engine’s metal parts to <b>reduce friction</b> and <b>prevent early wear</b>. The <b>oil-pressure warning light</b> stays off while lubrication is right; if it <b>comes on (red)</b>, the pressure is <b>below the minimum</b>: "
        "<b>stop the engine quickly</b>.",
        "Interpone una <b>película de aceite</b> entre las piezas metálicas del motor para <b>reducir el rozamiento</b> y <b>evitar un desgaste prematuro</b>. El <b>indicador de presión de aceite</b> permanece apagado si se lubrica bien; si <b>se enciende (rojo)</b>, la presión está <b>por debajo del mínimo</b>: "
        "hay que <b>detener el motor rápidamente</b>."))
    B.append(TABLE(
        [T("Task", "Tarea"), T("How", "Cómo")],
        [
            [T("<b>Check the oil level</b>", "<b>Comprobar el nivel de aceite</b>"),
             T("Regularly, with the <b>dipstick</b>: pull it out, wipe it, put it back, pull it out again and check the oil is <b>between MIN and MAX</b>. With the <b>engine stopped and cold</b> and the car <b>level</b>. If it is low, <b>top up</b> as the manufacturer says.",
               "Periódicamente, con la <b>varilla indicadora</b>: sacarla, limpiarla, volver a meterla, sacarla de nuevo y comprobar que está <b>entre la marca de mínimo y máximo</b>. Con el <b>motor parado y frío</b> y el vehículo <b>en llano</b>. Si falta, <b>añadir</b> según el fabricante.")],
            [T("<b>Change the oil</b>", "<b>Cambiar el aceite</b>"),
             T("Drain it through the <b>drain plug</b> at the bottom of the <b>sump</b> (<i>cárter</i>) and refill through the <b>cap on top of the cylinder head</b>. With the <b>engine warm</b> (the oil flows better) and the car <b>level</b>.",
               "Vaciarlo por el <b>tapón de vaciado</b> de la parte inferior del <b>cárter</b> y rellenar por el <b>tapón superior de la culata</b>. Con el <b>motor caliente</b> (mayor fluidez) y el vehículo <b>en llano</b>.")],
            [T("<b>Oil filter</b>", "<b>Filtro de aceite</b>"), T("Replace it as the manufacturer says.", "Sustituirlo según el fabricante.")],
        ],
        widths=["26%", "74%"],
    ))
    B.append(FIG(oil, "Check the oil cold and level, between MIN and MAX; change it warm. In SAE 10W-60, 10W is the winter (cold) grade and 60 the grade when hot.",
                 "El aceite se comprueba en frío y en llano, entre MIN y MAX; se cambia en caliente. En SAE 10W-60, 10W es el grado de invierno (en frío) y 60 el grado en caliente."))
    B.append(P(
        "Oils are graded by <b>viscosity</b> (SAE): <b>low numbers are fluid</b>, high numbers <b>viscous</b> (your course gives a scale from <b>0</b> to <b>70</b>). <b>Multigrade</b> oils have <b>two grades</b>: in <b>SAE 10W-60</b>, the first number is the "
        "<b>winter</b> grade (<b>W</b> for <i>winter</i>), very fluid in the cold, and the second is the grade at <b>summer, hot</b> temperatures, more viscous.",
        "Los aceites se clasifican por su <b>viscosidad</b> (normas SAE): los <b>números bajos son fluidos</b> y los altos, <b>viscosos</b> (tu curso da una escala de <b>0</b> a <b>70</b>). Los <b>multigrados</b> tienen <b>dos grados</b>: en <b>SAE 10W-60</b>, el primer número es el "
        "de <b>invierno</b> (<b>W</b> de <i>winter</i>), muy fluido en frío, y el segundo el de <b>verano</b>, en caliente, más viscoso."))
    B.append(BOX("trap", "Changing the oil", "El cambio de aceite", [
        ("It is <b>not allowed on the public road</b> — it is very polluting. Used oil goes to an <b>oil-recovery container</b>.", "<b>No se puede realizar en la vía pública</b>: es muy contaminante. Se debe entregar en un <b>contenedor de recuperación de aceite</b>."),
    ]))
    B.append(H3("2.4 Cooling", "2.4 Sistema de refrigeración"))
    B.append(P(
        "It gets rid of part of the <b>heat</b> the engine produces, with a <b>coolant</b> (distilled water mixed with <b>antifreeze</b> additives) that flows through passages inside the engine and through the radiator.",
        "Se encarga de <b>expulsar parte del calor</b> del motor mediante el <b>líquido refrigerante</b> (agua destilada mezclada con aditivos <b>anticongelantes</b>), que circula por orificios y huecos en el interior del motor y por el radiador."))
    B.append(FIG(cooling, "The coolant takes heat from the engine to the radiator and comes back cooled. Check the level cold, on the expansion tank; never open it hot.",
                 "El refrigerante lleva el calor del motor al radiador y vuelve enfriado. El nivel se comprueba en frío, en el vaso de expansión; nunca se abre en caliente."))
    B.append(TABLE(
        [T("Looking after the cooling system", "Mantenimiento de la refrigeración")],
        rows([
            ("<b>Check the coolant level</b>: between the <b>MIN and MAX</b> marks on the <b>expansion tank</b>, with the <b>engine cold</b>. If it is low, your course says <b>top up with distilled water</b> (many makers ask for the same coolant mixture).",
             "<b>Comprobar el nivel del refrigerante</b>: entre las marcas de <b>mínimo y máximo</b> del <b>vaso de expansión</b>, con el <b>motor en frío</b>. Si está bajo, tu curso indica <b>rellenar con agua destilada</b> (muchos fabricantes piden la misma mezcla de refrigerante)."),
            ("<b>Change the coolant</b> as the manufacturer says (about <b>every 2 years</b>). Look for <b>leaks</b>. Add <b>antifreeze</b> if the car will face <b>very low temperatures</b>.",
             "<b>Cambiar el refrigerante</b> según el fabricante (unos <b>2 años</b>). Observar que no haya <b>fugas</b>. Añadir <b>anticongelante</b> si va a estar expuesto a <b>temperaturas muy bajas</b>."),
        ]),
    ))
    B.append(BOX("trap", "Never…", "Nunca…", [("…open the <b>expansion tank</b> with the <b>engine hot</b>.", "…abrir el <b>vaso de expansión</b> con el <b>motor caliente</b>.")]))

    # ---------------------------------------------------------------- 3. electrical system
    B.append(H2("3", "The electrical system", "Sistema eléctrico"))
    B.append(FIG(battery, "The battery gives power with the engine off; the alternator, driven by a belt, recharges it with the engine running. A red warning light means act now.",
                 "La batería da energía con el motor parado; el alternador, movido por una correa, la recarga con el motor en marcha. Un testigo rojo exige actuar ya."))
    B.append(TABLE(
        [T("Part", "Elemento"), T("What it does", "Qué hace"), T("Care and faults", "Mantenimiento y averías")],
        [
            [T("<b>Battery</b>", "<b>Batería</b>"),
             T("Supplies electricity <b>while the engine is stopped</b>. Inside: plastic walls make <b>cells</b> holding <b>lead plates</b> in <b>distilled water with sulphuric acid</b> (the <b>electrolyte</b>). Outside: the <b>terminals</b> (<i>bornes</i>) for the cables.",
               "Proporciona <b>energía eléctrica mientras el motor está parado</b>. Dentro, unas placas de plástico forman <b>vasos</b> con <b>placas de plomo</b> en <b>agua destilada con ácido sulfúrico</b> (<b>electrolito</b>). Fuera, los <b>bornes</b>, donde se conectan los cables."),
             T("The electrolyte must always <b>cover the plates</b>: top up with <b>distilled water only</b>. Keep the terminals <b>tight, clean and greased</b> (petroleum jelly or soft grease) against sulphation. "
               "<b>Low-maintenance</b> batteries: check the level about every <b>6 months</b>; <b>maintenance-free</b>: no need.",
               "El electrolito debe <b>cubrir siempre las placas</b>: añadir <b>solo agua destilada</b>. Bornes <b>apretados, limpios y engrasados</b> (vaselina o grasa blanda) para evitar sulfataciones. "
               "Baterías de <b>bajo mantenimiento</b>: revisar el nivel cada <b>6 meses</b>; <b>sin mantenimiento</b>: no hace falta.")],
            [T("<b>Charging</b>: the <b>alternator</b>", "<b>Carga</b>: el <b>alternador</b>"),
             T("Supplies electricity <b>while the engine runs</b>, recharging the battery and feeding the electrics. It is driven by the engine through a <b>belt</b>.",
               "Proporciona energía <b>con el motor en movimiento</b>: repone la carga de la batería y alimenta los elementos eléctricos. Recibe el giro del motor mediante una <b>correa</b>."),
             T("Keep the <b>belt</b> in good condition; replace it if broken or worn. <b>Charge light on</b>: the alternator isn’t charging enough — probably a <b>broken belt or worn brushes</b>. "
               "<b>Irregular charging</b>: the <b>electrolyte level may be very low</b>.",
               "Mantener la <b>correa</b> en buen estado; sustituirla si se rompe o deteriora. <b>Testigo encendido</b>: el alternador no carga lo suficiente, probablemente <b>correa rota o escobillas desgastadas</b>. "
               "<b>Carga irregular</b>: puede ser que el <b>nivel del electrolito sea muy bajo</b>.")],
            [T("<b>Starter</b>", "<b>Arranque</b>"),
             T("An electric <b>starter motor</b>, fed straight from the battery and worked by the <b>key or start button</b>, turns the engine over for the first time.",
               "Un <b>motor de arranque</b> eléctrico, alimentado directamente por la batería y accionado con la <b>llave o pulsador de contacto</b>, provoca los primeros giros del motor."),
             T("<b>Don’t keep trying</b> too long — it flattens the battery. Engine <b>doesn’t turn, or very slowly, and the lights go out</b>: battery <b>flat</b>. Engine turns <b>slowly</b>: battery low or <b>bad connections</b>. "
               "Check the terminals, recharge or replace the battery.",
               "<b>No insistir</b> demasiado: podría <b>descargar la batería</b>. Si <b>no gira o gira muy despacio y las luces se apagan</b>: batería <b>descargada</b>. Si gira <b>muy despacio</b>: batería baja o <b>malas conexiones</b>. "
               "Comprobar los bornes, recargar o sustituir la batería.")],
            [T("<b>Ignition</b> (petrol)", "<b>Encendido</b> (gasolina)"),
             T("Makes the <b>spark</b> in the <b>spark plugs</b> (<i>bujías</i>) that ignites the air–fuel mixture in the cylinders of a <b>petrol</b> engine.",
               "Produce la <b>chispa</b> en las <b>bujías</b> que inflama la mezcla de aire y carburante en los cilindros del motor de <b>gasolina</b>."),
             T("Check and replace the plugs as the manufacturer says. A <b>bad plug</b> leaves mixture unburnt: <b>more fuel</b> and <b>dirtier exhaust</b>.",
               "Revisar y sustituir las bujías según el fabricante. Una <b>bujía en mal estado</b> deja mezcla sin quemar: <b>más consumo</b> y gases <b>más contaminantes</b>.")],
            [T("<b>Lighting and others</b>", "<b>Iluminación y otros</b>"),
             T("Powers the <b>lights</b> (to see, be seen and signal) and the radio, horn, electric windows, air conditioning…", "Da energía al <b>alumbrado</b> (ver, ser vistos y señalizar) y a la radio, bocina, elevalunas, aire acondicionado…"),
             T("<b>Don’t overuse</b> lights, radio, air conditioning or horn with the <b>engine off</b> (flat battery). Check the headlights and that every light works. A <b>pair of lamps or a whole set</b> fails: <b>blown bulbs, a fuse</b> or a <b>faulty switch</b>. "
               "<b>Xenon and bi-xenon</b> lamps: <b>specialists only</b> (very high voltage). Check the <b>aim</b> after loading or unloading.",
               "<b>No abusar</b> de luces, radio, aire acondicionado o bocina con el <b>motor apagado</b> (descarga la batería). Comprobar los faros y que funcionan todas las luces. Si no enciende <b>un par de lámparas o un juego completo</b>: <b>lámparas fundidas, fusible</b> o <b>interruptor defectuoso</b>. "
               "<b>Xenón y bixenón</b>: solo <b>personal especializado</b> (tensión muy alta). Comprobar el <b>reglaje</b> tras cargar o descargar.")],
        ],
        widths=["16%", "38%", "46%"],
        cls="small",
    ))
    B.append(BOX("trap", "Light aim after loading", "Reglaje tras cargar", [
        ("A <b>heavily loaded</b> car can aim the beam <b>too high</b> — it lights the road badly and <b>dazzles</b> others; aimed <b>too low</b>, it lights fewer metres and you see obstacles <b>later</b>.",
         "Muy cargado, el haz puede quedar <b>demasiado alto</b>: ilumina mal la vía y <b>deslumbra</b>; <b>demasiado bajo</b>, ilumina menos metros y se tarda más en ver los obstáculos."),
    ]))

    # ---------------------------------------------------------------- 4. transmission
    B.append(H2("4", "The transmission", "Sistema de transmisión"))
    B.append(P(
        "It takes the engine’s force to the <b>driving wheels</b>: the <b>front</b> ones (a <i>vehículo de tracción</i>), the <b>rear</b> ones (<i>de propulsión</i>) or <b>all four</b> (<i>tracción integral o total</i>, 4×4).",
        "Transmite la fuerza del motor a las <b>ruedas motrices</b>: las <b>delanteras</b> (vehículo de <b>tracción</b>), las <b>traseras</b> (vehículo de <b>propulsión</b>) o <b>todas</b> (<b>tracción integral o total</b>, 4×4)."))
    B.append(FIG(drivetrain, "Front-wheel drive pulls, rear-wheel drive pushes, four-wheel drive uses all four wheels.",
                 "La tracción delantera tira, la trasera empuja y la total usa las cuatro ruedas."))
    B.append(TABLE(
        [T("Part", "Elemento"), T("What it does", "Qué hace")],
        [
            [T("<b>Clutch</b> (<i>embrague</i>)", "<b>Embrague</b>"), T("Between the engine and the gearbox: <b>connects and disconnects</b> the engine’s turn from the transmission.", "Situado entre el motor y la caja de cambios, <b>acopla y desacopla</b> el giro del motor a la transmisión.")],
            [T("<b>Gearbox</b>", "<b>Caja de cambios</b>"), T("Makes the most of the engine’s power, sending <b>more or less turning speed</b> to the drive shaft and the wheels.", "Aprovecha la potencia del motor, transmitiendo <b>mayor o menor velocidad de giro</b> al árbol de transmisión y a las ruedas.")],
            [T("<b>Differential, drive shaft…</b>", "<b>Grupo cónico-diferencial, árbol de transmisión…</b>"), T("Connect the gearbox to the driving wheels and let the wheels <b>turn at different speeds</b> (in bends).", "Unen la caja de cambios con las ruedas motrices y permiten que las ruedas <b>giren a distinta velocidad</b> (en curvas).")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(TABLE(
        [T("Symptom or habit", "Síntoma o hábito"), T("Cause · what to do", "Causa · qué hacer")],
        [
            [T("Riding the clutch, or resting your foot on the pedal", "Ir a medio embrague o con el pie apoyado en el pedal"), T("<b>Damages the clutch</b> or shortens its life.", "<b>Puede averiar el embrague</b> o reducir su vida útil.")],
            [T("Speed <b>doesn’t rise with the revs</b>", "La velocidad <b>no aumenta con las revoluciones</b>"), T("The <b>clutch is slipping</b>: worn linings. <b>Workshop</b>.", "<b>Patina el embrague</b>: forros desgastados. <b>Taller</b>.")],
            [T("Gears go in or out <b>with great difficulty</b>", "Las marchas entran o salen <b>con mucha dificultad</b>"), T("An internal <b>gearbox fault</b>, possibly the <b>wrong oil level</b>. <b>Workshop</b>.", "<b>Avería interna de la caja de cambios</b>, posiblemente por <b>nivel de aceite incorrecto</b>. <b>Taller</b>.")],
            [T("Changing gear", "Al cambiar de marcha"), T("Press the pedal <b>all the way down</b>, without the engine revving high.", "<b>Pisar el pedal hasta el fondo</b>, evitando que el motor esté revolucionado.")],
        ],
        widths=["40%", "60%"],
    ))

    # ---------------------------------------------------------------- 5. accessories
    B.append(H2("5", "Accessories, spares and tools", "Accesorios, repuestos y herramientas"))
    B.append(P("Motor vehicles must carry <b>at least</b> this equipment (Reglamento General de Vehículos, annex XII):", "Los vehículos de motor deben llevar, <b>como mínimo</b>, esta dotación (Reglamento General de Vehículos, anexo XII):"))
    B.append(FIG(equipment, "Cars and light vans: V-16, vest and a spare wheel (or temporary wheel or repair kit). Buses and heavy vehicles: V-16, vest and an extinguisher. Motorcycles: a vest.",
                 "Turismos y furgonetas ligeras: V-16, chaleco y rueda de repuesto (o de uso temporal o kit). Autobuses y pesados: V-16, chaleco y extintor. Motocicletas: chaleco."))
    B.append(TABLE(
        [T("Vehicle", "Vehículo"), T("Compulsory equipment", "Dotación obligatoria")],
        [
            [T("<b>Cars</b>, and <b>mixed and goods vehicles up to 3,500 kg</b> MMA (not three-wheelers or quadricycles)", "<b>Turismos</b>, y <b>vehículos mixtos y de mercancías de hasta 3.500 kg</b> de MMA (excepto tres ruedas y cuadriciclos)"),
             T("• A <b>V-16 warning light</b> (connected, since 1 January 2026 — Topic 5).<br>• A certified <b>high-visibility vest</b>, worn when you get out onto the carriageway or shoulder of an interurban road. Escort vehicles carry one for the driver and for each assistant.<br>"
               "• A <b>spare wheel</b> or a <b>temporary-use wheel</b>, with the <b>tools</b> to change it — or an <b>alternative system</b> (such as a puncture-repair kit) that keeps the vehicle mobile. Respect its limits: a temporary wheel is usually limited to <b>80 km/h</b> and <b>50–200 km</b>, as the maker states.",
               "• El <b>dispositivo luminoso V-16</b> (conectado, desde el 1 de enero de 2026; Tema 5).<br>• Un <b>chaleco de alta visibilidad</b> certificado, que se usa al salir y ocupar la calzada o el arcén de las vías interurbanas. Los vehículos piloto llevan uno para el conductor y otro para cada auxiliar.<br>"
               "• Una <b>rueda de repuesto</b> o de <b>uso temporal</b>, con las <b>herramientas</b> para cambiarla, o un <b>sistema alternativo</b> (como un kit reparapinchazos) que garantice la movilidad. Se respetan sus limitaciones: la rueda de uso temporal suele limitarse a <b>80 km/h</b> y <b>50–200 km</b>, según el fabricante.")],
            [T("<b>Buses</b>, <b>mixed and goods vehicles over 3,500 kg</b> and <b>non-special combinations</b>", "<b>Autobuses</b>, <b>mixtos y de mercancías de más de 3.500 kg</b> y <b>conjuntos no especiales</b>"),
             T("• A <b>V-16 warning light</b>.<br>• A <b>high-visibility vest</b>.<br>• An approved <b>fire extinguisher</b>, suitable and <b>ready to use</b>.", "• El <b>dispositivo V-16</b>.<br>• Un <b>chaleco de alta visibilidad</b>.<br>• Un <b>equipo homologado de extinción de incendios</b>, adecuado y <b>en condiciones de uso</b>.")],
            [T("<b>Motorcycles</b>", "<b>Motocicletas</b>"), T("A <b>high-visibility vest</b> (compulsory since <b>1 October 2026</b>), for getting off onto the carriageway or shoulder of an interurban road.", "Un <b>chaleco de alta visibilidad</b> (obligatorio desde el <b>1 de octubre de 2026</b>), para cuando se bajen y ocupen la calzada o el arcén de las vías interurbanas.")],
        ],
        widths=["32%", "68%"],
    ))
    B.append(BOX("key", "The high-visibility vest", "El chaleco reflectante de alta visibilidad", [
        ("<b>Certified</b> (CE marking, at least class 2) and <b>yellow, orange-red or red</b>. Your course adds that it must be <b>visible at 150 m</b>.", "<b>Certificado</b> (marcado CE, mínimo clase 2) y de color <b>amarillo, rojo anaranjado o rojo</b>. Tu curso añade que debe ser <b>visible a 150 metros</b>."),
        ("Wear it whenever you <b>get out</b> and stand on the <b>carriageway or shoulder of an interurban road</b>.", "Se usa al <b>salir del vehículo</b> y ocupar la <b>calzada o el arcén de las vías interurbanas</b>."),
        ("Keep it <b>out of the light</b> (so it keeps its reflective properties) but <b>within reach</b>, so you can put it on <b>before getting out</b>.", "Guardarlo en un lugar <b>no expuesto a la luz</b> (para que no pierda sus propiedades reflectantes) pero <b>accesible</b>, para salir del vehículo <b>con él puesto</b>."),
    ]))
    B.append(BOX("trap", "Professional riders", "Conductores profesionales", [
        ("Those who <b>work</b> riding <b>motorcycles, three-wheelers and quadricycles, mopeds, quads, bicycles and other cycles, or VMP</b> must wear a high-visibility vest <b>on all roads</b>, at all times.",
         "Quienes desarrollan su <b>actividad profesional</b> en <b>motocicletas, vehículos de tres ruedas y cuadriciclos, ciclomotores, quads, bicicletas y ciclos, o VMP</b> deben llevar chaleco de alta visibilidad <b>en todo tipo de vías</b>."),
    ]))

    # ---------------------------------------------------------------- 6. traps
    B.append(H2("6", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("Smoke: <b>white</b> on a cold start = water vapour (no fault); <b>bluish</b> = burning oil; <b>black</b> = too much fuel / too little air.", "Humo: <b>blanco</b> al arrancar en frío = vapor de agua (no es avería); <b>blanco azulado</b> = consume aceite; <b>negro</b> = exceso de carburante o falta de aire."),
        ("A dirty <b>air filter</b> raises fuel use; it gets dirtier in <b>summer</b>. Idle <b>too high</b>: more fuel; <b>too low</b>: the engine stalls.", "Un <b>filtro de aire</b> sucio aumenta el consumo; se ensucia más en <b>verano</b>. Ralentí <b>alto</b>: más consumo; <b>bajo</b>: se cala."),
        ("Catalyst: about <b>150,000 km</b>; damaged by burning oil and by running the tank empty. <b>No silencer</b>: no driving anywhere (except electric vehicles).", "Catalizador: unos <b>150.000 km</b>; lo dañan el consumo de aceite y apurar el depósito. <b>Sin silenciador</b>: prohibido circular (salvo eléctricos)."),
        ("Oil <b>check</b>: engine <b>cold</b>, level ground. Oil <b>change</b>: engine <b>warm</b>, level ground. Red oil light: <b>stop the engine</b>.", "Aceite: <b>comprobar</b> en <b>frío</b> y en llano; <b>cambiar</b> en <b>caliente</b> y en llano. Testigo rojo de aceite: <b>parar el motor</b>."),
        ("In <b>10W-60</b>, <b>W</b> = winter; the first number is for the cold, the second for hot.", "En <b>10W-60</b>, la <b>W</b> = winter (invierno); el primer número es para frío y el segundo para caliente."),
        ("Coolant: check <b>cold</b>, on the expansion tank; change about every <b>2 years</b>; <b>never open the tank hot</b>.", "Refrigerante: comprobar en <b>frío</b>, en el vaso de expansión; cambiar cada <b>2 años</b> aprox.; <b>nunca abrir el vaso en caliente</b>."),
        ("Battery: top up with <b>distilled water only</b>; terminals <b>greased</b>; low-maintenance: every <b>6 months</b>; maintenance-free: never.", "Batería: añadir <b>solo agua destilada</b>; bornes <b>engrasados</b>; bajo mantenimiento: cada <b>6 meses</b>; sin mantenimiento: nunca."),
        ("Charge light on: <b>alternator</b> (belt or brushes). Starter turns slowly and lights go out: <b>flat battery</b>.", "Testigo de carga: <b>alternador</b> (correa o escobillas). Arranque lento y luces que se apagan: <b>batería descargada</b>."),
        ("Spark plugs are for <b>petrol</b> engines. Xenon lamps: <b>specialists only</b>.", "Las bujías son de los motores de <b>gasolina</b>. Xenón: <b>solo especialistas</b>."),
        ("Front-wheel drive = <b>tracción</b>; rear-wheel drive = <b>propulsión</b>. Speed doesn’t rise with revs = <b>slipping clutch</b>.", "Ruedas delanteras motrices = <b>tracción</b>; traseras = <b>propulsión</b>. La velocidad no sube con las revoluciones = <b>patina el embrague</b>."),
        ("Cars: V-16 + vest + spare/temporary wheel or kit. Heavy and buses: V-16 + vest + <b>extinguisher</b> (no spare wheel required). Motorcycles: <b>vest</b>.", "Turismos: V-16 + chaleco + rueda o kit. Pesados y autobuses: V-16 + chaleco + <b>extintor</b> (no se exige rueda). Motos: <b>chaleco</b>."),
    ]))

    # ---------------------------------------------------------------- 7. numbers
    B.append(H2("7", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Accidents caused by the vehicle factor", "Accidentes por el factor vehículo"), T("4–13 %", "4–13 %")],
            [T("Replace the catalytic converter", "Sustituir el catalizador"), T("about every 150,000 km", "cada 150.000 km aprox.")],
            [T("Change the coolant", "Cambiar el refrigerante"), T("about every 2 years", "cada 2 años aprox.")],
            [T("Check a low-maintenance battery", "Revisar una batería de bajo mantenimiento"), T("about every 6 months", "cada 6 meses aprox.")],
            [T("Temporary spare wheel", "Rueda de uso temporal"), T("usually 80 km/h, 50–200 km", "normalmente 80 km/h, 50–200 km")],
            [T("Mass limit: car equipment / heavy-vehicle equipment", "Límite de masa: dotación de turismo / de pesado"), T("up to 3,500 kg / over 3,500 kg", "hasta 3.500 kg / más de 3.500 kg")],
            [T("V-16 must be connected", "V-16 conectada obligatoria"), T("since 1 January 2026", "desde el 1 de enero de 2026")],
            [T("Vest compulsory equipment on motorcycles", "Chaleco en la dotación de las motos"), T("since 1 October 2026", "desde el 1 de octubre de 2026")],
        ],
        widths=["58%", "42%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["en2", "fu2", "ex3", "lu2", "lu5", "co2", "ba2", "el3", "el6", "tr2", "tr5", "eq3"]


def quiz():
    from .bank import BANK
    by_id = {q["id"]: q for q in BANK}
    out = []
    for i, qid in enumerate(QUIZ_IDS):
        q = by_id[qid]
        opts = [T(o["en"], o["es"]) for o in q["o"]]
        k = i % 3
        order = opts[1:]
        order.insert(k, opts[0])
        out.append((T(q["q"]["en"], q["q"]["es"]), order, k, T(q["why"]["en"], q["why"]["es"])))
    return out


SOURCES = [
    ("Reglamento General de Vehículos (RD 2822/1998), art. 19 and annex XII: accessories, spares and tools — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-1999-1826"),
    ("Real Decreto 518/2026 (BOE 26-06-2026): high-visibility vest for motorcycles and for professional riders, in force 1 October 2026", "https://www.boe.es/boe/dias/2026/06/26/pdfs/BOE-A-2026-13889.pdf"),
    ("Real Decreto 159/2021: the V-16 warning light replaces the triangles", "https://www.boe.es/buscar/act.php?id=BOE-A-2021-4194"),
    ("Reglamento General de Circulación (RD 1428/2003), art. 7.2: no driving without a silencer, in town or out — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
]

GLOSSARY = [
    ("mantenimiento", "maintenance"),
    ("motor térmico", "combustion (heat) engine"),
    ("gasolina · gasóleo (diésel)", "petrol · diesel"),
    ("sistema de alimentación", "fuel and air supply"),
    ("filtro de aire / de combustible / de aceite", "air / fuel / oil filter"),
    ("ralentí", "idle speed"),
    ("calarse", "to stall"),
    ("sistema de escape", "exhaust system"),
    ("silenciador (silencioso)", "silencer (muffler)"),
    ("catalizador", "catalytic converter"),
    ("lubricación · cárter · culata", "lubrication · sump · cylinder head"),
    ("varilla indicadora", "dipstick"),
    ("tapón de vaciado", "drain plug"),
    ("aceite multigrado", "multigrade oil"),
    ("refrigeración · radiador", "cooling · radiator"),
    ("líquido refrigerante · anticongelante", "coolant · antifreeze"),
    ("vaso de expansión", "expansion tank"),
    ("batería · vaso · electrolito", "battery · cell · electrolyte"),
    ("bornes · sulfatación", "battery terminals · sulphation"),
    ("alternador · correa · escobillas", "alternator · belt · brushes"),
    ("testigo", "warning light"),
    ("motor de arranque", "starter motor"),
    ("bujía", "spark plug"),
    ("fusible · lámpara fundida", "fuse · blown bulb"),
    ("transmisión · ruedas motrices", "transmission · driving wheels"),
    ("tracción / propulsión / tracción total", "front-wheel / rear-wheel / four-wheel drive"),
    ("embrague · patinar · forros", "clutch · to slip · linings"),
    ("caja de cambios · diferencial · árbol de transmisión", "gearbox · differential · drive shaft"),
    ("dotación obligatoria", "compulsory equipment"),
    ("rueda de repuesto / de uso temporal", "spare wheel / temporary-use spare"),
    ("kit reparapinchazos", "puncture-repair kit"),
    ("extintor", "fire extinguisher"),
]
