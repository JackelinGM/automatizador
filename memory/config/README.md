# Memoria: Configuración

**Dominio:** Variables de entorno y dependencias
**Fecha creación:** 2026-06-08

---

## Estado Actual

| Métrica | Valor |
|---------|-------|
| Variables de entorno | 3 |
| Dependencias explícitas | 3 (tkinter, openai, dotenv) |
| Archivos config | 2 (.env, requirements.txt) |

## Variables de Entorno

| Variable | Propósito | Ejemplo |
|----------|-----------|---------|
| `OPENCODE_API_KEY` | Clave de autenticación | sk-... |
| `OPENCODE_BASE_URL` | Endpoint de la API | https://opencode.ai/zen/go/v1 |
| `OPENCODE_MODEL` | Modelo a utilizar | deepseek-v4-flash |

## Dependencias

| Paquete | Versión | Uso |
|---------|---------|-----|
| tkinter | (stdlib) | GUI |
| openai | >=1.0.0 | Cliente API |
| python-dotenv | >=1.0.0 | Carga de .env |

## Historial de Cambios

### 2026-06-08 — Creación inicial
- **Cambio:** Archivo `.env` con 3 variables
- **Cambio:** `requirements.txt` con dependencias esenciales
- **Decisión:** `.gitignore` excluye `.env` (secreto)

## Pendientes

- [ ] Agregar variable `LOG_LEVEL` para debug
- [ ] Documentar setup en README.md
- [ ] Agregar validación de .env al inicio de la app
