# Memoria: Backend (Lógica de Negocio)

**Dominio:** Orquestación y lógica de la aplicación
**Fecha creación:** 2026-06-08

---

## Estado Actual

| Métrica | Valor |
|---------|-------|
| Funciones | 2 (consultar_ia, generar_defecto) |
| Validaciones | 1 (campo vacío) |
| Estados del botón | 2 (normal, disabled) |
| Errores manejados | 3 tipos |

## Historial de Cambios

### 2026-06-08 — Integración IA
- **Cambio:** `generar_defecto()` ahora llama a `consultar_ia()`
- **Cambio:** Botón se deshabilita durante consulta
- **Cambio:** Mensaje "Consultando IA..." mientras espera
- **Métrica antes:** Respuesta hardcodeada
- **Métrica después:** Respuesta dinámica de IA

## Flujo Actual

```
Usuario escribe defecto
  → generar_defecto() valida entrada
    → consultar_ia() envía a API
      → Respuesta se muestra en salida_texto
        → Botón se re-habilita
```

## Pendientes

- [ ] Separar en módulo `ia_service.py`
- [ ] Agregar persistencia (guardar/cargar defectos)
- [ ] Exportar reportes (PDF, Word)
- [ ] Logging de errores y métricas
