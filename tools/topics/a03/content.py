# -*- coding: utf-8 -*-
"""Category A1/A2, Topic 3 content (speed), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Manual Permiso A1/A2, Tema 3: La velocidad). The wording and
two figures are original; three figures are shared with Category B, Topic 3. The rules come from the Ley sobre Tráfico
(RDL 6/2015, art. 21) and the Reglamento General de Circulación (RD 1428/2003, arts. 12, 45–50 and 55) as amended by
RD 1514/2018, RD 970/2020 and RD 518/2026, as they stand in November 2026.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import moto_speed_band, moto_limits, trailer_rule, urban_limits, pedestrian_risk


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Most questions are <b>numbers</b> for your family of vehicles: the <b>motorcycle</b> (120 and 90, minimums 60 and 45), the <b>three-wheeled vehicle and heavy quadricycle</b> (70, minimums 60 and 35), "
         "the <b>moped</b> (45), the urban limits (20, 30, 50, 80) and the <b>−10 %</b> when towing a trailer.",
         "Casi todas las preguntas son <b>números</b> de tu familia de vehículos: la <b>motocicleta</b> (120 y 90, mínimas 60 y 45), el <b>vehículo de tres ruedas y el cuatriciclo pesado</b> (70, mínimas 60 y 35), "
         "el <b>ciclomotor</b> (45), los límites urbanos (20, 30, 50, 80) y el <b>−10 %</b> con remolque."),
        ("The rest are <b>words</b>: <i>velocidad adecuada</i>, <i>inadecuada</i>, <i>excesiva</i>, <i>anormalmente reducida</i> and <i>exceso de velocidad</i>, "
         "plus the list of situations where you must slow down.",
         "El resto son <b>palabras</b>: velocidad adecuada, inadecuada, excesiva, anormalmente reducida y exceso de velocidad, "
         "más la lista de situaciones en las que hay que moderar la velocidad."),
        ("The sections follow the order of your A1/A2 course. <b>Category B, Topic 3</b> covers the same chapter for cars, buses, lorries and special vehicles.",
         "Los apartados siguen el orden de tu curso A1/A2. El <b>Tema 3 del permiso B</b> trata el mismo capítulo para turismos, autobuses, camiones y vehículos especiales."),
    ]))

    # ---------------------------------------------------------------- 1. concepts
    B.append(H2("1", "Speed concepts", "Conceptos relacionados con la velocidad"))
    B.append(FIG(moto_speed_band, "The limits mark the allowed range; the adequate speed is the one inside it that fits the conditions at that moment.",
                 "Los límites marcan el margen permitido; la velocidad adecuada es la que, dentro de él, encaja con las circunstancias del momento."))
    B.append(TABLE(
        [T("Term", "Término"), T("Meaning", "Significado")],
        [
            [T("<b>Maximum speed</b> (<i>velocidad máxima</i>)", "<b>Velocidad máxima</b>"),
             T("The <b>upper limit allowed</b> for your vehicle on the road you are on. Going above it is <b>speeding</b> (<i>exceso de velocidad</i>).",
               "<b>Límite superior permitido</b> en función del vehículo y de la vía. Superarlo es circular con <b>exceso de velocidad</b>.")],
            [T("<b>Minimum speed</b> (<i>velocidad mínima</i>)", "<b>Velocidad mínima</b>"),
             T("The <b>lower limit allowed</b> for your vehicle on that road.", "<b>Límite inferior permitido</b> en función del vehículo y de la vía.")],
            [T("<b>Adequate speed</b> (<i>velocidad adecuada</i>)", "<b>Velocidad adecuada</b>"),
             T("Speed <b>adapted to the circumstances</b> of each moment (limits, weather, your own state…) that lets you control the motorcycle in <b>any unforeseen event</b>.",
               "La <b>adaptada a las circunstancias</b> de cada momento (limitaciones, meteorología, factores del conductor…) que permite controlar el vehículo ante <b>cualquier imprevisto</b>.")],
        ],
        widths=["32%", "68%"],
    ))
    B.append(E(
        "Speeding vs too fast for the conditions", "Exceso de velocidad frente a velocidad excesiva",
        "<b>Exceso de velocidad</b> = above the <b>signed or generic limit</b>. <b>Velocidad excesiva</b> = above what the <b>circumstances</b> require, "
        "which can happen <b>inside the limit</b>.",
        "<b>Exceso de velocidad</b> = por encima del <b>límite</b> señalizado o genérico. <b>Velocidad excesiva</b> = por encima de lo que exigen las <b>circunstancias</b>, "
        "y puede darse <b>dentro del límite</b>.",
        tip=("A motorcycle at 100 km/h on an autopista in heavy snow: no exceso de velocidad, but velocidad excesiva.",
             "Una motocicleta a 100 km/h en autopista con mucha nieve: no hay exceso de velocidad, pero sí velocidad excesiva.")))

    # ---------------------------------------------------------------- 2. generic limits
    B.append(H2("2", "Generic speed limits", "Límites genéricos"))
    B.append(H3("2.1 Generic speeds on interurban roads (out of town)", "2.1 Velocidades genéricas en vías interurbanas (fuera de poblado)"))
    B.append(P(
        "Out of town the generic limit depends on the <b>type of vehicle</b> and the <b>type of road</b>. For speed, roads come in two groups: "
        "<b>autopistas and autovías</b>, and <b>vías para automóviles and carreteras convencionales</b>. Signs can lower these limits; they apply when no sign says otherwise.",
        "Fuera de poblado el límite genérico depende del <b>tipo de vehículo</b> y del <b>tipo de vía</b>. A efectos de velocidad, las vías forman dos grupos: "
        "<b>autopistas y autovías</b>, y <b>vías para automóviles y carreteras convencionales</b>. Las señales pueden rebajarlos; rigen si nada indica otra cosa."))
    B.append(FIG(moto_limits, "Each bar runs from the minimum to the maximum. On autopistas and autovías the minimum is 60 km/h; on the other roads, half the maximum.",
                 "Cada barra va de la mínima a la máxima. En autopistas y autovías la mínima es 60 km/h; en las demás vías, la mitad de la máxima."))
    B.append(TABLE(
        [T("Vehicle", "Vehículo"), T("Autopista and autovía<br>max · min", "Autopista y autovía<br>máx. · mín."),
         T("Vía para automóviles and carretera convencional<br>max · min", "Vía para automóviles y carretera convencional<br>máx. · mín.")],
        [
            [T("<b>Motorcycle</b>", "<b>Motocicleta</b>"), T("<b>120</b> · 60", "<b>120</b> · 60"), T("<b>90</b> · 45", "<b>90</b> · 45")],
            [T("<b>Three-wheeled vehicle</b> and <b>heavy quadricycle</b>", "<b>Vehículo de tres ruedas</b> y <b>cuatriciclo pesado</b>"), T("<b>70</b> · 60", "<b>70</b> · 60"), T("<b>70</b> · 35", "<b>70</b> · 35")],
            [T("<b>Cycles and mopeds</b> (and light quadricycles)", "<b>Ciclos y ciclomotores</b> (y cuatriciclos ligeros)"),
             T("<b>45</b>, only <b>bicycles</b> and only on <b>autovías</b>", "<b>45</b>, solo <b>bicicletas</b> y solo en <b>autovías</b>"),
             T("<b>45</b>, only on carreteras convencionales: they may not use vías para automóviles", "<b>45</b>, solo en carreteras convencionales: no pueden circular por vías para automóviles")],
        ],
        widths=["38%", "28%", "34%"],
    ))
    B.append(E(
        "Conventional roads with the two directions physically separated", "Carreteras convencionales con separación física de los dos sentidos",
        "The <b>road owner may</b> set a maximum of <b>100 km/h</b> for <b>motorcycles</b> (and cars and motorhomes up to 3,500 kg) on carreteras convencionales "
        "where a physical barrier separates the two directions. It is not automatic: it has to be set and signed.",
        "El <b>titular de la vía podrá</b> fijar un máximo de <b>100 km/h</b> para <b>motocicletas</b> (y turismos y autocaravanas de hasta 3.500 kg) en carreteras convencionales "
        "con <b>separación física</b> de los dos sentidos. No es automático: debe fijarse y señalizarse.",
        pills_=[T("up to 100 km/h", "hasta 100 km/h"), T("only if the owner sets it", "solo si lo fija el titular")]))
    B.append(BOX("key", "Three-wheeled vehicles: two cases in the Reglamento", "Vehículos de tres ruedas: dos casos en el Reglamento", [
        ("As a rule, three-wheeled vehicles and quadricycles have <b>70 km/h on any road</b> where they may circulate. This is the figure in your course and the usual exam answer.",
         "Como norma, a los vehículos de tres ruedas y cuatriciclos se les aplica <b>70 km/h en cualquier vía</b> donde puedan circular. Es la cifra de tu curso y la respuesta habitual del examen."),
        ("Three-wheeled vehicles that the rules <b>treat as motorcycles</b> (<i>asimilados a las motocicletas</i>) take the <b>motorcycle limits</b>: 120 and 90.",
         "Los vehículos de tres ruedas <b>asimilados a las motocicletas</b> tienen los <b>mismos límites que las motocicletas</b> de dos ruedas: 120 y 90."),
    ]))
    B.append(E(
        "Towing a trailer: −10 %", "Con remolque: −10 %",
        "Motorcycles, three-wheeled vehicles and mopeds may tow a trailer or semitrailer of <b>no more than 50 %</b> of the towing vehicle’s <b>unladen mass</b>, "
        "only <b>by day</b> with good visibility, with <b>nobody</b> in the trailer, and with their generic maximum <b>reduced by 10 %</b>. In towns, local bylaws apply.",
        "Las motocicletas, los vehículos de tres ruedas y los ciclomotores pueden arrastrar un remolque o semirremolque de <b>no más del 50 %</b> de la <b>masa en vacío</b> del vehículo tractor, "
        "solo <b>de día</b> y con buena visibilidad, <b>sin personas</b> en el remolque y <b>reduciendo un 10 %</b> su velocidad máxima genérica. En poblado, lo que digan las ordenanzas municipales.",
        pills_=[T("−10 %, not −10 km/h", "−10 %, no −10 km/h"), T("≤ 50 % unladen mass", "≤ 50 % de la masa en vacío")],
        tip=("Your course also lists cycles. Since 1 October 2026 bicycles have their own trailer rules and are no longer in this list.",
             "Tu curso incluye también los ciclos. Desde el 1 de octubre de 2026 las bicicletas tienen sus propias normas de remolque y ya no figuran en esta lista.")))
    B.append(FIG(trailer_rule, "The 10 % comes off the generic maximum for that vehicle on that road. The minimum stays the same.",
                 "El 10 % se resta de la máxima genérica de ese vehículo en esa vía. La mínima no cambia."))
    B.append(BOX("key", "Also remember", "Además", [
        ("On roads <b>without a paved surface</b> the maximum is <b>30 km/h</b>.", "En las vías <b>sin pavimentar</b> la velocidad máxima es de <b>30 km/h</b>."),
        ("There is <b>no extra 20 km/h</b> for overtaking: that allowance was removed on 21 March 2022.", "<b>No hay 20 km/h extra</b> para adelantar: esa posibilidad se suprimió el 21 de marzo de 2022."),
        ("<b>Since 1 October 2026</b>, to overtake <b>pedestrians, animals, mopeds, VMP or cyclists out of town</b> you must go <b>at least 20 km/h below</b> the road’s limit (Topic 5 of category B).",
         "<b>Desde el 1 de octubre de 2026</b>, para adelantar <b>fuera de poblado a peatones, animales, ciclomotores, VMP o ciclistas</b> hay que ir <b>al menos 20 km/h por debajo</b> del límite de la vía (Tema 5 del permiso B)."),
    ]))

    B.append(H3("2.2 Generic speeds on urban roads (in town)", "2.2 Velocidades genéricas en vías urbanas (dentro de poblado)"))
    B.append(FIG(urban_limits, "Inside a town the limit depends on the street, not on the vehicle. Urban autopistas and autovías also have a 60 km/h minimum.",
                 "Dentro de poblado el límite depende de la calle, no del vehículo. Las autopistas y autovías urbanas tienen además una mínima de 60 km/h."))
    B.append(TABLE(
        [T("Street", "Vía"), T("Generic limit", "Límite genérico")],
        [
            [T("<b>Single platform</b>: road and pavement at the same level (<i>plataforma única de calzada y acera</i>)", "<b>Plataforma única</b> de calzada y acera"), T("<b>20 km/h</b>", "<b>20 km/h</b>")],
            [T("<b>One lane per direction</b>", "<b>Único carril por sentido</b> de circulación"), T("<b>30 km/h</b>", "<b>30 km/h</b>")],
            [T("<b>Two or more lanes per direction</b> (bus and other reserved lanes don’t count)", "<b>Dos o más carriles por sentido</b> (los carriles bus y reservados no se cuentan)"), T("<b>50 km/h</b>", "<b>50 km/h</b>")],
            [T("<b>Travesía</b> (an interurban road through the town)", "<b>Travesía</b>"), T("<b>50 km/h</b>", "<b>50 km/h</b>")],
            [T("<b>Autopista and autovía</b> inside the town", "<b>Autopista y autovía</b> dentro de poblado"), T("<b>80 km/h</b> max · <b>60 km/h</b> min", "<b>80 km/h</b> máx. · <b>60 km/h</b> mín.")],
        ],
        widths=["66%", "34%"],
    ))
    B.append(P(
        "Signs can <b>lower</b> these limits on urban roads and travesías, or <b>raise</b> them on urban autopistas and autovías, <b>never above</b> the generic limit for that road out of town "
        "or for the type of vehicle. Exceptionally, a <b>one-lane-per-direction</b> street can be raised to <b>50 km/h at most</b>. "
        "Your course says travesías can also be raised: since May 2021 the Reglamento only allows <b>lowering</b> the travesía limit.",
        "Mediante señalización, estos límites pueden <b>rebajarse</b> en vías urbanas y travesías, o <b>ampliarse</b> en autopistas y autovías urbanas, <b>sin rebasar nunca</b> los genéricos de esas vías fuera de poblado "
        "ni los del tipo de vehículo. Excepcionalmente, una vía de <b>único carril por sentido</b> puede subirse hasta <b>50 km/h como máximo</b>. "
        "Tu curso dice que las travesías también pueden ampliarse: desde mayo de 2021 el Reglamento solo permite <b>rebajar</b> el límite de las travesías."))

    B.append(H3("2.3 Respect the generic limits", "2.3 Respetar los límites genéricos"))
    B.append(P(
        "Each limit rests on <b>technical criteria</b>: the road’s design speed, the acceptable congestion, traffic demand, the environmental impact… "
        "Their aim is that vehicles move with the <b>greatest safety and flow</b>.",
        "Detrás de cada límite hay <b>criterios técnicos</b>: la velocidad de diseño de la vía, el grado aceptable de congestión, la demanda de tráfico, el impacto ambiental… "
        "Su objetivo es que los vehículos se desplacen con la <b>máxima garantía de seguridad y fluidez</b>."))
    B.append(E(
        "Design speed (<i>velocidad de diseño</i>)", "Velocidad de diseño",
        "The <b>highest speed that can be kept</b> on a stretch of road, <b>in good conditions</b>, safely. Never exceed it: the road’s safety margins were calculated for it.",
        "La <b>máxima velocidad que puede mantenerse</b> en un tramo, <b>en condiciones favorables</b>, con seguridad. No debe superarse nunca: las condiciones de seguridad se calcularon para ella."))
    B.append(TABLE(
        [T("Why", "Por qué"), T("What it means", "Qué supone")],
        [
            [T("<b>Higher speed</b>", "<b>A mayor velocidad</b>"),
             T("The motorcycle is <b>harder to control</b> and needs <b>more metres to stop</b>. Injuries are more serious: crashes above <b>120 km/h</b> are usually fatal.",
               "Es <b>más difícil controlar el vehículo</b> y se recorren <b>más metros antes de detenerlo</b>. Aumenta la gravedad de las lesiones: a más de <b>120 km/h</b> los accidentes suelen ser mortales.")],
            [T("<b>Conventional roads</b> are more dangerous than autopistas and autovías", "<b>Carreteras convencionales</b> (más peligrosas) frente a autopistas y autovías (más seguras)"),
             T("Both <b>directions share</b> the road, usually one lane each, so you meet oncoming traffic; there are <b>junctions</b>; and they are <b>not fenced</b>, so a pedestrian or animal may cross.",
               "Los <b>dos sentidos van juntos</b>, normalmente con un carril cada uno, y hay tráfico de frente; tienen <b>intersecciones</b>; y <b>no están valladas</b>: puede cruzar un peatón o un animal.")],
            [T("<b>In towns</b> pedestrians share the space", "<b>En ciudad</b> los peatones comparten el espacio"),
             T("They have the same rights as vehicles and the risk of hitting one is high. Speed decides whether they survive.",
               "Tienen los mismos derechos que los vehículos y el riesgo de atropello es importante. La velocidad decide si sobreviven.")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(FIG(pedestrian_risk, "Your course: close to 50 % at 50 km/h, practically all at 80 km/h. Recent DGT material gives higher figures (about 80 % at 50 km/h). "
                                  "Every source agrees that at 80 km/h practically no pedestrian survives.",
                 "Tu curso: cerca del 50 % a 50 km/h y prácticamente todos a 80 km/h. Material reciente de la DGT da cifras más altas (en torno al 80 % a 50 km/h). "
                 "Todas las fuentes coinciden en que a 80 km/h prácticamente ningún peatón sobrevive."))

    # ---------------------------------------------------------------- 3. adequate speed
    B.append(H2("3", "Speed suited to the circumstances", "Velocidad adecuada a las circunstancias"))
    B.append(P(
        "Every rider must <b>respect the speed limits</b> and, on top of that, take into account their own <b>physical and mental condition</b>, the features and <b>state of the road</b>, "
        "the <b>vehicle</b> and its <b>load</b>, the <b>weather</b>, the environment and the traffic. The more of these there are at once, the more you adapt, so that you can always "
        "<b>stop within your field of vision</b> and before any obstacle.",
        "Todo conductor está obligado a <b>respetar los límites de velocidad</b> y a tener en cuenta, además, sus <b>condiciones físicas y psíquicas</b>, las características y el <b>estado de la vía</b>, "
        "del <b>vehículo</b> y de su <b>carga</b>, las condiciones <b>meteorológicas</b>, ambientales y de circulación. Cuantas más concurran, más hay que adecuar la velocidad, de manera que siempre "
        "pueda <b>detenerse dentro de los límites de su campo de visión</b> y ante cualquier obstáculo."))
    B.append(E(
        "Inadequate and excessive speed", "Velocidad inadecuada y velocidad excesiva",
        "Not adapting to the circumstances = <b>inadequate speed</b>. When it is <b>higher</b> than the circumstances require, it is <b>excessive speed</b> (<i>velocidad excesiva</i>): "
        "one of the <b>main causes of accidents</b>, and it makes a fatal outcome more likely.",
        "No adaptar la velocidad a las circunstancias = <b>velocidad inadecuada</b>. Cuando es <b>superior</b> a la que requieren las circunstancias, es <b>velocidad excesiva</b>: "
        "una de las <b>principales causas de accidente</b>, y aumenta la probabilidad de que sea mortal.",
        tip=("Example: a motorcycle at 100 km/h on an autopista is within the limits, but in heavy snow it is inadequate and excessive.",
             "Ejemplo: una motocicleta a 100 km/h en autopista está dentro de los límites, pero con mucha nieve es una velocidad inadecuada y excesiva.")))

    B.append(H3("3.1 When you must moderate your speed", "3.1 Situaciones en las que se debe moderar la velocidad"))
    B.append(P("Ride at a <b>moderate speed</b> and, if necessary, <b>stop</b>:", "Se circulará a <b>velocidad moderada</b> y, si fuera preciso, se <b>detendrá</b> el vehículo:"))
    B.append(TABLE(
        [T("Group", "Grupo"), T("Situations", "Situaciones")],
        [
            [T("<b>People and animals</b>", "<b>Personas y animales</b>"),
             T("Pedestrians or animals on the part of the road you use, or likely to step onto it, above all <b>children, elderly people, blind people</b> or others clearly impaired. "
               "Near <b>markets, schools</b> and places where children are likely. Approaching <b>cycles</b>, junctions, the surroundings of cycle routes and <b>cycle crossings</b>, "
               "and <b>pedestrian crossings not controlled</b> by traffic lights or agents. Stretches with <b>buildings opening directly</b> onto the road.",
               "Peatones o animales en la parte de la vía que se utiliza, o cuando pueda preverse su irrupción, sobre todo <b>niños, ancianos, invidentes</b> u otras personas manifiestamente impedidas. "
               "Cerca de <b>mercados, centros docentes</b> y lugares con presencia previsible de niños. Al aproximarse a <b>ciclos</b>, a intersecciones y a las proximidades de vías ciclistas y <b>pasos para ciclistas</b>, "
               "y a <b>pasos de peatones no regulados</b> por semáforo o agentes. En tramos con <b>edificios de inmediato acceso</b> a la vía.")],
            [T("<b>Other vehicles</b>", "<b>Otros vehículos</b>"),
             T("A <b>stopped bus</b>, above all <b>school transport</b>. <b>Out of town</b>: vehicles <b>immobilised</b> on the carriageway, <b>assistance vehicles</b> at work, "
               "and <b>cycles</b> on the carriageway or its shoulder.",
               "Un <b>autobús en situación de parada</b>, sobre todo si es de <b>transporte escolar</b>. <b>Fuera de poblado</b>: vehículos <b>inmovilizados</b> en la calzada, <b>vehículos de auxilio</b> prestando servicio "
               "y <b>ciclos</b> que circulan por ella o por su arcén.")],
            [T("<b>The road</b>", "<b>La vía</b>"),
             T("<b>Slippery</b> surface, or when you could <b>splash water, gravel</b> or other material onto others. <b>Level crossings</b> and <b>movable bridges</b>. <b>Roundabouts</b>. "
               "Junctions where you <b>do not have priority</b>, places with <b>reduced visibility</b> (bends, brows) and <b>narrowings</b>. Wherever <b>signs warn of danger</b>. "
               "When you <b>cannot pass oncoming vehicles</b> safely.",
               "<b>Pavimento deslizante</b>, o cuando pueda <b>salpicarse o proyectarse agua, gravilla</b> u otras materias. <b>Pasos a nivel</b> y <b>puentes móviles</b>. <b>Glorietas</b>. "
               "Intersecciones en las que <b>no se goce de prioridad</b>, lugares de <b>reducida visibilidad</b> (curvas, cambios de rasante) y <b>estrechamientos</b>. Cuando la <b>señalización advierta de un peligro</b>. "
               "Cuando no se pueda realizar el <b>cruce con otro vehículo</b> con seguridad.")],
            [T("<b>Seeing and being seen</b>", "<b>Visibilidad</b>"),
             T("<b>Dazzle</b>, to avoid hitting vehicles or pedestrians. <b>Dense fog, heavy rain, snowfall</b>, or clouds of <b>dust or smoke</b>.",
               "<b>Deslumbramiento</b>, para evitar el alcance de vehículos o peatones. <b>Niebla densa, lluvia intensa, nevada</b> o nubes de <b>polvo o humo</b>.")],
        ],
        widths=["20%", "80%"],
        cls="small",
    ))
    B.append(E(
        "Signed junction with almost no visibility", "Intersección señalizada sin apenas visibilidad",
        "If a junction is properly signed but the visibility is <b>practically nil</b>, vehicles may <b>not exceed 50 km/h</b>.",
        "Si las intersecciones están debidamente señalizadas y la visibilidad es <b>prácticamente nula</b>, la velocidad <b>no deberá exceder de 50 km/h</b>.",
        pills_=[T("≤ 50 km/h", "≤ 50 km/h")]))

    B.append(H3("3.2 Speed competitions", "3.2 Competiciones de velocidad"))
    B.append(E(
        "Racing on public roads", "Competiciones de velocidad",
        "<b>Racing</b> on public roads or roads open to the public is <b>prohibited</b>, unless the competent authority has <b>authorised</b> it and <b>closed off</b> the area for it. "
        "It is a <b>very serious</b> offence.",
        "Se <b>prohíbe</b> entablar <b>competiciones de velocidad</b> en vías públicas o de uso público, salvo que la autoridad competente conceda la <b>autorización</b> y se <b>acondicione</b> la zona. "
        "Es una infracción <b>muy grave</b>."))

    # ---------------------------------------------------------------- 4. minimum speed
    B.append(H2("4", "Minimum speed", "Velocidad mínima"))
    B.append(P(
        "Do not <b>hold up</b> other vehicles by riding at an <b>abnormally low speed</b> without good reason. Motor vehicles may <b>not</b> ride on <b>autopistas and autovías below 60 km/h</b>, "
        "nor on <b>other roads below half the generic maximum</b> for their category, <b>even if there is no other traffic</b>.",
        "No se deberá <b>entorpecer</b> la marcha normal de otro vehículo circulando sin causa justificada a <b>velocidad anormalmente reducida</b>. Se prohíbe circular en <b>autopistas y autovías</b> "
        "con vehículos a motor a <b>menos de 60 km/h</b>, y en las <b>restantes vías a menos de la mitad de la genérica</b> de cada categoría de vehículo, <b>aunque no circulen otros vehículos</b>."))
    B.append(TABLE(
        [T("Vehicle", "Vehículo"), T("Autopista and autovía", "Autopista y autovía"), T("Vía para automóviles and carretera convencional", "Vía para automóviles y carretera convencional")],
        [
            [T("Motorcycle", "Motocicleta"), T("<b>60</b> (half of 120)", "<b>60</b> (la mitad de 120)"), T("<b>45</b> (half of 90)", "<b>45</b> (la mitad de 90)")],
            [T("Three-wheeled vehicle, heavy quadricycle", "Vehículo de tres ruedas, cuatriciclo pesado"), T("<b>60</b> (the motorway minimum)", "<b>60</b> (la mínima de autopista)"), T("<b>35</b> (half of 70)", "<b>35</b> (la mitad de 70)")],
        ],
        widths=["36%", "30%", "34%"],
        cls="small",
    ))
    B.append(TABLE(
        [T("May ride below the minimum", "Pueden circular por debajo de la mínima")],
        [
            [T("<b>Cycles</b> and <b>animal-drawn</b> vehicles (Ley sobre Tráfico, art. 21.5)", "Los <b>ciclos</b> y los vehículos de <b>tracción animal</b> (Ley sobre Tráfico, art. 21.5)")],
            [T("<b>Special vehicles</b> and vehicles moving under <b>special-transport</b> rules", "Los <b>vehículos especiales</b> y los vehículos en régimen de <b>transporte especial</b>")],
            [T("Anyone, when <b>traffic, vehicle or road</b> conditions make a higher speed unsafe", "Cualquiera, cuando las circunstancias <b>del tráfico, del vehículo o de la vía</b> impidan mantener una velocidad superior sin riesgo")],
            [T("<b>Escort or protection vehicles</b>, matching the speed of the vehicle they accompany", "Los <b>vehículos de protección o acompañamiento</b>, adecuando su velocidad a la del acompañado")],
        ],
    ))
    B.append(BOX("key", "When you cannot keep up", "Cuando no se puede mantener la mínima", [
        ("If a vehicle <b>cannot reach the required minimum</b> and there is a risk of being <b>hit from behind</b>, it rides with its <b>hazard warning lights</b> on.",
         "Si un vehículo <b>no puede alcanzar la velocidad mínima</b> exigida y hay peligro de <b>alcance</b>, debe circular con la <b>luz o señal de emergencia</b>."),
        ("If an <b>emergency</b> forces you to ride on an <b>autopista or autovía</b> at an abnormally low speed, <b>leave it at the first exit</b>.",
         "Quien por <b>emergencia</b> deba circular por una <b>autopista o autovía</b> a velocidad anormalmente reducida debe <b>abandonarla por la primera salida</b>."),
    ]))

    # ---------------------------------------------------------------- 5. traps
    B.append(H2("5", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("<b>Exceso de velocidad</b> = over the limit. <b>Velocidad excesiva</b> = too fast for the conditions, even inside the limit.",
         "<b>Exceso de velocidad</b> = por encima del límite. <b>Velocidad excesiva</b> = demasiado rápido para las circunstancias, aunque sea dentro del límite."),
        ("Motorcycle on a <b>vía para automóviles</b>: same as a carretera convencional, <b>90</b> (min 45) — not 120.", "Moto por una <b>vía para automóviles</b>: igual que en carretera convencional, <b>90</b> (mín. 45), no 120."),
        ("Three-wheeled vehicle or heavy quadricycle: <b>70 on every road</b>; minimum 60 on autopistas, <b>35</b> on the rest.", "Vehículo de tres ruedas o cuatriciclo pesado: <b>70 en todas las vías</b>; mínima 60 en autopistas y <b>35</b> en las demás."),
        ("Mopeds: <b>45</b>, never on autopistas, autovías or vías para automóviles. Bicycles: autovías only, on the shoulder.", "Ciclomotores: <b>45</b>, nunca por autopistas, autovías ni vías para automóviles. Bicicletas: solo autovías, por el arcén."),
        ("Trailer: <b>−10 %</b> (per cent), not −10 km/h. A motorcycle: 108 on autopistas, 81 on conventional roads.", "Remolque: <b>−10 %</b> (por ciento), no −10 km/h. Una moto: 108 en autopista y 81 en convencional."),
        ("100 km/h on a separated conventional road only if the road owner sets it and it is signed.", "100 km/h en convencional con separación física solo si lo fija el titular y está señalizado."),
        ("In town the limit depends on the <b>street</b>: 20, 30 or 50; urban autopista 80 (min 60).", "En poblado el límite depende de la <b>calle</b>: 20, 30 o 50; autopista urbana 80 (mín. 60)."),
        ("Travesía: 50, and it can only be <b>lowered</b>.", "Travesía: 50, y solo puede <b>rebajarse</b>."),
        ("No extra 20 km/h to overtake. To overtake vulnerable users out of town: <b>20 km/h below</b> the limit.", "No hay 20 km/h extra para adelantar. Para adelantar a usuarios vulnerables fuera de poblado: <b>20 km/h por debajo</b> del límite."),
        ("Signed junction with practically nil visibility: <b>≤ 50 km/h</b>.", "Intersección señalizada con visibilidad prácticamente nula: <b>≤ 50 km/h</b>."),
        ("Minimum speed applies <b>even with no other traffic</b>.", "La mínima rige <b>aunque no circulen otros vehículos</b>."),
        ("Can’t reach the minimum and risk of being hit from behind: <b>hazard lights</b>. Emergency on an autopista: <b>first exit</b>.", "No alcanzas la mínima y hay peligro de alcance: <b>señal de emergencia</b>. Emergencia en autopista: <b>primera salida</b>."),
    ]))

    # ---------------------------------------------------------------- 6. numbers
    B.append(H2("6", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Motorcycle: autopista / autovía", "Motocicleta: autopista / autovía"), T("120 max · 60 min", "120 máx. · 60 mín.")],
            [T("Motorcycle: vía para automóviles / carretera convencional", "Motocicleta: vía para automóviles / convencional"), T("90 max · 45 min (100 if signed, separated roads)", "90 máx. · 45 mín. (100 si se señaliza, con separación física)")],
            [T("Three-wheeled vehicle, heavy quadricycle", "Vehículo de tres ruedas, cuatriciclo pesado"), T("70 · min 60 (autopista) or 35", "70 · mín. 60 (autopista) o 35")],
            [T("Moped, light quadricycle, cycle", "Ciclomotor, cuatriciclo ligero, ciclo"), T("45", "45")],
            [T("Towing a trailer", "Con remolque"), T("−10 % · trailer ≤ 50 % unladen mass", "−10 % · remolque ≤ 50 % de la masa en vacío")],
            [T("Unpaved roads", "Vías sin pavimentar"), T("30", "30")],
            [T("Urban: single platform / one lane / two or more lanes / travesía", "Urbana: plataforma única / un carril / dos o más / travesía"), T("20 / 30 / 50 / 50", "20 / 30 / 50 / 50")],
            [T("Urban autopista and autovía", "Autopista y autovía urbana"), T("80 max · 60 min", "80 máx. · 60 mín.")],
            [T("Signed junction, practically nil visibility", "Intersección señalizada, visibilidad prácticamente nula"), T("≤ 50", "≤ 50")],
            [T("Pedestrian hit (your course)", "Peatón atropellado (tu curso)"), T("50 km/h ≈ 50 % die · 80 km/h practically all", "50 km/h ≈ 50 % mueren · 80 km/h prácticamente todos")],
        ],
        widths=["54%", "46%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
QUIZ_IDS = ["co2", "ot1", "ot3", "ot6", "tr1", "ur1", "ur4", "wh2", "ad2", "md3", "mn1", "mn4"]


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
    ("Reglamento General de Circulación (RD 1428/2003), arts. 12.3, 45–50 and 55 — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Ley sobre Tráfico (RDL 6/2015), art. 21: speed limits and who may ride below the minimum", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722"),
    ("Real Decreto 518/2026 (BOE 26-06-2026): trailers on motorcycles and mopeds (art. 12), overtaking vulnerable users (art. 85), in force 1 October 2026", "https://www.boe.es/boe/dias/2026/06/26/pdfs/BOE-A-2026-13889.pdf"),
    ("Real Decreto 970/2020: urban speed limits (20, 30, 50), in force 11 May 2021", "https://www.boe.es/buscar/doc.php?id=BOE-A-2020-13969"),
]

GLOSSARY = [
    ("velocidad máxima / mínima", "maximum / minimum speed"),
    ("velocidad adecuada", "speed suited to the conditions"),
    ("velocidad inadecuada", "inappropriate speed"),
    ("velocidad excesiva", "too fast for the conditions"),
    ("exceso de velocidad", "speeding (over the limit)"),
    ("velocidad anormalmente reducida", "abnormally low speed"),
    ("velocidad de diseño", "design speed"),
    ("límite genérico", "default (generic) limit"),
    ("autopista · autovía", "motorway · dual carriageway (expressway)"),
    ("vía para automóviles", "motor road (no cycles or mopeds)"),
    ("carretera convencional", "ordinary (single-carriageway) road"),
    ("separación física de los dos sentidos", "physical barrier between the two directions"),
    ("vehículo de tres ruedas", "three-wheeled vehicle"),
    ("asimilado a motocicleta", "treated as a motorcycle"),
    ("cuatriciclo pesado / ligero", "heavy / light quadricycle"),
    ("remolque · semirremolque", "trailer · semitrailer"),
    ("masa en vacío", "unladen mass"),
    ("vía sin pavimentar", "unpaved road"),
    ("plataforma única de calzada y acera", "single-level street (road and pavement at one level)"),
    ("travesía", "stretch of an interurban road through a town"),
    ("atropello", "pedestrian being hit by a vehicle"),
    ("moderar la velocidad", "to slow down / ride at a moderate speed"),
    ("paso a nivel · puente móvil", "level crossing · movable bridge"),
    ("estrechamiento", "road narrowing"),
    ("deslumbramiento", "dazzle"),
    ("competición de velocidad", "speed race"),
    ("señal de emergencia", "hazard warning lights"),
]
