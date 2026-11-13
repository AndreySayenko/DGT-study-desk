#!/usr/bin/env node
// Local server for DGT Study Desk: serves the pages. Progress is not kept here: the pages save it in the
// browser (localStorage) and move it between devices with Export / Import on the main screen.
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
// plus anything starting with a dot; progress/ is where earlier versions saved progress
const NOT_SERVED = new Set(['progress', 'node_modules']);

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
    console.log('Progress is saved in the browser; Export / Import on the main screen moves it to another device.');
    console.log('Press Ctrl+C to stop.');
  });
});
