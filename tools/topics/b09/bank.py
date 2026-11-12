# -*- coding: utf-8 -*-
"""Question bank for the interactive Topic 9 page (documentation). In every question the FIRST option is the
correct one (the page shuffles options when it shows them). Ids must be unique and must not start with "ai"."""

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
    "docs": dict(sec=1, en="Carrying and getting a licence", es="Llevar y obtener el permiso",
        recap=[("Carry a valid licence and the vehicle’s papers; show them as original, certified copy or in miDGT.", "Llevar permiso y documentación del vehículo válidos; mostrarlos en original, fotocopia compulsada o miDGT."),
               ("miDGT is as valid as paper, but only in Spain.", "miDGT vale lo mismo que el papel, pero solo en España."),
               ("Only one EU licence per person. You need fitness and to pass the tests at the Traffic Office.", "Solo un permiso de la UE por persona. Hacen falta aptitudes y aprobar las pruebas en la Jefatura."),
               ("Hidden devices in a test: very serious, fine and 6 months without tests. Lost fitness: no driving until recovered.", "Dispositivos en el examen: muy grave, multa y 6 meses sin examinarse. Sin aptitudes: no conducir hasta recuperarlas.")],
        trap=("Using miDGT as proof abroad.", "Usar miDGT como documento en el extranjero.")),
    "classes": dict(sec=1, en="Licence classes and ages", es="Clases y edades",
        recap=[("LCM 14 (reduced mobility); LVA 16 (farm vehicles ≤ 45 km/h or ordinary limits).", "LCM 14 (movilidad reducida); LVA 16 (agrícolas ≤ 45 km/h o límites ordinarios)."),
               ("AM 15: mopeds and light quadricycles. A1 16: ≤ 125 cc, ≤ 11 kW, 0.1 kW/kg; trikes ≤ 15 kW.", "AM 15: ciclomotores y cuadriciclos ligeros. A1 16: ≤ 125 c.c., ≤ 11 kW, 0,1 kW/kg; triciclos ≤ 15 kW."),
               ("A2 18: ≤ 35 kW, 0.2 kW/kg, not derived from more than double the power.", "A2 18: ≤ 35 kW, 0,2 kW/kg, no derivadas de más del doble de potencia."),
               ("A 20, after 2 years with A2 and training; trikes over 15 kW need 21.", "A 20, tras 2 años de A2 y formación; triciclos de más de 15 kW, 21.")],
        trap=("Thinking A can be taken straight at 18.", "Pensar que el A se puede obtener directamente a los 18.")),
    "permb": dict(sec=1, en="The B licence and others", es="El permiso B y otros",
        recap=[("B at 18: MMA ≤ 3,500 kg, at most 8 passengers plus the driver.", "B a los 18: MMA ≤ 3.500 kg y como máximo 8 pasajeros más el conductor."),
               ("Light trailer ≤ 750 kg; heavier trailer if the combination ≤ 4,250 kg — over 3,500 kg needs B96.", "Remolque ligero ≤ 750 kg; no ligero si el conjunto ≤ 4.250 kg — más de 3.500 kg exige B96."),
               ("B + 2 years: alternative-fuel goods vans up to 4,250 kg in Spain. B + 3 years: A1 motorcycles in Spain.", "B + 2 años: mercancías de combustibles alternativos hasta 4.250 kg en España. B + 3 años: motos A1 en España."),
               ("B+E: trailer ≤ 3,500 kg. C: over 3,500 kg. D: more than 9 seats.", "B+E: remolque ≤ 3.500 kg. C: más de 3.500 kg. D: más de 9 plazas.")],
        trap=("Thinking B lets you ride any motorcycle.", "Pensar que el B permite conducir cualquier moto.")),
    "validity": dict(sec=1, en="Validity, changes and new drivers", es="Vigencia, cambios y noveles",
        recap=[("AM, A1, A2, A, B, B+E: every 10 years until 65, then every 5; shorter if an illness may worsen.", "AM, A1, A2, A, B, B+E: cada 10 años hasta los 65, después cada 5; menos si hay enfermedad que pueda agravarse."),
               ("An expired licence does not let you drive and is withdrawn. Data changes: 15 days for a duplicate.", "El permiso caducado no autoriza a conducir y se interviene. Cambio de datos: 15 días para el duplicado."),
               ("V-13 “L” for the first year, rear left; extended by any suspension.", "V-13 «L» el primer año, detrás a la izquierda; se amplía con la suspensión."),
               ("Loss of validity if all points or requirements are lost; precautionary suspension for serious danger.", "Pérdida de vigencia si se pierden los puntos o los requisitos; suspensión cautelar por grave peligro.")],
        trap=("Putting the L plate on the right.", "Poner la «L» a la derecha.")),
    "vehdocs": dict(sec=2, en="Registration certificate and plates", es="Permiso de circulación y placas",
        recap=[("Carry the registration certificate and ITV card (originals or certified copies), plus the last ITV report.", "Llevar permiso de circulación y tarjeta ITV (originales o fotocopias cotejadas) y el último informe ITV."),
               ("Registration certificate: all motor vehicles and trailers over 750 kg; light trailers are not registered.", "Permiso de circulación: todos los de motor y remolques de más de 750 kg; los ligeros no se matriculan."),
               ("Owner’s details: 15 days. Sale: seller 10 days, buyer 30 days.", "Datos del titular: 15 días. Venta: vendedor 10 días, comprador 30 días."),
               ("Cars: front and rear plates. Two-wheelers: rear only. Trailer > 750 kg: towing vehicle’s plate on the right + red plate.", "Automóviles: delante y detrás. Dos ruedas: solo detrás. Remolque > 750 kg: placa del tractor a la derecha + placa roja.")],
        trap=("Thinking the buyer notifies the sale in 10 days.", "Pensar que el comprador notifica la venta en 10 días.")),
    "itv": dict(sec=2, en="ITV", es="ITV",
        recap=[("ITV card: technical fitness; pass up to 30 calendar days early without losing time. e-ITV and NIVE (32 characters).", "Tarjeta ITV: aptitud técnica; se puede adelantar 30 días naturales sin perder tiempo. e-ITV y NIVE (32 dígitos)."),
               ("Cars: exempt 4 years, every 2 to 10, then yearly. Mopeds: 3 years exempt. Motorcycles: 4.", "Turismos: exentos 4 años, cada 2 hasta 10, luego anual. Ciclomotores: 3 años exentos. Motos: 4."),
               ("Vans ≤ 3.5 t: 2 exempt, biennial to 6, annual to 10, then every 6 months.", "Furgonetas ≤ 3,5 t: 2 exentos, bienal hasta 6, anual hasta 10, después semestral."),
               ("Unfavourable: to the workshop and back. Negative: tow truck. V-19 top right of the windscreen. Overdue: 10-day slip.", "Desfavorable: al taller y vuelta. Negativa: grúa. V-19 arriba a la derecha. Caducada: volante de 10 días.")],
        trap=("Thinking you cannot drive at all after an unfavourable ITV.", "Pensar que tras una ITV desfavorable no se puede circular en absoluto.")),
    "insurance": dict(sec=2, en="Compulsory insurance", es="Seguro obligatorio",
        recap=[("Covers the driver’s civil liability for injuries and damage to others.", "Cubre la responsabilidad civil del conductor por daños a personas y bienes de otros."),
               ("Required: motor vehicles, mopeds, trailers over 750 kg; since 2026 also e-scooters (VMP), after registering them.", "Obligatorio: vehículos de motor, ciclomotores, remolques de más de 750 kg; desde 2026 también VMP, previa inscripción."),
               ("Not covered: the guilty driver’s injuries, the insured vehicle and its load, property of the policyholder and close family.", "No cubre: lesiones del conductor culpable, vehículo asegurado y carga, bienes del tomador y familiares."),
               ("Agents check the FIVA. Uninsured: banned, impounded, fined. Accident form: off the road, report to your insurer in 7 days.", "Los agentes consultan el FIVA. Sin seguro: prohibición, depósito o precinto y multa. Parte: fuera de la vía, comunicar en 7 días.")],
        trap=("Thinking the insurance pays the guilty driver’s own injuries.", "Pensar que el seguro paga las lesiones del propio conductor culpable.")),
    "points": dict(sec=3, en="Points balance", es="Crédito de puntos",
        recap=[("12 points; 8 for licences under 2 years and for licences regained.", "12 puntos; 8 los permisos de menos de 2 años y los recuperados."),
               ("Bonus without firm sanctions: +2 after 3 years, +1 after 3 more, maximum 15.", "Bonificación sin sanciones firmes: +2 a los 3 años, +1 a los 3 siguientes, máximo 15."),
               ("One single credit for all licences. Max 8 points lost per day unless a very serious offence.", "Un único crédito para todas las autorizaciones. Máximo 8 puntos al día salvo infracción muy grave."),
               ("2 years without firm sanctions: back to the full initial 12.", "2 años sin sanciones firmes: se recupera el crédito inicial de 12.")],
        trap=("Thinking you can lose more than 8 points in a day for several serious offences.", "Pensar que se pueden perder más de 8 puntos en un día por varias graves.")),
    "infra": dict(sec=3, en="Offences and points", es="Infracciones y puntos",
        recap=[("3 points: illegal U-turn, headphones or phone held by the helmet, radar detector.", "3 puntos: cambio de sentido indebido, auriculares o móvil sujeto en el casco, detector de radar."),
               ("4 points: STOP/red light/priority, dangerous overtaking, reversing on motorways, distance, seat belt/helmet/child seat, alcohol 0.25–0.50.", "4 puntos: stop/rojo/prioridad, adelantamiento peligroso, marcha atrás en autopista, distancia, cinturón/casco/SRI, alcohol 0,25–0,50."),
               ("6 points: alcohol over 0.50, drugs, refusing tests, reckless, wrong way, jammers, phone in hand, throwing objects, cyclists without 1.5 m.", "6 puntos: alcohol de más de 0,50, drogas, negarse, temeraria, sentido contrario, inhibidores, móvil en la mano, arrojar objetos, ciclistas sin 1,5 m."),
               ("Speeding: 100 € no points, then 2, 4, 6 and 6 points (very serious).", "Velocidad: 100 € sin puntos; luego 2, 4, 6 y 6 puntos (muy grave).")],
        trap=("Mixing up headphones (3 points) and a phone held in the hand (6).", "Confundir auriculares (3 puntos) con móvil en la mano (6).")),
    "courses": dict(sec=3, en="Re-education courses", es="Cursos de reeducación",
        recap=[("Partial course: 10 hours, up to 4 points (never more than lost).", "Curso parcial: 10 horas, hasta 4 puntos (nunca más de los perdidos)."),
               ("Once every 2 years; professionals once a year.", "Una vez cada 2 años; profesionales una al año."),
               ("Licence course: 20 hours plus a test at the Traffic Office; also after a court ban over 2 years.", "Curso de recuperación del permiso: 20 horas y test en la Jefatura; también tras condena de más de 2 años."),
               ("Wait 6 months (3 professionals), doubled if lost again within 3 years. Back with 8 points, same seniority.", "Esperar 6 meses (3 profesionales), el doble si se pierde de nuevo en 3 años. Vuelve con 8 puntos y misma antigüedad.")],
        trap=("Thinking the partial course restores 6 points.", "Pensar que el curso parcial devuelve 6 puntos.")),
    "liability": dict(sec=4, en="Liability and road crimes", es="Responsabilidad y delitos",
        recap=[("The author answers, but the driver answers for passengers’ helmets and age, and for child restraints (except professional public service).", "Responde el autor, pero el conductor responde del casco y la edad del pasajero, y de la SRI (salvo profesionales de servicio público)."),
               ("Under-18s: parents or guardians jointly liable for the fine. Documents, ITV and vehicle condition: the owner.", "Menores de 18: padres o tutores responsables solidarios de la multa. Documentación, ITV y estado del vehículo: el titular."),
               ("The owner must identify the driver; a named habitual driver answers when the vehicle was not stopped.", "El titular debe identificar al conductor; si hay conductor habitual, responde él cuando no se detuvo el vehículo."),
               ("Crimes: +60 km/h urban / +80 interurban, over 0.60 mg/l or drugs, refusing tests, reckless driving, driving without a licence, serious risk.", "Delitos: +60 km/h urbana / +80 interurbana, más de 0,60 mg/l o drogas, negarse a las pruebas, temeraria, sin carné, grave riesgo.")],
        trap=("Thinking the owner always pays, whoever drove.", "Pensar que el titular siempre responde, condujera quien condujera.")),
}

# ---------------------------------------------------------------- 1. driver
Q("dc1", "docs", "You show your licence on the miDGT app to a police officer in France. Is it valid?", "Muestras el permiso en la app miDGT a un policía en Francia. ¿Es válido?",
  [("No: the app is valid only in Spain", "No: la app solo vale en territorio nacional"), ("Yes, in the whole EU", "Sí, en toda la UE"), ("Yes, if it is up to date", "Sí, si está actualizada")],
  "Abroad you need the physical documents.", "En el extranjero hacen falta los documentos físicos.")
Q("dc2", "docs", "Which format of the licence does the DGT recommend most?", "¿Qué formato del permiso recomienda más la DGT?",
  [("The physical original", "El formato físico original"), ("A photo on your phone", "Una foto en el móvil"), ("A plain photocopy", "Una fotocopia simple")],
  "It can be checked in any situation.", "Permite su verificación en cualquier situación.")
Q("dc3", "docs", "May a person hold two driving licences from two EU countries?", "¿Puede una persona tener dos permisos de dos países de la UE?",
  [("No; one of them will be withdrawn", "No; se le retirará el que proceda"), ("Yes", "Sí"), ("Yes, if they are different classes", "Sí, si son de clases distintas")],
  "Only one EU licence per person.", "Solo un permiso de la UE por persona.")
Q("dc4", "docs", "Having to wear glasses to drive makes your licence…", "Tener que llevar gafas para conducir hace que tu permiso sea…",
  [("still ordinary", "ordinario igualmente"), ("extraordinary", "extraordinario"), ("temporary", "temporal")],
  "Glasses or hearing aids do not make it extraordinary.", "Las gafas o audífonos no lo convierten en extraordinario.")
Q("dc5", "docs", "Someone is caught using a hidden earpiece in the driving test. Apart from the fine…", "Pillan a alguien con un pinganillo en el examen. Además de la multa…",
  [("they cannot take tests for six months", "no puede presentarse a las pruebas durante seis meses"), ("they lose 6 points", "pierde 6 puntos"), ("nothing else", "nada más")],
  "It is a very serious offence.", "Es una infracción muy grave.")
Q("dc6", "docs", "Who declares you fit (apto) in the licence tests?", "¿Quién te declara apto en las pruebas del permiso?",
  [("The Provincial Traffic Office", "La Jefatura Provincial de Tráfico"), ("The driving school", "La autoescuela"), ("The town hall", "El ayuntamiento")],
  "It also issues the licences.", "También expide los permisos.")
Q("dc7", "docs", "After an injury you lose the fitness to drive, but your licence is still in force. You…", "Tras una lesión pierdes las aptitudes, pero tu permiso sigue vigente. Tú…",
  [("may not drive until you recover", "no puedes conducir hasta recuperarlas"), ("may drive until it expires", "puedes conducir hasta que caduque"), ("may drive in town only", "puedes conducir solo en poblado")],
  "If the car must be adapted, tell the Traffic Office.", "Si hay que adaptar el vehículo, se comunica a la Jefatura.")
Q("dc8", "docs", "Which tests must you pass for a licence?", "¿Qué pruebas hay que superar para el permiso?",
  [("Knowledge, skills, aptitudes and behaviour", "Conocimientos, habilidades, aptitudes y comportamientos"), ("Only a theory test", "Solo un examen teórico"), ("A medical test only", "Solo un reconocimiento médico")],
  "Plus the physical and mental fitness.", "Además de las aptitudes psicofísicas.")
Q("cl1", "classes", "The LCM licence (reduced-mobility vehicles) can be obtained from age…", "La licencia LCM (vehículos de movilidad reducida) se puede obtener desde los…",
  [("14", "14 años"), ("15", "15 años"), ("16", "16 años")],
  "LVA from 16.", "La LVA, desde los 16.")
Q("cl2", "classes", "The LVA licence allows…", "La licencia LVA permite conducir…",
  [("self-propelled agricultural special vehicles within ordinary limits or ≤ 45 km/h", "vehículos especiales agrícolas autopropulsados dentro de los límites ordinarios o ≤ 45 km/h"), ("mopeds", "ciclomotores"), ("tractors of any size", "tractores de cualquier tamaño")],
  "From age 16.", "Desde los 16 años.")
Q("cl3", "classes", "The minimum age for the AM licence is…", "La edad mínima para el permiso AM es…",
  [("15", "15 años"), ("14", "14 años"), ("16", "16 años")],
  "Mopeds and light quadricycles.", "Ciclomotores y cuadriciclos ligeros.")
Q("cl4", "classes", "An A1 lets you ride motorcycles of at most…", "El A1 permite conducir motos de como máximo…",
  [("125 cc and 11 kW", "125 c.c. y 11 kW"), ("250 cc and 25 kW", "250 c.c. y 25 kW"), ("35 kW", "35 kW")],
  "And 0.1 kW/kg.", "Y 0,1 kW/kg.")
Q("cl5", "classes", "An A1 also lets you drive motor tricycles of up to…", "El A1 permite también triciclos de motor de hasta…",
  [("15 kW", "15 kW"), ("11 kW", "11 kW"), ("any power", "cualquier potencia")],
  "Over 15 kW you need A or B and age 21.", "Por encima, A o B y 21 años.")
Q("cl6", "classes", "An A2 allows motorcycles up to…", "El A2 permite motocicletas de hasta…",
  [("35 kW and 0.2 kW/kg, not derived from over double the power", "35 kW y 0,2 kW/kg, no derivadas de más del doble de potencia"), ("125 cc", "125 c.c."), ("any power", "cualquier potencia")],
  "From age 18.", "Desde los 18 años.")
Q("cl7", "classes", "To get the A licence you must…", "Para obtener el permiso A hay que…",
  [("have held an A2 for at least 2 years and pass a training course", "tener el A2 con al menos 2 años y superar una formación"), ("be 18", "tener 18 años"), ("have held a B for 3 years", "tener el B con 3 años")],
  "Minimum age 20.", "Edad mínima 20 años.")
Q("cl8", "classes", "To drive a motor tricycle of more than 15 kW you must be at least…", "Para conducir un triciclo de motor de más de 15 kW hay que tener al menos…",
  [("21", "21 años"), ("18", "18 años"), ("20", "20 años")],
  "With an A or a B.", "Con permiso A o B.")
Q("cl9", "classes", "Which licence lets a 15-year-old drive a light quadricycle?", "¿Qué permiso permite a alguien de 15 años conducir un cuadriciclo ligero?",
  [("AM", "AM"), ("A1", "A1"), ("B", "B")],
  "AM: mopeds and light quadricycles.", "AM: ciclomotores y cuadriciclos ligeros.")
Q("pb1", "permb", "A B licence lets you drive a car with at most…", "El permiso B permite conducir un automóvil de como máximo…",
  [("3,500 kg MMA and 8 passengers plus the driver", "3.500 kg de MMA y 8 pasajeros además del conductor"), ("3,500 kg and 9 passengers plus the driver", "3.500 kg y 9 pasajeros además del conductor"), ("4,250 kg and 8 passengers", "4.250 kg y 8 pasajeros")],
  "More than 9 seats needs a D licence.", "Más de 9 plazas exige el D.")
Q("pb2", "permb", "With a B licence held for more than 3 years you may ride in Spain…", "Con el B de más de 3 años puedes conducir en España…",
  [("A1 motorcycles (up to 125 cc)", "motos del A1 (hasta 125 c.c.)"), ("any motorcycle", "cualquier moto"), ("no motorcycle", "ninguna moto")],
  "Only in Spain.", "Solo en territorio nacional.")
Q("pb3", "permb", "A B licence lets you tow a light trailer of MMA up to…", "El B permite arrastrar un remolque ligero de MMA hasta…",
  [("750 kg", "750 kg"), ("1,000 kg", "1.000 kg"), ("3,500 kg", "3.500 kg")],
  "Heavier ones if the combination is ≤ 4,250 kg.", "Más pesados si el conjunto ≤ 4.250 kg.")
Q("pb4", "permb", "With B, a car and heavier trailer weigh 4,000 kg together. You need…", "Con el B, un turismo y un remolque no ligero suman 4.000 kg. Necesitas…",
  [("the B96 authorisation", "la autorización B96"), ("nothing more", "nada más"), ("a C1 licence", "el permiso C1")],
  "Combination over 3,500 kg and up to 4,250 kg.", "Conjunto de más de 3.500 kg y hasta 4.250 kg.")
Q("pb5", "permb", "With B for more than 2 years you may drive in Spain alternative-fuel goods vehicles up to…", "Con el B de más de 2 años puedes conducir en España vehículos de mercancías de combustibles alternativos de hasta…",
  [("4,250 kg MMA, without a trailer", "4.250 kg de MMA, sin remolque"), ("3,500 kg with a trailer", "3.500 kg con remolque"), ("7,500 kg", "7.500 kg")],
  "The extra mass must come only from the propulsion system.", "El exceso debe proceder solo del sistema de propulsión.")
Q("pb6", "permb", "With B you may drive a non-agricultural special vehicle if it does not exceed…", "Con el B puedes conducir un vehículo especial no agrícola si no excede de…",
  [("40 km/h and 3,500 kg", "40 km/h y 3.500 kg"), ("45 km/h and 4,250 kg", "45 km/h y 4.250 kg"), ("25 km/h", "25 km/h")],
  "At most 9 people including the driver.", "Como máximo 9 personas con el conductor.")
Q("pb7", "permb", "The B+E licence covers a B vehicle with a trailer of MMA up to…", "El B+E permite un vehículo del B con remolque de MMA hasta…",
  [("3,500 kg", "3.500 kg"), ("750 kg", "750 kg"), ("unlimited", "sin límite")],
  "Minimum age 18.", "Edad mínima 18 años.")
Q("pb8", "permb", "The D1 or D licence is for automobiles with…", "El permiso D1 o D es para automóviles de…",
  [("more than nine seats, driver included", "más de nueve plazas, incluido el conductor"), ("more than 3,500 kg", "más de 3.500 kg"), ("trailers over 750 kg", "remolques de más de 750 kg")],
  "C1/C: over 3,500 kg.", "C1/C: más de 3.500 kg.")
Q("pb9", "permb", "Does a B licence let you drive mopeds?", "¿El permiso B permite conducir ciclomotores?",
  [("Yes", "Sí"), ("No", "No"), ("Only three-wheeled ones", "Solo de tres ruedas")],
  "And reduced-mobility vehicles.", "Y vehículos de movilidad reducida.")
Q("va1", "validity", "Until what age is a B licence renewed every 10 years?", "¿Hasta qué edad se renueva el B cada 10 años?",
  [("65", "65 años"), ("60", "60 años"), ("70", "70 años")],
  "From 65, every 5 years.", "Desde los 65, cada 5 años.")
Q("va2", "validity", "Your licence expired last week. May you drive?", "Tu permiso caducó la semana pasada. ¿Puedes conducir?",
  [("No; if you do, it is withdrawn on the spot", "No; si lo usas, se interviene inmediatamente"), ("Yes, for 3 months", "Sí, durante 3 meses"), ("Yes, in town", "Sí, en poblado")],
  "An expired licence does not authorise driving.", "Caducado no autoriza a conducir.")
Q("va3", "validity", "You change address. You must tell the Traffic Office about your licence within…", "Cambias de domicilio. Debes comunicarlo a la Jefatura para tu permiso en…",
  [("15 days", "15 días"), ("30 days", "30 días"), ("10 days", "10 días")],
  "They issue a duplicate.", "Expiden un duplicado.")
Q("va4", "validity", "The novice plate V-13 must be placed…", "La señal V-13 de conductor novel se coloca…",
  [("somewhere visible at the rear left", "en un lugar visible de la parte posterior izquierda"), ("at the rear right", "detrás a la derecha"), ("on the windscreen", "en el parabrisas")],
  "Motorcycles: visible at the rear.", "En motos, en un sitio visible detrás.")
Q("va5", "validity", "For how long must a new driver display the “L”?", "¿Durante cuánto tiempo debe llevar la «L» un conductor novel?",
  [("The first year", "El primer año"), ("Two years", "Dos años"), ("Six months", "Seis meses")],
  "Extended by any suspension.", "Se amplía si se suspende el permiso.")
Q("va6", "validity", "A novice’s licence is suspended for 2 months. The “L” period…", "A un novel le suspenden el permiso 2 meses. El periodo de la «L»…",
  [("is extended by 2 months", "se amplía 2 meses"), ("stays the same", "no cambia"), ("starts again", "vuelve a empezar")],
  "The same period is added.", "Se añade el mismo periodo.")
Q("va7", "validity", "The V-13 is…", "La V-13 es…",
  [("retroreflective, green with a white “L”", "reflectante, verde con la «L» blanca"), ("white with a red “L”", "blanca con «L» roja"), ("blue with a white “L”", "azul con «L» blanca")],
  "V-14 is the learner plate.", "La V-14 es la de aprendizaje.")
Q("va8", "validity", "You lose your licence. You must…", "Pierdes tu permiso. Debes…",
  [("notify the Traffic Office to get a duplicate", "notificarlo a la Jefatura para obtener un duplicado"), ("wait until it expires", "esperar a que caduque"), ("take the tests again", "repetir las pruebas")],
  "Return the original if it turns up.", "Devolver el original si aparece.")
Q("va9", "validity", "A licence loses its validity when the holder…", "Un permiso pierde su vigencia cuando el titular…",
  [("loses all the points or the requirements", "pierde todos los puntos o los requisitos"), ("changes address", "cambia de domicilio"), ("turns 65", "cumple 65 años")],
  "The office notifies it within six months at most.", "La Jefatura lo notifica en un máximo de seis meses.")
Q("va10", "validity", "Driving during a precautionary suspension counts as…", "Conducir durante una suspensión cautelar equivale a…",
  [("driving with the licence suspended by sanction", "conducir con la autorización suspendida por sanción"), ("a minor offence", "una infracción leve"), ("driving without the L plate", "conducir sin la «L»")],
  "The suspension comes with immediate withdrawal.", "Va con la intervención inmediata del permiso.")

# ---------------------------------------------------------------- 2. vehicle
Q("vd1", "vehdocs", "Which documents must be in the vehicle?", "¿Qué documentos deben llevarse en el vehículo?",
  [("Registration certificate and ITV card (originals or certified copies)", "Permiso de circulación y tarjeta ITV (originales o fotocopias cotejadas)"), ("Only the insurance receipt", "Solo el recibo del seguro"), ("The purchase invoice", "La factura de compra")],
  "Plus the last ITV report if it has passed one.", "Y el último informe ITV si ya la pasó.")
Q("vd2", "vehdocs", "A registration certificate is compulsory for…", "El permiso de circulación es obligatorio para…",
  [("all motor vehicles and trailers over 750 kg", "todos los vehículos de motor y remolques de más de 750 kg"), ("all trailers", "todos los remolques"), ("only cars", "solo turismos")],
  "Light trailers are not registered.", "Los ligeros no se matriculan.")
Q("vd3", "vehdocs", "You sell your car. You (the seller) must notify the Traffic Office within…", "Vendes tu coche. Tú (vendedor) debes notificarlo a la Jefatura en…",
  [("10 days", "10 días"), ("30 days", "30 días"), ("15 days", "15 días")],
  "The buyer has 30 days to apply for the new certificate.", "El comprador tiene 30 días para la renovación.")
Q("vd4", "vehdocs", "The buyer does not apply for the registration change within 30 days. Then…", "El comprador no solicita el cambio en 30 días. Entonces…",
  [("the vehicle may not be driven and is immobilised", "el vehículo no puede circular y se inmoviliza"), ("nothing happens", "no pasa nada"), ("the seller keeps the car", "el vendedor recupera el coche")],
  "Within 30 days of buying.", "En 30 días desde la adquisición.")
Q("vd5", "vehdocs", "How many plates does a motorcycle carry?", "¿Cuántas placas lleva una motocicleta?",
  [("One, at the rear", "Una, detrás"), ("Two, front and rear", "Dos, delante y detrás"), ("None", "Ninguna")],
  "Same for mopeds and self-propelled special vehicles.", "Igual ciclomotores y especiales autopropulsados.")
Q("vd6", "vehdocs", "A trailer of 600 kg MMA carries…", "Un remolque de 600 kg de MMA lleva…",
  [("one plate, the same as the towing vehicle’s, in the centre or on the left", "una placa igual que la del tractor, en el centro o a la izquierda"), ("its own red plate", "su propia placa roja"), ("no plate", "ninguna placa")],
  "Light trailers are not registered.", "Los ligeros no se matriculan.")
Q("vd7", "vehdocs", "A trailer of 1,500 kg MMA carries…", "Un remolque de 1.500 kg de MMA lleva…",
  [("the towing vehicle’s plate on the right and its own red plate", "la placa del tractor a la derecha y su propia placa roja"), ("only the towing vehicle’s plate", "solo la placa del tractor"), ("only a red plate", "solo una placa roja")],
  "Over 750 kg: two plates.", "Más de 750 kg: dos placas.")
Q("vd8", "vehdocs", "Who must make sure the plates can be read?", "¿Quién debe verificar que las placas se pueden leer?",
  [("The driver", "El conductor"), ("The owner only", "Solo el titular"), ("The ITV station", "La estación ITV")],
  "Nothing may hide or hinder them.", "Nada debe impedir o dificultar su lectura.")
Q("vd9", "vehdocs", "The owner changes address without selling the car. They notify it within…", "El titular cambia de domicilio sin vender el coche. Lo comunica en…",
  [("15 days", "15 días"), ("10 days", "10 días"), ("3 months", "3 meses")],
  "Name, surname or address.", "Nombre, apellidos o domicilio.")
Q("it1", "itv", "How many days early can you pass the ITV without losing validity?", "¿Con cuántos días de antelación se puede pasar la ITV sin perder vigencia?",
  [("Up to 30 calendar days", "Hasta 30 días naturales"), ("Up to 15 days", "Hasta 15 días"), ("Up to 3 months", "Hasta 3 meses")],
  "The new period starts when the old one ends.", "La nueva vigencia empieza al terminar la anterior.")
Q("it2", "itv", "A private car is first inspected when it is…", "Un turismo particular pasa su primera ITV a los…",
  [("4 years old", "4 años"), ("2 years old", "2 años"), ("3 years old", "3 años")],
  "Then every 2 years until 10, and yearly after.", "Después cada 2 años hasta los 10, y anual.")
Q("it3", "itv", "A private car more than 10 years old passes the ITV…", "Un turismo de más de 10 años pasa la ITV…",
  [("every year", "cada año"), ("every 2 years", "cada 2 años"), ("every 6 months", "cada 6 meses")],
  "Every 6 months is for vans over 10 years.", "Cada 6 meses: furgonetas de más de 10 años.")
Q("it4", "itv", "A two-wheel moped is exempt from ITV until it is…", "Un ciclomotor de dos ruedas está exento de ITV hasta los…",
  [("3 years old", "3 años"), ("4 years old", "4 años"), ("5 years old", "5 años")],
  "Then every 2 years.", "Después cada 2 años.")
Q("it5", "itv", "A van (goods ≤ 3.5 t) that is 11 years old passes the ITV…", "Una furgoneta (mercancías ≤ 3,5 t) de 11 años pasa la ITV…",
  [("every 6 months", "cada 6 meses"), ("every year", "cada año"), ("every 2 years", "cada 2 años")],
  "Exempt 2, biennial to 6, annual to 10.", "Exenta 2, bienal hasta 6, anual hasta 10.")
Q("it6", "itv", "The V-19 sticker goes on a car…", "El distintivo V-19 se coloca en un turismo…",
  [("in the top right corner of the windscreen, inside", "en el ángulo superior derecho del parabrisas, por dentro"), ("on the rear window", "en la luna trasera"), ("next to the rear plate", "junto a la placa trasera")],
  "On trailers: somewhere visible.", "En remolques: en un lugar visible.")
Q("it7", "itv", "Result “unfavourable” at the ITV. You…", "Resultado «desfavorable» en la ITV. Tú…",
  [("may only drive to the workshop and back to the ITV", "solo puedes ir al taller y volver a la ITV"), ("may drive normally for 2 months", "puedes circular normalmente 2 meses"), ("must call a tow truck", "debes llamar a una grúa")],
  "Negative: tow truck.", "Negativa: grúa.")
Q("it8", "itv", "Result “negative” at the ITV means…", "Resultado «negativo» en la ITV significa…",
  [("dangerous defects: the vehicle leaves by other means (tow truck)", "defectos peligrosos: el vehículo sale por medios ajenos (grúa)"), ("you can go to the workshop", "puedes ir al taller"), ("you passed with remarks", "has pasado con observaciones")],
  "It may not be driven.", "No puede circular.")
Q("it9", "itv", "After an unfavourable or negative ITV, the owner has to repair the vehicle within…", "Tras una ITV desfavorable o negativa, el titular debe repararlo en…",
  [("up to 2 months", "hasta 2 meses"), ("6 months", "6 meses"), ("1 year", "1 año")],
  "The ITV decree gives no more than two months (your course says less than two); otherwise the station proposes deregistering it.", "El decreto de ITV da un plazo no superior a dos meses (tu curso dice inferior); si no, el centro propone su baja.")
Q("it10", "itv", "Stopped with the ITV out of date, the agent gives you a slip (volante) to pass it within…", "Te paran con la ITV caducada y el agente te da un volante para pasarla en…",
  [("10 days", "10 días"), ("30 days", "30 días"), ("2 months", "2 meses")],
  "Otherwise the vehicle is sealed off.", "Si no, se acuerda el precinto.")
Q("it11", "itv", "Do light trailers (≤ 750 kg) pass periodic ITV?", "¿Pasan ITV periódica los remolques ligeros (≤ 750 kg)?",
  [("No, but they need an ITV card", "No, pero sí necesitan tarjeta ITV"), ("Yes, every year", "Sí, cada año"), ("Yes, every 2 years", "Sí, cada 2 años")],
  "No periodic inspection.", "Sin inspecciones periódicas.")
Q("it12", "itv", "After a major modification (e.g. fitting a tow bar) the vehicle must…", "Tras una reforma de importancia (p. ej., un enganche) el vehículo debe…",
  [("pass an extraordinary inspection before being driven", "pasar una inspección extraordinaria antes de circular"), ("wait for the next periodic ITV", "esperar a la próxima ITV periódica"), ("only inform the insurer", "solo avisar a la aseguradora")],
  "Modifications appear on the back of the card.", "Las reformas constan en el reverso.")
Q("it13", "itv", "The NIVE on an e-ITV has…", "El NIVE de una e-ITV tiene…",
  [("32 characters", "32 dígitos"), ("17 characters", "17 dígitos"), ("10 characters", "10 dígitos")],
  "The car’s “ID card”.", "El «DNI del coche».")
Q("it14", "itv", "May you choose which ITV station to use?", "¿Puedes elegir la estación ITV?",
  [("Yes, for the first and later inspections", "Sí, para la primera y las siguientes"), ("No, the one assigned", "No, la asignada"), ("Only for the first", "Solo para la primera")],
  "Free choice.", "Libertad de elección.")
Q("it15", "itv", "A towed caravan of 1,200 kg is exempt from ITV until it is…", "Una caravana remolcada de 1.200 kg está exenta de ITV hasta los…",
  [("6 years old", "6 años"), ("4 years old", "4 años"), ("10 years old", "10 años")],
  "Then every 2 years.", "Después cada 2 años.")
Q("in1", "insurance", "Which of these must have compulsory insurance?", "¿Cuál de estos debe tener seguro obligatorio?",
  [("A trailer of 1,000 kg MMA", "Un remolque de 1.000 kg de MMA"), ("A trailer of 600 kg MMA", "Un remolque de 600 kg de MMA"), ("A bicycle", "Una bicicleta")],
  "Trailers over 750 kg.", "Remolques de más de 750 kg.")
Q("in2", "insurance", "You cause an accident. The compulsory insurance does NOT pay for…", "Causas un accidente. El seguro obligatorio NO paga…",
  [("your own injuries", "tus propias lesiones"), ("the injuries of the other driver", "las lesiones del otro conductor"), ("the other car’s damage", "los daños del otro coche")],
  "Nor your own vehicle.", "Ni tu propio vehículo.")
Q("in3", "insurance", "Your passenger (your brother) is injured in an accident you caused. The compulsory insurance…", "Tu pasajero (tu hermano) resulta herido en un accidente que causaste. El seguro obligatorio…",
  [("covers his injuries", "cubre sus lesiones"), ("covers nothing", "no cubre nada"), ("covers only his phone", "solo cubre su móvil")],
  "Relatives’ injuries are covered; their property is not.", "Las lesiones de los parientes sí; sus bienes, no.")
Q("in4", "insurance", "Damage to the policyholder’s or the driver’s relatives’ property is…", "Los daños a los bienes del tomador o de los parientes del conductor…",
  [("not covered", "no están cubiertos"), ("covered", "están cubiertos"), ("covered up to 750 €", "están cubiertos hasta 750 €")],
  "Up to the third degree.", "Hasta el tercer grado.")
Q("in5", "insurance", "Are a vehicle’s defects or breakages force majeure that frees the insurer?", "¿Los defectos o roturas del vehículo son fuerza mayor que libera a la aseguradora?",
  [("No", "No"), ("Yes", "Sí"), ("Only the brakes", "Solo los frenos")],
  "They are not considered force majeure.", "No se consideran fuerza mayor.")
Q("in6", "insurance", "How do agents usually check that a vehicle is insured?", "¿Cómo comprueban normalmente los agentes que un vehículo está asegurado?",
  [("By checking the FIVA database", "Consultando el Fichero Informativo de Vehículos Asegurados"), ("By asking the insurer by phone", "Llamando a la aseguradora"), ("By looking at a windscreen sticker", "Mirando una pegatina")],
  "If not possible, the driver shows the receipt.", "Si no es posible, el conductor presenta el recibo.")
Q("in7", "insurance", "Driving an uninsured vehicle leads to…", "Circular con un vehículo sin seguro conlleva…",
  [("a ban on driving it, impounding or sealing, and a fine", "prohibición de circular, depósito o precinto y multa"), ("only a warning", "solo un aviso"), ("losing 12 points", "perder 12 puntos")],
  "Not a points offence.", "No es infracción de puntos.")
Q("in8", "insurance", "Where should you fill in the accident report form?", "¿Dónde se debe rellenar el parte amistoso?",
  [("In a safe place off the road", "En un lugar seguro fuera de la vía"), ("On the carriageway, next to the cars", "En la calzada, junto a los coches"), ("On the hard shoulder", "En el arcén")],
  "It is forbidden on the road platform.", "Prohibido en la plataforma de circulación.")
Q("in9", "insurance", "The accident report form is sent to…", "La declaración amistosa de accidente se entrega a…",
  [("your own insurer", "tu propia aseguradora"), ("the other driver’s insurer", "la aseguradora del otro conductor"), ("the Traffic Office", "la Jefatura de Tráfico")],
  "It speeds up payment for material damage.", "Agiliza las indemnizaciones de daños materiales.")
Q("in10", "insurance", "Since 2026, which vehicles also need compulsory insurance after being registered with the DGT?", "Desde 2026, ¿qué vehículos necesitan también seguro obligatorio tras inscribirse en la DGT?",
  [("Personal mobility vehicles (e-scooters)", "Los vehículos de movilidad personal (patinetes)"), ("Bicycles", "Las bicicletas"), ("Light trailers", "Los remolques ligeros")],
  "Ley 5/2025, in force since 2 January 2026.", "Ley 5/2025, vigente desde el 2 de enero de 2026.")
Q("in11", "insurance", "A drunk driver causes an accident. The victims…", "Un conductor ebrio causa un accidente. Las víctimas…",
  [("are paid by the insurer, which can then claim it back from the driver", "cobran de la aseguradora, que después puede repetir contra el conductor"), ("get nothing", "no cobran nada"), ("must sue the Traffic Office", "deben reclamar a Tráfico")],
  "The driver ends up paying.", "Al final paga el conductor.")
Q("in12", "insurance", "Who should take out the vehicle’s compulsory insurance?", "¿Quién debe concertar el seguro obligatorio?",
  [("The owner", "El propietario"), ("The usual driver", "El conductor habitual"), ("The seller", "El vendedor")],
  "If someone else signs it, they are the policyholder.", "Si lo contrata otro, es el tomador.")

# ---------------------------------------------------------------- 3. points
Q("pt1", "points", "A driver with more than 2 years’ licence and no sanctions starts with…", "Un conductor con más de 2 años de permiso y sin sanciones parte de…",
  [("12 points", "12 puntos"), ("8 points", "8 puntos"), ("15 points", "15 puntos")],
  "Bonus points come later.", "La bonificación llega después.")
Q("pt2", "points", "A newly qualified driver has…", "Un conductor que acaba de obtener el permiso tiene…",
  [("8 points", "8 puntos"), ("12 points", "12 puntos"), ("6 points", "6 puntos")],
  "Unless they held another licence for more than 2 years.", "Salvo que tuviera otro permiso de más de 2 años.")
Q("pt3", "points", "The maximum number of points is…", "El máximo de puntos es…",
  [("15", "15"), ("12", "12"), ("14", "14")],
  "+2 after 3 clean years, +1 after 3 more.", "+2 tras 3 años sin sanción, +1 tras otros 3.")
Q("pt4", "points", "With 12 points and no firm sanctions for 3 years, you get…", "Con 12 puntos y sin sanciones firmes durante 3 años, obtienes…",
  [("+2 points", "+2 puntos"), ("+1 point", "+1 punto"), ("+3 points", "+3 puntos")],
  "Then +1 for the next 3 years.", "Después, +1 por los 3 siguientes.")
Q("pt5", "points", "You get your licence back after losing all your points. You start with…", "Recuperas el permiso tras perder todos los puntos. Empiezas con…",
  [("8 points", "8 puntos"), ("12 points", "12 puntos"), ("4 points", "4 puntos")],
  "Same class and seniority.", "Misma clase y antigüedad.")
Q("pt6", "points", "In one day you commit several serious offences worth 10 points. You lose…", "En un día cometes varias infracciones graves que suman 10 puntos. Pierdes…",
  [("8 points", "8 puntos"), ("10 points", "10 puntos"), ("12 points", "12 puntos")],
  "Unless one of them is very serious.", "Salvo que alguna sea muy grave.")
Q("pt7", "points", "You lost 4 points 2 years ago and have had no sanctions since. Now you have…", "Perdiste 4 puntos hace 2 años y no has tenido sanciones desde entonces. Ahora tienes…",
  [("your full initial 12 points back", "de nuevo tus 12 puntos iniciales"), ("8 points", "8 puntos"), ("10 points", "10 puntos")],
  "Automatic recovery after 2 years.", "Recuperación automática tras 2 años.")
Q("pt8", "points", "You hold a B and a C licence. Your points…", "Tienes permiso B y C. Tus puntos…",
  [("are one single credit for both", "son un único crédito para ambos"), ("are 12 per licence", "son 12 por permiso"), ("count only for B", "cuentan solo para el B")],
  "One credit for all licences.", "Crédito único para todas las autorizaciones.")
Q("pt9", "points", "Points are taken away when…", "Los puntos se pierden cuando…",
  [("an administrative sanction for a serious or very serious offence becomes final", "una sanción administrativa por infracción grave o muy grave es firme"), ("the agent stops you", "el agente te para"), ("you receive the notice", "recibes la notificación")],
  "Minor offences don’t take points.", "Las leves no quitan puntos.")
Q("if1", "infra", "Driving while holding your mobile phone in your hand costs…", "Conducir sujetando el móvil con la mano supone perder…",
  [("6 points", "6 puntos"), ("3 points", "3 puntos"), ("4 points", "4 puntos")],
  "Headphones: 3 points.", "Auriculares: 3 puntos.")
Q("if2", "infra", "Driving with headphones connected to a music player costs…", "Conducir con auriculares conectados a un reproductor supone perder…",
  [("3 points", "3 puntos"), ("6 points", "6 puntos"), ("no points", "ningún punto")],
  "So does a radar detector.", "Igual que un detector de radar.")
Q("if3", "infra", "Not using the seat belt costs…", "No usar el cinturón de seguridad supone perder…",
  [("4 points", "4 puntos"), ("3 points", "3 puntos"), ("6 points", "6 puntos")],
  "Same for helmets and child seats.", "Igual casco y SRI.")
Q("if4", "infra", "A general driver blows 0.40 mg/l. They lose…", "Un conductor general da 0,40 mg/l. Pierde…",
  [("4 points", "4 puntos"), ("6 points", "6 puntos"), ("no points", "ningún punto")],
  "Over 0.25 up to 0.50: 4 points.", "Más de 0,25 hasta 0,50: 4 puntos.")
Q("if5", "infra", "A driver with a 1-year-old licence blows 0.35 mg/l. They lose…", "Un conductor con permiso de 1 año da 0,35 mg/l. Pierde…",
  [("6 points", "6 puntos"), ("4 points", "4 puntos"), ("3 points", "3 puntos")],
  "For new drivers, over 0.30 is double the limit.", "Para noveles, más de 0,30 es el doble.")
Q("if6", "infra", "Refusing the alcohol test costs…", "Negarse a la prueba de alcohol supone perder…",
  [("6 points", "6 puntos"), ("4 points", "4 puntos"), ("3 points", "3 puntos")],
  "It can also be a crime.", "También puede ser delito.")
Q("if7", "infra", "Running a red light costs…", "Saltarse un semáforo en rojo supone perder…",
  [("4 points", "4 puntos"), ("6 points", "6 puntos"), ("2 points", "2 puntos")],
  "Same for STOP and give way.", "Igual el stop y el ceda.")
Q("if8", "infra", "Overtaking a cyclist without leaving 1.5 m costs…", "Adelantar a un ciclista sin dejar 1,5 m supone perder…",
  [("6 points", "6 puntos"), ("4 points", "4 puntos"), ("3 points", "3 puntos")],
  "Since the 2021 reform.", "Desde la reforma de 2021.")
Q("if9", "infra", "Reversing on a motorway costs…", "Dar marcha atrás en autopista supone perder…",
  [("4 points", "4 puntos"), ("3 points", "3 puntos"), ("6 points", "6 puntos")],
  "Driving the wrong way: 6.", "Sentido contrario: 6.")
Q("if10", "infra", "On a 90 km/h road you are caught at 130 km/h. Fine and points?", "En una vía de 90 km/h te cazan a 130 km/h. ¿Multa y puntos?",
  [("300 € and 2 points", "300 € y 2 puntos"), ("100 € and no points", "100 € y sin puntos"), ("400 € and 4 points", "400 € y 4 puntos")],
  "121–140 on a 90 road.", "121–140 en vía de 90.")
Q("if11", "infra", "In a 50 km/h street you are caught at 65 km/h. You get…", "En una calle de 50 km/h te cazan a 65 km/h. Te ponen…",
  [("100 € and no points", "100 € y sin puntos"), ("300 € and 2 points", "300 € y 2 puntos"), ("only a warning", "solo un aviso")],
  "51–70 on a 50 street.", "51–70 en vía de 50.")
Q("if12", "infra", "On a 120 km/h motorway you are caught at 195 km/h. That is…", "En autopista de 120 km/h te cazan a 195 km/h. Es…",
  [("very serious: 600 € and 6 points", "muy grave: 600 € y 6 puntos"), ("400 € and 4 points", "400 € y 4 puntos"), ("300 € and 2 points", "300 € y 2 puntos")],
  "191 or more on a 120 road. It can also be a crime above 200.", "191 o más en vía de 120. Por encima de 200 puede ser delito.")
Q("if13", "infra", "Throwing a lit cigarette out of the window costs…", "Tirar una colilla encendida por la ventanilla supone perder…",
  [("6 points", "6 puntos"), ("4 points", "4 puntos"), ("no points", "ningún punto")],
  "Objects that can cause fires or accidents.", "Objetos que puedan provocar incendios o accidentes.")
Q("if14", "infra", "Not keeping the safety distance costs…", "No mantener la distancia de seguridad supone perder…",
  [("4 points", "4 puntos"), ("3 points", "3 puntos"), ("6 points", "6 puntos")],
  "A serious offence.", "Infracción grave.")
Q("cs1", "courses", "A partial points course lets you recover…", "Un curso de recuperación parcial permite recuperar…",
  [("up to 4 points", "hasta 4 puntos"), ("up to 6 points", "hasta 6 puntos"), ("all 12 points", "los 12 puntos")],
  "Never more than you lost.", "Nunca más de los perdidos.")
Q("cs2", "courses", "How often may a non-professional driver do a partial points course?", "¿Cada cuánto puede hacer un curso parcial un conductor no profesional?",
  [("Once every 2 years", "Una vez cada 2 años"), ("Once a year", "Una vez al año"), ("Whenever they want", "Cuando quiera")],
  "Professionals: once a year.", "Profesionales: una vez al año.")
Q("cs3", "courses", "How long is the partial recovery course?", "¿Cuánto dura el curso de recuperación parcial?",
  [("10 hours", "10 horas"), ("20 hours", "20 horas"), ("4 hours", "4 horas")],
  "The licence course lasts 20 hours.", "El de recuperación del permiso, 20 horas.")
Q("cs4", "courses", "To get your licence back after losing all points you must…", "Para recuperar el permiso tras perder todos los puntos debes…",
  [("pass a 20-hour course and a test at the Traffic Office", "superar un curso de 20 horas y un test en la Jefatura"), ("only wait 2 years", "solo esperar 2 años"), ("take a driving test again", "repetir el examen práctico")],
  "After the waiting period.", "Tras el plazo de espera.")
Q("cs5", "courses", "A non-professional loses their licence for the first time. They must wait before the course…", "Un no profesional pierde el permiso por primera vez. Debe esperar antes del curso…",
  [("6 months", "6 meses"), ("3 months", "3 meses"), ("1 year", "1 año")],
  "Professionals 3 months; doubled if repeated within 3 years.", "Profesionales 3 meses; el doble si se repite en 3 años.")
Q("cs6", "courses", "A court bans someone from driving for 18 months. To drive again they need…", "Un juez priva a alguien del derecho a conducir 18 meses. Para volver a conducir necesita…",
  [("only the course", "solo el curso"), ("the course and the test", "el curso y el test"), ("a new licence from scratch", "un permiso nuevo desde cero")],
  "Course and test if the ban was over 2 years.", "Curso y test si la condena supera 2 años.")
Q("cs7", "courses", "The licence obtained again after a recovery course has…", "El permiso recuperado tras el curso tiene…",
  [("the same class and seniority, with 8 points", "la misma clase y antigüedad, con 8 puntos"), ("a new seniority and 12 points", "nueva antigüedad y 12 puntos"), ("B only, 8 points", "solo el B, con 8 puntos")],
  "Like a new driver’s balance.", "Como el saldo de un novel.")

# ---------------------------------------------------------------- 4. liability
Q("lb1", "liability", "A motorcycle passenger rides without a helmet. Who is liable?", "Un pasajero de moto va sin casco. ¿Quién es responsable?",
  [("The driver", "El conductor"), ("The passenger", "El pasajero"), ("The owner", "El titular")],
  "Also for carrying passengers below the minimum age.", "También por llevar pasajeros sin la edad mínima.")
Q("lb2", "liability", "A child travels without a child seat in a private car. Who is liable?", "Un niño viaja sin SRI en un turismo particular. ¿Quién es responsable?",
  [("The driver", "El conductor"), ("The parents only", "Solo los padres"), ("Nobody", "Nadie")],
  "Except professional drivers of public services.", "Salvo conductores profesionales de servicio público.")
Q("lb3", "liability", "A 17-year-old moped rider is fined. Who else answers for the fine?", "Multan a un motorista de 17 años. ¿Quién más responde de la multa?",
  [("The parents or guardians, jointly", "Los padres o tutores, solidariamente"), ("The moped shop", "La tienda"), ("Nobody", "Nadie")],
  "Under 18.", "Menores de 18.")
Q("lb4", "liability", "Who answers for an overdue ITV?", "¿Quién responde de una ITV caducada?",
  [("The owner (titular)", "El titular"), ("The driver", "El conductor"), ("The ITV station", "La estación ITV")],
  "Also documents and condition affecting safety.", "También documentación y estado que afecte a la seguridad.")
Q("lb5", "liability", "A speed camera catches your car, which has a named habitual driver. Who is liable?", "Un radar capta tu coche, que tiene un conductor habitual designado. ¿Quién responde?",
  [("The habitual driver, unless they prove otherwise", "El conductor habitual, salvo que acredite otra cosa"), ("Always the owner", "Siempre el titular"), ("Nobody", "Nadie")],
  "Unless someone else drove or it was stolen.", "Salvo que condujera otro o hubiera sustracción.")
Q("lb6", "liability", "The owner of a vehicle must…", "El titular de un vehículo tiene la obligación de…",
  [("identify the driver at the time of an offence", "identificar al conductor en el momento de la infracción"), ("pay every fine", "pagar todas las multas"), ("drive it personally", "conducirlo personalmente")],
  "Failing to do so is itself an offence.", "No hacerlo es otra infracción.")
Q("lb14", "liability", "Since 1 October 2026, when must the owner name a habitual driver?", "Desde el 1 de octubre de 2026, ¿cuándo debe el titular designar un conductor habitual?",
  [("When a person without a driving licence registers the vehicle in their name", "Cuando una persona sin permiso de conducción matricula el vehículo a su nombre"),
   ("Always, for every vehicle", "Siempre, para todo vehículo"), ("Only for company vehicles", "Solo en los vehículos de empresa")],
  "RD 518/2026 made it compulsory when the owner is a person who cannot drive.", "El RD 518/2026 lo hizo obligatorio cuando el titular es una persona que no puede conducir.")
Q("lb7", "liability", "Driving 70 km/h over the limit in town is…", "Circular 70 km/h por encima del límite en vía urbana es…",
  [("a crime", "un delito"), ("a serious offence only", "solo una infracción grave"), ("a minor offence", "una infracción leve")],
  "More than 60 km/h over in town.", "Más de 60 km/h por encima en urbana.")
Q("lb8", "liability", "Out of town, speeding becomes a crime when you exceed the limit by more than…", "En interurbana, la velocidad es delito si superas el límite en más de…",
  [("80 km/h", "80 km/h"), ("60 km/h", "60 km/h"), ("50 km/h", "50 km/h")],
  "60 km/h in town.", "60 km/h en urbana.")
Q("lb9", "liability", "Alcohol becomes a crime above…", "El alcohol es delito por encima de…",
  [("0.60 mg/l in air (1.2 g/l in blood)", "0,60 mg/l en aire (1,2 g/l en sangre)"), ("0.50 mg/l in air", "0,50 mg/l en aire"), ("0.25 mg/l in air", "0,25 mg/l en aire")],
  "Or when driving under the influence of drugs or alcohol.", "O conduciendo bajo su influencia.")
Q("lb10", "liability", "Driving after losing all your points is…", "Conducir tras perder todos los puntos es…",
  [("a crime", "un delito"), ("a serious offence", "una infracción grave"), ("allowed in town", "permitido en poblado")],
  "Also when banned by a court or never licensed.", "También con privación judicial o sin haberlo obtenido nunca.")
Q("lb11", "liability", "Penalties of more than 2 years’ licence ban mean…", "Una pena de privación de más de 2 años supone…",
  [("the licence loses its validity", "la pérdida de vigencia del permiso"), ("4 points are lost", "perder 4 puntos"), ("nothing extra", "nada más")],
  "To drive again: course and test.", "Para volver: curso y test.")
Q("lb12", "liability", "Refusing the alcohol and drug tests can be punished with prison of…", "Negarse a las pruebas de alcohol y drogas puede castigarse con prisión de…",
  [("6 months to 1 year", "6 meses a 1 año"), ("3 to 6 months", "3 a 6 meses"), ("2 to 5 years", "2 a 5 años")],
  "Plus a 1–4 year licence ban.", "Más privación de 1 a 4 años.")
Q("lb13", "liability", "Leaving obstacles on the road or spilling slippery substances can be…", "Dejar obstáculos en la vía o derramar sustancias deslizantes puede ser…",
  [("a crime of creating serious risk", "un delito de grave riesgo para la circulación"), ("only a minor offence", "solo una infracción leve"), ("allowed with hazard lights", "permitido con la luz de emergencia")],
  "So is altering signs.", "También alterar la señalización.")
