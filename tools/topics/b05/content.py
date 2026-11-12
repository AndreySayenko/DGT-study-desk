# -*- coding: utf-8 -*-
"""Topic 5 content (manoeuvres), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Tema 5: Las maniobras). The wording and the figures are
original; the rules come from the Reglamento General de Circulación (RD 1428/2003, arts. 72–118) as amended up to
RD 518/2026 (in force 1 October 2026), the Ley sobre Tráfico (RDL 6/2015) and DGT material on the V-16 light.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import arm_signals, immobilisations, overtake_cyclist, turn_positions, park_slope, breakdown


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Every manoeuvre follows the same three steps: <b>observe, signal, carry out</b>. The exam checks whether you know the step order, "
         "the <b>signals</b> (lights, arm, horn, flashes) and the special rules of each manoeuvre.",
         "Toda maniobra sigue los mismos tres pasos: <b>observar, señalizar y realizar</b>. El examen comprueba el orden, "
         "las <b>señales</b> (luces, brazo, claxon, ráfagas) y las normas propias de cada maniobra."),
        ("The heavy parts are <b>overtaking</b> (where it is forbidden, the 1.5 m gap and the −20 km/h rule) and <b>stopping and parking</b> "
         "(where it is forbidden, which cases are serious offences, the V-16 light).",
         "Las partes más densas son el <b>adelantamiento</b> (dónde está prohibido, la separación de 1,5 m y la reducción de 20 km/h) y la <b>parada y el estacionamiento</b> "
         "(dónde están prohibidos, qué casos son infracción grave, la señal V-16)."),
        ("The sections follow the order of your course’s Topic 5. Spanish exam terms are in <i>italics</i> in the English text, "
         "and a glossary closes the topic.",
         "Los apartados siguen el orden del Tema 5 de tu curso. Al final hay un glosario español–inglés."),
    ]))

    # ---------------------------------------------------------------- 1. what manoeuvres are
    B.append(H2("1", "What manoeuvres are", "Qué son las maniobras"))
    B.append(P(
        "A <b>manoeuvre</b> is a noticeable change that a driver makes with the vehicle and that the <b>road layout does not impose</b>: the opposite of <b>normal progression</b>, "
        "which is driving within the flow of traffic without changing your position on the carriageway, simply following the road and the traffic.",
        "Las <b>maniobras</b> son las variaciones o alteraciones sensibles que realizan los conductores con sus vehículos, <b>no impuestas por el trazado de la vía</b>: lo contrario de la "
        "<b>progresión normal</b>, que es circular dentro de la corriente circulatoria sin alterar la posición en la calzada, adaptándose al trazado y a la densidad de circulación."))
    B.append(TABLE(
        [T("Before any manoeuvre", "Antes de cualquier maniobra"), T("Order", "Orden")],
        [
            [T("<b>RSM</b>", "<b>RSM</b>"), T("1 <b>Mirror</b> (<i>retrovisor</i>) · 2 <b>Signal</b> · 3 <b>Manoeuvre</b>", "1.º <b>Retrovisor</b> · 2.º <b>Señalizar</b> · 3.º <b>Maniobra</b>")],
            [T("<b>PVO</b>", "<b>PVO</b>"), T("1 <b>Position</b> · 2 <b>Speed</b> (<i>velocidad</i>) · 3 <b>Observation</b>", "1.º <b>Posición</b> · 2.º <b>Velocidad</b> · 3.º <b>Observación</b>")],
            [T("In short", "En resumen"), T("<b>Observe, signal, carry out.</b>", "<b>Observar, señalizar y realizar.</b>")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(TABLE(
        [T("Basic manoeuvres", "Maniobras básicas"), T("Not manoeuvres", "No son maniobras")],
        [
            [T("Joining traffic (<i>incorporación</i>)", "Incorporación"), T("A <b>detention</b> imposed by the road (red light, agent…)", "La <b>detención</b> impuesta por la vía (semáforo en rojo, agente…)")],
            [T("Moving sideways (<i>desplazamiento lateral</i>)", "Desplazamiento lateral"), T("Following a <b>curved path</b> (roundabout, bend…)", "La trayectoria <b>curva</b> (glorieta, curva de la carretera…)")],
            [T("Overtaking (<i>adelantamiento</i>)", "Adelantamiento"), T("<b>Reversing</b>: it only complements other manoeuvres, such as parking", "La <b>marcha atrás</b>: es complementaria de otras, como el estacionamiento")],
            [T("Turning (<i>cambio de dirección</i>)", "Cambio de dirección"), T("", "")],
            [T("Turning round (<i>cambio de sentido</i>)", "Cambio de sentido"), T("", "")],
            [T("Stopping or parking (<i>parada o estacionamiento</i>)", "Parada o estacionamiento"), T("", "")],
        ],
        widths=["50%", "50%"],
    ))

    # ---------------------------------------------------------------- 2. warnings
    B.append(H2("2", "Drivers’ warnings", "Advertencias de los conductores"))
    B.append(P("Drivers must <b>announce every manoeuvre</b>, showing what they intend <b>clearly and in good time</b>.",
               "Los conductores están <b>obligados a advertir las maniobras</b>, indicando su intención <b>de forma clara y con suficiente antelación</b>."))
    B.append(H3("2.1 Light and arm signals", "2.1 Advertencias ópticas"))
    B.append(P(
        "As a rule, use the <b>vehicle’s lights</b>, kept on for <b>the whole manoeuvre</b> and switched off when it ends; failing that, the <b>arm</b>, usually the <b>left</b> one. "
        "Arm signals only count when they are made <b>correctly</b> and are <b>visible to everyone</b>.",
        "Como norma general se usa la <b>señalización luminosa</b>, encendida <b>todo el tiempo que dure la maniobra</b> y apagada al terminar; en su defecto, el <b>brazo</b>, normalmente el <b>izquierdo</b>. "
        "Las señales con el brazo solo valen si se hacen <b>correctamente</b> y son <b>visibles para todos</b>."))
    B.append(FIG(arm_signals, "Each manoeuvre has a light and an arm signal. The arm signals are made with the left arm out of the driver’s window.",
                 "Cada maniobra tiene su señal luminosa y su señal con el brazo, que se hace con el brazo izquierdo por la ventanilla del conductor."))
    B.append(H3("2.2 Horn and headlight flashes", "2.2 Advertencias acústicas y destellos"))
    B.append(P(
        "The horn is <b>exceptional</b>: it warns others that you are there. Non-priority vehicles may use it <b>in and out of town</b> to <b>avoid a possible accident or running someone over</b> "
        "(above all on <b>narrow, winding roads</b>) and when on an <b>emergency trip</b>; and <b>only out of town</b> to <b>announce that you are going to overtake</b>.",
        "Las señales acústicas son <b>excepcionales</b>: advierten de la presencia del vehículo. Los no prioritarios solo pueden usarlas, <b>dentro y fuera de poblado</b>, para <b>evitar un posible accidente o atropello</b> "
        "(en especial en <b>vías estrechas con muchas curvas</b>) y en un <b>servicio de urgencia</b>; y <b>solo fuera de poblado</b>, para <b>advertir la intención de adelantar</b>."))
    B.append(TABLE(
        [T("Use", "Uso"), T("In town", "En poblado"), T("Out of town", "Fuera de poblado")],
        [
            [T("Avoid a possible accident or running someone over", "Evitar un posible accidente o atropello"), T("horn · flashes", "claxon · ráfagas"), T("horn · flashes", "claxon · ráfagas")],
            [T("Emergency trip (non-priority vehicle)", "Servicio de urgencia (no prioritario)"), T("horn · flashes", "claxon · ráfagas"), T("horn · flashes", "claxon · ráfagas")],
            [T("Announce that you are going to overtake", "Advertir la intención de adelantar"), T("<b>flashes only</b>", "<b>solo ráfagas</b>"), T("horn · flashes", "claxon · ráfagas")],
        ],
        widths=["50%", "25%", "25%"],
    ))
    B.append(E(
        "The horn itself", "El claxon",
        "A <b>continuous, steady</b> sound, loud enough to be heard but <b>not annoying</b>; never <b>shrill</b>, never varied musical notes or a tone that could be mistaken for another kind of vehicle. "
        "Using it <b>for no reason</b>, excessively, or for anything other than traffic (<b>greeting, telling someone off, warning of police</b>) is forbidden: it is noise pollution.",
        "Señal acústica <b>continua, uniforme</b> y con intensidad suficiente pero <b>sin molestar</b>; no debe ser <b>estridente</b> ni emitir notas musicales variadas o tonos que confundan sobre la naturaleza del vehículo. "
        "Está <b>prohibido su uso inmotivado</b>, exagerado o con otros fines (<b>saludar, recriminar, avisar de la presencia de agentes</b>): produce contaminación acústica."))
    B.append(E(
        "Headlight flashes (<i>destellos o ráfagas</i>)", "Destellos o ráfagas",
        "Short flashes of the <b>dipped or main beam</b>, or both alternately, at <b>very short intervals</b> so as not to dazzle. Allowed in the same cases as the horn, or <b>instead of it</b> "
        "(they make no noise). Forbidden for greeting, telling someone off or warning of police.",
        "Uso intermitente de la <b>luz de cruce o de carretera</b>, o de ambas alternativamente, a <b>intervalos muy cortos</b> para no deslumbrar. Se permiten en los mismos casos que el claxon o <b>para sustituirlo</b> "
        "(no producen contaminación acústica). Prohibido usarlos para saludar, recriminar o avisar de los agentes.",
        tip=("In town you announce an overtaking with flashes, never with the horn.", "En poblado el adelantamiento se avisa con ráfagas, nunca con el claxon.")))

    # ---------------------------------------------------------------- 3. joining traffic
    B.append(H2("3", "Joining traffic", "Incorporación a la circulación"))
    B.append(P(
        "<b>Joining traffic</b> is starting to drive (from stopped or parked, or out of a garage) or entering another road (from a slip road, a service area…). "
        "Moving off again after a <b>detention</b> ordered by agents or lights, or caused by normal traffic, is <b>not</b> joining.",
        "La <b>incorporación</b> es la maniobra para <b>comenzar a circular</b> (vehículo parado o estacionado, saliendo de un garaje…) o para entrar en otra vía (desde vías de acceso o zonas de servicio…). "
        "<b>No</b> es incorporación reanudar la marcha tras una <b>detención</b> ordenada por agentes o semáforos o impuesta por la circulación normal."))
    B.append(H3("3.1 How to join", "3.1 Cómo se realiza"))
    B.append(TABLE(
        [T("Step", "Paso"), T("What to do", "Qué hacer")],
        [
            [T("<b>1 Observe</b>", "<b>1.º Observar</b>"), T("Directly and in the <b>mirrors</b>: nobody on the road you are joining whom you could hinder or endanger (position, distance, path and speed). If there is, you may <b>not start</b>: they have priority.",
                                                         "Directamente y por los <b>retrovisores</b>: que no haya usuarios en la vía a los que se pueda entorpecer o poner en peligro (posición, distancia, trayectoria y velocidad). Si los hay, <b>no se puede iniciar</b>: tienen prioridad.")],
            [T("<b>2 Signal</b>", "<b>2.º Señalizar</b>"), T("With the <b>indicator</b> for the side you move to, or the arm. Joining <b>straight ahead</b>, with no sideways move: switch on <b>briefly</b> the indicator for the side you join from.",
                                                           "Con el <b>intermitente</b> del lado hacia el que nos desplazamos o, en su defecto, el brazo. Si nos incorporamos <b>de frente</b>, sin desplazamiento lateral: encender <b>momentáneamente</b> el intermitente del lado por el que nos incorporamos.")],
            [T("<b>3 Join</b>", "<b>3.º Realizar</b>"), T("<b>Give way</b>, and never force others to change their <b>position or speed</b> abruptly.", "<b>Cediendo el paso</b> y sin que los demás tengan que modificar bruscamente su <b>posición o velocidad</b>.")],
        ],
        widths=["20%", "80%"],
    ))
    B.append(P("If <b>dense traffic</b> stops you from joining, you <b>may signal</b> the manoeuvre so that others make room for you.",
               "Si la <b>densidad del tráfico</b> impide incorporarse, <b>está permitido señalizar</b> la maniobra para que los demás nos la faciliten."))
    B.append(E(
        "From a building or private road", "Desde un inmueble o camino privado",
        "Drive at a speed that lets you <b>stop at once</b> to give way to <b>vehicles and pedestrians</b> coming <b>from the right and from the left</b>.",
        "Circular a una velocidad que permita <b>detenerse en el acto</b> para ceder el paso a los <b>vehículos y peatones</b> que se aproximen <b>tanto por la derecha como por la izquierda</b>."))
    B.append(E(
        "From an acceleration lane", "Desde un carril de aceleración",
        "At the <b>start</b> of the lane make sure you can join safely, giving way to traffic on the main road (<b>stopping there if necessary</b>); then <b>speed up</b> to the right speed by the <b>end</b> of the lane.",
        "Al <b>principio</b> del carril, asegurarse de que se puede hacer con seguridad, cediendo el paso a los de la vía principal (<b>deteniéndose allí si fuera necesario</b>); y <b>aumentar la velocidad</b> hasta la adecuada al <b>final</b> del carril."))
    B.append(H3("3.2 Helping others join", "3.2 Obligación de facilitar la maniobra"))
    B.append(P(
        "When you see someone trying to join, help them <b>as far as you can</b>, above all a <b>bus leaving a signed stop</b>. In town, to let it out you must <b>move sideways</b> when possible, "
        "or <b>slow down</b> if it is safe and signalled, and <b>stop if necessary</b>. The bus driver still takes every precaution after signalling with the indicators.",
        "Quien vea a otro intentando incorporarse debe <b>facilitarle la maniobra en la medida de lo posible</b>, sobre todo a un <b>autobús que sale de una parada señalizada</b>. En poblado, hay que "
        "<b>desplazarse lateralmente</b> cuando sea posible, o <b>reducir la velocidad</b> sin peligro y señalizándolo, <b>llegando a detenerse si fuera preciso</b>. El conductor del autobús debe igualmente "
        "adoptar todas las precauciones tras anunciar con los intermitentes que reanuda la marcha.",))

    # ---------------------------------------------------------------- 4. moving sideways
    B.append(H2("4", "Moving sideways", "Desplazamiento lateral"))
    B.append(P(
        "Any change of position on the carriageway, left or right, that moves you <b>partly or fully into a lane you were not using</b> (a <b>lane change</b>). "
        "A <b>small correction within your own lane</b> is not one.",
        "Cualquier cambio de posición en la calzada, a izquierda o derecha, que implique la <b>invasión parcial o total de un carril</b> por el que no se circulaba (<b>cambio de carril</b>). "
        "<b>No</b> lo es la <b>simple corrección de trayectoria dentro del carril</b>."))
    B.append(TABLE(
        [T("Usual reasons", "Motivos habituales"), T("How to do it", "Cómo se realiza")],
        [
            [T("To turn · to pass an immobilised vehicle · to start an overtaking and come back · to stop or park · to join, or to make room for someone joining · because signs require a lane change",
               "Cambiar de dirección · rebasar a un inmovilizado · iniciar un adelantamiento y volver · parar o estacionar · incorporarse o facilitar la incorporación de otro · cambio de carril obligado por la señalización"),
             T("<b>Observe</b> that you hinder and endanger nobody; <b>signal</b> until the move is finished; move <b>early, gradually and smoothly</b> (no sudden swerves), "
               "respecting the <b>priority</b> of whoever is in the lane you are moving into.",
               "<b>Observar</b> que no se entorpece ni pone en peligro a nadie; <b>señalizar</b> hasta finalizar el desplazamiento; realizarlo con <b>antelación</b>, de forma gradual y <b>progresiva</b> (sin volantazos), "
               "respetando la <b>prioridad</b> del que circula por el carril que se quiere ocupar.")],
        ],
        widths=["45%", "55%"],
    ))

    # ---------------------------------------------------------------- 5. overtaking
    B.append(H2("5", "Overtaking", "Adelantamiento"))
    B.append(P("<b>Overtaking</b> is passing a vehicle ahead of you that is going <b>more slowly</b>.",
               "El <b>adelantamiento</b> es la maniobra de <b>sobrepasar</b> a otro vehículo que circula delante a una velocidad inferior."))
    B.append(BOX("trap", "It is not overtaking when…", "No se considera adelantamiento…", [
        ("In <b>congested</b> traffic filling the carriageway, your lane moves faster than the next one. Here you may <b>not change lanes to overtake</b>, "
         "only to get ready to turn, leave the carriageway or take a particular direction.",
         "Circular más rápido que el carril contiguo cuando la <b>circulación congestionada</b> ocupa toda la calzada. En esta situación <b>no se puede cambiar de carril para adelantar</b>, "
         "solo para prepararse a girar, salir de la calzada o tomar una dirección."),
        ("Lanes or parts of the road for certain vehicles or manoeuvres (<b>acceleration, deceleration, bus lane, shoulder</b>) move faster than the normal lanes, or the other way round.",
         "Se circula más rápido por carriles o partes de la vía destinados a determinados vehículos o maniobras (<b>aceleración, deceleración, bus, arcén</b>) que por los normales, o al revés."),
        ("Cyclists <b>riding in a group</b> pass each other.", "Se adelantan entre sí <b>ciclistas que circulan en grupo</b>."),
    ]))
    B.append(H3("5.1 How to overtake", "5.1 Cómo se debe adelantar"))
    B.append(P("Always safely, without endangering or hindering anyone. <b>If it is not 100 % safe, do not overtake.</b>",
               "Siempre con seguridad, sin poner en peligro ni entorpecer a nadie. <b>Si no hay seguridad al 100 %, no se adelanta.</b>"))
    B.append(TABLE(
        [T("Before you start", "Antes de iniciar la maniobra")],
        [
            [T("<b>1</b> Keep a <b>suitable distance</b> behind (too close cuts your view and risks a collision; too far means more time and distance) so that you can check there is "
               "<b>room to overtake</b> (your speed, theirs and any <b>oncoming</b> vehicle) and room to <b>accelerate</b> to a speed clearly higher than theirs.",
               "<b>1.º</b> Mantener una <b>separación adecuada</b> (ni muy cerca, porque reduce el campo de visión y hay peligro de colisión; ni muy lejos, porque se necesita más tiempo y distancia) que permita comprobar que hay "
               "<b>espacio suficiente para adelantar</b> (velocidad propia, la del adelantado y la del que viene <b>de frente</b>) y para <b>acelerar</b> hasta una velocidad notoriamente superior.")],
            [T("<b>2</b> Check there is room to <b>get back to the right</b>. Do not overtake <b>several vehicles</b> unless you are sure you could pull in if someone comes the other way.",
               "<b>2.º</b> Comprobar que hay espacio para <b>volver a la derecha</b>. No adelantar a <b>varios vehículos</b> si no es seguro poder regresar si aparece otro de frente.")],
            [T("<b>3</b> Check the vehicle ahead has <b>not signalled</b> a move to the same side (if so, it goes first; if after a reasonable time it does not move, you may overtake after warning it with the horn or lights), "
               "and that nobody behind has <b>already started overtaking you</b>.",
               "<b>3.º</b> Comprobar que el de delante <b>no ha indicado</b> que se desplaza hacia el mismo lado (si lo ha hecho, tiene preferencia; si tras un tiempo prudencial no lo hace, se le puede adelantar avisando con señales acústicas u ópticas), "
               "y que los de detrás <b>no han iniciado ya el adelantamiento</b> a tu vehículo.")],
            [T("<b>4</b> If you need to move sideways, <b>signal early</b>, and stop signalling once you are in position.",
               "<b>4.º</b> Si requiere desplazamiento lateral, <b>advertirlo con suficiente antelación</b> y quitar la señal al estar en la posición adecuada.")],
        ],
    ))
    B.append(P("To tell the driver ahead you want to overtake: <b>headlight flashes</b> (in and out of town) or the <b>horn</b> (out of town only).",
               "Para advertir al de delante del propósito de adelantar: <b>destellos</b> (dentro y fuera de poblado) o <b>señales acústicas</b> (solo fuera de poblado)."))
    B.append(TABLE(
        [T("Overtake on the…", "Se adelanta por…"), T("When", "Cuándo")],
        [
            [T("<b>Left</b>", "<b>La izquierda</b>"), T("As a <b>general rule</b>.", "Como <b>norma general</b>.")],
            [T("<b>Right</b> (exceptionally, with room and maximum care)", "<b>La derecha</b> (excepcionalmente, con espacio y máxima precaución)"),
             T("A vehicle clearly signalling a <b>left turn</b> or a stop on its left · <b>trams</b> running in the centre of a two-way road · <b>in town</b>, on carriageways with at least <b>two marked lanes</b> in your direction.",
               "Al que indica claramente que va a <b>girar a la izquierda</b> o a inmovilizarse en ese lado · a los <b>tranvías</b> que marchen por la zona central en vías de doble sentido · <b>en poblado</b>, en calzadas con al menos <b>dos carriles delimitados</b> en el mismo sentido.")],
        ],
        widths=["32%", "68%"],
    ))
    B.append(P(
        "Finishing: get back to the <b>right-hand lane</b> as soon as you can, <b>gradually</b>, without forcing anyone to change path or speed (when you see the overtaken vehicle in your mirror). "
        "If, once started, you see you <b>cannot finish safely</b>, <b>slow down quickly and pull back in</b> to the right, signalling it.",
        "Al terminar: volver al <b>carril de la derecha</b> tan pronto como sea posible y de forma <b>gradual</b>, sin obligar a nadie a cambiar su trayectoria o velocidad (cuando se vea al adelantado por el espejo). "
        "Si una vez iniciado se ve que <b>no se puede terminar sin peligro</b>, se <b>reduce rápidamente la velocidad y se regresa</b> al carril derecho, señalizándolo."))
    B.append(BOX("key", "Overtaking on multi-lane carriageways", "Adelantamientos en calzadas de varios carriles", [
        ("<b>One-way</b>, at least two lanes your way: for a new overtaking you may <b>stay in the lane</b> you used for the previous one, if you do not bother faster vehicles behind.",
         "<b>Sentido único</b>, al menos dos carriles: para un <b>nuevo adelantamiento</b> se puede <b>permanecer en el carril</b> utilizado para el anterior, si no se molesta a los que vienen detrás más rápido."),
        ("<b>Two-way</b> with three lanes separated by broken lines: overtake <b>only in the centre lane</b>, and only if oncoming drivers are not using it.",
         "<b>Doble sentido</b> con tres carriles separados por discontinuas: <b>solo por el carril central</b> y siempre que no lo ocupen los que vienen en sentido contrario."),
    ]))
    B.append(H3("5.2 Side gap when overtaking", "5.2 Distancia de seguridad al adelantar"))
    B.append(FIG(overtake_cyclist, "Overtaking a cyclist: side gap of at least 1.5 m and, out of town, 20 km/h below the road’s limit.",
                 "Adelantar a un ciclista: separación lateral mínima de 1,5 m y, fuera de poblado, 20 km/h por debajo del límite de la vía."))
    B.append(TABLE(
        [T("Overtaking…", "Al adelantar a…"), T("Gap", "Separación")],
        [
            [T("<b>Pedestrians, animals, animal-drawn vehicles, mopeds, personal mobility vehicles, cyclists</b> or groups of cyclists; vehicles <b>immobilised</b> by a breakdown or accident; "
               "<b>assistance vehicles</b> at work (in and out of town)",
               "<b>Peatones, animales, vehículos de tracción animal, ciclomotores, vehículos de movilidad personal, ciclistas</b> o grupos de ciclistas; vehículos <b>inmovilizados</b> por avería o accidente; "
               "<b>vehículos de auxilio</b> en operaciones de auxilio y rescate (dentro y fuera de poblado)"),
             T("Move <b>partly or fully</b> into the next or opposite lane (a <b>full lane change</b> if there is more than one lane your way), when the rules allow it; side gap <b>never under 1.5 m</b>.",
               "Ocupar <b>parcial o totalmente</b> el carril contiguo o contrario (<b>cambio completo de carril</b> si hay más de uno por sentido), si se dan las condiciones reglamentarias; separación lateral <b>no inferior a 1,50 m</b>.")],
            [T("<b>Any other vehicle</b>", "<b>Cualquier otro vehículo</b>"), T("A side gap <b>proportional</b> to the speed and to the width and features of the carriageway.", "Separación lateral <b>proporcional</b> a la velocidad y a la anchura y características de la calzada.")],
            [T("A <b>two-wheeler</b> overtaking anything, <b>out of town</b>", "Un <b>vehículo de dos ruedas</b> que adelanta a otro cualquiera, <b>fuera de poblado</b>"), T("At least <b>1.5 m</b> between it and the other vehicle.", "Al menos <b>1,50 m</b> de separación lateral.")],
        ],
        widths=["50%", "50%"],
        cls="small",
    ))
    B.append(BOX("key", "When you must slow down by 20 km/h below the road’s limit", "Cuándo reducir 20 km/h respecto al límite de la vía", [
        ("<b>Out of town</b>: overtaking pedestrians, animals, animal-drawn vehicles, mopeds, personal mobility vehicles, cyclists or groups of cyclists.",
         "<b>Fuera de poblado</b>: al adelantar a peatones, animales, vehículos de tracción animal, ciclomotores, vehículos de movilidad personal, ciclistas o grupos de ciclistas."),
        ("<b>In and out of town</b>: overtaking vehicles immobilised by a breakdown or accident, or assistance vehicles at work (rescue, road maintenance, traffic management).",
         "<b>Dentro y fuera de poblado</b>: al adelantar a vehículos inmovilizados por avería o accidente, o a vehículos de auxilio trabajando (rescate, mantenimiento de la vía, gestión del tráfico)."),
        ("It is <b>forbidden</b> to overtake if that endangers or hinders <b>cyclists coming the other way</b>, even on the shoulder. A group of cyclists counts as <b>one moving unit</b>.",
         "Está <b>prohibido</b> adelantar poniendo en peligro o entorpeciendo a <b>ciclistas que circulen en sentido contrario</b>, incluso por el arcén. Un grupo de ciclistas es <b>una única unidad móvil</b>."),
    ]))
    B.append(H3("5.3 What the overtaken driver must do", "5.3 Qué debe hacer el vehículo adelantado"))
    B.append(TABLE(
        [T("Duty", "Obligación"), T("Detail", "Detalle")],
        [
            [T("<b>Position</b>", "<b>Posición</b>"), T("Keep to the <b>right edge</b> of the carriageway (not on the shoulder). If you want to turn or stop on the left, keep as far left as possible without getting in the way of oncoming traffic.",
                                                        "<b>Ceñirse al borde derecho</b> de la calzada (sin pisar el arcén). Si se quiere girar o inmovilizar a la izquierda, ceñirse a la izquierda todo lo posible sin interferir a los del sentido contrario.")],
            [T("<b>Speed</b>", "<b>Velocidad</b>"), T("<b>Never speed up</b> or make it harder. <b>Slow down</b> if a danger appears once the overtaking has started; if the overtaker gives up and slows down, <b>let them back in</b>.",
                                                     "<b>Prohibido aumentar la velocidad</b> o dificultar el adelantamiento. <b>Disminuir la velocidad</b> si, iniciado, surge un peligro; si el que adelanta desiste y frena, <b>facilitarle la vuelta al carril</b>.")],
            [T("<b>Heavy or large vehicles</b>, or with their own speed limit", "<b>Pesados, de grandes dimensiones</b> o con límite específico de velocidad"),
             T("If they cannot keep fully to the right but can be overtaken safely, they show it by <b>moving the arm from back to front</b> (back of the hand facing backwards) or with the <b>right indicator</b>. "
               "They also slow down or pull onto a passable shoulder when oncoming traffic, the width or the state of the road make overtaking difficult.",
               "Si no pueden ceñirse del todo a la derecha pero se les puede adelantar con seguridad, lo indican <b>extendiendo el brazo y moviéndolo de atrás hacia delante</b> (dorso de la mano hacia atrás) o con el <b>intermitente derecho</b>. "
               "Además, aminoran la marcha o se apartan al arcén practicable cuando el tráfico de frente, la anchura o el estado de la vía impiden adelantarlos con facilidad.")],
        ],
        widths=["26%", "74%"],
    ))
    B.append(H3("5.4 Where overtaking is forbidden", "5.4 Dónde está prohibido adelantar"))
    B.append(TABLE(
        [T("Reason", "Motivo"), T("Forbidden", "Prohibido")],
        [
            [T("<b>Signs</b>", "<b>Señalización</b>"), T("A no-overtaking sign; a road marking you may not cross (unless you can overtake without crossing it).",
                                                          "Señales verticales que lo prohíben; marca vial que no se puede atravesar (salvo que no sea necesario atravesarla).")],
            [T("<b>Poor visibility</b>", "<b>Falta de visibilidad</b>"), T("Bends and brows with reduced visibility · fog, heavy rain, snow… · <b>behind a vehicle that is overtaking</b> when its size hides the road ahead. "
                                                                          "<b>Exception:</b> allowed if the two directions are clearly separated and you do not enter the opposite one.",
                                                                          "Curvas y cambios de rasante de visibilidad reducida · niebla, lluvia intensa, nevada… · <b>detrás de otro que adelanta</b> si por sus dimensiones impide ver. "
                                                                          "<b>Excepción:</b> se puede si los dos sentidos están claramente delimitados y no se invade el contrario.")],
            [T("<b>Junctions</b> and near them", "<b>Intersecciones</b> y sus proximidades"), T("Forbidden, <b>except</b>: roundabouts · overtaking on the <b>right</b> a vehicle turning or stopping on the left · junctions where you have <b>signed priority</b> · overtaking <b>two-wheelers</b>.",
                                                                                         "Prohibido, <b>salvo</b>: glorietas y plazas de circulación giratoria · adelantar por la <b>derecha</b> al que gira o se inmoviliza a la izquierda · intersecciones con <b>prioridad señalizada</b> · a <b>vehículos de dos ruedas</b>.")],
            [T("<b>Other places</b>", "<b>Otros casos</b>"), T("<b>Level crossings</b>, <b>pedestrian crossings</b> and junctions with <b>cycle routes</b>, and near them · <b>tunnels</b> and underpasses with <b>one lane</b> your way · "
                                                               "a vehicle that is <b>already overtaking</b> another, if you would have to enter the opposite direction.",
                                                               "<b>Pasos a nivel</b>, <b>pasos para peatones</b> e intersecciones con <b>vías ciclistas</b>, y sus proximidades · <b>túneles</b> y pasos inferiores con <b>un solo carril</b> para tu sentido · "
                                                               "a los que <b>ya están adelantando</b>, si hay que invadir el sentido contrario.")],
        ],
        widths=["24%", "76%"],
        cls="small",
    ))
    B.append(H3("5.5 Special cases", "5.5 Supuestos especiales"))
    B.append(P(
        "You may use the opposite half of the road, <b>even where signs forbid it</b>, to: pass an <b>obstacle or immobilised vehicle</b> blocking your lane (breakdown, accident…), after making sure there is no danger; "
        "and overtake <b>cycles, mopeds, personal mobility vehicles, pedestrians, animals, animal-drawn vehicles and agricultural special vehicles</b> when their speed lets you do it without risk. "
        "But if a vehicle has stopped <b>because of the traffic</b>, you stay behind it.",
        "Se puede ocupar la parte del sentido contrario, <b>incluso donde la señalización lo prohíbe</b>, para: rebasar un <b>obstáculo o un vehículo inmovilizado</b> que ocupa el carril (avería, accidente…), tras asegurarse de que no hay peligro; "
        "y adelantar a <b>ciclos, ciclomotores, vehículos de movilidad personal, peatones, animales, vehículos de tracción animal y vehículos especiales agrícolas</b> cuando, por su velocidad, se les pueda adelantar sin riesgo. "
        "Pero si el vehículo está parado <b>por necesidades del tráfico</b>, hay que quedarse detrás."))

    # ---------------------------------------------------------------- 6. turning
    B.append(H2("6", "Turning", "Cambio de dirección"))
    B.append(P(
        "Turning left or right to <b>use another road</b>, take <b>another carriageway</b> of the same road, or <b>leave</b> the road. Turning the wheel to <b>follow a bend</b> is not a manoeuvre.",
        "Maniobra de girar a izquierda o derecha para <b>utilizar otra vía</b>, tomar <b>otra calzada</b> de la misma vía o <b>salir de la vía</b>. <b>No</b> es maniobra el giro para <b>seguir el trazado de una curva</b>."))
    B.append(P(
        "<b>1 Observe</b> that you can do it without hindering or endangering anyone (speed and distance of those approaching), or do not do it. <b>2 Signal</b> in good time to those behind. <b>3 Turn</b> from the right position:",
        "<b>1.º Observar</b> que se puede hacer sin entorpecer ni poner en peligro a nadie (velocidad y distancia de los que se acercan), o abstenerse. <b>2.º Señalizar</b> con antelación a los que vienen detrás. <b>3.º Realizar</b> la maniobra desde la posición correcta:"))
    B.append(FIG(turn_positions, "Before turning, position yourself on the side you are turning to, as far as the road allows.",
                 "Antes de girar, colócate en el lado hacia el que giras, todo lo que permita la vía."))
    B.append(TABLE(
        [T("Turn", "Giro"), T("Position", "Posición")],
        [
            [T("<b>Right</b>", "<b>A la derecha</b>"), T("As close as possible to the <b>right edge</b>.", "Ceñirse todo lo posible al <b>borde derecho</b>.")],
            [T("<b>Left</b>, one-way road", "<b>A la izquierda</b>, sentido único"), T("As close as possible to the <b>left edge</b>.", "Ceñirse todo lo posible al <b>borde izquierdo</b>.")],
            [T("<b>Left</b>, two-way road", "<b>A la izquierda</b>, doble sentido"),
             T("With a <b>centre marking</b>: next to it, without crossing it. With <b>no marking</b>: next to the <b>centre of the road</b>, without entering the other half. "
               "<b>Three lanes</b> with broken lines: in the <b>centre lane</b>.",
               "Con <b>marca vial</b> que separe los sentidos: ceñirse a ella sin rebasarla. <b>Sin marca</b>: ceñirse al <b>eje de la calzada</b> sin invadir el sentido contrario. "
               "<b>Tres carriles</b> con discontinuas: colocarse en el <b>carril central</b>.")],
            [T("Squares, roundabouts, crossroads", "Plazas, glorietas y cruces"), T("Leave the <b>centre on your left</b>, unless the road is designed to leave it on the right.", "Dejar el <b>centro a la izquierda</b>, salvo que la vía esté acondicionada para dejarlo a la derecha.")],
            [T("Leaving by a <b>deceleration lane</b>", "Salir por un <b>carril de deceleración</b>"), T("Signal early, move to the lane next to it, <b>enter it as soon as possible</b> and slow down <b>inside it</b>.",
                                                                                                  "Señalizar con antelación, colocarse en el carril más próximo, <b>entrar en él lo antes posible</b> y reducir la velocidad <b>dentro</b> de él.")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(BOX("key", "Special cases", "Casos especiales", [
        ("If the vehicle’s <b>size</b> or other reasons stop you following these rules, take the precautions needed to avoid any danger.",
         "Si por las <b>dimensiones del vehículo</b> u otras circunstancias no se pueden aplicar estas normas, hay que adoptar las precauciones necesarias para evitar todo peligro."),
        ("On <b>interurban roads</b>, <b>cyclists and two-wheeled mopeds</b> turning <b>left</b> with no special lane wait on the <b>right-hand shoulder</b> if possible and start from there.",
         "En <b>vías interurbanas</b>, los <b>ciclos y ciclomotores de dos ruedas</b> que van a girar a la <b>izquierda</b> sin carril acondicionado se colocan en el <b>arcén de la derecha</b> si es posible y la inician desde allí."),
    ]))

    # ---------------------------------------------------------------- 7. turning round
    B.append(H2("7", "Turning round", "Cambio de sentido"))
    B.append(P(
        "A <b>half turn (180°)</b> to carry on along the same road in the opposite direction. <b>1 Observe</b> (if it is not safe, do not do it). <b>2 Signal</b> that you will slow down a lot and move sideways (lights or arm). "
        "<b>3 Turn</b> at a <b>suitable place</b>, as quickly as possible, in <b>one go and without reversing</b>. If waiting on the carriageway holds up those behind, <b>pull off to the right</b> if you can and wait there.",
        "Dar <b>media vuelta (180°)</b> para seguir por la misma vía en sentido contrario. <b>1.º Observar</b> (si no hay seguridad, abstenerse). <b>2.º Señalizar</b> la intención de frenar considerablemente y el desplazamiento lateral (luces o brazo). "
        "<b>3.º Realizar</b> en un <b>lugar adecuado</b>, en el menor tiempo posible, de <b>un solo giro y sin marcha atrás</b>. Si esperar en la calzada impide seguir a los de detrás, <b>salir por la derecha</b> si es posible y esperar allí."))
    B.append(TABLE(
        [T("Turning round is forbidden…", "Prohibido el cambio de sentido…")],
        [
            [T("Where <b>signs</b> forbid it, unless expressly authorised: no U-turn, no left turn, no overtaking, one-way signs, or a <b>continuous line</b>.",
               "Donde lo prohíba la <b>señalización</b>, salvo autorización expresa: prohibido cambiar de sentido, giro a la izquierda prohibido, adelantamiento prohibido, sentido único… o una <b>línea continua</b>.")],
            [T("As a rule, wherever <b>overtaking is forbidden</b>: poor visibility · <b>on level crossings</b> (near them it <b>is</b> allowed) · tunnels, underpasses and stretches signed “Tunnel” · pedestrian crossings and junctions with cycle routes, and near them.",
               "Como norma general, donde esté <b>prohibido adelantar</b>: falta de visibilidad · <b>pasos a nivel</b> (en sus proximidades <b>sí</b> está permitido) · túneles, pasos inferiores y tramos con la señal «Túnel» · pasos para peatones e intersecciones con vías ciclistas, y sus proximidades.")],
            [T("At <b>junctions</b> and near them, <b>except</b> where you have signed priority, and at roundabouts.", "En las <b>intersecciones</b> y sus proximidades, <b>salvo</b> donde se tenga prioridad señalizada y en glorietas.")],
            [T("On <b>autopistas and autovías</b>, except at the places built for it at a different level (over- or underpass). <b>Never</b> through an open gap in the <b>median</b>.",
               "En <b>autopistas y autovías</b>, salvo en los lugares habilitados a distinto nivel (paso superior o inferior). <b>Nunca</b> atravesando el paso abierto de la <b>mediana</b>.")],
        ],
    ))

    # ---------------------------------------------------------------- 8. reversing
    B.append(H2("8", "Reversing", "Marcha atrás"))
    B.append(P(
        "Reversing is <b>not a basic manoeuvre</b>: it only complements others. As a rule, <b>driving in reverse is forbidden</b> on every road. Exceptionally, it is allowed when you <b>cannot go forward, turn or turn round</b>, "
        "and only for the <b>shortest distance needed</b>.",
        "La marcha atrás <b>no es una maniobra básica</b>: es complementaria de otras. Como norma general, <b>está prohibido circular marcha atrás</b> en todas las vías. Excepcionalmente, se permite cuando <b>no sea posible marchar hacia delante ni cambiar de dirección o sentido</b>, "
        "y siempre con el <b>recorrido mínimo indispensable</b>."))
    B.append(BOX("key", "Reversing as part of another manoeuvre", "Marcha atrás complementaria", [
        ("Allowed to complete <b>stopping or parking</b> and <b>joining traffic</b>.", "Se permite como complemento de la <b>parada o estacionamiento</b> y de la <b>incorporación a la circulación</b>."),
        ("Then it may <b>not exceed 15 m</b> and must <b>not enter any junction</b>.", "En estos casos, el recorrido <b>no puede superar 15 metros</b> ni <b>invadir ninguna intersección</b>."),
        ("Reversing is <b>forbidden on autopistas and autovías</b>.", "Se <b>prohíbe la marcha atrás en autopistas y autovías</b>."),
    ]))
    B.append(TABLE(
        [T("Step", "Paso"), T("What to do", "Qué hacer")],
        [
            [T("<b>1 Observe</b>", "<b>1.º Observar</b>"), T("That you hinder and endanger nobody, <b>even getting out</b> to look or following <b>another person’s directions</b>.", "Que no se entorpece ni pone en peligro a nadie, <b>incluso bajándose del vehículo</b> o siguiendo las <b>indicaciones de otra persona</b>.")],
            [T("<b>2 Signal</b>", "<b>2.º Señalizar</b>"), T("With the <b>reversing light</b> (it comes on by itself), or the <b>arm horizontal, palm facing backwards</b>.", "Con la <b>luz de marcha atrás</b> (se enciende sola) o con el <b>brazo horizontal y la palma de la mano hacia atrás</b>.")],
            [T("<b>3 Reverse</b>", "<b>3.º Realizar</b>"), T("<b>Slowly</b> and with maximum care, stopping at once if you hear a warning, sense someone close or for safety. <b>Without total safety, do not do it.</b>",
                                                           "<b>Lentamente</b> y con la máxima precaución, deteniéndose rápidamente si se oyen avisos, se percibe a otro usuario o por seguridad. <b>Sin seguridad total, se desiste.</b>")],
        ],
        widths=["20%", "80%"],
    ))

    # ---------------------------------------------------------------- 9. immobilisations
    B.append(H2("9", "Stopping and parking", "Inmovilizaciones"))
    B.append(FIG(immobilisations, "Three ways a vehicle can be standing still. Only the stop and the parking are manoeuvres.",
                 "Tres formas de estar inmovilizado. Solo la parada y el estacionamiento son maniobras."))
    B.append(P(
        "A <b>detention</b> is imposed by an <b>emergency</b>, by <b>traffic needs</b>, or to <b>obey a rule</b> (agents, signs, lights). A <b>stop</b> (<i>parada</i>) is voluntary, lasts <b>under two minutes</b>, "
        "and the driver does not abandon the vehicle (they may get out if they keep watching it). <b>Parking</b> (<i>estacionamiento</i>) is any voluntary immobilisation that is neither.",
        "La <b>detención</b> viene impuesta por <b>emergencia</b>, por <b>necesidades de la circulación</b> o para <b>cumplir un precepto</b> (agentes, señales, semáforos). La <b>parada</b> es voluntaria, dura <b>menos de dos minutos</b> "
        "y el conductor no abandona el vehículo (puede bajarse si lo tiene vigilado). El <b>estacionamiento</b> es la inmovilización voluntaria que no es ni detención ni parada."))
    B.append(H3("9.1 Detentions", "9.1 Tipos de detención"))
    B.append(E(
        "Emergency: accident or breakdown", "Por emergencia: accidente o avería",
        "If the vehicle or its load blocks the carriageway (breakdown, fallen load, illness…), get it <b>off the carriageway and the usable shoulder</b> as soon as possible, following the parking rules where you can. "
        "If it can still move, <b>carry on</b>; if it needs help, leave the lanes and head for the <b>first exit on the right shoulder</b>, or stop on the right shoulder or where it obstructs least. "
        "If it cannot move: occupants get out if there is a <b>safe place off the road platform</b>, on the side <b>away from the traffic</b>, never walking or waiting on lanes or shoulders; otherwise they stay inside <b>with belts fastened</b>.",
        "Si el vehículo o su carga obstaculizan la calzada (avería, caída de la carga, malestar…), hay que sacarlo <b>de la calzada y de la parte transitable del arcén</b> cuanto antes, cumpliendo si es factible las normas de estacionamiento. "
        "Si puede continuar, <b>seguir</b>; si necesita auxilio, abandonar los carriles y dirigirse a la <b>primera salida por el arcén derecho</b>, o detenerse en el arcén derecho o donde menos estorbe. "
        "Si no puede reemprender la marcha: los ocupantes salen si hay un <b>lugar seguro fuera de la plataforma</b>, por el lado <b>contrario al tráfico</b>, sin transitar ni permanecer en carriles o arcenes; si no, se quedan dentro <b>con el cinturón abrochado</b>."))
    B.append(FIG(breakdown, "What to do when your car is stuck on an interurban road.",
                 "Qué hacer cuando el vehículo queda inmovilizado en una vía interurbana."))
    B.append(TABLE(
        [T("Signal the obstacle", "Señalizar el obstáculo")],
        [
            [T("Switch on the <b>hazard lights</b>.", "Encender la <b>luz o señal de emergencia</b>.")],
            [T("Place the <b>V-16</b> warning light.", "Colocar el <b>dispositivo de preseñalización de peligro</b> (señal luminosa <b>V-16</b>).")],
            [T("At night or in poor visibility, <b>position lights</b> on (and clearance lights, if fitted).", "De noche o con poca visibilidad, la <b>luz de posición</b> (y, en su caso, la de gálibo).")],
        ],
    ))
    B.append(BOX("key", "The V-16 light", "El dispositivo luminoso V-16", [
        ("<b>Compulsory</b> for cars, vans, buses, mixed vehicles, lorries and combinations (not special vehicles). <b>Recommended, not compulsory</b>, for motorcycles.",
         "<b>Obligatorio</b> para turismos, furgonetas, autobuses, vehículos mixtos, camiones y conjuntos no especiales. <b>Recomendable, no obligatorio</b>, para motocicletas."),
        ("An approved <b>flashing yellow</b> light that marks an immobilised vehicle or a fallen load. Place it on the <b>highest point</b> of the vehicle; it is visible <b>360°</b>.",
         "Dispositivo homologado de luz <b>amarilla auto</b> que indica un vehículo inmovilizado o una carga caída. Se coloca en la <b>parte más alta</b> del vehículo; visible en <b>360°</b>."),
        ("It switches on when you put it on the <b>metal roof</b> (magnetic). Its own battery must still work after <b>18 months</b>.",
         "Se activa al colocarlo <b>sobre el techo metálico</b> (imantado). Alimentación autónoma que debe garantizar su uso al cabo de <b>18 meses</b>."),
        ("Since <b>1 January 2026</b> only <b>connected</b>, approved models count; older unconnected lights are no longer valid.",
         "Desde el <b>1 de enero de 2026</b> solo valen los modelos <b>conectados</b> y homologados; las balizas no conectadas ya no son válidas."),
        ("It reports <b>activation, deactivation and location</b> to the national traffic access point by itself, with the cost included for <b>12 years</b> and no phone app needed.",
         "Comunica su <b>activación, desactivación y geolocalización</b> al punto de acceso nacional de tráfico, con el coste incluido durante <b>12 años</b> y sin depender de aplicaciones móviles."),
        ("The <b>triangle</b> may be used as well (you are not fined for it), but it <b>does not replace</b> the V-16: not using the V-16 can be fined even if you put a triangle.",
         "El <b>triángulo</b> puede colocarse además (no se multa por usarlo), pero <b>no sustituye</b> a la V-16: no usar la V-16 puede sancionarse aunque se ponga el triángulo."),
    ]))
    B.append(BOX("trap", "Vest and accident report", "Chaleco y parte de accidente", [
        ("Drivers of automobiles must wear an approved <b>high-visibility vest</b> when they get out and are on the <b>carriageway or shoulder of an interurban road</b>, by <b>day and night</b>.",
         "Los conductores de automóviles deben usar el <b>chaleco reflectante</b> homologado cuando salgan del vehículo y ocupen la <b>calzada o el arcén de vías interurbanas</b>, <b>de día y de noche</b>."),
        ("Filling in the <b>accident report</b> on the road platform is <b>forbidden</b>: do it somewhere safe off the road.",
         "Está <b>prohibido cumplimentar el parte de accidente</b> en la plataforma: se hace en un lugar seguro fuera de la vía."),
    ]))
    B.append(H3("9.1.1 In a tunnel or underpass", "9.1.1 En un túnel o paso inferior"))
    B.append(TABLE(
        [T("Case", "Caso"), T("What to do", "Qué hacer")],
        [
            [T("<b>Breakdown</b>", "<b>Avería</b>"),
             T("If you can move, <b>leave the tunnel</b>; if not, go to the nearest <b>emergency lay-by</b> ahead; otherwise stop as close as possible to the <b>right edge</b>. Then: <b>engine off</b>, position lights and <b>hazard lights</b> on; "
               "place and switch on the <b>V-16</b>; ask for help at the nearest <b>SOS post</b> and follow its instructions; everybody leaves the vehicle and goes quickly to the nearest <b>refuge or exit</b>, "
               "never along the carriageway if there are areas closed to traffic.",
               "Si puede continuar, <b>salir del túnel</b>; si no, ir a la <b>zona de emergencia</b> más cercana en su sentido (apartadero); si no, inmovilizar lo más cerca posible del <b>borde derecho</b>. Además: <b>parar el motor</b>, luz de posición y <b>luz de emergencia</b>; "
               "colocar y activar la <b>V-16</b>; pedir auxilio en el <b>poste S.O.S.</b> más próximo y seguir sus instrucciones; todos abandonan el vehículo hacia el <b>refugio o salida</b> más próximos, "
               "sin transitar por la calzada si hay zonas excluidas a la circulación.")],
            [T("<b>Fire</b>", "<b>Incendio</b>"),
             T("Pull <b>as far right</b> as possible so as not to block emergency vehicles; <b>engine off, key left in, doors open</b>; everybody goes quickly to the nearest refuge or exit, "
               "<b>away from the fire</b>, never along the carriageway if there are areas closed to traffic.",
               "<b>Aproximar el vehículo a la derecha</b> todo lo posible para no obstruir a los de emergencia; <b>apagar el motor, dejar la llave puesta y las puertas abiertas</b>; todos se dirigen rápidamente al refugio o salida más próximos, "
               "<b>en sentido contrario al fuego</b>, sin transitar por la calzada si hay zonas excluidas.")],
            [T("<b>Held up by traffic</b>", "<b>Por necesidades de la circulación</b>"),
             T("Stop <b>as far as possible</b> from the vehicle ahead; <b>switch off the engine</b> if you have to wait <b>more than 2 minutes</b> in any enclosed place; keep <b>position lights</b> on and use the <b>hazard lights</b> briefly to warn those behind.",
               "Detenerse <b>lo más lejos posible</b> del vehículo de delante; <b>apagar el motor</b> si se va a estar detenido <b>más de 2 minutos</b> en cualquier lugar cerrado; mantener la <b>luz de posición</b> y conectar la <b>luz de emergencia</b> temporalmente para avisar a los de detrás.")],
            [T("<b>Always</b>", "<b>Siempre</b>"),
             T("Obey the <b>lights and message panels</b> and the <b>loudspeaker</b> instructions; never enter if the entrance light forbids it (except emergency, mechanical assistance and road maintenance crews).",
               "Cumplir <b>semáforos y paneles</b> e instrucciones por <b>megafonía</b>; no entrar si el semáforo de entrada no lo permite (salvo servicios de urgencia, asistencia mecánica y conservación de carreteras).")],
        ],
        widths=["22%", "78%"],
        cls="small",
    ))
    B.append(H3("9.2 Stopping and parking: how", "9.2 Parada y estacionamiento"))
    B.append(TABLE(
        [T("Where", "Dónde"), T("Rule", "Norma")],
        [
            [T("<b>Everywhere</b>", "<b>Reglas generales</b>"), T("<b>Parallel</b> to the edge, <b>one behind another</b>; oblique or side-by-side (<i>en batería</i>) only if the road or circumstances advise it. Use the space well: <b>never take up two spaces</b>.",
                                                              "En <b>paralelo</b> al borde, <b>uno detrás de otro</b>; oblicuo o en batería solo si la vía u otras circunstancias lo aconsejan. Aprovechar el espacio: <b>no ocupar dos plazas</b>.")],
            [T("<b>Urban roads</b>", "<b>Vías urbanas</b>"), T("On the carriageway or the shoulder (even if usable), <b>as close as possible to the right edge</b> (except on one-way streets). <b>Both sides</b> on one-way streets; <b>only the right</b> on two-way streets. Plus municipal rules.",
                                                              "Dentro de la calzada y del arcén (aunque sea transitable), <b>lo más cerca posible del borde derecho</b> (salvo en sentido único). En <b>ambos lados</b> si es de sentido único; <b>solo en el derecho</b> si es de doble sentido. Más la normativa municipal.")],
            [T("<b>Interurban roads</b>", "<b>Vías interurbanas</b>"), T("<b>Always off the carriageway</b> and off the usable shoulder, on the <b>right-hand side</b>.", "<b>Siempre fuera de la calzada</b> y de la parte transitable del arcén, en el <b>lado derecho</b>.")],
        ],
        widths=["22%", "78%"],
    ))
    B.append(BOX("key", "What town councils may regulate", "Qué pueden regular los ayuntamientos", [
        ("<b>Time limits</b> for parking; and <b>removing or clamping</b> vehicles without a ticket in time-limited zones, or that stay <b>over three times the time paid</b>, until the driver is identified.",
         "<b>Limitaciones horarias</b> de estacionamiento; y la <b>retirada o inmovilización</b> de vehículos sin título en zonas limitadas o que <b>rebasen el triple del tiempo abonado</b>, hasta identificar al conductor."),
        ("Special rules for dropping off and picking up <b>children, older people and people with reduced mobility</b>, even in restricted zones.",
         "Normas para la subida y bajada de <b>niños, personas mayores y con movilidad reducida</b>, incluso en zonas restringidas."),
        ("Parking <b>fees</b> by vehicle size and environmental label; <b>tow trucks</b> may stop or park as long as needed to remove a vehicle; <b>two-wheelers</b> on pavements and pedestrian areas if pedestrians are not hindered.",
         "<b>Tarifas</b> según dimensiones y clasificación ambiental; parada o estacionamiento de <b>grúas de auxilio</b> el tiempo indispensable para retirar un vehículo; <b>vehículos de dos ruedas</b> en aceras y zonas peatonales sin perjudicar a los peatones."),
    ]))
    B.append(H3("9.3 Where you may not stop or park", "9.3 Prohibiciones"))
    B.append(TABLE(
        [T("No parking (stopping allowed)", "Prohibido estacionar (la parada sí)"), T("Serious offence if it obstructs or is dangerous", "Infracción grave si obstaculiza o es peligroso")],
        [
            [T("Time-limited spaces without a ticket or over the time · <b>loading and unloading</b> zones · spaces for <b>disabled</b> drivers · <b>pavements</b> and pedestrian areas · "
               "in front of a signed <b>dropped kerb</b> (<i>vado</i>) · <b>double parking</b> · where a sign, a <b>broken yellow line</b> or a <b>yellow zig-zag</b> forbids it",
               "Zonas de limitación horaria sin título o superado el tiempo · zonas de <b>carga y descarga</b> · zonas para <b>minusválidos</b> · <b>aceras</b>, paseos y zonas peatonales · "
               "delante de <b>vados</b> señalizados · en <b>doble fila</b> · donde lo prohíba una señal, una <b>línea amarilla discontinua</b> o una <b>marca en zig-zag</b>"),
             T("Loading zone <b>during its hours</b> · <b>double parking with no driver</b> · a signed <b>public transport stop</b> · spaces for <b>emergency and security services</b> · "
               "prohibited spaces on a road of <i>atención preferente</i> · the <b>middle of the carriageway</b>",
               "Carga y descarga <b>en horas de utilización</b> · <b>doble fila sin conductor</b> · <b>parada de transporte público</b> señalizada · espacios para <b>servicios de urgencia y seguridad</b> · "
               "espacios prohibidos en vía de <b>atención preferente</b> · en <b>medio de la calzada</b>")],
        ],
        widths=["50%", "50%"],
        cls="small",
    ))
    B.append(TABLE(
        [T("No stopping and no parking", "Prohibido parar y estacionar"), T("Serious offence if it obstructs or is dangerous", "Infracción grave si obstaculiza o es peligroso")],
        [
            [T("Bends and brows with reduced visibility, and near them · <b>tunnels</b>, underpasses and “Tunnel” stretches · <b>level crossings</b> · <b>pedestrian crossings</b> · "
               "<b>cycle lanes</b> and cycle crossings · <b>junctions</b> and near them (if it hinders turning; out of town, if it creates danger through lack of visibility) · "
               "where it <b>hides signs</b> · bus and taxi lanes, taxi ranks and bus stops · <b>autopistas and autovías</b> (except authorised areas) · on or too close to <b>tram rails</b> · "
               "lanes reserved for certain users · where a sign or a <b>continuous yellow line</b> forbids it",
               "Curvas y cambios de rasante de visibilidad reducida, y sus proximidades · <b>túneles</b>, pasos inferiores y tramos con la señal «Túnel» · <b>pasos a nivel</b> · <b>pasos para peatones</b> · "
               "<b>carriles bici</b> y pasos para ciclistas · <b>intersecciones</b> y sus proximidades (si dificulta el giro; en interurbanas, si genera peligro por falta de visibilidad) · "
               "donde se <b>impida la visibilidad de la señalización</b> · carriles bus/taxi y zonas de parada y estacionamiento del transporte público · <b>autopistas y autovías</b> (salvo zonas habilitadas) · "
               "sobre o junto a los <b>raíles del tranvía</b> · carriles reservados a determinados usuarios · donde lo prohíba una señal o una <b>línea amarilla continua</b>"),
             T("Less than <b>3 m</b> between the vehicle and the opposite edge or a continuous line, or no room for others to pass · blocking a properly parked vehicle from leaving · "
               "blocking access to a building for people or animals · blocking a signed <b>vado</b> · blocking <b>dropped kerbs</b> for disabled people · on <b>medians, separators, islands</b> · blocking an authorised turn",
               "Distancia <b>inferior a 3 m</b> entre el vehículo y el borde opuesto o una marca continua, o que no deje pasar a otros · impedir la incorporación de un vehículo correctamente parado o estacionado · "
               "obstaculizar la salida o acceso a un inmueble de personas o animales · obstaculizar un <b>vado</b> señalizado · obstaculizar <b>pasos rebajados</b> para disminuidos físicos · en <b>medianas, separadores, isletas</b> · impedir un giro autorizado")],
        ],
        widths=["58%", "42%"],
        cls="small",
    ))
    B.append(H3("9.4 Securing the vehicle", "9.4 Inmovilizar correctamente el vehículo"))
    B.append(P(
        "Before leaving the driver’s seat, make sure the vehicle cannot move and switch on any lights needed: <b>engine off</b> and starting system disconnected, precautions against <b>unauthorised use</b> if you walk away, "
        "and the <b>parking brake</b> on. On a slope: <b>first gear</b> facing uphill, <b>reverse gear</b> facing downhill, <b>P</b> with an automatic gearbox.",
        "Antes de abandonar el puesto de conducción hay que asegurar la inmovilización y encender las luces necesarias: <b>apagar el motor</b> y desconectar el arranque, precauciones contra el <b>uso sin autorización</b> si se aleja, "
        "y <b>freno de estacionamiento</b> accionado. En pendiente: <b>primera</b> si es ascendente, <b>marcha atrás</b> si es descendente, <b>posición P</b> con cambio automático."))
    B.append(FIG(park_slope, "On a slope, the gear and the front wheels both work against the car rolling away.",
                 "En pendiente, la marcha engranada y las ruedas delanteras impiden que el vehículo se desplace."))
    B.append(BOX("key", "Heavy vehicles and motorhomes", "Vehículos pesados y autocaravanas", [
        ("Vehicles <b>over 3,500 kg</b> MMA, <b>buses</b> and <b>combinations</b> must also be chocked: proper <b>chocks</b> (never <b>stones</b> or other improvised objects, removed when you leave), "
         "or a <b>front wheel against the kerb</b>, turned towards the centre of the road facing uphill and towards the kerb facing downhill.",
         "Los vehículos de <b>más de 3.500 kg</b> de MMA, <b>autobuses</b> y <b>conjuntos</b> deben dejarse además calzados: <b>calzos adecuados</b> (nunca <b>piedras</b> u otros elementos no destinados a ello, que se retiran al reanudar la marcha), "
         "o <b>apoyando una rueda directriz en el bordillo</b>, inclinadas hacia el centro de la calzada en pendiente ascendente y hacia fuera en descendente."),
        ("<b>Motorhomes</b> park <b>without extending anything</b> beyond the vehicle’s outline, resting <b>only on their tyres</b> (chocks or wedges allowed) and <b>without spilling fluids</b> from the living area.",
         "Las <b>autocaravanas</b> estacionan <b>sin extender elementos</b> que desborden su perímetro, apoyadas <b>solo sobre los neumáticos</b> (con posibilidad de calzos o cuñas) y <b>sin verter fluidos</b> del habitáculo."),
    ]))

    # ---------------------------------------------------------------- 10. traps
    B.append(H2("10", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("<b>Not manoeuvres</b>: a detention imposed by the road, following a bend or roundabout, and reversing (it only complements others).",
         "<b>No son maniobras</b>: la detención impuesta, la trayectoria curva (curva o glorieta) y la marcha atrás (es complementaria)."),
        ("Lights and arm disagree? The <b>arm</b> wins.", "¿Luces y brazo se contradicen? Prevalece el <b>brazo</b>."),
        ("Announcing an overtaking: <b>flashes</b> in and out of town; the <b>horn only out of town</b>.", "Avisar del adelantamiento: <b>ráfagas</b> dentro y fuera de poblado; <b>claxon solo fuera</b>."),
        ("Moving off after a red light or an agent’s order is <b>not</b> joining traffic.", "Reanudar la marcha tras un semáforo o un agente <b>no</b> es incorporación."),
        ("Out of a garage or private road: stop-at-once speed, giving way to <b>both sides</b>, pedestrians included.", "Desde un garaje o camino privado: velocidad para detenerse en el acto, cediendo a <b>ambos lados</b>, peatones incluidos."),
        ("Congested traffic, faster lane: <b>not</b> overtaking, and you may not change lanes to overtake.", "Tráfico congestionado, carril más rápido: <b>no</b> es adelantamiento, y no se puede cambiar de carril para adelantar."),
        ("Overtaking on the <b>right</b> is allowed: a car turning left, trams in the centre, in town with 2+ marked lanes.",
         "Se adelanta por la <b>derecha</b>: al que gira a la izquierda, al tranvía central, en poblado con 2 o más carriles delimitados."),
        ("Cyclists, pedestrians, mopeds, VMP, animals: <b>1.5 m</b>, and <b>−20 km/h</b> out of town. Broken-down vehicles and assistance vehicles: <b>−20 km/h in and out of town</b>.",
         "Ciclistas, peatones, ciclomotores, VMP, animales: <b>1,5 m</b> y <b>−20 km/h</b> fuera de poblado. Averiados y vehículos de auxilio: <b>−20 km/h dentro y fuera</b>."),
        ("Overtaking <b>two-wheelers</b> at a junction is allowed; overtaking <b>at a level crossing</b> is not.", "Adelantar a <b>vehículos de dos ruedas</b> en una intersección está permitido; en un <b>paso a nivel</b>, no."),
        ("You may cross a continuous line to pass a <b>broken-down</b> vehicle, but not one stopped <b>because of traffic</b>.",
         "Se puede rebasar una línea continua para pasar a un vehículo <b>averiado</b>, pero no a uno detenido <b>por el tráfico</b>."),
        ("Turning round: in <b>one go, without reversing</b>; on a level crossing no, <b>near</b> it yes; on a motorway <b>never through the median</b>.",
         "Cambio de sentido: de <b>un solo giro y sin marcha atrás</b>; en el paso a nivel no, en sus <b>proximidades</b> sí; en autopista, <b>nunca por la mediana</b>."),
        ("Reversing: <b>15 m</b> at most, never into a junction, <b>never on motorways</b>.", "Marcha atrás: <b>15 m</b> como máximo, sin invadir intersecciones, <b>nunca en autopista</b>."),
        ("Stop = <b>under 2 minutes</b>, driver with the vehicle. Double parking: stopping yes, parking no.", "Parada = <b>menos de 2 minutos</b> sin abandonar el vehículo. Doble fila: parar sí, estacionar no."),
        ("<b>Broken yellow line</b>: no parking. <b>Continuous yellow line</b>: no stopping and no parking.", "<b>Amarilla discontinua</b>: prohibido estacionar. <b>Amarilla continua</b>: prohibido parar y estacionar."),
        ("The triangle does <b>not</b> replace the V-16; the V-16 is <b>not compulsory</b> on motorcycles.", "El triángulo <b>no</b> sustituye a la V-16; la V-16 <b>no es obligatoria</b> en motocicletas."),
        ("Tunnel fire: <b>key in, doors open</b>, walk away from the fire. Waiting in a tunnel over 2 minutes: <b>engine off</b>.",
         "Incendio en túnel: <b>llave puesta y puertas abiertas</b>, alejarse del fuego. Esperar en un túnel más de 2 minutos: <b>motor apagado</b>."),
        ("Slope: uphill <b>1st gear</b>, downhill <b>reverse</b>; chocks never stones.", "Pendiente: subida <b>primera</b>, bajada <b>marcha atrás</b>; calzos, nunca piedras."),
    ]))

    # ---------------------------------------------------------------- 11. key numbers
    B.append(H2("11", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Side gap overtaking vulnerable users, immobilised and assistance vehicles", "Separación al adelantar a vulnerables, inmovilizados y vehículos de auxilio"), T("≥ 1.5 m", "≥ 1,5 m")],
            [T("Two-wheeler overtaking anything out of town", "Vehículo de dos ruedas que adelanta fuera de poblado"), T("≥ 1.5 m", "≥ 1,5 m")],
            [T("Speed reduction when overtaking (see 5.2)", "Reducción de velocidad al adelantar (ver 5.2)"), T("20 km/h below the limit", "20 km/h por debajo del límite")],
            [T("Reversing as part of another manoeuvre", "Marcha atrás complementaria"), T("≤ 15 m, no junction", "≤ 15 m, sin invadir intersecciones")],
            [T("Stop (parada)", "Parada"), T("&lt; 2 minutes", "&lt; 2 minutos")],
            [T("Engine off when held up in a tunnel or enclosed place", "Apagar el motor detenido en túnel o lugar cerrado"), T("&gt; 2 minutes", "&gt; 2 minutos")],
            [T("Removal in time-limited parking", "Retirada en estacionamiento limitado"), T("over 3 × the time paid", "más del triple del tiempo abonado")],
            [T("Serious offence: gap to the opposite edge or a continuous line", "Infracción grave: distancia al borde opuesto o a la línea continua"), T("&lt; 3 m", "&lt; 3 m")],
            [T("V-16: battery / communications included", "V-16: batería / comunicaciones incluidas"), T("works after 18 months / 12 years", "funciona a los 18 meses / 12 años")],
            [T("Chocks or kerb compulsory", "Calzos o bordillo obligatorios"), T("&gt; 3,500 kg MMA, buses, combinations", "&gt; 3.500 kg de MMA, autobuses, conjuntos")],
            [T("Turning round", "Cambio de sentido"), T("180°, one go, no reversing", "180°, un solo giro, sin marcha atrás")],
        ],
        widths=["58%", "42%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["bs3", "op4", "hn3", "jn3", "ov2", "ov6", "gp2", "no3", "tr3", "ut3", "rv2", "pk5"]


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
    ("Reglamento General de Circulación (RD 1428/2003), manoeuvres, stopping and parking (arts. 72–118) — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Ley sobre Tráfico, Circulación de Vehículos a Motor y Seguridad Vial (RDL 6/2015)", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722"),
    ("Real Decreto 518/2026 (reform of the Reglamento, in force 1 October 2026): overtaking cyclists and immobilised vehicles", "https://www.boe.es/eli/es/rd/2026/06/24/518"),
    ("La Moncloa, 30-09-2026: the reform comes into force",
     "https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/interior/paginas/2026/300926-reforma-reglamento-circulacion.aspx"),
    ("DGT: V-16 warning devices (approved connected models)", "https://www.dgt.es/muevete-con-seguridad/tecnologia-e-innovacion-en-carretera/Dispositivos-de-presenalizacion-V16/"),
    ("DGT press release, 25-11-2025: the connected V-16 is compulsory from 1 January 2026",
     "https://www.dgt.es/comunicacion/notas-de-prensa/20251125-dgt-recuerda-la-obligacion-de-disponer-de-la-baliza-v-16-para-senalizar-averias-y-accidentes-en-carretera/"),
    ("Revista DGT: the connected V-16 in 20 questions", "https://revista.dgt.es/es/reportajes/2025/10OCTUBRE/1015-N275-20Preguntas_V16conectada.shtml"),
]

GLOSSARY = [
    ("maniobra · progresión normal", "manoeuvre · normal progression"),
    ("retrovisor · señalizar", "mirror · to signal"),
    ("incorporación a la circulación", "joining traffic / moving off"),
    ("desplazamiento lateral · cambio de carril", "moving sideways · lane change"),
    ("adelantamiento · vehículo adelantado", "overtaking · vehicle being overtaken"),
    ("cambio de dirección", "turning (left or right)"),
    ("cambio de sentido", "turning round (U-turn)"),
    ("marcha atrás", "reversing"),
    ("intermitente · indicador de dirección", "indicator"),
    ("avisador acústico · claxon", "horn"),
    ("destellos · ráfagas", "headlight flashes"),
    ("contaminación acústica", "noise pollution"),
    ("camino privado · inmueble", "private road · building / property"),
    ("carril de aceleración / deceleración", "acceleration / deceleration lane"),
    ("circulación congestionada", "congested traffic"),
    ("separación lateral", "side gap"),
    ("vehículo de auxilio", "assistance / recovery vehicle"),
    ("ceñirse al borde", "keep close to the edge"),
    ("eje de la calzada", "centre of the carriageway"),
    ("mediana · paso a distinto nivel", "median · grade-separated crossing"),
    ("detención · parada · estacionamiento", "detention · stop · parking"),
    ("en doble fila · en batería · en línea", "double-parked · side by side · in line"),
    ("vado", "dropped kerb / driveway entrance"),
    ("zona de carga y descarga", "loading and unloading zone"),
    ("dispositivo de preseñalización de peligro (V-16)", "warning light (V-16)"),
    ("chaleco reflectante de alta visibilidad", "high-visibility vest"),
    ("parte de accidente", "accident report form"),
    ("poste S.O.S.", "emergency phone post"),
    ("luz de gálibo", "clearance light"),
    ("freno de estacionamiento", "parking brake"),
    ("calzo · bordillo", "chock · kerb"),
    ("autocaravana · habitáculo", "motorhome · living area"),
]
