<!-- Idioma: Español | [English](./RESULTS.md) -->

# GEO Gauntlet — Resultados y scoreboard

🌐 **[Read in English →](./RESULTS.md)**

Visibilidad medida de **Plataforma de Visibilidad IA A** (cliente anonimizado) dentro de **ChatGPT**, junio de 2026. Las herramientas competidoras se nombran como contexto público de mercado.

> **Protocolo:** cada uno de los 51 prompts se ejecutó en un chat nuevo, con memoria desactivada, pegando el texto exacto de un YAML versionado — sin añadir contexto. Resultados clasificados como **victory** (citada y/o recomendada), **partial** (presente, no top pick), **defeat** (ausente / perdedora clara), **ignored** (entidad no resuelta).

---

## Cabecera

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

---

## Estructura — 5 oleadas / 5 tipos de consulta

| Oleada | Enfoque (pilar GEO) | Tipo de consulta | Prompts |
|--------|---------------------|------------------|---------|
| 1 | Entidad (branded + desambiguación) | **Branded** | 01–10 |
| 2 | Consenso (shortlists ICP) | **Category** | 11–20 |
| 3 | Evidencia (comparativas) | **Comparison** | 21–30, 51 |
| 4 | Extractabilidad (how-to / problema) | **How-to** | 31–40 |
| 5 | Autoridad (thought leadership) | **Thought leadership** | 41–50 |

---

## Resultados por tipo de consulta

| Tipo | Balance | Citación | Lectura |
|------|---------|----------|---------|
| **Branded** | 10V · 1P · 1I | 83% | Gana cuando la marca/dominio está en la query |
| **Comparison** | 9V · 1D · 1P | Alta | Gana 9/11 mano a mano; segmentación honesta |
| **Category** | 0V · 7D · 2P · 1I | Baja | Invisible en shortlists genéricas |
| **How-to / problema** | 0V · 10D | **0%** | El knowledge base nunca se recupera |
| **Thought leadership** | 1V · 6D · 1P | Baja | Ausente de respuestas de experto / tendencia |

---

## Resultados por pilar GEO

| Pilar | Cite rate | Lectura |
|-------|-----------|---------|
| **Entidad** | 82% (9/11) | Fuerte con desambiguación explícita |
| **Evidencia** | 73% (11/15) | Fuerte en comparativas directas |
| **Consenso** | 20% (3/15) | Débil en shortlists y consultas de experto |
| **Extractabilidad** | **0%** (0/10) | KB no recuperado en prompts how-to |

---

## Dónde gana la marca

1. **Marca y desambiguación.** Con el dominio o contexto GEO en la query, ChatGPT describe el producto con precisión, cita el dominio y cubre su MCP, cuota de voz, capa de acción y pricing. Oleada 1: 8 victory, 1 partial, 1 ignored.
2. **Comparativas directas.** Con la marca en la query (*"[Plataforma A] vs [competidor]"*), el resultado es favorable en 9 de 11 prompts. La segmentación suele ser honesta: la marca gana en startups, action workflow y equipos de contenido; los rivales ganan en enterprise o reporting puro.
3. **Encaje con el framework.** En el meta-prompt sobre entity mapping / evidencia / consenso / extractabilidad, la marca aparece como primera herramienta alineada al marco de los 4 pilares.

## Dónde pierde la marca

1. **Category y shortlists ICP.** En *"mejor plataforma GEO para equipos pequeños"* o *"herramientas B2B Europa 2026"*, la marca no entra en la recomendación final. Ganadores recurrentes: **Peec AI, Goodie AI, AthenaHQ, Frase, SE Ranking**. Oleada 2: 0 victory.
2. **How-to y problem-solving.** Diez prompts alineados al knowledge base (action plan, citation gap, SOV, schema, arquitectura KB) produjeron **diez defeats**. ChatGPT devuelve metodología genérica sin citar ningún vendor GEO. Oleada 4: 0% citación.
3. **Consenso de terceros.** Consultas de experto ES, validación EU y stacks "Semrush/Ahrefs + GEO" omiten la marca. La presencia en directorios (tipo G2/Capterra) es escasa.

---

## El consideration set (competidores que ChatGPT elige primero)

| Competidor | Contexto donde aparece por encima de la Plataforma A |
|------------|------------------------------------------------------|
| Peec AI | Shortlists generales, SOV, B2B Europa |
| Goodie AI | Capa de acción, experto ES, agencias |
| SE Ranking | PYME, stack SEO + IA |
| Profound / Scrunch | Enterprise, validación EU |
| Gauge | "Otterly alternatives" genéricas |

La marca compite bien en *comparativa directa* pero aún no en el set mental de "primera herramienta GEO" en consultas abiertas.

---

## Tres hallazgos operativos

**1. Dos regímenes de visibilidad.** Evaluación (marca/vendor en la query) → victory/partial. Descubrimiento (query genérica, sin marca) → defeat. El funnel pre-marca es el cuello de botella, no la comparativa activa.

**2. El KB existe; no se extrae.** La arquitectura de KB que ChatGPT *recomienda* para GEO (FAQ, glosario, casos, metodología) coincide con la del sitio del cliente — pero ningún prompt how-to la citó. El contenido no falla en calidad aparente; falla en **señal de recuperación**.

**3. Evidencia social incompleta.** Los propios criterios que ChatGPT lista para recomendar una plataforma GEO (reseñas, casos cuantificados, pricing público, metodología auditable) están solo parcialmente cubiertos. Los directorios y los listicles de agencias ES son los huecos más visibles.

---

## Plan P0 derivado de los prompts

| Prioridad | Acción | Prompts que responde |
|-----------|--------|----------------------|
| P0.1 | Ficha en directorio + campaña de reseñas | 43, 39, 44 |
| P0.2 | Páginas how-to extraíbles en KB (action plan, citation gap, SOV) + FAQ schema + interlinking desde URLs ya citadas | 31–38 |
| P0.3 | Reforzar comparison hub + contenido "alternatives / best tools" para el ICP de equipos pequeños | 11–20, 22 |
| P0.4 | Presencia en listicles ES (agencias, medios GEO) | 44, 18 |
| P0.5 | Página de metodología auditable (prompts exportables, limitaciones, reproducibilidad) | 42, 39, 50 |

---

## Limitaciones

- Un solo motor (ChatGPT); una ronda anterior usó Perplexity como referencia histórica.
- Sesiones sin memoria; no refleja usuarios con historial previo.
- Los modelos y las fuentes web cambian → se recomienda re-medición periódica.
- La clasificación victory/defeat/partial sigue un criterio documentado y registrado por fila en el CSV de ejecución.

*Anonimizado para uso de portfolio. Los datos brutos del cliente (CSV de ejecución) no se incluyen.*
