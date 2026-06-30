<!-- Idioma: Español | [English](./METHODOLOGY.md) -->

# Metodología — Auditoría GEO / Visibilidad en IA

🌐 **[Read in English →](./METHODOLOGY.md)**

Este documento explica *cómo* se realizó la auditoría del [caso de estudio](./README.es.md), para que el enfoque sea reproducible en cualquier marca. El cliente está anonimizado (codename **«Plataforma de Visibilidad IA A»**); los competidores se nombran como contexto público de mercado.

---

## 1. Para qué optimizamos

El SEO clásico optimiza para **clics** desde una página de resultados. El GEO (Generative Engine Optimization) optimiza para **menciones y recomendaciones dentro de las respuestas de IA** — con frecuencia sin ningún clic.

La unidad de medida cambia de *keyword → posición de ranking* a **prompt → presencia en la respuesta**. Ese único cambio determina toda la metodología.

---

## 2. El GEO Gauntlet (batería de prompts)

Una batería curada de prompts que imita cómo un comprador real interroga a un asistente de IA sobre una categoría y una marca.

### Estructura
- **20 prompts**, agrupados en **3 oleadas**:
  - **Oleada 1 — Crítica**: branded + desambiguación + reputación.
  - **Oleada 2 — Comercial**: categoría, comparación, intención "mejor herramienta para X".
  - **Oleada 3 — Autoridad**: liderazgo de opinión / how-to / planteamiento de problemas.
- Cada prompt etiquetado por **intención de funnel**: TOFU · MOFU · BOFU.
- Cada prompt etiquetado **branded** vs. **no-branded**.

### Por qué importan las oleadas
Las marcas casi siempre ganan los prompts **branded + dominio explícito** y pierden los **genéricos / de categoría** — que es justo donde el comprador investiga *antes* de conocer la marca. Separar por oleadas hace ese punto ciego medible.

### Métricas por prompt × motor
| Métrica | Definición |
|---------|------------|
| **Mención** | La marca aparece en la respuesta (sí/no). |
| **Citación** | Se usa una URL propia como fuente. |
| **Cuota de voz (SoV)** | Menciones de marca ÷ menciones totales en el conjunto de respuestas. |
| **Sentimiento** | Por función: *endorsed* / *neutral* / *undermined*. |
| **Fuentes citadas** | Las URLs reales que usó el motor (propias / sociales / terceros). |

Motores analizados: **Perplexity, ChatGPT, Google AI Overviews, Google AI Mode** (ampliable a Claude, Gemini, Copilot, Grok).

---

## 3. Los 4 pilares GEO

Cada hallazgo y recomendación se mapea a un pilar, para que el cliente sepa siempre *por qué* importa un arreglo.

### Entity (Entidad)
¿Identifica la IA correctamente *quién eres*?
Señales: `<h1>` semántico, schema `Organization`/`sameAs`, naming consistente, desambiguación de entidades con nombre similar.

### Extractability (Extractabilidad)
¿Puede un modelo extraer datos limpiamente de tu página?
Señales: encabezados limpios, frases declarativas completas, datos estructurados, contenido modular apto para fragmentos, sin copy roto.

### Evidence (Evidencia)
¿Hay pruebas en las que el modelo pueda confiar?
Señales: casos de éxito, datos y sobre todo **citaciones de terceros** (prensa, directorios, reseñas) — no solo páginas propias.

### Consensus (Consenso)
¿Coinciden las señales en toda la web y entre idiomas?
Señales: `hreflang`, terminología consistente, presentación de SERP alineada, acuerdo entre fuentes propias y ganadas.

---

## 4. Auditoría técnica de base

| Capa | Herramienta | Qué nos dice |
|------|-------------|--------------|
| Rendimiento real | **CrUX** (Core Web Vitals) | ¿La velocidad es un bloqueo? (A menudo *no* — no sobreinvertir.) |
| Arquitectura de rastreo | **Screaming Frog** (doble rastreo EN + ES) | ¿Idiomas en silos? ¿URLs huérfanas? |
| Semántica on-page | SF + manual | `<h1>` semántico, orden de encabezados, claridad temática. |
| i18n | SF + manual | `hreflang` / `x-default`, enlazado entre idiomas. |
| Higiene SERP | SF | Longitud de títulos, meta faltante, slugs rotos. |

**Por qué doble rastreo:** un rastreo solo en inglés puede no descubrir nunca el árbol español vía enlaces internos, infrarreportando todo el conjunto de activos localizados.

---

## 5. Análisis de contenido y gap de citaciones

1. **Mapear lo que la IA ya cita** — URLs propias vs. sociales vs. terceros.
2. **Encontrar el gap de citaciones** — dónde los competidores tienen validación de terceros y tú no.
3. **Auditar la base de conocimiento** — ¿tu mayor activo de autoridad se está *recuperando* para prompts how-to/problema?
4. **Interlinking desde los ganadores** — empujar autoridad desde URLs que la IA ya cita hacia el contenido pilar poco recuperado.

---

## 6. Del diagnóstico a la capa de acción

El entregable nunca es "aquí tienes un PDF de problemas". Es un **backlog priorizado**:

- **P0** — desplegar esta semana (entidad, semántica, schema, hreflang).
- **P1** — siguiente (localización, interlinking, citaciones ganadas).
- **P2** — backlog (limpieza de 404, higiene de title/meta).

Cada ítem lleva un **pilar**, una **pista de responsable** y una **estimación de esfuerzo**, más un paso de **re-medición**: volver a ejecutar los prompts relevantes del Gauntlet tras desplegar los cambios para demostrar el avance en cuota de voz.

---

## 7. Checklist de reproducibilidad

- [ ] Definir el Gauntlet de 20 prompts para la categoría de la marca.
- [ ] Ejecutar en ≥2 motores de IA; registrar mención / citación / SoV / sentimiento.
- [ ] Doble rastreo (por idioma) + extracción de CrUX.
- [ ] Mapear cada hallazgo a un pilar.
- [ ] Clasificar las fuentes citadas (propias / sociales / terceros).
- [ ] Producir backlog P0/P1/P2 con responsables + esfuerzo.
- [ ] Programar re-medición para cuantificar el avance.
