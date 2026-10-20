"""Helpers and templates for the NETW 100 site generator."""
import html, json

VERIFIED = "October 2026"

UNITS = {
    1: ("Unit 1", "Career landscape and IT foundations", "Weeks 1–4"),
    2: ("Unit 2", "Career roles deep dive", "Weeks 5–8"),
    3: ("Unit 3", "Career readiness and professional development", "Weeks 9–12"),
    4: ("Unit 4", "Future trends and portfolio presentations", "Weeks 13–15"),
}

NAV = [("index.html", "Weeks", "home"), ("schedule.html", "Schedule", "schedule"),
       ("portfolio.html", "Portfolio", "portfolio"), ("resources.html", "Resources", "resources"),
       ("glossary.html", "Glossary", "glossary"), ("my-work.html", "My work", "mywork")]

EXT_ICON = ('<svg class="ext-icon" viewBox="0 0 12 12" aria-hidden="true" focusable="false">'
            '<path d="M4.5 2H2v8h8V7.5M7 1.5h3.5V5M10.3 1.7 5.5 6.5" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>')

LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true" focusable="false">'
        '<path d="M4 24 C10 24 10 8 16 8 S22 24 28 24" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round"/>'
        '<circle cx="4" cy="24" r="3.4" fill="currentColor"/><circle cx="16" cy="8" r="3.4" fill="currentColor"/>'
        '<circle cx="28" cy="24" r="3.4" fill="currentColor"/></svg>')

def esc(s):
    return html.escape(s, quote=True)

def ext(url, text):
    return (f'<a href="{esc(url)}" target="_blank" rel="noopener">{text}{EXT_ICON}'
            f'<span class="visually-hidden"> (opens in a new tab)</span></a>')

def res(label, url, desc=""):
    d = f'<span class="rdesc">{desc}</span>' if desc else ""
    return f"<li>{ext(url, label)}{d}</li>"

def res_list(items):
    return '<ul class="res-list">' + "".join(res(*i) for i in items) + "</ul>"

def field(key, label, help=None, kind="textarea", words=None, rows=5, placeholder=""):
    fid = "f-" + key
    h = f'<span class="help">{help}</span>' if help else ""
    w = f' data-words="{words}"' if words else ""
    ph = f' placeholder="{esc(placeholder)}"' if placeholder else ""
    if kind == "textarea":
        ctl = f'<textarea id="{fid}" data-key="{key}" rows="{rows}"{w}{ph}></textarea>'
    else:
        ctl = f'<input type="{kind}" id="{fid}" data-key="{key}"{ph}>'
    return f'<div class="field"><label for="{fid}">{label}{h}</label>{ctl}</div>'

def checks(title, items):
    lis = "".join(f'<li><label><input type="checkbox" data-key="{k}"> <span>{t}</span></label></li>' for k, t in items)
    return f'<ul class="check-list" data-title="{esc(title)}">{lis}</ul>'

def act(kind, aid, title, intro, spec, tag="Activity"):
    data = json.dumps(spec, ensure_ascii=False).replace("</", "<\\/")
    return (f'<section class="act" id="act-{aid}" data-type="{kind}" data-id="{aid}" aria-labelledby="act-{aid}-h">'
            f'<span class="act-tag">{tag}</span><h3 id="act-{aid}-h">{title}</h3>'
            f'<p class="act-intro">{intro}</p><script type="application/json" class="spec">{data}</script>'
            f'<div class="act-body"></div></section>')

def callout(title, body, note=False):
    cls = "callout note" if note else "callout"
    return f'<div class="{cls}"><p class="callout-title">{title}</p>{body}</div>'

def stats(items):
    return '<div class="stat-row">' + "".join(f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a, b in items) + "</div>"

def roles(cards):
    return '<div class="roles-grid">' + "".join(f'<article class="role-card"><h4>{t}</h4>{b}</article>' for t, b in cards) + "</div>"

def job_cards(prefix, n, label="Job posting"):
    out = ['<div class="job-cards">']
    for i in range(1, n + 1):
        p = f"{prefix}-job{i}"
        out.append(f'<div class="job-card"><h4>{label} {i}</h4>'
                   + field(f"{p}-title", f"{label} {i}: job title and employer", kind="text")
                   + field(f"{p}-url", f"{label} {i}: link", kind="url", placeholder="https://")
                   + field(f"{p}-where", f"{label} {i}: location, remote or on-site, pay if listed", kind="text")
                   + field(f"{p}-req", f"{label} {i}: required skills, education, and certifications", rows=3)
                   + "</div>")
    out.append("</div>")
    return "".join(out)

def name_field():
    return field("profile-name", "Your name (printed at the top of every PDF)", kind="text")

def export_btn(scope, title, label):
    return (f'<div class="btn-row"><button type="button" class="btn btn-primary" data-export="{scope}" '
            f'data-export-title="{esc(title)}">{label}</button></div>'
            '<p class="small muted" id="export-msg" aria-live="polite">Your browser’s print window opens. Choose “Save as PDF” as the printer, then upload the PDF to Canvas.</p>')

def shell(title, desc, page_id, depth, main, current, body_class="unit-1"):
    cur = ' aria-current="page"'
    nav = "".join(
        f'<li><a href="{depth}{href}"{cur if key == current else ""}>{label}</a></li>'
        for href, label, key in NAV)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | NETW 100 Explore IT &amp; Cyber Careers</title>
<meta name="description" content="{esc(desc)}">
<link rel="stylesheet" href="{depth}assets/css/site.css">
<script src="{depth}assets/js/theme-init.js"></script>
</head>
<body class="{body_class}" data-page="{page_id}">
<a href="#main" class="skip-link">Skip to main content</a>
<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="{depth}index.html">{LOGO}<span>NETW 100 <span class="brand-sub">Explore IT &amp; Cyber Careers</span></span></a>
    <button type="button" class="nav-toggle" id="nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="site-nav" id="site-nav" aria-label="Site"><ul>{nav}</ul></nav>
    <div class="tools">
      <span class="save-status" id="save-status" aria-live="polite"></span>
      <button type="button" id="text-smaller" aria-label="Decrease text size">A−</button>
      <button type="button" id="text-larger" aria-label="Increase text size">A+</button>
      <button type="button" id="theme-btn">Theme: auto</button>
    </div>
  </div>
</header>
<main id="main" class="page">
{main}
</main>
<footer class="site-foot">
  <p>Built for NETW 100 Explore IT &amp; Cyber Careers, Brookdale Community College, 2026. Original open educational resource.</p>
  <p>Your answers are saved only in this browser on this device. Links were last checked {VERIFIED}; salary and job data change, so always check the live source.</p>
</footer>
<div id="print-root"></div>
<script src="{depth}assets/js/app.js"></script>
</body>
</html>
"""

SECTION_NAMES = [("explore", "Explore"), ("do", "Do"), ("investigate", "Investigate"), ("portfolio", "Portfolio"), ("wrap", "Wrap-up")]

def week_page(w, weeks_meta):
    n = w["n"]; nn = f"{n:02d}"; pid = f"w{nn}"
    u = w["unit"]; ulabel, uname, _ = UNITS[u]
    secs = [s for s in SECTION_NAMES if s[0] != "portfolio" or w.get("portfolio")]
    stations = "".join(
        f'<li data-sec="{k}"><a href="#{k}"><span class="dot" aria-hidden="true"></span>{lab}</a></li>' for k, lab in secs)
    due = "".join(f'<li class="due">Due: {d}</li>' for d in w.get("due", []))
    objs = "".join(f'<li>{t} <span class="clo">(CLO {c})</span></li>' for t, c in w["objectives"])

    def section(key, label, inner, intro=""):
        return (f'<section class="wk-section" id="{key}" data-export-h="{label}: {esc(w["title"])}">'
                f'<h2><span class="sec-dot" aria-hidden="true"></span>{label}</h2>{intro}{inner}'
                f'<div class="section-footer"><button type="button" class="btn btn-small mark-done" data-sec="{key}" aria-pressed="false">Mark this part done</button></div></section>')

    inv = w["investigate"]
    inv_html = (f'<div class="assign"><span class="act-tag">{inv["tag"]}</span><h3>{inv["title"]}</h3>'
                f'<div class="prose">{inv["intro"]}</div>'
                f'<h4>Resources</h4>{res_list(inv["resources"])}'
                f'<h4>What to do</h4><ol class="steps">{"".join(f"<li>{s}</li>" for s in inv["steps"])}</ol>'
                f'{inv["fields"]}'
                + (f'<p class="grade-note">{inv["grade"]}</p>' if inv.get("grade") else "")
                + (export_btn("#investigate", f"NETW 100 {inv['tag']}: {inv['title']}", f"Save this {inv.get('short', 'assignment')} as PDF") if inv.get("submit") else "")
                + "</div>")

    body = [section("explore", "Explore", w["explore"]),
            section("do", "Do", "".join(w["do"]), '<p class="prose muted">In-class activities. Your answers save as you go.</p>'),
            section("investigate", "Investigate", inv_html)]
    if w.get("portfolio"):
        body.append(section("portfolio", "Portfolio", w["portfolio"] +
                            '<p><a class="btn btn-small" href="../portfolio.html">Open the full portfolio</a></p>'))
    wrap_inner = (w.get("wrap", "") +
                  '<h3>Exit ticket</h3>' +
                  field(f"{pid}-exit-1", "One thing I learned or want to remember from this week", rows=3) +
                  field(f"{pid}-exit-2", "One question I still have", rows=2) +
                  '<h3>Save this week’s work</h3><p class="prose">Saves every answer on this page, including activities, as one PDF.</p>' +
                  name_field() +
                  export_btn(".wk-section", f"NETW 100 Week {n}: {w['title']}", f"Save Week {n} as PDF"))
    body.append(section("wrap", "Wrap-up", wrap_inner))

    instr = ""
    if w.get("instructor"):
        rows = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in w["instructor"])
        instr = (f'<details class="instructor"><summary>Instructor notes: a 50-minute run of this session</summary>'
                 f'<div class="table-wrap"><table><thead><tr><th scope="col">Time</th><th scope="col">What happens</th></tr></thead><tbody>{rows}</tbody></table></div>'
                 + (f'<p class="small">{w["instructor_note"]}</p>' if w.get("instructor_note") else "") + '</details>')

    prev_l = next_l = ""
    if n > 1:
        p = weeks_meta[n - 2]; prev_l = f'<a href="week-{n-1:02d}.html"><span>Previous</span>Week {n-1}: {p}</a>'
    else:
        prev_l = '<a href="../index.html"><span>Back to</span>All weeks</a>'
    if n < 15:
        q = weeks_meta[n]; next_l = f'<a href="week-{n+1:02d}.html"><span>Next</span>Week {n+1}: {q}</a>'
    else:
        next_l = '<a href="../portfolio.html"><span>Finish with</span>Your portfolio</a>'

    main = f"""<header class="week-head">
  <p class="unit-tag">{ulabel}: {uname}</p>
  <h1>Week {n}: {w['title']}</h1>
  <p class="lede">{w['lede']}</p>
  <ul class="week-meta"><li>One 50-minute session</li>{due}</ul>
</header>
<nav class="stations" aria-label="Parts of this week"><ol>{stations}</ol></nav>
<section class="objectives" aria-labelledby="obj-h"><h2 id="obj-h">By the end of this week you can</h2><ul>{objs}</ul></section>
{''.join(body)}
{instr}
<nav class="pager" aria-label="Week to week">{prev_l}{next_l}</nav>"""
    return shell(f"Week {n}: {w['title']}", w["lede"], pid, "../", main, "home", f"unit-{u}")
