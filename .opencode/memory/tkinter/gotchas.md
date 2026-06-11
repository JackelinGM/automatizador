# CustomTkinter — Gotchas del dominio

## Siempre usar CustomTkinter, NO Tkinter estándar

```python
import customtkinter as ctk   # correcto
# import tkinter as tk        # incorrecto
```

La clase base es `ctk.CTk`, no `tk.Tk`.

## Tema oscuro y paleta de colores

El tema se configura en `automatizador.py` antes de crear la app:

```python
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
```

Todos los colores están centralizados en `config.py`. No se deben hardcodear colores en otros archivos. Consultar `config.py` para las constantes disponibles.

## Textbox en modo disabled

Para modificar un `CTkTextbox` que está en `state="disabled"`:

```python
self.salida_texto.configure(state="normal")
self.salida_texto.delete("0.0", "end")
self.salida_texto.insert("0.0", texto)
self.salida_texto.configure(text_color=COLOR_TEXTO)
self.salida_texto.configure(state="disabled")
```

Nunca intentar insertar texto con el widget en estado `disabled`.

## Placeholder manual

CustomTkinter no tiene placeholder nativo. El proyecto usa un sistema manual:
- Variable `self._placeholder_activo` (bool)
- Variable `self._texto_placeholder` (str)
- Eventos `<FocusIn>` y `<FocusOut>` para mostrar/ocultar

## Separación UI / lógica

Los módulos en `ia/` y `utils/` **no deben importar** `customtkinter`. La UI vive en `app.py`, la lógica es independiente.
