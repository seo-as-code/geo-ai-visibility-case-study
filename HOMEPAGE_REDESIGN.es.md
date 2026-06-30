<!-- Idioma: Español | [English](./HOMEPAGE_REDESIGN.md) -->

# Rediseño GEO de la home — Actual vs Propuesta

🌐 **[Read in English →](./HOMEPAGE_REDESIGN.md)**

Reescritura sección a sección de la home de **Plataforma de Visibilidad IA A** (anonimizada), entregada como **preview HTML** interactivo en EN y ES. Objetivo: convertir una página de marketing en algo que una IA pueda **leer, clasificar y citar**.

> La home propuesta fue una **muestra / preview**, no se desplegó en producción. Los nombres de clientes, marcas de testimonios y personas se han anonimizado.

---

## Puntuación GEO on-page: 5,5 → 8,8

| Pilar | Qué necesita la IA | Actual | Propuesto |
|-------|--------------------|--------|-----------|
| **Entidad** | "X = software SaaS", personas/marcas enlazadas | 6,5 | 9,0 |
| **Extractabilidad** | Frases completas, verbos, listas citables | 4,0 | 8,5 |
| **Evidencia** | Número + marca + resultado en un bloque | 5,5 | 8,5 |
| **Consenso** | Terminología 2026 consistente (GEO, MCP, motores) | 8,0 | 9,5 |
| **GEO Score** | | **5,5** | **8,8** |

---

## El problema de fondo de la home en vivo

El hero en vivo usaba un **`<div>` con estilo**, no un `<h1>` semántico, y el titular era una *promesa de marketing* ("10x your AI visibility. Built for small marketing teams") en vez de una *definición de entidad*. Además, gran parte de la página en español era **traducción automática rota** — el nombre de la marca aparecía a mitad de frase como si fuera un verbo o preposición, lo que destruye el parseo de entidad (NER) y la extracción RAG.

**SEO clásico vs GEO:** en SEO, un H1 emocional puede ganar CTR en la SERP. En GEO, ese mismo H1 es el **chunk primario** que el modelo lee para decidir si te cita o te recomienda. Si el chunk es un eslogan, no es citable como definición de producto.

---

## Sección a sección: antes → después

### S1 — Hero
| | Actual | Propuesto |
|---|--------|-----------|
| H1 | Eslogan en `<div>`: *"10x your AI visibility"* | `<h1>` real: **"Plataforma de visibilidad en LLMs"** |
| ICP | Dentro del H1 ("para equipos pequeños") | Movido a un **kicker** sobre el H1 |
| Subtítulo | Español roto, "5%/95%" no verificable | Factual: **7 motores nombrados** + método (navegadores reales) + métricas (menciones, citas, SOV) |

**Por qué:** el primer bloque funciona ahora como una entrada de Wikipedia interna — *definición + prueba de categoría* — un fragmento que el modelo puede copiar al clasificar el producto en una shortlist.

### S4 — Suite de producto
- **Actual:** cuatro tarjetas, tres con copy en español roto, un único CTA genérico "Learn more", módulos reales sin nombrar.
- **Propuesto:** un H2 de **suite de Analytics** + cuatro módulos citables — *Prompt Discovery · Visibility Tracking · Monitor · Advanced Insights* — cada uno con copy operativo y CTA específico de intención.

### S5 — MCP (Model Context Protocol)
- **Actual:** frases sin verbos claros; el diferenciador que *gana* en el Gauntlet es invisible.
- **Propuesto:** sección MCP nombrada con **strings de prompt reales** (*"¿En qué respuestas nos citan menos que [competidor] esta semana?"*) y un flujo de 3 pasos conectar → preguntar → actuar. Alinea la página con el mejor resultado del Gauntlet.

### S6 — Reseñas
- **Actual:** tokens rotos dentro de las citas, carrusel **duplicado 2× en el DOM**, sin H2, sin enlaces.
- **Propuesto:** H2 "Opiniones de clientes", `H3 nombre + rol + blockquote` limpio, enlace al caso de éxito, **schema de Review**, una sola pasada de carrusel.

### S7 — Casos de éxito
- **Actual:** métricas cruzadas entre clientes equivocados; una persona con el cargo erróneo; grafo entidad↔número roto (riesgo de alucinación).
- **Propuesto:** **una métrica = una entidad = un enlace**. Cliente A (+11,79% visibilidad IA) y Cliente B (+45% tráfico referido desde IA), cada uno anclado a su propio caso, evitando la contaminación cruzada.

### S8 — Sentimiento / Context Analysis
- **Actual:** H2 vago, falta la palabra *reputación*, capturas en inglés en la página española.
- **Propuesto:** H2 "Audita la reputación de tu marca en IA", pilares (Pricing, Soporte, UX, Integraciones), 7 motores nombrados, assets localizados.

### S10 — Pricing
- **Actual:** sin bloque de pricing en el scroll de la home.
- **Propuesto:** tres planes con **números concretos** (ilustrativo: 79 € / 279 € / 499 €) y público + señales clave — justo lo que necesitan recuperar las consultas de categoría tipo *"mejor herramienta GEO para agencias"*.

### S12 — FAQ
- **Actual:** gramática rota, *AEO* en vez de *GEO*, verbos ausentes → no citable literalmente.
- **Propuesto:** pares Q&A limpios, **GEO vs SEO** definido, mención-vs-citación explicado, plazos honestos → pasa de parche a fuente primaria citable.

---

## Qué demuestra el rediseño

- Copywriting GEO que sirve **a la vez** a la IA (entidad + evidencia extraíbles) y al humano (propuesta de valor clara).
- Traducir una auditoría (técnica + Gauntlet) en **copy concreto a nivel de página**, no consejos abstractos.
- Disciplina de locale: corregir el ES roto, nombrar motores, localizar prueba y assets.
- Schema y HTML semántico como palancas GEO de primera clase, no como añadidos.

*Anonimizado para uso de portfolio. El propio preview HTML no se incluye para proteger los activos de marca del cliente.*
