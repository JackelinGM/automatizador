📝 Reporte: Optimización de Instrucciones (agente-dev)
1 · Medición de Contexto
Antes: python-dev.md tenía 117 líneas (~1,456 tokens). El asistente estaba saturado.

Después: AGENTS.md (79 líneas) + python-dev.md (56 líneas).

Resultado: El archivo del desarrollador bajó un 52%. Creamos una base general compartida y compacta, verificable con el comando /context.

2 · Tres Decisiones de Poda (Limpieza)
Quitar herramientas y carpetas: Se eliminaron 55 líneas de código y rutas. El asistente puede revisar el proyecto por sí mismo; era información redundante.

Centralizar la Regla de Oro: Se quitaron 20 líneas de "preguntar antes de asumir". Ahora vive solo en AGENTS.md para evitar contradicciones.

Mantener el plan de trabajo en el agente: Los próximos pasos se quedaron en el archivo del desarrollador. Cambian seguido y no le interesan a otros asistentes (como el de pruebas).

3 · Un Gotcha Real Capturado
El problema: Las instrucciones largas y un límite bajo de respuesta (max_tokens) hacían que la IA se congelara y devolviera el reporte en blanco y sin errores.

Solución aplicada: Recortamos las instrucciones a la mitad, duplicamos el espacio de respuesta en la configuración y añadimos una alerta en el código. Ahora el sistema avisa con un diagnóstico claro.

4 · Tres Preguntas Difíciles
¿Por qué importa el orden? La IA atiende más al inicio (identidad) y al final (errores críticos). Lo secundario se deja al medio.

¿Por qué escribir cuesta más que leer? Leer se hace de una sola pasada. Escribir exige generar una palabra a la vez evaluando todo el contexto, lo que cuesta 2-4 veces más.

¿Dónde guardar 30 trucos viejos? En una carpeta de memoria por temas (memory/dominio). Así el contexto principal queda limpio y la IA solo los lee cuando falla esa área.

5 · Autoevaluación y Siguiente Paso
Cumplimiento: Se cumplió con las líneas (<500), el orden crítico, los criterios de verificación y el reporte ya genera datos reales.

⚠️ Lo que falta (Próximo paso): Conectar el generador de reportes con la API de Jira para automatizar la lectura de los defectos, y validar con /context que el asistente lea la nueva estructura sin perderse.