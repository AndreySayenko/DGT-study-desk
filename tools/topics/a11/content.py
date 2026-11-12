# -*- coding: utf-8 -*-
"""Category A1/A2, Topic 11 content (first aid), bilingual. Every text is a (EN, ES) pair.

The A1/A2 course's Tema 11 (Primeros auxilios) teaches the same first aid, in the same order, as the Category B course:
first aid does not depend on what you ride. This page therefore takes the text of Category B, Topic 11 — one source of
truth — and replaces what is different on a motorcycle: protecting yourself and the scene (the V-16 is optional on a
motorcycle; the vest has been compulsory equipment since 1 October 2026), a section on the injured rider's helmet, and
the exam traps.

The duties come from the Ley sobre Tráfico (art. 51), the Reglamento General de Circulación (art. 129) and the Código
Penal (arts. 195 and 382 bis); the motorcycle's equipment from the Reglamento General de Vehículos (Anexo XII, as
amended by RD 518/2026); the first-aid technique from the course, compared with the European Resuscitation Council
guidelines 2025.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from ..b11 import content as B11
from ..b11.diagrams import protect_scene, pas_rule
from .diagrams import pas_moto, protect_moto, helmet_off

TWO = ("On two wheels", "Sobre dos ruedas")


def _index(B, test, what):
    for i, b in enumerate(B):
        if test(b):
            return i
    raise KeyError(f"Topic B11 has no {what}")


def blocks():
    B = B11.blocks()

    # ---------------------------------------------------------------- how to use (replaces B11's)
    assert B[0][0] == "box"
    B[0] = BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("What the law asks of you at an accident (help, or call for help, and don’t leave the scene) and what to do, in order: the <b>PAS</b> rule — <b>protect, alert, help</b> — "
         "then <b>assess</b> the injured (conscious? breathing?) and treat them.",
         "Lo que te exige la ley en un accidente (auxiliar o pedir auxilio, y no marcharte) y qué hacer, en orden: la regla <b>PAS</b> —<b>proteger, avisar, socorrer</b>— "
         "y después <b>valorar</b> a los heridos (¿consciente?, ¿respira?) y actuar."),
        ("First aid is the same whatever you ride, so this page shares its text with <b>Category B, Topic 11</b>. What changes on a motorcycle is flagged <b>“On two wheels”</b>: "
         "protecting the scene without a car (the <b>vest</b> your motorcycle must now carry, the <b>V-16</b> that is optional), and the injured rider’s <b>helmet</b> (section 3.2).",
         "Los primeros auxilios son iguales conduzcas lo que conduzcas, así que esta página comparte su texto con el <b>Tema 11 del permiso B</b>. Lo que cambia en moto va marcado como <b>«Sobre dos ruedas»</b>: "
         "proteger el lugar sin coche (el <b>chaleco</b> que ahora debe llevar la moto y la <b>V-16</b>, que es opcional) y el <b>casco</b> del motorista herido (apartado 3.2)."),
        ("The exam loves <b>numbers and orders</b>: 112, <b>10–15 seconds</b> per injured person, breathing every <b>2–3 minutes</b>, CPR <b>30 : 2</b>, children <b>5</b> breaths first, the <b>golden hour</b>, "
         "<b>two people</b> to take off a helmet, <b>30 minutes</b> before taking someone in a private vehicle. Your course’s CPR depth and bleeding advice are older than the current European guidelines; "
         "the page keeps the course’s answer for the exam and notes the difference.",
         "El examen pregunta sobre todo <b>cifras y órdenes</b>: 112, <b>10–15 segundos</b> por herido, respiración cada <b>2–3 minutos</b>, RCP <b>30 : 2</b>, niños <b>5</b> ventilaciones iniciales, la <b>hora de oro</b>, "
         "<b>dos personas</b> para quitar un casco, <b>30 minutos</b> antes de llevar a alguien en un vehículo particular. La profundidad de la RCP y los consejos sobre hemorragias de tu curso son anteriores a las guías europeas actuales; "
         "la página mantiene la respuesta del curso para el examen e indica la diferencia."),
    ])

    # ---------------------------------------------------------------- 2.1 protect: the rider's version
    i = _index(B, lambda b: b[0] == "table" and b[1][0]["en"] == "In this order", "‘In this order’ table")
    B[i] = TABLE(
        [T("In this order", "En este orden"), T("What to do on a motorcycle", "Qué hacer en moto")],
        [
            [T("<b>1. Protect yourself</b>", "<b>1. Autoprotegerse</b>"),
             T("<b>Stop somewhere safe</b> without blocking traffic (off the carriageway if possible), following the rules. If you carry a <b>V-16</b> light — <b>optional</b> on a motorcycle — switch it on and place it, "
               "by hand, on the <b>most visible metal part</b> of the motorcycle before you walk away; use the <b>hazard lights</b> if your motorcycle has them. "
               "Put on the <b>reflective vest</b> your motorcycle must carry before you step onto the carriageway or shoulder of an interurban road. <b>Avoid walking on the carriageway</b>.",
               "<b>Detener la moto en un lugar seguro</b>, sin obstaculizar (preferiblemente fuera de la calzada) y cumpliendo las normas. Si llevas la luz <b>V-16</b> —<b>opcional</b> en moto—, enciéndela y colócala "
               "con la mano sobre la <b>parte metálica más visible</b> de la moto antes de alejarte; usa las <b>luces de emergencia</b> si tu moto las tiene. "
               "Ponte el <b>chaleco reflectante</b> que debe llevar la moto antes de pisar la calzada o el arcén de una vía interurbana. <b>Evitar circular por la calzada</b>.")],
            [T("<b>2. Protect the scene</b>", "<b>2. Proteger el lugar del accidente</b>"),
             T("Move vehicles or load <b>off the carriageway</b> (shoulder or central reservation) if they block traffic, and <b>switch the engines off</b>. Look for other risks: <b>no smoking</b>; "
               "in a fire, use an <b>extinguisher at the base of the flames</b> or, failing that, sand or blankets — <b>never water</b>.",
               "Colocar los vehículos o la carga <b>fuera de la calzada</b> (arcén o mediana) si son un obstáculo, e <b>inmovilizarlos con el motor parado</b>. Evaluar otros riesgos: <b>no fumar</b>; "
               "en caso de incendio, <b>extintor directamente sobre la base de las llamas</b> o, en su defecto, arena o mantas, <b>nunca agua</b>.")],
            [T("<b>3. Protect the victims</b>", "<b>3. Proteger a las víctimas</b>"),
             T("<b>Don’t move the injured</b> unless it is essential because of a danger — and then keep the <b>head–neck–trunk line</b> still first. <b>Don’t remove a rider’s helmet</b> unless it is essential and you know how (at least <b>two people</b>, section 3.2).",
               "<b>No mover a los heridos</b> salvo que sea imprescindible por existir un peligro, e inmovilizando antes el <b>eje cuello-cabeza-tronco</b>. <b>No quitar el casco</b> al motorista salvo que sea imprescindible y se sepa hacerlo (mínimo <b>dos personas</b>, apartado 3.2).")],
        ],
        widths=["24%", "76%"],
    )
    B.insert(i + 1, BOX("trap", f"{TWO[0]}: vest and V-16", f"{TWO[1]}: chaleco y V-16", [
        ("Your course still says “if you have a vest, it is advisable to put it on”. Since <b>1 October 2026</b> every motorcycle must <b>carry</b> a high-visibility vest, and you must <b>wear it</b> when you get off and stand on the "
         "<b>carriageway or shoulder of an interurban road</b>.",
         "Tu curso dice aún «si tuviese chaleco, es recomendable que se lo ponga». Desde el <b>1 de octubre de 2026</b> toda motocicleta debe <b>llevar</b> un chaleco de alta visibilidad, y hay que <b>ponérselo</b> al bajarse y ocupar la "
         "<b>calzada o el arcén de una vía interurbana</b>."),
        ("The connected <b>V-16</b> light is compulsory for cars, vans, buses and lorries; on a motorcycle it is <b>recommended, not compulsory</b>. Hazard lights are <b>optional</b> on motorcycles (Topic 7).",
         "La luz <b>V-16</b> conectada es obligatoria en turismos, furgonetas, autobuses y camiones; en moto es <b>recomendable, no obligatoria</b>. Las luces de emergencia son <b>opcionales</b> en moto (Tema 7)."),
    ]))
    f = _index(B, lambda b: b[0] == "fig" and b[1] is pas_rule, "pas_rule figure")
    B[f] = FIG(pas_moto, B[f][2]["en"], B[f][2]["es"])
    j = _index(B, lambda b: b[0] == "fig" and b[1] is protect_scene, "protect_scene figure")
    B[j] = FIG(protect_moto, "Motorcycle off the carriageway with the engine off; you in the vest, off the road; the damaged vehicles off the carriageway too.",
               "La moto fuera de la calzada y con el motor parado; tú, con chaleco y fuera de la calzada; los vehículos accidentados, también fuera.")

    # ---------------------------------------------------------------- 3.2 the injured rider's helmet (new)
    k = _index(B, lambda b: b[0] == "box" and b[2]["en"] == "Breathing problems", "‘Breathing problems’ box")
    B[k + 1:k + 1] = [
        H3("3.2 On two wheels: an injured rider’s helmet", "3.2 Sobre dos ruedas: el casco del motorista herido"),
        P("A rider who has fallen may have a <b>neck or spine injury</b>. Taking the helmet off badly can turn it into paralysis, so the rule is to <b>leave it on</b> and check the person through it.",
          "Un motorista que ha caído puede tener una <b>lesión en el cuello o la columna</b>. Quitarle mal el casco puede convertirla en una parálisis, así que la norma es <b>dejarlo puesto</b> y valorar al herido con él."),
        FIG(helmet_off, "Check breathing and the carotid pulse with the helmet on. Take it off only if essential — for example to do CPR — with two people: one holds neck and jaw, the other slides the helmet off.",
            "Comprueba la respiración y el pulso carotídeo con el casco puesto. Quítalo solo si es imprescindible —por ejemplo, para hacer la RCP— entre dos personas: una sujeta cuello y mandíbula y la otra saca el casco."),
        BOX("key", "A rider who is not breathing", "Actuación ante motorista accidentado que no respira", [
            ("Check the <b>pulse in the neck</b> (carotid) and the <b>breathing</b> <b>without removing the helmet</b>, unless it is essential to do <b>CPR</b>.",
             "Comprobar el <b>pulso carotídeo</b> en el cuello y la <b>respiración</b> <b>sin retirar el casco</b>, salvo que sea imprescindible para realizar una <b>RCP</b>."),
            ("If it must come off: <b>at least two people</b> who know the technique, to avoid injuring the <b>cervical spine</b>, keeping the <b>neck–head–trunk</b> line still before moving the person.",
             "Si hay que quitarlo: <b>mínimo dos personas</b> que conozcan la técnica, para evitar lesiones en la <b>columna cervical</b>, inmovilizando el eje <b>cuello-cabeza-tronco</b> antes de moverlo."),
        ]),
    ]

    # ---------------------------------------------------------------- exam traps: rider ones first
    t = _index(B, lambda b: b[0] == "box" and b[1] == "trap" and b[2]["en"] == "Read twice", "‘Read twice’ box")
    shared = [it for it in B[t][3] if not it["en"].startswith("The order is")]
    assert len(shared) == len(B[t][3]) - 1
    rider = [
        T("The order is <b>Protect → Alert → Help</b>. On a motorcycle: off the carriageway, engine off, <b>vest on</b> before you walk on an interurban road; the V-16 is <b>optional</b>.",
          "El orden es <b>Proteger → Avisar → Socorrer</b>. En moto: fuera de la calzada, motor parado y <b>chaleco puesto</b> antes de caminar por una interurbana; la V-16 es <b>opcional</b>."),
        T("Injured rider: check breathing and the <b>carotid pulse with the helmet on</b>. Off only if essential (CPR), by <b>two people</b>, keeping <b>neck–head–trunk</b> in line.",
          "Motorista herido: respiración y <b>pulso carotídeo con el casco puesto</b>. Quitarlo solo si es imprescindible (RCP), entre <b>dos personas</b>, con el eje <b>cuello-cabeza-tronco</b> alineado."),
    ]
    B[t] = ("box", "trap", T("Read twice", "Lee dos veces"), rider + shared)
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["du3", "pr1", "pr4", "al2", "hp3", "as2", "hm2", "rp3", "cp2", "bl2", "sh2", "tr2"]


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


SOURCES = list(B11.SOURCES) + [
    ("Real Decreto 518/2026 (in force 1 October 2026): every motorcycle must carry a high-visibility vest (Reglamento General de Vehículos, Anexo XII.3)", "https://www.boe.es/buscar/doc.php?id=BOE-A-2026-13889"),
]

GLOSSARY = list(B11.GLOSSARY) + [
    ("retirar el casco", "remove the helmet"),
    ("pulso carotídeo", "carotid (neck) pulse"),
    ("columna cervical · eje cuello-cabeza-tronco", "cervical spine · neck–head–trunk line"),
]
