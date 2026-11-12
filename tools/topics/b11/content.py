# -*- coding: utf-8 -*-
"""Topic 11 content (first aid), bilingual. Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Tema 11: Primeros auxilios). The wording and the figures are
original. The legal duties come from the Ley sobre Tráfico (RDL 6/2015, art. 51), the Reglamento General de Circulación
(RD 1428/2003, art. 129) and the Código Penal (arts. 195 and 382 bis), as they stand in November 2026. Where the course's
first-aid figures differ from the current European Resuscitation Council guidelines, the page keeps the course's
answer for the exam and notes the difference.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import pas_rule, call_112, protect_scene, triage_flow, airway, recovery_position, cpr, bleeding, shock


def rows(pairs):
    """[(en, es), ...] -> one-column table rows."""
    return [[T(a, b)] for a, b in pairs]


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("What the law asks of you at an accident (help, or call for help, and don’t leave the scene) and what to do, in order: the <b>PAS</b> rule — <b>protect, alert, help</b> — "
         "then <b>assess</b> the injured (conscious? breathing?) and treat them.",
         "Lo que te exige la ley en un accidente (auxiliar o pedir auxilio, y no marcharte) y qué hacer, en orden: la regla <b>PAS</b> —<b>proteger, avisar, socorrer</b>— "
         "y después <b>valorar</b> a los heridos (¿consciente?, ¿respira?) y actuar."),
        ("The exam loves <b>numbers and orders</b>: 112, <b>10–15 seconds</b> per injured person, check breathing every <b>2–3 minutes</b>, CPR <b>30 : 2</b>, children <b>5</b> breaths first, the <b>golden hour</b>, "
         "<b>30 minutes</b> before taking someone in your own car.",
         "El examen pregunta sobre todo <b>cifras y órdenes</b>: 112, <b>10–15 segundos</b> por herido, comprobar la respiración cada <b>2–3 minutos</b>, RCP <b>30 : 2</b>, niños <b>5</b> ventilaciones iniciales, la <b>hora de oro</b>, "
         "<b>30 minutos</b> antes de llevar a alguien en tu coche."),
        ("Your course’s CPR depth and its advice on bleeding are older than the current European guidelines. The page keeps the course’s answer for the exam and notes the difference.",
         "La profundidad de la RCP y los consejos sobre hemorragias de tu curso son anteriores a las guías europeas actuales. La página mantiene la respuesta del curso para el examen e indica la diferencia."),
        ("The sections follow the order of your course’s Topic 11. Spanish exam terms are in <i>italics</i> in the English text, and a glossary closes the topic.",
         "Los apartados siguen el orden del Tema 11 de tu curso. Al final hay un glosario español–inglés."),
    ]))

    # ---------------------------------------------------------------- 1. duty
    B.append(H2("1", "The duty to help others", "Deber de ayudar a los demás"))
    B.append(P(
        "Road users who are <b>involved</b> in an accident, or who <b>know about it</b> even if they are not involved, must:",
        "Los usuarios de la vía <b>implicados</b> en un accidente, o que <b>tengan conocimiento</b> de él aunque no estén implicados, están obligados a:"))
    B.append(TABLE(
        [T("Duty", "Obligación"), T("What it means", "Qué supone")],
        [
            [T("<b>Help, or call for help</b>", "<b>Auxiliar o solicitar auxilio</b>"),
             T("Look after the victims. Not helping is a <b>crime</b> in the Código Penal: <b>failure to help</b> (<i>omisión del deber de socorro</i>).",
               "Atender a las víctimas. No prestar auxilio es un <b>delito</b> del Código Penal: <b>omisión del deber de socorro</b>.")],
            [T("<b>Avoid further danger</b> and <b>work with the authorities</b>", "<b>Evitar peligros</b> y <b>colaborar con la Autoridad</b>"),
             T("Restore road safety as far as possible and help clarify what happened. If agents ask: show your <b>personal and vehicle documents</b>, explain <b>how it happened</b> and, if you are involved, "
               "take the <b>alcohol and drug tests</b>.",
               "Restablecer en lo posible la seguridad de la circulación y esclarecer los hechos. Si lo requieren los agentes: facilitar la <b>documentación personal y del vehículo</b>, explicar <b>cómo se produjo</b> y, si estás implicado, "
               "someterte a las <b>pruebas de alcohol y drogas</b>.")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(P(
        "Users who are <b>not involved</b> need not do this when the <b>authorities or their agents are already there</b>, or when their help is <b>clearly not needed</b>. If it isn’t needed, <b>keep driving</b>.",
        "Los usuarios <b>no implicados</b> no están obligados cuando ya se haya <b>personado la Autoridad o sus agentes</b>, o cuando claramente <b>no sea necesaria</b> su colaboración. Si no hace falta, hay que <b>continuar la marcha</b>."))
    B.append(BOX("trap", "If someone is dead or seriously injured…", "En caso de muertos o heridos graves…", [
        ("<b>Don’t change the state of things</b>, the marks or other <b>evidence</b> that can show who was responsible — unless leaving them would endanger the injured or the traffic.",
         "<b>Evitar la modificación del estado de las cosas</b>, de las huellas u otras <b>pruebas</b> útiles para determinar la responsabilidad, salvo que de no hacerlo se perjudique la seguridad de los heridos o de la circulación."),
        ("<b>Call the agents</b> and <b>stay at the scene</b>.", "<b>Avisar a los agentes</b> y <b>permanecer en el lugar</b> del accidente."),
    ]))
    B.append(TABLE(
        [T("Crime (Código Penal)", "Delito (Código Penal)"), T("Who", "Quién"), T("Penalty", "Pena")],
        [
            [T("<b>Failure to help</b> (art. 195)", "<b>Omisión del deber de socorro</b> (art. 195)"),
             T("Anyone who doesn’t help a person helpless and in serious danger when they could do it without risk — or who can’t help and doesn’t urgently call for it.",
               "Quien no socorra a una persona desamparada y en peligro manifiesto y grave pudiendo hacerlo sin riesgo, o quien, impedido de socorrer, no pida auxilio con urgencia."),
             T("Fine of 3–12 months. If <b>you caused</b> the accident: prison of <b>6–18 months</b> (by chance) or <b>6 months–4 years</b> (by negligence).",
               "Multa de 3 a 12 meses. Si <b>lo causaste tú</b>: prisión de <b>6 a 18 meses</b> (fortuito) o de <b>6 meses a 4 años</b> (imprudencia).")],
            [T("<b>Leaving the scene</b> (art. 382 bis)", "<b>Abandono del lugar del accidente</b> (art. 382 bis)"),
             T("A driver who, <b>without risk</b> to themselves or others, deliberately leaves after <b>causing</b> an accident in which someone died or was seriously injured.",
               "El conductor que, <b>sin riesgo</b> propio o de terceros, abandona voluntariamente el lugar tras <b>causar</b> un accidente con fallecidos o heridos graves."),
             T("Negligent: prison <b>6 months–4 years</b> and a <b>1–4-year</b> driving ban. By chance: <b>3–6 months</b> and a <b>6-month to 2-year</b> ban.",
               "Imprudente: prisión de <b>6 meses a 4 años</b> y privación del permiso de <b>1 a 4 años</b>. Fortuito: <b>3 a 6 meses</b> y privación de <b>6 meses a 2 años</b>.")],
        ],
        widths=["24%", "40%", "36%"],
        cls="small",
    ))
    B.append(H3("1.1 Giving your details to those involved", "1.1 Facilitar datos a implicados"))
    B.append(P(
        "If you must help, give your <b>identity</b> (name, ID number…) and your <b>vehicle’s</b> (number plate…) to the people involved who ask for them. If there is only <b>minor damage</b>, the sensible thing is to "
        "<b>agree between you</b> and tell the insurers as soon as possible, filling in the <b>accident report form</b> (<i>parte amistoso</i>) somewhere safe, <b>off the road</b>. "
        "By law you have <b>7 days</b> to report it to your insurer (Topic 9).",
        "Si estás obligado a prestar ayuda, debes comunicar tu <b>identidad</b> (nombre, DNI…) y la del <b>vehículo</b> (matrícula…) a los implicados que lo soliciten. Si solo hay <b>pequeños daños materiales</b>, lo acertado es "
        "<b>llegar a un acuerdo</b> y comunicarlo a las aseguradoras cuanto antes, con el <b>parte amistoso</b> cumplimentado en un lugar seguro, <b>fuera de la vía</b>. "
        "La ley da <b>7 días</b> para comunicarlo a tu aseguradora (Tema 9)."))

    # ---------------------------------------------------------------- 2. PAS
    B.append(H2("2", "What to do at an accident: the PAS rule", "Comportamiento en caso de accidente (PAS)"))
    B.append(P("At an accident, apply the basic <b>PAS</b> rule, in this order: <b>Protect</b> (<i>proteger</i>), <b>Alert</b> (<i>avisar</i>), <b>Help</b> (<i>socorrer</i>).",
               "Cuando sucede un accidente hay que aplicar la <b>regla básica PAS</b>, en este orden: <b>Proteger</b>, <b>Avisar</b>, <b>Socorrer</b>."))
    B.append(FIG(pas_rule, "Protect first, so there are no new victims; then alert 112; then help, only as far as you know how.",
                 "Primero proteger, para que no haya nuevas víctimas; después avisar al 112; después socorrer, solo en la medida en que sepas hacerlo."))

    B.append(H3("2.1 Protect", "2.1 Proteger"))
    B.append(TABLE(
        [T("In this order", "En este orden"), T("What to do", "Qué hacer")],
        [
            [T("<b>1. Protect yourself</b>", "<b>1. Autoprotegerse</b>"),
             T("<b>Stop somewhere safe</b> without blocking traffic (off the carriageway if possible), following the rules. Signal your vehicle with the <b>V-16 warning light</b> <b>before getting out</b> — window down, placed on the roof by hand — "
               "and use the <b>hazard lights</b>. Put the <b>reflective vest</b> on <b>before getting out</b>, even where it isn’t compulsory. <b>Avoid walking on the carriageway</b>.",
               "<b>Detener el vehículo en un lugar seguro</b>, sin obstaculizar (preferiblemente fuera de la calzada) y cumpliendo las normas. Señalizarlo con el <b>dispositivo luminoso V-16</b> <b>antes de salir</b>, bajando la ventanilla y colocándolo con la mano sobre el techo, "
               "y usar las <b>luces de emergencia</b>. Ponerse el <b>chaleco reflectante antes de salir</b>, aunque no sea obligatorio en esa vía. <b>Evitar circular por la calzada</b>.")],
            [T("<b>2. Protect the scene</b>", "<b>2. Proteger el lugar del accidente</b>"),
             T("Move vehicles or load <b>off the carriageway</b> (shoulder or central reservation) if they block traffic; <b>handbrake on, engine off</b>. Look for other risks: <b>no smoking</b>; "
               "in a fire, use an <b>extinguisher at the base of the flames</b> or, failing that, sand or blankets — <b>never water</b>.",
               "Colocar los vehículos o la carga <b>fuera de la calzada</b> (arcén o mediana) si son un obstáculo; <b>freno de mano y motor parado</b>. Evaluar otros riesgos: <b>no fumar</b>; "
               "en caso de incendio, <b>extintor directamente sobre la base de las llamas</b> o, en su defecto, arena o mantas, <b>nunca agua</b>.")],
            [T("<b>3. Protect the victims</b>", "<b>3. Proteger a las víctimas</b>"),
             T("<b>Don’t move the injured</b> unless it is essential because of a danger — and then keep the <b>head–neck–trunk line</b> still first. <b>Don’t remove a helmet</b> unless it is essential and you know how (at least <b>two people</b>).",
               "<b>No mover a los heridos</b> salvo que sea imprescindible por existir un peligro, e inmovilizando antes el <b>eje cuello-cabeza-tronco</b>. <b>No quitar el casco</b> salvo que sea imprescindible y se sepa hacerlo (mínimo <b>dos personas</b>).")],
        ],
        widths=["24%", "76%"],
    ))
    B.append(FIG(protect_scene, "Your car off the carriageway with the V-16 on the roof; you in the vest, off the road; the damaged vehicles off the carriageway too.",
                 "Tu coche fuera de la calzada con la V-16 en el techo; tú, con chaleco y fuera de la calzada; los vehículos accidentados, también fuera."))

    B.append(H3("2.2 Alert", "2.2 Avisar o alertar"))
    B.append(P(
        "Call the emergency services on <b>112</b>: <b>free</b>, it works <b>even without credit</b>, it is the <b>same number in the whole EU</b>, and they answer in the caller’s language.",
        "Contactar con los servicios de emergencia en el <b>112</b>: es <b>gratuito</b>, se puede llamar <b>incluso sin saldo</b>, es <b>común en toda la Unión Europea</b> y atienden en el idioma de quien llama."))
    B.append(FIG(call_112, "Four things to tell 112: where, who is hurt, what happened and who you are.",
                 "Cuatro cosas que decir al 112: dónde, quién está herido, qué ha pasado y quién eres."))
    B.append(BOX("trap", "When you need not alert or stay", "Cuándo no es necesario avisar ni permanecer", [
        ("Only when <b>all three</b> are true: the injuries are <b>clearly minor</b>, road safety has been <b>restored</b>, and <b>none of the people involved asks</b> you to.",
         "Solo cuando se cumplen <b>las tres</b>: heridas <b>claramente leves</b>, la seguridad de la circulación está <b>restablecida</b> y <b>ninguna de las personas implicadas lo solicita</b>."),
    ]))

    B.append(H3("2.3 Help", "2.3 Socorrer"))
    B.append(P(
        "Be honest about <b>whether you know what to do</b>: the wrong help can make things worse. If you are not sure, <b>wait for the medical team</b>. To help, you must:",
        "Hay que <b>ser conscientes de si sabemos cómo actuar</b>: una ayuda inadecuada puede empeorar el resultado. Si no estás seguro, <b>espera a la ayuda sanitaria</b>. Para actuar, debes:"))
    B.append(TABLE(
        [T("Rules for helping", "Normas para socorrer")],
        rows([
            ("<b>Keep calm</b> and don’t rush. Decide the <b>order by seriousness</b>: unconscious victims and breathing problems first.", "<b>Mantener la calma</b> y no precipitarse. Establecer un <b>orden según la gravedad</b>: inconscientes y dificultades respiratorias primero."),
            ("Treat the injured <b>inside the vehicle</b> if needed, so as <b>not to move them</b> unless essential because of a danger (especially the unconscious), keeping the <b>head–neck–trunk line</b> still.",
             "Atender a los heridos <b>dentro del vehículo</b> si es necesario, para <b>no moverlos</b> salvo que sea imprescindible por un peligro (sobre todo inconscientes), manteniendo inmóvil el <b>eje cuello-cabeza-tronco</b>."),
            ("<b>Loosen clothing</b> that presses on the <b>neck and airway</b>. <b>Cover</b> the injured so they don’t lose body heat — <b>even in summer</b>.", "<b>Aflojar las prendas</b> que opriman el <b>cuello y las vías respiratorias</b>. <b>Tapar</b> a los heridos para que no pierdan temperatura, <b>incluso en verano</b>."),
            ("<b>Never give food, drink or medicines.</b> <b>Don’t touch wounds or burns</b> or put creams on them.", "<b>Nunca darles bebida, alimento ni medicamentos.</b> <b>No tocar las heridas o quemaduras</b> ni aplicar pomadas."),
            ("<b>Don’t remove a helmet</b> unless essential and you know how (at least two people). <b>Stay with the victims</b> to calm them.", "<b>No quitar el casco</b> salvo que sea imprescindible y se conozca la técnica (mínimo dos personas). <b>Acompañar a las víctimas</b> para transmitir tranquilidad."),
        ]),
    ))
    B.append(BOX("key", "The golden hour", "La hora de oro", [
        ("The <b>hour right after an accident</b> (<i>hora dorada</i>), when <b>most deaths happen</b>. What is done in that time is crucial.", "Es la <b>hora inmediatamente posterior a un accidente</b>, cuando se produce el <b>mayor porcentaje de fallecidos</b>. La actuación en ese tiempo es fundamental."),
    ]))

    # ---------------------------------------------------------------- 3. initial assessment
    B.append(H2("3", "Initial assessment of the injured", "Valoración inicial de los heridos"))
    B.append(P(
        "Before helping, <b>assess how serious</b> each person is: a first (primary) assessment of the <b>vital signs</b> — <b>consciousness, breathing and circulation</b>.",
        "Antes de socorrer hay que <b>valorar la gravedad</b>: una evaluación inicial o primaria de los <b>signos vitales</b>, comprobando la <b>consciencia, la respiración y la circulación</b>."))
    B.append(BOX("trap", "More than one injured person", "Más de un herido", [
        ("Assess <b>all of them</b> before helping <b>any</b>, spending <b>10–15 seconds</b> on each.", "Valorar el estado de <b>todos</b> antes de socorrer a <b>ninguno</b>, dedicando <b>10–15 segundos</b> a cada herido."),
    ]))
    B.append(TABLE(
        [T("State", "Estado"), T("How you know", "Cómo se sabe"), T("What next", "Qué hacer")],
        [
            [T("<b>Conscious</b>", "<b>Consciente</b>"), T("Answers <b>simple questions</b> asked loudly, or reacts to <b>pain</b> (a pinch on the back of the hand).", "<b>Contesta a preguntas sencillas</b> en tono alto o <b>responde a estímulos dolorosos</b> (un pellizco en el dorso de la mano)."),
             T("Check they <b>breathe</b> and have <b>no bleeding</b> or serious wounds; go on to the next, but keep an eye on them (still, covered).", "Comprobar que <b>respira</b> y <b>no tiene hemorragias</b> ni heridas graves; pasar al siguiente, vigilándolo (que no se mueva, tapado).")],
            [T("<b>Unconscious</b>", "<b>Inconsciente</b>"), T("<b>Doesn’t respond</b> to anything.", "<b>No responde a los estímulos</b>."), T("Apply the <b>ABC rule</b>.", "Aplicar la <b>regla ABC</b>.")],
        ],
        widths=["18%", "44%", "38%"],
    ))
    B.append(FIG(triage_flow, "Does the person respond? If not, open the airway and check the breathing: breathing → recovery position; not breathing → CPR.",
                 "¿Responde? Si no, abre la vía aérea y comprueba la respiración: si respira, posición lateral de seguridad; si no respira, RCP."))
    B.append(H3("3.1 The ABC rule (airway, breathing, circulation)", "3.1 Regla ABC (aérea, boca y circulación)"))
    B.append(FIG(airway, "The head-tilt, chin-lift opens the airway; then see, feel and hear whether the person breathes.",
                 "La maniobra frente-mentón abre la vía aérea; después ver, sentir y oír si respira."))
    B.append(TABLE(
        [T("Step", "Paso"), T("What to do", "Qué hacer")],
        [
            [T("<b>A — Airway</b> (<i>vía aérea</i>)", "<b>A — Vía aérea</b>"),
             T("1. Check for anything <b>blocking the airway</b> that could choke them (the <b>tongue falling back</b>, a sweet, gum…). 2. Open the airway with the <b>head-tilt, chin-lift</b> (<i>maniobra frente-mentón</i>): "
               "one hand on the <b>forehead</b> pushing back, the other <b>lifting the chin</b>; if needed, remove the object with a <b>hooked index finger</b> or put the tongue back in place.",
               "1. Comprobar si hay <b>objetos que impidan respirar</b> y puedan asfixiarle (<b>caída de la lengua</b>, caramelo, chicle…). 2. Abrir las vías respiratorias con la <b>maniobra frente-mentón</b>: "
               "una mano <b>sujeta la frente</b> y empuja hacia atrás, la otra <b>eleva el mentón</b>; si hace falta, con el <b>dedo índice doblado en gancho</b> se saca el cuerpo extraño o se coloca bien la lengua.")],
            [T("<b>B — Breathing</b> (<i>boca</i>)", "<b>B — Boca</b>"),
             T("Check whether and how the person breathes: <b>SEE</b> the chest or belly move, <b>FEEL</b> the air on your cheek, <b>HEAR</b> it go in and out.",
               "Comprobar si respira y cómo: <b>VER</b> si se mueve el pecho o el abdomen, <b>SENTIR</b> el aire en la mejilla, <b>OÍR</b> la entrada y salida de aire.")],
            [T("<b>C — Circulation</b>", "<b>C — Circulación</b>"),
             T("If the person is <b>not breathing and/or has no pulse</b>, they are in <b>cardio-respiratory arrest</b>: start <b>CPR</b> (heart massage) <b>urgently</b>.",
               "Si <b>no respira y/o no tiene pulso</b>, está en <b>parada cardio-respiratoria</b>: hay que realizar <b>urgentemente</b> la <b>reanimación cardiopulmonar</b> (masaje cardíaco).")],
        ],
        widths=["22%", "78%"],
    ))
    B.append(BOX("key", "Breathing problems", "Problemas respiratorios", [
        ("<b>Noisy, snoring or very laboured</b> breathing: the airway is <b>partly blocked</b>.", "Respiración <b>ruidosa, con ronquidos o muy dificultosa</b>: vías aéreas <b>parcialmente obstruidas</b>."),
        ("<b>Irregular, gasping or shallow</b> breathing: possible <b>serious brain damage</b>.", "Respiración <b>irregular, entrecortada o superficial</b>: posible <b>daño cerebral grave</b>."),
    ]))

    # ---------------------------------------------------------------- 4. treating the injured
    B.append(H2("4", "Treating the injured", "Actuación con los heridos"))
    B.append(H3("4.1 Conscious and breathing", "4.1 Herido consciente que respira"))
    B.append(P("Make sure there are no serious wounds or injuries, then go on to check the others — <b>without stopping watching</b> this person in case they get worse.",
               "Asegurarse de que no tiene heridas o lesiones graves antes de pasar a comprobar a otros heridos, pero <b>sin abandonar su vigilancia</b> por si empeora."))
    B.append(H3("4.2 Unconscious but breathing", "4.2 Herido inconsciente que respira"))
    B.append(P(
        "Check <b>regularly</b> that the person breathes (head-tilt, chin-lift). Put them in the <b>recovery position</b> (<i>posición lateral de seguridad</i>, PLS, or <i>de defensa</i>) so they don’t choke if:",
        "Hay que <b>comprobar regularmente que respira</b> (maniobra frente-mentón). Hay que colocarlo en la <b>posición lateral de seguridad</b> o de defensa (PLS) para evitar que se asfixie si:"))
    B.append(TABLE(
        [T("Recovery position when…", "PLS cuando…")],
        rows([
            ("You have to <b>leave them alone</b> for a moment to help others or call for help.", "Hay que <b>dejarle solo</b> un momento para atender a otros heridos o pedir ayuda."),
            ("They <b>vomit or bleed</b> from the mouth or nose. If they bleed from an <b>ear</b>, lay them on <b>that side</b>.", "<b>Vomita o sangra</b> por la boca o la nariz. Si sangra por un <b>oído</b>, se le coloca sobre <b>ese lado</b>."),
        ]),
    ))
    B.append(BOX("trap", "Keep checking", "Seguir comprobando", [
        ("If the person stops breathing they can go into cardiac arrest, so check the breathing every <b>2–3 minutes</b>.", "Si deja de respirar puede entrar en parada cardíaca: es recomendable comprobar la respiración cada <b>2–3 minutos</b>."),
    ]))
    B.append(FIG(recovery_position, "Best done by two people: raise the near arm, bend the far arm and leg, and roll the person towards you in one movement.",
                 "Mejor entre dos personas: sube el brazo cercano, dobla el brazo y la pierna alejados y gíralo hacia ti en un solo movimiento."))
    B.append(TABLE(
        [T("Recovery position, step by step (two people if possible)", "Posición lateral de seguridad, paso a paso (mejor entre dos)")],
        rows([
            ("<b>1.</b> <b>Raise the arm nearest to you</b> — the head will rest on it at the end.", "<b>1.</b> <b>Subir el brazo del herido más cercano</b> al auxiliador (donde apoyará la cabeza finalmente)."),
            ("<b>2.</b> <b>Bend the far arm</b> and the <b>leg on the same side</b>.", "<b>2.</b> <b>Doblar el brazo más alejado</b> y la <b>pierna del mismo lado</b>."),
            ("<b>3.</b> <b>Roll the person in one go</b> (a helper keeps the head and neck turning with the trunk). They end up with the <b>leg bent</b> and the <b>head on the arm</b> you raised first.",
             "<b>3.</b> <b>Voltear al herido de forma sincronizada</b> (el ayudante asegura que la cabeza-cuello gire a la vez que el tronco). Queda con la <b>pierna flexionada</b> y la <b>cabeza sobre el brazo</b> que se movió primero."),
        ]),
    ))

    B.append(H3("4.3 Unconscious and not breathing: CPR", "4.3 Herido inconsciente que no respira: RCP"))
    B.append(P("Start <b>cardiopulmonary resuscitation</b> (<i>reanimación cardiopulmonar</i>, RCP) <b>immediately</b>.", "Hay que realizar <b>inmediatamente</b> la <b>reanimación cardiopulmonar</b> (RCP)."))
    B.append(TABLE(
        [T("1 · Chest compressions", "1 · Compresiones torácicas")],
        rows([
            ("The injured person <b>face up</b>, on a <b>flat, hard surface</b>. Kneel next to their chest. Ideally <b>two rescuers</b>, taking turns every <b>1–2 minutes</b>.",
             "Herido <b>boca arriba</b>, sobre una <b>superficie plana y dura</b>. El auxiliador se arrodilla junto a su pecho. Recomendable, al menos, <b>dos auxiliadores</b> que se turnen cada <b>1 o 2 minutos</b>."),
            ("<b>Heel of one hand on the centre of the chest</b>, the heel of the other on top, fingers interlaced.", "<b>Talón de la mano en el centro del pecho</b> y el talón de la otra encima, entrelazando los dedos."),
            ("<b>Arms straight</b>: let your body weight press the chest down about <b>4–5 cm</b> (your course), <b>without bending the arms</b>. Release without losing contact and repeat until <b>30 compressions</b>.",
             "<b>Brazos rectos</b>: dejar caer el peso del cuerpo para hundir el pecho unos <b>4–5 cm</b> (tu curso), <b>sin doblar los brazos</b>. Dejar de presionar sin perder el contacto y repetir hasta <b>30 compresiones</b>."),
        ]),
    ))
    B.append(TABLE(
        [T("2 · Rescue breaths (artificial respiration)", "2 · Ventilaciones o insuflaciones (respiración artificial)")],
        rows([
            ("Keep the airway open with the head-tilt, chin-lift and <b>pinch the nose</b> with the thumb and index finger of the hand on the forehead.", "Mantener abierta la vía aérea con la maniobra frente-mentón y <b>pinzar la nariz</b> con el índice y el pulgar de la mano que está en la frente."),
            ("Breathe in, seal your lips round their mouth and <b>breathe out for one second</b>. Watch the <b>chest rise</b>; if it doesn’t, check your technique and that the <b>airway is not blocked</b>.",
             "Inspirar, colocar los labios junto a su boca y <b>expulsar el aire durante un segundo</b>. Observar cómo <b>se eleva el pecho</b>; si no, comprobar la técnica y que las <b>vías respiratorias no están obstruidas</b>."),
            ("Take your mouth away and watch the chest fall. If it worked, give a <b>second breath</b>. Then <b>repeat compressions and breaths</b>.", "Retirar la boca y observar cómo se deshincha el pecho. Si ha sido eficaz, <b>repetir con una segunda insuflación</b>. Después, <b>repetir compresiones e insuflaciones</b>."),
        ]),
    ))
    B.append(FIG(cpr, "Hands in the centre of the chest, arms straight; cycles of 30 compressions and 2 breaths until help arrives or the person reacts.",
                 "Manos en el centro del pecho y brazos rectos; ciclos de 30 compresiones y 2 ventilaciones hasta que llegue la ayuda o el herido reaccione."))
    B.append(TABLE(
        [T("CPR for…", "RCP en…"), T("How", "Cómo")],
        [
            [T("<b>Adults</b> (mouth to mouth)", "<b>Adultos</b> (boca a boca)"), T("Cycles of <b>30 compressions then 2 breaths</b>, at about <b>100 compressions a minute</b>, until help arrives or the person reacts.",
                                                                                   "Ciclos de <b>30 compresiones seguidas de 2 ventilaciones</b>, a un ritmo de <b>100 compresiones por minuto</b>, hasta que llegue la ayuda o el herido reaccione.")],
            [T("<b>Children</b> (mouth to mouth-and-nose)", "<b>Niños</b> (boca a boca-nariz)"), T("<b>5 breaths first</b>, then cycles of <b>30 : 2</b>. Press with <b>less force</b>: one hand, or <b>two fingers</b> for a baby.",
                                                                                                "<b>5 ventilaciones iniciales</b> y luego ciclos de <b>30 : 2</b>. Compresiones con <b>menos fuerza</b>: con una sola mano o, incluso, <b>con dos dedos</b> (bebés).")],
        ],
        widths=["28%", "72%"],
    ))
    B.append(BOX("key", "Current European guidelines (ERC 2025)", "Guías europeas actuales (ERC 2025)", [
        ("They ask for compressions <b>5–6 cm</b> deep at <b>100–120 a minute</b>, letting the chest come fully back up. For the exam, give your course’s figures (4–5 cm, 100 a minute).",
         "Piden compresiones de <b>5–6 cm</b> de profundidad a <b>100–120 por minuto</b>, dejando que el pecho vuelva a subir del todo. En el examen, da las cifras de tu curso (4–5 cm, 100 por minuto)."),
        ("If you are <b>not trained</b> in rescue breaths, give <b>compressions only</b> — the 112 operator will guide you. If a <b>defibrillator (AED)</b> is at hand, switch it on and follow its voice instructions.",
         "Si <b>no tienes formación</b> en ventilaciones, haz <b>solo compresiones</b>: el operador del 112 te guiará. Si hay un <b>desfibrilador (DEA)</b> a mano, enciéndelo y sigue sus instrucciones de voz."),
    ]))

    B.append(H3("4.4 Bleeding", "4.4 Hemorragias"))
    B.append(FIG(bleeding, "Firm pressure on the wound first. Your course then adds raising the limb and pressing the armpit or groin; a tourniquet is the last resort.",
                 "Primero, presión firme sobre la herida. Tu curso añade después elevar el miembro y presionar en la axila o la ingle; el torniquete es el último recurso."))
    B.append(TABLE(
        [T("External bleeding (blood comes out of a wound)", "Hemorragias externas (sale sangre de una herida)")],
        rows([
            ("<b>1. Press directly on the wound</b> with gauze or a clean piece of cloth. If it soaks through, <b>put more on top without removing the first</b>.",
             "<b>1. Presionar directamente sobre la herida</b> con una gasa o un trozo de tela limpia. Si se empapa, <b>poner otra gasa encima sin retirar la anterior</b>."),
            ("<b>2.</b> If it doesn’t stop, <b>raise the limb</b> and keep pressing: <b>arm</b> — press in the hollow of the <b>armpit</b>, on the arm bone; <b>leg</b> — press in the fold of the <b>groin</b> (where the artery runs).",
             "<b>2.</b> Si no se contiene, <b>elevar el miembro</b> manteniendo la presión: <b>brazo</b>, presionar en el hueco de la <b>axila</b>, sobre el hueso del brazo; <b>pierna</b>, presionar en el pliegue de la <b>ingle</b> (donde está la arteria)."),
            ("<b>3. Last resort</b> — very dangerous, avoid it if possible: a <b>tourniquet above</b> the wound.", "<b>3. Como último recurso</b> (muy peligroso, debe evitarse si es posible): un <b>torniquete por encima</b> de la hemorragia."),
        ]),
    ))
    B.append(BOX("trap", "After applying a tourniquet", "Tras realizar un torniquete", [
        ("Only for <b>amputation or very serious bleeding</b>. <b>Leave it on</b> — don’t remove or loosen it — and <b>visible</b> (not covered).", "Solo en caso de <b>amputación o hemorragias muy graves</b>. <b>Mantenerlo</b> (no quitarlo ni aflojarlo) y <b>visible</b> (sin tapar)."),
        ("Write the <b>time it was applied</b> somewhere visible (a note next to it) for the medical team.", "Anotar en un lugar visible la <b>hora en que se realizó</b> (cartel o escrito junto a él) para los sanitarios."),
    ]))
    B.append(TABLE(
        [T("Internal bleeding that shows (blood from an opening)", "Hemorragias internas exteriorizadas (sale sangre por un orificio)"), T("What it may mean · what to do", "Qué puede indicar · qué hacer")],
        [
            [T("<b>Ear</b>", "<b>Oído</b>"), T("Possible fracture of the <b>base of the skull</b>. Cover with gauze <b>without plugging it</b>; recovery position <b>on the bleeding ear</b>.",
                                               "Posible fractura de la <b>base del cráneo</b>. <b>Cubrir con una gasa sin taponar</b>; posición lateral de seguridad <b>sobre el oído que sangra</b>.")],
            [T("<b>Nose</b>", "<b>Nariz</b>"), T("Possible skull fracture. <b>Unconscious</b>: recovery position. <b>Conscious</b>: head <b>straight or tilted forward</b>.",
                                               "Posible fractura del cráneo. <b>Inconsciente</b>: posición lateral de seguridad. <b>Consciente</b>: cabeza <b>recta o hacia delante</b>.")],
            [T("<b>Mouth</b>", "<b>Boca</b>"), T("<b>Lung</b> (coughs up blood): <b>half-sitting</b> if conscious, recovery position if not. <b>Stomach</b> (vomits blood): recovery position.",
                                               "<b>Pulmón</b> (sangra con tos): <b>semisentado</b> si está consciente; si no, posición lateral de seguridad. <b>Estómago</b> (vomita sangre): posición lateral de seguridad.")],
        ],
        widths=["16%", "84%"],
    ))
    B.append(BOX("trap", "Don’t stop it", "No cortarla", [
        ("Internal bleeding that shows through an opening must <b>not be stopped or plugged</b>: it is extremely serious.", "Las hemorragias internas exteriorizadas <b>no deben cortarse ni taponarse</b>: son de extrema gravedad."),
    ]))
    B.append(BOX("key", "Current European guidance on bleeding", "Guía europea actual sobre hemorragias", [
        ("It relies on <b>firm, direct pressure</b> on the wound and no longer recommends <b>raising the limb</b> or pressing <b>pressure points</b> (armpit, groin). "
         "For life-threatening limb bleeding that pressure can’t stop, a <b>tourniquet</b> is the next step, not a last resort. For the exam, give your course’s answers.",
         "Se basa en la <b>presión directa y firme</b> sobre la herida y ya no recomienda <b>elevar el miembro</b> ni presionar <b>puntos de compresión</b> (axila, ingle). "
         "Ante una hemorragia de un miembro que pone en peligro la vida y no cede con presión, el <b>torniquete</b> es el siguiente paso, no un último recurso. En el examen, responde como tu curso."),
    ]))

    B.append(H3("4.5 Shock", "4.5 Estado de shock"))
    B.append(P("<b>Shock</b> can follow a <b>major loss of blood</b>.", "El <b>estado de shock</b> se puede producir por una <b>pérdida importante de sangre</b>."))
    B.append(FIG(shock, "Anti-shock position: lying down with the legs raised, so the head is lower than the body; lightly covered, clothing loosened, nothing to drink.",
                 "Posición antishock: tumbado con las piernas elevadas, de modo que la cabeza quede más baja que el cuerpo; tapado ligeramente, con la ropa aflojada y sin dar bebidas."))
    B.append(TABLE(
        [T("Signs", "Síntomas"), T("What to do", "Qué hacer")],
        [[T("<b>Cold sweat</b>, <b>pale skin</b>, confusion, restlessness, <b>fast, shallow breathing</b>, <b>fast, weak pulse</b>…", "<b>Sudoración fría</b>, <b>piel pálida</b>, confusión, inquietud, <b>respiración rápida y superficial</b>, <b>pulso rápido y débil</b>…"),
          T("<b>Anti-shock position</b> (head lower than the rest of the body); loosen tight clothing; <b>cover lightly</b> (without making them sweat); <b>no drinks</b>. "
            "Raise the legs only if there is no sign of a leg, hip or spine injury.",
            "<b>Posición antishock</b> (la cabeza más baja que el resto del cuerpo); aflojar la ropa que oprima; <b>taparlo ligeramente</b> (sin hacerle sudar); <b>no dar bebidas</b>. "
            "Eleva las piernas solo si no hay indicios de lesión en piernas, cadera o columna.")]],
        widths=["40%", "60%"],
    ))

    # ---------------------------------------------------------------- 5. secondary assessment
    B.append(H2("5", "Secondary assessment", "Valoración secundaria de los heridos"))
    B.append(TABLE(
        [T("Injury", "Lesión"), T("What to do", "Qué hacer")],
        [
            [T("<b>Fractures</b>", "<b>Fracturas</b>"),
             T("In <b>open</b> fractures, cover the wound and control the bleeding. If a limb is <b>deformed</b> (painful), <b>don’t try to set it</b> (don’t put the bone back). <b>Immobilise</b> the fracture by holding <b>both ends</b>.",
               "En fracturas <b>abiertas</b> y complicadas, tapar la herida y contener la hemorragia. Si hay <b>deformidad</b> en una extremidad (dolorosa), <b>no reducir la fractura</b> (no recolocar el hueso). <b>Inmovilizar</b> la zona sujetando <b>los dos extremos</b>.")],
            [T("<b>Wounds</b>", "<b>Heridas</b>"),
             T("Cover with <b>sterile dressings</b>. <b>Don’t handle or explore</b> them (unless you must stop bleeding). <b>Don’t pull out embedded objects</b> — it can worsen the injury and the bleeding: dress around the object and immobilise it all as one. "
               "If <b>organs come out</b>, don’t move the person except to lay them down, and cover the organs with <b>damp cloths</b>, without touching them.",
               "Cubrir con <b>apósitos estériles</b>. <b>No manipular ni explorar</b> (salvo para reducir una hemorragia). <b>No retirar los objetos clavados</b> (puede aumentar la lesión y la hemorragia): tapar la herida con el objeto, fijarlo con un vendaje e inmovilizar en bloque. "
               "Si hay <b>salida de vísceras</b>, no mover al herido salvo para tumbarlo y cubrir los órganos con <b>paños humedecidos</b>, sin tocarlos.")],
        ],
        widths=["18%", "82%"],
    ))
    B.append(TABLE(
        [T("Treating burns", "Cómo tratar las quemaduras")],
        rows([
            ("<b>Don’t touch</b> the burnt area; <b>don’t remove clothing stuck</b> to it; <b>don’t burst or cut blisters</b>.", "<b>No tocar</b> la zona quemada; <b>no quitar la ropa pegada</b>; <b>no manipular las ampollas</b> (ni pincharlas ni cortarlas)."),
            ("Apply <b>cold water</b> (no creams) and cover with <b>damp sterile dressings</b>. Bandage different burnt areas <b>separately</b>, never together.", "Aplicar <b>agua fría</b> (no pomadas) y <b>cubrir con apósitos estériles húmedos</b>. Vendar las distintas zonas quemadas <b>por separado</b>, nunca juntas."),
            ("<b>Raise</b> the burnt part (less pain and swelling). Watch for <b>shock</b>, and for <b>breathing problems</b> if the face is burnt.", "<b>Elevar</b> la zona quemada (menos dolor e hinchazón). Vigilar un posible <b>shock</b> o <b>problemas respiratorios</b> si hay quemaduras en la cara."),
        ]),
    ))
    B.append(BOX("key", "Putting out a fire", "Cómo apagar un incendio", [
        ("<b>Vehicle</b>: get the injured out first; then an <b>extinguisher at the base of the flames</b> or, failing that, <b>sand or blankets</b> — <b>never water</b>.", "<b>Vehículo</b>: primero sacar a los heridos; después <b>extintor sobre la base de las llamas</b> o, en su defecto, <b>arena o mantas</b>, <b>nunca agua</b>."),
        ("<b>A person on fire</b>: cover them with a <b>blanket</b> or roll them on the ground. With an extinguisher, <b>don’t aim at the face</b>.", "<b>Ocupante en llamas</b>: cubrirle con una <b>manta</b> o hacerle rodar por el suelo. Con extintor, <b>no apuntar a la cara</b>."),
    ]))

    # ---------------------------------------------------------------- 6. moving the injured
    B.append(H2("6", "Moving the injured", "Traslado de heridos"))
    B.append(P(
        "<b>Wait for the ambulance</b> to take the injured. A <b>private vehicle</b> may be used — if the person can travel immobilised in a position suited to their state — but <b>only exceptionally</b>, when:",
        "Se debe <b>esperar a la ambulancia</b> para trasladar a los heridos. Se puede usar un <b>vehículo particular</b>, si el herido puede ir inmovilizado en una posición adecuada a su estado, pero solo <b>excepcionalmente</b>, si:"))
    B.append(TABLE(
        [T("Only if…", "Solo si…")],
        rows([
            ("<b>Medical help can’t be requested</b> by any means.", "<b>No es posible solicitar ayuda sanitaria</b> por ningún medio."),
            ("The person is <b>getting seriously worse</b> and help is <b>late</b>: <b>more than 30 minutes</b> since it was called, with bleeding that can’t be controlled, <b>signs of shock getting worse</b>, or a <b>tourniquet</b>.",
             "El herido <b>empeora gravemente</b> y la ayuda <b>se retrasa</b>: <b>más de 30 minutos</b> desde que se solicitó, con una hemorragia externa que no se puede contener, <b>signos de shock en aumento</b> o un <b>torniquete</b>."),
        ]),
    ))
    B.append(BOX("key", "Taking an injured person in a private car", "Trasladar al herido en vehículo particular", [
        ("Keep the <b>head–neck–trunk line</b> straight; use a vehicle that lets them lie in the <b>right position</b>; <b>go with them</b> to watch their state.", "Mantener <b>alineado el eje cabeza-cuello-tronco</b>; usar un vehículo que permita la <b>posición adecuada</b>; <b>acompañar al herido</b> para vigilarlo."),
        ("A non-priority vehicle on an urgent run warns others of its presence (<b>horn and hazard lights</b>, or <b>waving a handkerchief</b>) and still <b>follows the traffic rules</b>.",
         "Un vehículo no prioritario en servicio de urgencia advierte su presencia (<b>claxon y luces de emergencia</b>, o <b>agitando un pañuelo</b>) y <b>respeta las normas de circulación</b>."),
    ]))

    # ---------------------------------------------------------------- 7. first-aid kit
    B.append(H2("7", "First-aid kit", "Botiquín"))
    B.append(P(
        "A <b>first-aid kit</b> in the vehicle is <b>not compulsory, but recommended</b> and useful. Keep it usable, with: gloves, bandages, gauze, sterile dressings, elastic bands, large handkerchiefs, tape, scissors, tweezers, safety pins, disinfectant…",
        "Llevar un <b>botiquín</b> en el vehículo <b>no es obligatorio, pero sí recomendable</b> y útil. Que esté en condiciones de uso e incluya: guantes, vendas, gasas, apósitos estériles, gomas elásticas, pañuelos grandes, esparadrapo, tijeras, pinzas, imperdibles, desinfectante…"))

    # ---------------------------------------------------------------- 8. traps
    B.append(H2("8", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("The order is <b>Protect → Alert → Help</b>. Vest and V-16 <b>before</b> getting out.", "El orden es <b>Proteger → Avisar → Socorrer</b>. Chaleco y V-16 <b>antes</b> de salir."),
        ("Non-involved users may drive on if the <b>agents are already there</b> or their help is <b>clearly not needed</b>.", "Los no implicados pueden seguir si ya están los <b>agentes</b> o su ayuda <b>claramente no es necesaria</b>."),
        ("No need to alert or stay only if <b>all three</b>: clearly minor injuries, safety restored, nobody asks.", "No hace falta avisar ni quedarse solo si se dan <b>las tres</b>: heridas leves, seguridad restablecida y nadie lo pide."),
        ("Fire: extinguisher at the <b>base</b> of the flames, sand or blankets — <b>never water</b>. Person on fire: blanket or roll; never aim the extinguisher at the face.", "Fuego: extintor en la <b>base</b> de las llamas, arena o mantas, <b>nunca agua</b>. Persona en llamas: manta o rodar; nunca extintor a la cara."),
        ("<b>Don’t move</b> the injured or <b>remove a helmet</b> unless essential (two people). <b>Nothing to eat or drink</b>, not even water. Cover them <b>even in summer</b>.", "<b>No mover</b> a los heridos ni <b>quitar el casco</b> salvo que sea imprescindible (dos personas). <b>Ni comida ni bebida</b>, ni siquiera agua. Taparlos <b>incluso en verano</b>."),
        ("Several injured: assess <b>all first</b>, <b>10–15 s</b> each. Unconscious first.", "Varios heridos: valorar <b>a todos primero</b>, <b>10–15 s</b> cada uno. Primero los inconscientes."),
        ("Unconscious and breathing: <b>recovery position</b>, check every <b>2–3 min</b>; bleeding ear → lie on <b>that ear</b>.", "Inconsciente que respira: <b>PLS</b> y comprobar cada <b>2–3 min</b>; sangra por un oído → sobre <b>ese oído</b>."),
        ("CPR: <b>30 : 2</b>, about <b>100 a minute</b>; children <b>5 breaths first</b>; baby: <b>two fingers</b>. Arms <b>straight</b>.", "RCP: <b>30 : 2</b>, unas <b>100 por minuto</b>; niños <b>5 ventilaciones iniciales</b>; bebés: <b>dos dedos</b>. Brazos <b>rectos</b>."),
        ("Soaked gauze: put another <b>on top</b>, don’t remove it. Tourniquet: <b>don’t loosen</b>, leave <b>visible</b>, note the <b>time</b>.", "Gasa empapada: otra <b>encima</b>, sin retirarla. Torniquete: <b>no aflojar</b>, <b>visible</b> y anotar la <b>hora</b>."),
        ("Blood from an ear, nose or mouth: <b>don’t plug it</b>. Embedded object: <b>don’t pull it out</b>. Fracture: <b>don’t set it</b>.", "Sangre por oído, nariz o boca: <b>no taponar</b>. Objeto clavado: <b>no retirarlo</b>. Fractura: <b>no reducirla</b>."),
        ("Burns: cold water, <b>no creams</b>, don’t burst blisters or remove stuck clothing.", "Quemaduras: agua fría, <b>sin pomadas</b>, no pinchar ampollas ni quitar la ropa pegada."),
        ("Own car to hospital only <b>exceptionally</b> (no way to call, or help over <b>30 min</b> late and getting worse). First-aid kit: <b>not compulsory</b>.", "Coche particular solo <b>excepcionalmente</b> (sin forma de avisar, o la ayuda tarda más de <b>30 min</b> y empeora). Botiquín: <b>no obligatorio</b>."),
    ]))

    # ---------------------------------------------------------------- 9. numbers
    B.append(H2("9", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Emergency number (free, whole EU, no credit needed)", "Teléfono de emergencias (gratuito, toda la UE, sin saldo)"), T("112", "112")],
            [T("Golden hour", "Hora de oro"), T("the first hour after the accident", "la primera hora tras el accidente")],
            [T("Time to assess each injured person", "Tiempo para valorar a cada herido"), T("10–15 seconds", "10–15 segundos")],
            [T("Check breathing of someone in the recovery position", "Comprobar la respiración en PLS"), T("every 2–3 minutes", "cada 2–3 minutos")],
            [T("People to remove a helmet / for the recovery position", "Personas para quitar el casco / para la PLS"), T("at least 2 / 2 if possible", "mínimo 2 / 2 si es posible")],
            [T("CPR: compressions : breaths", "RCP: compresiones : ventilaciones"), T("30 : 2 (children: 5 breaths first)", "30 : 2 (niños: 5 ventilaciones iniciales)")],
            [T("Compression depth / rate (course)", "Profundidad / ritmo (curso)"), T("4–5 cm / 100 a minute (ERC 2025: 5–6 cm, 100–120)", "4–5 cm / 100 por minuto (ERC 2025: 5–6 cm, 100–120)")],
            [T("Swap rescuers doing CPR", "Turnarse en la RCP"), T("every 1–2 minutes", "cada 1–2 minutos")],
            [T("One rescue breath lasts", "Cada insuflación dura"), T("1 second", "1 segundo")],
            [T("Help late before using a private car", "Retraso de la ayuda para usar un coche particular"), T("more than 30 minutes", "más de 30 minutos")],
            [T("Report the accident form to your insurer (law)", "Comunicar el parte a la aseguradora (ley)"), T("7 days", "7 días")],
            [T("Failure to help, if you caused the accident by negligence", "Omisión de socorro si causaste el accidente por imprudencia"), T("prison 6 months–4 years", "prisión de 6 meses a 4 años")],
        ],
        widths=["58%", "42%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["du2", "pa1", "pr3", "al3", "hp4", "as2", "rp2", "cp1", "cp6", "bl3", "bl8", "ij5"]


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
    ("Ley sobre Tráfico (RDL 6/2015), art. 51: duties in case of an accident", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722"),
    ("Reglamento General de Circulación (RD 1428/2003), art. 129: duties of those involved in or aware of an accident — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2003-23514"),
    ("Código Penal (LO 10/1995), art. 195 (failure to help) and art. 382 bis (leaving the scene of an accident)", "https://www.boe.es/buscar/act.php?id=BOE-A-1995-25444"),
    ("European Resuscitation Council Guidelines 2025: adult basic life support (summary by the Resuscitation Council UK)", "https://www.resus.org.uk/professional-library/2025-resuscitation-guidelines/adult-basic-life-support-guidelines"),
    ("European Resuscitation Council Guidelines 2021: First aid (bleeding control, shock position)", "https://cprguidelines.eu/assets/guidelines/European-Resuscitation-Council-Guidelines-2021-Fi.pdf"),
]

GLOSSARY = [
    ("omisión del deber de socorro", "failure to help (a crime)"),
    ("abandono del lugar del accidente", "leaving the scene of an accident"),
    ("implicado / no implicado", "involved / not involved"),
    ("parte amistoso (declaración amistosa)", "accident report form"),
    ("regla PAS: proteger, avisar, socorrer", "PAS rule: protect, alert, help"),
    ("autoprotegerse", "protect yourself"),
    ("señal V-16 · chaleco reflectante", "V-16 warning light · reflective vest"),
    ("extintor", "fire extinguisher"),
    ("eje cabeza-cuello-tronco", "head–neck–trunk line"),
    ("hora de oro (hora dorada)", "golden hour"),
    ("valoración inicial / secundaria", "primary / secondary assessment"),
    ("consciente / inconsciente", "conscious / unconscious"),
    ("signos vitales", "vital signs"),
    ("maniobra frente-mentón", "head-tilt, chin-lift"),
    ("vía aérea · cuerpo extraño", "airway · foreign object"),
    ("parada cardio-respiratoria", "cardiac arrest"),
    ("reanimación cardiopulmonar (RCP)", "cardiopulmonary resuscitation (CPR)"),
    ("compresiones torácicas · ventilaciones (insuflaciones)", "chest compressions · rescue breaths"),
    ("desfibrilador (DEA)", "defibrillator (AED)"),
    ("posición lateral de seguridad (PLS)", "recovery position"),
    ("hemorragia externa / interna exteriorizada", "external bleeding / internal bleeding that shows"),
    ("torniquete", "tourniquet"),
    ("axila · ingle", "armpit · groin"),
    ("estado de shock · posición antishock", "shock · shock position (legs raised)"),
    ("fractura abierta · reducir una fractura", "open fracture · set a fracture"),
    ("apósito estéril · objeto clavado", "sterile dressing · embedded object"),
    ("quemadura · ampolla", "burn · blister"),
    ("botiquín", "first-aid kit"),
]
