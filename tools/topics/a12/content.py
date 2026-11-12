# -*- coding: utf-8 -*-
"""Category A1/A2, Topic 12 content (riding techniques), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the A1/A2 course's Tema 12 (Técnicas de conducción): choosing the motorcycle (its
features, types, controls and mirrors) and riding it (handling with the engine off, moving off, posture and the
passenger, bends, braking, town, groups, the sidecar, luggage, and fuel use). It is all about motorcycles, so the page
is written for this topic; only the controls figure is shared with Category B, Topic 10.

The rules come from the Reglamento General de Circulación (arts. 12, 36 and 118) and the Reglamento General de Vehículos
(Anexo III, mirrors), as they stand in November 2026. Riding technique (the 60–70 % braking split, the 30 km/h
gyroscopic effect, group formations) is your course's teaching and is presented as such.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import moto_controls, mirrors_moto, curve_moto, braking_moto, group_ride, luggage_moto


def rows(pairs):
    return [[T(a, b)] for a, b in pairs]


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("How a motorcycle differs from a car, its <b>controls</b> and <b>mirrors</b>, and the techniques for riding it safely: <b>moving off</b>, <b>posture</b>, the <b>passenger</b>, <b>bends</b>, <b>braking</b>, "
         "<b>town</b>, <b>groups</b>, the <b>sidecar</b> and <b>luggage</b>.",
         "En qué se diferencia la moto de un turismo, sus <b>mandos</b> y <b>espejos</b>, y las técnicas para conducirla con seguridad: <b>puesta en marcha</b>, <b>postura</b>, el <b>acompañante</b>, las <b>curvas</b>, la <b>frenada</b>, "
         "la <b>ciudad</b>, el <b>grupo</b>, el <b>sidecar</b> y la <b>carga</b>."),
        ("The exam asks above all: which hand and foot work each control, how many <b>mirrors</b> (the <b>100 km/h</b> line), where the <b>passenger</b> sits, what changes with a passenger, "
         "<b>brake before the bend</b>, the <b>60–70 % / 30–40 %</b> braking split, <b>30 km/h</b> and the gyroscopic effect, groups of <b>3–4</b>, and where heavy and light luggage go.",
         "El examen pregunta sobre todo: qué mano y qué pie manejan cada mando, cuántos <b>espejos</b> (la frontera de <b>100 km/h</b>), dónde va el <b>acompañante</b>, qué cambia con pasajero, "
         "<b>frenar antes de la curva</b>, el reparto <b>60–70 % / 30–40 %</b>, los <b>30 km/h</b> y el efecto giroscópico, grupos de <b>3–4</b> y dónde va la carga pesada y la ligera."),
        ("The sections follow your A1/A2 course’s Topic 12. Spanish exam terms are in <i>italics</i>, and a glossary closes the topic.",
         "Los apartados siguen el Tema 12 de tu curso A1/A2. Al final hay un glosario español–inglés."),
    ]))

    # ---------------------------------------------------------------- 1. choosing the motorcycle
    B.append(H2("1", "Choosing the motorcycle", "Elección de la motocicleta"))
    B.append(P(
        "Riding a motorcycle is very different from driving other vehicles: it moves differently in traffic and manoeuvres differently. It needs <b>special preparation</b>, because motorcycles are:",
        "Conducir una moto es muy diferente de conducir otros automóviles: se mueve de otra forma en el tráfico y maniobra de otra forma. Hay que tener una <b>preparación especial</b>, porque las motos son:"))
    B.append(TABLE(
        [T("Motorcycles are…", "Las motos son…"), T("Why it matters", "Por qué importa")],
        [
            [T("<b>Less stable</b>", "<b>Menos estables</b>"), T("They stand on <b>two wheels</b>: the rider must keep the balance, even in bad conditions.", "Se apoyan solo en <b>dos ruedas</b>: el conductor debe mantener el equilibrio, incluso en condiciones desfavorables.")],
            [T("<b>More fragile</b>", "<b>Más frágiles</b>"), T("In a collision or a fall the occupants take the <b>impact directly</b>: there is no bodywork to absorb it.", "En una colisión o caída los ocupantes reciben el <b>impacto directamente</b>: no hay carrocería que lo absorba.")],
            [T("<b>Less visible</b>", "<b>Menos visibles</b>"), T("Their small size, quick movements and speed make them <b>harder for others to see</b>.", "Su menor tamaño, la agilidad de sus movimientos y su velocidad las hacen <b>menos perceptibles</b> para los demás.")],
            [T("<b>Powerful for their mass</b>", "<b>Más potentes respecto a su masa</b>"),
             T("Strong acceleration can <b>surprise</b> others, and the rider or passenger. Under hard acceleration the centre of gravity shifts <b>backwards</b>, the <b>front wheel loses grip</b> and the motorcycle can <b>wobble</b> (<i>fluctuación</i>).",
               "Las grandes aceleraciones pueden <b>sorprender</b> a otros usuarios, al conductor o al acompañante. Al acelerar fuerte el centro de gravedad se desplaza <b>hacia atrás</b>, la <b>rueda delantera pierde adherencia</b> y se favorece la <b>fluctuación</b>.")],
        ],
        widths=["26%", "74%"],
    ))
    B.append(H3("1.1 Common types of motorcycle", "1.1 Tipos de motocicletas más comunes"))
    B.append(TABLE(
        [T("Type", "Tipo"), T("What it is for", "Para qué sirve")],
        [
            [T("<b>Scooter</b>", "<b>Scooter</b>"), T("Ideal in <b>town</b>: easy to handle, <b>automatic</b>, economical and clean (mechanics covered).", "Ideal en <b>zonas urbanas</b>: buena manejabilidad, <b>automática</b>, bajo consumo y limpia (partes mecánicas cubiertas).")],
            [T("<b>Self-protection structure</b>", "<b>Estructura de autoprotección</b>"), T("Short trips and town; a protective body against collisions and the weather.", "Desplazamientos cortos o urbanos; carrocería de protección ante colisiones o inclemencias.")],
            [T("<b>Naked</b> (neoclassic)", "<b>Neoclásica</b> (naked)"), T("Short distances, comfortable, easy to handle, cheap to maintain; you can add cases, fairings and other parts.", "Distancias cortas, conducción cómoda, buena manejabilidad, mantenimiento económico; admite maletas, carenados y otras piezas.")],
            [T("<b>Tourer</b> (gran turismo)", "<b>Rutera</b> (gran turismo)"), T("Usually large engines; for <b>long trips</b>, even with a passenger; big fairings against rain and wind. <b>Less manoeuvrable</b>: bigger and heavier.",
                                                                                   "Suelen ser de gran cilindrada; para <b>viajes largos</b>, incluso con acompañante; amplios carenados contra lluvia y viento. <b>Menos maniobrables</b> por su tamaño y peso.")],
            [T("<b>Trial</b>", "<b>Trial</b>"), T("Sport: getting over obstacles. Small, and needs a very special technique.", "Deporte de superar obstáculos. Pequeñas y con una técnica muy especial.")],
            [T("<b>Cross</b>", "<b>Cross</b>"), T("Tracks and unpaved ground, though it can be used on asphalt.", "Caminos y terrenos sin asfaltar, aunque se puede usar en vías asfaltadas.")],
            [T("<b>Sports</b>", "<b>Deportiva</b>"), T("Built for <b>high speed</b>: needs training and experience. Very aerodynamic fairings and a <b>riding position uncomfortable</b> on long trips.", "Pensada para <b>velocidades altas</b>: requiere formación y experiencia. Carenados muy aerodinámicos y una <b>postura incómoda</b> en viajes largos.")],
        ],
        widths=["28%", "72%"],
    ))
    B.append(BOX("key", "Important features of a motorcycle", "Aspectos importantes de una moto", [
        ("<b>Fairing</b> (<i>carenado</i>): a shell or screen that leaves the front wheel free. It improves <b>safety</b> (stability, protection from the weather and in falls) and <b>aerodynamics</b> (less fuel, more comfort, fatigue later).",
         "<b>Carenado</b>: estructura o cúpula que deja libre la rueda delantera. Mejora la <b>seguridad</b> (estabilidad, protección frente al tiempo y en caídas) y la <b>aerodinámica</b> (menos consumo, más comodidad, la fatiga tarda más)."),
        ("<b>Seat height</b>: not adjustable, except on a few motorcycles.", "<b>Altura del asiento</b>: no es regulable, salvo en casos excepcionales."),
        ("<b>Handlebar</b>: usually adjustable in height and reach. <b>Long and high</b>: more wind resistance (tiring on long trips). <b>Short and low</b>: less resistance, better at speed, but <b>less steering angle</b> to avoid obstacles.",
         "<b>Manillar</b>: suele ser ajustable en altura y distancia. <b>Largo y alto</b>: más resistencia aerodinámica (incómodo en viajes largos). <b>Corto y bajo</b>: menos resistencia, mejor a velocidad, pero <b>menor ángulo de giro</b> para esquivar obstáculos."),
    ]))
    B.append(BOX("key", "Good to know: self-protection structures and the helmet", "Conviene saberlo: autoprotección y casco", [
        ("A motorcycle with a <b>self-protection structure and seat belts</b>, when its ITV card says so, exempts rider and passenger from the <b>helmet, gloves and closed shoes</b>: they must wear the <b>seat belt</b> instead (art. 118 of the Reglamento General de Circulación).",
         "Una moto con <b>estructura de autoprotección y cinturones</b>, si así consta en su tarjeta ITV, exime a conductor y pasajero del <b>casco, los guantes y el calzado cerrado</b>: deben usar el <b>cinturón</b> (art. 118 del Reglamento General de Circulación)."),
    ]))

    B.append(H3("1.2 The main controls", "1.2 Principales mandos de la motocicleta"))
    B.append(FIG(moto_controls, "The usual layout: right hand — throttle and front brake; left hand — clutch; right foot — rear brake; left foot — gear lever.",
                 "La disposición habitual: mano derecha, acelerador y freno delantero; mano izquierda, embrague; pie derecho, freno trasero; pie izquierdo, selector de marchas."))
    B.append(TABLE(
        [T("Most common layout", "Disposición más generalizada"), T("Control", "Mando")],
        [
            [T("<b>Right hand</b>", "<b>Mano derecha</b>"), T("<b>Throttle</b> (use it gently) and <b>front brake</b> (gently and progressively).", "<b>Acelerador</b> (accionar suavemente) y <b>freno delantero</b> (suave y progresivamente).")],
            [T("<b>Left hand</b>", "<b>Mano izquierda</b>"), T("<b>Clutch</b>. The lights and horn switches are on this side too.", "<b>Embrague</b>. También se accionan las luces y el claxon.")],
            [T("<b>Right foot</b>", "<b>Pie derecho</b>"), T("<b>Rear brake</b>.", "<b>Freno trasero</b>.")],
            [T("<b>Left foot</b>", "<b>Pie izquierdo</b>"), T("<b>Gear lever</b> (selector).", "<b>Selector de marchas</b>.")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(P("Other devices: the <b>instrument panel</b> (speedometer, odometer, rev counter, warning lights…), indicators, ignition key, fuel tank, footrests, <b>side or centre stand</b>, mudguards, anti-theft devices…",
               "Otros dispositivos: el <b>tablero de instrumentos</b> (velocímetro, cuentakilómetros, cuentarrevoluciones, testigos luminosos…), intermitentes, llave de contacto, depósito, reposapiés, <b>caballete o pata de cabra</b>, guardabarros, antirrobo…"))

    B.append(H3("1.3 Mirrors", "1.3 Espejos retrovisores"))
    B.append(P("Mirrors let you see what is around and behind the motorcycle.", "Los espejos retrovisores permiten observar lo que rodea al vehículo por la parte trasera."))
    B.append(FIG(mirrors_moto, "Each mirror shows a strip behind; beside and slightly behind you there is a blind spot big enough to hide a car. Turn your head before moving sideways.",
                 "Cada espejo muestra una franja por detrás; a los lados y algo por detrás queda un ángulo muerto que puede ocultar un coche. Gira la cabeza antes de desplazarte."))
    B.append(TABLE(
        [T("Vehicle", "Vehículo"), T("Compulsory mirrors", "Espejos obligatorios")],
        [
            [T("<b>Motorcycle</b> (with or without sidecar) with a top speed <b>up to 100 km/h</b>; two-wheel moped", "<b>Motocicleta</b> (con o sin sidecar) de velocidad máxima <b>hasta 100 km/h</b>; ciclomotor de dos ruedas"),
             T("<b>One on the left</b>; the right one is optional.", "<b>Uno izquierdo</b>; el derecho es optativo.")],
            [T("<b>Motorcycle</b> with a top speed <b>over 100 km/h</b>", "<b>Motocicleta</b> de velocidad máxima <b>superior a 100 km/h</b>"), T("<b>Left and right</b>.", "<b>Izquierdo y derecho</b>.")],
            [T("<b>Three-wheelers and quadricycles</b> with a closed or semi-closed body", "<b>Vehículos de tres ruedas y cuadriciclos</b> con carrocería cerrada o semicerrada"),
             T("<b>One inside and one on the left</b>. If the interior one cannot give the required view: two outside (left and right).", "<b>Uno interior y otro izquierdo</b>. Si por el interior no se ve lo exigido: dos exteriores (izquierdo y derecho).")],
            [T("Three-wheelers and quadricycles <b>without</b> a body", "Vehículos de tres ruedas y cuadriciclos <b>sin</b> carrocería"), T("Left and right (your course leaves this case out).", "Izquierdo y derecho (tu curso no recoge este caso).")],
        ],
        widths=["56%", "44%"],
    ))
    B.append(BOX("key", "Adjusting the mirrors", "El reglaje correcto de los espejos", [
        ("Adjust them <b>before moving off</b> (or at least check them), with the motorcycle <b>still</b>, ideally on <b>straight, level</b> ground.",
         "Se regulan <b>antes de iniciar la marcha</b> (o al menos se comprueba su reglaje), con el vehículo <b>inmovilizado</b>, preferiblemente en terreno <b>recto y llano</b>."),
        ("A good adjustment makes the <b>blind spot</b> smaller — the area at the sides and behind that the mirrors don’t show. Cover it by <b>turning your head</b> before any manoeuvre.",
         "Un buen reglaje reduce el <b>ángulo muerto</b>, la zona lateral y trasera que no se ve por los espejos. Se completa la visión <b>girando la cabeza</b> antes de cualquier maniobra."),
    ]))

    # ---------------------------------------------------------------- 2. riding
    B.append(H2("2", "Riding a motorcycle", "Conducción de motocicletas"))
    B.append(P("Riding a two-wheeler is very different from driving other vehicles: you must work the <b>controls</b> and also keep the motorcycle <b>balanced</b>. Knowing how to handle it is the basis of safe riding.",
               "La técnica para conducir motos de dos ruedas es muy diferente: no solo hay que manejar los <b>mandos</b>, también mantener el <b>equilibrio</b>. Conocer el manejo de la moto es la base de una conducción segura."))
    B.append(H3("2.1 Handling it with the engine off", "2.1 Control con el motor parado"))
    B.append(P(
        "First get to know the motorcycle’s <b>mass</b> and <b>turning circle</b>: hold the handlebar <b>with both hands</b>, try the turning circle, push it forwards and backwards. <b>Don’t brake sharply</b> with the front brake (it unbalances the bike and you can fall). "
        "Lean it slightly to feel its weight and centre of gravity. Practise, on <b>flat, firm ground</b>, putting the <b>side stand</b> (<i>pata de cabra</i>) and the <b>centre stand</b> (<i>caballete</i>) down and up — first standing beside it, then sitting on it, without looking.",
        "Primero hay que conocer la <b>masa</b> y el <b>radio de giro</b>: sujetar el manillar <b>con ambas manos</b>, comprobar el radio de giro, moverla hacia delante y hacia atrás. <b>No frenar bruscamente</b> con el freno delantero (se desestabiliza y puede caerse). "
        "Inclinarla ligeramente para notar el peso y el centro de gravedad. Practicar en terreno <b>llano y compacto</b> la puesta y quita de la <b>pata de cabra</b> (soporte lateral) y del <b>caballete</b> (soporte central): primero a pie y después subido en la moto, sin mirar."))
    B.append(TABLE(
        [T("Stand", "Soporte"), T("Putting it down", "Ponerlo"), T("Taking it off", "Quitarlo")],
        [
            [T("<b>Side stand</b> (<i>pata de cabra</i>)", "<b>Soporte lateral</b> (pata de cabra)"),
             T("Unfold it with your foot, holding the handlebar and the rear, and lean the motorcycle on it until it is steady.", "Extenderlo con el pie sujetando la moto por el manillar y la parte trasera, y dejarla inclinada hasta que quede estable."),
             T("Hold the handlebar with both hands, <b>braking</b>, bring the motorcycle upright and push the stand back with your foot.", "Sujetar el manillar con ambas manos, <b>frenando</b>, poner la moto perpendicular a la calzada y empujar el soporte con el pie a su posición de reposo.")],
            [T("<b>Centre stand</b> (<i>caballete</i>)", "<b>Soporte central</b> (caballete)"),
             T("One hand on the handlebar, the other on the rear; press the stand down with your foot and, keeping your weight on it, pull the motorcycle <b>back and slightly up</b>.", "Una mano en el manillar y otra atrás; bajar el soporte con el pie y, cargando tu peso sobre él, tirar de la moto <b>hacia atrás y un poco hacia arriba</b>."),
             T("Sitting on the motorcycle with your feet on the ground, <b>push it forwards</b>, ready to use the <b>front brake</b>.", "Subido en la moto y con los pies en el suelo, <b>empujarla hacia delante</b>, con el <b>freno delantero</b> preparado.")],
        ],
        widths=["22%", "39%", "39%"],
        cls="small",
    ))
    B.append(H3("2.2 Moving off", "2.2 Puesta en marcha"))
    B.append(TABLE(
        [T("Step by step", "Paso a paso")],
        rows([
            ("Start the engine with the <b>electric starter</b> (button) or, failing that, the <b>kick-starter</b>.", "Arrancar con el <b>arranque eléctrico</b> (mando manual) o, en su defecto, con el <b>arranque de pedal</b>."),
            ("<b>Right foot on the ground</b>; with the <b>left</b> foot select <b>first gear</b> by pushing the lever <b>down</b>.", "<b>Pie derecho en el suelo</b>; con el <b>izquierdo</b> se selecciona la <b>primera</b> empujando la palanca <b>hacia abajo</b>."),
            ("<b>Open the throttle and let the clutch out gently and progressively</b>, to avoid a jerky start: the mass shifts back and the front wheel can even lift off (a <b>wheelie</b>).",
             "<b>Acelerar y soltar el embrague suave y progresivamente</b> para evitar salidas bruscas: la masa se desplaza hacia atrás y puede producirse un <b>caballito</b> (la rueda delantera se levanta)."),
            ("Once moving, <b>feet on the footrests</b>. Left foot: lever <b>up</b> to change <b>up</b>, <b>down</b> to change <b>down</b>.", "En movimiento, <b>pies en los estribos</b>. Con el pie izquierdo: palanca <b>hacia arriba</b> para <b>subir</b> marcha, <b>hacia abajo</b> para <b>bajarla</b>."),
        ]),
    ))

    B.append(H3("2.3 Riding position and the passenger", "2.3 La postura del conductor y el acompañante"))
    B.append(P(
        "Sit <b>astride</b> (a leg on each side), <b>relaxed and comfortable</b>, not leaning forward more than you need to reach the handlebar, head up and looking <b>well ahead</b> — not at the vehicle in front, but at the ones further on. "
        "A very high, upright position raises the centre of gravity: more fatigue and more wind resistance. Hold the handlebar <b>gently but firmly</b> (no tension), <b>arms slightly bent</b>. "
        "Keep your <b>knees against the tank</b>, especially in <b>bends</b> (better control of the weight) and when <b>braking</b> (so your body does not slide forward).",
        "Se va <b>sentado a horcajadas</b> (una pierna a cada lado), con una postura <b>suelta y cómoda</b>, sin inclinarse más de lo necesario para llegar al manillar, con la vista levantada y mirando <b>a lo lejos</b>: no al vehículo de delante, sino a los que van más adelante. "
        "Una posición muy alta y erguida eleva el centro de gravedad: más fatiga y más resistencia al avance. El manillar se agarra con <b>suavidad y firmeza</b> (sin agarrotamiento), con los <b>brazos ligeramente flexionados</b>. "
        "Las <b>rodillas contra el depósito</b>, sobre todo en las <b>curvas</b> (más control del peso) y en las <b>frenadas</b> (para que el cuerpo no se desplace hacia delante)."))
    B.append(BOX("key", "The passenger", "El acompañante", [
        ("Always <b>behind the rider</b> — <b>never between the rider and the handlebar</b> — <b>astride</b>, feet on the <b>footrests</b>. The law adds: over <b>12</b> (or over 7 with a parent, guardian or authorised adult), and only if the registration certificate allows a passenger (Topic 6).",
         "Siempre <b>detrás del conductor</b> —<b>nunca entre el conductor y el manillar</b>—, <b>a horcajadas</b> y con los pies en los <b>reposapiés</b>. La ley añade: mayor de <b>12 años</b> (o de 7 con su padre, madre, tutor o adulto autorizado), y solo si el permiso de circulación admite pasajero (Tema 6)."),
        ("Proper clothing and a <b>helmet</b>, like the rider.", "<b>Ropa adecuada y casco</b>, igual que el conductor."),
        ("Tell them how to behave: <b>hold on to the rider</b> and lean <b>exactly as the rider does</b>, especially in bends, so as not to unbalance the motorcycle.", "Informarle de cómo comportarse: que <b>se agarre al conductor</b> y adopte <b>la misma inclinación</b> que él, sobre todo en curvas, para no desequilibrar la moto."),
    ]))
    B.append(BOX("trap", "What changes with a passenger", "Cambios en la conducción con acompañante", [
        ("The motorcycle’s <b>centre of gravity</b> shifts. <b>Acceleration is weaker</b>, and when you accelerate the mass moves <b>backwards</b>.", "El <b>centro de gravedad</b> varía. La <b>aceleración es menor</b> y, al acelerar, la masa se desplaza <b>hacia atrás</b>."),
        ("<b>Braking takes longer</b>, but the <b>rear wheel locks less easily</b>, so you can use the <b>rear brake harder</b>.", "Las <b>frenadas son más prolongadas</b>, pero es <b>menos probable que se bloquee la rueda trasera</b>, así que se puede usar el <b>freno trasero con más fuerza</b>."),
        ("Raise the <b>rear tyre pressure</b> (as the manufacturer says), to avoid <b>wobble</b> (<i>fluctuación</i>): a swaying of the tyres that harms grip and stability, caused by the centre of gravity moving back, especially at speed, "
         "or by badly placed luggage or a poor road or motorcycle.",
         "Hay que <b>aumentar la presión del neumático trasero</b> (según el fabricante), para evitar la <b>fluctuación</b>: un oscilamiento o vaivén de los neumáticos que perjudica la adherencia y la estabilidad, por el desplazamiento del centro de gravedad hacia atrás, sobre todo a velocidad alta, "
         "o por una mala distribución del equipaje o el mal estado de la calzada o de la moto."),
    ]))

    B.append(H3("2.4 Bends", "2.4 Conducción en curvas"))
    B.append(P(
        "<b>In a straight line</b>: at <b>low speed it is harder to keep your balance</b>, so the rider has to move the handlebar and the body to avoid falling. From about <b>30 km/h</b> the <b>gyroscopic effect</b> of the spinning wheels starts to help keep the motorcycle balanced (your course).",
        "<b>En recta</b>: a <b>baja velocidad es más difícil mantener el equilibrio</b>, por lo que el conductor tiene que hacer giros de manillar y movimientos para no caer. <b>A partir de 30 km/h</b> el <b>efecto giroscópico</b> de las ruedas empieza a facilitar el equilibrio (tu curso)."))
    B.append(FIG(curve_moto, "Brake on the straight, before the bend; inside it, a gentle, steady throttle and your eyes on the exit; a leaning motorcycle takes up more width, so keep away from the centre line.",
                 "Frena en la recta, antes de la curva; dentro, acelera suave y progresivamente y mira a la salida; inclinada, la moto ocupa más anchura: aléjate del eje."))
    B.append(TABLE(
        [T("In a bend", "En curva"), T("What to do", "Qué hacer")],
        [
            [T("<b>Before</b> the bend", "<b>Antes</b> de la curva"),
             T("Judge the <b>line</b> you will follow and <b>adapt your speed</b>: brake <b>before entering</b>, not inside the bend, so you don’t lose grip. A leaning motorcycle <b>takes up more width</b>: don’t invade the opposite lane.",
               "Valorar la <b>trayectoria</b> y <b>adaptar la velocidad</b>: frenar <b>antes de entrar</b>, no durante la curva, para no perder adherencia. Inclinada, la moto <b>ocupa más espacio en anchura</b>: no invadir el sentido contrario.")],
            [T("<b>Inside</b> the bend", "<b>Dentro</b> de la curva"),
             T("<b>Accelerate progressively</b> to bring the motorcycle back upright. If braking is essential, do it <b>very gently</b>, so as not to lose stability.", "<b>Acelerar progresivamente</b> para recuperar la verticalidad. Si fuese imprescindible frenar, hacerlo <b>muy suavemente</b> para no perder estabilidad.")],
        ],
        widths=["22%", "78%"],
    ))
    B.append(BOX("key", "Enter in full control", "Entrar con la moto dominada", [
        ("Enter the bend with the motorcycle <b>fully under control</b>, so you won’t need to brake in it.", "Se debe entrar en la curva con el vehículo <b>totalmente dominado</b>, para no tener que frenar dentro."),
        ("<b>Emergency braking in a bend</b>: use <b>both brakes</b> and <b>look at the exit</b>. If you look at the obstacle, you instinctively steer towards it.", "<b>Frenada de emergencia en curva</b>: accionar los <b>dos frenos</b> y <b>mirar hacia la salida</b>. Si se mira el obstáculo, instintivamente se dirige la moto hacia él."),
    ]))
    B.append(BOX("trap", "Centrifugal force", "La fuerza centrífuga", [
        ("In a bend the rider fights the <b>centrifugal force</b> that pushes them outwards. It is greater with <b>more weight</b> (motorcycle and occupants), <b>more speed</b>, and a <b>tighter bend</b> (smaller radius).",
         "Al trazar una curva el motorista lucha contra la <b>fuerza centrífuga</b>, que le empuja hacia el exterior. Es mayor con <b>más peso</b> (moto y ocupantes), con <b>más velocidad</b> y cuanto <b>más cerrada</b> es la curva (menor radio)."),
    ]))

    B.append(H3("2.5 Braking", "2.5 Técnica de frenado"))
    B.append(P(
        "On a motorcycle the <b>front wheel</b> matters most for stability. Braking must be <b>progressive</b>: braking too hard with the front brake can <b>lock the front wheel</b> and throw you off, especially in bends. "
        "If a wheel locks, <b>release that brake at once</b> and apply it again once the wheel turns.",
        "En la moto, la rueda de <b>mayor importancia</b> para estabilizarla es la <b>delantera</b>. La frenada debe ser <b>progresiva</b>: frenar demasiado fuerte con el freno delantero puede <b>bloquear la rueda delantera</b> y provocar la caída, sobre todo en curvas. "
        "Si se bloquea una rueda, <b>soltar inmediatamente ese freno</b> y volver a accionarlo una vez desbloqueada."))
    B.append(FIG(braking_moto, "In an emergency, brake upright and share the braking: 60–70 % on the front wheel, 30–40 % on the rear (your course).",
                 "En una emergencia, frena con la moto recta y reparte la frenada: 60–70 % en la rueda delantera y 30–40 % en la trasera (tu curso)."))
    B.append(TABLE(
        [T("Emergency braking", "Frenada de emergencia")],
        rows([
            ("Brake when the motorcycle is <b>not leaning</b>, or before it leans.", "Frenar cuando <b>no exista inclinación lateral</b> o antes de ella."),
            ("Share it: <b>60–70 % on the front</b> wheel and <b>30–40 % on the rear</b>.", "Repartir la frenada: un <b>60–70 % en la delantera</b> y un <b>30–40 % en la trasera</b>."),
            ("<b>Pull the clutch in</b> and use <b>both brakes hard</b> (only in this kind of braking).", "Conviene <b>desembragar</b> y hacer un <b>uso intensivo de ambos frenos</b> (solo en este tipo de frenadas)."),
            ("The weight moves <b>forward</b>: the rear wheel loses traction and can <b>lock and skid</b>. With a passenger it locks less easily.", "El peso se desplaza <b>hacia delante</b>: la rueda trasera queda sin tracción y puede <b>bloquearse y derrapar</b>. Con pasajero es más difícil que se bloquee."),
            ("<b>Rigid body</b>: arms straight, <b>knees against the tank</b>, <b>heels pressing on the footrests</b>, so you don’t slide forward (harder than in normal braking).", "<b>Postura rígida</b>: brazos estirados, <b>rodillas contra el depósito</b> y <b>talones presionando los reposapiés</b> para no deslizarte hacia delante (con más fuerza que en una frenada normal)."),
        ]),
    ))
    B.append(BOX("key", "Engine brake", "Freno motor", [
        ("Support braking by <b>changing down</b> (engine brake), carefully, so the rising revs cause <b>no jolt and no locked wheel</b>. <b>Don’t pull the clutch in</b> until the motorcycle has almost stopped, except in emergency braking.",
         "Apoyar la frenada <b>reduciendo marchas</b> (freno motor), con cuidado de que el aumento de revoluciones no provoque <b>sacudidas ni bloqueo</b> de la rueda. <b>No accionar el embrague</b> hasta que la moto esté prácticamente detenida, salvo en frenadas de emergencia."),
        ("<b>Downhill</b>, use the engine brake so the service brakes <b>don’t overheat</b>.", "En <b>pendientes descendentes</b>, aprovechar el freno motor para <b>no calentar el freno de servicio</b>."),
    ]))
    B.append(BOX("trap", "Shaft drive", "Transmisión por cardan", [
        ("On a <b>shaft-drive</b> motorcycle, picking a <b>lower gear</b> by mistake and letting the clutch out <b>sharply</b> can make the rear wheel <b>bounce</b> hard and damage the transmission.",
         "En motos con transmisión por <b>cardan</b>, si por equivocación se selecciona una <b>marcha inferior</b> y se suelta <b>bruscamente</b> el embrague, puede producirse un <b>rebote acusado de la rueda trasera</b> y una avería de la transmisión."),
    ]))

    B.append(H3("2.6 In town", "2.6 Conducción en urbano"))
    B.append(TABLE(
        [T("Riding in town", "En poblado")],
        rows([
            ("Pay <b>more attention</b> (<b>defensive riding</b>): motorcycles are more vulnerable among pedestrians, junctions and traffic.", "Aumentar la atención (<b>conducción defensiva</b>): las motos son más vulnerables (peatones, intersecciones, la propia circulación)."),
            ("<b>Keep your feet on the footrests</b>, even at low speed, to avoid losing balance.", "<b>No quitar los pies de los estribos</b>, aunque se circule despacio, para evitar desequilibrios."),
            ("At <b>very low speed</b>, use the <b>rear brake</b> to keep the motorcycle stable, and <b>look ahead</b> — not just in front of the wheel.", "A <b>muy poca velocidad</b> es recomendable usar el <b>freno trasero</b> para mantener la estabilidad, y <b>mirar a lo lejos</b>, no cerca de la rueda delantera."),
        ]),
    ))

    B.append(H3("2.7 Riding in a group", "2.7 Conducción en grupo"))
    B.append(P("Group riding is very different from riding alone: each rider is <b>influenced by the others</b>, and competitiveness and other bad habits can appear.",
               "La conducción en grupo es muy diferente de la individual: el <b>comportamiento de cada uno se ve influido por el de los demás</b> (afán competitivo y otras conductas inadecuadas)."))
    B.append(FIG(group_ride, "Big groups split into subgroups of three or four with a gap between them; the least experienced in front; single file, slightly offset.",
                 "Los grupos grandes se dividen en subgrupos de tres o cuatro separados entre sí; los menos experimentados delante; en hilera, algo desviados."))
    B.append(TABLE(
        [T("In a group", "En grupo")],
        rows([
            ("A large group should not ride all together but in <b>subgroups of three or four</b>, with gaps between them.", "Si el grupo es numeroso, no deben ir todos juntos sino <b>divididos en subgrupos de tres o cuatro</b>, distanciados entre sí."),
            ("The <b>least experienced riders</b> and the <b>least powerful motorcycles</b> go in the <b>front groups</b>.", "Los <b>conductores con menos experiencia</b> y las <b>motos de menor potencia</b> van en los <b>grupos de cabeza</b>."),
            ("<b>Not side by side</b>, but in <b>single file</b>, slightly offset so each rider can see ahead.", "<b>No en paralelo</b>, sino <b>en hilera</b>, aunque algo desviados para facilitar la visión hacia delante."),
            ("<b>Responsibility is individual</b>: each rider answers for their own riding.", "<b>La responsabilidad es individual</b>, de cada conductor."),
        ]),
    ))
    B.append(P("For <b>mopeds</b>, which must use the shoulder when there is a suitable one, the law expressly forbids riding <b>side by side</b> (art. 36 of the Reglamento General de Circulación); only bicycles may ride two abreast.",
               "En los <b>ciclomotores</b>, que deben circular por el arcén si es transitable y suficiente, la ley prohíbe expresamente circular <b>en posición paralela</b> (art. 36 del Reglamento General de Circulación); solo las bicicletas pueden ir en columna de a dos."))

    B.append(H3("2.8 Motorcycle with a sidecar", "2.8 Conducción de motocicleta con sidecar"))
    B.append(P(
        "A sidecar outfit handles very differently: the <b>weight is not symmetrical</b> and the centre of gravity is <b>not in the middle</b> but shifted towards the motorcycle. "
        "Beware of the <b>centrifugal force</b> when turning <b>towards the side away from the sidecar</b>, or when swerving: you can lose grip and even <b>tip over towards the sidecar</b>. Ride <b>more gently</b> with a sidecar.",
        "La moto con sidecar se conduce de forma muy diferente: el <b>peso no está repartido simétricamente</b> y el centro de gravedad <b>no está en el medio</b>, sino desplazado hacia la moto. "
        "Hay que tener en cuenta la <b>fuerza centrífuga</b> al girar <b>hacia el lado contrario al sidecar</b> o al esquivar un obstáculo: se puede perder adherencia e incluso <b>volcar hacia el lado del sidecar</b>. La conducción debe ser <b>más moderada</b>."))
    B.append(TABLE(
        [T("Who rides where", "Quién va dónde")],
        rows([
            ("Up to <b>three people</b>, if the registration certificate allows it: the rider and one passenger on the motorcycle, and one in the sidecar (art. 12).", "Hasta <b>tres personas</b>, si lo autoriza el permiso de circulación: conductor y un pasajero en la moto y otro en el sidecar (art. 12)."),
            ("Your course adds: the <b>heavier</b> person goes in the sidecar, and a <b>single passenger</b> always rides <b>in the sidecar</b>, for the outfit’s stability, especially in turns.", "Tu curso añade: la persona de <b>mayor peso</b> va en el sidecar, y si hay <b>un solo pasajero</b>, siempre <b>en el sidecar</b>, por la estabilidad del conjunto, sobre todo en los giros."),
        ]),
    ))

    B.append(H3("2.9 Luggage on trips", "2.9 La carga en viajes"))
    B.append(FIG(luggage_moto, "Heavy things low and close to the centre of gravity (front rack on the tank); light things in the top case; the same weight in each side case.",
                 "Lo pesado, bajo y cerca del centro de gravedad (portaequipajes delantero, sobre el depósito); lo ligero, en el baúl; el mismo peso en cada maleta lateral."))
    B.append(TABLE(
        [T("Luggage rack", "Portaequipajes"), T("Use", "Uso")],
        [
            [T("<b>Front</b> (on the tank)", "<b>Delantero</b> (sobre el depósito)"), T("Good for <b>heavy</b> items: it doesn’t change the centre of gravity.", "Adecuado para objetos <b>pesados</b>: no modifica el centro de gravedad.")],
            [T("<b>Rear</b> (over the rear wheel)", "<b>Trasero</b> (sobre la rueda trasera)"), T("For <b>light</b> items only: heavy ones cause <b>wobble</b>.", "Para objetos <b>ligeros</b>: los pesados provocarían <b>fluctuación</b>.")],
            [T("<b>Side cases</b>", "<b>Laterales</b>"), T("Either side of the rear wheel: the <b>same weight on each side</b>, without overloading — dangerous at high speed.", "A los lados de la rueda trasera: <b>repartir el peso por igual</b> a cada lado y sin sobrecargar, porque a velocidad elevada puede ser peligroso.")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(P("How far a load may stick out on a motorcycle, and the passenger rules, are in <b>Topic 6</b>.", "Cuánto puede sobresalir la carga en una moto y las normas del pasajero están en el <b>Tema 6</b>."))

    B.append(H3("2.10 Pollution and fuel consumption", "2.10 Contaminación y consumo"))
    B.append(TABLE(
        [T("What raises fuel use and pollution", "Qué aumenta el consumo y la contaminación")],
        rows([
            ("<b>High speed</b> — the main factor.", "La <b>velocidad elevada</b>: el principal factor."),
            ("<b>Air resistance</b>: don’t modify the motorcycle’s aerodynamics (fairing).", "La <b>resistencia al aire</b>: no modificar la aerodinámica (carenado)."),
            ("<b>Aggressive riding</b>, with hard acceleration and braking: ride at a moderate speed and anticipate (<b>efficient riding</b>).", "La <b>conducción agresiva</b>, con acelerones y frenadas bruscas: circular a velocidad moderada y anticipándose (<b>conducción eficiente</b>)."),
            ("Riding in <b>town</b> uses more than on the open road; <b>poor maintenance</b>; <b>overloading</b>.", "En <b>poblado</b> se consume más que en carretera; el <b>mantenimiento defectuoso</b>; <b>cargar en exceso</b> la moto."),
        ]),
    ))
    B.append(BOX("key", "Tyres too", "También los neumáticos", [
        ("The same factors also wear the <b>tyres</b> faster, through friction and heat.", "Estos factores afectan también al <b>desgaste de los neumáticos</b>, por rozamiento y por calentamiento."),
    ]))

    # ---------------------------------------------------------------- 3. traps
    B.append(H2("3", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("Right hand: <b>throttle and front brake</b>. Left hand: <b>clutch</b>. Right foot: <b>rear brake</b>. Left foot: <b>gears</b>.", "Mano derecha: <b>acelerador y freno delantero</b>. Mano izquierda: <b>embrague</b>. Pie derecho: <b>freno trasero</b>. Pie izquierdo: <b>marchas</b>."),
        ("Mirrors: up to <b>100 km/h</b>, the <b>left</b> one is compulsory; over 100 km/h, <b>left and right</b>. Adjust them stopped, on level ground.", "Espejos: hasta <b>100 km/h</b>, obligatorio el <b>izquierdo</b>; más de 100 km/h, <b>izquierdo y derecho</b>. Se regulan parado y en llano."),
        ("First gear: lever <b>down</b>. Then up to change up, down to change down.", "Primera: palanca <b>hacia abajo</b>. Después, hacia arriba para subir y hacia abajo para bajar."),
        ("Passenger: <b>behind</b>, astride, feet on the footrests — <b>never between rider and handlebar</b>.", "Pasajero: <b>detrás</b>, a horcajadas, pies en los reposapiés: <b>nunca entre el conductor y el manillar</b>."),
        ("With a passenger: <b>longer braking</b>, <b>less acceleration</b>, the rear locks <b>less</b>, <b>more pressure</b> in the rear tyre.", "Con pasajero: <b>frenadas más largas</b>, <b>menos aceleración</b>, la trasera se bloquea <b>menos</b>, <b>más presión</b> en el neumático trasero."),
        ("Balance is hardest at <b>low speed</b>; the gyroscopic effect helps from about <b>30 km/h</b>.", "El equilibrio es más difícil a <b>baja velocidad</b>; el efecto giroscópico ayuda a partir de unos <b>30 km/h</b>."),
        ("Brake <b>before</b> the bend; inside it, <b>accelerate progressively</b>. Emergency in a bend: both brakes, <b>look at the exit</b>.", "Frenar <b>antes</b> de la curva; dentro, <b>acelerar progresivamente</b>. Emergencia en curva: los dos frenos y <b>mirar a la salida</b>."),
        ("Centrifugal force grows with <b>weight</b>, <b>speed</b> and a <b>tighter</b> bend.", "La fuerza centrífuga crece con el <b>peso</b>, la <b>velocidad</b> y una curva <b>más cerrada</b>."),
        ("Emergency braking: <b>60–70 % front, 30–40 % rear</b>, upright, clutch in. Locked wheel: <b>release and brake again</b>.", "Frenada de emergencia: <b>60–70 % delante, 30–40 % detrás</b>, recto y desembragado. Rueda bloqueada: <b>soltar y volver a frenar</b>."),
        ("Very slow in town: the <b>rear</b> brake, feet <b>on the footrests</b>.", "Muy despacio en ciudad: el freno <b>trasero</b> y los pies <b>en los estribos</b>."),
        ("Group: subgroups of <b>3–4</b>; the <b>least experienced in front</b>; single file, never side by side.", "Grupo: subgrupos de <b>3–4</b>; los <b>menos experimentados delante</b>; en hilera, nunca en paralelo."),
        ("Luggage: heavy on the <b>front rack</b>, light in the <b>top case</b>, side cases <b>balanced</b>.", "Carga: lo pesado en el portaequipajes <b>delantero</b>, lo ligero en el <b>baúl</b>, laterales <b>equilibradas</b>."),
    ]))

    # ---------------------------------------------------------------- 4. numbers
    B.append(H2("4", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Top speed above which a right mirror is also compulsory", "Velocidad máxima a partir de la cual el espejo derecho también es obligatorio"), T("over 100 km/h", "más de 100 km/h")],
            [T("Speed from which the gyroscopic effect helps balance", "Velocidad a partir de la cual el efecto giroscópico ayuda al equilibrio"), T("about 30 km/h", "unos 30 km/h")],
            [T("Emergency braking: front / rear", "Frenada de emergencia: delantera / trasera"), T("60–70 % / 30–40 %", "60–70 % / 30–40 %")],
            [T("Riders in each subgroup", "Motoristas por subgrupo"), T("3 or 4", "3 o 4")],
            [T("People on a motorcycle with a sidecar", "Personas en una moto con sidecar"), T("up to 3, if the certificate allows it", "hasta 3, si lo autoriza el permiso de circulación")],
            [T("Passenger’s minimum age", "Edad mínima del pasajero"), T("over 12 (over 7 with a parent, guardian or authorised adult)", "mayor de 12 (mayor de 7 con padre, madre, tutor o adulto autorizado)")],
        ],
        widths=["62%", "38%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["ft2", "ct1", "mr2", "st4", "ps1", "ps4", "cv2", "cv5", "bk2", "bk6", "gr2", "ld2"]


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
    ("Reglamento General de Circulación (RD 1428/2003), arts. 12 (passengers on motorcycles), 36 (riding side by side) and 118 (helmet and self-protection structures) — consolidated text",
     "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Reglamento General de Vehículos (RD 2822/1998), Anexo III.3: mirrors on mopeds, motorcycles, three-wheelers and quadricycles — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-1999-1826"),
    ("Real Decreto 518/2026 (reform in force 1 October 2026: art. 118 on helmets, gloves, closed shoes and self-protection structures)", "https://www.boe.es/buscar/doc.php?id=BOE-A-2026-13889"),
]

GLOSSARY = [
    ("scooter · naked (neoclásica) · rutera · deportiva", "scooter · naked · tourer · sports bike"),
    ("estructura de autoprotección", "self-protection structure"),
    ("carenado · cúpula", "fairing · screen"),
    ("manillar · maneta", "handlebar · lever"),
    ("acelerador (puño) · embrague", "throttle (twist grip) · clutch"),
    ("selector de marchas", "gear lever"),
    ("espejo retrovisor · ángulo muerto", "mirror · blind spot"),
    ("pata de cabra · caballete", "side stand · centre stand"),
    ("arranque eléctrico · de pedal", "electric starter · kick-starter"),
    ("estribos · reposapiés", "footrests"),
    ("a horcajadas", "astride"),
    ("acompañante · pasajero", "passenger (pillion)"),
    ("caballito", "wheelie"),
    ("fluctuación", "wobble"),
    ("efecto giroscópico", "gyroscopic effect"),
    ("fuerza centrífuga", "centrifugal force"),
    ("freno motor · reducir marchas", "engine brake · change down"),
    ("transmisión por cardan", "shaft drive"),
    ("conducción defensiva", "defensive riding"),
    ("en hilera · en paralelo", "in single file · side by side"),
    ("sidecar", "sidecar"),
    ("portaequipajes · baúl · maletas laterales", "luggage rack · top case · side cases (panniers)"),
    ("conducción eficiente", "efficient riding"),
]
