# -*- coding: utf-8 -*-
"""Extra languages for topic pages.

Every topic is written in English and Spanish: T(en, es) pairs in content.py, bank.py and diagrams.py. A topic can
also have a Ukrainian translation in uk.py inside its package (tools/topics/a01/uk.py). build_site.py and
build_pdf.py then give it a Ukrainian page version and a Ukrainian PDF. Topics without uk.py stay in English and
Spanish. The English is the source: each Ukrainian entry translates one English text.

uk.py contains:

    from i18n import Book
    UK = Book()
    X, TAG, Q = UK.X, UK.TAG, UK.Q
    UK.meta(title="...", eyebrow="...", lead="...", footer="...", quiz_sub="...")
    X("1a2b3c4d", "...")    one text from the page: a heading, paragraph, table cell, box item, caption,
                            figure label or glossary term. The key is the first 8 hex digits of the SHA-1 of the
                            English text (key() below), so editing the English makes its translation show as missing.
    TAG("rules", "name", ["recap 1", "recap 2", "recap 3", "recap 4"], "typical confusion")
    Q("ru1", "question", ["correct option", "wrong option", "wrong option"], "explanation")
                            one question of bank.py, by its id, options in the same order as there.

Figure labels are translated one <text> line at a time, from the English drawing. X("tree:Vehicles", "...") gives
a label its own translation in one figure only (figure function name, a colon, the English label), for when the
wording used on the page is too long for the drawing. Texts that are the same in English and Spanish (sign codes,
"45 km/h", MIN/MAX) are optional: they only get Ukrainian units (км/год, кг, см³…) unless uk.py gives a translation.

    python3 tools/i18n.py todo a-05     list the English that has no Ukrainian yet, with the key to use
    python3 tools/i18n.py check         count missing and unused Ukrainian entries in every translated topic

A missing entry does not stop the build: that text is shown in English and the build prints a warning."""
import copy
import hashlib
import html
import importlib
import re
import sys

BASE = ("en", "es")
EXTRA = ("uk",)
ORDER = BASE + EXTRA
NAMES = {"en": "English", "es": "Español", "uk": "Українська"}

SVG = re.compile(r"<svg\b.*?</svg>", re.S)
TEXT = re.compile(r"(<text\b[^>]*>)(.*?)(</text>)", re.S)
ARIA = re.compile(r'(aria-label=")([^"]*)(")')
WORD = re.compile(r"[A-Za-z]{2,}")
HOLE = "⟦svg⟧"
MARKUP = re.compile(r"(<svg\b.*?</svg>|<[^>]*>)", re.S)
# Numbers and units in texts that need no other translation ("45 km/h", "≤ 1.5 m" → "≤ 1,5 м", "3,500" → "3 500").
UNITS = {"uk": [(re.compile(r"(\d),(\d{3})(?!\d)"), "\\1\u00a0\\2"), (re.compile(r"(\d)\.(\d)"), r"\1,\2"), (re.compile(r"km/h\b"), "км/год"), (re.compile(r"\bcm³"), "см³"), (re.compile(r"(\d)\s?kg\b"), r"\1 кг"),
                (re.compile(r"(\d)\s?kW\b"), r"\1 кВт"), (re.compile(r"(\d)\s?W\b"), r"\1 Вт"), (re.compile(r"(\d)\s?mm\b"), r"\1 мм"),
                (re.compile(r"(\d)\s?cm\b"), r"\1 см"), (re.compile(r"(\d)\s?km\b"), r"\1 км"), (re.compile(r"(\d)\s?m\b"), r"\1 м"),
                (re.compile(r"(\d)\s?mg/l\b"), r"\1 мг/л"), (re.compile(r"(\d)\s?g/l\b"), r"\1 г/л"), (re.compile(r"(\d)\s?s\b"), r"\1 с"),
                (re.compile(r"(\d)\s?h\b"), r"\1 год"), (re.compile(r"(\d)\s?min\b"), r"\1 хв"), (re.compile(r"(\d)\s?l\b"), r"\1 л")]}


def key(en):
    return hashlib.sha1(en.encode("utf-8")).hexdigest()[:8]


def wordy(s):
    """True when a text needs translating: it has a Latin word once tags and drawings are taken out."""
    return bool(WORD.search(re.sub(r"<[^>]+>", " ", SVG.sub(" ", s))))


class Book:
    """The Ukrainian entries of one topic, filled in by its uk.py."""

    def __init__(self):
        self.META, self.TEXT, self.TAGS, self.BANK = {}, {}, {}, {}

    def meta(self, **kw):
        self.META.update(kw)

    def X(self, k, uk):
        if k in self.TEXT and self.TEXT[k] != uk:
            raise ValueError(f"uk.py: key {k} is given twice with different text")
        self.TEXT[k] = uk

    def TAG(self, tag, name, recap, trap):
        self.TAGS[tag] = (name, list(recap), trap)

    def Q(self, qid, q, opts, why):
        if qid in self.BANK:
            raise ValueError(f"uk.py: question {qid} is given twice")
        self.BANK[qid] = (q, list(opts), why)


def book(mod, lang):
    """The Book for this topic module and language, or None."""
    if lang not in EXTRA:
        return None
    try:
        sub = importlib.import_module(f"{mod.__name__}.{lang}")
    except ModuleNotFoundError as e:
        if e.name != f"{mod.__name__}.{lang}":
            raise
        return None
    return getattr(sub, "UK", None)


def langs(mod):
    return BASE + tuple(lg for lg in EXTRA if book(mod, lg))


# ------------------------------------------------------------------------------------------ translating
class Translator:
    def __init__(self, mod, lang):
        self.lang, self.b = lang, book(mod, lang)
        self.missing = []          # (where, english[, spanish])
        self.optional = []         # (where, english): texts left as they are because English and Spanish agree
        self.used = set()
        # The PDF self-test copies questions out of the bank, so bank texts are also looked up by their English.
        self.rev = {}
        for q in mod.BANK:
            t = self.b.BANK.get(q["id"])
            if not t:
                continue
            pairs = [(q["q"]["en"], t[0]), (q["why"]["en"], t[2])] + [(o["en"], u) for o, u in zip(q["o"], t[1])]
            for en, uk in pairs:
                self.rev.setdefault(en, uk)

    def units(self, s):
        """Ukrainian numbers and units in the visible text only: never inside a drawing or a tag,
        where "12.5" or "10,200" are coordinates."""
        rules = UNITS.get(self.lang, [])
        parts = MARKUP.split(s)
        for i in range(0, len(parts), 2):
            for rx, to in rules:
                parts[i] = rx.sub(to, parts[i])
        return "".join(parts)

    def text(self, en, es=None, where="text", optional=False, fig=None):
        if not wordy(en):
            return self.units(en)
        holes = SVG.findall(en)
        tmpl = SVG.sub(HOLE, en)
        k = key(tmpl)
        if fig and f"{fig}:{tmpl}" in self.b.TEXT:
            self.used.add(f"{fig}:{tmpl}")
            out = self.b.TEXT[f"{fig}:{tmpl}"]
        elif k in self.b.TEXT:
            self.used.add(k)
            out = self.b.TEXT[k]
        elif tmpl in self.rev:
            out = self.rev[tmpl]
        else:
            if optional or (es is not None and es == en):
                self.optional.append((where, tmpl))
                return self.units(en)
            self.missing.append((where, tmpl, es))
            return en
        for h in holes:
            out = out.replace(HOLE, h, 1)
        return out

    def pair(self, x, where):
        y = dict(x)
        y[self.lang] = self.text(x["en"], x.get("es"), where)
        return y

    def walk(self, x, where):
        if isinstance(x, dict) and "en" in x and isinstance(x["en"], str):
            return self.pair(x, where)
        if isinstance(x, tuple):
            return tuple(self.walk(i, where) for i in x)
        if isinstance(x, list):
            return [self.walk(i, where) for i in x]
        return x

    def svg(self, en_svg, es_svg, where):
        """The English drawing with each label translated."""
        same = set(m.group(2) for m in TEXT.finditer(es_svg))
        fig = where.split(" ")[-1]

        def sub(m):
            s = m.group(2)
            return m.group(1) + self.text(s, None, where, optional=s in same, fig=fig) + m.group(3)

        out = TEXT.sub(sub, en_svg)
        return ARIA.sub(lambda m: m.group(1) + self.text(m.group(2), None, where + " title") + m.group(3), out, count=1)

    def figure(self, fn, where):
        cache = {}

        def draw(lang):
            if lang not in cache:
                cache[lang] = self.svg(fn("en"), fn("es"), where) if lang == self.lang else fn(lang)
            return cache[lang]
        draw(self.lang)
        return draw


def _block(tr, b, i):
    kind = b[0]
    where = f"{kind} {i}"
    if kind == "fig":
        name = getattr(b[1], "__name__", "figure")
        return ("fig", tr.figure(b[1], f"figure {name}"), tr.walk(b[2], f"caption {name}"))
    if kind == "entry":
        _, name, body, pills, tip, k = b
        if tip:
            tip = (tip[0], tip[1], tr.text(tip[0], tip[1], where + " tip"))
        return ("entry", tr.walk(name, where), tr.walk(body, where), tr.walk(pills, where), tip, k)
    return tr.walk(b, where)


class View:
    """What the page and PDF builders read from a topic, in one language."""

    def __init__(self, mod, lang):
        self.mod, self.lang = mod, lang
        self.SOURCES = mod.SOURCES
        if lang in BASE:
            self.META, self.BANK, self.TAGS, self.GLOSSARY = mod.META, mod.BANK, mod.TAGS, mod.GLOSSARY
            self._blocks, self._quiz = mod.blocks, mod.quiz
            self.missing = []
            return
        tr = self.tr = Translator(mod, lang)
        b = tr.b
        meta = dict(mod.META["en"])
        for k in meta:
            if k in b.META:
                meta[k] = b.META[k]
            else:
                tr.missing.append(("meta " + k, meta[k], None))
        self.META = dict(mod.META)
        self.META[lang] = meta
        # bank: every text gets a third language
        self.BANK = []
        for q in mod.BANK:
            t = b.BANK.get(q["id"])
            if t and len(t[1]) != len(q["o"]):
                raise ValueError(f"{lang}.py: question {q['id']} has {len(t[1])} options, bank.py has {len(q['o'])}")
            if not t:
                tr.missing.append(("question " + q["id"], q, None))
            nq = copy.deepcopy(q)
            nq["q"][lang] = t[0] if t else q["q"]["en"]
            nq["why"][lang] = t[2] if t else q["why"]["en"]
            for j, o in enumerate(nq["o"]):
                o[lang] = t[1][j] if t else o["en"]
            self.BANK.append(nq)
        self.TAGS = {}
        for k, v in mod.TAGS.items():
            t = b.TAGS.get(k)
            if t and len(t[1]) != len(v["recap"]):
                raise ValueError(f"{lang}.py: tag {k} has {len(t[1])} recap lines, bank.py has {len(v['recap'])}")
            if not t:
                tr.missing.append(("tag " + k, v, None))
            nv = dict(v)
            nv[lang] = t[0] if t else v["en"]
            nv["recap"] = [tuple(r) + ((t[1][j] if t else r[0]),) for j, r in enumerate(v["recap"])]
            nv["trap"] = tuple(v["trap"]) + ((t[2] if t else v["trap"][0]),)
            self.TAGS[k] = nv
        self.GLOSSARY = [(es, tr.text(en, None, "glossary")) for es, en in mod.GLOSSARY]
        self._blocks = lambda: [_block(tr, x, i) for i, x in enumerate(mod.blocks())]
        self._quiz = lambda: tr.walk(mod.quiz(), "self-test")
        self.missing = tr.missing

    def blocks(self):
        return self._blocks()

    def quiz(self):
        return self._quiz()


def view(mod, lang):
    return View(mod, lang)


def missing(mod, lang):
    """Everything the page and the PDF would show in English instead of `lang`."""
    v = View(mod, lang)
    v.blocks()
    v.quiz()
    seen, out = set(), []
    for m in v.missing:
        k = (m[0].split(" ")[0], repr(m[1]))
        if k not in seen:
            seen.add(k)
            out.append(m)
    return v, out


# ------------------------------------------------------------------------------------------ command line
def _plain(s):
    return re.sub(r"\s+", " ", s).strip()


def todo(tid, lang="uk"):
    import topics
    mod = topics.load(tid)
    if not book(mod, lang):
        print(f"{tid}: no {lang}.py yet. Create tools/topics/{topics.BUILT[tid]}/{lang}.py first (see the top of tools/i18n.py).")
        return
    v, miss = missing(mod, lang)
    print(f"## {tid}: {len(miss)} to translate")
    figs = {}
    for where, en, es in miss:
        if where.startswith("figure"):
            figs.setdefault(where.split(" ")[1], []).append(en)
    for where, en, es in miss:
        kind = where.split(" ")[0]
        if kind == "meta":
            print(f"META {where[5:]}: {_plain(en)}")
        elif kind == "question":
            q = en
            o = " || ".join(_plain(x["en"]) for x in q["o"])
            print(f"Q {q['id']} [{q['tag']}] {_plain(q['q']['en'])} || {o} || WHY: {_plain(q['why']['en'])}")
        elif kind == "tag":
            print(f"TAG {where[4:]}: {en['en']} || " + " || ".join(r[0] for r in en["recap"]) + f" || TRAP: {en['trap'][0]}")
        elif kind == "figure":
            continue
        else:
            print(f"X {key(en)} ({where}) {_plain(en)}")
    opt, seen = [], set()
    for where, en in v.tr.optional:
        if en not in seen and re.search(r"[a-z]{2,}", re.sub(r"<[^>]+>", " ", en)):
            seen.add(en)
            opt.append((where, en))
    if opt:
        print("## optional: the same in English and Spanish, shown as they are (with Ukrainian units) unless given here")
        for where, en in opt:
            fig = where.split(" ")[1] if where.startswith("figure") else None
            print(f"X {fig + ':' + en if fig else key(en)} ({where}) {_plain(en)}")
    for name, items in figs.items():
        es_txt = []
        try:
            fn = next(b[1] for b in mod.blocks() if b[0] == "fig" and getattr(b[1], "__name__", "") == name)
            es_txt = [html.unescape(m.group(2)) for m in TEXT.finditer(fn("es"))]
        except StopIteration:
            pass
        print(f"## figure {name}" + (f" (Spanish labels: {' | '.join(es_txt)})" if es_txt else ""))
        for en in items:
            print(f"X {key(en)} {en}")


def check(tids, lang="uk"):
    import topics
    bad = 0
    for tid in tids:
        mod = topics.load(tid)
        b = book(mod, lang)
        if not b:
            continue
        v, miss = missing(mod, lang)
        unused = sorted(set(b.TEXT) - v.tr.used)
        stale_q = sorted(set(b.BANK) - {q["id"] for q in mod.BANK})
        stale_t = sorted(set(b.TAGS) - set(mod.TAGS))
        # an unused key can still serve the self-test through the bank, or a label that is optional
        print(f"{tid}: {len(miss)} missing, {len(unused)} unused text keys, {len(stale_q)} unknown question ids, {len(stale_t)} unknown tags"
              + (f"  unused: {' '.join(unused[:12])}" if unused else "") + (f"  ids: {' '.join(stale_q)}" if stale_q else ""))
        bad += len(miss) + len(stale_q) + len(stale_t)
    return bad


if __name__ == "__main__":
    import topics
    cmd, args = (sys.argv[1] if len(sys.argv) > 1 else "check"), sys.argv[2:]
    if cmd == "todo":
        for t in args:
            todo(t)
    elif cmd == "check":
        sys.exit(1 if check(args or list(topics.BUILT)) else 0)
    else:
        print(__doc__)
