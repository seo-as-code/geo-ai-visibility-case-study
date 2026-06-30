<!-- Language: English | [Español](./README.es.md) -->

# GEO / AI-Visibility Audit & Optimization — Case Study

> A full Month-1 engagement for a B2B SaaS: measuring **visibility inside AI answers** (ChatGPT), auditing the technical foundation, **redesigning the homepage for GEO**, and shipping **new AI-ready content** + a repeatable operating system.

🌐 **[Leer en Español →](./README.es.md)**

![type](https://img.shields.io/badge/type-case--study-blue) ![field](https://img.shields.io/badge/field-GEO%20%2F%20AI%20Visibility-7c3aed) ![client](https://img.shields.io/badge/client-anonymized-success)

---

## ⚠️ About this case study

Portfolio piece. The client is referred to by the codename **“AI Visibility Platform A”** — real name, domain, customers and people are withheld. Competitor *tools* are named because they are public products and add market context. All metrics are real, measured in June 2026.

---

## Context

| | |
|---|---|
| **Client (codename)** | **AI Visibility Platform A** — a B2B SaaS in the GEO / AI-visibility category |
| **Site** | Bilingual marketing site (EN + ES), ~540 URLs |
| **Role** | GEO & Content Lead — audit **and** action layer |
| **Engine measured** | ChatGPT (51-prompt Gauntlet) |
| **Duration** | Month 1, ~4 h/day |

**GEO (Generative Engine Optimization)** is the discipline of getting a brand cited and recommended *inside* AI-generated answers — the successor to classic SEO, where the "click" is often replaced by a model's recommendation.

### The competitive landscape
Platform A competes in a crowded category, benchmarked against **GEO-native tools** (Profound, Peec AI, Otterly AI, Scrunch AI, Rankscale, AirOps, Conductor, Goodie AI, AthenaHQ) and **legacy SEO suites adding "GEO features"** (Semrush, Ahrefs, SE Ranking, BrightEdge, Surfer, Frase). Legacy suites advertise *millions* of keywords/prompts, but in a specific niche most are irrelevant or stale; GEO-native platforms generate prompts from a brand's **entity, context and market** — the real battleground.

---

## The problem

Platform A sells AI-visibility software, yet its **own** site under-performed on the exact queries its buyers ask AI assistants. The brief: diagnose *why* the brand was invisible on generic/category prompts, and deliver an operator-grade plan — not a one-off audit.

---

## Scope of work delivered (Month 1)

Four streams, from measurement to shipped assets:

| Stream | What I delivered |
|--------|------------------|
| **1. Measurement** | The **GEO Gauntlet** — 51 prompts run on ChatGPT, scored by mention / citation / SoV / sentiment, mapped to 5 query types and 4 GEO pillars. Reproducible (YAML + CSV + scoreboard script). |
| **2. Technical audit** | CrUX (Core Web Vitals) + dual EN/ES Screaming Frog crawl: i18n silos, semantic-HTML gaps, SERP hygiene, KB crawl footprint. |
| **3. Homepage GEO redesign** | Section-by-section rewrite of the homepage (EN + ES) as an **HTML preview**, lifting the on-page GEO score from **5.5 → 8.8**. Real `<h1>`, citable product modules, fixed broken Spanish copy, Review/FAQ schema. |
| **4. Content + operating layer** | New AI-ready content (EN blog + ES knowledge-base article), an interlinking plan, content-brief templates, and a weekly operating protocol with a P0/P1/P2 backlog. |

Detail: **[RESULTS.md](./RESULTS.md)** (Gauntlet scoreboard) · **[HOMEPAGE_REDESIGN.md](./HOMEPAGE_REDESIGN.md)** (before/after) · **[METHODOLOGY.md](./METHODOLOGY.md)** (how).

---

## Measured results — the GEO Gauntlet (ChatGPT)

**51 prompts**, single engine, fresh chat + memory off, exact prompt text from a versioned YAML.

| Metric | Result |
|--------|--------|
| Prompts completed | 51 / 51 |
| Mention rate | 49% (25/51) |
| Citation rate | 45% (23/51) |
| Branded citation rate | 83% (10/12) |

| Outcome | N |
|---------|---|
| Victory | 20 |
| Defeat | 24 |
| Partial | 5 |
| Ignored | 2 |

### By query type
| Query type | Balance | Citation |
|------------|---------|----------|
| **Branded** | 10V · 1P · 1I | 83% |
| **Comparison** | 9V · 1D · 1P | High |
| **Category** | 0V · 7D · 2P · 1I | Low |
| **How-to / problem** | 0V · 10D | **0%** |
| **Thought leadership** | 1V · 6D · 1P | Low |

### By GEO pillar
| Pillar | Cite rate | Reading |
|--------|-----------|---------|
| Entity | 82% (9/11) | Strong with disambiguation |
| Evidence | 73% (11/15) | Strong in direct comparisons |
| Consensus | 20% (3/15) | Weak in shortlists / expert queries |
| Extractability | **0%** (0/10) | Knowledge base never retrieved on how-to |

**The core insight — two visibility regimes:** Platform A *wins* when the buyer already knows the brand or names a vendor (branded + comparison). It *loses* the entire **discovery** funnel — generic category and how-to queries, exactly where buyers shop *before* they know the brand. The bottleneck is pre-brand discovery, not active comparison.

---

## Homepage GEO redesign: **5.5 → 8.8**

I audited the live homepage section by section and produced a GEO-optimized **HTML preview** (EN + ES). Full before/after in **[HOMEPAGE_REDESIGN.md](./HOMEPAGE_REDESIGN.md)**.

| Pillar | Live | Proposed |
|--------|------|----------|
| Entity | 6.5 | 9.0 |
| Extractability | 4.0 | 8.5 |
| Evidence | 5.5 | 8.5 |
| Consensus | 8.0 | 9.5 |
| **GEO Score** | **5.5** | **8.8** |

Highlights of the redesign:
- **Real semantic `<h1>`** with a *category* definition (“Platform for visibility in LLMs”) instead of a styled `<div>` marketing slogan — so an LLM can copy/paraphrase what the product *is*.
- **ICP moved to a kicker** above the H1, so audience targeting stops competing with the entity definition.
- **Factual subhead**: 7 named AI engines + method + metrics (extractable triplets).
- **Product suite rewritten** into 4 citable modules, each with operational copy and an intent-specific CTA.
- **Fixed broken machine-translated Spanish** across hero, product cards, MCP and reviews (the live site rendered tokens like *“…la plataforma por ti”* fragments that broke entity parsing).
- **Review + FAQ schema**, one-metric-one-entity-one-link case studies, and a GEO-vs-SEO FAQ that becomes literally citable.

---

## Technical findings

### Finding 1 — Performance was *not* the problem
Core Web Vitals passed at origin (LCP 1,392 ms · INP 66 ms · CLS 0.01). This redirected all effort to **semantics, architecture and copy** instead of a pointless "site-speed project".

### Finding 2 — EN and ES were disconnected silos
The English crawl reached **0** internal links to the Spanish tree, orphaning **~176 Spanish URLs**. `hreflang` / `x-default` were not implemented correctly → AI engines received mixed language signals.

### Finding 3 — No semantic `<h1>`
The homepage headline was a styled `<div>`, not a semantic `<h1>` — repeated across **7 key URLs**. Models weighting the first heading block couldn't classify the page topic.

### Finding 4 — Localization debt: 87% of Spanish URLs had English slugs
Of **219** Spanish URLs, **190 (87%)** had **English slugs serving fully Spanish content**. I built a script to classify slug-language vs. content-language, flag every mismatch, and **propose a clean Spanish slug + 301 map** for all 190. (See `tooling/`.)

### Finding 5 — Broken-link & SERP-hygiene debt
A full crawl of ~**540 URLs** surfaced **~103 returning 404** (≈19%). Plus long title tags (**133/176 ES**, 49/177 EN over 60 chars), missing meta on `/compare`, and a broken KB slug (`/%20ai-retrieval-layer`).

### Finding 6 — The citation gap (Evidence pillar)
Strong **owned + social** citations but **zero third-party** ones, while competitors appeared in press and directories. A Share-of-Voice lead built only on your own domain is fragile — it collapses the moment a rival earns editorial coverage.

---

## New content & operating layer produced

Not just diagnostics — shipped assets:

- **EN blog draft** — *"AI Visibility for Small Marketing Teams: From Data to Weekly Actions"* — a 4-step weekly operating loop (built to win the how-to/problem prompts that scored 0%).
- **ES knowledge-base draft** — *"From citation gap to content brief in 10 minutes"* — a practical, extractable workflow with a fill-in brief template.
- **Interlinking plan** — push authority from URLs ChatGPT *already cites* (product, MCP, pricing) into under-retrieved KB pillars, with recommended anchor text.
- **Operating system** — weekly protocol, content-brief templates, and a P0/P1/P2 backlog tied to *specific* losing prompts (not a generic checklist), plus a re-measurement loop.

---

## Recommendations (prioritized)

| Priority | Action | Pillar | Answers prompts |
|----------|--------|--------|-----------------|
| **P0** | Real semantic `<h1>` + category copy on home (EN/ES) | Entity / Extractability | category, entity |
| **P0** | `hreflang` EN↔ES + `x-default` + bidirectional links | Consensus | localized discovery |
| **P0** | Extractable how-to KB pages + FAQ schema, interlinked from cited URLs | Extractability | 31–38 (the 0% wave) |
| **P1** | Earn third-party citations (directories, press, reviews) | Evidence | expert / consensus |
| **P1** | Localize 190 ES slugs (301 map provided) | Consensus | localized retrieval |
| **P2** | Fix 103× 404s, title/meta hygiene, broken slugs | Extractability | SERP-fed retrieval |

---

## Skills & tools demonstrated

- **GEO / AEO strategy** — 51-prompt battery, pillar scoring, two-regime diagnosis, reproducible protocol
- **Technical SEO** — Screaming Frog dual crawl, CrUX, hreflang, semantic HTML, SERP hygiene
- **Conversion/GEO copywriting** — full homepage rewrite (EN/ES) optimized for LLM extraction *and* humans
- **Content production** — AI-ready blog + KB articles, content-brief templates, interlinking plans
- **Data tooling** — Python crawler + a slug/content language classifier with auto-generated 301 proposals
- **Operator mindset** — turned diagnostics into a P0/P1/P2 system with owners, effort and re-measurement

**Stack:** Python (`requests`, `BeautifulSoup`, `csv`) · Screaming Frog · CrUX · ChatGPT · HTML/CSS preview · Markdown reporting.

---

## Repo structure

```
geo-audit-case-study/
├── README.md / README.es.md          ← case study (EN / ES)
├── RESULTS.md / RESULTS.es.md         ← full GEO Gauntlet scoreboard
├── HOMEPAGE_REDESIGN.md / .es.md      ← homepage before/after (5.5 → 8.8)
├── METHODOLOGY.md / METHODOLOGY.es.md ← Gauntlet, pillars, technical, content
├── LINKEDIN_POST.md                   ← ready-to-post summary (EN + ES)
└── tooling/
    └── url_language_audit.py          ← crawler + slug/content language classifier
```

---

## About

GEO & Content specialist focused on the **action layer**: not just measuring AI visibility, but operating it — shipping the technical, design and content changes that make AI engines cite a brand. Open to GEO / AI-visibility / technical-SEO roles.

*Client anonymized. This repository is a methodology and skills demonstration.*
