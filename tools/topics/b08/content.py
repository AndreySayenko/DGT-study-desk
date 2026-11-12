# -*- coding: utf-8 -*-
"""Topic 8 content (signs and signals), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Tema 8: Las señales); the course's section 5 (vertical signs)
is split here into sections 5–7 so each family of signs has its own entry in the contents. The wording, the figures
and the sign drawings are original (simplified from the official designs); the rules come from the Reglamento General
de Circulación (RD 1428/2003, Título IV and Anexo I) with the official sign catalogue approved by RD 465/2025 (in force
1 July 2025) and the reform made by RD 518/2026 (in force 1 October 2026).
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import priority_order, sign_sides, agent_arms, exit_colours
from .signs import ICON
import re

_CODE = re.compile(r"([PRS]-\d+[a-z]?)")


def nw(text):
    """Keep sign codes such as S-301 on one line in narrow table cells."""
    return _CODE.sub(r'<span style="white-space:nowrap">\1</span>', text)


def SG(code, en, es, m_en, m_es, icon=None):
    """A row of a sign table: drawing, name (with code) and meaning."""
    ic = ICON[icon or code]
    tag = nw(f" ({code})") if code[:2] in ("P-", "R-", "S-") else ""     # drawings of lights, devices and markings have no official code
    return [T(ic, ic), T(f"<b>{en}</b>{tag}<br><i>{nw(es)}</i>", f"<b>{nw(es)}</b>{tag}"), T(m_en, m_es)]


def SIGNS(rows, h_en="Sign", h_es="Señal"):
    return TABLE([T(h_en, h_es), T("Name", "Nombre"), T("Meaning", "Significado")], rows, widths=["15%", "30%", "55%"], cls="small")


def TX(code, en, es, m_en, m_es):
    """A row of a text-only sign table (orientation signs that are mostly words)."""
    return [T(f"<b>{nw(code)}</b>", f"<b>{nw(code)}</b>"), T(f"<b>{en}</b><br><i>{es}</i>", f"<b>{es}</b>"), T(m_en, m_es)]


def TXSIGNS(rows):
    return TABLE([T("Code", "Código"), T("Name", "Nombre"), T("What it shows", "Qué indica")], rows, widths=["12%", "36%", "52%"], cls="small")


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Every sign belongs to a family you can tell by its <b>shape and colour</b>: red-bordered <b>triangle</b> = danger warning; red-ringed <b>circle</b> = prohibition or restriction; "
         "<b>blue circle</b> = obligation; white circle with <b>black diagonal stripes</b> (or blue with a red bar) = end of a prohibition or obligation; <b>blue square or rectangle</b> = information. "
         "A <b>yellow</b> background means <b>roadworks</b>.",
         "Cada señal pertenece a una familia que se reconoce por su <b>forma y color</b>: <b>triángulo</b> con borde rojo = advertencia de peligro; <b>círculo</b> con borde rojo = prohibición o restricción; "
         "<b>círculo azul</b> = obligación; círculo blanco con <b>franjas negras</b> (o azul con barra roja) = fin de prohibición u obligación; <b>cuadrado o rectángulo azul</b> = indicación. "
         "El <b>fondo amarillo</b> indica <b>obras</b>."),
        ("The exam asks above all about the <b>order of priority</b> (agents → temporary signs → traffic lights → vertical signs → road markings), what each <b>agent’s gesture</b> means, "
         "the <b>traffic lights</b>, the signs that are easy to confuse, and the <b>road markings</b>.",
         "El examen pregunta sobre todo por el <b>orden de prioridad</b> (agentes → señalización circunstancial → semáforos → señales verticales → marcas viales), el significado de cada <b>señal de los agentes</b>, "
         "los <b>semáforos</b>, las señales que se confunden y las <b>marcas viales</b>."),
        ("The course’s section 5 (vertical signs) is split here into <b>5 warning</b>, <b>6 regulatory</b> and <b>7 indication</b> signs. The sign drawings are our own simplified versions of the "
         "official catalogue (RD 465/2025, in force since 1 July 2025). Spanish exam terms are in <i>italics</i>, and a glossary closes the topic.",
         "El apartado 5 del curso (señales verticales) se divide aquí en señales de <b>5 advertencia</b>, <b>6 reglamentación</b> e <b>7 indicación</b>. Los dibujos de las señales son versiones simplificadas propias "
         "del catálogo oficial (RD 465/2025, vigente desde el 1 de julio de 2025). Al final hay un glosario español–inglés."),
    ]))

    # ---------------------------------------------------------------- 1. general rules
    B.append(H2("1", "General rules", "Normas generales"))
    B.append(P(
        "<b>Signposting</b> (<i>señalización</i>) is the set of signs and agents’ orders whose <b>job is to warn, inform, order or regulate</b> how road users behave, with enough notice. "
        "<b>Every road user must obey the traffic signs.</b>",
        "La <b>señalización</b> es el conjunto de señales y órdenes de los agentes cuya <b>misión es advertir, informar, ordenar o reglamentar</b> el comportamiento de los usuarios, con la necesaria antelación. "
        "<b>Todos los usuarios de las vías están obligados a obedecer las señales</b> de la circulación."))
    B.append(BOX("trap", "Nobody may tamper with signs", "Nadie puede manipular las señales", [
        ("Without a justified reason, nobody may <b>install, remove, move, hide or alter</b> a road’s signs without permission from the road’s owner or, where applicable, the traffic authority or whoever is responsible for the installation.",
         "Salvo causa justificada, nadie debe <b>instalar, retirar, trasladar, ocultar o modificar</b> la señalización de una vía sin permiso de su titular o, en su caso, de la autoridad encargada de regular el tráfico o de la responsable de las instalaciones."),
        ("It is forbidden to change what a sign says or to put <b>plates, posters, marks or other objects</b> on or near it that could cause confusion, reduce its visibility or effectiveness, dazzle road users or distract them.",
         "Se prohíbe modificar el contenido de las señales o colocar sobre ellas o en sus inmediaciones <b>placas, carteles, marcas u otros objetos</b> que puedan inducir a confusión, reducir su visibilidad o su eficacia, deslumbrar a los usuarios o distraer su atención."),
    ]))
    B.append(H3("1.1 Order of priority", "1.1 Orden de prioridad"))
    B.append(FIG(priority_order, "When signals disagree, the higher kind wins: an agent’s order beats everything, and road markings come last.",
                 "Si las señales no coinciden, prevalece la de rango superior: la orden de un agente prevalece sobre todo y las marcas viales van en último lugar."))
    B.append(TABLE(
        [T("Order", "Orden"), T("Kind of signal", "Tipo de señal")],
        [
            [T("1st", "1º"), T("<b>Agents’ signals and orders</b>", "<b>Señales y órdenes de los agentes</b>")],
            [T("2nd", "2º"), T("<b>Temporary signs</b> that change the normal use of the road, plus <b>beaconing</b> and containment devices", "<b>Señalización circunstancial</b> que modifica el régimen normal de utilización de la vía, y <b>balizamiento</b> y contención")],
            [T("3rd", "3º"), T("<b>Traffic lights</b>", "<b>Semáforos</b>")],
            [T("4th", "4º"), T("<b>Vertical signs</b>", "<b>Señales verticales</b>")],
            [T("5th", "5º"), T("<b>Road markings</b>", "<b>Marcas viales</b>")],
        ],
        widths=["14%", "86%"],
    ))
    B.append(H3("1.2 Where signs are placed", "1.2 Colocación de la señalización"))
    B.append(FIG(sign_sides, "A sign on the right binds everyone; one on the left binds those going straight on or turning left.",
                 "La señal de la derecha obliga a todos; la de la izquierda, a los que siguen de frente o giran a la izquierda."))
    B.append(TABLE(
        [T("Where the sign is", "Dónde está la señal"), T("Who must obey it", "A quién obliga")],
        [
            [T("On the <b>right</b>", "A la <b>derecha</b>"), T("<b>Everyone</b>, whether they go straight on or turn.", "A <b>todos</b>, sigan de frente o giren.")],
            [T("On the <b>left</b>", "A la <b>izquierda</b>"), T("Those going <b>straight on or turning left</b>.", "A los que sigan <b>de frente o giren a la izquierda</b>.")],
            [T("<b>Different</b> signs on each side", "Señales <b>distintas</b> a cada lado"), T("Left one: <b>straight on or left</b>. Right one: <b>turning right</b>.", "La de la izquierda: <b>de frente o a la izquierda</b>. La de la derecha: <b>giro a la derecha</b>.")],
            [T("<b>Above the carriageway</b>", "<b>Encima de la calzada</b>"), T("The <b>whole carriageway</b>.", "<b>Toda la calzada</b>.")],
            [T("<b>Above one lane</b>", "<b>Encima de un carril</b>"), T("<b>That lane only</b>.", "<b>Solo ese carril</b>.")],
        ],
        widths=["34%", "66%"],
    ))
    B.append(H3("1.3 When signs contradict each other", "1.3 Contradicción entre señales"))
    B.append(TABLE(
        [T("The contradiction is…", "La contradicción es…"), T("You obey…", "Se obedece…")],
        [
            [T("Between signs of <b>different groups</b>", "Entre señales de <b>diferentes grupos</b>"), T("The one with <b>priority</b> by the order above.", "La <b>prioritaria</b> según el orden de prioridad.")],
            [T("Between signs of the <b>same group</b>", "Entre señales del <b>mismo grupo</b>"), T("The <b>most restrictive</b> one.", "La <b>más restrictiva</b>.")],
            [T("Between a sign and the <b>traffic rules</b>", "Entre una señal y las <b>normas de circulación</b>"), T("<b>The sign</b>, unless special circumstances justify otherwise.", "<b>La señal</b>, salvo circunstancias especiales que lo justifiquen.")],
        ],
        widths=["44%", "56%"],
    ))
    B.append(H3("1.4 How far a sign applies", "1.4 Aplicación de las señales"))
    B.append(P(
        "A sign addressed to drivers applies to the <b>whole width of the carriageway</b> they may use, <b>except</b> when it is <b>painted inside a lane</b> (for example a “30” on one lane) "
        "or a <b>panel limits its message</b> (for example a lorry panel under a speed limit).",
        "Las señales dirigidas al conductor se aplican a <b>toda la anchura de la calzada</b> que esté autorizado a utilizar, <b>salvo</b> que esté <b>dentro de algún carril</b> (por ejemplo, un «30» pintado en un carril) "
        "o que tenga algún <b>panel que limite su mensaje</b> (por ejemplo, un panel de camión bajo una limitación de velocidad)."))
    B.append(P(
        "To make a sign easier to understand, a wording may be added on a <b>rectangular complementary panel below it</b>, or inside a rectangular panel that contains the sign.",
        "Para facilitar su interpretación, se puede añadir una inscripción en un <b>panel complementario rectangular colocado debajo</b> de la señal, o en el interior de un panel rectangular que la contenga."))
    B.append(H3("1.5 Roadworks signs", "1.5 Señales de obras"))
    B.append(TABLE(
        [T("Rule", "Norma")],
        [
            [T("Works that hinder traffic must be <b>signed by day and by night</b>, and <b>lit</b> at night or when the weather or surroundings require it.",
               "Las <b>obras</b> que dificulten la circulación deben estar <b>señalizadas de día y de noche</b> y <b>balizadas luminosamente</b> de noche o cuando las condiciones meteorológicas o ambientales lo exijan.")],
            [T("In roadworks the <b>road markings are yellow</b>.", "En las obras, las <b>marcas viales son de color amarillo</b>.")],
            [T("Some <b>warning</b> and <b>regulatory</b> signs, and <b>all lane and orientation</b> signs, have a <b>yellow background</b>. Their meaning is the <b>same</b> as without works.",
               "Tienen <b>fondo amarillo</b> algunas señales de <b>advertencia</b> y de <b>reglamentación</b>, y <b>todas las de carriles y de orientación</b>. Su significado es el <b>mismo</b> que sin obras.")],
        ],
    ))

    # ---------------------------------------------------------------- 2. agents
    B.append(H2("2", "Agents’ signals", "Señales de los agentes"))
    B.append(P(
        "You must obey <b>at once</b> the signals and orders of traffic agents (they must be visible and easy to recognise). They <b>prevail over every other sign and traffic rule</b>, even when they contradict them. "
        "Agents signal <b>with their arms</b>, <b>with a whistle</b> and <b>from their vehicle</b>.",
        "Los usuarios deben obedecer <b>inmediatamente</b> las señales y órdenes de los agentes de la circulación (serán visibles y fácilmente reconocibles), que <b>prevalecen sobre las demás señales y normas</b>, aunque estén en contradicción con ellas. "
        "Se realizan <b>con los brazos</b>, <b>con el silbato</b> y <b>desde el vehículo</b>."))
    B.append(H3("2.1 Arm signals", "2.1 Señales con los brazos"))
    B.append(FIG(agent_arms, "Three signals mean STOP and one means SLOW DOWN. A stop order stays in force while the agent keeps the same position, even with the arms down.",
                 "Tres señales obligan a DETENERSE y una a REDUCIR. La orden de detención sigue en vigor mientras el agente mantenga su posición, aunque baje los brazos."))
    B.append(E(
        "Arm raised vertically", "Brazo levantado verticalmente",
        "<b>Everyone approaching the agent must stop</b>, except drivers who cannot do so safely. Where to stop: at the <b>nearest stop line</b>; if there is none, <b>before the agent</b>; "
        "at an intersection, <b>before entering it</b> (drivers <b>already inside need not stop</b>); or where the agent points after making the signal.",
        "Obliga a <b>detenerse a todos los usuarios que se acerquen al agente</b>, salvo a los conductores que no puedan hacerlo en condiciones de seguridad suficiente. La detención se hace: ante la <b>línea de detención más cercana</b>; si no existe, <b>antes del agente</b>; "
        "en una intersección, <b>antes de entrar en ella</b> (los que <b>ya estén dentro no están obligados a detenerse</b>); o en el lugar que señale el agente después de hacer la señal.",
        tip=("It is the only arm signal that stops traffic from <b>every</b> direction.", "Es la única señal de brazo que detiene el tráfico de <b>todas</b> las direcciones.")))
    B.append(E(
        "Arm or arms held out horizontally", "Brazo o brazos extendidos horizontalmente",
        "Users approaching from directions that <b>cross the line of the outstretched arm(s)</b> must stop, whichever way they are travelling. "
        "Agents’ signals <b>stay in force</b> even if the agent lowers the arms, as long as they do not change position or make another signal.",
        "Obliga a <b>detenerse</b> a los usuarios que se acerquen al agente <b>desde las direcciones que corten la indicada por el brazo o brazos extendidos</b>, cualquiera que sea el sentido de su marcha. "
        "Las señales de los agentes <b>permanecen en vigor</b> aunque el agente baje los brazos, siempre que no cambien de posición ni realicen otra señal."))
    B.append(E(
        "Swinging a red or amber light", "Balanceo de una luz roja o amarilla",
        "Users <b>towards whom the agent aims the light</b> must stop.", "Obliga a <b>detenerse</b> a los usuarios <b>hacia los que el agente dirija la luz</b>."))
    B.append(E(
        "Arm held out, moving up and down", "Brazo extendido moviéndolo alternativamente arriba y abajo",
        "Drivers approaching <b>at right angles to the arm</b> must <b>slow down</b>.", "Obliga a <b>disminuir la velocidad</b> a los conductores que se acerquen <b>perpendicularmente al brazo</b> que ejecuta la señal."))
    B.append(H3("2.2 Whistle signals", "2.2 Señales con el silbato"))
    B.append(TABLE(
        [T("Whistle", "Silbato"), T("Means", "Significa")],
        [
            [T("A series of <b>short, frequent blasts</b>", "Una serie de <b>toques cortos y frecuentes</b>"), T("<b>Stop</b> the vehicles.", "<b>Detención</b> de los vehículos.")],
            [T("<b>One long blast</b>", "<b>Un toque largo</b>"), T("<b>Move off again</b>.", "<b>Reanudar la marcha</b>.")],
        ],
        widths=["44%", "56%"],
    ))
    B.append(H3("2.3 Signals from the agents’ vehicle", "2.3 Señales desde el vehículo"))
    B.append(P(
        "Agents may give orders while using the <b>V-1 flashing light</b>, through a <b>loudspeaker</b> or by any other means, among them:",
        "Los agentes pueden dar órdenes o indicaciones mientras utilizan la <b>señal luminosa V-1</b>, a través de la <b>megafonía</b> o por cualquier otro medio, entre ellos:"))
    B.append(SIGNS([
        SG("ag-red", "Red flag", "Bandera roja",
           "From the moment the vehicle carrying it passes, the road is <b>temporarily closed</b> to all users, <b>except</b> those <b>accompanied or escorted by agents</b>.",
           "A partir del paso del vehículo que la lleva, la <b>calzada queda temporalmente cerrada</b> a todos los usuarios, <b>excepto</b> los <b>acompañados o escoltados por los agentes</b>."),
        SG("ag-yellow", "Yellow flag", "Bandera amarilla",
           "Take <b>extreme care</b>, or a <b>danger is near</b>. Staff doing order, control or safety jobs during cycle marches or other activities on public roads may also use it.",
           "Necesidad de <b>extremar la atención</b> o <b>proximidad de un peligro</b>. También puede usarla el personal que realice funciones de orden, control o seguridad en marchas ciclistas u otras actividades en vías públicas."),
        SG("ag-green", "Green flag", "Bandera verde",
           "From the moment the vehicle carrying it passes, the road is <b>open again</b>.", "A partir del paso del vehículo que la lleva, la <b>calzada queda de nuevo abierta</b> al tráfico."),
        SG("ag-arm", "Arm held out downwards, slanted and still", "Brazo extendido hacia abajo, inclinado y fijo",
           "From a vehicle: the users it is aimed at must <b>stop on the right</b>.", "Desde un vehículo: obligación de <b>detenerse en el lado derecho</b> para los usuarios a los que va dirigida."),
        SG("ag-light", "Flashing red light facing forwards", "Luz roja intermitente o destelleante hacia delante",
           "The vehicle in front must <b>stop on the right, ahead of the police vehicle</b>, where it causes no greater risk or nuisance, and <b>obey the instructions given over the loudspeaker</b>.",
           "El vehículo que circula delante debe <b>detenerse en el lado derecho delante del vehículo policial</b>, donde no genere mayores riesgos o molestias, y <b>obedecer las instrucciones</b> que el agente dé por <b>megafonía</b>."),
    ], "Signal", "Señal"))
    B.append(H3("2.4 Other signals", "2.4 Otras señales"))
    B.append(P("Agents may use <b>any other indication</b> when circumstances require it, as long as it is <b>clear</b>.",
               "Los agentes pueden utilizar <b>cualquier otra indicación</b> distinta cuando las circunstancias lo exijan y se realice de forma <b>clara</b>."))
    B.append(H3("2.5 People who help the agents", "2.5 Auxiliares de los agentes"))
    B.append(SIGNS([
        SG("ag-paddle", "Roadworks staff and special-transport escorts", "Personal de obras y de acompañamiento de transportes especiales",
           "Where there are no agents, or to help them, they may <b>regulate traffic with the signs on a paddle</b>. Drivers <b>must obey</b> them.",
           "Si no hay agentes o para ayudarles, pueden <b>regular el paso con las señales de una paleta</b>. Los conductores <b>deben obedecer sus indicaciones</b>."),
        SG("ag-school", "School patrols", "Patrullas escolares",
           "They may <b>“invite”</b> road users to <b>stop</b>, using the sign on a paddle.", "Pueden <b>«invitar»</b> a los usuarios a que <b>detengan su marcha</b>, con la señal de una paleta."),
    ], "Paddle", "Paleta"))
    B.append(TABLE(
        [T("Also…", "Además…")],
        [
            [T("The <b>Military Police</b> may regulate traffic.", "La <b>Policía Militar</b> puede regular la circulación.")],
            [T("When a <b>sports event</b> or similar is authorised with traffic limits, the traffic authority may let <b>civil-protection staff</b> or the <b>organisers’ staff</b> stop vehicles or pedestrians entering the affected area or route.",
               "Cuando se autorice una <b>prueba deportiva</b> o acto que exija limitar la circulación, la autoridad de tráfico puede habilitar al <b>personal de protección civil</b> o de la <b>organización</b> para impedir el acceso de vehículos o peatones a la zona o itinerario afectados.")],
            [T("All of them must wear <b>bright-coloured clothing</b> and <b>retroreflective</b> elements that let others see them from at least <b>150 metres</b>.",
               "Todos deben llevar <b>prendas de colores llamativos</b> y elementos <b>retrorreflectantes</b> que permitan distinguirlos a una distancia mínima de <b>150 metros</b>.")],
        ],
    ))

    # ---------------------------------------------------------------- 3. temporary signs and beaconing
    B.append(H2("3", "Temporary signs, beaconing and barriers", "Señales circunstanciales y elementos de balizamiento"))
    B.append(H3("3.1 Variable message signs", "3.1 Paneles de mensaje variable"))
    B.append(SIGNS([
        SG("vms", "Variable message sign", "Panel de mensaje variable",
           "<b>Regulates traffic by adapting it to the circumstances</b>: it informs, <b>warns of dangers</b> and gives <b>recommendations or compulsory instructions</b>. "
           "Its changes end when the panel itself says so or when their causes disappear. It <b>never shows more than two alternating messages</b>.",
           "Su finalidad es <b>regular la circulación adaptándola a las circunstancias</b>: informa, <b>advierte de peligros</b> y da <b>recomendaciones o instrucciones de obligado cumplimiento</b>. "
           "Las modificaciones terminan cuando lo establezca el propio panel o cuando cesen sus causas. <b>Nunca se usan más de dos mensajes alternados</b>."),
    ], "Panel", "Panel"))
    B.append(H3("3.2 Beaconing", "3.2 Elementos de balizamiento"))
    B.append(P("They show the <b>course, layout and obstacles</b> of the road: delimiting devices, guide devices, other beaconing elements and beaconing signals.",
               "Tienen la misión de indicar el <b>desarrollo, trazado y obstáculos</b> de la vía: dispositivos delimitadores, dispositivos de guía, otros elementos de balizamiento y señales de balizamiento."))
    B.append(H3("3.2.1 Delimiting devices", "3.2.1 Dispositivos delimitadores"))
    B.append(SIGNS([
        SG("dev-barrier", "Fixed barrier", "Dispositivo delimitador fijo (barrera fija)", "<b>Forbids passing</b> into the road or the part of it that it closes off.", "<b>Prohíbe el paso</b> a la vía o a la parte de ella que delimita."),
        SG("dev-boom", "Moving barrier or half-barrier", "Dispositivo delimitador móvil (barrera o semibarrera móviles)",
           "<b>Temporarily forbids passing</b> while it is moving or across the road. Used at <b>level crossings</b>, tolls, customs posts, entrances to premises… "
           "At a level crossing or movable bridge that is closed or whose barrier is moving, <b>stop one behind the other in your lane</b> until the way is clear.",
           "<b>Prohíbe temporalmente el paso</b> mientras esté en movimiento o en posición transversal a la calzada. Se coloca en <b>pasos a nivel</b>, peajes, aduanas, accesos a establecimientos… "
           "En un paso a nivel o puente móvil cerrado o con la barrera en movimiento, hay que <b>detenerse uno detrás de otro en el carril</b> correspondiente hasta tener paso libre."),
        SG("dev-panel", "Temporary direction panel", "Panel direccional provisional", "<b>Forbids passing</b> and <b>shows the direction to follow</b>.", "<b>Prohíbe el paso</b> e <b>informa sobre el sentido de circulación</b>."),
        SG("dev-cones", "Temporary edge beacons, cones or similar", "Balizas de borde provisionales, conos o análogos", "You may <b>not cross the real or imaginary line</b> joining them.", "<b>Prohíben el paso</b> a través de la <b>línea real o imaginaria</b> que los une."),
        SG("dev-redlight", "Steady red light", "Luz roja fija", "The carriageway is <b>completely closed</b>.", "Indica que la calzada está <b>totalmente cerrada</b> al tránsito."),
        SG("dev-yellow", "Steady or flashing yellow lights", "Luces amarillas fijas o intermitentes", "You may <b>not cross the real or imaginary line</b> joining them.", "<b>Prohíben el paso</b> a través de la <b>línea real o imaginaria</b> que las une."),
    ], "Device", "Dispositivo"))
    B.append(H3("3.2.2 Guide devices", "3.2.2 Dispositivos de guía"))
    B.append(P("They show the <b>edge of the carriageway</b>, a <b>bend</b> and its direction, the limits of bridges and other structures, or other obstacles.",
               "Indican el <b>borde de la calzada</b>, la presencia de una <b>curva</b> y su sentido, los límites de obras de fábrica u otros obstáculos."))
    B.append(SIGNS([
        SG("dev-vertice", "Gore marker", "Hito de vértice", "Half-cylinder with <b>two opposed retroreflective triangles</b>: marks where <b>two streams of traffic separate</b>.",
           "Forma semicilíndrica con <b>2 triángulos opuestos</b> retrorreflectantes: indica el punto donde <b>se separan dos corrientes de tráfico</b>."),
        SG("dev-arista", "Edge post *", "Hito de arista *", "Marks the <b>edges of the road</b>, above all at night or in poor visibility.", "Su finalidad es <b>balizar los bordes de las vías</b>, sobre todo de noche o con baja visibilidad."),
        SG("dev-chevrons", "Permanent direction panel", "Panel direccional permanente",
           "Warns of a <b>specific danger</b> and shows the <b>direction to follow</b>. Three levels: <b>moderate (single panel), medium (double), high (triple)</b>.",
           "Guía y señala un <b>peligro puntual informando del sentido de circulación</b>. Tres niveles: <b>moderado (panel sencillo), medio (doble) y elevado (triple)</b>."),
        SG("dev-catseye", "Road studs, “cat’s eyes” *", "Captafaros horizontales retrorreflectantes («ojos de gato») *",
           "On the road surface, they <b>highlight lane limits</b>, directions and edges and help optical guidance.", "Se colocan en la calzada para <b>resaltar los límites de los carriles</b>, los sentidos y los bordes, y facilitar el guiado óptico."),
        SG("dev-guardrail-refl", "Barrier reflectors *", "Captafaros verticales o de barrera *", "Fitted to the <b>side barriers</b>; retroreflective or luminous.", "Van incorporados a las <b>barreras laterales</b>; retrorreflectantes o luminosos."),
        SG("dev-flat", "Flat vertical markers", "Paneles verticales (balizas planas)", "Show the <b>edge of the carriageway</b>, a <b>narrowing</b>, the limits of structures or other <b>obstacles</b>.",
           "Indican el <b>borde de la calzada</b>, un <b>estrechamiento</b>, los límites de obras de fábrica u otros <b>obstáculos</b>."),
        SG("dev-cyl", "Cylindrical bollards", "Balizas cilíndricas", "Reinforce other safety measures. You may <b>not cross the line, imaginary or not, that joins them</b>.",
           "Refuerzan cualquier medida de seguridad. Está <b>prohibido atravesar la línea, imaginaria o no, que las une</b>."),
        SG("dev-fogbox", "Fog beacon lights", "Balizamiento circunstancial luminoso",
           "Installed where <b>dense fog</b> is frequent, to help keep the <b>safety distance</b>. Two sets of lights: <b>steady amber</b> marks the direction and the edge; <b>steady red</b> shows a vehicle passing.",
           "Se instala en tramos de <b>niebla intensa</b> para adecuar la <b>distancia mínima de seguridad</b>. Dos conjuntos luminosos: <b>ámbar fijo</b> para el sentido y la delimitación de la vía; <b>rojo fijo</b> para señalizar el paso de un vehículo."),
        SG("dev-snowpole", "Snow poles", "Jalones de nieve", "Mark out the road when it is <b>covered by snow</b>, to help you follow it.", "<b>Delimitan la plataforma</b> cuando está <b>cubierta de nieve</b>, favoreciendo el guiado óptico."),
        SG("dev-rumble", "Rumble strips", "Guías sonoras longitudinales", "Small grooves or bumps in the line that <b>vibrate and/or make a noise</b> under the tyres to <b>warn of drifting off course</b>.",
           "Pequeñas hendiduras o resaltes en la marca vial que, al ser pisadas, <b>producen vibración y/o sonido</b> para <b>alertar de desvíos involuntarios</b>."),
    ], "Device", "Dispositivo"))
    B.append(BOX("key", "* Colour of edge posts and reflectors", "* Color de hitos de arista y captafaros", [
        ("On the <b>left</b>: <b>white</b>.", "A la <b>izquierda</b>: <b>blanco</b>."),
        ("On the <b>right</b>: <b>white or yellow</b>.", "A la <b>derecha</b>: <b>blanco o amarillo</b>."),
    ]))
    B.append(H3("3.2.3 Other beaconing elements and 3.2.4 beaconing signals", "3.2.3 Otros elementos y 3.2.4 señales de balizamiento"))
    B.append(SIGNS([
        SG("dev-windsock", "Windsock", "Manga de viento", "Adds to the <b>“crosswind”</b> warning sign: shows that a steady or gusty wind exists, its <b>direction and strength</b>.",
           "Complementa la señal «Viento transversal»: informa de la <b>existencia, sentido e intensidad</b> de un viento continuo o racheado."),
        SG("dev-gantry", "Height-control gantry", "Pórtico de control de gálibo", "<b>Warns or stops vehicles taller</b> than the bridge, overpass or tunnel that comes next.",
           "Estructura que sirve para <b>advertir o impedir el paso de vehículos que sobrepasan la altura</b> del puente, paso superior o túnel que viene a continuación."),
        SG("dev-studs", "Luminous road studs", "Baliza o captafaro horizontal luminoso",
           "Set in the road to mark lanes, guide traffic through diversions, mark merging areas or restrict lane changes. <b>Green, orange or red</b>: you may only <b>cross them when green</b>.",
           "Colocada en la calzada para delimitar carriles, orientar en desvíos obligatorios, delimitar zonas de incorporación o restringir cambios de carril. Luz <b>verde, naranja o roja</b>: solo se puede <b>franquear cuando es verde</b>."),
    ], "Element", "Elemento"))
    B.append(H3("3.3 Vehicle restraint systems", "3.3 Sistemas de contención de vehículos"))
    B.append(SIGNS([
        SG("dev-rail", "Safety barriers", "Barreras de seguridad", "Mark the edge and <b>reduce the chance of leaving the road</b> after a loss of control, on verges and central reserves.",
           "Indican el borde de la plataforma y <b>protegen</b>, <b>reduciendo la posibilidad de que el vehículo se salga de la vía</b>, en márgenes y medianas."),
        SG("dev-pretil", "Parapets", "Pretiles", "Protect against leaving the road on <b>bridges</b>, overpasses and walls: they stop a <b>fall</b>.", "Protegen frente a salidas de la vía en <b>puentes</b>, pasos y muros: evitan la <b>caída al vacío</b>."),
        SG("dev-moto", "Motorcyclist protection", "Sistemas de protección para motoristas", "Barriers designed to protect <b>two-wheelers</b> (a lower rail).", "Barreras diseñadas para proteger a los <b>vehículos de dos ruedas</b>."),
        SG("dev-atten", "Crash cushions", "Atenuadores de impacto", "Used at <b>forks and splits</b>; they reduce the impact on vehicles that hit them.", "Se usan en <b>bifurcaciones o divergencias</b> y reducen el impacto en los vehículos que chocan contra ellos."),
    ], "System", "Sistema"))

    # ---------------------------------------------------------------- 4. traffic lights
    B.append(H2("4", "Traffic lights", "Semáforos"))
    B.append(P("Their main job is to <b>regulate who goes first</b>.", "Su misión principal es <b>regular la prioridad de paso</b>."))
    B.append(H3("4.1 Pedestrian lights", "4.1 Semáforos para peatones"))
    B.append(SIGNS([
        SG("tl-ped-green", "Steady green walking figure", "Luz verde fija en forma de peatón en marcha", "Pedestrians <b>may start crossing</b>.", "Pueden <b>comenzar a cruzar</b>."),
        SG("tl-ped-flash", "Flashing green walking figure", "Luz verde intermitente en forma de peatón en marcha", "The time to <b>finish crossing is running out</b>; red comes next.", "El tiempo para <b>terminar de cruzar está a punto de finalizar</b> y va a encenderse la roja."),
        SG("tl-ped-red", "Steady red standing figure", "Luz roja fija en forma de peatón inmóvil", "Pedestrians <b>must not start crossing</b>.", "<b>No deben comenzar a cruzar</b>."),
    ], "Light", "Luz"))
    B.append(H3("4.2 Round lights for vehicles", "4.2 Semáforos circulares para vehículos"))
    B.append(SIGNS([
        SG("tl-green", "Steady green", "Luz verde no intermitente",
           "You may go, <b>with priority</b>, <b>unless</b> traffic is such that you would foreseeably be <b>left stopped inside the junction</b>, a pedestrian or cyclist crossing, blocking cross traffic.",
           "Permite el paso <b>con prioridad</b>, <b>salvo</b> que previsiblemente el vehículo pueda <b>quedar detenido en una intersección</b>, paso para peatones o ciclistas, obstruyendo la circulación transversal."),
        SG("tl-amber", "Steady amber", "Luz amarilla no intermitente",
           "<b>Stop as for a red</b>, unless when it comes on you are so close that you <b>cannot stop safely before the light</b>.",
           "Obliga a <b>detenerse en las mismas condiciones que la roja</b>, salvo que, al encenderse, el vehículo esté tan cerca que <b>no pueda detenerse antes del semáforo en condiciones de seguridad suficientes</b>."),
        SG("tl-red", "Steady red", "Luz roja no intermitente",
           "<b>No passing.</b> Stop without passing the light or the nearest stop line before it. If the light is <b>inside or on the far side of a junction</b>, do <b>not enter</b> the junction or cross the stop line before it.",
           "<b>Prohíbe el paso.</b> Obliga a detenerse sin rebasar el semáforo ni la línea de detención más próxima. Si el semáforo está <b>dentro o al lado opuesto de una intersección</b>, <b>no se debe entrar</b> en ella ni rebasar la línea de detención anterior."),
        SG("tl-flash-red", "One flashing red, or two reds flashing alternately", "Una luz roja intermitente o dos rojas alternativamente intermitentes",
           "<b>Temporarily no passing.</b> Found before <b>level crossings</b>, movable bridges, ferry landings, near <b>fire-engine exits</b> or when a <b>low-flying aircraft</b> is coming.",
           "<b>Prohíben temporalmente el paso.</b> Están antes de <b>pasos a nivel</b>, puentes móviles o pontones transbordadores, cerca de <b>salidas de vehículos de extinción de incendios</b> o por la aproximación de una <b>aeronave a escasa altura</b>."),
        SG("tl-flash-amber", "One flashing amber, or two ambers flashing alternately", "Una luz amarilla intermitente o dos amarillas alternativamente intermitentes",
           "<b>Take extreme care</b> and, where appropriate, <b>give way</b>. It does <b>not cancel other signs</b> that make you stop.",
           "Obligan a <b>extremar la precaución</b> y, en su caso, <b>ceder el paso</b>. <b>No eximen</b> del cumplimiento de otras señales que obliguen a detenerse."),
        SG("tl-arrow-green", "Green arrow on a black round lens", "Flecha verde sobre fondo circular negro",
           "You may go in the <b>direction of the arrow</b>, whatever other light is on in that set or the next one, <b>with care</b>: <b>give way</b> to vehicles in the lane you join and do not endanger <b>pedestrians crossing</b>. "
           "If you are in the lane others need for that move when it lights up, you <b>must move off in that direction</b> (if yours is not possible), even if you did not want to go that way.",
           "Permite tomar la <b>dirección y sentido de la flecha</b>, cualquiera que sea la luz encendida en el mismo semáforo u otro contiguo, <b>con precaución</b>: <b>cediendo el paso</b> a los vehículos del carril al que se incorporan y sin poner en peligro a los <b>peatones que crucen</b>. "
           "El vehículo que, al encenderse, esté en el carril que necesitan otros para ese movimiento <b>debe avanzar en ese sentido</b> (si en el suyo no es posible), aunque no fuera el que deseaba."),
        SG("tl-arrow-black", "Black arrow on a red or amber light", "Flecha negra sobre luz roja o amarilla",
           "Steady or flashing, the light keeps its meaning but <b>only for the movement shown by the arrow</b>.",
           "Tanto fijas como intermitentes, no cambian el significado de la luz, pero lo <b>limitan al movimiento indicado por la flecha</b>."),
    ], "Light", "Luz"))
    B.append(BOX("key", "New since 1 October 2026", "Novedad desde el 1 de octubre de 2026", [
        ("At crossings with traffic lights, as a rule, vehicles no longer get a <b>flashing amber</b> while pedestrians have a <b>steady green</b> (see Topic 4).",
         "En los pasos con semáforo, como norma general, ya no coincide el <b>ámbar intermitente</b> para vehículos con el <b>verde fijo</b> para peatones (ver Tema 4)."),
    ]))
    B.append(H3("4.3 Square lane lights", "4.3 Semáforos cuadrados para vehículos o de carril"))
    B.append(P("They apply <b>only to the lane they hang over</b> (or the lane a variable message sign points to). You also find them at <b>motorway tolls</b>.",
               "Afectan <b>exclusivamente a los vehículos del carril sobre el que están</b> (o del que indique el panel de mensaje variable). También pueden estar en los <b>peajes de las autopistas</b>."))
    B.append(SIGNS([
        SG("tl-lane-down", "Green arrow pointing down", "Luz verde en forma de flecha apuntando hacia abajo",
           "You <b>may use the lane</b> it is above. It does <b>not</b> excuse you from stopping at a <b>red round light</b>, from signs or markings that make you stop or give way, or from the general priority rules.",
           "Está <b>permitido circular por el carril</b> sobre el que está encendida. <b>No exime</b> de detenerse ante una <b>luz roja circular</b> ni de obedecer señales o marcas que obliguen a detenerse o ceder el paso, ni de las normas generales de prioridad."),
        SG("tl-lane-diag", "White or yellow arrow pointing down at an angle (steady or flashing)", "Luz blanca o amarilla en forma de flecha oblicua hacia abajo (fija o intermitente)",
           "<b>Move safely into the lane it points to</b>: your lane is about to close.", "Hay que <b>irse incorporando en condiciones de seguridad al carril al que apunta</b>: el carril por el que se circula va a quedar cerrado en corto espacio."),
        SG("tl-lane-x", "Red cross", "Luz roja en forma de aspa", "<b>You may not use the lane</b>; anyone in it must <b>leave it as soon as possible</b>.", "<b>Prohíbe ocupar el carril</b>; quien circule por él debe <b>abandonarlo en el tiempo más breve posible</b>."),
    ], "Light", "Luz"))
    B.append(H3("4.4 Lights for certain vehicles only", "4.4 Semáforos reservados a determinados vehículos"))
    B.append(P(
        "Lights with an <b>illuminated white bar on a black round lens</b> apply <b>only to trams and regular-line buses</b>, unless there is a reserved lane for buses (or buses, taxis and others): then they apply to <b>everyone using that lane</b>.",
        "Los semáforos con una <b>franja blanca iluminada sobre fondo circular negro</b> afectan <b>solo a tranvías y autobuses de líneas regulares</b>, salvo que exista un carril reservado para autobuses (o autobuses, taxis y otros): entonces afectan <b>a todos los que circulen por él</b>."))
    B.append(SIGNS([
        SG("tl-bus-h", "Horizontal bar", "Franja horizontal", "<b>No passing</b>.", "<b>Prohíbe el paso</b>."),
        SG("tl-bus-v", "Vertical bar", "Franja vertical", "<b>Straight on</b> allowed.", "Permite el paso <b>de frente</b>."),
        SG("tl-bus-l", "Bar slanting to the left", "Franja inclinada a la izquierda", "Turning <b>left</b> allowed.", "Permite girar a la <b>izquierda</b>."),
        SG("tl-bus-r", "Bar slanting to the right", "Franja inclinada a la derecha", "Turning <b>right</b> allowed.", "Permite girar a la <b>derecha</b>."),
        SG("tl-bus-flash", "Flashing white bar", "Franja blanca intermitente", "<b>Stop as for a steady amber</b>.", "Hay que <b>detenerse como ante una luz amarilla fija</b>."),
        SG("tl-cycle", "Lights showing a bicycle", "Semáforos con la silueta de un ciclo", "They apply <b>only to cycles</b>.", "Sus indicaciones <b>afectan exclusivamente a los ciclos</b>."),
    ], "Light", "Luz"))
    return B + _vertical() + _markings() + _closing()


# ================================================================== 5–7 vertical signs
def _vertical():
    B = []
    # ---------------------------------------------------------------- 5. warning signs
    B.append(H2("5", "Warning signs (P)", "Señales de advertencia de peligro (P)"))
    B.append(P(
        "Vertical signs come in three families: <b>warning</b> (P), <b>regulatory</b> (R: priority, no entry, restriction, other prohibitions, obligation and end of prohibition) and <b>indication</b> (S).",
        "Las señales verticales son de tres tipos: de <b>advertencia de peligro</b> (P), de <b>reglamentación</b> (R: prioridad, prohibición de entrada, restricción de paso, otras de prohibición, obligación y fin de prohibición) y de <b>indicación</b> (S)."))
    B.append(P(
        "Warning signs announce that a <b>danger that is hard to see in time</b> is near, and what it is. A <b>complementary panel</b> may give the <b>distance</b> from the sign to the start of the danger and even the <b>length</b> of the stretch.",
        "Indican la <b>proximidad</b> y la naturaleza de un <b>peligro difícil de percibir a tiempo</b>. La <b>distancia</b> entre la señal y el principio del peligro puede indicarse en un <b>panel complementario</b>, e incluso la <b>longitud del tramo</b> afectado."))
    B.append(H3("5.1 Junctions, crossings and rail", "5.1 Intersecciones, cruces y ferrocarril"))
    B.append(SIGNS([
        SG("P-1", "Junction with priority", "Intersección con prioridad", "A junction with a road whose users <b>must give way to you</b>.", "Intersección con una vía cuyos usuarios <b>deben ceder el paso</b>."),
        SG("P-1a", "Junction with priority over a road on the right", "Intersección con prioridad sobre vía a la derecha", "Junction with a road on the <b>right</b> whose users must give way.", "Intersección con una vía a la <b>derecha</b> cuyos usuarios deben ceder el paso."),
        SG("P-1b", "Junction with priority over a road on the left", "Intersección con prioridad sobre vía a la izquierda", "Junction with a road on the <b>left</b> whose users must give way.", "Intersección con una vía a la <b>izquierda</b> cuyos usuarios deben ceder el paso."),
        SG("P-1c", "Priority over traffic merging from the right", "Intersección con prioridad sobre incorporación por la derecha",
           "A road <b>merges from the right</b> and its users must give way. Even so, you should <b>make the merge easier</b> as far as possible.",
           "<b>Incorporación por la derecha</b> de una vía cuyos usuarios deben ceder el paso. Aun así, quien encuentre la señal debe <b>facilitar la incorporación</b> en la medida de lo posible."),
        SG("P-1d", "Priority over traffic merging from the left", "Intersección con prioridad sobre incorporación por la izquierda",
           "Same, merging from the <b>left</b>; you should also make the merge easier.", "Igual, con incorporación por la <b>izquierda</b>; también hay que facilitar la incorporación."),
        SG("P-1e", "Stretch with direct accesses", "Tramo con accesos directos", "Several <b>direct accesses</b> join the road; their users <b>must give way</b>.", "Tramo con varios <b>accesos directos</b> a la vía; sus usuarios <b>deben ceder el paso</b>."),
        SG("P-2", "Junction with priority to the right", "Intersección con prioridad de la derecha", "A junction where the <b>general priority rule</b> applies (give way to the right).", "Intersección en la que rige la <b>regla general de prioridad de paso</b> (la de la derecha)."),
        SG("P-3", "Traffic lights", "Semáforos", "A junction or stretch <b>controlled by traffic lights</b>.", "Intersección aislada o tramo con la circulación <b>regulada por semáforos</b>."),
        SG("P-4", "Roundabout", "Glorieta", "A <b>roundabout</b>; traffic goes the way the arrows show.", "Proximidad de una <b>glorieta</b>, con circulación en el sentido de las flechas."),
        SG("P-5", "Movable bridge", "Puente móvil", "A bridge that can be <b>raised or turned</b>, stopping traffic for a while.", "Puente que puede ser <b>levantado o girado</b>, interrumpiéndose temporalmente la circulación."),
        SG("P-6", "Tram crossing", "Cruce de tranvía", "A crossing with a <b>tram line</b>, and the <b>tram has priority</b>.", "Cruce con una línea de <b>tranvía</b>, que <b>tiene prioridad de paso</b>."),
        SG("P-7", "Level crossing with barriers", "Paso a nivel con barreras", "A level crossing <b>with barriers or half-barriers</b>.", "Paso a nivel <b>provisto de barreras o semibarreras</b>."),
        SG("P-8", "Level crossing without barriers", "Paso a nivel sin barreras", "A level crossing <b>without barriers</b>.", "Paso a nivel <b>no provisto de barreras</b> o semibarreras."),
        SG("P-10a", "Approach to a level crossing, movable bridge or quay: 200 m", "Aproximación a paso a nivel, puente móvil o muelle: 200 m (P-10a y P-9a)",
           "Posts on the <b>left and right</b>: <b>3 stripes = 200 m</b>, 2 = 150 m (P-10b, P-9b), 1 = 100 m (P-10c, P-9c). Always with sign <b>P-5, P-7, P-8 or P-27</b>.",
           "Balizas a <b>izquierda y derecha</b>: <b>3 franjas = 200 m</b>, 2 = 150 m (P-10b, P-9b), 1 = 100 m (P-10c, P-9c). Siempre acompañadas de la señal <b>P-5, P-7, P-8 o P-27</b>."),
        SG("P-11", "Level crossing without barriers (at the crossing)", "Situación de un paso a nivel sin barreras", "Marks the <b>immediate presence</b> of an unbarriered level crossing.", "<b>Presencia inmediata</b> de un paso a nivel sin barreras."),
        SG("P-11a", "Same, more than one track", "Situación de un paso a nivel sin barreras de más de una vía férrea", "Unbarriered level crossing with <b>more than one track</b>.", "Paso a nivel sin barreras de <b>más de una vía férrea</b>."),
    ]))
    B.append(BOX("key", "Warning signs that are also priority signs", "Señales de advertencia que también son de prioridad", [
        ("Although they do not look like regulatory signs, <b>P-1, P-1a, P-1b, P-1c, P-1d, P-1e, P-2, P-6, P-7 and P-8</b> are also <b>priority signs</b>.",
         "Aunque no tienen la forma, color o diseño de las de reglamentación, <b>P-1, P-1a, P-1b, P-1c, P-1d, P-1e, P-2, P-6, P-7 y P-8</b> <b>también son señales de prioridad</b>."),
    ]))
    B.append(H3("5.2 Road layout and surface", "5.2 Trazado y firme de la vía"))
    B.append(SIGNS([
        SG("P-12", "Airport", "Aeropuerto", "Aircraft often fly <b>low over the road</b> and may make <b>sudden noise</b>.", "Lugar donde frecuentemente <b>vuelan aeronaves a baja altura</b> sobre la vía y pueden originar <b>ruidos imprevistos</b>."),
        SG("P-13a", "Dangerous bend to the right", "Curva peligrosa hacia la derecha", "A dangerous bend to the right.", "Curva peligrosa hacia la derecha."),
        SG("P-13b", "Dangerous bend to the left", "Curva peligrosa hacia la izquierda", "A dangerous bend to the left.", "Curva peligrosa hacia la izquierda."),
        SG("P-14a", "Dangerous bends, first to the right", "Curvas peligrosas hacia la derecha", "A series of close bends; <b>the first one to the right</b>.", "Sucesión de curvas próximas; <b>la primera, hacia la derecha</b>."),
        SG("P-14b", "Dangerous bends, first to the left", "Curvas peligrosas hacia la izquierda", "A series of close bends; <b>the first one to the left</b>.", "Sucesión de curvas próximas; <b>la primera, hacia la izquierda</b>."),
        SG("P-15", "Uneven road", "Perfil irregular", "A <b>bump or dip</b>, or a <b>road surface in poor condition</b>.", "<b>Resalte o badén</b> en la vía o <b>pavimento en mal estado</b>."),
        SG("P-15a", "Bump", "Resalte", "A <b>bump</b> in the road.", "<b>Resalte</b> en la vía."),
        SG("P-15b", "Dip", "Badén", "A <b>dip</b> in the road.", "<b>Badén</b> en la vía."),
        SG("P-16a", "Steep descent", "Bajada con fuerte pendiente", "A steep <b>downhill</b> stretch; the figure is the <b>gradient in %</b>.", "Tramo con fuerte pendiente <b>descendente</b>; la cifra indica la <b>inclinación en porcentaje</b>."),
        SG("P-16b", "Steep ascent", "Subida con fuerte pendiente", "A steep <b>uphill</b> stretch; the figure is the gradient in %.", "Tramo con fuerte pendiente <b>ascendente</b>; la cifra indica la inclinación en porcentaje."),
        SG("P-17", "Road narrows", "Estrechamiento de calzada",
           "The carriageway gets narrower. Also used when the <b>shoulders</b> get narrower. <b>Not</b> used when, after losing a lane, the remaining lanes and shoulders keep their width.",
           "Zona en la que se estrecha la calzada. También puede usarse si se reduce la anchura de los <b>arcenes</b>. <b>No</b> se usa cuando, tras reducirse el número de carriles, la anchura de los restantes y de los arcenes no varía."),
        SG("P-17a", "Road narrows on the right", "Estrechamiento de calzada por la derecha", "The carriageway narrows <b>on the right</b> (or the right shoulder does).", "La calzada se estrecha por la <b>derecha</b> (o el arcén derecho)."),
        SG("P-17b", "Road narrows on the left", "Estrechamiento de calzada por la izquierda", "The carriageway narrows <b>on the left</b> (or the left shoulder, on a one-way carriageway).", "La calzada se estrecha por la <b>izquierda</b> (o el arcén izquierdo, en calzada de sentido único)."),
        SG("P-18", "Roadworks", "Obras", "A stretch of road <b>under works</b> (yellow background).", "Tramo de vía en <b>obras</b> (fondo amarillo)."),
        SG("P-19", "Slippery road", "Pavimento deslizante", "The surface may be very slippery <b>for any reason</b>.", "Pavimento que puede resultar muy deslizante <b>por cualquier motivo</b>."),
        SG("P-25", "Two-way traffic", "Circulación en los dos sentidos", "Traffic runs <b>both ways</b>, temporarily or permanently.", "Zona donde la circulación se realiza, provisional o permanentemente, <b>en los dos sentidos</b>."),
        SG("P-26", "Falling rocks", "Desprendimiento", "Frequent <b>rockfalls</b>, so there may be obstacles on the road.", "Zona con <b>desprendimientos</b> frecuentes y posible presencia de obstáculos en la calzada."),
        SG("P-27", "Quay or riverbank", "Muelle", "The road <b>ends at a quay or at water</b>.", "La vía <b>desemboca en un muelle o en una corriente de agua</b>."),
        SG("P-28", "Loose chippings", "Proyección de gravilla", "Risk of <b>gravel being thrown up</b> by passing vehicles.", "Riesgo de que se <b>proyecte gravilla</b> al pasar los vehículos."),
        SG("P-29", "Crosswind", "Viento transversal", "Strong <b>crosswinds</b> are frequent. It does <b>not show which side</b> the wind comes from.", "Zona donde sopla frecuentemente <b>viento fuerte transversal</b>. <b>No indica el lado</b> del que sopla."),
        SG("P-30", "Side drop", "Escalón lateral", "A <b>drop along the edge</b> of the road, on the side the symbol shows.", "<b>Desnivel</b> a lo largo de la vía en el lado que indique el símbolo."),
        SG("P-34", "Ice or snow", "Pavimento deslizante por hielo o nieve", "In winter there is often <b>ice or snow</b> on this stretch.", "Tramo en el que frecuentemente, en invierno, hay <b>hielo o nieve</b>."),
    ]))
    B.append(H3("5.3 Road users and animals", "5.3 Usuarios y animales"))
    B.append(SIGNS([
        SG("P-20a", "Pedestrian crossing", "Paso para peatones", "<b>One or more</b> pedestrian crossings ahead.", "Proximidad de <b>uno o varios</b> pasos para peatones."),
        SG("P-20b", "Pedestrians", "Peatones", "A place or stretch with <b>many pedestrians</b>.", "Lugar o tramo con <b>elevado tránsito de peatones</b>."),
        SG("P-20c", "Pedestrian and cycle crossings", "Pasos para peatones y ciclistas", "A pedestrian crossing <b>next to or shared with</b> a cycle crossing.", "Paso para peatones <b>adosado o compartido</b> con un paso para ciclistas."),
        SG("P-21a", "Children", "Niños", "A place often used by <b>children</b>: a school, a playground…", "Lugar frecuentado por <b>niños</b>: escuela, zona de juegos…"),
        SG("P-21b", "People with reduced mobility", "Personas con dificultades motrices", "A place often used by people with <b>mobility or sensory</b> difficulties.", "Lugar frecuentado por personas con dificultades <b>motrices o sensoriales</b>."),
        SG("P-22a", "Cycle crossing", "Paso para ciclistas", "<b>One or more</b> cycle crossings ahead.", "Proximidad de <b>uno o varios</b> pasos para ciclistas."),
        SG("P-22b", "Cyclists", "Ciclistas", "A stretch with <b>frequent cyclists</b>.", "Tramo con <b>circulación frecuente de ciclistas</b>."),
        SG("P-23", "Farm animals", "Paso de animales domésticos o ganado", "<b>Domestic animals or livestock</b> often cross.", "La vía puede ser atravesada frecuentemente por <b>animales domésticos o ganado</b>."),
        SG("P-24", "Wild animals", "Paso de animales en libertad", "<b>Wild animals</b> often cross.", "La vía puede ser atravesada frecuentemente por <b>animales en libertad</b>."),
        SG("P-24a", "Wild animals (wild boar)", "Paso de animales en libertad (jabalíes)", "Wild animals often cross, a <b>large share of them wild boar</b>.", "Animales en libertad, en una proporción muy significativa <b>jabalíes</b>."),
    ]))
    B.append(H3("5.4 Traffic conditions", "5.4 Condiciones de la circulación"))
    B.append(SIGNS([
        SG("P-31", "Congestion", "Congestión", "Traffic is often <b>stopped or slow</b> because of congestion.", "Tramo en el que frecuentemente la circulación está <b>detenida o dificultada</b> por congestión."),
        SG("P-32", "Obstruction on the road", "Obstrucción en la calzada", "Vehicles are <b>blocking the road</b> because of a breakdown, accident or other causes.", "Vehículos que <b>obstruyen la calzada</b> por <b>avería, accidente u otras causas</b>."),
        SG("P-33", "Reduced visibility", "Visibilidad reducida", "Visibility is often lost through <b>fog, rain, snow, smoke</b>…", "Pérdida frecuente de visibilidad por <b>niebla, lluvia, nieve, humos</b>…"),
        SG("P-35", "Weaving", "Trenzado", "A stretch between a <b>merge and a fork</b> where vehicles change lanes and <b>their paths cross</b>, raising the risk of collisions.",
           "<b>Tramo entre una confluencia y una bifurcación</b> donde se producen cambios de carril, <b>cruzándose las trayectorias</b> y aumentando el riesgo de colisión."),
        SG("P-50", "Other dangers", "Otros peligros", "A danger <b>not covered by the other signs</b>.", "Peligro <b>distinto de los advertidos por otras señales</b>."),
    ]))

    # ---------------------------------------------------------------- 6. regulatory signs
    B.append(H2("6", "Regulatory signs (R)", "Señales de reglamentación (R)"))
    B.append(P("They tell road users the <b>obligations, limits or special prohibitions</b> they must respect.",
               "Indican a los usuarios las <b>obligaciones, limitaciones o prohibiciones especiales</b> que deben respetar."))
    B.append(H3("6.1 Where they start to apply", "6.1 Cuándo y cómo se aplican"))
    B.append(TABLE(
        [T("Rule", "Norma")],
        [
            [T("Prohibition, restriction and obligation signs apply <b>from the point where they stand</b>, unless a <b>complementary panel</b> below gives a distance.",
               "Las obligaciones, limitaciones o prohibiciones rigen <b>desde la sección transversal donde está la señal</b>, <b>salvo</b> que un <b>panel complementario</b> indique la distancia.")],
            [T("A regulatory sign <b>beside or above a town-name sign</b> applies to the <b>whole town</b>, unless other signs set something different on some stretches. "
               "If it is <b>before or after</b> the town sign, it applies only to that <b>travesía</b>.",
               "Las señales colocadas <b>al lado o en la vertical de la señal con el nombre del poblado</b> se aplican <b>a todo el poblado</b>, salvo otra reglamentación en ciertos tramos. "
               "Si están <b>antes o después</b> de la señal de poblado, solo se aplican a esa <b>travesía</b>.")],
        ],
    ))
    B.append(H3("6.2 Priority signs", "6.2 Señales de prioridad"))
    B.append(SIGNS([
        SG("R-1", "Give way", "Ceda el paso", "<b>Give way at the next junction</b> to vehicles on the road you are approaching or in the lane you want to join.",
           "Obligación de <b>ceder el paso en la próxima intersección</b> a los vehículos de la vía a la que se aproxime o del carril al que pretende incorporarse."),
        SG("R-2", "Stop", "Detención obligatoria o STOP",
           "<b>Stop at the next stop line</b> or, if there is none, <b>right before the junction</b>, and give way. If you still <b>cannot see</b> from there, <b>stop again</b> where you can, without endangering anyone.",
           "<b>Detenerse ante la próxima línea de detención</b> o, si no existe, <b>inmediatamente antes de la intersección</b>, y ceder el paso. Si desde allí <b>no hay visibilidad suficiente</b>, hay que <b>detenerse de nuevo</b> donde la haya, sin poner en peligro a nadie."),
        SG("R-3", "Priority road", "Calzada con prioridad", "On this carriageway you have <b>priority at junctions</b> over vehicles on, or coming from, the other one.",
           "Los conductores de esta calzada tienen <b>prioridad en las intersecciones</b> sobre los que circulen por otra o procedan de ella."),
        SG("R-4", "End of priority", "Fin de prioridad", "Your carriageway is about to <b>lose its priority</b>.", "Proximidad del lugar en que la calzada <b>pierde su prioridad</b>."),
        SG("R-5", "Give way to oncoming traffic", "Prioridad en sentido contrario", "<b>Do not enter a narrow passage</b> until you can get through without making oncoming vehicles stop.",
           "<b>Prohíbe entrar en un paso estrecho</b> mientras no se pueda atravesar sin obligar a detenerse a los que vienen en sentido contrario."),
        SG("R-6", "Priority over oncoming traffic", "Prioridad respecto al sentido contrario", "In the next narrow passage <b>you have priority</b> over oncoming vehicles.", "En el próximo paso estrecho <b>tienes prioridad</b> sobre los que circulan en sentido contrario."),
    ]))
    B.append(H3("6.3 No-entry signs", "6.3 Señales de prohibición de entrada"))
    B.append(P("They forbid entry to the vehicles or users <b>who meet them head-on</b>, from the point where they stand.",
               "Prohíben la entrada a los vehículos o usuarios <b>que se las encuentren de frente</b> en el sentido de su marcha, desde el lugar en que están."))
    B.append(SIGNS([
        SG("R-100", "No vehicles", "Circulación prohibida", "No vehicles of any kind, <b>in either direction</b>.", "Prohíbe la circulación de toda clase de vehículos <b>en ambos sentidos</b>."),
        SG("R-101", "No entry", "Entrada prohibida", "No entry for <b>any vehicle</b>.", "Prohíbe el acceso <b>a toda clase de vehículos</b>."),
        SG("R-102", "No motor vehicles", "Entrada prohibida a vehículos de motor", "No entry for <b>motor vehicles</b>.", "Prohíbe el acceso a <b>vehículos de motor</b>."),
        SG("R-103", "No motor vehicles except two-wheeled motorcycles", "Entrada prohibida a vehículos de motor, excepto motocicletas de dos ruedas",
           "No motor vehicles, but <b>two-wheeled motorcycles</b> and three-wheelers treated as motorcycles <b>may enter</b>.",
           "Prohíbe los vehículos de motor, pero <b>no</b> las <b>motocicletas de dos ruedas</b> ni los vehículos de tres ruedas asimilados."),
        SG("R-104", "No motorcycles", "Entrada prohibida a motocicletas", "No motorcycles or three-wheelers treated as motorcycles.", "Prohíbe motocicletas y vehículos de tres ruedas asimilados."),
        SG("R-105", "No mopeds", "Entrada prohibida a ciclomotores", "No mopeds, and <b>no vehicles for people with reduced mobility</b> either.", "Prohíbe ciclomotores y también los <b>vehículos para personas de movilidad reducida</b>."),
        SG("R-106", "No goods vehicles", "Entrada prohibida a vehículos destinados al transporte de mercancías", "No lorries, tractor units, vans… <b>whatever their mass</b>.", "Prohíbe camiones, tractocamiones y furgones o furgonetas, <b>independientemente de su masa</b>."),
        SG("R-107", "No goods vehicles over the mass shown", "Entrada prohibida a vehículos de mercancías con mayor masa autorizada que la indicada",
           "No goods vehicles whose <b>maximum authorised mass</b> is over the figure, <b>even if empty</b>.", "Prohíbe los de mercancías cuya <b>masa máxima autorizada</b> supere la indicada, <b>aunque circulen vacíos</b>."),
        SG("R-108", "No vehicles with dangerous goods", "Entrada prohibida a vehículos que transporten mercancías peligrosas", "No vehicles carrying dangerous goods that must be signed under their rules.", "Prohíbe los vehículos con mercancías peligrosas que deban ir señalizados según su normativa."),
        SG("R-109", "No vehicles with explosive or flammable goods", "Entrada prohibida a vehículos que transporten mercancías explosivas o inflamables", "No vehicles carrying explosive or easily flammable goods.", "Prohíbe los vehículos con mercancías explosivas o fácilmente inflamables."),
        SG("R-110", "No vehicles with water pollutants", "Entrada prohibida a vehículos que transporten productos contaminantes del agua", "No vehicles carrying <b>more than 1,000 litres</b> of products that can pollute water.", "Prohíbe los vehículos con <b>más de 1.000 litros</b> de productos capaces de contaminar el agua."),
        SG("R-111", "No farm vehicles", "Entrada prohibida a vehículos agrícolas de motor", "No tractors or other self-propelled farm machines.", "Prohíbe tractores y otras máquinas agrícolas autopropulsadas."),
        SG("R-112", "No vehicles with a trailer, except single-axle", "Entrada prohibida a vehículos de motor con remolque, excepto los de un solo eje",
           "A <b>tonnage</b> on the trailer (or on a plate) means it applies only when the <b>trailer’s maximum mass</b> is over that figure.", "Una <b>cifra de tonelaje</b> significa que solo se aplica si la <b>masa máxima del remolque</b> supera esa cifra."),
        SG("R-113", "No animal-drawn vehicles", "Entrada prohibida a vehículos de tracción animal", "No animal-drawn vehicles.", "Prohíbe los vehículos de tracción animal."),
        SG("R-114", "No cycles", "Entrada prohibida a ciclos", "No cycles.", "Prohíbe los ciclos."),
        SG("R-115", "No handcarts", "Entrada prohibida a carros de mano", "No handcarts.", "Prohíbe los carros de mano."),
        SG("R-116", "No pedestrians", "Entrada prohibida a peatones", "No pedestrians.", "Prohíbe el acceso a peatones."),
        SG("R-117", "No ridden animals", "Entrada prohibida a animales de montura", "No horses or other ridden animals.", "Prohíbe los animales de montura."),
        SG("R-118", "No personal mobility vehicles", "Entrada prohibida a vehículos de movilidad personal", "No <b>VMP</b> (e-scooters and similar).", "Prohíbe los <b>VMP</b>."),
        SG("R-119", "No cycles or VMP", "Entrada prohibida a ciclos y a vehículos de movilidad personal", "No cycles and no VMP.", "Prohíbe ciclos y VMP."),
        SG("R-120", "Entry restricted by environmental label", "Entrada prohibida a vehículos en función de su distintivo ambiental",
           "No entry depending on the vehicle’s <b>environmental label</b> or other criteria, given on panel <b>S-860</b> or on a placard (low-emission zones).",
           "Prohíbe el acceso según el <b>distintivo ambiental</b> u otros criterios, detallados en un panel <b>S-860</b> o en un cartel (zonas de bajas emisiones)."),
    ]))
    B.append(H3("6.4 Restriction signs", "6.4 Señales de restricción de paso"))
    B.append(P("They forbid or limit entry, as each one says, for those who meet them head-on, from where they stand.",
               "Prohíben o limitan la entrada, en la forma que se detalla, a quienes se las encuentren de frente, desde donde estén situadas."))
    B.append(SIGNS([
        SG("R-200", "No passing without stopping", "Prohibición de pasar sin detenerse",
           "You <b>must stop</b> because of a <b>customs, police, toll</b> or other post (there may be barriers). You may not go on until you have done what the sign requires.",
           "Lugar donde es <b>obligatoria la detención</b> por la proximidad de un <b>puesto de aduana, policía, peaje</b> u otro (puede haber medios mecánicos). No se puede reanudar la marcha hasta cumplir lo que establece."),
        SG("R-201", "Weight limit", "Limitación de masa", "No vehicles whose <b>actual laden mass</b> is over the tonnes shown.", "Prohíbe el paso a vehículos cuya <b>masa en carga</b> supere la indicada."),
        SG("R-202", "Axle-weight limit", "Limitación de masa por eje", "No vehicles with <b>any axle</b> carrying more than the figure.", "Prohíbe el paso si <b>algún eje</b> transmite más masa de la indicada."),
        SG("R-203", "Length limit", "Limitación de longitud", "No vehicles or combinations longer than shown, <b>load included</b>.", "Prohíbe vehículos o conjuntos más largos de lo indicado, <b>incluida la carga</b>."),
        SG("R-204", "Width limit", "Limitación de anchura", "No vehicles wider than shown, <b>load included</b>.", "Prohíbe vehículos más anchos de lo indicado, <b>incluida la carga</b>."),
        SG("R-205", "Height limit", "Limitación de altura", "No vehicles taller than shown, <b>load included</b>.", "Prohíbe vehículos más altos de lo indicado, <b>incluida la carga</b>."),
    ]))
    B.append(H3("6.5 Other prohibitions", "6.5 Otras señales de prohibición o restricción"))
    B.append(SIGNS([
        SG("R-300", "Minimum distance", "Separación mínima",
           "Keep <b>at least that gap</b> from the vehicle ahead, <b>except to overtake</b>. Without a figure it is a general reminder to keep a safe distance.",
           "Prohíbe circular sin mantener con el precedente una <b>separación igual o mayor</b> a la indicada, <b>excepto para adelantar</b>. Sin cifra, recuerda de forma genérica la distancia de seguridad."),
        SG("R-301", "Speed limit", "Velocidad máxima",
           "Do not go faster than the figure (km/h). It lasts until an <b>“end of speed limit”</b>, <b>“end of prohibitions”</b> or another <b>speed limit</b> sign; on the <b>same post as a warning sign</b>, it ends with the danger. "
           "On a road without priority it stops applying <b>after a junction with a priority road</b>. If it equals the road’s general limit, it is just a reminder.",
           "Prohíbe superar la velocidad indicada (km/h). Rige hasta la próxima señal de <b>«Fin de limitación de velocidad»</b>, <b>«Fin de prohibiciones»</b> u otra de <b>«Velocidad máxima»</b>; si está <b>en el mismo poste que una de peligro</b>, termina con el peligro. "
           "En una vía sin prioridad, deja de regir <b>al salir de una intersección con una vía con prioridad</b>. Si coincide con el límite genérico de la vía, solo lo recuerda."),
        SG("R-302", "No right turn", "Giro a la derecha prohibido", "Turning <b>right</b> is forbidden.", "Prohíbe girar a la <b>derecha</b>."),
        SG("R-303", "No left turn", "Giro a la izquierda prohibido", "Turning <b>left</b> is forbidden, and so is a <b>U-turn</b>.", "Prohíbe girar a la <b>izquierda</b> e <b>incluye</b> la prohibición del <b>cambio de sentido</b>."),
        SG("R-304", "No U-turn", "Media vuelta prohibida", "U-turns are forbidden, but you <b>may still turn left</b>.", "Prohíbe el cambio de sentido de la marcha, pero <b>sí permite cambiar de dirección</b> (girar)."),
        SG("R-305", "No overtaking", "Adelantamiento prohibido",
           "No vehicle may overtake <b>motor vehicles</b> when that means <b>using the side of the road for oncoming traffic</b>. From the sign until <b>“end of no overtaking”</b> or <b>“end of prohibitions”</b>.",
           "Prohíbe a todos adelantar a <b>vehículos de motor</b> cuando la maniobra <b>implique invadir la zona del sentido contrario</b>. Desde la señal hasta «Fin de prohibición de adelantamiento» o «Fin de prohibiciones»."),
        SG("R-306", "No overtaking for lorries", "Adelantamiento prohibido para camiones",
           "Lorries over <b>3,500 kg</b> may not overtake motor vehicles, <b>even without using the oncoming side</b>.", "Prohíbe a los camiones de MMA superior a <b>3.500 kg</b> adelantar a vehículos de motor, <b>incluso sin invadir el sentido contrario</b>."),
        SG("R-307", "No stopping or parking", "Parada y estacionamiento prohibido",
           "On the <b>side of the road where the sign stands</b>, from the sign <b>to the next junction</b> in your direction, unless shown otherwise.",
           "En el <b>lado de la calzada en que está la señal</b>, desde su vertical <b>hasta la intersección más próxima</b> en el sentido de la marcha, salvo indicación en contrario."),
        SG("R-307a", "No stopping or parking, both ways from the sign", "Parada y estacionamiento prohibido hacia ambos lados", "Between the nearest junctions or R-307b/R-307c signs on both sides.", "Entre las intersecciones o señales R-307b y R-307c más próximas a ambos lados."),
        SG("R-307b", "No stopping or parking, towards the arrow", "Parada y estacionamiento prohibido hacia el lado de la flecha", "From the sign to the junction or R-307c in the arrow’s direction (R-307c: the other way).", "Desde la señal hasta la intersección o R-307c en el sentido de la flecha (R-307c: al revés)."),
        SG("R-308", "No parking", "Estacionamiento prohibido", "On the side where it stands, from the sign to the next junction. <b>Stopping is allowed.</b>", "En el lado de la señal, desde su vertical hasta la intersección más próxima. <b>No prohíbe la parada.</b>"),
        SG("R-308c", "No parking, first half of the month", "Estacionamiento prohibido la primera quincena", "From <b>9:00 on day 1 to 9:00 on day 16</b>. Stopping allowed.", "Desde las <b>9 h del día 1 hasta las 9 h del día 16</b>. No prohíbe la parada."),
        SG("R-308d", "No parking, second half of the month", "Estacionamiento prohibido la segunda quincena", "From <b>9:00 on day 16 to 9:00 on day 1</b>. Stopping allowed.", "Desde las <b>9 h del día 16 hasta las 9 h del día 1</b>. No prohíbe la parada."),
        SG("R-308e", "No parking in front of an entrance", "Estacionamiento prohibido en vado", "No parking in front of a <b>vado</b> (a vehicle entrance).", "Prohíbe estacionar delante de un <b>vado</b>."),
        SG("R-308f", "No parking, both ways from the sign", "Estacionamiento prohibido hacia ambos lados", "Between the nearest junctions or R-308g/R-308h signs (R-308g/h: towards the arrow). Stopping allowed.", "Entre las intersecciones o señales R-308g y R-308h más próximas (R-308g/h: hacia la flecha). No prohíbe la parada."),
        SG("R-309", "Limited parking zone", "Zona de estacionamiento limitado",
           "Parking time is <b>limited</b> and you must show your <b>arrival time</b> as required. It may give the maximum time, the hours, and whether you <b>must pay</b>.",
           "Estacionamiento de <b>duración limitada</b>, con obligación de indicar la <b>hora de comienzo</b>. Puede incluir el tiempo máximo, el horario y si es <b>de pago</b>."),
        SG("R-310", "No horn", "Advertencias acústicas prohibidas", "Reminds you that the horn is forbidden, <b>except to avoid an accident</b>.", "Recuerda la prohibición de señales acústicas, <b>salvo para evitar un accidente</b>."),
    ]))
    B.append(H3("6.6 Obligation signs", "6.6 Señales de obligación"))
    B.append(P("They show a <b>compulsory traffic rule</b>.", "Señalan una <b>norma de circulación obligatoria</b>."))
    B.append(SIGNS([
        SG("R-400a", "Compulsory direction", "Sentido obligatorio", "The arrow shows the <b>direction you must follow</b> (R-400a to R-400e: right, left, straight on, turn right, turn left).", "La flecha señala la <b>dirección y sentido obligatorios</b> (R-400a a R-400e)."),
        SG("R-401a", "Pass on this side", "Paso obligatorio", "The arrow shows the <b>side of the island</b> you must pass (R-401c: either side).", "La flecha señala el <b>lado del refugio</b> por el que hay que pasar (R-401c: por ambos)."),
        SG("R-402", "Roundabout", "Sentido obligatorio en glorieta", "The arrows show the <b>direction to go round</b>.", "Las flechas señalan el <b>sentido del giro</b> obligatorio."),
        SG("R-403a", "Only directions allowed", "Únicas direcciones y sentidos permitidos", "The arrows are the <b>only directions</b> you may take (R-403a/b/c). They do <b>not allow U-turns</b>.", "Las flechas son las <b>únicas direcciones</b> permitidas (R-403a/b/c). <b>No permiten el cambio de sentido</b>."),
        SG("R-404", "Carriageway for automobiles (not two-wheeled motorcycles)", "Calzada obligatoria para automóviles, excepto motocicletas de dos ruedas", "Drivers of automobiles (except two-wheeled motorcycles and assimilated three-wheelers) must use this carriageway.", "Obligación para los automóviles (salvo motos de dos ruedas y tres ruedas asimilados) de circular por esta calzada."),
        SG("R-405", "Carriageway for two-wheeled motorcycles", "Calzada obligatoria para motocicletas de dos ruedas", "Two-wheeled motorcycles (and assimilated three-wheelers) must use it.", "Obligación para las motocicletas de dos ruedas y tres ruedas asimilados."),
        SG("R-406", "Carriageway for goods vehicles", "Calzada obligatoria para camiones, tractocamiones y furgones o furgonetas",
           "Lorries, tractor units and vans must use it, <b>whatever their mass</b>; with a tonnage, only those whose maximum mass is over it.", "Obligación para camiones, tractocamiones y furgones, <b>independientemente de su masa</b>; con tonelaje, solo si su MMA lo supera."),
        SG("R-407a", "Cycle track", "Vía reservada y obligatoria para ciclos", "Cyclists <b>must use it</b> and <b>no one else may</b>.", "Obligación para los ciclos y <b>prohibición para los demás</b> usuarios."),
        SG("R-407b", "Moped track", "Vía reservada y obligatoria para ciclomotores", "Mopeds must use it and no one else may.", "Obligación para los ciclomotores y prohibición para los demás."),
        SG("R-408", "Path for animal-drawn vehicles", "Camino obligatorio para vehículos de tracción animal", "Animal-drawn vehicles must use it.", "Obligación para los vehículos de tracción animal."),
        SG("R-409", "Bridle path", "Camino reservado y obligatorio para animales de montura", "Riders must use it and no one else may.", "Obligación para los jinetes y prohibición para los demás."),
        SG("R-410", "Footpath", "Camino reservado y obligatorio para peatones", "Pedestrians must use it and no one else may.", "Obligación para los peatones y prohibición para los demás."),
        SG("R-411", "Minimum speed", "Velocidad mínima",
           "Go <b>at least</b> at that speed until another minimum-speed sign, an <b>“end of minimum speed”</b> or a <b>speed limit equal or lower</b>.",
           "Circular <b>al menos</b> a esa velocidad hasta otra de velocidad mínima, la de <b>«Fin de velocidad mínima»</b> o una de <b>velocidad máxima igual o inferior</b>."),
        SG("R-412", "Snow chains", "Cadenas para nieve",
           "Do not go on without <b>snow chains</b> or other approved anti-skid devices on <b>at least one wheel on each side of the same drive axle</b>, or <b>special snow tyres</b>.",
           "No seguir sin <b>cadenas</b> u otros dispositivos antideslizantes autorizados en <b>al menos una rueda a cada lado del mismo eje motor</b>, o <b>neumáticos especiales de nieve</b>."),
        SG("R-412b", "Winter tyres", "Neumáticos de invierno", "Do not go on without <b>special winter tyres</b>.", "No seguir sin <b>neumáticos especiales de invierno</b>."),
        SG("R-413", "Dipped headlights", "Alumbrado de corto alcance", "Use <b>at least dipped beam</b>, whatever the visibility, until the sign ending the obligation.", "Circular <b>al menos con luz de corto alcance</b>, con independencia de la visibilidad, hasta la señal de fin."),
        SG("R-414", "Carriageway for dangerous goods", "Calzada obligatoria para vehículos con mercancías peligrosas", "Vehicles with dangerous goods must use it, following their special rules.", "Obligación para los que transporten mercancías peligrosas."),
        SG("R-415", "Carriageway for water pollutants", "Calzada obligatoria para vehículos con productos contaminantes del agua", "Vehicles carrying <b>more than 1,000 litres</b> of water pollutants must use it.", "Obligación para los que lleven <b>más de 1.000 litros</b> de contaminantes del agua."),
        SG("R-416", "Carriageway for explosive or flammable goods", "Calzada obligatoria para vehículos con materias explosivas o inflamables", "Those vehicles must use it.", "Obligación para esos vehículos."),
        SG("R-417", "Seat belt", "Uso obligatorio del cinturón de seguridad", "Reminds you that the <b>seat belt</b> is compulsory.", "Recuerda la obligación de usar el <b>cinturón</b>."),
        SG("R-418", "Electronic toll only", "Vía exclusiva para vehículos con telepeaje (telepeaje obligatorio)", "You must pay by <b>electronic toll</b>; vehicles in that lane must carry the device.", "Obligación de pagar con <b>telepeaje</b>; los vehículos de ese carril deben llevar el dispositivo."),
        SG("R-419", "Path for tractors", "Camino obligatorio para tractores", "Tractors must use it.", "Obligación para los tractores."),
        SG("R-420", "VMP track", "Vía reservada y obligatoria para VMP", "VMP must use it and no one else may.", "Obligación para los VMP y prohibición para los demás."),
        SG("R-421", "Track for cycles and VMP", "Vía reservada y obligatoria para ciclos y VMP", "Cycles and VMP must use it and no one else may.", "Obligación para ciclos y VMP y prohibición para los demás."),
        SG("R-422", "Dismount and walk", "Desmontar y continuar a pie", "Cyclists must <b>go on foot</b>. If only at certain times, a panel says so.", "Los ciclistas deben <b>continuar a pie</b>. Si es solo en ciertos periodos, lo indica un panel."),
    ]))
    B.append(H3("6.7 End of prohibition or restriction", "6.7 Señales de fin de prohibición o restricción"))
    B.append(SIGNS([
        SG("R-500", "End of all prohibitions", "Fin de prohibiciones", "From here, <b>all the specific prohibitions</b> set by earlier signs for moving vehicles stop applying.", "Desde aquí dejan de aplicarse <b>todas las prohibiciones específicas</b> de señales anteriores para vehículos en movimiento."),
        SG("R-501", "End of speed limit", "Fin de limitación de velocidad", "Ends an earlier <b>speed limit</b> sign.", "Fin de una señal anterior de «Velocidad máxima»."),
        SG("R-502", "End of no overtaking", "Fin de la prohibición de adelantamiento", "Ends an earlier <b>no overtaking</b> sign.", "Fin de una señal anterior de «Adelantamiento prohibido»."),
        SG("R-503", "End of no overtaking for lorries", "Fin de la prohibición de adelantamiento para camiones", "Ends the lorry overtaking ban.", "Fin de «Adelantamiento prohibido para camiones»."),
        SG("R-504", "End of limited parking zone", "Fin de zona de estacionamiento limitado", "Ends the limited parking zone.", "Fin de «Zona de estacionamiento limitado»."),
        SG("R-505", "End of cycle track", "Fin de vía reservada para ciclos", "Ends the cycle track.", "Fin de «Vía reservada para ciclos»."),
        SG("R-506", "End of minimum speed", "Fin de velocidad mínima", "Ends the minimum speed.", "Fin de una señal anterior de velocidad mínima."),
        SG("R-507", "End of the carriageway for automobiles", "Fin de calzada obligatoria para automóviles", "Ends R-404. R-508 to R-516 end the other obligations in the same way (motorcycles, goods vehicles, mopeds, animal-drawn vehicles, riders, pedestrians, tractors, VMP, cycles and VMP).",
           "Fin de R-404. Las R-508 a R-516 terminan del mismo modo las demás obligaciones (motocicletas, camiones, ciclomotores, tracción animal, montura, peatones, tractores, VMP, ciclos y VMP)."),
        SG("R-513", "End of footpath", "Fin de camino reservado y obligatorio para peatones", "Ends the footpath.", "Fin del camino para peatones."),
    ]))

    # ---------------------------------------------------------------- 7. indication signs
    B.append(H2("7", "Indication signs (S)", "Señales de indicación (S)"))
    B.append(P(
        "They give road users <b>useful information</b>. Families: general indications, lanes, services, orientation, complementary panels and other signs. "
        "They may carry a <b>panel underneath</b> with the distance to the place they refer to.",
        "Facilitan al usuario <b>indicaciones útiles</b>. Categorías: indicaciones generales, carriles, servicio, orientación, paneles complementarios y otras señales. "
        "Pueden llevar un <b>panel en su parte inferior</b> con la distancia entre la señal y el lugar señalado."))
    B.append(H3("7.1 General indications: types of road and zones", "7.1 Indicaciones generales: tipos de vía y zonas"))
    B.append(SIGNS([
        SG("S-1", "Motorway", "Autopista", "Start of a motorway: its <b>special rules</b> apply from here. It can also announce one or mark the slip road to it. <b>S-2</b>: end of motorway.",
           "Principio de una autopista: desde aquí se aplican sus <b>reglas especiales</b>. También puede anunciarla o indicar el ramal que conduce a ella. <b>S-2</b>: fin de autopista."),
        SG("S-1a", "Autovía (dual carriageway)", "Autovía", "Start of an autovía and its special rules. <b>S-2a</b>: end.", "Principio de una autovía y de sus reglas especiales. <b>S-2a</b>: fin."),
        SG("S-3", "Road for automobiles", "Vía reservada para automóviles", "Start of a road reserved for automobiles. <b>S-4</b>: end.", "Principio de una vía reservada a automóviles. <b>S-4</b>: fin."),
        SG("S-1b", "Multi-lane road", "Carretera multicarril", "Start of a multi-lane road, where its special rules apply; may mark the slip road to one. <b>S-2b</b>: end.", "Principio de una carretera multicarril y de sus reglas especiales; puede indicar el ramal que conduce a ella. <b>S-2b</b>: fin."),
        SG("S-1c", "2+1 road", "Carretera 2+1", "Three lanes, both directions: the <b>middle lane is for overtaking</b>, given to each direction <b>in turn</b>. <b>S-2c</b>: end.",
           "Tres carriles en ambos sentidos: el <b>carril central es para adelantar</b>, reservado <b>de forma alterna</b> a uno y otro sentido. <b>S-2c</b>: fin."),
        SG("S-5", "Tunnel", "Túnel", "Start (and maybe name) of a tunnel, underpass or stretch treated as a tunnel; may show its <b>length</b>.", "Principio (y quizá nombre) de un túnel, paso inferior o tramo equiparado; puede indicar su <b>longitud</b>."),
        SG("S-7", "Advisory maximum speed", "Velocidad máxima aconsejable",
           "<b>Recommends</b> not going faster than about that speed, even in good conditions. Under a warning sign, it refers to the dangerous stretch. <b>S-8</b>: end.",
           "<b>Recomienda</b> no sobrepasar esa velocidad aproximada, aunque las condiciones sean favorables. Bajo una señal de peligro, se refiere al tramo peligroso. <b>S-8</b>: fin."),
        SG("S-9", "Advisory speed range", "Intervalo aconsejado de velocidades", "<b>Recommends</b> keeping between the two figures in good conditions. <b>S-10</b>: end.", "<b>Recomienda</b> mantener la velocidad entre los valores, con condiciones favorables. <b>S-10</b>: fin."),
        SG("S-11", "One-way carriageway", "Calzada de sentido único", "Drive in the <b>direction of the arrow</b>; going the other way is forbidden. <b>S-11a/S-11b</b>: one arrow per lane.", "Se circula en el <b>sentido de la flecha</b>; prohibido el contrario. <b>S-11a/S-11b</b>: una flecha por carril."),
        SG("S-12", "One-way stretch", "Tramo de calzada de sentido único", "The stretch the arrow points to is one-way (left or right).", "En el tramo hacia el que apunta la flecha se circula en ese sentido (izquierda o derecha)."),
        SG("S-13", "Pedestrian crossing here", "Situación de un paso para peatones", "Where a pedestrian crossing is. <b>S-45</b>: cycle crossing; <b>S-46</b>: pedestrian and cycle crossing.", "Situación de un paso para peatones. <b>S-45</b>: paso para ciclistas; <b>S-46</b>: para peatones y ciclistas."),
        SG("S-14a", "Pedestrian footbridge", "Paso superior para peatones", "<b>S-14b</b>: underpass; <b>S-14c/d</b>: with ramp; <b>S-14e/f</b>: with a rail or ramp for cycles.", "<b>S-14b</b>: paso inferior; <b>S-14c/d</b>: con rampa; <b>S-14e/f</b>: con rail o rampa para ciclos."),
        SG("S-15a", "No through road ahead", "Preseñalización de calzada sin salida", "The road marked with a <b>red bar has no exit</b> (S-15a to S-15d; mirror versions possible). <b>S-15e</b>: except for pedestrians or cycles.",
           "La calzada con el <b>recuadro rojo no tiene salida</b> (S-15a a S-15d; puede usarse la figura simétrica). <b>S-15e</b>: salvo para peatones o ciclos."),
        SG("S-16", "Emergency escape lane", "Zona de frenado de emergencia", "An <b>escape area</b> to stop a vehicle whose <b>brakes have failed</b>.", "Zona de escape para detener un vehículo con <b>fallo de frenos</b>."),
        SG("S-17", "Parking", "Estacionamiento", "Parking allowed. A vehicle symbol reserves it; times <b>limit its length</b>.", "Estacionamiento autorizado. Un símbolo de vehículo lo reserva; los horarios <b>limitan su duración</b>."),
        SG("S-17a", "Parking for a specific need", "Estacionamiento de necesidad", "Parking <b>only for a specific purpose</b> (pharmacy, hospital…) shown by a pictogram, for a time given on a panel.", "Estacionamiento <b>solo para un fin concreto</b> (farmacia, hospital…) indicado con pictograma, durante el tiempo del panel."),
        SG("S-18", "Taxi rank", "Lugar reservado para taxis", "Reserved for <b>stopping and parking</b> free and in-service taxis; a number gives the spaces.", "Reservado a la <b>parada y estacionamiento</b> de taxis libres y en servicio; un número indica las plazas."),
        SG("S-19", "Bus stop", "Parada de autobuses", "Place reserved for buses to stop. <b>S-20</b>: tram stop.", "Lugar reservado a la parada de autobuses. <b>S-20</b>: parada de tranvías."),
        SG("S-21", "Mountain pass status", "Transitabilidad en tramo o puerto de montaña", "Whether the pass or stretch is open, restricted, closed or needs <b>chains</b>.", "Situación de transitabilidad del puerto o tramo (abierto, con restricción, cerrado, cadenas)."),
        SG("S-22", "U-turn on the same level", "Cambio de sentido al mismo nivel", "A place nearby where you can <b>turn round on the same level</b>. <b>S-25</b>: via an exit at a different level.", "Lugar próximo para <b>cambiar de sentido al mismo nivel</b>. <b>S-25</b>: por una salida a distinto nivel."),
        SG("S-23", "Hospital", "Hospital", "Take the care medical centres need, above all <b>avoid noise</b>.", "Conviene tomar precauciones por la proximidad de centros médicos, sobre todo <b>evitar ruidos</b>."),
        SG("S-24", "End of compulsory dipped beam", "Fin de obligación de alumbrado de corto alcance", "Reminds you that you <b>may switch it off</b> unless visibility, time or lighting require it.", "Recuerda que se <b>puede prescindir</b> de él salvo que lo exijan la visibilidad, la hora o la iluminación."),
        SG("S-26", "Exit countdown markers", "Paneles de aproximación a salida",
           "On motorways, autovías and roads for automobiles: the next exit is about <b>300, 200 or 100 m</b> away. For an exit on the <b>left</b>, the bars slope the other way and the panels stand on the left.",
           "En autopista, autovía o vía para automóviles, la próxima salida está a unos <b>300, 200 o 100 m</b>. Si la salida es por la <b>izquierda</b>, las diagonales descienden de izquierda a derecha y los paneles van a la izquierda."),
        SG("S-32", "Electronic toll", "Telepeaje", "In these lanes you <b>can</b> pay by electronic toll if your vehicle has the device.", "En esos carriles se <b>puede</b> pagar con telepeaje si se dispone del medio técnico."),
        SG("S-34", "Lay-by", "Apartadero", "A place to <b>pull over in an emergency</b> and leave the way clear. <b>S-34a</b>: in a tunnel, with an emergency phone.", "Lugar donde <b>apartar el vehículo en caso de emergencia</b>. <b>S-34a</b>: en túnel, con teléfono de emergencia."),
        SG("S-27", "Roadside help", "Auxilio en carretera", "Nearest <b>SOS post</b> to ask for help after an accident or breakdown; may give the distance.", "<b>Poste o puesto de socorro</b> más próximo; puede indicar la distancia."),
        SG("S-28", "Residential play zone", "Zona de estancia y juego",
           "Mainly for pedestrians: vehicles at <b>10 km/h</b> maximum; <b>no parking</b> except in marked places; pedestrians may use the whole area (<b>games and sports allowed</b>); no marked crossings; "
           "pedestrians must not needlessly hinder vehicles; cycles and VMP may go <b>both ways</b> unless signed. Always with a 10 km/h limit sign. <b>S-29</b>: end.",
           "Destinada en primer lugar a peatones: <b>velocidad máxima 10 km/h</b>; <b>no se puede estacionar</b> salvo en lugares designados; los peatones usan toda la zona (<b>juegos y deportes autorizados</b>); no se señalizan pasos; "
           "los peatones no deben estorbar inútilmente; ciclos y VMP pueden ir <b>en ambos sentidos</b> salvo indicación. Siempre con señal de 10 km/h. <b>S-29</b>: fin."),
        SG("S-47", "Shared space (coexistence zone)", "Zona de coexistencia",
           "Mainly for pedestrians: vehicles at <b>20 km/h</b> maximum; no parking except in marked places; pedestrians may use the whole area but <b>games and sports are NOT allowed</b>; no marked crossings; "
           "cycles and VMP may go both ways unless signed. <b>S-48</b>: end.",
           "Destinada en primer lugar a peatones: <b>velocidad máxima 20 km/h</b>; no se puede estacionar salvo en lugares designados; los peatones usan toda la zona, pero <b>juegos y deportes NO autorizados</b>; no se señalizan pasos; "
           "ciclos y VMP en ambos sentidos salvo indicación. <b>S-48</b>: fin."),
        SG("S-30a", "Pedestrian zone", "Zona peatonal", "Zone reserved for pedestrians. <b>S-31a</b>: end.", "Zona reservada al uso peatonal. <b>S-31a</b>: fin."),
        SG("S-33", "Shared foot and cycle path", "Senda ciclopeatonal",
           "Path for pedestrians, cycles and maybe VMP, <b>away from motor traffic</b> (parks, open spaces; out of town it may run beside the road). Cycles and VMP <b>slow down</b> near walkers; walkers <b>let them pass</b>. Green sign.",
           "Vía para peatones, ciclos y, en su caso, VMP, <b>segregada del tráfico motorizado</b> (parques, espacios abiertos; fuera de poblado puede ir paralela a la carretera). Ciclos y VMP <b>reducen</b> ante peatones; los peatones <b>facilitan su paso</b>. Señal verde."),
        SG("S-35", "Cycle track", "Vía reservada para ciclos", "A road for cycles; <b>others may not use it</b>. <b>S-36</b>: end. Same pattern: <b>S-37/S-39</b> VMP, <b>S-38/S-40</b> cycles and VMP.",
           "Vía para ciclos; <b>prohibida a los demás</b>. <b>S-36</b>: fin. Igual: <b>S-37/S-39</b> VMP, <b>S-38/S-40</b> ciclos y VMP."),
        SG("S-41", "Cycles and pedestrians, separate spaces", "Vía reservada para ciclos y peatones con espacio diferenciado", "Each has its own space; the drawing may match the real layout. <b>S-42</b>: end. <b>S-43/S-44</b>: cycles, VMP and pedestrians.",
           "Cada uno con su espacio; el diseño puede adaptarse a la vía. <b>S-42</b>: fin. <b>S-43/S-44</b>: ciclos, VMP y peatones."),
        SG("S-49", "Advanced stop box for motorbikes or bikes", "Avanza moto o bici",
           "A <b>waiting area before the stop line</b> at a junction with traffic lights, reserved for the vehicles shown: motorcycles, three-wheelers and mopeds (all shown by the motorcycle), or cycles.",
           "<b>Zona de espera previa a la línea de detención</b> en una intersección con semáforos, reservada a los vehículos de la señal: motocicletas, tres ruedas y ciclomotores (todos con el pictograma de moto), o ciclos."),
    ]))
    B.append(H3("7.2 Lane signs", "7.2 Señales de carriles"))
    B.append(P("They set special rules for one or more lanes of the carriageway.", "Indican una reglamentación especial para uno o más carriles de la calzada."))
    B.append(SIGNS([
        SG("S-50d", "Lanes by minimum speed", "Carriles reservados en función de la velocidad señalizada",
           "The lane(s) with a minimum-speed figure are only for vehicles going <b>at least that fast</b>; even so, you should keep to the <b>right lane</b> when you can (S-50a to S-50e).",
           "El carril o carriles con velocidad mínima solo pueden usarlos quienes circulen a <b>velocidad igual o superior</b>; aun así, si es posible, hay que ir por el <b>carril derecho</b> (S-50a a S-50e)."),
        SG("S-51a", "Bus lane", "Carril reservado para autobuses",
           "Only for the vehicles shown (buses, motorcycles, taxis, cycles…). Where its line is <b>dashed</b>, others may use it <b>only for a manoeuvre other than stopping, parking, turning round or overtaking</b>, giving preference to authorised vehicles.",
           "Exclusivo para los vehículos del pictograma (autobuses, motos, taxis, ciclos…). Donde la marca es <b>discontinua</b>, los demás pueden usarlo <b>solo para maniobras que no sean parar, estacionar, cambiar de sentido o adelantar</b>, dando preferencia a los autorizados."),
        SG("S-51b", "High-occupancy (VAO) lane", "Carril reservado para vehículos con alta ocupación (VAO)", "Only for vehicles with <b>at least the number of people shown</b>; may be combined with other vehicle types.", "Exclusivo para vehículos con <b>al menos el número de ocupantes indicado</b>; puede combinarse con otros tipos."),
        SG("S-52", "End of a lane", "Final de carril destinado a la circulación", "On a one-way carriageway, the lane shown <b>ends</b> and you must change lane (S-52, S-52c to S-52g). <b>S-52a/b</b>: the same on a two-way road.",
           "En calzada de sentido único, el carril indicado <b>desaparece</b> y hay que cambiar de carril (S-52, S-52c a S-52g). <b>S-52a/b</b>: igual en calzada de doble sentido."),
        SG("S-53", "One lane becomes two", "Paso de uno a dos carriles", "A one-lane stretch gets a <b>second lane</b> in the same direction. <b>S-53a</b>: with each lane’s speed limit. <b>S-53b/S-53c</b>: two become three.", "Se pasa a disponer de <b>dos carriles</b> en el mismo sentido. <b>S-53a</b>: con la velocidad máxima de cada uno. <b>S-53b/S-53c</b>: de dos a tres."),
        SG("S-60a", "Fork to the left (two lanes)", "Bifurcación hacia la izquierda en calzada de dos carriles", "Next stretch: the <b>left lane splits off to the left</b>. <b>S-60b</b>: right lane to the right; <b>S-61a/b</b> three lanes; <b>S-62a/b</b> four lanes.",
           "En el próximo tramo el <b>carril izquierdo se bifurca hacia la izquierda</b>. <b>S-60b</b>: el derecho a la derecha; <b>S-61a/b</b> tres carriles; <b>S-62a/b</b> cuatro."),
        SG("S-61c", "Fork right with one oncoming lane", "Bifurcación hacia la derecha con un carril en sentido opuesto", "Two-way road with two lanes your way: the <b>right lane</b> forks with a change of direction.", "Calzada de doble sentido con dos carriles en el propio: bifurcación con cambio de dirección en el <b>carril derecho</b>."),
        SG("S-63a", "Fork on a four-lane carriageway", "Bifurcación en calzada de cuatro carriles", "The <b>two left lanes go left</b> and the <b>two right lanes go right</b>. <b>S-63c/d</b>: two lanes fork left/right. <b>S-63b</b>: three lanes, the middle one splits.",
           "Los <b>dos izquierdos van a la izquierda</b> y los <b>dos derechos a la derecha</b>. <b>S-63c/d</b>: dos carriles a izquierda/derecha. <b>S-63b</b>: tres carriles, se bifurca el central."),
        SG("S-64a", "Compulsory cycle lane beside the carriageway", "Vía reservada y obligatoria para ciclos adosada a calzada", "Cyclists <b>must use</b> the lane under the cycle; <b>others may not</b>. The arrows show the lanes and their directions (S-64a/b). <b>S-65a/b</b>: reserved but not compulsory.",
           "Los ciclos <b>deben usar</b> el carril de la señal y los <b>demás no pueden</b>. Las flechas indican carriles y sentidos (S-64a/b). <b>S-65a/b</b>: reservado, no obligatorio."),
        SG("S-66", "Contraflow cycle lane", "Carril bici en sentido opuesto", "A compulsory cycle lane running <b>against the direction</b> of the next lane.", "Carril obligatorio para ciclos cuyo sentido es <b>opuesto al del carril contiguo</b>."),
        SG("S-68", "One lane your way, two the other way", "Un carril para el sentido propio y dos para el opuesto", "On a two-way road, you have <b>one lane</b> and oncoming traffic two; a panel gives the length.", "En doble sentido, se dispone de <b>un carril</b> y el contrario de dos; un panel indica la longitud."),
        SG("S-70a", "Lane merging from the left", "Confluencia de un carril por la izquierda", "A lane <b>joins</b> on the side of the <b>dashed arrow</b>; solid arrows are the lanes your way (S-70 to S-72, a = left, b = right). <b>S-73a/b</b>: two lanes join.",
           "Confluye un carril por el lado de la <b>flecha discontinua</b>; las continuas son los carriles en ese sentido (S-70 a S-72, a = izquierda, b = derecha). <b>S-73a/b</b>: confluyen dos carriles."),
    ]))
    B.append(H3("7.3 Service signs", "7.3 Señales de servicio"))
    B.append(P("They tell you where a <b>service</b> that may be useful is.", "Informan de la situación de un <b>servicio</b> de posible utilidad."))
    B.append(SIGNS([
        SG("S-100", "First-aid post", "Puesto de socorro", "An officially recognised centre for <b>emergency treatment</b>.", "Centro oficialmente reconocido para <b>curas de urgencia</b>."),
        SG("S-101", "Ambulance base", "Base de ambulancia", "An <b>ambulance on permanent duty</b> to treat and move people injured in road accidents.", "<b>Ambulancia en servicio permanente</b> para curar y trasladar heridos en accidentes."),
        SG("S-102", "Vehicle inspection (ITV)", "Servicio de inspección técnica de vehículos", "An <b>ITV</b> station.", "Estación de <b>ITV</b>."),
        SG("S-103", "Repair workshop", "Taller de reparación", "A garage. <b>S-106</b>: workshop and fuel.", "Taller. <b>S-106</b>: taller y surtidor."),
        SG("S-104", "Telephone", "Teléfono", "A telephone.", "Aparato telefónico."),
        SG("S-105", "Fuel", "Surtidor de carburante", "Fuel station. <b>S-105b</b>: fuel and LPG; <b>S-105c</b>: LPG.", "Surtidor de carburante. <b>S-105b</b>: carburante y GLP; <b>S-105c</b>: GLP."),
        SG("S-105e", "Electric charging station", "Estación de recarga eléctrica", "Charging point. <b>S-105d</b>: fuel and charging; <b>S-105f</b>: fuel, LPG and charging.", "Recarga eléctrica. <b>S-105d</b>: carburante y recarga; <b>S-105f</b>: carburante, GLP y recarga."),
        SG("S-107", "Campsite", "Campamento", "A place where you can camp. <b>S-113</b>: caravans; <b>S-116</b>: both.", "Lugar donde puede acamparse. <b>S-113</b>: remolques vivienda; <b>S-116</b>: ambos."),
        SG("S-108", "Water", "Agua", "Drinking water.", "Agua."),
        SG("S-109", "Scenic spot", "Lugar pintoresco", "A picturesque place.", "Lugar pintoresco."),
        SG("S-110", "Hotel or motel", "Hotel o motel", "Accommodation.", "Alojamiento."),
        SG("S-111", "Restaurant", "Restauración", "A restaurant. <b>S-112</b>: café.", "Restaurante. <b>S-112</b>: cafetería."),
        SG("S-114", "Picnic area", "Merendero", "A place to eat and drink.", "Lugar para el consumo de comidas o bebidas."),
        SG("S-115", "Start of walking routes", "Punto de partida para excursiones a pie", "Starting point for walks.", "Punto de partida para excursiones."),
        SG("S-117", "Youth hostel", "Albergue juvenil", "A hostel reserved for youth organisations.", "Albergue reservado a organizaciones juveniles."),
        SG("S-118", "Tourist information", "Información turística", "Tourist information.", "Información turística."),
        SG("S-119", "Fishing reserve", "Coto de pesca", "A fishing reserve.", "Coto de pesca."),
        SG("S-120", "Park or natural area", "Parque o espacio natural", "A park or nature area. <b>S-121</b>: monument.", "Parque o espacio natural. <b>S-121</b>: monumento."),
        SG("S-122", "Other services", "Otros servicios", "Generic sign: the service is drawn in the white square.", "Señal genérica: el servicio se inscribe en el recuadro blanco."),
        SG("S-123", "Rest area", "Área de descanso", "A rest area.", "Área de descanso."),
        SG("S-124", "Park and ride (train)", "Estacionamiento para usuarios del ferrocarril", "Parking linked to a station, for drivers who continue by train. <b>S-125</b>: metro; <b>S-126</b>: bus.", "Estacionamiento conectado con una estación para seguir en tren. <b>S-125</b>: metro; <b>S-126</b>: autobús."),
        SG("S-128", "Caravan waste disposal point", "Punto de vaciado de caravanas y autocaravanas", "Emptying point for caravans’ and motorhomes’ waste water.", "Vaciado de aguas residuales de caravanas y autocaravanas."),
        SG("S-129", "Emergency snow parking", "Estacionamiento de emergencia por nevadas", "Emergency parking during snowfalls and, exceptionally, incidents.", "Estacionamiento de emergencia por nevadas y, excepcionalmente, incidencias."),
    ]))
    B.append(H3("7.4 Orientation signs", "7.4 Señales de orientación"))
    B.append(P("They <b>locate and guide</b> road users: pre-signposting, direction, road numbers, location, confirmation and urban signs.",
               "Su finalidad es <b>situar y orientar</b> a los usuarios: preseñalización, dirección, identificación de carreteras, localización, confirmación y uso específico en poblado."))
    B.append(TABLE(
        [T("Feature", "Elemento"), T("Rule", "Norma")],
        [
            [T("<b>Distance panels</b> (pre-signposting)", "<b>Paneles complementarios</b> (preseñalización)"),
             T("Conventional and multi-lane roads: <b>distance</b> to the exit. Motorways and autovías: <b>distance and the exit’s kilometre</b> (exit number). Direction signs on motorways: <b>kilometre</b> of the exit.",
               "Convencionales y multicarril: <b>distancia</b> a la salida. Autopista y autovía: <b>distancia y kilómetro</b> de la salida. Señales de dirección en autopista y autovía: <b>kilómetro</b> de la salida inmediata.")],
            [T("<b>Arrows</b>", "<b>Flechas</b>"),
             T("Direction signs: <b>one arrow per lane, pointing down</b>, under the place name and smaller. Pre-signposting: <b>slanted (45° up or down)</b>, beside the name and bigger.",
               "Señales de dirección: <b>tantas flechas como carriles, hacia abajo</b>, bajo el nombre y de menor tamaño. Preseñalización: <b>inclinadas (45°)</b>, junto al nombre y de mayor tamaño.")],
            [T("<b>Colours</b>", "<b>Colores</b>"),
             T("Conventional and multi-lane roads: <b>white</b> background, black letters. Motorways and autovías: <b>blue</b> background, white letters (some pictograms black).",
               "Convencionales y multicarril: fondo <b>blanco</b>, letras negras. Autopistas y autovías: fondo <b>azul</b>, letras blancas (algunos pictogramas en negro).")],
        ],
        widths=["26%", "74%"],
    ))
    B.append(FIG(exit_colours, "On a motorway, the exit sign at the exit always takes the colour of the road you are heading to; the pre-signposting stays blue when the exit leads to a lower-category road.",
                 "En autopista, el cartel de la salida toma siempre el color de la vía de destino; la preseñalización sigue en azul si la salida lleva a una vía de inferior categoría."))
    B.append(BOX("key", "How exits are signed", "¿Cómo se señalizan las salidas?", [
        ("<b>Confirmation</b> signs <b>always</b> have the colour of the road <b>you are on</b>.", "Los carteles de <b>confirmación</b> tienen <b>siempre</b> el color de la vía <b>por la que se circula</b>."),
        ("<b>Pre-signposting</b> signs are the only ones that <b>change colour</b>: the colour of the road the exit <b>leads to</b>, <b>except</b> when it leads to a road of <b>lower category</b>. "
         "Withholding that information avoids drivers slowing down before the deceleration lane.",
         "Los de <b>preseñalización</b> son los únicos en los que <b>cambia el color</b>: el de la vía <b>hacia la que se dirige</b> la salida, <b>salvo</b> que sea hacia una carretera de <b>inferior categoría</b>. "
         "Esta falta de información evita reducciones de velocidad antes del carril de deceleración."),
        ("<b>Immediate exit</b> signs <b>always</b> have the colour of the road the exit <b>leads to</b>.", "Los carteles de <b>salida inmediata</b> tienen <b>siempre</b> el color de la vía <b>hacia la que se dirige</b> la salida."),
    ]))
    B.append(H3("Pre-signposting signs", "Señales de preseñalización"))
    B.append(P("Placed at a suitable distance before the junction and well in view, so they work as well as possible.", "Se colocan a una distancia adecuada de la intersección y visibles para que su eficacia sea máxima."))
    B.append(TXSIGNS([
        TX("S-200", "Roundabout ahead", "Preseñalización de glorieta", "The exits of the next roundabout; a destination on <b>blue</b> leads to a motorway or autovía.", "Direcciones de las salidas de la próxima glorieta; una inscripción sobre <b>azul</b> lleva a autopista o autovía."),
        TX("S-201 / S-202", "Split roundabout (from the main / the secondary road)", "Glorieta partida desde la calzada principal / secundarias",
           "A junction that looks like a roundabout but where the <b>main road keeps going through</b> (S-201: you are on it; S-202: you are not).",
           "Intersección con planta de glorieta en la que la <b>calzada principal no pierde continuidad</b> (S-201: circulas por ella; S-202: no)."),
        TX("S-203", "Roundabout with lane selection", "Glorieta con selección de carriles", "The exits and <b>which lane</b> to use for each.", "Las salidas y el <b>carril</b> para cada una."),
        TX("S-220 · S-220a · S-222 · S-222a", "Side signs on a conventional or multi-lane road", "Con cartel lateral, en carretera convencional o multicarril",
           "Destinations of the next junction’s exits and their distance; white when they lead to conventional roads, <b>blue</b> when to a motorway/autovía; “a” versions add your own direction.",
           "Destinos de las salidas del próximo nudo y su distancia; blancas si llevan a convencional o multicarril, <b>azules</b> hacia autopista/autovía; las «a» añaden la dirección propia."),
        TX("S-225", "On a motorway or autovía, to any road", "En autopista o autovía hacia cualquier carretera", "Destinations of the next exit, its <b>distance</b>, <b>number</b> and letter.", "Destinos de la próxima salida, su <b>distancia</b>, <b>número</b> y letra."),
        TX("S-230 to S-235a", "Overhead signs (gantries)", "Con carteles sobre la calzada", "The same information over the carriageway, on conventional roads (S-230, S-232) or motorways (S-235); “a” adds your own direction.", "La misma información sobre la calzada, en convencional (S-230, S-232) o autopista (S-235); las «a» añaden la dirección propia."),
        TX("S-242 · S-242a", "Two exits very close together", "Dos salidas muy próximas", "Destinations, distance and numbers of <b>two consecutive exits</b>.", "Destinos, distancia y números de <b>dos salidas consecutivas</b>."),
        TX("S-245 · S-246", "Extra towns (road / motorway)", "Preseñalización complementaria de poblaciones", "Nearby towns of <b>more than 5,000 inhabitants</b> reached through the next junction, and its distance.", "Poblaciones cercanas de <b>más de 5.000 habitantes</b> accesibles por el siguiente nudo y su distancia."),
        TX("S-247", "Exits on a town bypass", "Salidas en variante de población", "The town’s exits with the name of the road into town or the <b>compass point</b> (north, centre, south).", "Salidas de la variante con el nombre de la vía de penetración o el <b>punto cardinal</b>."),
        TX("S-250", "Route to follow", "Preseñalización de itinerario", "The route you must follow to go the way the arrow shows.", "Itinerario preciso para tomar la dirección de la flecha."),
        TX("S-260", "Lane pre-signposting", "Preseñalización de carriles", "The <b>only directions</b> allowed from each lane at the next junction; used only in exceptional cases.", "Las <b>únicas direcciones</b> permitidas desde cada carril en el próximo nudo; uso excepcional."),
        TX("S-261 · S-263 · S-267 · S-268 · S-271", "Services ahead", "Preseñalización de servicios y áreas de servicio",
           "An exit to services (fuel, charging, restaurant…), with distance and opening hours of the next service station; S-267/S-268 for estates, ports, leisure; S-271 for a <b>service area</b>.",
           "Salida hacia servicios, con distancia y horario de la siguiente estación de servicio o recarga; S-267/S-268 para urbanizaciones, puertos, ocio…; S-271 para un <b>área de servicio</b>."),
    ]))
    B.append(H3("Direction signs", "Señales de dirección"))
    B.append(TXSIGNS([
        TX("S-300 · S-301", "Towns on a route (road / motorway)", "Poblaciones de un itinerario", "Town names and the direction to reach them; the boxes give the road number and the figures the <b>distance in km</b>.", "Poblaciones y el sentido para alcanzarlas; los cajetines identifican la carretera y las cifras son <b>kilómetros</b>."),
        TX("S-320 · S-321 · S-322", "Places of interest; cycle routes", "Lugares de interés; vía ciclista o senda ciclopeatonal", "Places that are not towns (beach, port, airport), or a cycle route, with distance in km.", "Lugares que no son poblaciones (playa, puerto, aeropuerto) o una vía ciclista, con distancia en km."),
        TX("S-341 · S-342", "Immediate exit (to a road / to a motorway)", "Destino de salida inmediata", "Where you leave the motorway; the figure is the <b>junction number</b>, which matches the <b>kilometre point</b>.", "Lugar de salida de la autopista; la cifra es el <b>número del enlace</b>, que coincide con el <b>punto kilométrico</b>."),
        TX("S-344 · S-347", "Immediate exit to services", "Salida inmediata hacia servicios", "Exit to the services shown (maybe shared with a road exit).", "Salida hacia los servicios señalizados (puede coincidir con otra salida)."),
        TX("S-348 to S-353a", "Immediate exit signs (side or overhead)", "Señalización de salida inmediata (lateral o sobre la calzada)", "At the exit itself, on conventional roads or motorways; motorway ones give the <b>exit number</b>.", "En la propia salida, en convencional o autopista; las de autopista indican el <b>número de salida</b>."),
        TX("S-373 · S-375", "First of two very close exits", "Primera salida de dos muy próximas", "Your own direction, the second exit’s destinations and the first exit’s destinations.", "Dirección propia, destinos de la segunda salida y de la primera."),
        TX("S-376 to S-380", "Immediate exit to services or a service area", "Salida inmediata a servicios o área de servicio", "Exit to services, with opening hours; S-379/S-380 for a <b>service area</b>.", "Salida hacia servicios con su horario; S-379/S-380 para un <b>área de servicio</b>."),
    ]))
    B.append(H3("Road numbers, location and confirmation", "Identificación de carreteras, localización y confirmación"))
    B.append(SIGNS([
        SG("S-400", "European route", "Itinerario de la red internacional «E»", "A route of the <b>European “E” network</b> (green).", "Itinerario de la <b>red europea «E»</b> (verde)."),
        SG("S-410", "Motorway or autovía", "Autopista y autovía",
           "Blue “A”. Regional ones may add the region’s initials; <b>only motorways and autovías may use the letter A</b>; ring roads may use the city’s letters instead.",
           "«A» azul. Las autonómicas pueden añadir las siglas de la comunidad; <b>ninguna carretera que no sea autopista o autovía puede llevar la A</b>; las rondas pueden usar las letras de la ciudad."),
        SG("S-410a", "Toll motorway", "Autopista de peaje", "Blue “AP”.", "«AP» azul."),
        SG("S-420", "State conventional or multi-lane road", "Carretera convencional o multicarril de la red del Estado", "<b>Red</b>: a State road that is not a motorway.", "<b>Roja</b>: carretera del Estado que no es autopista o autovía."),
        SG("S-430", "First-level regional road", "Carretera de primer nivel de otra red", "<b>Orange</b>.", "<b>Naranja</b>."),
        SG("S-440", "Second-level regional road", "Carretera de segundo nivel de otra red", "<b>Brown</b>.", "<b>Marrón</b>."),
        SG("S-450", "Third-level regional road", "Carretera de tercer nivel de otra red", "<b>Yellow</b>.", "<b>Amarilla</b>."),
        SG("S-500", "Town entry", "Entrada a poblado",
           "The town’s name and the point where <b>town rules start</b>. The upper panel reminds you to adapt to <b>pedestrians, cyclists and other vulnerable users</b>, and may give that road’s speed limit (other streets may differ).",
           "Nombre de la población y lugar desde el que <b>rigen las normas de poblado</b>. El subcartel superior recuerda adaptar la conducción a <b>peatones, ciclistas y otros usuarios vulnerables</b> y puede incluir la velocidad máxima de esa vía (otras vías pueden tener límites distintos)."),
        SG("S-510", "End of town", "Fin de poblado", "Town rules <b>stop applying</b>.", "Dejan de aplicarse las <b>normas de poblado</b>."),
        SG("S-520", "Geographical point", "Localización de puntos geográficos", "A mountain pass, river or other feature the road crosses (brown). S-530 to S-533: tunnels, with safety equipment or specific rules inside.",
           "Puerto, río u otro punto que atraviesa la vía (marrón). S-530 a S-533: túneles, con sus instalaciones de seguridad u obligaciones específicas."),
        SG("S-540", "Province boundary", "Situación de límite de provincia", "You enter that province (green). <b>S-550</b>: autonomous community; <b>S-560</b>: both; <b>S-551</b>: river basin district.", "Entrada en la provincia (verde). <b>S-550</b>: comunidad autónoma; <b>S-560</b>: ambas; <b>S-551</b>: demarcación hidrográfica."),
        SG("S-570", "Kilometre post on a motorway or autovía", "Hito kilométrico en autopista o autovía", "The road and its kilometre point. <b>S-570a</b>: toll motorway; <b>S-571</b>: also a European route.", "Punto kilométrico de la vía identificada arriba. <b>S-570a</b>: de peaje; <b>S-571</b>: también itinerario europeo."),
        SG("S-572", "Kilometre post on a conventional road", "Hito kilométrico en carretera convencional", "Top part in the <b>colour of the road’s network</b>. <b>S-573</b>: on an international route.", "Parte superior del <b>color de la red</b> a la que pertenece. <b>S-573</b>: en itinerario internacional."),
        SG("S-574", "Ten-kilometre post", "Hito miriamétrico", "Tall post where the kilometre point is a <b>multiple of 10</b> (S-574 to S-575, in the colour of the road).", "Poste alto donde el punto kilométrico es <b>múltiplo de 10</b> (S-574 a S-575, del color de la carretera)."),
        SG("S-600", "Confirmation on a conventional road", "Confirmación de poblaciones en carretera convencional o multicarril", "The towns on the route and their <b>distances in km</b>, after a junction (white).", "Poblaciones del itinerario y sus <b>distancias en km</b> (blanca)."),
        SG("S-602", "Confirmation on a motorway or autovía", "Confirmación de poblaciones en autopista o autovía", "Same, in blue. <b>S-603</b>: adds distant provincial capitals and the next exit.", "Igual, en azul. <b>S-603</b>: añade capitales de provincia no adyacentes y la próxima salida."),
    ]))
    B.append(P("<b>Confirmation signs</b> remind you of the road’s direction and may give the distance in km after the place name.",
               "Las <b>señales de confirmación</b> recuerdan la dirección de la vía y pueden indicar la distancia en km tras el nombre de la localidad."))
    B.append(H3("Signs for use in towns", "Señales de uso específico en poblado"))
    B.append(P("Modules, used alone or together, that tell you a place is <b>reached by following the arrow</b>. The colour gives the kind of place.",
               "Módulos, usados juntos o por separado, que indican que el lugar se <b>alcanza siguiendo la flecha</b>. El color indica el tipo de lugar."))
    B.append(SIGNS([
        SG("S-700", "Urban road network", "Lugares de la red viaria urbana", "<b>Green</b>: streets, avenues, squares, roundabouts.", "<b>Verde</b>: calles, avenidas, plazas, glorietas."),
        SG("S-710", "Places of interest for travellers", "Lugares de interés para viajeros", "<b>Yellow</b>: stations, airports, ports, hotels, campsites, tourist offices.", "<b>Amarillo</b>: estaciones, aeropuertos, puertos, hoteles, campamentos, oficinas de turismo."),
        SG("S-720", "Sports or leisure", "Lugares de interés deportivo o recreativo", "<b>Orange</b>.", "<b>Naranja</b>."),
        SG("S-730", "Geographical, ecological, historic or artistic interest", "Lugares geográficos, ecológicos, monumentales, históricos o artísticos", "<b>Brown</b>: monuments, castles, museums, palaces.", "<b>Marrón</b>: monumentos, castillos, museos, palacios."),
        SG("S-740", "Cultural interest", "Lugares de interés monumental o cultural", "<b>White</b>: universities, libraries, theatres.", "<b>Blanco</b>: universidades, bibliotecas, teatros."),
        SG("S-750", "Industrial zones", "Zonas de uso industrial", "<b>White</b>: places that attract lorries and heavy traffic.", "<b>Blanco</b>: zonas que atraen camiones y tráfico pesado."),
        SG("S-760", "Motorways and autovías", "Autopistas y autovías", "<b>Blue</b>: motorways and the places reached by them.", "<b>Azul</b>: autopistas, autovías y lugares a los que llevan."),
        SG("S-770", "Other places and roads", "Otros lugares y vías", "<b>White</b> with a road box: other roads, towns and public places not in S-700 to S-760.", "<b>Blanco</b> con cajetín: otras carreteras, poblados y lugares no incluidos en S-700 a S-760."),
    ]))
    B.append(H3("7.5 Complementary panels", "7.5 Paneles complementarios"))
    B.append(P("They make the meaning of the sign above them <b>more precise</b>.", "Precisan el significado de la señal que <b>acompañan</b>."))
    B.append(SIGNS([
        SG("S-800", "Distance to the danger or rule", "Distancia al comienzo del peligro o prescripción", "Distance from the sign to where the danger or rule starts. Under <b>“road narrows”</b> it may give the <b>free width</b>.", "Distancia hasta donde empieza el peligro o la prescripción. Bajo <b>«estrechamiento de calzada»</b> puede indicar la <b>anchura libre</b>."),
        SG("S-810", "Length of the stretch", "Longitud del tramo peligroso o sujeto a prescripción", "How long the danger or the rule lasts.", "Longitud en que existe el peligro o se aplica la prescripción."),
        SG("S-820", "Extent of the prohibition, one side", "Extensión de la prohibición, a un lado", "Under a prohibition: the distance it applies <b>in the arrow’s direction</b> (S-820 right, S-821 left).", "Bajo una prohibición: distancia en que se aplica <b>en el sentido de la flecha</b> (S-820 derecha, S-821 izquierda)."),
        SG("S-830", "Extent of the prohibition, both sides", "Extensión de la prohibición, a ambos lados", "The distances in <b>each direction</b> shown.", "Distancias en <b>cada sentido</b> indicado."),
        SG("S-840", "STOP ahead", "Preseñalización de detención obligatoria", "Under a <b>give way</b> sign: the distance to the <b>STOP</b> at the next junction.", "Bajo un <b>«Ceda el paso»</b>: distancia a la señal de <b>STOP</b> de la próxima intersección."),
        SG("S-850", "Priority route", "Itinerario con prioridad", "Added to <b>R-3</b>: shows which route has priority (S-850 to S-853).", "Panel adicional de la <b>R-3</b> que indica el itinerario con prioridad (S-850 a S-853)."),
        SG("S-860", "Generic panel", "Genérico", "Any other clarification or limit of the sign or <b>traffic light</b> above it.", "Cualquier otra aclaración o delimitación de la señal o <b>semáforo</b> bajo el que está."),
        SG("S-870a", "Applies to the exit road", "Aplicación de la señalización", "Under a prohibition or obligation: it applies <b>only to the exit road</b> in the arrow’s direction (S-870a/b).", "Bajo una prohibición u obligación: se refiere <b>solo al ramal de salida</b> en la dirección de la flecha (S-870a/b)."),
        SG("S-880a", "Applies to lorries", "Aplicación de señalización a camiones",
           "The sign above applies <b>only to lorries</b>. Same for S-880b (vehicles with a trailer except single-axle), S-880c buses, S-880d cycles, S-880e VMP, S-880f cycles and VMP.",
           "La señal se refiere <b>solo a camiones</b>. Igual S-880b (con remolque salvo de un eje), S-880c autobuses, S-880d ciclos, S-880e VMP, S-880f ciclos y VMP."),
        SG("S-890a", "Applies in snow", "Aplicación a circunstancias de nieve", "The sign applies <b>only when there is snow</b>. S-890b: rain; S-890c: fog.", "La señal se aplica <b>solo con nieve</b>. S-890b: lluvia; S-890c: niebla."),
        SG("S-891", "Side gap when overtaking cycles or mopeds", "Distancia lateral en adelantamiento a ciclo o ciclomotor",
           "Reminds you of the <b>minimum 1.5 m</b> side gap when overtaking a cycle or moped (or a group; then measured from the one furthest left).",
           "Recuerda la anchura de seguridad <b>mínima de 1,5 m</b> al adelantar a un ciclo o ciclomotor (o a un grupo; entonces se mide desde el más escorado a la izquierda)."),
        SG("S-892", "Automatic enforcement", "Vigilancia por medios automáticos", "The sign above is enforced by <b>automatic cameras</b>.", "El cumplimiento de la señal se vigila con <b>medios automáticos</b>."),
    ], "Panel", "Panel"))
    B.append(H3("7.6 Other signs", "7.6 Otras señales"))
    B.append(SIGNS([
        SG("S-900", "Fire danger", "Peligro de incendio", "Warns of the danger of lighting a fire.", "Advierte del peligro de encender fuego."),
        SG("S-910", "Fire extinguisher", "Extintor", "Where a fire extinguisher is. <b>S-970</b>: emergency phone and extinguisher.", "Situación de un extintor. <b>S-970</b>: teléfono de emergencia y extintor."),
        SG("S-920", "Entering Spain", "Entrada a España", "You have entered Spain from another country.", "Se ha entrado en España desde otro país."),
        SG("S-930", "Country ahead", "Confirmación del país", "The country the road leads to; the figure is the distance to the <b>border</b>.", "País hacia el que se dirige la carretera; la cifra es la distancia a la <b>frontera</b>."),
        SG("S-940", "Speed limits in Spain", "Limitaciones de velocidad en España", "The general limits by type of road and in town.", "Límites genéricos según el tipo de vía y en poblado."),
        SG("S-950", "Traffic radio frequency", "Radiofrecuencia de emisoras de información sobre carreteras", "The station with road information.", "Emisora con información de carreteras."),
        SG("S-960", "Emergency telephone", "Teléfono de emergencia", "Where an emergency phone is.", "Situación de un teléfono de emergencia."),
        SG("S-980", "Emergency exit", "Salidas de emergencia", "An emergency exit. <b>S-980a/b</b>: the nearest one, to the right or left.", "Salida de emergencia. <b>S-980a/b</b>: la más cercana, a derecha o izquierda."),
        SG("S-990a", "Emergency exit ahead", "Salida de emergencia próxima", "Direction and <b>distance</b> to the nearest emergency exit (S-990a/b).", "Dirección y <b>distancia</b> a la salida de emergencia más cercana (S-990a/b)."),
        SG("S-991a", "Speed camera (conventional road)", "Control de velocidad en carretera convencional o multicarril", "A <b>speed camera</b> at a point or along a stretch; may include the speed limit. <b>S-991b</b>: on a motorway (blue).", "<b>Control de velocidad</b> en un punto o tramo; puede incluir la velocidad máxima. <b>S-991b</b>: en autopista o autovía (azul)."),
        SG("S-991c", "Red-light camera", "Control de semáforo en rojo", "A camera checks that vehicles <b>stop at the red light</b>. <b>S-991d</b>: at a STOP.", "Control de paso con <b>semáforo en rojo</b>. <b>S-991d</b>: control de STOP."),
        SG("S-991e", "Following-distance camera", "Control de separación mínima", "A camera checks the <b>minimum gap</b> between vehicles. <b>S-991f</b>: on a motorway.", "Control de la <b>separación mínima</b> entre vehículos. <b>S-991f</b>: en autopista o autovía."),
        SG("S-991g", "Speed checks from the air", "Control de velocidad mediante medios aéreos", "Speed may be checked by <b>helicopter or drone</b> (yellow).", "Posibles controles de velocidad desde <b>helicóptero o dron</b> (amarilla)."),
        SG("S-992a", "Minimum gap between vehicles (chevrons)", "Distancia mínima entre vehículos",
           "Where rear-end crashes are frequent: how many <b>chevron marks</b> to leave between you and the vehicle ahead. S-992b/d in tunnels; S-992c on motorways.",
           "Donde son frecuentes los alcances: número de <b>galones</b> que hay que dejar con el precedente. S-992b/d en túneles; S-992c en autopista o autovía."),
        SG("S-992e", "Minimum gap in fog (beacon lights)", "Distancia mínima indicada mediante balizas luminosas", "Where fog often cuts visibility: how many <b>beacon lights</b> to leave between you and the vehicle ahead.", "Donde la niebla es frecuente: número de <b>balizas luminosas</b> que hay que dejar con el precedente."),
        SG("S-993", "Rear-end risk uphill", "Advertencia de riesgo de alcances en pendiente ascendente", "On an uphill motorway stretch <b>lorries go much slower</b> than cars: risk of rear-end crashes.", "En una subida de autopista o autovía los <b>camiones van mucho más lentos</b> que los turismos: riesgo de alcances."),
    ]))
    return B


# ================================================================== 8 road markings
def _markings():
    B = []
    B.append(H2("8", "Road markings", "Marcas viales"))
    B.append(P(
        "Road markings <b>regulate traffic and warn or guide</b> road users: they mark out lanes, directions, areas closed to traffic, reserved areas and parking. They can be used <b>alone or with other signs</b> to reinforce or clarify them. "
        "They are <b>white</b>, <b>yellow</b>, <b>blue</b> or <b>white and red</b>.",
        "Las marcas viales tienen la finalidad de <b>regular la circulación y advertir o guiar</b> a los usuarios: delimitan carriles, sentidos, zonas excluidas al tráfico, reservadas o de estacionamiento. Pueden emplearse <b>solas o con otros medios de señalización</b> para reforzarlos o precisarlos. "
        "Pueden ser <b>blancas</b>, <b>amarillas</b>, <b>azules</b> o <b>blancas y rojas</b>."))
    B.append(H3("8.1 White lines along the road", "8.1 Marcas blancas longitudinales"))
    B.append(SIGNS([
        SG("mk-cont", "Continuous line (one or two lines)", "Marca longitudinal continua",
           "<b>No one may cross it or drive on it</b>, and where it separates the two directions, <b>nor drive to its left</b>. Two continuous lines side by side mean the same.",
           "<b>Ningún conductor debe atravesarla ni circular sobre ella</b> ni, si separa los dos sentidos, <b>circular por su izquierda</b>. Dos líneas continuas adosadas tienen el mismo significado."),
        SG("mk-wide", "Wider continuous line", "Continua sensiblemente más ancha",
           "Marks a <b>special lane</b> (bus…). Only those <b>driving in that lane</b> may cross it, to leave it when their manoeuvre or destination requires, with care.",
           "Indica un <b>carril especial</b>. Solo pueden atravesarla <b>los que circulen por él</b>, para abandonarlo cuando lo exija la maniobra o el destino, con precaución."),
        SG("mk-dash", "Broken line", "Marca longitudinal discontinua",
           "Separates lanes to <b>guide traffic</b>. Do <b>not drive on it</b> unless the lanes are narrow and it is safe.",
           "Delimita carriles para <b>guiar la circulación</b>. <b>No se debe circular sobre ella</b>, salvo que la estrechez de los carriles lo haga necesario y la seguridad lo permita."),
        SG("mk-dash-short", "Broken line with shorter gaps", "Discontinua con menor separación entre trazos",
           "Warns that a <b>continuous line</b> or a stretch of <b>special risk</b> is coming. Broken lines can also announce <b>forks or merges</b>.",
           "Anuncia que se aproxima una <b>línea continua</b> o un tramo de <b>riesgo especial</b>. La discontinua también puede preavisar <b>bifurcaciones o confluencias</b>."),
        SG("mk-dash-wide", "Wider broken line", "Discontinua sensiblemente más ancha", "Marks a <b>special lane</b> (for some vehicles, an entry or exit lane…).", "Indica un <b>carril especial</b> (para determinados vehículos, de entrada o salida…)."),
        SG("mk-cont-dash", "Continuous line beside a broken line", "Continua adosada a discontinua",
           "Each driver only heeds the line <b>on their own side</b>. Between directions, it does not stop drivers who have <b>finished overtaking from returning</b> to their side; "
           "between lanes in the same direction, it <b>stops them going back</b> to the lane they left.",
           "Cada conductor solo tiene en cuenta la línea <b>de su lado</b>. Si separa sentidos, no impide a quien ha <b>adelantado volver</b> a su lugar; "
           "si no separa sentidos, <b>impide volver</b> al carril por el que circulaba."),
        SG("mk-reversible", "Double broken lines on both sides", "Marcas discontinuas dobles", "A <b>reversible lane</b>: its direction is set by lane lights or other means.", "<b>Carril reversible</b>: su sentido se regula con semáforos de carril u otros medios."),
        SG("mk-guide", "Guide lines in a junction", "Marcas de guía en la intersección", "Show <b>how to make certain manoeuvres</b> in a junction.", "Indican <b>cómo realizar determinadas maniobras</b> en una intersección."),
    ], "Marking", "Marca"))
    B.append(BOX("trap", "Not counted as white lines along the road", "No se consideran marcas longitudinales", [
        ("Lines that mark the <b>edges of the carriageway</b> or <b>parking places</b> are not longitudinal white markings for these rules.",
         "Las líneas que delimitan los <b>bordes de la calzada</b> o los <b>lugares de estacionamiento</b> no se consideran marcas blancas longitudinales a estos efectos."),
    ]))
    B.append(H3("8.2 White lines across the road", "8.2 Marcas blancas transversales"))
    B.append(SIGNS([
        SG("mk-stop", "Continuous line across (stop line)", "Marca transversal continua (línea de detención)",
           "No vehicle, animal or load may <b>cross it</b> when it must stop because of: a <b>STOP</b> sign (painted or upright), <b>“no passing without stopping”</b>, a <b>pedestrian crossing</b>, a <b>traffic light</b>, an <b>agent’s stop signal</b>, a <b>level crossing or movable bridge</b>. "
           "If in exceptional cases you <b>cannot see</b> from it, <b>move forward and stop again</b> where you can see, without endangering anyone.",
           "Ningún vehículo, animal ni su carga <b>debe franquearla</b> cuando deba detenerse por: señal de <b>detención obligatoria</b> (horizontal o vertical), <b>prohibición de pasar sin detenerse</b>, <b>paso para peatones</b>, <b>semáforo</b>, <b>detención ordenada por un agente</b>, <b>paso a nivel o puente móvil</b>. "
           "Si por circunstancias excepcionales <b>no hay visibilidad</b>, se debe <b>avanzar y detenerse de nuevo</b> donde la haya, sin poner en peligro a nadie."),
        SG("mk-yield", "Broken line across (give-way line)", "Marca transversal discontinua (línea de ceda el paso)",
           "Unless abnormal conditions reduce visibility, do not cross it <b>when you have to give way</b> because of: a <b>give way</b> sign (upright or painted), a light with a <b>green turning arrow</b>, or the <b>priority rules</b> where there are no signs. "
           "If you cannot see from it, you <b>may move forward until you can</b>, without having to stop at it.",
           "Salvo circunstancias que reduzcan la visibilidad, no se debe franquear <b>cuando haya que ceder el paso</b> por: señal de <b>ceda el paso</b> (vertical u horizontal), semáforo con <b>flecha verde de giro</b> o las <b>normas de prioridad</b> en ausencia de señales. "
           "Si no hay visibilidad desde ella, se <b>puede avanzar hasta conseguirla</b>, sin necesidad de detenerse ante ella."),
        SG("mk-zebra", "Pedestrian crossing (zebra)", "Marca de paso para peatones",
           "<b>Wide bands parallel to the road’s axis</b>, forming a set across it; <b>no other colours</b> may alternate with the white. Drivers must <b>give way to pedestrians</b>. It may be the usual one, an alternative one at traffic lights, or <b>raised</b>.",
           "<b>Líneas de gran anchura paralelas al eje de la calzada</b>, formando un conjunto transversal; <b>no pueden alternarse otros colores</b> con el blanco. Los conductores deben <b>ceder el paso a los peatones</b>. Puede ser la habitual, la alternativa con semáforo o <b>sobreelevado</b>."),
        SG("mk-cycle", "Cycle crossing", "Marca de paso para ciclistas",
           "<b>Two parallel broken lines</b> across the road. <b>Cyclists have priority</b>: give way to them. The surface may be painted, preferably <b>red</b>, and it may run beside a pedestrian crossing.",
           "<b>Dos líneas transversales discontinuas y paralelas</b>. <b>Los ciclistas tienen preferencia</b>: hay que cederles el paso. El pavimento puede pintarse, preferiblemente de <b>rojo</b>, y puede ir junto a un paso para peatones."),
        SG("mk-hump", "Speed-hump marking (“lomo de asno”)", "Marca de reductor de velocidad (lomo de asno)",
           "<b>Three triangles</b> on the rising side of a physical <b>hump</b>: you <b>must slow down</b>, mainly to protect pedestrians and cyclists. Used near crossings, roundabout entrances, schools, hospitals…",
           "<b>Tres triángulos</b> en la parte ascendente de un <b>resalto físico</b>: <b>obliga a reducir la velocidad</b>, sobre todo por peatones y ciclistas. Se usa antes de pasos para peatones, accesos a glorietas, colegios, hospitales…"),
    ], "Marking", "Marca"))
    B.append(H3("8.3 Signs painted on the road", "8.3 Señales horizontales de circulación"))
    B.append(P("When painted <b>in a lane bounded by longitudinal lines</b>, they apply <b>only to vehicles in that lane</b>.",
               "Cuando están <b>en un carril delimitado por líneas longitudinales</b>, afectan <b>exclusivamente a los vehículos que circulan por dicho carril</b>."))
    B.append(SIGNS([
        SG("mk-yield-tri", "Give way (painted triangle)", "Ceda el paso", "A triangle with its <b>point towards you</b>: <b>give way</b> at the next junction.", "Triángulo con un <b>vértice hacia el vehículo</b> que se acerca: <b>ceder el paso</b> en la próxima intersección."),
        SG("mk-stop-word", "STOP (painted)", "Detención obligatoria o STOP", "<b>Stop at the next stop line</b> or, if none, right before the road you are joining, and give way.", "<b>Detenerse ante la próxima línea de detención</b> o, si no existe, inmediatamente antes de la calzada, y ceder el paso."),
        SG("mk-speed", "Speed limit (painted)", "Señal de limitación de velocidad", "Do not exceed that speed (km/h) until an “end of speed limit”, “end of prohibitions” or a different speed limit sign.", "No sobrepasar esa velocidad (km/h) hasta «Fin de limitación», «Fin de prohibiciones» u otra de velocidad máxima distinta."),
        SG("mk-reserved", "Reserved or priority area", "Zona reservada o con prioridad para determinados usuarios", "Lanes or areas reserved for, or giving priority to, certain users (reduced mobility, pedestrians, cycles, VMP, electric vehicles…); pictograms may show what a parking space is for (pharmacy, health centre…).",
           "Carriles o zonas reservadas o con prioridad para determinados usuarios (movilidad reducida, peatones, ciclos, VMP, eléctricos…); pictogramas pueden indicar la función de una plaza (farmacia, centro de salud…)."),
        SG("mk-lane-arrows", "Lane-selection arrows", "Flecha de selección de carriles", "Follow the <b>arrow’s direction</b> or, if markings allow, <b>change lane</b>. It may carry a destination.", "Hay que <b>seguir la dirección</b> o, si la señalización lo permite, <b>cambiarse de carril</b>. Puede llevar inscripción de destino."),
        SG("mk-exit", "Exit arrow", "Flecha de salida", "Where you may <b>start changing lane</b> to take an exit, and its direction.", "Dónde se puede <b>iniciar el cambio de carril</b> para tomar una salida y su dirección."),
        SG("mk-endlane", "End-of-lane arrow", "Flecha de fin de carril", "Your lane <b>ends soon</b>: follow the arrow.", "El carril <b>termina próximamente</b>: hay que seguir su indicación."),
        SG("mk-return", "Return arrow", "Flecha de retorno",
           "Near the centre of a two-way road, pointing <b>right</b>: a <b>continuous line</b> is coming, so <b>move back to the right lane as soon as possible</b>.",
           "En el eje de una calzada de doble sentido, apuntando a la <b>derecha</b>: se aproxima una <b>línea continua</b>; hay que pasar <b>cuanto antes al carril al que apunta</b>."),
        SG("mk-rbt-arrows", "Roundabout lane arrows", "Flecha en acceso a glorieta con selección de carriles", "<b>Before entering</b>, which exits you can take from your lane.", "<b>Antes de entrar</b>, qué salidas se pueden tomar desde ese carril."),
        SG("mk-minirbt", "Mini-roundabout arrows", "Flecha en minirrotondas", "A small roundabout and the way round it; the central island is <b>4 m or less</b> across.", "Glorieta pequeña y su sentido de circulación; isleta central de <b>4 m o menos</b> de diámetro."),
    ], "Marking", "Marca"))
    B.append(H3("8.4 Other white markings", "8.4 Otras marcas e inscripciones blancas"))
    B.append(SIGNS([
        SG("mk-bifurcation", "Fork marking", "Marca de bifurcación", "A <b>fork</b> is coming, perhaps with a change in the number of lanes.", "Se aproxima una <b>bifurcación</b>, con posible reajuste del número de carriles."),
        SG("mk-pn", "Level-crossing marking", "Marca de paso a nivel", "The letters <b>“P” and “N”</b> either side of a cross: a <b>level crossing</b> is near.", "Las letras <b>«P» y «N»</b> a cada lado de un aspa: proximidad de un <b>paso a nivel</b>."),
        SG("mk-bus", "Reserved lane or area lettering", "Inscripción de carril o zona reservada", "A lane or area <b>reserved</b>, temporarily or permanently, for driving, stopping or parking certain vehicles (bus, taxi, cycles).", "Carril o zona <b>reservados</b>, temporal o permanentemente, para la circulación, parada o estacionamiento de determinados vehículos (bus, taxi, ciclos)."),
        SG("mk-res-start", "Start of a reserved lane", "Comienzo de carril reservado", "Where a reserved lane begins; the markings stop other vehicles entering.", "Comienzo de un carril reservado; las marcas prohíben la entrada al resto."),
        SG("mk-cycleway", "Cycle-route marking", "Marca de vía ciclista", "A cycle route or cycle path.", "Vía ciclista o senda ciclable."),
        SG("mk-park-line", "Parking bays", "Líneas y marcas de estacionamiento", "Mark out parking areas and how to use them: <b>in line</b>, <b>in battery</b> (side by side) or <b>diagonal</b>.", "Delimitan el estacionamiento y su forma: <b>en línea o cordón</b>, <b>en batería</b> u <b>oblicuo</b>.", "mk-park-battery"),
        SG("mk-hatch", "Hatched area (cebreado)", "Cebreado", "Oblique stripes framed by a continuous line: <b>no one may enter</b> it, <b>except those who must use the shoulder</b>.", "Franjas oblicuas enmarcadas por una línea continua: <b>ningún conductor debe entrar</b>, <b>excepto los obligados a circular por el arcén</b>."),
        SG("mk-edge", "Edge line", "Línea de borde de calzada", "Makes the edges more visible; <b>continuous or broken makes no difference</b>.", "Hace más visibles los bordes; <b>es indiferente si es continua o discontinua</b>."),
        SG("mk-orient", "Destination lettering", "Marcas de orientación", "The place (road, town, car park, airport, toll…) you reach by staying in that lane.", "Lugar (carretera, población, aparcamiento, aeropuerto, peaje…) al que se llega siguiendo ese carril."),
        SG("mk-chevrons", "Distance chevrons (galones)", "Marca de separación de seguridad entre vehículos (galones)",
           "Arrow-shaped marks in the middle of the lane to judge the <b>minimum gap</b>: keep at least <b>two chevrons</b> on any road. Used in tunnels and stretches with many rear-end crashes; the <b>R-300</b> sign stands at the start.",
           "Marcas en forma de ángulo en el centro del carril para la <b>separación mínima</b>: al menos <b>dos galones</b> en cualquier vía. En túneles y tramos con muchos alcances; al inicio debe haber una señal <b>R-300</b>."),
        SG("mk-avanza", "Advanced stop box (avanza-motos / avanza-bici)", "Avanza-motos o avanza-bici",
           "Space between <b>two continuous lines 4 m apart</b> before some junctions or crossings with lights. <b>On red</b>, only the vehicles shown may wait there (cycles, VMP, motorcycles or mopeds).",
           "Espacio entre <b>dos marcas transversales continuas separadas 4 metros</b>, antes de intersecciones o pasos con semáforo. <b>Con el semáforo en rojo</b> solo pueden ocuparlo los vehículos de los pictogramas (ciclos, VMP, motos o ciclomotores)."),
    ], "Marking", "Marca"))
    B.append(H3("8.4.1 Markings that calm traffic", "8.4.1 Marcas para aumentar la seguridad o calmar el tráfico"))
    B.append(P("They tell you that you are on a special stretch and must <b>adapt your driving and take extreme care</b>, because of <b>vulnerable users</b> or other factors.",
               "Indican que se circula por un tramo con características especiales y hay que <b>adaptar la conducción extremando la precaución</b> por la presencia de <b>usuarios vulnerables</b> u otros factores."))
    B.append(SIGNS([
        SG("mk-dragon", "Dragon’s teeth", "Dientes de dragón", "<b>Slow down noticeably</b>: you are reaching a <b>travesía or urban road</b>; expect vulnerable users.", "<b>Reducir sensiblemente la velocidad</b> por la aproximación a una <b>travesía o vía urbana</b>; posibles usuarios vulnerables."),
        SG("mk-broken-edge", "Zig-zag edge lines", "Líneas de borde quebradas", "Slow down and pay attention: a <b>pedestrian or cycle crossing</b> is coming.", "Disminuir la velocidad y aumentar la atención por un <b>paso para peatones o ciclistas</b>."),
        SG("mk-damero", "Chequerboard", "Damero para la reducción de velocidad", "Slow down: the risk ahead is <b>greater than it looks</b> (roundabout, toll plaza…); often with bumps or rumble effects.", "Reducir la velocidad: tramo con un riesgo <b>superior al percibido</b> (glorieta, peaje…); suele ir con resaltes o efectos acústicos."),
        SG("mk-moto-guide", "Motorcyclist guidance marks", "Marcas de guiado para motoristas", "Warn motorcyclists and cyclists of a <b>risky bend</b> and the part of the lane better <b>not to ride on</b>.", "Indican a motoristas y ciclistas una <b>curva de especial riesgo</b> y la zona del carril que conviene <b>evitar pisar</b>."),
        SG("mk-zbe", "Low-emission zone (ZBE) marking", "Marcas de zona de bajas emisiones", "Start or edge of a <b>low-emission zone</b>: only vehicles meeting its environmental rules may enter.", "Inicio o límite de una <b>zona de bajas emisiones</b>: solo acceden los vehículos que cumplan sus requisitos ambientales."),
    ], "Marking", "Marca"))
    B.append(P("<b>Trial stretches</b>: other markings may be used on test stretches announced by vertical signs and approved by the responsible engineer’s report.",
               "<b>Tramos de ensayo</b>: puede haber otras marcas en tramos de ensayo advertidos con señalización vertical y aprobados por informe del técnico responsable."))
    B.append(H3("8.5 Markings of other colours", "8.5 Marcas de otros colores"))
    B.append(SIGNS([
        SG("mk-y-zigzag", "Yellow zig-zag *", "Marca amarilla en zigzag *", "<b>No parking</b>: the place is kept for a special use that does not mean staying long (bus stops, loading and unloading).", "<b>Prohibido estacionar</b>: lugar reservado para un uso especial sin larga permanencia (paradas de autobús, carga y descarga)."),
        SG("mk-y-cont", "Continuous yellow line on the kerb *", "Marca amarilla longitudinal continua *", "On that side, along the whole line, <b>stopping and parking are forbidden</b> (or restricted as signs say).", "En ese lado y en toda su longitud, <b>parada y estacionamiento prohibidos</b> (o restringidos según las señales)."),
        SG("mk-y-dash", "Broken yellow line on the kerb *", "Marca amarilla longitudinal discontinua *", "On that side, along the whole line, <b>parking is forbidden</b> (or restricted); stopping is allowed.", "En ese lado y en toda su longitud, <b>estacionamiento prohibido</b> (o restringido); la parada sí."),
        SG("mk-y-grid", "Yellow box (criss-cross)", "Cuadrícula de marcas amarillas", "Do <b>not enter the junction</b> if you are likely to be <b>left stopped</b> there, blocking cross traffic.", "Recuerda la <b>prohibición de entrar en la intersección</b> si previsiblemente se puede <b>quedar detenido</b> obstruyendo la circulación transversal."),
        SG("mk-redwhite", "Red and white chequerboard", "Damero blanco y rojo", "Start of an <b>emergency escape lane</b>: no stopping, parking or any other use.", "Comienzo de una <b>zona de frenado de emergencia</b>: prohibida la parada, el estacionamiento y cualquier otro uso."),
        SG("mk-blue", "Blue parking lines", "Marcas azules", "Parking is allowed but, at certain times, its <b>length is limited</b> (regulated parking).", "Estacionamiento permitido, pero en ciertos periodos su <b>duración está limitada</b>."),
    ], "Marking", "Marca"))
    B.append(BOX("key", "* Yellow markings and time limits", "* Marcas amarillas y prohibición temporal", [
        ("The yellow zig-zag and the continuous and broken yellow lines can mean a <b>temporary</b> prohibition if an upright sign at the start of the stretch says so.",
         "La marca amarilla en zigzag y las longitudinales continua y discontinua pueden indicar una prohibición <b>temporal</b> si una señal vertical al principio del tramo lo especifica."),
    ]))
    return B


# ================================================================== 9–10 traps and numbers
def _closing():
    B = []
    B.append(H2("9", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("Order: <b>agent</b> → temporary signs → <b>light</b> → upright sign → <b>marking</b>. Same group: the <b>most restrictive</b>. Sign vs rule: <b>the sign</b>.",
         "Orden: <b>agente</b> → circunstancial → <b>semáforo</b> → vertical → <b>marca</b>. Mismo grupo: la <b>más restrictiva</b>. Señal frente a norma: <b>la señal</b>."),
        ("A sign on the <b>left</b> binds only those going <b>straight on or left</b>; on the right, everyone.", "La señal de la <b>izquierda</b> solo obliga a los que van <b>de frente o a la izquierda</b>; la de la derecha, a todos."),
        ("Agent’s arm raised: everyone stops, but drivers <b>already inside the junction</b> carry on.", "Brazo levantado: todos se detienen, pero los que <b>ya están dentro de la intersección</b> siguen."),
        ("Arm up and down: <b>slow down</b>, not stop. Whistle: short blasts stop, <b>one long blast</b> = go.", "Brazo arriba y abajo: <b>reducir</b>, no parar. Silbato: toques cortos paran; <b>uno largo</b> = reanudar."),
        ("Yellow flag: <b>extreme care</b>. Red flag: road closed. Green flag: road open again.", "Bandera amarilla: <b>extremar la atención</b>. Roja: calzada cerrada. Verde: de nuevo abierta."),
        ("Amber flashing: <b>take care and give way if needed</b> — it does not let you ignore a STOP. Flashing white bar for buses: stop as for <b>steady amber</b>.",
         "Ámbar intermitente: <b>precaución y ceder si procede</b>, no anula un STOP. Franja blanca intermitente: detenerse como ante <b>ámbar fijo</b>."),
        ("Green arrow: you go <b>with care</b>, giving way to the lane you join and to pedestrians. Black arrow on red: the red <b>only for that move</b>.",
         "Flecha verde: se pasa <b>con precaución</b>, cediendo al carril al que te incorporas y a peatones. Flecha negra sobre roja: la roja <b>solo para ese movimiento</b>."),
        ("R-303 (no left turn) also bans <b>U-turns</b>; R-304 (no U-turn) <b>still lets you turn left</b>.", "R-303 (giro izquierda prohibido) prohíbe también el <b>cambio de sentido</b>; R-304 (media vuelta) <b>sí permite girar</b>."),
        ("R-308 and blue lines: <b>stopping is allowed</b>. R-307 and continuous yellow kerb line: <b>no stopping either</b>.", "R-308 y marcas azules: <b>la parada sí</b>. R-307 y amarilla continua: <b>tampoco parar</b>."),
        ("R-103 lets <b>two-wheeled motorcycles</b> in; R-102 does not. R-105 also bans vehicles for <b>reduced mobility</b>.", "La R-103 deja pasar a las <b>motos de dos ruedas</b>; la R-102 no. La R-105 prohíbe también vehículos para <b>movilidad reducida</b>."),
        ("S-7 (blue square) is <b>advice</b>; R-301 (red ring) is the <b>limit</b>. P-29 does <b>not</b> say which side the wind blows from.",
         "S-7 (cuadrado azul) es una <b>recomendación</b>; R-301 (borde rojo) es el <b>límite</b>. La P-29 <b>no</b> indica el lado del viento."),
        ("S-28 play zone: <b>10 km/h</b>, games allowed. S-47 coexistence zone: <b>20 km/h</b>, games <b>not</b> allowed.", "S-28 estancia y juego: <b>10 km/h</b>, juegos permitidos. S-47 coexistencia: <b>20 km/h</b>, juegos <b>no</b>."),
        ("Continuous + broken line: obey <b>only the one on your side</b>. Hatched area: <b>only those who must use the shoulder</b> may enter.",
         "Continua adosada a discontinua: se atiende <b>solo a la de tu lado</b>. Cebreado: solo entran <b>los obligados a usar el arcén</b>."),
        ("Give-way line: you may <b>edge forward to see</b> without stopping; stop line: stop, then <b>stop again</b> where you can see.",
         "Línea de ceda: se puede <b>avanzar hasta ver</b> sin detenerse; línea de detención: parar y <b>volver a parar</b> donde haya visibilidad."),
        ("Edge posts and cat’s eyes: <b>white on the left</b>, white or yellow on the right.", "Hitos de arista y captafaros: <b>blancos a la izquierda</b>; blancos o amarillos a la derecha."),
        ("Pre-signposting to a <b>lower-category</b> road keeps the colour of the road you are on; the immediate exit sign changes.",
         "La preseñalización hacia una vía de <b>inferior categoría</b> mantiene el color de la vía actual; el cartel de salida inmediata sí cambia."),
    ]))
    B.append(H2("10", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Visibility of people helping agents", "Visibilidad de los auxiliares de los agentes"), T("at least 150 m", "mínimo 150 m")],
            [T("Variable message sign", "Panel de mensaje variable"), T("at most 2 alternating messages", "como máximo 2 mensajes alternados")],
            [T("Permanent direction panels", "Paneles direccionales permanentes"), T("single = moderate, double = medium, triple = high danger", "sencillo = moderada, doble = media, triple = elevada")],
            [T("Approach posts P-9/P-10", "Balizas P-9/P-10"), T("3 stripes 200 m · 2 stripes 150 m · 1 stripe 100 m", "3 franjas 200 m · 2 franjas 150 m · 1 franja 100 m")],
            [T("Exit countdown panels S-26", "Paneles de aproximación a salida S-26"), T("300, 200 and 100 m", "300, 200 y 100 m")],
            [T("No overtaking for lorries (R-306)", "Adelantamiento prohibido para camiones (R-306)"), T("MMA over 3,500 kg", "MMA superior a 3.500 kg")],
            [T("Water pollutants (R-110, R-415)", "Contaminantes del agua (R-110, R-415)"), T("more than 1,000 litres", "más de 1.000 litros")],
            [T("Parking by fortnights (R-308c / R-308d)", "Estacionamiento por quincenas (R-308c / R-308d)"), T("9:00 day 1 → 9:00 day 16 / 9:00 day 16 → 9:00 day 1", "9 h día 1 → 9 h día 16 / 9 h día 16 → 9 h día 1")],
            [T("Residential play zone S-28 / coexistence zone S-47", "Zona de estancia y juego S-28 / de coexistencia S-47"), T("10 km/h / 20 km/h", "10 km/h / 20 km/h")],
            [T("Side gap overtaking cycles or mopeds (S-891)", "Separación lateral al adelantar a ciclos o ciclomotores (S-891)"), T("1.5 m", "1,5 m")],
            [T("Advanced stop box (avanza-motos)", "Avanza-motos o avanza-bici"), T("two lines 4 m apart", "dos líneas separadas 4 m")],
            [T("Mini-roundabout central island", "Isleta central de una minirrotonda"), T("4 m across or less", "4 m o menos de diámetro")],
            [T("Distance chevrons", "Galones"), T("keep at least 2", "al menos 2")],
            [T("Extra towns on pre-signposting (S-245/S-246)", "Poblaciones en preseñalización complementaria (S-245/S-246)"), T("more than 5,000 inhabitants", "más de 5.000 habitantes")],
            [T("Ten-kilometre posts (hitos miriamétricos)", "Hitos miriamétricos"), T("every multiple of 10 km", "cada múltiplo de 10 km")],
        ],
        widths=["56%", "44%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["or1", "pl2", "ag1", "ag5", "ha3", "tl4", "tl8", "wn5", "pr3", "ot4", "zn2", "mk6"]


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
    ("Reglamento General de Circulación (RD 1428/2003), Título IV (signs, arts. 132–173) and Anexo I — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Real Decreto 465/2025, de 10 de junio: new official catalogue of signs and road markings (BOE 17-06-2025, in force 1 July 2025)", "https://www.boe.es/buscar/doc.php?id=BOE-A-2025-12199"),
    ("DGT press release, 10-06-2025: the Government approves the updated official catalogue of traffic signs",
     "https://www.dgt.es/comunicacion/notas-de-prensa/20250610-el-gobierno-aprueba-la-actualizacion-del-catalogo-oficial-de-senales-de-trafico/"),
    ("Real Decreto 518/2026 (reform of the Reglamento for vulnerable road users, in force 1 October 2026)", "https://www.boe.es/buscar/doc.php?id=BOE-A-2026-13889"),
    ("DGT press release, 30-09-2026: reform of the Reglamento for vulnerable road users",
     "https://www.dgt.es/comunicacion/notas-de-prensa/20260930-reforma-del-reglamento-de-circulacion-usuarios-vulnerables/"),
    ("Ley sobre Tráfico, Circulación de Vehículos a Motor y Seguridad Vial (RDL 6/2015)", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722"),
]

GLOSSARY = [
    ("señalización · señal", "signposting · sign"),
    ("agente de la circulación", "traffic officer (agent)"),
    ("silbato · toque largo / corto", "whistle · long / short blast"),
    ("señalización circunstancial", "temporary (variable) signs"),
    ("panel de mensaje variable", "variable message sign"),
    ("balizamiento · baliza", "beaconing · beacon, marker"),
    ("barrera · semibarrera", "barrier · half-barrier"),
    ("hito de arista · hito de vértice", "edge post · gore marker"),
    ("captafaro («ojo de gato»)", "road stud (cat’s eye), reflector"),
    ("sistema de contención · pretil · atenuador de impacto", "restraint system · parapet · crash cushion"),
    ("semáforo · luz intermitente", "traffic light · flashing light"),
    ("semáforo de carril · aspa", "lane-control light · cross"),
    ("señal de advertencia de peligro", "danger warning sign"),
    ("señal de reglamentación · de prioridad · de obligación", "regulatory · priority · mandatory sign"),
    ("prohibición de entrada · restricción de paso", "no entry · access restriction"),
    ("fin de prohibición", "end of prohibition"),
    ("señal de indicación · de orientación", "information sign · direction (route) sign"),
    ("preseñalización · confirmación", "advance direction sign · confirmation sign"),
    ("panel complementario", "supplementary plate"),
    ("vado", "dropped kerb, vehicle entrance"),
    ("marca vial · línea continua / discontinua", "road marking · continuous / broken line"),
    ("línea de detención · de ceda el paso", "stop line · give-way line"),
    ("cebreado", "hatched area (chevron area)"),
    ("galones", "distance chevrons"),
    ("dientes de dragón · damero", "dragon’s teeth · chequerboard"),
    ("avanza-motos / avanza-bici", "advanced stop box"),
    ("zona de estancia y juego · zona de coexistencia", "residential play zone · shared space"),
    ("zona de bajas emisiones (ZBE)", "low-emission zone"),
]
