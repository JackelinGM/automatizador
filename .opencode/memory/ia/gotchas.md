# Integración IA — Gotchas del dominio

## Configuración desde `.env`

```ini
OPENCODE_API_KEY=tu_api_key
OPENCODE_BASE_URL=https://...
OPENCODE_MODEL=deepseek-v4-pro
MAX_TOKENS=3000
SSL_VERIFY=false    # solo en entornos corporativos con proxy
```

`config.py` carga estas variables y las expone como diccionario.

## Cliente OpenAI con httpx (control SSL)

```python
client = OpenAI(
    api_key=config["api_key"],
    base_url=config["base_url"],
    http_client=httpx.Client(verify=config["ssl_verify"]),
)
```

El cliente usa `httpx` internamente, no `requests`. En entornos corporativos con proxy que rompe SSL, se debe setear `SSL_VERIFY=false` en `.env`.

## max_tokens configurable

`max_tokens` se lee de `MAX_TOKENS` en `.env` (default 3000). El valor quemado anterior (1500) era insuficiente y causaba `finish_reason: length`.

## Validación de respuesta

Siempre validar que `response.choices[0].message.content` no sea `None` ni vacío. Si la API devuelve contenido vacío, lanzar `ValueError` con mensaje claro incluyendo el `finish_reason`.

## finish_reason

| Valor | Significado |
|---|---|
| `stop` | Respuesta completa, sin problemas |
| `length` | Se agotaron los tokens — aumentar `MAX_TOKENS` o acortar el prompt |
| `content_filter` | El modelo rechazó la solicitud por filtro de seguridad |

## Debug temporal

Hay un bloque de `print` en `cliente.py` que imprime en consola: modelo, finish_reason, si el contenido está vacío, tipo, longitud y vista previa. Útil para diagnosticar problemas de API. Se puede remover en producción.
