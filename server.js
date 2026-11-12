#!/usr/bin/env node
// Local server for DGT Study Desk: serves the pages and keeps your progress for every topic in
// progress/progress.json, so it survives browser resets and works in any browser.
// No packages needed. Start it with `npm start` (or `node server.js`).
//
//   PORT=5174 npm start    use another port
//   HOST=0.0.0.0 npm start listen on the network too (default: this computer only)
'use strict';
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const PORT = Number(process.env.PORT) || 5173;
const HOSTS = process.env.HOST ? [process.env.HOST] : ['127.0.0.1', '::1'];
const DATA_DIR = path.join(ROOT, 'progress');
const DATA_FILE = path.join(DATA_DIR, 'progress.json');
const MAX_BODY = 5 * 1024 * 1024;
const NOT_SERVED = new Set(['progress', 'node_modules']); // plus anything starting with a dot

const TYPES = {
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8', '.md': 'text/plain; charset=utf-8', '.txt': 'text/plain; charset=utf-8',
  '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif',
  '.webp': 'image/webp', '.ico': 'image/x-icon', '.pdf': 'application/pdf', '.woff2': 'font/woff2'
};

function send(res, status, body, type) {
  res.writeHead(status, { 'Content-Type': type || 'text/plain; charset=utf-8', 'Cache-Control': 'no-store' });
  res.end(body);
}

// ------------------------------------------------------------------ progress API
// progress/progress.json holds every topic: {app, kind, v: 2, saved, prefs, topics: {"b-01": state, ...}}.
// It has the same format as an exported file. Pages save one topic (or the preferences) at a time, and the
// server folds that into the file, so two tabs on different topics never overwrite each other.
//
//   GET /api/progress                  the whole document
//   PUT /api/progress/topics/<id>      body {state}
//   PUT /api/progress/prefs            body {prefs}
const TOPIC_PATH = /^\/topics\/([a-z]-\d{2})$/;

function emptyDoc() { return { app: 'dgt-study-desk', kind: 'progress', v: 2, saved: null, prefs: null, topics: {} }; }
// Before topics existed the file held Topic 1 alone: {state: {..., lang, theme}}.
function upgrade(doc) {
  if (!doc || typeof doc !== 'object') return null;
  if (doc.topics && typeof doc.topics === 'object') return doc;
  if (!doc.state || doc.state.v !== 1) return null;
  const { lang, theme, ...state } = doc.state;
  return { ...emptyDoc(), saved: doc.saved || null, prefs: { lang: lang || null, theme: theme || null, updated: state.updated || 0 }, topics: { 'b-01': state } };
}
async function readDoc() {
  let text;
  try { text = await fs.promises.readFile(DATA_FILE, 'utf8'); } catch (e) {
    if (e.code === 'ENOENT') return emptyDoc();
    throw e;
  }
  let doc = null;
  try { doc = upgrade(JSON.parse(text)); } catch (e) { /* handled below */ }
  if (!doc) {
    // Leave a damaged file alone: the page keeps working on browser storage and nothing overwrites it.
    console.error('progress/progress.json is damaged. Fix it or move it away, then reload the page.');
    throw Object.assign(new Error('damaged'), { damaged: true });
  }
  return doc;
}
// Write to a temporary file and rename it over the old one, so a crash never leaves half a file.
async function writeDoc(doc) {
  doc.saved = new Date().toISOString();
  await fs.promises.mkdir(DATA_DIR, { recursive: true });
  const tmp = DATA_FILE + '.tmp';
  await fs.promises.writeFile(tmp, JSON.stringify(doc, null, 2) + '\n', 'utf8');
  await fs.promises.rename(tmp, DATA_FILE);
}

function getProgress(res) {
  readDoc().then((doc) => send(res, 200, JSON.stringify(doc), TYPES['.json']),
    (e) => send(res, 500, e.damaged ? 'The progress file is damaged' : 'Could not read the progress file'));
}

let writeQueue = Promise.resolve();
function putProgress(req, res, apply) {
  if (!/^application\/json\b/i.test(req.headers['content-type'] || '')) return send(res, 415, 'Expected JSON');
  const origin = req.headers.origin;
  if (origin) {
    let host = null;
    try { host = new URL(origin).host; } catch (e) { /* "null" or junk */ }
    if (host !== req.headers.host) return send(res, 403, 'Forbidden');
  }
  const chunks = [];
  let size = 0, tooBig = false;
  req.on('data', (c) => {
    size += c.length;
    if (size > MAX_BODY) tooBig = true; else chunks.push(c);
  });
  req.on('end', () => {
    if (tooBig) return send(res, 413, 'Too large');
    let body;
    try { body = JSON.parse(Buffer.concat(chunks).toString('utf8')); } catch (e) { return send(res, 400, 'Invalid JSON'); }
    if (!body || typeof body !== 'object') return send(res, 400, 'Invalid body');
    // Read, change and write one request at a time.
    writeQueue = writeQueue.then(async () => {
      const doc = await readDoc();
      if (!apply(doc, body)) return 400;
      await writeDoc(doc);
      return 204;
    }).then((status) => send(res, status, status === 204 ? '' : 'Not a progress update'), (e) => {
      if (!e.damaged) console.error('Could not save progress:', e.message);
      send(res, 500, 'Could not save');
    });
  });
}
function setTopic(id) {
  return (doc, body) => {
    const st = body.state;
    if (!st || typeof st !== 'object' || st.v !== 1 || !st.stats || typeof st.stats !== 'object') return false;
    doc.topics[id] = st;
    return true;
  };
}
function setPrefs(doc, body) {
  if (!body.prefs || typeof body.prefs !== 'object') return false;
  doc.prefs = body.prefs;
  return true;
}

// ------------------------------------------------------------------ static files
function serveStatic(req, res, pathname) {
  let rel;
  try { rel = decodeURIComponent(pathname); } catch (e) { return send(res, 400, 'Bad request'); }
  let file = path.join(ROOT, path.normalize(rel));
  if (file !== ROOT && !file.startsWith(ROOT + path.sep)) return send(res, 403, 'Forbidden');
  const parts = path.relative(ROOT, file).split(path.sep);
  if (parts.some((p) => p.startsWith('.')) || NOT_SERVED.has(parts[0])) return send(res, 404, 'Not found');
  fs.stat(file, (err, st) => {
    if (!err && st.isDirectory()) { file = path.join(file, 'index.html'); return fs.stat(file, done); }
    done(err, st);
  });
  function done(err, st) {
    if (err || !st.isFile()) return send(res, 404, 'Not found');
    res.writeHead(200, {
      'Content-Type': TYPES[path.extname(file).toLowerCase()] || 'application/octet-stream',
      'Content-Length': st.size,
      'Cache-Control': 'no-cache'
    });
    if (req.method === 'HEAD') return res.end();
    fs.createReadStream(file).pipe(res);
  }
}

function handle(req, res) {
  const { pathname } = new URL(req.url, 'http://localhost');
  if (pathname === '/api/progress' || pathname.startsWith('/api/progress/')) {
    const rest = pathname.slice('/api/progress'.length);
    if (rest === '' && req.method === 'GET') return getProgress(res);
    if (rest === '/prefs' && req.method === 'PUT') return putProgress(req, res, setPrefs);
    const m = TOPIC_PATH.exec(rest);
    if (m && req.method === 'PUT') return putProgress(req, res, setTopic(m[1]));
    return send(res, 404, 'Not found');
  }
  if (req.method !== 'GET' && req.method !== 'HEAD') return send(res, 405, 'Method not allowed');
  serveStatic(req, res, pathname);
}

// ------------------------------------------------------------------ start
let announced = false;
HOSTS.forEach((host, i) => {
  const server = http.createServer(handle);
  server.on('error', (e) => {
    // No IPv6 on this machine: the IPv4 address is enough.
    if (i > 0 && (e.code === 'EADDRNOTAVAIL' || e.code === 'EAFNOSUPPORT')) return;
    if (e.code === 'EADDRINUSE') {
      console.error('Port ' + PORT + ' is already in use. Is Live Server or another `npm start` running?\n' +
        'Stop it, or pick another port: PORT=5174 npm start');
    } else console.error(e.message);
    process.exit(1);
  });
  server.listen(PORT, host, () => {
    if (announced) return;
    announced = true;
    const shown = HOSTS.length > 1 ? 'localhost' : host.includes(':') ? '[' + host + ']' : host;
    console.log('Serving DGT Study Desk at http://' + shown + ':' + PORT);
    console.log('Progress is saved to ' + path.relative(process.cwd(), DATA_FILE));
    console.log('Press Ctrl+C to stop.');
  });
});
