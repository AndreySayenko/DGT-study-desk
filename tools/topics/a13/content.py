# -*- coding: utf-8 -*-
"""Category A1/A2, Topic 13 content (motorcycle maintenance and accessories), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the A1/A2 course's Tema 13 (Mantenimiento del vehículo y accesorios): the motorcycle's
parts and systems (fuel, lubrication, cooling, electrical, transmission, steering and suspension), accessories and
spares, and maintenance and breakdowns. It is written for motorcycles; only the exhaust-smoke figure is shared with
Category B, Topic 13.

The rules come from the Reglamento General de Vehículos (Anexo XII, as amended by RD 518/2026: every motorcycle must
carry a reflective vest from 1 October 2026). The mechanics are your course's, with two corrections noted on the page
(two-stroke and four-stroke lubrication; chain slack).
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import moto_systems, strokes, oil_moto, chain_care, exhaust_smoke


def rows(pairs):
    return [[T(a, b)] for a, b in pairs]


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("How a motorcycle is built — <b>chassis, engine and transmission</b> — and its systems (<b>fuel, lubrication, cooling, electrical, steering and suspension</b>), what to check and when, "
         "the equipment it must carry, and how to read the most common <b>breakdowns</b>.",
         "Cómo está hecha una moto —<b>chasis, motor y transmisión</b>— y sus sistemas (<b>alimentación, lubricación, refrigeración, eléctrico, dirección y suspensión</b>), qué revisar y cuándo, "
         "lo que debe llevar y cómo interpretar las <b>averías</b> más comunes."),
        ("The exam asks above all: <b>two-stroke vs four-stroke</b>, how to <b>check and change the oil</b>, the two cooling systems, what to do with the <b>battery</b>, chain care <b>after rain</b>, "
         "the <b>colour of the exhaust smoke</b>, and that accessories must be <b>approved</b>.",
         "El examen pregunta sobre todo: <b>dos tiempos y cuatro tiempos</b>, cómo <b>comprobar y cambiar el aceite</b>, los dos sistemas de refrigeración, la <b>batería</b>, el cuidado de la cadena <b>tras la lluvia</b>, "
         "el <b>color del humo del escape</b> y que los accesorios deben estar <b>homologados</b>."),
        ("The sections follow your A1/A2 course’s Topic 13. Two slips in the course are corrected and flagged: the lubrication of <b>two- and four-stroke</b> engines, and the <b>chain slack</b>. "
         "Spanish exam terms are in <i>italics</i>, and a glossary closes the topic.",
         "Los apartados siguen el Tema 13 de tu curso A1/A2. Se corrigen y señalan dos errores del curso: la lubricación de los motores de <b>dos y cuatro tiempos</b> y la <b>holgura de la cadena</b>. "
         "Al final hay un glosario español–inglés."),
    ]))

    # ---------------------------------------------------------------- 1. mechanics
    B.append(H2("1", "Mechanics and maintenance", "Mecánica y mantenimiento"))
    B.append(P(
        "For a motorcycle to work well it must be kept in <b>perfect condition</b>, with the <b>checks</b> done as often as they are due. A motorcycle is made of a <b>chassis</b>, an <b>engine</b> and a <b>transmission</b>, plus several other systems.",
        "Para su buen funcionamiento, la moto debe mantenerse en <b>perfecto estado de funcionamiento y conservación</b>, con las <b>revisiones</b> necesarias en la frecuencia que corresponda. Está formada por un <b>chasis</b>, un <b>motor</b> y una <b>transmisión</b>, además de otros sistemas."))
    B.append(FIG(moto_systems, "The frame carries everything; the engine drives the rear wheel through the transmission; the other systems feed, lubricate, cool, power, steer and cushion it.",
                 "El bastidor sostiene todo; el motor mueve la rueda trasera a través de la transmisión; los demás sistemas lo alimentan, lubrican, refrigeran, dan corriente, dirigen y amortiguan."))
    B.append(TABLE(
        [T("Part", "Parte"), T("What it is", "Qué es")],
        [
            [T("<b>Chassis or frame</b> (<i>bastidor</i>)", "<b>Chasis o bastidor</b>"), T("A <b>steel or aluminium</b> structure — strong and light — that carries all the systems and parts.", "Estructura de <b>acero o aluminio</b> (resistente y ligera) que soporta todos los sistemas y elementos.")],
            [T("<b>Engine</b>", "<b>Motor</b>"), T("Turns energy into <b>mechanical energy</b> to move the motorcycle. It can be <b>two-stroke</b> or <b>four-stroke</b>.", "Transforma la energía en <b>energía mecánica</b> para desplazar la moto. Puede ser de <b>dos tiempos</b> o de <b>cuatro tiempos</b>.")],
            [T("<b>Transmission</b>", "<b>Transmisión</b>"), T("Takes the engine’s movement to the <b>driving wheel</b> (the <b>rear</b> one).", "Traslada el movimiento del motor a la <b>rueda motriz</b> (la <b>trasera</b>).")],
        ],
        widths=["28%", "72%"],
    ))
    B.append(FIG(strokes, "A two-stroke does the four phases in two piston strokes and burns oil mixed with the petrol; a four-stroke needs four strokes and keeps its oil in the crankcase.",
                 "El de dos tiempos hace las cuatro fases en dos movimientos del pistón y quema el aceite mezclado con la gasolina; el de cuatro tiempos necesita cuatro y guarda el aceite en el cárter."))
    B.append(TABLE(
        [T("Engine", "Motor"), T("Phases", "Fases"), T("Oil", "Aceite")],
        [
            [T("<b>Two-stroke</b> (<i>dos tiempos</i>)", "<b>Dos tiempos</b>"), T("The piston does <b>intake, compression, explosion and exhaust</b> in <b>two movements</b>.", "El pistón realiza <b>admisión, compresión, explosión y escape</b> en <b>dos movimientos</b>."),
             T("<b>Mixed into the petrol</b>, in the proportion the manufacturer gives, or from a separate <b>oil tank</b> (top it up regularly) whose pump sends it to the carburettor or injection. It burns with the fuel.",
               "<b>Se añade a la gasolina</b> en la proporción del fabricante, o va a un <b>depósito</b> (hay que reponerlo periódicamente) desde el que una bomba o dosificador lo mezcla con la gasolina. Se quema con el combustible.")],
            [T("<b>Four-stroke</b> (<i>cuatro tiempos</i>)", "<b>Cuatro tiempos</b>"), T("<b>Four</b> phases, one per piston movement.", "<b>Cuatro</b> fases, una por cada movimiento del pistón."),
             T("Kept in the <b>crankcase</b>, checked with a dipstick or sight glass; the fuel mixture is <b>air and petrol</b>.", "Va en el <b>cárter</b> y se comprueba con varilla o mirilla; la mezcla de combustible es de <b>aire y gasolina</b>.")],
        ],
        widths=["20%", "34%", "46%"],
        cls="small",
    ))
    B.append(BOX("trap", "A slip in your course", "Un error de tu curso", [
        ("The course’s introduction says a two-stroke runs on “petrol and air, without oil” and a four-stroke on “petrol, air and oil”. It is the <b>other way round</b> — as the course’s own lubrication section says: "
         "a <b>two-stroke</b> takes its oil <b>with the petrol</b>; a <b>four-stroke</b> keeps it in the <b>crankcase</b>.",
         "La introducción del curso dice que el de dos tiempos funciona con «gasolina y aire, no lleva aceite» y el de cuatro con «gasolina, aire y aceite». Es <b>al revés</b>, como dice el propio apartado de lubricación del curso: "
         "el de <b>dos tiempos</b> lleva el aceite <b>con la gasolina</b>; el de <b>cuatro tiempos</b> lo tiene en el <b>cárter</b>."),
    ]))

    B.append(H3("1.1 Fuel system", "1.1 Sistema de alimentación"))
    B.append(P("It delivers to the <b>cylinders</b> the right amount of <b>air and fuel</b> for the engine to work properly.",
               "Es el encargado de hacer llegar a los <b>cilindros</b> la cantidad de <b>aire y combustible</b> necesaria para su correcto funcionamiento."))
    B.append(TABLE(
        [T("Part", "Componente"), T("What it does", "Qué hace")],
        [
            [T("<b>Air filter</b>", "<b>Filtro de aire</b>"), T("Lets only <b>clean air</b> into the engine. Change it regularly as the manufacturer says — more often in <b>summer</b> and on <b>dusty tracks</b>. A <b>dirty filter</b> means <b>more fuel use and more pollution</b>.",
                                                              "Asegura la entrada de <b>aire limpio</b>. Cambiarlo regularmente según el fabricante, sobre todo en <b>verano</b> y por <b>caminos polvorientos</b>. Un <b>filtro sucio</b> supone <b>más consumo y más contaminación</b>.")],
            [T("<b>Carburettor</b>", "<b>Carburador</b>"), T("Makes the mixture of air and petrol in the right proportion. Now <b>giving way to electronic injection</b>.", "Elabora la mezcla de aire y gasolina en la proporción adecuada. Hoy <b>en desuso frente a la inyección electrónica</b>.")],
            [T("<b>Injection</b>", "<b>Inyección</b>"), T("A pump injects fuel <b>under pressure</b> into the intake; <b>sensors</b> give each cylinder the exact amount at each moment.", "Una bomba inyecta combustible <b>a presión</b> en la admisión; mediante <b>sensores</b>, cada cilindro recibe en cada momento la cantidad precisa.")],
        ],
        widths=["22%", "78%"],
    ))
    B.append(BOX("key", "Maintenance", "Mantenimiento", [
        ("Regularly <b>clean the carburettor</b> and <b>clean or replace the air filter</b>, to avoid using too much fuel.", "Periódicamente, <b>limpiar el carburador</b> y <b>limpiar o sustituir el filtro del aire</b> para evitar un consumo excesivo."),
        ("Adjust the <b>idle speed</b> (<i>ralentí</i>) when needed.", "Regular el <b>ralentí</b> cuando sea necesario."),
    ]))

    B.append(H3("1.2 Lubrication", "1.2 Sistema de lubricación"))
    B.append(P("It puts a <b>film of oil</b> between the engine’s metal parts to <b>reduce friction</b> and <b>prevent early wear</b>.",
               "Interpone una <b>película de aceite</b> entre las piezas metálicas del motor para <b>reducir el rozamiento</b> y <b>evitar un desgaste prematuro</b>."))
    B.append(FIG(oil_moto, "Four-stroke: check the oil cold, with the motorcycle upright, between MIN and MAX; change it warm. Used oil goes to a collection point.",
                 "Cuatro tiempos: comprueba el aceite en frío y con la moto vertical, entre MIN y MAX; cámbialo en caliente. El aceite usado va a un punto de recogida."))
    B.append(TABLE(
        [T("Engine", "Motor"), T("What to do", "Qué hacer")],
        [
            [T("<b>Four-stroke</b>", "<b>Cuatro tiempos</b>"),
             T("<b>Check the level regularly</b> with the <b>engine stopped and cold</b> and the motorcycle <b>upright and level</b>, with the <b>dipstick</b>: keep it between <b>MIN and MAX</b>. "
               "<b>Change</b> it regularly with the <b>engine warm</b> and the motorcycle upright, and the <b>filter</b> as the manufacturer says.",
               "<b>Comprobar periódicamente el nivel</b> con el <b>motor parado y frío</b> y la moto <b>en posición horizontal</b>, mediante la <b>varilla</b>: entre <b>mínimo y máximo</b>. "
               "<b>Cambiarlo</b> periódicamente con el <b>motor caliente</b> y en posición horizontal, y el <b>filtro</b> según el fabricante.")],
            [T("<b>Two-stroke</b>", "<b>Dos tiempos</b>"),
             T("The oil is <b>added to the petrol</b> in the manufacturer’s proportion, or goes into an <b>oil tank</b> that must be <b>topped up</b> regularly.", "El aceite se <b>añade a la gasolina</b> en la proporción del fabricante, o va a un <b>depósito</b> que hay que <b>reponer</b> periódicamente.")],
        ],
        widths=["20%", "80%"],
    ))
    B.append(BOX("trap", "Used oil", "Aceite usado", [
        ("Oil is <b>highly polluting</b>: when you change it, it must not fall on the ground or go down the drain. Take it to a <b>recycling or collection point</b>.",
         "El aceite es <b>altamente contaminante</b>: al cambiarlo no debe caer al suelo ni derramarse en la alcantarilla. Debe ir a un <b>centro de reciclaje o recogida</b>."),
    ]))

    B.append(H3("1.3 Cooling", "1.3 Sistema de refrigeración"))
    B.append(TABLE(
        [T("System", "Sistema"), T("How it works", "Cómo funciona"), T("Maintenance", "Mantenimiento")],
        [
            [T("<b>Air</b>", "<b>Por aire</b>"), T("<b>Direct</b> air from the motorcycle’s movement, or <b>forced</b> by a fan or turbine driven by the engine.", "Aire <b>directo</b> por el movimiento de la moto, o <b>forzado</b> por un ventilador o turbina que mueve el motor."),
             T("Clean and keep in perfect condition the <b>cooling fins</b> and the <b>turbine’s protective slots</b>.", "Limpiar y mantener en perfecto estado las <b>aletas exteriores</b> y las <b>ranuras de protección de la turbina</b>.")],
            [T("<b>Liquid</b>", "<b>Por líquido</b>"), T("Coolant runs through passages in the engine block, driven by a <b>pump</b>.", "El líquido recorre el bloque motor por huecos o cámaras, impulsado por una <b>bomba</b>."),
             T("Check the <b>coolant level</b> regularly; top it up or change it when the manufacturer says.", "Comprobar periódicamente el <b>nivel del líquido refrigerante</b>, añadiendo o cambiándolo cuando lo recomiende el fabricante.")],
        ],
        widths=["14%", "43%", "43%"],
        cls="small",
    ))

    B.append(H3("1.4 Electrical system", "1.4 Sistema eléctrico"))
    B.append(P("The <b>battery</b> supplies the electrical energy the motorcycle needs <b>while the engine is stopped</b>.",
               "La <b>batería</b> proporciona la <b>energía eléctrica</b> que necesita el vehículo <b>mientras el motor está parado</b>."))
    B.append(TABLE(
        [T("Circuit", "Circuito"), T("What it does", "Qué hace")],
        [
            [T("<b>Starting circuit</b>", "<b>Circuito de arranque</b>"), T("A switch (button or ignition key) turns an <b>electric motor</b> that gives the engine its <b>first turns</b>.", "Un interruptor (pulsador o llave de contacto) hace girar un <b>motor eléctrico</b> que da al motor sus <b>primeros giros</b>.")],
            [T("<b>Ignition circuit</b>", "<b>Circuito de encendido</b>"), T("Makes a <b>spark</b> with the <b>spark plug</b> inside the cylinder of a petrol engine, to ignite the air–fuel mixture.", "Provoca una <b>chispa</b> mediante la <b>bujía</b> dentro del cilindro de los motores de gasolina, para encender la mezcla de aire y carburante.")],
        ],
        widths=["26%", "74%"],
    ))
    B.append(BOX("key", "Maintenance", "Mantenimiento", [
        ("Check the <b>battery electrolyte</b> (sulphuric acid and distilled water) regularly; if it is low, add <b>distilled water only</b>. Keep the <b>terminals</b> and the gas vents clean. Many batteries today are <b>maintenance-free</b>.",
         "Verificar periódicamente el nivel del <b>electrolito</b> (ácido sulfúrico y agua destilada); si hace falta, añadir <b>solo agua destilada</b>. Mantener limpios los <b>bornes</b> y los orificios de salida de gases. Hoy muchas baterías <b>no requieren mantenimiento</b>."),
        ("Check the <b>spark plugs</b> and the engine <b>tuning</b>.", "Verificar el estado de las <b>bujías</b> y la <b>puesta a punto</b> del motor."),
    ]))

    B.append(H3("1.5 Transmission", "1.5 Sistema de transmisión"))
    B.append(TABLE(
        [T("Part", "Elemento"), T("What it does", "Qué hace")],
        [
            [T("<b>Clutch</b>", "<b>Embrague</b>"), T("Connects or cuts the engine’s movement to the gearbox.", "Transmite o interrumpe el movimiento del motor a la caja de velocidades.")],
            [T("<b>Gearbox</b>", "<b>Caja de cambios</b>"), T("Adapts the motorcycle’s pace to what is needed.", "Permite adaptar la marcha del vehículo según convenga.")],
            [T("<b>Final drive</b>", "<b>Transmisión final</b>"), T("Links the gearbox to the rear wheel: <b>chain</b>, <b>belt</b> or <b>shaft</b> (<i>cardan</i>).", "Une la caja de cambios con la rueda trasera: <b>cadena</b>, <b>correa</b> o <b>cardan</b>.")],
        ],
        widths=["24%", "76%"],
    ))
    B.append(BOX("key", "Maintenance", "Mantenimiento", [
        ("Regularly check the <b>clutch disc</b> adjustment (replace it when due), the <b>gearbox lubrication</b>, and the chain’s <b>tension and greasing</b> — <b>especially after riding in the rain</b>.",
         "Verificar periódicamente el ajuste del <b>disco de embrague</b> (sustituirlo cuando proceda), el <b>lubricado de la caja de velocidades</b>, y el <b>tensado y engrase de la cadena</b>, <b>especialmente después de circular con lluvia</b>."),
        ("A <b>shaft drive</b> needs little maintenance: an <b>oil change every 10,000 or 15,000 km</b> (your course; follow the manufacturer).", "El <b>cardan</b> requiere un mantenimiento mínimo: <b>cambio de aceite cada 10.000 o 15.000 km</b> (tu curso; sigue al fabricante)."),
    ]))
    B.append(FIG(chain_care, "Check the slack in the middle of the lower run with the wheel on the ground; tension and grease the chain regularly, and always after rain.",
                 "Comprueba la holgura en el centro del tramo inferior con la rueda en el suelo; tensa y engrasa la cadena periódicamente, y siempre después de la lluvia."))
    B.append(BOX("trap", "Chain slack: millimetres or centimetres?", "Holgura de la cadena: ¿milímetros o centímetros?", [
        ("Your course says to tension the chain “until the slack is between <b>2 and 3 mm</b>”. Owner’s manuals usually give about <b>20–30 mm</b> (2–3 cm), measured in the middle of the lower run; "
         "a chain with only 2–3 mm of play would be <b>far too tight</b> and would wear the chain, sprockets and bearings. Follow your motorcycle’s manual.",
         "Tu curso dice tensar la cadena «hasta una holgura entre <b>2 y 3 mm</b>». Los manuales suelen indicar unos <b>20–30 mm</b> (2–3 cm), medidos en el centro del tramo inferior; "
         "una cadena con solo 2–3 mm de juego estaría <b>demasiado tensa</b> y desgastaría cadena, piñones y rodamientos. Sigue el manual de tu moto."),
    ]))

    B.append(H3("1.6 Steering and suspension", "1.6 Sistema de dirección y suspensión"))
    B.append(TABLE(
        [T("System", "Sistema"), T("What to know", "Lo que hay que saber")],
        [
            [T("<b>Steering</b>", "<b>Dirección</b>"),
             T("Controlled with the <b>handlebar</b>, held <b>firmly but not rigidly</b>: a small movement changes the front wheel’s angle at once. A good design gives smooth, stable riding, with the <b>steering-head bearings</b> (in the <i>tija</i>) <b>without play or stiffness</b>.",
               "Se controla con el <b>manillar</b>, manejado <b>con firmeza pero sin rigidez</b>: un pequeño movimiento cambia al instante el ángulo de la rueda delantera. Un buen diseño da una conducción suave y estable, con los <b>rodamientos</b> (dentro de la <b>tija</b>) <b>sin holguras ni agarrotamiento</b>.")],
            [T("<b>Suspension</b>", "<b>Suspensión</b>"),
             T("Keeps <b>even contact with the ground</b>, avoiding sudden movements and giving some comfort to rider and passenger. The rear usually has a <b>swingarm</b>; check the <b>shock absorbers</b> regularly — they <b>affect control</b>.",
               "Asegura un <b>contacto uniforme con el suelo</b>, evitando movimientos bruscos y dando cierto confort a conductor y acompañante. La trasera suele ser por <b>horquilla oscilante</b> (basculante); hay que revisar los <b>amortiguadores</b>, que <b>afectan al control</b>.")],
        ],
        widths=["20%", "80%"],
    ))

    B.append(H3("1.7 Accessories and spares", "1.7 Accesorios y repuestos"))
    B.append(TABLE(
        [T("Rule", "Norma")],
        rows([
            ("Any <b>accessory</b> you fit (racks, fairings, anti-theft devices, levers, mirrors, exhausts, shock absorbers…) must be <b>approved</b> (<i>homologado</i>), whether it is the manufacturer’s or another make. "
             "A <b>major modification</b> also needs an extraordinary ITV inspection before you ride again (Topic 9).",
             "Cualquier <b>accesorio</b> que se instale (portaequipajes, carenados, antirrobos, manetas, retrovisores, escapes, amortiguadores…) debe estar <b>homologado</b>, sea del fabricante o de otro. "
             "Una <b>reforma de importancia</b> exige además una ITV extraordinaria antes de volver a circular (Tema 9)."),
            ("<b>No spare part is compulsory</b> on a motorcycle. Carrying <b>spare bulbs</b> is recommended: agents may <b>immobilise</b> a vehicle with a blown light.",
             "En la moto <b>no es obligatorio llevar ningún repuesto</b>. Es recomendable llevar <b>lámparas de repuesto</b>: los agentes pueden <b>inmovilizar</b> el vehículo con una luz fundida."),
        ]),
    ))
    B.append(BOX("trap", "New since 1 October 2026: the vest is compulsory equipment", "Novedad desde el 1 de octubre de 2026: el chaleco es dotación obligatoria", [
        ("Spare parts are still optional, but every motorcycle must now <b>carry a high-visibility reflective vest</b> (Reglamento General de Vehículos, Anexo XII). Wear it when you get off and stand on the carriageway or shoulder of an interurban road.",
         "Los repuestos siguen siendo opcionales, pero toda motocicleta debe ahora <b>llevar un chaleco reflectante de alta visibilidad</b> (Reglamento General de Vehículos, anexo XII). Se usa al bajarse y ocupar la calzada o el arcén de una vía interurbana."),
        ("The <b>V-16</b> light, compulsory in cars, is <b>recommended, not compulsory</b> on motorcycles.", "La luz <b>V-16</b>, obligatoria en los turismos, es <b>recomendable, no obligatoria</b> en las motos."),
    ]))

    B.append(H3("1.8 Maintenance and breakdowns", "1.8 Mantenimiento y averías"))
    B.append(P("With some <b>general mechanical knowledge</b> — without going to a workshop — you can:", "Con unos <b>conocimientos mecánicos generales</b>, sin necesidad de acudir a un taller especializado, se puede:"))
    B.append(TABLE(
        [T("Basic maintenance you can do", "Mantenimiento que puedes hacer")],
        rows([
            ("<b>Adjust and change</b> the control <b>pedals</b>.", "<b>Ajustar y cambiar</b> los <b>pedales de mando</b>."),
            ("<b>Tighten</b> some nuts and bolts (rear-axle split pin, front-axle clamp, rear shock, steering head, axles, footrests…).", "<b>Apretar</b> algunas tuercas y tornillos (pasador del eje trasero, abrazadera del eje delantero, amortiguador trasero, tija de dirección, ejes, estriberas…)."),
            ("<b>Adjust the chain</b> (tension it regularly) and <b>grease and lubricate</b> the main parts.", "<b>Ajustar la cadena</b> (tensarla periódicamente) y <b>engrasar y lubricar</b> las piezas fundamentales."),
            ("<b>Clean the air filter</b>.", "<b>Limpiar el filtro del aire</b>."),
        ]),
    ))
    B.append(FIG(exhaust_smoke, "Black smoke: too much fuel. Bluish white: the engine is burning oil. White: water condensed in the exhaust evaporating.",
                 "Humo negro: consumo excesivo de combustible. Blanco azulado: el motor quema aceite. Blanco: evaporación del agua condensada en el escape."))
    B.append(TABLE(
        [T("Problem", "Avería"), T("Possible causes", "Posibles causas")],
        [
            [T("<b>Engine won’t start</b>", "<b>El motor no arranca</b>"), T("Flat battery or bad connections; spark plug in poor condition; <b>no fuel</b> getting through; faulty starter button or key.", "Batería descargada o problema en las conexiones; bujía en malas condiciones; <b>no llega combustible</b>; fallo en el pulsador o la llave de arranque.")],
            [T("<b>Clutch drags</b> (hard to disengage)", "<b>Problemas al desembragar</b>"), T("Oil in poor condition, <b>too thick</b>, or <b>too much</b> oil.", "Aceite en mal estado, <b>muy viscoso</b>, o <b>exceso de nivel</b>.")],
            [T("<b>Loss of power at high speed</b>", "<b>Falta de potencia a alta velocidad</b>"),
             T("Wrong, dirty, broken or badly gapped <b>spark plug</b>; wrong fuel level in the carburettor; blocked air vents or jet; <b>air filter</b> in poor condition; <b>dragging brake</b>; pre-ignition from the wrong fuel or plugs.",
               "<b>Bujía</b> inapropiada, sucia, rota o mal ajustada; nivel de combustible inadecuado en el carburador; orificios de purga o surtidor atascados; <b>filtro del aire</b> en mal estado; <b>rozamiento del freno</b>; autoencendido por combustible o bujías incorrectos.")],
            [T("<b>Poor running at low speed</b>", "<b>Fallos a baja velocidad</b>"), T("Air filter blocked or badly fitted; <b>dirty carburettor</b>; wrong air–petrol mixture.", "Filtro del aire obstruido o mal instalado; <b>carburador sucio</b>; mezcla incorrecta de aire y gasolina.")],
            [T("<b>Exhaust smoke</b>", "<b>Humo del escape</b>"), T("<b>Black</b>: too much fuel. <b>Bluish white</b>: too much oil being burnt. <b>White</b>: condensed water evaporating.", "<b>Negro</b>: consumo excesivo de combustible. <b>Blanco azulado</b>: consumo excesivo de aceite. <b>Blanco</b>: evaporación del agua condensada.")],
            [T("<b>Unstable handling</b>", "<b>Conducción inestable</b>"), T("Low tyre pressure or uneven wear; <b>misaligned wheel</b>; bent or unbalanced rim; <b>steering head too tight</b>.", "Falta de presión o desgaste desigual de los neumáticos; <b>rueda desalineada</b>; llanta torcida o desequilibrada; <b>tija de dirección demasiado apretada</b>.")],
            [T("<b>Overheating</b>", "<b>Recalentamiento</b>"), T("Wrong, dirty, broken or badly gapped spark plug; air filter in poor condition; <b>low coolant</b>; lubrication problems; low fuel level in the carburettor’s float bowl.",
                                                                "Bujía inapropiada, sucia, rota o mal ajustada; filtro del aire en mal estado; <b>nivel de refrigerante bajo</b>; problemas de lubricación; nivel bajo de combustible en la cuba del flotador del carburador.")],
        ],
        widths=["28%", "72%"],
        cls="small",
    ))

    # ---------------------------------------------------------------- 2. traps
    B.append(H2("2", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("Two-stroke: the four phases in <b>two</b> piston movements; oil <b>mixed with the petrol</b>. Four-stroke: <b>four</b> movements; oil in the <b>crankcase</b>.", "Dos tiempos: las cuatro fases en <b>dos</b> movimientos; aceite <b>con la gasolina</b>. Cuatro tiempos: <b>cuatro</b> movimientos; aceite en el <b>cárter</b>."),
        ("Oil level: <b>engine stopped and cold</b>, motorcycle <b>upright</b>, between MIN and MAX. Oil change: <b>engine warm</b>. Used oil: <b>never down the drain</b>.", "Nivel de aceite: <b>motor parado y frío</b>, moto <b>vertical</b>, entre MIN y MAX. Cambio: <b>motor caliente</b>. Aceite usado: <b>nunca a la alcantarilla</b>."),
        ("A <b>dirty air filter</b> means more fuel and more pollution; change it more often in summer and on dusty tracks.", "Un <b>filtro del aire sucio</b> supone más consumo y contaminación; cambiarlo más a menudo en verano y por caminos polvorientos."),
        ("Air cooling: keep the <b>fins</b> clean. Liquid cooling: check the <b>coolant level</b>.", "Refrigeración por aire: <b>aletas</b> limpias. Por líquido: <b>nivel del refrigerante</b>."),
        ("The battery powers the motorcycle <b>with the engine stopped</b>. Top up the electrolyte with <b>distilled water only</b>.", "La batería da corriente <b>con el motor parado</b>. El electrolito se repone <b>solo con agua destilada</b>."),
        ("After rain: <b>grease and tension the chain</b>, and grease cables, levers, pedals and stands.", "Tras la lluvia: <b>engrasar y tensar la cadena</b>, y engrasar cables, manetas, pedales y caballetes."),
        ("Shaft drive: little maintenance — oil every <b>10,000–15,000 km</b> (your course).", "Cardan: mantenimiento mínimo, aceite cada <b>10.000–15.000 km</b> (tu curso)."),
        ("Accessories: always <b>approved</b>. Spare parts: <b>none compulsory</b>, spare bulbs recommended. Vest: <b>compulsory</b> since 1 October 2026.", "Accesorios: siempre <b>homologados</b>. Repuestos: <b>ninguno obligatorio</b>, recomendables las lámparas. Chaleco: <b>obligatorio</b> desde el 1 de octubre de 2026."),
        ("Smoke: <b>black</b> = fuel, <b>bluish white</b> = oil, <b>white</b> = condensed water.", "Humo: <b>negro</b> = combustible, <b>blanco azulado</b> = aceite, <b>blanco</b> = agua condensada."),
        ("Unstable handling: tyres, a misaligned wheel, a bent rim, or a <b>steering head too tight</b>.", "Conducción inestable: neumáticos, rueda desalineada, llanta torcida o <b>tija demasiado apretada</b>."),
    ]))

    # ---------------------------------------------------------------- 3. numbers
    B.append(H2("3", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Piston movements per cycle: two-stroke / four-stroke", "Movimientos del pistón por ciclo: dos / cuatro tiempos"), T("2 / 4", "2 / 4")],
            [T("Shaft-drive oil change (course)", "Cambio de aceite del cardan (curso)"), T("every 10,000–15,000 km", "cada 10.000–15.000 km")],
            [T("Chain slack (owner’s manuals; course: 2–3 mm)", "Holgura de la cadena (manuales; curso: 2–3 mm)"), T("about 20–30 mm", "unos 20–30 mm")],
            [T("Compulsory spare parts on a motorcycle", "Repuestos obligatorios en la moto"), T("none", "ninguno")],
            [T("Compulsory equipment on a motorcycle (since 1 October 2026)", "Dotación obligatoria de la moto (desde el 1 de octubre de 2026)"), T("a high-visibility vest", "un chaleco de alta visibilidad")],
        ],
        widths=["62%", "38%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["en2", "en4", "fu2", "lu2", "lu5", "co1", "el2", "tr2", "tr4", "ac1", "ac4", "br3"]


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
    ("Reglamento General de Vehículos (RD 2822/1998), Anexo XII: accessories, spares and tools — consolidated text (motorcycles: a vest since 1 October 2026)", "https://www.boe.es/buscar/act.php?id=BOE-A-1999-1826"),
    ("Real Decreto 518/2026 (in force 1 October 2026), final provision 2: the vest in motorcycles’ compulsory equipment", "https://www.boe.es/buscar/doc.php?id=BOE-A-2026-13889"),
    ("Real Decreto 920/2017: ITV, including inspections after major modifications — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2017-12841"),
    ("Motor16: motorcycle chain maintenance (slack usually 20–30 mm, per the owner’s manual)", "https://www.motor16.com/las-ultimas-noticias/mantenimiento-cadena-moto-tensar-itv/"),
]

GLOSSARY = [
    ("chasis · bastidor", "chassis · frame"),
    ("motor de dos / cuatro tiempos", "two-stroke / four-stroke engine"),
    ("admisión · compresión · explosión · escape", "intake · compression · combustion · exhaust"),
    ("pistón · cilindro · cárter", "piston · cylinder · crankcase"),
    ("sistema de alimentación", "fuel system"),
    ("filtro del aire · carburador · inyección", "air filter · carburettor · fuel injection"),
    ("ralentí", "idle speed"),
    ("varilla · mirilla del aceite", "dipstick · oil sight glass"),
    ("refrigeración por aire · por líquido", "air · liquid cooling"),
    ("aletas · radiador · líquido refrigerante", "cooling fins · radiator · coolant"),
    ("batería · electrolito · bornes", "battery · electrolyte · terminals"),
    ("bujía · puesta a punto", "spark plug · engine tuning"),
    ("embrague · caja de cambios", "clutch · gearbox"),
    ("cadena · correa · cardan", "chain · belt · shaft drive"),
    ("corona · piñón · holgura", "rear sprocket · front sprocket · slack"),
    ("tija de dirección · rodamientos", "steering head · bearings"),
    ("horquilla oscilante (basculante) · amortiguador", "swingarm · shock absorber"),
    ("accesorio homologado · reforma de importancia", "approved accessory · major modification"),
    ("repuesto · lámpara de repuesto", "spare part · spare bulb"),
    ("humo negro / blanco azulado / blanco", "black / bluish-white / white smoke"),
    ("recalentamiento · avería", "overheating · breakdown"),
]
