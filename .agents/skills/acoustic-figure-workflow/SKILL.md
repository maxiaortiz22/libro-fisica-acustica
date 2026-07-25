---
name: acoustic-figure-workflow
description: Diseña, genera, integra y valida figuras, diagramas y gráficos reproducibles para el libro LaTeX de Física Acústica. Usar para TikZ, PGFPlots, Python/Matplotlib, esquemas conceptuales, señales, espectros y visualizaciones de mediciones.
---

# Objetivo

Crear figuras que mejoren la comprensión y que puedan regenerarse, revisarse y publicarse con calidad consistente.

# Material obligatorio

Leer:

1. `AGENTS.md`.
2. El texto que introduce y comenta la figura.
3. `references/figure-policy.md`.
4. Las convenciones de notación y unidades de la skill de revisión.

# Procedimiento

## 1. Definir el propósito

Antes de dibujar, formular en una frase qué debe aprender el estudiante al mirar la figura.

No crear una figura si una ecuación, una tabla pequeña o una explicación breve resuelve mejor el objetivo.

## 2. Elegir la tecnología

- **TikZ:** esquemas de propagación, geometría, bloques, reflexión, anatomía simplificada y diagramas conceptuales.
- **PGFPlots:** funciones, curvas teóricas, datos tabulados y comparaciones con ejes.
- **Python + Matplotlib/NumPy/SciPy:** señales, FFT, filtros, ruido, simulaciones, procesamiento y datos experimentales.
- **Imagen raster:** únicamente para fotografías, capturas o material que no pueda representarse razonablemente como vector.

Conservar la tecnología ya usada en el proyecto cuando sea adecuada.

## 3. Garantizar trazabilidad

Para figuras calculadas:

- guardar el script;
- fijar semillas aleatorias;
- registrar parámetros físicos y unidades;
- no inventar datos experimentales;
- distinguir claramente datos medidos, simulados y esquemáticos;
- guardar la salida en la carpeta de generados definida por el repositorio.

## 4. Diseñar

- usar etiquetas en español coherentes con el texto;
- indicar magnitud y unidad en cada eje;
- evitar ejes decorativos o escalas engañosas;
- usar escala logarítmica cuando el fenómeno lo requiera y explicitarla;
- evitar exceso de curvas, colores, flechas y texto;
- mantener legibilidad al ancho final de columna o página;
- hacer que la información sobreviva a impresión en escala de grises cuando sea razonable;
- no usar imágenes de baja resolución ni estilos visuales incompatibles entre capítulos.

## 5. Integrar

- citar la figura en el texto antes o cerca de su aparición;
- escribir un epígrafe que indique qué representa y qué debe observarse;
- agregar `\label{fig:...}` estable;
- incluir fuente o indicar elaboración propia cuando corresponda;
- no repetir en el epígrafe todo el texto del cuerpo.

## 6. Validar científicamente

- revisar ecuaciones y parámetros;
- comprobar unidades;
- verificar normalizaciones;
- confirmar que la figura sustenta la afirmación del texto;
- no extrapolar resultados simulados como si fueran mediciones reales.

## 7. Validar visualmente

- generar la salida final;
- compilar el libro;
- inspeccionar la página al tamaño de lectura;
- comprobar recortes, superposiciones, textos pequeños y leyendas;
- revisar referencias y numeración.

# Resultado esperado

Entregar:

- fuente editable de la figura;
- script o datos cuando correspondan;
- archivo generado;
- integración LaTeX;
- breve descripción de parámetros y validaciones.
