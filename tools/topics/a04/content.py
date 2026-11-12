# -*- coding: utf-8 -*-
"""Category A1/A2, Topic 4 content (priority), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Manual Permiso A1/A2, Tema 4: La prioridad). The wording and
two figures are original; seven figures are shared with Category B, Topic 4. The rules come from the Ley sobre Tráfico
(RDL 6/2015, art. 25) and the Reglamento General de Circulación (RD 1428/2003, arts. 32 and 56–69) as amended by
RD 465/2025 and RD 518/2026, as they stand in November 2026.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import (priority_signs, right_rule, blocking_box, vulnerable_turn, narrowing, narrow_order,
                       emergency_signals, corridor, police_stop)


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Who goes first. At a junction the answer comes from the <b>signs</b> if there are any; if not, from the <b>right-hand rule</b> "
         "and its <b>four exceptions</b> (paved road, rails, roundabouts, autopistas and autovías).",
         "Quién pasa primero. En una intersección la respuesta la dan las <b>señales</b> si las hay; si no, la <b>regla de la derecha</b> "
         "y sus <b>cuatro excepciones</b> (vía pavimentada, raíles, glorietas, autopistas y autovías)."),
        ("Then pedestrians, cyclists and animals, <b>narrow stretches</b> — where a motorcycle comes <b>last</b> in the order — and emergency vehicles.",
         "Después, peatones, ciclistas y animales, los <b>estrechamientos</b> (donde la moto va <b>la última</b> en el orden) y los vehículos de urgencia."),
        ("New since your course was written: the <b>police signal to stop</b> (red light flashing forward, July 2025) and, since October 2026, pedestrian priority on "
         "<b>single-platform streets</b>. Since then motorcyclists also count, by law, as <b>vulnerable road users</b>.",
         "Novedades posteriores a tu curso: la <b>orden de detención de la policía</b> (luz roja intermitente hacia delante, julio de 2025) y, desde octubre de 2026, la prioridad del peatón en "
         "<b>zonas de plataforma única</b>. Desde entonces los motoristas también son, por ley, <b>usuarios vulnerables</b>."),
    ]))

    # ---------------------------------------------------------------- 1. junctions
    B.append(H2("1", "Priority at junctions", "Prioridad en intersecciones"))
    B.append(P(
        "<b>Priority</b> (<i>prioridad</i> or <i>preferencia de paso</i>) is the <b>right to go before</b> another road user at a junction or wherever your paths cross. "
        "A <b>junction</b> (<i>intersección</i>) is a point of the road network where all the possible crossings of vehicle paths happen <b>at the same level</b>.",
        "La <b>prioridad o preferencia de paso</b> es el <b>derecho a pasar antes</b> que otro usuario en las intersecciones o cuando se cruzan sus trayectorias. "
        "Una <b>intersección</b> es el nudo de la red viaria en el que todos los cruces de trayectorias posibles de los vehículos se realizan <b>a nivel</b>."))

    B.append(H3("1.1 Junctions with signs", "1.1 Intersecciones señalizadas"))
    B.append(FIG(priority_signs, "Simplified drawings. In the P-1 signs the thick line is the road you are on, which has priority; the thin one is the road that gives way to you.",
                 "Dibujos simplificados. En las señales P-1, la línea gruesa es la vía por la que circulas, que tiene prioridad; la fina, la que te cede el paso."))
    B.append(P(
        "At junctions priority always follows the signs that regulate it: <b>agents’ signals, traffic lights, vertical signs or road markings</b>.",
        "En las intersecciones la preferencia de paso se verifica siempre ateniéndose a la señalización que la regule: <b>señales de los agentes, semáforos, señales verticales o marcas viales</b>."))
    B.append(E(
        "Junction with a give-way or STOP sign", "Intersección con «ceda el paso» o «stop»",
        "You <b>always give way</b> to vehicles on the priority road, <b>whichever side they come from</b>, stopping completely when necessary, and <b>always</b> at a STOP. "
        "You stop <b>at the stop line</b> or, if there is none, <b>immediately before the junction</b>; if you still cannot see, <b>stop again</b> where you can, without endangering anyone.",
        "Se <b>cede siempre el paso</b> a los vehículos de la vía preferente, <b>cualquiera que sea el lado por el que se aproximen</b>, deteniéndose cuando sea preciso y, en todo caso, en el stop. "
        "La detención se hace <b>ante la línea de detención</b> o, si no existe, <b>inmediatamente antes de la intersección</b>; si aun así no se ve, hay que <b>detenerse de nuevo</b> donde se vea, sin poner en peligro a nadie.",
        pills_=[T("any side", "cualquier lado"), T("STOP = always stop", "STOP = detención siempre")],
        tip=("If signals disagree, the order is: agents → temporary signs → traffic lights → vertical signs → road markings.",
             "Si las señales se contradicen, el orden es: agentes → señalización circunstancial → semáforos → señales verticales → marcas viales.")))

    B.append(H3("1.2 Junctions without signs", "1.2 Intersecciones sin señalizar"))
    B.append(P(
        "When no sign regulates priority, you must <b>give way to vehicles approaching from your right</b>. This general rule has <b>four exceptions</b>:",
        "Cuando no hay señal que regule la preferencia de paso, el conductor está obligado a <b>cederla a los vehículos que se aproximen por su derecha</b>. "
        "Esta norma general tiene <b>cuatro excepciones</b>:"))
    B.append(TABLE(
        [T("Exception", "Excepción"), T("Who goes first", "Quién pasa primero")],
        [
            [T("<b>Paved vs unpaved</b>", "<b>Pavimentada frente a sin pavimentar</b>"), T("Vehicles on a <b>paved road</b>, over those coming from an <b>unpaved</b> one.", "Los que circulen por una <b>vía pavimentada</b>, frente a los que vengan de otra <b>sin pavimentar</b>.")],
            [T("<b>Rails</b>", "<b>Raíles</b>"), T("Vehicles running on <b>rails</b>, over all other road users.", "Los vehículos que circulen sobre <b>raíles</b>, sobre los demás usuarios.")],
            [T("<b>Roundabouts</b>", "<b>Glorietas</b>"), T("Vehicles <b>already in</b> the ring, over those wanting to <b>enter</b>.", "Los que se hallen <b>dentro</b> de la vía circular, sobre los que pretendan <b>acceder</b>.")],
            [T("<b>Autopistas and autovías</b>", "<b>Autopistas y autovías</b>"), T("Vehicles <b>on</b> the road, over those wanting to <b>join</b> it.", "Los que <b>circulen por</b> ella, sobre los que pretendan <b>acceder</b>.")],
        ],
        widths=["32%", "68%"],
    ))
    B.append(FIG(right_rule, "Left: each vehicle gives way to the one on its right, so they go 1, 2, 3. Right: one of the exceptions overrides the right-hand rule.",
                 "Izquierda: cada uno cede al que tiene a su derecha, así que pasan 1, 2 y 3. Derecha: una de las excepciones se impone a la regla de la derecha."))

    B.append(H3("1.3 How to act", "1.3 Normas de actuación"))
    B.append(TABLE(
        [T("You…", "Si…"), T("Rule", "Norma")],
        [
            [T("<b>must give way</b>", "<b>debes ceder el paso</b>"),
             T("Do not start, continue or resume your ride or manoeuvre until you are sure you will <b>not force</b> the rider or driver with priority to change "
               "<b>path or speed</b> abruptly. Show it <b>early</b> by the way you ride, above all by <b>slowing down gradually</b>.",
               "No inicies, continúes ni reemprendas la marcha o la maniobra hasta asegurarte de que <b>no obligas</b> al que tiene prioridad a modificar bruscamente su "
               "<b>trayectoria o su velocidad</b>. Demuéstralo <b>con antelación</b> con tu forma de circular, sobre todo con la <b>reducción paulatina de la velocidad</b>.")],
            [T("<b>have priority</b>", "<b>tienes prioridad</b>"),
             T("Even so, do <b>not enter</b> a junction, a <b>pedestrian crossing</b> or a <b>cycle crossing</b> if traffic is such that you will probably <b>stop inside it</b> "
               "and block the cross traffic.",
               "Aun así, <b>no penetres</b> en una intersección, un <b>paso para peatones</b> o un <b>paso para ciclistas</b> si, por la situación del tráfico, previsiblemente "
               "<b>quedarás detenido</b> obstruyendo la circulación transversal.")],
            [T("are <b>stuck inside</b> a junction with traffic lights", "has quedado <b>detenido dentro</b> de una intersección con semáforo"),
             T("If you block traffic, <b>leave</b> it <b>without waiting</b> for your light to allow your direction, as long as you do not hinder those moving with a green light.",
               "Si constituyes un obstáculo, <b>sal</b> de ella <b>sin esperar</b> a que se permita la circulación en tu dirección, siempre que no entorpezcas a los que avanzan en el sentido permitido.")],
        ],
        widths=["26%", "74%"],
    ))
    B.append(FIG(blocking_box, "A yellow criss-cross grid marks a box you must not enter if you might have to stop inside it.",
                 "La cuadrícula amarilla marca una zona en la que no se debe entrar si se puede quedar detenido dentro."))

    # ---------------------------------------------------------------- 2. pedestrians, cyclists and animals
    B.append(H2("2", "Pedestrians, cyclists and animals", "Peatones, ciclistas y animales"))
    B.append(P(
        "As a <b>general rule</b>, whenever your paths cross, drivers have priority for their vehicles <b>on the carriageway and the hard shoulder</b>, <b>except</b> in these cases, "
        "where you let them go first, <b>stopping if necessary</b>:",
        "Como <b>norma general</b>, siempre que sus trayectorias se corten, los conductores tienen prioridad de paso para sus vehículos <b>en la calzada y en el arcén</b>, <b>salvo</b> en estos casos, "
        "en los que hay que dejarlos pasar, <b>llegando a detenerse</b> si es necesario:"))
    B.append(TABLE(
        [T("They go first…", "Pasan primero…")],
        [
            [T("On properly signed <b>pedestrian crossings</b>, <b>cycle crossings</b> and <b>cañadas</b> (livestock routes); and on <b>pavements</b> and pedestrian zones.",
               "En los <b>pasos para peatones</b>, <b>pasos para ciclistas</b> y <b>cañadas</b> debidamente señalizados; y en <b>aceras</b> y zonas peatonales.")],
            [T("When you <b>turn into another road</b> and pedestrians, cyclists or animals are <b>crossing</b> it, <b>even if there is no crossing</b> for them.",
               "Cuando <b>gires</b> con tu vehículo <b>para entrar en otra vía</b> y haya peatones, ciclistas o animales <b>cruzándola</b>, <b>aunque no exista paso</b> para ellos.")],
            [T("When you <b>cross a hard shoulder</b> used by pedestrians, cyclists or animals that have <b>no pedestrian zone</b> (or cañada).",
               "Cuando el vehículo <b>cruce un arcén</b> por el que circulen peatones, ciclistas o animales que <b>no dispongan de zona peatonal</b> (o cañada).")],
            [T("When you cross <b>pedestrian zones</b> through the <b>passages</b> made for that (a garage entrance, for example).",
               "Cuando cruces las <b>zonas peatonales</b> por los <b>pasos habilitados</b> al efecto (la entrada de un garaje, por ejemplo).")],
            [T("When pedestrians are getting <b>on or off a bus</b> at a <b>signed stop</b> and are between the bus and the nearest pedestrian zone or refuge.",
               "Cuando los peatones vayan a <b>subir o hayan bajado</b> de un <b>autobús</b> en una <b>parada señalizada</b> y estén entre el vehículo y la zona peatonal o refugio más próximo.")],
            [T("<b>Troops</b> on foot, <b>school rows</b> and <b>organised processions</b>.", "<b>Tropas en formación</b>, <b>filas escolares</b> y <b>comitivas organizadas</b>.")],
            [T("A <b>group of cyclists</b> once the <b>first</b> has started crossing or has <b>entered a roundabout</b>: the group counts as <b>one moving unit</b>.",
               "Un <b>grupo de ciclistas</b> cuando el <b>primero</b> haya iniciado ya el cruce o haya <b>entrado en una glorieta</b>: se considera <b>una unidad móvil</b>.")],
        ],
    ))
    B.append(FIG(vulnerable_turn, "When you turn into another road, those crossing it on foot, a cyclist close by and animals crossing all go first.",
                 "Cuando giras para entrar en otra vía, pasan primero quienes la cruzan a pie, el ciclista próximo y los animales que la cruzan."))
    B.append(TABLE(
        [T("Cyclists also have priority over other vehicles…", "Los ciclistas tienen además prioridad sobre otros vehículos…")],
        [
            [T("When riding on a properly signed <b>cycle lane</b>, <b>cycle crossing</b> or <b>hard shoulder</b>.", "Cuando circulen por un <b>carril bici</b>, <b>paso para ciclistas</b> o <b>arcén</b> debidamente señalizados.")],
            [T("When a <b>motor vehicle or moped turns</b> right or left to enter another road and a cyclist is <b>close by</b> — your motorcycle included.",
               "Cuando, para entrar en otra vía, el <b>vehículo de motor o el ciclomotor gire</b> a derecha o izquierda y haya un ciclista <b>en sus proximidades</b>: también tu moto.")],
        ],
    ))
    B.append(BOX("key", "New since 1 October 2026", "Novedad desde el 1 de octubre de 2026", [
        ("In a zone with a <b>single platform</b> (road and pavement at the same level), the <b>pedestrian has priority at any point</b> of the carriageway.",
         "En las zonas de <b>plataforma única</b> de calzada y acera, el <b>peatón tiene prioridad de paso en cualquier punto</b> de la calzada."),
        ("The rules now define <b>vulnerable road users</b>: pedestrians (above all disabled people, children and older people), cyclists, VMP riders, "
         "and <b>riders and passengers of motorcycles and mopeds</b> — you.",
         "La norma define ahora a los <b>usuarios vulnerables</b>: peatones (sobre todo personas con discapacidad, menores y mayores), ciclistas, conductores de VMP "
         "y <b>conductores y pasajeros de motocicletas y ciclomotores</b>: tú."),
    ]))
    B.append(E(
        "How a cañada is signed", "Cómo se señaliza una cañada",
        "With a <b>supplementary panel</b> reading <b>«cañada»</b> under the <b>“domestic animals”</b> warning sign, together with the corresponding <b>speed-limit</b> signs.",
        "Con <b>paneles complementarios</b> con la inscripción <b>«cañada»</b> debajo de la señal de <b>«paso de animales domésticos»</b>, complementados con las señales de <b>limitación de velocidad</b>."))

    # ---------------------------------------------------------------- 3. narrow stretches
    B.append(H2("3", "Narrow stretches", "Estrechamientos"))
    B.append(P(
        "A <b>narrow stretch</b> (<i>estrechamiento</i>) is a part of the road so narrow that two vehicles going in <b>opposite directions</b> cannot pass each other, or only with great difficulty.",
        "Son los tramos de la vía en los que, por su estrechez, es <b>imposible o muy difícil el paso simultáneo</b> de dos vehículos que circulen en <b>sentidos opuestos</b>."))
    B.append(H3("3.1 Who goes first in a narrow stretch", "3.1 Preferencia en estrechamientos"))
    B.append(FIG(narrowing, "Each end of the narrow stretch has its own sign: the blue square means you go first, the red circle means you give way.",
                 "Cada extremo del estrechamiento tiene su señal: el cuadrado azul indica que pasas primero; el círculo rojo, que cedes el paso."))
    B.append(E(
        "With signs", "Con señalización",
        "Priority is set by <b>agents</b>, <b>traffic lights</b> or <b>vertical signs</b>: <b>R-6 “priority over oncoming traffic”</b> (blue square) or <b>R-5 “give way to oncoming traffic”</b> (red circle).",
        "La preferencia la regulan <b>agentes</b>, <b>semáforos</b> o <b>señales verticales</b>: <b>R-6 «Prioridad respecto al sentido contrario»</b> (cuadrado azul) o <b>R-5 «Prioridad en sentido contrario»</b> (círculo rojo).",
        tip=("Square and blue = yours. Round and red = theirs.", "Cuadrada y azul = tuya. Redonda y roja = suya.")))
    B.append(E(
        "Without signs", "Sin señalización",
        "The vehicle that <b>entered first</b> goes first. Only if it is <b>unclear</b> who entered first does the vehicle that is <b>harder to manoeuvre</b> go first, in this order. "
        "A <b>motorcycle</b> is at the <b>bottom</b>: in doubt, it gives way to everything except another motorcycle, moped or bicycle.",
        "Tiene preferencia el vehículo que <b>hubiera entrado primero</b>. Solo <b>en caso de duda</b> la tiene el de <b>mayor dificultad de maniobra</b>, según este orden. "
        "La <b>motocicleta</b> está <b>al final</b>: en caso de duda, cede ante todos salvo otra moto, un ciclomotor de dos ruedas o una bicicleta."))
    B.append(FIG(narrow_order, "Ten steps, from hardest to easiest to manoeuvre. With a sidecar a motorcycle moves up to step 9.",
                 "Diez puestos, de mayor a menor dificultad de maniobra. Con sidecar, la moto sube al puesto 9."))
    B.append(BOX("key", "Narrow stretch on a steep gradient (7 % or more)", "Estrechamiento en tramo de gran pendiente (7 % o más)", [
        ("The vehicle going <b>uphill</b> goes first, <b>unless</b> it could reach a <b>lay-by</b> (<i>apartadero</i>) provided for this before the other one could.",
         "Tiene preferencia el vehículo que circula en <b>sentido ascendente</b>, <b>salvo</b> que este pudiera llegar antes a un <b>apartadero</b> establecido al efecto."),
        ("In doubt about the gradient or the distance to the lay-by, the general rules for narrow stretches apply.",
         "En caso de duda sobre la inclinación o la distancia al apartadero, se aplican las normas generales de los estrechamientos."),
    ]))
    B.append(H3("3.2 Bridges and other narrow structures", "3.2 Paso de puentes u obras de paso"))
    B.append(TABLE(
        [T("Case", "Caso"), T("Rule", "Norma")],
        [
            [T("Bridge too narrow for two vehicles", "Puente u obra de paso que no permite el cruce"), T("Follow the <b>signs</b> that regulate it.", "Se sigue la <b>señalización</b> que lo regule.")],
            [T("Two vehicles meet on it; one end has <b>R-5</b> or <b>give way</b>", "Se encuentran dos vehículos; en un extremo hay <b>R-5</b> o <b>ceda el paso</b>"),
             T("The one that came in by <b>that end reverses</b> to let the other pass.", "El que llegó por <b>ese extremo retrocede</b> para dejar paso al otro.")],
            [T("No signs", "Sin señalización"), T("The order of vehicles in 3.1.", "El orden de vehículos del apartado 3.1.")],
        ],
        widths=["40%", "60%"],
    ))

    # ---------------------------------------------------------------- 4. emergency vehicles
    B.append(H2("4", "Vehicles on emergency service", "Vehículos en servicio de urgencia"))
    B.append(H3("4.1 Priority vehicles", "4.1 Vehículos prioritarios"))
    B.append(P(
        "<b>Emergency service vehicles</b> (<b>police, fire brigade, civil protection and ambulances</b>), public or private, have priority over all other vehicles and road users "
        "when they are <b>on urgent service</b> and signal it correctly; so do <b>road maintenance crews</b> and vehicles going to provide <b>roadside assistance</b>.",
        "Tienen prioridad de paso sobre los demás vehículos y usuarios los <b>vehículos de servicios de urgencia</b> (<b>policía, extinción de incendios, protección civil y asistencia sanitaria</b>), "
        "públicos o privados, cuando estén <b>en servicio de urgencia</b> y lo señalicen correctamente; así como los <b>equipos de mantenimiento de la vía</b> y los vehículos que acudan a un <b>auxilio en carretera</b>."))
    B.append(FIG(emergency_signals, "How each kind of emergency driver makes itself noticed, and what everyone else does.",
                 "Cómo se hace notar cada tipo de conductor en urgencia y qué hacen los demás."))
    B.append(E(
        "When they count as priority vehicles", "Cuándo son prioritarios",
        "When on <b>urgent service</b> and announcing it with the <b>light signal and the special siren at the same time</b>. Exceptionally, the <b>light alone</b>, "
        "when leaving out the siren is <b>no danger</b> to anyone. The light signal (<b>V-1</b>) is one or more <b>blue</b> lights.",
        "Cuando circulan en <b>servicio urgente</b> y advierten de su presencia con el uso <b>simultáneo de la señal luminosa y del aparato de señales acústicas especiales</b>. "
        "Excepcionalmente, la <b>señal luminosa aislada</b>, cuando omitir las acústicas <b>no entrañe peligro</b>. La señal luminosa (<b>V-1</b>) es un dispositivo con una o varias luces de color <b>azul</b>.",
        pills_=[T("light + siren", "luz + sirena"), T("V-1 blue", "V-1 azul")]))
    B.append(TABLE(
        [T("On urgent service and signalling correctly, they…", "En servicio de urgencia y señalizándolo correctamente…")],
        [
            [T("May go <b>above the speed limits</b> and are <b>exempt from other rules and signs</b>, on their <b>own responsibility</b>; but <b>agents’ instructions</b> must always be obeyed.",
               "Pueden circular por <b>encima de los límites de velocidad</b> y están <b>exentos de cumplir otras normas o señales</b>, bajo su <b>exclusiva responsabilidad</b>; salvo las de los <b>agentes</b>, siempre de obligado cumplimiento.")],
            [T("Must <b>not force their way</b> through junctions or red lights until sure there is <b>no risk of hitting pedestrians</b> and that other drivers have <b>stopped</b> or are making way.",
               "Cuidarán de <b>no vulnerar la prioridad</b> en las intersecciones ni los <b>semáforos</b> hasta cerciorarse de que no hay <b>riesgo de atropello</b> y de que los demás han <b>detenido su marcha</b> o se disponen a facilitar la suya.")],
        ],
    ))

    B.append(H3("4.2 What everyone else does", "4.2 Comportamiento de los demás usuarios"))
    B.append(P(
        "As soon as you notice the special signals of a vehicle on emergency service (priority or not), take the measures the situation allows to <b>let it through</b>: "
        "normally <b>move to your right</b>, and <b>stop</b> if necessary.",
        "Los demás conductores, en cuanto perciban las señales especiales de un vehículo en servicio de urgencia (prioritario o no), adoptarán las medidas adecuadas para <b>facilitarle el paso</b>: "
        "<b>apartarse normalmente a su derecha</b> o <b>detenerse</b> si fuera preciso."))
    B.append(FIG(corridor, "On autopistas and autovías, a queue that slows to walking pace or stops opens an emergency corridor.",
                 "En autopistas y autovías, una retención que avanza a paso de peatón o se detiene abre un carril de emergencia."))
    B.append(BOX("key", "Emergency corridor on autopistas and autovías", "Carril de emergencia en autopistas y autovías", [
        ("When a queue moves at <b>walking pace or stops</b>, vehicles move aside to leave a free gap for <b>priority vehicles</b>: the <b>emergency corridor</b>.",
         "Cuando por una retención se circula a <b>paso de peatón o se detiene</b>, los vehículos se orillan dejando un espacio libre para los <b>vehículos prioritarios</b>: el <b>carril de emergencia</b>."),
        ("<b>Two lanes</b> in the same direction: the gap is in the <b>centre</b>, between them.", "<b>Dos carriles</b> en el mismo sentido: se forma en el <b>centro</b>, entre ambos."),
        ("<b>Three or more</b>: between the <b>leftmost lane and the next one</b>; the left lane moves as far left as possible, the rest as far right as possible.",
         "<b>Tres o más</b>: entre el <b>carril de más a la izquierda y su contiguo</b>; los del izquierdo, lo más a la izquierda posible, y el resto, lo más a la derecha posible."),
        ("On a motorcycle, you move aside like everyone else. The corridor is kept free for priority vehicles; it is not a lane for motorcycles. "
         "The only extra space the rules open to motorcycles in a jam is the <b>signed right-hand shoulder</b> (Topic 2).",
         "En moto te apartas como los demás. El carril de emergencia se deja libre para los prioritarios; no es un carril para motos. "
         "El único espacio adicional que la norma abre a las motos en un atasco es el <b>arcén derecho señalizado</b> (Tema 2)."),
    ]))
    B.append(FIG(police_stop, "The forward red light is an order to stop, not a request to let the police through.",
                 "La luz roja hacia delante es una orden de detenerse, no una petición de paso."))
    B.append(E(
        "Police order to stop (since 1 July 2025)", "Orden de detención de la policía (desde el 1 de julio de 2025)",
        "If a <b>police vehicle</b> with its blue light and siren places itself <b>behind you</b> and also switches on a <b>red light flashing forward</b>, you must <b>stop</b> carefully "
        "<b>on the right, in front of the police vehicle</b>, where you create no extra risk or nuisance, <b>stay there</b>, and follow the agent’s instructions given by loudspeaker or other clear means.",
        "Si un <b>vehículo de policía</b> con su luz azul y sirena se sitúa <b>detrás de ti</b> y activa además una <b>luz roja intermitente o destellante hacia delante</b>, debes <b>detenerte</b> con precaución "
        "<b>en el lado derecho, delante del vehículo policial</b>, donde no generes mayores riesgos o molestias, <b>permanecer</b> en tu sitio y seguir las instrucciones del agente por megafonía u otro medio claro.",
        pills_=[T("red forward = stop", "rojo hacia delante = detente"), T("on the right, ahead of the police", "a la derecha, delante de la policía")],
        tip=("Your course doesn’t include this rule yet; it is in art. 69 of the Reglamento since July 2025.",
             "Tu curso aún no incluye esta norma; está en el art. 69 del Reglamento desde julio de 2025.")))
    B.append(E(
        "A non-priority vehicle in an emergency", "Vehículo no prioritario en servicio de urgencia",
        "If, in <b>especially serious</b> circumstances and with no other way out, an ordinary driver has to make an <b>urgent trip</b>, they warn others with the <b>horn on and off</b> "
        "and the <b>hazard lights</b>, or by <b>waving a handkerchief</b>. They have <b>no priority</b> and must <b>obey every rule</b>; agents may ask them to <b>justify</b> it.",
        "Si, por circunstancias <b>especialmente graves</b> y sin otro medio, un conductor cualquiera debe hacer un <b>servicio de urgencia</b>, advierte con el <b>avisador acústico intermitente</b> "
        "y la <b>luz de emergencia</b>, o <b>agitando un pañuelo</b>. <b>No tiene prioridad</b> y debe <b>respetar todas las normas</b>; los agentes pueden exigirle que lo <b>justifique</b>.",
        pills_=[T("no priority", "sin prioridad")]))

    # ---------------------------------------------------------------- 5. traps
    B.append(H2("5", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("Give way or STOP: you give way to vehicles from <b>both sides</b>, not only from the right.", "Ceda el paso o stop: se cede a los que vienen por <b>ambos lados</b>, no solo por la derecha."),
        ("Inside a roundabout or on an autovía you have priority over those <b>entering</b>, even if they come from your right.",
         "Dentro de la glorieta o en la autovía tienes prioridad sobre los que <b>entran</b>, aunque vengan por tu derecha."),
        ("A paved road beats an unpaved one, even if the unpaved one is on your right.", "La vía pavimentada pasa antes que la de tierra, aunque esta venga por tu derecha."),
        ("Having priority does <b>not</b> let you enter a junction or crossing where you will get stuck.", "Tener prioridad <b>no</b> permite entrar en una intersección o paso donde vas a quedar detenido."),
        ("Stuck inside a junction with lights: <b>leave without waiting</b> for your green.", "Detenido dentro de una intersección con semáforo: <b>sal sin esperar</b> a tu verde."),
        ("Turning into another road: pedestrians, cyclists and animals crossing go first <b>even without a crossing</b>.", "Al girar para entrar en otra vía: peatones, ciclistas y animales que cruzan pasan primero <b>aunque no haya paso</b>."),
        ("A group of cyclists is <b>one unit</b> once the first has started crossing or entered the roundabout.", "Un grupo de ciclistas es <b>una unidad</b> en cuanto el primero ha iniciado el cruce o entrado en la glorieta."),
        ("Narrow stretch: <b>first in</b> goes first; only <b>in doubt</b> does the list apply — and there your motorcycle is <b>last</b> (with sidecar, 9th).",
         "Estrechamiento: pasa <b>quien entró primero</b>; la lista solo rige <b>en caso de duda</b>, y en ella tu moto es <b>la última</b> (con sidecar, 9.ª)."),
        ("Two motorcycles in a narrow stretch: the one that would have to <b>reverse further</b> goes first.", "Dos motos en un estrechamiento: pasa la que tendría que <b>retroceder más distancia</b>."),
        ("Steep narrow stretch (≥ 7 %): <b>uphill</b> goes first, unless it can reach a lay-by first.", "Estrechamiento con pendiente (≥ 7 %): pasa el que <b>sube</b>, salvo que llegue antes a un apartadero."),
        ("Priority vehicle: <b>light and siren together</b>; light alone only when leaving out the siren is no danger.", "Prioritario: <b>luz y sirena a la vez</b>; solo la luz cuando omitir la sirena no entrañe peligro."),
        ("Police behind you with a <b>red light flashing forward</b>: stop on the right, <b>in front of</b> the police vehicle.", "Policía detrás con <b>luz roja intermitente hacia delante</b>: detente a la derecha, <b>delante</b> del vehículo policial."),
        ("Emergency corridor, 3 or more lanes: between the <b>leftmost lane and the next</b> — not between the two right-hand lanes.", "Carril de emergencia con 3 o más carriles: entre el <b>izquierdo y su contiguo</b>, no entre los dos de la derecha."),
    ]))

    # ---------------------------------------------------------------- 6. quick reference
    B.append(H2("6", "Key numbers and orders on one page", "Números y órdenes clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Answer", "Respuesta")],
        [
            [T("Unsigned junction", "Intersección sin señalizar"), T("give way to the right, except: paved road · rails · roundabout · autopista/autovía", "ceder a la derecha, salvo: vía pavimentada · raíles · glorieta · autopista/autovía")],
            [T("Order of precedence of signals", "Orden de prioridad entre señales"), T("agents → temporary → lights → vertical signs → markings", "agentes → circunstanciales → semáforos → verticales → marcas viales")],
            [T("Narrow stretch, no signs", "Estrechamiento sin señales"), T("first in; in doubt, the list (10 steps)", "el que entró primero; en duda, la lista (10 puestos)")],
            [T("Motorcycle in the list", "La moto en la lista"), T("10th (with sidecar, 9th)", "10.ª (con sidecar, 9.ª)")],
            [T("Same type of vehicle", "Mismo tipo de vehículo"), T("longer reversing distance, then width, length or MMA", "mayor distancia de marcha atrás; después anchura, longitud o MMA")],
            [T("Steep gradient", "Gran pendiente"), T("7 % or more: uphill first", "7 % o más: pasa el que sube")],
            [T("Light trailer in the list", "Remolque ligero en la lista"), T("cars with a trailer up to 750 kg MMA: 4th", "turismos con remolque de hasta 750 kg de MMA: 4.º")],
            [T("Priority vehicle light", "Señal luminosa de prioritario"), T("V-1, blue", "V-1, azul")],
            [T("Emergency corridor", "Carril de emergencia"), T("2 lanes: centre · 3+: between the left lane and the next", "2 carriles: centro · 3 o más: entre el izquierdo y su contiguo")],
            [T("Police order to stop", "Orden de detención policial"), T("red light flashing forward · since July 2025", "luz roja intermitente hacia delante · desde julio de 2025")],
        ],
        widths=["40%", "60%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
QUIZ_IDS = ["sg1", "un2", "un4", "cd2", "vu2", "vu5", "nr2", "nr5", "br1", "em2", "ot2", "ot5"]


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
    ("Reglamento General de Circulación (RD 1428/2003), arts. 32 and 56–69 — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Ley sobre Tráfico (RDL 6/2015), art. 25: drivers, pedestrians, cyclists and animals", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722"),
    ("Real Decreto 465/2025 (BOE 17-06-2025): police order to stop with a forward red light (art. 69), in force 1 July 2025", "https://www.boe.es/buscar/doc.php?id=BOE-A-2025-12199"),
    ("Real Decreto 518/2026 (BOE 26-06-2026): emergency corridor (art. 32), cyclists and pedestrians (arts. 64–65), single-platform zones and vulnerable road users, in force 1 October 2026",
     "https://www.boe.es/boe/dias/2026/06/26/pdfs/BOE-A-2026-13889.pdf"),
]

GLOSSARY = [
    ("prioridad · preferencia de paso", "priority · right of way"),
    ("ceder el paso", "to give way"),
    ("intersección · cruce a nivel", "junction · level crossing of paths"),
    ("vía preferente", "priority road"),
    ("línea de detención", "stop line"),
    ("vía pavimentada / sin pavimentar", "paved / unpaved road"),
    ("glorieta · vía circular", "roundabout · circular carriageway"),
    ("acceder · incorporarse", "to enter · to join"),
    ("cuadrícula amarilla", "yellow box junction (criss-cross grid)"),
    ("paso para peatones · paso para ciclistas", "pedestrian crossing · cycle crossing"),
    ("cañada", "livestock route (drove road)"),
    ("tropas en formación · filas escolares · comitivas", "troops on foot · school rows · processions"),
    ("unidad móvil", "one moving unit (group of cyclists)"),
    ("plataforma única", "single-level street (road and pavement at one level)"),
    ("usuario vulnerable", "vulnerable road user"),
    ("estrechamiento", "narrow stretch"),
    ("dificultad de maniobra", "difficulty of manoeuvring"),
    ("dar marcha atrás · retroceder", "to reverse · to back up"),
    ("apartadero", "lay-by (passing place)"),
    ("gran pendiente", "steep gradient"),
    ("puente · obra de paso", "bridge · narrow structure"),
    ("vehículo prioritario", "priority (emergency) vehicle"),
    ("servicio de urgencia", "emergency service"),
    ("señal luminosa V-1 · señales acústicas especiales", "V-1 blue light · siren"),
    ("auxilio en carretera", "roadside assistance"),
    ("carril de emergencia", "emergency corridor"),
    ("orillarse", "to pull over to the side"),
    ("orden de detención", "order to stop"),
]
