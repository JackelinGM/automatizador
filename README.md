# Automatizador de Defectos

Aplicación de escritorio para generar reportes de defectos de software con asistencia de inteligencia artificial.

## Características

- **Interfaz moderna** con CustomTkinter (tema oscuro, diseño responsive)
- **Análisis con IA** mediante OpenCode API
- **Reportes estructurados** con título, severidad, pasos para reproducir, resultado actual y esperado
- **Contador de caracteres** en tiempo real
- **Nuevo defecto** con confirmación para limpiar y empezar otro reporte
- **Control SSL** para entornos corporativos

## Requisitos

- Python 3.10+
- pip (gestor de paquetes de Python)

## Instalación

```bash
git clone <url-del-repositorio>
cd automatizador
pip install -r requirements.txt
```

## Configuración

Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

```ini
OPENCODE_API_KEY=tu_api_key
OPENCODE_BASE_URL=https://opencode.ai/zen/go/v1
OPENCODE_MODEL=deepseek-v4-flash
# MAX_TOKENS=3000          # Opcional: tokens máximos de la respuesta (default: 3000)

# Opcional: deshabilitar verificación SSL (entornos corporativos)
# SSL_VERIFY=false
```

## Uso

```bash
python automatizador.py
```

1. Describe el defecto en la caja de texto izquierda
2. Haz clic en **"Generar Reporte"**
3. El reporte estructurado aparecerá en el panel derecho
4. Usa **"Nuevo defecto"** para limpiar y empezar otro reporte

## Estructura del proyecto

```
automatizador/
├── .env                  # Variables de entorno (API key, modelo, SSL)
├── .opencode/            # Configuración de OpenCode (no modificar)
├── requirements.txt      # Dependencias del proyecto
├── README.md             # Este archivo
│
├── automatizador.py      # Punto de entrada de la aplicación
├── config.py             # Constantes, colores y carga de .env
├── app.py                # Interfaz gráfica (CustomTkinter)
│
├── ia/                   # Lógica de inteligencia artificial
│   ├── __init__.py
│   └── cliente.py        # Conexión con la API y prompt del sistema
│
└── utils/                # Utilidades varias
    └── __init__.py
```

## Arquitectura

```
automatizador.py  →  app.py  →  ia/cliente.py  →  OpenAI API
                    (UI)        (lógica pura)     (externo)
                        ↕
                    config.py
                    (constantes + .env)
```

- `app.py` importa la lógica, no al revés
- `ia/cliente.py` no depende de Tkinter
- `config.py` centraliza colores y configuración

## Tecnologías

- Python 3.x
- CustomTkinter (GUI)
- OpenCode API / OpenAI (IA)
- httpx (cliente HTTP con control SSL)

## Próximos pasos

- [ ] Guardar/cargar defectos desde archivo
- [ ] Validación de campos obligatorios
