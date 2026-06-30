<!-- Idioma: Español | [English](./README.md) -->

# Auditoría GEO / Visibilidad en IA — Caso de estudio

> Cómo audité la web de un SaaS B2B para mejorar su **visibilidad dentro de las respuestas de IA** (ChatGPT, Perplexity, Google AI Overviews/Mode) y convertí los hallazgos en un plan de acción priorizado y listo para ejecutar.

🌐 **[Read in English →](./README.md)**

![tipo](https://img.shields.io/badge/tipo-caso--de--estudio-blue) ![area](https://img.shields.io/badge/area-GEO%20%2F%20Visibilidad%20IA-7c3aed) ![cliente](https://img.shields.io/badge/cliente-anonimizado-success)

---

## ⚠️ Sobre este caso de estudio

Es una **pieza de portfolio**. Al cliente se le nombra con el codename **«Plataforma de Visibilidad IA A»** — su nombre real y dominio se omiten. Los competidores sí se nombran porque son productos públicos y aportan contexto de mercado útil. Todas las métricas son reales.

---

## Contexto

| | |
|---|---|
| **Cliente (codename)** | **Plataforma de Visibilidad IA A** — SaaS B2B en la categoría GEO / visibilidad en IA |
| **Sitio** | Web de marketing bilingüe (EN + ES), ~540 URLs |
| **Rol** | GEO & Content Lead (auditoría + capa de acción) |
| **Motores analizados** | Perplexity, ChatGPT, Google AI Overviews y AI Mode |
| **Duración** | ~1 mes, a tiempo parcial |

El **GEO (Generative Engine Optimization)** es la disciplina de conseguir que una marca sea citada y recomendada *dentro* de las respuestas generadas por IA — el sucesor del SEO clásico, donde el "clic" se sustituye a menudo por la recomendación de un modelo.

### El panorama competitivo
La Plataforma A compite en una categoría saturada. La auditoría la comparó con:
- **Herramientas GEO-nativas:** Profound, Peec AI, Otterly AI, Scrunch AI, Rankscale, AirOps, Conductor, Knowatoa, LLM Pulse, xFunnel.
- **Suites SEO clásicas que añaden "funciones GEO":** Semrush, Ahrefs, SE Ranking, BrightEdge, Surfer SEO, Writesonic.

Esto importa: las suites clásicas anuncian *millones* de keywords/prompts, pero en un nicho concreto la mayoría son irrelevantes o están obsoletas. Las plataformas GEO-nativas, en cambio, generan los prompts a partir de la **entidad, el contexto y el mercado** de la marca — que es la verdadera batalla.

---

## El problema

La Plataforma A vende software de visibilidad en IA, pero su **propia** web rendía mal en las consultas exactas que sus compradores hacen a los asistentes de IA. El encargo: diagnosticar *por qué* la marca era invisible en prompts genéricos/de categoría y producir un plan de acción de nivel operativo — no una auditoría puntual.

---

## Metodología

Cuatro líneas de trabajo. Detalle completo en **[METHODOLOGY.es.md](./METHODOLOGY.es.md)**.

### 1. El GEO Gauntlet (batería de prompts)
Una batería estructurada de **20 prompts en 3 oleadas** (crítica / comercial / autoridad), mapeada por intención de funnel (TOFU · MOFU · BOFU) y por consultas branded vs. no-branded. Cada prompt se ejecuta contra motores de IA en vivo y se puntúa por:
- **Mención** — ¿aparece la marca?
- **Citación** — ¿se cita una URL propia como fuente?
- **Cuota de voz** — menciones de marca ÷ menciones totales vs. competidores.
- **Sentimiento** — endorsed / neutral / undermined, función por función.

### 2. Los 4 pilares GEO

| Pilar | Pregunta que responde |
|-------|------------------------|
| **Entity (Entidad)** | ¿Sabe la IA *quién* es la marca sin confundirla? |
| **Extractability (Extractabilidad)** | ¿Puede el modelo extraer datos limpiamente de la página? |
| **Evidence (Evidencia)** | ¿Hay pruebas (casos, datos, fuentes de terceros)? |
| **Consensus (Consenso)** | ¿Coinciden las señales en toda la web y entre idiomas? |

### 3. Auditoría técnica de base
Doble rastreo EN/ES, Core Web Vitals (datos de usuario real), semántica HTML, i18n/hreflang, higiene de SERP.

### 4. Análisis de contenido y gap de citaciones
Qué URLs cita *ya* la IA, dónde falta validación de terceros y por qué la base de conocimiento no se recupera.

---

## Hallazgos clave

### Puntuación GEO: **5,5 → 8,8** (proyectada)

| Pilar | Actual | Propuesto |
|-------|--------|-----------|
| Entity | 6,5 | 9,0 |
| Extractability | 4,0 | 8,5 |
| Evidence | 5,5 | 8,5 |
| Consensus | 8,0 | 9,5 |
| **Global** | **5,5** | **8,8** |

El mayor gap estaba en **Extractabilidad (+4,5)** — el pilar que más directamente controla si la IA te cita o te ignora.

### Hallazgo 1 — El rendimiento *no* era el problema
Los Core Web Vitals pasaban en origen (LCP 1.392 ms · INP 66 ms · CLS 0,01). Esto permitió redirigir todo el esfuerzo a **semántica, arquitectura y copy** en vez de a un inútil "proyecto de velocidad".

### Hallazgo 2 — EN y ES eran silos desconectados
El rastreo en inglés encontró **0** enlaces internos al árbol español, dejando huérfanas **~176 URLs en español**. El `hreflang` / `x-default` no estaba bien implementado → los motores de IA recibían señales de idioma contradictorias.

### Hallazgo 3 — Deuda de localización: el 87% de URLs ES tenían slug en inglés
De **219** URLs en español, **190 (87%)** tenían **slug en inglés sirviendo contenido íntegramente en español**. Construí un script para clasificar idioma-del-slug vs. idioma-del-contenido, marcar cada desajuste y **proponer un slug español limpio + mapa 301** para las 190. (Ver `tooling/`.)

### Hallazgo 4 — Deuda de enlaces rotos
Un rastreo completo de ~**540 URLs** detectó **~103 con 404** (≈19%) — presupuesto de rastreo desperdiciado y destinos de citación muertos.

### Hallazgo 5 — El gap de citaciones (pilar Evidencia)
En la auditoría de una marca piloto, esta tenía citaciones **propias + sociales** fuertes pero **cero citaciones de terceros**, mientras los competidores aparecían en prensa y directorios. Un liderazgo en cuota de voz construido solo sobre tu propio dominio es frágil: se desmorona en cuanto un rival consigue cobertura editorial.

### Hallazgo 6 — Sin `<h1>` semántico
El titular de la home era un `<div>` con estilo, no un `<h1>` semántico — repetido en **7 URLs clave**. Los modelos que ponderan el primer bloque de encabezado no podían clasificar el tema de la página.

---

## Recomendaciones (priorizadas)

| Prioridad | Acción | Pilar |
|-----------|--------|-------|
| **P0** | `<h1>` semántico real con copy de categoría en home (EN/ES) | Entity / Extractability |
| **P0** | `hreflang` EN↔ES + `x-default` + enlaces bidireccionales | Consensus |
| **P0** | Schema de Review/Organization + prueba social estructurada | Entity / Evidence |
| **P1** | Localizar 190 slugs ES (mapa 301 incluido) | Consensus |
| **P1** | Interlinking de pilares KB desde URLs que la IA ya cita | Extractability |
| **P1** | Conseguir citaciones de terceros (prensa, directorios) | Evidence |
| **P2** | Corregir 103× 404, higiene de title/meta, slugs rotos | Extractability |

---

## Competencias y herramientas demostradas

- **Estrategia GEO / AEO** — baterías de prompts, scoring por pilares, medición multi-motor
- **SEO técnico** — doble rastreo con Screaming Frog, CrUX, hreflang, HTML semántico
- **Tooling de datos** — crawler en Python + clasificador de desajuste de idioma (slug vs. contenido) con propuestas 301 automáticas
- **Análisis** — cuota de voz, gap de citaciones y análisis de sentimiento vs. competidores
- **Mentalidad de operador** — convertí el diagnóstico en un plan P0/P1/P2 con responsables y esfuerzo

**Stack:** Python (`requests`, `BeautifulSoup`, `csv`) · Screaming Frog · CrUX · motores de IA en vivo · reporting en Markdown.

---

## Estructura del repo

```
geo-audit-case-study/
├── README.md           ← caso de estudio (English)
├── README.es.md        ← caso de estudio (Español)
├── METHODOLOGY.md      ← GEO Gauntlet, pilares, scoring (EN)
├── METHODOLOGY.es.md   ← metodología (ES)
├── LINKEDIN_POST.md    ← resumen listo para publicar (EN + ES)
└── tooling/
    └── url_language_audit.py   ← crawler + clasificador de idioma slug/contenido
```

---

## Sobre mí

Especialista en GEO y contenido centrado en la **capa de acción**: no solo medir la visibilidad en IA, sino operarla — ejecutar los cambios estructurales y de contenido que hacen que los motores de IA citen una marca. Abierto a roles de GEO / visibilidad en IA / SEO técnico.

*Cliente anonimizado. Este repositorio es una demostración de metodología y competencias.*
