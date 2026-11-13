// Shared by the main screen (home.js) and the topic pages (app.js): preferences, saving progress,
// export/import, and the header controls (language, theme, save indicator). Exposed as window.DGT.
//
// Where progress lives: this browser's localStorage, one key per topic ("dgt-progress-b-01") and one for
// preferences ("dgt-prefs"). Export writes every topic to a JSON file; Import merges such a file into
// localStorage and every open page redraws from it, so progress moves between devices without a server.
// Only when the page runs as a Claude artifact is there also a remote copy, in the Claude account; then each
// topic keeps whichever copy changed last.
(function () {
  'use strict';
  var K_PREFS = 'dgt-prefs', K_LAST = 'dgt-last-topic', K_TOPIC = 'dgt-progress-';
  var K_V1 = 'dgt-topic1-v1', V1_TOPIC = 'b-01';                  // before topics existed, Topic 1 was the only one
  var TOPIC_ID = /^[a-z]-\d{2}$/;
  // Every page has English and Spanish; a page translated further lists its languages in <html data-langs>.
  var LANGS = ['en', 'es', 'uk'];
  var NAMES = { en: 'English', es: 'Español', uk: 'Українська' };

  var TXT = {
    en: { light: 'Light', dark: 'Dark', saveCloud: 'Progress saved to your account', saveLocal: 'Progress saved in this browser', saveOff: 'Progress is not saved: this browser blocks storage' },
    es: { light: 'Claro', dark: 'Oscuro', saveCloud: 'Progreso guardado en tu cuenta', saveLocal: 'Progreso guardado en este navegador', saveOff: 'El progreso no se guarda: este navegador bloquea el almacenamiento' },
    uk: { light: 'Світла', dark: 'Темна', saveCloud: 'Прогрес збережено у вашому обліковому записі', saveLocal: 'Прогрес збережено в цьому браузері', saveOff: 'Прогрес не зберігається: цей браузер блокує сховище' }
  };
  // Shown, in the language the reader chose, on a page that is not translated into it.
  var NOT_HERE = { uk: 'Цю сторінку ще не перекладено українською, тому вона англійською.' };

  // ------------------------------------------------------------------ shapes
  function num(x) { return typeof x === 'number' && isFinite(x); }
  function clone(o) { return JSON.parse(JSON.stringify(o)); }
  function freshTopic() { return { v: 1, updated: 0, stats: {}, sessions: [], cur: null, task: null, ai: null }; }
  function saneTopic(o) {
    if (!o || typeof o !== 'object' || o.v !== 1) return null;
    var b = freshTopic();
    Object.keys(b).forEach(function (k) { if (o[k] !== undefined && o[k] !== null) b[k] = o[k]; });
    if (!num(b.updated)) b.updated = 0;
    var stats = {};
    if (b.stats && typeof b.stats === 'object') Object.keys(b.stats).forEach(function (id) {
      var x = b.stats[id];
      if (x && typeof x === 'object' && typeof x.tag === 'string' && num(x.r) && num(x.w)) stats[id] = x;
    });
    b.stats = stats;
    b.sessions = Array.isArray(b.sessions) ? b.sessions.filter(function (s) { return s && num(s.t); }) : [];
    return b;
  }
  function sanePrefs(o) {
    var p = { lang: null, theme: null, updated: 0 };
    if (!o || typeof o !== 'object') return p;
    if (LANGS.indexOf(o.lang) >= 0) p.lang = o.lang;
    if (o.theme === 'light' || o.theme === 'dark') p.theme = o.theme;
    if (num(o.updated)) p.updated = o.updated;
    return p;
  }
  // Reads any progress document: the current format ({topics: {...}}), the old one-topic format ({state}),
  // or a bare old state. Returns {topicId: state} or null.
  function topicsOf(doc) {
    if (!doc || typeof doc !== 'object') return null;
    var out = {};
    if (doc.topics && typeof doc.topics === 'object') {
      Object.keys(doc.topics).forEach(function (id) { var st = TOPIC_ID.test(id) && saneTopic(doc.topics[id]); if (st) out[id] = st; });
      return out;
    }
    var old = saneTopic('state' in doc ? doc.state : doc);
    if (!old) return null;
    out[V1_TOPIC] = old;
    return out;
  }

  // ------------------------------------------------------------------ browser storage
  var mem = {};   // in-memory copy, so the open page keeps working when localStorage is blocked or full
  function lsGet(k) { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } }
  function lsSet(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); return true; } catch (e) { return false; } }
  // False when this browser refuses to store anything (some private windows, blocked site data) or a write failed.
  var canStore = lsSet('dgt-probe', 1);
  try { localStorage.removeItem('dgt-probe'); } catch (e) { /* unavailable */ }
  function localIds() {
    var ids = {};
    try { for (var i = 0; i < localStorage.length; i++) { var k = localStorage.key(i); if (k && k.indexOf(K_TOPIC) === 0) ids[k.slice(K_TOPIC.length)] = 1; } } catch (e) { /* unavailable */ }
    Object.keys(mem).forEach(function (id) { ids[id] = 1; });
    return Object.keys(ids).filter(function (id) { return TOPIC_ID.test(id); });
  }
  function loadTopic(id) { return mem[id] ? clone(mem[id]) : saneTopic(lsGet(K_TOPIC + id)); }
  function storeTopic(id, st) {
    mem[id] = clone(st);
    if (!lsSet(K_TOPIC + id, st) && canStore) { canStore = false; paintSync(); }
  }

  // One-time move of the old single-topic key. The old key is left in place as a fallback copy.
  (function migrate() {
    var old = lsGet(K_V1);
    if (!old || lsGet(K_TOPIC + V1_TOPIC)) return;
    var st = saneTopic(old); if (st) lsSet(K_TOPIC + V1_TOPIC, st);
    if (!lsGet(K_PREFS)) lsSet(K_PREFS, sanePrefs({ lang: old.lang, theme: old.theme, updated: num(old.updated) ? old.updated : 0 }));
  })();

  var P = sanePrefs(lsGet(K_PREFS));

  // ------------------------------------------------------------------ change notifications
  var listeners = [];
  function on(fn) { listeners.push(fn); }
  function emit(ev) { listeners.forEach(function (fn) { try { fn(ev); } catch (e) { console.error(e); } }); }

  // ------------------------------------------------------------------ remote copy (Claude artifact only)
  // A remote has kind and put(topicId, state) -> Promise, which rejects with {fatal: true} when retrying cannot help.
  var remote = null, mode = 'local', probing = true;
  var pending = {}, writing = false, timer = null, retryMs = 5000;

  function setMode(m) {
    if (m === mode) return;
    mode = m; paintSync(); emit({ type: 'mode' });
  }
  function queue(key) {
    if (!remote) return;
    pending[key] = true;
    clearTimeout(timer); retryMs = 5000; timer = setTimeout(flush, 700);
  }
  function flush() {
    clearTimeout(timer); timer = null;
    if (!remote || writing) return;
    var keys = Object.keys(pending); if (!keys.length) return;
    pending = {}; writing = true;
    var r = remote, failed = [], fatal = false;
    Promise.all(keys.map(function (k) {
      var data = loadTopic(k);
      if (!data) return null;
      return r.put(k, clone(data)).catch(function (e) { failed.push(k); if (e && e.fatal) fatal = true; });
    })).then(function () {
      writing = false;
      if (fatal) { remote = null; setMode('local'); return; }
      if (failed.length) {
        // Temporary problem (network down): try again later, backing off up to a minute.
        failed.forEach(function (k) { pending[k] = true; });
        setMode('local');
        timer = setTimeout(flush, retryMs); retryMs = Math.min(retryMs * 2, 60000);
        return;
      }
      retryMs = 5000; setMode(r.kind);
      if (Object.keys(pending).length) flush();
    });
  }
  // Bring browser and remote in line: per topic the newer copy wins; newer local copies are pushed.
  function reconcile(r, remoteTopics, ids) {
    var changed = [];
    remote = r;
    ids.forEach(function (id) {
      var loc = loadTopic(id), rem = remoteTopics[id];
      if (rem && (!loc || rem.updated > loc.updated)) { storeTopic(id, rem); changed.push(id); }
      else if (loc && loc.updated > (rem ? rem.updated : 0)) queue(id);
    });
    flush();
    setMode(r.kind);
    if (changed.length) emit({ type: 'remote', topics: changed, prefs: false });
  }
  function withTimeout(p) {
    return Promise.race([p, new Promise(function (_, rej) { setTimeout(function () { rej(new Error('timeout')); }, 10000); })]);
  }

  function connectCloud(ids) {
    return Promise.all([window.claude.use('db'), window.claude.use('user')]).then(function (r) {
      var db = r[0], user = r[1];
      if (!db || !user) throw new Error('no db');
      return user.id().then(function (uid) {
        if (!uid) throw new Error('no user');
        // Topic 1 keeps the document name it had before topics existed.
        function ref(id) { return db.doc('data/users/' + uid + '/' + (id === V1_TOPIC ? 'topic1' : id)); }
        return withTimeout(Promise.all(ids.map(function (id) {
          return ref(id).get().then(function (snap) { return snap.exists ? saneTopic(clone((snap.data() || {}).state || null)) : null; });
        }))).then(function (states) {
          var topics = {}; ids.forEach(function (id, i) { if (states[i]) topics[id] = states[i]; });
          reconcile({
            kind: 'cloud',
            put: function (key, data) {
              return ref(key).set({ state: data }).catch(function (e) {
                throw { fatal: !(e && (e.code === 'unavailable' || e.code === 'resource_exhausted')) };
              });
            }
          }, topics, ids);
        });
      });
    });
  }

  // Another tab of this site changed something (an answer, or an import on the main screen): pick it up, so
  // this page shows it at once and never saves an older copy over it.
  window.addEventListener('storage', function (e) {
    if (!e.key) return;
    if (e.key.indexOf(K_TOPIC) === 0) {
      var id = e.key.slice(K_TOPIC.length); delete mem[id];
      emit({ type: 'remote', topics: [id], prefs: false });
    } else if (e.key === K_PREFS) {
      P = sanePrefs(lsGet(K_PREFS)); applyPrefs(); emit({ type: 'remote', topics: [], prefs: true });
    }
  });

  // ------------------------------------------------------------------ public: topics
  function saveTopic(id, st) {
    st.updated = Date.now();
    storeTopic(id, st);
    queue(id);
  }
  function topicSummary(id) {
    var st = loadTopic(id); if (!st) return null;
    var aiIds = {};
    if (st.ai && Array.isArray(st.ai.questions)) st.ai.questions.forEach(function (q) { if (q && q.id) aiIds[q.id] = 1; });
    var s = { r: 0, w: 0, seen: 0, open: 0, unfinished: !!st.cur, tests: st.sessions.length, updated: st.updated };
    Object.keys(st.stats).forEach(function (qid) {
      var x = st.stats[qid], ai = qid.indexOf('ai') === 0;
      s.r += x.r; s.w += x.w;
      if (!ai) s.seen++;
      if (x.w > 0 && x.streak < 2 && (!ai || aiIds[qid])) s.open++;
    });
    return s;
  }

  // ------------------------------------------------------------------ public: export / import
  function exportDoc() {
    var topics = {};
    localIds().forEach(function (id) {
      var st = loadTopic(id);
      if (st && (Object.keys(st.stats).length || st.sessions.length || st.cur)) topics[id] = st;
    });
    return { app: 'dgt-study-desk', kind: 'progress', v: 2, saved: new Date().toISOString(), prefs: P, topics: topics };
  }
  // Per question, keep whichever record was answered most recently, so moving back and forth between
  // devices never loses anything. Tests in the history are combined. The unfinished test, study task and
  // Claude's questions come from whichever side changed last.
  function merge(base, inc) {
    var out = clone(base);
    Object.keys(inc.stats).forEach(function (id) {
      var a = out.stats[id], b = inc.stats[id];
      if (!a || (b.last || 0) > (a.last || 0)) out.stats[id] = b;
    });
    var seen = {};
    out.sessions = base.sessions.concat(inc.sessions).filter(function (s) {
      var k = [s.t, s.mode, s.total, s.good].join('|');
      if (seen[k]) return false; seen[k] = true; return true;
    }).sort(function (a, b) { return b.t - a.t; }).slice(0, 30);
    if (inc.updated > base.updated) { out.cur = inc.cur; out.task = inc.task; out.ai = inc.ai; }
    return out;
  }
  // Merges a parsed export (or an old one-topic export, or an old progress/progress.json) into localStorage and
  // tells every page: this one through the 'import' event, other open tabs through the storage event.
  // Language and theme stay as they are. Returns {topics, questions, tests, date} or null when it is not progress.
  function importDoc(doc) {
    var inc = topicsOf(doc);
    if (!inc || !Object.keys(inc).length) return null;
    var sum = { topics: 0, questions: 0, tests: 0, date: 0 };
    Object.keys(inc).forEach(function (id) {
      var st = inc[id];
      saveTopic(id, merge(loadTopic(id) || freshTopic(), st));
      sum.topics++; sum.questions += Object.keys(st.stats).length; sum.tests += st.sessions.length;
      sum.date = Math.max(sum.date, st.updated);
    });
    emit({ type: 'import', topics: Object.keys(inc) });
    return sum;
  }

  // ------------------------------------------------------------------ public: preferences + header
  function pageLangs() { return (document.documentElement.getAttribute('data-langs') || 'en es').split(/\s+/); }
  // The language the reader asked for (or their browser's), whether or not this page has it.
  function wanted() {
    if (P.lang) return P.lang;
    var nav = (navigator.language || 'en').toLowerCase();
    for (var i = 1; i < LANGS.length; i++) if (nav.indexOf(LANGS[i]) === 0) return LANGS[i];
    return 'en';
  }
  // The language this page is shown in: the wanted one, or English when the page is not translated into it.
  function lang() { var w = wanted(); return pageLangs().indexOf(w) >= 0 ? w : 'en'; }
  function locale() { return { en: 'en-GB', es: 'es-ES', uk: 'uk-UA' }[lang()]; }
  function t(k) { return TXT[lang()][k] || TXT.en[k] || k; }
  function theme() {
    if (P.theme) return P.theme;
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  function setPrefs(patch) {
    Object.keys(patch).forEach(function (k) { P[k] = patch[k]; });
    P.updated = Date.now(); lsSet(K_PREFS, P);
    applyPrefs();
  }
  function paintSync() {
    var el = document.getElementById('sync'); if (!el) return;
    el.className = 'sync' + (mode !== 'local' || canStore ? ' on' : '');
    el.lastChild.textContent = t(mode === 'cloud' ? 'saveCloud' : canStore ? 'saveLocal' : 'saveOff');
  }
  function paintNote(lg) {
    var w = wanted(), msg = w !== lg ? NOT_HERE[w] : null, el = document.getElementById('langnote');
    if (!msg) { if (el) el.hidden = true; return; }
    var bar = document.querySelector('.bar'); if (!bar) return;
    if (!el) {
      el = document.createElement('p'); el.id = 'langnote'; el.className = 'langnote'; el.setAttribute('role', 'note');
      bar.parentNode.insertBefore(el, bar.nextSibling);
    }
    el.lang = w; el.textContent = msg; el.hidden = false;
  }
  // The language menu shows the reader's choice. On a page not translated into it (a B page when Ukrainian
  // is chosen) the menu gets that language as an extra entry, so it still shows the choice, and picking
  // English or Spanish there is a real change.
  function paintLangMenu() {
    var sel = document.getElementById('lang-select'); if (!sel) return;
    var w = wanted(), extra = sel.querySelector('option[data-extra]');
    if (pageLangs().indexOf(w) < 0) {
      if (!extra) { extra = document.createElement('option'); extra.setAttribute('data-extra', ''); sel.appendChild(extra); }
      extra.value = w; extra.lang = w; extra.textContent = NAMES[w] || w;
    } else if (extra) sel.removeChild(extra);
    sel.value = w;
  }
  function applyPrefs() {
    var root = document.documentElement, lg = lang(), th = theme();
    root.setAttribute('data-lang', lg); root.setAttribute('lang', lg);
    if (P.theme) root.setAttribute('data-theme', P.theme); else root.removeAttribute('data-theme');
    paintLangMenu();
    paintNote(lg);
    ['light', 'dark'].forEach(function (x) { var b = document.getElementById('theme-' + x); if (b) { b.setAttribute('aria-pressed', String(x === th)); b.textContent = t(x); } });
    paintSync();
    emit({ type: 'prefs' });
  }
  // A page may set DGT.beforeLang = function (newLang) { return afterFn; } to keep its scroll position.
  document.addEventListener('click', function (ev) {
    var el = ev.target.closest('[data-theme-btn]'); if (el) setPrefs({ theme: el.getAttribute('data-theme-btn') });
  });
  document.addEventListener('change', function (ev) {
    var el = ev.target; if (!el || el.id !== 'lang-select') return;
    var lg = el.value; if (LANGS.indexOf(lg) < 0 || lg === wanted()) return;
    var after = typeof api.beforeLang === 'function' ? api.beforeLang(lg) : null;
    setPrefs({ lang: lg });
    if (typeof after === 'function') after();
  });

  // ------------------------------------------------------------------ start
  // ids: the topics this page needs from a Claude account.
  function start(ids) {
    applyPrefs();
    var p = window.claude && typeof window.claude.use === 'function' ? connectCloud(ids || []) : Promise.resolve();
    return p.catch(function () { /* stay on browser storage */ }).then(function () {
      probing = false; emit({ type: 'ready' });
    });
  }

  var api = {
    start: start, on: on,
    lang: lang, locale: locale, theme: theme, setPrefs: setPrefs,
    mode: function () { return mode; }, probing: function () { return probing; }, canStore: function () { return canStore; },
    loadTopic: loadTopic, saveTopic: saveTopic, freshTopic: freshTopic, topicSummary: topicSummary, flush: flush,
    exportDoc: exportDoc, importDoc: importDoc,
    last: function () { try { return localStorage.getItem(K_LAST); } catch (e) { return null; } },
    setLast: function (id) { try { localStorage.setItem(K_LAST, id); } catch (e) { /* unavailable */ } },
    beforeLang: null
  };
  window.DGT = api;
})();
