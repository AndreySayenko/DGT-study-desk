# -*- coding: utf-8 -*-
"""Topic 4 content (priority), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Tema 4: La prioridad). The wording and the figures are
original; the rules come from the Ley sobre Tráfico (RDL 6/2015, arts. 23–27), the Reglamento General de Circulación
(RD 1428/2003, arts. 56–70) as amended up to RD 518/2026 (in force 1 October 2026), and DGT material.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import priority_signs, right_rule, blocking_box, vulnerable_turn, narrowing, emergency_signals, corridor


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Who goes first. At a junction the answer comes from the <b>signs</b> if there are any; if not, from the <b>right-hand rule</b> "
         "and its <b>four exceptions</b> (paved road, rails, roundabouts, motorways).",
         "Quién pasa primero. En una intersección la respuesta la dan las <b>señales</b> si las hay; si no, la <b>regla de la derecha</b> "
         "y sus <b>cuatro excepciones</b> (vía pavimentada, raíles, glorietas, autopistas y autovías)."),
        ("Then the special cases the exam loves: level crossings, tunnels, pedestrians, cyclists and animals when you <b>turn</b>, "
         "the <b>order of vehicles in a narrow stretch</b>, and emergency vehicles.",
         "Después, los casos especiales que le gustan al examen: pasos a nivel, túneles, peatones, ciclistas y animales cuando <b>giras</b>, "
         "el <b>orden de vehículos en un estrechamiento</b> y los vehículos de urgencia."),
        ("The sections follow the order of your course’s Topic 4. Spanish exam terms are in <i>italics</i> in the English text, "
         "and a glossary closes the topic.",
         "Los apartados siguen el orden del Tema 4 de tu curso. Al final hay un glosario español–inglés."),
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
        "On a road with a <b>give way</b> or <b>STOP</b> sign (vertical sign and/or road marking), you <b>always give way</b> to vehicles on the priority road, "
        "<b>whichever side they come from</b>, stopping completely when necessary, and <b>always</b> when the sign requires it (STOP). "
        "You stop <b>at the stop line</b> or, if there is none, <b>immediately before the junction</b>. If, exceptionally, you cannot see enough from there, "
        "<b>stop again</b> where you can see, without endangering anyone.",
        "En vías con señal de <b>«ceda el paso»</b> o <b>«detención obligatoria o stop»</b> (señal vertical y/o marca vial), se <b>cede siempre el paso</b> a los vehículos de la vía preferente, "
        "<b>cualquiera que sea el lado por el que se aproximen</b>, llegando a detenerse por completo cuando sea preciso y, en todo caso, cuando lo indique la señal (stop). "
        "La detención se hace <b>ante la línea de detención</b> o, si no existe, <b>inmediatamente antes de la intersección</b>. Si, excepcionalmente, desde allí no hay visibilidad suficiente, "
        "hay que <b>detenerse de nuevo</b> donde se tenga, sin poner en peligro a nadie.",
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
            [T("<b>Autopistas and autovías</b>", "<b>Autopistas y autovías</b>"), T("Vehicles <b>on</b> the motorway, over those wanting to <b>join</b> it.", "Los que <b>circulen por</b> ella, sobre los que pretendan <b>acceder</b>.")],
        ],
        widths=["32%", "68%"],
    ))
    B.append(FIG(right_rule, "Left: each car gives way to the one on its right, so they go 1, 2, 3. Right: one of the exceptions overrides the right-hand rule.",
                 "Izquierda: cada uno cede al que tiene a su derecha, así que pasan 1, 2 y 3. Derecha: una de las excepciones se impone a la regla de la derecha."))
    B.append(E(
        "Sign P-2 “Junction with priority to the right”", "Señal P-2 «Intersección con prioridad de la derecha»",
        "The P-2 sign <b>does not change</b> the priority. It only <b>reminds</b> you that the general rules apply: first the four exceptions "
        "(paved road, rails, roundabouts, motorways), and if none applies, <b>give way to vehicles from the right</b>.",
        "La señal P-2 <b>no modifica</b> la prioridad. Solo <b>recuerda</b> que se aplican las normas generales: primero los cuatro supuestos "
        "(vía pavimentada, raíles, glorietas, autopistas y autovías) y, si no se da ninguno, <b>ceder el paso a los que vienen por la derecha</b>."))

    B.append(H3("1.3 How to act", "1.3 Normas de actuación"))
    B.append(TABLE(
        [T("You…", "Si…"), T("Rule", "Norma")],
        [
            [T("<b>must give way</b>", "<b>debes ceder el paso</b>"),
             T("Do not start, continue or resume your journey or manoeuvre until you are sure you will <b>not force</b> the driver with priority to change "
               "<b>path or speed</b> abruptly. Show it <b>early</b> by the way you drive, above all by <b>slowing down gradually</b>.",
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

    # ---------------------------------------------------------------- 2. level crossings and tunnels
    B.append(H2("2", "Level crossings, movable bridges and tunnels", "Pasos a nivel, puentes móviles y túneles"))
    B.append(H3("2.1 Level crossings and movable bridges", "2.1 Pasos a nivel y puentes móviles"))
    B.append(TABLE(
        [T("Situation", "Situación"), T("Rule", "Norma")],
        [
            [T("<b>Approaching</b> a level crossing or movable bridge", "<b>Al aproximarse</b> a un paso a nivel o a un puente móvil"),
             T("Take <b>extreme care</b> and <b>slow down below</b> the maximum allowed.", "<b>Extremar la prudencia</b> y <b>reducir la velocidad por debajo</b> de la máxima permitida.")],
            [T("<b>Barriers or half-barriers</b> across the road or <b>moving</b> (up or down), or <b>lights</b> showing stop", "<b>Barreras o semibarreras</b> atravesadas o <b>en movimiento</b> (subiendo o bajando), o <b>semáforos</b> que indiquen detención"),
             T("<b>Do not enter.</b> Wait one behind another in your lane until the way is clear.", "<b>No penetrar.</b> Detenerse uno detrás de otro en el carril correspondiente hasta tener paso libre.")],
            [T("<b>No barriers</b>, half-barriers or lights", "<b>Sin barreras</b>, semibarreras ni semáforos"),
             T("Do not enter without first making sure <b>no rail vehicle is coming</b>. You do <b>not have to stop</b> to look (unless a STOP sign tells you to).",
               "No penetrar sin <b>asegurarse de que no se acerca ningún vehículo</b> sobre raíles. <b>No es obligatorio detenerse</b> para observar (salvo que lo exija una señal de stop).")],
            [T("<b>Crossing</b>", "<b>El cruce</b>"),
             T("Cross <b>without delay</b>, and only once you are sure you will <b>not get stuck</b> inside because of the traffic or anything else.",
               "<b>Sin demora</b> y después de asegurarse de que <b>no hay riesgo de quedar inmovilizado</b> dentro del paso por la circulación u otras causas.")],
        ],
        widths=["36%", "64%"],
    ))
    B.append(BOX("trap", "Stuck on a level crossing", "Detenido en un paso a nivel", [
        ("If <b>force majeure</b> stops your vehicle on a level crossing, or its <b>load falls</b> there, get the <b>occupants out quickly</b> and <b>clear the crossing</b> as fast as possible.",
         "Si por <b>fuerza mayor</b> el vehículo queda detenido en un paso a nivel, o se le <b>cae la carga</b> dentro, hay que <b>desalojar rápidamente a los ocupantes</b> y <b>dejar el paso libre</b> cuanto antes."),
        ("If you cannot, do everything you can at once so that <b>train drivers</b> and the <b>drivers of other vehicles</b> approaching are <b>warned of the danger</b> in good time.",
         "Si no se consigue, se adoptarán de inmediato todas las medidas al alcance para que los <b>maquinistas</b> y los <b>conductores del resto de vehículos</b> sean <b>advertidos del peligro</b> con suficiente antelación."),
    ]))
    B.append(E(
        "Vehicles on rails", "Vehículos que circulan por raíles",
        "Vehicles on <b>rails</b> have priority over all other road users. <b>Trams</b>, at junctions without priority signs, have priority <b>both from the right and from the left</b>, "
        "except over <b>priority vehicles on urgent service</b>; signs may still give priority to drivers. <b>Trains</b>, given their nature, <b>always</b> have priority.",
        "Los vehículos que circulan por <b>raíles</b> tienen prioridad de paso sobre los demás usuarios. Los <b>tranvías</b>, en intersecciones sin señal de preferencia, tienen prioridad "
        "<b>tanto por la derecha como por la izquierda</b>, salvo sobre los <b>vehículos prioritarios en servicio de urgencia</b>; aun así, puede haber señales que den la prioridad a los conductores. "
        "Los <b>trenes</b>, por sus características, tienen prioridad <b>siempre</b>.",
        pills_=[T("train: always", "tren: siempre"), T("tram: right and left", "tranvía: derecha e izquierda")]))

    B.append(H3("2.2 Tunnels and underpasses", "2.2 Túneles y pasos inferiores"))
    B.append(TABLE(
        [T("Rule", "Norma"), T("Detail", "Detalle")],
        [
            [T("<b>Signs</b>", "<b>Señalización</b>"), T("Tunnels of <b>any length</b>, and underpasses <b>longer than 200 m</b>, are signed.",
                                                          "Los túneles de <b>cualquier longitud</b> y los pasos inferiores de <b>más de 200 m</b> están señalizados.")],
            [T("<b>Instructions</b>", "<b>Indicaciones</b>"), T("Obey the <b>traffic lights</b> (do not enter if they do not allow it) and the <b>variable-message panels</b>, and follow instructions given over <b>loudspeakers</b> or any other means.",
                                                                 "Obedecer los <b>semáforos</b> (no entrar si no lo permiten) y los <b>paneles de mensaje variable</b>, y seguir las instrucciones por <b>megafonía</b> o cualquier otro medio.")],
            [T("<b>Forbidden</b>", "<b>Prohibido</b>"), T("<b>Stopping, parking, turning round, reversing</b> and <b>overtaking</b> (see the next row). Use the <b>lights</b> required, and keep the safety distance strictly.",
                                                          "<b>Parar, estacionar, cambiar el sentido de la marcha, marchar hacia atrás</b> y <b>adelantar</b> (ver la fila siguiente). Usar el <b>alumbrado</b> correspondiente y respetar rigurosamente la distancia de seguridad.")],
            [T("<b>Overtaking</b>", "<b>Adelantamiento</b>"), T("In <b>two-way</b> tunnels and underpasses it is <b>forbidden</b>, unless there is <b>more than one lane for your direction</b>; then you may overtake without entering the opposite direction.",
                                                               "En túneles o pasos inferiores de <b>doble sentido</b> está <b>prohibido</b>, salvo que haya <b>más de un carril para tu sentido</b>; entonces se puede adelantar sin invadir el sentido contrario.")],
            [T("<b>Safety distance</b> (when not overtaking)", "<b>Distancia de seguridad</b> (cuando no se adelanta)"),
             T("At least <b>100 m or 4 seconds</b>. Vehicles with MMA <b>over 3,500 kg</b>: <b>150 m or 6 seconds</b>, or three chevrons in sight.",
               "Al menos <b>100 m o 4 segundos</b>. Vehículos de MMA <b>superior a 3.500 kg</b>: <b>150 m o 6 segundos</b>, o la visión de tres galones.")],
        ],
        widths=["26%", "74%"],
    ))

    # ---------------------------------------------------------------- 3. pedestrians, cyclists, animals
    B.append(H2("3", "Pedestrians, cyclists and animals", "Peatones, ciclistas y animales"))
    B.append(P(
        "Since October 2026 the Reglamento defines the <b>vulnerable road user</b> (<i>usuario vulnerable</i>): pedestrians (above all children, older and disabled people), cyclists, "
        "users of personal mobility vehicles, and riders and passengers of motorcycles and mopeds. The priority rules below protect most of them.",
        "Desde octubre de 2026 el Reglamento define al <b>usuario vulnerable de la vía</b>: peatones (sobre todo menores, personas mayores y con discapacidad), ciclistas, "
        "usuarios de vehículos de movilidad personal, y conductores y pasajeros de motocicletas y ciclomotores. Las normas de prioridad siguientes protegen a la mayoría de ellos."))
    B.append(FIG(vulnerable_turn, "When you turn into another road, those crossing it on foot, a cyclist close by and animals crossing all go first.",
                 "Cuando giras para entrar en otra vía, pasan primero quienes la cruzan a pie, el ciclista próximo y los animales que la cruzan."))
    B.append(H3("3.1 Pedestrians", "3.1 Peatones"))
    B.append(TABLE(
        [T("Pedestrians have priority over vehicles…", "Los peatones tienen prioridad sobre los vehículos…")],
        [
            [T("On properly signed <b>pedestrian crossings</b>, on <b>pavements</b> and in <b>pedestrian zones</b>.", "En los <b>pasos para peatones</b> debidamente señalizados, <b>aceras</b> y <b>zonas peatonales</b>.")],
            [T("When a vehicle <b>turns into another road</b> and pedestrians are <b>crossing</b> it, <b>even if there is no crossing</b>.", "Cuando un vehículo <b>gire para entrar en otra vía</b> y haya peatones <b>cruzando</b>, <b>aunque no exista paso</b> para ellos.")],
            [T("When a vehicle <b>crosses a hard shoulder</b> used by pedestrians who have <b>no pedestrian zone</b>.", "Cuando el vehículo <b>cruce un arcén</b> por el que circulen peatones que <b>no dispongan de zona peatonal</b>.")],
            [T("When vehicles cross <b>pedestrian zones</b> through the <b>passages</b> made for that (for example, a garage entrance across the pavement).", "Cuando los vehículos crucen las <b>zonas peatonales</b> por los <b>pasos habilitados</b> al efecto (por ejemplo, la entrada de un garaje).")],
            [T("When they are getting <b>on or off a bus</b> at a <b>signed stop</b> and are between the bus and the nearest pedestrian zone or refuge.", "Cuando vayan a <b>subir o hayan bajado</b> de un <b>autobús</b> en una <b>parada señalizada</b> y estén entre el vehículo y la zona peatonal o refugio más próximo.")],
            [T("<b>Troops</b>, <b>school rows</b> or <b>organised processions</b> on foot.", "Cuando transiten <b>unidades militares</b>, <b>filas escolares</b> o <b>comitivas organizadas</b>.")],
        ],
    ))
    B.append(BOX("key", "New since 1 October 2026", "Novedad desde el 1 de octubre de 2026", [
        ("On streets with a <b>single platform</b> (road and pavement at the same level), <b>pedestrians have priority</b>.",
         "En las calles de <b>plataforma única</b> (calzada y acera al mismo nivel), <b>los peatones tienen prioridad</b>."),
        ("At crossings with traffic lights, as a rule, vehicles no longer get a <b>flashing amber</b> while pedestrians have a <b>steady green</b>.",
         "En los pasos con semáforo, como norma general, ya no coincide el <b>ámbar intermitente</b> para vehículos con el <b>verde fijo</b> para peatones."),
    ]))
    B.append(H3("3.2 Cyclists", "3.2 Ciclistas"))
    B.append(TABLE(
        [T("Cyclists have priority over vehicles…", "Los ciclistas tienen prioridad sobre los vehículos…")],
        [
            [T("When riding on a properly signed <b>cycle lane</b>, <b>cycle crossing</b> or <b>hard shoulder</b>.", "Cuando circulen por un <b>carril bici</b>, <b>paso para ciclistas</b> o <b>arcén</b> debidamente señalizados.")],
            [T("When a <b>motor vehicle or moped turns</b> right or left to enter another road and a cyclist is <b>close by</b>.", "Cuando, para entrar en otra vía, el <b>vehículo de motor o el ciclomotor gire</b> a derecha o izquierda y haya un ciclista <b>en sus proximidades</b>.")],
            [T("When riding in a <b>group</b> and the <b>first one has already started crossing</b> or has <b>entered a roundabout</b>: the group counts as <b>one moving unit</b>.", "Cuando, circulando en <b>grupo</b>, el <b>primero haya iniciado ya el cruce</b> o haya <b>entrado en una glorieta</b>: el grupo se considera <b>una unidad móvil</b>.")],
        ],
    ))
    B.append(P("In <b>every other case</b>, the general priority rules between vehicles apply.",
               "En los <b>demás casos</b> se aplican las normas generales de prioridad entre vehículos."))
    B.append(H3("3.3 Animals", "3.3 Animales"))
    B.append(TABLE(
        [T("Drivers have priority over animals, except…", "Los conductores tienen prioridad sobre los animales, salvo…")],
        [
            [T("On properly signed <b>cañadas</b> (livestock routes).", "En las <b>cañadas</b> debidamente señalizadas.")],
            [T("When you <b>turn into another road</b> and animals are <b>crossing</b> it, <b>even if there is no crossing</b> for them.", "Cuando vayan a <b>girar para entrar en otra vía</b> y haya animales <b>cruzando</b>, <b>aunque no exista paso</b> para ellos.")],
            [T("When the vehicle <b>crosses a hard shoulder</b> along which animals are moving that have <b>no cañada</b>.", "Cuando el vehículo <b>cruce un arcén</b> por el que circulen animales que <b>no dispongan de cañada</b>.")],
        ],
    ))
    B.append(E(
        "How a cañada is signed", "Cómo se señaliza una cañada",
        "With a <b>supplementary panel</b> reading <b>«cañada»</b> under the <b>“domestic animals”</b> warning sign, together with the corresponding <b>speed-limit</b> signs.",
        "Con <b>paneles complementarios</b> con la inscripción <b>«cañada»</b> colocados debajo de la señal de <b>«paso de animales domésticos»</b>, complementados con las señales de <b>limitación de velocidad</b>."))

    # ---------------------------------------------------------------- 4. narrow stretches
    B.append(H2("4", "Narrow stretches", "Estrechamientos"))
    B.append(P(
        "A <b>narrow stretch</b> (<i>estrechamiento</i>) is a part of the road so narrow that two vehicles going in <b>opposite directions</b> cannot pass each other, or can only with great difficulty.",
        "Son los tramos de la vía en los que, por su estrechez, es <b>imposible o muy difícil el paso simultáneo</b> de dos vehículos que circulen en <b>sentidos opuestos</b>."))
    B.append(H3("4.1 Who goes first in a narrow stretch", "4.1 Preferencia en estrechamientos"))
    B.append(FIG(narrowing, "Each end of the narrow stretch has its own sign: the blue square means you go first, the red circle means you give way.",
                 "Cada extremo del estrechamiento tiene su señal: el cuadrado azul indica que pasas primero; el círculo rojo, que cedes el paso."))
    B.append(E(
        "With signs", "Con señalización",
        "Priority is set by <b>agents</b>, <b>traffic lights</b> or <b>vertical signs</b>: <b>R-6 “priority over oncoming traffic”</b> (blue square) or <b>R-5 “give way to oncoming traffic”</b> (red circle).",
        "La preferencia la regulan <b>agentes</b>, <b>semáforos</b> o <b>señales verticales</b>: <b>R-6 «Prioridad respecto al sentido contrario»</b> (cuadrado azul) o <b>R-5 «Prioridad en sentido contrario»</b> (círculo rojo).",
        tip=("Square and blue = yours. Round and red = theirs.", "Cuadrada y azul = tuya. Redonda y roja = suya.")))
    B.append(E(
        "Without signs", "Sin señalización",
        "The vehicle that <b>entered first</b> goes first. If it is unclear who entered first, the vehicle that is <b>harder to manoeuvre</b> goes first, in this order:",
        "Tiene preferencia el vehículo que <b>hubiera entrado primero</b>. En caso de duda, la tiene el de <b>mayor dificultad de maniobra</b>, según este orden:"))
    B.append(TABLE(
        [T("#", "#"), T("Goes first (most difficult to manoeuvre at the top)", "Pasa primero (mayor dificultad de maniobra arriba)")],
        [
            [T("1", "1"), T("<b>Special vehicles</b> and special transport that <b>exceed</b> the set masses or dimensions", "<b>Vehículos especiales</b> y en régimen de transporte especial que <b>excedan</b> de las masas o dimensiones establecidas")],
            [T("2", "2"), T("<b>Vehicle combinations</b> (except those in 4)", "<b>Conjuntos de vehículos</b> (excepto los del punto 4)")],
            [T("3", "3"), T("<b>Animal-drawn</b> vehicles", "Vehículos de <b>tracción animal</b>")],
            [T("4", "4"), T("<b>Cars towing a trailer</b> of up to <b>750 kg</b> MMA, and <b>motorhomes</b>", "<b>Turismos con remolque</b> de hasta <b>750 kg</b> de MMA y <b>autocaravanas</b>")],
            [T("5", "5"), T("<b>Buses</b>", "<b>Autobuses</b> (transporte colectivo de viajeros)")],
            [T("6", "6"), T("<b>Lorries</b>, tractor units and large vans (<i>furgones</i>)", "<b>Camiones</b>, tractocamiones y furgones")],
            [T("7", "7"), T("<b>Cars</b>, car-derived vans and adaptable mixed vehicles", "<b>Turismos</b>, derivados de turismo y vehículos mixtos adaptables")],
            [T("8", "8"), T("<b>Special vehicles</b> within the set masses and dimensions, quadricycles and light quadricycles", "<b>Vehículos especiales</b> que no excedan de las masas o dimensiones, cuadriciclos y cuadriciclos ligeros")],
            [T("9", "9"), T("Three-wheeled vehicles, <b>motorcycles with sidecar</b> and three-wheeled mopeds", "Vehículos de tres ruedas, <b>motocicletas con sidecar</b> y ciclomotores de tres ruedas")],
            [T("10", "10"), T("<b>Motorcycles without sidecar</b>, two-wheeled mopeds and <b>bicycles</b>", "<b>Motocicletas sin sidecar</b>, ciclomotores de dos ruedas y <b>bicicletas</b>")],
        ],
        widths=["8%", "92%"],
        cls="small",
    ))
    B.append(P(
        "Two vehicles of the <b>same type</b>, or of a type not on the list: the one that would have to <b>reverse the longer distance</b> goes first; if that is equal, "
        "the one with the greater <b>width, length or MMA</b>.",
        "Entre <b>vehículos del mismo tipo</b> o en supuestos no enumerados, tiene preferencia el que tuviera que <b>dar marcha atrás mayor distancia</b> y, en caso de igualdad, "
        "el de mayor <b>anchura, longitud o masa máxima autorizada</b>."))
    B.append(BOX("key", "Narrow stretch on a steep gradient (7 % or more)", "Estrechamiento en tramo de gran pendiente (7 % o más)", [
        ("The vehicle going <b>uphill</b> goes first, <b>unless</b> it could reach a <b>lay-by</b> (<i>apartadero</i>) provided for this before the other one could.",
         "Tiene preferencia el vehículo que circula en <b>sentido ascendente</b>, <b>salvo</b> que este pudiera llegar antes a un <b>apartadero</b> establecido al efecto."),
        ("In doubt about the gradient or the distance to the lay-by, the general rules for narrow stretches apply.",
         "En caso de duda sobre la inclinación o la distancia al apartadero, se aplican las normas generales de los estrechamientos."),
    ]))
    B.append(H3("4.2 Bridges and other narrow structures", "4.2 Paso de puentes u obras de paso"))
    B.append(TABLE(
        [T("Case", "Caso"), T("Rule", "Norma")],
        [
            [T("Bridge too narrow for two vehicles", "Puente que no permite el cruce"), T("Follow the <b>signs</b> that regulate it.", "Se sigue la <b>señalización</b> que lo regule.")],
            [T("Two vehicles meet on it; one end has <b>R-5</b> or <b>give way</b>", "Se encuentran dos vehículos; en un extremo hay <b>R-5</b> o <b>ceda el paso</b>"),
             T("The one that came in by <b>that end reverses</b> to let the other pass.", "El que llegó por <b>ese extremo retrocede</b> para dejar paso al otro.")],
            [T("No signs", "Sin señalización"), T("The order of vehicles in 4.1.", "El orden de vehículos del apartado 4.1.")],
            [T("Vehicles that need a <b>special permit</b>", "Vehículos que necesitan <b>autorización especial</b>"),
             T("May <b>not pass each other</b> on bridges whose carriageway is <b>narrower than 6 m</b>. If they meet, apply 4.1.",
               "<b>No pueden cruzarse</b> en puentes cuya calzada tenga <b>menos de 6 m</b> de anchura. Si se encuentran, se aplica el 4.1.")],
        ],
        widths=["38%", "62%"],
    ))

    # ---------------------------------------------------------------- 5. emergency vehicles
    B.append(H2("5", "Vehicles on emergency service", "Vehículos en servicio de urgencia"))
    B.append(H3("5.1 Priority vehicles", "5.1 Vehículos prioritarios"))
    B.append(P(
        "<b>Emergency service vehicles</b> (<b>police, fire brigade, civil protection and ambulances</b>), public or private, have priority over all other vehicles and road users "
        "when they are <b>on urgent service</b> and signal it correctly. The law extends this to <b>road maintenance crews</b> and vehicles going to provide <b>roadside assistance</b>.",
        "Tienen prioridad de paso sobre los demás vehículos y usuarios los <b>vehículos de servicios de urgencia</b> (<b>policía, extinción de incendios, protección civil y asistencia sanitaria</b>), "
        "públicos o privados, cuando estén <b>en servicio de urgencia</b> y lo señalicen correctamente; así como los <b>equipos de mantenimiento de la vía</b> y los vehículos que acudan a un <b>auxilio en carretera</b>."))
    B.append(FIG(emergency_signals, "How each kind of emergency driver makes itself noticed, and what everyone else does.",
                 "Cómo se hace notar cada tipo de conductor en urgencia y qué hacen los demás."))
    B.append(E(
        "When they count as priority vehicles", "Cuándo son prioritarios",
        "When on <b>urgent service</b> and announcing it with the <b>light signal and the special siren at the same time</b>. Exceptionally, the <b>light alone</b>, "
        "when leaving out the siren is <b>no danger</b> to anyone. The light signal (<b>V-1</b>) is one or more <b>blue</b> lights, visible in all directions from at least <b>50 m</b>.",
        "Cuando circulan en <b>servicio urgente</b> y advierten de su presencia con el uso <b>simultáneo de la señal luminosa y el aparato de señales acústicas especiales</b>. "
        "Excepcionalmente, la <b>señal luminosa aislada</b>, cuando omitir las acústicas <b>no entrañe peligro</b>. La señal luminosa (<b>V-1</b>) es uno o varios destellos de color <b>azul</b>, "
        "visibles en todas las direcciones a <b>50 m</b> como mínimo.",
        pills_=[T("light + siren", "luz + sirena"), T("V-1 blue, 50 m", "V-1 azul, 50 m")]))
    B.append(TABLE(
        [T("On urgent service and signalling correctly, they…", "En servicio de urgencia y señalizándolo correctamente…")],
        [
            [T("May go <b>above the speed limits</b> and are <b>exempt from other rules and signs</b>, on their <b>own responsibility</b>; but <b>agents’ instructions</b> must always be obeyed.",
               "Pueden circular por <b>encima de los límites de velocidad</b> y están <b>exentos de cumplir otras normas o señales</b>, bajo su <b>exclusiva responsabilidad</b>; salvo las órdenes de los <b>agentes</b>, siempre de obligado cumplimiento.")],
            [T("Must <b>not force their way</b> through junctions or red lights until sure there is <b>no risk of hitting pedestrians</b> and that other drivers have <b>stopped</b> or are making way.",
               "Cuidarán de <b>no vulnerar la prioridad</b> en las intersecciones ni los <b>semáforos</b> hasta cerciorarse de que no hay <b>riesgo de atropello</b> y de que los demás han <b>detenido su marcha</b> o se disponen a facilitar la suya.")],
            [T("On <b>autopistas and autovías</b>, exceptionally and without endangering anyone: <b>turn round or reverse</b>, drive <b>against the traffic on the shoulder</b>, or <b>enter the median</b> or its crossing points.",
               "En <b>autopista o autovía</b>, con carácter excepcional y sin comprometer la seguridad: <b>dar media vuelta o marcha atrás</b>, circular en <b>sentido contrario por el arcén</b>, o <b>penetrar en la mediana</b> o sus pasos transversales.")],
        ],
    ))
    B.append(P(
        "Traffic <b>agents</b> may put their vehicles wherever needed to help road users or for the service, and decide where emergency and other special-service vehicles stand.",
        "Los <b>agentes</b> de tráfico pueden situar sus vehículos donde sea necesario para auxiliar a los usuarios o por necesidades del servicio, y determinan dónde se colocan los vehículos de urgencia y de otros servicios especiales."))
    B.append(H3("5.2 Non-priority vehicles on emergency service", "5.2 Vehículos no prioritarios en servicio de urgencia"))
    B.append(E(
        "An ordinary car in an emergency", "Un turismo cualquiera en una urgencia",
        "If, in <b>especially serious</b> circumstances and with no other way out, the driver of a non-priority vehicle has to make an <b>urgent trip</b>, they make others notice by sounding the "
        "<b>horn on and off</b> and switching on the <b>hazard lights</b> if the vehicle has them, or by <b>waving a handkerchief</b> or similar. They must still <b>obey every traffic rule</b>, "
        "above all at junctions, and agents may ask them at any time to <b>justify</b> the emergency.",
        "Si, por circunstancias <b>especialmente graves</b> y sin poder recurrir a otro medio, el conductor de un vehículo no prioritario se ve forzado a efectuar un <b>servicio de urgencia</b>, "
        "procurará que los demás adviertan su presencia con el <b>avisador acústico en forma intermitente</b> y la <b>luz de emergencia</b> si dispone de ella, o <b>agitando un pañuelo</b> o similar. "
        "Debe <b>respetar todas las normas de circulación</b>, especialmente en las intersecciones, y los agentes pueden exigirle en cualquier momento que <b>justifique</b> la urgencia.",
        pills_=[T("no priority", "sin prioridad"), T("all rules apply", "todas las normas")]))
    B.append(H3("5.3 What everyone else does", "5.3 Comportamiento de los demás usuarios"))
    B.append(P(
        "As soon as you notice the special signals of a vehicle on emergency service (priority or not), take the measures the situation allows to <b>let it through</b>: "
        "normally <b>move to your right</b>, and <b>stop</b> if necessary.",
        "Los demás conductores, en cuanto perciban las señales especiales de un vehículo en servicio de urgencia (prioritario o no), adoptarán las medidas adecuadas para <b>facilitarle el paso</b>: "
        "<b>apartarse normalmente a su derecha</b> o <b>detenerse</b> si fuera preciso."))
    B.append(FIG(corridor, "On autopistas and autovías, a queue that slows to walking pace or stops opens an emergency corridor.",
                 "En autopistas y autovías, una retención que avanza a paso de peatón o se detiene abre un carril de emergencia."))
    B.append(BOX("key", "Emergency corridor on autopistas and autovías", "Carril de emergencia en autopistas y autovías", [
        ("When a queue moves at <b>walking pace or stops</b>, vehicles move aside to leave a free gap for <b>priority vehicles</b>.",
         "Cuando por una retención se circula a <b>paso de peatón o se detiene</b>, los vehículos se orillan dejando un espacio libre para los <b>vehículos prioritarios</b>."),
        ("<b>Two lanes</b> in the same direction: the gap is in the <b>centre</b>, between them.", "<b>Dos carriles</b> en el mismo sentido: se forma en el <b>centro</b>, entre ambos."),
        ("<b>Three or more</b>: between the <b>leftmost lane and the next one</b>; the left lane moves as far left as possible, the rest as far right as possible.",
         "<b>Tres o más</b>: entre el <b>carril de más a la izquierda y su contiguo</b>; los del izquierdo, lo más a la izquierda posible, y el resto, lo más a la derecha posible."),
    ]))

    B.append(E(
        "Police order to stop (since 1 July 2025)", "Orden de detención de la policía (desde el 1 de julio de 2025)",
        "If a <b>police vehicle</b> with its blue light and siren places itself <b>behind you</b> and also switches on a <b>red light flashing forward</b>, you must <b>stop</b> carefully "
        "<b>on the right, in front of the police vehicle</b>, where you create no extra risk or nuisance, <b>stay inside</b> your vehicle, and follow the agent’s instructions given by loudspeaker or other clear means.",
        "Si un <b>vehículo de policía</b> con su luz azul y sirena se sitúa <b>detrás de ti</b> y activa además una <b>luz roja intermitente o destellante hacia delante</b>, debes <b>detenerte</b> con precaución "
        "<b>en el lado derecho, delante del vehículo policial</b>, donde no generes mayores riesgos o molestias, <b>permanecer en su interior</b> y seguir las instrucciones del agente por megafonía u otro medio claro.",
        pills_=[T("red forward = stop", "rojo hacia delante = detente"), T("on the right, ahead of the police", "a la derecha, delante de la policía")]))

    # ---------------------------------------------------------------- 6. traps
    B.append(H2("6", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("Give way or STOP: you give way to vehicles from <b>both sides</b>, not only from the right.", "Ceda el paso o stop: se cede a los que vienen por <b>ambos lados</b>, no solo por la derecha."),
        ("No stop line? Stop <b>immediately before the junction</b>; can’t see? <b>Stop again</b> further on.", "¿Sin línea de detención? Detente <b>inmediatamente antes de la intersección</b>; ¿no ves? <b>Detente de nuevo</b> más adelante."),
        ("The P-2 sign <b>changes nothing</b>: it only reminds you of the general rules.", "La señal P-2 <b>no cambia nada</b>: solo recuerda las normas generales."),
        ("Inside a roundabout or on a motorway you have priority over those <b>entering</b>, even if they come from your right.",
         "Dentro de la glorieta o en la autopista tienes prioridad sobre los que <b>entran</b>, aunque vengan por tu derecha."),
        ("Having priority does <b>not</b> let you enter a junction or crossing where you will get stuck.", "Tener prioridad <b>no</b> permite entrar en una intersección o paso donde vas a quedar detenido."),
        ("Stuck inside a junction with lights: <b>leave without waiting</b> for your green.", "Detenido dentro de una intersección con semáforo: <b>sal sin esperar</b> a tu verde."),
        ("Level crossing <b>without barriers</b>: make sure nothing is coming; stopping is <b>not compulsory</b> (unless signed).",
         "Paso a nivel <b>sin barreras</b>: asegúrate de que no viene nada; <b>no es obligatorio</b> detenerse (salvo señal)."),
        ("Trams have priority from <b>right and left</b> at unsigned junctions, but <b>not over priority vehicles</b> on urgent service; trains <b>always</b>.",
         "El tranvía tiene prioridad por la <b>derecha y por la izquierda</b> en intersecciones sin señalizar, pero <b>no sobre los prioritarios</b> en servicio urgente; el tren, <b>siempre</b>."),
        ("Underpasses are signed from <b>200 m</b>; tunnels at <b>any length</b>.", "Los pasos inferiores se señalizan a partir de <b>200 m</b>; los túneles, de <b>cualquier longitud</b>."),
        ("Turning into another road: pedestrians and animals crossing go first <b>even without a crossing</b>; a nearby cyclist too.",
         "Al girar para entrar en otra vía: peatones y animales que cruzan pasan primero <b>aunque no haya paso</b>; el ciclista próximo, también."),
        ("A group of cyclists is <b>one unit</b> once the first has started crossing or entered the roundabout.",
         "Un grupo de ciclistas es <b>una unidad</b> en cuanto el primero ha iniciado el cruce o entrado en la glorieta."),
        ("Narrow stretch: <b>first in</b> goes first; only <b>in doubt</b> does the vehicle list apply. A car with a small trailer (≤ 750 kg) is <b>4th</b>, a bus <b>5th</b>, a lorry <b>6th</b>.",
         "Estrechamiento: pasa <b>quien entró primero</b>; la lista solo rige <b>en caso de duda</b>. Turismo con remolque ligero (≤ 750 kg): <b>4.º</b>; autobús: <b>5.º</b>; camión: <b>6.º</b>."),
        ("Steep narrow stretch (≥ 7 %): <b>uphill</b> goes first, unless it can reach a lay-by first.", "Estrechamiento con pendiente (≥ 7 %): pasa el que <b>sube</b>, salvo que llegue antes a un apartadero."),
        ("R-6 blue square = <b>you</b> go first; R-5 red circle = <b>they</b> go first, and you reverse if you meet on a bridge.",
         "R-6 cuadrado azul = pasas <b>tú</b>; R-5 círculo rojo = pasa <b>el otro</b>, y retrocedes si os encontráis en el puente."),
        ("A non-priority car in an emergency has <b>no priority</b>: horn + hazard lights or handkerchief, and every rule still applies.",
         "Un turismo no prioritario en urgencia <b>no tiene prioridad</b>: claxon + luz de emergencia o pañuelo, y debe cumplir todas las normas."),
    ]))

    # ---------------------------------------------------------------- 7. quick reference
    B.append(H2("7", "Key numbers and orders on one page", "Números y órdenes clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Answer", "Respuesta")],
        [
            [T("Unsigned junction", "Intersección sin señalizar"), T("give way to the right, except: paved road · rails · roundabout · motorway", "ceder a la derecha, salvo: vía pavimentada · raíles · glorieta · autopista/autovía")],
            [T("Order of precedence of signals", "Orden de prioridad entre señales"), T("agents → temporary → lights → vertical signs → markings", "agentes → circunstanciales → semáforos → verticales → marcas viales")],
            [T("Tunnels / underpasses signed", "Túneles / pasos inferiores señalizados"), T("any length / &gt; 200 m", "cualquier longitud / &gt; 200 m")],
            [T("Distance in tunnels (not overtaking)", "Distancia en túneles (sin adelantar)"), T("100 m or 4 s; &gt; 3,500 kg: 150 m or 6 s (3 chevrons)", "100 m o 4 s; &gt; 3.500 kg: 150 m o 6 s (3 galones)")],
            [T("Narrow stretch, no signs", "Estrechamiento sin señales"), T("first in; in doubt, the list (10 steps)", "el que entró primero; en duda, la lista (10 puestos)")],
            [T("Light trailer in the list", "Remolque ligero en la lista"), T("up to 750 kg MMA (with motorhomes: 4th)", "hasta 750 kg de MMA (con autocaravanas: 4.º)")],
            [T("Same type of vehicle", "Mismo tipo de vehículo"), T("longer reversing distance, then width, length or MMA", "mayor distancia de marcha atrás; después anchura, longitud o MMA")],
            [T("Steep gradient", "Gran pendiente"), T("7 % or more: uphill first", "7 % o más: pasa el que sube")],
            [T("Bridges: specially permitted vehicles may not pass each other", "Puentes: vehículos con autorización especial no se cruzan"), T("carriageway &lt; 6 m", "calzada &lt; 6 m")],
            [T("Priority vehicle light (V-1)", "Señal luminosa de prioritario (V-1)"), T("blue, visible from 50 m in all directions", "azul, visible a 50 m en todas direcciones")],
            [T("Emergency corridor", "Carril de emergencia"), T("2 lanes: centre · 3+: between the left lane and the next", "2 carriles: centro · 3 o más: entre el izquierdo y su contiguo")],
        ],
        widths=["40%", "60%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["sg2", "sg4", "us2", "us5", "co2", "rl3", "rl6", "pe2", "cy3", "nr3", "nr6", "pr3"]


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
    ("Reglamento General de Circulación (RD 1428/2003), priority rules (arts. 56–70) — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Ley sobre Tráfico, Circulación de Vehículos a Motor y Seguridad Vial (RDL 6/2015), arts. 23–27", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722"),
    ("Real Decreto 518/2026 (reform of the Reglamento, in force 1 October 2026)", "https://www.boe.es/eli/es/rd/2026/06/24/518"),
    ("La Moncloa, 30-09-2026: the reform comes into force (vulnerable road users, single-platform streets, emergency corridor)",
     "https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/interior/paginas/2026/300926-reforma-reglamento-circulacion.aspx"),
    ("DGT press release, 30-09-2026: reform of the Reglamento for vulnerable road users",
     "https://www.dgt.es/comunicacion/notas-de-prensa/20260930-reforma-del-reglamento-de-circulacion-usuarios-vulnerables/"),
]

GLOSSARY = [
    ("prioridad · preferencia de paso", "priority · right of way"),
    ("ceder el paso", "give way"),
    ("detención obligatoria (stop)", "compulsory stop (STOP)"),
    ("línea de detención", "stop line"),
    ("vía preferente · calzada con prioridad", "priority road"),
    ("intersección con prioridad de la derecha", "junction with priority to the right"),
    ("vía pavimentada · sin pavimentar", "paved · unpaved road"),
    ("raíles · tranvía", "rails · tram"),
    ("glorieta", "roundabout"),
    ("paso a nivel · barreras · semibarreras", "level crossing · barriers · half-barriers"),
    ("puente móvil", "movable (lifting or swing) bridge"),
    ("maquinista", "train driver"),
    ("fuerza mayor", "force majeure (circumstances beyond your control)"),
    ("túnel · paso inferior", "tunnel · underpass"),
    ("megafonía · panel de mensaje variable", "loudspeakers · variable-message panel"),
    ("usuario vulnerable de la vía", "vulnerable road user"),
    ("paso para peatones · paso para ciclistas", "pedestrian crossing · cycle crossing"),
    ("filas escolares · comitivas organizadas", "school rows · organised processions"),
    ("unidad móvil", "single moving unit"),
    ("cañada", "livestock route (drove road)"),
    ("estrechamiento", "narrow stretch"),
    ("prioridad respecto al sentido contrario (R-6)", "priority over oncoming traffic"),
    ("prioridad en sentido contrario (R-5)", "give way to oncoming traffic"),
    ("mayor dificultad de maniobra", "harder to manoeuvre"),
    ("apartadero", "lay-by / passing place"),
    ("obra de paso", "narrow structure (bridge, culvert)"),
    ("vehículo prioritario · servicio de urgencia", "priority vehicle · urgent service"),
    ("aparato de señales acústicas especiales", "siren"),
    ("auxilio en carretera", "roadside assistance"),
    ("avisador acústico · pañuelo", "horn · handkerchief"),
    ("carril de emergencia · orillarse", "emergency corridor · move to the edge"),
]
