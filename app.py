"""
Aplicación principal de Automatizador de Defectos.
Interfaz gráfica con CustomTkinter y orquestación de la lógica.
"""
import customtkinter as ctk
import httpx
from tkinter import messagebox

from config import (
    COLOR_CIAN,
    COLOR_CIAN_OSCURO,
    COLOR_FONDO,
    COLOR_TARJETA,
    COLOR_BORDE,
    COLOR_TEXTO,
    COLOR_TEXTO_SECUNDARIO,
    COLOR_PLACEHOLDER,
    COLOR_BOTON_GRIS,
    COLOR_BOTON_GRIS_HOVER,
    obtener_config_ia,
)
from ia.cliente import generar_reporte_ia


class AutomatizadorApp(ctk.CTk):
    """Aplicación principal para automatización de defectos."""

    def __init__(self):
        super().__init__()

        # ─── Cargar configuración de IA ────────────────────
        self.config_ia = obtener_config_ia()
        self.api_key = self.config_ia["api_key"]
        self.base_url = self.config_ia["base_url"]
        self.modelo_ia = self.config_ia["modelo"]
        self.ssl_verify = self.config_ia["ssl_verify"]

        if not self.api_key:
            messagebox.showerror(
                "Error de Configuración",
                "No se encontró la API Key en el archivo .env.\n\n"
                "Verifica que:\n"
                "1. Tu archivo se llame exactamente '.env'\n"
                "2. La variable se llame 'OPENCODE_API_KEY'\n"
                "3. El archivo .env esté en la misma carpeta que este script.",
            )
            return

        # ─── Ventana principal ────────────────────────────
        self.title("Automatizador de Defectos")
        self.geometry("1000x550")
        self.minsize(1000, 550)
        self.configure(fg_color=COLOR_FONDO)

        # ─── Grid layout general ──────────────────────────
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # ─── Construir interfaz ───────────────────────────
        self._crear_encabezado()
        self._crear_cuerpo()

        # ─── Eventos ──────────────────────────────────────
        self._enlazar_eventos()

    # ─────────────────────────────────────────────────────────
    # ENCABEZADO
    # ─────────────────────────────────────────────────────────
    def _crear_encabezado(self):
        """Barra superior con título y badge del modelo."""
        frame_encabezado = ctk.CTkFrame(self, fg_color="transparent")
        frame_encabezado.grid(row=0, column=0, sticky="ew", padx=30, pady=(25, 5))
        frame_encabezado.grid_columnconfigure(0, weight=1)

        self.titulo_label = ctk.CTkLabel(
            frame_encabezado,
            text="🐛  Automatizador de Defectos",
            font=("Arial", 24, "bold"),
            text_color=COLOR_CIAN,
            anchor="w",
        )
        self.titulo_label.grid(row=0, column=0, sticky="w")

        self.badge_modelo = ctk.CTkLabel(
            frame_encabezado,
            text=f"  Modelo: {self.modelo_ia}  ",
            font=("Arial", 12),
            text_color=COLOR_CIAN,
            fg_color=COLOR_TARJETA,
            corner_radius=12,
            anchor="e",
        )
        self.badge_modelo.grid(row=0, column=1, sticky="e", padx=(10, 0))

    # ─────────────────────────────────────────────────────────
    # CUERPO PRINCIPAL
    # ─────────────────────────────────────────────────────────
    def _crear_cuerpo(self):
        """Contenedor principal con dos columnas (40/60) y controles abajo."""
        frame_cuerpo = ctk.CTkFrame(self, fg_color="transparent")
        frame_cuerpo.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        frame_cuerpo.grid_columnconfigure(0, weight=4)
        frame_cuerpo.grid_columnconfigure(1, weight=6)
        frame_cuerpo.grid_rowconfigure(0, weight=12)
        frame_cuerpo.grid_rowconfigure(1, weight=1)

        self._crear_columna_entrada(frame_cuerpo)
        self._crear_columna_reporte(frame_cuerpo)
        self._crear_pie_y_botones(frame_cuerpo)

    # ─────────────────────────────────────────────────────────
    # COLUMNA IZQUIERDA — Entrada del defecto
    # ─────────────────────────────────────────────────────────
    def _crear_columna_entrada(self, padre):
        """Panel izquierdo: título + caja de texto."""
        frame_izq = ctk.CTkFrame(padre, fg_color="transparent")
        frame_izq.grid(row=0, column=0, sticky="nsew", padx=(0, 4))
        frame_izq.grid_columnconfigure(0, weight=1)
        frame_izq.grid_rowconfigure(1, weight=1)

        seccion_entrada = ctk.CTkLabel(
            frame_izq,
            text="📝  Describe el defecto:",
            font=("Arial", 15, "bold"),
            text_color=COLOR_TEXTO,
            anchor="w",
        )
        seccion_entrada.grid(row=0, column=0, sticky="w", pady=(0, 8))

        self.entrada_texto = ctk.CTkTextbox(
            frame_izq,
            font=("Consolas", 13),
            text_color=COLOR_TEXTO,
            fg_color=COLOR_TARJETA,
            border_color=COLOR_BORDE,
            border_width=1,
            corner_radius=8,
            wrap="word",
        )
        self.entrada_texto.grid(row=1, column=0, sticky="nsew")

        # Placeholder manual
        self._placeholder_activo = True
        self._texto_placeholder = "Describe aquí el defecto con el mayor detalle posible..."
        self.entrada_texto.insert("0.0", self._texto_placeholder)
        self.entrada_texto.configure(text_color=COLOR_PLACEHOLDER)

    # ─────────────────────────────────────────────────────────
    # COLUMNA DERECHA — Reporte generado
    # ─────────────────────────────────────────────────────────
    def _crear_columna_reporte(self, padre):
        """Panel derecho: título + caja de solo lectura."""
        frame_der = ctk.CTkFrame(padre, fg_color="transparent")
        frame_der.grid(row=0, column=1, sticky="nsew", padx=(4, 0))
        frame_der.grid_columnconfigure(0, weight=1)
        frame_der.grid_rowconfigure(1, weight=1)

        seccion_reporte = ctk.CTkLabel(
            frame_der,
            text="📄  Reporte generado:",
            font=("Arial", 15, "bold"),
            text_color=COLOR_TEXTO,
            anchor="w",
        )
        seccion_reporte.grid(row=0, column=0, sticky="w", pady=(0, 8))

        self.salida_texto = ctk.CTkTextbox(
            frame_der,
            font=("Consolas", 13),
            text_color=COLOR_TEXTO,
            fg_color=COLOR_TARJETA,
            border_color=COLOR_BORDE,
            border_width=1,
            corner_radius=8,
            wrap="word",
            state="disabled",
        )
        self.salida_texto.grid(row=1, column=0, sticky="nsew")

        self._insertar_texto_inicial_reporte()

    # ─────────────────────────────────────────────────────────
    # PIE Y BOTONES
    # ─────────────────────────────────────────────────────────
    def _crear_pie_y_botones(self, padre):
        """Barra inferior: consejos + contador + botones."""
        frame_bottom = ctk.CTkFrame(padre, fg_color="transparent")
        frame_bottom.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(10, 0))
        frame_bottom.grid_columnconfigure(0, weight=1)

        # Fila 1: Consejos + Contador
        frame_pie = ctk.CTkFrame(frame_bottom, fg_color="transparent", height=28)
        frame_pie.grid(row=0, column=0, sticky="ew")
        frame_pie.grid_columnconfigure(0, weight=1)

        consejos = ctk.CTkLabel(
            frame_pie,
            text="💡 Sé claro y específico    |    📋 Incluye pasos para reproducirlo",
            font=("Arial", 11),
            text_color=COLOR_TEXTO_SECUNDARIO,
            anchor="w",
        )
        consejos.grid(row=0, column=0, sticky="w")

        self.contador_label = ctk.CTkLabel(
            frame_pie,
            text="0 / 4000",
            font=("Arial", 11),
            text_color=COLOR_TEXTO_SECUNDARIO,
            anchor="e",
        )
        self.contador_label.grid(row=0, column=1, sticky="e")

        # Fila 2: Botones
        frame_botones = ctk.CTkFrame(frame_bottom, fg_color="transparent")
        frame_botones.grid(row=1, column=0, sticky="w", pady=(8, 0))

        self.boton_generar = ctk.CTkButton(
            frame_botones,
            text="📋  Generar Reporte",
            command=self.generar_reporte,
            font=("Arial", 14, "bold"),
            fg_color=COLOR_CIAN,
            hover_color=COLOR_CIAN_OSCURO,
            text_color="#0A0A0A",
            corner_radius=10,
            height=42,
            width=190,
        )
        self.boton_generar.grid(row=0, column=0, padx=(0, 12))

        self.boton_nuevo = ctk.CTkButton(
            frame_botones,
            text="🔄  Nuevo defecto",
            command=self.nuevo_defecto,
            font=("Arial", 14, "bold"),
            fg_color=COLOR_BOTON_GRIS,
            hover_color=COLOR_BOTON_GRIS_HOVER,
            text_color=COLOR_TEXTO,
            border_color=COLOR_BORDE,
            border_width=1,
            corner_radius=10,
            height=42,
            width=160,
        )
        self.boton_nuevo.grid(row=0, column=1)

    # ─────────────────────────────────────────────────────────
    # MANEJO DEL TEXTO EN EL REPORTE
    # ─────────────────────────────────────────────────────────
    def _insertar_texto_inicial_reporte(
        self,
        texto="Aquí se mostrará el reporte generado...",
        color=COLOR_PLACEHOLDER,
    ):
        """Inserta texto informativo en el reporte de forma segura."""
        self.salida_texto.configure(state="normal")
        self.salida_texto.delete("0.0", "end")
        self.salida_texto.insert("0.0", texto)
        self.salida_texto.configure(text_color=color)
        self.salida_texto.configure(state="disabled")

    # ─────────────────────────────────────────────────────────
    # EVENTOS
    # ─────────────────────────────────────────────────────────
    def _enlazar_eventos(self):
        """Conecta eventos de teclado a sus manejadores."""
        self.entrada_texto.bind("<FocusIn>", self._on_focus_in_entrada)
        self.entrada_texto.bind("<FocusOut>", self._on_focus_out_entrada)
        self.entrada_texto.bind("<KeyRelease>", self._actualizar_contador)

    def _on_focus_in_entrada(self, _evento=None):
        """Elimina el placeholder cuando el usuario enfoca la caja."""
        if self._placeholder_activo:
            self.entrada_texto.delete("0.0", "end")
            self.entrada_texto.configure(text_color=COLOR_TEXTO)
            self._placeholder_activo = False

    def _on_focus_out_entrada(self, _evento=None):
        """Restaura el placeholder si la caja está vacía al perder el foco."""
        contenido = self.entrada_texto.get("0.0", "end").strip()
        if not contenido:
            self.entrada_texto.insert("0.0", self._texto_placeholder)
            self.entrada_texto.configure(text_color=COLOR_PLACEHOLDER)
            self._placeholder_activo = True

    def _actualizar_contador(self, _evento=None):
        """Actualiza el contador de caracteres en el pie."""
        contenido = self.entrada_texto.get("0.0", "end").strip()
        if self._placeholder_activo:
            longitud = 0
        else:
            longitud = len(contenido)
        self.contador_label.configure(text=f"{longitud} / 4000")

    # ─────────────────────────────────────────────────────────
    # ACCIONES PRINCIPALES
    # ─────────────────────────────────────────────────────────
    def generar_reporte(self):
        """Valida entrada, llama a la IA y muestra el resultado."""
        if self._placeholder_activo or not self.entrada_texto.get("0.0", "end").strip():
            messagebox.showwarning(
                "Advertencia",
                "Por favor, escribe una descripción del defecto antes de generar.",
            )
            return

        descripcion = self.entrada_texto.get("0.0", "end").strip()

        if not self.api_key:
            self._insertar_texto_inicial_reporte("❌ API Key no configurada.", "#ff4a4a")
            messagebox.showerror(
                "Error de Configuración",
                "No se encontró la API Key.\n\n"
                "Verifica que el archivo .env tenga la variable OPENCODE_API_KEY.",
            )
            return

        # Estado de carga
        self._insertar_texto_inicial_reporte(
            "🤖 Analizando y generando reporte profesional... Por favor espera.",
            COLOR_CIAN,
        )
        self.boton_generar.configure(state="disabled", text="⏳ Procesando...")
        self.update()

        try:
            reporte = generar_reporte_ia(descripcion, self.config_ia)

            self.salida_texto.configure(state="normal")
            self.salida_texto.delete("0.0", "end")
            self.salida_texto.insert("0.0", reporte)
            self.salida_texto.configure(text_color=COLOR_TEXTO)
            self.salida_texto.configure(state="disabled")

        except httpx.ConnectError as e:
            mensaje = str(e)
            if "CERTIFICATE_VERIFY_FAILED" in mensaje:
                texto_ayuda = (
                    "Error de verificación SSL.\n\n"
                    "Tu computadora no puede verificar el certificado "
                    "de seguridad del servidor.\n\n"
                    "Soluciones:\n"
                    "1. Agrega SSL_VERIFY=false en tu archivo .env\n"
                    "2. O instala los certificados raíz CA en tu sistema\n"
                    "3. O configura el proxy corporativo correctamente"
                )
            else:
                texto_ayuda = (
                    f"No se pudo conectar con el servidor:\n{e}\n\n"
                    "Verifica tu conexión a internet y que la URL base sea correcta."
                )
            self._insertar_texto_inicial_reporte("❌ Error de conexión.", "#ff4a4a")
            messagebox.showerror("Error de Conexión", texto_ayuda)

        except Exception as e:
            self._insertar_texto_inicial_reporte("❌ Error al generar el reporte.", "#ff4a4a")
            messagebox.showerror(
                "Error de API",
                f"No se pudo generar el reporte:\n\n{e}",
            )

        finally:
            self.boton_generar.configure(state="normal", text="📋  Generar Reporte")

    def nuevo_defecto(self):
        """Limpia la entrada y el reporte para empezar un nuevo defecto."""
        if self._placeholder_activo and (
            "Aquí se mostrará" in self.salida_texto.get("0.0", "end")
            or "Analizando y generando" in self.salida_texto.get("0.0", "end")
        ):
            messagebox.showinfo(
                "Nuevo defecto",
                "No hay nada que limpiar. Escribe un defecto y genera un reporte primero.",
            )
            return

        confirmar = messagebox.askyesno(
            "Nuevo defecto",
            "¿Estás seguro?\n\nSe limpiará la descripción y el reporte actual.",
            icon="warning",
        )

        if not confirmar:
            return

        # Limpiar entrada
        self.entrada_texto.delete("0.0", "end")
        self.entrada_texto.insert("0.0", self._texto_placeholder)
        self.entrada_texto.configure(text_color=COLOR_PLACEHOLDER)
        self._placeholder_activo = True

        # Limpiar reporte
        self._insertar_texto_inicial_reporte()

        # Resetear contador
        self.contador_label.configure(text="0 / 4000")
