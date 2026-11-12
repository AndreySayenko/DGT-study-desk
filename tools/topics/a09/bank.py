# -*- coding: utf-8 -*-
"""Question bank for the interactive Category A1/A2, Topic 9 page (documentation). In every question the FIRST option
is the correct one (the page shuffles options when it shows them). Ids must be unique and must not start with "ai"."""

BANK = []


def Q(qid, tag, en, es, opts, why_en, why_es):
    BANK.append({
        "id": qid, "tag": tag,
        "q": {"en": en, "es": es},
        "o": [{"en": a, "es": b} for a, b in opts],
        "why": {"en": why_en, "es": why_es},
    })


# tag -> section number, names, recap bullets, typical confusion
TAGS = {
    "docs": dict(sec=1, en="Carrying and getting the licence", es="Llevar y obtener el permiso",
        recap=[("Licence and the motorcycle’s papers, valid and in force; show them when agents ask.", "Permiso y documentación de la moto, válidos y vigentes; mostrarlos cuando lo pidan los agentes."),
               ("Original, certified photocopy or miDGT; the app is valid only in Spain.", "Original, fotocopia compulsada o miDGT; la app solo vale en España."),
               ("Only one EU licence per person, with all its classes.", "Un solo permiso de la UE por persona, con todas sus clases."),
               ("Fitness plus being declared fit in knowledge, skills, aptitudes and behaviour; glasses do not make it extraordinary.", "Aptitudes psicofísicas y ser declarado apto en conocimientos, habilidades, aptitudes y comportamientos; las gafas no lo hacen extraordinario.")],
        trap=("Thinking miDGT is enough when riding in France.", "Pensar que la app miDGT basta si circulas por Francia.")),
    "classes": dict(sec=1, en="A1, A2 and A", es="A1, A2 y A",
        recap=[("A1 at 16: ≤ 125 cc, ≤ 11 kW, ≤ 0.1 kW/kg; trikes ≤ 15 kW; includes AM.", "A1 a los 16: ≤ 125 c.c., ≤ 11 kW, ≤ 0,1 kW/kg; triciclos ≤ 15 kW; incluye el AM."),
               ("A2 at 18: ≤ 35 kW, ≤ 0.2 kW/kg, not derived from more than twice its power; includes A1.", "A2 a los 18: ≤ 35 kW, ≤ 0,2 kW/kg, no derivada de más del doble; incluye el A1."),
               ("A at 20: two years with A2 plus a training course; trikes over 15 kW only from 21.", "A a los 20: dos años con el A2 más una formación; triciclos de más de 15 kW solo desde los 21."),
               ("B held for more than 3 years: A1 motorcycles in Spain only.", "B con más de 3 años: motos del A1 solo en España.")],
        trap=("Thinking a 35 kW motorcycle always fits the A2.", "Pensar que una moto de 35 kW siempre vale con el A2.")),
    "validity": dict(sec=1, en="Validity, duplicates and suspension", es="Vigencia, duplicados y suspensión",
        recap=[("Every 10 years; every 5 from 65; shorter if an illness may get worse.", "Cada 10 años; cada 5 desde los 65; menos si una enfermedad puede agravarse."),
               ("An expired licence does not let you ride and is withdrawn on the spot.", "Un permiso caducado no autoriza a conducir y se interviene en el acto."),
               ("Change of details: tell the Traffic Office within 15 days for a duplicate.", "Cambio de datos: comunicarlo a la Jefatura en 15 días para un duplicado."),
               ("Precautionary suspension: serious danger or public interest; riding then = riding with a suspended licence.", "Suspensión cautelar: grave peligro o interés público; conducir entonces = conducir con el permiso suspendido.")],
        trap=("Thinking you can ride for a few weeks after the licence expires.", "Pensar que se puede conducir unas semanas tras caducar el permiso.")),
    "novice": dict(sec=1, en="New riders", es="Conductores noveles",
        recap=[("V-13 “L” during the first year of the first licence.", "V-13 «L» durante el primer año del primer permiso."),
               ("On a motorcycle: somewhere visible at the rear (smaller plate, 10 × 13 cm).", "En moto: en un sitio visible de la parte posterior (placa más pequeña, 10 × 13 cm)."),
               ("Withdrawn or suspended in that year: the year is extended by the same time.", "Intervenido o suspendido en ese año: el año se amplía ese mismo tiempo."),
               ("Not a first licence if you held another for at least a year.", "No es primer permiso si ya tuviste otro durante al menos un año.")],
        trap=("Putting the “L” on a new A2 when you have had the B for years.", "Poner la «L» con un A2 nuevo cuando tienes el B desde hace años.")),
    "vehdocs": dict(sec=2, en="Registration certificate and plate", es="Permiso de circulación y placa",
        recap=[("Carry the registration certificate and the ITV card with the last report.", "Llevar el permiso de circulación y la tarjeta ITV con el último informe."),
               ("Change of the owner’s name or address: 15 days.", "Cambio de nombre o domicilio del titular: 15 días."),
               ("Sale: seller notifies within 10 days; buyer renews within 30, or the vehicle is immobilised.", "Venta: el vendedor notifica en 10 días; el comprador renueva en 30 o se inmoviliza."),
               ("Motorcycles and mopeds: one plate, at the rear; the rider keeps it readable.", "Motos y ciclomotores: una placa, detrás; el conductor la mantiene legible.")],
        trap=("Thinking the buyer has 10 days and the seller 30.", "Pensar que el comprador tiene 10 días y el vendedor 30.")),
    "itv": dict(sec=2, en="The ITV", es="La ITV",
        recap=[("Two-wheel moped: exempt to 3 years, then every 2.", "Ciclomotor de dos ruedas: exento hasta 3 años, después cada 2."),
               ("Motorcycle, three-wheel moped, quad: exempt to 4 years, then every 2.", "Moto, ciclomotor de tres ruedas, quad: exento hasta 4 años, después cada 2."),
               ("Unfavourable: only to the workshop and back. Negative: tow truck. Repairs: up to 2 months.", "Desfavorable: solo al taller y vuelta. Negativa: grúa. Reparación: hasta 2 meses."),
               ("Overdue: certificate withdrawn, slip for 10 days, then sealing off.", "Caducada: se interviene el permiso de circulación, volante de 10 días y después precinto.")],
        trap=("Riding home normally after an unfavourable ITV.", "Volver a casa con normalidad tras una ITV desfavorable.")),
    "insurance": dict(sec=2, en="Compulsory insurance", es="Seguro obligatorio",
        recap=[("The owner insures the motorcycle or moped, even if it is not ridden.", "El propietario asegura la moto o el ciclomotor, aunque no circule."),
               ("Covered: other people’s injuries (passenger included) and other people’s property.", "Cubre: lesiones de otras personas (incluido el pasajero) y bienes de terceros."),
               ("Not covered: the guilty rider’s injuries, the motorcycle, relatives’ property.", "No cubre: lesiones del conductor culpable, la moto, bienes de los parientes."),
               ("Drunk rider: insurer pays and claims back. Stolen motorcycle: the Consorcio pays.", "Conductor ebrio: paga la aseguradora y repite. Moto robada: paga el Consorcio.")],
        trap=("Thinking a relative riding pillion is not covered.", "Pensar que un familiar que va de pasajero no está cubierto.")),
    "points": dict(sec=3, en="The points balance", es="El saldo de puntos",
        recap=[("12 points; 8 with a licence of 2 years or less (unless another of more than 2 years) or after regaining it.", "12 puntos; 8 con un permiso de 2 años o menos (salvo otro de más de 2) o tras recuperarlo."),
               ("Bonus: +2 after 3 clean years, +1 after 3 more: up to 15.", "Bonificación: +2 tras 3 años sin sanción, +1 tras otros 3: hasta 15."),
               ("At most 8 points a day, unless a very serious offence.", "Como máximo 8 puntos al día, salvo infracción muy grave."),
               ("2 years without firm sanctions: back to the full 12.", "2 años sin sanciones firmes: se recuperan los 12.")],
        trap=("Thinking you have one balance for the motorcycle and another for the car.", "Pensar que hay un saldo para la moto y otro para el coche.")),
    "offences": dict(sec=3, en="Offences and speeding", es="Infracciones y velocidad",
        recap=[("3 points: U-turn, headphones or phone inside the helmet, radar detector.", "3 puntos: cambio de sentido, auriculares o móvil dentro del casco, detector de radar."),
               ("4 points: wrong licence, red light/STOP, helmet, distance, alcohol up to twice the limit.", "4 puntos: permiso que no habilita, rojo/STOP, casco, distancia, alcohol hasta el doble."),
               ("6 points: alcohol over twice, drugs, refusing tests, reckless, phone in hand, cyclists without 1.5 m.", "6 puntos: alcohol más del doble, drogas, negarse a las pruebas, temeraria, móvil en la mano, ciclistas sin 1,5 m."),
               ("Speeding: 100 € without points up to +20/+30; then 2, 4, 6 points.", "Velocidad: 100 € sin puntos hasta +20/+30; después 2, 4 y 6 puntos.")],
        trap=("Thinking a phone held inside the helmet is allowed because your hands are free.", "Pensar que el móvil sujeto dentro del casco está permitido porque llevas las manos libres.")),
    "courses": dict(sec=3, en="Road-safety courses", es="Cursos de reeducación",
        recap=[("Partial course: 10 hours, up to 4 points, never more than lost.", "Curso parcial: 10 horas, hasta 4 puntos, nunca más de los perdidos."),
               ("Once every 2 years (professionals once a year).", "Una vez cada 2 años (profesionales, una vez al año)."),
               ("Licence course: 20 hours plus a test; back with 8 points, same class and seniority.", "Curso de recuperación del permiso: 20 horas y un test; vuelve con 8 puntos, misma clase y antigüedad."),
               ("Wait 6 months after the first loss (3 for professionals), doubled if lost again within 3 years.", "Esperar 6 meses tras la primera pérdida (3 los profesionales), el doble si se pierde otra vez en 3 años.")],
        trap=("Thinking the partial course can take you above your initial points.", "Pensar que el curso parcial puede subirte por encima de tus puntos iniciales.")),
    "liability": dict(sec=4, en="Who is liable", es="Quién responde",
        recap=[("The author answers, as a rule.", "Responde el autor, como norma."),
               ("Passenger without a helmet or under the minimum age: the rider.", "Pasajero sin casco o sin la edad mínima: el conductor."),
               ("Rider under 18: parents or guardians jointly liable for the fine.", "Conductor menor de 18: padres o tutores responsables solidarios de la multa."),
               ("Documents, ITV and condition: the owner. Owner without a licence: must name a habitual driver.", "Documentación, ITV y estado: el titular. Titular sin permiso: debe designar un conductor habitual.")],
        trap=("Thinking the passenger pays for their own missing helmet.", "Pensar que el pasajero responde de su propio casco.")),
}

# ---------------------------------------------------------------- 1 carrying and getting the licence
Q("dc1", "docs", "An agent stops you on your motorcycle and asks for your licence. In which forms may you show it?",
  "Un agente te para en moto y te pide el permiso. ¿En qué formatos puedes mostrarlo?",
  [("The original, a certified photocopy or the miDGT app", "El original, una fotocopia compulsada o la app miDGT"), ("Only the original card", "Solo la tarjeta original"), ("Any photo of it on the phone", "Cualquier foto del permiso en el móvil")],
  "The documents may be shown in their physical original, as a certified photocopy or in digital form in miDGT.", "Los documentos pueden mostrarse en original, fotocopia compulsada o en formato digital en miDGT.")
Q("dc2", "docs", "You are going on a motorcycle trip to Portugal with your licence only in the miDGT app. Is that enough?",
  "Haces un viaje en moto a Portugal y llevas el permiso solo en la app miDGT. ¿Es suficiente?",
  [("No: the app is valid only in Spain; abroad, carry the physical documents", "No: la app solo vale en España; en el extranjero hay que llevar los documentos físicos"),
   ("Yes, in any EU country", "Sí, en cualquier país de la UE"), ("Yes, if you also carry the certificate on paper", "Sí, si además llevas el permiso de circulación en papel")],
  "miDGT has the same value as paper for traffic purposes, but only in Spain.", "miDGT tiene la misma validez que el papel a efectos de tráfico, pero solo en España.")
Q("dc3", "docs", "How many driving licences issued by EU states may one person hold?",
  "¿De cuántos permisos expedidos por Estados de la UE puede ser titular una persona?",
  [("One, with all its classes", "Uno, con todas sus clases"), ("One per class", "Uno por cada clase"), ("Two, if they live in two countries", "Dos, si vive en dos países")],
  "Nobody may hold more than one; all the classes go on a single document.", "Nadie puede ser titular de más de uno; todas las clases constan en un único documento.")
Q("dc4", "docs", "You must wear glasses to reach the minimum eyesight. What kind of licence do you get?",
  "Necesitas gafas para alcanzar la agudeza visual mínima. ¿Qué tipo de permiso obtienes?",
  [("An ordinary licence", "Un permiso ordinario"), ("An extraordinary licence", "Un permiso extraordinario"), ("A temporary licence", "Un permiso temporal")],
  "Having to wear glasses or hearing aids does not make a licence extraordinary.", "La obligación de usar lentes o audífonos no le hace perder su carácter ordinario.")
Q("dc5", "docs", "Which tests must you pass to be declared fit (apto) for a motorcycle licence?",
  "¿Qué pruebas hay que superar para ser declarado apto para un permiso de moto?",
  [("Knowledge, skills, aptitudes and behaviour", "Conocimientos, habilidades, aptitudes y comportamientos"), ("Only a theory test", "Solo una prueba teórica"), ("Only a medical check", "Solo un reconocimiento médico")],
  "The Provincial Traffic Office declares you fit in the tests of knowledge, skills, aptitudes and behaviour.", "La Jefatura Provincial de Tráfico declara apto en las pruebas de conocimientos, habilidades, aptitudes y comportamientos.")
Q("dc6", "docs", "After an injury you no longer have the required physical fitness, but your licence is still in force. May you ride?",
  "Tras una lesión ya no reúnes las aptitudes físicas requeridas, pero el permiso sigue en vigor. ¿Puedes conducir?",
  [("No, until you recover the fitness", "No, hasta recuperarlas"), ("Yes, until the licence expires", "Sí, hasta que caduque el permiso"), ("Yes, but only in town", "Sí, pero solo en ciudad")],
  "If fitness is lost through illness, injury or anything else, you may not drive until you recover it.", "Si se pierden las aptitudes, no se podrá conducir hasta recuperarlas.")
Q("dc7", "docs", "Your physical condition changes and the motorcycle has to be adapted. What must you do?",
  "Cambian tus condiciones físicas y hay que adaptar la motocicleta. ¿Qué debes hacer?",
  [("Tell the Traffic Office, even though the licence is in force", "Comunicarlo a la Jefatura de Tráfico, aunque el permiso esté en vigor"), ("Nothing until the next renewal", "Nada hasta la próxima renovación"), ("Only tell the insurer", "Solo comunicarlo a la aseguradora")],
  "When the vehicle must be adapted, the Traffic Office must be told even if the licence is in force.", "Si hay que adaptar el vehículo, se debe comunicar a la Jefatura aunque el permiso esté en vigor.")

# ---------------------------------------------------------------- 1.1 classes
Q("cl1", "classes", "What is the minimum age for the A1 licence?", "¿Cuál es la edad mínima para el permiso A1?",
  [("16", "16 años"), ("15", "15 años"), ("18", "18 años")],
  "A1 from 16; AM from 15; A2 from 18.", "A1 desde los 16; AM desde los 15; A2 desde los 18.")
Q("cl2", "classes", "Which motorcycle may you ride with an A1?", "¿Qué motocicleta puedes conducir con el A1?",
  [("Up to 125 cc, 11 kW and 0.1 kW/kg", "Hasta 125 c.c., 11 kW y 0,1 kW/kg"), ("Up to 125 cc and 15 kW", "Hasta 125 c.c. y 15 kW"), ("Up to 35 kW and 0.2 kW/kg", "Hasta 35 kW y 0,2 kW/kg")],
  "The A1 motorcycle must meet all three limits: 125 cc, 11 kW and 0.1 kW/kg.", "La moto del A1 debe cumplir los tres límites: 125 c.c., 11 kW y 0,1 kW/kg.")
Q("cl3", "classes", "Besides A1 motorcycles, what else does the A1 licence let you drive?", "Además de las motos del A1, ¿qué más permite conducir el A1?",
  [("Motor tricycles up to 15 kW, mopeds and light quadricycles", "Triciclos de motor de hasta 15 kW, ciclomotores y cuadriciclos ligeros"), ("Cars with automatic gearbox", "Turismos con cambio automático"), ("Any motor tricycle", "Cualquier triciclo de motor")],
  "A1 also covers tricycles up to 15 kW, reduced-mobility vehicles and, because it includes AM, mopeds and light quadricycles.", "El A1 también cubre triciclos de hasta 15 kW, vehículos de movilidad reducida y, como incluye el AM, ciclomotores y cuadriciclos ligeros.")
Q("cl4", "classes", "What is the minimum age for the A2 licence?", "¿Cuál es la edad mínima para el permiso A2?",
  [("18", "18 años"), ("16", "16 años"), ("20", "20 años")],
  "A2 from 18.", "A2 desde los 18 años.")
Q("cl5", "classes", "What are the power limits of an A2 motorcycle?", "¿Cuáles son los límites de potencia de una moto del A2?",
  [("35 kW and 0.2 kW/kg", "35 kW y 0,2 kW/kg"), ("11 kW and 0.1 kW/kg", "11 kW y 0,1 kW/kg"), ("70 kW and 0.4 kW/kg", "70 kW y 0,4 kW/kg")],
  "A2: at most 35 kW, a power-to-weight ratio of at most 0.2 kW/kg, and not derived from a vehicle with more than twice its power.", "A2: como máximo 35 kW, relación potencia/peso de 0,2 kW/kg como máximo, y no derivada de un vehículo con más del doble de su potencia.")
Q("cl6", "classes", "A motorcycle has been limited to 35 kW. What may its original power be, at most, for it to fit the A2?",
  "Una moto ha sido limitada a 35 kW. ¿Cuál puede ser, como máximo, su potencia original para que valga con el A2?",
  [("70 kW", "70 kW"), ("35 kW", "35 kW"), ("Any power, once limited", "Cualquiera, una vez limitada")],
  "It may not be derived from a vehicle with more than twice its power: 2 × 35 = 70 kW.", "No puede derivar de un vehículo con más del doble de su potencia: 2 × 35 = 70 kW.")
Q("a2a", "classes", "A motorcycle has 35 kW and weighs 150 kg. May you ride it with the A2?",
  "Una moto tiene 35 kW y pesa 150 kg. ¿Puedes conducirla con el A2?",
  [("No: 35 ÷ 150 is about 0.23 kW/kg, over the 0.2 limit", "No: 35 ÷ 150 son unos 0,23 kW/kg, más del límite de 0,2"), ("Yes: it does not exceed 35 kW", "Sí: no supera los 35 kW"), ("Yes, if it was built with that power", "Sí, si se fabricó con esa potencia")],
  "Both limits apply: 35 kW and 0.2 kW/kg. A light 35 kW motorcycle can exceed the ratio.", "Se aplican los dos límites: 35 kW y 0,2 kW/kg. Una moto ligera de 35 kW puede superar la relación.")
Q("a2b", "classes", "A motorcycle has been limited to 30 kW from an original 70 kW. Does it fit the A2?",
  "Una moto ha sido limitada a 30 kW desde 70 kW originales. ¿Vale con el A2?",
  [("No: 70 kW is more than twice 30 kW", "No: 70 kW es más del doble de 30 kW"), ("Yes: 30 kW is below 35", "Sí: 30 kW es menos de 35"), ("Yes: 70 kW is the general maximum", "Sí: 70 kW es el máximo general")],
  "The original may not exceed twice the limited power: 2 × 30 = 60 kW, and 70 is more.", "La potencia original no puede superar el doble de la limitada: 2 × 30 = 60 kW, y 70 es más.")
Q("cl7", "classes", "How do you get the A licence?", "¿Cómo se obtiene el permiso A?",
  [("Holding an A2 with at least 2 years of experience and completing a training course", "Siendo titular del A2 con al menos 2 años de experiencia y superando una formación"),
   ("With theory and practical exams at 20, without the A2", "Con las pruebas teórica y práctica a los 20 años, sin el A2"), ("Automatically after 5 years with the A1", "Automáticamente tras 5 años con el A1")],
  "The A is only issued to holders of an A2 in force with at least two years’ experience, who complete a training course.", "El A solo se expide a titulares de un A2 en vigor con al menos dos años de experiencia que superen una formación.")
Q("cl8", "classes", "What is the minimum age for the A licence, and for driving motor tricycles over 15 kW with it?",
  "¿Cuál es la edad mínima del permiso A y para conducir con él triciclos de más de 15 kW?",
  [("20, and 21 for those tricycles", "20 años, y 21 para esos triciclos"), ("18, and 20 for those tricycles", "18 años, y 20 para esos triciclos"), ("21 for both", "21 años para los dos")],
  "A from 20; until 21 it does not cover motor tricycles over 15 kW.", "A desde los 20; hasta los 21 no autoriza triciclos de motor de más de 15 kW.")
Q("cl9", "classes", "You have held a B licence for four years. Which motorcycles may you ride with it?",
  "Tienes el permiso B desde hace cuatro años. ¿Qué motos puedes conducir con él?",
  [("The A1 motorcycles, in Spain only", "Las motos del A1, solo en España"), ("The A1 motorcycles, anywhere in the EU", "Las motos del A1, en cualquier país de la UE"), ("The A2 motorcycles, in Spain only", "Las motos del A2, solo en España")],
  "With a B of more than three years you may ride A1 motorcycles within Spain.", "Con un B de más de tres años se pueden conducir las motocicletas del A1 dentro del territorio nacional.")
Q("cl10", "classes", "You have held the B for two years. May you ride a 125 cc motorcycle with it?",
  "Tienes el B desde hace dos años. ¿Puedes conducir una moto de 125 c.c. con él?",
  [("No: the B must be more than three years old", "No: el B debe tener más de tres años"), ("Yes, in Spain", "Sí, en España"), ("Yes, if it is automatic", "Sí, si es automática")],
  "The B only covers A1 motorcycles after more than three years.", "El B solo cubre las motos del A1 con una antigüedad superior a tres años.")
Q("cl11", "classes", "Does an A2 licence let you ride mopeds?", "¿Permite el A2 conducir ciclomotores?",
  [("Yes: A2 includes A1, and A1 includes AM", "Sí: el A2 incluye el A1, y el A1 incluye el AM"), ("No: you need a separate AM", "No: hace falta el AM aparte"), ("Only three-wheel mopeds", "Solo ciclomotores de tres ruedas")],
  "Obtaining the A2 implies the A1, and the A1 implies the AM.", "La obtención del A2 implica la del A1, y la del A1 la del AM.")
Q("cl12", "classes", "Is the A1 compulsory before taking the A2?", "¿Es obligatorio tener el A1 antes de sacar el A2?",
  [("No: the A2 can be taken directly at 18", "No: el A2 se puede obtener directamente a los 18 años"), ("Yes, with two years of experience", "Sí, con dos años de experiencia"), ("Yes, with one year of experience", "Sí, con un año de experiencia")],
  "Only the A requires holding a previous class (the A2). The A2 can be taken with its own exams.", "Solo el A exige tener antes otra clase (el A2). El A2 se obtiene con sus propias pruebas.")

# ---------------------------------------------------------------- 1.2–1.5 validity, duplicates, suspension
Q("va1", "validity", "How often must a 40-year-old renew an A2 licence?", "¿Cada cuánto debe renovar el A2 una persona de 40 años?",
  [("Every 10 years", "Cada 10 años"), ("Every 5 years", "Cada 5 años"), ("Every 15 years", "Cada 15 años")],
  "AM, A1, A2 and A: 10 years until 65, then 5.", "AM, A1, A2 y A: 10 años hasta los 65, después 5.")
Q("va2", "validity", "And from the age of 65?", "¿Y a partir de los 65 años?",
  [("Every 5 years", "Cada 5 años"), ("Every 2 years", "Cada 2 años"), ("Every year", "Cada año")],
  "From 65 the period is 5 years, and it may be shorter for health reasons.", "Desde los 65 el periodo es de 5 años, y puede reducirse por motivos de salud.")
Q("va3", "validity", "Your licence expired last week and you ride to renew it. What happens if you are stopped?",
  "Tu permiso caducó la semana pasada y vas en moto a renovarlo. ¿Qué ocurre si te paran?",
  [("It does not let you ride and the agents withdraw it on the spot", "No autoriza a conducir y los agentes lo intervienen en el acto"), ("Nothing: there is a month of grace", "Nada: hay un mes de cortesía"), ("Only a warning", "Solo un aviso")],
  "An expired licence does not authorise driving, and using it leads to its immediate withdrawal.", "Un permiso caducado no autoriza a conducir y su utilización da lugar a su intervención inmediata.")
Q("va4", "validity", "You move house. Within how long must you tell the Traffic Office so it issues a duplicate of your licence?",
  "Cambias de domicilio. ¿En qué plazo debes comunicarlo a la Jefatura para que expida un duplicado del permiso?",
  [("15 days", "15 días"), ("10 days", "10 días"), ("30 days", "30 días")],
  "Any change of the data on the licence must be reported within 15 days.", "Cualquier variación de los datos del permiso debe comunicarse en un plazo máximo de 15 días.")
Q("va5", "validity", "You get a duplicate because you lost your licence, and later you find the original. What do you do?",
  "Obtienes un duplicado por pérdida del permiso y después encuentras el original. ¿Qué haces?",
  [("Hand the original back to the Traffic Office", "Devolver el original a la Jefatura de Tráfico"), ("Keep both, in case", "Guardar los dos, por si acaso"), ("Destroy the duplicate", "Destruir el duplicado")],
  "After a duplicate for theft or loss, the original must be returned when found.", "Tras un duplicado por sustracción o extravío, el original debe devolverse cuando se encuentre.")
Q("va6", "validity", "A licence is suspended as a precaution. What does riding during that suspension count as?",
  "Un permiso es objeto de suspensión cautelar. ¿Qué supone conducir durante esa suspensión?",
  [("Riding with a licence suspended by sanction", "Conducir con la autorización suspendida por sanción"), ("A minor offence", "Una infracción leve"), ("Nothing, if the suspension is not yet final", "Nada, si la suspensión no es firme")],
  "Driving during a precautionary suspension counts as driving with the licence suspended by sanction.", "Conducir durante la suspensión cautelar se considera conducir con la autorización suspendida por sanción.")

# ---------------------------------------------------------------- 1.4 novice
Q("nv1", "novice", "For how long must a new rider display the V-13 “L” plate?", "¿Durante cuánto tiempo debe llevar la señal V-13 «L» un conductor novel?",
  [("The first year of the licence", "El primer año del permiso"), ("The first two years", "Los dos primeros años"), ("Until the first renewal", "Hasta la primera renovación")],
  "Whoever gets a licence for the first time carries the V-13 during its first year.", "Quien obtiene un permiso por primera vez lleva la V-13 durante su primer año.")
Q("nv2", "novice", "Where does the “L” go on a motorcycle?", "¿Dónde se coloca la «L» en una motocicleta?",
  [("Somewhere visible at the rear", "En un sitio visible de la parte posterior"), ("At the rear left, as on a car", "Detrás a la izquierda, como en un turismo"), ("On the front mudguard", "En el guardabarros delantero")],
  "On cars it goes at the rear left; on motorcycles and three-wheelers it is enough somewhere visible at the rear.", "En los turismos va detrás a la izquierda; en motocicletas y vehículos de tres ruedas basta un sitio visible de la parte posterior.")
Q("nv3", "novice", "What does the V-13 plate look like?", "¿Cómo es la señal V-13?",
  [("Retroreflective, green with a white “L”", "Reflectante, verde con la «L» en blanco"), ("White with a green “L”", "Blanca con la «L» en verde"), ("Blue with a white “L”", "Azul con la «L» en blanco")],
  "Green background, white letter L, retroreflective; smaller on motorcycles.", "Fondo verde, letra L blanca, reflectante; más pequeña en las motos.")
Q("nv4", "novice", "A new rider’s licence is suspended for one month during the first year. What happens to the “L” period?",
  "Al novel le suspenden el permiso un mes durante el primer año. ¿Qué pasa con el periodo de la «L»?",
  [("It is extended by that month", "Se amplía en ese mes"), ("It starts again from zero", "Vuelve a empezar desde cero"), ("It does not change", "No cambia")],
  "The year is extended by the same time the licence was withdrawn or suspended.", "El año se amplía el mismo tiempo que el permiso estuvo intervenido o suspendido.")
Q("nv5", "novice", "You have had a B for five years and you have just passed the A2. Must you carry the “L” on the motorcycle?",
  "Tienes el B desde hace cinco años y acabas de aprobar el A2. ¿Debes llevar la «L» en la moto?",
  [("No: you have held another licence for at least a year", "No: ya has sido titular de otro permiso durante al menos un año"), ("Yes, for the first year of the A2", "Sí, durante el primer año del A2"), ("Yes, for six months", "Sí, durante seis meses")],
  "Those who have held another licence of any class for at least one year do not count as first-time holders.", "No se considera primer permiso si se ha sido titular de otro, de cualquier clase, durante al menos un año.")

# ---------------------------------------------------------------- 2.1 registration certificate and plate
Q("vd1", "vehdocs", "Which of the motorcycle’s documents must you carry when riding?", "¿Qué documentos de la moto debes llevar al circular?",
  [("The registration certificate and the ITV card, with the last inspection report", "El permiso de circulación y la tarjeta ITV, con el último informe de inspección"),
   ("Only the insurance receipt", "Solo el recibo del seguro"), ("The purchase invoice", "La factura de compra")],
  "Originals or certified copies of the registration certificate and the ITV card (and the last report, if it has been to the ITV).", "Originales o fotocopias cotejadas del permiso de circulación y de la tarjeta ITV (y el último informe, si ya la ha pasado).")
Q("vd2", "vehdocs", "You sell your motorcycle. Within how long must you, the seller, notify the Traffic Office?",
  "Vendes tu moto. ¿En qué plazo debes notificarlo tú, como vendedor, a la Jefatura de Tráfico?",
  [("10 days", "10 días"), ("15 days", "15 días"), ("30 days", "30 días")],
  "The seller notifies within 10 days; the buyer applies for the new certificate within 30.", "El vendedor lo notifica en 10 días; el comprador solicita el nuevo permiso de circulación en 30.")
Q("vd3", "vehdocs", "You buy a second-hand motorcycle. What happens if you do not apply for the certificate in your name within 30 days?",
  "Compras una moto de segunda mano. ¿Qué ocurre si no solicitas el permiso de circulación a tu nombre en 30 días?",
  [("It may not be ridden and is immobilised", "No puede circular y se ordena su inmovilización"), ("Nothing: the seller is still responsible", "Nada: sigue respondiendo el vendedor"), ("You lose 2 points", "Pierdes 2 puntos")],
  "The buyer has 30 days to renew the registration certificate; otherwise the vehicle may not be driven and is immobilised.", "El comprador tiene 30 días para renovar el permiso de circulación; si no, el vehículo no puede circular y se inmoviliza.")
Q("vd4", "vehdocs", "You move house but keep your motorcycle. Within how long must you report the new address for the registration certificate?",
  "Cambias de domicilio y conservas la moto. ¿En qué plazo debes comunicar el nuevo domicilio para el permiso de circulación?",
  [("15 days", "15 días"), ("10 days", "10 días"), ("3 months", "3 meses")],
  "A change of the owner’s name, surname or address without a change of owner is reported within 15 days.", "La variación del nombre, apellidos o domicilio del titular, sin cambio de titularidad, se comunica en 15 días.")
Q("vd5", "vehdocs", "How many number plates does a motorcycle carry, and where?", "¿Cuántas placas de matrícula lleva una motocicleta y dónde?",
  [("One, at the rear", "Una, en la parte posterior"), ("Two, front and rear", "Dos, delante y detrás"), ("One, at the front", "Una, en la parte delantera")],
  "Motorcycles and mopeds carry a single plate, at the rear.", "Las motocicletas y ciclomotores llevan una sola placa, en la parte posterior.")
Q("vd6", "vehdocs", "Your top case partly hides the number plate. Who is responsible?", "Tu baúl tapa en parte la placa de matrícula. ¿Quién es responsable?",
  [("The rider", "El conductor"), ("The owner only", "Solo el titular"), ("The manufacturer of the case", "El fabricante del baúl")],
  "The driver must check that nothing prevents or hinders reading the plates.", "El conductor es responsable de verificar que nada impida o dificulte la lectura de las placas.")
Q("vd7", "vehdocs", "Which of these data appears on the registration certificate?", "¿Cuál de estos datos figura en el permiso de circulación?",
  [("The owner’s name and address", "El nombre y domicilio del titular"), ("The rider’s licence number", "El número de permiso del conductor"), ("The insurance company", "La compañía de seguros")],
  "It shows the plate, registration date, owner’s name and address, make, model, MMA, seats and use.", "Figuran la matrícula, fecha de matriculación, nombre y domicilio del titular, marca, modelo, MMA, plazas y servicio.")

# ---------------------------------------------------------------- 2.2 ITV
Q("it1", "itv", "When does a two-wheel moped go to the ITV for the first time?", "¿Cuándo pasa la ITV por primera vez un ciclomotor de dos ruedas?",
  [("When it turns 3", "Al cumplir 3 años"), ("When it turns 4", "Al cumplir 4 años"), ("Never", "Nunca")],
  "Two-wheel mopeds are exempt up to 3 years and then go every 2 years.", "Los ciclomotores de dos ruedas están exentos hasta los 3 años y después pasan cada 2 años.")
Q("it2", "itv", "How often does a motorcycle go to the ITV?", "¿Con qué frecuencia pasa la ITV una motocicleta?",
  [("Exempt up to 4 years, then every 2 years", "Exenta hasta 4 años, después cada 2 años"), ("Exempt up to 4 years, every 2 years until 10, then every year", "Exenta hasta 4 años, cada 2 hasta los 10 y después cada año"),
   ("Every year from the first year", "Cada año desde el primero")],
  "Motorcycles: exempt to 4 years, then biennial for good. Annual inspections after 10 years apply to cars, not motorcycles.", "Motocicletas: exentas hasta 4 años y después bienal siempre. La ITV anual a partir de 10 años es de los turismos, no de las motos.")
Q("it3", "itv", "A three-wheel moped is 3½ years old. Must it already have passed the ITV?", "Un ciclomotor de tres ruedas tiene 3 años y medio. ¿Debe haber pasado ya la ITV?",
  [("No: three-wheel mopeds are exempt up to 4 years", "No: los ciclomotores de tres ruedas están exentos hasta 4 años"), ("Yes: mopeds go at 3 years", "Sí: los ciclomotores la pasan a los 3 años"), ("Yes: every year", "Sí: cada año")],
  "Only two-wheel mopeds go at 3 years; three-wheel mopeds follow the motorcycles: 4 years.", "Solo los de dos ruedas van a los 3 años; los ciclomotores de tres ruedas siguen a las motos: 4 años.")
Q("it4", "itv", "From what date is a motorcycle’s age counted for the ITV?", "¿Desde qué fecha se cuenta la antigüedad de una moto para la ITV?",
  [("The registration date on the registration certificate", "La fecha de matriculación del permiso de circulación"), ("The date of manufacture", "La fecha de fabricación"), ("The date the current owner bought it", "La fecha en que la compró el titular actual")],
  "The age counts from the first registration; for later inspections check the ITV card or the V-19.", "La antigüedad se cuenta desde la primera matriculación; para las siguientes, se consulta la tarjeta ITV o el V-19.")
Q("it5", "itv", "Your motorcycle has no windscreen. Where does the V-19 ITV sticker go?", "Tu moto no tiene parabrisas. ¿Dónde se coloca el distintivo V-19 de la ITV?",
  [("Somewhere clearly visible", "En un sitio bien visible"), ("On the helmet", "En el casco"), ("It is not needed on motorcycles", "No es necesario en las motos")],
  "With a windscreen, top right corner on the inside; otherwise somewhere clearly visible.", "Con parabrisas, en el ángulo superior derecho por dentro; si no, en un sitio bien visible.")
Q("it6", "itv", "You fit a sidecar to your motorcycle, a major modification. What must you do before riding it again?",
  "Instalas un sidecar en la moto, una reforma de importancia. ¿Qué debes hacer antes de volver a circular?",
  [("Pass an extraordinary ITV inspection", "Pasar una inspección técnica extraordinaria"), ("Wait for the next periodic ITV", "Esperar a la próxima ITV periódica"), ("Only tell the insurer", "Solo comunicarlo a la aseguradora")],
  "After a major modification the vehicle needs an extraordinary inspection before it circulates again.", "Tras una reforma de importancia hay que pasar una inspección técnica extraordinaria antes de volver a circular.")
Q("it7", "itv", "The ITV result is unfavourable. May you ride the motorcycle?", "El resultado de la ITV es desfavorable. ¿Puedes circular con la moto?",
  [("Only to the workshop and back to the ITV station", "Solo para ir al taller y volver a la estación ITV"), ("Normally, for 2 months", "Con normalidad, durante 2 meses"), ("No: only on a tow truck", "No: solo en grúa")],
  "Unfavourable: defects of some importance; only the trip to the workshop and back to the ITV is allowed.", "Desfavorable: defectos de cierta importancia; solo se permite el traslado al taller y la vuelta a la ITV.")
Q("it8", "itv", "And if the result is negative?", "¿Y si el resultado es negativo?",
  [("It may not be ridden: it leaves the station by other means, such as a tow truck", "No puede circular: sale de la estación por medios ajenos, como una grúa"), ("You may ride it straight to the workshop", "Puedes ir directamente al taller con ella"), ("You may ride it home", "Puedes volver a casa con ella")],
  "Negative: defects that are a danger on the road; the vehicle is moved by means other than itself.", "Negativa: defectos que son un peligro en la vía; el traslado se hace por medios ajenos al propio vehículo.")
Q("it9", "itv", "Agents stop you with the ITV out of date. What happens?", "Los agentes te paran con la ITV caducada. ¿Qué ocurre?",
  [("They report it, keep the registration certificate and give you a slip with 10 days to pass the ITV", "Denuncian, intervienen el permiso de circulación y te dan un volante con 10 días para pasarla"),
   ("They seal off the motorcycle on the spot", "Precintan la moto en el acto"), ("They give you 2 months to pass it, without a report", "Te dan 2 meses para pasarla, sin denuncia")],
  "If the ITV is not passed in those 10 days, the vehicle is sealed off.", "Si no se pasa en esos 10 días, se acuerda el precinto del vehículo.")
Q("it10", "itv", "How early may you pass your motorcycle’s ITV without losing time on the next date?",
  "¿Con cuánta antelación puedes pasar la ITV de tu moto sin perder tiempo en la siguiente fecha?",
  [("Up to 30 days", "Hasta 30 días"), ("Up to 10 days", "Hasta 10 días"), ("Up to 3 months", "Hasta 3 meses")],
  "Up to 30 calendar days early, the new period still starts when the old one ends.", "Hasta 30 días naturales antes, la nueva vigencia empieza cuando termina la anterior.")

# ---------------------------------------------------------------- 2.3 insurance
Q("in1", "insurance", "Who must take out the compulsory insurance of a motorcycle?", "¿Quién debe contratar el seguro obligatorio de una moto?",
  [("The owner, even if the motorcycle is not being ridden", "El propietario, aunque la moto no esté circulando"), ("Whoever rides it each day", "Quien la conduzca cada día"), ("Nobody, while it is parked", "Nadie, mientras esté aparcada")],
  "The owner must insure it even when it is not on the road; whoever signs is the policyholder.", "Debe concertarlo el propietario aunque no circule; quien lo contrata es el tomador.")
Q("in2", "insurance", "Must a moped be insured?", "¿Debe estar asegurado un ciclomotor?",
  [("Yes", "Sí"), ("Only if it goes faster than 45 km/h", "Solo si supera los 45 km/h"), ("Only if it carries a passenger", "Solo si lleva pasajero")],
  "All motor vehicles and mopeds must have compulsory insurance.", "Todos los vehículos de motor y los ciclomotores deben tener seguro obligatorio.")
Q("in3", "insurance", "You cause a crash and your passenger, who is your partner, is injured. Does your compulsory insurance pay for the passenger’s injuries?",
  "Causas un accidente y tu pasajera, que es tu pareja, resulta herida. ¿Paga tu seguro obligatorio sus lesiones?",
  [("Yes: relatives are excluded only for damage to their property", "Sí: los parientes solo quedan excluidos en los daños a sus bienes"), ("No: relatives are never covered", "No: los parientes nunca están cubiertos"), ("Only if she is the policyholder", "Solo si ella es la tomadora")],
  "The compulsory insurance covers personal injury to the policyholder, owner and relatives; it excludes only their property.", "El seguro obligatorio cubre los daños personales del tomador, propietario y parientes; solo excluye sus bienes.")
Q("in4", "insurance", "You fall on your own because of a mistake and you are injured. Does your compulsory insurance pay for your injuries?",
  "Te caes solo por un error tuyo y resultas herido. ¿Paga tu seguro obligatorio tus lesiones?",
  [("No: the guilty driver’s own injuries are never covered", "No: las lesiones del propio conductor culpable nunca están cubiertas"), ("Yes, always", "Sí, siempre"), ("Yes, if you wore all the gear", "Sí, si llevabas todo el equipo")],
  "The driver’s own injuries are excluded; cover for them has to be added voluntarily.", "Los daños personales del conductor quedan excluidos; para ellos hay que contratar coberturas voluntarias.")
Q("in5", "insurance", "Does the compulsory insurance pay for the damage to your own motorcycle after a crash you caused?",
  "¿Paga el seguro obligatorio los daños de tu propia moto en un accidente que causaste?",
  [("No", "No"), ("Yes, up to a limit", "Sí, hasta un límite"), ("Only if it was parked", "Solo si estaba aparcada")],
  "Damage to the insured vehicle and the goods it carries is not covered.", "Los daños al vehículo asegurado y a las cosas transportadas no están cubiertos.")
Q("in6", "insurance", "A rider who was over the alcohol limit injures a pedestrian. Who pays the victim?",
  "Un motorista que superaba la tasa de alcohol atropella a un peatón. ¿Quién indemniza a la víctima?",
  [("The insurer, which can then claim the money back from the rider", "La aseguradora, que después puede repetir contra el conductor"), ("Nobody: alcohol voids the insurance", "Nadie: el alcohol anula el seguro"), ("The Consorcio, always", "Siempre el Consorcio")],
  "Victims are paid; the insurer may then recover the money from the rider.", "Las víctimas cobran; la aseguradora puede después repetir contra el conductor.")
Q("in7", "insurance", "A stolen motorcycle injures someone. Who pays the victim?", "Una moto robada atropella a alguien. ¿Quién indemniza a la víctima?",
  [("The Consorcio de Compensación de Seguros", "El Consorcio de Compensación de Seguros"), ("The owner’s insurer", "La aseguradora del propietario"), ("Nobody", "Nadie")],
  "Damage caused by a stolen vehicle is paid by the Consorcio.", "Los daños causados por un vehículo robado los indemniza el Consorcio.")
Q("in8", "insurance", "How do agents check that your motorcycle is insured?", "¿Cómo comprueban los agentes que tu moto está asegurada?",
  [("In the FIVA database; if not possible, you show the receipt", "En el fichero FIVA; si no es posible, presentas el recibo"), ("Only with the paper policy", "Solo con la póliza en papel"), ("With a sticker on the plate", "Con una pegatina en la placa")],
  "They consult the Fichero Informativo de Vehículos Asegurados; otherwise the driver shows proof.", "Consultan el Fichero Informativo de Vehículos Asegurados; si no, el conductor presenta el justificante.")

# ---------------------------------------------------------------- 3 points
Q("pt1", "points", "How many points does a rider with an A2 of three years have, with no sanctions?", "¿Cuántos puntos tiene un conductor con un A2 de tres años y sin sanciones?",
  [("12", "12"), ("8", "8"), ("15", "15")],
  "After two years the balance is 12; the bonuses come after three more clean years.", "Tras dos años el saldo es de 12; las bonificaciones llegan tras tres años más sin sanción.")
Q("pt2", "points", "You get your first licence, an A1, at 16. How many points do you start with?", "Obtienes tu primer permiso, el A1, a los 16 años. ¿Con cuántos puntos empiezas?",
  [("8", "8"), ("12", "12"), ("6", "6")],
  "A licence of two years or less starts with 8, unless you already held another for more than two years.", "Un permiso de dos años o menos empieza con 8, salvo que ya fueras titular de otro con más de dos años.")
Q("pt3", "points", "You have had the B for five years and now get the A2. How many points do you have?", "Tienes el B desde hace cinco años y ahora sacas el A2. ¿Cuántos puntos tienes?",
  [("Your balance stays the same: the credit is one for all your licences", "Tu saldo no cambia: el crédito es único para todos tus permisos"), ("8, because the A2 is new", "8, porque el A2 es nuevo"), ("12 for the A2 and 12 for the B", "12 para el A2 y 12 para el B")],
  "There is one single points credit for all of a driver’s licences, and the 8-point rule does not apply after more than two years with another licence.", "El crédito de puntos es único para todas las autorizaciones, y la regla de los 8 puntos no se aplica con otro permiso de más de dos años.")
Q("pt4", "points", "What is the highest points balance you can reach?", "¿Cuál es el saldo máximo de puntos que se puede alcanzar?",
  [("15", "15"), ("12", "12"), ("20", "20")],
  "With all your points and no firm sanctions: +2 after 3 years and +1 after 3 more, up to 15.", "Con todos los puntos y sin sanciones firmes: +2 a los 3 años y +1 a los 3 siguientes, hasta 15.")
Q("pt5", "points", "In one day you commit several serious offences worth 12 points in total, none of them very serious. How many do you lose?",
  "En un mismo día cometes varias infracciones graves que suman 12 puntos, ninguna muy grave. ¿Cuántos pierdes?",
  [("8", "8"), ("12", "12"), ("6", "6")],
  "At most 8 points a day, unless one of the offences is very serious.", "Como máximo 8 puntos en un solo día, salvo que haya alguna infracción muy grave.")
Q("pt6", "points", "You lost some points and then go two years without any firm sanction that takes points. What happens?",
  "Perdiste algunos puntos y luego pasas dos años sin ninguna sanción firme con pérdida de puntos. ¿Qué ocurre?",
  [("You get back your full initial 12", "Recuperas la totalidad del crédito inicial de 12"), ("You get back 4 points", "Recuperas 4 puntos"), ("Nothing: you need a course", "Nada: hace falta un curso")],
  "Automatic recovery after two years without firm sanctions for partial losses.", "Recuperación automática tras dos años sin sanciones firmes en caso de pérdida parcial.")
Q("pt7", "points", "When are points actually taken from your balance?", "¿Cuándo se restan realmente los puntos de tu saldo?",
  [("When the administrative sanction for a serious or very serious offence becomes final", "Cuando la sanción por una infracción grave o muy grave es firme en vía administrativa"),
   ("When the agent reports you", "Cuando el agente te denuncia"), ("When you pay the fine", "Cuando pagas la multa")],
  "Points are reduced for each firm administrative sanction for offences that carry them.", "Los puntos se reducen por cada sanción firme en vía administrativa por infracciones que lleven aparejada su pérdida.")
Q("pt8", "points", "You regain your licence after losing all your points. How many points does it have?", "Recuperas el permiso tras perder todos los puntos. ¿Cuántos puntos tiene?",
  [("8", "8"), ("12", "12"), ("4", "4")],
  "The licence comes back with the same class and seniority, but with 8 points.", "El permiso vuelve con la misma clase y antigüedad, pero con 8 puntos.")

# ---------------------------------------------------------------- 3.2 offences and speeding
Q("of1", "offences", "You ride with your phone held between the helmet and your head to talk. How many points?",
  "Circulas con el móvil sujeto entre el casco y la cabeza para hablar. ¿Cuántos puntos?",
  [("3", "3"), ("6", "6"), ("None: your hands are free", "Ninguno: llevas las manos libres")],
  "Keeping a phone between helmet and head while riding is a 3-point offence.", "Mantener ajustado entre el casco y la cabeza un móvil mientras se conduce supone 3 puntos.")
Q("of2", "offences", "Which device may you use while riding a motorcycle?", "¿Qué dispositivo puedes usar mientras conduces una moto?",
  [("A certified wireless device built into the helmet, for intercom or navigation", "Un dispositivo inalámbrico certificado integrado en el casco, para intercomunicación o navegación"),
   ("Earphones under the helmet to listen to music", "Auriculares bajo el casco para escuchar música"), ("The phone in your hand at a red light", "El móvil en la mano en un semáforo en rojo")],
  "The Reglamento allows certified or approved wireless devices integrated in the helmet, only for intercom or navigation and without affecting safety.", "El Reglamento permite los dispositivos inalámbricos certificados u homologados integrados en el casco, solo para intercomunicación o navegación y sin afectar a la seguridad.")
Q("of3", "offences", "You ride without a helmet. How many points do you lose?", "Circulas sin casco. ¿Cuántos puntos pierdes?",
  [("4", "4"), ("3", "3"), ("6", "6")],
  "Not using, or using badly, the helmet and other compulsory protection: 4 points.", "No usar, o usar mal, el casco y demás elementos de protección obligatorios: 4 puntos.")
Q("of4", "offences", "Since 1 October 2026, what must a rider and passenger wear on an interurban road, besides the helmet?",
  "Desde el 1 de octubre de 2026, ¿qué deben llevar conductor y pasajero en una vía interurbana, además del casco?",
  [("Protective gloves and closed shoes", "Guantes de protección y calzado cerrado"), ("A reflective vest", "Un chaleco reflectante"), ("A back protector", "Un protector de espalda")],
  "Art. 118 of the Reglamento now requires gloves on interurban roads and closed shoes on every road. The reflective vest is equipment the motorcycle must carry, for when you get off on the road.", "El art. 118 exige ahora guantes en vías interurbanas y calzado cerrado en todas las vías. El chaleco reflectante es un accesorio que la moto debe llevar, para cuando te bajes en la vía.")
Q("of5", "offences", "You ride an 80 kW motorcycle with only an A2. What does it cost?", "Conduces una moto de 80 kW con solo el A2. ¿Qué supone?",
  [("4 points: riding with a licence that does not cover that vehicle", "4 puntos: conducir con un permiso que no habilita para ese vehículo"), ("Nothing, if you ride carefully", "Nada, si conduces con cuidado"), ("2 points", "2 puntos")],
  "Driving a vehicle with a licence that does not entitle you to it costs 4 points.", "Conducir un vehículo con un permiso que no habilite para ello supone 4 puntos.")
Q("of6", "offences", "Your licence is less than two years old and the breath test gives 0.22 mg/l. What happens?",
  "Tu permiso tiene menos de dos años y la prueba da 0,22 mg/l en aire. ¿Qué ocurre?",
  [("4 points: the limit for you is 0.15 mg/l", "4 puntos: tu límite es 0,15 mg/l"), ("Nothing: the limit is 0.25 mg/l", "Nada: el límite es 0,25 mg/l"), ("6 points", "6 puntos")],
  "New and professional drivers: over 0.15 and up to 0.30 mg/l, 4 points; over 0.30, 6 points.", "Noveles y profesionales: más de 0,15 hasta 0,30 mg/l, 4 puntos; más de 0,30, 6 puntos.")
Q("of7", "offences", "You use your phone holding it in your hand while riding. How many points?", "Usas el móvil sujetándolo con la mano mientras conduces. ¿Cuántos puntos?",
  [("6", "6"), ("3", "3"), ("4", "4")],
  "Using a mobile phone held in the hand is a very serious offence: 6 points.", "Utilizar el móvil sujetándolo con la mano es infracción muy grave: 6 puntos.")
Q("of8", "offences", "You overtake a group of cyclists leaving less than 1.5 m. How many points?", "Adelantas a un grupo de ciclistas dejando menos de 1,5 m. ¿Cuántos puntos?",
  [("6", "6"), ("4", "4"), ("3", "3")],
  "Overtaking cyclists dangerously or without the 1.5 m minimum: 6 points.", "Adelantar a ciclistas poniéndolos en peligro o sin dejar 1,5 m: 6 puntos.")
Q("of9", "offences", "On a motorway (limit 120) you are caught at 175 km/h. What is the sanction?", "En autopista (límite 120) te captan a 175 km/h. ¿Cuál es la sanción?",
  [("400 € and 4 points", "400 € y 4 puntos"), ("300 € and 2 points", "300 € y 2 puntos"), ("600 € and 6 points", "600 € y 6 puntos")],
  "With a 120 limit: 171–180 km/h is 400 € and 4 points.", "Con límite 120: de 171 a 180 km/h, 400 € y 4 puntos.")
Q("of10", "offences", "In town, with a 50 km/h limit, you are caught at 65 km/h. What is the sanction?", "En ciudad, con límite de 50 km/h, te captan a 65 km/h. ¿Cuál es la sanción?",
  [("100 € and no points", "100 € y sin puntos"), ("300 € and 2 points", "300 € y 2 puntos"), ("400 € and 4 points", "400 € y 4 puntos")],
  "With a 50 limit: 51–70 km/h is 100 € without points; 71–80 is 300 € and 2 points.", "Con límite 50: de 51 a 70 km/h, 100 € sin puntos; de 71 a 80, 300 € y 2 puntos.")
Q("of11", "offences", "Which of these costs 3 points?", "¿Cuál de estas infracciones supone 3 puntos?",
  [("Riding with a radar detector", "Circular con un detector de radar"), ("Riding with a radar jammer", "Circular con un inhibidor de radar"), ("Running a red light", "Saltarse un semáforo en rojo")],
  "Radar detector: 3 points; jammer: 6; red light: 4.", "Detector de radar: 3 puntos; inhibidor: 6; semáforo en rojo: 4.")

# ---------------------------------------------------------------- 3.3 courses
Q("cs1", "courses", "How many points can a partial-recovery course give back at most?", "¿Cuántos puntos puede devolver como máximo un curso de recuperación parcial?",
  [("4, never more than you lost", "4, nunca más de los perdidos"), ("6", "6"), ("All the lost points", "Todos los perdidos")],
  "The 10-hour course gives back up to 4 points.", "El curso de 10 horas permite recuperar hasta 4 puntos.")
Q("cs2", "courses", "How often may a private rider take the partial-recovery course?", "¿Cada cuánto puede hacer un conductor particular el curso de recuperación parcial?",
  [("Once every 2 years", "Una vez cada 2 años"), ("Once a year", "Una vez al año"), ("As often as needed", "Tantas veces como quiera")],
  "Once every 2 years; professional drivers, once a year.", "Una vez cada 2 años; los profesionales, una vez al año.")
Q("cs3", "courses", "How long is the course to regain a lost licence?", "¿Cuánto dura el curso para recuperar el permiso perdido?",
  [("20 hours, followed by a test at the Traffic Office", "20 horas, seguido de una prueba en la Jefatura"), ("10 hours, without a test", "10 horas, sin prueba"), ("30 hours and a practical exam", "30 horas y un examen práctico")],
  "The 20-hour course and a multiple-choice test at the Traffic Office.", "El curso de 20 horas y una prueba tipo test en la Jefatura.")
Q("cs4", "courses", "You lose your licence for the first time. How long must you wait before taking the course?",
  "Pierdes el permiso por primera vez. ¿Cuánto debes esperar para hacer el curso?",
  [("6 months", "6 meses"), ("3 months", "3 meses"), ("1 year", "1 año")],
  "6 months (3 for professionals), doubled if all points are lost again within the next three years.", "6 meses (3 los profesionales), el doble si se vuelven a perder todos los puntos en los tres años siguientes.")
Q("cs5", "courses", "When you regain an A2 lost through points, what class and seniority does it have?", "Cuando recuperas un A2 perdido por puntos, ¿con qué clase y antigüedad vuelve?",
  [("The same class and seniority, with 8 points", "La misma clase y antigüedad, con 8 puntos"), ("An A1, with 12 points", "Un A1, con 12 puntos"), ("The same class, but as a new licence", "La misma clase, pero como permiso nuevo")],
  "The licence obtained is of the same class and seniority, with a balance of 8 points.", "El permiso que se obtenga será de la misma clase y antigüedad, con un saldo de 8 puntos.")

# ---------------------------------------------------------------- 4 liability
Q("lb1", "liability", "Your passenger rides without a helmet. Who is liable?", "Tu pasajero va sin casco. ¿Quién es responsable?",
  [("You, the rider", "Tú, el conductor"), ("The passenger", "El pasajero"), ("The owner of the motorcycle", "El titular de la moto")],
  "The rider of a motorcycle or moped answers for the passenger not wearing a helmet.", "El conductor de una moto o ciclomotor responde de que el pasajero no use casco.")
Q("lb2", "liability", "You carry a passenger who is under the minimum age to ride pillion. Who is liable?", "Llevas un pasajero que no tiene la edad mínima para ir de pasajero. ¿Quién es responsable?",
  [("The rider", "El conductor"), ("The passenger’s parents", "Los padres del pasajero"), ("Nobody, if the passenger wears a helmet", "Nadie, si el pasajero lleva casco")],
  "The rider answers for carrying passengers who do not have the minimum age.", "El conductor responde por transportar pasajeros que no tengan la edad mínima exigida.")
Q("lb3", "liability", "A 17-year-old riding an A1 motorcycle is fined. Who answers for the fine with them?",
  "Multan a un chico de 17 años que conduce una moto del A1. ¿Quién responde de la multa con él?",
  [("The parents or guardians, jointly", "Los padres o tutores, de forma solidaria"), ("Nobody: minors do not pay fines", "Nadie: los menores no pagan multas"), ("The driving school", "La autoescuela")],
  "For offences by under-18s, parents or guardians are jointly liable for the fine.", "Por los hechos cometidos por menores de 18 años, padres o tutores son responsables solidarios de la multa.")
Q("lb4", "liability", "Your friend borrows your motorcycle and is stopped with the ITV out of date. Who answers for the ITV?",
  "Un amigo te pide la moto y le paran con la ITV caducada. ¿Quién responde de la ITV?",
  [("You, the owner", "Tú, el titular"), ("Your friend, who was riding", "Tu amigo, que conducía"), ("The ITV station", "La estación ITV")],
  "The owner answers for the vehicle’s documents, periodic inspections and condition affecting safety.", "El titular responde de la documentación, las inspecciones periódicas y el estado de conservación que afecte a la seguridad.")
Q("lb5", "liability", "A camera catches your motorcycle speeding, but nobody was stopped. What must you, the owner, do?",
  "Un radar capta tu moto con exceso de velocidad, pero no se detuvo a nadie. ¿Qué debes hacer tú, como titular?",
  [("Identify who was riding", "Identificar a quien conducía"), ("Pay, whoever was riding", "Pagar, condujera quien condujera"), ("Nothing: without a stop there is no fine", "Nada: sin detención no hay multa")],
  "The owner must identify the driver at the time of the offence; not doing so is itself an offence.", "El titular tiene la obligación de identificar al conductor; no hacerlo es otra infracción.")
Q("lb6", "liability", "Your motorcycle has a named habitual driver and a camera catches it speeding. Who is liable?",
  "Tu moto tiene un conductor habitual designado y un radar la capta con exceso de velocidad. ¿Quién responde?",
  [("The habitual driver, unless they prove someone else rode it or it was stolen", "El conductor habitual, salvo que acredite que conducía otro o que fue sustraída"),
   ("Always the owner", "Siempre el titular"), ("Nobody", "Nadie")],
  "If the vehicle was not stopped and has a habitual driver, the liability falls on that driver.", "Si no se detuvo el vehículo y tiene conductor habitual, la responsabilidad recae en él.")
Q("lb7", "liability", "A mother without a driving licence registers a motorcycle in her name for her son. What must she do since 1 October 2026?",
  "Una madre sin permiso de conducción matricula una moto a su nombre para su hijo. ¿Qué debe hacer desde el 1 de octubre de 2026?",
  [("Name a habitual driver", "Designar un conductor habitual"), ("Nothing special", "Nada especial"), ("Get a moped licence first", "Sacarse antes el permiso de ciclomotor")],
  "When a person without a licence registers a vehicle, designating a habitual driver is now compulsory.", "Cuando una persona sin permiso matricula un vehículo, designar un conductor habitual es ahora obligatorio.")
