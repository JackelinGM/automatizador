import tkinter as tk
from tkinter import scrolledtext, messagebox
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI, APIError, APIConnectionError

# Cargar variables de entorno
load_dotenv(Path(__file__).parent / ".env")

# Configurar cliente de OpenCode Go
client = OpenAI(
    api_key=os.getenv("OPENCODE_API_KEY"),
    base_url=os.getenv("OPENCODE_BASE_URL", "https://opencode.ai/zen/go/v1")
)

MODELO_IA = os.getenv("OPENCODE_MODEL", "deepseek-v4-flash")

SYSTEM_PROMPT = """Eres un experto en testing de software que genera reportes de defectos profesionales.
Cuando el usuario te describa un defecto, genera un reporte estructurado con estas secciones:

1. DESCRIPCIÓN: Un resumen claro y conciso del problema identificado.
2. PASOS PARA REPRODUCIR: Lista numerada con pasos detallados y específicos.
3. RESULTADO ACTUAL: Qué está ocurriendo (el comportamiento erróneo).
4. RESULTADO ESPERADO: Qué debería ocurrir según los requisitos.

Reglas:
- Sé específico y técnico
- Usa lenguaje claro en español
- Incluye detalles relevantes del contexto
- Formato limpio y profesional"""


def consultar_ia(texto_defecto: str) -> str:
    """Envía el defecto a la IA y retorna el reporte generado."""
    try:
        respuesta = client.chat.completions.create(
            model=MODELO_IA,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Genera un reporte de defecto para:\n\n{texto_defecto}"}
            ],
            temperature=0.7,
            max_tokens=4000
        )
        contenido = respuesta.choices[0].message.content
        if not contenido or contenido.strip() == "":
            raise RuntimeError("La IA devolvió una respuesta vacía. Intenta con otro modelo.")
        return contenido
    except APIConnectionError:
        raise ConnectionError("No se pudo conectar con la API de OpenCode Go. Verifica tu conexión a internet.")
    except APIError as e:
        raise RuntimeError(f"Error de la API: {e}")


def generar_defecto():
    """Genera un reporte de defecto usando IA."""
    texto = entrada_texto.get("1.0", tk.END).strip()

    if not texto:
        messagebox.showwarning("Campo vacío", "Por favor ingresa el contexto del defecto.")
        return

    boton.config(state=tk.DISABLED, text="Generando...")
    salida_texto.delete("1.0", tk.END)
    salida_texto.insert(tk.END, "Consultando IA... por favor espera.\n")
    ventana.update()

    try:
        resultado = consultar_ia(texto)
        salida_texto.delete("1.0", tk.END)
        salida_texto.insert(tk.END, resultado)
    except (ConnectionError, RuntimeError) as e:
        salida_texto.delete("1.0", tk.END)
        messagebox.showerror("Error", str(e))
    finally:
        boton.config(state=tk.NORMAL, text="Generar Defecto")


# Ventana principal
ventana = tk.Tk()
ventana.configure(bg="#0D0D0D")
ventana.title("Automatizador de Defectos - con IA")
ventana.geometry("750x650")

# Título
titulo = tk.Label(
    ventana,
    text="Automatizador de Defectos",
    font=("Arial", 20, "bold"),
    bg="#0D0D0D",
    fg="#00D9D9"
)
titulo.pack(pady=10)

# Indicador de modelo
modelo_label = tk.Label(
    ventana,
    text=f"Modelo: {MODELO_IA}",
    font=("Arial", 9),
    bg="#0D0D0D",
    fg="#666666"
)
modelo_label.pack()

# Texto de entrada
label_entrada = tk.Label(
    ventana,
    text="Describe el defecto que encontraste:",
    bg="#0D0D0D",
    fg="white",
    font=("Arial", 11)
)
label_entrada.pack()

entrada_texto = scrolledtext.ScrolledText(
    ventana,
    width=85,
    height=8,
    bg="#161616",
    fg="white",
    insertbackground="white",
    font=("Consolas", 11),
    relief="flat"
)
entrada_texto.pack(pady=10)

# Botón
boton = tk.Button(
    ventana,
    text="Generar Defecto",
    command=generar_defecto,
    bg="#00D9D9",
    fg="black",
    activebackground="#00B8B8",
    font=("Arial", 13, "bold"),
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2"
)
boton.pack(pady=10)

# Resultado
label_salida = tk.Label(
    ventana,
    text="Reporte generado:",
    bg="#0D0D0D",
    fg="white",
    font=("Arial", 11)
)
label_salida.pack()

salida_texto = scrolledtext.ScrolledText(
    ventana,
    width=85,
    height=14,
    bg="#161616",
    fg="#00FFFF",
    insertbackground="white",
    font=("Consolas", 11),
    relief="flat"
)
salida_texto.pack(pady=10)

ventana.mainloop()
