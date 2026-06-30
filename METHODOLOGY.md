<!-- Language: English | [Español](./METHODOLOGY.es.md) -->

# Methodology — GEO / AI-Visibility Audit

🌐 **[Leer en Español →](./METHODOLOGY.es.md)**

This document explains *how* the audit in the [case study](./README.md) was run, so the approach is reproducible on any brand. The client is anonymized (codename **“AI Visibility Platform A”**); competitor tools are named as public market context.

---

## 1. What we are optimizing for

Classic SEO optimizes for **clicks** from a results page. GEO (Generative Engine Optimization) optimizes for **mentions and recommendations inside AI answers** — frequently with no click at all.

The unit of measurement shifts from *keyword → ranking position* to **prompt → answer presence**. That single shift drives the whole methodology below.

---

## 2. The GEO Gauntlet (prompt battery)

A curated battery of prompts that mirrors how a real buyer interrogates an AI assistant about a category and a brand.

### Structure
- **51 prompts**, run against **ChatGPT**.
- Each prompt classified into one of **5 query types**:
  - **Branded** — brand name, disambiguation, reputation.
  - **Category** — generic "tools / platforms for X", no brand named.
  - **Comparison** — "X vs Y", "best alternative to…", shortlists.
  - **How-to** — task / problem-solving informational queries.
  - **Thought leadership** — trends, opinions, "where is the category heading".
- Each prompt mapped to **funnel intent** (TOFU · MOFU · BOFU) and tagged **branded** vs. **non-branded**.

### Why the query types matter
Brands almost always win **branded** prompts and lose **category / comparison / how-to** prompts — which is exactly where buyers shop *before* they know the brand. Splitting by query type makes that blind spot measurable.

### Metrics captured per prompt × engine
| Metric | Definition |
|--------|------------|
| **Mention** | Brand appears in the answer (yes/no). |
| **Citation** | An owned URL is used as a source. |
| **Share of Voice (SoV)** | Brand mentions ÷ total brand mentions in the answer set. |
| **Sentiment** | Per feature: *endorsed* / *neutral* / *undermined*. |
| **Cited sources** | The actual URLs the engine pulled (owned / social / third-party). |

Engine analyzed: **ChatGPT** (51-prompt battery). The method is extensible to Perplexity, Google AI Overviews / AI Mode, Claude and Gemini.

---

## 3. The 4 GEO pillars

Every finding and recommendation is mapped to one pillar, so the client always knows *why* a fix matters.

### Entity
Does the AI correctly identify *who you are*?
Signals: semantic `<h1>`, `Organization`/`sameAs` schema, consistent naming, disambiguation from similarly-named entities.

### Extractability
Can a model cleanly lift facts from your page?
Signals: clean headings, complete declarative sentences, structured data, modular/snippet-friendly content, no broken copy.

### Evidence
Are there proof points a model can trust?
Signals: case studies, data, and crucially **third-party citations** (press, directories, reviews) — not just owned pages.

### Consensus
Do signals agree across the web and across languages?
Signals: `hreflang`, consistent terminology, aligned SERP presentation, agreement between owned and earned sources.

---

## 4. Technical foundation audit

| Layer | Tool | What it tells us |
|-------|------|------------------|
| Real-user performance | **CrUX** (Core Web Vitals) | Is speed a blocker? (Often it is *not* — don't over-invest.) |
| Crawl architecture | **Screaming Frog** (dual EN + ES crawl) | Are locales siloed? Orphaned URLs? |
| On-page semantics | SF + manual | Semantic `<h1>`, heading order, topic clarity. |
| i18n | SF + manual | `hreflang` / `x-default`, cross-locale linking. |
| SERP hygiene | SF | Title length, missing meta, broken slugs. |

**Why a dual crawl:** an English-only crawl may never discover the Spanish tree through internal links, under-reporting the entire localized asset set.

---

## 5. Content & citation-gap analysis

1. **Map what AI already cites** — owned vs. social vs. third-party URLs.
2. **Find the citation gap** — where competitors have third-party validation and you don't.
3. **Audit the knowledge base** — is your largest authority asset actually getting *retrieved* for how-to/problem prompts?
4. **Interlink from winners** — push authority from URLs AI already cites into under-retrieved pillar content.

---

## 6. From diagnosis to action layer

The deliverable is never "here's a PDF of problems". It is a **prioritized backlog**:

- **P0** — ship this week (entity, semantics, schema, hreflang).
- **P1** — next (localization, interlinking, earned citations).
- **P2** — backlog (404 cleanup, title/meta hygiene).

Each item carries a **pillar**, an **owner hint**, and an **effort estimate**, plus a **re-measurement** step: re-run the relevant Gauntlet prompts after changes ship to prove lift in Share of Voice.

---

## 7. Reproducibility checklist

- [ ] Define the prompt Gauntlet (e.g. 51 prompts across 5 query types) for the brand's category.
- [ ] Run on the target AI engine(s); log mention / citation / SoV / sentiment.
- [ ] Dual crawl (per locale) + CrUX pull.
- [ ] Map every finding to a pillar.
- [ ] Classify cited sources (owned / social / third-party).
- [ ] Produce P0/P1/P2 backlog with owners + effort.
- [ ] Schedule re-measurement to quantify lift.
