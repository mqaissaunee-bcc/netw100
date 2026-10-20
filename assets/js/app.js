/* NETW 100 Explore IT & Cyber Careers — shared site script.
   Everything a student does is saved in this browser only (localStorage).
   No network requests, no inline handlers, CSP-safe. */
(function () {
  'use strict';

  /* ================= Storage ================= */
  var KEY = 'netw100-v1';
  var S = load();
  ['r', 'a', 'done', 'tot', 'prefs'].forEach(function (k) { if (!S[k] || typeof S[k] !== 'object') S[k] = {}; });

  function load() {
    try { var v = JSON.parse(localStorage.getItem(KEY)); return (v && typeof v === 'object') ? v : {}; }
    catch (e) { return {}; }
  }
  var statusEl = null, statusTimer = null;
  function persist(silent) {
    var ok = true;
    try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) { ok = false; }
    if (statusEl && (!silent || !ok)) {
      statusEl.textContent = ok ? 'Saved in this browser' : 'Not saved: storage is blocked';
      clearTimeout(statusTimer);
      statusTimer = setTimeout(function () { statusEl.textContent = ''; }, 2500);
    }
  }
  function rget(k) { return S.r[k] == null ? '' : S.r[k]; }
  function rset(k, v) { S.r[k] = v; persist(); }
  function aget(id) { return S.a[id]; }
  function aset(id, v) { S.a[id] = v; persist(); }

  /* ================= Helpers ================= */
  function el(tag, attrs, kids) {
    var n = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      var v = attrs[k];
      if (v == null || v === false) return;
      if (k === 'text') n.textContent = v;
      else if (k === 'html') n.innerHTML = v; /* only used for trusted course content from spec JSON */
      else n.setAttribute(k, v === true ? '' : v);
    });
    (kids || []).forEach(function (c) { if (c != null) n.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    return n;
  }
  function svg(tag, attrs) {
    var n = document.createElementNS('http://www.w3.org/2000/svg', tag);
    Object.keys(attrs || {}).forEach(function (k) { n.setAttribute(k, attrs[k]); });
    return n;
  }
  function shuffle(a) {
    a = a.slice();
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }
  function words(s) { s = (s || '').trim(); return s ? s.split(/\s+/).length : 0; }
  function page() { return document.body.getAttribute('data-page') || ''; }
  function money(n) { return '$' + Math.round(n).toLocaleString('en-US'); }
  function today() { return new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' }); }

  /* ================= Top bar ================= */
  function initTopbar() {
    statusEl = document.getElementById('save-status');
    var navBtn = document.getElementById('nav-toggle'), nav = document.getElementById('site-nav');
    if (navBtn && nav) navBtn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      navBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    var themeBtn = document.getElementById('theme-btn');
    function showTheme() { if (themeBtn) themeBtn.textContent = 'Theme: ' + (S.prefs.theme || 'auto'); }
    showTheme();
    if (themeBtn) themeBtn.addEventListener('click', function () {
      var order = ['auto', 'light', 'dark'];
      var next = order[(order.indexOf(S.prefs.theme || 'auto') + 1) % 3];
      S.prefs.theme = next;
      if (next === 'auto') document.documentElement.removeAttribute('data-theme');
      else document.documentElement.setAttribute('data-theme', next);
      persist(); showTheme();
    });
    function setFs(d) {
      var fs = Math.min(150, Math.max(85, (S.prefs.fs || 100) + d));
      S.prefs.fs = fs; document.documentElement.style.fontSize = fs + '%'; persist();
    }
    var sm = document.getElementById('text-smaller'), lg = document.getElementById('text-larger');
    if (sm) sm.addEventListener('click', function () { setFs(-10); });
    if (lg) lg.addEventListener('click', function () { setFs(10); });
    if (/^w\d\d$/.test(page())) { S.last = page(); persist(true); }
  }

  /* ================= Saved fields ================= */
  function initFields(scope) {
    (scope || document).querySelectorAll('[data-key]').forEach(function (f) {
      var k = f.getAttribute('data-key');
      if (f.type === 'checkbox') {
        f.checked = rget(k) === true;
        f.addEventListener('change', function () { rset(k, f.checked); syncSame(k, f); });
        return;
      }
      f.value = rget(k);
      var counter = null, range = f.getAttribute('data-words');
      if (range) {
        counter = el('p', { class: 'wc', 'aria-live': 'polite' });
        f.insertAdjacentElement('afterend', counter);
      }
      function count() {
        if (!counter) return;
        var n = words(f.value), p = range.split('-'), lo = +p[0], hi = +p[1];
        counter.textContent = n + ' words (target ' + lo + '–' + hi + ')' + (n < lo ? '' : n > hi ? ', a bit over' : ', in range');
        counter.classList.toggle('in-range', n >= lo && n <= hi);
      }
      count();
      var t = null;
      f.addEventListener('input', function () {
        count(); clearTimeout(t);
        t = setTimeout(function () { rset(k, f.value); syncSame(k, f); }, 350);
      });
      f.addEventListener('change', function () { rset(k, f.value); });
    });
  }
  function syncSame(k, src) {
    document.querySelectorAll('[data-key="' + k + '"]').forEach(function (o) {
      if (o === src) return;
      if (o.type === 'checkbox') o.checked = src.checked; else o.value = src.value;
    });
  }

  /* ================= Section completion ================= */
  function initDone() {
    var p = page(); if (!/^w\d\d$/.test(p)) return;
    var btns = document.querySelectorAll('.mark-done');
    S.tot[p] = btns.length; persist(true);
    var d = S.done[p] || (S.done[p] = {});
    function paint() {
      btns.forEach(function (b) {
        var sec = b.getAttribute('data-sec'), on = !!d[sec];
        b.setAttribute('aria-pressed', on ? 'true' : 'false');
        b.textContent = on ? 'Done ✓ (select to undo)' : 'Mark this part done';
        var st = document.querySelector('.stations li[data-sec="' + sec + '"]');
        if (st) st.classList.toggle('is-done', on);
      });
    }
    btns.forEach(function (b) {
      b.addEventListener('click', function () {
        var sec = b.getAttribute('data-sec'); d[sec] = !d[sec]; persist(); paint();
      });
    });
    paint();
  }

  /* ================= Components ================= */
  var registry = [];
  var C = {};

  function mockCard(card) {
    var box = el('div', { class: 'mock ' + (card.kind || 'email') });
    var head = el('div', { class: 'mock-head' });
    (card.head || []).forEach(function (pair) {
      head.appendChild(el('div', null, [el('b', { text: pair[0] }), ' ' + pair[1]]));
    });
    box.appendChild(head);
    var body = el('div', { class: 'mock-body' });
    String(card.body || '').split(/(\[\[[^\]]+\]\])/).forEach(function (part) {
      if (/^\[\[/.test(part)) body.appendChild(el('span', { class: 'fake-link', text: part.slice(2, -2) }));
      else body.appendChild(document.createTextNode(part));
    });
    box.appendChild(body);
    return box;
  }

  /* ---- Sort cards into buckets ---- */
  C.sort = function (root, spec, id, title) {
    var st = aget(id) || { place: {}, checked: false };
    var selected = null;
    var help = el('p', { class: 'small muted', text: 'Select a card, then select the group it belongs in. You can also drag cards with a mouse.' });
    var pool = el('div', { class: 'sort-pool', 'aria-label': 'Cards still to sort' });
    var wrap = el('div', { class: 'buckets' });
    var status = el('p', { class: 'act-status', 'aria-live': 'polite' });
    var whyBox = el('div', { 'aria-live': 'polite' });
    var lists = {};
    var chips = spec.items.map(function (it, i) {
      var c = el('button', { type: 'button', class: 'chip', 'aria-pressed': 'false', draggable: 'true' }, [it.t]);
      c.addEventListener('click', function () {
        selected = (selected === i) ? null : i;
        chips.forEach(function (o, j) { o.setAttribute('aria-pressed', j === selected ? 'true' : 'false'); });
        status.textContent = selected === null ? '' : 'Selected: “' + it.t + '”. Now choose a group.';
      });
      c.addEventListener('dragstart', function (e) { e.dataTransfer.setData('text/plain', String(i)); selected = i; });
      return c;
    });
    spec.buckets.forEach(function (b) {
      var btn = el('button', { type: 'button', class: 'bucket-btn' }, [b.label, el('span', { class: 'hint', text: b.hint || 'Place the selected card here' })]);
      var list = el('ul', { class: 'bucket-list', 'aria-label': b.label });
      var box = el('div', { class: 'bucket' }, [btn, list]);
      lists[b.id] = list;
      function drop(i) {
        st.place[i] = b.id; st.checked = false; selected = null; aset(id, st); render();
        status.textContent = '“' + spec.items[i].t + '” placed in ' + b.label + '.';
      }
      btn.addEventListener('click', function () {
        if (selected === null) { status.textContent = 'Select a card first.'; return; }
        drop(selected);
      });
      box.addEventListener('dragover', function (e) { e.preventDefault(); box.classList.add('drag-over'); });
      box.addEventListener('dragleave', function () { box.classList.remove('drag-over'); });
      box.addEventListener('drop', function (e) { e.preventDefault(); box.classList.remove('drag-over'); var i = +e.dataTransfer.getData('text/plain'); if (!isNaN(i)) drop(i); });
      wrap.appendChild(box);
    });
    function bucketLabel(bid) { var f = spec.buckets.filter(function (b) { return b.id === bid; })[0]; return f ? f.label : ''; }
    function render() {
      Object.keys(lists).forEach(function (k) { lists[k].textContent = ''; });
      chips.forEach(function (c, i) {
        c.setAttribute('aria-pressed', 'false'); c.classList.remove('is-right', 'is-wrong');
        var v = c.querySelector('.verdict'); if (v) v.remove();
        var p = st.place[i];
        if (p && lists[p]) { lists[p].appendChild(el('li', null, [c])); } else pool.appendChild(c);
        if (st.checked && p) {
          var right = p === spec.items[i].b;
          c.classList.add(right ? 'is-right' : 'is-wrong');
          c.insertBefore(el('span', { class: 'verdict', text: right ? '✓ ' : '✗ ' }), c.firstChild);
        }
      });
      whyBox.textContent = '';
      if (st.checked) {
        var placed = 0, correct = 0, misses = [];
        spec.items.forEach(function (it, i) {
          if (st.place[i]) { placed++; if (st.place[i] === it.b) correct++; else misses.push(it); }
        });
        status.textContent = correct + ' of ' + spec.items.length + ' correct' + (placed < spec.items.length ? ' (' + (spec.items.length - placed) + ' not placed yet)' : '') + '.';
        status.classList.toggle('good', correct === spec.items.length);
        misses.forEach(function (it) {
          whyBox.appendChild(el('p', { class: 'fb no' }, [el('b', { class: 'mark-no', text: '✗ ' }), '“' + it.t + '” belongs in ' + bucketLabel(it.b) + '. ' + (it.why || '')]));
        });
        if (correct === spec.items.length && spec.done) whyBox.appendChild(el('p', { class: 'fb ok', text: spec.done }));
      } else status.classList.remove('good');
    }
    var check = el('button', { type: 'button', class: 'btn btn-primary btn-small', text: 'Check my sort' });
    var reset = el('button', { type: 'button', class: 'btn btn-small', text: 'Start over' });
    check.addEventListener('click', function () { st.checked = true; aset(id, st); render(); });
    reset.addEventListener('click', function () { st = { place: {}, checked: false }; aset(id, st); render(); status.textContent = 'Cleared. All cards are back in the pile.'; });
    root.append(help, pool, wrap, el('div', { class: 'btn-row' }, [check, reset]), status, whyBox);
    render();
    return {
      title: title, summary: function () {
        var placed = Object.keys(st.place).length;
        if (!placed) return [{ q: title, a: '' }];
        var correct = spec.items.filter(function (it, i) { return st.place[i] === it.b; }).length;
        return [{ q: title, a: 'Placed ' + placed + ' of ' + spec.items.length + ' cards; ' + correct + ' correct when last checked.' }];
      }
    };
  };

  /* ---- Multiple choice: quizzes, scenarios, inbox, ticket triage ---- */
  C.choices = function (root, spec, id, title) {
    var st = aget(id) || { ans: {}, best: null };
    var scored = spec.scored !== false;
    var label = spec.label || 'Question';
    var qWrap = el('div');
    var scoreLine = el('p', { class: 'score-line', 'aria-live': 'polite' });
    var orders = spec.items.map(function (it) {
      var idx = it.options.map(function (_, j) { return j; });
      return (spec.shuffle && !it.fixed) ? shuffle(idx) : idx;
    });
    var itemEls = [];
    spec.items.forEach(function (it, i) {
      var q = el('div', { class: 'q' });
      q.appendChild(el('p', { class: 'q-num', text: label + ' ' + (i + 1) + ' of ' + spec.items.length }));
      if (it.card) q.appendChild(mockCard(it.card));
      var pid = id + '-q' + i;
      q.appendChild(el('p', { class: 'q-prompt', id: pid, text: it.q }));
      var opts = el('div', { class: 'opts', role: 'group', 'aria-labelledby': pid });
      var fb = el('div', { 'aria-live': 'polite' });
      var btns = orders[i].map(function (j) {
        var b = el('button', { type: 'button', class: 'opt', text: it.options[j].t });
        b.addEventListener('click', function () { st.ans[i] = j; aset(id, st); paintItem(i); paintScore(); });
        opts.appendChild(b);
        return { b: b, j: j };
      });
      q.append(opts, fb);
      qWrap.appendChild(q);
      itemEls.push({ btns: btns, fb: fb });
    });
    function paintItem(i) {
      var it = spec.items[i], e = itemEls[i], a = st.ans[i];
      e.fb.textContent = '';
      e.btns.forEach(function (o) {
        o.b.className = 'opt'; o.b.disabled = a != null;
        if (a == null) return;
        var ok = !!it.options[o.j].ok;
        if (o.j === a) o.b.classList.add(ok ? 'picked-ok' : 'picked-no');
        else if (ok && scored) o.b.classList.add('reveal-ok');
      });
      if (a == null) return;
      var opt = it.options[a], ok = !!opt.ok;
      var head = ok ? (spec.okLabel || 'Correct.') : (spec.noLabel || 'Not quite.');
      var p = el('p', { class: 'fb ' + (ok ? 'ok' : 'no') }, [el('b', { class: ok ? 'mark-ok' : 'mark-no', text: (ok ? '✓ ' : '✗ ') + head + ' ' }), (opt.fb ? opt.fb + ' ' : '') + (it.explain || '')]);
      e.fb.appendChild(p);
    }
    function counts() {
      var n = 0, c = 0;
      spec.items.forEach(function (it, i) { if (st.ans[i] != null) { n++; if (it.options[st.ans[i]].ok) c++; } });
      return { n: n, c: c };
    }
    function paintScore() {
      var k = counts(), total = spec.items.length;
      if (!scored) { scoreLine.textContent = k.n + ' of ' + total + ' worked through.'; return; }
      if (k.n === total && (st.best == null || k.c > st.best)) { st.best = k.c; aset(id, st); }
      scoreLine.textContent = k.c + ' correct out of ' + k.n + ' answered (' + total + ' total).' + (st.best != null ? ' Best complete score: ' + st.best + '/' + total + '.' : '');
    }
    var reset = el('button', { type: 'button', class: 'btn btn-small', text: scored ? 'Retake' : 'Start over' });
    reset.addEventListener('click', function () { st.ans = {}; aset(id, st); spec.items.forEach(function (_, i) { paintItem(i); }); paintScore(); scoreLine.textContent = 'Cleared. Answer again.'; });
    root.append(qWrap, scoreLine, el('div', { class: 'btn-row' }, [reset]));
    spec.items.forEach(function (_, i) { paintItem(i); });
    paintScore();
    return {
      title: title, summary: function () {
        var k = counts();
        if (!k.n) return [{ q: title, a: '' }];
        var lines = spec.items.map(function (it, i) {
          var a = st.ans[i]; if (a == null) return (i + 1) + '. (not answered)';
          return (i + 1) + '. ' + it.options[a].t + (scored ? (it.options[a].ok ? '  [correct]' : '  [incorrect]') : '');
        });
        var head = scored ? ('Score: ' + k.c + '/' + spec.items.length + (st.best != null ? ' (best complete: ' + st.best + ')' : '')) : (k.n + ' of ' + spec.items.length + ' completed');
        return [{ q: title, a: head + '\n' + lines.join('\n') }];
      }
    };
  };

  /* ---- Flip cards ---- */
  C.flip = function (root, spec, id, title) {
    var grid = el('div', { class: 'flips' });
    var labels = spec.labels || ['Front', 'Back'];
    spec.cards.forEach(function (c) {
      var face = el('span', { class: 'face', text: c.f });
      var side = el('span', { class: 'side-label', text: labels[0] });
      var b = el('button', { type: 'button', class: 'flip', 'aria-pressed': 'false' }, [side, face, el('span', { class: 'small muted', text: 'Select to flip' })]);
      b.addEventListener('click', function () {
        var on = b.getAttribute('aria-pressed') !== 'true';
        b.setAttribute('aria-pressed', on ? 'true' : 'false');
        face.textContent = on ? c.b : c.f; side.textContent = on ? labels[1] : labels[0];
      });
      grid.appendChild(b);
    });
    root.appendChild(grid);
    return { title: title, summary: function () { return []; } };
  };

  /* ---- Diagram stepper ---- */
  C.diagram = function (root, spec, id, title) {
    var W = spec.w || 760, H = spec.h || 300, step = 0;
    var s = svg('svg', { viewBox: '0 0 ' + W + ' ' + H, class: 'diagram', role: 'img', 'aria-label': spec.alt || title });
    var nodeEls = {}, linkEls = [];
    var pos = {};
    spec.nodes.forEach(function (n) { pos[n.id] = n; });
    spec.links.forEach(function (l) {
      var a = pos[l[0]], b = pos[l[1]];
      var line = svg('line', { x1: a.x, y1: a.y, x2: b.x, y2: b.y, class: 'link' });
      s.appendChild(line); linkEls.push(line);
    });
    spec.nodes.forEach(function (n) {
      var w = n.w || 128, h = 56, g = svg('g', { class: 'node' });
      g.appendChild(svg('rect', { x: n.x - w / 2, y: n.y - h / 2, width: w, height: h, rx: 8 }));
      var t = svg('text', { x: n.x, y: n.y - (n.sub ? 3 : -5), 'text-anchor': 'middle' }); t.textContent = n.label; g.appendChild(t);
      if (n.sub) { var t2 = svg('text', { x: n.x, y: n.y + 15, 'text-anchor': 'middle', class: 'sub' }); t2.textContent = n.sub; g.appendChild(t2); }
      s.appendChild(g); nodeEls[n.id] = g;
    });
    var panelH = el('h4'), panelP = el('p'), count = el('p', { class: 'step-count' });
    var panel = el('div', { class: 'step-panel', 'aria-live': 'polite' }, [count, panelH, panelP]);
    var prev = el('button', { type: 'button', class: 'btn btn-small', text: 'Previous step' });
    var next = el('button', { type: 'button', class: 'btn btn-primary btn-small', text: 'Next step' });
    function paint() {
      var cur = spec.steps[step];
      Object.keys(nodeEls).forEach(function (k) { nodeEls[k].classList.toggle('on', (cur.on || []).indexOf(k) > -1); });
      linkEls.forEach(function (l, i) { l.classList.toggle('on', (cur.links || []).indexOf(i) > -1); });
      count.textContent = 'Step ' + (step + 1) + ' of ' + spec.steps.length;
      panelH.textContent = cur.title; panelP.textContent = cur.text;
      prev.disabled = step === 0; next.disabled = step === spec.steps.length - 1;
      if (step === spec.steps.length - 1) { var a = aget(id) || {}; if (!a.seen) { a.seen = true; aset(id, a); } }
    }
    prev.addEventListener('click', function () { if (step > 0) { step--; paint(); } });
    next.addEventListener('click', function () { if (step < spec.steps.length - 1) { step++; paint(); } });
    root.append(s, panel, el('div', { class: 'btn-row' }, [prev, next]));
    paint();
    return { title: title, summary: function () { return [{ q: title, a: (aget(id) || {}).seen ? 'Walked through all ' + spec.steps.length + ' steps.' : '' }]; } };
  };

  /* ---- Interest survey ---- */
  C.survey = function (root, spec, id, title) {
    var st = aget(id) || { ans: {}, res: null };
    var scale = spec.scale || ['Not me', 'A little', 'Somewhat', 'Mostly', 'Very me'];
    var form = el('div');
    spec.items.forEach(function (it, i) {
      var fs = el('fieldset', { class: 'likert' }, [el('legend', { text: (i + 1) + '. ' + it.t })]);
      var row = el('div', { class: 'scale' });
      scale.forEach(function (lab, v) {
        var inp = el('input', { type: 'radio', name: id + '-' + i, value: String(v + 1) });
        if (st.ans[i] === v + 1) inp.checked = true;
        inp.addEventListener('change', function () { st.ans[i] = v + 1; aset(id, st); });
        row.appendChild(el('label', null, [inp, el('span', { text: lab })]));
      });
      fs.appendChild(row); form.appendChild(fs);
    });
    var out = el('div', { 'aria-live': 'polite' });
    var go = el('button', { type: 'button', class: 'btn btn-primary', text: 'Show my results' });
    function compute() {
      var sum = {}, n = {};
      spec.cats.forEach(function (c) { sum[c.id] = 0; n[c.id] = 0; });
      spec.items.forEach(function (it, i) {
        if (!st.ans[i]) return;
        it.c.forEach(function (cid) { sum[cid] += st.ans[i]; n[cid]++; });
      });
      return spec.cats.map(function (c) { return { id: c.id, label: c.label, desc: c.desc, score: n[c.id] ? sum[c.id] / n[c.id] : 0 }; })
        .sort(function (a, b) { return b.score - a.score; });
    }
    function show() {
      out.textContent = '';
      if (!st.res) return;
      var answered = Object.keys(st.ans).length;
      out.appendChild(el('p', { class: 'act-status', text: 'Based on ' + answered + ' of ' + spec.items.length + ' statements. Higher bars mean a stronger match.' }));
      var bars = el('div', { class: 'bars' });
      st.res.forEach(function (r) {
        var pct = Math.round((r.score / 5) * 100);
        bars.appendChild(el('div', { class: 'bar-row' }, [el('span', { text: r.label }),
          el('div', { class: 'bar-track' }, [el('div', { class: 'bar-fill', style: 'width:' + pct + '%' })]), el('span', { class: 'bar-val', text: r.score.toFixed(1) + ' / 5' })]));
      });
      out.appendChild(bars);
      st.res.slice(0, 2).forEach(function (r, k) {
        out.appendChild(el('p', { class: 'fb info' }, [el('b', { text: (k === 0 ? 'Strongest match: ' : 'Runner-up: ') + r.label + '. ' }), r.desc]));
      });
    }
    go.addEventListener('click', function () {
      if (!Object.keys(st.ans).length) { out.textContent = 'Answer at least a few statements first.'; return; }
      st.res = compute(); aset(id, st); show();
    });
    root.append(form, el('div', { class: 'btn-row' }, [go]), out);
    show();
    return {
      title: title, summary: function () {
        if (!st.res) return [{ q: title, a: '' }];
        return [{ q: title, a: st.res.map(function (r, i) { return (i + 1) + '. ' + r.label + ' (' + r.score.toFixed(1) + '/5)'; }).join('\n') }];
      }
    };
  };

  /* ---- Labor market compare ---- */
  C.compare = function (root, spec, id, title) {
    var st = aget(id) || { rows: [] };
    var out = el('div');
    var form = el('div', { class: 'cols cols-3' });
    function inputField(lbl, type, ph) {
      var fid = id + '-' + lbl.replace(/\W+/g, '').toLowerCase();
      var inp = el('input', { type: type, id: fid, placeholder: ph || '' });
      if (type === 'number') inp.setAttribute('step', 'any');
      form.appendChild(el('div', { class: 'field' }, [el('label', { for: fid, text: lbl }), inp]));
      return inp;
    }
    var fName = inputField('Occupation or job title', 'text', 'e.g. Computer network architects');
    var fPay = inputField('Median pay ($ per year)', 'number', 'e.g. 130390');
    var fGrow = inputField('Projected growth (%)', 'number', 'e.g. 12');
    var fSrc = el('input', { type: 'text', id: id + '-src', placeholder: 'e.g. BLS OOH, NJ OEWS, a job posting' });
    var add = el('button', { type: 'button', class: 'btn btn-primary btn-small', text: 'Add to chart' });
    var msg = el('p', { class: 'act-status', 'aria-live': 'polite' });
    add.addEventListener('click', function () {
      var name = fName.value.trim(), pay = parseFloat(fPay.value), g = fGrow.value === '' ? null : parseFloat(fGrow.value);
      if (!name || isNaN(pay)) { msg.textContent = 'Enter at least an occupation name and a median pay number.'; return; }
      st.rows.push({ name: name, pay: pay, growth: g, src: fSrc.value.trim() || 'my research' });
      aset(id, st); fName.value = fPay.value = fGrow.value = fSrc.value = '';
      msg.textContent = 'Added ' + name + '.'; draw();
    });
    function draw() {
      out.textContent = '';
      var rows = spec.rows.map(function (r) { return Object.assign({ preset: true }, r); }).concat(st.rows);
      var maxPay = Math.max.apply(null, rows.map(function (r) { return r.pay; }).concat([1]));
      out.appendChild(el('h4', { text: 'Median annual pay' }));
      var b1 = el('div', { class: 'bars' });
      rows.forEach(function (r) {
        b1.appendChild(el('div', { class: 'bar-row' }, [el('span', { text: r.name + (r.preset ? '' : ' (yours)') }),
          el('div', { class: 'bar-track' }, [el('div', { class: 'bar-fill', style: 'width:' + (r.pay / maxPay * 100) + '%' })]), el('span', { class: 'bar-val', text: money(r.pay) })]));
      });
      out.appendChild(b1);
      out.appendChild(el('h4', { text: spec.growthLabel || 'Projected employment change' }));
      var gr = rows.filter(function (r) { return r.growth != null && !isNaN(r.growth); });
      var mx = Math.max.apply(null, gr.map(function (r) { return Math.abs(r.growth); }).concat([5]));
      var b2 = el('div', { class: 'bars' });
      gr.forEach(function (r) {
        var half = 50, w = Math.abs(r.growth) / mx * 50;
        var fill = el('div', { class: 'bar-fill' + (r.growth < 0 ? ' neg' : ''), style: (r.growth < 0 ? 'right:' + half + '%;' : 'left:' + half + '%;') + 'width:' + w + '%' });
        b2.appendChild(el('div', { class: 'bar-row' }, [el('span', { text: r.name }),
          el('div', { class: 'bar-track diverge' }, [el('div', { class: 'zero', style: 'left:50%' }), fill]), el('span', { class: 'bar-val', text: (r.growth > 0 ? '+' : '') + r.growth + '%' + (r.growth < 0 ? ' (decline)' : '') })]));
      });
      out.appendChild(b2);
      out.appendChild(el('p', { class: 'source', text: spec.note || '' }));
      if (st.rows.length) {
        var list = el('ul');
        st.rows.forEach(function (r, i) {
          var del = el('button', { type: 'button', class: 'btn btn-small', text: 'Remove' });
          del.addEventListener('click', function () { st.rows.splice(i, 1); aset(id, st); draw(); msg.textContent = 'Removed ' + r.name + '.'; });
          list.appendChild(el('li', null, [r.name + ': ' + money(r.pay) + (r.growth != null ? ', ' + r.growth + '%' : '') + ' (source: ' + r.src + ') ', del]));
        });
        out.append(el('h4', { text: 'Rows you added' }), list);
      }
    }
    root.append(form, el('div', { class: 'field' }, [el('label', { for: id + '-src', text: 'Where did this number come from?' }), fSrc]),
      el('div', { class: 'btn-row' }, [add]), msg, out);
    draw();
    return {
      title: title, summary: function () {
        return [{ q: title + ' (rows I added)', a: st.rows.map(function (r) { return r.name + ': ' + money(r.pay) + (r.growth != null ? ', growth ' + r.growth + '%' : '') + ' (source: ' + r.src + ')'; }).join('\n') }];
      }
    };
  };

  /* ---- Pathway interest ratings ---- */
  C.rating = function (root, spec, id, title) {
    var st = aget(id) || { r: {}, n: {} };
    spec.groups.forEach(function (g) {
      var grp = el('div', { class: 'rate-group' }, [el('h4', { text: g.label })]);
      g.roles.forEach(function (r) {
        var rid = id + '-' + r.id;
        var out = el('output', { for: rid, text: st.r[r.id] ? String(st.r[r.id]) : 'not rated' });
        var rng = el('input', { type: 'range', id: rid, min: '0', max: '5', step: '1', value: String(st.r[r.id] || 0), 'aria-describedby': rid + '-d' });
        rng.addEventListener('input', function () {
          var v = +rng.value; st.r[r.id] = v; out.textContent = v ? String(v) : 'not rated'; aset(id, st);
        });
        var note = el('input', { type: 'text', id: rid + '-n', placeholder: 'Your note: why this rating?', value: st.n[r.id] || '' });
        note.addEventListener('input', function () { st.n[r.id] = note.value; aset(id, st); });
        grp.appendChild(el('div', { class: 'rate-row' }, [
          el('div', null, [el('span', { class: 'rname', text: r.name }), r.d ? el('span', { class: 'help small muted', id: rid + '-d', text: ' ' + r.d }) : null]),
          el('div', null, [el('label', { for: rid, class: 'small', text: 'Interest 0–5: ' }), out, rng]),
          el('div', null, [el('label', { for: rid + '-n', class: 'visually-hidden', text: 'Note for ' + r.name }), note])
        ]));
      });
      root.appendChild(grp);
    });
    return {
      title: title, summary: function () {
        var lines = [];
        spec.groups.forEach(function (g) {
          g.roles.forEach(function (r) {
            if (st.r[r.id] || st.n[r.id]) lines.push(g.label + ', ' + r.name + ': ' + (st.r[r.id] ? st.r[r.id] + '/5' : 'not rated') + (st.n[r.id] ? ' — ' + st.n[r.id] : ''));
          });
        });
        return [{ q: title, a: lines.join('\n') }];
      }
    };
  };

  /* ---- Roadmap builder ---- */
  C.roadmap = function (root, spec, id, title) {
    var st = aget(id) || { sel: {}, custom: [] };
    var H = spec.horizon || 18;
    function monthSelect(val, lbl) {
      var s = el('select', { 'aria-label': lbl });
      for (var m = 0; m <= H; m++) {
        var o = el('option', { value: String(m), text: m === 0 ? 'This semester' : 'Month ' + m });
        if (m === val) o.selected = true;
        s.appendChild(o);
      }
      return s;
    }
    var opts = el('div', { class: 'rm-options' });
    var groups = {};
    spec.options.forEach(function (o) {
      if (!groups[o.type]) { groups[o.type] = el('div'); opts.appendChild(el('h4', { text: spec.typeLabels[o.type] || o.type })); opts.appendChild(groups[o.type]); }
      var cid = id + '-' + o.id;
      var cb = el('input', { type: 'checkbox', id: cid });
      var ms = monthSelect(st.sel[o.id] != null ? st.sel[o.id] : (o.m || 0), 'When for ' + o.label);
      cb.checked = st.sel[o.id] != null; ms.disabled = !cb.checked;
      cb.addEventListener('change', function () { if (cb.checked) st.sel[o.id] = +ms.value; else delete st.sel[o.id]; ms.disabled = !cb.checked; aset(id, st); draw(); });
      ms.addEventListener('change', function () { st.sel[o.id] = +ms.value; aset(id, st); draw(); });
      groups[o.type].appendChild(el('div', { class: 'rm-opt' }, [cb, el('label', { for: cid }, [o.label, o.note ? el('span', { class: 'rm-type', text: ' ' + o.note }) : null]), ms]));
    });
    var cText = el('input', { type: 'text', id: id + '-ct', placeholder: 'e.g. Volunteer at a CTF, apply for a help desk internship' });
    var cMonth = monthSelect(3, 'When for your own item');
    var cAdd = el('button', { type: 'button', class: 'btn btn-small', text: 'Add to roadmap' });
    cAdd.addEventListener('click', function () {
      var t = cText.value.trim(); if (!t) return;
      st.custom.push({ label: t, m: +cMonth.value }); cText.value = ''; aset(id, st); draw();
    });
    var addRow = el('div', { class: 'rm-add' }, [el('div', { class: 'field', style: 'margin:0' }, [el('label', { for: id + '-ct', text: 'Add your own step' }), cText]), cMonth, cAdd]);
    var tl = el('ol', { class: 'timeline', 'aria-live': 'polite' });
    function items() {
      var list = [];
      spec.options.forEach(function (o) { if (st.sel[o.id] != null) list.push({ label: o.label, m: st.sel[o.id] }); });
      st.custom.forEach(function (c, i) { list.push({ label: c.label, m: c.m, ci: i }); });
      return list.sort(function (a, b) { return a.m - b.m; });
    }
    function draw() {
      tl.textContent = '';
      var list = items();
      if (!list.length) { tl.appendChild(el('li', { class: 'empty', text: 'Your timeline is empty. Check off courses, certifications, and experiences above and pick when.' })); return; }
      var byM = {};
      list.forEach(function (it) { (byM[it.m] = byM[it.m] || []).push(it); });
      Object.keys(byM).map(Number).sort(function (a, b) { return a - b; }).forEach(function (m) {
        var ul = el('ul');
        byM[m].forEach(function (it) {
          var li = el('li', null, [it.label + ' ']);
          if (it.ci != null) {
            var del = el('button', { type: 'button', class: 'btn btn-small', text: 'Remove' });
            del.addEventListener('click', function () { st.custom.splice(it.ci, 1); aset(id, st); draw(); });
            li.appendChild(del);
          }
          ul.appendChild(li);
        });
        tl.appendChild(el('li', null, [el('span', { class: 'when', text: m === 0 ? 'This semester' : 'Month ' + m }), ul]));
      });
    }
    root.append(opts, addRow, el('h4', { text: 'Your ' + H + '-month roadmap' }), tl);
    draw();
    return {
      title: title, summary: function () {
        return [{ q: title, a: items().map(function (it) { return (it.m === 0 ? 'This semester' : 'Month ' + it.m) + ': ' + it.label; }).join('\n') }];
      }
    };
  };

  /* ---- Countdown timer ---- */
  C.timer = function (root, spec, id, title) {
    var total = spec.seconds || 60, left = total, running = false, endAt = 0, iv = null, said = {};
    var face = el('p', { class: 'timer-face', 'aria-hidden': 'true' });
    var bar = el('div'); var track = el('div', { class: 'timer-bar', role: 'progressbar', 'aria-valuemin': '0', 'aria-valuemax': String(total), 'aria-label': 'Time used' }, [bar]);
    var live = el('p', { class: 'act-status', 'aria-live': 'assertive' });
    var start = el('button', { type: 'button', class: 'btn btn-primary', text: 'Start' });
    var reset = el('button', { type: 'button', class: 'btn', text: 'Reset' });
    function fmt(s) { s = Math.max(0, Math.ceil(s)); return Math.floor(s / 60) + ':' + ('0' + (s % 60)).slice(-2); }
    function paint() {
      face.textContent = fmt(left);
      bar.style.width = ((total - left) / total * 100) + '%';
      track.setAttribute('aria-valuenow', String(Math.round(total - left)));
    }
    function tick() {
      left = (endAt - Date.now()) / 1000;
      if (left <= total / 2 && !said.half) { said.half = 1; live.textContent = 'Halfway.'; }
      if (left <= 10 && !said.ten) { said.ten = 1; live.textContent = 'Ten seconds left. Land your ask.'; }
      if (left <= 0) { left = 0; stop(); live.textContent = 'Time. How did it feel? Note one thing to tighten.'; }
      paint();
    }
    function stop() { running = false; clearInterval(iv); start.textContent = left > 0 && left < total ? 'Resume' : 'Start'; }
    start.addEventListener('click', function () {
      if (running) { stop(); live.textContent = 'Paused.'; return; }
      if (left <= 0) { left = total; said = {}; }
      running = true; endAt = Date.now() + left * 1000; iv = setInterval(tick, 200);
      start.textContent = 'Pause'; live.textContent = 'Go.';
    });
    reset.addEventListener('click', function () { stop(); left = total; said = {}; live.textContent = 'Reset to ' + fmt(total) + '.'; start.textContent = 'Start'; paint(); });
    root.append(face, track, el('div', { class: 'btn-row' }, [start, reset]), live);
    paint();
    return { title: title, summary: function () { return []; } };
  };

  function initComponents(scope) {
    (scope || document).querySelectorAll('.act[data-type]').forEach(function (box) {
      var type = box.getAttribute('data-type'), id = box.getAttribute('data-id');
      var specEl = box.querySelector('script.spec'), body = box.querySelector('.act-body');
      if (!C[type] || !specEl || !body) return;
      var spec;
      try { spec = JSON.parse(specEl.textContent); } catch (e) { body.textContent = 'This activity could not load.'; return; }
      var h = box.querySelector('h3');
      var api = C[type](body, spec, id, h ? h.textContent : id);
      registry.push({ el: box, api: api });
    });
  }

  /* ================= PDF export (print to PDF) ================= */
  function apiFor(box) { for (var i = 0; i < registry.length; i++) if (registry[i].el === box) return registry[i].api; return null; }
  function labelFor(field) {
    var l = field.querySelector('label, .label');
    if (!l) return '';
    var c = l.cloneNode(true);
    c.querySelectorAll('.help').forEach(function (h) { h.remove(); });
    return c.textContent.trim();
  }
  function collect(scope) {
    var out = [];
    scope.querySelectorAll('.field, .check-list, .act[data-type]').forEach(function (n) {
      if (n.closest('.no-export')) return;
      if (n.classList.contains('field')) {
        if (n.closest('.act[data-type]')) return;
        var c = n.querySelector('[data-key]'); if (!c) return;
        if (c.type === 'checkbox') return;
        out.push({ q: labelFor(n), a: c.value || '' });
      } else if (n.classList.contains('check-list')) {
        var lines = [];
        n.querySelectorAll('input[type="checkbox"][data-key]').forEach(function (cb) {
          var lab = cb.closest('label'); lines.push((cb.checked ? '[x] ' : '[ ] ') + (lab ? lab.textContent.trim() : ''));
        });
        if (lines.length) out.push({ q: n.getAttribute('data-title') || 'Checklist', a: lines.join('\n') });
      } else {
        var api = apiFor(n); if (api) api.summary().forEach(function (s) { out.push(s); });
      }
    });
    return out;
  }
  function exportPDF(docTitle, sections) {
    var root = document.getElementById('print-root');
    if (!root) { root = el('div', { id: 'print-root' }); document.body.appendChild(root); }
    root.textContent = '';
    var name = rget('profile-name') || '(add your name before saving)';
    root.appendChild(el('h1', { text: docTitle }));
    root.appendChild(el('p', { class: 'pmeta', text: name + ' | NETW 100 Explore IT & Cyber Careers, Brookdale Community College | ' + today() }));
    sections.forEach(function (sec) {
      if (!sec.items.length) return;
      root.appendChild(el('h2', { text: sec.h }));
      sec.items.forEach(function (it) {
        var b = el('div', { class: 'pblock' });
        if (it.q) b.appendChild(el('h3', { text: it.q }));
        b.appendChild(it.a ? el('div', { class: 'pans', text: it.a }) : el('p', { class: 'pempty', text: 'No response yet.' }));
        root.appendChild(b);
      });
    });
    var oldTitle = document.title;
    document.title = docTitle.replace(/[^\w\- ]+/g, '').replace(/\s+/g, '_');
    document.body.classList.add('print-mode');
    function done() { document.body.classList.remove('print-mode'); document.title = oldTitle; window.removeEventListener('afterprint', done); }
    window.addEventListener('afterprint', done);
    window.print();
    setTimeout(function () { if (document.body.classList.contains('print-mode')) done(); }, 1500);
  }
  function initExport() {
    document.querySelectorAll('[data-export]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        if (!rget('profile-name')) {
          var nm = document.querySelector('[data-key="profile-name"]');
          if (nm) { nm.focus(); var msg = document.getElementById('export-msg'); if (msg) msg.textContent = 'Add your name first so your instructor knows whose work this is.'; return; }
        }
        var scopeSel = btn.getAttribute('data-export');
        var title = btn.getAttribute('data-export-title') || document.title;
        var secs = [];
        document.querySelectorAll(scopeSel).forEach(function (sec) {
          var h = sec.getAttribute('data-export-h') || (sec.querySelector('h2') || {}).textContent || '';
          secs.push({ h: h.trim(), items: collect(sec) });
        });
        exportPDF(title, secs);
      });
    });
  }

  /* ================= Home page progress ================= */
  var PF = [
    { n: 1, t: 'Professional bio', keys: ['pf-bio'] },
    { n: 2, t: 'Two NICE work role analyses', keys: ['pf-r1-role', 'pf-r1-tasks', 'pf-r2-role', 'pf-r2-tasks'] },
    { n: 3, t: 'Annotated CyberSeek pathway', act: 'pf-pathway' },
    { n: 4, t: 'Education and certification roadmap', act: 'pf-roadmap', keys: ['pf-roadmap-why'] },
    { n: 5, t: 'Resume or LinkedIn draft', keys: ['pf-headline', 'pf-about', 'pf-bullets'] },
    { n: 6, t: 'Final reflection', keys: ['pf-reflection'] }
  ];
  function pfStatus(sec) {
    var have = 0, need = 0;
    (sec.keys || []).forEach(function (k) { need++; if (String(rget(k)).trim()) have++; });
    if (sec.act) {
      need++;
      var a = aget(sec.act);
      if (a && ((a.r && Object.keys(a.r).some(function (k) { return a.r[k] > 0; })) || (a.sel && Object.keys(a.sel).length) || (a.custom && a.custom.length))) have++;
    }
    if (sec.n === 6) { var w = words(rget('pf-reflection')); return w >= 400 ? 'Drafted' : w ? 'In progress (' + w + ' words)' : 'Not started'; }
    return have === 0 ? 'Not started' : have < need ? 'In progress' : 'Drafted';
  }
  function weekTouched(p) {
    var pre = p + '-';
    return Object.keys(S.r).some(function (k) { return k.indexOf(pre) === 0 && String(S.r[k]).trim() && S.r[k] !== false; }) ||
      Object.keys(S.a).some(function (k) { return k.indexOf(pre) === 0; }) ||
      (S.done[p] && Object.keys(S.done[p]).some(function (k) { return S.done[p][k]; }));
  }
  function initHome() {
    document.querySelectorAll('.rm-st[data-week]').forEach(function (g) {
      var p = g.getAttribute('data-week'), d = S.done[p] || {}, tot = S.tot[p] || 0;
      var n = Object.keys(d).filter(function (k) { return d[k]; }).length;
      var a = g.querySelector('a');
      var state = (tot && n >= tot) ? 'done' : weekTouched(p) ? 'partial' : '';
      if (state) g.classList.add(state);
      if (a) a.setAttribute('aria-label', a.getAttribute('aria-label') + (state === 'done' ? ', complete' : state === 'partial' ? ', in progress' : ''));
    });
    var pf = document.getElementById('pf-progress');
    if (pf) PF.forEach(function (sec) {
      var s = pfStatus(sec);
      pf.appendChild(el('li', null, [el('span', { class: 'st' + (s === 'Drafted' ? ' ok' : ''), text: s }), '§' + sec.n + ' ' + sec.t]));
    });
    var cont = document.getElementById('continue');
    if (cont && S.last) {
      var n = parseInt(S.last.slice(1), 10);
      cont.setAttribute('href', 'weeks/week-' + ('0' + n).slice(-2) + '.html');
      cont.textContent = 'Continue with Week ' + n;
    }
  }
  function initPortfolioStatus() {
    document.querySelectorAll('[data-pf-status]').forEach(function (n) {
      var sec = PF[+n.getAttribute('data-pf-status') - 1];
      function paint() { n.textContent = 'Status: ' + pfStatus(sec); }
      paint(); document.addEventListener('input', function () { setTimeout(paint, 400); });
    });
  }

  /* ================= My work: backup, restore, delete ================= */
  function initMyWork() {
    var tbody = document.getElementById('mw-rows');
    if (tbody) {
      for (var w = 1; w <= 15; w++) {
        var p = 'w' + ('0' + w).slice(-2), d = S.done[p] || {}, tot = S.tot[p] || 0;
        var n = Object.keys(d).filter(function (k) { return d[k]; }).length;
        var resp = Object.keys(S.r).filter(function (k) { return k.indexOf(p + '-') === 0 && String(S.r[k]).trim() && S.r[k] !== false; }).length;
        var acts = Object.keys(S.a).filter(function (k) { return k.indexOf(p + '-') === 0; }).length;
        tbody.appendChild(el('tr', null, [el('td', null, [el('a', { href: 'weeks/week-' + ('0' + w).slice(-2) + '.html', text: 'Week ' + w })]),
          el('td', { text: tot ? n + ' of ' + tot : (n ? String(n) : 'Not opened') }), el('td', { text: String(resp) }), el('td', { text: String(acts) })]));
      }
    }
    var dl = document.getElementById('mw-backup');
    if (dl) dl.addEventListener('click', function () {
      var blob = new Blob([JSON.stringify({ app: 'netw100', v: 1, saved: new Date().toISOString(), data: S }, null, 1)], { type: 'application/json' });
      var a = el('a', { href: URL.createObjectURL(blob), download: 'netw100-backup-' + new Date().toISOString().slice(0, 10) + '.json' });
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 2000);
      msg('Backup downloaded. Keep it somewhere safe such as OneDrive.');
    });
    var file = document.getElementById('mw-file'), restore = document.getElementById('mw-restore');
    if (restore && file) restore.addEventListener('click', function () {
      var f = file.files && file.files[0];
      if (!f) { msg('Choose a backup file first.'); return; }
      var rd = new FileReader();
      rd.onload = function () {
        try {
          var j = JSON.parse(rd.result); var data = j && j.app === 'netw100' ? j.data : null;
          if (!data) throw new Error('bad');
          var mode = (document.querySelector('input[name="mw-mode"]:checked') || {}).value || 'merge';
          if (mode === 'replace') S = data;
          else ['r', 'a', 'done', 'tot', 'prefs'].forEach(function (k) { S[k] = Object.assign({}, S[k] || {}, data[k] || {}); });
          ['r', 'a', 'done', 'tot', 'prefs'].forEach(function (k) { if (!S[k]) S[k] = {}; });
          persist(); msg('Restored. Reloading so every page shows your work.');
          setTimeout(function () { location.reload(); }, 900);
        } catch (e) { msg('That file is not a NETW 100 backup. Choose the .json file this page downloaded.'); }
      };
      rd.readAsText(f);
    });
    var del = document.getElementById('mw-delete'), del2 = document.getElementById('mw-delete-confirm');
    if (del && del2) {
      del.addEventListener('click', function () { del2.hidden = false; del2.focus(); msg('Select “Yes, delete everything” to confirm. This cannot be undone.'); });
      del2.addEventListener('click', function () { try { localStorage.removeItem(KEY); } catch (e) {} msg('All NETW 100 data deleted from this browser.'); setTimeout(function () { location.reload(); }, 900); });
    }
    function msg(t) { var m = document.getElementById('mw-msg'); if (m) m.textContent = t; }
  }

  /* ================= Glossary filter ================= */
  function initGlossary() {
    var f = document.getElementById('gloss-filter'); if (!f) return;
    var pairs = [];
    document.querySelectorAll('dl.gloss dt').forEach(function (dt) { pairs.push([dt, dt.nextElementSibling]); });
    var count = document.getElementById('gloss-count');
    f.addEventListener('input', function () {
      var q = f.value.trim().toLowerCase(), shown = 0;
      pairs.forEach(function (p) {
        var hit = !q || (p[0].textContent + ' ' + p[1].textContent).toLowerCase().indexOf(q) > -1;
        p[0].hidden = p[1].hidden = !hit; if (hit) shown++;
      });
      if (count) count.textContent = shown + ' of ' + pairs.length + ' terms shown';
    });
  }

  /* ================= Start ================= */
  initTopbar();
  initFields();
  initComponents();
  initDone();
  initExport();
  initHome();
  initPortfolioStatus();
  initMyWork();
  initGlossary();
})();
