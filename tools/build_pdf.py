# -*- coding: utf-8 -*-
"""Build the topic PDFs (English and Spanish) into ../pdf.

Usage: python3 tools/build_pdf.py [version-tag] [topic-id ...]     e.g. python3 tools/build_pdf.py v1 b-02
Without topic ids it builds every written topic (topics.BUILT).
Needs Google Chrome. Set CHROME to its path if it is not found automatically."""
import html
import os
import shutil
import subprocess
import sys
from pathlib import Path

import topics

VER = sys.argv[1] if len(sys.argv) > 1 else "v1"
OUT = Path(__file__).resolve().parent.parent / "pdf"
CHROME = (os.environ.get("CHROME") or shutil.which("google-chrome") or shutil.which("chromium")
          or "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

# Labels shared by every topic. Titles, intro text and footers come from each topic's META.
UI = {
    "en": dict(
        quiz="Self-test",
        answers="Answer key",
        glossary="Spanish – English glossary",
        gl_es="Spanish (exam term)",
        gl_en="English",
        sources="Sources",
        sources_note="Wording is the author’s own; the thresholds come from the texts below. Check dgt.es before the exam in case a rule has changed.",
        lawdate="Law checked: November 2026",
        qn="Question",
    ),
    "es": dict(
        quiz="Autoevaluación",
        answers="Soluciones",
        glossary="Glosario español – inglés",
        gl_es="Español (término del examen)",
        gl_en="Inglés",
        sources="Fuentes",
        sources_note="La redacción es propia; las cifras proceden de los textos siguientes. Conviene consultar dgt.es antes del examen por si cambia alguna norma.",
        lawdate="Normativa revisada: noviembre de 2026",
        qn="Pregunta",
    ),
}


def last_section(blks):
    """Number of the last numbered section; the quiz, glossary and sources follow it."""
    return max(int(b[1]) for b in blks if b[0] == "h2" and str(b[1]).isdigit())


CSS = """
@page { size: A4; margin: 15mm 13mm 17mm 13mm;
  @bottom-left { content: "%(footer)s"; font-family: Inter, 'DejaVu Sans', sans-serif; font-size: 7.5pt; color: #64748b; }
  @bottom-right { content: counter(page) " / " counter(pages); font-family: Inter, 'DejaVu Sans', sans-serif; font-size: 7.5pt; color: #64748b; } }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: Inter, 'DejaVu Sans', Arial, sans-serif; font-size: 9.3pt; line-height: 1.4; color: #0f172a; margin: 0; }
.band { background: #12355b; color: #fff; padding: 16px 20px 14px; border-radius: 10px; margin-bottom: 10px; }
.band .eyebrow { font-size: 8.2pt; letter-spacing: .09em; text-transform: uppercase; color: #93c5fd; font-weight: 600; }
.band h1 { font-size: 20pt; line-height: 1.15; margin: 4px 0 6px; font-weight: 800; }
.band p { margin: 0; font-size: 9pt; color: #dbeafe; }
.band .stamp { margin-top: 7px; font-size: 7.8pt; color: #93c5fd; }
h2 { font-size: 13.5pt; margin: 16px 0 6px; color: #12355b; border-bottom: 2px solid #12355b; padding-bottom: 3px; break-after: avoid; display: flex; align-items: center; gap: 8px; }
h2 .n { background: #12355b; color: #fff; border-radius: 6px; font-size: 10.5pt; padding: 0 7px; line-height: 1.5; }
h3 { font-size: 10.5pt; margin: 10px 0 4px; color: #0f766e; break-after: avoid; }
p { margin: 4px 0 6px; }
i { color: #334155; }
.entry { border-left: 3px solid #0f766e; background: #f8fafc; padding: 5px 10px 6px; margin: 6px 0; border-radius: 0 6px 6px 0; break-inside: avoid; }
.entry .name { font-weight: 700; color: #12355b; font-size: 9.8pt; margin-bottom: 1px; }
.entry .body { margin: 0; }
.pills { margin-top: 3px; }
.pill { display: inline-block; background: #e0f2fe; color: #075985; border-radius: 9px; padding: 0 7px; font-size: 8.2pt; font-weight: 600; margin: 2px 4px 0 0; }
.tip { margin-top: 4px; background: #ecfdf5; border-left: 3px solid #059669; padding: 3px 8px; font-size: 8.8pt; border-radius: 0 5px 5px 0; }
.tip b.lab { color: #047857; }
figure { margin: 8px 0; break-inside: avoid; border: 1px solid #e2e8f0; border-radius: 8px; padding: 8px 10px 4px; background: #fff; }
figcaption { font-size: 8.3pt; color: #475569; margin: 2px 0 4px; }
table { width: 100%; border-collapse: collapse; margin: 6px 0 10px; font-size: 9pt; break-inside: auto; }
th { background: #12355b; color: #fff; text-align: left; padding: 4px 7px; font-size: 8.6pt; }
td { padding: 4px 7px; border-bottom: 1px solid #e2e8f0; vertical-align: top; }
tr { break-inside: avoid; }
tr:nth-child(even) td { background: #f8fafc; }
table.small { font-size: 8.5pt; }
table.small td { padding: 2.5px 7px; }
.box { border-radius: 8px; padding: 6px 12px 6px; margin: 8px 0; break-inside: avoid; }
.box.key { background: #eff6ff; border: 1px solid #bfdbfe; }
.box.trap { background: #fef2f2; border: 1px solid #fecaca; }
.box .bt { font-weight: 800; font-size: 9.6pt; margin-bottom: 2px; }
.box.key .bt { color: #1d4ed8; }
.box.trap .bt { color: #b42318; }
.box ul { margin: 2px 0 2px 16px; padding: 0; }
.box li { margin: 2px 0; }
.q { break-inside: avoid; margin: 6px 0 9px; }
.q .qt { font-weight: 700; }
.q .opt { margin-left: 14px; }
.ans { margin: 3px 0; }
.ans .ok { color: #047857; font-weight: 700; }
.src li { margin: 2px 0; font-size: 8.6pt; word-break: break-all; }
.note { font-size: 8.4pt; color: #475569; }
.pb { break-before: page; }
h2 + p { break-after: avoid; }
table.keep { break-inside: avoid; }
.quiz .q { margin: 3px 0 5px; line-height: 1.3; font-size: 8.8pt; }
.quiz h2 { margin-top: 0; }
"""


def pick(x, lang):
    return x[lang] if isinstance(x, dict) else x


def render_block(b, lang):
    kind = b[0]
    if kind == "h2":
        return f'<h2><span class="n">{b[1]}</span><span>{pick(b[2], lang)}</span></h2>'
    if kind == "h3":
        return f"<h3>{pick(b[1], lang)}</h3>"
    if kind == "p":
        return f"<p>{pick(b[1], lang)}</p>"
    if kind == "entry":
        _, name, body, pills_, tip, _k = b
        out = ['<div class="entry">', f'<div class="name">{pick(name, lang)}</div>', f'<div class="body">{pick(body, lang)}</div>']
        if pills_:
            out.append('<div class="pills">' + "".join(f'<span class="pill">{pick(p, lang)}</span>' for p in pills_) + "</div>")
        if tip:
            lab = "Exam tip: " if lang == "en" else "Ojo: "
            txt = tip[0] if lang == "en" else tip[1]
            out.append(f'<div class="tip"><b class="lab">{lab}</b>{txt}</div>')
        out.append("</div>")
        return "".join(out)
    if kind == "fig":
        _, fn, cap = b
        return f"<figure>{fn(lang)}<figcaption>{pick(cap, lang)}</figcaption></figure>"
    if kind == "table":
        _, head, rows, widths, cls = b
        cg = ""
        if widths:
            cg = "<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>"
        th = "<tr>" + "".join(f"<th>{pick(h, lang)}</th>" for h in head) + "</tr>"
        tr = "".join("<tr>" + "".join(f"<td>{pick(c, lang)}</td>" for c in r) + "</tr>" for r in rows)
        if len(rows) <= 9:
            cls = (cls + " keep").strip()
        return f'<table class="{cls}">{cg}<thead>{th}</thead><tbody>{tr}</tbody></table>'
    if kind == "box":
        _, k, title, items = b
        lis = "".join(f"<li>{pick(i, lang)}</li>" for i in items)
        return f'<div class="box {k}"><div class="bt">{pick(title, lang)}</div><ul>{lis}</ul></div>'
    if kind == "pagebreak":
        return '<div class="pb"></div>'
    raise ValueError(kind)


def render_quiz(mod, lang, n):
    ui = UI[lang]
    Q = mod.quiz()
    parts = [f'<div class="quiz"><h2 class="pb"><span class="n">{n}</span><span>{ui["quiz"]}</span></h2>', f'<p class="note">{mod.META[lang]["quiz_sub"]}</p>']
    for i, (q, opts, correct, ex) in enumerate(Q, 1):
        opt_html = "".join(f'<div class="opt"><b>{"ABC"[j]})</b> {pick(o, lang)}</div>' for j, o in enumerate(opts))
        parts.append(f'<div class="q"><div class="qt">{i}. {pick(q, lang)}</div>{opt_html}</div>')
    parts.append('</div>')
    parts.append(f'<h2 class="pb"><span class="n">✓</span><span>{ui["answers"]}</span></h2>')
    for i, (q, opts, correct, ex) in enumerate(Q, 1):
        parts.append(f'<div class="ans"><b>{i}.</b> <span class="ok">{"ABC"[correct]}) {pick(opts[correct], lang)}</span> — {pick(ex, lang)}</div>')
    return "".join(parts)


def render_glossary(mod, lang, n):
    ui = UI[lang]
    rows = "".join(f"<tr><td><i>{es}</i></td><td>{en}</td></tr>" for es, en in mod.GLOSSARY)
    return (f'<h2><span class="n">{n}</span><span>{ui["glossary"]}</span></h2>'
            f'<table class="small"><colgroup><col style="width:46%"><col style="width:54%"></colgroup>'
            f'<thead><tr><th>{ui["gl_es"]}</th><th>{ui["gl_en"]}</th></tr></thead><tbody>{rows}</tbody></table>')


def render_sources(mod, lang, n):
    ui = UI[lang]
    lis = "".join(f'<li>{html.escape(t)} — <span style="color:#1d4ed8">{html.escape(u)}</span></li>' for t, u in mod.SOURCES)
    return f'<h2><span class="n">{n}</span><span>{ui["sources"]}</span></h2><p class="note">{ui["sources_note"]}</p><ul class="src">{lis}</ul>'


def build(tid, lang):
    mod = topics.load(tid)
    ui, meta = UI[lang], mod.META[lang]
    blks = mod.blocks()
    n = last_section(blks)
    body = [
        f'<div class="band"><div class="eyebrow">{meta["eyebrow"]}</div><h1>{meta["title"]}</h1><p>{meta["lead"]}</p><div class="stamp">{ui["lawdate"]} · {VER}</div></div>'
    ]
    for b in blks:
        body.append(render_block(b, lang))
    body.append(render_quiz(mod, lang, n + 1))
    body.append(render_glossary(mod, lang, n + 2))
    body.append(render_sources(mod, lang, n + 3))
    css = CSS.replace("%(footer)s", (meta["footer"] + " · " + VER).replace('"', "'"))
    doc = f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{meta["title"]}</title><style>{css}</style></head><body>{"".join(body)}</body></html>'
    OUT.mkdir(parents=True, exist_ok=True)
    hp = OUT / f"{mod.META['pdf']}_{lang.upper()}_{VER}.html"
    hp.write_text(doc, encoding="utf-8")
    pdf = OUT / f"{mod.META['pdf']}_{lang.upper()}_{VER}.pdf"
    subprocess.run(
        [CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf}", f"file://{hp}"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180,
    )
    hp.unlink()
    print("built", pdf)


if __name__ == "__main__":
    for t in (sys.argv[2:] or list(topics.BUILT)):
        for lg in ("en", "es"):
            build(t, lg)
