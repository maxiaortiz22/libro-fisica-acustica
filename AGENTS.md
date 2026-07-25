# AGENTS.md — Libro de Física Acústica para Fonoaudiología

## Propósito del proyecto

Este repositorio contiene un libro universitario de **Física Acústica para estudiantes de primer año de la Licenciatura en Fonoaudiología**.

El objetivo es mejorar progresivamente el manuscrito existente sin perder su orientación pedagógica, su relación con la práctica fonoaudiológica ni su correspondencia con el programa oficial de la materia.

## Prioridades

En cada tarea, priorizar en este orden:

1. Exactitud científica, matemática y terminológica.
2. Correspondencia con el programa de la materia.
3. Comprensión pedagógica para estudiantes con formación matemática inicial.
4. Coherencia con el resto del libro.
5. Calidad editorial y visual.
6. Cambios pequeños, revisables y reproducibles.

## Fuentes de verdad

Usar esta jerarquía:

1. El programa oficial resumido en `.agents/skills/acoustic-book-authoring/references/course-map.md`.
2. Las convenciones y definiciones ya consolidadas en el manuscrito.
3. Bibliografía académica primaria, libros reconocidos, normas técnicas y documentación oficial.
4. Material complementario claramente identificado.

No inventar referencias, normas, resultados experimentales, números de cláusulas ni valores normativos. Cuando una afirmación necesite verificación externa, agregar un comentario LaTeX del tipo:

```tex
% TODO(verify): confirmar esta afirmación y agregar una fuente primaria.
```

## Alcance curricular

El libro debe cubrir las diez unidades del programa:

1. Nociones básicas e introducción a la acústica.
2. Mecánica clásica y termodinámica.
3. Mecánica ondulatoria.
4. Propiedades y magnitudes del sonido.
5. Análisis frecuencial.
6. Mecanismo de la percepción auditiva.
7. Psicoacústica.
8. Enfermedades, estudios auditivos y rehabilitación.
9. Propagación, aislamiento y cabinas.
10. Ruidos y enmascaramiento.

Antes de ampliar una sección, consultar el mapa curricular y revisar el capítulo anterior y el siguiente para evitar repeticiones, anticipaciones innecesarias o contradicciones.

## Público y enfoque pedagógico

- Asumir conocimientos matemáticos iniciales, pero no ausencia total de razonamiento científico.
- Explicar primero el fenómeno y su significado físico; luego introducir la ecuación.
- Definir cada símbolo inmediatamente antes o después de usarlo por primera vez.
- Incluir unidades, hipótesis y dominio de validez.
- Usar ejemplos clínicos para conectar conceptos, no para reemplazar la explicación física.
- Evitar analogías que atribuyan al sistema auditivo funciones físicamente incorrectas.
- Diferenciar claramente fenómeno físico, correlato perceptual y aplicación clínica.
- Introducir ejercicios de dificultad progresiva y preguntas conceptuales, no solo sustitución numérica.
- No infantilizar el lenguaje.

## Convenciones científicas obligatorias

Mantener separadas, entre otras, las siguientes magnitudes y nociones:

- amplitud, valor eficaz y valor medio;
- presión acústica, intensidad y potencia;
- frecuencia y altura tonal o *pitch*;
- nivel de presión sonora, sonoridad y nivel de audición;
- dB como relación, dB SPL, dB HL y niveles ponderados A;
- desplazamiento de partícula, velocidad de partícula y velocidad de propagación;
- absorción, transmisión, reflexión y aislamiento;
- espectro de una señal y respuesta en frecuencia de un sistema;
- audición por vía aérea y mecanismos de conducción ósea.

No usar expresiones como “la amplitud es el volumen”, “los decibeles miden la intensidad” o “el oído funciona de manera logarítmica” sin las precisiones necesarias.

Ver las convenciones recomendadas en:

- `.agents/skills/acoustic-book-review/references/notation-and-units.md`
- `.agents/skills/acoustic-book-review/references/review-checklist.md`

## Estilo de redacción

- Escribir en español académico claro y natural.
- Preferir construcciones impersonales o primera persona plural para evitar mezclar tuteo y voseo.
- Usar oraciones directas y párrafos con una idea principal reconocible.
- Definir los tecnicismos y mantener una misma traducción a lo largo del libro.
- Evitar relleno, exageraciones, falsos “datos curiosos” y preguntas retóricas repetitivas.
- No afirmar que un ejemplo es clínicamente decisivo si solo ilustra una escala o un orden de magnitud.
- Conservar la voz del autor y mejorarla; no convertir el capítulo en un texto genérico de IA.

Consultar `.agents/skills/acoustic-book-authoring/references/editorial-style.md`.

## Estructura recomendada de cada unidad

Cuando resulte apropiado, incluir:

1. Propósito y resultados de aprendizaje.
2. Conocimientos previos.
3. Situación o pregunta introductoria.
4. Desarrollo conceptual progresivo.
5. Ecuaciones y ejemplos resueltos.
6. Relación con Fonoaudiología.
7. Figuras y actividades reproducibles.
8. Errores frecuentes o advertencias.
9. Síntesis.
10. Ejercicios y preguntas de autoevaluación.
11. Glosario breve cuando aporte valor.
12. Referencias y recursos complementarios.

No forzar todos los elementos si no aportan al capítulo.

## LaTeX

- Detectar y conservar la clase, el motor de compilación, el preámbulo y los comandos existentes.
- No agregar paquetes sin comprobar primero que no exista una solución con los paquetes actuales.
- No redefinir comandos globales desde un capítulo.
- Usar etiquetas semánticas y estables: `chap:`, `sec:`, `fig:`, `tab:`, `eq:`.
- Usar `\label`, `\ref`, `\eqref` y el sistema bibliográfico existente; no escribir números de secciones o figuras manualmente.
- Respetar la convención existente para comas decimales, símbolos y unidades.
- Preferir `siunitx`, `booktabs`, `amsmath`, TikZ y PGFPlots solo si ya están disponibles o si se autoriza su incorporación.
- No modificar archivos generados: PDF, AUX, BBL, BLG, FLS, LOG, OUT, TOC, SYNCTEX ni gráficos generados por scripts.
- Evitar rutas absolutas.
- Mantener los cambios localizados y fáciles de revisar.

## Figuras y gráficos

- Preferir figuras originales y reproducibles.
- Usar TikZ para esquemas conceptuales, PGFPlots para gráficos matemáticos o tabulados y Python para simulaciones o procesamiento de señales.
- Preferir PDF vectorial para la salida final; usar raster solo cuando sea necesario.
- Toda figura debe tener propósito pedagógico, ejes y unidades legibles, epígrafe informativo y `\label`.
- No reutilizar imágenes de Internet sin confirmar licencia, atribución y calidad.
- Para señales aleatorias, fijar una semilla y guardar el script generador.
- Verificar la figura al tamaño real de impresión, no solamente ampliada en pantalla.

Usar la skill `$acoustic-figure-workflow` para tareas centradas en figuras.

## Flujo de trabajo obligatorio

Antes de editar:

1. Identificar el archivo principal del libro y el comando de compilación existente.
2. Leer el capítulo afectado, sus dependencias y el mapa curricular.
3. Indicar cualquier incertidumbre que pueda cambiar el enfoque.
4. Planificar cambios concretos y acotados.

Después de editar:

1. Compilar con el flujo existente del repositorio.
2. Corregir errores de compilación causados por el cambio.
3. Revisar referencias y citas indefinidas.
4. Revisar advertencias relevantes, especialmente `Overfull/Underfull`, figuras ausentes y etiquetas duplicadas.
5. Ejecutar las validaciones disponibles.
6. Inspeccionar visualmente las páginas modificadas cuando se haya cambiado maquetación o gráficos.
7. Informar archivos modificados, verificaciones realizadas y puntos pendientes.

No afirmar que la tarea está completa si el libro no compila. Si el error ya existía, documentarlo con precisión.

## Comandos y dependencias

Usar primero los comandos documentados en `README`, `Makefile`, `latexmkrc`, scripts o configuración del editor.

Si no existe un flujo documentado, proponer —sin imponer— un comando basado en `latexmk`, conservando el motor actual. No instalar paquetes del sistema ni dependencias nuevas sin autorización.

La skill `$latex-book-validation` contiene el procedimiento de validación.

## Política de edición

- En una revisión solicitada como “solo diagnóstico”, no modificar archivos.
- En una solicitud de “corregir”, “mejorar” o “reescribir”, realizar los cambios y mostrar un resumen del criterio aplicado.
- No eliminar contenido técnico solo para reducir longitud.
- Evitar duplicar explicaciones entre unidades; usar referencias cruzadas cuando corresponda.
- No hacer reestructuraciones globales durante una corrección localizada, salvo que el usuario lo pida.
- Preservar el historial de autoría y el tono docente de Maximiliano Ortiz.
