# -*- coding: utf-8 -*-
"""Category A1/A2, Topic 10 content (accidents and their factors), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the A1/A2 course's Tema 10 (Los accidentes y sus factores): social impact, the human
factor (falls, speed, fatigue, illness, alcohol and drugs, and the law on them), the vehicle factor (the motorcycle's
active and passive safety) and the road and the weather. The text is written for riders. The rules on alcohol and drugs
and the testing procedure are the same for every driver, so those tables are taken from Category B, Topic 10.

The rules come from the Ley sobre Tráfico (RDL 6/2015, art. 14), the Reglamento General de Circulación (arts. 20–28,
118 and, after the reform by RD 518/2026 in force 1 October 2026, the snow rule for motorways), and the Reglamento
General de Vehículos (Anexo XII), as they stand in November 2026.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from ..b10 import content as B10
from .diagrams import stop_moto, guardrail_posts, helmet_types, upright_low_grip, bac_curve, drowsy_clock

TWO = ("On two wheels", "Sobre dos ruedas")


def rows(pairs):
    return [[T(a, b)] for a, b in pairs]


# ------------------------------------------------------------------------------------------ taking blocks from Topic B10
def _under(B, start):
    i = next((k for k, b in enumerate(B) if b[0] == "h3" and b[1]["en"].startswith(start)), None)
    if i is None:
        raise KeyError(f"Topic B10 has no heading starting with {start!r}")
    out = []
    for b in B[i + 1:]:
        if b[0] in ("h2", "h3"):
            break
        out.append(b)
    return out


def _pick(B, start, kind, first):
    """The block of `kind` under heading `start` whose first English text starts with `first` (for figures: the function)."""
    for b in _under(B, start):
        if b[0] != kind:
            continue
        if kind == "p" and b[1]["en"].startswith(first):
            return b
        if kind == "table" and b[1][0]["en"].startswith(first):
            return b
        if kind == "box" and b[2]["en"].startswith(first):
            return b
        if kind == "fig" and b[1] is first:
            return b
    raise KeyError(f"No {kind} {first!r} under {start!r} in Topic B10")


def blocks():
    b10 = B10.blocks()
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Why accidents happen and how to avoid them on a motorcycle: the <b>human factor</b> (speed, fatigue, illness, alcohol and drugs), the <b>vehicle factor</b> (tyres, brakes, electronic aids, helmet and gear) "
         "and the <b>road and the weather</b>.",
         "Por qué se producen los accidentes y cómo evitarlos en moto: el <b>factor humano</b> (velocidad, fatiga, enfermedades, alcohol y drogas), el <b>factor vehículo</b> (neumáticos, frenos, ayudas electrónicas, casco y equipamiento) "
         "y la <b>vía y la climatología</b>."),
        ("The exam asks above all about <b>stopping distance</b> (0.75 s, rain ×2, ice ×10), <b>breaks</b> (every 2 hours or 200 km), the <b>alcohol limits</b> (0.25 / 0.15 / 0 mg/l) and the <b>tests</b>, "
         "the <b>helmet</b>, and <b>riding in rain, snow, fog, wind and sun</b>.",
         "El examen pregunta sobre todo por la <b>distancia de detención</b> (0,75 s, lluvia ×2, hielo ×10), los <b>descansos</b> (cada 2 horas o 200 km), las <b>tasas de alcohol</b> (0,25 / 0,15 / 0 mg/l) y las <b>pruebas</b>, "
         "el <b>casco</b> y la <b>conducción con lluvia, nieve, niebla, viento y sol</b>."),
        ("The sections follow your A1/A2 course’s Topic 10. The alcohol and drug rules are shared with <b>Category B, Topic 10</b>, which also covers cars, pedestrians, cyclists and e-scooters. "
         "Spanish exam terms are in <i>italics</i>, and a glossary closes the topic.",
         "Los apartados siguen el Tema 10 de tu curso A1/A2. Las normas de alcohol y drogas son comunes con el <b>Tema 10 del permiso B</b>, que trata además turismos, peatones, ciclistas y patinetes. "
         "Al final hay un glosario español–inglés."),
    ]))

    # ---------------------------------------------------------------- 1. social impact
    B.append(H2("1", "The social impact of accidents", "Impacto social"))
    B.append(P(
        "For the World Health Organization, road accidents are a <b>serious, priority public-health problem</b> worldwide. In Spain they are one of the <b>main causes of death and injury</b>, and "
        "<b>excessive speed</b> is the leading cause of accidents.",
        "Según la Organización Mundial de la Salud, los accidentes de tráfico son un <b>problema grave y prioritario de salud pública</b> en todo el mundo. En España son una de las <b>principales causas de muerte y lesiones</b>, y "
        "el <b>exceso de velocidad</b> es la causa principal de los accidentes."))
    B.append(TABLE(
        [T("Where and when", "Dónde y cuándo"), T("Most dangerous", "Más peligrosos")],
        [
            [T("<b>Places</b>", "<b>Lugares</b>"),
             T("More accidents with victims happen in <b>towns</b>, but more people <b>die</b> on <b>interurban roads</b>, where speeds are higher. <b>Autopistas and autovías</b> are the <b>safest</b> roads: separate directions, no intersections, gentler layout.",
               "El número de accidentes con víctimas es <b>mayor en vías urbanas</b>, pero el de <b>víctimas mortales</b> es mayor en las <b>carreteras</b>, donde se circula más deprisa. Las <b>autopistas y autovías</b> son las <b>más seguras</b>: sentidos separados, sin intersecciones, trazado menos sinuoso.")],
            [T("<b>Times</b>", "<b>Momentos</b>"),
             T("<b>Going to and coming back from work</b>, above all the <b>evening</b> return; <b>holidays, bank holidays and weekends</b>, above all in the <b>early hours</b> (<i>madrugada</i>).",
               "<b>Horas de entrada y salida del trabajo</b>, sobre todo al terminar la jornada por la <b>tarde</b>; <b>vacaciones, festivos y fines de semana</b>, sobre todo de <b>madrugada</b>.")],
        ],
        widths=["16%", "84%"],
    ))
    B.append(BOX("trap", "Weaving and sudden moves", "Zigzaguear y maniobras súbitas", [
        ("<b>Weaving between vehicles</b> and making <b>sudden manoeuvres without warning</b> are forbidden. Every sideways move must be <b>checked and signalled in advance</b>, and weaving through traffic counts as riding without due care.",
         "Está <b>prohibido zigzaguear entre los vehículos</b> y realizar <b>maniobras súbitas sin previo aviso</b>. Todo desplazamiento lateral debe <b>comprobarse y señalizarse con antelación</b>, y zigzaguear entre el tráfico es conducir sin la diligencia debida."),
    ]))

    # ---------------------------------------------------------------- 2. human factor
    B.append(H2("2", "The human factor", "Factor humano"))
    B.append(P(
        "The human factor is the <b>main cause</b> of accidents (<b>70–90 %</b>): most come from <b>unsuitable behaviour by the rider</b>. You must adapt your riding to what each moment demands (your own state, speed, the road, the weather, "
        "traffic, distractions, rules and signs); your ability depends on your <b>training</b> and your <b>experience</b>. Many motorcycle accidents happen at <b>weekends</b>, on leisure rides (your course puts it at 90 %), "
        "and they are a leading cause of death among <b>young people</b>.",
        "El factor humano es el <b>principal responsable</b> de los accidentes (<b>70–90 %</b>): la mayoría se deben a <b>comportamientos inadecuados del conductor</b>. Hay que adaptar la conducción a lo que exige cada momento (estado propio, velocidad, vía, climatología, "
        "circulación, distracciones, normas y señales); la capacidad depende de la <b>formación</b> y de la <b>experiencia</b>. Muchos accidentes de moto se producen los <b>fines de semana</b>, en salidas de ocio (tu curso habla del 90 %), "
        "y son una de las principales causas de mortalidad <b>juvenil</b>."))
    B.append(BOX("key", "Motorcycle accidents are easily fatal", "Los accidentes de moto son fácilmente letales", [
        ("A motorcycle accident often ends in <b>death or multiple injuries</b>: the rider has no bodywork around them.", "Un accidente de moto acaba muchas veces en <b>muerte o traumatismos múltiples</b>: el motorista no tiene carrocería que le proteja."),
        ("One of the main reasons for the high death rate is <b>not wearing a helmet</b>, or wearing it <b>unfastened</b>.", "Uno de los principales motivos de la alta mortalidad es <b>no usar el casco</b> o llevarlo <b>sin abrochar</b>."),
    ]))

    # 2.1 accident and fall
    B.append(H3("2.1 After an accident, and if you fall", "2.1 En caso de accidente y de caída"))
    B.append(P(
        "After an accident, <b>even a minor one</b>, check the <b>handlebar</b>, the <b>wheels</b>, the <b>lights</b> and the levels of <b>brake fluid, coolant, battery and oil</b>, and make sure there is <b>no oil on the brakes or tyres</b>. "
        "A careless check can leave you with a <b>mechanical failure</b> a few kilometres later.",
        "Después de un accidente, <b>aunque sea de poca importancia</b>, hay que comprobar el <b>manillar</b>, las <b>ruedas</b>, las <b>luces</b> y los niveles de <b>líquido de frenos, refrigeración, batería y aceite</b>, y que <b>no haya aceite en frenos ni neumáticos</b>. "
        "Una comprobación descuidada puede acabar en un <b>fallo mecánico</b> unos kilómetros después."))
    B.append(TABLE(
        [T("If the fall can’t be avoided", "Si la caída es inevitable")],
        rows([
            ("<b>Let go of the controls</b> at once, so the motorcycle does <b>not drag you</b> along.", "<b>Soltar los mandos</b> inmediatamente para <b>no ser arrastrado</b> por la motocicleta."),
            ("On the ground, stay calm and <b>slide — don’t roll</b> — until your body stops. <b>Don’t try to get up</b> before you have stopped, or you will fall again.",
             "En el suelo, mantener la calma y <b>deslizarse, no rodar</b>, hasta que el cuerpo se detenga. <b>No intentar levantarse</b> antes de haberse detenido, para no volver a caer."),
            ("The <b>helmet</b> and the right <b>clothing</b> make the difference: a <b>full-face helmet</b> and <b>leather or special fabrics with protectors</b> are recommended.",
             "El <b>casco</b> y la <b>ropa adecuada</b> marcan la diferencia: se recomienda <b>casco integral</b> y <b>ropa de cuero o tejidos especiales con protectores</b>."),
        ]),
    ))
    B.append(FIG(guardrail_posts, "In a fall, a rider slides towards the edge. A post with a cutting “H” profile causes very serious injuries; a rounded “C” profile, or a lower rail covering the posts, is far less dangerous.",
                 "En una caída, el motorista desliza hacia el borde. Un poste de perfil cortante en «H» causa lesiones muy graves; uno redondeado en «C», o una banda inferior que tape los postes, es mucho menos peligroso."))

    # 2.2 speed
    B.append(H3("2.2 Speed", "2.2 La velocidad"))
    B.append(TABLE(
        [T("Speed and safety", "Relación velocidad y seguridad")],
        rows([
            ("As speed rises you have <b>less time to see and analyse</b> what is around you (more serious mistakes): <b>anticipation and reaction get worse</b>, and <b>injuries are more serious</b>.",
             "A medida que aumenta la velocidad hay <b>menos capacidad para ver y analizar</b> lo que ocurre alrededor (errores más graves): <b>disminuye la anticipación y la reacción</b>, y las <b>lesiones son más graves</b>."),
            ("Riding fast for a long time raises <b>tension</b>, brings on <b>fatigue</b> sooner and makes you more <b>hostile or aggressive</b>.",
             "Conducir mucho tiempo a velocidad elevada aumenta la <b>tensión</b>, acelera la aparición de la <b>fatiga</b> y los comportamientos <b>hostiles o agresivos</b>."),
        ]),
    ))
    B.append(FIG(stop_moto, "From seeing the danger to stopping: the motorcycle first covers the reaction distance at full speed, then the braking distance. Rain doubles the braking distance; snow or ice multiplies it by ten.",
                 "Desde que se ve el peligro hasta que se para: la moto recorre primero la distancia de reacción sin frenar y después la de frenado. La lluvia duplica la distancia de frenado; la nieve o el hielo la multiplican por diez."))
    B.append(TABLE(
        [T("Term", "Concepto"), T("Meaning", "Significado")],
        [
            [T("<b>Reaction time</b>", "<b>Tiempo de reacción</b>"),
             T("From <b>perceiving</b> something to <b>responding</b>: normally half a second to a second, <b>typically 0.75 s</b>. It grows with <b>age</b>, <b>fatigue</b> and sleepiness, <b>alcohol, drugs</b> and some <b>medicines</b>, mood, illness, stress and <b>heat</b>.",
               "Desde que se <b>percibe</b> un estímulo hasta que se <b>responde</b>: normalmente entre medio y un segundo, <b>habitual 0,75 s</b>. Aumenta con la <b>edad</b>, la <b>fatiga</b> y la somnolencia, el <b>alcohol, las drogas</b> y algunos <b>medicamentos</b>, el estado de ánimo, enfermedades, estrés y el <b>calor</b>.")],
            [T("<b>Reaction distance</b>", "<b>Distancia de reacción</b>"), T("What you cover <b>during the reaction time</b>: more speed or a slower reaction, more metres.", "Lo que se recorre <b>durante el tiempo de reacción</b>: a más velocidad o más tiempo de reacción, más metros.")],
            [T("<b>Braking distance</b>", "<b>Distancia de frenado</b>"),
             T("From <b>applying the brakes</b> to <b>stopping</b>. It depends on the <b>speed</b>, the <b>mass</b> (passenger and load, and how it is placed), your <b>technique</b>, the motorcycle’s <b>condition</b> (tyres, brakes, suspension), "
               "the <b>road surface</b> and the <b>weather</b> (rain <b>×2</b>, snow or ice <b>×10</b>).",
               "Desde que se <b>accionan los frenos</b> hasta que la moto <b>se detiene</b>. Depende de la <b>velocidad</b>, la <b>masa</b> (pasajero y carga, y su colocación), la <b>técnica</b>, el <b>estado</b> de la moto (neumáticos, frenos, suspensión), "
               "el <b>firme</b> y la <b>meteorología</b> (lluvia <b>×2</b>, nieve o hielo <b>×10</b>).")],
            [T("<b>Stopping distance</b> (<i>parada técnica</i>)", "<b>Distancia de detención</b> (parada técnica)"), T("From <b>seeing the obstacle</b> to stopping: <b>reaction distance + braking distance</b>.", "Desde que se <b>ve el obstáculo</b> hasta detenerse: <b>distancia de reacción + distancia de frenado</b>.")],
        ],
        widths=["24%", "76%"],
    ))

    # 2.3 fatigue and sleep
    B.append(H3("2.3 Fatigue and sleep", "2.3 Fatiga y sueño"))
    B.append(TABLE(
        [T("Main effects of fatigue", "Principales efectos de la fatiga")],
        rows([
            ("<b>Muscle stiffness</b>; <b>slow, imprecise movements</b>.", "<b>Agarrotamiento muscular</b>; <b>lentitud y falta de precisión</b> en los movimientos."),
            ("<b>Behaviour changes</b>: more irritable, more risks.", "<b>Cambios de comportamiento</b>: más irritable, asume más riesgos."),
            ("<b>Less attention and concentration</b>, and a <b>longer reaction time</b>.", "<b>Menos atención y concentración</b>, y un <b>tiempo de reacción mayor</b>."),
        ]),
    ))
    B.append(TABLE(
        [T("Fatigue comes from…", "La fatiga aparece o aumenta debido…"), T("Circumstances", "Circunstancias")],
        [
            [T("<b>The rider</b>", "<b>Al conductor</b>"),
             T("Little experience; <b>riding for long periods without proper breaks</b> (the main cause); bad posture; high speed for a long time; riding sleepy, after alcohol or ill (even with a cold); changes in your usual riding habits.",
               "Poca experiencia; <b>conducir largos periodos sin descansar</b> o descansando mal (principal causa); posturas inadecuadas; velocidad excesiva mucho tiempo; conducir con sueño, alcohol o enfermo (incluso resfriado); cambios en los hábitos de conducción.")],
            [T("<b>The road</b>", "<b>A la vía y entorno</b>"), T("Heavy traffic; a poor surface; unfamiliar roads; bad weather.", "Mucho tráfico; firme en mal estado; vías poco conocidas; climatología adversa.")],
            [T("<b>The motorcycle</b>", "<b>Al vehículo</b>"), T("Poor condition (suspension, steering, lights).", "Mal estado de conservación (suspensión, dirección, iluminación).")],
        ],
        widths=["22%", "78%"],
    ))
    B.append(TABLE(
        [T("Why sleep raises the risk", "Por qué el sueño aumenta el riesgo")],
        rows([
            ("<b>Longer reaction time</b>; <b>more distractions</b> (especially on monotonous roads with little traffic); slower decisions with more mistakes.", "<b>Aumenta el tiempo de reacción</b>; <b>más distracciones</b> (sobre todo en entornos monótonos y con poco tráfico); decisiones más lentas y con más errores."),
            ("Slower, less precise movements; <b>microsleeps</b> — a few seconds asleep without realising it.", "Movimientos más lentos y menos precisos; <b>microsueños</b>: unos segundos dormido sin darse cuenta."),
            ("Worse perception (tired eyes, blurred vision, more dazzle); restlessness, hostility, more risk and <b>speeding to arrive sooner</b>.", "Peor percepción (fatiga ocular, visión borrosa, más deslumbramiento); inquietud, hostilidad, más riesgo y <b>acelerar para llegar antes</b>."),
        ]),
    ))
    B.append(FIG(drowsy_clock, "Drowsiness strikes hardest in the early hours (3–5 h) and early afternoon (14–16 h). Stop at least every 2 hours or 200 km, for 20–30 minutes.",
                 "La somnolencia aprieta de madrugada (3–5 h) y a primera hora de la tarde (14–16 h). Para como mínimo cada 2 horas o 200 km, de 20 a 30 minutos."))
    B.append(BOX("key", "Against drowsiness", "Para evitar la somnolencia", [
        ("Watch for the first <b>signs of fatigue and sleep</b>. If you are tired or sleepy, <b>stop somewhere suitable and sleep a little</b>.", "Atención a la aparición de los <b>síntomas de fatiga y sueño</b>. Si estás cansado o tienes sueño, <b>para en un lugar adecuado y duerme un poco</b>."),
        ("Rest <b>at least every 2 hours or 200 km</b>, for <b>20–30 minutes</b>.", "Descansa <b>como máximo cada 2 horas o cada 200 km</b>, de <b>20 a 30 minutos</b>."),
        ("On a motorcycle the <b>wind, noise, vibration, cold or heat</b> tire you sooner than in a car: take that into account when you plan the breaks.",
         "En moto el <b>viento, el ruido, las vibraciones, el frío o el calor</b> cansan antes que en un coche: tenlo en cuenta al planificar las paradas."),
    ]))

    # 2.4 illness, medicines, distractions
    B.append(H3("2.4 Illness, medicines and distractions", "2.4 Enfermedades, medicamentos y distracciones"))
    B.append(P(
        "Illnesses and medicines can affect the basic abilities for riding safely (especially <b>mental illnesses</b> and <b>neurological disorders</b>). A rider with a <b>chronic illness</b> should know it and the <b>side effects of the medicines</b>, "
        "recognise the <b>first symptoms of a crisis</b> and what to do, avoid what triggers one, <b>never drink alcohol while taking medicines</b>, and <b>ask the doctor</b> when in doubt.",
        "Las enfermedades y los medicamentos pueden afectar a las capacidades básicas para conducir con seguridad (sobre todo las <b>enfermedades mentales</b> y los <b>trastornos neurológicos</b>). Quien padezca una <b>enfermedad crónica</b> debe conocerla y los <b>efectos secundarios de los medicamentos</b>, "
        "reconocer los <b>primeros síntomas de una crisis</b> y saber actuar, evitar lo que la desencadena, <b>no tomar alcohol con medicamentos</b> y <b>consultar al médico</b> en caso de duda."))
    B.append(BOX("key", "Other causes of distraction", "Otras causas de distracción", [
        ("<b>Stress</b>, <b>anxiety</b>, <b>depression</b> and <b>advanced age</b>.", "El <b>estrés</b>, la <b>ansiedad</b>, la <b>depresión</b> y la <b>edad avanzada</b>."),
        ("<b>Medicines</b>: follow the doctor’s doses, don’t self-medicate, read whether the leaflet warns about driving, and never mix medicines with drugs or alcohol.",
         "Los <b>fármacos</b>: seguir la pauta del médico, no automedicarse, consultar si el prospecto advierte sobre la conducción y no mezclarlos con drogas ni alcohol."),
        ("Looking at the <b>sat-nav</b> or at directions, and the <b>phone</b> — <b>even hands-free</b>.", "Mirar el <b>GPS</b> o las indicaciones para llegar al destino, y el <b>teléfono móvil</b>, <b>incluso con manos libres</b>."),
    ]))

    # 2.5 alcohol and drugs
    B.append(H3("2.5 Alcohol and drugs", "2.5 Alcohol y drogas"))
    B.append(P(
        "Alcohol makes an accident <b>more likely</b> and its injuries <b>more serious</b>. It <b>depresses the central nervous system</b>, although at first it has a <b>euphoric phase</b>.",
        "El alcohol <b>aumenta la posibilidad de tener un accidente</b> y la <b>gravedad de las lesiones</b>. Es un <b>depresor del sistema nervioso central</b>, aunque al principio tiene una <b>fase euforizante</b>."))
    B.append(_pick(b10, "4.1.6 Alcohol", "table", "What alcohol changes"))
    B.append(_pick(b10, "4.1.6 Alcohol", "p", "The <b>blood alcohol level</b>"))
    B.append(_pick(b10, "4.1.6 Alcohol", "table", "Driver"))
    B.append(BOX("trap", f"{TWO[0]}: an A1 at 16 or 17", f"{TWO[1]}: el A1 con 16 o 17 años", [
        ("A rider <b>under 18</b> may not ride with <b>any alcohol at all</b>: <b>0.0</b>, not the 0.15 mg/l of new licences. Under 18 the zero rule wins; the 0.15 mg/l of the first two years only matters from 18.",
         "Un conductor <b>menor de 18 años</b> no puede circular con <b>nada de alcohol</b>: <b>0,0</b>, no los 0,15 mg/l de los permisos nuevos. Hasta los 18 manda la tasa cero; los 0,15 mg/l de los dos primeros años solo cuentan desde los 18."),
    ]))
    B.append(_pick(b10, "4.1.6 Alcohol", "box", "You can’t fool"))
    B.append(_pick(b10, "4.1.6 Alcohol", "fig", bac_curve))
    B.append(_pick(b10, "4.1.7 Drugs", "p", "Driving on public roads is <b>prohibited</b>"))

    # 2.6 the law
    B.append(H3("2.6 Alcohol, drugs and the law", "2.6 Tratamiento legal del alcohol y las drogas"))
    B.append(_pick(b10, "4.1.8", "table", "Step"))
    B.append(_pick(b10, "4.1.8", "table", "Result"))
    B.append(P(
        "In <b>serious cases</b> it is a <b>crime</b> and can mean prison: over <b>0.60 mg/l</b> in air (1.2 g/l in blood), riding under the influence of drugs, or <b>refusing the tests</b>. Category B, Topic 9 has the table of road-safety crimes.",
        "En los <b>casos graves</b> es <b>delito</b> y puede acarrear prisión: más de <b>0,60 mg/l</b> en aire (1,2 g/l en sangre), conducir bajo la influencia de drogas o <b>negarse a las pruebas</b>. El Tema 9 del permiso B recoge la tabla de delitos contra la seguridad vial."))

    # ---------------------------------------------------------------- 3. vehicle
    B.append(H2("3", "The vehicle factor", "Factor vehículo"))
    B.append(P(
        "Modern motorcycles carry devices that make an accident <b>less likely</b> or <b>less serious</b>. They are no use if the rider <b>uses them badly</b> or if <b>poor maintenance</b> has left them in bad condition — which can itself cause an accident.",
        "Las motos actuales incorporan dispositivos que reducen la posibilidad de sufrir un accidente o <b>minimizan sus consecuencias</b>. No sirven de nada si el conductor <b>no los usa bien</b> o si un <b>mantenimiento deficiente</b> los ha dejado en mal estado, lo que puede causar un accidente."))
    B.append(H3("3.1 Active safety: tyres", "3.1 Seguridad activa: neumáticos"))
    B.append(P(
        "<b>Active safety</b> tries to <b>prevent the accident</b>: wheels, brakes, suspension, steering and lights. The <b>tyres</b> are the only part of the motorcycle that touches the ground. Their <b>tread</b> has channels that give <b>grip</b> and clear the <b>water</b> from the road.",
        "La <b>seguridad activa</b> trata de <b>evitar que se produzca el accidente</b>: ruedas, frenos, suspensión, dirección y luces. Los <b>neumáticos</b> son lo único de la moto que toca el suelo. Su <b>banda de rodamiento</b> tiene canales que dan <b>agarre</b> y evacuan el <b>agua</b> de la calzada."))
    B.append(TABLE(
        [T("Tyres", "Neumáticos"), T("Rule", "Norma")],
        [
            [T("<b>Pressure</b>", "<b>Presión de inflado</b>"),
             T("The one the <b>manufacturer</b> gives, checked <b>regularly</b>, with the tyres <b>cold</b> and a gauge in good condition. If you check them hot, <b>don’t let out the extra pressure</b>: the manufacturer counts on it.",
               "La que indica el <b>fabricante</b>, comprobada <b>periódicamente</b>, con los neumáticos <b>fríos</b> y un manómetro en buen estado. Si los compruebas calientes, <b>no quites el aumento</b>: el fabricante lo prevé como normal.")],
            [T("<b>Changing tyres</b>", "<b>Cambio de neumáticos</b>"),
             T("Never sizes other than the <b>manufacturer’s</b>. A new tyre’s design affects safety and handling. Fit it in the right <b>direction of rotation</b> (arrow on the sidewall).",
               "Nunca medidas distintas a las del <b>fabricante</b>. El diseño del neumático nuevo influye en la seguridad y en la conducción. Móntalo en el <b>sentido de giro</b> correcto (flecha en el flanco).")],
            [T("<b>Condition</b>", "<b>Estado</b>"),
             T("No <b>cuts or deformations</b>: they cause dangerous steering movements, above all at high speed. A <b>worn</b> tyre loses grip.",
               "Sin <b>cortes ni deformaciones</b>: provocan movimientos peligrosos en la dirección, sobre todo a alta velocidad. Un neumático <b>desgastado</b> pierde adherencia.")],
        ],
        widths=["22%", "78%"],
    ))
    B.append(H3("3.2 Active safety: brakes", "3.2 Seguridad activa: frenos"))
    B.append(P(
        "Brakes <b>slow the motorcycle down, stop it or hold it still</b>, by pressing a fixed part (<b>pads or shoes</b>) against a moving one (<b>discs or drums</b>). Every motorcycle must have <b>two braking devices</b>, "
        "one acting at least on the <b>rear wheel</b> and the other on the <b>front wheel</b>; with a <b>sidecar</b>, its wheel need not have a brake.",
        "Los frenos <b>reducen la velocidad, detienen o inmovilizan</b> la moto haciendo rozar una parte fija (<b>pastillas o zapatas</b>) con una móvil (<b>discos o tambores</b>). Toda motocicleta debe tener <b>dos dispositivos de frenado</b>, "
        "que actúen, uno por lo menos, sobre la <b>rueda trasera</b> y el otro sobre la <b>delantera</b>; con <b>sidecar</b>, no se exige frenar su rueda."))
    B.append(TABLE(
        [T("Brake", "Freno"), T("What to know", "Lo que hay que saber")],
        [
            [T("<b>Front</b>", "<b>Delantero</b>"),
             T("It <b>wears more</b>. Usually a <b>disc</b>: it stops in <b>fewer metres</b>, has <b>less risk of locking</b>, and <b>cools better</b> (it delays <b>fading</b>, the loss of braking when the brakes overheat).",
               "Se <b>desgasta más</b>. Suele ser de <b>disco</b>: frena en <b>menos metros</b>, tiene <b>menos riesgo de bloqueo</b> y <b>se refrigera mejor</b> (retrasa el <b>fading</b>, la pérdida de eficacia por calentamiento).")],
            [T("<b>Rear</b>", "<b>Trasero</b>"), T("<b>Disc or drum</b>.", "<b>Disco o tambor</b>.")],
            [T("<b>Maintenance</b>", "<b>Mantenimiento</b>"),
             T("The system is usually <b>hydraulic</b>: check the <b>brake fluid</b> between minimum and maximum, the <b>hoses</b>, the <b>pads or shoes</b> and the <b>discs or drums</b> — especially if the motorcycle has spent days <b>outside in damp weather</b>.",
               "El mando suele ser <b>hidráulico</b>: comprobar el <b>líquido de frenos</b> entre mínimo y máximo, los <b>latiguillos</b>, las <b>pastillas o zapatas</b> y los <b>discos o tambores</b>, sobre todo si la moto ha pasado días <b>a la intemperie con humedad</b>.")],
            [T("<b>ABS</b>", "<b>ABS</b>"),
             T("Fitted to many motorcycles: it <b>stops the wheels locking under hard braking</b>, adjusting the braking force to the <b>grip</b>, so you <b>keep control of your path</b>.",
               "Lo llevan muchas motos: <b>evita el bloqueo de las ruedas en una frenada brusca</b>, regulando la frenada según la <b>adherencia</b>, y permite <b>controlar la trayectoria</b>.")],
        ],
        widths=["18%", "82%"],
    ))
    B.append(H3("3.3 Suspension, steering and electronic aids", "3.3 Suspensión, dirección y sistemas ADAS"))
    B.append(P(
        "The <b>suspension</b> keeps the wheels <b>on the ground</b> (grip and control, less skidding or locking) and stops bumps reaching the rider and passenger (comfort). "
        "The <b>steering</b> points the front wheel where the handlebar sends it; its angle and trail give a smooth, stable ride.",
        "La <b>suspensión</b> mantiene las ruedas <b>apoyadas</b> en el pavimento (adherencia y control, menos derrapes o bloqueos) y evita que las irregularidades lleguen al conductor y al pasajero (comodidad). "
        "La <b>dirección</b> orienta la rueda delantera según la trayectoria marcada con el manillar; su avance e inclinación dan una conducción suave y estable."))
    B.append(TABLE(
        [T("System", "Sistema"), T("What it does", "Qué hace")],
        [
            [T("<b>IMU</b> (inertial measurement unit)", "<b>IMU</b> (unidad de medición inercial)"), T("The motorcycle’s “electronic brain”: accelerometers and gyroscopes measure its movement and lean in real time and feed the other aids.", "El «cerebro electrónico» de la moto: acelerómetros y giroscopios miden su movimiento e inclinación en tiempo real y alimentan las demás ayudas.")],
            [T("<b>Quickshifter</b>", "<b>Quickshifter</b>"), T("Changes gear <b>without the clutch lever</b>, cutting the power for an instant so the gears engage smoothly.", "Cambia de marcha <b>sin usar la maneta de embrague</b>, cortando la potencia un instante para que las marchas engranen con suavidad.")],
            [T("<b>Anti-wheelie</b>", "<b>Anti-wheelie</b> (anti caballito)"), T("Stops the <b>front wheel lifting</b> under hard acceleration, by cutting power or braking gently.", "Evita que la <b>rueda delantera se levante</b> al acelerar fuerte, reduciendo potencia o frenando suavemente.")],
            [T("<b>Traction control</b>", "<b>Control de tracción</b>"), T("Doses the power to the <b>grip</b> so the rear wheel does not spin. <b>It can be switched off.</b>", "Dosifica la potencia según la <b>adherencia</b> para que la rueda trasera no patine. <b>Se puede desconectar.</b>")],
            [T("<b>Combined braking</b>", "<b>Frenada combinada</b>"), T("One control brakes <b>both wheels</b>, sharing the pressure for a steadier stop.", "Un mando frena <b>las dos ruedas</b>, repartiendo la presión para una frenada más uniforme.")],
            [T("<b>Hill holder</b>", "<b>Hill holder</b>"), T("Holds the rear brake when you move off uphill, so the motorcycle does not roll back.", "Mantiene el freno trasero al arrancar en subida para que la moto no vaya hacia atrás.")],
            [T("<b>Downhill brake control</b>", "<b>Control de frenada en pendiente</b>"), T("On steep descents, with the ABS, stops the <b>rear wheel lifting</b>.", "En bajadas pronunciadas, con el ABS, impide que la <b>rueda trasera se despegue</b> del suelo.")],
            [T("<b>Emergency brake signal</b>", "<b>Señal de frenada de emergencia</b>"), T("Under hard braking the <b>indicators flash</b> to warn whoever is behind.", "En una frenada enérgica, los <b>intermitentes parpadean</b> para avisar al de detrás.")],
            [T("<b>Blind-spot detection</b>", "<b>Detección de ángulo muerto</b>"), T("Warns of vehicles <b>coming up behind in the next lanes</b>.", "Avisa de los vehículos que se <b>aproximan por detrás en los carriles contiguos</b>.")],
            [T("<b>Adaptive cruise control</b>", "<b>Control de crucero adaptativo</b>"), T("Holds the speed you set, or the road’s, <b>keeping the safety distance</b>.", "Mantiene la velocidad fijada, o la de la vía, <b>conservando la distancia de seguridad</b>.")],
            [T("<b>Active speed limiter</b>", "<b>Limitador de velocidad activo</b>"), T("The motorcycle <b>will not exceed</b> the limit you set.", "La moto <b>no superará</b> el límite que fijes.")],
            [T("<b>Forward collision warning</b>", "<b>Advertencia de colisión frontal</b>"), T("A visual <b>warning</b> of a possible head-on collision.", "<b>Aviso</b> visual de una posible colisión frontal.")],
        ],
        widths=["30%", "70%"],
        cls="small",
    ))
    B.append(P(
        "Your course repeats the blind-spot description under a second “adaptive cruise control”; the table above gives each system once.",
        "Tu curso repite la descripción del ángulo muerto bajo un segundo «control de crucero adaptativo»; la tabla da cada sistema una sola vez."))

    B.append(H3("3.4 Passive safety: helmet and gear", "3.4 Seguridad pasiva: casco y equipamiento"))
    B.append(P(
        "<b>Passive safety</b> reduces the <b>consequences</b> of an accident. A motorcycle has much less of it than a car: the fairing (protects from the weather and some impacts), crash bars, the right clothing and, above all, the <b>helmet</b>. "
        "The helmet absorbs much of an impact’s energy, greatly reducing the chance of <b>fatal injuries</b>, and protects head and face from <b>abrasion</b> on the road. <b>Not wearing it is the main cause of death</b> in motorcycle and moped accidents; "
        "it is <b>compulsory for rider and passenger</b>.",
        "La <b>seguridad pasiva</b> reduce las <b>consecuencias</b> de un accidente. En la moto es mucho menor que en un turismo: el carenado (protege de agentes atmosféricos y de algunos impactos), los arcos de protección, la ropa adecuada y, sobre todo, el <b>casco</b>. "
        "El casco absorbe gran parte de la energía del impacto, reduce mucho la posibilidad de <b>lesiones mortales</b> y protege cabeza y cara de la <b>abrasión</b> contra el pavimento. <b>No usarlo es la principal causa de mortalidad</b> en los accidentes de moto y ciclomotor; "
        "es <b>obligatorio para conductor y pasajero</b>."))
    B.append(FIG(helmet_types, "The full-face helmet is the one to recommend; the modular one only protects like it with the chin bar closed; the jet leaves the chin bare.",
                 "El casco integral es el recomendable; el modular solo protege como él con la mentonera cerrada; el jet deja la barbilla al descubierto."))
    B.append(TABLE(
        [T("Choosing a helmet", "Requisitos para elegir un casco")],
        rows([
            ("<b>Approved to UNECE Regulation 22</b> (label inside): it has passed the safety tests. Since 1 October 2026 this is required on mopeds too (certified moped helmets may be used until 1 October 2027).",
             "<b>Homologado conforme al Reglamento UNECE R22</b> (etiqueta interior): ha superado las pruebas de seguridad. Desde el 1 de octubre de 2026 se exige también en ciclomotor (los cascos certificados de ciclomotor pueden usarse hasta el 1 de octubre de 2027)."),
            ("<b>Type</b>: full-face recommended. <b>Size</b>: a snug fit. <b>Material</b>: according to the resistance it gives.", "<b>Tipo</b>: recomendable el integral. <b>Tamaño</b>: bien ajustado. <b>Material</b>: según la resistencia que proporciona."),
            ("<b>Fastening</b>: properly done up, so it cannot fly off in an accident.", "<b>Cierres y correas</b>: perfectamente abrochado, para que no salga despedido en un accidente."),
            ("<b>Colour</b>: light, bright and reflective colours are safer (you are seen). <b>Ventilation</b>: more comfort, less misting.", "<b>Color</b>: más seguros los claros, brillantes y reflectantes (más visibles). <b>Ventilación</b>: más comodidad y menos vaho."),
            ("<b>Visor</b>: in perfect condition, ideally <b>anti-fog</b>; without a visor, wear <b>goggles or glasses</b>.", "<b>Pantalla</b>: en perfecto estado, recomendable <b>antivaho</b>; sin pantalla, usar <b>gafas</b>."),
        ]),
    ))
    B.append(BOX("trap", "Replace the helmet", "Sustituir el casco", [
        ("Replace (throw away) the helmet <b>after an accident</b> or any <b>hard knock</b>, even if you see no damage.", "El casco se debe <b>sustituir</b> (desechar) <b>después de un accidente</b> o de <b>un fuerte golpe</b>, aunque no se vean daños."),
    ]))
    B.append(TABLE(
        [T("Rider’s gear", "Equipamiento motorista"), T("What to know", "Lo que hay que saber")],
        [
            [T("<b>Suit or jacket</b>", "<b>Traje o chaqueta</b>"), T("Leather or another <b>abrasion-resistant</b> material, with <b>protectors</b> (back, knees, elbows…); bright, even reflective, colours.", "De piel u otro material <b>resistente a la abrasión</b>, con <b>protecciones</b> (espalda, rodillas, codos…); colores llamativos e incluso reflectantes.")],
            [T("<b>Closed shoes</b>", "<b>Calzado cerrado</b>"), T("<b>Compulsory on every road</b> since 1 October 2026: covering the whole foot. High, fitted boots with a heel are recommended; never sandals.", "<b>Obligatorio en todo tipo de vías</b> desde el 1 de octubre de 2026: que cubra todo el pie. Se recomienda caña alta, ajustado y con tacón; nunca sandalias.")],
            [T("<b>Protective gloves</b>", "<b>Guantes de protección</b>"), T("<b>Compulsory on interurban roads</b>. They protect from the cold, keep the feel of the controls, and protect your hands in a <b>fall</b>.", "<b>Obligatorios en vías interurbanas</b>. Protegen del frío, mantienen la sensibilidad para manejar los mandos y protegen las manos en una <b>caída</b>.")],
            [T("<b>Other gear</b>", "<b>Otras prendas</b>"),
             T("<b>Balaclavas</b> against the cold; <b>kidney belts and back protectors</b> (support the back, reduce vibration and fatigue, protect in a fall); <b>goggles</b> if the helmet has no visor; an <b>airbag jacket or vest</b>, which inflates when you are thrown off to protect chest, neck and spine.",
               "<b>Sotocascos</b> contra el frío; <b>fajas y espalderas</b> (sujetan la espalda, reducen vibraciones y fatiga, protegen en una caída); <b>gafas</b> si el casco no tiene visera; <b>chaqueta o chaleco airbag</b>, que se activa al salir despedido y protege tórax, cervicales y columna.")],
        ],
        widths=["22%", "78%"],
    ))
    B.append(BOX("key", "The reflective vest", "El chaleco reflectante", [
        ("Since 1 October 2026 every motorcycle must <b>carry</b> a high-visibility <b>reflective vest</b>. Wear it when you <b>get off</b> and stand on the <b>carriageway or shoulder of an interurban road</b>.",
         "Desde el 1 de octubre de 2026 toda motocicleta debe <b>llevar</b> un <b>chaleco reflectante</b> de alta visibilidad. Se usa al <b>bajarse</b> y ocupar la <b>calzada o el arcén de una vía interurbana</b>."),
        ("Riders who <b>work</b> on a motorcycle, three-wheeler, quad, moped, bicycle or VMP must wear the vest <b>on every road</b> while riding.",
         "Quienes <b>trabajan</b> circulando en moto, vehículo de tres ruedas, quad, ciclomotor, bicicleta o VMP deben llevarlo puesto <b>en todo tipo de vías</b>."),
    ]))

    # ---------------------------------------------------------------- 4. road and weather
    B.append(H2("4", "The road and its surroundings", "Factor vía y su entorno"))
    B.append(P(
        "Adapt your riding to the <b>road</b> — take special care with <b>loose gravel or sand</b>, <b>train or tram rails</b>, dirt or damp, <b>painted road markings</b> and slippery spots such as <b>oil</b> — keeping the safety distance at all times, "
        "and to the <b>weather</b> (rain, snow, fog…).",
        "Adapta la conducción a la <b>vía</b> (especial cuidado con <b>gravilla suelta o arena</b>, <b>raíles de tren o tranvía</b>, suciedad o humedad, la <b>pintura de las marcas viales</b> y lugares deslizantes como <b>manchas de aceite</b>), "
        "manteniendo siempre la distancia de seguridad, y a la <b>climatología</b> (lluvia, nieve, niebla…)."))
    B.append(FIG(upright_low_grip, "Where grip is low, slow down before you reach it and cross it with the motorcycle as upright as possible, at a right angle to the road surface.",
                 "Donde hay baja adherencia, reduce antes de llegar y pasa con la moto lo más enderezada posible, formando un ángulo recto con el pavimento."))

    B.append(H3("4.1 Rain", "4.1 Lluvia"))
    B.append(P(
        "Rain cuts <b>visibility</b> and <b>grip</b>, and is most dangerous with the <b>first drops</b>, which mix with the dirt into a very slippery film. Drops on the <b>visor</b> blur what you see; the visor <b>mists up</b> more easily "
        "(riding with it <b>slightly open</b> helps) and lights work less well. Water on the road hides the markings when your light reflects on it — <b>main beam is a bad idea</b>, it dazzles you.",
        "La lluvia reduce la <b>visibilidad</b> y la <b>adherencia</b>, y es más peligrosa con las <b>primeras gotas</b>, que forman con la suciedad un barrillo muy deslizante. Las gotas en la <b>visera</b> distorsionan lo que ves; la visera se <b>empaña</b> con más facilidad "
        "(ayuda llevarla <b>semiabierta</b>) y las luces pierden eficacia. El agua en la calzada oculta las marcas al reflejar la luz: <b>la luz de carretera no conviene</b>, te deslumbra."))
    B.append(TABLE(
        [T("For grip in the rain", "Para mejorar la adherencia con lluvia")],
        rows([
            ("Ride <b>smoothly at a moderate speed</b>, without sudden moves when changing lane, braking or accelerating; look <b>far ahead</b>.", "Conducir con <b>suavidad y a velocidad moderada</b>, sin movimientos bruscos al cambiar de carril, frenar o acelerar; mirar <b>a lo lejos</b>."),
            ("<b>Brake early and gently</b> (braking distance can <b>double</b>) and leave more distance.", "<b>Frenar con antelación y suavidad</b> (la distancia de frenado puede <b>duplicarse</b>) y aumentar la distancia de seguridad."),
            ("<b>Share the braking between both wheels</b>, with <b>less pressure on the front</b> (your course: a locked rear wheel is easier to control than a locked front one). If a wheel locks, <b>release the brake and brake again</b>.",
             "<b>Repartir la frenada entre las dos ruedas</b>, con <b>menos presión en la delantera</b> (tu curso: el bloqueo de la trasera se controla mejor que el de la delantera). Si se bloquea una rueda, <b>soltar el freno y volver a frenar</b>."),
            ("In bends, <b>lean less</b> and slow down more than usual before entering.", "En las curvas, <b>inclinar menos</b> la moto y reducir más de lo normal antes de entrar."),
            ("Keep off <b>painted markings</b>, <b>cobbles</b> and other slippery spots (dirt, fallen leaves).", "Evitar circular sobre las <b>marcas viales</b>, <b>adoquines o empedrados</b> y otros elementos deslizantes (suciedad, hojas)."),
            ("Wet brakes lose effect: <b>dry them with short presses</b>, above all after a flooded stretch (better to avoid puddles).", "Los frenos mojados pierden eficacia: <b>secarlos con pequeñas frenadas</b>, sobre todo tras una zona anegada (mejor evitar los charcos)."),
        ]),
    ))
    B.append(BOX("key", "Storms and aquaplaning", "Tormentas y aquaplaning", [
        ("Waterproof clothing is recommended (a rain suit on trips). In a <b>very heavy storm</b>, the best thing is to <b>stop and take shelter away from the motorcycle</b>.",
         "Es recomendable ropa impermeable (en viajes, un mono de agua). Con una <b>tormenta muy intensa</b>, lo mejor es <b>detener la marcha y resguardarse apartado de la moto</b>."),
        ("<b>Aquaplaning</b>: at too high a speed the tread <b>cannot clear the water</b> and the tyre slides on it — the motorcycle <b>ignores steering and brakes</b>. Worst with <b>worn tyres</b> and on <b>two-wheelers</b>.",
         "<b>Aquaplaning</b>: a velocidad excesiva el dibujo <b>no puede desalojar el agua</b> y el neumático se desliza sobre ella: la moto <b>no obedece a la dirección ni al freno</b>. Peor con <b>neumáticos gastados</b> y en <b>vehículos de dos ruedas</b>."),
    ]))

    B.append(H3("4.2 Snow and ice", "4.2 Nieve y hielo"))
    B.append(TABLE(
        [T("Snow", "Nieve"), T("What to do", "Qué hacer")],
        [
            [T("<b>The danger</b>", "<b>El peligro</b>"),
             T("Less <b>visibility</b> and <b>grip</b>; worst with the <b>first flakes</b> and when it <b>hardens</b>. Cold slows your reactions and numbs hands and feet, so you work the controls more roughly: <b>gloves, boots and warm clothes</b> are essential.",
               "Menos <b>visibilidad</b> y <b>adherencia</b>; más peligrosa con los <b>primeros copos</b> y cuando se <b>endurece</b>. Con el frío el cuerpo reacciona más despacio y se pierde tacto en pies y manos: son fundamentales <b>guantes, botas y ropa</b> de abrigo.")],
            [T("<b>To see</b>", "<b>Visibilidad</b>"),
             T("The compulsory lights (no main beam: the reflection dazzles you); a <b>dark visor or sunglasses</b> by day against the glare.", "El alumbrado obligatorio (sin luces largas: el reflejo deslumbra); <b>visera oscura o gafas de sol</b> de día contra el reflejo.")],
            [T("<b>For grip</b>", "<b>Adherencia</b>"),
             T("Move off with the wheels <b>straight</b>, releasing the clutch slowly and with <b>smooth, steady throttle</b>; no braking or sudden moves, especially in bends; <b>more distance</b> and low speed; the <b>highest gear possible</b>. "
               "Uphill: <b>long gears</b>, slow and steady; downhill: <b>short gears</b> (engine brake), braking very gently and early if at all.",
               "Arrancar con las ruedas <b>rectas</b>, soltando el embrague despacio y con <b>aceleración suave y constante</b>; sin frenar ni movimientos bruscos, sobre todo en curvas; <b>más distancia</b> y velocidad reducida; la <b>marcha más alta posible</b>. "
               "Subiendo: <b>marchas largas</b>, lento y sostenido; bajando: <b>marchas cortas</b> (freno motor), y si se frena, con mucha suavidad y antelación.")],
        ],
        widths=["18%", "82%"],
    ))
    B.append(P(
        "<b>Ice</b> is the <b>most dangerous</b> situation: grip is almost nil and the stopping distance is multiplied by <b>10</b>. The best advice is <b>not to ride</b> on icy roads. On <b>hard snow or ice</b>, <b>don’t brake or accelerate</b>.",
        "El <b>hielo</b> es la <b>situación más peligrosa</b>: la adherencia es casi nula y la distancia de detención se multiplica por <b>10</b>. Lo recomendable es <b>no circular</b> con hielo en la calzada. Sobre <b>nieve endurecida o hielo</b>, <b>ni frenar ni acelerar</b>."))
    B.append(BOX("trap", "Snow rules", "Normas con nieve", [
        ("On <b>autopistas and autovías</b>, when snow makes driving difficult, <b>overtaking is forbidden</b> and you must use the <b>right-hand lane</b> (also the next one where there are three or more lanes), leaving the left lanes for <b>emergency vehicles and snowploughs</b>.",
         "En <b>autopistas y autovías</b>, cuando la nieve dificulte la circulación, está <b>prohibido adelantar</b> y es obligatorio circular por el <b>carril de la derecha</b> (también su contiguo en tramos de tres o más carriles), dejando libres los de la izquierda para <b>emergencias y quitanieves</b>."),
        ("Agents can <b>make chains compulsory</b> (a snow spray does not count). If you don’t comply, you are <b>fined and the vehicle is immobilised</b>.",
         "Los agentes pueden <b>obligar a usar cadenas</b> (no sustituibles por sprays para nieve). Si no se cumple, se <b>sanciona y se inmoviliza el vehículo</b>."),
    ]))

    B.append(H3("4.3 Fog, wind and sun", "4.3 Niebla, viento y sol"))
    B.append(TABLE(
        [T("Weather", "Meteorología"), T("What to do", "Qué hacer")],
        [
            [T("<b>Fog</b> (also smoke or dust)", "<b>Niebla</b> (también humo o polvo)"),
             T("It cuts <b>visibility</b> and <b>grip</b> (the road gets slippery). Use the compulsory lights, <b>not main beam</b> (it reflects back: mirror effect), and the <b>fog light</b> if fitted and conditions require it; "
               "follow the <b>road markings, beacons and other vehicles’ lights</b>. <b>Slow down</b> to what you can see, <b>more distance</b>, <b>no overtaking</b>, and <b>stop riding</b> if visibility is almost nil.",
               "Reduce la <b>visibilidad</b> y la <b>adherencia</b> (calzada más deslizante). Alumbrado obligatorio, <b>sin luz de carretera</b> (efecto espejo), y la <b>antiniebla</b> si la moto la tiene y las condiciones lo exigen; "
               "guiarse por las <b>marcas viales, el balizamiento y las luces de otros</b>. <b>Reducir la velocidad</b> según el campo de visión, <b>más distancia</b>, <b>evitar adelantar</b> y <b>dejar de conducir</b> si la visibilidad es casi nula.")],
            [T("<b>Wind</b>", "<b>Viento</b>"),
             T("Dangerous from the <b>side</b> or in <b>gusts</b>: it can push you off your line or make you fall. <b>Motorcycles</b> (especially <b>with a passenger</b>), mopeds, bicycles and bulky vehicles suffer most. "
               "<b>Slow down</b>, <b>hold the handlebar firmly</b>, leaning into the wind, and take care with the <b>screen effect</b> (banks, buildings, tunnels, lorries that suddenly cut the wind). A headwind slows you; a tailwind pushes you.",
               "Peligroso <b>transversal</b> o a <b>ráfagas</b>: puede variar la trayectoria o provocar la caída. Los más afectados: <b>motocicletas</b> (sobre todo <b>con pasajero</b>), ciclomotores, bicicletas y vehículos voluminosos. "
               "<b>Reducir la velocidad</b>, <b>sujetar el manillar con firmeza</b>, contrarrestando el viento, y cuidado con el <b>efecto pantalla</b> (taludes, edificios, túneles, camiones que tapan el viento de golpe). De frente frena; por detrás empuja.")],
            [T("<b>Sun</b>", "<b>Sol</b>"),
             T("It can <b>dazzle</b>. Choose a good <b>departure time</b> (avoid sunrise and sunset); a <b>dark, clean, unscratched visor</b> or <b>sunglasses</b> — but <b>never</b> a dark visor or sunglasses <b>at night or in tunnels</b>; <b>moderate your speed</b>, and stop if you must.",
               "Puede <b>deslumbrar</b>. Elegir una <b>hora de salida</b> adecuada (evitar la salida y la puesta de sol); <b>visera oscura, limpia y sin rayar</b> o <b>gafas de sol</b>, pero <b>nunca</b> visera oscura ni gafas de sol <b>de noche ni en túneles</b>; <b>moderar la velocidad</b> y detenerse si hace falta.")],
        ],
        widths=["20%", "80%"],
    ))
    B.append(P(
        "Where strong crosswinds are frequent there is a <b>warning sign</b> (P-29, which does not show the wind’s side) and sometimes a <b>windsock</b>, which does show the <b>side and strength</b> of the wind.",
        "Donde sopla con frecuencia viento fuerte transversal hay una <b>señal de peligro</b> (P-29, que no indica el lado) y a veces una <b>manga de viento</b>, que sí indica el <b>lado y la intensidad</b> del viento."))

    # ---------------------------------------------------------------- 5. traps
    B.append(H2("5", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("More <b>accidents</b> in town, more <b>deaths</b> out of town; motorways and autovías are the <b>safest</b>.", "Más <b>accidentes</b> en ciudad, más <b>muertos</b> en carretera; autopistas y autovías son las <b>más seguras</b>."),
        ("Falling: <b>let go</b> of the controls, <b>slide, don’t roll</b>, and don’t get up until you have stopped.", "En una caída: <b>soltar</b> los mandos, <b>deslizarse, no rodar</b>, y no levantarse hasta haberse detenido."),
        ("Stopping distance = <b>reaction + braking</b>. Reaction time <b>≈ 0.75 s</b>. Braking distance: rain <b>×2</b>, snow or ice <b>×10</b>.", "Distancia de detención = <b>reacción + frenado</b>. Tiempo de reacción <b>≈ 0,75 s</b>. Frenado: lluvia <b>×2</b>, nieve o hielo <b>×10</b>."),
        ("Breaks: <b>every 2 hours or 200 km</b>, for <b>20–30 minutes</b>. The main cause of fatigue: <b>long rides without proper rests</b>.", "Descansos: <b>cada 2 horas o 200 km</b>, de <b>20 a 30 minutos</b>. Principal causa de fatiga: <b>conducir largos periodos sin descansar</b>."),
        ("Alcohol: <b>0.25</b> mg/l in air (0.5 g/l blood); first <b>2 years</b> and professionals <b>0.15</b> (0.3); <b>under 18: 0</b>. The only safe level is <b>0</b>.", "Alcohol: <b>0,25</b> mg/l en aire (0,5 g/l en sangre); <b>2 primeros años</b> y profesionales <b>0,15</b> (0,3); <b>menores: 0</b>. La única tasa segura es <b>0</b>."),
        ("Peak alcohol <b>30–90 minutes</b> after drinking; <b>nothing</b> fools the breathalyser.", "Pico de alcohol <b>entre 30 y 90 minutos</b> después de beber; <b>nada</b> engaña al etilómetro."),
        ("Second breath test: at least <b>10 minutes</b> after the first. Contrast analysis: <b>paid in advance</b>, refunded if negative.", "Segunda prueba: al menos <b>10 minutos</b> después de la primera. Análisis de contraste: <b>se paga antes</b> y se devuelve si es negativo."),
        ("Drugs: forbidden, except medicines <b>on prescription</b> that <b>don’t affect riding</b>; saliva test.", "Drogas: prohibidas, salvo medicamentos <b>con receta</b> que <b>no afecten a la conducción</b>; prueba salival."),
        ("Tyre pressure: check it <b>cold</b>; if hot, don’t let air out.", "Presión de los neumáticos: comprobarla <b>en frío</b>; si están calientes, no quitar aire."),
        ("Two brakes, one on each wheel; the <b>sidecar</b> wheel needs none. The front disc stops in fewer metres and delays <b>fading</b>.", "Dos frenos, uno en cada rueda; la del <b>sidecar</b> no lo necesita. El disco delantero frena en menos metros y retrasa el <b>fading</b>."),
        ("Helmet: <b>R22</b>, fastened, <b>full-face</b> recommended; replace it after a <b>hard knock</b>.", "Casco: <b>R22</b>, abrochado, <b>integral</b> recomendable; sustituirlo tras un <b>golpe fuerte</b>."),
        ("Gloves: compulsory <b>out of town</b>; closed shoes: <b>every road</b>; vest: <b>carried</b> on the motorcycle, worn when you get off on an interurban road.", "Guantes: obligatorios <b>en interurbanas</b>; calzado cerrado: <b>en todas las vías</b>; chaleco: <b>en la moto</b>, puesto al bajarse en una interurbana."),
        ("Rain: most dangerous with the <b>first drops</b>; no main beam; less pressure on the <b>front</b> brake. Low grip: cross it <b>upright</b>.", "Lluvia: más peligrosa con las <b>primeras gotas</b>; sin luz larga; menos presión en el freno <b>delantero</b>. Baja adherencia: pasar <b>enderezado</b>."),
        ("Snow on motorways: <b>no overtaking</b>, <b>right-hand lane</b>. Ice: the most dangerous, <b>×10</b>.", "Nieve en autopista: <b>prohibido adelantar</b>, <b>carril derecho</b>. Hielo: lo más peligroso, <b>×10</b>."),
    ]))

    # ---------------------------------------------------------------- 6. numbers
    B.append(H2("6", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Human factor in accidents", "Factor humano en los accidentes"), T("70–90 %", "70–90 %")],
            [T("Typical reaction time", "Tiempo de reacción habitual"), T("0.75 s (0.5–1 s)", "0,75 s (0,5–1 s)")],
            [T("Braking distance: rain / snow or ice", "Distancia de frenado: lluvia / nieve o hielo"), T("×2 / ×10", "×2 / ×10")],
            [T("Breaks", "Descansos"), T("every 2 h or 200 km, 20–30 min", "cada 2 h o 200 km, 20–30 min")],
            [T("Drowsiness peaks", "Horas de más somnolencia"), T("3–5 h and 14–16 h", "3–5 h y 14–16 h")],
            [T("Alcohol in air: general / first 2 years and professionals / under 18", "Alcohol en aire: general / 2 primeros años y profesionales / menores"), T("0.25 / 0.15 / 0 mg/l", "0,25 / 0,15 / 0 mg/l")],
            [T("Alcohol in blood: general / first 2 years and professionals / under 18", "Alcohol en sangre: general / 2 primeros años y profesionales / menores"), T("0.5 / 0.3 / 0 g/l", "0,5 / 0,3 / 0 g/l")],
            [T("Alcohol peak after drinking", "Pico de alcoholemia tras beber"), T("30–90 minutes", "30–90 minutos")],
            [T("Between the two breath tests", "Entre las dos pruebas de alcohol"), T("at least 10 minutes", "al menos 10 minutos")],
            [T("Alcohol fines: up to twice the limit / more", "Multas por alcohol: hasta el doble / más"), T("500 €, 4 points / 1,000 €, 6 points", "500 €, 4 puntos / 1.000 €, 6 puntos")],
            [T("Alcohol crime", "Delito de alcohol"), T("over 0.60 mg/l in air (1.2 g/l in blood)", "más de 0,60 mg/l en aire (1,2 g/l en sangre)")],
            [T("Braking devices on a motorcycle", "Dispositivos de frenado en la moto"), T("2: front and rear", "2: delantero y trasero")],
            [T("Moped helmets: certified ones allowed until", "Cascos de ciclomotor: certificados admitidos hasta"), T("1 October 2027", "1 de octubre de 2027")],
        ],
        widths=["56%", "44%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["im2", "fl1", "fl4", "sp3", "fa2", "al3", "al5", "lw2", "br2", "hm3", "ge2", "wt3"]


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
    ("Ley sobre Tráfico, Circulación de Vehículos a Motor y Seguridad Vial (RDL 6/2015), art. 14: alcohol and drugs (0.0 for under-18s)", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722"),
    ("Reglamento General de Circulación (RD 1428/2003), arts. 20–28 (alcohol and drug tests) and 118 (helmets and protective gear) — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Real Decreto 518/2026 (reform in force 1 October 2026: gloves, closed shoes, the vest on motorcycles, snow on motorways)", "https://www.boe.es/buscar/doc.php?id=BOE-A-2026-13889"),
    ("Reglamento General de Vehículos (RD 2822/1998), art. 12 (two braking devices on motorcycles) and Anexo XII (vest) — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-1999-1826"),
]

GLOSSARY = [
    ("siniestralidad · víctima mortal", "accident rate · fatality"),
    ("factor humano · vehículo · vía", "human · vehicle · road factor"),
    ("zigzaguear entre los vehículos", "weave between vehicles"),
    ("caída · deslizarse · rodar", "fall · slide · roll"),
    ("guardarraíl · barrera de seguridad", "guardrail · safety barrier"),
    ("sistema de protección para motoristas", "motorcyclist protection system (lower rail)"),
    ("tiempo / distancia de reacción", "reaction time / distance"),
    ("distancia de frenado · de detención", "braking · stopping distance"),
    ("fatiga · somnolencia · microsueño", "fatigue · drowsiness · microsleep"),
    ("tasa de alcoholemia · etilómetro", "blood alcohol level · breathalyser"),
    ("aire espirado · prueba salival", "exhaled air · saliva test"),
    ("análisis de contraste", "contrast (confirmatory) analysis"),
    ("inmovilización · precinto", "immobilisation · sealing off"),
    ("seguridad activa · pasiva", "active · passive safety"),
    ("banda de rodamiento · presión de inflado", "tread · tyre pressure"),
    ("pastillas · zapatas · disco · tambor", "pads · shoes · disc · drum"),
    ("fading", "brake fade"),
    ("casco integral · modular · jet", "full-face · modular · open-face helmet"),
    ("mentonera · pantalla · visera", "chin bar · visor · peak"),
    ("guantes de protección · calzado cerrado", "protective gloves · closed shoes"),
    ("chaleco reflectante de alta visibilidad", "high-visibility reflective vest"),
    ("adherencia · aquaplaning", "grip · aquaplaning"),
    ("efecto pantalla · manga de viento", "screen effect · windsock"),
    ("cadenas para nieve · quitanieves", "snow chains · snowplough"),
]
