# Memoria: GUI (Interfaz Gráfica)

**Dominio:** Interfaz de usuario con Tkinter
**Fecha creación:** 2026-06-08

---

## Estado Actual

| Métrica | Valor |
|---------|-------|
| Líneas UI | ~86 |
| Widgets totales | 7 |
| Tema | Oscuro (#0D0D0D) |
| Layout | pack() |

## Historial de Cambios

### 2026-06-08 — Integración IA
- **Cambio:** Se agregó `modelo_label` para mostrar el modelo activo
- **Cambio:** Se aumentó ventana de 700x600 a 750x650
- **Métrica antes:** 7 widgets, 700x600
- **Métrica después:** 8 widgets, 750x650
- **Decisión:** Mantener pack() por simplicidad en prototipo

## Pendientes

- [ ] Separar UI de lógica de negocio (módulo independiente)
- [ ] Agregar scrollbar horizontal al ScrolledText de salida
- [ ] Soporte para copiar reporte al portapapeles con un click
