<!-- Idioma: Español | [English](./README.md) -->

# Auditoría y optimización GEO / Visibilidad en IA — Caso de estudio

> Un proyecto completo de Mes 1 para un SaaS B2B: medir la **visibilidad dentro de las respuestas de IA** (ChatGPT), auditar la base técnica, **rediseñar la home para GEO** y producir **contenido nuevo apto para IA** + un sistema operativo repetible.

🌐 **[Read in English →](./README.md)**

![tipo](https://img.shields.io/badge/tipo-caso--de--estudio-blue) ![area](https://img.shields.io/badge/area-GEO%20%2F%20Visibilidad%20IA-7c3aed) ![cliente](https://img.shields.io/badge/cliente-anonimizado-success)

---

## ⚠️ Sobre este caso de estudio

Pieza de portfolio. Al cliente se le nombra con el codename **«Plataforma de Visibilidad IA A»** — su nombre real, dominio, clientes y personas se omiten. Las *herramientas* competidoras sí se nombran porque son productos públicos y aportan contexto de mercado. Todas las métricas son reales, medidas en junio de 2026.

---

## Contexto

| | |
|---|---|
| **Cliente (codename)** | **Plataforma de Visibilidad IA A** — SaaS B2B en la categoría GEO / visibilidad en IA |
| **Sitio** | Web de marketing bilingüe (EN + ES), ~540 URLs |
| **Rol** | GEO & Content Lead — auditoría **y** capa de acción |
| **Motor medido** | ChatGPT (Gauntlet de 51 prompts) |
| **Duración** | Mes 1, ~4 h/día |

El **GEO (Generative Engine Optimization)** es la disciplina de conseguir que una marca sea citada y recomendada *dentro* de las respuestas generadas por IA — el sucesor del SEO clásico, donde el "clic" se sustituye a menudo por la recomendación de un modelo.

### El panorama competitivo
La Plataforma A compite en una categoría saturada, comparada con **herramientas GEO-nativas** (Profound, Peec AI, Otterly AI, Scrunch AI, Rankscale, AirOps, Conductor, Goodie AI, AthenaHQ) y **suites SEO clásicas que añaden "funciones GEO"** (Semrush, Ahrefs, SE Ranking, BrightEdge, Surfer, Frase). Las suites clásicas anuncian *millones* de keywords/prompts, pero en un nicho concreto la mayoría son irrelevantes u obsoletas; las plataformas GEO-nativas generan los prompts a partir de la **entidad, el contexto y el mercado** de la marca — la verdadera batalla.

---

## El problema

La Plataforma A vende software de visibilidad en IA, pero su **propia** web rendía mal en las consultas exactas que sus compradores hacen a los asistentes de IA. El encargo: diagnosticar *por qué* la marca era invisible en prompts genéricos/de categoría y entregar un plan de nivel operativo — no una auditoría puntual.

---

## Alcance del trabajo entregado (Mes 1)

Cuatro líneas, de la medición a los activos publicables:

| Línea | Qué entregué |
|-------|--------------|
| **1. Medición** | El **GEO Gauntlet** — 51 prompts en ChatGPT, puntuados por mención / citación / SoV / sentimiento, mapeados a 5 tipos de consulta y 4 pilares GEO. Reproducible (YAML + CSV + script de scoreboard). |
| **2. Auditoría técnica** | CrUX (Core Web Vitals) + doble rastreo EN/ES con Screaming Frog: silos i18n, fallos de HTML semántico, higiene de SERP, huella de rastreo del KB. |
| **3. Rediseño GEO de la home** | Reescritura sección a sección de la home (EN + ES) como **preview HTML**, subiendo la puntuación GEO on-page de **5,5 → 8,8**. `<h1>` real, módulos de producto citables, copy en español corregido, schema de Review/FAQ. |
| **4. Contenido + capa operativa** | Contenido nuevo apto para IA (blog EN + artículo de knowledge base ES), un plan de interlinking, plantillas de briefs y un protocolo operativo semanal con backlog P0/P1/P2. |

Detalle: **[RESULTS.es.md](./RESULTS.es.md)** (scoreboard) · **[HOMEPAGE_REDESIGN.es.md](./HOMEPAGE_REDESIGN.es.md)** (antes/después) · **[METHODOLOGY.es.md](./METHODOLOGY.es.md)** (cómo).

---

## Resultados medidos — el GEO Gauntlet (ChatGPT)

**51 prompts**, un solo motor, chat nuevo + memoria desactivada, texto exacto desde un YAML versionado.

| Métrica | Resultado |
|---------|-----------|
| Prompts completados | 51 / 51 |
| Mention rate | 49% (25/51) |
| Citation rate | 45% (23/51) |
| Branded citation rate | 83% (10/12) |

| Resultado | N |
|-----------|---|
| Victory | 20 |
| Defeat | 24 |
| Partial | 5 |
| Ignored | 2 |

### Por tipo de consulta
| Tipo | Balance | Citación |
|------|---------|----------|
| **Branded** | 10V · 1P · 1I | 83% |
| **Comparison** | 9V · 1D · 1P | Alta |
| **Category** | 0V · 7D · 2P · 1I | Baja |
| **How-to / problema** | 0V · 10D | **0%** |
| **Thought leadership** | 1V · 6D · 1P | Baja |

### Por pilar GEO
| Pilar | Cite rate | Lectura |
|-------|-----------|---------|
| Entidad | 82% (9/11) | Fuerte con desambiguación |
| Evidencia | 73% (11/15) | Fuerte en comparativas directas |
| Consenso | 20% (3/15) | Débil en shortlists / consultas de experto |
| Extractabilidad | **0%** (0/10) | El knowledge base nunca se recupera en how-to |

**El hallazgo central — dos regímenes de visibilidad:** la Plataforma A *gana* cuando el comprador ya conoce la marca o nombra un vendor (branded + comparativa). *Pierde* todo el funnel de **descubrimiento** — consultas genéricas de categoría y how-to, justo donde el comprador investiga *antes* de conocer la marca. El cuello de botella es el descubrimiento pre-marca, no la comparativa activa.

---

## Rediseño GEO de la home: **5,5 → 8,8**

Audité la home en vivo sección a sección y produje un **preview HTML** optimizado para GEO (EN + ES). Antes/después completo en **[HOMEPAGE_REDESIGN.es.md](./HOMEPAGE_REDESIGN.es.md)**.

| Pilar | Actual | Propuesto |
|-------|--------|-----------|
| Entidad | 6,5 | 9,0 |
| Extractabilidad | 4,0 | 8,5 |
| Evidencia | 5,5 | 8,5 |
| Consenso | 8,0 | 9,5 |
| **GEO Score** | **5,5** | **8,8** |

Claves del rediseño:
- **`<h1>` semántico real** con una definición de *categoría* («Plataforma de visibilidad en LLMs») en vez de un eslogan dentro de un `<div>` con estilo — para que la IA pueda copiar/parafrasear qué *es* el producto.
- **ICP movido a un kicker** sobre el H1, para que el público objetivo deje de competir con la definición de entidad.
- **Subtítulo factual**: 7 motores de IA nombrados + método + métricas (triples extraíbles).
- **Suite de producto reescrita** en 4 módulos citables, cada uno con copy operativo y CTA específico de intención.
- **Español corregido**: la home en vivo mostraba tokens de traducción automática rotos (fragmentos tipo *«…la plataforma por ti»*) que rompían el parseo de entidad.
- **Schema de Review + FAQ**, casos de éxito con una-métrica-una-entidad-un-enlace y una FAQ GEO-vs-SEO literalmente citable.

---

## Hallazgos técnicos

### Hallazgo 1 — El rendimiento *no* era el problema
Los Core Web Vitals pasaban en origen (LCP 1.392 ms · INP 66 ms · CLS 0,01). Esto redirigió todo el esfuerzo a **semántica, arquitectura y copy** en vez de a un inútil "proyecto de velocidad".

### Hallazgo 2 — EN y ES eran silos desconectados
El rastreo en inglés encontró **0** enlaces internos al árbol español, dejando huérfanas **~176 URLs en español**. El `hreflang` / `x-default` no estaba bien implementado → los motores de IA recibían señales de idioma contradictorias.

### Hallazgo 3 — Sin `<h1>` semántico
El titular de la home era un `<div>` con estilo, no un `<h1>` semántico — repetido en **7 URLs clave**. Los modelos que ponderan el primer bloque de encabezado no podían clasificar el tema de la página.

### Hallazgo 4 — Deuda de localización: el 87% de URLs ES tenían slug en inglés
De **219** URLs en español, **190 (87%)** tenían **slug en inglés sirviendo contenido íntegramente en español**. Construí un script para clasificar idioma-del-slug vs. idioma-del-contenido, marcar cada desajuste y **proponer un slug español limpio + mapa 301** para las 190. (Ver `tooling/`.)

### Hallazgo 5 — Deuda de enlaces rotos e higiene de SERP
Un rastreo completo de ~**540 URLs** detectó **~103 con 404** (≈19%). Además, títulos demasiado largos (**133/176 ES**, 49/177 EN sobre 60 caracteres), meta ausente en `/compare` y un slug de KB roto (`/%20ai-retrieval-layer`).

### Hallazgo 6 — El gap de citaciones (pilar Evidencia)
Citaciones **propias + sociales** fuertes pero **cero de terceros**, mientras los competidores aparecían en prensa y directorios. Un liderazgo en cuota de voz construido solo sobre tu dominio es frágil: se cae en cuanto un rival consigue cobertura editorial.

---

## Contenido nuevo y capa operativa producidos

No solo diagnóstico — activos publicables:

- **Borrador de blog EN** — *"AI Visibility for Small Marketing Teams: From Data to Weekly Actions"* — un bucle operativo semanal en 4 pasos (diseñado para ganar los prompts how-to/problema que puntuaron 0%).
- **Borrador de KB ES** — *"De citation gap a brief de contenido en 10 minutos"* — un flujo práctico y extraíble con plantilla de brief rellenable.
- **Plan de interlinking** — empujar autoridad desde URLs que ChatGPT *ya cita* (producto, MCP, pricing) hacia los pilares del KB poco recuperados, con anchor text recomendado.
- **Sistema operativo** — protocolo semanal, plantillas de brief y un backlog P0/P1/P2 ligado a prompts *concretos* que se perdían (no una checklist genérica), más un bucle de re-medición.

---

## Recomendaciones (priorizadas)

| Prioridad | Acción | Pilar | Responde a prompts |
|-----------|--------|-------|--------------------|
| **P0** | `<h1>` semántico real + copy de categoría en home (EN/ES) | Entity / Extractability | categoría, entidad |
| **P0** | `hreflang` EN↔ES + `x-default` + enlaces bidireccionales | Consensus | descubrimiento localizado |
| **P0** | Páginas how-to extraíbles en KB + FAQ schema, enlazadas desde URLs ya citadas | Extractability | 31–38 (la oleada del 0%) |
| **P1** | Conseguir citaciones de terceros (directorios, prensa, reseñas) | Evidence | experto / consenso |
| **P1** | Localizar 190 slugs ES (mapa 301 incluido) | Consensus | recuperación localizada |
| **P2** | Corregir 103× 404, higiene de title/meta, slugs rotos | Extractability | recuperación vía SERP |

---

## Competencias y herramientas demostradas

- **Estrategia GEO / AEO** — batería de 51 prompts, scoring por pilares, diagnóstico de dos regímenes, protocolo reproducible
- **SEO técnico** — doble rastreo con Screaming Frog, CrUX, hreflang, HTML semántico, higiene de SERP
- **Copywriting de conversión/GEO** — reescritura completa de la home (EN/ES) optimizada para extracción por LLM *y* para humanos
- **Producción de contenido** — blog + artículos KB aptos para IA, plantillas de brief, planes de interlinking
- **Tooling de datos** — crawler en Python + clasificador de idioma slug/contenido con propuestas 301 automáticas
- **Mentalidad de operador** — convertí el diagnóstico en un sistema P0/P1/P2 con responsables, esfuerzo y re-medición

**Stack:** Python (`requests`, `BeautifulSoup`, `csv`) · Screaming Frog · CrUX · ChatGPT · preview HTML/CSS · reporting en Markdown.

---

## Estructura del repo

```
geo-audit-case-study/
├── README.md / README.es.md          ← caso de estudio (EN / ES)
├── RESULTS.md / RESULTS.es.md         ← scoreboard completo del GEO Gauntlet
├── HOMEPAGE_REDESIGN.md / .es.md      ← home antes/después (5,5 → 8,8)
├── METHODOLOGY.md / METHODOLOGY.es.md ← Gauntlet, pilares, técnico, contenido
└── tooling/
    └── url_language_audit.py          ← crawler + clasificador de idioma slug/contenido
```

---

## Sobre mí

Especialista en GEO y contenido centrado en la **capa de acción**: no solo medir la visibilidad en IA, sino operarla — ejecutar los cambios técnicos, de diseño y de contenido que hacen que los motores de IA citen una marca. Abierto a roles de GEO / visibilidad en IA / SEO técnico.

*Cliente anonimizado. Este repositorio es una demostración de metodología y competencias.*
