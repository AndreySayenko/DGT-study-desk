# -*- coding: utf-8 -*-
"""Category A1/A2, Topic 5 content (manoeuvres), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Manual Permiso A1/A2, Tema 5: Las maniobras). The wording and
two figures are original; three figures are shared with Category B, Topic 5. The rules come from the Ley sobre Tráfico
(RDL 6/2015) and the Reglamento General de Circulación (RD 1428/2003, arts. 72–94, 109–110, 130 and 156) as amended
by RD 518/2026 (in force 1 October 2026), as they stand in November 2026.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import rider_arm_signals, two_wheel_overtake, overtake_cyclist, turn_positions, immobilisations


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Every manoeuvre follows three steps: <b>observe, signal, carry out</b>. The exam checks the <b>signals</b> (indicators, arm, horn, flashes) and the special rules of each manoeuvre.",
         "Toda maniobra sigue tres pasos: <b>observar, señalizar y realizar</b>. El examen comprueba las <b>señales</b> (intermitentes, brazo, claxon, ráfagas) y las normas propias de cada maniobra."),
        ("The heavy parts are <b>overtaking</b> (the 1.5 m gap, the −20 km/h rule, where it is forbidden) and <b>stopping and parking</b> (where it is forbidden and which cases are serious).",
         "Las partes más densas son el <b>adelantamiento</b> (la separación de 1,5 m, la reducción de 20 km/h, dónde está prohibido) y la <b>parada y el estacionamiento</b> (dónde están prohibidos y qué casos son graves)."),
        ("Since <b>1 October 2026</b> two old exceptions are gone: you may no longer overtake <b>two-wheelers at a level crossing</b>, nor overtake slowly at a <b>pedestrian crossing</b>. "
         "Some photo captions in your course still show them.",
         "Desde el <b>1 de octubre de 2026</b> han desaparecido dos excepciones: ya no se puede adelantar a <b>vehículos de dos ruedas en un paso a nivel</b>, ni adelantar despacio en un <b>paso para peatones</b>. "
         "Algunos pies de foto de tu curso aún las muestran."),
    ]))

    # ---------------------------------------------------------------- 1. what manoeuvres are
    B.append(H2("1", "What manoeuvres are", "¿Qué son las maniobras?"))
    B.append(P(
        "<b>Manoeuvres</b> are noticeable <b>changes in the vehicle’s position</b> on the carriageway compared with its normal progress. They must be <b>signalled in good time</b> "
        "and made only when they cause <b>no danger</b>, following the rules. In short: <b>observe, signal and carry out</b>.",
        "Son las <b>variaciones</b> o alteraciones sensibles de la <b>posición del vehículo en la calzada</b> con respecto a su circulación. Deben <b>señalizarse con antelación</b> "
        "y solo se realizarán cuando no representen <b>ningún peligro</b>, observando las normas. En resumen: <b>observar, señalizar y realizar</b>."))
    B.append(TABLE(
        [T("Basic manoeuvres", "Maniobras básicas de la circulación")],
        [
            [T("<b>Joining traffic</b> (<i>incorporación</i>) · <b>moving sideways</b> (<i>desplazamiento lateral</i>) · <b>overtaking</b> (<i>adelantamiento</i>)",
               "<b>Incorporación</b> · <b>desplazamiento lateral</b> · <b>adelantamiento</b>")],
            [T("<b>Turning</b> (<i>cambio de dirección</i>) · <b>turning round</b> (<i>cambio de sentido</i>) · <b>stopping or parking</b> (<i>parada o estacionamiento</i>)",
               "<b>Cambio de dirección</b> · <b>cambio de sentido</b> · <b>parada o estacionamiento</b>")],
        ],
    ))

    # ---------------------------------------------------------------- 2. warnings
    B.append(H2("2", "Riders’ warnings", "Advertencias de los conductores"))
    B.append(P("You must <b>announce every manoeuvre</b>, showing your intention <b>clearly and in good time</b>.",
               "Los conductores están <b>obligados a advertir las maniobras</b>, indicando su intención <b>de forma clara y con suficiente antelación</b>."))
    B.append(H3("2.1 Light and arm signals", "2.1 Advertencias ópticas"))
    B.append(P(
        "As a rule, use the <b>lights</b> (indicators, brake light), kept on for <b>the whole manoeuvre</b> and switched off when it ends; failing that, the <b>arm</b>, usually the <b>left</b> one. "
        "Arm signals only count when they are made <b>correctly</b> and are <b>visible to everyone</b>.",
        "Como norma general se usa la <b>señalización luminosa</b>, encendida <b>todo el tiempo que dure la maniobra</b> y apagada al terminar; en su defecto, el <b>brazo</b>, normalmente el <b>izquierdo</b>. "
        "Las señales con el brazo solo valen si se hacen <b>correctamente</b> y son <b>visibles para todos</b>."))
    B.append(FIG(rider_arm_signals, "On a motorcycle the right hand stays on the throttle, so arm signals are made with the left arm.",
                 "En moto la mano derecha va en el acelerador, así que las señales con el brazo se hacen con el izquierdo."))
    B.append(TABLE(
        [T("Manoeuvre", "Maniobra"), T("Light", "Luminosa"), T("Arm", "Brazo")],
        [
            [T("Move or turn <b>left</b>", "Desplazamiento o giro a la <b>izquierda</b>"), T("Left indicator", "Intermitente izquierdo"), T("Left arm <b>horizontal</b>, palm down", "Brazo izquierdo <b>horizontal</b>, palma hacia abajo")],
            [T("Move or turn <b>right</b>", "Desplazamiento o giro a la <b>derecha</b>"), T("Right indicator", "Intermitente derecho"), T("Left arm <b>bent upwards</b>, palm extended", "Brazo izquierdo <b>doblado hacia arriba</b>, palma extendida")],
            [T("<b>Slow down</b> a lot or stop", "<b>Frenar</b> considerablemente o detenerse"), T("Brake light, used repeatedly", "Luz de freno, de forma reiterada"), T("Arm moved <b>up and down</b>, short quick movements", "Brazo de <b>arriba abajo</b>, movimientos cortos y rápidos")],
            [T("<b>Reverse</b> (vehicles that can)", "<b>Marcha atrás</b> (si el vehículo la tiene)"), T("Reversing light", "Luz de marcha atrás"), T("Arm <b>horizontal</b>, palm <b>backwards</b>", "Brazo <b>horizontal</b>, palma <b>hacia atrás</b>")],
        ],
        widths=["32%", "28%", "40%"],
        cls="small",
    ))
    B.append(BOX("key", "If they contradict each other", "En caso de contradicción", [
        ("According to your course, when the lights and the arm say different things, the <b>arm signal prevails</b>.",
         "Según tu curso, en caso de contradicción, las advertencias hechas con el <b>brazo prevalecen</b> sobre las luminosas."),
    ]))

    B.append(H3("2.2 Horn and headlight flashes", "2.2 Advertencias acústicas y destellos"))
    B.append(P(
        "The horn is <b>exceptional</b>: it warns others that you are there. Non-priority vehicles may use it <b>in and out of town</b> to <b>avoid a possible accident or running someone over</b> "
        "(above all on <b>narrow, winding roads</b>) and on an <b>emergency trip</b>; and <b>only out of town</b> to <b>announce that you are going to overtake</b>.",
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
        "The horn", "El claxon",
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
        "<b>Joining traffic</b> is starting to ride (from stopped or parked, or out of a garage) or entering another road (from a slip road, a service area…). "
        "Moving off again after a <b>detention</b> ordered by agents or lights, or caused by normal traffic, is <b>not</b> joining. "
        "<b>Observe</b> (directly and in the mirrors), <b>signal</b> (indicator for the side you move to, or the arm) and <b>join</b> safely without forcing anyone to change position or speed abruptly, "
        "<b>giving way</b> to vehicles already on the road.",
        "La <b>incorporación</b> es la maniobra para <b>comenzar a circular</b> (vehículo parado o estacionado, saliendo de un garaje…) o para entrar en otra vía (desde vías de acceso o zonas de servicio…). "
        "<b>No</b> es incorporación reanudar la marcha tras una <b>detención</b> ordenada por agentes o semáforos o impuesta por la circulación normal. "
        "Hay que <b>observar</b> (directamente y por los retrovisores), <b>señalizar</b> (intermitente del lado hacia el que nos desplazamos o, en su defecto, el brazo) y <b>ejecutarla</b> sin peligro ni obligar a nadie a modificar bruscamente su posición o velocidad, "
        "<b>cediendo el paso</b> a los que ya circulan."))
    B.append(E(
        "From a building or private road", "Desde un inmueble o camino privado",
        "Ride at a speed that lets you <b>stop at once</b> to give way to <b>vehicles and pedestrians</b> coming <b>from the right and from the left</b>.",
        "Circular a una velocidad que permita <b>detenerse en el acto</b> para ceder el paso a los <b>vehículos y peatones</b> que se aproximen <b>tanto por la derecha como por la izquierda</b>."))
    B.append(E(
        "From an acceleration lane", "Desde un carril de aceleración",
        "At the <b>start</b> of the lane make sure you can join safely, giving way to traffic on the main road (<b>stopping there if necessary</b>); then <b>speed up</b> to the right speed by the <b>end</b> of the lane.",
        "Al <b>principio</b> del carril, asegurarse de que se puede hacer con seguridad, cediendo el paso a los de la vía principal (<b>deteniéndose allí si fuera necesario</b>); y <b>aumentar la velocidad</b> hasta la adecuada al <b>final</b> del carril."))
    B.append(H3("3.1 Helping others join", "3.1 Obligación de facilitar la maniobra"))
    B.append(P(
        "When you see someone trying to join, help them <b>as far as you can</b>, above all a <b>bus leaving a signed stop</b>. In town, to let it out you <b>move sideways</b> when possible, "
        "or <b>slow down</b> if it is safe and signalled, <b>stopping if necessary</b>. The bus driver must still take every precaution after signalling with the indicators.",
        "Quien vea a otro intentando incorporarse debe <b>facilitarle la maniobra en la medida de lo posible</b>, sobre todo a un <b>autobús que sale de una parada señalizada</b>. En poblado, hay que "
        "<b>desplazarse lateralmente</b> cuando sea posible, o <b>reducir la velocidad</b> sin peligro y señalizándolo, <b>llegando a detenerse si fuera preciso</b>. El conductor del autobús debe igualmente "
        "adoptar las precauciones necesarias tras anunciar con los intermitentes que reanuda la marcha."))

    # ---------------------------------------------------------------- 4. moving sideways
    B.append(H2("4", "Moving sideways", "Desplazamiento lateral"))
    B.append(P(
        "Any change of position on the carriageway, left or right, that moves you <b>partly or fully into a lane you were not using</b> (a <b>lane change</b>). "
        "A <b>small correction within your own lane</b> is not one.",
        "Cualquier cambio de posición en la calzada, a izquierda o derecha, que implique la <b>invasión parcial o total de un carril</b> por el que no se circulaba (<b>cambio de carril</b>). "
        "<b>No</b> lo es la <b>simple corrección de trayectoria dentro del carril</b>."))
    B.append(TABLE(
        [T("When it is done", "Cuándo se realiza"), T("How to do it", "Cómo se realiza")],
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
    B.append(H3("5.1 How to overtake", "5.1 ¿Cómo se debe adelantar?"))
    B.append(P("Always safely, without endangering or hindering anyone. <b>If it is not 100 % safe, do not overtake.</b>",
               "Siempre con seguridad, sin poner en peligro ni entorpecer a otros usuarios. <b>Si no hay seguridad al 100 %, no se adelanta.</b>"))
    B.append(TABLE(
        [T("Before you start", "Antes de iniciar la maniobra")],
        [
            [T("<b>1</b> Keep a <b>suitable distance</b> behind, which lets you check there is <b>room to overtake</b> without danger.",
               "<b>1.º</b> Mantener una <b>separación adecuada</b> con el vehículo que se quiere adelantar que permita comprobar que hay <b>espacio suficiente para adelantar</b> sin peligro.")],
            [T("<b>2</b> Check there is room to <b>get back to the right</b> when you finish.", "<b>2.º</b> Comprobar que hay espacio suficiente para <b>volver a la derecha</b> al terminar.")],
            [T("<b>3</b> Check the vehicle ahead has <b>not signalled</b> a move to the same side (if so, it goes first; if after a reasonable time it does not move, you may overtake after warning it with the horn or lights), "
               "and that those behind you have <b>not started overtaking you</b>.",
               "<b>3.º</b> Comprobar que el de delante <b>no ha indicado</b> su propósito de desplazarse hacia el mismo lado (si lo ha hecho, tiene preferencia; si tras un tiempo prudencial no lo hace, se le puede adelantar avisando con señales acústicas u ópticas), "
               "y que los que le siguen <b>no han iniciado la maniobra de adelantarle</b>.")],
            [T("<b>4</b> If you need to move sideways, <b>signal early</b>, and stop signalling once you are in position.",
               "<b>4.º</b> Si requiere desplazamiento lateral, <b>advertirlo con suficiente antelación</b> y finalizar la señal cuando el vehículo esté en su posición adecuada.")],
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
        "Finishing: get back to the <b>right-hand lane</b> as soon as you can, <b>gradually</b>, without forcing anyone to change path or speed (when you see the overtaken vehicle in your mirrors).",
        "Al finalizar: volver al <b>carril de la derecha</b> tan pronto como sea posible y de forma <b>gradual</b>, sin obligar a nadie a modificar su trayectoria o velocidad (cuando se vea al adelantado por los espejos)."))
    B.append(BOX("trap", "Two rules to remember", "Dos normas que recordar", [
        ("If, once started, you see you <b>cannot finish safely</b>, <b>slow down quickly and return</b> to the right-hand lane, signalling it.",
         "Si una vez iniciado se percibe dificultad para finalizarlo sin peligro, se <b>reduce rápidamente la velocidad y se regresa</b> al carril de la derecha, señalizándolo."),
        ("With <b>at least two lanes</b> in your direction, for a <b>new overtaking</b> you may <b>stay in the lane</b> you used, as long as you do not bother faster vehicles behind.",
         "En calzadas con <b>al menos dos carriles</b> en el mismo sentido, para un <b>nuevo adelantamiento</b> se puede <b>permanecer en el carril</b> utilizado, si no se molesta a los que vienen detrás más rápido."),
    ]))

    B.append(H3("5.2 Side gap when overtaking", "5.2 Distancia de seguridad al adelantar"))
    B.append(TABLE(
        [T("Overtaking…", "Al adelantar a…"), T("Gap", "Separación")],
        [
            [T("<b>Pedestrians, animals, animal-drawn vehicles, mopeds, VMP, cyclists</b> or groups of cyclists; vehicles <b>immobilised</b> by a breakdown or accident; "
               "<b>assistance vehicles</b> at work (in and out of town)",
               "<b>Peatones, animales, vehículos de tracción animal, ciclomotores, VMP, ciclistas</b> o conjuntos de ciclistas; vehículos <b>inmovilizados</b> por avería o accidente; "
               "<b>vehículos de auxilio</b> en operaciones de auxilio y rescate (dentro y fuera de poblado)"),
             T("Move <b>partly or fully</b> into the next or opposite lane (a <b>full lane change</b> if there is more than one lane your way), when the rules allow it; side gap <b>never under 1.5 m</b>.",
               "Ocupar <b>parcial o totalmente</b> el carril contiguo o contrario (<b>cambio completo de carril</b> si hay más de uno por sentido), si se dan las condiciones reglamentarias; separación lateral <b>no inferior a 1,50 m</b>.")],
            [T("<b>Any other vehicle</b>", "<b>Cualquier otro vehículo</b>"), T("A side gap <b>proportional</b> to the speed and to the width and features of the carriageway.", "Separación lateral <b>proporcional</b> a la velocidad y a la anchura y características de la calzada.")],
            [T("Your <b>motorcycle</b> (a two-wheeler) overtaking anything, <b>out of town</b>", "Tu <b>moto</b> (vehículo de dos ruedas) adelantando a otro cualquiera, <b>fuera de poblado</b>"),
             T("At least <b>1.5 m</b> between you and the most protruding part of the other vehicle.", "Al menos <b>1,50 m</b> entre tú y la parte más saliente del otro vehículo.")],
        ],
        widths=["50%", "50%"],
        cls="small",
    ))
    B.append(FIG(overtake_cyclist, "Overtaking a cyclist: side gap of at least 1.5 m and, out of town, 20 km/h below the road’s limit.",
                 "Adelantar a un ciclista: separación lateral mínima de 1,5 m y, fuera de poblado, 20 km/h por debajo del límite de la vía."))
    B.append(BOX("key", "When you must slow down by 20 km/h below the road’s limit", "Cuándo reducir 20 km/h respecto al límite de la vía", [
        ("<b>Out of town</b>: overtaking pedestrians, animals, animal-drawn vehicles, mopeds, VMP, cyclists or groups of cyclists.",
         "<b>Fuera de poblado</b>: al adelantar a peatones, animales, vehículos de tracción animal, ciclomotores, vehículos de movilidad personal, ciclistas o conjuntos de ciclistas."),
        ("<b>In and out of town</b>: passing vehicles immobilised by a breakdown or accident, or assistance vehicles at work (rescue, road maintenance, traffic management).",
         "<b>Dentro y fuera de poblado</b>: al adelantar a vehículos inmovilizados por avería o accidente, o a vehículos de auxilio trabajando (auxilio y rescate, mantenimiento de la vía, regulación y gestión del tráfico)."),
        ("It is <b>forbidden</b> to overtake if that endangers or hinders <b>cyclists coming the other way</b>, even on the shoulder. A group of cyclists counts as <b>one moving unit</b>.",
         "Está <b>prohibido</b> adelantar poniendo en peligro o entorpeciendo a <b>ciclistas que circulen en sentido contrario</b>, incluso por el arcén. Un grupo de ciclistas es <b>una única unidad móvil</b>."),
    ]))
    B.append(FIG(two_wheel_overtake, "Three rules where being on two wheels changes the answer.",
                 "Tres normas en las que ir en dos ruedas cambia la respuesta."))

    B.append(H3("5.3 What the overtaken vehicle must do", "5.3 ¿Qué debe hacer el vehículo adelantado?"))
    B.append(TABLE(
        [T("Duty", "Obligación"), T("Detail", "Detalle")],
        [
            [T("<b>Position</b>", "<b>Posición adecuada</b>"), T("Keep to the <b>right edge</b> of the carriageway (not on the shoulder). If you want to turn or stop on the left, keep as far left as possible without getting in the way of oncoming traffic.",
                                                                "<b>Ceñirse al borde derecho</b> de la calzada (sin pisar el arcén). Si se quiere girar o inmovilizar a la izquierda, ceñirse a la izquierda todo lo posible sin interferir a los del sentido contrario.")],
            [T("<b>Speed</b>", "<b>Velocidad adecuada</b>"), T("<b>Never speed up</b> or make the overtaking harder. <b>Slow down</b> if a danger arises once it has started; if the overtaker gives up and slows down, <b>let them back in</b>.",
                                                             "<b>Prohibido aumentar la velocidad</b> o dificultar el adelantamiento. <b>Disminuir la velocidad</b> si, iniciado, surge un peligro; si el que adelanta desiste y reduce, <b>facilitarle la vuelta al carril</b>.")],
        ],
        widths=["26%", "74%"],
    ))

    B.append(H3("5.4 Where overtaking is forbidden", "5.4 ¿Dónde está prohibido adelantar?"))
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
            [T("<b>Other places</b>", "<b>Otros casos</b>"), T("<b>Level crossings</b>, <b>pedestrian crossings</b> and junctions with <b>cycle routes</b>, and near them · <b>tunnels</b>, underpasses and “Tunnel” stretches with <b>one lane</b> your way · "
                                                               "a vehicle that is <b>already overtaking</b> another, if you would have to enter the opposite direction.",
                                                               "<b>Pasos a nivel</b>, <b>pasos para peatones</b> e intersecciones con <b>vías ciclistas</b>, y sus proximidades · <b>túneles</b>, pasos inferiores y tramos con la señal «Túnel» con <b>un solo carril</b> para tu sentido · "
                                                               "a los que <b>ya están adelantando</b>, si hay que invadir el sentido contrario.")],
        ],
        widths=["24%", "76%"],
        cls="small",
    ))
    B.append(E(
        "Your course is out of date on two photos", "Tu curso está desactualizado en dos fotos",
        "Its captions say “level crossing (except two-wheelers)” and “pedestrian crossing (if your speed lets you stop)”. Those two exceptions were <b>deleted on 1 October 2026</b> (RD 518/2026): "
        "today overtaking at level crossings and pedestrian crossings, and near them, is forbidden <b>with no exceptions</b>.",
        "Sus pies de foto dicen «paso a nivel (excepto dos ruedas)» y «paso de peatones (velocidad que permita detenerse)». Esas dos excepciones se <b>suprimieron el 1 de octubre de 2026</b> (RD 518/2026): "
        "hoy está prohibido adelantar en pasos a nivel y pasos para peatones, y en sus proximidades, <b>sin excepciones</b>.",
        pills_=[T("no exceptions since 1-10-2026", "sin excepciones desde el 1-10-2026")]))

    B.append(H3("5.5 Special cases", "5.5 Supuestos especiales de adelantamiento"))
    B.append(P(
        "You may use the opposite half of the road, <b>even where signs forbid overtaking</b>, to: pass an <b>obstacle or immobilised vehicle</b> blocking your lane (breakdown, accident…), after making sure there is no danger "
        "— but if it has stopped <b>because of the traffic</b>, you stay behind it; and overtake <b>cycles, mopeds, VMP, pedestrians, animals, animal-drawn vehicles and agricultural special vehicles</b> "
        "when their speed lets you do it without risk.",
        "Se puede ocupar la parte reservada al sentido contrario, <b>incluso cuando esté prohibido por la señalización</b>, para: rebasar un <b>obstáculo o un vehículo inmovilizado</b> (avería, accidente…) que ocupe su carril, tras asegurarse de que no hay peligro "
        "(pero si la inmovilización responde a <b>necesidades del tráfico</b>, hay que quedarse detrás); y adelantar a <b>ciclos, ciclomotores, VMP, peatones, animales, vehículos de tracción animal y vehículos especiales agrícolas</b> "
        "cuando su velocidad permita hacerlo sin riesgo."))

    # ---------------------------------------------------------------- 6. turning
    B.append(H2("6", "Turning", "Cambio de dirección"))
    B.append(P(
        "Turning left or right to <b>use another road</b>, take <b>another carriageway</b> of the same road, or <b>leave</b> the road. Leaning into a bend to <b>follow the road</b> is not a manoeuvre. "
        "<b>1 Observe</b> that you can do it without hindering or endangering anyone (speed and distance of those approaching), or do not do it. <b>2 Signal</b> in good time to those behind. <b>3 Turn</b> from the right position:",
        "Maniobra para girar a izquierda o derecha y <b>utilizar otra vía</b>, tomar <b>otra calzada</b> de la misma vía o <b>salir de la vía</b>. <b>No</b> es maniobra el giro para <b>seguir el trazado de una curva</b>. "
        "<b>1.º Observar</b> que se puede hacer sin entorpecer ni poner en peligro a nadie (velocidad y distancia de los que se acercan), o abstenerse. <b>2.º Señalizar</b> con suficiente antelación a los que circulan detrás. <b>3.º Realizar</b> la maniobra:"))
    B.append(FIG(turn_positions, "Before turning, position yourself on the side you are turning to, as far as the road allows.",
                 "Antes de girar, colócate en el lado hacia el que giras, todo lo que permita la vía."))
    B.append(TABLE(
        [T("Turn", "Giro"), T("Position", "Posición")],
        [
            [T("<b>Right</b>", "<b>A la derecha</b>"), T("As close as possible to the <b>right edge</b>.", "Ceñirse todo lo posible al <b>borde derecho</b>.")],
            [T("<b>Left</b>, one-way road", "<b>A la izquierda</b>, sentido único"), T("As close as possible to the <b>left edge</b>.", "Ceñirse todo lo posible al <b>borde izquierdo</b>.")],
            [T("<b>Left</b>, two-way road", "<b>A la izquierda</b>, doble sentido"),
             T("With a marking separating the directions: next to it, <b>without crossing it</b>. Without one: next to the <b>centre of the carriageway</b>, without entering the opposite side. "
               "With <b>three lanes</b> separated by broken lines: the <b>centre lane</b>.",
               "Con marca vial que separe los sentidos: ceñirse a ella <b>sin rebasarla</b>. Sin marca: ceñirse al <b>eje de la calzada</b> sin invadir el sentido contrario. "
               "Con <b>tres carriles</b> separados por discontinuas: colocarse en el <b>carril central</b>.")],
            [T("Squares, roundabouts, junctions", "Plazas, glorietas y encuentros de vías"), T("Leave the <b>centre on your left</b>, unless the road is laid out otherwise.", "Dejar a la <b>izquierda el centro</b>, salvo que la vía esté acondicionada para dejarlo a la derecha.")],
            [T("Leaving by a <b>deceleration lane</b>", "Salir por un <b>carril de deceleración</b>"), T("Signal early, move to the lane next to it without hindering anyone, <b>enter it as soon as possible</b> and slow down <b>inside it</b>.",
                                                                                              "Señalizar con antelación, situarse en el carril contiguo sin entorpecer, <b>entrar en él lo antes posible</b> y reducir la velocidad <b>ya dentro</b>.")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(BOX("trap", "Mopeds and bicycles are different", "Ciclomotores y bicicletas son distintos", [
        ("On interurban roads, <b>cycles and two-wheeled mopeds</b> turning <b>left</b> with no special lane wait on the <b>right-hand shoulder</b> if possible. A <b>motorcycle</b> does not: it turns from the centre of the road like a car.",
         "En vías interurbanas, los <b>ciclos y ciclomotores de dos ruedas</b> que giran a la <b>izquierda</b> sin carril acondicionado esperan en el <b>arcén derecho</b> si es posible. La <b>motocicleta</b> no: gira desde el eje como un turismo."),
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
            [T("As a rule, wherever <b>overtaking is forbidden</b>: poor visibility · <b>on level crossings</b> (near them your course says it <b>is</b> allowed) · tunnels, underpasses and “Tunnel” stretches · pedestrian crossings and junctions with cycle routes, and near them.",
               "Como norma general, donde esté <b>prohibido adelantar</b>: falta de visibilidad · <b>pasos a nivel</b> (en sus proximidades, según tu curso, <b>sí</b> está permitido) · túneles, pasos inferiores y tramos con la señal «Túnel» · pasos para peatones e intersecciones con vías ciclistas, y sus proximidades.")],
            [T("At <b>junctions</b> and near them, <b>except</b> where you have signed priority, and at roundabouts.", "En las <b>intersecciones</b> y sus proximidades, <b>salvo</b> donde se tenga prioridad señalizada y en glorietas.")],
            [T("On <b>autopistas and autovías</b>, except at the places built for it at a different level (over- or underpass).", "En <b>autopistas y autovías</b>, salvo en los lugares habilitados a distinto nivel (paso superior o inferior).")],
        ],
    ))
    B.append(BOX("trap", "Never through the median", "Nunca por la mediana", [
        ("On autopistas and autovías you may <b>never</b> turn round by crossing an <b>open gap in the median</b>.", "En autopistas y autovías <b>nunca</b> se puede atravesar el <b>paso abierto de la mediana</b> para cambiar de sentido."),
    ]))

    # ---------------------------------------------------------------- 8. immobilisations
    B.append(H2("8", "Stopping and parking", "Inmovilizaciones"))
    B.append(FIG(immobilisations, "Three ways of standing still. Only the stop and the parking are manoeuvres.",
                 "Tres formas de estar inmovilizado. Solo la parada y el estacionamiento son maniobras."))
    B.append(TABLE(
        [T("Type", "Tipo"), T("What it is", "Qué es")],
        [
            [T("<b>Detention</b> (<i>detención</i>)", "<b>Detención</b>"), T("<b>Not voluntary</b> and not a manoeuvre: imposed by an <b>emergency</b>, by <b>traffic needs</b>, or to <b>obey a rule</b> (agents, signs, lights).",
                                                                            "<b>No es voluntaria</b> ni es maniobra: viene impuesta por <b>emergencia</b>, por <b>necesidades de la circulación</b> o para <b>cumplir un precepto</b> (agentes, señales, semáforos).")],
            [T("<b>Stop</b> (<i>parada</i>)", "<b>Parada</b>"), T("<b>Voluntary</b>, for <b>less than two minutes</b>, without the rider <b>abandoning</b> the vehicle (you may get off as long as you keep watching it).",
                                                                 "<b>Voluntaria</b>, durante <b>menos de dos minutos</b>, sin que el conductor <b>abandone</b> el vehículo (puede bajarse si lo tiene vigilado).")],
            [T("<b>Parking</b> (<i>estacionamiento</i>)", "<b>Estacionamiento</b>"), T("Any <b>voluntary</b> immobilisation that is neither a detention nor a stop.", "Inmovilización <b>voluntaria</b> que no es ni detención ni parada.")],
        ],
        widths=["26%", "74%"],
    ))
    B.append(H3("8.1 Detention", "8.1 Detención"))
    B.append(P(
        "A detention in a <b>tunnel or other enclosed place</b> for <b>more than two minutes</b> means you <b>switch off the engine</b> and keep the <b>position lights</b> on.",
        "La detención en un <b>túnel o lugar cerrado</b> durante <b>más de dos minutos</b> obliga a <b>parar el motor</b>, conservando encendidas las <b>luces de posición</b>."))
    B.append(BOX("key", "If your motorcycle breaks down out of town", "Si tu moto se avería fuera de poblado", [
        ("If you can still ride, <b>carry on</b>; if you need help, leave the lanes and head for the <b>first exit along the right shoulder</b>, or stop on the right shoulder or where you obstruct least.",
         "Si puede seguir, <b>continúa</b>; si necesitas auxilio, abandona los carriles y dirígete a la <b>primera salida por el arcén derecho</b>, o detente en el arcén derecho o donde menos estorbes."),
        ("Get yourself <b>off the road platform</b> to a safe place, on the side away from the traffic. Since 1 October 2026 every motorcycle must carry a <b>high-visibility vest</b>: wear it if you get off onto the carriageway or shoulder.",
         "Sal de la <b>plataforma</b> a un lugar seguro, por el lado contrario al tráfico. Desde el 1 de octubre de 2026 toda motocicleta debe llevar un <b>chaleco de alta visibilidad</b>: póntelo si bajas a la calzada o al arcén."),
        ("The connected <b>V-16</b> warning light is compulsory for cars, vans, buses and lorries; for motorcycles it is <b>recommended, not compulsory</b>.",
         "La señal <b>V-16</b> conectada es obligatoria en turismos, furgonetas, autobuses y camiones; en motocicletas es <b>recomendable, no obligatoria</b>."),
    ]))

    B.append(H3("8.2 Stopping and parking", "8.2 Parada y estacionamiento"))
    B.append(TABLE(
        [T("Where", "Dónde"), T("Rule", "Norma")],
        [
            [T("<b>General rules</b>", "<b>Reglas generales</b>"), T("<b>Parallel</b> to the edge, <b>one behind another</b> (in line); oblique or side-by-side (<i>en batería</i>) only if the road or circumstances advise it. "
                                                                    "Use the space well: <b>never take up two spaces</b>.",
                                                                    "En <b>paralelo</b> al borde de la calzada, <b>uno detrás de otro</b> (en línea); oblicuo o en batería solo si la vía u otras circunstancias lo aconsejan. "
                                                                    "Permitir la mejor utilización del espacio: <b>no ocupar dos plazas</b>.")],
            [T("<b>Urban roads</b>", "<b>Vías urbanas</b>"), T("On the carriageway or the shoulder, <b>as close as possible to the right edge</b>. <b>Both sides</b> on one-way streets; <b>only the right</b> on two-way streets. Plus municipal rules.",
                                                              "En la calzada o el arcén, <b>lo más cerca posible del borde derecho</b>. En <b>ambos lados</b> si la vía es de sentido único; <b>solo en el derecho</b> si es de doble sentido. Más la normativa municipal.")],
            [T("<b>Interurban roads</b>", "<b>Vías interurbanas</b>"), T("<b>Always off the carriageway</b>, on the <b>right</b>, leaving the usable part of the shoulder free.", "<b>Siempre fuera de la calzada</b>, en el <b>lado derecho</b>, dejando libre la parte transitable del arcén.")],
        ],
        widths=["22%", "78%"],
    ))
    B.append(E(
        "Motorcycles on pavements: only if the town allows it", "Motos en las aceras: solo si lo permite el ayuntamiento",
        "Parking on <b>pavements</b>, promenades and pedestrian areas is forbidden. Town councils may, by <b>bylaw</b>, allow <b>two-wheelers</b> to stop and park there as long as pedestrians are "
        "<b>not hindered</b>, paying special attention to people with reduced mobility or disabilities.",
        "Está prohibido estacionar en <b>aceras</b>, paseos y zonas peatonales. Los ayuntamientos pueden, por <b>ordenanza</b>, regular la parada y el estacionamiento de <b>vehículos de dos ruedas</b> en ellas siempre que "
        "<b>no se perjudique ni entorpezca</b> a los peatones, atendiendo especialmente a las personas con movilidad reducida o discapacidad.",
        pills_=[T("municipal bylaw", "ordenanza municipal"), T("pedestrians first", "el peatón primero")]))

    B.append(H3("8.3 Where you may not stop or park", "8.3 Prohibiciones"))
    B.append(TABLE(
        [T("No parking (stopping allowed)", "Prohibido estacionar (la parada sí)"), T("Serious offence if it obstructs or is dangerous", "Infracción grave si obstaculiza gravemente o es peligroso")],
        [
            [T("Time-limited spaces without a ticket or over the time (if you exceed <b>three times the time paid</b>, the council may remove or clamp the vehicle) · <b>loading and unloading</b> zones · spaces for <b>disabled</b> drivers · "
               "<b>pavements</b> and pedestrian areas · in front of a signed <b>dropped kerb</b> (<i>vado</i>) · <b>double parking</b> · where a sign, a <b>broken yellow line</b> or a <b>yellow zig-zag</b> forbids it",
               "Zonas de limitación horaria sin título o superado el tiempo (si se rebasa el <b>triple del tiempo abonado</b>, el ayuntamiento puede retirar o inmovilizar el vehículo) · zonas de <b>carga y descarga</b> · zonas para <b>minusválidos</b> · "
               "<b>aceras</b>, paseos y zonas peatonales · delante de <b>vados</b> señalizados · en <b>doble fila</b> · donde lo prohíba una señal, una <b>línea amarilla discontinua</b> o una <b>marca en zig-zag</b>"),
             T("Loading zone <b>during its hours</b> · <b>double parking with no driver</b> · a signed <b>public transport stop</b> · spaces for <b>emergency and security services</b> · "
               "prohibited spaces on a road of <i>atención preferente</i> · the <b>middle of the carriageway</b>",
               "Carga y descarga <b>en horas de utilización</b> · <b>doble fila sin conductor</b> · <b>parada de transporte público</b> señalizada y delimitada · espacios para <b>servicios de urgencia y seguridad</b> · "
               "espacios prohibidos en vía de <b>atención preferente</b> · en <b>medio de la calzada</b>")],
        ],
        widths=["50%", "50%"],
        cls="small",
    ))
    B.append(TABLE(
        [T("No stopping and no parking", "Prohibido parar y estacionar"), T("Serious offence if it obstructs or is dangerous", "Infracción grave si obstaculiza gravemente o es peligroso")],
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
               "Distancia <b>inferior a 3 m</b> entre el vehículo y el borde opuesto o una marca continua, o que no deje pasar a otros · impedir la incorporación de un vehículo parado o estacionado · "
               "obstaculizar la salida o acceso a un inmueble de personas o animales · obstaculizar un <b>vado</b> señalizado · obstaculizar <b>pasos rebajados</b> para disminuidos físicos · en <b>medianas, separadores, isletas</b> · impedir un giro autorizado")],
        ],
        widths=["58%", "42%"],
        cls="small",
    ))
    B.append(H3("8.4 Securing the vehicle", "8.4 Inmovilizar correctamente el vehículo"))
    B.append(P(
        "Before leaving the riding position, make sure the vehicle cannot move: <b>engine off</b>, <b>starting system disconnected</b> (take the key), and <b>precautions against unauthorised use</b> if you walk away "
        "(steering lock); switch on any <b>lights</b> needed.",
        "Antes de abandonar el puesto de conducción hay que asegurar la inmovilización: <b>apagar el motor</b>, <b>desconectar el sistema de arranque</b> (quitar la llave) e <b>impedir su uso sin autorización</b> si se aleja "
        "(bloqueo de dirección); y encender las <b>luces</b> correspondientes si fuera necesario."))

    # ---------------------------------------------------------------- 9. traps
    B.append(H2("9", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("Moving off after a red light or an agent’s order is <b>not</b> joining traffic.", "Reanudar la marcha tras un semáforo o un agente <b>no</b> es incorporación."),
        ("Arm signal for <b>right</b>: <b>left arm bent upwards</b>. Lights and arm disagree? The <b>arm</b> wins (your course).", "Brazo para la <b>derecha</b>: <b>izquierdo doblado hacia arriba</b>. ¿Luces y brazo se contradicen? Prevalece el <b>brazo</b> (tu curso)."),
        ("Horn to announce overtaking: <b>only out of town</b>. In town, flashes.", "Claxon para avisar del adelantamiento: <b>solo fuera de poblado</b>. En poblado, ráfagas."),
        ("A small correction <b>within your lane</b> is not a lateral move; leaning into a <b>bend</b> is not a turn.", "Una corrección <b>dentro del carril</b> no es desplazamiento lateral; seguir una <b>curva</b> no es cambio de dirección."),
        ("Overtaking out of town on your motorcycle: <b>≥ 1.5 m</b> from <b>any</b> vehicle.", "Adelantar en moto fuera de poblado: <b>≥ 1,5 m</b> con <b>cualquier</b> vehículo."),
        ("Overtaking cyclists, mopeds, VMP, pedestrians or animals <b>out of town</b>: ≥ 1.5 m <b>and 20 km/h below the limit</b>.", "Adelantar <b>fuera de poblado</b> a ciclistas, ciclomotores, VMP, peatones o animales: ≥ 1,5 m <b>y 20 km/h por debajo del límite</b>."),
        ("Others may overtake you <b>at a junction</b> (two-wheelers are the exception), but <b>not at a level crossing</b> (since October 2026).", "A ti pueden adelantarte <b>en una intersección</b> (los de dos ruedas son la excepción), pero <b>no en un paso a nivel</b> (desde octubre de 2026)."),
        ("The overtaken vehicle may <b>never speed up</b>.", "El adelantado <b>nunca</b> puede aumentar la velocidad."),
        ("Stopped vehicle <b>because of the traffic</b> on a no-overtaking stretch: stay behind.", "Vehículo parado <b>por necesidades del tráfico</b> en tramo de adelantamiento prohibido: quedarse detrás."),
        ("Turning round: <b>one go, no reversing</b>; never through the median of an autovía.", "Cambio de sentido: <b>de un solo giro y sin marcha atrás</b>; nunca por la mediana de la autovía."),
        ("A stop is <b>under 2 minutes</b> without abandoning the vehicle; double parking: <b>stopping yes, parking no</b>.", "La parada dura <b>menos de 2 minutos</b> sin abandonar el vehículo; doble fila: <b>parada sí, estacionamiento no</b>."),
        ("Broken yellow line: <b>no parking</b>. Continuous yellow line: <b>no stopping or parking</b>.", "Línea amarilla discontinua: <b>prohibido estacionar</b>. Continua: <b>prohibido parar y estacionar</b>."),
        ("Detention in a tunnel <b>over 2 minutes</b>: engine off, <b>position lights on</b>.", "Detención en túnel <b>más de 2 minutos</b>: motor apagado y <b>luces de posición encendidas</b>."),
    ]))

    # ---------------------------------------------------------------- 10. numbers
    B.append(H2("10", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Side gap overtaking vulnerable users, immobilised or assistance vehicles", "Separación al adelantar a vulnerables, inmovilizados o auxilio"), T("≥ 1.5 m", "≥ 1,5 m")],
            [T("Side gap of a two-wheeler overtaking anything out of town", "Separación de un vehículo de dos ruedas que adelanta fuera de poblado"), T("≥ 1.5 m", "≥ 1,5 m")],
            [T("Speed reduction overtaking vulnerable users (out of town) or immobilised and assistance vehicles (everywhere)", "Reducción al adelantar a vulnerables (fuera de poblado) o a inmovilizados y auxilio (siempre)"), T("≥ 20 km/h below the limit", "≥ 20 km/h por debajo del límite")],
            [T("Stop (parada)", "Parada"), T("&lt; 2 minutes", "&lt; 2 minutos")],
            [T("Detention in a tunnel: engine off", "Detención en túnel: motor apagado"), T("&gt; 2 minutes", "&gt; 2 minutos")],
            [T("Serious offence: gap to the opposite edge or continuous line", "Infracción grave: distancia al borde opuesto o marca continua"), T("&lt; 3 m", "&lt; 3 m")],
            [T("Removal in time-limited zones", "Retirada en zonas de estacionamiento limitado"), T("over 3 × the time paid", "más del triple del tiempo abonado")],
            [T("Turning round", "Cambio de sentido"), T("180°, one go, no reversing", "180°, un solo giro, sin marcha atrás")],
        ],
        widths=["62%", "38%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
QUIZ_IDS = ["bs1", "wn2", "hn3", "jn2", "lt1", "ov3", "gp2", "gp5", "no3", "tr2", "ut2", "np3"]


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
    ("Reglamento General de Circulación (RD 1428/2003), arts. 72–94, 109–110, 130 and 156 — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Real Decreto 518/2026 (BOE 26-06-2026): overtaking rules (arts. 85, 87 and 88), municipal parking rules (art. 156), vest on motorcycles; in force 1 October 2026", "https://www.boe.es/boe/dias/2026/06/26/pdfs/BOE-A-2026-13889.pdf"),
    ("Ley sobre Tráfico (RDL 6/2015), arts. 40 (parking prohibitions, two-wheelers on pavements) and 105 (removal of vehicles)", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722"),
]

GLOSSARY = [
    ("maniobra", "manoeuvre"),
    ("observar · señalizar · realizar", "observe · signal · carry out"),
    ("incorporación a la circulación", "joining traffic"),
    ("desplazamiento lateral · cambio de carril", "moving sideways · lane change"),
    ("adelantamiento · adelantar", "overtaking · to overtake"),
    ("cambio de dirección", "turning (into another road)"),
    ("cambio de sentido", "turning round (U-turn)"),
    ("advertencias ópticas / acústicas", "light / sound warnings"),
    ("intermitente · luz de freno", "indicator · brake light"),
    ("destellos · ráfagas", "headlight flashes"),
    ("claxon · avisador acústico", "horn"),
    ("contaminación acústica", "noise pollution"),
    ("inmueble · camino privado", "building · private road"),
    ("carril de aceleración / deceleración", "acceleration / deceleration lane"),
    ("parada señalizada", "signed (bus) stop"),
    ("ceñirse al borde", "to keep close to the edge"),
    ("eje de la calzada", "centre of the carriageway"),
    ("separación lateral", "side gap"),
    ("conjunto de ciclistas · unidad móvil", "group of cyclists · one moving unit"),
    ("vehículo inmovilizado · vehículo de auxilio", "immobilised vehicle · assistance vehicle"),
    ("paso a nivel", "level crossing"),
    ("mediana · paso abierto de la mediana", "central reservation · gap in it"),
    ("detención · parada · estacionamiento", "detention · stop · parking"),
    ("en línea · en batería", "parallel · side by side (bay parking)"),
    ("doble fila", "double parking"),
    ("vado", "dropped kerb / vehicle entrance"),
    ("carga y descarga", "loading and unloading"),
    ("limitación horaria", "time-limited parking"),
    ("atención preferente", "priority-maintenance road"),
    ("chaleco de alta visibilidad", "high-visibility vest"),
]
