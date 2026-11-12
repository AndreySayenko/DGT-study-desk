# -*- coding: utf-8 -*-
"""Question bank for the interactive Category A1/A2, Topic 4 page (priority). In every question the FIRST option is
the correct one (the page shuffles options when it shows them). Ids must be unique and must not start with "ai"."""

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
    "signed": dict(sec=1, en="Junctions with signs", es="Intersecciones señalizadas",
        recap=[("Priority follows agents, lights, vertical signs or markings.", "La prioridad sigue a agentes, semáforos, señales verticales o marcas viales."),
               ("Give way or STOP: give way to vehicles from either side.", "Ceda el paso o stop: ceder a los que vienen por cualquier lado."),
               ("STOP: always stop, at the line or just before the junction; stop again if you can’t see.", "Stop: detenerse siempre, en la línea o justo antes de la intersección; de nuevo si no se ve."),
               ("Order: agents → temporary signs → lights → vertical signs → markings.", "Orden: agentes → circunstancial → semáforos → verticales → marcas viales.")],
        trap=("Thinking that at a give-way sign you only give way to the right.", "Pensar que en un ceda el paso solo se cede a la derecha.")),
    "unsigned": dict(sec=1, en="Junctions without signs", es="Intersecciones sin señalizar",
        recap=[("Give way to vehicles from your right.", "Ceder el paso a los que vienen por la derecha."),
               ("Except: paved road over unpaved.", "Salvo: la vía pavimentada sobre la que no lo está."),
               ("Except: rails over everyone.", "Salvo: los raíles sobre todos."),
               ("Except: inside a roundabout or on an autopista/autovía over those entering.", "Salvo: dentro de la glorieta o en autopista/autovía sobre los que acceden.")],
        trap=("Giving way to a vehicle from the right that is entering a roundabout you are already in.", "Ceder al que viene por la derecha y entra en la glorieta en la que ya estás.")),
    "conduct": dict(sec=1, en="How to act", es="Normas de actuación",
        recap=[("Without priority: don’t force the other to change path or speed.", "Sin prioridad: no obligar al otro a cambiar de trayectoria o velocidad."),
               ("Show it early, above all by slowing down gradually.", "Demostrarlo con antelación, sobre todo reduciendo la velocidad poco a poco."),
               ("With priority: don’t enter a junction or crossing where you’ll get stuck.", "Con prioridad: no entrar en una intersección o paso donde vas a quedar detenido."),
               ("Stuck in a junction with lights: leave without waiting for green.", "Detenido en una intersección con semáforo: salir sin esperar al verde.")],
        trap=("Thinking that having priority lets you enter a blocked junction.", "Pensar que tener prioridad permite entrar en una intersección bloqueada.")),
    "vulnerable": dict(sec=2, en="Pedestrians, cyclists and animals", es="Peatones, ciclistas y animales",
        recap=[("As a rule drivers have priority on the carriageway and shoulder.", "Como norma, los conductores tienen prioridad en la calzada y el arcén."),
               ("Except: crossings and cañadas; turning into a road they are crossing; crossing a shoulder they use.", "Salvo: pasos y cañadas; al girar a una vía que están cruzando; al cruzar un arcén que usan."),
               ("Except: bus stop passengers, troops, school rows, processions; a cyclist group once the first is across.", "Salvo: viajeros en la parada, tropas, filas escolares, comitivas; grupo ciclista si el primero ya cruzó."),
               ("Since 2026: single-platform zones, pedestrians first anywhere; motorcyclists are vulnerable users.", "Desde 2026: plataforma única, el peatón primero en cualquier punto; los motoristas son usuarios vulnerables.")],
        trap=("Thinking pedestrians only have priority on a marked crossing.", "Pensar que el peatón solo tiene prioridad en un paso señalizado.")),
    "narrow": dict(sec=3, en="Narrow stretches", es="Estrechamientos",
        recap=[("Signs: R-6 blue square = you first; R-5 red circle = oncoming first.", "Señales: R-6 cuadrado azul = pasas tú; R-5 círculo rojo = pasa el que viene."),
               ("No signs: whoever entered first; in doubt, the 10-step list.", "Sin señales: el que entró primero; en duda, la lista de 10 puestos."),
               ("Motorcycles are 10th; with sidecar 9th.", "Las motos son las 10.as; con sidecar, 9.as."),
               ("Same type: longer reversing distance; steep (≥ 7 %): uphill first.", "Mismo tipo: mayor marcha atrás; pendiente (≥ 7 %): pasa el que sube.")],
        trap=("Applying the list when it is clear who entered first.", "Aplicar la lista cuando está claro quién entró primero.")),
    "bridge": dict(sec=3, en="Bridges", es="Puentes",
        recap=[("Narrow bridge: follow its signs.", "Puente estrecho: seguir su señalización."),
               ("R-5 or give way at one end: who came in that way reverses.", "R-5 o ceda el paso en un extremo: retrocede quien entró por ahí."),
               ("No signs: the same order as narrow stretches.", "Sin señales: el mismo orden que en los estrechamientos."),
               ("Square blue = yours; round red = theirs.", "Cuadrada azul = tuya; redonda roja = suya.")],
        trap=("Thinking the vehicle at the R-6 end reverses.", "Pensar que retrocede el que entró por el extremo de la R-6.")),
    "emergency": dict(sec=4, en="Priority vehicles", es="Vehículos prioritarios",
        recap=[("Police, fire, civil protection, ambulances, public or private, on urgent service.", "Policía, bomberos, protección civil, asistencia sanitaria, públicos o privados, en servicio urgente."),
               ("Light (V-1, blue) and siren together; light alone if no danger.", "Luz (V-1, azul) y sirena a la vez; solo luz si no hay peligro."),
               ("May exceed limits and skip rules on their own responsibility; agents’ orders always apply.", "Pueden superar límites y no cumplir normas bajo su responsabilidad; las órdenes de los agentes, siempre."),
               ("Non-priority vehicle in an emergency: horn + hazard lights or handkerchief, no priority.", "No prioritario en urgencia: claxon + luz de emergencia o pañuelo, sin prioridad.")],
        trap=("Thinking a priority vehicle may ignore an agent’s orders.", "Pensar que un prioritario puede saltarse las órdenes de un agente.")),
    "others": dict(sec=4, en="What everyone else does", es="Comportamiento de los demás",
        recap=[("Make way: normally move to the right, or stop.", "Facilitar el paso: apartarse a la derecha o detenerse."),
               ("Emergency corridor at walking pace or stopped, on autopistas and autovías.", "Carril de emergencia a paso de peatón o detenidos, en autopistas y autovías."),
               ("Two lanes: centre. Three or more: between the left lane and the next.", "Dos carriles: centro. Tres o más: entre el izquierdo y su contiguo."),
               ("Police red light flashing forward: stop on the right, in front of the police.", "Luz roja policial hacia delante: detenerse a la derecha, delante de la policía.")],
        trap=("Opening the corridor between the two right-hand lanes of a three-lane road.", "Abrir el carril entre los dos carriles de la derecha en una vía de tres.")),
}

# ---------------------------------------------------------------- signed junctions
Q("sg1", "signed", "You reach a give-way sign. You must give way to vehicles on the priority road coming…", "Llegas a un ceda el paso. Debes ceder el paso a los vehículos de la vía preferente que vengan…",
  [("from either side", "por cualquier lado"), ("only from the right", "solo por la derecha"), ("only from the left", "solo por la izquierda")],
  "Whichever side they come from.", "Cualquiera que sea el lado por el que se aproximen.")
Q("sg2", "signed", "At a STOP sign you must…", "En una señal de stop debes…",
  [("always stop, even if nobody is coming", "detenerte siempre, aunque no venga nadie"), ("stop only if someone is coming", "detenerte solo si viene alguien"), ("slow down without stopping", "reducir sin detenerte")],
  "And then give way.", "Y después ceder el paso.")
Q("sg3", "signed", "A STOP sign without a stop line: where do you stop?", "Un stop sin línea de detención: ¿dónde te detienes?",
  [("Immediately before the junction", "Inmediatamente antes de la intersección"), ("At the sign", "Junto a la señal"), ("Inside the junction, to see better", "Dentro de la intersección, para ver mejor")],
  "If you still can’t see, stop again where you can.", "Si aun así no ves, detente de nuevo donde veas.")
Q("sg4", "signed", "An agent signals you to go, but your traffic light is red. You…", "Un agente te indica que pases, pero tu semáforo está en rojo. Tú…",
  [("obey the agent", "obedeces al agente"), ("wait for green", "esperas al verde"), ("give way to the right", "cedes a la derecha")],
  "Agents come first in the order of precedence.", "Los agentes van primero en el orden de prioridad.")
Q("sg5", "signed", "A temporary sign contradicts a permanent one. Which do you follow?", "Una señal circunstancial contradice a una permanente. ¿Cuál sigues?",
  [("The temporary sign", "La circunstancial"), ("The permanent sign", "La permanente"), ("The road markings", "Las marcas viales")],
  "Agents → temporary → lights → vertical signs → markings.", "Agentes → circunstancial → semáforos → verticales → marcas viales.")
Q("sg6", "signed", "A traffic light that is not working (off) and a give-way sign at the same junction. You…", "Un semáforo apagado y una señal de ceda el paso en la misma intersección. Tú…",
  [("follow the give-way sign", "sigues el ceda el paso"), ("give way to the right", "cedes a la derecha"), ("have priority", "tienes prioridad")],
  "The vertical sign regulates the junction.", "La señal vertical regula la intersección.")
Q("sg7", "signed", "Which of these gives you priority at the next junction?", "¿Cuál de estas señales te da prioridad en la próxima intersección?",
  [("A triangular P-1 sign with a thick line for your road", "Una señal triangular P-1 con trazo grueso para tu vía"), ("An inverted triangle", "Un triángulo invertido"), ("An octagon", "Un octógono")],
  "The inverted triangle is give way; the octagon, STOP.", "El triángulo invertido es ceda el paso; el octógono, stop.")
Q("sg8", "signed", "A flashing amber light at a junction means…", "Un ámbar intermitente en una intersección significa…",
  [("take extra care and follow the priority rules or signs", "extremar la precaución y respetar las normas o señales de prioridad"), ("you have priority", "tienes prioridad"), ("you must stop", "debes detenerte")],
  "It gives you no priority.", "No da prioridad.")

# ---------------------------------------------------------------- unsigned junctions
Q("un1", "unsigned", "At a junction without signs, as a rule you give way to vehicles coming…", "En una intersección sin señalizar, como norma cedes el paso a los que vienen…",
  [("from your right", "por tu derecha"), ("from your left", "por tu izquierda"), ("from both sides", "por ambos lados")],
  "With four exceptions.", "Con cuatro excepciones.")
Q("un2", "unsigned", "You ride on a paved road. A car comes from your right along a dirt track. Who goes first?", "Circulas por una vía pavimentada. Un turismo viene por tu derecha por un camino de tierra. ¿Quién pasa primero?",
  [("You", "Tú"), ("The car, because it comes from the right", "El turismo, porque viene por la derecha"), ("Whoever arrives first", "El que llegue antes")],
  "Paved beats unpaved.", "La pavimentada pasa antes que la que no lo está.")
Q("un3", "unsigned", "A tram approaches an unsigned junction from your left. Who goes first?", "Un tranvía se acerca por tu izquierda a una intersección sin señalizar. ¿Quién pasa primero?",
  [("The tram", "El tranvía"), ("You, because it comes from the left", "Tú, porque viene por la izquierda"), ("Whoever is faster", "El más rápido")],
  "Vehicles on rails go first.", "Los vehículos sobre raíles pasan primero.")
Q("un4", "unsigned", "You are inside a roundabout without signs. A car wants to enter from your right. Who goes first?", "Estás dentro de una glorieta sin señales. Un turismo quiere entrar por tu derecha. ¿Quién pasa primero?",
  [("You", "Tú"), ("The car", "El turismo"), ("The bigger vehicle", "El vehículo más grande")],
  "Those inside go before those entering.", "Los que están dentro pasan antes que los que acceden.")
Q("un5", "unsigned", "You want to join an autovía from a slip road without signs. Who has priority?", "Quieres incorporarte a una autovía desde un acceso sin señales. ¿Quién tiene prioridad?",
  [("Vehicles already on the autovía", "Los que ya circulan por la autovía"), ("You, coming from the right", "Tú, que vienes por la derecha"), ("Whoever goes faster", "El que vaya más rápido")],
  "Even if you come from their right.", "Aunque vengas por su derecha.")
Q("un6", "unsigned", "Sign P-2 “junction with priority to the right”…", "La señal P-2 «intersección con prioridad de la derecha»…",
  [("only reminds you of the general rules", "solo recuerda las normas generales"), ("gives you priority", "te da prioridad"), ("obliges you to stop", "obliga a detenerse")],
  "It changes nothing.", "No cambia nada.")
Q("un7", "unsigned", "Three vehicles reach an unsigned crossroads at the same time, from three different roads. How do they go?", "Tres vehículos llegan a la vez a un cruce sin señales, por tres vías distintas. ¿Cómo pasan?",
  [("Each gives way to the one on its right", "Cada uno cede al que tiene a su derecha"), ("The biggest first", "El más grande primero"), ("The motorcycle first", "La moto primero")],
  "The one with no vehicle on its right goes first.", "Pasa primero el que no tiene a nadie a su derecha.")

# ---------------------------------------------------------------- how to act
Q("cd1", "conduct", "If you must give way, you must not…", "Si debes ceder el paso, no debes…",
  [("force the other rider or driver to change path or speed abruptly", "obligar al otro a modificar bruscamente su trayectoria o velocidad"), ("slow down", "reducir la velocidad"), ("look both ways", "mirar a ambos lados")],
  "Not even when continuing or resuming the manoeuvre.", "Ni al continuar o reemprender la maniobra.")
Q("cd2", "conduct", "You have priority, but traffic ahead is stopped and you would stay inside the junction. You…", "Tienes prioridad, pero el tráfico de delante está parado y quedarías dentro de la intersección. Tú…",
  [("don’t enter the junction", "no entras en la intersección"), ("enter: you have priority", "entras: tienes prioridad"), ("enter and use the horn", "entras y tocas el claxon")],
  "Don’t block the cross traffic.", "No obstruyas la circulación transversal.")
Q("cd3", "conduct", "You are stuck inside a junction with traffic lights and you block the cross traffic. You…", "Te has quedado detenido dentro de una intersección con semáforo y obstruyes el tráfico transversal. Tú…",
  [("leave without waiting for your light to turn green", "sales sin esperar a que tu semáforo se ponga en verde"), ("wait for green", "esperas al verde"), ("reverse", "das marcha atrás")],
  "Without hindering those moving with green.", "Sin entorpecer a los que avanzan en el sentido permitido.")
Q("cd4", "conduct", "How do you show early that you are going to give way?", "¿Cómo demuestras con antelación que vas a ceder el paso?",
  [("By slowing down gradually", "Reduciendo la velocidad paulatinamente"), ("By flashing your headlight", "Con ráfagas de luz"), ("By sounding the horn", "Tocando el claxon")],
  "Your way of riding shows it.", "Lo muestra tu forma de circular.")
Q("cd5", "conduct", "Having priority, may you enter a pedestrian crossing where you will probably have to stop on it?", "Teniendo prioridad, ¿puedes entrar en un paso de peatones donde probablemente quedarás detenido?",
  [("No", "No"), ("Yes, if no pedestrians are crossing", "Sí, si no cruzan peatones"), ("Yes, on a motorcycle", "Sí, en moto")],
  "Nor in a cycle crossing.", "Tampoco en un paso para ciclistas.")
Q("cd6", "conduct", "A yellow criss-cross grid painted on a junction means…", "Una cuadrícula amarilla pintada en una intersección significa…",
  [("don’t enter if you might have to stop inside", "no entrar si puedes quedar detenido dentro"), ("parking for motorcycles", "aparcamiento para motos"), ("a stop zone for buses", "zona de parada de autobuses")],
  "Keep the junction clear.", "Mantener la intersección despejada.")

# ---------------------------------------------------------------- pedestrians, cyclists, animals
Q("vu1", "vulnerable", "As a general rule, on the carriageway and the hard shoulder, priority belongs to…", "Como norma general, en la calzada y el arcén la prioridad la tienen…",
  [("drivers, except in the listed cases", "los conductores, salvo en los casos señalados"), ("pedestrians, always", "los peatones, siempre"), ("animals", "los animales")],
  "The exceptions protect pedestrians, cyclists and animals.", "Las excepciones protegen a peatones, ciclistas y animales.")
Q("vu2", "vulnerable", "You turn right into another street. A pedestrian is crossing it where there is no crossing. Who goes first?", "Giras a la derecha para entrar en otra calle. Un peatón la cruza donde no hay paso. ¿Quién pasa primero?",
  [("The pedestrian", "El peatón"), ("You, because there is no crossing", "Tú, porque no hay paso"), ("Whoever arrives first", "El que llegue antes")],
  "Even if there is no crossing.", "Aunque no exista paso para él.")
Q("vu3", "vulnerable", "You cross a hard shoulder used by pedestrians who have no pedestrian zone. You…", "Cruzas un arcén por el que circulan peatones que no disponen de zona peatonal. Tú…",
  [("let them go first", "les dejas pasar"), ("have priority", "tienes prioridad"), ("sound the horn and cross", "tocas el claxon y cruzas")],
  "Stopping if necessary.", "Llegando a detenerte si es necesario.")
Q("vu4", "vulnerable", "Passengers have just got off a bus at a signed stop and are walking to the pavement. You…", "Unos viajeros acaban de bajar de un autobús en una parada señalizada y van hacia la acera. Tú…",
  [("let them pass", "les dejas pasar"), ("have priority: they are on the carriageway", "tienes prioridad: están en la calzada"), ("pass between them slowly", "pasas entre ellos despacio")],
  "Between the bus and the nearest pedestrian zone or refuge.", "Entre el vehículo y la zona peatonal o refugio más próximo.")
Q("vu5", "vulnerable", "A group of cyclists is crossing a junction; the first has already started. You…", "Un grupo de ciclistas cruza una intersección; el primero ya ha iniciado el cruce. Tú…",
  [("let the whole group pass", "dejas pasar a todo el grupo"), ("pass after the first cyclist", "pasas tras el primer ciclista"), ("have priority over the rest", "tienes prioridad sobre los demás")],
  "The group counts as one moving unit.", "El grupo se considera una unidad móvil.")
Q("vu6", "vulnerable", "A school row is crossing the road with no pedestrian crossing. You…", "Una fila escolar cruza la vía sin paso de peatones. Tú…",
  [("let it pass", "la dejas pasar"), ("have priority", "tienes prioridad"), ("sound the horn", "tocas el claxon")],
  "Also troops on foot and organised processions.", "También tropas en formación y comitivas organizadas.")
Q("vu7", "vulnerable", "A flock of sheep is on a signed cañada. Who has priority?", "Un rebaño de ovejas está en una cañada señalizada. ¿Quién tiene prioridad?",
  [("The animals", "Los animales"), ("You", "Tú"), ("Whoever arrives first", "El que llegue antes")],
  "Out of a cañada, drivers normally go first.", "Fuera de la cañada, normalmente pasan los conductores.")
Q("vu8", "vulnerable", "You turn left into another road and a cyclist is close by going straight on. Who goes first?", "Giras a la izquierda para entrar en otra vía y hay un ciclista próximo que sigue recto. ¿Quién pasa primero?",
  [("The cyclist", "El ciclista"), ("You, on a motorcycle", "Tú, en moto"), ("Whoever goes faster", "El que vaya más rápido")],
  "When a motor vehicle or moped turns and a cyclist is close by.", "Cuando el vehículo de motor o ciclomotor gira y hay un ciclista próximo.")
Q("vu9", "vulnerable", "In a single-platform zone (road and pavement at one level), pedestrians have priority…", "En una zona de plataforma única de calzada y acera, los peatones tienen prioridad…",
  [("at any point of the carriageway", "en cualquier punto de la calzada"), ("only on marked crossings", "solo en los pasos señalizados"), ("only at night", "solo de noche")],
  "Since 1 October 2026.", "Desde el 1 de octubre de 2026.")
Q("vu10", "vulnerable", "Since October 2026, which of these is legally a vulnerable road user?", "Desde octubre de 2026, ¿cuál de estos es legalmente un usuario vulnerable?",
  [("A motorcycle passenger", "El pasajero de una moto"), ("A bus driver", "El conductor de un autobús"), ("A van driver", "El conductor de una furgoneta")],
  "Also pedestrians, cyclists, VMP riders and moped riders.", "También peatones, ciclistas, conductores de VMP y de ciclomotores.")
Q("vu11", "vulnerable", "You leave a garage across the pavement. A pedestrian is walking along it. You…", "Sales de un garaje cruzando la acera. Un peatón camina por ella. Tú…",
  [("let the pedestrian pass", "dejas pasar al peatón"), ("have priority, coming out", "tienes prioridad al salir"), ("sound the horn and go", "tocas el claxon y sales")],
  "Crossing a pedestrian zone by the passage made for it.", "Al cruzar una zona peatonal por el paso habilitado.")

# ---------------------------------------------------------------- narrow stretches
Q("nr1", "narrow", "In a narrow stretch without signs, who goes first?", "En un estrechamiento sin señalizar, ¿quién pasa primero?",
  [("The vehicle that entered first", "El vehículo que entró primero"), ("The heavier vehicle", "El más pesado"), ("The one coming uphill, always", "El que sube, siempre")],
  "The list applies only in doubt.", "La lista solo rige en caso de duda.")
Q("nr2", "narrow", "In a narrow stretch, in doubt who entered first, your motorcycle meets a car. Who goes first?", "En un estrechamiento, con duda sobre quién entró primero, tu moto se encuentra con un turismo. ¿Quién pasa primero?",
  [("The car", "El turismo"), ("Your motorcycle", "Tu moto"), ("The one going uphill", "El que suba")],
  "Motorcycles are last in the order.", "Las motos son las últimas en el orden.")
Q("nr3", "narrow", "In that order, a motorcycle with a sidecar comes…", "En ese orden, una moto con sidecar va…",
  [("9th, ahead of solo motorcycles", "9.ª, por delante de las motos sin sidecar"), ("10th, with solo motorcycles", "10.ª, con las motos sin sidecar"), ("1st", "1.ª")],
  "With three-wheeled vehicles and three-wheeled mopeds.", "Con los vehículos de tres ruedas y los ciclomotores de tres ruedas.")
Q("nr4", "narrow", "A narrow stretch, in doubt: a motorcycle and a two-wheeled moped meet. How is it decided?", "Estrechamiento, con duda: se encuentran una moto y un ciclomotor de dos ruedas. ¿Cómo se decide?",
  [("The one that would have to reverse further goes first", "Pasa el que tendría que dar marcha atrás mayor distancia"), ("The motorcycle, being bigger", "La moto, por ser mayor"), ("The moped, being slower", "El ciclomotor, por ser más lento")],
  "Same step in the list; if equal, width, length or MMA.", "Mismo puesto de la lista; si es igual, anchura, longitud o MMA.")
Q("nr5", "narrow", "Narrow stretch on a slope of 8 %. Who goes first?", "Estrechamiento en una pendiente del 8 %. ¿Quién pasa primero?",
  [("The one going uphill, unless it can reach a lay-by first", "El que sube, salvo que pueda llegar antes a un apartadero"), ("The one going downhill", "El que baja"), ("The heavier one", "El más pesado")],
  "Steep means 7 % or more.", "Gran pendiente: 7 % o más.")
Q("nr6", "narrow", "At the entrance of a narrow stretch you see a blue square sign with a white arrow up and a red arrow down. You…", "A la entrada de un estrechamiento ves una señal cuadrada azul con una flecha blanca hacia arriba y otra roja hacia abajo. Tú…",
  [("have priority over oncoming vehicles", "tienes prioridad respecto al sentido contrario"), ("must give way to oncoming vehicles", "debes ceder el paso al sentido contrario"), ("must stop", "debes detenerte")],
  "R-6: square and blue = yours.", "R-6: cuadrada y azul = tuya.")
Q("nr7", "narrow", "A round sign with a red border, a black arrow up and a red arrow down, at a narrow stretch, means…", "Una señal redonda de borde rojo, con flecha negra hacia arriba y roja hacia abajo, en un estrechamiento, significa…",
  [("give way to oncoming vehicles", "prioridad en sentido contrario: cedes"), ("you have priority", "tienes prioridad"), ("no entry", "entrada prohibida")],
  "R-5: round and red = theirs.", "R-5: redonda y roja = suya.")
Q("nr8", "narrow", "In doubt in a narrow stretch, a bus and a lorry meet. Who goes first?", "Con duda en un estrechamiento, se encuentran un autobús y un camión. ¿Quién pasa primero?",
  [("The bus", "El autobús"), ("The lorry", "El camión"), ("The one going downhill", "El que baja")],
  "Bus 5th, lorry 6th.", "Autobús 5.º, camión 6.º.")
Q("nr9", "narrow", "In doubt in a narrow stretch, a car towing a 600 kg trailer meets a bus. Who goes first?", "Con duda en un estrechamiento, un turismo con remolque de 600 kg se encuentra con un autobús. ¿Quién pasa primero?",
  [("The car with the trailer", "El turismo con remolque"), ("The bus", "El autobús"), ("The one that entered last", "El que entró el último")],
  "Cars with a trailer up to 750 kg are 4th; buses 5th.", "Turismo con remolque de hasta 750 kg: 4.º; autobús: 5.º.")
Q("nr10", "narrow", "In doubt in a narrow stretch, your motorcycle meets a bicycle. They are on the same step, so…", "Con duda en un estrechamiento, tu moto se encuentra con una bicicleta. Están en el mismo puesto, así que…",
  [("the one that would have to reverse further goes first", "pasa el que tendría que retroceder más distancia"), ("the bicycle always goes first", "la bicicleta pasa siempre"), ("the motorcycle always goes first", "la moto pasa siempre")],
  "Motorcycles, two-wheeled mopeds and bicycles share step 10.", "Motos, ciclomotores de dos ruedas y bicicletas comparten el puesto 10.")

# ---------------------------------------------------------------- bridges
Q("br1", "bridge", "Two vehicles meet on a narrow bridge. One end has a give-way sign. Who reverses?", "Dos vehículos se encuentran en un puente estrecho. En un extremo hay un ceda el paso. ¿Quién retrocede?",
  [("The one that came in by the give-way end", "El que entró por el extremo del ceda el paso"), ("The one that came in by the other end", "El que entró por el otro extremo"), ("The lighter one", "El más ligero")],
  "Also with R-5 at that end.", "También con la R-5 en ese extremo.")
Q("br2", "bridge", "A narrow bridge has no signs. Who goes first?", "Un puente estrecho no tiene señales. ¿Quién pasa primero?",
  [("As in narrow stretches: first in; in doubt, the vehicle order", "Como en los estrechamientos: el que entró primero; en duda, el orden de vehículos"), ("Always the one coming from the right", "Siempre el que viene por la derecha"), ("Always the lighter vehicle", "Siempre el más ligero")],
  "Same rules as narrow stretches.", "Las mismas normas que los estrechamientos.")
Q("br3", "bridge", "You entered a narrow bridge by the end with the R-6 sign and meet an oncoming car. Who reverses?", "Entraste en un puente estrecho por el extremo con la señal R-6 y te encuentras con un turismo. ¿Quién retrocede?",
  [("The car, which entered by the R-5 end", "El turismo, que entró por el extremo de la R-5"), ("You, being a motorcycle", "Tú, por ser moto"), ("Nobody: you squeeze past", "Nadie: os cruzáis como podáis")],
  "R-6 gives you priority.", "La R-6 te da prioridad.")

# ---------------------------------------------------------------- emergency
Q("em1", "emergency", "Which of these is a priority vehicle on urgent service?", "¿Cuál de estos es un vehículo prioritario en servicio urgente?",
  [("A private ambulance with light and siren on", "Una ambulancia privada con luz y sirena"), ("A taxi with hazard lights", "Un taxi con la luz de emergencia"), ("A tow truck parked", "Una grúa estacionada")],
  "Public or private.", "Públicos o privados.")
Q("em2", "emergency", "A vehicle is a priority vehicle when, on urgent service, it uses…", "Un vehículo es prioritario cuando, en servicio urgente, utiliza…",
  [("the light signal and the siren at the same time", "la señal luminosa y la acústica a la vez"), ("only the horn", "solo el claxon"), ("only the headlights", "solo las luces de cruce")],
  "Light alone only if leaving out the siren is no danger.", "Solo la luz si omitir la sirena no entraña peligro.")
Q("em3", "emergency", "The light signal V-1 of emergency vehicles is…", "La señal luminosa V-1 de los vehículos de urgencia es…",
  [("blue", "azul"), ("amber", "amarilla"), ("red", "roja")],
  "One or more blue lights.", "Una o varias luces azules.")
Q("em4", "emergency", "A priority vehicle on urgent service must always obey…", "Un vehículo prioritario en servicio urgente debe obedecer siempre…",
  [("the agents’ orders", "las órdenes de los agentes"), ("the speed limits", "los límites de velocidad"), ("traffic lights", "los semáforos")],
  "The rest, on its own responsibility.", "El resto, bajo su exclusiva responsabilidad.")
Q("em5", "emergency", "May a priority vehicle exceed the speed limit?", "¿Puede un vehículo prioritario superar el límite de velocidad?",
  [("Yes, on urgent service and signalling it, on its own responsibility", "Sí, en servicio urgente y señalizándolo, bajo su responsabilidad"), ("No, never", "No, nunca"), ("Only on autopistas", "Solo en autopistas")],
  "Without endangering anyone.", "Sin poner en peligro a nadie.")
Q("em6", "emergency", "Before crossing a red light, a priority vehicle must…", "Antes de pasar un semáforo en rojo, un vehículo prioritario debe…",
  [("make sure there is no risk and others have stopped or are making way", "cerciorarse de que no hay riesgo y de que los demás se han detenido o le facilitan el paso"), ("just sound the siren", "solo hacer sonar la sirena"), ("stop completely", "detenerse por completo")],
  "Extreme precautions.", "Con extremadas precauciones.")
Q("em7", "emergency", "A driver without a priority vehicle must rush someone to hospital. They…", "Un conductor sin vehículo prioritario debe llevar urgentemente a alguien al hospital. Él…",
  [("use the horn on and off and hazard lights, and obey every rule", "usa el claxon intermitente y la luz de emergencia, y respeta todas las normas"), ("may exceed the limits", "puede superar los límites"), ("have priority at junctions", "tiene prioridad en las intersecciones")],
  "Or waves a handkerchief. No priority.", "O agita un pañuelo. Sin prioridad.")
Q("em8", "emergency", "Besides emergency services, who else may have priority under your course?", "Además de los servicios de urgencia, ¿quién más puede tener prioridad según tu curso?",
  [("Road maintenance crews and roadside assistance vehicles", "Los equipos de mantenimiento de la vía y los vehículos de auxilio en carretera"), ("Taxis", "Los taxis"), ("School buses", "Los autobuses escolares")],
  "When on service.", "Cuando prestan servicio.")

# ---------------------------------------------------------------- others
Q("ot1", "others", "You hear the siren of an ambulance behind you. You…", "Oyes la sirena de una ambulancia detrás de ti. Tú…",
  [("move to your right, or stop if necessary", "te apartas a tu derecha o te detienes si es preciso"), ("speed up to get out of its way", "aceleras para apartarte"), ("brake sharply where you are", "frenas bruscamente donde estás")],
  "Facilitate its way.", "Facilítale el paso.")
Q("ot2", "others", "On an autovía with two lanes, traffic stops. Where is the emergency corridor formed?", "En una autovía de dos carriles, el tráfico se detiene. ¿Dónde se forma el carril de emergencia?",
  [("In the centre, between the two lanes", "En el centro, entre los dos carriles"), ("On the right-hand shoulder", "En el arcén derecho"), ("On the left-hand shoulder", "En el arcén izquierdo")],
  "Left lane moves left, right lane moves right.", "El carril izquierdo se orilla a la izquierda y el derecho a la derecha.")
Q("ot3", "others", "On an autopista with three lanes in your direction, the emergency corridor is formed…", "En una autopista con tres carriles en tu sentido, el carril de emergencia se forma…",
  [("between the leftmost lane and the next one", "entre el carril de más a la izquierda y su contiguo"), ("between the two right-hand lanes", "entre los dos carriles de la derecha"), ("on the hard shoulder", "en el arcén")],
  "The left lane moves left; the rest move right.", "El izquierdo se orilla a la izquierda; el resto, a la derecha.")
Q("ot4", "others", "When must the emergency corridor be formed?", "¿Cuándo hay que formar el carril de emergencia?",
  [("When the queue moves at walking pace or stops", "Cuando la retención avanza a paso de peatón o se detiene"), ("Only when you see an ambulance", "Solo cuando ves una ambulancia"), ("At any speed under 60 km/h", "A cualquier velocidad inferior a 60 km/h")],
  "On autopistas and autovías.", "En autopistas y autovías.")
Q("ot5", "others", "A police car with blue lights and siren is behind you and switches on a red light flashing forward. You must…", "Un coche de policía con luz azul y sirena va detrás de ti y activa una luz roja intermitente hacia delante. Debes…",
  [("stop on the right, in front of the police vehicle", "detenerte a la derecha, delante del vehículo policial"), ("move aside and let it pass", "apartarte y dejarle pasar"), ("accelerate to the next exit", "acelerar hasta la próxima salida")],
  "It is an order to stop (since July 2025).", "Es una orden de detención (desde julio de 2025).")
Q("ot6", "others", "Once stopped after that police signal, you…", "Una vez detenido tras esa señal de la policía, tú…",
  [("stay where you are and follow the agent’s instructions", "permaneces en tu sitio y sigues las instrucciones del agente"), ("walk to the police car", "vas andando al coche policial"), ("continue if they don’t come within a minute", "continúas si no vienen en un minuto")],
  "Given by loudspeaker or other clear means.", "Por megafonía u otro medio claro.")
Q("ot7", "others", "In a stopped queue on an autovía, may you ride your motorcycle along the emergency corridor?", "En una retención detenida en autovía, ¿puedes circular con tu moto por el carril de emergencia?",
  [("No: it is kept free for priority vehicles", "No: se deja libre para los vehículos prioritarios"), ("Yes, at up to 30 km/h", "Sí, a 30 km/h como máximo"), ("Yes, if it is wide enough", "Sí, si es lo bastante ancho")],
  "The only extra space for motorcycles in a jam is the signed right-hand shoulder.", "El único espacio adicional para motos en un atasco es el arcén derecho señalizado.")
