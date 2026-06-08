# Mini Reporte - Context Engineering y AGENTS.md

## Medición de contexto

No se realizó la medición inicial mediante `/context`, por lo que no fue posible comparar cuantitativamente el consumo de contexto antes y después de la poda. Como aprendizaje, se identificó la importancia de realizar esta medición desde el inicio para contar con evidencia objetiva del impacto de los cambios realizados.

---

## Tres decisiones de poda

### Decisión 1: Eliminación de código hardcodeado

El proyecto inicialmente generaba defectos mediante respuestas y estructuras definidas directamente en el código. Se eliminó esta dependencia para permitir una generación más dinámica mediante el agente.

### Decisión 2: Reducción de información redundante

Se retiraron instrucciones y descripciones que podían inferirse directamente desde el código fuente, reduciendo ruido dentro del contexto.

### Decisión 3: Priorización de reglas críticas

Se mantuvieron únicamente las reglas necesarias para la generación de defectos, evitando agregar documentación extensa o información de bajo valor para el agente.

---

## Gotcha identificado

Durante las pruebas, el agente generaba una respuesta, pero no devolvía la estructura esperada para el defecto.

### Causa

La configuración de los token´s era minima se aumento a 4000 

### Error evitado

Evita generar defectos incompletos o sin formato estándar, dificultando su posterior registro y seguimiento.

---

## Reflexión

Inicialmente, el proyecto de automatización de defectos estaba construido únicamente con código hardcodeado y no contaba con un agente de IA. La generación de defectos se realizaba mediante plantillas fijas definidas directamente en el código.

Durante el ejercicio se identificó que un agente aporta valor cuando debe interpretar descripciones libres, generar información estructurada y facilitar una futura integración con Jira.

También se identificó la necesidad de utilizar prompts más específicos y robustos para obtener resultados consistentes, así como la importancia de medir el contexto desde el inicio para evaluar objetivamente las mejoras realizadas.

---

