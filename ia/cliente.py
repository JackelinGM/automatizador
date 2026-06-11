import httpx
from openai import OpenAI


# ─── Prompts del sistema ──────────────────────────────────
PROMPT_QA = (
    "Eres QA senior. Convierte la descripción del usuario en un reporte "
    "de bug con este formato Markdown:\n\n"
    "**Título:** [corto]\n"
    "**Severidad:** [Crítica/Alta/Media/Baja]\n"
    "**Descripción:** [contexto]\n"
    "**Pasos para reproducir:**\n"
    "1. [paso]\n"
    "**Resultado actual:** [lo observado]\n"
    "**Resultado esperado:** [lo esperado]\n\n"
    "Sé conciso. No inventes."
)


def generar_reporte_ia(descripcion: str, config: dict) -> str:
    """
    Envía la descripción del defecto a la IA y retorna el reporte generado.

    Parámetros:
        descripcion: Texto con la descripción informal del defecto.
        config: Diccionario con 'api_key', 'base_url', 'modelo' y 'ssl_verify'.

    Retorna:
        str con el reporte generado por la IA.

    Lanza:
        httpx.ConnectError: Si hay error de conexión o SSL.
        Exception: Para cualquier otro error de la API.
    """
    client = OpenAI(
        api_key=config["api_key"],
        base_url=config["base_url"],
        http_client=httpx.Client(verify=config["ssl_verify"]),
    )

    response = client.chat.completions.create(
        model=config["modelo"],
        messages=[
            {"role": "system", "content": PROMPT_QA},
            {"role": "user", "content": descripcion},
        ],
        temperature=0.3,
        max_tokens=config["max_tokens"],
    )

    contenido = response.choices[0].message.content

    # ─── Depuración temporal ────────────────────────────
    print("\n" + "=" * 60)
    print("📡 DEBUG — Respuesta de la IA:")
    print(f"   Modelo: {config['modelo']}")
    print(f"   Finish reason: {response.choices[0].finish_reason}")
    print(f"   ¿Contenido vacío?: {not contenido}")
    print(f"   Tipo de contenido: {type(contenido).__name__}")
    if contenido:
        print(f"   Longitud: {len(contenido)} caracteres")
        print(f"   Vista previa (200 chars):\n   {contenido[:200]}...")
    else:
        print("   ⚠️ CONTENIDO ES NONE O VACÍO")
    print("=" * 60 + "\n")

    # ─── Validación ─────────────────────────────────────
    if not contenido:
        raise ValueError(
            "La IA no generó contenido. Esto puede deberse a:\n"
            "- El modelo rechazó la solicitud (filtro de contenido)\n"
            "- La API devolvió una respuesta vacía\n"
            "- El finish_reason no fue 'stop'\n\n"
            f"Finish reason recibido: {response.choices[0].finish_reason}"
        )

    return contenido
