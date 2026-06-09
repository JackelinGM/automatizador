# Automatizador de Defectos

Aplicación de escritorio para generar reportes de defectos de software con asistencia de inteligencia artificial.

## Características

- **Interfaz moderna** con CustomTkinter (tema oscuro, diseño responsive)
- **Análisis con IA** mediante OpenCode API
- **Reportes estructurados** con Descripción, Pasos para reproducir, Resultado actual y Resultado esperado
- **Contador de caracteres** en tiempo real
- **Copiado al portapapeles** con un clic

## Requisitos

- Python 3.10+
- pip (gestor de paquetes de Python)

## Instalación

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd automatizador

# Instalar dependencias
pip install -r requirements.txt
```

## Configuración

Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

```
OPENCODE_API_KEY=tu_api_key
OPENCODE_BASE_URL=https://opencode.ai/zen/go/v1
OPENCODE_MODEL=deepseek-v4-flash
```

## Uso

```bash
python automatizador.py
```

1. Describe el defecto en la caja de texto izquierda
2. Haz clic en **"Generar Reporte"**
3. El reporte estructurado aparecerá en el panel derecho
4. Usa **"Copiar"** para copiar el reporte al portapapeles

## Estructura del reporte

Cada reporte generado incluye:

- **Descripción**: Contexto general del problema identificado
- **Pasos para reproducir**: Secuencia detallada para reproducir el defecto
- **Resultado actual**: Comportamiento observado durante la prueba
- **Resultado esperado**: Comportamiento correcto esperado

## Estructura del proyecto

```
automatizador/
├── .env                  # Variables de entorno (API key, modelo)
├── .opencode/            # Configuración de OpenCode
├── automatizador.py      # Aplicación principal
├── memory/               # Métricas y documentación interna
├── opencode.json         # Configuración del agente opencode
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Este archivo
```

## Tecnologías

- Python 3.x
- CustomTkinter (GUI)
- OpenCode API (IA)

## Próximos pasos

- [ ] Integrar API de IA para análisis de defectos
- [ ] Guardar/cargar defectos desde archivo
- [ ] Exportar reportes a PDF y Word
- [ ] Validación de campos obligatorios

