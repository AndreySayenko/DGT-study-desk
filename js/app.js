(function () {
  'use strict';
  var BANK = window.DGT_DATA.bank;
  var TAGS = window.DGT_DATA.tags;
  var TAG_ORDER = Object.keys(TAGS);
  var QMAP = {};
  BANK.forEach(function (q) { QMAP[q.id] = q; });
  var TOPIC = window.DGT_DATA.topic;   // e.g. "b-01"
  var EXAM_N = 30, EXAM_MAX_ERR = 3;

  var TXT = {
    en: {
      tests: 'Tests',
      xferHome: 'To back up your progress or move it to another computer, use Export and Import on the <a href="../index.html">main screen</a>.',
      answered: 'answers given', accuracy: 'accuracy', open: 'open mistakes', seen: 'questions seen',
      exam: 'Exam simulation (30 questions)', all: 'All questions by section', resume: 'Resume unfinished test', mistakes: 'Practise my mistakes',
      examNote: 'The exam simulation follows the DGT format: 30 questions, pass with 3 mistakes or fewer.',
      bySection: 'Results by section', sNew: 'not started', sWeak: 'weak', sMid: 'improving', sOk: 'solid',
      myErr: 'My mistakes', noErr: 'No open mistakes. Take a test and any wrong answer will be kept here until you get it right twice in a row.',
      you: 'You answered', right: 'Correct answer', times: 'wrong', review: 'Review the section',
      analysis: 'Error analysis', noData: 'Answer some questions first and the analysis will appear here.',
      genTask: 'Generate my study task', regen: 'Generate a new task', taskTitle: 'Your study task',
      taskNone: 'You have no open mistakes. To keep learning, here are the sections you have practised least.',
      step1: 'Re-read', step2: 'Memorise these rules', step3: 'Drill', drillStart: 'Start the drill', why: 'Why you probably slip here',
      drillGoal: 'questions. A mistake counts as fixed after two correct answers in a row.',
      ai: 'Ask Claude for new questions on my weak points', aiBusy: 'Claude is writing your questions…', aiFail: 'Claude could not write the questions just now. The built-in study task still works.',
      aiNote: 'Written by Claude from the rules on this page. Check anything surprising against the section text.',
      aiCoach: 'Coach note from Claude', aiStart: 'Start Claude’s questions',
      q: 'Question', of: 'of', next: 'Next question', finish: 'See the result', quit: 'Stop and save',
      ok: 'Correct.', no: 'Not correct.', result: 'Result', passed: 'Passed', failed: 'Not passed', errors: 'mistakes',
      back: 'Back to the test desk', retryWrong: 'Practise the ones I got wrong', done: 'Done',
      reset: 'Erase my progress in this topic', reset2: 'Click again to erase this topic’s progress', history: 'Recent tests',
      mExam: 'Exam simulation', mAll: 'All questions', mDrill: 'Drill', mAi: 'Claude’s questions', section: 'Section'
    },
    es: {
      tests: 'Tests',
      xferHome: 'Para hacer una copia de seguridad o llevar tu progreso a otro ordenador, usa Exportar e Importar en la <a href="../index.html">pantalla principal</a>.',
      answered: 'respuestas dadas', accuracy: 'aciertos', open: 'errores pendientes', seen: 'preguntas vistas',
      exam: 'Simulacro de examen (30 preguntas)', all: 'Todas las preguntas por apartado', resume: 'Continuar el test sin terminar', mistakes: 'Practicar mis errores',
      examNote: 'El simulacro sigue el formato de la DGT: 30 preguntas y se aprueba con 3 fallos o menos.',
      bySection: 'Resultados por apartado', sNew: 'sin empezar', sWeak: 'flojo', sMid: 'mejorando', sOk: 'sólido',
      myErr: 'Mis errores', noErr: 'No hay errores pendientes. Haz un test: cada fallo se guarda aquí hasta que aciertes esa pregunta dos veces seguidas.',
      you: 'Respondiste', right: 'Respuesta correcta', times: 'fallos', review: 'Repasar el apartado',
      analysis: 'Análisis de errores', noData: 'Responde primero algunas preguntas y aquí aparecerá el análisis.',
      genTask: 'Generar mi tarea de estudio', regen: 'Generar una tarea nueva', taskTitle: 'Tu tarea de estudio',
      taskNone: 'No tienes errores pendientes. Para seguir aprendiendo, estos son los apartados que menos has practicado.',
      step1: 'Vuelve a leer', step2: 'Memoriza estas reglas', step3: 'Practica', drillStart: 'Empezar la práctica', why: 'Por qué sueles fallar aquí',
      drillGoal: 'preguntas. Un error se da por corregido tras dos aciertos seguidos.',
      ai: 'Pedir a Claude preguntas nuevas sobre mis puntos flojos', aiBusy: 'Claude está escribiendo tus preguntas…', aiFail: 'Claude no ha podido escribir las preguntas ahora. La tarea de estudio integrada sigue funcionando.',
      aiNote: 'Escrito por Claude a partir de las reglas de esta página. Si algo te sorprende, compruébalo con el texto del apartado.',
      aiCoach: 'Nota de Claude', aiStart: 'Empezar las preguntas de Claude',
      q: 'Pregunta', of: 'de', next: 'Siguiente pregunta', finish: 'Ver el resultado', quit: 'Parar y guardar',
      ok: 'Correcto.', no: 'Incorrecto.', result: 'Resultado', passed: 'Aprobado', failed: 'No aprobado', errors: 'fallos',
      back: 'Volver a los tests', retryWrong: 'Practicar las que he fallado', done: 'Hecho',
      reset: 'Borrar mi progreso de este tema', reset2: 'Pulsa otra vez para borrar el progreso de este tema', history: 'Tests recientes',
      mExam: 'Simulacro de examen', mAll: 'Todas las preguntas', mDrill: 'Práctica', mAi: 'Preguntas de Claude', section: 'Apartado'
    }
  };

  // ------------------------------------------------------------------ state
  // S is this topic's progress. Saving it, language and theme are handled by js/shared.js (window.DGT).
  var S = DGT.loadTopic(TOPIC) || DGT.freshTopic();
  var view = 'home';       // home | run | result
  var lastResult = null;
  var answeredNow = null;  // {pick, ok} for the question on screen
  var aiBusy = false, aiError = false, resetArmed = false;
  var sampleFn = null;

  function save() { DGT.saveTopic(TOPIC, S); }
  // A newer copy of this topic arrived: from the project file, the Claude account, or another tab.
  function reload() {
    var st = DGT.loadTopic(TOPIC);
    if (!st || st.updated <= S.updated) return;
    S = st; answeredNow = null;
    if (view !== 'run') view = 'home';
    render();
  }
  DGT.on(function (ev) {
    if (ev.type === 'remote' || ev.type === 'import') { if (ev.topics.indexOf(TOPIC) >= 0) reload(); }
    else if (ev.type === 'prefs') { var h = document.getElementById('tests-h'); if (h) h.textContent = t('tests'); render(); }
  });

  // ------------------------------------------------------------------ helpers
  function lang() { return DGT.lang(); }
  function t(k) { return TXT[lang()][k] || k; }
  function L(o) { return o ? (o[lang()] || o.en || '') : ''; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function getQ(id) {
    if (QMAP[id]) return QMAP[id];
    if (S.ai && S.ai.questions) for (var i = 0; i < S.ai.questions.length; i++) if (S.ai.questions[i].id === id) return S.ai.questions[i];
    return null;
  }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var x = a[i]; a[i] = a[j]; a[j] = x; } return a; }
  function isOpen(st) { return st && st.w > 0 && st.streak < 2; }

  function tagStats() {
    var out = {};
    TAG_ORDER.forEach(function (g) { out[g] = { r: 0, w: 0, open: 0, seen: 0, total: 0 }; });
    BANK.forEach(function (q) { out[q.tag].total++; });
    Object.keys(S.stats).forEach(function (id) {
      var st = S.stats[id], g = out[st.tag]; if (!g) return;
      g.r += st.r; g.w += st.w; if (QMAP[id]) g.seen++; if (isOpen(st)) g.open++;
    });
    return out;
  }
  function tagStatus(g) {
    var n = g.r + g.w;
    if (!n) return 'new';
    if (g.open > 0 && g.r / n < 0.6) return 'weak';
    if (g.open > 0) return 'mid';
    return g.r / n >= 0.8 ? 'ok' : 'mid';
  }
  function openErrors() {
    return Object.keys(S.stats).filter(function (id) { return isOpen(S.stats[id]) && getQ(id); })
      .sort(function (a, b) { return S.stats[b].w - S.stats[a].w || S.stats[b].last - S.stats[a].last; });
  }
  function weakTags(n) {
    var ts = tagStats();
    var withErr = TAG_ORDER.filter(function (g) { return ts[g].open > 0; }).sort(function (a, b) {
      return ts[b].open - ts[a].open || (ts[a].r / (ts[a].r + ts[a].w)) - (ts[b].r / (ts[b].r + ts[b].w));
    });
    if (withErr.length) return { tags: withErr.slice(0, n), fromErrors: true };
    var least = TAG_ORDER.slice().sort(function (a, b) { return (ts[a].seen / ts[a].total) - (ts[b].seen / ts[b].total); });
    return { tags: least.slice(0, n), fromErrors: false };
  }
  function drillIds(tags) {
    var ids = [];
    tags.forEach(function (g) {
      var mine = BANK.filter(function (q) { return q.tag === g; }).map(function (q) { return q.id; });
      var wrong = mine.filter(function (id) { return isOpen(S.stats[id]); });
      var unseen = shuffle(mine.filter(function (id) { return !S.stats[id]; }));
      var rest = shuffle(mine.filter(function (id) { return S.stats[id] && !isOpen(S.stats[id]); }));
      ids = ids.concat(wrong.concat(unseen, rest).slice(0, Math.max(4, wrong.length)));
    });
    return ids;
  }
  function sectionLink(tag, label) {
    return '<a href="#' + lang() + '-s' + TAGS[tag].sec + '" data-go="s' + TAGS[tag].sec + '">' + label + '</a>';
  }

  // ------------------------------------------------------------------ sessions
  function start(mode, ids) {
    if (!ids.length) return;
    S.cur = { mode: mode, ids: ids, idx: 0, log: [], order: {} };
    answeredNow = null; view = 'run'; save(); render(); toDesk();
  }
  function answer(pick) {
    var c = S.cur; if (!c || answeredNow) return;
    var id = c.ids[c.idx], q = getQ(id); if (!q) return;
    var ok = pick === 0;
    var st = S.stats[id] || { tag: q.tag, r: 0, w: 0, streak: 0, last: 0, pick: null };
    if (ok) { st.r++; st.streak++; } else { st.w++; st.streak = 0; st.pick = pick; }
    st.last = Date.now(); S.stats[id] = st;
    c.log.push({ id: id, ok: ok, pick: pick });
    answeredNow = { pick: pick, ok: ok };
    save(); render();
  }
  function next() {
    var c = S.cur; if (!c) return;
    answeredNow = null; c.idx++;
    if (c.idx >= c.ids.length) return finish();
    save(); render();
  }
  function finish() {
    var c = S.cur; if (!c) { view = 'home'; return render(); }
    var good = c.log.filter(function (x) { return x.ok; }).length;
    lastResult = { mode: c.mode, total: c.log.length, good: good, wrong: c.log.filter(function (x) { return !x.ok; }).map(function (x) { return x.id; }) };
    if (c.log.length) { S.sessions.unshift({ t: Date.now(), mode: c.mode, total: c.log.length, good: good }); S.sessions = S.sessions.slice(0, 30); }
    S.cur = null; answeredNow = null; view = c.log.length ? 'result' : 'home';
    save(); render();
  }

  // ------------------------------------------------------------------ study task
  function makeTask() {
    var w = weakTags(3);
    S.task = { t: Date.now(), tags: w.tags, fromErrors: w.fromErrors, ids: drillIds(w.tags) };
    save(); render();
    var el = document.getElementById('task'); if (el) el.scrollIntoView({ block: 'start' });
  }
  function askClaude() {
    if (!sampleFn || aiBusy) return;
    var w = weakTags(3), es = lang() === 'es';
    var facts = w.tags.map(function (g) {
      return '[' + g + '] ' + TAGS[g].en + ':\n' + TAGS[g].recap.map(function (r) { return '- ' + r[0]; }).join('\n');
    }).join('\n\n');
    var errs = openErrors().slice(0, 10).map(function (id) {
      var q = getQ(id), st = S.stats[id];
      return '- [' + q.tag + '] Q: ' + q.q.en.replace(/<[^>]+>/g, '') + ' | learner chose: ' + (q.o[st.pick] ? q.o[st.pick].en.replace(/<[^>]+>/g, '') : '?') +
        ' | correct: ' + q.o[0].en.replace(/<[^>]+>/g, '') + ' | wrong ' + st.w + ' time(s)';
    }).join('\n');
    var about = (window.DGT_DATA.category === 'a' ? 'category A1/A2' : 'category B') + ', ' + ((window.DGT_DATA.title || {}).en || 'this topic');
    var prompt = 'You are a tutor for the Spanish DGT driving theory exam (' + about + ').\n' +
      'Use ONLY the facts below. Do not add numbers or rules that are not listed.\n\nFACTS\n' + facts +
      '\n\nLEARNER MISTAKES\n' + (errs || '(none yet; the learner has practised these sections least)') +
      '\n\nWrite in ' + (es ? 'Spanish' : 'English, keeping the Spanish exam term in parentheses where useful') + '.\n' +
      'Return ONLY a JSON object with this shape:\n' +
      '{"coach": "3 to 5 sentences: what pattern the mistakes show and one memory trick per weak section",' +
      ' "questions": [{"tag": "one of: ' + w.tags.join(', ') + '", "q": "question text", "options": ["correct answer", "plausible wrong answer", "plausible wrong answer"], "why": "one-sentence explanation"}]}\n' +
      'Write exactly 6 new multiple-choice questions that are different from the ones in the mistakes list, each testing a fact above. ' +
      'In every question the FIRST option must be the correct one. Exactly 3 options each. Plain text, no markdown.';
    aiBusy = true; aiError = false; render();
    Promise.resolve().then(function () { return sampleFn.json(prompt, { cache: false }); }).then(function (v) {
      if (typeof v === 'string') v = JSON.parse(v);
      var qs = (v && Array.isArray(v.questions) ? v.questions : []).filter(function (x) {
        return x && typeof x.q === 'string' && Array.isArray(x.options) && x.options.length === 3 && TAGS[x.tag];
      }).slice(0, 8);
      if (!qs.length) throw new Error('empty');
      var stamp = Date.now();
      S.ai = {
        t: stamp, coach: String(v.coach || ''), questions: qs.map(function (x, i) {
          var o = x.options.map(function (s) { s = esc(String(s)); return { en: s, es: s }; });
          var qq = esc(x.q), ww = esc(String(x.why || ''));
          return { id: 'ai' + stamp + '_' + i, tag: x.tag, ai: true, q: { en: qq, es: qq }, o: o, why: { en: ww, es: ww } };
        })
      };
      aiBusy = false; save(); render();
      var el = document.getElementById('aibox'); if (el) el.scrollIntoView({ block: 'start' });
    }).catch(function () { aiBusy = false; aiError = true; render(); });
  }

  // ------------------------------------------------------------------ rendering
  function pct(r, w) { return r + w ? Math.round(100 * r / (r + w)) : 0; }
  function modeName(m) { return t({ exam: 'mExam', all: 'mAll', drill: 'mDrill', ai: 'mAi' }[m] || 'mDrill'); }

  function renderHome() {
    var ts = tagStats(), R = 0, W = 0, seen = 0;
    TAG_ORDER.forEach(function (g) { R += ts[g].r; W += ts[g].w; seen += ts[g].seen; });
    var errs = openErrors(), h = '';
    h += '<div class="tiles">' +
      '<div class="tile"><div class="v">' + (R + W) + '</div><div class="k">' + t('answered') + '</div></div>' +
      '<div class="tile"><div class="v">' + (R + W ? pct(R, W) + ' %' : '–') + '</div><div class="k">' + t('accuracy') + '</div></div>' +
      '<div class="tile"><div class="v">' + errs.length + '</div><div class="k">' + t('open') + '</div></div>' +
      '<div class="tile"><div class="v">' + seen + ' / ' + BANK.length + '</div><div class="k">' + t('seen') + '</div></div></div>';
    h += '<div class="actions">';
    if (S.cur) h += '<button class="btn primary" data-act="resume">' + t('resume') + ' (' + (S.cur.idx + 1) + '/' + S.cur.ids.length + ')</button>';
    h += '<button class="btn ' + (S.cur ? '' : 'primary') + '" data-act="exam">' + t('exam') + '</button>' +
      '<button class="btn" data-act="all">' + t('all') + '</button>' +
      '<button class="btn" data-act="mistakes"' + (errs.length ? '' : ' disabled') + '>' + t('mistakes') + (errs.length ? ' (' + errs.length + ')' : '') + '</button></div>';
    h += '<p class="note">' + t('examNote') + '</p>';

    // by section
    h += '<div class="sub">' + t('bySection') + '</div>';
    TAG_ORDER.forEach(function (g) {
      var s = ts[g], n = s.r + s.w, p = pct(s.r, s.w), st = tagStatus(s);
      h += '<div class="trow"><div>' + sectionLink(g, esc(L(TAGS[g]))) + '</div>' +
        '<div class="meter"><span class="' + (p < 60 ? 'low' : p < 80 ? 'mid' : '') + '" style="width:' + (n ? p : 0) + '%"></span></div>' +
        '<div class="num">' + (n ? s.r + '/' + n : '–') + '</div>' +
        '<div class="chip ' + st + '">' + t({ 'new': 'sNew', weak: 'sWeak', mid: 'sMid', ok: 'sOk' }[st]) + '</div></div>';
    });

    // analysis + task
    h += '<div class="sub">' + t('analysis') + '</div>';
    if (!(R + W)) h += '<p class="note">' + t('noData') + '</p>';
    else {
      var w = weakTags(3);
      if (w.fromErrors) {
        h += '<ul>';
        w.tags.forEach(function (g) {
          var s = ts[g];
          h += '<li><b>' + esc(L(TAGS[g])) + '</b>: ' + s.open + ' ' + t('open') + ', ' + pct(s.r, s.w) + ' % ' + t('accuracy') + '. <span class="note">' + esc(TAGS[g].trap[lang() === 'es' ? 1 : 0]) + '</span></li>';
        });
        h += '</ul>';
      } else h += '<p class="note">' + t('taskNone') + '</p>';
    }
    h += '<div class="actions"><button class="btn primary" data-act="task">' + t(S.task ? 'regen' : 'genTask') + '</button>';
    if (sampleFn) h += '<button class="btn" data-act="ai"' + (aiBusy ? ' disabled' : '') + '>' + t(aiBusy ? 'aiBusy' : 'ai') + '</button>';
    h += '</div>';
    if (aiError) h += '<p class="note">' + t('aiFail') + '</p>';
    if (S.task) h += renderTask();
    if (S.ai && S.ai.questions && S.ai.questions.length) {
      h += '<div class="task" id="aibox"><div class="sub" style="margin-top:0">' + t('aiCoach') + '</div><p class="coach">' + esc(S.ai.coach) + '</p>' +
        '<p class="note">' + t('aiNote') + '</p><button class="btn primary" data-act="airun">' + t('aiStart') + ' (' + S.ai.questions.length + ')</button></div>';
    }

    // mistakes
    h += '<div class="sub">' + t('myErr') + (errs.length ? ' (' + errs.length + ')' : '') + '</div>';
    if (!errs.length) h += '<p class="note">' + t('noErr') + '</p>';
    errs.forEach(function (id) {
      var q = getQ(id), st = S.stats[id];
      h += '<div class="err"><div class="q">' + L(q.q) + '</div>' +
        (q.o[st.pick] ? '<div class="you">' + t('you') + ': ' + L(q.o[st.pick]) + '</div>' : '') +
        '<div class="right">' + t('right') + ': ' + L(q.o[0]) + '</div><div>' + L(q.why) + '</div>' +
        '<div class="meta">' + st.w + ' ' + t('times') + ' · ' + sectionLink(q.tag, t('review') + ' ' + TAGS[q.tag].sec) + '</div></div>';
    });

    // history
    if (S.sessions.length) {
      h += '<div class="sub">' + t('history') + '</div>';
      S.sessions.slice(0, 6).forEach(function (s) {
        var d = new Date(s.t);
        h += '<div class="trow" style="grid-template-columns:minmax(0,1fr) 90px 70px"><div>' + modeName(s.mode) + '</div><div class="num">' +
          d.toLocaleDateString(lang() === 'es' ? 'es-ES' : 'en-GB', { day: 'numeric', month: 'short' }) + '</div><div class="num">' + s.good + '/' + s.total + '</div></div>';
      });
    }
    if (R + W) h += '<div class="actions" style="margin-top:18px"><button class="btn ghost" data-act="reset">' + t(resetArmed ? 'reset2' : 'reset') + '</button></div>';
    h += '<p class="note">' + t('xferHome') + '</p>';
    return h;
  }

  function renderTask() {
    var k = S.task, li = lang() === 'es' ? 1 : 0;
    var h = '<div class="task" id="task"><div class="sub" style="margin-top:0">' + t('taskTitle') + '</div>';
    if (!k.fromErrors) h += '<p class="note">' + t('taskNone') + '</p>';
    k.tags.forEach(function (g, i) {
      var T = TAGS[g];
      h += '<h4>' + (i + 1) + '. ' + esc(L(T)) + '</h4><ul>' +
        '<li><b>' + t('step1') + ':</b> ' + sectionLink(g, t('section') + ' ' + T.sec) + '</li>' +
        '<li><b>' + t('step2') + ':</b><ul>' + T.recap.map(function (r) { return '<li>' + esc(r[li]) + '</li>'; }).join('') + '</ul></li>' +
        '<li><b>' + t('why') + ':</b> ' + esc(T.trap[li]) + '</li></ul>';
    });
    h += '<h4>' + (k.tags.length + 1) + '. ' + t('step3') + '</h4><p>' + k.ids.length + ' ' + t('drillGoal') + '</p>' +
      '<button class="btn primary" data-act="drill">' + t('drillStart') + '</button></div>';
    return h;
  }

  function renderRun() {
    var c = S.cur, id = c.ids[c.idx], q = getQ(id);
    if (!q) { c.ids.splice(c.idx, 1); if (c.idx >= c.ids.length) { finish(); return ''; } return renderRun(); }
    if (!c.order[id]) { c.order[id] = shuffle([0, 1, 2]); }
    var ord = c.order[id];
    var h = '<div class="qcard"><div class="prog"><span>' + modeName(c.mode) + ' · ' + t('q') + ' ' + (c.idx + 1) + ' ' + t('of') + ' ' + c.ids.length + '</span>' +
      '<div class="meter"><span style="width:' + Math.round(100 * c.idx / c.ids.length) + '%"></span></div></div>' +
      '<div class="qtext">' + L(q.q) + '</div><div class="opts">';
    ord.forEach(function (oi, pos) {
      var cls = 'opt';
      if (answeredNow) { if (oi === 0) cls += ' right'; else if (oi === answeredNow.pick) cls += ' wrong'; }
      h += '<button class="' + cls + '" data-pick="' + oi + '"' + (answeredNow ? ' disabled' : '') + '><b>' + 'ABC'[pos] + '</b><span>' + L(q.o[oi]) + '</span></button>';
    });
    h += '</div>';
    if (answeredNow) {
      h += '<div class="fb ' + (answeredNow.ok ? 'ok' : 'no') + '"><span class="v">' + t(answeredNow.ok ? 'ok' : 'no') + '</span> ' + L(q.why) +
        ' <span class="note">' + sectionLink(q.tag, t('review') + ' ' + TAGS[q.tag].sec) + '</span></div>';
      h += '<div class="actions"><button class="btn primary" data-act="next" id="nextbtn">' + t(c.idx + 1 >= c.ids.length ? 'finish' : 'next') + '</button>';
    } else h += '<div class="actions">';
    h += '<button class="btn ghost" data-act="quit">' + t('quit') + '</button></div></div>';
    return h;
  }

  function renderResult() {
    var r = lastResult, bad = r.total - r.good, h = '<div class="result"><div class="sub" style="margin-top:0">' + t('result') + ' · ' + modeName(r.mode) + '</div>';
    h += '<div class="big">' + r.good + ' / ' + r.total + '</div>';
    if (r.mode === 'exam' && r.total === EXAM_N) h += '<p class="' + (bad <= EXAM_MAX_ERR ? 'pass' : 'fail') + '"><b>' + t(bad <= EXAM_MAX_ERR ? 'passed' : 'failed') + '</b> · ' + bad + ' ' + t('errors') + '</p>';
    else h += '<p>' + bad + ' ' + t('errors') + '</p>';
    h += '<div class="actions">';
    if (r.wrong.length) h += '<button class="btn primary" data-act="retry">' + t('retryWrong') + ' (' + r.wrong.length + ')</button>';
    h += '<button class="btn" data-act="task">' + t('genTask') + '</button><button class="btn" data-act="home">' + t('back') + '</button></div>';
    r.wrong.forEach(function (id) {
      var q = getQ(id), st = S.stats[id]; if (!q || !st) return;
      h += '<div class="err"><div class="q">' + L(q.q) + '</div>' + (q.o[st.pick] ? '<div class="you">' + t('you') + ': ' + L(q.o[st.pick]) + '</div>' : '') +
        '<div class="right">' + t('right') + ': ' + L(q.o[0]) + '</div><div>' + L(q.why) + '</div></div>';
    });
    return h + '</div>';
  }

  function render() {
    var desk = document.getElementById('desk'); if (!desk) return;
    if (view === 'run' && !S.cur) view = 'home';
    if (view === 'result' && !lastResult) view = 'home';
    desk.innerHTML = view === 'run' ? renderRun() : view === 'result' ? renderResult() : renderHome();
    var nb = document.getElementById('nextbtn'); if (nb) nb.focus({ preventScroll: true });
  }
  function toDesk() { var el = document.getElementById('tests'); if (el) el.scrollIntoView({ block: 'start' }); }

  // ------------------------------------------------------------------ prefs
  function currentSection() {
    var hs = document.querySelectorAll('.lang-' + lang() + ' h2[id]'), best = null;
    for (var i = 0; i < hs.length; i++) { if (hs[i].getBoundingClientRect().top < 120) best = hs[i]; }
    return best ? best.id.split('-')[1] : null;
  }
  // Switching language swaps the whole article, so jump to the same section in the other language.
  DGT.beforeLang = function (lg) {
    var testsTop = document.getElementById('tests').getBoundingClientRect().top;
    var sec = testsTop < 200 ? null : currentSection();
    return function () { if (sec) { var el = document.getElementById(lg + '-' + sec); if (el) el.scrollIntoView({ block: 'start', behavior: 'auto' }); } };
  };

  // ------------------------------------------------------------------ events
  document.addEventListener('click', function (ev) {
    var el = ev.target.closest('[data-go],[data-act],[data-pick]');
    if (!el) return;
    if (el.hasAttribute('data-go')) {
      ev.preventDefault();
      var target = el.getAttribute('data-go') === 'tests' ? document.getElementById('tests') : document.getElementById(lang() + '-' + el.getAttribute('data-go'));
      if (target) target.scrollIntoView({ block: 'start' });
      return;
    }
    if (el.hasAttribute('data-pick')) return answer(Number(el.getAttribute('data-pick')));
    var act = el.getAttribute('data-act');
    if (act !== 'reset') resetArmed = false;
    if (act === 'exam') start('exam', shuffle(BANK.map(function (q) { return q.id; })).slice(0, EXAM_N));
    else if (act === 'all') start('all', BANK.map(function (q) { return q.id; }));
    else if (act === 'mistakes') start('drill', openErrors().filter(function (id) { return QMAP[id]; }));
    else if (act === 'retry') start('drill', lastResult.wrong.filter(function (id) { return getQ(id); }));
    else if (act === 'drill') start('drill', (S.task ? S.task.ids : []).filter(function (id) { return QMAP[id]; }));
    else if (act === 'airun') start('ai', S.ai.questions.map(function (q) { return q.id; }));
    else if (act === 'resume') { view = 'run'; answeredNow = null; render(); toDesk(); }
    else if (act === 'next') next();
    else if (act === 'quit') { view = 'home'; answeredNow = null; if (S.cur && S.cur.log.length === S.cur.idx + 1) S.cur.idx++; if (S.cur && S.cur.idx >= S.cur.ids.length) finish(); else { save(); render(); } }
    else if (act === 'home') { view = 'home'; render(); }
    else if (act === 'task') { view = 'home'; makeTask(); }
    else if (act === 'ai') askClaude();
    else if (act === 'reset') {
      if (!resetArmed) { resetArmed = true; render(); }
      else { S = DGT.freshTopic(); resetArmed = false; lastResult = null; save(); DGT.flush(); render(); }
    }
  });

  // ------------------------------------------------------------------ boot
  DGT.setLast(TOPIC);
  DGT.start([TOPIC]);
  render();
  if (window.claude && typeof window.claude.use === 'function') {
    window.claude.use('sample').then(function (s) { if (s) { sampleFn = s; if (view === 'home') render(); } }).catch(function () {});
  }
  window.__dgt = { state: function () { return S; } };
})();
