#!/usr/bin/env python3
"""Builds clarify/index.html from tools/clarify_content.json. Unlisted page: noindex, no nav link, not in sitemap."""
import json, html, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
c = json.loads((root / "tools" / "clarify_content.json").read_text(encoding="utf-8"))
e = html.escape

def li(items):
    return "".join(f"<li>{e(i)}</li>" for i in items)

def idea(i):
    bullets = f"<ul class=\"tight\">{li(i['bullets'])}</ul>" if i["bullets"] else ""
    rows = "".join(f"<tr><th>{e(a)}</th><td>{e(b)}</td></tr>" for a, b in i["rows"])
    return (f"<article class=\"idea\"><h3><span class=\"num\">{i['n']}</span>{e(i['title'])}</h3>"
            f"<p>{e(i['body'])}</p>{bullets}<table class=\"rows\">{rows}</table></article>")

css = """
:root{--slate:#46605A;--slate-dk:#2F433E;--ink:#22302D;--muted:#5E6B68;--yellow:#F4C430;--yellow-soft:#FBE9A6;--bg:#F6F7F5;--card:#FFFFFF;--line:#E3E7E4}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:400 17px/1.65 Montserrat,system-ui,-apple-system,Segoe UI,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--slate);text-decoration-thickness:2px;text-underline-offset:3px}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
h1,h2,h3{font-family:Anton,Impact,"Arial Narrow",sans-serif;font-weight:400;letter-spacing:.01em;text-transform:uppercase;color:var(--slate);margin:0}
h1{font-size:clamp(3rem,9vw,6rem);line-height:.95;margin:.25em 0 .1em}
h2{font-size:clamp(1.8rem,4.5vw,2.6rem);line-height:1.05;margin-bottom:.5em}
h3{font-size:1.5rem;line-height:1.15;display:flex;align-items:center;gap:12px;margin-bottom:.5em}
p{margin:0 0 1em}
.btn{display:inline-block;font:700 .9rem Montserrat,sans-serif;padding:.5em 1.1em;border-radius:999px;text-decoration:none;border:2px solid var(--slate);color:var(--slate)}
.btn:hover{background:#fff}
.nav{background:rgba(246,247,245,.93);border-bottom:1px solid var(--line)}
.navin{display:flex;align-items:center;justify-content:space-between;padding-top:10px;padding-bottom:10px}
.brand{font:400 1.3rem Anton,Impact,sans-serif;letter-spacing:.04em;text-transform:uppercase;color:var(--slate);text-decoration:none}
.pill{display:inline-block;background:var(--yellow);color:var(--slate-dk);font:700 .8rem Montserrat,sans-serif;letter-spacing:.06em;text-transform:uppercase;padding:.45em 1.1em;border-radius:999px}
.hero{padding:36px 0 18px}
.byline{color:var(--muted);font-size:.95rem;margin:0 0 .8em}
.dl{margin:0 0 1.2em}.dl a{font:600 .9rem Montserrat,sans-serif;color:var(--slate-dk);background:var(--yellow-soft);border-radius:999px;padding:.5em 1.1em;text-decoration:none;display:inline-block}.dl a:hover{background:var(--yellow)}
.lead{max-width:760px}
section{padding:26px 0}
.two{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:20px 22px}
.card h3{font-size:1.3rem}
ul{margin:0;padding-left:1.1em}
li{margin:0 0 .55em}
.tight{margin:0 0 .9em}
.tight li{margin:0 0 .25em}
.idea{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:20px 22px;margin:0 0 18px}
.num{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:50%;background:var(--yellow);color:var(--slate-dk);font:400 1.2rem Anton,Impact,sans-serif}
.rows{width:100%;border-collapse:collapse;font-size:.92rem}
.rows th{width:150px;text-align:left;vertical-align:top;background:var(--yellow-soft);color:var(--slate-dk);font:700 .78rem Montserrat,sans-serif;letter-spacing:.05em;text-transform:uppercase;padding:8px 12px;border:1px solid var(--line)}
.rows td{padding:8px 12px;border:1px solid var(--line);vertical-align:top}
.next{font-weight:700;color:var(--slate-dk)}
.foot{color:var(--muted);font-size:.82rem;padding:10px 0 40px}
@media (max-width:760px){.two{grid-template-columns:1fr}.rows th{width:105px}}
@page{size:Letter;margin:.45in .5in}
.foot-print{display:none}
@media print{
 body{background:#fff;font-size:8.9pt;line-height:1.32}
 .ideas-sec h2{font-size:12pt;margin:2px 0 0}
 .nav,.read-sec,.see-sec,.q-sec,.foot-screen,.dl{display:none}
 .hero{padding:0 0 4px;border-bottom:3px solid var(--yellow);margin-bottom:6px}
 h1{font-size:26pt;margin:.15em 0 .05em}
 .byline{font-size:8.6pt;margin:0 0 4px}
 .lead{font-size:9.2pt;max-width:none;margin:4px 0 0}
 .wrap{max-width:none;padding:0}
 section{padding:0}
 h3{font-size:13pt;margin-bottom:3px}
 .num{width:22px;height:22px;font-size:11pt}
 .idea{border-radius:8px;padding:6px 10px;margin:0 0 5px;break-inside:avoid}
 .idea p{margin:0 0 4px}
 .tight{margin:0 0 3px;font-size:8.4pt}
 .tight li{margin:0 0 1px}
 .rows{font-size:8pt}
 .rows th{width:100px;padding:2px 7px;font-size:6.8pt}
 .rows td{padding:2px 7px}
 .next{margin:6px 0 2px;font-size:9.6pt}
 .foot-print{display:block;font-size:7.4pt;color:var(--muted);margin:0}
}
"""

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(c['title'])} | Matt Lyman</title>
<meta name="robots" content="noindex, nofollow, noarchive">
<meta name="description" content="A short read on Clarify and three ideas for its first 90 days, prepared for Patrick Thompson.">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<nav class="nav"><div class="wrap navin"><a class="brand" href="/">Matt Lyman</a><a class="btn" href="https://www.linkedin.com/in/mattlyman" rel="me noopener">LinkedIn</a></div></nav>
<header class="hero"><div class="wrap">
<span class="pill">{e(c['pill'])}</span>
<h1>{e(c['title'])}</h1>
<p class="byline">{e(c['byline'])}</p>
<p class="dl"><a href="/clarify/Three-Ideas-for-Clarify.pdf" download>Download the one-page PDF</a></p>
</div></header>
<main>
<section class="read-sec"><div class="wrap"><h2>My Read</h2><p class="lead">{e(c['read'])}</p></div></section>
<section class="see-sec"><div class="wrap"><h2>My quick read from the outside</h2>
<div class="two"><div class="card"><h3>Areas of strength</h3><ul>{li(c['strengths'])}</ul></div>
<div class="card"><h3>Areas for growth</h3><ul>{li(c['growth'])}</ul></div></div></div></section>
<section class="ideas-sec"><div class="wrap"><h2>Three Ideas for the First 90 Days</h2>
<p class="lead ideas-intro">{e(c['ideas_intro'])}</p>
{''.join(idea(i) for i in c['ideas'])}
<p class="next">{e(c['next'])}</p>
<p class="foot-print">{e(c['footnote'])}</p>
</div></section>
<section class="q-sec"><div class="wrap"><h2>What I would need to know</h2><p class="lead">{e(c['questions_intro'])}</p><ul>{li(c['questions'])}</ul></div></section>
</main>
<footer class="foot-screen"><div class="wrap foot"><p>{e(c['footnote'])}</p><p><a href="/">mattlyman.com</a> &middot; <a href="https://www.linkedin.com/in/mattlyman" rel="me noopener">LinkedIn</a></p></div></footer>
</body>
</html>
"""
out = root / "clarify" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(page, encoding="utf-8")
print("wrote", out, len(page), "bytes")
