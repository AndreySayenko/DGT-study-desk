# -*- coding: utf-8 -*-
"""Topic 3 content (speed), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Tema 3: La velocidad). The wording and the figures are
original; the rules come from the Reglamento General de Circulación (RD 1428/2003, speed chapter, arts. 45–55) as
amended by RD 1514/2018, RD 970/2020 and RD 518/2026 (in force 1 October 2026), and DGT material.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import speed_band, limits_ranges, urban_limits, pedestrian_risk, v4_sign, slow_down


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Most questions are <b>numbers</b>: the generic limits for each vehicle and road (120, 100, 90, 80), the urban ones (20, 30, 50, 80), "
         "and the minimums (60 on motorways, half the maximum elsewhere).",
         "Casi todas las preguntas son <b>números</b>: los límites genéricos de cada vehículo y vía (120, 100, 90, 80), los urbanos (20, 30, 50, 80) "
         "y las mínimas (60 en autopistas y autovías, la mitad de la máxima en las demás vías)."),
        ("The rest are <b>words</b> the exam likes to swap: <i>velocidad adecuada</i>, <i>inadecuada</i>, <i>excesiva</i>, <i>anormalmente reducida</i> "
         "and <i>exceso de velocidad</i>, plus the list of situations where you must slow down.",
         "El resto son <b>palabras</b> que el examen intercambia: velocidad adecuada, inadecuada, excesiva, anormalmente reducida y exceso de velocidad, "
         "más la lista de situaciones en las que hay que moderar la velocidad."),
        ("The sections follow the order of your course’s Topic 3. Spanish exam terms are in <i>italics</i> in the English text, "
         "and a glossary closes the topic.",
         "Los apartados siguen el orden del Tema 3 de tu curso. Al final hay un glosario español–inglés."),
    ]))

    # ---------------------------------------------------------------- 1. concepts
    B.append(H2("1", "Speed concepts", "Conceptos relacionados con la velocidad"))
    B.append(FIG(speed_band, "The same road, five ideas. The limits mark the allowed range; the adequate speed is the one inside it that fits the conditions at that moment.",
                 "La misma vía, cinco ideas. Los límites marcan el margen permitido; la velocidad adecuada es la que, dentro de él, encaja con las circunstancias del momento."))
    B.append(TABLE(
        [T("Term", "Término"), T("Meaning", "Significado")],
        [
            [T("<b>Maximum speed</b> (<i>velocidad máxima</i>)", "<b>Velocidad máxima</b>"),
             T("The <b>upper limit allowed</b> for your vehicle on the road you are on. Going above it is <b>speeding</b> (<i>exceso de velocidad</i>).",
               "<b>Límite superior permitido</b> según el vehículo y la vía por la que se circula. Superarlo es circular con <b>exceso de velocidad</b>.")],
            [T("<b>Minimum speed</b> (<i>velocidad mínima</i>)", "<b>Velocidad mínima</b>"),
             T("The <b>lower limit allowed</b> for your vehicle on that road.", "<b>Límite inferior permitido</b> según el vehículo y la vía.")],
            [T("<b>Adequate speed</b> (<i>velocidad adecuada</i>)", "<b>Velocidad adecuada</b>"),
             T("Speed <b>adapted to the circumstances</b> of each moment (limits, weather, the driver’s state…) that lets you control the vehicle in <b>any unforeseen event</b>.",
               "La <b>adaptada a las circunstancias</b> de cada momento (límites, meteorología, factores del conductor…) que permite controlar el vehículo ante <b>cualquier imprevisto</b>.")],
            [T("<b>Inadequate speed</b> (<i>velocidad inadecuada</i>)", "<b>Velocidad inadecuada</b>"),
             T("When you do not take into account <b>all the factors</b> that affect driving. It <b>raises the risk of an accident</b>.",
               "Cuando no se tienen en cuenta <b>todos los factores</b> que afectan a la conducción. <b>Aumenta el riesgo de accidente</b>.")],
            [T("<b>Abnormally low speed</b> (<i>velocidad anormalmente reducida</i>)", "<b>Velocidad anormalmente reducida</b>"),
             T("<b>Below the minimum allowed</b>. It can hold up traffic and cause accidents.", "<b>Inferior a la mínima permitida</b>. Puede entorpecer la circulación y causar accidentes.")],
        ],
        widths=["32%", "68%"],
    ))
    B.append(E(
        "Speeding vs too fast for the conditions", "Exceso de velocidad frente a velocidad excesiva",
        "<b>Exceso de velocidad</b> = above the <b>signed or generic limit</b>. <b>Velocidad excesiva</b> = above what the <b>circumstances</b> require, "
        "which can happen <b>inside the limit</b>. It is a kind of inadequate speed and one of the main causes of accidents.",
        "<b>Exceso de velocidad</b> = por encima del <b>límite</b> señalizado o genérico. <b>Velocidad excesiva</b> = por encima de lo que exigen las <b>circunstancias</b>, "
        "y puede darse <b>dentro del límite</b>. Es una forma de velocidad inadecuada y una de las principales causas de accidente.",
        tip=("A car at 100 km/h on a motorway in heavy snow: no exceso de velocidad, but velocidad excesiva.",
             "Un turismo a 100 km/h en autopista con mucha nieve: no hay exceso de velocidad, pero sí velocidad excesiva.")))

    # ---------------------------------------------------------------- 2. generic limits
    B.append(H2("2", "Generic speed limits", "Límites genéricos de velocidad"))
    B.append(P(
        "Out of town the generic limit depends on <b>two things</b>: the <b>type of vehicle</b> and the <b>type of road</b>. For speed, roads come in two groups: "
        "<b>autopistas and autovías</b>, and <b>vías para automóviles and carreteras convencionales</b>. Signs can lower these limits; they are the default when no sign says otherwise.",
        "Fuera de poblado el límite genérico depende de <b>dos cosas</b>: el <b>tipo de vehículo</b> y el <b>tipo de vía</b>. A efectos de velocidad, las vías forman dos grupos: "
        "<b>autopistas y autovías</b>, y <b>vías para automóviles y carreteras convencionales</b>. Las señales pueden rebajarlos; son los que rigen si nada indica otra cosa."))
    B.append(FIG(limits_ranges, "Each bar runs from the minimum to the maximum. On motorways the minimum is 60 km/h for everyone; on the other roads it is half the maximum.",
                 "Cada barra va de la mínima a la máxima. En autopistas y autovías la mínima es 60 km/h para todos; en las demás vías, la mitad de la máxima."))
    B.append(TABLE(
        [T("Vehicle", "Vehículo"), T("Autopista and autovía<br>max · min", "Autopista y autovía<br>máx. · mín."),
         T("Vía para automóviles and carretera convencional<br>max · min", "Vía para automóviles y carretera convencional<br>máx. · mín.")],
        [
            [T("<b>Car, motorcycle</b>, motorhome with MMA up to 3,500 kg, <b>pick-up</b>", "<b>Turismo, motocicleta</b>, autocaravana de MMA hasta 3.500 kg, <b>pick-up</b>"),
             T("<b>120</b> · 60", "<b>120</b> · 60"), T("<b>90</b> · 45", "<b>90</b> · 45")],
            [T("<b>Bus</b>, car-derived van (<i>derivado de turismo</i>), adaptable mixed vehicle", "<b>Autobús</b>, derivado de turismo, vehículo mixto adaptable"),
             T("<b>100</b> · 60", "<b>100</b> · 60"), T("<b>90</b> · 45", "<b>90</b> · 45")],
            [T("<b>Lorry, van</b> (<i>furgoneta</i>), motorhome over 3,500 kg, vehicles <b>with a trailer</b> and the rest", "<b>Camión, furgoneta</b>, autocaravana de más de 3.500 kg, <b>remolques</b> y resto de vehículos"),
             T("<b>90</b> · 60", "<b>90</b> · 60"), T("<b>80</b> · 40", "<b>80</b> · 40")],
        ],
        widths=["46%", "27%", "27%"],
    ))
    B.append(E(
        "Conventional roads with the two directions physically separated", "Carreteras convencionales con separación física de los dos sentidos",
        "The <b>road owner may</b> set a maximum of <b>100 km/h</b> for <b>cars, motorcycles and motorhomes up to 3,500 kg</b> on carreteras convencionales "
        "where a physical barrier separates the two directions. It is not automatic: it has to be set and signed.",
        "El <b>titular de la vía podrá</b> fijar un máximo de <b>100 km/h</b> para <b>turismos, motocicletas y autocaravanas de MMA hasta 3.500 kg</b> en carreteras convencionales "
        "con <b>separación física</b> de los dos sentidos. No es automático: debe fijarse y señalizarse.",
        pills_=[T("up to 100 km/h", "hasta 100 km/h"), T("only if the owner sets it", "solo si lo fija el titular")]))
    B.append(E(
        "Unpaved roads", "Vías sin pavimentar",
        "On roads <b>without a paved surface</b> the maximum is <b>30 km/h</b>.",
        "En las <b>vías sin pavimentar</b> la velocidad máxima es de <b>30 km/h</b>.",
        pills_=[T("30 km/h", "30 km/h")]))

    B.append(H3("2.1 Generic limits in built-up areas", "2.1 Límites genéricos en vías urbanas (dentro de poblado)"))
    B.append(FIG(urban_limits, "Inside a town the limit depends on the street, not on the vehicle. Urban motorways also have a 60 km/h minimum.",
                 "Dentro de poblado el límite depende de la calle, no del vehículo. Las autopistas y autovías urbanas tienen además una mínima de 60 km/h."))
    B.append(TABLE(
        [T("Street", "Vía"), T("Generic limit", "Límite genérico")],
        [
            [T("<b>Single platform</b>: road and pavement at the same level (<i>plataforma única de calzada y acera</i>)", "<b>Plataforma única</b> de calzada y acera"), T("<b>20 km/h</b>", "<b>20 km/h</b>")],
            [T("<b>One lane per direction</b>", "<b>Único carril por sentido</b> de circulación"), T("<b>30 km/h</b>", "<b>30 km/h</b>")],
            [T("<b>Two or more lanes per direction</b>", "<b>Dos o más carriles por sentido</b>"), T("<b>50 km/h</b>", "<b>50 km/h</b>")],
            [T("<b>Travesía</b> (a main road through the town)", "<b>Travesía</b>"), T("<b>50 km/h</b>", "<b>50 km/h</b>")],
            [T("<b>Autopista and autovía</b> inside the town", "<b>Autopista y autovía</b> dentro de poblado"), T("<b>80 km/h</b> max · <b>60 km/h</b> min", "<b>80 km/h</b> máx. · <b>60 km/h</b> mín.")],
        ],
        widths=["66%", "34%"],
    ))
    B.append(P(
        "Signs can <b>lower</b> these limits on urban roads and travesías, or <b>raise</b> them on urban autopistas and autovías, "
        "but <b>never above</b> the generic limit for that kind of road out of town. The <b>travesía</b> limit can only be <b>lowered</b> (since May 2021); "
        "older material, your course included, still says it can be raised. Exceptionally, the authority may raise a <b>one-lane-per-direction</b> street "
        "to <b>50 km/h at most</b>, with specific signs.",
        "Mediante señalización, estos límites pueden <b>rebajarse</b> en vías urbanas y travesías, o <b>ampliarse</b> en autopistas y autovías urbanas, "
        "<b>sin rebasar nunca</b> los límites genéricos de esas vías fuera de poblado. El límite de las <b>travesías</b> solo puede <b>rebajarse</b> (desde mayo de 2021); "
        "material más antiguo, incluido tu curso, dice aún que puede ampliarse. Excepcionalmente, la autoridad puede subir una vía de <b>único carril por sentido</b> "
        "hasta <b>50 km/h como máximo</b>, con señalización específica."))

    B.append(H3("2.2 Limits for other vehicles", "2.2 Velocidades de otros vehículos"))
    B.append(TABLE(
        [T("Vehicle", "Vehículo"), T("Autopista and autovía", "Autopista y autovía"),
         T("Vía para automóviles and carretera convencional", "Vía para automóviles y carretera convencional"), T("Town and travesía", "Poblado y travesía")],
        [
            [T("<b>Dangerous goods</b> transport", "Transporte de <b>mercancías peligrosas</b>"), T("generic <b>− 10 km/h</b>", "genérica <b>− 10 km/h</b>"),
             T("generic <b>− 10 km/h</b>", "genérica <b>− 10 km/h</b>"), T("<b>40</b>", "<b>40</b>")],
            [T("<b>School and minors</b> transport", "Transporte <b>escolar y de menores</b>"), T("generic <b>− 10 km/h</b>", "genérica <b>− 10 km/h</b>"),
             T("generic <b>− 10 km/h</b>", "genérica <b>− 10 km/h</b>"), T("<b>50</b>", "<b>50</b>")],
            [T("<b>Cycles, mopeds</b> and vehicles for people with reduced mobility", "<b>Ciclos, ciclomotores</b> y vehículos para personas de movilidad reducida"),
             T("<b>45</b>, bicycles only and only on autovías", "<b>45</b>, solo bicicletas y solo en autovías"), T("<b>45</b> (conventional roads only)", "<b>45</b> (solo carreteras convencionales)"), T("<b>45</b>", "<b>45</b>")],
            [T("<b>Three-wheeled vehicles</b>, including heavy quadricycles", "<b>Vehículos de tres ruedas</b>, incluidos los cuadriciclos pesados"),
             T("<b>70</b>", "<b>70</b>"), T("<b>70</b>", "<b>70</b>"), T("<b>50</b>", "<b>50</b>")],
            [T("<b>Special vehicles</b> without brake lights, with a trailer, or two-wheeled tractors (<i>motocultores</i>)", "<b>Vehículos especiales</b> sin señalización de frenado, con remolque o motocultores"),
             T("not allowed", "no pueden"), T("<b>25</b> (conventional roads only)", "<b>25</b> (solo carreteras convencionales)"), T("<b>25</b>", "<b>25</b>")],
            [T("<b>Other special vehicles</b>", "<b>Restantes vehículos especiales</b>"),
             T("not allowed", "no pueden"), T("<b>40</b> (conventional roads only)", "<b>40</b> (solo carreteras convencionales)"), T("<b>40</b>", "<b>40</b>")],
            [T("Special vehicles able to exceed <b>60 km/h on the flat</b> that meet the vehicle regulations", "Especiales que superen <b>60 km/h en llano</b> y cumplan las normas reguladoras de los vehículos"),
             T("<b>70</b>", "<b>70</b>"), T("<b>70</b> (conventional roads only)", "<b>70</b> (solo carreteras convencionales)"), T("<b>50</b>", "<b>50</b>")],
        ],
        widths=["36%", "20%", "26%", "18%"],
        cls="small",
    ))
    B.append(P(
        "<b>− 10 km/h</b>: the maximum for that vehicle on that road drops by 10 km/h; the <b>minimum stays</b> the general one. "
        "“Conventional roads only” means these vehicles may not use a <i>vía para automóviles</i>.",
        "<b>− 10 km/h</b>: la máxima de ese vehículo en esa vía baja 10 km/h; la <b>mínima sigue siendo</b> la general. "
        "«Solo carreteras convencionales» significa que no pueden circular por vías para automóviles."))
    B.append(BOX("key", "Also remember", "Además", [
        ("<b>Cyclists</b> may go faster than their generic maximum on stretches where the road allows a higher speed.",
         "Los <b>ciclistas</b> pueden superar su velocidad máxima genérica en los tramos en que las circunstancias de la vía lo permitan."),
        ("<b>Motorcycles, three-wheeled vehicles and mopeds towing a trailer or semitrailer</b> reduce their maximum by <b>10 %</b> (per cent, not km/h). "
         "Since October 2026 bicycles have their own trailer rules and are no longer in this list.",
         "<b>Motocicletas, vehículos de tres ruedas y ciclomotores que arrastren remolque o semirremolque</b> reducen un <b>10 %</b> su velocidad máxima (por ciento, no km/h). "
         "Desde octubre de 2026 las bicicletas tienen sus propias normas de remolque y ya no figuran en esta lista."),
        ("A <b>bus</b> with <b>standing passengers</b> (where allowed) or <b>without seat belts</b>: <b>80 km/h</b> at most, on <b>any road out of town</b>.",
         "Un <b>autobús</b> con <b>pasajeros de pie</b> (si está autorizado) o <b>sin cinturones</b>: <b>80 km/h</b> como máximo, en <b>cualquier vía fuera de poblado</b>."),
        ("There is <b>no extra 20 km/h</b> for overtaking: that allowance was removed on 21 March 2022 (Ley 18/2021).",
         "<b>No hay 20 km/h extra</b> para adelantar: esa posibilidad se suprimió el 21 de marzo de 2022 (Ley 18/2021)."),
        ("<b>New since 1 October 2026:</b> to overtake <b>cyclists</b> on interurban roads you go <b>at least 20 km/h below</b> the road’s limit (the overtaking topic covers the gap and lane rules).",
         "<b>Novedad desde el 1 de octubre de 2026:</b> para adelantar a <b>ciclistas</b> en vías interurbanas hay que ir <b>al menos 20 km/h por debajo</b> del límite de la vía (el tema de adelantamientos trata la separación y el cambio de carril)."),
    ]))

    B.append(H3("2.3 Why the generic limits matter", "2.3 Respetar los límites genéricos"))
    B.append(P(
        "Each limit rests on <b>technical criteria</b>: the road’s design speed, the congestion that is acceptable, traffic demand, the environmental impact… "
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
             T("The vehicle is <b>harder to control</b> and needs <b>more metres to stop</b>. Injuries are more serious: crashes above <b>120 km/h</b> are usually fatal.",
               "Es <b>más difícil controlar el vehículo</b> y se recorren <b>más metros antes de detenerse</b>. Las lesiones son más graves: a más de <b>120 km/h</b> los accidentes suelen ser mortales.")],
            [T("<b>Conventional roads</b> are more dangerous than autopistas and autovías", "<b>Carreteras convencionales</b> (más peligrosas) frente a autopistas y autovías (más seguras)"),
             T("Both <b>directions share</b> the road, usually one lane each, so you meet oncoming traffic; there are <b>junctions</b>; and they are <b>not fenced</b>, so a pedestrian or animal can cross at any time.",
               "Los <b>dos sentidos van juntos</b>, normalmente con un carril cada uno, y hay tráfico de frente; tienen <b>intersecciones</b>; y <b>no están valladas</b>, así que puede cruzar un peatón o un animal.")],
            [T("<b>In towns</b> pedestrians share the space", "<b>En ciudad</b> los peatones comparten el espacio"),
             T("They have the same rights as vehicles, and the risk of hitting one is high. Speed decides whether they survive.",
               "Tienen los mismos derechos que los vehículos y el riesgo de atropello es importante. La velocidad decide si sobreviven.")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(FIG(pedestrian_risk, "Your course gives 15 % at 30 km/h and about 50 % at 50 km/h; recent DGT material gives 10 % and 80 %. "
                                  "Every source agrees that at 80 km/h practically no pedestrian survives.",
                 "Tu curso da un 15 % a 30 km/h y cerca del 50 % a 50 km/h; material reciente de la DGT da un 10 % y un 80 %. "
                 "Todas las fuentes coinciden en que a 80 km/h prácticamente ningún peatón sobrevive."))

    # ---------------------------------------------------------------- 3. prevailing speeds
    B.append(H2("3", "Speeds that take precedence", "Velocidades prevalentes"))
    B.append(P(
        "Over the maximum speeds above, these <b>prevail</b>: the limits set <b>by signs</b>; those set for certain <b>drivers</b> because of their <b>personal circumstances</b>; "
        "and those set for certain <b>vehicles</b> because of their <b>special features</b> or the <b>nature of their load</b>.",
        "Sobre las velocidades máximas indicadas <b>prevalecen</b> las que se fijen: a través de <b>señales</b>; a determinados <b>conductores</b> por sus <b>circunstancias personales</b>; "
        "y a determinados <b>vehículos</b> por sus <b>especiales características</b> o por la <b>naturaleza de su carga</b>."))
    B.append(FIG(v4_sign, "The V-4 plate goes at the back of the vehicle and shows the speed it must not exceed, whatever the road’s limit.",
                 "La señal V-4 va en la parte posterior del vehículo e indica la velocidad que no debe rebasar, sea cual sea el límite de la vía."))
    B.append(E(
        "V-4 speed-limitation plate", "Señal V-4 de limitación de velocidad",
        "When the limit is set for the <b>driver</b> or the <b>vehicle</b>, the vehicle carries the <b>V-4</b> plate <b>at the rear, always visible</b>. "
        "It shows the speed the vehicle <b>must not exceed</b>. If the road allows more, the V-4 still rules; if a sign sets less, the sign rules: the lowest applicable limit always wins.",
        "Cuando el límite se fija al <b>conductor</b> o al <b>vehículo</b>, este lleva la señal <b>V-4</b> en la <b>parte posterior, siempre visible</b>. "
        "Indica la velocidad que el vehículo <b>no debe rebasar</b>. Si la vía permite más, manda la V-4; si una señal fija menos, manda la señal: siempre rige el límite aplicable más bajo.",
        pills_=[T("rear, always visible", "detrás, siempre visible")]))

    # ---------------------------------------------------------------- 4. adequate speed
    B.append(H2("4", "Speed suited to the circumstances", "Velocidad adecuada a las circunstancias"))
    B.append(P(
        "Every driver must <b>respect the speed limits</b> and, on top of that, take into account their own <b>physical and mental condition</b>, the features and <b>state of the road</b>, "
        "the <b>vehicle</b> and its <b>load</b>, the <b>weather</b>, the environment and the traffic. The more of these there are at once, the more you adapt, so that you can always "
        "<b>stop within your field of vision</b> and before any obstacle that may appear.",
        "Todo conductor está obligado a <b>respetar los límites de velocidad</b> y a tener en cuenta, además, sus <b>condiciones físicas y psíquicas</b>, las características y el <b>estado de la vía</b>, "
        "del <b>vehículo</b> y de su <b>carga</b>, las condiciones <b>meteorológicas</b>, ambientales y de circulación. Cuantas más concurran, más hay que adecuar la velocidad, de manera que siempre "
        "pueda <b>detenerse dentro de los límites de su campo de visión</b> y ante cualquier obstáculo."))
    B.append(E(
        "Inadequate and excessive speed", "Velocidad inadecuada y velocidad excesiva",
        "Not adapting to the circumstances = <b>inadequate speed</b>. When it is <b>higher</b> than the circumstances require, it is <b>excessive speed</b> "
        "(<i>velocidad excesiva</i>): one of the <b>main causes of accidents</b>, and it makes a fatal outcome more likely.",
        "No adaptar la velocidad a las circunstancias = <b>velocidad inadecuada</b>. Cuando es <b>superior</b> a la que requieren las circunstancias, es <b>velocidad excesiva</b>: "
        "una de las <b>principales causas de accidente</b>, y aumenta la probabilidad de que sea mortal.",
        tip=("Example: 100 km/h on a motorway is within the limits, but in heavy snow it is inadequate and excessive.",
             "Ejemplo: 100 km/h en autopista está dentro de los límites, pero con mucha nieve es una velocidad inadecuada y excesiva.")))

    B.append(H3("4.1 When you must moderate your speed", "4.1 Situaciones en las que se debe moderar la velocidad"))
    B.append(P("Drive at a <b>moderate speed</b> and, if necessary, <b>stop</b>:", "Se circulará a <b>velocidad moderada</b> y, si fuera preciso, se <b>detendrá</b> el vehículo:"))
    B.append(TABLE(
        [T("Group", "Grupo"), T("Situations", "Situaciones")],
        [
            [T("<b>People and animals</b>", "<b>Personas y animales</b>"),
             T("Pedestrians or animals on the part of the road you use, or likely to step onto it, above all <b>children, elderly people, blind people</b> or others clearly impaired. "
               "Near <b>markets, schools</b> and places where children are likely. Approaching <b>cycles</b>, junctions and the surroundings of cycle routes and <b>cycle crossings</b>, "
               "and <b>pedestrian crossings not controlled</b> by traffic lights or agents. Stretches with <b>buildings opening directly</b> onto the road.",
               "Peatones o animales en la parte de la vía que se utiliza, o cuando pueda preverse su irrupción, sobre todo <b>niños, ancianos, invidentes</b> u otras personas manifiestamente impedidas. "
               "Cerca de <b>mercados, centros docentes</b> y lugares con presencia previsible de niños. Al aproximarse a <b>ciclos</b>, a intersecciones y a las proximidades de vías ciclistas y <b>pasos para ciclistas</b>, "
               "y a <b>pasos de peatones no regulados</b> por semáforo o agentes. En tramos con <b>edificios de inmediato acceso</b> a la vía.")],
            [T("<b>Other vehicles</b>", "<b>Otros vehículos</b>"),
             T("A <b>stopped bus</b>, above all <b>school transport</b>. <b>Out of town</b>: vehicles <b>immobilised</b> on the carriageway, <b>recovery and assistance vehicles</b> at work, "
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

    B.append(H3("4.2 Speed competitions and cycling events", "4.2 Competiciones de velocidad y marchas ciclistas"))
    B.append(E(
        "Speed competitions", "Competiciones de velocidad",
        "<b>Racing</b> on public roads or roads open to the public is <b>forbidden</b>, unless the competent authority <b>authorises</b> it and the area is <b>prepared</b> for it.",
        "Se <b>prohíbe</b> entablar <b>competiciones de velocidad</b> en vías públicas o de uso público, salvo que la autoridad competente lo <b>autorice</b> y se <b>acondicione</b> la zona."))
    B.append(E(
        "Organised cycling events", "Pruebas y marchas ciclistas organizadas",
        "Events with <b>more than 50 cyclists</b> need <b>prior authorisation</b> to use public roads, <b>whether on a holiday or not</b> and on <b>urban or interurban</b> roads. "
        "<b>Traffic agents</b> or the organisation’s <b>authorised staff</b> keep control and order. That staff acts as the agents’ <b>auxiliaries</b>, so their instructions "
        "carry the <b>same weight as an agent’s</b>.",
        "Las de <b>más de 50 ciclistas</b> necesitan <b>autorización previa</b> para circular por vías públicas, <b>sea festivo o no</b> y en vía <b>urbana o interurbana</b>. "
        "El control y orden corresponde a los <b>agentes de la autoridad</b> o al <b>personal habilitado</b> de la organización, que actúa como <b>auxiliar</b> de los agentes: "
        "sus órdenes tienen la <b>misma consideración</b> que las de los agentes.",
        pills_=[T("&gt; 50 cyclists", "&gt; 50 ciclistas"), T("prior authorisation", "autorización previa")]))

    # ---------------------------------------------------------------- 5. minimum speed
    B.append(H2("5", "Minimum speed", "Velocidad mínima"))
    B.append(P(
        "Do not <b>hold up</b> other vehicles by driving at an <b>abnormally low speed</b> without good reason. Motor vehicles may <b>not</b> drive on <b>autopistas and autovías below 60 km/h</b>, "
        "nor on <b>other roads below half the generic maximum</b> for their category, <b>even if there is no other traffic</b>.",
        "No se deberá <b>entorpecer</b> la marcha normal de otro vehículo circulando sin causa justificada a <b>velocidad anormalmente reducida</b>. Se prohíbe circular en <b>autopistas y autovías</b> "
        "con vehículos a motor a <b>menos de 60 km/h</b>, y en las <b>restantes vías a menos de la mitad de la genérica</b> de cada categoría de vehículo, <b>aunque no circulen otros vehículos</b>."))
    B.append(TABLE(
        [T("May drive below the minimum", "Pueden circular por debajo de la mínima")],
        [
            [T("<b>Cycles</b> and <b>animal-drawn</b> vehicles", "Los <b>ciclos</b> y los vehículos de <b>tracción animal</b>")],
            [T("<b>Special vehicles</b> and vehicles moving under <b>special-transport</b> rules", "Los <b>vehículos especiales</b> y los vehículos en régimen de <b>transporte especial</b>")],
            [T("Anyone, when <b>traffic, vehicle or road</b> conditions make a higher speed unsafe", "Cualquiera, cuando las circunstancias <b>del tráfico, del vehículo o de la vía</b> impidan mantener una velocidad superior sin riesgo")],
            [T("<b>Escort or protection vehicles</b>, matching the speed of the vehicle they accompany", "Los <b>vehículos de protección o acompañamiento</b>, adecuando su velocidad a la del acompañado")],
        ],
    ))
    B.append(BOX("key", "When you cannot keep up", "Cuando no se puede mantener la mínima", [
        ("If a vehicle <b>cannot reach the required minimum</b> and there is a risk of being <b>hit from behind</b>, it drives with its <b>hazard warning lights</b> on.",
         "Si un vehículo <b>no puede alcanzar la velocidad mínima</b> exigida y hay peligro de <b>alcance</b>, debe circular con la <b>luz o señal de emergencia</b>."),
        ("If an <b>emergency</b> forces you to drive on an <b>autopista or autovía</b> at an abnormally low speed, <b>leave it at the first exit</b>.",
         "Quien por <b>emergencia</b> deba circular por una <b>autopista o autovía</b> a velocidad anormalmente reducida debe <b>abandonarla por la primera salida</b>."),
    ]))

    B.append(H3("5.1 Slowing down", "5.1 Reducción de la velocidad"))
    B.append(FIG(slow_down, "Three steps before slowing down sharply: look, warn, then brake smoothly.",
                 "Tres pasos antes de reducir mucho la velocidad: mirar, avisar y frenar sin brusquedad."))
    B.append(TABLE(
        [T("Step", "Paso"), T("Rule", "Norma")],
        [
            [T("<b>1. Make sure</b>", "<b>1. Cerciorarse</b>"),
             T("Except in <b>imminent danger</b>, before reducing speed considerably check it is safe for others: watch in the <b>mirrors</b> the <b>distance and speed</b> of the vehicles behind.",
               "Salvo <b>peligro inminente</b>, antes de reducir considerablemente la velocidad hay que cerciorarse de que no hay riesgo: observar por los <b>espejos</b> la <b>distancia y velocidad</b> de los que vienen detrás.")],
            [T("<b>2. Warn</b>", "<b>2. Advertir</b>"),
             T("Whenever possible, warn in advance with <b>repeated use of the brake lights</b>, or by moving the <b>arm up and down</b> with <b>short, quick</b> movements.",
               "Siempre que sea posible, advertirlo previamente con el <b>empleo reiterado de las luces de frenado</b> o moviendo el <b>brazo alternativamente de arriba abajo</b> con movimientos <b>cortos y rápidos</b>.")],
            [T("<b>3. Brake smoothly</b>", "<b>3. Reducir sin brusquedad</b>"),
             T("Slow down <b>without sudden braking</b>, so that the vehicles behind are not at risk of hitting you.",
               "Reducir la velocidad <b>evitando brusquedades</b>, para no provocar riesgo de colisión con los vehículos que circulan detrás.")],
        ],
        widths=["24%", "76%"],
    ))

    # ---------------------------------------------------------------- 6. traps
    B.append(H2("6", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("<b>Exceso de velocidad</b> = over the limit. <b>Velocidad excesiva</b> = too fast for the conditions, even inside the limit.",
         "<b>Exceso de velocidad</b> = por encima del límite. <b>Velocidad excesiva</b> = demasiado rápida para las circunstancias, aunque sea dentro del límite."),
        ("<b>Abnormally low</b> speed means below the <b>minimum</b>, not just slow.", "Velocidad <b>anormalmente reducida</b> es inferior a la <b>mínima</b>, no simplemente lenta."),
        ("Car-derived vans and adaptable mixed vehicles go with <b>buses</b> (100 on motorways); <b>furgonetas</b> go with lorries (90).",
         "Los derivados de turismo y los mixtos adaptables van con los <b>autobuses</b> (100 en autopista); las <b>furgonetas</b>, con los camiones (90)."),
        ("Motorhomes: <b>up to 3,500 kg</b> like a car (120 / 90); <b>over 3,500 kg</b> like a lorry (90 / 80).",
         "Autocaravanas: <b>hasta 3.500 kg</b> como un turismo (120 / 90); <b>más de 3.500 kg</b> como un camión (90 / 80)."),
        ("A car <b>towing a trailer</b> drops to the lorry group: <b>90</b> on motorways, <b>80</b> on other roads.",
         "Un turismo <b>con remolque</b> pasa al grupo de los camiones: <b>90</b> en autopista, <b>80</b> en las demás vías."),
        ("Minimum: <b>60</b> on autopistas and autovías for every motor vehicle; elsewhere <b>half</b> the generic maximum (car 45, lorry 40), even with no traffic.",
         "Mínima: <b>60</b> en autopistas y autovías para todo vehículo a motor; en las demás, la <b>mitad</b> de la genérica (turismo 45, camión 40), aunque no haya tráfico."),
        ("The <b>100 km/h</b> on conventional roads exists only where the directions are <b>physically separated</b> and the <b>road owner</b> sets it.",
         "Los <b>100 km/h</b> en convencional solo existen con <b>separación física</b> de sentidos y si lo fija el <b>titular de la vía</b>."),
        ("Towing a trailer with a motorcycle, moped, three-wheeler or cycle: <b>− 10 %</b>. Dangerous goods and school transport: <b>− 10 km/h</b>.",
         "Moto, ciclomotor, tres ruedas o ciclo con remolque: <b>− 10 %</b>. Mercancías peligrosas y transporte escolar: <b>− 10 km/h</b>."),
        ("Bus with <b>standing passengers</b> or <b>no seat belts</b>: <b>80</b> on any road out of town.",
         "Autobús con <b>pasajeros de pie</b> o <b>sin cinturones</b>: <b>80</b> en cualquier vía fuera de poblado."),
        ("Signed junction with <b>practically nil</b> visibility: <b>50 km/h</b> at most.", "Intersección señalizada con visibilidad <b>prácticamente nula</b>: <b>50 km/h</b> como máximo."),
        ("Cycling events need authorisation from <b>more than 50</b> cyclists, holiday or not, urban or interurban.",
         "Las marchas ciclistas necesitan autorización a partir de <b>más de 50</b> ciclistas, sea festivo o no, en vía urbana o interurbana."),
        ("Overtaking gives <b>no extra 20 km/h</b>; overtaking a <b>cyclist</b> on an interurban road now means going <b>20 km/h below</b> the limit.",
         "Adelantar <b>no da 20 km/h extra</b>; adelantar a un <b>ciclista</b> en vía interurbana obliga ahora a ir <b>20 km/h por debajo</b> del límite."),
        ("Emergency at low speed on a motorway: <b>leave at the first exit</b>; can’t reach the minimum and risk being hit: <b>hazard lights</b>.",
         "Emergencia a baja velocidad en autopista: <b>salir por la primera salida</b>; sin alcanzar la mínima y con peligro de alcance: <b>luz de emergencia</b>."),
    ]))

    # ---------------------------------------------------------------- 7. key numbers
    B.append(H2("7", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Car, motorcycle, motorhome ≤ 3,500 kg, pick-up", "Turismo, moto, autocaravana ≤ 3.500 kg, pick-up"), T("120 / 90 (max) · 60 / 45 (min)", "120 / 90 (máx.) · 60 / 45 (mín.)")],
            [T("Bus, car-derived van, adaptable mixed", "Autobús, derivado de turismo, mixto adaptable"), T("100 / 90 · 60 / 45", "100 / 90 · 60 / 45")],
            [T("Lorry, van, motorhome &gt; 3,500 kg, with trailer", "Camión, furgoneta, autocaravana &gt; 3.500 kg, con remolque"), T("90 / 80 · 60 / 40", "90 / 80 · 60 / 40")],
            [T("Conventional road with separated directions (if signed)", "Convencional con separación física (si se fija)"), T("up to 100", "hasta 100")],
            [T("Unpaved road", "Vía sin pavimentar"), T("30", "30")],
            [T("Town: single platform · one lane per direction · 2+ lanes · travesía", "Poblado: plataforma única · un carril por sentido · 2 o más · travesía"), T("20 · 30 · 50 · 50", "20 · 30 · 50 · 50")],
            [T("Urban autopista / autovía", "Autopista / autovía urbana"), T("80 max · 60 min", "80 máx. · 60 mín.")],
            [T("Raising a one-lane-per-direction street", "Subir una vía de un carril por sentido"), T("50 at most", "50 como máximo")],
            [T("Dangerous goods · school transport (out of town / in town)", "Mercancías peligrosas · escolar (fuera / dentro de poblado)"), T("− 10 km/h / 40 · − 10 km/h / 50", "− 10 km/h / 40 · − 10 km/h / 50")],
            [T("Cycles, mopeds, reduced-mobility vehicles", "Ciclos, ciclomotores, vehículos de movilidad reducida"), T("45", "45")],
            [T("Three-wheeled vehicles, heavy quadricycles", "Tres ruedas, cuadriciclos pesados"), T("70 · 70 · 50 in town", "70 · 70 · 50 en poblado")],
            [T("Special vehicles: no brake lights / with trailer · the rest · able to exceed 60", "Especiales: sin señal de frenado / con remolque · resto · que superan 60"), T("25 · 40 · 70 (50 in town)", "25 · 40 · 70 (50 en poblado)")],
            [T("Motorcycle, moped, three-wheeler or cycle with trailer", "Moto, ciclomotor, tres ruedas o ciclo con remolque"), T("− 10 %", "− 10 %")],
            [T("Bus with standing passengers or no belts (out of town)", "Autobús con pasajeros de pie o sin cinturones (fuera de poblado)"), T("80", "80")],
            [T("Signed junction, visibility practically nil", "Intersección señalizada, visibilidad prácticamente nula"), T("≤ 50", "≤ 50")],
            [T("Cycling event needing authorisation", "Marcha ciclista que necesita autorización"), T("&gt; 50 cyclists", "&gt; 50 ciclistas")],
            [T("Overtaking a cyclist on an interurban road (since Oct 2026)", "Adelantar a un ciclista en vía interurbana (desde oct. 2026)"), T("limit − 20 km/h at least", "límite − 20 km/h como mínimo")],
            [T("Pedestrian hit at 30 · 50 · 80 km/h: chance of dying", "Peatón atropellado a 30 · 50 · 80 km/h: probabilidad de morir"), T("10–15 % · 50–80 % · almost 100 %", "10–15 % · 50–80 % · casi 100 %")],
        ],
        widths=["58%", "42%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["cn5", "gn3", "gn7", "ur2", "ur5", "ov1", "ex1", "pv6", "md2", "rc2", "mn3", "sl2"]


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
    ("Reglamento General de Circulación (RD 1428/2003), speed chapter (arts. 45–55) — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Real Decreto 1514/2018: generic limits out of town (90 km/h on conventional roads)", "https://www.boe.es/eli/es/rd/2018/12/28/1514"),
    ("Ley 18/2021: end of the extra 20 km/h for overtaking (from 21 March 2022)", "https://www.boe.es/eli/es/l/2021/12/20/18"),
    ("Real Decreto 970/2020: urban limits of 20, 30 and 50 km/h", "https://www.boe.es/eli/es/rd/2020/11/10/970"),
    ("Ley sobre Tráfico, Circulación de Vehículos a Motor y Seguridad Vial (RDL 6/2015)", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722"),
    ("DGT press release, 30-09-2026: the Reglamento reform (RD 518/2026) comes into force, including overtaking cyclists",
     "https://www.dgt.es/comunicacion/notas-de-prensa/20260930-reforma-del-reglamento-de-circulacion-usuarios-vulnerables/"),
    ("DGT, 16-05-2025: pedestrians hit on crossings (death risk at 30 and 50 km/h)", "https://www.dgt.es/comunicacion/noticias/20250516-atropellos-en-pasos-de-peatones"),
    ("Revista DGT, 2017: speed and vulnerable road users (report)", "https://revista.dgt.es/Galerias/noticia/nacional/2017/05MAYO/INFORME-VELOCIDAD-Y-COLECTIVOS-VULNERABLES.pdf"),
]

GLOSSARY = [
    ("velocidad máxima · velocidad mínima", "maximum speed · minimum speed"),
    ("velocidad adecuada · inadecuada", "appropriate · inappropriate speed"),
    ("velocidad excesiva", "speed too high for the conditions"),
    ("exceso de velocidad", "speeding (over the limit)"),
    ("velocidad anormalmente reducida", "abnormally low speed"),
    ("límites genéricos", "default (generic) speed limits"),
    ("velocidad de diseño", "design speed"),
    ("velocidades prevalentes", "limits that take precedence"),
    ("señal V-4", "speed-limitation plate (rear of the vehicle)"),
    ("plataforma única de calzada y acera", "shared street with road and pavement at one level"),
    ("travesía", "main road through a town"),
    ("vehículo derivado de turismo · vehículo mixto adaptable", "car-derived van · adaptable mixed vehicle"),
    ("furgoneta · autocaravana", "van · motorhome"),
    ("vehículo especial · motocultor", "special vehicle · two-wheeled (walking) tractor"),
    ("cuadriciclo pesado", "heavy quadricycle"),
    ("mercancías peligrosas · transporte escolar", "dangerous goods · school transport"),
    ("remolque · semirremolque", "trailer · semitrailer"),
    ("titular de la vía", "road owner (authority in charge of the road)"),
    ("pavimento deslizante", "slippery surface"),
    ("deslumbramiento", "dazzle"),
    ("paso a nivel · puente móvil", "level crossing · movable bridge"),
    ("estrechamiento", "narrowing"),
    ("vehículo inmovilizado · vehículo de auxilio", "immobilised vehicle · recovery or assistance vehicle"),
    ("competición de velocidad · marcha ciclista", "speed race · organised cycling event"),
    ("transporte especial · vehículo de acompañamiento", "special transport · escort vehicle"),
    ("luz o señal de emergencia", "hazard warning lights"),
    ("alcance", "rear-end collision"),
    ("luces de frenado", "brake lights"),
]
