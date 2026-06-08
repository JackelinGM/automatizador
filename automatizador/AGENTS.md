# Automatizador de Defectos

## Descripción
Aplicación Python que recibe defectos por entrada manual, los analiza con IA y genera reportes estructurados.

## Objetivo
Crear una herramienta que ayude a los testers a generar reportes de defectos profesionales y consistentes.

## Estructura del Reporte
Cada defecto debe incluir:
- **Descripción**: Contexto general del problema identificado
- **Pasos para reproducir**: Secuencia detallada que permita reproducir el defecto
- **Resultado actual**: Comportamiento observado durante la prueba
- **Resultado esperado**: Comportamiento correcto esperado según la funcionalidad

## Componentes del Proyecto
- `automatizador.py` - Aplicación principal con Tkinter (interfaz gráfica)

## Stack Tecnológico
- Python 3.x
- Tkinter (GUI)
- APIs de IA (a integrar según necesidad)

## Comandos Útiles
```bash
# Ejecutar la aplicación
python automatizador.py

# Instalar dependencias (futuro)
pip install -r requirements.txt
```

## Notas para el Agente de Desarrollo
- Usar Tkinter para la interfaz gráfica
- Mantener tema oscuro en la interfaz (estilo actual)
- Preparar arquitectura para integración con API de IA
- Separar lógica de negocio de la UI cuando sea posible
- Usar nombres de variables y funciones descriptivos en español
- Manejar errores de forma apropiada

## Próximos Pasos
- [ ] Integrar API de IA para análisis de defectos
- [ ] Agregar funcionalidad de guardar/cargar defectos
- [ ] Implementar exportación de reportes (PDF, Word)
- [ ] Agregar validación de campos obligatorios
