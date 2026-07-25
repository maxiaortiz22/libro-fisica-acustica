---
name: acoustic-book-review
description: Revisa capítulos del libro de Física Acústica para detectar y corregir errores científicos, matemáticos, curriculares, pedagógicos, terminológicos y editoriales. Usar cuando se pida revisar, validar, auditar, corregir o mejorar contenido existente; no usar para una figura aislada.
---

# Objetivo

Evaluar el manuscrito con criterio de revisor científico y docente, diferenciando problemas de exactitud, profundidad, claridad y estilo.

# Material obligatorio

Leer:

1. `AGENTS.md`.
2. La sección completa, no solo el párrafo señalado.
3. Las definiciones previas de los símbolos involucrados.
4. `references/review-checklist.md`.
5. `references/notation-and-units.md`.
6. El mapa curricular de la skill de autoría cuando la revisión incluya alineación con el programa.

# Modos de revisión

Aplicar los modos pedidos por el usuario. Si no se especifican, usar los cuatro:

- **científico:** exactitud física, acústica, auditiva y matemática;
- **curricular:** correspondencia con el programa y profundidad adecuada;
- **pedagógico:** secuencia, prerequisitos, ejemplos y evaluación;
- **editorial:** claridad, cohesión, terminología y estilo.

# Procedimiento

## 1. Determinar si se edita

- Si el usuario pide “revisar”, “auditar” o “decirme qué está mal”, entregar primero un informe y no modificar archivos.
- Si pide “corregir” o “mejorar”, registrar hallazgos y realizar cambios acotados.
- Si existe ambigüedad con consecuencias grandes, conservar el texto y señalarla.

## 2. Clasificar hallazgos

Usar severidad:

- **Crítico:** afirmación falsa, ecuación incorrecta, error de unidad, riesgo de seguridad o conclusión clínica injustificada.
- **Mayor:** definición ambigua, omisión curricular importante, modelo usado fuera de su dominio o contradicción interna.
- **Moderado:** salto pedagógico, ejemplo débil, terminología inestable o figura insuficiente.
- **Menor:** estilo, puntuación, repetición o maquetación sin impacto conceptual.

Para cada hallazgo indicar:

- ubicación;
- fragmento o concepto afectado;
- problema;
- motivo;
- corrección propuesta;
- necesidad de fuente o verificación.

## 3. Revisar ecuaciones y números

- comprobar dimensiones;
- distinguir valor instantáneo, pico, RMS y media;
- verificar factores 10/20 en niveles;
- verificar referencias y unidades;
- recalcular ejemplos;
- comprobar signos y redondeo;
- confirmar que la conclusión se desprenda del cálculo;
- distinguir igualdad, aproximación y proporcionalidad.

## 4. Revisar relaciones físico-perceptuales

Comprobar especialmente:

- frecuencia frente a pitch;
- presión/nivel frente a sonoridad;
- amplitud frente a “volumen”;
- espectro frente a timbre;
- atenuación física frente a reducción perceptual;
- dB SPL frente a dB HL;
- mecanismo del oído frente a metáforas de amplificación.

## 5. Revisar aplicaciones fonoaudiológicas

- delimitar el alcance introductorio;
- evitar diagnósticos o recomendaciones clínicas no sustentadas;
- identificar qué magnitud o respuesta mide cada prueba;
- no confundir calibración, verificación y medición;
- no presentar ejemplos numéricos didácticos como valores clínicos universales.

## 6. Corregir con mínima intervención

Cuando se autorice edición:

- conservar el contenido válido;
- corregir primero la causa conceptual;
- actualizar ejemplos, resúmenes y ejercicios afectados;
- evitar una reescritura total salvo que el problema sea estructural;
- agregar comentarios de verificación para fuentes aún no disponibles.

## 7. Validar

Compilar y revisar las páginas cambiadas. Usar `$latex-book-validation` cuando la tarea incluya edición.

# Formato del informe

Entregar:

1. evaluación general;
2. hallazgos ordenados por severidad;
3. brechas curriculares;
4. cambios propuestos o realizados;
5. verificaciones pendientes;
6. resultado de compilación, si hubo edición.
