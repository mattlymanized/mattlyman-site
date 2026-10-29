import json, html, os
OUT=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),".."))
SITE="https://mattlyman.com"
LI="https://www.linkedin.com/in/mattlyman"
e=html.escape

faq=[
("Who is Matt Lyman?","Matt Lyman is a B2B marketing leader based in Seattle with nearly 20 years in marketing, specializing in demand generation, with hands-on marketing operations and AI skills behind it. He has served as VP of Marketing at Flosum, VP of Demand Generation at LeanData, and Director of Revenue Marketing at Chef Software, where the revenue team grew about 2.7x through the company's acquisition by Progress."),
("What does Matt Lyman do?","He is a B2B marketing leader who builds demand generation programs around buyer stories and the data to prove they work. He has built demand engines across paid media, ABM, SEO, events, and content at Chef, LeanData, and Flosum, and builds with AI every day."),
("What is B2H?","Business to human is Matt's approach to B2B marketing. Every campaign starts with a real story about who the buyer is and what they're afraid of, because a person makes the decision at the end of every enterprise deal."),
("What results has Matt driven?","At LeanData, marketing's share of new business pipeline went from 18% to 50% while demand gen spend fell 41%. At Flosum, cost per paid MQL fell 87% in six months and monthly search impressions grew 1,329%."),
("What is Matt's experience with ABM and GEO/AEO?","At Flosum, Matt ran ABM across 51 named accounts and 10 AEs. Target accounts clicked at 3 to 7x the campaign average, and 7 became opportunities within five months. He also led an SEO and GEO/AEO rebuild with 120+ assets updated, rebuilt FAQs, and third-party authority placements, which took monthly search impressions from 70,000 to over one million."),
("How does Matt use AI?","Matt builds with AI every day. At Flosum he worked with product marketing on an agent that tracks competitor and industry news for Sales, built an ABM dashboard that pulls ad, intent, and site data into one view, set up an AI SDR, and rebuilt content for AI search (GEO/AEO)."),
("What roles is Matt open to?","Matt is open to VP, Head of, and Senior Director roles in marketing, demand generation, and growth at growth-stage B2B software companies."),
("What does Matt do outside of marketing?","He founded R.I.D.E. 4 ALL, a nonprofit for inclusive recreation, and is president of the Highline Special Needs PTA. He also rides bikes, a lot."),
("Where can I hear Matt talk about marketing and leadership?","Matt has been a guest on Marketers of Technology, Straight To Voicemail, Content Matters, The Hype Within, and Everything's Coming Up Marketing, and gave a Finovate talk on LeanData's revenue orchestration platform. Links to each are in the Talks and podcasts section of this page."),
("Where is Matt based and how can I reach him?","Seattle, working remotely since 2020. The best way to reach him is LinkedIn at linkedin.com/in/mattlyman."),
]


episodes=[
 {"show":"Straight To Voicemail","title":"How can teams build trust to maintain consistent brand messaging?","date":"2025-09-23","year":"2025","mins":5,
  "url":"https://podcasts.apple.com/us/podcast/how-can-teams-build-trust-to-maintain-consistent-brand/id1648953137?i=1000728017889",
  "blurb":"Why brand consistency is really about trust, and how documentation, transparent strategy, and feedback loops keep teams aligned.","type":"podcast"},
 {"show":"Marketers of Technology","title":"Welcome to the era of B2H","date":"2025-08-27","year":"2025","mins":33,
  "url":"https://podcasts.apple.com/us/podcast/welcome-to-the-era-of-b2h-w-matt-lyman/id1747223698?i=1000723724993",
  "blurb":"The B2H philosophy: even in B2B, you're selling to people, not companies.","type":"podcast"},
 {"show":"Content Matters","title":"From Ops to Strategy: The Rise of a Marketing Generalist","date":"2025-03-18","year":"2025","mins":46,
  "url":"https://podcasts.apple.com/us/podcast/from-ops-to-strategy-the-rise-of-a/id1772999666?i=1000699612652",
  "blurb":"How a path through theater, collections, and marketing ops shaped Matt's leadership, and why strong marketers understand both operations and creativity.","type":"podcast"},
 {"show":"Streamly, for Finovate","title":"Transforming CRM in financial services: LeanData's approach","date":"2024-05-21","year":"2024","mins":None,
  "url":"https://streamly.video/video/transforming-crm-in-financial-services-lean-data-s-approach",
  "blurb":"Matt on LeanData's revenue orchestration platform and what it does for data management and operational efficiency in financial services.","type":"video"},
 {"show":"The Hype Within","title":"Empathy and Inclusion: The Cornerstones of Leadership","date":"2023-06-01","year":"2023","mins":36,
  "url":"https://podcasts.apple.com/us/podcast/empathy-and-inclusion-the-cornerstones-of/id1690523496?i=1000615317173",
  "blurb":"How empathy, inclusion, and psychological safety shape the way Matt leads.","type":"podcast"},
 {"show":"Everything's Coming Up Marketing","title":"Making dad jokes with Matt Lyman","date":"2023-03-16","year":"2023","mins":47,
  "url":"https://podcasts.apple.com/us/podcast/making-dad-jokes-with-matt-lyman/id1672705227?i=1000604468650",
  "blurb":"Parenthood and full-time work, why marketing is a lot like sports, and building inclusive spaces for learning and play.","type":"podcast"},
]
eps_html="\n".join(
 f'<li><span class="show">{e(x["show"])} &middot; {x["year"]}{(" &middot; "+str(x["mins"])+" min") if x["mins"] else ""}{" &middot; video" if x["type"]=="video" else ""}</span>'
 f'<a href="{x["url"]}" rel="noopener">{e(x["title"])}</a><p>{e(x["blurb"])}</p></li>' for x in episodes)

faq_html="\n".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in faq)

jsonld={"@context":"https://schema.org","@graph":[
 {"@type":"WebSite","@id":SITE+"/#website","url":SITE+"/","name":"Matt Lyman","inLanguage":"en-US","publisher":{"@id":SITE+"/#person"}},
 {"@type":"ProfilePage","@id":SITE+"/#webpage","url":SITE+"/","name":"Matt Lyman | B2B Marketing Leader, Demand Generation","isPartOf":{"@id":SITE+"/#website"},"about":{"@id":SITE+"/#person"},"mainEntity":{"@id":SITE+"/#person"},"inLanguage":"en-US"},
 {"@type":"Person","@id":SITE+"/#person","name":"Matt Lyman","url":SITE+"/","image":SITE+"/images/matt-headshot.jpg","jobTitle":"B2B Marketing Leader","description":"B2B marketing leader with nearly 20 years in marketing, specializing in demand generation, with hands-on marketing operations and AI skills behind it. Most recently VP of Marketing at Flosum.",
  "address":{"@type":"PostalAddress","addressLocality":"Seattle","addressRegion":"WA","addressCountry":"US"},
  "sameAs":[LI,"https://www.ride4all.org"],
  "knowsAbout":["Demand generation","Marketing operations","Account-based marketing","Paid media","SEO","Generative engine optimization","Answer engine optimization","Marketo","HubSpot","Salesforce","Lead scoring","Marketing attribution","B2B SaaS marketing","Team leadership","AI agents for marketing","Generative AI"],
  "alumniOf":[
    {"@type":"Organization","name":"Flosum"},
    {"@type":"Organization","name":"LeanData"},
    {"@type":"Organization","name":"Chef Software"},
    {"@type":"CollegeOrUniversity","name":"City University of Seattle"},
    {"@type":"CollegeOrUniversity","name":"Western Washington University"}],
  "owns":{"@id":SITE+"/#ride4all"}},
 {"@type":"NGO","@id":SITE+"/#ride4all","name":"R.I.D.E. 4 ALL","url":"https://www.ride4all.org","description":"A nonprofit bringing inclusive recreation to people of all abilities.","founder":{"@id":SITE+"/#person"}},
 *[ ({"@type":"PodcastEpisode","name":x["title"],"url":x["url"],"datePublished":x["date"],"timeRequired":f"PT{x['mins']}M","partOfSeries":{"@type":"PodcastSeries","name":x["show"]},"actor":{"@id":SITE+"/#person"}} if x["type"]=="podcast" else {"@type":"VideoObject","name":x["title"],"url":x["url"],"uploadDate":x["date"],"description":x["blurb"],"publisher":{"@type":"Organization","name":x["show"]},"actor":{"@id":SITE+"/#person"}}) for x in episodes],
 {"@type":"FAQPage","@id":SITE+"/#faq","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
]}
ld=json.dumps(jsonld,indent=1,ensure_ascii=False)

TITLE="Matt Lyman | B2B Marketing Leader, Demand Generation"
DESC="Marketing leader with nearly 20 years in marketing. Most recently VP of Marketing at Flosum. Seattle, remote."

page=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(TITLE)}</title>
<meta name="description" content="{e(DESC)}">
<link rel="canonical" href="{SITE}/">
<meta name="author" content="Matt Lyman">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="profile">
<meta property="og:title" content="{e(TITLE)}">
<meta property="og:description" content="{e(DESC)}">
<meta property="og:url" content="{SITE}/">
<meta property="og:image" content="{SITE}/images/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Matt Lyman, B2B marketing leader">
<meta property="profile:first_name" content="Matt">
<meta property="profile:last_name" content="Lyman">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(TITLE)}">
<meta name="twitter:description" content="{e(DESC)}">
<meta name="twitter:image" content="{SITE}/images/og-image.jpg">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="text/plain" href="/llms.txt" title="llms.txt">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<script type="application/ld+json">
{ld}
</script>
<style>
:root{{--slate:#46605A;--slate-dk:#2F433E;--ink:#22302D;--muted:#5E6B68;--yellow:#F4C430;--yellow-soft:#FBE9A6;--bg:#F6F7F5;--card:#FFFFFF;--line:#E3E7E4}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--bg);color:var(--ink);font:400 17px/1.65 Montserrat,system-ui,-apple-system,Segoe UI,sans-serif;-webkit-font-smoothing:antialiased}}
img{{max-width:100%;height:auto;display:block}}
a{{color:var(--slate);text-decoration-thickness:2px;text-underline-offset:3px}}
a:hover{{color:var(--slate-dk)}}
.wrap{{max-width:1080px;margin:0 auto;padding:0 20px}}
h1,h2,h3{{font-family:Anton,Impact,"Arial Narrow",sans-serif;font-weight:400;letter-spacing:.01em;text-transform:uppercase;color:var(--slate);margin:0}}
h2{{font-size:clamp(2rem,5vw,3rem);line-height:1.05;margin-bottom:.5em}}
p{{margin:0 0 1em}}
.btn{{display:inline-block;font:700 .95rem Montserrat,sans-serif;padding:.8em 1.4em;border-radius:999px;text-decoration:none;border:2px solid var(--slate);transition:transform .15s,background .15s}}
.btn:hover{{transform:translateY(-2px)}}
.btn.primary{{background:var(--slate);color:#fff}}
.btn.primary:hover{{background:var(--slate-dk);color:#fff}}
.btn.ghost{{background:transparent;color:var(--slate)}}
.btn.ghost:hover{{background:#fff}}
.pill{{display:inline-block;background:var(--yellow);color:var(--slate-dk);font:700 .85rem Montserrat,sans-serif;letter-spacing:.06em;text-transform:uppercase;padding:.45em 1.1em;border-radius:999px}}
.nav{{position:sticky;top:0;z-index:50;background:rgba(246,247,245,.93);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}}
.navin{{display:flex;align-items:center;gap:18px;padding-top:10px;padding-bottom:10px}}
.nav .brand{{font:400 1.3rem Anton,Impact,sans-serif;letter-spacing:.04em;text-transform:uppercase;color:var(--slate);text-decoration:none;white-space:nowrap}}
.links{{display:flex;gap:2px;list-style:none;margin:0 0 0 auto;padding:0;overflow-x:auto;scrollbar-width:none}}
.links::-webkit-scrollbar{{display:none}}
.links a{{display:block;padding:.45em .85em;border-radius:999px;font:600 .85rem Montserrat,sans-serif;color:var(--ink);text-decoration:none;white-space:nowrap}}
.links a:hover{{background:#fff}}
.links a.active{{background:var(--yellow);color:var(--slate-dk)}}
.nav .btn{{padding:.5em 1.1em;font-size:.85rem;white-space:nowrap}}
section{{scroll-margin-top:62px}}
.skl{{margin:0;display:grid;gap:16px}}
.skl dt{{font-size:.78rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}}
.skl dd{{margin:.15em 0 0;font-size:1rem;line-height:1.65}}
@media (max-width:820px){{.navin{{flex-wrap:wrap;gap:6px 12px}}.nav .btn{{margin-left:auto}}.links{{order:3;width:100%;margin:0}}section{{scroll-margin-top:100px}}}}
/* hero */
.hero{{position:relative;overflow:hidden;padding:20px 0 56px}}
.hero:before,.hero:after{{content:"";position:absolute;background:#fff;border-radius:50%;z-index:0}}
.hero:before{{width:520px;height:420px;right:-160px;top:-120px;border-radius:60% 40% 55% 45%}}
.hero:after{{width:420px;height:360px;left:-180px;bottom:-140px;border-radius:45% 55% 40% 60%}}
.hero .grid{{position:relative;z-index:1;display:grid;grid-template-columns:1.25fr .75fr;gap:40px;align-items:center}}
.hero h1{{font-size:clamp(3.4rem,10vw,7.2rem);line-height:.92;margin:.25em 0 .15em}}
.hero .sub{{font-weight:700;font-size:1.2rem;color:var(--slate-dk);margin-bottom:1em}}
.portrait{{position:relative;width:min(360px,80vw);aspect-ratio:1;justify-self:center}}
.portrait:before{{content:"";position:absolute;inset:-14px;border-radius:50%;background:var(--yellow)}}
.portrait img{{position:relative;width:100%;height:100%;object-fit:cover;border-radius:50%;border:6px solid var(--bg)}}
.community-line{{font-weight:600;color:var(--slate);border-left:4px solid var(--yellow);padding-left:12px;margin:1.2em 0}}
.cta{{display:flex;flex-wrap:wrap;gap:12px;margin:1.4em 0 .8em}}
.open{{font-size:.95rem;color:var(--muted)}}
.open b{{color:var(--slate-dk)}}
.stats{{position:relative;z-index:1;display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:40px}}
.stat{{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:22px 22px 18px;border-top:6px solid var(--yellow)}}
.stat .n{{font:400 clamp(2.2rem,5vw,3.2rem)/1 Anton,Impact,sans-serif;color:var(--slate)}}
.stat .l{{font-weight:600;margin:.5em 0 .3em;line-height:1.4}}
.stat .s{{font-size:.82rem;color:var(--muted)}}
.pull{{position:relative;z-index:1;margin:36px auto 0;max-width:760px;text-align:center}}
.pull blockquote{{margin:0;font-size:1.2rem;font-weight:500;line-height:1.6;color:var(--ink)}}
.pull cite{{display:block;margin-top:.7em;font-style:normal;font-size:.9rem;font-weight:700;color:var(--slate)}}
section{{padding:56px 0}}
section.alt{{background:#fff;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}}
/* about */
.about{{display:grid;grid-template-columns:1.4fr .6fr;gap:40px;align-items:start}}
.about .lead{{font-size:1.1rem;font-weight:500;background:var(--yellow-soft);border-radius:14px;padding:18px 20px}}
.photo{{border-radius:20px;overflow:hidden;box-shadow:0 8px 28px rgba(34,48,45,.14)}}
.photo img{{width:100%}}
figcaption{{font-size:.8rem;color:var(--muted);padding:8px 2px 0}}
figure{{margin:0}}
/* proof */
.roles{{display:grid;gap:20px}}
.role{{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:26px 28px}}
.role header{{display:flex;flex-wrap:wrap;justify-content:space-between;gap:4px 16px;margin-bottom:.4em}}
.role h3{{font-size:1.7rem}}
.role .when{{font-weight:600;color:var(--muted);font-size:.9rem;align-self:center}}
.role .title{{font-weight:700;color:var(--slate-dk);margin:0 0 .6em}}
.role .scope{{font-size:.95rem;color:var(--muted);margin-bottom:.8em}}
.role ul{{margin:0;padding-left:1.2em}}
.role li{{margin:.45em 0}}
.earlier{{font-size:.95rem;color:var(--muted);margin-top:18px}}
/* community */
.story{{display:grid;grid-template-columns:1fr 1fr;gap:36px;align-items:start}}
.story p{{font-size:1.05rem}}
.pair{{display:grid;gap:16px}}
.news{{margin-top:1.2em;padding:16px 18px;background:var(--bg);border-radius:14px;border:1px solid var(--line);font-size:.95rem}}
.news strong{{display:block;margin-bottom:.3em;color:var(--slate-dk)}}
.news ul{{margin:0;padding-left:1.1em}}
.roles-list{{margin:1em 0 0;padding:0;list-style:none}}
.roles-list li{{padding:.35em 0;border-bottom:1px solid var(--line)}}
/* talks */
.eps{{list-style:none;margin:0;padding:0;display:grid;gap:14px}}
.eps li{{background:var(--card);border:1px solid var(--line);border-left:6px solid var(--yellow);border-radius:14px;padding:16px 22px}}
.eps .show{{display:block;font-size:.78rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}}
.eps a{{display:inline-block;font-weight:700;font-size:1.08rem;margin:.2em 0 .1em}}
.eps p{{margin:0;font-size:.97rem;color:var(--ink)}}
/* quotes */
.quotes{{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}}
.q{{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:24px 26px;position:relative}}
.q:before{{content:"\\201C";font:400 4rem/1 Anton,serif;color:var(--yellow);position:absolute;top:6px;left:18px}}
.q p{{margin:1.4em 0 .6em;font-weight:500}}
.q cite{{font-style:normal;font-weight:700;font-size:.88rem;color:var(--slate)}}
.tabs{{display:none;gap:8px;margin:0 0 22px;overflow-x:auto;white-space:nowrap;padding-bottom:4px}}
.js .tabs{{display:flex}}
.tabs button{{font:inherit;font-weight:700;font-size:.9rem;color:var(--slate-dk);background:transparent;border:2px solid var(--slate);border-radius:999px;padding:7px 18px;cursor:pointer}}
.tabs button[aria-selected="true"]{{background:var(--yellow);border-color:var(--yellow);color:var(--ink)}}
.tabs button:focus-visible{{outline:3px solid var(--slate-dk);outline-offset:2px}}
.q[hidden]{{display:none}}
.q cite .who{{display:block}}
.q cite .rel{{display:block;font-weight:500;font-size:.82rem;color:var(--muted);margin-top:2px}}
/* skills */
.skills p{{margin:0 0 .8em}}
.skills .small{{font-size:.9rem;color:var(--muted)}}
/* faq */
details{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:0 20px;margin:0 0 10px}}
summary{{cursor:pointer;font-weight:700;padding:16px 0;color:var(--slate-dk);list-style:none;display:flex;justify-content:space-between;gap:12px}}
summary::-webkit-details-marker{{display:none}}
summary:after{{content:"+";font-size:1.4rem;line-height:1;color:var(--slate)}}
details[open] summary:after{{content:"\\2212"}}
details p{{padding-bottom:4px}}
/* contact */
.contact{{display:grid;grid-template-columns:.8fr 1.2fr;gap:36px;align-items:center}}
footer{{padding:28px 0 40px;font-size:.85rem;color:var(--muted);text-align:center}}
@media (max-width:820px){{
 .hero .grid,.about,.story,.contact{{grid-template-columns:1fr}}
 .stats,.quotes{{grid-template-columns:1fr}}
 .hero .grid{{gap:28px}}
 .portrait{{order:-1}}
 section{{padding:40px 0}}
}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}.btn{{transition:none}}}}
</style>
</head>
<body id="top">
<nav class="nav" aria-label="Page sections">
 <div class="wrap navin">
  <a class="brand" href="#top">Matt Lyman</a>
  <ul class="links">
   <li><a href="#about">About</a></li>
   <li><a href="#proof">Work</a></li>
   <li><a href="#community">Community</a></li>
   <li><a href="#talks">Talks</a></li>
   <li><a href="#people">Testimonials</a></li>
   <li><a href="#skills">Skills</a></li>
   <li><a href="#faq">FAQ</a></li>
  </ul>
  <a class="btn ghost" href="{LI}" rel="me noopener">LinkedIn</a>
 </div>
</nav>

<header class="hero">
 <div class="wrap">
  <div class="grid">
   <div>
    <span class="pill">B2B marketing leader</span>
    <h1>Matt Lyman</h1>
    <p class="sub">Demand generation built on stories buyers believe and numbers Sales trusts.</p>
    <p>I fix pipeline. Not by throwing more budget at the top of the funnel, but by finding where it's actually broken: conversion rates, messaging that doesn't land, content that doesn't move buyers, and handoffs between Marketing, Sales, and Customer Success that leak revenue at every stage. Most recently VP of Marketing at Flosum. Seattle, remote.</p>
    <p class="community-line">Founder, R.I.D.E. 4 ALL. President, Highline Special Needs PTA.</p>
    <div class="cta">
     <a class="btn primary" href="{LI}" rel="me noopener">Message Matt on LinkedIn</a>
     <a class="btn ghost" href="/Matt_Lyman_Resume.pdf">Resume (PDF)</a>
    </div>
    <p class="open"><b>Open to</b> VP and Head-of marketing roles.</p>
   </div>
   <div class="portrait">
    <img src="/images/matt-headshot.jpg" width="800" height="800" alt="Matt Lyman smiling, wearing dark-framed glasses and a gray-blue t-shirt" fetchpriority="high">
   </div>
  </div>

  <div class="stats">
   <div class="stat"><div class="n">18% to 50%</div><div class="l">Marketing's share of new business pipeline, with demand gen spend down 41%</div><div class="s">LeanData, 2022 to 2024</div></div>
   <div class="stat"><div class="n">87%</div><div class="l">Drop in cost per paid MQL in six months</div><div class="s">Flosum, Oct to Mar</div></div>
   <div class="stat"><div class="n">+467%</div><div class="l">Growth in meetings booked from paid media, 3 to 17 a month</div><div class="s">Flosum, Oct to Apr</div></div>
  </div>

  <figure class="pull">
   <blockquote>&ldquo;Matt's leadership style is one of empowerment. He sets the culture and direction and has allowed me to go take risks without the fear of failure. I have grown so much under his leadership.&rdquo;</blockquote>
   <cite>Direct report</cite>
  </figure>
 </div>
</header>

<section id="about">
 <div class="wrap about">
  <div>
   <h2>About</h2>
   <p class="lead">Matt Lyman is a B2B marketing leader based in Seattle with nearly 20 years in marketing, specializing in demand generation, with hands-on marketing operations and AI skills behind it. He has served as VP of Marketing at Flosum, VP of Demand Generation at LeanData, and Director of Revenue Marketing at Chef Software, where the revenue team grew about 2.7x through the company's acquisition by Progress. He founded R.I.D.E. 4 ALL, a nonprofit for inclusive recreation, and is president of the Highline Special Needs PTA.</p>
   <p>I review customer calls, talk to the people who said yes and the ones who said no, and build programs around what I find. Nearly 20 years in marketing, most recently at Chef, LeanData, and Flosum. At LeanData, marketing's share of new business pipeline went from 18% to 50% while demand gen spend dropped 41%. At Flosum, cost per paid MQL fell 87% in six months and monthly search impressions grew from 70,000 to over a million.</p>
   <p>Before software, I ran sales and marketing for a craft beer publication. I also have a degree in playwriting, and it shows. Every campaign I build starts with a story, a real one, about who the buyer is, what they're afraid of, and what changes if they solve the problem. I call it B2H, business to human, because at the end of every enterprise deal is a person making a decision. At Flosum, that meant scrapping product-first messaging and rebuilding the strategic narrative from the ground up. Then I make sure the numbers behind it are ones Sales believes.</p>
   <p>I build with AI every day. At Flosum I worked with product marketing on an agent that tracks competitor and industry news and hands Sales what changed, built an ABM dashboard that pulled ad, intent, and site data into one view across 51 accounts, set up our AI SDR, and rebuilt our content for AI search.</p>
   <p>I lead from alongside, not above. My job is to coach my team well enough that they can take my job and go find a bigger one.</p>
  </div>
  <figure class="photo-fig">
   <div class="photo"><img src="/images/matt-cycling.jpg" width="900" height="1200" loading="lazy" alt="Matt Lyman in a yellow cycling jersey and blue helmet, riding into low sun"></div>
   <figcaption>You'll probably find me on a bike.</figcaption>
  </figure>
 </div>
</section>

<section id="proof" class="alt">
 <div class="wrap">
  <h2>The work</h2>
  <div class="roles">
   <article class="rel">
    <header><h3>Flosum</h3><span class="when">Apr 2025 to Jun 2026</span></header>
    <p class="title">VP of Marketing</p>
    <p class="scope">Rebuilt the marketing function at an enterprise Salesforce governance platform. Reported to the CEO, led a team of 5. Agency partners ran the ad accounts. I owned strategy, measurement, and creative direction.</p>
    <ul>
     <li>Cost per paid MQL down 87% in six months. In one quarter, spend rose about 42% while paid MQLs rose 167%.</li>
     <li>Meetings from paid up 467%.</li>
     <li>Monthly search impressions went from 70,000 to over one million, up 1,329%, through the SEO and GEO/AEO rebuild: 120+ assets updated, FAQ rebuilds, third-party authority placements.</li>
     <li>ABM across 51 named accounts and 10 AEs. Target accounts clicked at 3 to 7x the campaign average, and 7 became opportunities within five months, mostly through BDR meetings.</li>
     <li>Built an agent with product marketing that tracks competitor and industry news and hands Sales what changed, and an ABM dashboard that pulls ad, intent, and site data into one view. Also set up the AI SDR.</li>
    </ul>
   </article>
   <article class="rel">
    <header><h3>LeanData</h3><span class="when">Feb 2022 to Nov 2024</span></header>
    <p class="title">VP of Demand Generation</p>
    <p class="scope">Moved the team from growth-at-all-costs to a demand model that scaled. Team of 4.</p>
    <ul>
     <li>Marketing's share of new business pipeline went from 18% to 50%. In 2023, demand gen spend fell 41% while marketing-sourced pipeline grew 45%.</li>
     <li>Enterprise went from 36% to 65% of pipeline.</li>
     <li>BookIt, the scheduling product, hit 2x its ARR target in year one.</li>
     <li>Lead-to-qualified-opportunity conversion rose from 2.5% to 10%+ after a lead scoring rebuild. Events returned 4:1 in pipeline. Paid inbound leads doubled while cost per demo fell by more than half.</li>
     <li>Widened the audience from RevOps to sales and marketing leaders, then IT managers. Led the internal rollout of the Revenue Orchestration Platform.</li>
    </ul>
   </article>
   <article class="rel">
    <header><h3>Chef Software</h3><span class="when">2015 to 2022</span></header>
    <p class="title">Director of Revenue Marketing at exit</p>
    <p class="scope">Ran demand gen, ops, web, and SDR teams. Team of 7. Joined the business unit leadership team after Progress acquired Chef.</p>
    <ul>
     <li>Revenue team grew about 2.7x through the acquisition, with quarterly pipeline goals beaten by 4x or more.</li>
     <li>SDR and BDR teams averaged 120%+ of quota.</li>
     <li>Rebuilt Marketo from the ground up. An external auditor rated it best-in-class.</li>
     <li>Marketed the training site to 10,000 active users in six months.</li>
    </ul>
   </article>
  </div>
  <p class="earlier">Earlier: G2 Web Services, marketing to financial institutions (2011 to 2015). AmericanCraftBeer.com, director of sales and marketing (2014 to 2017).</p>
 </div>
</section>

<section id="community">
 <div class="wrap">
  <h2>The other job</h2>
  <div class="story">
   <div>
    <p>In 2020 I rode 32.1 miles on March 21 to celebrate inclusion on World Down Syndrome Day. In 2021 and 2022 it became 321 miles over three days, Bellingham to Portland, with friends riding legs alongside me. Anyone could join, whether they rode 321 miles or 3.21 minutes.</p>
    <p>In 2022 we started <a href="https://www.ride4all.org" rel="noopener">R.I.D.E. 4 ALL</a>, a nonprofit for inclusive recreation. In 2025 and 2026 the ride evolved into Day of Play, a free event that brings kids of all abilities together to play in the same space, with the same activities.</p>
    <ul class="roles-list">
     <li><strong>R.I.D.E. 4 ALL</strong>, founder and board member. Chair of 321 for 3.21.</li>
     <li><strong>Highline Special Needs PTA</strong>, president since 2024, vice president 2022 to 2024.</li>
    </ul>
    <div class="news">
     <strong>In the news</strong>
     <ul>
      <li><a href="https://king5.com/article/news/local/seattle-dad-down-syndrome-community-puget-sound-bike-ride-321/281-02b0f153-2541-4820-9520-8de10d7c46c6" rel="noopener">KING5: Seattle dad embarks on 321-mile bike ride to raise awareness</a></li>
      <li><a href="https://king5.com/article/features/down-syndrome-awareness-trisomy-21-puget-sound-down-syndrome-community/281-0ca3a37c-213c-40c9-b270-e01b1d8c7e46" rel="noopener">KING5: Father to ride 321 miles from Bellingham to Portland</a></li>
     </ul>
    </div>
   </div>
   <div class="pair">
    <figure class="photo"><img src="/images/matt-family.jpg" width="1400" height="933" loading="lazy" alt="Matt Lyman with his family, smiling and arm in arm in front of a tall green hedge"></figure>
    <figure class="photo"><img src="/images/matt-river.jpg" width="1200" height="900" loading="lazy" alt="Matt Lyman making a big open-mouthed grin in a selfie with two kids beside a river"></figure>
   </div>
  </div>
 </div>
</section>

<section id="talks" class="alt">
 <div class="wrap">
  <h2>Talks and podcasts</h2>
  <ul class="eps">
{eps_html}
  </ul>
 </div>
</section>

<section id="people">
 <div class="wrap">
  <h2>What people say</h2>
  <div class="tabs" role="tablist" aria-label="Filter testimonials by who is speaking">
   <button type="button" role="tab" aria-selected="true" data-f="all">All</button>
   <button type="button" role="tab" aria-selected="false" data-f="mgr">Managers</button>
   <button type="button" role="tab" aria-selected="false" data-f="rpt">Direct reports</button>
   <button type="button" role="tab" aria-selected="false" data-f="peer">Peers</button>
  </div>
  <script>document.documentElement.classList.add('js')</script>
  <div class="quotes" id="quotes" role="tabpanel">
   <div class="q" data-g="mgr"><p>Matt was a key leader on my marketing team who regularly rose to the occasion and inspired his employees to do the same. His charismatic style makes him a natural mentor and coach.</p><cite><span class='who'>Dan Frechtling</span><span class="rel">Direct manager, SVP Product and Strategy, LegitScript</span></cite></div>
   <div class="q" data-g="mgr"><p>Matt's superpower isn't just that he is a fantastic operator, it's that his team and everyone they interface with become happy high performers. Also, ask him about beer.</p><cite><span class="rel">Direct manager</span></cite></div>
   <div class="q" data-g="rpt"><p>He's a rare marketing executive who pairs strategic vision with a hands-on approach&hellip; Matt has a genuine ability to make people feel seen, heard, and valued.</p><cite><span class='who'>Rocio E. Garza</span><span class="rel">Direct report</span></cite></div>
   <div class="q" data-g="rpt"><p>Matt leads with both heart and data, creating an environment where his team thrives and delivers real impact. His mix of strategic thinking, collaboration, and mentorship has not only driven results but also helped me learn and grow in my own career.</p><cite><span class='who'>Shaun Yap</span><span class="rel">Direct report, Langchain</span></cite></div>
   <div class="q" data-g="peer"><p>Matt's team fears how much they love him.</p><cite><span class='who'>Dan Hauenstein</span><span class="rel">Leadership colleague, VP Product Marketing, SolarWinds</span></cite></div>
   <div class="q" data-g="peer"><p>Matt has the superpower to connect people, processes, and products to drive results through demand gen programs.</p><cite><span class="rel">Leadership colleague</span></cite></div>
   <div class="q" data-g="peer"><p>Matt has an ease about him&hellip; He is a valuable asset to any company, and an invaluable human being to get to know. In short; if given the opportunity? Hire. This. Man.</p><cite><span class='who'>Nichol Goldstein</span><span class="rel">Peer, Community Manager, Progress Software</span></cite></div>
  </div>
 </div>
</section>

<section id="skills" class="alt">
 <div class="wrap skills">
  <h2>Skills and tools</h2>
  <dl class="skl">
   <div><dt>Focus</dt><dd>Marketing leadership, demand generation, ABM, paid media, SEO and GEO/AEO, AI workflows and agents, messaging and narrative, lifecycle and lead scoring, attribution, marketing operations, sales and BDR alignment, product and category launches, events.</dd></div>
   <div><dt>Tools</dt><dd>Marketo, HubSpot, Eloqua, Pardot, Salesforce, LeanData, Qualified, Outreach, Salesloft, Demandbase, 6sense, UserGems, Intellimize, Claude, ChatGPT.</dd></div>
   <div><dt>Training</dt><dd>MBA, Global Marketing Management. Six Sigma Green Belt. Franklin Covey and Dale Carnegie leadership training.</dd></div>
  </dl>
 </div>
</section>

<section id="faq">
 <div class="wrap">
  <h2>Questions people ask</h2>
  {faq_html}
 </div>
</section>

<section id="contact" class="alt">
 <div class="wrap contact">
  <figure class="photo"><img src="/images/matt-beach.jpg" width="1200" height="900" loading="lazy" alt="Matt Lyman smiling in sunglasses and a green cap on a driftwood beach below a sandy bluff"></figure>
  <div>
   <h2>Say hello</h2>
   <p>If you're hiring for a marketing leader, or you just want to talk pipeline, LinkedIn is the fastest way to reach me.</p>
   <div class="cta">
    <a class="btn primary" href="{LI}" rel="me noopener">Message Matt on LinkedIn</a>
    <a class="btn ghost" href="/Matt_Lyman_Resume.pdf">Resume (PDF)</a>
   </div>
  </div>
 </div>
</section>

<footer><div class="wrap">&copy; 2026 Matt Lyman. Seattle, WA.</div></footer>
<script>
(function(){{try{{var links=[].slice.call(document.querySelectorAll('.links a')),map={{}};links.forEach(function(a){{map[a.getAttribute('href').slice(1)]=a}});var secs=Object.keys(map).map(function(id){{return document.getElementById(id)}}).filter(Boolean);if(!('IntersectionObserver' in window))return;var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{links.forEach(function(a){{a.classList.remove('active')}});map[e.target.id].classList.add('active')}}}})}},{{rootMargin:'-45% 0px -50% 0px'}});secs.forEach(function(x){{io.observe(x)}})}}catch(e){{}}}})();
(function(){{try{{var tabs=[].slice.call(document.querySelectorAll('.tabs [role=tab]')),qs=[].slice.call(document.querySelectorAll('#quotes .q'));function pick(t){{tabs.forEach(function(b){{b.setAttribute('aria-selected',b===t?'true':'false');b.tabIndex=b===t?0:-1}});var f=t.getAttribute('data-f');qs.forEach(function(q){{q.hidden=!(f==='all'||q.getAttribute('data-g')===f)}})}}tabs.forEach(function(b,i){{b.tabIndex=i===0?0:-1;b.addEventListener('click',function(){{pick(b)}});b.addEventListener('keydown',function(e){{var n=e.key==='ArrowRight'?i+1:e.key==='ArrowLeft'?i-1:-1;if(n<0)return;n=(n+tabs.length)%tabs.length;tabs[n].focus();pick(tabs[n]);e.preventDefault()}})}})}}catch(e){{}}}})();
</script>
</body>
</html>
'''
open(f"{OUT}/index.html","w").write(page)

# support files
open(f"{OUT}/CNAME","w").write("mattlyman.com")
open(f"{OUT}/.nojekyll","w").write("")
bots=["GPTBot","OAI-SearchBot","ChatGPT-User","ClaudeBot","Claude-SearchBot","Claude-User","PerplexityBot","Perplexity-User","Google-Extended","Applebot-Extended","Bingbot","Googlebot"]
DIS="Disallow: /docs/\nDisallow: /tools/\n"
robots="User-agent: *\nAllow: /\n"+DIS+"\n"+"".join(f"User-agent: {b}\nAllow: /\n"+DIS+"\n" for b in bots)+f"Sitemap: {SITE}/sitemap.xml\n"
open(f"{OUT}/robots.txt","w").write(robots)
open(f"{OUT}/sitemap.xml","w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n <url><loc>{SITE}/</loc><lastmod>2026-10-29</lastmod><changefreq>monthly</changefreq><priority>1.0</priority></url>\n</urlset>\n')
llms=f"""# Matt Lyman

> B2B marketing leader based in Seattle with nearly 20 years in marketing, specializing in demand generation, with hands-on marketing operations and AI skills behind it. Most recently VP of Marketing at Flosum. Open to VP and Head-of marketing roles.

## Summary
- Roles: VP of Marketing at Flosum (Apr 2025 to Jun 2026); VP of Demand Generation at LeanData (Feb 2022 to Nov 2024); Director of Revenue Marketing at Chef Software (2015 to 2022, acquired by Progress).
- LeanData: marketing's share of new business pipeline went from 18% to 50% while demand gen spend fell 41%.
- Flosum: cost per paid MQL down 87% in six months; meetings from paid up 467%; monthly search impressions up 1,329% after an SEO and GEO/AEO rebuild.
- Chef: revenue team grew about 2.7x through acquisition by Progress; SDR and BDR teams averaged 120%+ of quota.
- Community: founder of R.I.D.E. 4 ALL (inclusive recreation nonprofit); president of the Highline Special Needs PTA.

## Links
- [Home page]({SITE}/): full background, results, and FAQ
- [Resume (PDF)]({SITE}/Matt_Lyman_Resume.pdf)
- [LinkedIn]({LI})
- [R.I.D.E. 4 ALL](https://www.ride4all.org)

## Talks and podcasts
"""+"".join(f"- [{x['title']}]({x['url']}): {x['show']}, {x['year']}. {x['blurb']}\n" for x in episodes)
open(f"{OUT}/llms.txt","w").write(llms)
open(f"{OUT}/favicon.svg","w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="32" fill="#F4C430"/><circle cx="32" cy="32" r="27" fill="#46605A"/><text x="32" y="41" font-family="Impact,Arial Narrow,sans-serif" font-size="26" text-anchor="middle" fill="#fff">ML</text></svg>\n')
print("ok", len(page))
