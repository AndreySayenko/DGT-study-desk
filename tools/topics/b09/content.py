# -*- coding: utf-8 -*-
"""Topic 9 content (documentation: licences, vehicle papers, insurance, points and liability), bilingual.
Every text is a (EN, ES) pair.

The sections follow the order of the learner's course (Tema 9: Documentación). The wording and the figures are original;
the rules come from the Ley sobre Tráfico (RDL 6/2015, with the points system in its annexes), the Reglamento General
de Conductores (RD 818/2009), the Reglamento General de Vehículos (RD 2822/1998), the ITV decree (RD 920/2017), the
motor-insurance law (RDL 8/2004, as amended by Ley 5/2025) and the Código Penal, as they stand in November 2026.
"""

from blocks import T, H2, H3, P, E, FIG, TABLE, BOX  # noqa: F401
from .diagrams import licence_ages, plates, itv_chart, insurance_grid, points_path


def blocks():
    B = []

    # ---------------------------------------------------------------- how to use
    B.append(BOX("key", "What this topic is really about", "De qué va realmente este tema", [
        ("Three families of papers: the <b>driver’s</b> (licence and its points), the <b>vehicle’s</b> (registration certificate, ITV card, insurance), and what happens when rules are broken "
         "(<b>points</b>, <b>who pays the fine</b>, and <b>road crimes</b>).",
         "Tres familias de documentos: los del <b>conductor</b> (permiso y sus puntos), los del <b>vehículo</b> (permiso de circulación, tarjeta ITV, seguro) y lo que ocurre al incumplir "
         "(<b>puntos</b>, <b>quién responde</b> y <b>delitos contra la seguridad vial</b>)."),
        ("The exam loves <b>numbers</b>: minimum ages (14, 15, 16, 18, 20, 21), <b>750 kg</b>, <b>3,500 / 4,250 kg</b>, deadlines (<b>10, 15 and 30 days</b>), points (<b>8, 12, 15</b>), and the ITV calendar.",
         "El examen pregunta sobre todo <b>cifras</b>: edades mínimas (14, 15, 16, 18, 20, 21), <b>750 kg</b>, <b>3.500 / 4.250 kg</b>, plazos (<b>10, 15 y 30 días</b>), puntos (<b>8, 12, 15</b>) y el calendario de la ITV."),
        ("The sections follow the order of your course’s Topic 9. Spanish exam terms are in <i>italics</i> in the English text, and a glossary closes the topic.",
         "Los apartados siguen el orden del Tema 9 de tu curso. Al final hay un glosario español–inglés."),
    ]))

    # ---------------------------------------------------------------- 1. driver
    B.append(H2("1", "The driver’s documents", "Documentación del conductor"))
    B.append(P(
        "The driver must have their <b>driving licence</b> and the <b>vehicle’s documents</b>, <b>valid and in force</b>, and <b>show them</b> to the authorities or their agents when asked. They can be shown as the "
        "<b>physical original</b> (the format the DGT recommends, because it can be checked in any situation), a <b>certified photocopy</b>, or in <b>digital form</b> in the DGT’s <b>miDGT app</b>. "
        "The app is as valid as the paper document for traffic purposes, but <b>only in Spain</b>: abroad you must carry the physical documents.",
        "El conductor debe estar en <b>posesión de su permiso o licencia de conducción y de la documentación del vehículo</b>, <b>válida y vigente</b>, y <b>mostrarla a la autoridad</b> o a sus agentes cuando lo soliciten, "
        "en su <b>formato físico original</b> (el más recomendado por la DGT, porque permite verificarlo en cualquier situación), <b>fotocopia compulsada</b> o <b>digital</b> en la app <b>miDGT</b>. "
        "La app tiene la misma validez que el soporte físico a efectos de tráfico, pero <b>solo en territorio nacional</b>: en el extranjero hay que llevar los documentos en soporte físico."))
    B.append(P("Nobody may hold <b>more than one</b> driving licence issued by an EU member state. If they do, the one that applies is withdrawn.",
               "Nadie puede ser titular de <b>más de un</b> permiso o licencia expedido por un Estado miembro de la UE. Si fuese así, se le retirará el que proceda."))
    B.append(TABLE(
        [T("To get a driving licence you must…", "Para obtener el permiso de conducir hay que…")],
        [
            [T("Have the required <b>physical and mental fitness</b>. People with an illness or condition that prevents an ordinary licence may get an <b>extraordinary</b> one with restrictions "
               "(having to wear <b>glasses or hearing aids</b> does <b>not</b> make a licence extraordinary).",
               "<b>Reunir las aptitudes psicofísicas requeridas</b>. Quien padezca una enfermedad o deficiencia que le impida obtener uno ordinario podrá obtener uno <b>extraordinario</b> con restricciones "
               "(la obligación de usar <b>lentes o audífonos</b> <b>no</b> le hace perder su carácter ordinario).")],
            [T("Be declared <b>fit (apto)</b> by the Provincial Traffic Office (<i>Jefatura Provincial de Tráfico</i>) in the tests of <b>knowledge, skills, aptitudes and behaviour</b>. The office issues the licences and the temporary permits that stand in for them.",
               "Ser declarado <b>apto</b> por la Jefatura Provincial de Tráfico en las pruebas de <b>conocimientos, habilidades, aptitudes y comportamientos</b>. La Jefatura expide los permisos y las autorizaciones temporales que los sustituyan.")],
        ],
    ))
    B.append(BOX("trap", "Two rules that catch people out", "Dos normas que conviene recordar", [
        ("Using <b>unauthorised communication devices</b> in the licence tests (or helping someone use them) is a <b>very serious</b> offence: a <b>fine</b> and <b>no new attempt for six months</b>.",
         "Utilizar <b>dispositivos de intercomunicación no autorizados</b> en las pruebas (o colaborar en ello) es infracción <b>muy grave</b>: <b>multa</b> e <b>imposibilidad de presentarse durante seis meses</b>."),
        ("If illness, injury or anything else takes away the required fitness, you may <b>not drive until you recover it</b>. If the vehicle must be <b>adapted</b>, tell the Traffic Office, even if your licence is in force.",
         "Si por enfermedad, lesión u otra circunstancia se pierden las aptitudes, <b>no se podrá conducir hasta recuperarlas</b>. Si hay que <b>adaptar el vehículo</b>, se debe comunicar a la Jefatura, aunque el permiso esté en vigor."),
    ]))
    B.append(H3("1.1 Driving licences (licencias)", "1.1 Clases de licencias de conducción"))
    B.append(TABLE(
        [T("Licence", "Licencia"), T("Minimum age", "Edad mínima"), T("Lets you drive", "Permite conducir")],
        [
            [T("<b>LCM</b>", "<b>LCM</b>"), T("14", "14"), T("<b>Vehicles for people with reduced mobility</b>.", "<b>Vehículos para personas de movilidad reducida</b>.")],
            [T("<b>LVA</b>", "<b>LVA</b>"), T("16", "16"), T("<b>Self-propelled agricultural special vehicles</b> and their combinations, if their mass or size does not exceed the limits for ordinary vehicles, or their design speed is <b>≤ 45 km/h</b>.",
                                                          "<b>Vehículos especiales agrícolas autopropulsados</b> y sus conjuntos cuya masa o dimensiones no excedan los límites de los vehículos ordinarios o cuya velocidad máxima por construcción no exceda de <b>45 km/h</b>.")],
        ],
        widths=["14%", "16%", "70%"],
    ))
    B.append(H3("1.2 Driving permits (permisos)", "1.2 Clases de permisos de conducción"))
    B.append(FIG(licence_ages, "Minimum ages at a glance. A needs two years with A2; trikes over 15 kW need 21 even with an A or B.",
                 "Las edades mínimas de un vistazo. El A exige dos años de A2; los triciclos de más de 15 kW exigen 21 años, también con A o B."))
    B.append(TABLE(
        [T("Permit", "Permiso"), T("Age", "Edad"), T("Lets you drive", "Permite conducir")],
        [
            [T("<b>AM</b>", "<b>AM</b>"), T("15", "15"), T("<b>Mopeds</b> with two or three wheels and <b>light quadricycles</b>.", "<b>Ciclomotores</b> de dos o tres ruedas y <b>cuadriciclos ligeros</b>.")],
            [T("<b>A1</b>", "<b>A1</b>"), T("16", "16"),
             T("Motorcycles up to <b>125 cc</b>, <b>11 kW</b> (a little under 15 hp) and <b>0.1 kW/kg</b>. Also <b>motor tricycles up to 15 kW</b>, mopeds, light quadricycles and reduced-mobility vehicles.",
               "Motocicletas de <b>125 c.c.</b> como máximo, <b>11 kW</b> (algo menos de 15 CV) y <b>0,1 kW/kg</b>. También <b>triciclos de motor de hasta 15 kW</b>, ciclomotores, cuadriciclos ligeros y vehículos para personas de movilidad reducida.")],
            [T("<b>A2</b>", "<b>A2</b>"), T("18", "18"),
             T("Motorcycles up to <b>35 kW</b> and <b>0.2 kW/kg</b>, <b>not derived</b> from a vehicle with more than <b>twice</b> that power. Plus everything AM and A1 allow, and reduced-mobility vehicles.",
               "Motocicletas de hasta <b>35 kW</b> y <b>0,2 kW/kg</b>, <b>no derivadas</b> de un vehículo de más del <b>doble</b> de su potencia. Más todo lo de AM y A1, y vehículos de movilidad reducida.")],
            [T("<b>A</b>", "<b>A</b>"), T("20 (21 for trikes over 15 kW)", "20 (21 para triciclos de más de 15 kW)"),
             T("<b>All motorcycles</b> and motor tricycles, plus everything AM, A1 and A2 allow. You must have held an <b>A2 for at least two years</b> and pass a training course.",
               "<b>Motocicletas</b> y triciclos de motor, más todo lo de AM, A1 y A2. Hay que ser titular de un <b>A2 con al menos dos años</b> de experiencia y superar una formación.")],
        ],
        widths=["12%", "22%", "66%"],
    ))
    B.append(H3("The B licence", "El permiso B"))
    B.append(P("Minimum age <b>18</b>. It lets you drive:", "Edad mínima <b>18 años</b>. Permite conducir:"))
    B.append(TABLE(
        [T("Vehicle", "Vehículo"), T("Condition", "Condición")],
        [
            [T("<b>Automobiles</b>", "<b>Automóviles</b>"), T("Maximum authorised mass (MMA) <b>≤ 3,500 kg</b>, designed for <b>no more than eight passengers</b> besides the driver.", "MMA <b>≤ 3.500 kg</b>, diseñados para <b>no más de ocho pasajeros</b> además del conductor.")],
            [T("<b>Alternative-fuel goods vehicles</b>", "<b>Mercancías con combustibles alternativos</b>"),
             T("In Spain only, after holding B for <b>more than two years</b>: up to <b>4,250 kg</b> MMA without a trailer, if the mass over 3,500 kg comes only from the heavier propulsion system and the load capacity does not grow.",
               "Solo en territorio nacional y con <b>más de dos años</b> de antigüedad del permiso: hasta <b>4.250 kg</b> de MMA sin remolque, si el exceso sobre 3.500 kg procede solo del sistema de propulsión y no aumenta la capacidad de carga.")],
            [T("<b>Light trailer</b>", "<b>Remolque ligero</b>"), T("MMA up to <b>750 kg</b>.", "MMA hasta <b>750 kg</b>.")],
            [T("<b>Heavier trailer</b>", "<b>Remolque no ligero</b>"),
             T("Over 750 kg, if the <b>combination’s MMA is ≤ 4,250 kg</b>. If the combination is over <b>3,500 kg</b>, you need an extra skills test: the <b>B96</b> authorisation.",
               "De más de 750 kg, si la <b>MMA del conjunto no excede de 4.250 kg</b>. Si el conjunto supera <b>3.500 kg</b>, hay que superar una prueba: la autorización <b>B96</b>.")],
            [T("<b>Motor tricycles and quadricycles</b>", "<b>Triciclos y cuadriciclos de motor</b>"), T("Tricycles over <b>15 kW</b> only from age <b>21</b>.", "Los triciclos de más de <b>15 kW</b>, solo desde los <b>21 años</b>.")],
            [T("<b>Mopeds</b> and reduced-mobility vehicles", "<b>Ciclomotores</b> y vehículos de movilidad reducida"), T("Yes.", "Sí.")],
            [T("<b>Special vehicles</b>", "<b>Vehículos especiales</b>"),
             T("<b>Agricultural</b> ones; <b>non-agricultural</b> ones up to <b>40 km/h</b> and <b>3,500 kg</b> (above either, the licence for their mass is needed). At most <b>nine people</b>, driver included.",
               "<b>Agrícolas</b>; <b>no agrícolas</b> hasta <b>40 km/h</b> y <b>3.500 kg</b> (si exceden, el permiso que corresponda a su MMA). Como máximo <b>nueve personas</b>, incluido el conductor.")],
        ],
        widths=["30%", "70%"],
    ))
    B.append(BOX("key", "B and motorcycles", "El B y las motocicletas", [
        ("B does <b>not</b> let you drive motorcycles, with or without sidecar…", "El B <b>no</b> autoriza a conducir motocicletas, con o sin sidecar…"),
        ("…but after holding B for <b>more than three years</b> you may ride <b>A1 motorcycles (up to 125 cc)</b> <b>in Spain</b>.", "…pero con una antigüedad del B de <b>más de tres años</b> se pueden conducir <b>motocicletas del A1 (hasta 125 c.c.)</b> <b>en territorio nacional</b>."),
    ]))
    B.append(H3("1.3 Other permits", "1.3 Otros permisos"))
    B.append(TABLE(
        [T("Permit", "Permiso"), T("Lets you drive", "Permite conducir")],
        [
            [T("<b>B+E</b>", "<b>B+E</b>"), T("A B towing vehicle with a <b>trailer or semitrailer of MMA ≤ 3,500 kg</b>. Minimum age <b>18</b>.", "Un tractor del B con <b>remolque o semirremolque de MMA ≤ 3.500 kg</b>. Edad mínima <b>18 años</b>.")],
            [T("<b>C1, C</b>", "<b>C1, C</b>"), T("Automobiles over <b>3,500 kg</b> MMA (goods); they may tow a light trailer.", "Automóviles de MMA superior a <b>3.500 kg</b>; pueden arrastrar un remolque ligero.")],
            [T("<b>D1, D</b>", "<b>D1, D</b>"), T("Automobiles with <b>more than nine seats</b>, driver included; they may tow a light trailer.", "Automóviles de <b>más de nueve plazas</b>, incluido el conductor; pueden arrastrar un remolque ligero.")],
            [T("<b>C1+E, C+E, D1+E, D+E</b>", "<b>C1+E, C+E, D1+E, D+E</b>"), T("Those vehicles with <b>heavier (non-light) trailers</b>, under the set conditions.", "Esos vehículos con <b>remolques no ligeros</b>, en las condiciones que se impongan.")],
        ],
        widths=["24%", "76%"],
    ))
    B.append(H3("1.4 Validity and renewal", "1.4 Vigencia y prórroga"))
    B.append(TABLE(
        [T("AM, A1, A2, A, B and B+E", "AM, A1, A2, A, B y B+E"), T("Renew every…", "Se renuevan cada…")],
        [
            [T("Until the holder turns <b>65</b>", "Hasta que el titular cumpla <b>65 años</b>"), T("<b>10 years</b>", "<b>10 años</b>")],
            [T("From <b>65</b>", "A partir de <b>65 años</b>"), T("<b>5 years</b>", "<b>5 años</b>")],
        ],
        widths=["60%", "40%"],
    ))
    B.append(BOX("trap", "Renewal", "Prórroga", [
        ("These periods can be <b>shorter</b> if the holder has an illness that may get worse, even if it does not yet prevent the licence.", "Los periodos pueden <b>reducirse</b> si el titular padece una enfermedad que pueda agravarse, aunque de momento no impida la concesión o prórroga."),
        ("A licence is renewed if you still meet the requirements and have <b>not lost all your points</b>. An <b>expired</b> licence does <b>not</b> let you drive and is <b>withdrawn on the spot</b> (<i>intervención</i>) if used.",
         "Se prorroga si se conservan los requisitos y no se ha <b>perdido la totalidad de puntos</b>. Un permiso <b>caducado</b> <b>no</b> autoriza a conducir y su uso da lugar a su <b>intervención inmediata</b>."),
    ]))
    B.append(H3("1.5 Changes of details and duplicates", "1.5 Cambio de datos y duplicados"))
    B.append(TABLE(
        [T("Event", "Caso"), T("What to do", "Qué hacer")],
        [
            [T("Any <b>change of the details</b> on the licence", "Cualquier <b>variación de los datos</b> del permiso"), T("Tell the Traffic Office within <b>15 days</b>, to get a <b>duplicate</b>.", "Comunicarlo a la Jefatura en un plazo <b>máximo de 15 días</b> para que expida un <b>duplicado</b>.")],
            [T("<b>Theft, loss or damage</b> of the licence", "<b>Sustracción, extravío o deterioro</b>"), T("Also tell the Traffic Office for a duplicate, and <b>hand back the original</b> where applicable.", "También notificarlo para obtener un duplicado, y <b>devolver el original</b> en su caso.")],
        ],
        widths=["40%", "60%"],
    ))
    B.append(H3("1.6 New drivers", "1.6 Conductores noveles"))
    B.append(FIG(plates, "Plates: two on cars, one at the back of two-wheelers; trailers over 750 kg add their own red plate. The novice’s “L” goes at the rear left.",
                 "Placas: dos en los automóviles, una detrás en las de dos ruedas; los remolques de más de 750 kg añaden su placa roja. La «L» del novel va detrás a la izquierda."))
    B.append(E(
        "The novice plate V-13 (“L”)", "La señal V-13 («L»)",
        "Anyone who gets a driving licence <b>for the first time</b> must display the <b>V-13</b> during its <b>first year</b>. It is <b>retroreflective, green with a white “L”</b>, placed somewhere visible at the <b>rear left</b> "
        "(on motorcycles and three-wheelers, somewhere visible at the rear). If the novice’s licence is <b>withdrawn or suspended</b> in that time, the year is <b>extended</b> by the same period.",
        "Quien obtenga <b>por primera vez</b> un permiso debe llevar la <b>V-13</b> durante su <b>primer año</b> de vigencia. Es <b>reflectante, de fondo verde con la letra «L» en blanco</b>, en un lugar visible de la <b>parte posterior izquierda</b> "
        "(en motocicletas y vehículos de tres ruedas, en un sitio visible de la parte posterior). Si al novel le <b>intervienen o suspenden</b> el permiso, el año se <b>amplía</b> en ese mismo periodo.",
        pills_=[T("first year", "primer año"), T("rear left", "detrás a la izquierda")]))
    B.append(H3("1.7 Nullity, loss of validity and suspension", "1.7 Nulidad o lesividad y pérdida de vigencia"))
    B.append(TABLE(
        [T("Measure", "Medida"), T("When", "Cuándo")],
        [
            [T("<b>Declared null or harmful</b> (<i>nulidad o lesividad</i>)", "<b>Declaración de nulidad o lesividad</b>"), T("Through a judicial or administrative procedure.", "Mediante procedimiento judicial o administrativo.")],
            [T("<b>Loss of validity</b> (<i>pérdida de vigencia</i>)", "<b>Pérdida de vigencia</b>"),
             T("When the holder has <b>lost all their points</b> or no longer meets the <b>requirements</b> (knowledge, skills, aptitudes, behaviour). The Traffic Office notifies the decision within <b>six months</b> at most, with the steps and tests to recover it.",
               "Si el titular ha <b>perdido la totalidad de los puntos</b> o los <b>requisitos</b> (conocimientos, habilidades, aptitudes y comportamientos). La Jefatura notifica la resolución en un plazo <b>máximo de seis meses</b>, con los trámites y pruebas para recuperarlo.")],
            [T("<b>Precautionary suspension</b> (<i>suspensión cautelar</i>)", "<b>Suspensión cautelar</b>"),
             T("When keeping the licence is a <b>serious danger</b> to road safety or clearly harms the <b>public interest</b>. The licence is <b>withdrawn at once</b>. Driving during the suspension counts as <b>driving with a licence suspended by sanction</b>.",
               "Cuando su mantenimiento entrañe un <b>grave peligro</b> para la seguridad del tráfico o perjudique notoriamente el <b>interés público</b>. Se ordena su <b>intervención inmediata</b>. Conducir durante la suspensión cautelar equivale a conducir con la autorización <b>suspendida por sanción</b>.")],
        ],
        widths=["30%", "70%"],
    ))

    # ---------------------------------------------------------------- 2. vehicle
    B.append(H2("2", "The vehicle’s documents", "Documentación del vehículo"))
    B.append(P(
        "To drive on public roads, the vehicle must carry the <b>originals or duly certified photocopies</b> of: the <b>registration certificate</b> (<i>permiso de circulación</i>); "
        "and the <b>ITV card</b> with its inspections up to date (a <b>certificate of characteristics</b> for some mopeds) plus the <b>last inspection report</b>, if it has already been to the ITV.",
        "Para circular, en el vehículo deben llevarse los <b>originales o fotocopias debidamente cotejadas</b> de: el <b>permiso de circulación</b>; "
        "y la <b>tarjeta de inspección técnica</b> al corriente de las inspecciones (el <b>certificado de características</b> en algunos ciclomotores) y el <b>último informe de inspección</b>, si ya ha pasado la ITV."))
    B.append(H3("2.1 The registration certificate (permiso de circulación)", "2.1 El permiso de circulación"))
    B.append(P(
        "It <b>authorises the vehicle to be driven</b>. The Traffic Office issues it after checking that the vehicle meets the conditions. It is <b>compulsory for every motor vehicle</b>, and for <b>trailers and semitrailers over 750 kg</b> MMA. "
        "It shows the <b>plate number, registration date, owner’s name and address, make, model, MMA, number of seats and use</b>.",
        "<b>Autoriza la circulación del vehículo</b>. Lo expide la Jefatura tras comprobar que reúne las condiciones. Es <b>obligatorio para todos los vehículos de motor</b> y para los <b>remolques y semirremolques de más de 750 kg</b> de MMA. "
        "Figuran la <b>matrícula, fecha de matriculación, nombre y domicilio del titular, marca, modelo, MMA, número de plazas y servicio</b>."))
    B.append(TABLE(
        [T("Change", "Cambio"), T("Who and when", "Quién y cuándo")],
        [
            [T("Owner’s <b>name, surname or address</b> (no change of owner)", "<b>Nombre, apellidos o domicilio</b> del titular (sin cambio de titularidad)"), T("Owner tells the Traffic Office within <b>15 days</b>.", "El titular lo comunica a la Jefatura en <b>15 días</b>.")],
            [T("<b>Sale</b> (change of owner)", "<b>Transmisión</b> (venta)"),
             T("The <b>seller</b> notifies within <b>10 days</b>. The <b>buyer</b> applies for the new certificate within <b>30 days</b>; otherwise the vehicle may not be driven and is <b>immobilised</b>.",
               "El <b>vendedor</b> lo notifica en un plazo máximo de <b>10 días</b>. El <b>comprador</b> solicita la renovación del permiso de circulación en <b>30 días</b>; si no, el vehículo no puede circular y se ordena su <b>inmovilización</b>.")],
        ],
        widths=["40%", "60%"],
    ))
    B.append(TABLE(
        [T("Registration and number plates", "Matriculación y placas")],
        [
            [T("Must be <b>registered</b> and carry plates: <b>motor vehicles, mopeds</b>, and <b>trailers and semitrailers over 750 kg</b>. <b>Light trailers</b> (≤ 750 kg) are <b>not</b> registered.",
               "Deben estar <b>matriculados</b> y llevar placas: <b>vehículos de motor, ciclomotores</b> y <b>remolques y semirremolques de más de 750 kg</b>. Los <b>ligeros</b> (≤ 750 kg) <b>no</b> se matriculan.")],
            [T("<b>Automobiles</b> (not motorcycles): <b>one plate in front and one behind</b>, white background with black letters and numbers.", "<b>Automóviles</b> (salvo motos): <b>una delante y otra detrás</b>, fondo blanco con letras y números negros.")],
            [T("<b>Motorcycles, mopeds and self-propelled special vehicles</b>: <b>one plate, at the rear</b>.", "<b>Motocicletas, ciclomotores y vehículos especiales autopropulsados</b>: <b>una sola placa, detrás</b>.")],
            [T("Trailer <b>up to 750 kg</b>: <b>one plate</b>, the same as the <b>towing vehicle’s</b>, in the <b>centre or on the left</b>.", "Remolque <b>hasta 750 kg</b>: <b>una placa</b>, igual que la del <b>vehículo tractor</b>, en el <b>centro o a la izquierda</b>.")],
            [T("Trailer <b>over 750 kg</b>: <b>two plates</b>: the towing vehicle’s on the <b>right</b>, and its own <b>red</b> plate in the middle.", "Remolque de <b>más de 750 kg</b>: <b>dos placas</b>: la del tractor a la <b>derecha</b> y otra de <b>fondo rojo</b>, propia del remolque, en el plano longitudinal medio.")],
            [T("The <b>driver</b> must make sure nothing makes the plates hard to read.", "El <b>conductor</b> debe verificar que nada impida o dificulte su lectura.")],
        ],
    ))
    B.append(H3("2.2 The ITV card and inspections", "2.2 La tarjeta de inspección técnica (ITV)"))
    B.append(P(
        "The <b>ITV card</b> certifies that the vehicle meets the <b>technical conditions</b> to be driven. You may pass the inspection <b>up to 30 calendar days early</b>: the new period still starts when the old one ends. "
        "<b>Light trailers</b> (≤ 750 kg) have <b>no periodic ITV</b>, but they do need an ITV card. The front of the card records the <b>inspections</b>; the back holds the <b>technical data</b> "
        "(chassis number, make, type, tare, seats, power, towable mass…) and any <b>major modifications</b> (tow bar, extra lights…).",
        "La <b>tarjeta ITV</b> acredita que el vehículo reúne las <b>condiciones técnicas</b> para circular. La inspección se puede pasar <b>hasta 30 días naturales antes</b>: la nueva vigencia empieza cuando termina la anterior. "
        "Los <b>remolques ligeros</b> (≤ 750 kg) <b>no pasan ITV periódica</b>, pero sí tienen tarjeta. En el anverso, las <b>inspecciones</b>; en el reverso, las <b>características técnicas</b> "
        "(bastidor, marca, tipo, tara, asientos, potencia, masa remolcable…) y las <b>reformas de importancia</b> (enganche, faros adicionales…)."))
    B.append(BOX("key", "e-ITV (electronic card)", "e-ITV (tarjeta en soporte electrónico)", [
        ("Issued by the <b>manufacturers</b>, it replaces the paper card and holds the vehicle’s data (make, model, chassis number, power, mass, seats, plate…), plus the results of compulsory ITVs and inspections after modifications. A paper copy is also issued.",
         "La emiten los <b>fabricantes</b> y sustituye a la tarjeta clásica: datos del vehículo (marca, modelo, bastidor, potencia, peso, plazas, matrícula…) y los resultados de las ITV obligatorias y tras reformas. También se expide una copia en papel."),
        ("It carries the <b>NIVE</b> (vehicle identification number), <b>32 characters</b> long: the car’s “ID card”.", "Incluye el <b>NIVE</b> (Número de Identificación de Vehículo), de <b>32 dígitos</b>: el «DNI del coche»."),
    ]))
    B.append(H3("How often", "Frecuencia de la ITV"))
    B.append(P("The vehicle’s age counts from the <b>registration date</b> on its registration certificate. For the 2nd and later inspections, check the <b>ITV card</b> or the <b>V-19 sticker</b> on the windscreen.",
               "La antigüedad se cuenta desde la <b>fecha de matriculación</b> del permiso de circulación. Para la 2.ª ITV y siguientes, se consulta la <b>tarjeta ITV</b> o el <b>distintivo V-19</b> del parabrisas."))
    B.append(FIG(itv_chart, "Read across: each bar shows how often that vehicle goes to the ITV as it gets older.", "Lee cada barra: cada cuánto pasa la ITV ese vehículo según envejece."))
    B.append(TABLE(
        [T("Vehicle", "Vehículo"), T("Frequency", "Frecuencia")],
        [
            [T("Two-wheel <b>mopeds</b>", "<b>Ciclomotores</b> de dos ruedas"), T("Exempt up to <b>3 years</b>; then every <b>2 years</b>.", "Exentos hasta <b>3 años</b>; después, cada <b>2 años</b>.")],
            [T("Three-wheel mopeds, light quadricycles, <b>motorcycles</b>, three-wheelers, quadricycles, quads", "Ciclomotores de tres ruedas, cuadriciclos ligeros, <b>motocicletas</b>, tres ruedas, cuadriciclos y quads"),
             T("Exempt up to <b>4 years</b>; then every <b>2 years</b>.", "Exentos hasta <b>4 años</b>; después, cada <b>2 años</b>.")],
            [T("Private <b>cars</b> and motorhomes", "<b>Turismos</b> de uso privado y autocaravanas"), T("Exempt up to <b>4 years</b>; every <b>2 years</b> from 4 to 10; <b>every year</b> after 10.", "Exentos hasta <b>4 años</b>; cada <b>2 años</b> de 4 a 10; <b>cada año</b> después de 10.")],
            [T("Goods and mixed vehicles <b>≤ 3.5 t</b>", "Mercancías y mixtos de MMA <b>≤ 3,5 t</b>"),
             T("Exempt up to <b>2 years</b>; every 2 years from 2 to 6; every year from 6 to 10; <b>every 6 months</b> after 10.", "Exentos hasta <b>2 años</b>; cada 2 años de 2 a 6; cada año de 6 a 10; <b>cada 6 meses</b> después de 10.")],
            [T("Trailers <b>over 750 kg</b>", "Remolques de MMA <b>superior a 750 kg</b>"), T("<b>Every year</b> up to 10 years; every <b>6 months</b> after.", "<b>Cada año</b> hasta 10 años; cada <b>6 meses</b> después.")],
            [T("Towed <b>caravans</b> 750 kg – 3.5 t", "<b>Caravanas</b> remolcadas de 750 kg a 3,5 t"), T("Exempt up to <b>6 years</b>; then every <b>2 years</b>.", "Exentas hasta <b>6 años</b>; después, cada <b>2 años</b>.")],
            [T("Goods vehicles <b>over 3.5 t</b> (and trailers over 750 kg except towed caravans)", "Mercancías de MMA <b>superior a 3,5 t</b> (y remolques de más de 750 kg salvo caravanas)"),
             T("<b>Every year</b> up to 10 years; every <b>6 months</b> after.", "<b>Cada año</b> hasta 10 años; cada <b>6 meses</b> después.")],
        ],
        widths=["46%", "54%"],
        cls="small",
    ))
    B.append(BOX("key", "The V-19 sticker", "Colocación del distintivo V-19", [
        ("<b>Motor vehicles</b>: in the <b>top right corner of the windscreen</b>, on the inside.", "<b>Vehículos de motor</b>: en el <b>ángulo superior derecho del parabrisas</b>, por su cara interior."),
        ("<b>Trailers and semitrailers</b>: somewhere <b>visible</b>.", "<b>Remolques y semirremolques</b>: en un <b>lugar visible</b>."),
    ]))
    B.append(BOX("trap", "Major changes and overdue ITVs", "Reformas e ITV caducada", [
        ("After a <b>major modification</b>, the vehicle needs an <b>extraordinary inspection</b> before it is driven again.", "Tras una <b>reforma de importancia</b>, hay que pasar una <b>inspección técnica extraordinaria</b> antes de volver a circular."),
        ("Driving with the ITV <b>out of date</b>: the agent reports it, <b>keeps the registration certificate</b> and gives the driver a <b>temporary slip</b> (<i>volante</i>) with <b>10 days</b> to pass the ITV. Otherwise the vehicle is <b>sealed off</b> (<i>precinto</i>).",
         "Circular sin la ITV al corriente: el agente denuncia, <b>interviene el permiso de circulación</b> y entrega un <b>volante</b> con <b>10 días</b> para pasar la ITV. Si no, se acuerda el <b>precinto</b> del vehículo."),
    ]))
    B.append(TABLE(
        [T("Result of the periodic ITV", "Resultado de la ITV periódica"), T("Meaning", "Significado")],
        [
            [T("<b>Favourable</b>", "<b>Favorable</b>"), T("Fit to drive. The station notes the validity on the card and gives the <b>V-19</b>, showing the date of the next inspection.", "En condiciones de circular. El centro anota la validez en la tarjeta y entrega el <b>V-19</b> con la fecha de la próxima inspección.")],
            [T("<b>Unfavourable</b>", "<b>Desfavorable</b>"), T("Defects of <b>some importance</b>: it may only be driven <b>to the workshop</b> and <b>back to the ITV</b>.", "Defectos de <b>cierta importancia</b>: solo puede circular <b>para ir al taller</b> y <b>volver a la ITV</b>.")],
            [T("<b>Negative</b>", "<b>Negativa</b>"), T("Defects that are a <b>danger on the road</b>: it may <b>not</b> be driven; it leaves the station by other means (<b>tow truck</b>).", "Defectos que son un <b>peligro en la vía</b>: <b>no</b> puede circular; se traslada por medios ajenos (<b>grúa</b>).")],
        ],
        widths=["26%", "74%"],
    ))
    B.append(P(
        "After an unfavourable or negative result, the owner has <b>up to 2 months</b> to repair the vehicle and bring it back (your course says “less than 2 months”; the ITV decree says “no more than two months”). If it is not brought back in time, the station tells the Traffic Office, proposing to <b>deregister</b> it (<i>baja</i>). "
        "You may <b>choose any ITV station</b>, both for the first inspection and after repairs.",
        "Con resultado desfavorable o negativo, el titular tiene un plazo de <b>hasta 2 meses</b> para repararlo y volver a presentarlo (tu curso dice «inferior a 2 meses»; el decreto de ITV, «no superior a dos meses»). Si no se presenta, el centro lo comunica a la Jefatura proponiendo la <b>baja</b> del vehículo. "
        "Hay <b>libertad de elección de estación ITV</b>, tanto para la primera inspección como tras subsanar los defectos."))
    B.append(H3("2.3 Compulsory insurance", "2.3 Seguro obligatorio"))
    B.append(P(
        "The compulsory <b>third-party liability</b> insurance covers, within certain limits, the <b>driver’s civil liability</b> for <b>injuries to people</b> and <b>damage to property</b> caused in road traffic. "
        "Other cover can be added freely. The <b>owner</b> should take it out; whoever signs it is the <b>policyholder</b> (<i>tomador</i>).",
        "El seguro de responsabilidad civil de suscripción obligatoria cubre, dentro de ciertos límites, la <b>responsabilidad civil del conductor</b> por <b>daños a las personas</b> (corporales) <b>o a los bienes</b> (materiales) causados con motivo de la circulación. "
        "Se pueden contratar otras coberturas. Debe concertarlo el <b>propietario</b>; quien lo contrata es el <b>tomador</b>."))
    B.append(TABLE(
        [T("Must be insured", "Deben estar asegurados")],
        [
            [T("<b>All motor vehicles</b> (cars, motorcycles, lorries…), <b>mopeds</b>, and <b>trailers and semitrailers over 750 kg</b>.", "<b>Todos los vehículos de motor</b> (turismos, motos, camiones…), los <b>ciclomotores</b> y los <b>remolques y semirremolques de MMA superior a 750 kg</b>.")],
            [T("<b>Not compulsory</b>: trailers, semitrailers and towed special machines of <b>750 kg or less</b>.", "<b>No hay obligación</b>: remolques, semirremolques y máquinas remolcadas especiales de <b>750 kg o menos</b>.")],
        ],
    ))
    B.append(BOX("key", "New in 2026: e-scooters (VMP)", "Novedad 2026: patinetes (VMP)", [
        ("Since <b>2 January 2026</b> (Ley 5/2025), <b>personal mobility vehicles</b> such as e-scooters also need <b>third-party insurance</b>. To get it, the owner must first <b>register</b> the VMP with the DGT (register opened in January 2026), and it carries an identification label.",
         "Desde el <b>2 de enero de 2026</b> (Ley 5/2025), los <b>vehículos de movilidad personal</b> (patinetes) también necesitan <b>seguro obligatorio</b>. Para contratarlo hay que <b>inscribir</b> antes el VMP en la DGT (registro en marcha desde enero de 2026), y lleva una etiqueta identificativa."),
        ("VMP without a circulation certificate (sold before 22 January 2024) may be used until <b>21 January 2027</b>, registered and insured; from 22 January 2027 only certified ones.", "Los VMP sin certificado de circulación (comercializados antes del 22 de enero de 2024) pueden circular hasta el <b>21 de enero de 2027</b>, inscritos y asegurados; desde el 22 de enero de 2027, solo los certificados."),
    ]))
    B.append(FIG(insurance_grid, "The guilty driver’s own injuries and own vehicle are never paid by the compulsory insurance; other people’s injuries and property are.",
                 "Las lesiones del propio conductor culpable y su vehículo nunca las paga el seguro obligatorio; los daños a otras personas y sus bienes, sí."))
    B.append(TABLE(
        [T("Covered", "Quedan cubiertos"), T("Not covered", "No quedan cubiertos")],
        [
            [T("<b>Injuries to people</b>, except those due <b>only</b> to the victim’s own conduct or negligence, or to <b>force majeure</b> unrelated to driving or the vehicle (vehicle <b>defects or breakages</b> are <b>not</b> force majeure).",
               "<b>Daños a las personas</b>, salvo los debidos <b>únicamente</b> a la conducta o negligencia del <b>perjudicado</b>, o a <b>fuerza mayor</b> extraña a la conducción o al vehículo (los <b>defectos o roturas</b> del vehículo <b>no</b> son fuerza mayor)."),
             T("The <b>driver’s own injuries</b>.", "Los <b>daños personales del conductor</b> del vehículo asegurado.")],
            [T("<b>Damage to third parties’ property</b> when the driver is civilly liable.", "<b>Daños a los bienes de terceros</b> cuando resulte civilmente responsable."),
             T("Damage to the <b>insured vehicle</b>, the <b>goods it carries</b>, and property of the <b>policyholder, insured, owner, driver</b>, their <b>spouse or relatives</b> up to the third degree.",
               "Los daños al <b>vehículo asegurado</b>, a las <b>cosas transportadas</b> y a los bienes del <b>tomador, asegurado, propietario, conductor</b>, su <b>cónyuge o parientes</b> hasta el tercer grado.")],
            [T("", ""), T("Damage caused by a <b>stolen vehicle</b> or by driving under <b>alcohol or drugs</b> (see the note below).", "Los daños causados por un <b>vehículo robado</b> o conduciendo bajo los efectos del <b>alcohol o drogas</b> (ver la nota).")],
        ],
        widths=["50%", "50%"],
    ))
    B.append(BOX("key", "Good to know: victims are still paid", "Conviene saberlo: las víctimas cobran igualmente", [
        ("If the driver was <b>drunk or on drugs</b>, the insurer pays the victims and can then <b>claim the money back from the driver</b>.", "Si el conductor iba <b>bajo los efectos del alcohol o drogas</b>, la aseguradora indemniza a las víctimas y después puede <b>repetir contra el conductor</b>."),
        ("If the vehicle was <b>stolen</b>, the victims are paid by the <b>Consorcio de Compensación de Seguros</b>.", "Si el vehículo era <b>robado</b>, a las víctimas las indemniza el <b>Consorcio de Compensación de Seguros</b>."),
    ]))
    B.append(TABLE(
        [T("Topic", "Tema"), T("Rule", "Norma")],
        [
            [T("<b>Proof of insurance</b>", "<b>Acreditar el seguro</b>"), T("Agents check the <b>FIVA</b> (insured-vehicles database). If that is not possible, the driver shows the <b>receipt</b> or proof of cover.", "Los agentes consultan el <b>Fichero Informativo de Vehículos Asegurados (FIVA)</b>. Si no es posible, el conductor presenta el <b>recibo</b> o justificante.")],
            [T("<b>Uninsured vehicle</b>", "<b>Vehículo no asegurado</b>"), T("<b>Banned from the road</b>, <b>impounded or sealed</b>, and a <b>fine</b>.", "<b>Prohibición de circular</b>, <b>depósito o precinto</b> del vehículo y <b>sanción económica</b>.")],
            [T("<b>Accident report form</b>", "<b>Declaración amistosa de accidente</b>"),
             T("The insurer provides the <b>declaración amistosa</b> (“parte”) to speed up payment for damage. The driver sends it to <b>their own insurer</b>. "
               "The Insurance Contract Act (art. 16) gives <b>7 days</b> to report the accident unless the policy allows longer (your course says 15).",
               "La aseguradora facilita la <b>declaración amistosa</b> («parte») para agilizar las indemnizaciones; el conductor la entrega a <b>su propia aseguradora</b>. "
               "La Ley de Contrato de Seguro (art. 16) da <b>7 días</b> para comunicar el siniestro salvo que la póliza fije más (tu curso indica 15).")],
            [T("<b>Where to fill it in</b>", "<b>Dónde rellenarlo</b>"), T("<b>Never on the road</b> itself: in a <b>safe place off the road</b>.", "<b>Prohibido en la plataforma</b> de circulación: en un <b>lugar seguro fuera de la vía</b>.")],
        ],
        widths=["26%", "74%"],
    ))

    # ---------------------------------------------------------------- 3. points
    B.append(H2("3", "The points licence", "Permiso por puntos"))
    B.append(H3("3.1 How many points do I have?", "3.1 ¿Cuántos puntos tengo?"))
    B.append(TABLE(
        [T("Situation", "Situación"), T("Points", "Puntos")],
        [
            [T("Licence held for <b>more than 2 years</b> (or 2 years without losing points)", "Permiso de <b>más de 2 años</b> (o 2 años sin perder puntos)"), T("<b>12</b>", "<b>12</b>")],
            [T("Licence held for <b>2 years or less</b>, unless you already held another licence for more than 2 years", "Permiso de <b>2 años o menos</b>, salvo que ya fuera titular de otro con más de 2 años"), T("<b>8</b>", "<b>8</b>")],
            [T("Licence <b>obtained again</b> after losing all the points", "Permiso <b>obtenido de nuevo</b> tras perder todos los puntos"), T("<b>8</b>", "<b>8</b>")],
            [T("<b>Bonus</b>: with all your points and no firm sanction, <b>+2</b> after 3 years, then <b>+1</b> after 3 more", "<b>Bonificación</b>: con todos los puntos y sin sanción firme, <b>+2</b> a los 3 años y <b>+1</b> a los 3 siguientes"), T("up to <b>15</b>", "hasta <b>15</b>")],
        ],
        widths=["78%", "22%"],
    ))
    B.append(FIG(points_path, "A new driver who never loses a point goes from 8 to 12, then 14, then the maximum of 15.",
                 "Un conductor novel que nunca pierde puntos pasa de 8 a 12, después a 14 y al máximo de 15."))
    B.append(TABLE(
        [T("Rule", "Norma")],
        [
            [T("The points credit is <b>one single credit</b> for all the licences the driver holds.", "El crédito de puntos es <b>único</b> para todas las autorizaciones del conductor.")],
            [T("Points are lost for each <b>firm administrative sanction</b> for a <b>serious or very serious</b> offence that carries points.", "Se pierden por cada <b>sanción firme en vía administrativa</b> por infracciones <b>graves o muy graves</b> que lleven aparejada la pérdida de puntos.")],
            [T("You lose <b>at most 8 points in one day</b>, unless one of the offences is <b>very serious</b>: then you lose all the points that apply.", "No se pierden <b>más de 8 puntos en un solo día</b>, salvo que haya alguna infracción <b>muy grave</b>: entonces se pierden todos los que correspondan.")],
            [T("<b>Automatic recovery</b>: <b>2 years</b> without a firm sanction that takes points, and those who lost some points get back their <b>full initial 12</b>.", "<b>Recuperación automática</b>: tras <b>2 años</b> sin sanción firme con pérdida de puntos, quien perdió parte de ellos recupera el <b>crédito inicial de 12</b>.")],
        ],
    ))
    B.append(H3("3.2 Offences and points", "3.2 Infracciones y pérdida de puntos"))
    B.append(TABLE(
        [T("3 points (serious offences)", "3 puntos (infracciones graves)")],
        [
            [T("Making a <b>U-turn</b> against the rules.", "Efectuar el <b>cambio de sentido</b> incumpliendo las normas.")],
            [T("Driving with <b>headphones or earphones</b> connected to sound devices, with a <b>phone held between helmet and head</b>, or <b>handling</b> sat-navs, communication systems or phones in ways not allowed.",
               "Conducir con <b>cascos o auriculares</b> conectados a aparatos de sonido, con el <b>móvil sujeto entre el casco y la cabeza</b>, o <b>manipulando</b> navegadores, sistemas de comunicación o móviles en condiciones no previstas.")],
            [T("Driving with a <b>radar detector</b>.", "Conducir con <b>detectores de radar</b> o cinemómetros.")],
        ],
    ))
    B.append(TABLE(
        [T("4 points (serious or very serious offences)", "4 puntos (infracciones graves o muy graves)")],
        [
            [T("Driving with a licence that does <b>not cover</b> that vehicle.", "Conducir con un permiso que <b>no habilite</b> para ese vehículo.")],
            [T("Breaking <b>priority rules</b> and not stopping at a <b>STOP</b>, a <b>give way</b> or a <b>red light</b>.", "Incumplir la <b>prioridad de paso</b> y no detenerse en el <b>stop</b>, el <b>ceda el paso</b> o el <b>semáforo en rojo</b>.")],
            [T("<b>Overtaking</b> dangerously or hindering oncoming traffic, or overtaking where visibility is reduced.", "<b>Adelantar</b> poniendo en peligro o entorpeciendo a quienes vienen de frente, o con visibilidad reducida.")],
            [T("<b>Reversing</b> on motorways and autovías.", "<b>Marcha atrás</b> en autopistas y autovías.")],
            [T("Ignoring the <b>signs or orders</b> of the traffic authority or its agents.", "No respetar las <b>señales u órdenes</b> de la autoridad o de sus agentes.")],
            [T("Not keeping the <b>safety distance</b>.", "No mantener la <b>distancia de seguridad</b>.")],
            [T("Driving with a <b>suspended licence</b> or a vehicle whose use is forbidden.", "Conducir con la autorización <b>suspendida</b> o con prohibición de usar el vehículo.")],
            [T("Not using (properly) the <b>seat belt, child seat, helmet</b> or other protection. For child seats and passengers’ helmets, the <b>driver</b> is responsible.",
               "No usar (o mal) el <b>cinturón, sistemas de retención infantil, casco</b> y demás protecciones. Si es por la SRI o el casco del pasajero, el responsable es el <b>conductor</b>.")],
            [T("Alcohol <b>over 0.25 and up to 0.50 mg/l</b> in exhaled air (professionals and licences under 2 years: <b>over 0.15 and up to 0.30</b>).", "Alcohol de <b>más de 0,25 hasta 0,50 mg/l</b> en aire espirado (profesionales y permisos de menos de 2 años: <b>más de 0,15 hasta 0,30</b>).")],
        ],
    ))
    B.append(TABLE(
        [T("6 points (very serious offences)", "6 puntos (infracciones muy graves)")],
        [
            [T("Alcohol <b>over twice the limit</b>: <b>over 0.50 mg/l</b> (professionals and new drivers: <b>over 0.30</b>).", "Alcohol <b>superior al doble</b>: <b>más de 0,50 mg/l</b> (profesionales y noveles: <b>más de 0,30</b>).")],
            [T("Driving with <b>drugs</b> in the body.", "Conducir con presencia de <b>drogas</b> en el organismo.")],
            [T("<b>Refusing</b> alcohol or drug tests.", "<b>Negarse</b> a las pruebas de alcohol o drogas.")],
            [T("<b>Reckless</b> driving, driving the <b>wrong way</b>, or unauthorised <b>races</b>.", "Conducción <b>temeraria</b>, circular en <b>sentido contrario</b> o participar en <b>carreras</b> no autorizadas.")],
            [T("Vehicles fitted with <b>radar jammers</b> or anything that interferes with traffic enforcement.", "Vehículos con <b>inhibidores de radar</b> u otros mecanismos que interfieran en la vigilancia.")],
            [T("Exceeding <b>driving times</b> or cutting <b>rest times</b> by more than <b>50 %</b> (professional transport).", "Exceder en más del <b>50 %</b> los <b>tiempos de conducción</b> o reducir los de <b>descanso</b> (transporte).")],
            [T("Tampering with the <b>tachograph</b> or the <b>speed limiter</b>.", "Manipular el <b>tacógrafo</b> o el <b>limitador de velocidad</b>.")],
            [T("Using a <b>mobile phone held in the hand</b> while driving.", "Utilizar, <b>sujetando con la mano</b>, el <b>teléfono móvil</b> mientras se conduce.")],
            [T("<b>Throwing objects</b> onto or near the road that can cause fires, accidents or block traffic.", "<b>Arrojar objetos</b> a la vía o sus inmediaciones que puedan producir incendios, accidentes u obstaculizar la circulación.")],
            [T("<b>Overtaking cyclists</b> dangerously or <b>without the 1.5 m</b> minimum gap.", "<b>Adelantar a ciclistas</b> poniéndolos en peligro o <b>sin dejar 1,5 m</b>.")],
        ],
    ))
    B.append(H3("Speeding: fine and points", "Exceso de velocidad: multa y puntos"))
    B.append(TABLE(
        [T("Limit (km/h)", "Límite (km/h)"), T("100 € · 0 points", "100 € · 0 puntos"), T("300 € · 2 points", "300 € · 2 puntos"), T("400 € · 4 points", "400 € · 4 puntos"),
         T("500 € · 6 points", "500 € · 6 puntos"), T("600 € · 6 points (very serious)", "600 € · 6 puntos (muy grave)")],
        [[T(f"<b>{lim}</b>", f"<b>{lim}</b>")] + [T(f'<span style="white-space:nowrap">{c}</span>', f'<span style="white-space:nowrap">{c}</span>') for c in cells] for lim, cells in [
            (30, ["31–50", "51–60", "61–70", "71–80", "81+"]), (40, ["41–60", "61–70", "71–80", "81–90", "91+"]),
            (50, ["51–70", "71–80", "81–90", "91–100", "101+"]), (60, ["61–90", "91–110", "111–120", "121–130", "131+"]),
            (70, ["71–100", "101–120", "121–130", "131–140", "141+"]), (80, ["81–110", "111–130", "131–140", "141–150", "151+"]),
            (90, ["91–120", "121–140", "141–150", "151–160", "161+"]), (100, ["101–130", "131–150", "151–160", "161–170", "171+"]),
            (110, ["111–140", "141–160", "161–170", "171–180", "181+"]), (120, ["121–150", "151–170", "171–180", "181–190", "191+"])]],
        widths=["14%", "17%", "17%", "17%", "17%", "18%"],
        cls="small",
    ))
    B.append(H3("3.3 Road-safety courses", "3.3 Cursos de sensibilización y reeducación vial"))
    B.append(TABLE(
        [T("Course", "Curso"), T("Rule", "Norma")],
        [
            [T("<b>Partial recovery</b> (10 hours)", "<b>Recuperación parcial</b> (10 horas)"),
             T("Passing it gives back <b>up to 4 points</b> (never more than you lost). Only <b>once every 2 years</b> (professional drivers, once a year).", "Permite recuperar <b>hasta 4 puntos</b> (nunca más de los perdidos). Solo <b>una vez cada 2 años</b> (profesionales, una vez al año).")],
            [T("<b>Getting the licence back</b> (20 hours)", "<b>Recuperación del permiso</b> (20 horas)"),
             T("Pass the course <b>and a written test</b> at the Traffic Office. Also needed after a court ban of <b>more than 2 years</b> (only the course if the ban is shorter). "
               "The licence returns in the <b>same class and seniority</b>, with <b>8 points</b>.",
               "Superar el curso <b>y una prueba tipo test</b> en la Jefatura. También tras una condena de privación del derecho a conducir de <b>más de 2 años</b> (solo el curso si es inferior). "
               "El permiso será de la <b>misma clase y antigüedad</b>, con <b>8 puntos</b>.")],
            [T("<b>Waiting time</b>", "<b>Plazo de espera</b>"),
             T("After losing the licence for the <b>first time</b>, wait <b>6 months</b> (3 for professionals) before doing the course. <b>Doubled</b> if all points are lost again within the next 3 years.",
               "Tras perderlo por <b>primera vez</b>, hay que esperar <b>6 meses</b> (3 los profesionales) para hacer el curso. Se <b>duplica</b> si se vuelven a perder todos los puntos en los tres años siguientes.")],
            [T("<b>Safe and efficient driving</b> (<i>conducción segura y eficiente</i>, CCSE)", "<b>Conducción segura y eficiente</b> (CCSE)"),
             T("Voluntary course, with separate programmes for cars and for motorcycles. Passing it gives <b>2 extra points</b>, up to the maximum of <b>15</b>; at most one course of each type every 2 years.",
               "Curso voluntario, con programas distintos para turismos y para motocicletas. Superarlo bonifica con <b>2 puntos</b>, hasta el máximo de <b>15</b>; como máximo un curso de cada tipo cada 2 años.")],
        ],
        widths=["26%", "74%"],
    ))

    # ---------------------------------------------------------------- 4. liability
    B.append(H2("4", "Who is liable for an offence", "Responsabilidad de las infracciones"))
    B.append(P("Liability falls <b>directly on the person who commits</b> the offence, <b>except</b>:", "La responsabilidad recae <b>directamente en el autor</b> del hecho, <b>excepto</b>:"))
    B.append(TABLE(
        [T("Case", "Caso"), T("Who answers", "Quién responde")],
        [
            [T("A <b>passenger without a helmet</b>, or a passenger <b>under the minimum age</b>, on a motorcycle or moped", "<b>Pasajero sin casco</b>, o pasajero <b>sin la edad mínima</b>, en moto o ciclomotor"), T("The <b>driver</b>.", "El <b>conductor</b>.")],
            [T("A child <b>without a child restraint</b>", "Menor <b>sin sistema de retención infantil</b>"), T("The <b>driver</b>, except professional drivers of public transport services.", "El <b>conductor</b>, salvo conductores profesionales de servicio público a terceros.")],
            [T("Offence committed by someone <b>under 18</b>", "Hechos cometidos por un <b>menor de 18 años</b>"), T("The <b>parents or guardians</b> are <b>jointly liable</b> for the fine.", "Los <b>padres o tutores</b> son <b>responsables solidarios</b> de la multa.")],
            [T("Vehicle <b>documents</b>, <b>periodic inspections</b>, or <b>condition</b> affecting safety", "<b>Documentación</b> del vehículo, <b>inspecciones periódicas</b> o <b>estado de conservación</b> que afecte a la seguridad"), T("The <b>owner</b> (<i>titular</i>).", "El <b>titular</b>.")],
        ],
        widths=["58%", "42%"],
    ))
    B.append(P(
        "The <b>owner must identify the driver</b> at the time of an offence. If the vehicle was not stopped and has a registered <b>habitual driver</b>, that driver is liable, unless they prove someone else was driving or the vehicle had been stolen.",
        "El <b>titular</b> tiene la obligación de <b>identificar al conductor</b> cuando se comete una infracción. Si no se detuvo el vehículo y tiene un <b>conductor habitual</b> designado, la responsabilidad recae en él, salvo que acredite que conducía otro o la sustracción del vehículo."))
    B.append(BOX("key", "New since 1 October 2026: owners without a licence", "Novedad desde el 1 de octubre de 2026: titulares sin permiso", [
        ("The <b>habitual driver</b> (<i>conductor habitual</i>) is the person, with a licence and with their consent, whom the owner registers with the DGT as the one who usually drives the vehicle.",
         "El <b>conductor habitual</b> es la persona, con permiso y con su consentimiento, que el titular comunica a la DGT como quien conduce el vehículo de forma usual."),
        ("If a person <b>without a driving licence</b> registers a vehicle in their name (for example, a parent who buys it for a son or daughter), naming a habitual driver is now <b>compulsory</b> (RD 518/2026).",
         "Si una persona <b>sin permiso de conducción</b> matricula un vehículo a su nombre (por ejemplo, un padre que lo compra para su hijo o hija), designar un conductor habitual es ahora <b>obligatorio</b> (RD 518/2026)."),
    ]))
    B.append(H3("4.1 Road-safety crimes in the Penal Code", "4.1 Delitos contra la seguridad vial del Código Penal"))
    B.append(TABLE(
        [T("Crime", "Delito"), T("Prison", "Prisión"), T("Fine", "Multa"), T("Community work", "Trabajos comunidad"), T("Licence ban", "Retirada del permiso")],
        [
            [T("<b>Speeding</b> by more than <b>60 km/h in town</b> or <b>80 km/h out of town</b>", "<b>Velocidad</b>: superarla en <b>60 km/h en vía urbana</b> u <b>80 km/h en interurbana</b>"), T("3–6 months", "3 a 6 meses"), T("6–12 months", "6 a 12 meses"), T("31–90 days", "31 a 90 días"), T("1–4 years", "1 a 4 años")],
            [T("Driving under <b>drugs</b>, or alcohol over <b>0.60 mg/l</b> in air (<b>1.2 g/l</b> in blood) *", "Bajo la influencia de <b>drogas</b> o alcohol superior a <b>0,60 mg/l</b> en aire (<b>1,2 g/l</b> en sangre) *"), T("3–6 months", "3 a 6 meses"), T("6–12 months", "6 a 12 meses"), T("31–90 days", "31 a 90 días"), T("1–4 years", "1 a 4 años")],
            [T("<b>Refusing</b> alcohol and drug tests", "<b>Negarse</b> a las pruebas de alcohol y drogas"), T("6 months–1 year", "6 meses a 1 año"), T("—", "—"), T("—", "—"), T("1–4 years", "1 a 4 años")],
            [T("<b>Reckless driving</b> endangering lives or safety *", "<b>Conducción temeraria</b> poniendo en peligro la vida o integridad *"), T("6 months–2 years", "6 meses a 2 años"), T("—", "—"), T("—", "—"), T("1–6 years", "1 a 6 años")],
            [T("Driving with <b>manifest contempt for others’ lives</b>, endangering them *", "Con <b>manifiesto desprecio por la vida</b> de los demás, poniéndola en peligro *"), T("2–5 years", "2 a 5 años"), T("12–24 months", "12 a 24 meses"), T("—", "—"), T("6–10 years", "6 a 10 años")],
            [T("Same contempt, <b>without</b> endangering anyone", "Igual, <b>sin</b> poner en peligro a nadie"), T("1–2 years", "1 a 2 años"), T("6–12 months", "6 a 12 meses"), T("—", "—"), T("6–10 years", "6 a 10 años")],
            [T("<b>Driving without a licence</b>: all points lost, court ban, or never obtained", "<b>Conducir sin carné</b>: pérdida total de puntos, privación judicial o no haberlo obtenido nunca"), T("3–6 months", "3 a 6 meses"), T("12–24 months", "12 a 24 meses"), T("31–90 days", "31 a 90 días"), T("—", "—")],
            [T("Creating a <b>serious risk</b>: obstacles, slippery or flammable spills, altering signs; or not restoring safety when obliged", "<b>Grave riesgo</b>: obstáculos, sustancias deslizantes o inflamables, alterar la señalización; o no restablecer la seguridad"),
             T("6 months–2 years", "6 meses a 2 años"), T("12–24 months", "12 a 24 meses"), T("10–40 days", "10 a 40 días"), T("—", "—")],
        ],
        widths=["36%", "16%", "15%", "15%", "18%"],
        cls="small",
    ))
    B.append(BOX("key", "Reading the table", "Cómo leer la tabla", [
        ("For speeding, alcohol/drugs and driving without a licence, prison, fine and community work are <b>alternatives</b>; the <b>licence ban comes on top</b> where shown.",
         "En velocidad, alcohol/drogas y conducir sin carné, prisión, multa y trabajos son <b>alternativos</b>; la <b>retirada del permiso se suma</b> donde se indica."),
        ("* If someone is <b>harmed</b>, only the most serious crime is punished, with the penalty in its <b>upper half</b>, plus compensation.", "* Si se produce un <b>resultado lesivo</b>, se aprecia solo la infracción más grave, con la pena en su <b>mitad superior</b> y el resarcimiento de la responsabilidad civil."),
        ("A ban of <b>more than 2 years</b> means the licence <b>loses its validity</b>.", "Una pena de <b>más de 2 años</b> supone la <b>pérdida de vigencia</b> del permiso."),
    ]))

    # ---------------------------------------------------------------- 5. traps
    B.append(H2("5", "Classic exam traps", "Trampas clásicas del examen"))
    B.append(BOX("trap", "Read twice", "Lee dos veces", [
        ("miDGT on your phone is valid <b>only in Spain</b>; abroad, carry the physical documents.", "La app miDGT vale <b>solo en España</b>; en el extranjero, documentos físicos."),
        ("Glasses or hearing aids do <b>not</b> make a licence extraordinary.", "Las gafas o audífonos <b>no</b> convierten el permiso en extraordinario."),
        ("Ages: LCM <b>14</b>, AM <b>15</b>, A1 and LVA <b>16</b>, A2/B/B+E <b>18</b>, A <b>20</b> (after 2 years of A2), trikes over 15 kW <b>21</b>.", "Edades: LCM <b>14</b>, AM <b>15</b>, A1 y LVA <b>16</b>, A2/B/B+E <b>18</b>, A <b>20</b> (tras 2 años de A2), triciclos de más de 15 kW <b>21</b>."),
        ("B + 3 years = <b>125 cc motorcycles in Spain</b>. B + 2 years = alternative-fuel vans up to <b>4,250 kg</b> in Spain.", "B + 3 años = <b>motos de 125 c.c. en España</b>. B + 2 años = furgonetas de combustibles alternativos hasta <b>4.250 kg</b> en España."),
        ("Combination over 3,500 kg (up to 4,250 kg) with B: you need <b>B96</b>; B+E covers trailers up to <b>3,500 kg</b>.", "Conjunto de más de 3.500 kg (hasta 4.250) con el B: <b>B96</b>; el B+E, remolques hasta <b>3.500 kg</b>."),
        ("Deadlines: data change <b>15 days</b>; seller <b>10 days</b>; buyer <b>30 days</b>; overdue ITV slip <b>10 days</b>; repair after unfavourable ITV <b>up to 2 months</b>.", "Plazos: cambio de datos <b>15 días</b>; vendedor <b>10 días</b>; comprador <b>30 días</b>; volante ITV <b>10 días</b>; reparar tras ITV desfavorable <b>hasta 2 meses</b>."),
        ("Light trailers (≤ 750 kg): no registration, no periodic ITV, no compulsory insurance, but they <b>do</b> need an ITV card and carry the towing vehicle’s plate.", "Remolques ligeros (≤ 750 kg): sin matrícula, sin ITV periódica, sin seguro obligatorio, pero <b>sí</b> tarjeta ITV y la placa del tractor."),
        ("Unfavourable ITV: <b>you may drive to the workshop</b>; negative: <b>tow truck</b> only.", "ITV desfavorable: <b>se puede ir al taller</b>; negativa: <b>solo en grúa</b>."),
        ("V-19: top <b>right</b> of the windscreen; V-13 “L”: rear <b>left</b>.", "V-19: arriba a la <b>derecha</b> del parabrisas; V-13 «L»: detrás a la <b>izquierda</b>."),
        ("Compulsory insurance never covers the <b>guilty driver’s own injuries</b> or the insured vehicle.", "El seguro obligatorio nunca cubre las <b>lesiones del propio conductor culpable</b> ni el vehículo asegurado."),
        ("At most <b>8 points a day</b>, unless there is a very serious offence. Mobile <b>in hand</b> = 6 points; headphones = 3.", "Como máximo <b>8 puntos al día</b>, salvo infracción muy grave. Móvil <b>en la mano</b> = 6 puntos; auriculares = 3."),
        ("Partial course: up to <b>4 points</b>, once every <b>2 years</b>. Licence regained: <b>8 points</b>, same seniority.", "Curso parcial: hasta <b>4 puntos</b>, una vez cada <b>2 años</b>. Permiso recuperado: <b>8 puntos</b>, misma antigüedad."),
    ]))

    # ---------------------------------------------------------------- 6. numbers
    B.append(H2("6", "Key numbers on one page", "Números clave en una página"))
    B.append(TABLE(
        [T("Item", "Concepto"), T("Number", "Cifra")],
        [
            [T("Banned from tests after using hidden devices", "Sin poder presentarse a examen por usar dispositivos"), T("6 months", "6 meses")],
            [T("A1 motorcycle", "Moto del A1"), T("≤ 125 cc, ≤ 11 kW, ≤ 0.1 kW/kg", "≤ 125 c.c., ≤ 11 kW, ≤ 0,1 kW/kg")],
            [T("A2 motorcycle", "Moto del A2"), T("≤ 35 kW, ≤ 0.2 kW/kg", "≤ 35 kW, ≤ 0,2 kW/kg")],
            [T("B: mass / passengers / trailer", "B: masa / pasajeros / remolque"), T("3,500 kg / 8 + driver / 750 kg (combination up to 4,250 kg)", "3.500 kg / 8 + conductor / 750 kg (conjunto hasta 4.250 kg)")],
            [T("Validity of AM, A1, A2, A, B, B+E", "Vigencia de AM, A1, A2, A, B, B+E"), T("10 years; 5 years from 65", "10 años; 5 años desde los 65")],
            [T("Novice “L” plate", "Señal «L»"), T("first year", "primer año")],
            [T("ITV can be passed early", "Adelantar la ITV"), T("up to 30 calendar days", "hasta 30 días naturales")],
            [T("NIVE (e-ITV)", "NIVE (e-ITV)"), T("32 characters", "32 dígitos")],
            [T("Points: standard / new driver / maximum", "Puntos: normal / novel / máximo"), T("12 / 8 / 15", "12 / 8 / 15")],
            [T("Recovering all points automatically", "Recuperar todos los puntos automáticamente"), T("2 years without firm sanctions", "2 años sin sanciones firmes")],
            [T("Courses: partial / licence", "Cursos: parcial / recuperación del permiso"), T("10 h, up to 4 points / 20 h + test, 8 points", "10 h, hasta 4 puntos / 20 h + test, 8 puntos")],
            [T("Alcohol in air: general / new and professional", "Alcohol en aire: general / noveles y profesionales"), T("0.25 mg/l / 0.15 mg/l (crime: over 0.60 mg/l)", "0,25 mg/l / 0,15 mg/l (delito: más de 0,60 mg/l)")],
            [T("Speeding crime", "Delito de velocidad"), T("+60 km/h in town, +80 km/h out of town", "+60 km/h en urbana, +80 km/h en interurbana")],
        ],
        widths=["52%", "48%"],
        cls="small",
    ))
    return B


# ------------------------------------------------------------------------------------------
# The PDF self-test reuses twelve questions from the page's question bank. The correct option is placed in
# turn at A, B and C so the answer key is not always the same letter.
QUIZ_IDS = ["dc1", "cl3", "pb2", "va4", "vd3", "it2", "it6", "in2", "pt2", "if3", "cs1", "lb2"]


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
    ("Ley sobre Tráfico, Circulación de Vehículos a Motor y Seguridad Vial (RDL 6/2015), including the points system (annexes II and III)", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722"),
    ("Reglamento General de Conductores (RD 818/2009) — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2009-9481"),
    ("Reglamento General de Vehículos (RD 2822/1998): registration and plates — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-1999-1826"),
    ("Real Decreto 920/2017: technical vehicle inspection (ITV) — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2017-12841"),
    ("Ley sobre responsabilidad civil y seguro en la circulación de vehículos a motor (RDL 8/2004) — consolidated text", "https://www.boe.es/buscar/act.php?id=BOE-A-2004-18911"),
    ("Ley 50/1980, de Contrato de Seguro (art. 16: 7 days to report a claim)", "https://www.boe.es/buscar/act.php?id=BOE-A-1980-22501"),
    ("Código Penal (LO 10/1995), arts. 379–385: crimes against road safety", "https://www.boe.es/buscar/act.php?id=BOE-A-1995-25444"),
    ("Real Decreto 518/2026 (reform in force 1 October 2026: compulsory habitual driver when the owner has no licence)", "https://www.boe.es/buscar/doc.php?id=BOE-A-2026-13889"),
    ("DGT press release, 27-01-2026: register of light personal vehicles; compulsory insurance for VMP (Ley 5/2025)",
     "https://www.dgt.es/comunicacion/notas-de-prensa/20260127-trafico-pone-en-marcha-registro-vehiculos-personales-ligeros/"),
]

GLOSSARY = [
    ("permiso / licencia de conducción", "driving licence (permit / licence class)"),
    ("aptitudes psicofísicas", "physical and mental fitness"),
    ("permiso ordinario / extraordinario", "ordinary / restricted licence"),
    ("Jefatura Provincial de Tráfico", "Provincial Traffic Office"),
    ("vigencia · prórroga", "validity · renewal"),
    ("duplicado", "duplicate"),
    ("conductor novel", "new (novice) driver"),
    ("nulidad o lesividad", "annulment"),
    ("pérdida de vigencia", "loss of validity"),
    ("suspensión cautelar · intervención", "precautionary suspension · withdrawal on the spot"),
    ("permiso de circulación", "vehicle registration certificate"),
    ("titular · tomador", "registered owner · policyholder"),
    ("transmisión · transferencia", "change of ownership"),
    ("placa de matrícula", "number plate"),
    ("tarjeta de inspección técnica (ITV)", "roadworthiness (MOT) certificate"),
    ("inspección favorable / desfavorable / negativa", "pass / fail (repairable) / fail (dangerous)"),
    ("precinto · baja", "sealing off · deregistration"),
    ("seguro de responsabilidad civil obligatorio", "compulsory third-party insurance"),
    ("declaración amistosa de accidente (parte)", "accident report form"),
    ("Consorcio de Compensación de Seguros", "Spanish insurance compensation fund"),
    ("crédito de puntos · bonificación", "points balance · bonus points"),
    ("sanción firme en vía administrativa", "final administrative penalty"),
    ("curso de sensibilización y reeducación vial", "driver re-education course"),
    ("responsable solidario", "jointly liable"),
    ("conductor habitual", "regular (named) driver"),
    ("delito contra la seguridad vial", "road-safety crime"),
    ("trabajos en beneficio de la comunidad", "community service"),
]
