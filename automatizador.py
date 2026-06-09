"""
Automatizador de Defectos - Interfaz con CustomTkinter
------------------------------------------------------
Aplicación de escritorio para generar reportes de defectos
con asistencia de inteligencia artificial.
"""

import customtkinter as ctk

# ─────────────────────────────────────────────────────────
# Configuración global de CustomTkinter
# ─────────────────────────────────────────────────────────
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Colores personalizados
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


class AutomatizadorApp(ctk.CTk):
    """Aplicación principal para automatización de defectos."""

    def __init__(self):
        super().__init__()

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
        frame_encabezado = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )
        frame_encabezado.grid(row=0, column=0, sticky="ew", padx=30, pady=(25, 5))
        frame_encabezado.grid_columnconfigure(0, weight=1)

        # ── Título (izquierda) ────────────────────────────
        self.titulo_label = ctk.CTkLabel(
            frame_encabezado,
            text="🐛  Automatizador de Defectos",
            font=("Arial", 24, "bold"),
            text_color=COLOR_CIAN,
            anchor="w",
        )
        self.titulo_label.grid(row=0, column=0, sticky="w")

        # ── Badge del modelo (derecha) ────────────────────
        self.badge_modelo = ctk.CTkLabel(
            frame_encabezado,
            text="  Modelo: deepseek-v4-flash  ",
            font=("Arial", 12),
            text_color=COLOR_CIAN,
            fg_color=COLOR_TARJETA,
            corner_radius=12,
            anchor="e",
        )
        self.badge_modelo.grid(row=0, column=1, sticky="e", padx=(10, 0))

    # ─────────────────────────────────────────────────────────
    # CUERPO PRINCIPAL (dos columnas + zona inferior)
    # ─────────────────────────────────────────────────────────
    def _crear_cuerpo(self):
        """Contenedor principal con dos columnas (40/60) y controles abajo."""
        frame_cuerpo = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )
        frame_cuerpo.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        # Columna izquierda 40%, columna derecha 60% (más ancha)
        frame_cuerpo.grid_columnconfigure(0, weight=4)
        frame_cuerpo.grid_columnconfigure(1, weight=6)
        # Fila 0: las dos columnas con las cajas de texto (expandibles)
        frame_cuerpo.grid_rowconfigure(0, weight=12)
        # Fila 1: pie + botones (altura mínima)
        frame_cuerpo.grid_rowconfigure(1, weight=1)

        # ── Columna izquierda: entrada (solo título + textbox) ──
        self._crear_columna_entrada(frame_cuerpo)

        # ── Columna derecha: reporte ──────────────────────
        self._crear_columna_reporte(frame_cuerpo)

        # ── Pie + botones (abajo, ocupando todo el ancho) ─
        self._crear_pie_y_botones(frame_cuerpo)

    # ─────────────────────────────────────────────────────────
    # COLUMNA IZQUIERDA — Describe el defecto
    # ─────────────────────────────────────────────────────────
    def _crear_columna_entrada(self, padre):
        """Panel izquierdo: solo título + caja de texto (sin pie ni botones)."""
        frame_izq = ctk.CTkFrame(
            padre,
            fg_color="transparent",
        )
        frame_izq.grid(row=0, column=0, sticky="nsew", padx=(0, 4))
        frame_izq.grid_columnconfigure(0, weight=1)
        frame_izq.grid_rowconfigure(1, weight=1)

        # ── Título de sección ─────────────────────────────
        seccion_entrada = ctk.CTkLabel(
            frame_izq,
            text="📝  Describe el defecto:",
            font=("Arial", 15, "bold"),
            text_color=COLOR_TEXTO,
            anchor="w",
        )
        seccion_entrada.grid(row=0, column=0, sticky="w", pady=(0, 8))

        # ── Caja de texto ─────────────────────────────────
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

        # ── Placeholder manual ────────────────────────────
        self._placeholder_activo = True
        self._texto_placeholder = "Describe aquí el defecto con el mayor detalle posible..."
        self.entrada_texto.insert("0.0", self._texto_placeholder)
        self.entrada_texto.configure(text_color=COLOR_PLACEHOLDER)

    def _crear_pie_y_botones(self, padre):
        """Barra inferior: consejos + contador (fila 1) y botones (fila 2)."""
        frame_bottom = ctk.CTkFrame(
            padre,
            fg_color="transparent",
        )
        frame_bottom.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(10, 0))
        frame_bottom.grid_columnconfigure(0, weight=1)

        # ── Fila 1: Consejos + Contador ───────────────────
        frame_pie = ctk.CTkFrame(
            frame_bottom,
            fg_color="transparent",
            height=28,
        )
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

        # ── Fila 2: Botones (alineados a la izquierda) ────
        frame_botones = ctk.CTkFrame(
            frame_bottom,
            fg_color="transparent",
        )
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

        self.boton_copiar = ctk.CTkButton(
            frame_botones,
            text="📋  Copiar",
            command=self.copiar_reporte,
            font=("Arial", 14, "bold"),
            fg_color=COLOR_BOTON_GRIS,
            hover_color=COLOR_BOTON_GRIS_HOVER,
            text_color=COLOR_TEXTO,
            border_color=COLOR_BORDE,
            border_width=1,
            corner_radius=10,
            height=42,
            width=140,
        )
        self.boton_copiar.grid(row=0, column=1)

    # ─────────────────────────────────────────────────────────
    # COLUMNA DERECHA — Reporte generado
    # ─────────────────────────────────────────────────────────
    def _crear_columna_reporte(self, padre):
        """Panel derecho: solo título + caja de texto de solo lectura (más ancho)."""
        frame_der = ctk.CTkFrame(
            padre,
            fg_color="transparent",
        )
        frame_der.grid(row=0, column=1, sticky="nsew", padx=(4, 0))
        frame_der.grid_columnconfigure(0, weight=1)
        frame_der.grid_rowconfigure(1, weight=1)

        # ── Título de sección ─────────────────────────────
        seccion_reporte = ctk.CTkLabel(
            frame_der,
            text="📄  Reporte generado:",
            font=("Arial", 15, "bold"),
            text_color=COLOR_TEXTO,
            anchor="w",
        )
        seccion_reporte.grid(row=0, column=0, sticky="w", pady=(0, 8))

        # ── Caja de texto (solo lectura) ──────────────────
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

        # ── Texto por defecto ─────────────────────────────
        self._insertar_texto_inicial_reporte()

    def _insertar_texto_inicial_reporte(self):
        """Inserta el mensaje placeholder en el reporte (solo lectura)."""
        self.salida_texto.configure(state="normal")
        self.salida_texto.delete("0.0", "end")
        self.salida_texto.insert(
            "0.0",
            "Aquí se mostrará el reporte generado...",
        )
        self.salida_texto.configure(text_color=COLOR_PLACEHOLDER)
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
    # MÉTODOS DE ACCIÓN (pendientes de implementar)
    # ─────────────────────────────────────────────────────────
    def generar_reporte(self):
        """Genera un reporte de defecto usando IA.

        TODO: Implementar lógica de conexión con la API de IA
        para analizar el defecto ingresado y poblar salida_texto.
        """
        pass

    def copiar_reporte(self):
        """Copia el contenido del reporte al portapapeles.

        TODO: Implementar lógica para copiar el texto al
        portapapeles del sistema.
        """
        pass


# ─────────────────────────────────────────────────────────
# PUNTO DE ENTRADA
# ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = AutomatizadorApp()
    app.mainloop()
