# DGT Study Desk

Study notes and tests for the Spanish DGT theory exam, for category B (cars) and A1/A2 (motorcycles).

The main screen lets you choose a category, then one of its 13 topics. Category B is complete, with all 13 topics written: Topic 1, definitions and general concepts; Topic 2, use of the road; Topic 3, speed; Topic 4, priority; Topic 5, manoeuvres; Topic 6, carrying people and goods; Topic 7, lights; Topic 8, signs and signals; Topic 9, documentation; Topic 10, accidents and their factors; Topic 11, first aid; Topic 12, driving techniques; and Topic 13, vehicle maintenance and accessories. Category A1/A2 is complete too, with all 13 topics written: Topic 1, definitions and general concepts; Topic 2, use of the road; Topic 3, speed; Topic 4, priority; Topic 5, manoeuvres; Topic 6, carrying people and goods; Topic 7, lights; Topic 8, signs and signals; Topic 9, documentation; Topic 10, accidents and their factors; Topic 11, first aid; Topic 12, riding techniques; and Topic 13, maintenance and accessories. A topic that is listed in the catalogue but not yet written shows as "Coming soon".

- English, Spanish and Ukrainian, chosen from a language menu at the top of every page
- Light and dark theme
- Questions per topic (58 in Topic 1, 92 in Topic 2, 88 in Topic 3, 91 in Topic 4, 137 in Topic 5, 95 in Topic 6, 77 in Topic 7, 196 in Topic 8, 116 in Topic 9, 259 in Topic 10, 107 in Topic 11, 99 in Topic 12, 77 in Topic 13; 60 in A1/A2 Topic 1, 89 in A1/A2 Topic 2, 70 in A1/A2 Topic 3, 60 in A1/A2 Topic 4, 93 in A1/A2 Topic 5, 60 in A1/A2 Topic 6, 62 in A1/A2 Topic 7, 120 in A1/A2 Topic 8, 88 in A1/A2 Topic 9, 89 in A1/A2 Topic 10, 79 in A1/A2 Topic 11, 81 in A1/A2 Topic 12, 63 in A1/A2 Topic 13): exam simulation (30 questions, pass with 3 mistakes or fewer), all questions by section, and practice of your own mistakes
- Printable PDFs of each topic in English, Spanish and Ukrainian, with a self-test
- Progress, mistakes, error analysis and a generated study task

## Open it

Open `dgt-study-desk.code-workspace` in VS Code (File > Open Workspace from File). It carries the settings, tasks, debug configuration and extension recommendations.

## Run it

1. **Terminal** (recommended): `npm start`, then open http://localhost:5173. Needs Node.js, no packages.
2. **Run and Debug (F5):** "Open in Chrome" starts the same server and opens the main screen with the debugger attached.

Both save your progress to a file in the project folder (see below). **Live Server** and opening `index.html` directly from disk also work, but then progress is kept in that browser only.

## Pages

- `index.html`: the main screen. Choose a category, then a topic (`index.html#b` lists category B, `index.html#a` lists A1/A2). Each topic shows how far you've got: questions seen, accuracy and open mistakes. **Continue** reopens the last topic you studied. Export and Import are at the bottom.
- `topics/b-01.html` to `topics/b-13.html`: Topics 1 to 13 of category B; `topics/a-01.html` to `topics/a-13.html`: Topics 1 to 13 of category A1/A2; with their study notes and tests. The arrow at the top left goes back to the topic list.

## Layout

| Path | What it is | Edit by hand? |
|---|---|---|
| `index.html` | Main screen: categories and topics | Yes |
| `topics/b-01.html` … `b-13.html`, `a-01.html` … `a-13.html` | One page per written topic, in all of its languages | No, generated |
| `server.js` | Local server: serves the pages and saves progress (`npm start`) | Yes |
| `progress/` | Your saved progress, `progress.json`. Not in git | No |
| `css/styles.css` | All styles and the light/dark colour tokens | Yes |
| `js/shared.js` | Used by every page: saving progress, export/import, language and theme | Yes |
| `js/home.js` | The main screen | Yes |
| `js/app.js` | A topic's tests, error analysis and study task | Yes |
| `js/catalog.js` | Categories and topics for the main screen | No, generated |
| `js/topics/b-01.js` … `b-13.js`, `a-01.js` … `a-13.js` | Each topic's question bank and section recaps | No, generated |
| `tools/catalog.py` | Categories, the 13 topics in each, and their titles | Yes |
| `tools/topics/__init__.py` | The list of written topics (`BUILT`) | Yes |
| `tools/topics/b01/`, `b02/` | One folder per topic: `content.py` (study text as English/Spanish pairs), `diagrams.py` (SVG figures), `bank.py` (questions; the first option is always the correct one), `__init__.py` (titles and intro), `uk.py` (the Ukrainian text, see below) | Yes |
| `tools/i18n.py` | Puts the Ukrainian text into a topic for the build; `todo` and `check` show what is left to translate | Yes |
| `tools/blocks.py`, `tools/svgkit.py` | Building blocks for the study text and the figures, shared by all topics | Yes |
| `tools/build_site.py` | Regenerates the topic pages, their data and `js/catalog.js` | |
| `tools/build_pdf.py` | Regenerates the PDFs in `pdf/` (needs Google Chrome) | |
| `pdf/` | Printable topics in English, Spanish and Ukrainian (`…_UK_v1.pdf`) | |

After changing anything in `tools/`, run `npm run build` (needs Python 3, no packages).
`npm run build:pdf` rebuilds every topic's PDFs. `python3 tools/build_pdf.py v1 a-13` rebuilds just one topic, in each of its languages.

## Ukrainian

All 26 topics, in both categories, are also in Ukrainian: study text, figures, questions, section recaps, the glossary (Spanish → Ukrainian) and the PDFs. Choose Українська from the language menu on any page; the choice is kept for every page.

- Each topic folder has a `uk.py`. `UK.meta(...)` holds the titles and intro, `Q(id, question, [correct, wrong, wrong], why)` the questions, and `TAG(tag, name, [recaps], trap)` the section recaps. Every other text is `X("key", "…")`, where the key is a short hash of the English text.
- An A1/A2 topic builds on the B topic with the same number, so its `uk.py` uses that B file as a base (`UK.use(B08)`) and holds only its own questions, recaps and the texts that differ. A text the two pages share is translated once, in the B file, and a correction there reaches both pages.
- Figures are the English drawing with each label swapped. Where a label must read differently in one figure, use `X("figure_name:English label", "…")`.
- Text that is the same in English and Spanish (numbers, sign codes, MIN/MAX) needs no entry. It gets Ukrainian units and number format only (km/h → км/год, 1.5 → 1,5, 3,500 → 3 500), and drawings are never touched.
- `python3 tools/i18n.py todo b-05` lists what is left to translate in a topic, with the Spanish shown next to each figure's labels. `python3 tools/i18n.py check` reports missing, unused and unknown entries for every translated topic.
- When you change an English text, its key changes. Until the new text is translated, the page and the PDF show it in English and the build prints a warning. `check` then lists the old entry as unused.
- Spanish exam terms stay in Spanish and in *italics*, as in the English text.
- A new topic without a `uk.py` offers only English and Spanish in its language menu. If Українська was chosen, the page shows in English with a note saying it is not translated yet (`NOT_HERE` in `js/shared.js`), and the main screen marks its category as English and Spanish only. To translate it, add a `uk.py` to its folder and the Ukrainian title to `tools/catalog.py`, then run the build.

## Where progress is stored

Progress is kept per topic. With `npm start` (or F5), every answer is saved to `progress/progress.json` in the project folder, which holds all topics plus your language and theme. Stop the server, come back weeks later, run `npm start` again and your progress is still there, in any browser. The indicator at the top of each page shows a green dot and "Progress saved in the project folder".

The browser also keeps a copy in `localStorage` (one key per topic, such as `dgt-progress-b-01`, and `dgt-prefs` for language and theme). When a page loads, each topic keeps whichever copy changed last. With Live Server or `file://` only the browser copy exists. It belongs to that one browser and that one address, because `localhost:5173`, `127.0.0.1:5173` and `file://` each have their own storage.

Progress saved before topics existed is converted automatically. That covers the old `dgt-topic1-v1` browser key and the old one-topic `progress.json`. Both become Topic 1 of category B.

`progress/` is git-ignored, so your progress never ends up in a commit.

### Moving progress to another computer

At the bottom of the main screen, under **Back up or move your progress**:

1. On this computer, click **Export progress**. A file named like `dgt-progress-2026-11-11.json` is downloaded. It holds every topic.
2. Copy the file to the other computer (USB stick, cloud drive, email to yourself).
3. There, run the project, open the main screen, click **Import progress** and pick the file.

Importing merges the file with whatever is already there, topic by topic. Files exported before topics existed still import, into Topic 1 of category B. Nothing is thrown away. For each question the most recently answered record is kept, and the test histories are combined. You can move back and forth between computers this way. Language and theme stay as each computer has them.

`progress/progress.json` has the same format as an exported file, so you can import that file with the button too. Copying it straight into another project's `progress/` folder only works on a computer that has never run the project. Otherwise that browser's own newer copy wins, so use **Import**, which merges.

### Inside a Claude artifact

`js/shared.js` and `js/app.js` also look for `window.claude`. That object exists only when the pages run as a Claude artifact, where progress is saved to the account and a button asks Claude for new questions. Locally it is absent and those two features switch themselves off.

## Adding topics

- **Name a topic** before it's written: add its title to `titles` for that category in `tools/catalog.py`, then run `npm run build`.
- **Write a topic:** both categories are complete, so a new topic means a new entry in `tools/catalog.py` (a new category or topic number). Copy a topic folder, for example `tools/topics/a07/`, to a new folder and replace its content, figures, questions and titles. Then add it to `BUILT` in `tools/topics/__init__.py` (topic id → folder, as in `"a-07": "a07"`), give it a title in `tools/catalog.py`, and run `npm run build`. Its page is built to `topics/<topic id>.html`, the main screen links to it automatically, and its progress is saved under the same id. Question ids must be unique within the topic and must not start with `ai`. The build checks this.

## Content

The text is original, written from Spanish traffic law (sources are listed at the end of each page) and checked in November 2026. Topic 2 follows the section order of the course's Topic 2 (*Uso de las vías*). Its wording and diagrams are original, and it includes the Reglamento General de Circulación reform in force since 1 October 2026: motorcycles on the hard shoulder in traffic jams, the emergency corridor, and snow on motorways. Topic 3 follows the course's Topic 3 (*La velocidad*) the same way and adds the new rule for overtaking cyclists out of town (at least 20 km/h below the limit); it notes that the travesía limit can only be lowered since 2021 and that the extra 20 km/h for overtaking ended in March 2022. Topic 4 follows the course's Topic 4 (*La prioridad*) and adds the reform's new pedestrian priority on single-level shared streets, the definition of vulnerable road users, and the police order to stop with a forward red light (July 2025). Topic 5 follows the course's Topic 5 (*Las maniobras*), including the 2026 overtaking rules and the connected V-16 warning light. Topic 6 follows the course's Topic 6 (*Transporte de personas y mercancías*), including the seat-belt exemptions removed in October 2026. Topic 7 follows the course's Topic 7 (*Las luces*). Topic 8 follows the course's Topic 8 (*Las señales*), using the official sign catalogue in force since 1 July 2025 (RD 465/2025). Its sign drawings are simplified versions made for this site and live in `tools/topics/b08/signs.py`. Topic 9 follows the course's Topic 9 (*Documentación*) and adds the compulsory insurance for e-scooters (VMP) in force since January 2026; it gives the legal 7-day deadline for the accident report form where the course says 15 days. Topic 10 follows the course's Topic 10 (*Los accidentes y sus factores*) and states the October 2026 rules for e-scooters, cyclists and motorcyclists from the decree itself (RD 518/2026); its list of driver-assistance systems allowed in the driving test follows the DGT instruction COND 2024/12. Topic 11 follows the course's Topic 11 (*Primeros auxilios*) and adds the Penal Code penalties for failing to help and for leaving the scene; where the course's CPR and bleeding advice is older than the current European Resuscitation Council guidelines, the page keeps the course's answer for the exam and shows the current guidance next to it. Topic 12 follows the course's Topic 12 (*Técnicas de conducción*); it notes that displaying the environmental label is voluntary (DGT), that the labels did not change in 2026, and corrects the course on carbon monoxide (colourless, not black smoke). Topic 13 follows the course's Topic 13 (*Mantenimiento del vehículo y accesorios*); its compulsory-equipment list is checked against annex XII of the Reglamento General de Vehículos, including the vest that motorcycles must carry since 1 October 2026. A1/A2 Topic 1 follows that course's Topic 1 (*Definiciones y conceptos generales*); it shares three figures with B Topic 1 and notes where the course still gives the old quadricycle limits. A1/A2 Topic 2 follows that course's Topic 2 (*Uso de las vías*) from a rider's point of view: helmet intercoms, motorcycles in VAO lanes, and the hard-shoulder rule for motorcycles in jams (RD 518/2026). It notes that since January 2026 a single-occupant car, zero-emission ones included, may use a VAO lane only when the panels allow it, where the course says zero-emission cars always may. A1/A2 Topic 3 follows that course's Topic 3 (*La velocidad*) with the limits for motorcycles, three-wheeled vehicles, quadricycles and mopeds; it adds that three-wheelers treated as motorcycles take the motorcycle limits, and notes that since October 2026 the −10 % trailer rule no longer covers bicycles. A1/A2 Topic 4 follows that course's Topic 4 (*La prioridad*); it shows where motorcycles sit in the narrow-stretch order and adds the police order to stop, single-platform priority and the definition of vulnerable road users, which now includes motorcyclists. A1/A2 Topic 5 follows that course's Topic 5 (*Las maniobras*) with arm signals for riders and the overtaking rules that concern two-wheelers; it notes that since October 2026 there is no longer any exception for overtaking at level crossings or pedestrian crossings, and adds the high-visibility vest that motorcycles must carry. A1/A2 Topic 6 follows that course's Topic 6 (*Transporte de personas y mercancías*); it adds the gloves and closed shoes required since October 2026, shows how far a load may stick out on a motorcycle, and lists the vehicle signs in that course. A1/A2 Topic 7 follows that course's Topic 7 (*Las luces*) with a front-and-rear map of a motorcycle's compulsory and optional lights and how a passenger or load raises the headlight beam. A1/A2 Topic 8 follows that course's Topic 8 (*Las señales*). A sign means the same whatever you ride, so its page takes the sign catalogue from Category B Topic 8 (`tools/topics/a08/content.py` builds on `b08`, so a correction to a sign there reaches both pages) and adds what singles out motorcycles and mopeds: which no-entry signs stop each of them, the advanced stop box and the motorcyclist guidance marks, each with its own figure, and a rider's summary table. Its 120 questions are written from the rider's seat. A1/A2 Topic 9 follows that course's Topic 9 (*Documentación*): it writes the rider's parts itself (the A1, A2 and A licences with a figure of the steps between them and a worked check of which motorcycles fit the A2, the novice plate on a motorcycle, the ITV calendar of motorcycles and mopeds, and what the compulsory insurance pays for a passenger) and takes the rules that are the same for every driver (renewal, duplicates, ITV results, the points and speeding tables, liability) from `b09`. It includes the October 2026 reform: gloves and closed shoes for riders, and a compulsory habitual driver when the owner has no licence. A1/A2 Topic 10 follows that course's Topic 10 (*Los accidentes y sus factores*), written for riders, with its own figures for stopping distance on a motorcycle, guardrail posts and a fallen rider, helmet types, and crossing a low-grip patch upright; the alcohol and drug rules and the testing procedure come from `b10`. A1/A2 Topic 11 follows that course's Topic 11 (*Primeros auxilios*); first aid is the same for every road user, so its page takes the text of B Topic 11 and replaces only what differs on a motorcycle: protecting the scene (the vest every motorcycle must carry since October 2026, the V-16 that is optional), the PAS figure, and a section with a figure on the injured rider's helmet. A1/A2 Topic 12 follows that course's Topic 12 (*Técnicas de conducción*) and is written for this topic only, with figures for mirrors and blind spots on a motorcycle, the line through a bend, emergency braking, group riding and where to carry luggage; the controls figure comes from `b10`. A1/A2 Topic 13 follows that course's Topic 13 (*Mantenimiento del vehículo y accesorios*), written for motorcycles, with figures for the motorcycle's systems, two-stroke and four-stroke engines, checking the oil and looking after the chain; it corrects two slips in the course (two- and four-stroke lubrication swapped in its introduction, and a chain slack of "2–3 mm" where owner's manuals give about 20–30 mm) and adds the vest every motorcycle must carry since October 2026. Check dgt.es before the exam in case a rule has changed.
