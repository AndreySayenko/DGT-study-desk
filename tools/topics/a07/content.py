# -*- coding: utf-8 -*-
"""Category A1/A2, Topic 7 content (lights), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Manual Permiso A1/A2, Tema 7: Las luces). The wording and two
figures are original; four figures are shared with Category B, Topic 7. The rules come from the Reglamento General de
Circulación (RD 1428/2003, arts. 98–107 and 109) and the Reglamento General de Vehículos (annex I, lighting devices),
as they stand in November 2026.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import moto_lights, beam_tilt, fog_matrix_moto, overtake_dazzle, curve_dazzle, dazzled_view


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Lights are for <b>being seen</b>, <b>seeing</b> and <b>warning</b>. On a motorcycle the big rule is simple: <b>dipped beam and position lights on, day and night</b>.",
         "Las luces sirven para <b>ser visto</b>, <b>ver</b> y <b>avisar</b>. En moto la gran norma es sencilla: <b>luz de cruce y de posición encendidas, de día y de noche</b>."),
        ("The exam then asks <b>when</b> to use main beam (above 40 km/h, poorly lit roads out of town), front and rear <b>fog lights</b>, how to avoid and handle <b>dazzle</b>, "
         "and which lights are <b>compulsory or optional</b> on a motorcycle.",
         "Después el examen pregunta <b>cuándo</b> usar la luz larga (a más de 40 km/h, interurbanas mal iluminadas), las <b>antiniebla</b> delantera y trasera, cómo evitar y afrontar el <b>deslumbramiento</b> "
         "y qué luces son <b>obligatorias u opcionales</b> en la moto."),
    ]))

    # ---------------------------------------------------------------- 1. purpose
    B.append(H2("1", "What vehicle lights are for", "Finalidad de las luces del vehículo"))
    B.append(TABLE(
        [T("Lights and other lighting devices are meant to…", "Las luces y demás dispositivos luminosos están destinados a…")],
        [
            [T("<b>Show the vehicle is there</b> (be seen).", "<b>Indicar la presencia</b> del vehículo (ser visto).")],
            [T("<b>Light the road</b> (see and be seen).", "<b>Alumbrar la vía</b> (ver y ser visto).")],
            [T("<b>Warn</b> other road users (signal and be seen).", "<b>Avisar</b> a los demás usuarios (señalizar y ser visto).")],
        ],
    ))
    B.append(P(
        "Every vehicle on the road between <b>sunset and sunrise</b>, or at <b>any time</b> in tunnels, underpasses and stretches with the “Tunnel” sign, must have the right lights on.",
        "Todos los vehículos que circulen entre <b>el ocaso y la salida del sol</b>, o a <b>cualquier hora</b> por túneles, pasos inferiores y tramos con la señal «Túnel», deben llevar encendido el alumbrado que corresponda."))
    B.append(E(
        "Poorly lit road (<i>vía insuficientemente iluminada</i>)", "Vía insuficientemente iluminada",
        "A road where you <b>cannot read another vehicle’s number plate at 10 m</b>, or <b>cannot make out a dark-painted vehicle at 50 m</b>.",
        "Aquella en la que <b>no se puede leer la placa de matrícula de otro vehículo a 10 m</b> o no se distingue un vehículo pintado de <b>oscuro a 50 m</b>.",
        pills_=[T("plate at 10 m", "matrícula a 10 m"), T("dark vehicle at 50 m", "vehículo oscuro a 50 m")]))
    B.append(BOX("trap", "Lights fail on the way", "Avería del alumbrado en ruta", [
        ("If a <b>breakdown you cannot fix</b> on the way forces you to ride with <b>weaker lights</b>, <b>slow down</b> until you can <b>stop within the lit area</b>.",
         "Si por una <b>avería irreparable en ruta</b> hay que circular con <b>alumbrado de intensidad inferior</b>, hay que <b>reducir la velocidad</b> hasta poder <b>detenerse dentro de la zona iluminada</b>."),
    ]))

    # ---------------------------------------------------------------- 2. presence
    B.append(H2("2", "Showing the vehicle is there", "Indicar la presencia del vehículo"))
    B.append(FIG(moto_lights, "Compulsory and optional lights on a motorcycle, front and rear.",
                 "Luces obligatorias y opcionales de la motocicleta, delante y detrás."))
    B.append(H3("2.1 Position lights", "2.1 Luz de posición"))
    B.append(P("Position lights show the vehicle’s <b>presence and width</b>: <b>white</b> at the front, <b>red</b> at the rear.",
               "Las luces de posición indican la <b>presencia y la anchura</b> del vehículo: <b>blanca</b> delante y <b>roja</b> detrás."))
    B.append(TABLE(
        [T("Vehicle", "Vehículo"), T("Front", "Delanteras"), T("Rear", "Traseras")],
        [
            [T("Two-wheeled motorcycles, three-wheelers, quadricycles", "Motocicletas de dos ruedas, vehículos de tres ruedas y cuadriciclos"), T("1 or 2", "1 o 2"), T("1 or 2", "1 o 2")],
            [T("Three-wheelers and quadricycles <b>wider than 1,300 mm</b>", "Vehículos de tres ruedas y cuadriciclos de <b>más de 1.300 mm</b> de ancho"), T("2 (one at each end)", "2 (una en cada extremo)"), T("2 (one at each end)", "2 (una en cada extremo)")],
        ],
        widths=["50%", "25%", "25%"],
        cls="small",
    ))
    B.append(TABLE(
        [T("Position lights on, at night or in poor visibility, when the vehicle is…", "Luces de posición encendidas, de noche o con poca visibilidad, si el vehículo está…")],
        [
            [T("<b>Stopped</b> on the carriageway or shoulder of <b>any road</b> (tunnels, underpasses, “Tunnel” stretches and enclosed places included).",
               "<b>Detenido o parado</b> en la calzada o el arcén de <b>cualquier vía</b> (incluidos túneles, pasos inferiores, tramos con señal «Túnel» y lugares cerrados).")],
            [T("<b>Parked</b> on the <b>non-usable shoulder</b> of an <b>interurban</b> road.", "<b>Estacionado</b> en el <b>arcén no transitable</b> de una vía <b>interurbana</b>.")],
            [T("<b>Parked</b> on the carriageway or shoulder of a <b>poorly lit travesía</b>.", "<b>Estacionado</b> en la calzada o el arcén de una <b>travesía insuficientemente iluminada</b>.")],
            [T("<b>Parked</b> on an <b>urban</b> road whose lighting does not let others see the vehicle from far enough away.",
               "<b>Estacionado</b> en la calzada o el arcén de una <b>vía urbana</b> cuya iluminación no permita a otros distinguir el vehículo a suficiente distancia.")],
        ],
    ))
    B.append(P(
        "Position lights must come on <b>automatically</b> whenever the dipped, main or fog lights are on. Riding with <b>only the position lights</b> is <b>forbidden</b>.",
        "Las luces de posición deben <b>encenderse automáticamente</b> siempre que esté encendida la de cruce, carretera o antiniebla. Está <b>prohibido circular únicamente con la luz de posición</b>."))
    B.append(H3("2.2 Reflectors", "2.2 Catadióptricos o retrocatadióptricos"))
    B.append(P("Reflectors show the vehicle is there by <b>reflecting light</b>: they have no light of their own.",
               "Indican la presencia del vehículo mediante la <b>reflexión de la luz</b>: no tienen luz propia, son reflectantes."))
    B.append(TABLE(
        [T("Vehicle", "Vehículo"), T("Rear", "Parte trasera"), T("Sides", "Laterales")],
        [
            [T("<b>Motorcycles</b>", "<b>Motocicletas</b>"), T("<b>Compulsory</b>: one <b>red, non-triangular</b> reflector (two, symmetrical, with a sidecar)", "<b>Obligatorio</b>: un catadióptrico <b>rojo no triangular</b> (dos simétricos con sidecar)"),
             T("<b>Optional</b>: one or two per side, <b>amber</b>", "<b>Opcional</b>: uno o dos por lado, <b>amarillo auto</b>")],
            [T("<b>Three-wheelers</b> (heavy quadricycles included)", "<b>Vehículos de tres ruedas</b> (incluidos los cuadriciclos pesados)"),
             T("<b>Compulsory</b>: one red non-triangular (up to 1 m wide) or <b>two</b> (wider than 1 m)", "<b>Obligatorio</b>: uno rojo no triangular (hasta 1 m de ancho) o <b>dos</b> (más de 1 m)"),
             T("<b>Optional</b>: one or two non-triangular per side, amber", "<b>Opcional</b>: uno o dos no triangulares por lado, amarillo auto")],
        ],
        widths=["26%", "42%", "32%"],
        cls="small",
    ))

    # ---------------------------------------------------------------- 3. lighting the road
    B.append(H2("3", "Lighting the road", "Iluminar la vía"))
    B.append(H3("3.1 Dipped beam", "3.1 Luz de corto alcance o de cruce"))
    B.append(P(
        "<b>White</b>; it lights the road ahead <b>without dazzling</b> or bothering others. It is the light to use <b>whenever you meet another road user</b>.",
        "De <b>color blanco</b>; alumbra la vía por delante <b>sin deslumbrar</b> ni molestar. Es la que se usa <b>cuando se cruza con otro usuario</b>, para no deslumbrarle."))
    B.append(E(
        "Motorcycles: dipped beam all day", "Motocicletas: luz de cruce todo el día",
        "Motorcycles, with or without sidecar, must ride on public roads with the <b>dipped beam and the position lights on at any time of day</b> — even past an “end of dipped beam” sign.",
        "Las motocicletas, con o sin sidecar, deben llevar encendidas la <b>luz de cruce junto con la de posición</b> por las vías públicas <b>a cualquier hora del día</b>, aunque aparezca la señal «Fin de alumbrado de corto alcance».",
        pills_=[T("day and night", "de día y de noche")]))
    B.append(TABLE(
        [T("Dipped beam: vehicles required to have it", "Luz de cruce: vehículos obligados"), T("Number", "Número")],
        [[T("Mopeds, motorcycles, three-wheelers and quadricycles", "Ciclomotores, motocicletas, vehículos de tres ruedas y cuadriciclos"), T("1 or 2", "1 o 2")]],
        widths=["70%", "30%"],
    ))
    B.append(H3("3.2 Main beam", "3.2 Luz de largo alcance o de carretera"))
    B.append(P(
        "<b>White</b> and <b>more intense</b> than the dipped beam; it lights the road <b>far ahead</b>. Motorcycles equipped with it must use it <b>above 40 km/h</b>: "
        "<b>sunset to sunrise</b> on <b>poorly lit</b> roads <b>out of town</b>, and <b>at any time</b> in <b>poorly lit</b> tunnels, underpasses and “Tunnel” stretches.",
        "De <b>color blanco</b> y <b>más intensa</b> que la de cruce; alumbra la vía <b>a larga distancia</b>. Las motocicletas equipadas con ella deben usarla <b>a más de 40 km/h</b>: "
        "<b>entre el ocaso y la salida del sol</b> por vías <b>fuera de poblado insuficientemente</b> iluminadas, y <b>a cualquier hora</b> por túneles, pasos inferiores y tramos con señal «Túnel» <b>insuficientemente</b> iluminados."))
    B.append(TABLE(
        [T("Case", "Caso"), T("Light", "Luz")],
        [
            [T("No main beam fitted, or main beam could <b>dazzle</b> someone", "Sin luz de largo alcance, o con posibilidad de <b>deslumbrar</b>"), T("<b>Dipped</b>", "<b>Cruce</b>")],
            [T("At <b>40 km/h or less</b>", "A <b>40 km/h o menos</b>"), T("<b>Either</b>", "<b>Cualquiera de las dos</b>")],
            [T("Vehicle <b>stopped or parked</b>, or riding <b>in town</b>", "Vehículo <b>parado o estacionado</b>, o circulando <b>dentro de poblado</b>"), T("Main beam <b>forbidden</b>", "Largo alcance <b>prohibido</b>")],
            [T("Main beams fitted on motorcycles, three-wheelers and quadricycles", "Luces de carretera en motos, tres ruedas y cuadriciclos"), T("1 or 2", "1 o 2")],
        ],
        widths=["66%", "34%"],
    ))
    B.append(H3("3.3 Fog lights", "3.3 Luces antiniebla"))
    B.append(TABLE(
        [T("", ""), T("Front fog lights", "Antiniebla delantera"), T("Rear fog light", "Antiniebla trasera")],
        [
            [T("<b>Job</b>", "<b>Función</b>"), T("Light the road better in bad weather", "Aumentar la iluminación de la vía con meteorología adversa"),
             T("Make the vehicle more visible from behind when conditions are <b>especially</b> bad; it does not light the road", "Hacer más visible el vehículo por detrás con condiciones <b>especialmente</b> adversas; no alumbra la vía")],
            [T("<b>On a motorcycle</b>", "<b>En la moto</b>"), T("<b>Optional</b>: 1 or 2, <b>white or selective yellow</b>", "<b>No obligatoria</b>: 1 o 2, <b>blancas o amarillo selectivo</b>"),
             T("<b>Optional</b>: 1 or 2, <b>red</b>", "<b>No obligatoria</b>: 1 o 2, <b>rojas</b>")],
            [T("<b>Switches on only with</b>", "<b>Solo se enciende con</b>"), T("the <b>position lights</b> on; alone or with the dipped or even the main beam (not advisable: it reflects and dazzles you)",
                                                                              "la <b>luz de posición</b> encendida; sola o con la de cruce o incluso con la larga (no aconsejable: se refleja y deslumbra al conductor)"),
             T("the <b>dipped, main or front fog</b> light on", "la luz de <b>cruce, carretera o antiniebla delantera</b> encendida")],
        ],
        widths=["20%", "40%", "40%"],
        cls="small",
    ))
    B.append(FIG(fog_matrix_moto, "Front fog lights may be used in bad weather and on narrow winding roads; the rear one only when conditions are especially bad.",
                 "La antiniebla delantera puede usarse con mal tiempo y en vías estrechas con curvas; la trasera, solo con condiciones especialmente adversas."))
    B.append(TABLE(
        [T("When you may use…", "Cuándo se puede usar…"), T("Conditions", "Condiciones")],
        [
            [T("<b>Front</b> fog light", "Antiniebla <b>delantera</b>"), T("<b>Fog, heavy rain, snowfall, clouds of dust or smoke</b>; and on <b>narrow roads</b> (carriageway <b>6.50 m or less</b>) with the “dangerous bends” sign.",
                                                                       "<b>Niebla, lluvia intensa, nevada, nubes de polvo o humo</b>; y en <b>vías estrechas</b> (calzada de <b>6,50 m o menos</b>) con la señal «curvas peligrosas».")],
            [T("<b>Rear</b> fog light", "Antiniebla <b>trasera</b>"), T("Only when conditions are <b>especially</b> bad: <b>thick</b> fog, <b>very heavy</b> rain, <b>heavy</b> snowfall, <b>dense</b> clouds of dust or smoke. <b>Not</b> on narrow winding roads.",
                                                                      "Solo con condiciones <b>especialmente</b> desfavorables: niebla <b>espesa</b>, lluvia <b>muy</b> intensa, nevada <b>fuerte</b>, nubes <b>densas</b> de polvo o humo. <b>No</b> en vías estrechas con curvas.")],
        ],
        widths=["26%", "74%"],
        cls="small",
    ))
    B.append(BOX("key", "Poor visibility because of the weather", "Visibilidad reducida por la meteorología", [
        ("<b>By day</b>: at least the <b>position lights</b> plus <b>any</b> lighting light (fog, dipped or main).", "<b>De día</b>: al menos la <b>luz de posición</b> con <b>cualquier</b> luz de alumbrado (antiniebla, corto o largo alcance)."),
        ("<b>By night</b>: at least <b>position and dipped beam</b>; the others (fog or main) may be added.", "<b>De noche</b>: al menos <b>posición y cruce</b>, pudiendo usar las demás (antiniebla o largo alcance)."),
    ]))
    B.append(H3("3.4 Lanes where lights are always on", "3.4 Situaciones especiales"))
    B.append(P(
        "At least the <b>dipped beam</b>, <b>by day and by night</b>, for every vehicle on a <b>reversible lane</b>, on roads with a <b>temporary additional lane</b>, and on a <b>contraflow lane</b> and the <b>normal-direction lane next to it</b>.",
        "Deben llevar encendida al menos la <b>luz de cruce</b>, <b>de día y de noche</b>, todos los vehículos que circulen por un <b>carril reversible</b>, por vías con un <b>carril adicional circunstancial</b>, y por un <b>carril habilitado en sentido contrario al habitual</b> y el <b>carril del sentido normal contiguo</b>."))

    B.append(H3("3.5 Dazzle", "3.5 Deslumbramientos"))
    B.append(P("When the eyes get more light than they can take, a <b>temporary blindness</b> follows: dazzle.",
               "Cuando los ojos reciben más luz de la que pueden soportar se produce una <b>ceguera temporal</b> llamada deslumbramiento."))
    B.append(TABLE(
        [T("To avoid dazzling others", "Para no deslumbrar")],
        [
            [T("Switch from main to <b>dipped</b> as soon as you might dazzle anyone, above all <b>oncoming</b> drivers (<b>even if they don’t dip</b>) and drivers ahead in your direction, through their <b>mirrors</b>. "
               "Don’t switch back until you are sure you will dazzle nobody.",
               "Sustituir la luz larga por la de <b>cruce</b> en cuanto se pueda deslumbrar a alguien, sobre todo a los que vienen <b>en sentido contrario</b> (<b>aunque ellos no lo hagan</b>) y a los que van en el mismo sentido, por los <b>retrovisores</b>. "
               "No volver a la larga hasta estar seguro de que no se deslumbra a nadie.")],
            [T("<b>Overtaking</b>: the overtaking rider may not switch on the main beam until <b>level</b> with the other vehicle; at that moment the <b>overtaken</b> driver switches to dipped.",
               "<b>Adelantamientos</b>: el que adelanta no puede conectar la luz larga hasta que los dos vehículos estén en <b>posición paralela</b>; en ese momento, el <b>adelantado</b> conecta la de cruce.")],
            [T("<b>Bends</b>: the vehicle whose road turns <b>right</b> shines on oncoming drivers first, so it is the <b>first to dip</b>; the one turning left can wait a little.",
               "<b>Curvas</b>: el haz del que encuentra la curva hacia la <b>derecha</b> incide sobre los que vienen de frente, así que es el <b>primero en cambiar</b> a cruce; el que la encuentra hacia la izquierda puede retrasarlo.")],
        ],
    ))
    B.append(FIG(overtake_dazzle, "Overtaking at night: the overtaking rider waits until level before switching to main beam; at that moment the overtaken driver dips.",
                 "Adelantamiento de noche: el que adelanta espera a estar en paralelo para poner la larga; en ese momento el adelantado pone la de cruce."))
    B.append(FIG(curve_dazzle, "On a bend, the rider or driver whose road turns right is the first to dip.",
                 "En una curva, el primero en poner la de cruce es aquel para quien la curva es hacia la derecha."))
    B.append(FIG(beam_tilt, "Keep your headlight properly aimed, especially when you carry a passenger or a load at the back.",
                 "Mantén bien reglado el faro, sobre todo cuando llevas pasajero o carga en la parte trasera."))
    B.append(FIG(dazzled_view, "Reducing the chance of being dazzled, and what to do if it happens.",
                 "Cómo reducir la posibilidad de ser deslumbrado y qué hacer si ocurre."))
    B.append(TABLE(
        [T("Situation", "Situación"), T("What to do", "Qué hacer")],
        [
            [T("Oncoming vehicles could dazzle you", "Pueden deslumbrarte los que vienen de frente"), T("Look to the <b>right</b>, guided by the <b>line along the edge</b> of the carriageway, and close the <b>left eye</b> (it gets the most light).",
                                                                                                      "Mirar hacia la <b>derecha</b>, guiándose por la <b>línea que separa la calzada del arcén</b>, y cerrar el <b>ojo izquierdo</b>, que es el que más luz recibe.")],
            [T("Vehicles behind could dazzle you", "Pueden deslumbrarte los de detrás"), T("Change the angle of your <b>mirrors</b>, or change your <b>position</b> so the light doesn’t reach your eyes.",
                                                                                            "Cambiar la <b>orientación de los retrovisores</b> o <b>cambiar de posición</b> para que la luz no se refleje en los ojos.")],
            [T("You <b>are</b> dazzled", "Te <b>deslumbran</b>"), T("<b>Slow down</b> as much as needed, even to a <b>stop</b>, <b>without changing your position</b> on the carriageway (don’t move onto the shoulder: you could leave the road or hit someone using it).",
                                                                  "<b>Reducir la velocidad</b> todo lo necesario, incluso hasta la <b>detención</b>, <b>sin variar la posición</b> en la calzada (sin salir al arcén: se corre el riesgo de salirse de la vía o de encontrar a alguien en él).")],
        ],
        widths=["32%", "68%"],
    ))

    # ---------------------------------------------------------------- 4. warning
    B.append(H2("4", "Warning other road users", "Avisar a los demás usuarios"))
    B.append(TABLE(
        [T("Light", "Luz"), T("What it does · on a motorcycle", "Para qué sirve · en la moto")],
        [
            [T("<b>Indicators</b>", "<b>Intermitentes</b>"), T("Show you are going to make a manoeuvre that moves the vehicle <b>sideways</b>. <b>Amber</b>, <b>compulsory</b>.",
                                                              "Indican la intención de realizar una maniobra con <b>desplazamiento lateral</b>. Color <b>amarillo auto</b>, <b>obligatorios</b>.")],
            [T("<b>Hazard lights</b> (<i>luz de emergencia</i>)", "<b>Luz o señal de emergencia</b>"), T("<b>All indicators flashing together</b>, to warn of the danger the vehicle poses, stopped or moving, because of an emergency (breakdown, accident…). "
                                                                                                    "Compulsory on all automobiles <b>except motorcycles</b>, where it is <b>optional</b>. Switched on with a <b>flashing red</b> tell-tale on the controls.",
                                                                                                    "<b>Funcionamiento simultáneo de todos los intermitentes</b>, para advertir del peligro del vehículo, inmovilizado o en movimiento, por una emergencia (avería, accidente…). "
                                                                                                    "Obligatoria en todos los automóviles <b>salvo en las motocicletas</b>, donde es <b>opcional</b>. Se acciona con un testigo <b>rojo intermitente</b> en los mandos.")],
            [T("<b>Brake light</b>", "<b>Luz de frenado</b>"), T("Tells those behind that you are <b>braking</b> (front, rear or both brakes). Use it <b>repeatedly</b>, when possible, to warn that you will stop or brake hard.",
                                                                 "Indica a los de detrás que se <b>está frenando</b> (freno delantero, trasero o ambos). Debe <b>utilizarse de forma reiterada</b>, siempre que sea posible, para advertir que se va a inmovilizar el vehículo o frenar considerablemente.")],
            [T("<b>Reversing light</b>", "<b>Luz de marcha atrás</b>"), T("<b>White</b>, at the rear; lights the road behind and warns that the vehicle is reversing or about to. <b>Optional</b> on motorcycles.",
                                                                          "<b>Blanca</b>, en la parte posterior; alumbra la vía por detrás y advierte de que el vehículo va, o está a punto de ir, marcha atrás. <b>Opcional</b> en motocicletas.")],
        ],
        widths=["24%", "76%"],
    ))

    # ---------------------------------------------------------------- 5. other
    B.append(H2("5", "Other lights", "Otras luces"))
    B.append(E(
        "Number-plate light", "Luz de la placa de matrícula",
        "Whenever the <b>position lights</b> are on, the <b>rear number-plate light</b> must come on <b>automatically</b>.",
        "Cuando el vehículo lleve encendidas las <b>luces de posición</b>, debe encenderse <b>automáticamente</b> la luz de la <b>placa de matrícula posterior</b>."))

    # ---------------------------------------------------------------- 6. traps
    B.append(H2("6", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("Motorcycles: <b>dipped beam day and night</b>, even after an “end of dipped beam” sign.", "Motos: <b>luz de cruce de día y de noche</b>, aunque aparezca la señal «Fin de alumbrado de corto alcance»."),
        ("Riding with <b>only the position lights</b> is forbidden.", "Está prohibido circular <b>solo con la luz de posición</b>."),
        ("Main beam compulsory only <b>above 40 km/h</b>, on <b>poorly lit</b> roads out of town (or poorly lit tunnels); never in town, stopped or parked.",
         "Luz larga obligatoria solo <b>a más de 40 km/h</b>, en vías <b>insuficientemente iluminadas</b> fuera de poblado (o túneles mal iluminados); nunca en poblado, parado o estacionado."),
        ("Front fog: also on narrow roads (≤ 6.50 m) with the bends sign. Rear fog: <b>only especially bad</b> weather, never for bends.",
         "Antiniebla delantera: también en vías estrechas (≤ 6,50 m) con señal de curvas. Trasera: <b>solo con condiciones especialmente adversas</b>, nunca por las curvas."),
        ("Rear fog switches on only with dipped, main or front fog on; front fog only with position lights on.", "La antiniebla trasera solo con cruce, carretera o antiniebla delantera; la delantera, solo con la de posición."),
        ("Overtaking at night: main beam only once <b>level</b>; the overtaken driver then dips.", "Adelantamiento de noche: luz larga solo al estar <b>en paralelo</b>; entonces el adelantado pone la de cruce."),
        ("Bend: the one turning <b>right</b> dips first.", "Curva: cambia primero el que la encuentra hacia la <b>derecha</b>."),
        ("Dazzled: slow down, even stop, <b>without</b> moving onto the shoulder; look <b>right</b>, close the <b>left</b> eye.", "Deslumbrado: reducir, incluso parar, <b>sin</b> salir al arcén; mirar a la <b>derecha</b> y cerrar el ojo <b>izquierdo</b>."),
        ("Hazard lights and reversing light: <b>optional</b> on motorcycles. Rear red reflector: <b>compulsory</b>, not triangular.", "Emergencia y marcha atrás: <b>opcionales</b> en moto. Catadióptrico trasero rojo: <b>obligatorio</b>, no triangular."),
        ("Passenger or load at the back raises the beam: <b>adjust the headlight</b>.", "Pasajero o carga detrás elevan el haz: <b>regula el faro</b>."),
    ]))

    # ---------------------------------------------------------------- 7. numbers
    B.append(H2("7", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Poorly lit road", "Vía insuficientemente iluminada"), T("plate unreadable at 10 m · dark vehicle unseen at 50 m", "matrícula ilegible a 10 m · vehículo oscuro no visible a 50 m")],
            [T("Main beam compulsory above", "Luz larga obligatoria a más de"), T("40 km/h", "40 km/h")],
            [T("Narrow road for front fog lights", "Vía estrecha para la antiniebla delantera"), T("≤ 6.50 m carriageway + bends sign", "calzada ≤ 6,50 m + señal de curvas")],
            [T("Position, dipped and main lights on a motorcycle", "Posición, cruce y carretera en moto"), T("1 or 2 each", "1 o 2 de cada")],
            [T("Three-wheelers and quadricycles wider than", "Tres ruedas y cuadriciclos de más de"), T("1,300 mm: 2 position lights each end", "1.300 mm: 2 luces de posición, una en cada extremo")],
            [T("Three-wheelers: two rear reflectors if wider than", "Tres ruedas: dos catadióptricos traseros si miden más de"), T("1 m", "1 m")],
            [T("Hazard lights tell-tale", "Testigo de la luz de emergencia"), T("flashing red", "rojo intermitente")],
        ],
        widths=["50%", "50%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
QUIZ_IDS = ["pu2", "ps2", "rf1", "dp1", "dp3", "mb2", "fg2", "fg5", "sp1", "dz2", "dz5", "wr2"]


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
    ("Reglamento General de Circulación (RD 1428/2003), arts. 98–107 (lights) and 109 (warnings) — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Reglamento General de Vehículos (RD 2822/1998), annex I: lighting and light-signalling devices — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-1999-1826"),
]

GLOSSARY = [
    ("alumbrado · dispositivo luminoso", "lights · lighting device"),
    ("ocaso · salida del sol", "sunset · sunrise"),
    ("vía insuficientemente iluminada", "poorly lit road"),
    ("luz de posición", "position light"),
    ("catadióptrico", "reflector"),
    ("luz de corto alcance o de cruce", "dipped beam (low beam)"),
    ("luz de largo alcance o de carretera", "main beam (high beam)"),
    ("luz antiniebla delantera / trasera", "front / rear fog light"),
    ("amarillo selectivo", "selective yellow"),
    ("amarillo auto", "amber"),
    ("niebla espesa · lluvia muy intensa", "thick fog · very heavy rain"),
    ("curvas peligrosas", "dangerous bends (sign)"),
    ("carril reversible · adicional · en sentido contrario", "reversible · additional · contraflow lane"),
    ("deslumbramiento · deslumbrar", "dazzle · to dazzle"),
    ("ceguera temporal", "temporary blindness"),
    ("posición paralela", "level with (alongside)"),
    ("reglaje de los faros", "headlight aim"),
    ("intermitente · indicador de dirección", "indicator"),
    ("luz o señal de emergencia", "hazard warning lights"),
    ("testigo", "tell-tale (dashboard light)"),
    ("luz de frenado", "brake light"),
    ("luz de marcha atrás", "reversing light"),
    ("luz de la placa de matrícula", "number-plate light"),
]
