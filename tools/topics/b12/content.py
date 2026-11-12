# -*- coding: utf-8 -*-
"""Topic 12 content (driving techniques: preventive and efficient driving, pollution, low-emission zones and
environmental labels), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Tema 12: Técnicas de conducción). The wording and the figures
are original; the rules come from the Reglamento General de Circulación and the Reglamento General de Vehículos, the
Ley de Cambio Climático (Ley 7/2021, art. 14) for low-emission zones, the sign catalogue (RD 465/2025) for the R-120
sign, and the DGT's environmental-label criteria, as they stand in November 2026.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import blind_spots, time_gap, queue_gap, uncertainty, mirrors, rev_bands, eco_labels
from ..b08.signs import ICON


def rows(pairs):
    """[(en, es), ...] -> one-column table rows."""
    return [[T(a, b)] for a, b in pairs]


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Two families of techniques. <b>Preventive driving</b> (safety) rests on three principles: <b>vision</b>, <b>anticipation</b> and <b>space control</b>. "
         "<b>Efficient driving</b> saves fuel and pollutes less: high gears, low revs, smooth speed.",
         "Dos familias de técnicas. La <b>conducción preventiva</b> (seguridad) se basa en tres principios: <b>visión</b>, <b>anticipación</b> y <b>control del espacio</b>. "
         "La <b>conducción eficiente</b> ahorra combustible y contamina menos: marchas largas, pocas revoluciones, velocidad uniforme."),
        ("The exam loves <b>numbers</b>: mirrors every <b>5–10 s</b> in town and <b>10–15 s</b> on motorways, head turn <b>45°</b>, gap <b>2 s</b> in town and <b>3 s</b> on the road (<b>+1 s</b>), <b>2–3 m</b> when stopped, "
         "<b>5–6 m</b> if last in the queue, change gear at <b>1,500–2,000</b> rpm (diesel) or <b>2,000–2,500</b> (petrol), engine off after <b>60 s</b>, air conditioning at <b>23 °C</b>.",
         "El examen pregunta sobre todo <b>cifras</b>: retrovisores cada <b>5–10 s</b> en ciudad y <b>10–15 s</b> en autovía, giro de cabeza de <b>45°</b>, distancia de <b>2 s</b> en ciudad y <b>3 s</b> en carretera (<b>+1 s</b>), <b>2–3 m</b> al detenerse, "
         "<b>5–6 m</b> si eres el último de la cola, cambiar a <b>1.500–2.000</b> rpm (diésel) o <b>2.000–2.500</b> (gasolina), apagar el motor a partir de <b>60 s</b>, climatización a <b>23 °C</b>."),
        ("The sections follow the order of your course’s Topic 12. Spanish exam terms are in <i>italics</i> in the English text, and a glossary closes the topic.",
         "Los apartados siguen el orden del Tema 12 de tu curso. Al final hay un glosario español–inglés."),
    ]))

    # ---------------------------------------------------------------- 1. preventive driving
    B.append(H2("1", "Preventive driving techniques", "Técnicas de conducción preventiva"))
    B.append(P(
        "Preventive driving lets you drive <b>more safely</b>, gathering all the information you need from your surroundings so you can <b>react faster</b> to anything unexpected. "
        "It rests on <b>three basic principles: vision, anticipation and space control</b>.",
        "Las técnicas de conducción preventiva <b>permiten circular de una manera más segura</b>, recogiendo toda la información necesaria del entorno para <b>reaccionar con mayor rapidez</b> ante cualquier imprevisto. "
        "Se basan en <b>tres principios básicos: visión, anticipación y control del espacio</b>."))

    B.append(H3("1.1 Vision", "1.1 Técnicas de visión"))
    B.append(P("<b>Don’t look only at the vehicle in front.</b> It is recommended to:", "<b>No hay que limitarse a mirar al vehículo de delante.</b> Se recomienda:"))
    B.append(TABLE(
        [T("Technique", "Técnica"), T("What it means", "Qué supone")],
        [
            [T("<b>Look far ahead</b>", "<b>Mirar a lo lejos</b>"), T("Especially at higher speeds: look at the point where you will be in a few seconds.", "Sobre todo a mayor velocidad: mirar al punto donde vamos a estar dentro de unos segundos.")],
            [T("<b>Look to the sides often</b>", "<b>Mirar a los lados con frecuencia</b>"), T("Check what is happening beside the vehicle, to spot any sudden movement on either side (a lane change, for example).", "Comprobar lo que sucede en el entorno lateral para percibir cualquier movimiento imprevisto a ambos lados (por ejemplo, un cambio de carril).")],
            [T("<b>Check the mirrors often</b>", "<b>Mirar por los retrovisores con frecuencia</b>"), T("Even when you are not about to manoeuvre, to keep track of the vehicles behind and beside you — especially in stressful or heavy traffic.", "Aunque no se vaya a hacer ninguna maniobra, para controlar a los vehículos que circulan detrás y a los lados, sobre todo con estrés o tráfico denso.")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(BOX("key", "How often to check the mirrors", "Frecuencia recomendada para mirar los retrovisores", [
        ("<b>In town</b> and on roads with heavy traffic: every <b>5–10 seconds</b>.", "<b>Vía urbana</b> (poblado) y carreteras con tráfico denso: cada <b>5–10 segundos</b>."),
        ("<b>Autopistas, autovías</b> and roads with little traffic: every <b>10–15 seconds</b>.", "<b>Autopista o autovía</b> y carreteras sin tráfico: cada <b>10–15 segundos</b>."),
    ]))
    B.append(BOX("trap", "The blind spot", "El ángulo muerto", [
        ("Even with well-adjusted mirrors there is always a <b>blind spot</b> (<i>ángulo muerto</i>): a place where you <b>can’t tell</b> whether another road user is there.", "Aunque los espejos estén bien reglados, siempre queda un <b>ángulo muerto</b>: un lugar donde <b>no podemos percibir</b> si existe otro usuario."),
        ("To reduce the risk, <b>turn your head about 45°</b> and check by looking directly — above all <b>before moving sideways</b>.", "Para reducir el riesgo hay que <b>girar la cabeza unos 45°</b> y comprobarlo con la visión directa, sobre todo <b>antes de un desplazamiento lateral</b>."),
    ]))
    B.append(FIG(blind_spots, "The mirrors cover the areas behind; beside and slightly behind the car each side there is a blind spot, big enough to hide a motorcycle or even a car.",
                 "Los espejos cubren las zonas de detrás; a cada lado, junto y algo por detrás del coche, queda un ángulo muerto en el que cabe una moto o incluso un coche."))

    B.append(H3("1.2 Anticipation (defensive driving)", "1.2 Anticipación (conducción defensiva)"))
    B.append(P("To have more time to react and enough space to avoid risks:", "Para disponer de más tiempo para reaccionar y de espacio suficiente para evitar riesgos, se recomienda:"))
    B.append(TABLE(
        [T("Principle", "Principio"), T("What it means", "Qué supone")],
        [
            [T("<b>Don’t trust other road users</b>", "<b>Desconfiar de los demás</b>"),
             T("Assume that <b>anyone can make a mistake</b>, be distracted, apply the rules badly or not know them, and put you at risk at any moment.", "Pensar que, en cualquier momento, <b>cualquier usuario puede cometer un error</b>, distraerse, aplicar mal las normas o desconocerlas, y ponernos en riesgo.")],
            [T("<b>Adapt to the circumstances</b>", "<b>Adaptar la conducción a las circunstancias</b>"),
             T("To stop safely without hitting anything, always drive at a <b>speed suited to the circumstances</b> (weather, traffic, road, vehicle and your own state). When you see a possible risk, "
               "<b>cover the brake pedal</b> with your foot.",
               "Para detener el vehículo con seguridad (sin colisionar), circular siempre a una <b>velocidad adecuada a las circunstancias</b> (meteorológicas, del tráfico, de la vía, del vehículo y del propio conductor). Ante un posible riesgo, "
               "<b>preparar el pie sobre el pedal del freno</b>.")],
            [T("<b>Be seen and understood</b>", "<b>Hacerse ver y entender</b>"),
             T("<b>Signal manoeuvres early</b> and keep signalling until they are finished. Use your <b>lights</b> well, especially when others may see you badly — for example when oncoming drivers have the <b>sun in their eyes</b> or are <b>leaving a tunnel</b>.",
               "<b>Señalizar las maniobras con suficiente antelación</b> y mantener la señal hasta terminarlas. Hacer un <b>uso adecuado del alumbrado</b>, sobre todo cuando nos puedan ver con dificultad (por ejemplo, cuando los que vienen de frente tienen el <b>sol de cara</b> o <b>salen de un túnel</b>).")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(BOX("key", "Other drivers’ blind spots", "Los ángulos muertos de los demás", [
        ("Avoid staying in <b>other vehicles’ blind spots</b>, especially <b>heavy vehicles</b> — their driver may not see you — or when you ride something small, such as a <b>motorcycle</b>.",
         "Evitar posicionarse en los <b>ángulos muertos de otros vehículos</b>, sobre todo si son <b>pesados</b> (su conductor puede no detectarnos) o si se conduce un vehículo pequeño, como una <b>motocicleta</b>."),
    ]))

    B.append(H3("1.3 Space control", "1.3 Control del espacio"))
    B.append(TABLE(
        [T("Space", "Espacio"), T("What to do", "Qué hacer")],
        [
            [T("<b>In front</b>", "<b>Delantero</b>"),
             T("Keep a gap of at least <b>2 seconds in town</b> and <b>3 seconds on the open road</b>. Add <b>at least one more second</b> in bad weather, when tired, on a poor surface, or when the vehicle behind is too close.",
               "Mantener una distancia de seguridad de al menos <b>2 segundos en zona urbana</b> y <b>3 segundos en carretera</b>. <b>Aumentarla al menos un segundo más</b> con condiciones adversas, cansancio, pavimento en mal estado o si el de detrás va demasiado cerca.")],
            [T("<b>Behind</b> — a vehicle too close", "<b>Trasero</b>: un vehículo muy cerca"),
             T("<b>Increase your front gap</b> by at least one second, <b>signal early</b>, and <b>brake gently and progressively</b>. If a rear-end collision looks likely, try to <b>move aside</b>; if you are stopped and can’t avoid it, <b>keep the brake on</b>.",
               "<b>Aumentar la distancia delantera</b> al menos un segundo, <b>señalizar con antelación</b> y <b>frenar con suavidad y progresivamente</b>. Ante un posible alcance, intentar <b>apartarse</b>; si estamos detenidos y no se puede evitar, <b>mantener el vehículo frenado</b>.")],
            [T("<b>To the sides</b>", "<b>Lateral</b>"), T("Others may move into your lane or space: drive preventively and keep out of their <b>zone of uncertainty</b>.", "Otros usuarios pueden invadir nuestro espacio lateral: conducción preventiva y evitar su <b>zona de incertidumbre</b>.")],
        ],
        widths=["26%", "74%"],
    ))
    B.append(FIG(time_gap, "Two seconds in town, three on the open road, and at least one more when conditions are worse.",
                 "Dos segundos en ciudad, tres en carretera y al menos uno más cuando las condiciones empeoran."))
    B.append(BOX("key", "Zone of uncertainty", "Zona de incertidumbre", [
        ("The <b>space around any road user</b> into which they may move <b>unexpectedly</b>.", "Es el <b>espacio que rodea a cualquier usuario</b> en el que se puede desplazar de un modo <b>imprevisto</b>."),
        ("<b>Cyclists</b>: a large side zone — they sway, above all on long climbs, and may turn suddenly. <b>Vehicles</b>: a large side zone (lane change, sudden turn, a <b>door opening</b>). "
         "<b>Pedestrians</b>: a smaller zone, except <b>children</b>, who are unpredictable and sometimes hard to see.",
         "<b>Ciclistas</b>: gran zona lateral (oscilan, sobre todo en ascensos prolongados, y pueden girar de improviso). <b>Vehículos</b>: gran zona lateral (cambio de carril, giro imprevisto, <b>apertura de una puerta</b>). "
         "<b>Peatones</b>: menor zona, salvo los <b>niños</b>, imprevisibles y a veces poco visibles."),
    ]))
    B.append(FIG(uncertainty, "Each road user has a zone where they may move without warning; give cyclists and children the most room.",
                 "Cada usuario tiene una zona donde puede moverse sin avisar; da más espacio a ciclistas y niños."))
    B.append(P(
        "When traffic makes you <b>stop</b>, leave at least <b>2–3 metres</b> to the vehicle in front — you should be able to <b>see its rear tyres on the road</b>. That lets you react if it <b>rolls back</b> (especially uphill), "
        "and gives you room to <b>get round it</b> if it breaks down.",
        "Si por las necesidades del tráfico hay que <b>detenerse</b>, guardar una distancia mínima de <b>2 o 3 metros</b> con el vehículo de delante (debemos <b>ver sus ruedas traseras sobre el suelo</b>). Así podemos anticiparnos si <b>va hacia atrás</b> (sobre todo en pendiente ascendente) "
        "y tenemos espacio para <b>adelantarlo o esquivarlo</b> si queda inmovilizado."))
    B.append(BOX("key", "If you are the last vehicle in the queue", "Si eres el último vehículo, para reducir el riesgo de alcance", [
        ("Switch on the <b>hazard lights</b> if the hold-up is <b>unexpected</b>, and leave <b>5–6 metres</b> to the vehicle in front.", "Encender la <b>señalización de emergencia</b> si es una <b>retención imprevista</b> y aumentar la distancia con el de delante hasta los <b>5 o 6 metros</b>."),
        ("Watch the <b>mirrors</b> and be ready to <b>escape</b> if you see a rear-end crash coming (first gear in, move aside quickly). Keep this up until <b>several vehicles have stopped behind you</b>.",
         "Mirar regularmente los <b>retrovisores</b> y preparar una <b>maniobra de evasión</b> si se prevé el alcance (meter 1.ª y apartarse rápidamente). Mantener estas medidas hasta que <b>se detengan varios vehículos por detrás</b>."),
    ]))
    B.append(FIG(queue_gap, "Stopped: 2–3 m, so you can see the rear tyres of the car in front. Last in the queue: 5–6 m and hazard lights.",
                 "Detenido: 2–3 m, para ver las ruedas traseras del de delante. Último de la cola: 5–6 m y luces de emergencia."))

    B.append(H3("1.4 Preventive safety equipment", "1.4 Elementos de seguridad preventiva"))
    B.append(P("Equipment that helps you <b>stay attentive</b> (climate control, ergonomics, comfort) or makes it easier to <b>see and respond</b>:",
               "Son los elementos que ayudan al conductor a <b>mantener la atención</b> (climatización, ergonomía, confort) o facilitan el <b>control visual y su respuesta</b>:"))
    B.append(TABLE(
        [T("Equipment", "Elemento"), T("Rules", "Normas")],
        [
            [T("<b>Windscreen and glass</b>", "<b>Parabrisas y superficies acristaladas</b>"),
             T("Must <b>not distort</b> what you see through them, must be <b>clean</b>, and if glass, <b>safety glass</b> (the windscreen is laminated). <b>Tinted or coloured glass that is not approved is prohibited.</b>",
               "No deben <b>deformar</b> los objetos vistos a través de ellos, deben estar <b>limpios</b> y, si son de vidrio, <b>de seguridad</b> (el parabrisas, laminado). <b>Prohibido colocar vidrios tintados o coloreados no homologados.</b>")],
            [T("<b>Wipers, washers, rear washer</b>", "<b>Limpiaparabrisas, lavaparabrisas y lavalunetas</b>"),
             T("They keep the glass clear in rain, snow or mud. Every car with <b>wipers</b> must have a <b>windscreen washer</b> (a tank under the bonnet that sprays the glass). The <b>rear washer</b> is <b>not compulsory</b>, but recommended.",
               "Facilitan la visión con lluvia, nieve, barro… Todo automóvil con <b>limpiaparabrisas</b> debe tener <b>lavaparabrisas</b> (un depósito bajo el capó que lanza chorros sobre el cristal). El <b>lavalunetas</b> <b>no es obligatorio</b>, pero sí recomendable.")],
            [T("<b>Demisters and de-icers</b>", "<b>Dispositivos antivaho/antihielo</b>"),
             T("The <b>heated rear window</b> (filaments that clear frost and mist) and the front system that blows warm or cold air at the windscreen.", "La <b>luneta térmica</b> trasera (filamentos que eliminan la escarcha o el vaho) y el dispositivo delantero que, con aire caliente o frío dirigido al parabrisas, evita que se empañe o elimina el vaho o el hielo.")],
        ],
        widths=["28%", "72%"],
    ))
    B.append(BOX("key", "Looking after wipers and washers", "Mantenimiento de limpiaparabrisas y lavaparabrisas", [
        ("<b>Replace the blades</b> if they are cracked, damaged, don’t clean well or scratch the glass. <b>Never use the wipers on a dry screen with an empty washer tank</b>: the dust scratches the glass and damages the blade.",
         "<b>Sustituir las escobillas</b> si están cuarteadas, dañadas, no limpian bien o arañan el cristal. <b>No usar el limpiaparabrisas con el depósito vacío y el cristal seco</b>: arrastraría polvo que raya el cristal y daña la escobilla."),
        ("Use the <b>slowest wiper speed</b> that works (less distraction and wear). Fill the washer with <b>distilled water and a cleaning agent</b> (soap), and keep the <b>jets clean</b> so they reach the top of the screen.",
         "Usar la <b>velocidad más lenta</b> posible (menos molestia visual y desgaste). Rellenar el lavaparabrisas con <b>agua destilada y un agente limpiador</b> (jabón) y mantener <b>limpios los orificios</b> para que los chorros lleguen a la parte superior."),
    ]))
    B.append(TABLE(
        [T("How many mirrors", "Cuántos espejos retrovisores"), T("Compulsory", "Obligatorios")],
        [
            [T("<b>Cars, lorries and vans</b> (up to 2 tonnes MMA)", "<b>Turismos, camiones y furgones</b> (hasta 2 t de MMA)"),
             T("An <b>outside left mirror</b> and an <b>interior mirror</b> that shows at least part of a flat road from the horizon to <b>60 m behind</b>, <b>20 m wide</b>. "
               "If the interior mirror can’t give that view (trailer, curtains, luggage…), an <b>outside right mirror</b> becomes compulsory; otherwise it is optional.",
               "Un <b>espejo exterior izquierdo</b> y un <b>espejo interior</b> que permita ver, al menos, una parte de la carretera plana desde el horizonte <b>hasta 60 m por detrás</b> y en <b>20 m de anchura</b>. "
               "Si el interior no permite esa visión (remolque, cortinillas, equipaje…), es obligatorio un <b>espejo exterior derecho</b>; si no, es opcional.")],
            [T("<b>Motorcycles</b>, with or without sidecar", "<b>Motocicletas</b>, con o sin sidecar"), T("At least one on the <b>left</b> if their top speed is <b>100 km/h or less</b>; <b>left and right</b> if it is <b>over 100 km/h</b>.", "Al menos <b>uno en la izquierda</b> si su velocidad máxima <b>no supera los 100 km/h</b>; <b>izquierda y derecha</b> si <b>la superan</b>.")],
            [T("<b>Two-wheeled mopeds</b>", "<b>Ciclomotores de dos ruedas</b>"), T("At least one on the <b>left</b>.", "Al menos <b>uno en la izquierda</b>.")],
            [T("Other mopeds, three-wheelers and quadricycles", "Resto de ciclomotores, vehículos de tres ruedas y cuadriciclos"),
             T("With a body that fully or partly covers the driver: the <b>same as a car</b>. Without one: <b>left and right</b> outside mirrors.", "Con carrocería que cubra total o parcialmente al conductor: los <b>mismos que un turismo</b>. Sin carrocería: espejo <b>izquierdo y derecho</b>.")],
        ],
        widths=["32%", "68%"],
    ))
    B.append(P(
        "<b>Adjust the mirrors before setting off</b> (or check them), with the vehicle <b>still</b>, preferably on <b>flat, level ground</b>. With a slight movement of the eyes you should see:",
        "Los espejos <b>se regulan antes de iniciar la marcha</b> (o se comprueba su reglaje), con el vehículo <b>inmovilizado</b>, preferiblemente en <b>terreno recto y llano</b>. Con un leve movimiento de ojos se debe ver:"))
    B.append(FIG(mirrors, "Interior mirror: at least three of the four sides of the rear window. Door mirrors: as little of your car and as much road as possible, horizon in the middle.",
                 "Retrovisor interior: al menos tres de los cuatro lados de la luneta. Exteriores: lo mínimo del vehículo y lo máximo de la calzada, con el horizonte en medio."))
    B.append(TABLE(
        [T("Mirror type", "Tipo de espejo"), T("What it does", "Qué hace")],
        [
            [T("<b>Convex</b>", "<b>Convexo</b>"), T("A <b>wider view</b>, but it makes things look <b>smaller and further away</b> (a false sense of distance). <b>Door mirrors</b> are convex.", "Mayor ángulo visual, pero <b>empequeñece la imagen y la aleja</b> (falsa sensación de lejanía). Los <b>exteriores</b> son convexos.")],
            [T("<b>Flat</b>", "<b>Plano</b>"), T("A <b>true-size</b> image — usual for the <b>interior</b> mirror.", "Ofrece una <b>imagen real</b>; habitual en el espejo <b>interior</b>.")],
            [T("<b>Panoramic interior</b>", "<b>Interior panorámico</b>"), T("A <b>wider view</b>, but it <b>does not replace the door mirrors</b>.", "Mayor ángulo de visión, pero <b>no sustituye a los retrovisores exteriores</b>.")],
        ],
        widths=["26%", "74%"],
    ))

    # ---------------------------------------------------------------- 2. efficient driving
    B.append(H2("2", "Efficient driving techniques", "Técnicas de conducción eficiente"))
    B.append(P("Efficient driving can <b>considerably reduce</b> a vehicle’s polluting emissions.", "Con las técnicas de conducción eficiente se pueden <b>reducir considerablemente las emisiones contaminantes</b> de los vehículos."))
    B.append(BOX("key", "Advantages of efficient driving", "Ventajas de la conducción eficiente", [
        ("<b>Fuel use falls 10–25 %</b>. Your course adds that <b>CO<sub>2</sub> emissions fall 50–80 %</b> — give that figure in the exam. In fact CO<sub>2</sub> falls in the same proportion as the fuel you save: the IDAE (Spain’s energy agency) gives about 15 % for both.",
         "<b>Reduce el consumo de combustible entre el 10 % y el 25 %</b>. Tu curso añade que <b>reduce las emisiones de CO<sub>2</sub> entre el 50 % y el 80 %</b>: da esa cifra en el examen. En realidad, el CO<sub>2</sub> baja en la misma proporción que el combustible ahorrado: el IDAE da alrededor del 15 % para ambos."),
        ("Some systems <b>last longer</b> (brakes, gearbox…); <b>less noise</b>; <b>more comfort</b> for driver and passengers (calmer driving, less stress).", "<b>Aumenta la vida útil</b> de algunos sistemas (frenos, caja de cambios…); <b>menos ruido</b>; <b>más confort</b> para conductor y ocupantes (conducción más tranquila, menos estrés)."),
    ]))
    B.append(H3("2.1 Starting the engine and moving off", "2.1 Arrancar e inicio de la marcha"))
    B.append(TABLE(
        [T("Rule", "Norma")],
        rows([
            ("<b>Start the engine without pressing the accelerator</b>: modern cars don’t need it.", "<b>Arrancar el motor sin acelerar</b>: en los vehículos actuales no hace falta pisar el acelerador."),
            ("<b>Petrol</b>: move off <b>straight after starting</b>. <b>Diesel</b>: wait <b>a few seconds</b> with the engine running so it is properly lubricated.", "<b>Gasolina</b>: iniciar la marcha <b>inmediatamente después de arrancar</b>. <b>Diésel</b>: esperar <b>unos segundos</b> con el motor arrancado para que la lubricación sea adecuada."),
            ("Use <b>first gear only to move off</b>; change to <b>second after about 2 seconds or 6 metres</b>.", "Usar la <b>1.ª solo para iniciar la marcha</b> y cambiar a <b>2.ª a los 2 segundos o 6 metros</b>."),
            ("<b>Don’t rev hard with a cold engine</b>: its parts are not yet well lubricated.", "<b>Evitar acelerones con el motor en frío</b>: sus elementos aún no están bien lubricados."),
        ]),
    ))
    B.append(H3("2.2 Using the gears to accelerate", "2.2 Uso de las marchas para acelerar"))
    B.append(P("Fewer revs mean less fuel and less pollution, so drive in the <b>highest gear possible</b> for each situation:", "A menos revoluciones, menos consumo y menos contaminación. Hay que circular con la <b>marcha más alta posible</b> en cada situación:"))
    B.append(TABLE(
        [T("Rule", "Norma")],
        rows([
            ("<b>Don’t over-rev the engine</b>: change up between <b>1,500 and 2,000 rpm</b> (diesel) or <b>2,000 and 2,500 rpm</b> (petrol). Accelerate <b>smoothly and progressively</b>.",
             "<b>No forzar el motor</b>: cambiar evitando altas revoluciones, entre <b>1.500 y 2.000 rpm</b> (diésel) y entre <b>2.000 y 2.500 rpm</b> (gasolina). Acelerar de forma <b>suave y progresiva</b>."),
            ("<b>Avoid unnecessary gear changes</b>: you can <b>skip gears</b> — third at 30 km/h, fourth at 40, fifth at 50…", "<b>Evitar cambios innecesarios</b>: se puede subir <b>saltando marchas</b>: 3.ª a 30 km/h, 4.ª a 40, 5.ª a 50…"),
        ]),
    ))
    B.append(FIG(rev_bands, "Change up early — diesel at 1,500–2,000 rpm, petrol at 2,000–2,500 rpm — and skip gears when you can.",
                 "Cambia pronto —el diésel a 1.500–2.000 rpm y la gasolina a 2.000–2.500 rpm— y salta marchas cuando puedas."))
    B.append(H3("2.3 Using the gears to slow down", "2.3 Uso de las marchas para reducir"))
    B.append(TABLE(
        [T("Rule", "Norma")],
        rows([
            ("Use the <b>engine brake without changing down</b>, especially downhill: in gear and <b>off the accelerator, fuel use is zero</b>.", "<b>Utilizar el freno motor sin reducir de marcha</b>, sobre todo en bajada: con una marcha engranada y <b>sin acelerar, el consumo es nulo</b>."),
            ("<b>Change down as late as possible</b>, skipping intermediate gears.", "<b>Reducir de marcha lo más tarde posible</b>, pudiendo saltar marchas intermedias."),
            ("<b>Brake smoothly and progressively</b>.", "<b>Frenar de forma suave y progresiva</b>."),
        ]),
    ))
    B.append(H3("2.4 Other ways to save", "2.4 Otras medidas para ahorrar"))
    B.append(TABLE(
        [T("Measure", "Medida")],
        rows([
            ("A <b>moderate speed</b> suited to the circumstances (more speed, more fuel) and a <b>steady speed</b>, without unnecessary acceleration or braking.", "<b>Velocidad moderada</b> y adecuada (a mayor velocidad, mayor consumo) y <b>uniforme</b>, sin acelerones ni frenazos innecesarios."),
            ("For long stops — <b>more than 60 seconds</b> — <b>switch the engine off</b>.", "En <b>detenciones prolongadas</b> (más de <b>60 segundos</b>), <b>apagar el motor</b>."),
            ("<b>Maintain the vehicle</b> as the manufacturer says (air filter, idling…) and keep the <b>right tyre pressure</b> — under-inflated tyres use more fuel and wear out sooner.", "Hacer el <b>mantenimiento</b> marcado por el fabricante (filtro de aire, ralentí…) y llevar la <b>presión adecuada</b> en los neumáticos (con menos presión, más consumo y menos vida útil)."),
            ("<b>Don’t overload</b> the vehicle; load it properly — better in the <b>boot</b> than on a <b>roof rack</b>. <b>Don’t spoil the aerodynamics</b> (a roof rack you don’t need, needless body changes; on a motorcycle, <b>don’t alter the fairing</b>).",
             "<b>No cargar en exceso</b> y colocar bien la carga, mejor en el <b>maletero</b> que en la <b>baca</b>. <b>No modificar la aerodinámica</b> (baca innecesaria, cambios en la carrocería; en las motos, <b>no alterar el carenado</b>)."),
            ("Use air conditioning <b>moderately</b>, at about <b>23 °C</b>. Avoid town and heavy traffic where you can (constant stopping). Use <b>ECO mode</b>, which limits acceleration and climate control to save fuel; the driver can switch it on and off.",
             "<b>Uso moderado del aire acondicionado</b>, a unos <b>23 °C</b>. Evitar en lo posible las vías urbanas o de mucho tráfico (detenciones continuas). Usar el <b>modo ECO</b>, que limita la aceleración y la climatización para ahorrar; se conecta y desconecta manualmente."),
        ]),
    ))
    B.append(H3("2.5 What not to do", "2.5 Lo que no debemos hacer"))
    B.append(BOX("trap", "Don’t…", "No se debe…", [
        ("…coast in <b>neutral</b> when slowing or going down mountain passes — and even less with the <b>engine off</b>. …drive <b>too close</b> to the vehicle in front.", "…circular en <b>punto muerto</b> en las deceleraciones o al bajar puertos, y mucho menos con el <b>motor apagado</b>. …circular <b>muy cerca</b> del vehículo de delante."),
        ("…use petrol with a <b>lower octane</b> than the manufacturer recommends. …drive fast with the <b>windows down</b> (use the vents, or moderate air conditioning at 23 °C).", "…usar <b>gasolina de menor octanaje</b> que el recomendado. …circular a velocidades altas con las <b>ventanillas bajadas</b> (mejor las rejillas de ventilación o el aire acondicionado moderado a 23 °C)."),
        ("…climb hills in <b>low gears with high revs</b>. …save on <b>lights</b> by switching them on later at dusk or off earlier at dawn. …switch the engine off for <b>stops of a few seconds</b>.",
         "…subir pendientes con <b>marchas cortas y el motor revolucionado</b>. …<b>ahorrar en alumbrado</b> retrasando su encendido al anochecer o adelantando su apagado al amanecer. …<b>apagar el motor en detenciones momentáneas</b> (pocos segundos)."),
        ("…carry <b>more weight</b> than needed. A <b>roof rack</b> only when there is no other option — it raises consumption <b>even when empty</b>.", "…llevar <b>más peso</b> del necesario. La <b>baca</b>, solo cuando no haya otra opción: aumenta el consumo <b>incluso sin carga</b>."),
    ]))
    B.append(H3("2.6 The problem of pollution", "2.6 El problema de la contaminación"))
    B.append(P("Air and noise pollution must be avoided — they can be reported and fined — for public health and the environment. The main gases from engines:",
               "La contaminación (atmosférica y acústica) se debe evitar, además de por ser denunciable y sancionable, por salud pública y medio ambiente. Los gases más contaminantes del motor:"))
    B.append(TABLE(
        [T("Gas", "Gas"), T("Effect", "Efecto")],
        [
            [T("<b>CO</b> — carbon monoxide", "<b>CO</b>: monóxido de carbono"), T("<b>Very toxic</b> and poisonous — it can kill. Your course calls it “black smoke”, but CO is <b>colourless and odourless</b>; black smoke is <b>soot</b> (particles), mainly from diesel engines.",
                                                                                "<b>Muy tóxico</b> y venenoso: puede ser mortal. Tu curso lo llama «humo negro», pero el CO es <b>incoloro e inodoro</b>; el humo negro es <b>hollín</b> (partículas), sobre todo de los diésel.")],
            [T("<b>CO<sub>2</sub></b> — carbon dioxide", "<b>CO<sub>2</sub></b>: dióxido de carbono"), T("The <b>main cause of the greenhouse effect</b>.", "El <b>mayor responsable del efecto invernadero</b>.")],
            [T("<b>NOx</b> — nitrogen oxides", "<b>NOx</b>: óxidos de nitrógeno"), T("Cause <b>breathing problems</b>.", "Causan <b>problemas respiratorios</b>.")],
            [T("<b>HC</b> — unburnt hydrocarbons", "<b>HC</b>: hidrocarburos sin quemar"), T("<b>Toxic</b> for people.", "<b>Tóxicos</b> para el ser humano.")],
            [T("<b>SO<sub>2</sub></b> — sulphur dioxide", "<b>SO<sub>2</sub></b>: dióxido de azufre"), T("Responsible for <b>acid rain</b>.", "Responsable de la <b>lluvia ácida</b>.")],
        ],
        widths=["32%", "68%"],
    ))
    B.append(BOX("trap", "Not allowed", "No se permite", [
        ("<b>Throwing objects or rubbish</b> onto the road (cigarette ends, food…).", "<b>Arrojar objetos o desperdicios</b> a la vía (colillas, restos de comida…)."),
        ("<b>Noise or gases above the limits</b> — agents can fine you and <b>immobilise the vehicle</b>: <b>needless noise</b> (no silencer, resonator exhausts, exhausts in bad condition, excessive horn, loud music, revving) "
         "and driving without a device that stops <b>unburnt fuel</b> or <b>smoke that hampers visibility</b> or very harmful gases.",
         "<b>Emitir ruidos o gases por encima de los límites</b> (los agentes pueden sancionar e <b>inmovilizar el vehículo</b>): <b>ruidos innecesarios</b> (escape libre sin silenciador, tubos resonadores o en mal estado, claxon exagerado, música elevada, acelerones) "
         "y circular sin un dispositivo que evite la proyección de <b>combustible no quemado</b> o <b>humo que dificulte la visibilidad</b> o gases muy nocivos."),
        ("<b>Changing the oil on the public road</b> — it is very polluting. Used oil goes to an <b>oil-recovery container</b>.", "<b>Cambiar el aceite en la vía pública</b>: es muy contaminante. Se debe entregar en un <b>contenedor de recuperación de aceite</b>."),
    ]))

    B.append(H3("2.7 Access rules in urban areas", "2.7 Regulación de acceso en áreas urbanas"))
    B.append(P(
        "Traffic law has adapted to EU <b>air-quality</b> rules. The authority may change the direction of traffic, ban access to parts of the road totally or partly (for everyone or for some vehicles), close roads, "
        "impose set routes, or use pavements or lanes in the opposite direction. Under the climate-change law (Ley 7/2021), <b>municipalities of more than 50,000 people</b>, <b>island territories</b>, and "
        "<b>municipalities of more than 20,000</b> that <b>exceed the pollution limits</b> must adopt <b>sustainable urban mobility plans</b> (<i>PMUS</i>), including <b>low-emission zones</b>.",
        "La legislación de tráfico se ha adaptado a la normativa de la UE sobre <b>calidad del aire</b>. La autoridad puede ordenar otro sentido de circulación, prohibir total o parcialmente el acceso a partes de la vía (con carácter general o para determinados vehículos), cerrar vías, "
        "imponer itinerarios o usar aceras o carriles en sentido contrario. Según la ley de cambio climático (Ley 7/2021), los <b>municipios de más de 50.000 habitantes</b>, los <b>territorios insulares</b> y los "
        "<b>municipios de más de 20.000</b> que <b>superen los valores límite de contaminantes</b> deben implantar <b>planes de movilidad urbana sostenible</b> (PMUS), con <b>zonas de bajas emisiones</b>."))
    B.append(TABLE(
        [T("Term", "Concepto"), T("What it is", "Qué es")],
        [
            [T("<b>Low-emission zone</b> (<i>ZBE</i>)", "<b>Zona de bajas emisiones</b> (ZBE)"),
             T("An area set by a public authority, <b>continuous</b>, where <b>access, driving and parking are restricted</b> to improve air quality and cut greenhouse gases, according to each vehicle’s <b>emissions classification</b>. "
               "Its entrance needs a <b>sign</b> that is easy to identify, with the restrictions that apply.",
               "Ámbito delimitado por una Administración pública, <b>de carácter continuo</b>, en el que se aplican <b>restricciones de acceso, circulación y estacionamiento</b> para mejorar la calidad del aire y mitigar los gases de efecto invernadero, según la <b>clasificación de los vehículos por su nivel de emisiones</b>. "
               "Su entrada necesita una <b>señal</b> fácil de identificar, con las restricciones que afectan.")],
            [T("<b>National Access Point</b>", "<b>Punto de Acceso Nacional</b>"),
             T("Local authorities send it the areas and roads in their ZBE and other access rules (UVAR): criteria, hours, temporary pollution-protocol restrictions and the types of permit.",
               "Las entidades locales le facilitan las áreas y vías de las ZBE y otras medidas UVAR: criterios de acceso, horarios, restricciones temporales por protocolos de contaminación y tipos de autorizaciones.")],
            [T("<b>Residential priority zone</b>", "<b>Zona de prioridad residencial</b>"), T("An area regulated by the town council that restricts access or traffic for <b>non-residents</b>, to keep its use sustainable.", "Área regulada por la Autoridad municipal con restricciones de acceso o circulación a <b>vehículos de no residentes</b> para mantener su uso sostenible.")],
            [T("<b>Safe school route</b>", "<b>Camino o ruta escolar seguro</b>"), T("Roads adapted so that children can get to school <b>on foot, by public transport or by non-motorised means</b>; it can have signs, markings, speed limits and restrictions on motor vehicles.",
                                                                                   "Conjunto de vías acondicionadas para que los niños vayan al colegio <b>caminando, en transporte público o en medios no motorizados</b>; puede tener señales, marcas, límites de velocidad y restricciones a los vehículos a motor.")],
            [T("<b>Vulnerable users</b>", "<b>Usuarios vulnerables</b>"), T("Near <b>schools, hospitals, homes for older or disabled people</b>, there are specific measures: speed limits, parking rules and <b>traffic calming</b>.", "En las proximidades de <b>centros escolares, hospitalarios, de personas mayores o con discapacidad</b> se aplican medidas de <b>limitación de velocidad</b>, estacionamiento y <b>calmado del tráfico</b>.")],
        ],
        widths=["28%", "72%"],
    ))
    B.append(TABLE(
        [T("Sign", "Señal"), T("Meaning", "Significado")],
        [[T(ICON["R-120"], ICON["R-120"]),
          T("<b>R-120</b> “Entry prohibited to vehicles according to their environmental label or other environmental criteria”. The conditions (for example, which labels may enter) are on an <b>additional panel</b> or on a board that includes the sign.",
            "<b>R-120</b> «Entrada prohibida a vehículos en función de su distintivo ambiental u otros criterios ambientales». Las condiciones (por ejemplo, qué distintivos pueden entrar) se indican en un <b>panel complementario</b> o en un cartel que incluye la señal.")]],
        widths=["18%", "82%"],
    ))
    B.append(P(
        "The authorities can restrict, totally or partly, entry and driving in <b>low-emission zones</b>, <b>residential priority zones</b> or any other road under their control, using environmental criteria. "
        "There are <b>four environmental labels</b> (<i>distintivos ambientales</i>); from most to least efficient:",
        "Las autoridades pueden restringir, total o parcialmente, la entrada y circulación en las <b>zonas de bajas emisiones</b>, en las <b>zonas de prioridad residencial</b> o en cualquier otra vía de su competencia, según criterios medioambientales. "
        "Existen <b>cuatro distintivos ambientales</b>; de mayor a menor eficiencia:"))
    B.append(FIG(eco_labels, "Label 0 (blue), ECO (blue and green), C (green) and B (yellow). The remaining 50 % most polluting vehicles get no label.",
                 "Distintivo 0 (azul), ECO (azul y verde), C (verde) y B (amarillo). El 50 % restante, el más contaminante, no tiene distintivo."))
    B.append(BOX("key", "Placing the label", "Colocación del distintivo", [
        ("Getting and displaying the label is <b>voluntary</b> (DGT), but some town ordinances ask for it in their low-emission zones. If you display it, stick it in the <b>bottom right corner of the windscreen</b>; "
         "without a windscreen (motorcycles), anywhere visible.",
         "Obtener y colocar el distintivo es <b>voluntario</b> (DGT), aunque algunas ordenanzas municipales lo exigen en sus zonas de bajas emisiones. Si se coloca, va adherido en el <b>ángulo inferior derecho del parabrisas delantero</b>; "
         "si no hay parabrisas (motocicletas), en cualquier sitio visible."),
        ("The labels and their criteria have <b>not changed in 2026</b>: a plan to require 90 km of electric range for plug-in hybrids to keep the 0 label was dropped.",
         "Los distintivos y sus criterios <b>no han cambiado en 2026</b>: la propuesta de exigir 90 km de autonomía a los híbridos enchufables para mantener la etiqueta 0 se retiró."),
    ]))

    # ---------------------------------------------------------------- 3. traps
    B.append(H2("3", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("Mirrors: <b>5–10 s</b> in town and heavy traffic; <b>10–15 s</b> on motorways and empty roads. Even when not manoeuvring.", "Retrovisores: <b>5–10 s</b> en ciudad y tráfico denso; <b>10–15 s</b> en autovía y vías sin tráfico. Aunque no se haga ninguna maniobra."),
        ("Well-adjusted mirrors still leave a <b>blind spot</b>: turn your head <b>45°</b>.", "Con los espejos bien reglados sigue habiendo <b>ángulo muerto</b>: girar la cabeza <b>45°</b>."),
        ("Gap: <b>2 s</b> town, <b>3 s</b> road, <b>+1 s</b> if worse — including when the car <b>behind</b> is too close.", "Distancia: <b>2 s</b> ciudad, <b>3 s</b> carretera, <b>+1 s</b> si empeoran las condiciones, también si el de <b>detrás</b> va muy pegado."),
        ("Stopped: <b>2–3 m</b> (see its rear tyres). Last in an unexpected queue: <b>5–6 m</b> and hazard lights. Stopped and about to be hit: <b>keep braking</b>.", "Detenido: <b>2–3 m</b> (ver sus ruedas traseras). Último de una cola imprevista: <b>5–6 m</b> y emergencia. Detenido y sin poder evitar el alcance: <b>mantener frenado</b>."),
        ("Cyclists and vehicles have the <b>largest side</b> zone of uncertainty; adult pedestrians the smallest, except <b>children</b>.", "Ciclistas y vehículos tienen la <b>mayor zona lateral</b> de incertidumbre; los peatones adultos, la menor, salvo los <b>niños</b>."),
        ("Interior mirror: <b>3 of the 4 sides</b> of the rear window. Door mirrors: <b>50 % road, 50 % sky</b>. Convex mirrors make things look <b>further away</b>.", "Interior: <b>3 de los 4 lados</b> de la luneta. Exteriores: <b>50 % asfalto, 50 % cielo</b>. Los convexos <b>alejan</b> la imagen."),
        ("Car: <b>left outside + interior</b> mirror compulsory; right only if the interior one can’t see behind. Motorcycle over <b>100 km/h</b>: both sides.", "Turismo: obligatorio el <b>exterior izquierdo + interior</b>; el derecho, solo si el interior no permite ver. Moto de más de <b>100 km/h</b>: los dos."),
        ("Wipers need a <b>washer</b>; a <b>rear washer</b> is not compulsory. Never wipe a dry screen with an empty tank. <b>Slowest</b> wiper speed.", "Con limpiaparabrisas, <b>lavaparabrisas</b> obligatorio; el <b>lavalunetas</b> no. Nunca limpiar en seco con el depósito vacío. Velocidad <b>más lenta</b>."),
        ("Start <b>without accelerating</b>; petrol moves off <b>at once</b>, diesel <b>waits a few seconds</b>. Second gear after <b>2 s or 6 m</b>.", "Arrancar <b>sin acelerar</b>; gasolina sale <b>enseguida</b>, diésel <b>espera unos segundos</b>. 2.ª a los <b>2 s o 6 m</b>."),
        ("In gear, foot off: fuel use is <b>zero</b>. <b>Neutral</b> downhill: <b>wrong</b>. Engine off only for stops <b>over 60 s</b>.", "Con marcha y sin acelerar, el consumo es <b>nulo</b>. Bajar en <b>punto muerto</b>: <b>mal</b>. Apagar el motor solo en paradas de <b>más de 60 s</b>."),
        ("A roof rack raises consumption <b>even empty</b>. Windows down at speed: <b>worse</b> than moderate air conditioning at <b>23 °C</b>.", "La baca aumenta el consumo <b>incluso vacía</b>. Ventanillas bajadas a velocidad: <b>peor</b> que el aire acondicionado moderado a <b>23 °C</b>."),
        ("CO₂: greenhouse effect. SO₂: acid rain. NOx: breathing. CO: very toxic. Oil change on the street: <b>prohibited</b>.", "CO₂: efecto invernadero. SO₂: lluvia ácida. NOx: respiratorio. CO: muy tóxico. Cambiar el aceite en la calle: <b>prohibido</b>."),
        ("Label 0: PHEV with at least <b>40 km</b>. ECO must also meet the <b>C</b> criteria. C diesel from <b>September 2015</b>, petrol from <b>2006</b>. Display: <b>voluntary</b>, bottom right.", "Etiqueta 0: PHEV con al menos <b>40 km</b>. La ECO debe cumplir además la <b>C</b>. C diésel desde <b>septiembre de 2015</b>, gasolina desde <b>2006</b>. Colocación: <b>voluntaria</b>, abajo a la derecha."),
    ]))

    # ---------------------------------------------------------------- 4. numbers
    B.append(H2("4", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Mirror checks: town / motorway", "Retrovisores: ciudad / autovía"), T("every 5–10 s / 10–15 s", "cada 5–10 s / 10–15 s")],
            [T("Head turn for the blind spot", "Giro de cabeza para el ángulo muerto"), T("about 45°", "unos 45°")],
            [T("Time gap: town / road / worse conditions", "Distancia en tiempo: ciudad / carretera / peores condiciones"), T("2 s / 3 s / +1 s", "2 s / 3 s / +1 s")],
            [T("Stopped behind a vehicle / last in an unexpected queue", "Detenido tras un vehículo / último de una cola imprevista"), T("2–3 m / 5–6 m", "2–3 m / 5–6 m")],
            [T("Interior mirror must show behind the car", "El espejo interior debe mostrar por detrás"), T("up to 60 m, 20 m wide", "hasta 60 m, en 20 m de anchura")],
            [T("Motorcycle needs left and right mirrors above", "La moto lleva espejo izquierdo y derecho a partir de"), T("100 km/h top speed", "100 km/h de velocidad máxima")],
            [T("Fuel saved by efficient driving / CO₂ (course)", "Ahorro de combustible / CO₂ (curso)"), T("10–25 % / 50–80 %", "10–25 % / 50–80 %")],
            [T("Change to second gear after", "Cambiar a 2.ª a los"), T("2 seconds or 6 metres", "2 segundos o 6 metros")],
            [T("Change up: diesel / petrol", "Cambiar de marcha: diésel / gasolina"), T("1,500–2,000 / 2,000–2,500 rpm", "1.500–2.000 / 2.000–2.500 rpm")],
            [T("Skipping gears", "Saltar marchas"), T("3rd at 30, 4th at 40, 5th at 50 km/h", "3.ª a 30, 4.ª a 40, 5.ª a 50 km/h")],
            [T("Switch the engine off for stops over", "Apagar el motor en paradas de más de"), T("60 seconds", "60 segundos")],
            [T("Air conditioning", "Aire acondicionado"), T("about 23 °C", "unos 23 °C")],
            [T("Low-emission plans compulsory for municipalities over", "Planes con ZBE obligatorios en municipios de más de"), T("50,000 people (20,000 if over the pollution limits); islands", "50.000 habitantes (20.000 si superan los límites); territorios insulares")],
            [T("Label 0 for plug-in hybrids", "Etiqueta 0 para híbridos enchufables"), T("at least 40 km electric range", "al menos 40 km de autonomía")],
            [T("Label C: petrol / diesel cars from", "Etiqueta C: turismos gasolina / diésel desde"), T("January 2006 / September 2015", "enero de 2006 / septiembre de 2015")],
            [T("Label B: petrol / diesel cars from", "Etiqueta B: turismos gasolina / diésel desde"), T("January 2001 / 2006", "enero de 2001 / 2006")],
            [T("Vehicles with no label", "Vehículos sin distintivo"), T("the 50 % most polluting", "el 50 % más contaminante")],
        ],
        widths=["56%", "44%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["vi2", "vi5", "an3", "sp2", "sp7", "mi3", "mi6", "ef3", "ge2", "sv3", "po2", "lb3"]


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
    ("Reglamento General de Circulación (RD 1428/2003): safety distance, lights, pollution and noise — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Reglamento General de Vehículos (RD 2822/1998): mirrors and glazing — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-1999-1826"),
    ("Ley 7/2021, de cambio climático y transición energética, art. 14: sustainable mobility plans and low-emission zones", "https://www.boe.es/buscar/act.php?id=BOE-A-2021-8447"),
    ("DGT: environmental labels — criteria, and placement is voluntary", "https://www.dgt.es/nuestros-servicios/tu-vehiculo/tus-vehiculos/distintivo-ambiental/"),
    ("RACE, 25-02-2026: no changes to the DGT labels in 2026", "https://www.race.es/nuevas-etiquetas-dgt"),
    ("IDAE: efficient-driving manual (about 15 % less fuel and CO2)", "https://idae.es/uploads/documentos/documentos_Manual_de_conduccion_eficiente_488980a3.pdf"),
]

GLOSSARY = [
    ("conducción preventiva / defensiva", "preventive / defensive driving"),
    ("anticipación", "anticipation"),
    ("ángulo muerto", "blind spot"),
    ("retrovisor interior / exterior", "interior / door mirror"),
    ("espejo plano / convexo / panorámico", "flat / convex / panoramic mirror"),
    ("reglaje de los espejos", "mirror adjustment"),
    ("distancia de seguridad", "safe following distance"),
    ("zona de incertidumbre", "zone of uncertainty"),
    ("retención imprevista", "unexpected hold-up (queue)"),
    ("maniobra de evasión", "escape manoeuvre"),
    ("limpiaparabrisas · escobilla · lavaparabrisas · lavalunetas", "wipers · wiper blade · windscreen washer · rear washer"),
    ("luneta térmica · antivaho", "heated rear window · demister"),
    ("vidrio tintado homologado", "approved tinted glass"),
    ("conducción eficiente", "efficient (eco-) driving"),
    ("revoluciones por minuto (rpm)", "engine revs (rpm)"),
    ("freno motor · punto muerto", "engine braking · neutral"),
    ("octanaje", "octane rating"),
    ("baca · carenado", "roof rack · fairing"),
    ("monóxido / dióxido de carbono", "carbon monoxide / dioxide"),
    ("óxidos de nitrógeno · dióxido de azufre", "nitrogen oxides · sulphur dioxide"),
    ("lluvia ácida · efecto invernadero", "acid rain · greenhouse effect"),
    ("escape libre", "exhaust without a silencer"),
    ("plan de movilidad urbana sostenible (PMUS)", "sustainable urban mobility plan"),
    ("zona de bajas emisiones (ZBE)", "low-emission zone (LEZ)"),
    ("zona de prioridad residencial", "residential priority zone"),
    ("camino escolar seguro", "safe route to school"),
    ("distintivo ambiental (etiqueta)", "environmental label (sticker)"),
    ("híbrido enchufable / no enchufable", "plug-in / non-plug-in hybrid"),
]
