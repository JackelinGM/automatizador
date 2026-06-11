"""
Configuración global de la aplicación.
Constantes, colores y carga de variables de entorno.
"""
import os
from dotenv import load_dotenv

# ─── Cargar variables de entorno ──────────────────────────
ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_env = os.path.join(ruta_script, ".env")
load_dotenv(dotenv_path=ruta_env)

# ─── Colores personalizados ───────────────────────────────
COLOR_CIAN = "#00fad1"
COLOR_CIAN_OSCURO = "#14c3a7"
COLOR_FONDO = "#0D0D0D"
COLOR_TARJETA = "#1A1A1A"
COLOR_BORDE = "#2A2A2A"
COLOR_TEXTO = "#FFFFFF"
COLOR_TEXTO_SECUNDARIO = "#888888"
COLOR_PLACEHOLDER = "#555555"
COLOR_BOTON_GRIS = "#2D2D2D"
COLOR_BOTON_GRIS_HOVER = "#3D3D3D"

# ─── Obtener configuración del .env ───────────────────────
def obtener_config_ia():
    """Retorna la configuración de la IA desde variables de entorno."""
    api_key = os.getenv("OPENCODE_API_KEY")
    base_url = os.getenv("OPENCODE_BASE_URL")
    modelo = os.getenv("OPENCODE_MODEL", "deepseek-v4-flash")

    ssl_verify = os.getenv("SSL_VERIFY", "true").lower()
    ssl_habilitado = ssl_verify not in ("false", "0", "no")

    max_tokens = int(os.getenv("MAX_TOKENS", "3000"))

    return {
        "api_key": api_key,
        "base_url": base_url,
        "modelo": modelo,
        "ssl_verify": ssl_habilitado,
        "max_tokens": max_tokens,
    }
