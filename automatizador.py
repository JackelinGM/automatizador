"""
Automatizador de Defectos
─────────────────────────
Punto de entrada de la aplicación.
"""
import customtkinter as ctk
from config import COLOR_FONDO
from app import AutomatizadorApp


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = AutomatizadorApp()
    app.mainloop()
