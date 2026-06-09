# Memoria: IA (Integración con LLM)

**Dominio:** Conexión con OpenCode Go API
**Fecha creación:** 2026-06-08

---

## Estado Actual

| Métrica | Valor |
|---------|-------|
| Proveedor | OpenCode Go |
| Modelo | deepseek-v4-flash |
| Endpoint | /v1/chat/completions |
| Max tokens | 4000 |
| Temperature | 0.7 |
| Tipos de error manejados | 3 |

## Historial de Cambios

### 2026-06-08 — Fix: max_tokens insuficiente
- **Problema:** Respuesta vacía de la IA (content='')
- **Causa:** deepseek-v4-flash gasta tokens en reasoning_content
- **Tokens de reasoning:** ~120-150 por consulta
- **Solución:** max_tokens 1500 → 4000
- **Métrica antes:** 1500 tokens, 0% éxito
- **Métrica después:** 4000 tokens, 100% éxito
- **Gotcha documentado:** Modelos de razonamiento necesitan 3x más tokens

### 2026-06-08 — Creación inicial
- **Cambio:** Integración con OpenCode Go via SDK openai
- **Decisión:** Usar cliente OpenAI compatible (no requests directo)
- **Razón:** Mejor abstracción, manejo de errores tipado

## Prompt Actual

```
Eres un experto en testing de software que genera reportes de defectos profesionales.
4 secciones: DESCRIPCIÓN, PASOS, RESULTADO ACTUAL, RESULTADO ESPERADO.
```

## Pendientes

- [ ] Agregar retry logic con backoff exponencial
- [ ] Evaluar calidad de respuestas (rating post-generación)
- [ ] Probar con otros modelos (qwen3.6-plus, mimo-v2.5)
- [ ] Agregar cache de reportes frecuentes
