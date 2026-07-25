---
name: acoustic-book-authoring
description: Redacta, amplía, reestructura o mejora capítulos y ejercicios del libro de Física Acústica para Fonoaudiología, alineándolos con el programa, el nivel de primer año y las convenciones LaTeX del repositorio. No usar para una revisión puramente diagnóstica ni para una tarea centrada solo en figuras.
---

# Objetivo

Producir contenido didáctico, científicamente preciso y coherente con el programa oficial y con el manuscrito existente.

# Material que se debe consultar

Antes de editar, leer:

1. El `AGENTS.md` activo.
2. El capítulo o sección solicitados.
3. El capítulo anterior y el siguiente, al menos en sus objetivos, definiciones y referencias cruzadas.
4. `references/course-map.md`.
5. `references/editorial-style.md`.
6. `references/chapter-blueprint.md` cuando se cree o reestructure una unidad completa.
7. Las convenciones de `.agents/skills/acoustic-book-review/references/notation-and-units.md` cuando haya ecuaciones, niveles o unidades.

# Procedimiento

## 1. Delimitar la tarea

Identificar:

- unidad y sección afectadas;
- resultado de aprendizaje buscado;
- conocimientos previos requeridos;
- contenidos obligatorios del programa;
- profundidad matemática compatible con el resto del libro;
- elementos existentes que deben conservarse.

Si el pedido es amplio, preparar un plan breve por subsecciones antes de escribir.

## 2. Analizar brechas

Comparar el manuscrito con el mapa curricular y clasificar cada punto como:

- cubierto y correcto;
- cubierto pero demasiado breve;
- cubierto con riesgo de confusión;
- ausente o no explícito;
- ubicado en otra unidad y apto para referencia cruzada.

No repetir contenido completo solo porque aparece en dos unidades del programa. Decidir dónde se introduce, dónde se profundiza y dónde se referencia.

## 3. Diseñar la progresión pedagógica

Usar esta secuencia cuando sea pertinente:

1. fenómeno observable o problema;
2. explicación cualitativa;
3. magnitudes involucradas;
4. modelo y supuestos;
5. ecuación;
6. ejemplo numérico o gráfico;
7. interpretación física;
8. relación con Fonoaudiología;
9. limitaciones y errores frecuentes;
10. práctica guiada y práctica autónoma.

Cada ejemplo clínico debe ser físicamente defendible. No atribuir causalidad clínica a una analogía ilustrativa.

## 4. Redactar

- Mantener la voz y la estructura del libro.
- Escribir definiciones operativas y no circulares.
- Introducir símbolos y unidades en el punto de uso.
- Explicitar aproximaciones, condiciones y valores de referencia.
- Separar propiedades objetivas de correlatos perceptuales.
- Evitar sinónimos innecesarios para una misma magnitud.
- Añadir referencias cruzadas en lugar de duplicar desarrollos.
- Marcar las afirmaciones que requieran verificación bibliográfica.

## 5. Crear ejemplos y ejercicios

Para una sección importante, intentar incluir una combinación de:

- pregunta conceptual;
- ejercicio de unidades u orden de magnitud;
- problema numérico directo;
- interpretación de gráfico;
- aplicación a una medición o situación fonoaudiológica;
- pregunta que obligue a justificar una hipótesis.

Comprobar los resultados numéricos. No publicar una solución calculada mentalmente si puede verificarse con una herramienta o un script.

## 6. Proponer figuras

Solo añadir una figura cuando resuelva una dificultad pedagógica concreta. Para su producción, seguir `$acoustic-figure-workflow`.

## 7. Integrar en LaTeX

- Respetar el preámbulo y los comandos existentes.
- Mantener etiquetas estables.
- No introducir paquetes de forma silenciosa.
- Evitar cambios globales no solicitados.
- Comprobar que las citas y referencias cruzadas sigan siendo válidas.

## 8. Validar

- Compilar con el flujo del repositorio.
- Verificar ecuaciones, unidades y resultados.
- Revisar coherencia con secciones adyacentes.
- Inspeccionar visualmente las páginas modificadas si cambió la maquetación.
- Informar cambios, validaciones y dudas pendientes.

# Resultado esperado

Entregar cambios editables en el repositorio y un resumen con:

- contenidos agregados o reorganizados;
- decisiones pedagógicas relevantes;
- verificaciones ejecutadas;
- afirmaciones que todavía necesiten una fuente;
- posibles tareas posteriores, solo cuando sean necesarias.
