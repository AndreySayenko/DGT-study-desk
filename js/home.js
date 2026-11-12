// Main screen: choose a licence category, then one of its topics. Shows progress per topic and holds
// Export / Import for the progress of all topics. Categories and topics come from js/catalog.js.
//   index.html      categories
//   index.html#b    topics of category B (#a for A1 / A2)
(function () {
  'use strict';
  var CATS = window.DGT_CATALOG.categories;

  var TXT = {
    en: {
      eyebrow: 'Spanish driving theory · DGT exam', chooseH: 'Choose your licence',
      chooseLead: 'Pick the category you are studying for, then a topic. Each topic has study notes and tests, and your progress is saved as you go.',
      catReady: '{r} of {n} topics ready', catAnswers: '{a} answers given', cont: 'Continue: {c}, Topic {n}',
      allCats: '‹ All categories', topicsLead: '{n} topics. Topics marked “Coming soon” are not written yet.',
      topic: 'Topic', soon: 'Coming soon', notStarted: 'Not started', inProgress: 'In progress', unfinished: 'Unfinished test',
      qs: '{q} questions', seen: '{s} of {q} seen', acc: '{p} % correct', openErr: '{o} open mistakes',
      xfer: 'Back up or move your progress', export: 'Export progress', import: 'Import progress',
      xferNote: 'Export saves the progress of every topic to one file. On another computer, open this main screen and import that file. It is merged with any progress already there, keeping the most recent result for each question.',
      xferLocal: 'Right now progress is kept in this browser only. Start the project with npm start to also keep it in the project folder.',
      exported: 'Progress exported to {f}. Look in your Downloads folder.',
      imported: 'Imported progress from {d} (topics: {k}, questions: {n}, finished tests: {m}) and merged it with the progress here.',
      importBad: 'That file is not a DGT Study Desk progress file, so nothing was changed.'
    },
    es: {
      eyebrow: 'Teoría del permiso de conducir · Examen de la DGT', chooseH: 'Elige tu permiso',
      chooseLead: 'Elige el permiso que estás preparando y después un tema. Cada tema tiene apuntes y tests, y tu progreso se guarda sobre la marcha.',
      catReady: '{r} de {n} temas disponibles', catAnswers: '{a} respuestas dadas', cont: 'Continuar: {c}, tema {n}',
      allCats: '‹ Todos los permisos', topicsLead: '{n} temas. Los marcados como «Próximamente» aún no están escritos.',
      topic: 'Tema', soon: 'Próximamente', notStarted: 'Sin empezar', inProgress: 'En curso', unfinished: 'Test sin terminar',
      qs: '{q} preguntas', seen: '{s} de {q} vistas', acc: '{p} % de aciertos', openErr: '{o} errores pendientes',
      xfer: 'Copia de seguridad y traslado del progreso', export: 'Exportar progreso', import: 'Importar progreso',
      xferNote: 'Exportar guarda el progreso de todos los temas en un archivo. En otro ordenador, abre esta pantalla principal e importa ese archivo. Se combina con el progreso que ya haya allí y se conserva el resultado más reciente de cada pregunta.',
      xferLocal: 'Ahora el progreso se guarda solo en este navegador. Abre el proyecto con npm start para guardarlo también en la carpeta del proyecto.',
      exported: 'Progreso exportado a {f}. Búscalo en tu carpeta de Descargas.',
      imported: 'Progreso del {d} importado (temas: {k}, preguntas: {n}, tests terminados: {m}) y combinado con el progreso de aquí.',
      importBad: 'Ese archivo no es un archivo de progreso de DGT Study Desk, así que no se ha cambiado nada.'
    }
  };

  var xferMsg = null;   // {k, p, ok}: result of the last export or import

  function lang() { return DGT.lang(); }
  function t(k) { return TXT[lang()][k] || k; }
  function fmt(k, p) { return t(k).replace(/\{(\w)\}/g, function (_, x) { return p && p[x] !== undefined ? p[x] : ''; }); }
  function L(o) { return o ? (o[lang()] || o.en || '') : ''; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function pct(r, w) { return r + w ? Math.round(100 * r / (r + w)) : 0; }
  function findCat(id) { for (var i = 0; i < CATS.length; i++) if (CATS[i].id === id) return CATS[i]; return null; }
  function route() { return findCat(location.hash.slice(1)); }
  function title(tp) { return tp.title ? L(tp.title) : t('topic') + ' ' + tp.n; }
  function band(eyebrow, h1, lead) {
    return '<div class="band"><div class="eyebrow">' + esc(eyebrow) + '</div><h1 tabindex="-1">' + esc(h1) + '</h1><p>' + esc(lead) + '</p></div>';
  }
  function lastTopic() {
    var id = DGT.last();
    for (var i = 0; i < CATS.length; i++) for (var j = 0; j < CATS[i].topics.length; j++) {
      var tp = CATS[i].topics[j];
      if (tp.id === id && tp.page) return { c: CATS[i], tp: tp };
    }
    return null;
  }

  // ------------------------------------------------------------------ screens
  function renderCats() {
    var h = band(t('eyebrow'), t('chooseH'), t('chooseLead'));
    var last = lastTopic();
    if (last) h += '<div class="actions"><a class="btn primary" href="' + esc(last.tp.page) + '">' + esc(fmt('cont', { c: L(last.c.name), n: last.tp.n })) + '</a></div>';
    h += '<div class="cats">';
    CATS.forEach(function (c) {
      var ready = 0, answers = 0;
      c.topics.forEach(function (tp) {
        if (tp.page) ready++;
        var s = DGT.topicSummary(tp.id); if (s) answers += s.r + s.w;
      });
      h += '<a class="cat" href="#' + esc(c.id) + '"><span class="cat-tag">' + esc(c.tag) + '</span>' +
        '<span class="cat-name">' + esc(L(c.name)) + '</span><span class="cat-sub">' + esc(L(c.sub)) + '</span>' +
        '<span class="cat-meta">' + esc(fmt('catReady', { r: ready, n: c.topics.length })) + (answers ? ' · ' + esc(fmt('catAnswers', { a: answers })) : '') + '</span></a>';
    });
    return h + '</div>';
  }

  function renderTopics(c) {
    var h = '<a class="back-link" href="#">' + esc(t('allCats')) + '</a>';
    h += band(L(c.sub) + ' · DGT', L(c.name), fmt('topicsLead', { n: c.topics.length }));
    h += '<ol class="topics">';
    c.topics.forEach(function (tp) {
      if (!tp.page) {
        h += '<li><div class="topic soon"><span class="tn">' + tp.n + '</span><span class="tb"><span class="tt">' + esc(title(tp)) + '</span></span>' +
          '<span class="chip new">' + esc(t('soon')) + '</span></div></li>';
        return;
      }
      var s = DGT.topicSummary(tp.id), n = s ? s.r + s.w : 0, q = tp.questions;
      var chip = !n ? ['new', 'notStarted'] : s.unfinished ? ['mid', 'unfinished'] : ['go', 'inProgress'];
      var facts = [fmt('qs', { q: q })];
      if (n) {
        facts.push(fmt('seen', { s: Math.min(s.seen, q), q: q }), fmt('acc', { p: pct(s.r, s.w) }));
        if (s.open) facts.push(fmt('openErr', { o: s.open }));
      }
      h += '<li><a class="topic ready" href="' + esc(tp.page) + '"><span class="tn">' + tp.n + '</span><span class="tb">' +
        '<span class="tt">' + esc(title(tp)) + '</span><span class="ts">' + esc(facts.join(' · ')) + '</span>' +
        (n ? '<span class="meter" aria-hidden="true"><span style="width:' + Math.round(100 * Math.min(s.seen, q) / (q || 1)) + '%"></span></span>' : '') +
        '</span><span class="chip ' + chip[0] + '">' + esc(t(chip[1])) + '</span><span class="arrow" aria-hidden="true">›</span></a></li>';
    });
    return h + '</ol>';
  }

  function renderXfer() {
    var has = Object.keys(DGT.exportDoc().topics).length > 0;
    var h = '<section class="xfer"><div class="sub">' + esc(t('xfer')) + '</div><p class="note">' + esc(t('xferNote')) + '</p>';
    if (!DGT.probing() && DGT.mode() === 'local' && !window.claude) h += '<p class="note">' + esc(t('xferLocal')) + '</p>';
    h += '<div class="actions">';
    if (has) h += '<button class="btn" data-act="export">' + esc(t('export')) + '</button>';
    h += '<button class="btn" data-act="import">' + esc(t('import')) + '</button></div>';
    if (xferMsg) h += '<p class="xmsg ' + (xferMsg.ok ? 'ok' : 'no') + '" role="status">' + esc(fmt(xferMsg.k, xferMsg.p)) + '</p>';
    return h + '</section>';
  }

  function render() {
    var el = document.getElementById('home'); if (!el) return;
    var c = route();
    el.innerHTML = (c ? renderTopics(c) : renderCats()) + renderXfer();
    document.title = (c ? L(c.name) + ' · ' : '') + 'DGT Study Desk';
  }

  // ------------------------------------------------------------------ export / import
  function pad2(n) { return (n < 10 ? '0' : '') + n; }
  function exportFile() {
    var d = new Date(), name = 'dgt-progress-' + d.getFullYear() + '-' + pad2(d.getMonth() + 1) + '-' + pad2(d.getDate()) + '.json';
    var url = URL.createObjectURL(new Blob([JSON.stringify(DGT.exportDoc(), null, 2) + '\n'], { type: 'application/json' }));
    var a = document.createElement('a'); a.href = url; a.download = name;
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 2000);
    xferMsg = { k: 'exported', p: { f: name }, ok: true }; render();
  }
  function importFile() {
    var inp = document.createElement('input');
    inp.type = 'file'; inp.accept = '.json,application/json';
    inp.addEventListener('change', function () {
      var f = inp.files && inp.files[0]; if (!f) return;
      var rd = new FileReader();
      rd.onload = function () {
        var doc = null;
        try { doc = JSON.parse(String(rd.result)); } catch (e) { /* not JSON */ }
        var sum = DGT.importDoc(doc);
        if (!sum) { xferMsg = { k: 'importBad', ok: false }; return render(); }
        var d = sum.date ? new Date(sum.date).toLocaleDateString(lang() === 'es' ? 'es-ES' : 'en-GB', { day: 'numeric', month: 'short', year: 'numeric' }) : '–';
        xferMsg = { k: 'imported', p: { d: d, k: sum.topics, n: sum.questions, m: sum.tests }, ok: true };
        render();
      };
      rd.onerror = function () { xferMsg = { k: 'importBad', ok: false }; render(); };
      rd.readAsText(f);
    });
    inp.click();
  }

  // ------------------------------------------------------------------ events + boot
  document.addEventListener('click', function (ev) {
    var el = ev.target.closest('[data-act]'); if (!el) return;
    var act = el.getAttribute('data-act');
    if (act === 'export') exportFile();
    else if (act === 'import') importFile();
  });
  window.addEventListener('hashchange', function () {
    xferMsg = null; render(); window.scrollTo(0, 0);
    var h1 = document.querySelector('#home h1'); if (h1) h1.focus({ preventScroll: true });
  });
  DGT.on(function (ev) { if (ev.type !== 'import') render(); });

  var ids = [];
  CATS.forEach(function (c) { c.topics.forEach(function (tp) { if (tp.page) ids.push(tp.id); }); });
  DGT.start(ids);
  render();
})();
