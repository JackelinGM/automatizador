# AGENTS.md — Automatizador de Defectos

## Identidad

App de escritorio Python + CustomTkinter que recibe descripciones informales de bugs y genera reportes técnicos estructurados con IA (API OpenAI-compatible).

## Regla de oro: PREGUNTAR, NUNCA ASUMIR

Cuando no tengas certeza absoluta, PREGUNTA al usuario. No avances sin respuesta clara. Pregunta obligatoriamente si:
- La instrucción es ambigua o admite múltiples interpretaciones
- Necesitas crear un archivo nuevo y no sabes dónde o cómo llamarlo
- No sabes qué librería, versión o enfoque prefiere el usuario
- El código existente usa un patrón que no comprendes
- El usuario pide algo que contradice la estructura actual

Sé específico al preguntar: explica qué no entiendes y ofrece opciones concretas.

Nunca inventes nombres de archivos, variables ni clases. No asumas librerías no listadas en `requirements.txt`. No asumas la intención del usuario si el mensaje es vago. No cambies patrones existentes sin advertir primero.

## Stack

- Python 3.x
- CustomTkinter >= 5.2.0 (GUI, tema oscuro)
- OpenAI >= 1.0.0 (API compatible OpenAI-like)
- httpx (cliente HTTP con control SSL)
- python-dotenv (carga `.env`)

## Convenciones

- CustomTkinter **siempre**, nunca Tkinter estándar (`import customtkinter as ctk`)
- Nombres descriptivos en español
- Docstrings en español para clases/funciones públicas
- Sin comentarios innecesarios (código debe ser auto-explicativo)
- Tema oscuro fijo, colores desde `config.py` — no hardcodear colores
- Separación estricta: `ia/` y `utils/` **no** importan `customtkinter`
- `.env` nunca se commitea, secretos nunca se exponen

## Estructura

```
automatizador.py    → Punto de entrada (main, configura tema, lanza app)
app.py              → UI con CustomTkinter (AutomatizadorApp)
config.py           → Constantes, paleta de colores, carga .env
ia/cliente.py       → Cliente IA (OpenAI + httpx, prompt QA, validación)
utils/              → Utilidades puras (sin dependencia de UI)
.opencode/          → Config de opencode (no modificar sin preguntar)
  agents/           → Prompts de agentes especializados
  memory/           → Gotchas por dominio (consultar al tocar cada área)
```

## Arquitectura

```
automatizador.py → app.py (UI) → ia/cliente.py (IA) → API externa
                      ↕
                  config.py (.env + constantes)
```

- UI importa lógica, nunca al revés
- `ia/cliente.py` es independiente de la UI
- Colores y config centralizados en `config.py`

## Memoria por dominio

Cuando trabajes en un área específica, consulta su archivo de gotchas:

| Dominio | Archivo | Contenido |
|---------|---------|-----------|
| IA / API | `memory/ia/gotchas.md` | SSL corporativo, httpx, finish_reason, max_tokens, validación de respuesta |
| QA | `memory/qa/gotchas.md` | Estructura del reporte, prompt del sistema QA, formato Markdown |
| CustomTkinter | `memory/tkinter/gotchas.md` | Placeholder manual, Textbox disabled, paleta de colores, separación UI/lógica |

El historial del proyecto está en `memory/README.md`.

## Gotcha crítico: system prompt + max_tokens comparten presupuesto

Si el system prompt es verboso y `max_tokens` bajo, el modelo consume todo el presupuesto procesando instrucciones y **no genera respuesta**. La API devuelve `finish_reason: "length"` con `content: None`.

**Solución**: system prompt minimalista (~80 tokens), `max_tokens` configurable desde `.env` (default 3000). Siempre validar que `response.choices[0].message.content` no sea `None` ni vacío antes de usarlo.
