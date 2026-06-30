<!-- Language: English | [Español](./HOMEPAGE_REDESIGN.es.md) -->

# Homepage GEO Redesign — Live vs Proposed

🌐 **[Leer en Español →](./HOMEPAGE_REDESIGN.es.md)**

A section-by-section rewrite of the homepage of **AI Visibility Platform A** (anonymized), delivered as an interactive **HTML preview** in EN and ES. Goal: turn a marketing page into something an LLM can **read, classify and cite**.

> The proposed homepage was a **sample / preview**, not deployed to production. Customer names, testimonial brands and people have been anonymized.

---

## On-page GEO score: 5.5 → 8.8

| Pillar | What LLMs need | Live | Proposed |
|--------|----------------|------|----------|
| **Entity** | "X = SaaS software", people/brands linked | 6.5 | 9.0 |
| **Extractability** | Complete sentences, verbs, citable lists | 4.0 | 8.5 |
| **Evidence** | Number + brand + outcome in one block | 5.5 | 8.5 |
| **Consensus** | Consistent 2026 terminology (GEO, MCP, engines) | 8.0 | 9.5 |
| **GEO Score** | | **5.5** | **8.8** |

---

## The core problem with the live homepage

The live hero used a **styled `<div>`**, not a semantic `<h1>`, and the headline was a *marketing claim* (“10x your AI visibility. Built for small marketing teams”) rather than an *entity definition*. On top of that, large parts of the Spanish page were **broken machine translation** — the brand name appeared mid-sentence as if it were a verb or preposition, which destroys entity parsing (NER) and RAG extraction.

**Classic SEO vs GEO:** in SEO, an emotional H1 can win SERP click-through. In GEO, that same H1 is the **primary chunk** the model reads to decide whether to cite or recommend you. If the chunk is a slogan, it is not citable as a product definition.

---

## Section-by-section: before → after

### S1 — Hero
| | Live | Proposed |
|---|------|----------|
| H1 | `<div>` slogan: *"10x your AI visibility"* | Real `<h1>`: **"Platform for visibility in LLMs"** / *"Plataforma de visibilidad en LLMs"* |
| ICP | Inside the H1 ("for small teams") | Moved to a **kicker** above the H1 |
| Subhead | Broken Spanish, unverifiable "5%/95%" | Factual: **7 named engines** + method (real browsers) + metrics (mentions, citations, SOV) |

**Why:** the first block now works like an internal Wikipedia entry — *definition + category proof* — a fragment the model can copy when classifying the product in a shortlist.

### S4 — Product suite
- **Live:** four cards, three with broken Spanish copy, a single generic "Learn more" CTA, real modules not named.
- **Proposed:** an **Analytics suite** H2 + four citable modules — *Prompt Discovery · Visibility Tracking · Monitor · Advanced Insights* — each with operational copy and an intent-specific CTA.

### S5 — MCP (Model Context Protocol)
- **Live:** sentences without clear verbs; the differentiator that *wins* in the Gauntlet is invisible.
- **Proposed:** named MCP section with **real prompt strings** (*"In which answers are we cited less than [competitor] this week?"*) and a 3-step connect → ask → act flow. Aligns the page with the brand's strongest Gauntlet result.

### S6 — Reviews
- **Live:** broken tokens inside quotes, carousel **duplicated 2× in the DOM**, no H2, no links.
- **Proposed:** "Customer reviews" H2, clean `H3 name + role + blockquote`, link to case study, **Review schema**, single carousel pass.

### S7 — Case studies
- **Live:** metrics crossed between the wrong customers; a person shown with the wrong job title; broken entity↔number graph (hallucination risk).
- **Proposed:** **one metric = one entity = one link**. Customer A (+11.79% AI visibility) and Customer B (+45% referred traffic from AI) each anchored to their own case, preventing cross-contamination.

### S8 — Sentiment / Context Analysis
- **Live:** vague H2, the keyword *reputation* missing, English screenshots on the Spanish page.
- **Proposed:** "Audit your brand reputation in AI" H2, pillars (Pricing, Support, UX, Integrations), 7 engines named, localized assets.

### S10 — Pricing
- **Live:** no pricing block on the homepage scroll.
- **Proposed:** three tiers with **concrete numbers** (illustrative: €79 / €279 / €499) and audience + key signals — exactly what *"best GEO tool for agencies"* category queries need to retrieve.

### S12 — FAQ
- **Live:** broken grammar, *AEO* instead of *GEO*, missing verbs → not literally citable.
- **Proposed:** clean Q&A pairs, **GEO vs SEO** defined, mention-vs-citation explained, honest timelines → graduates from a patch to a primary citable source.

---

## What the redesign demonstrates

- GEO copywriting that serves **both** the LLM (extractable entity + evidence) and the human (clear value proposition).
- Translating an audit (technical + Gauntlet) into **concrete page-level copy**, not abstract advice.
- Locale discipline: fixing broken ES, naming engines, localizing proof and assets.
- Schema and semantic HTML as first-class GEO levers, not afterthoughts.

*Anonymized for portfolio use. The HTML preview itself is not included to protect the client's brand assets.*
