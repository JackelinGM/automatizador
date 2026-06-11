# Memory — Registro del Proyecto

**Proyecto:** Automatizador de Defectos
**Fecha creación:** 2026-06-08
**Última actualización:** 2026-06-11

---

## Estado actual

✅ Interfaz gráfica funcional con CustomTkinter (tema oscuro, dos paneles).
✅ API de IA integrada y generando reportes correctamente con la estructura:
   Título, Severidad, Descripción, Pasos para reproducir, Resultado actual y esperado.
✅ Botón "Nuevo defecto" con confirmación para limpiar y empezar de cero.
✅ Prompt del agente `python-dev` mejorado con reglas anti-asunción.
✅ `max_tokens` configurable desde `.env` (default 3000).

## Resumen de cambios

| Fecha | Descripción |
|-------|-------------|
| 2026-06-08 | Creación inicial del proyecto con interfaz UI en CustomTkinter |
| 2026-06-08 | Integración con OpenCode Go API (configuración) |
| 2026-06-09 | Reestructuración del proyecto: limpieza de archivos huérfanos y documentación |
| 2026-06-11 | Prompt del agente python-dev mejorado (reglas anti-asunción, estructura real) |
| 2026-06-11 | Botón "Copiar" reemplazado por "Nuevo defecto" con confirmación |
| 2026-06-11 | Eliminado `utils/portapapeles.py` (no se usaba) |
| 2026-06-11 | Fix: system prompt acortado y `max_tokens` configurable (soluciona `Finish reason: length`) |
| 2026-06-11 | Validación de respuesta vacía de la IA + debug en consola |

## Historial de commits

| Fecha | Commit | Descripción |
|-------|--------|-------------|
| 2026-06-08 | `0306e01` | Integración con OpenCode Go API |
| 2026-06-11 | — | Mejora de prompt del agente, fix de IA, botón "Nuevo defecto" |
