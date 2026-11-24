# -*- coding: utf-8 -*-
"""Topic 7 content (vehicle lights), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Tema 7: Las luces). The wording and the figures are original;
the rules come from the Reglamento General de Circulación (RD 1428/2003, arts. 98–113) and the Reglamento General de
Vehículos (RD 2822/1998, Anexo X on lighting), as they stand in November 2026.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import rear_lights, presence, fog_matrix, overtake_dazzle, curve_dazzle, dazzled_view


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Each light has a <b>job</b>: to <b>show the vehicle is there</b> (position, parking, reflectors, clearance), to <b>light the road</b> (dipped, main, fog) "
         "or to <b>warn</b> (indicators, hazard, brake, reversing). The exam asks which light, its <b>colour</b>, <b>how many</b>, and <b>when</b> it is used.",
         "Cada luz tiene una <b>función</b>: <b>indicar la presencia</b> (posición, estacionamiento, catadióptricos, gálibo), <b>alumbrar la vía</b> (cruce, carretera, antiniebla) "
         "o <b>avisar</b> (intermitentes, emergencia, freno, marcha atrás). El examen pregunta qué luz, su <b>color</b>, <b>cuántas</b> y <b>cuándo</b> se usa."),
        ("Key numbers: <b>10 m / 50 m</b> (insufficient lighting), <b>40 km/h</b> (main beam), <b>6 m and 2 m</b> (parking light), <b>2.10 m</b> (clearance lights), <b>6.50 m</b> (front fog on narrow roads), <b>150 m</b> (cyclist’s luminous or reflective element).",
         "Números clave: <b>10 m / 50 m</b> (iluminación insuficiente), <b>40 km/h</b> (luz larga), <b>6 m y 2 m</b> (luz de estacionamiento), <b>2,10 m</b> (gálibo), <b>6,50 m</b> (antiniebla en vías estrechas), <b>150 m</b> (elemento luminoso o reflectante del ciclista)."),
        ("The sections follow the order of your course’s Topic 7. Spanish exam terms are in <i>italics</i> in the English text, and a glossary closes the topic.",
         "Los apartados siguen el orden del Tema 7 de tu curso. Al final hay un glosario español–inglés."),
    ]))

    # ---------------------------------------------------------------- 1. purpose
    B.append(H2("1", "What vehicle lights are for", "Finalidad de las luces del vehículo"))
    B.append(TABLE(
        [T("Lights are for…", "Las luces sirven para…"), T("Which means", "Es decir")],
        [
            [T("<b>Showing</b> the vehicle is there", "<b>Indicar</b> la presencia del vehículo"), T("being seen", "ser vistos")],
            [T("<b>Lighting</b> the road", "<b>Alumbrar</b> la vía"), T("seeing and being seen", "ver y ser vistos")],
            [T("<b>Warning</b> other road users", "<b>Avisar</b> a los demás usuarios"), T("signalling and being seen", "señalizar y ser vistos")],
        ],
        widths=["50%", "50%"],
    ))
    B.append(P(
        "Every vehicle on the move <b>between sunset and sunrise</b>, and <b>at any time</b> in <b>tunnels, underpasses</b> and stretches signed “Tunnel”, must have the right lights on.",
        "Todos los vehículos que circulen <b>entre el ocaso y la salida del sol</b>, o <b>a cualquier hora</b> en <b>túneles, pasos inferiores</b> y tramos con la señal «Túnel», deben llevar encendido el alumbrado que corresponda."))
    B.append(E(
        "Insufficiently lit road", "Vía insuficientemente iluminada",
        "A road where you <b>cannot read a number plate at 10 m</b>, or <b>cannot make out a dark-painted vehicle at 50 m</b>.",
        "Aquella en la que <b>no se puede leer la placa de matrícula de otro vehículo a 10 m</b> o no se distingue un vehículo pintado de <b>oscuro a 50 m</b>.",
        pills_=[T("plate at 10 m", "matrícula a 10 m"), T("dark car at 50 m", "vehículo oscuro a 50 m")]))
    B.append(H3("1.2 Rules for the lights themselves", "1.2 Condiciones de los dispositivos luminosos"))
    B.append(TABLE(
        [T("Rule", "Norma")],
        [
            [T("Paired lights or reflectors with the same job have the <b>same colour and intensity</b> and sit <b>symmetrically</b>, if possible at the same distance from the edges.",
               "Las luces y catadióptricos dobles con la misma finalidad son del <b>mismo color e intensidad</b> y van <b>simétricos</b>, a ser posible a la misma distancia de los bordes.")],
            [T("No light may <b>flash</b> or change intensity, except those the rules allow (indicators, hazard lights…).", "Ninguna luz será <b>intermitente</b> o de intensidad variable, salvo las previstas (intermitentes, emergencia…).")],
            [T("No <b>more lights</b> than authorised; unauthorised paints or luminous or reflective devices are <b>forbidden</b>.",
               "No se instalan <b>más luces</b> de las autorizadas; se <b>prohíben</b> pinturas o dispositivos luminosos o reflectantes no autorizados.")],
            [T("If the lighting fails beyond repair on the way and you must use a <b>weaker light</b>, <b>slow down</b> until you can <b>stop within the lit area</b>.",
               "Si por una avería irreparable en ruta hay que circular con una luz de <b>intensidad inferior</b>, se <b>reduce la velocidad</b> hasta poder <b>detenerse dentro de la zona iluminada</b>.")],
        ],
    ))

    # ---------------------------------------------------------------- 2. showing presence
    B.append(H2("2", "Lights that show the vehicle is there", "Indicar la presencia del vehículo"))
    B.append(FIG(presence, "Position lights, reflectors and clearance lights: none of them lights the road, they make the vehicle visible.",
                 "Luces de posición, catadióptricos y gálibo: ninguna alumbra la vía, hacen visible el vehículo."))
    B.append(H3("2.1 Position lights", "2.1 Luz de posición"))
    B.append(P(
        "<b>Front (white)</b> and <b>rear (red)</b> position lights show the vehicle’s <b>presence and width</b>. <b>Side</b> ones show its presence: <b>amber</b>, or red when next to the rear lights.",
        "Las luces de posición <b>delanteras (blancas)</b> y <b>traseras (rojas)</b> indican la <b>presencia y la anchura</b> del vehículo. Las <b>laterales</b> indican su presencia: <b>amarillo auto</b>, o rojas si están junto a las traseras."))
    B.append(TABLE(
        [T("Vehicle", "Vehículo"), T("Front", "Delanteras"), T("Rear", "Traseras"), T("Side", "Laterales")],
        [
            [T("Two-wheeled motorcycles, three-wheelers, quadricycles", "Motocicletas de dos ruedas, vehículos de tres ruedas, cuadriciclos"), T("1 or 2", "1 o 2"), T("1 or 2", "1 o 2"), T("—", "—")],
            [T("Other automobiles", "Resto de automóviles"), T("2", "2"), T("2", "2"), T("—", "—")],
            [T("Trailers and semitrailers", "Remolques y semirremolques"), T("2 if wider than 1.60 m (otherwise optional)", "2 si miden más de 1,60 m de ancho (si no, opcional)"),
             T("2", "2"), T("at least 2 if longer than 6 m", "al menos 2 si miden más de 6 m de largo")],
        ],
        widths=["40%", "22%", "14%", "24%"],
        cls="small",
    ))
    B.append(TABLE(
        [T("Position lights on, at night or in poor visibility, when the vehicle is…", "Luces de posición encendidas, de noche o con poca visibilidad, si el vehículo está…")],
        [
            [T("<b>Stopped</b> on the carriageway or shoulder of <b>any road</b> (tunnels, underpasses and enclosed places included).",
               "<b>Detenido o parado</b> en la calzada o el arcén de <b>cualquier vía</b> (incluidos túneles, pasos inferiores y lugares cerrados).")],
            [T("<b>Parked</b> on the <b>non-usable shoulder</b> of an <b>interurban</b> road.", "<b>Estacionado</b> en el <b>arcén no transitable</b> de una vía <b>interurbana</b>.")],
            [T("<b>Parked</b> on the carriageway or shoulder of a <b>poorly lit travesía</b> (they may be replaced by <b>parking lights</b>, or by the position lights on the traffic side if parked in line).",
               "<b>Estacionado</b> en la calzada o el arcén de una <b>travesía insuficientemente iluminada</b> (pueden sustituirse por las <b>luces de estacionamiento</b>, o por las de posición del lado de la calzada si se estaciona en línea).")],
            [T("<b>Parked</b> on an <b>urban</b> street whose lighting does not let others see the vehicle from far enough away.",
               "<b>Estacionado</b> en una <b>vía urbana</b> cuya iluminación no permita a los demás distinguir el vehículo a suficiente distancia.")],
        ],
    ))
    B.append(P(
        "Position lights must also come on <b>automatically</b> whenever the dipped, main or fog lights are on, so every vehicle driving at night, in poor visibility or in tunnels has them on.",
        "Además, las luces de posición deben <b>encenderse automáticamente</b> siempre que estén encendidas la de cruce, carretera o antiniebla; por eso las llevan todos los vehículos que circulen de noche, con poca visibilidad o por túneles."))
    B.append(H3("2.2 Parking lights", "2.2 Luz de estacionamiento"))
    B.append(E(
        "Parking lights (<i>luz de estacionamiento</i>)", "Luz de estacionamiento",
        "May <b>replace the position lights</b> when the vehicle is <b>parked in a poorly lit travesía</b>. <b>Two white in front and two red behind</b>, in the same place as the position lights "
        "(usually only the pair on the <b>traffic side</b> is lit). <b>Optional</b> for vehicles <b>up to 6 m long and 2 m wide</b>; <b>forbidden</b> on all others.",
        "Puede <b>sustituir a la luz de posición</b> cuando el vehículo está <b>estacionado en una travesía insuficientemente iluminada</b>. <b>Dos blancas delante y dos rojas detrás</b>, coincidiendo con las de posición "
        "(lo normal es que solo se encienda la pareja del <b>lado de la calzada</b>). <b>Opcional</b> en vehículos de <b>hasta 6 m de largo y 2 m de ancho</b>; <b>prohibida</b> en los demás.",
        pills_=[T("≤ 6 m long, ≤ 2 m wide", "≤ 6 m de largo, ≤ 2 m de ancho")]))
    B.append(H3("2.3 Reflectors", "2.3 Catadióptricos o retrocatadióptricos"))
    B.append(P("They show the vehicle is there by <b>reflecting light</b> from another source, seen by an observer near that source: <b>they have no light of their own</b>.",
               "Indican la presencia del vehículo <b>reflejando la luz</b> de una fuente ajena, con el observador cerca de esa fuente: <b>no tienen luz propia</b>."))
    B.append(TABLE(
        [T("Reflector", "Catadióptrico"), T("Colour and shape", "Color y forma"), T("Compulsory on", "Obligatorio para")],
        [
            [T("<b>Front</b>", "<b>Delantero</b>"), T("<b>White</b>, any shape except triangular", "<b>Blanco</b>, cualquier forma salvo la triangular"), T("VMP, trailers, semitrailers", "VMP, remolques y semirremolques")],
            [T("<b>Rear</b>", "<b>Trasero</b>"), T("<b>Red</b>, any shape except triangular", "<b>Rojo</b>, cualquier forma salvo la triangular"), T("VMP, mopeds, automobiles", "VMP, ciclomotores y automóviles")],
            [T("<b>Side</b>", "<b>Lateral</b>"), T("<b>Amber</b>, not triangular (red if mounted with the rear reflector)", "<b>Amarillo auto</b>, no triangular (rojo si va junto al trasero)"), T("VMP, trailers, semitrailers", "VMP, remolques y semirremolques")],
        ],
        widths=["18%", "48%", "34%"],
        cls="small",
    ))
    B.append(P("The <b>triangular</b> shape is <b>reserved for the rear reflectors of trailers and semitrailers</b>. Other retroreflective plates and markings on vehicles are not reflectors.",
               "La <b>forma triangular</b> está <b>reservada a los catadióptricos traseros de remolques y semirremolques</b>. Las demás placas y señales retrorreflectantes no se consideran catadióptricos."))
    B.append(H3("2.4 Clearance lights", "2.4 Luz de gálibo"))
    B.append(E(
        "Clearance lights (<i>luz de gálibo</i>)", "Luz de gálibo",
        "Show the vehicle’s <b>width</b> and, with the position lights, its <b>size</b>. <b>Two white</b> at the front and <b>two red</b> at the rear. "
        "<b>Compulsory</b> for vehicles <b>wider than 2.10 m</b>; <b>optional</b> between <b>1.80 and 2.10 m</b>.",
        "Indica la <b>anchura</b> del vehículo y, junto a las de posición, su <b>volumen</b>. <b>Dos blancas</b> delante y <b>dos rojas</b> detrás. "
        "<b>Obligatoria</b> en vehículos de <b>más de 2,10 m</b> de ancho; <b>opcional</b> entre <b>1,80 y 2,10 m</b>.",
        pills_=[T("&gt; 2.10 m compulsory", "&gt; 2,10 m obligatoria"), T("1.80–2.10 m optional", "1,80–2,10 m opcional")]))

    # ---------------------------------------------------------------- 3. lighting the road
    B.append(H2("3", "Lights that light the road", "Iluminar la vía"))
    B.append(H3("3.1 Dipped beam", "3.1 Luz de corto alcance o de cruce"))
    B.append(P("<b>White</b>; it lights the road ahead <b>without dazzling</b> or bothering others. It is the light to use <b>whenever you meet another road user</b>.",
               "De <b>color blanco</b>; alumbra la vía por delante <b>sin deslumbrar</b> ni molestar. Es la que se usa <b>cuando se cruza con otro usuario</b>."))
    B.append(TABLE(
        [T("Dipped beam + position lights on, for every motor vehicle and moped…", "Cruce + posición encendidas, en todo vehículo de motor y ciclomotor…")],
        [
            [T("<b>Sunset to sunrise</b>: on <b>every road in town</b> (urban streets, travesías, tunnels…) <b>however well lit</b>; and on <b>out-of-town</b> roads that are <b>well lit</b>.",
               "<b>Entre el ocaso y la salida del sol</b>: en <b>todas las vías dentro de poblado</b> (urbanas, travesías, túneles…) <b>con independencia de su iluminación</b>; y en las <b>interurbanas suficientemente iluminadas</b>.")],
            [T("<b>At any time</b>: in <b>well-lit</b> tunnels, underpasses and “Tunnel” stretches.", "<b>A cualquier hora</b>: en túneles, pasos inferiores y tramos con señal «Túnel» <b>suficientemente iluminados</b>.")],
            [T("<b>Motorcycles</b>: on public roads <b>at any time of day</b>.", "<b>Motocicletas</b>: por las vías públicas <b>a cualquier hora del día</b>.")],
        ],
    ))
    B.append(H3("3.2 Main beam", "3.2 Luz de largo alcance o de carretera"))
    B.append(P(
        "<b>White</b> and <b>more intense</b>; it lights the road <b>far ahead</b>. Vehicles that have it must use it <b>above 40 km/h</b>: <b>sunset to sunrise</b> on <b>poorly lit out-of-town</b> roads, "
        "and <b>at any time</b> in <b>poorly lit</b> tunnels and underpasses. Use the dipped beam instead if the vehicle has no main beam, or whenever the main beam could <b>dazzle</b> someone. "
        "<b>At 40 km/h or less</b>, either may be used.",
        "De <b>color blanco</b> y <b>más intensa</b>; alumbra la vía <b>a larga distancia</b>. Quien la tenga debe usarla <b>a más de 40 km/h</b>: <b>entre el ocaso y la salida del sol</b> en vías <b>interurbanas insuficientemente iluminadas</b>, "
        "y <b>a cualquier hora</b> en túneles y pasos inferiores <b>insuficientemente iluminados</b>. Se usa la de cruce si no se tiene luz larga o si puede <b>deslumbrar</b> a alguien. "
        "<b>A 40 km/h o menos</b>, se puede usar cualquiera de las dos."))
    B.append(BOX("trap", "Main beam is forbidden…", "Prohibida la luz de largo alcance…", [
        ("With the vehicle <b>stopped or parked</b>.", "Con el vehículo <b>parado o estacionado</b>."),
        ("On <b>roads in town</b>.", "En <b>vías dentro de poblado</b>."),
    ]))
    B.append(TABLE(
        [T("Vehicle", "Vehículo"), T("Dipped beams", "Luces de cruce"), T("Main beams", "Luces de carretera")],
        [
            [T("Mopeds, motorcycles, three-wheelers, quadricycles", "Ciclomotores, motocicletas, tres ruedas, cuadriciclos"), T("1 or 2", "1 o 2"), T("1 or 2 (listed for motorcycles, three-wheelers and quadricycles)", "1 o 2 (motocicletas, tres ruedas y cuadriciclos)")],
            [T("Other automobiles", "Resto de automóviles"), T("2", "2"), T("an <b>even number</b>", "un <b>número par</b>")],
        ],
        widths=["46%", "22%", "32%"],
        cls="small",
    ))
    B.append(H3("3.3 Fog lights", "3.3 Luces antiniebla"))
    B.append(TABLE(
        [T("", ""), T("Front fog lights", "Antiniebla delantera"), T("Rear fog light", "Antiniebla trasera")],
        [
            [T("<b>Job</b>", "<b>Función</b>"), T("Light the road better in bad weather", "Aumentar la iluminación de la vía con meteorología adversa"),
             T("Make the vehicle more visible from behind; it does not light the road", "Hacer más visible el vehículo por detrás; no alumbra la vía")],
            [T("<b>Colour, number</b>", "<b>Color, número</b>"), T("<b>2 white or selective yellow</b> (motorcycles and three-wheelers: 1 or 2)", "<b>2 blancas o amarillo selectivo</b> (motos y tres ruedas: 1 o 2)"),
             T("<b>1 or 2 red</b>", "<b>1 o 2 rojas</b>")],
            [T("<b>Fitted</b>", "<b>Instalación</b>"), T("<b>Optional</b> for every motor vehicle", "<b>Opcional</b> en todos los vehículos de motor"),
             T("<b>Compulsory</b> for motor vehicles (except motorcycles and three-wheelers), trailers and semitrailers", "<b>Obligatoria</b> en vehículos de motor (salvo motos y tres ruedas), remolques y semirremolques")],
            [T("<b>Switches on only with</b>", "<b>Solo se enciende con</b>"), T("the <b>position lights</b> on; alone or with dipped or even main beam (not advisable: glare)", "la <b>luz de posición</b> encendida; sola o con la de cruce o incluso la de carretera (no aconsejable: deslumbra)"),
             T("the <b>dipped, main or front fog</b> lights on", "la luz de <b>cruce, carretera o antiniebla delantera</b> encendida")],
            [T("<b>Dashboard light</b>", "<b>Testigo</b>"), T("Green (optional)", "Verde (opcional)"), T("<b>Amber</b>, not flashing (compulsory)", "<b>Amarillo auto</b>, no intermitente (obligatorio)")],
        ],
        widths=["20%", "40%", "40%"],
        cls="small",
    ))
    B.append(FIG(fog_matrix, "Front fog lights may be used in bad weather and on narrow winding roads; the rear one must be used only when conditions are especially bad.",
                 "La antiniebla delantera se puede usar con meteorología adversa y en vías estrechas con curvas; la trasera se debe usar solo con condiciones especialmente adversas."))
    B.append(TABLE(
        [T("", ""), T("Front fog lights: you <b>may</b> use them", "Delantera: se <b>puede</b> usar"), T("Rear fog light: you <b>must</b> use it", "Trasera: se <b>debe</b> usar")],
        [
            [T("<b>Weather</b>", "<b>Meteorología</b>"), T("Fog, <b>heavy</b> rain, snowfall, clouds of dust or smoke", "Niebla, lluvia <b>intensa</b>, nevada, nubes de polvo o humo"),
             T("<b>Thick</b> fog, <b>very heavy</b> rain, <b>heavy</b> snowfall, <b>dense</b> dust or smoke", "Niebla <b>espesa</b>, lluvia <b>muy intensa</b>, nevada <b>fuerte</b>, nubes <b>densas</b> de polvo o humo")],
            [T("<b>Narrow road</b>", "<b>Vía estrecha</b>"), T("Carriageway <b>6.50 m wide or less</b> with the “dangerous bends” warning sign", "Calzada de <b>6,50 m o menos</b> con la señal de «curvas peligrosas»"),
             T("<b>No</b>", "<b>No</b>")],
        ],
        widths=["18%", "41%", "41%"],
        cls="small",
    ))
    B.append(BOX("key", "Poor visibility because of the weather", "Visibilidad reducida por la meteorología", [
        ("<b>By day</b>: at least the <b>position lights</b> plus <b>any</b> lighting light (fog, dipped or main).",
         "<b>De día</b>: al menos la <b>luz de posición</b> con <b>cualquier</b> luz de alumbrado (antiniebla, cruce o carretera)."),
        ("<b>By night</b>: at least <b>position and dipped beam</b>; the others (fog or main) may be added.",
         "<b>De noche</b>: al menos <b>posición y cruce</b>, pudiendo usar las demás (antiniebla o carretera)."),
    ]))
    B.append(H3("3.4 Lanes where lights are always on", "3.4 Situaciones especiales"))
    B.append(P(
        "At least the <b>dipped beam</b>, <b>by day and by night</b>, on a <b>reversible lane</b>, on roads with a <b>temporary additional lane</b>, and on a <b>contraflow lane</b> and the <b>normal-direction lane next to it</b>. "
        "Between sunset and sunrise, or when visibility is poor, <b>cyclists on interurban roads</b> also use at least one <b>luminous or reflective element</b> visible from <b>150 m</b>.",
        "Al menos la <b>luz de cruce</b>, <b>de día y de noche</b>, por un <b>carril reversible</b>, por vías con <b>carril adicional circunstancial</b>, y por un <b>carril habilitado en sentido contrario</b> y el <b>carril del sentido normal contiguo</b>. "
        "Entre el ocaso y la salida del sol, o con poca visibilidad, los <b>ciclistas en vías interurbanas</b> usan además al menos un <b>elemento luminoso o reflectante</b> visible a <b>150 m</b>."))
    B.append(H3("3.5 Dazzle", "3.5 Deslumbramientos"))
    B.append(P("When the eyes get more light than they can take, a <b>temporary blindness</b> follows: dazzle (<i>deslumbramiento</i>).",
               "Cuando los ojos reciben más luz de la que pueden soportar se produce una <b>ceguera temporal</b>: el deslumbramiento."))
    B.append(E(
        "Not dazzling others", "Cómo evitar deslumbrar",
        "Switch from main to <b>dipped</b> as soon as you could dazzle <b>anyone</b>: above all <b>oncoming drivers</b> (<b>even if they do not dip</b>) and drivers <b>ahead</b> through their <b>mirrors</b>. "
        "Do not switch back until you are sure nobody can be dazzled. Keep your <b>headlights aimed</b> and the <b>load well placed</b>, or even the dipped beam can dazzle.",
        "Hay que cambiar la luz de carretera por la de <b>cruce</b> en cuanto se pueda deslumbrar a <b>cualquier usuario</b>: sobre todo a los que vienen <b>de frente</b> (<b>aunque ellos no lo hagan</b>) y a los que van <b>delante</b> por sus <b>retrovisores</b>. "
        "No se vuelve a conectar hasta estar seguro de no deslumbrar. Hay que llevar los <b>faros bien reglados</b> y la <b>carga bien colocada</b>; si no, se puede deslumbrar incluso con la de cruce."))
    B.append(FIG(overtake_dazzle, "Overtaking at night: the overtaking driver waits until level before switching to main beam; at that moment the overtaken driver dips.",
                 "Adelantar de noche: el que adelanta espera a estar en paralelo para poner la luz larga; en ese momento el adelantado pone la de cruce."))
    B.append(FIG(curve_dazzle, "On a bend, the driver whose road turns right is the first to dip.",
                 "En una curva, el primero en cambiar a la luz de cruce es el que la toma hacia la derecha."))
    B.append(FIG(dazzled_view, "Reducing the chance of being dazzled, and what to do if it happens.",
                 "Cómo reducir la posibilidad de ser deslumbrado y qué hacer si ocurre."))
    B.append(BOX("trap", "If you are dazzled", "Si te deslumbran", [
        ("<b>Slow down</b> as much as needed, <b>even to a stop</b>.", "<b>Reduce la velocidad</b> todo lo necesario, <b>incluso hasta detenerte</b>."),
        ("<b>Keep your position</b> on the carriageway: do <b>not</b> move onto the shoulder, where you could leave the road or hit someone walking or cycling there.",
         "<b>Sin variar la posición</b> en la calzada: <b>no</b> salgas al arcén, donde podrías salirte de la vía o encontrar a usuarios que circulan por él."),
    ]))

    # ---------------------------------------------------------------- 4. warning
    B.append(H2("4", "Lights that warn others", "Avisar a los demás usuarios"))
    B.append(FIG(rear_lights, "The back of a car carries lights for every job: being seen, warning and, for the reversing light, lighting the road behind.",
                 "La parte trasera de un turismo reúne luces de todas las funciones: ser visto, avisar y, en el caso de la marcha atrás, alumbrar detrás."))
    B.append(E(
        "Indicators (<i>intermitentes</i>)", "Intermitentes (indicadores de dirección)",
        "Tell others you intend to make <b>any manoeuvre involving a sideways move</b>. <b>Amber</b>; <b>compulsory</b> on motor vehicles, trailers and semitrailers.",
        "Indican la intención de realizar <b>cualquier maniobra que implique un desplazamiento lateral</b>. <b>Amarillo auto</b>; <b>obligatorios</b> en vehículos de motor, remolques y semirremolques."))
    B.append(E(
        "Hazard warning lights (<i>luz o señal de emergencia</i>)", "Luz o señal de emergencia",
        "<b>All indicators flashing together</b>, to warn of the danger the vehicle poses, stopped or moving, because of an emergency. <b>Compulsory</b> on all automobiles; <b>optional</b> on motorcycles. "
        "Its switch has a <b>flashing red</b> dashboard light.",
        "<b>Funcionamiento simultáneo de todos los intermitentes</b>, para advertir del peligro que supone el vehículo, inmovilizado o en movimiento, por una emergencia. <b>Obligatoria</b> en todos los automóviles; <b>opcional</b> en motocicletas. "
        "Se acciona con un testigo <b>rojo intermitente</b> en el salpicadero."))
    B.append(TABLE(
        [T("Use the hazard lights…", "Se usa la luz de emergencia…")],
        [
            [T("When <b>immobilised</b> on an <b>autopista or autovía</b>, or where visibility is much reduced; and in a <b>tunnel</b> or underpass, in an emergency or held up by traffic.",
               "En las <b>inmovilizaciones</b> en <b>autopista o autovía</b>, o en lugares o circunstancias de visibilidad muy reducida; y en un <b>túnel</b> o paso inferior por emergencia o por necesidades de la circulación.")],
            [T("When the vehicle <b>cannot reach the minimum speed</b> and could be hit from behind.", "Cuando el vehículo <b>no pueda alcanzar la velocidad mínima</b> y haya peligro de alcance.")],
            [T("In any <b>momentary emergency</b>, stopped or moving (breakdown, accident…), on the carriageway, shoulder or median.",
               "En cualquier <b>situación momentánea de emergencia</b>, detenido o en movimiento (avería, accidente…), en la calzada, el arcén o la mediana.")],
            [T("While passengers get on or off a stopped <b>school or minors’ transport</b> vehicle.", "Mientras suben o bajan viajeros en las paradas de vehículos de <b>transporte escolar o de menores</b>.")],
            [T("On an <b>emergency trip</b> in a non-priority vehicle.", "En los <b>servicios de urgencia</b> con vehículos no prioritarios.")],
        ],
    ))
    B.append(BOX("trap", "Hazard lights are not…", "La luz de emergencia no…", [
        ("…a replacement for the <b>V-16</b> warning light.", "…sustituye a la señal <b>V-16</b>."),
        ("…an excuse for <b>double parking</b>: that is not an emergency.", "…sirve para indicar que se está parado en <b>doble fila</b>: no es una emergencia."),
    ]))
    B.append(E(
        "Brake lights (<i>luz de frenado</i>)", "Luz de frenado",
        "Show those behind that the <b>service brake</b> (foot brake) is being used. Most cars have a <b>third brake light</b>, higher up, to reinforce it. "
        "Use them <b>repeatedly</b>, when possible, to warn that you are going to <b>stop or brake hard</b>.",
        "Indica a los de detrás que se está usando el <b>freno de servicio</b> (freno de pie). La mayoría de turismos llevan una <b>tercera luz de freno</b> más elevada para reforzarla. "
        "Se usa de <b>forma reiterada</b>, siempre que sea posible, para advertir la intención de <b>inmovilizar el vehículo o frenar considerablemente</b>."))
    B.append(E(
        "Reversing light (<i>luz de marcha atrás</i>)", "Luz de marcha atrás",
        "<b>White</b>. Lights the road behind and warns that the vehicle is reversing or about to. It comes on <b>by itself</b> when reverse is selected with the ignition on, <b>even with the engine off</b>. "
        "<b>Compulsory</b> on automobiles (except motorcycles); <b>optional</b> on trailers and semitrailers.",
        "<b>Blanca</b>. Alumbra la vía por detrás y avisa de que el vehículo va o está a punto de ir marcha atrás. Se enciende <b>automáticamente</b> al poner la marcha atrás con el contacto conectado, <b>aun con el motor parado</b>. "
        "<b>Obligatoria</b> en automóviles (salvo motocicletas); <b>opcional</b> en remolques y semirremolques."))

    # ---------------------------------------------------------------- 5. other lights
    B.append(H2("5", "Other lights", "Otras luces"))
    B.append(TABLE(
        [T("Light", "Luz"), T("Rule", "Norma")],
        [
            [T("<b>Interior lighting</b>", "<b>Alumbrado interior</b>"), T("Compulsory in <b>public passenger</b> vehicles and <b>hire cars with driver</b>, without dazzling or bothering other road users.",
                                                                           "Obligatorio en vehículos de <b>servicio público de viajeros</b> y de <b>alquiler con conductor</b>, sin deslumbrar ni molestar a los demás usuarios.")],
            [T("<b>Number-plate lights</b>", "<b>Luces de las placas</b>"), T("The <b>rear number-plate</b> light (and the <b>SP</b> plate light, if any) comes on <b>automatically</b> with the position lights.",
                                                                            "La luz de la <b>placa de matrícula trasera</b> (y la de la placa <b>SP</b>, en su caso) se enciende <b>automáticamente</b> con las de posición.")],
        ],
        widths=["26%", "74%"],
    ))

    # ---------------------------------------------------------------- 6. traps
    B.append(H2("6", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("Insufficient lighting: number plate at <b>10 m</b>, dark car at <b>50 m</b>.", "Iluminación insuficiente: matrícula a <b>10 m</b>, vehículo oscuro a <b>50 m</b>."),
        ("In town at night: <b>dipped beam</b>, however bright the street. <b>Main beam is forbidden in town.</b>", "En poblado de noche: <b>luz de cruce</b>, aunque la calle esté muy iluminada. <b>La luz larga está prohibida en poblado.</b>"),
        ("Main beam is <b>compulsory</b> above <b>40 km/h</b> on dark interurban roads; at 40 km/h or less you choose.", "La luz larga es <b>obligatoria</b> a <b>más de 40 km/h</b> en interurbanas oscuras; a 40 km/h o menos, a elección."),
        ("Motorcycles: <b>dipped beam day and night</b>.", "Motocicletas: <b>luz de cruce de día y de noche</b>."),
        ("Parking light: optional only up to <b>6 m long and 2 m wide</b>; replaces position lights only in a <b>poorly lit travesía</b>.",
         "Luz de estacionamiento: opcional solo hasta <b>6 m de largo y 2 m de ancho</b>; sustituye a la de posición solo en <b>travesía mal iluminada</b>."),
        ("<b>Triangular</b> reflectors: <b>only</b> on the back of trailers and semitrailers.", "Catadióptricos <b>triangulares</b>: <b>solo</b> detrás de remolques y semirremolques."),
        ("Clearance lights: compulsory over <b>2.10 m</b> wide, optional from <b>1.80 m</b>.", "Gálibo: obligatoria a más de <b>2,10 m</b> de ancho, opcional desde <b>1,80 m</b>."),
        ("Front fog: <b>optional</b> to fit, you <b>may</b> use it. Rear fog: <b>compulsory</b> to fit, you <b>must</b> use it only in <b>especially</b> bad conditions.",
         "Antiniebla delantera: <b>opcional</b>, se <b>puede</b> usar. Trasera: <b>obligatoria</b>, se <b>debe</b> usar solo con condiciones <b>especialmente</b> adversas."),
        ("Narrow winding road (≤ 6.50 m with “dangerous bends”): front fog yes, <b>rear fog no</b>.", "Vía estrecha con curvas (≤ 6,50 m con «curvas peligrosas»): antiniebla delantera sí, <b>trasera no</b>."),
        ("Rear fog light dashboard tell-tale: <b>amber</b> (compulsory); front: green (optional); hazard: flashing red.",
         "Testigo de antiniebla trasera: <b>amarillo auto</b> (obligatorio); delantera: verde (opcional); emergencia: rojo intermitente."),
        ("Overtaking at night: switch to main beam only when <b>level</b>; the overtaken car dips <b>then</b>.", "Adelantar de noche: luz larga solo al estar <b>en paralelo</b>; el adelantado pone la de cruce <b>en ese momento</b>."),
        ("Dazzled: slow down, even stop, <b>without</b> moving onto the shoulder; look <b>right</b>, close the <b>left</b> eye.",
         "Deslumbrado: reducir, incluso parar, <b>sin</b> salir al arcén; mirar a la <b>derecha</b>, cerrar el ojo <b>izquierdo</b>."),
        ("Hazard lights do <b>not</b> replace the V-16 and do <b>not</b> justify double parking.", "La luz de emergencia <b>no</b> sustituye a la V-16 ni justifica parar en <b>doble fila</b>."),
        ("Reversing light comes on with the ignition on, <b>even with the engine off</b>.", "La luz de marcha atrás se enciende con el contacto, <b>aun con el motor parado</b>."),
    ]))

    # ---------------------------------------------------------------- 7. key numbers
    B.append(H2("7", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Insufficiently lit road", "Vía insuficientemente iluminada"), T("no plate readable at 10 m / dark car not seen at 50 m", "no se lee una matrícula a 10 m / no se ve un vehículo oscuro a 50 m")],
            [T("Trailer front position lights compulsory", "Posición delantera obligatoria en remolques"), T("wider than 1.60 m", "más de 1,60 m de ancho")],
            [T("Trailer side position lights", "Posición lateral en remolques"), T("at least 2 if longer than 6 m", "al menos 2 si miden más de 6 m")],
            [T("Parking light allowed", "Luz de estacionamiento permitida"), T("≤ 6 m long and ≤ 2 m wide", "≤ 6 m de largo y ≤ 2 m de ancho")],
            [T("Clearance lights", "Luz de gálibo"), T("compulsory &gt; 2.10 m wide; optional 1.80–2.10 m", "obligatoria &gt; 2,10 m; opcional 1,80–2,10 m")],
            [T("Main beam compulsory (dark roads)", "Luz larga obligatoria (vías oscuras)"), T("above 40 km/h", "a más de 40 km/h")],
            [T("Main beams on cars", "Luces de carretera en automóviles"), T("an even number", "un número par")],
            [T("Narrow road for front fog lights", "Vía estrecha para la antiniebla delantera"), T("carriageway ≤ 6.50 m + “dangerous bends” sign", "calzada ≤ 6,50 m + señal «curvas peligrosas»")],
            [T("Rear fog lights", "Antiniebla trasera"), T("1 or 2, red", "1 o 2, rojas")],
            [T("Cyclist’s luminous or reflective element (interurban, lights compulsory)", "Elemento luminoso o reflectante del ciclista (interurbana, alumbrado obligatorio)"), T("visible from 150 m", "visible a 150 m")],
        ],
        widths=["50%", "50%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["pu2", "ps3", "pk1", "rf2", "gb1", "dp2", "mb3", "fg3", "sp1", "dz3", "hz2", "br3"]


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
    ("Reglamento General de Circulación (RD 1428/2003), lighting rules (arts. 98–113) — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Reglamento General de Vehículos (RD 2822/1998), Anexo X: lights and reflectors — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-1999-1826"),
    ("Ley sobre Tráfico, Circulación de Vehículos a Motor y Seguridad Vial (RDL 6/2015)", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722"),
]

GLOSSARY = [
    ("alumbrado · dispositivo luminoso", "lighting · light"),
    ("entre el ocaso y la salida del sol", "between sunset and sunrise"),
    ("vía insuficientemente iluminada", "poorly lit road"),
    ("luz de posición", "position light (sidelight)"),
    ("luz de estacionamiento", "parking light"),
    ("catadióptrico · retrocatadióptrico", "reflector · retroreflector"),
    ("luz de gálibo", "clearance (end-outline marker) light"),
    ("luz de corto alcance o de cruce", "dipped beam (low beam)"),
    ("luz de largo alcance o de carretera", "main beam (high beam)"),
    ("luz antiniebla delantera / trasera", "front / rear fog light"),
    ("amarillo selectivo · amarillo auto", "selective yellow · amber"),
    ("testigo", "dashboard tell-tale"),
    ("deslumbramiento · deslumbrar", "dazzle · to dazzle"),
    ("faros reglados", "properly aimed headlights"),
    ("intermitente · indicador de dirección", "indicator (turn signal)"),
    ("luz o señal de emergencia", "hazard warning lights"),
    ("luz de frenado · tercera luz de freno", "brake light · third (high-level) brake light"),
    ("freno de servicio", "service (foot) brake"),
    ("luz de marcha atrás", "reversing light"),
    ("alumbrado interior del habitáculo", "interior light"),
    ("luz de la placa de matrícula", "number-plate light"),
    ("elemento luminoso o reflectante", "luminous or reflective element"),
    ("carril reversible · adicional circunstancial", "reversible lane · temporary additional lane"),
]
