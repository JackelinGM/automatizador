# QA — Gotchas del dominio

## Estructura del reporte de defectos

El reporte generado por la IA debe seguir este formato exacto:

- **Título** — corto y descriptivo del defecto
- **Severidad** — Crítica / Alta / Media / Baja
- **Descripción** — contexto general del problema identificado
- **Pasos para reproducir** — secuencia numerada detallada
- **Resultado actual** — comportamiento observado durante la prueba
- **Resultado esperado** — comportamiento correcto esperado según la funcionalidad

## Prompt del sistema (PROMPT_QA)

```python
PROMPT_QA = (
    "Eres QA senior. Convierte la descripción del usuario en un reporte "
    "de bug con este formato Markdown:\n\n"
    "**Título:** [corto]\n"
    "**Severidad:** [Crítica/Alta/Media/Baja]\n"
    "**Descripción:** [contexto]\n"
    "**Pasos para reproducir:**\n"
    "1. [paso]\n"
    "**Resultado actual:** [lo observado]\n"
    "**Resultado esperado:** [lo esperado]\n\n"
    "Sé conciso. No inventes."
)
```

## Gotcha: system prompt largo + max_tokens corto = finish_reason: length

El system prompt y `max_tokens` comparten el mismo presupuesto. Si el prompt es verboso y `max_tokens` es bajo, el modelo consume todos los tokens disponibles en procesar las instrucciones y no genera respuesta. La API devuelve `finish_reason: "length"` con `content: None`.

**Solución:** prompt del sistema minimalista (~80 tokens), `max_tokens` configurable desde `.env` (default 3000).
