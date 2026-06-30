<!-- Language: English | [Español](./README.es.md) -->

# GEO / AI-Visibility Audit — Case Study

> How I audited a B2B SaaS website for **visibility inside AI answers** (ChatGPT, Perplexity, Google AI Overviews/Mode) and turned the findings into a prioritized, ship-ready action plan.

🌐 **[Leer en Español →](./README.es.md)**

![type](https://img.shields.io/badge/type-case--study-blue) ![field](https://img.shields.io/badge/field-GEO%20%2F%20AI%20Visibility-7c3aed) ![client](https://img.shields.io/badge/client-anonymized-success)

---

## ⚠️ About this case study

This is a **portfolio piece**. The client is referred to by the codename **“AI Visibility Platform A”** — the real name and domain are withheld. Competitor tools are named because they are public products and provide useful market context. All metrics are real.

---

## Context

| | |
|---|---|
| **Client (codename)** | **AI Visibility Platform A** — a mid-market B2B SaaS in the GEO / AI-visibility category |
| **Site** | Bilingual marketing site (EN + ES), ~540 URLs |
| **Role** | GEO & Content Lead (audit + action layer) |
| **Engine analyzed** | ChatGPT (51-prompt Gauntlet) |
| **Duration** | ~1 month, part-time |

**GEO (Generative Engine Optimization)** is the discipline of getting a brand cited and recommended *inside* AI-generated answers — the successor to classic SEO, where the "click" is often replaced by a model's recommendation.

### The competitive landscape
Platform A competes in a crowded category. The audit benchmarked it against:
- **GEO-native tools:** Profound, Peec AI, Otterly AI, Scrunch AI, Rankscale, AirOps, Conductor, Knowatoa, LLM Pulse, xFunnel.
- **Legacy SEO suites adding "GEO features":** Semrush, Ahrefs, SE Ranking, BrightEdge, Surfer SEO, Writesonic.

This matters: legacy suites advertise *millions* of keywords/prompts, but in a specific niche most are irrelevant or stale. GEO-native platforms instead generate prompts from a brand's **entity, context and market** — which is the real battleground.

---

## The problem

Platform A sells AI-visibility software, yet its **own** site under-performed on the exact queries its buyers ask AI assistants. The brief: diagnose *why* the brand was invisible on generic/category prompts, and produce an operator-grade action plan — not a one-off audit.

---

## Methodology

Four workstreams. Full detail in **[METHODOLOGY.md](./METHODOLOGY.md)**.

### 1. The GEO Gauntlet (prompt battery)
A structured battery of **51 prompts run against ChatGPT**, classified into **5 query types** — Branded, Category, Comparison, How-to and Thought Leadership — and mapped to funnel intent (TOFU · MOFU · BOFU) and branded vs. non-branded queries. Each prompt is scored for:
- **Mention** — does the brand appear at all?
- **Citation** — is an owned URL cited as a source?
- **Share of Voice** — brand mentions ÷ total mentions vs. competitors.
- **Sentiment** — endorsed / neutral / undermined, feature by feature.

### 2. The 4 GEO pillars

| Pillar | Question it answers |
|--------|---------------------|
| **Entity** | Does AI know *who* the brand is and not confuse it? |
| **Extractability** | Can a model cleanly lift facts from the page? |
| **Evidence** | Are there proof points (cases, data, third-party sources)? |
| **Consensus** | Do signals agree across the web and across languages? |

### 3. Technical foundation audit
Dual EN/ES crawl, Core Web Vitals (real-user data), HTML semantics, i18n/hreflang, SERP hygiene.

### 4. Content & citation-gap analysis
Which URLs AI engines *already* cite, where third-party validation is missing, and how the knowledge base fails to get retrieved.

---

## Key findings

### GEO score: **5.5 → 8.8** (projected)

| Pillar | Live | Proposed |
|--------|------|----------|
| Entity | 6.5 | 9.0 |
| Extractability | 4.0 | 8.5 |
| Evidence | 5.5 | 8.5 |
| Consensus | 8.0 | 9.5 |
| **Overall** | **5.5** | **8.8** |

The biggest gap was **Extractability (+4.5)** — the pillar that most directly controls whether AI cites you or ignores you.

### Finding 1 — Performance was *not* the problem
Core Web Vitals passed at origin (LCP 1,392 ms · INP 66 ms · CLS 0.01). This redirected all effort to **semantics, architecture and copy** instead of a pointless "site-speed project".

### Finding 2 — EN and ES were disconnected silos
The English crawl reached **0** internal links to the Spanish tree, orphaning **~176 Spanish URLs**. `hreflang` / `x-default` were not implemented correctly → AI engines received mixed language signals.

### Finding 3 — Localization debt: 87% of Spanish URLs had English slugs
Of **219** Spanish URLs, **190 (87%)** had **English slugs serving fully Spanish content**. I built a script to classify slug-language vs. content-language, flag every mismatch, and **propose a clean Spanish slug + 301 map** for all 190. (See `tooling/`.)

### Finding 4 — Broken-link debt
A full crawl of ~**540 URLs** surfaced **~103 returning 404** (≈19%) — wasted crawl budget and dead citation targets.

### Finding 5 — The citation gap (Evidence pillar)
On a pilot brand audit, the brand held strong **owned + social** citations but **zero third-party citations**, while competitors appeared in press and directories. A Share-of-Voice lead built only on your own domain is fragile: it collapses the moment a rival earns editorial coverage.

### Finding 6 — No semantic `<h1>`
The homepage headline was a styled `<div>`, not a semantic `<h1>` — repeated across **7 key URLs**. Models weighting the first heading block couldn't classify the page topic.

---

## Recommendations (prioritized)

| Priority | Action | Pillar |
|----------|--------|--------|
| **P0** | Real semantic `<h1>` with category copy on home (EN/ES) | Entity / Extractability |
| **P0** | `hreflang` EN↔ES + `x-default` + bidirectional links | Consensus |
| **P0** | Review/entity schema + structured social proof | Entity / Evidence |
| **P1** | Localize 190 ES slugs (301 map provided) | Consensus |
| **P1** | Interlink KB pillars from URLs AI already cites | Extractability |
| **P1** | Earn third-party citations (press, directories) | Evidence |
| **P2** | Fix 103× 404s, title/meta hygiene, broken slugs | Extractability |

---

## Skills & tools demonstrated

- **GEO / AEO strategy** — prompt batteries, pillar scoring, multi-engine measurement
- **Technical SEO** — Screaming Frog dual crawl, CrUX, hreflang, semantic HTML
- **Data tooling** — Python crawler + a language-mismatch classifier (slug vs. content) with auto-generated 301 proposals
- **Analysis** — Share of Voice, citation-gap and sentiment analysis vs. competitor set
- **Operator mindset** — turned diagnostics into a P0/P1/P2 plan with owners and effort

**Stack:** Python (`requests`, `BeautifulSoup`, `csv`) · Screaming Frog · CrUX · live AI engines · Markdown reporting.

---

## Repo structure

```
geo-audit-case-study/
├── README.md           ← case study (English)
├── README.es.md        ← case study (Español)
├── METHODOLOGY.md      ← GEO Gauntlet, pillars, scoring (EN)
├── METHODOLOGY.es.md   ← metodología (ES)
├── LINKEDIN_POST.md    ← ready-to-post summary (EN + ES)
└── tooling/
    └── url_language_audit.py   ← crawler + slug/content language classifier
```

---

## About

GEO & Content specialist focused on the **action layer**: not just measuring AI visibility, but operating it — shipping the structural and content changes that make AI engines cite a brand. Open to GEO / AI-visibility / technical-SEO roles.

*Client anonymized. This repository is a methodology and skills demonstration.*
