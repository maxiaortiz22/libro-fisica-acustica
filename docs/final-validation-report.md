# Informe de validación final de publicación

**Fecha:** 27-07-2026<br>
**Rama:** `codex/integracion-global-libro`<br>
**Revisión de base:** `6df008b`
**Archivo principal:** `main.tex`

## Dictamen

| Dimensión | Resultado | Observación |
|---|---|---|
| Integración y compilación técnica | **Aprobada** | La reconstrucción limpia finalizó correctamente y produjo un PDF de 290 páginas. |
| Maquetación y legibilidad visual | **Aprobada** | No se observaron recortes, solapamientos, desbordes ni elementos ilegibles. |
| Preparación académica para publicación | **No aprobada todavía** | No existe un sistema bibliográfico activo y permanecen 199 afirmaciones marcadas para verificación externa. |

El manuscrito es técnicamente reproducible y estable, pero no debe distribuirse todavía como edición académica final. Los dos bloqueos documentales —bibliografía ausente y afirmaciones no verificadas— no son advertencias de LaTeX: requieren una revisión de fuentes primarias, clínicas y normativas.

## Reconstrucción desde cero

Se creó un directorio de salida vacío, externo al repositorio, y se ejecutó la receta oficial detectada en la configuración del proyecto:

```text
latexmk -synctex=1 -interaction=nonstopmode -file-line-error -pdf -outdir=<directorio-limpio>/build main.tex
```

`latexmk` realizó tres pasadas y terminó con código 0.

- PDF resultante: 290 páginas y 2.146.566 bytes.
- SHA-256: `dda53c0d09c95bff2ebc84fd48e4a876b9b27d202be188511d7a3645cb3b8f53`.
- Errores de TeX: 0.
- Referencias indefinidas: 0.
- Citas indefinidas: 0.
- Etiquetas duplicadas: 0.
- Archivos activos ausentes: 0.
- Solicitudes pendientes de otra pasada: 0.
- Cajas `Overfull`: 0.
- Cajas `Underfull \hbox`: 0.
- Cajas `Underfull \vbox`: 7, en las páginas 126, 130, 159, 181, 242, 271 y 278.

Las siete páginas con `Underfull \vbox` se inspeccionaron individualmente. Los avisos corresponden a distribución de texto y flotantes aceptable; no generan huecos anómalos, recortes ni colisiones.

La totalidad de las 290 páginas se renderizó y comparó con el PDF vigente de `build/`. Aunque los archivos binarios difieren por metadatos de creación, las 290 páginas resultaron idénticas píxel a píxel.

## Auditoría estructural

### Referencias, índice y numeración

- Se encontraron 521 etiquetas, todas únicas.
- La auditoría literal registró 352 órdenes `\ref`, `\eqref` o `\pageref`, dirigidas a 177 destinos diferentes; no existe ningún destino ausente. El validador estático del proyecto, que aplica un criterio de conteo más restrictivo, informó 287 referencias y llegó al mismo resultado de integridad.
- El índice contiene la Introducción no numerada y las diez unidades numeradas.
- Los capítulos `chap:unidad-1` a `chap:unidad-10` se resuelven exactamente como capítulos 1 a 10.
- No se detectaron prefijos de numeración incorrectos en figuras, tablas o ecuaciones.
- Los comienzos registrados en el índice son: Introducción, página 11; U1, 13; U2, 37; U3, 61; U4, 89; U5, 119; U6, 151; U7, 177; U8, 207; U9, 235; U10, 261.
- Las páginas en blanco entre unidades son coherentes con la apertura de capítulos en página impar de la clase de libro; no son pérdidas de contenido.

### Ecuaciones

- Hay 117 entornos de ecuación numerados y todos poseen etiqueta.
- Existen 118 etiquetas `eq:` porque un entorno `align` de la Unidad 5 contiene dos ecuaciones etiquetadas.
- La numeración por unidad es coherente: U1 2; U2 14; U3 16; U4 27; U5 21; U6 5; U7 8; U8 4; U9 10; U10 11.
- La inspección de todas las páginas con ecuaciones no incluidas ya en otros controles no mostró ecuaciones fuera del área útil, números separados ni símbolos ilegibles.

### Tablas

- Hay seis tablas numeradas; todas poseen epígrafe y etiqueta.
- Se encontraron ocho estructuras tabulares en total.
- Dos cuadros comparativos de la Unidad 10, en las páginas 273 y 277, se presentan sin entorno `table`, epígrafe ni etiqueta. Son legibles y no afectan la compilación, pero conviene formalizarlos como tablas numeradas si deben citarse o integrar el listado editorial de tablas.
- Las tablas mantienen su contenido dentro del área de impresión.

### Figuras y archivos gráficos

- Hay 64 entornos `figure`; todos poseen epígrafe y al menos una etiqueta.
- Las ocho inclusiones gráficas externas existen y corresponden a PDF vectoriales reproducibles de las Unidades 5 y 10.
- El PDF final no contiene imágenes raster incrustadas. La resolución, por lo tanto, no está limitada por una trama de píxeles: las figuras activas son vectoriales o TikZ.
- Los ocho PDF generados se revisaron individualmente: no contienen imágenes raster ni fuentes sin incrustar.
- Se detectaron dos figuras de la Unidad 8 con una etiqueta semántica y un alias heredado. No existe duplicación de claves ni fallo de referencia, pero esos alias pueden retirarse cuando se compruebe que ninguna edición externa depende de ellos.

### Glosarios

- Las diez unidades contienen un glosario.
- Los títulos, cortes de página y listas de términos se inspeccionaron en el PDF; no se observaron desbordes ni inconsistencias graves de presentación.
- El proyecto no utiliza un paquete de glosario con índice global: los glosarios son secciones ordinarias dentro de cada unidad.

### Enlaces

- El PDF contiene 649 enlaces internos y 2.195 destinos nombrados.
- No se detectaron enlaces internos con destino inexistente.
- El manuscrito no contiene órdenes `\href`, `\url` ni direcciones web activas; por lo tanto, no hay enlaces externos que comprobar.
- Los campos PDF `/Title`, `/Author`, `/Subject` y `/Keywords` están vacíos. El título y el autor se imprimen correctamente en la portada, pero se recomienda completar los metadatos mediante la configuración global de `hyperref` antes de distribuir el archivo.

### Bibliografía y afirmaciones pendientes

- Archivos `.bib`: 0.
- Órdenes de cita: 0.
- Órdenes de bibliografía: 0.
- Bibliografía generada: inexistente.
- Bloques activos `\verify{...}`: 199.

El texto literal `\verify{...}` aparece tres veces más dentro de ejemplos impresos mediante `\verb`, una vez en cada una de las Unidades 8, 9 y 10; esas tres apariciones no son afirmaciones pendientes. La distribución activa corregida es:

| Unidad | Bloques activos |
|---|---:|
| 1 | 5 |
| 2 | 6 |
| 3 | 4 |
| 4 | 19 |
| 5 | 11 |
| 6 | 27 |
| 7 | 23 |
| 8 | 70 |
| 9 | 24 |
| 10 | 10 |
| **Total** | **199** |

La ausencia de citas indefinidas en el log no equivale a una bibliografía aprobada: no hay citas porque todavía no se incorporó el sistema bibliográfico. Esta situación bloquea la publicación académica.

## Advertencias y análisis estático

El validador del proyecto revisó 68 archivos TeX y produjo 61 avisos heurísticos. Las supuestas rutas absolutas o inclusiones ausentes se originan en caracteres acentuados de la ruta de Windows, saltos de línea de TikZ y marcadores `\verify{...}`. El archivo `.fls`, la auditoría literal y la compilación limpia confirman que no falta ningún archivo activo.

ChkTeX se ejecutó sobre los 68 archivos de forma individual:

- Errores: 0.
- Advertencias: 1.799, distribuidas en 23 archivos.
- Reglas predominantes: W24, W10, W9, W44, W8, W13 y W12.

La mayoría corresponde a convenciones deliberadas del proyecto: ubicación de `\label`, intervalos y delimitadores matemáticos, guiones, espaciado español y tablas con reglas verticales. No se aplicaron correcciones automáticas porque esas reglas no identifican por sí solas errores inequívocos. W44 sí señala una oportunidad editorial: las tablas podrían homogeneizarse progresivamente con un criterio tipográfico equivalente a `booktabs`.

El entorno añadió dos avisos no bloqueantes: `C.UTF-8` no está disponible y MiKTeX todavía no comprobó si existen actualizaciones. Ninguno alteró la compilación ni el PDF.

## Consistencia tipográfica

- No aparecen las formas heredadas `dBSPL`, `dBA`, `\mathrm{dB\ SPL}` ni magnitudes `L_{Aeq...}` sin el operador `eq` romanizado.
- Las magnitudes y referencias se distinguen correctamente entre dB SPL, dB HL, dB SL y niveles ponderados.
- Todavía conviven formas fuente visualmente equivalentes:
  - `\text{dB SPL}`: 103; `\mathrm{dB\,SPL}`: 27.
  - `\text{dB HL}`: 12; `\mathrm{dB\,HL}`: 39.
  - `\mathrm{dB\,SL}`: 9.
- Esta convivencia no produce contradicción visual ni científica, pero conviene reemplazarla por comandos globales antes de futuras ediciones para evitar nuevas divergencias.
- Las 62 fuentes o subconjuntos tipográficos usados por el PDF están incrustados.

## Inspección visual

Se inspeccionaron:

- vistas generales de las 290 páginas;
- portada, índice e inicios de capítulos;
- todas las páginas con figuras;
- todas las páginas con tablas;
- los diez glosarios;
- las siete páginas con avisos `Underfull`;
- 50 páginas adicionales con ecuaciones;
- el cierre de la Unidad 10.

Resultado:

- sin texto, ecuaciones, tablas o figuras recortados;
- sin solapamientos;
- sin encabezados o números de ecuación fuera del área útil;
- sin imágenes pixeladas;
- ejes, unidades, rótulos y epígrafes legibles al tamaño de página;
- contraste suficiente en los gráficos inspeccionados;
- consistencia visual general entre figuras TikZ y PDF vectoriales;
- páginas en blanco justificadas por la estructura editorial del libro.

## Cambios necesarios antes de publicar

### Imprescindibles

1. Incorporar un sistema bibliográfico administrado.
2. Resolver los 199 bloques activos `\verify{...}` con fuentes primarias, bibliografía académica reconocida y normas versionadas.
3. Repetir esta validación después de incorporar las citas, porque la bibliografía puede modificar paginación, índice, referencias y composición.

### Recomendados

1. Completar los metadatos PDF de título, autor, asunto y palabras clave.
2. Formalizar los dos cuadros sin epígrafe de la Unidad 10 si deben tratarse como tablas citables.
3. Unificar mediante comandos globales la composición de dB SPL, dB HL y dB SL.
4. Homogeneizar gradualmente el estilo de tablas.
5. Retirar los dos alias heredados de etiquetas de figuras de la Unidad 8 cuando se confirme que no existen dependencias externas.
6. Actualizar MiKTeX y normalizar la configuración regional del entorno de compilación antes de fijar el entorno de publicación.

### Aceptados sin corrección

1. Los siete avisos `Underfull \vbox`, porque no causan defectos visibles.
2. Los avisos heurísticos de ChkTeX que responden a convenciones válidas y no señalan un error concreto.
3. Las páginas en blanco exigidas por la apertura de capítulos en página impar.

## Conclusión

La edición supera la validación técnica integral: compila limpiamente, sus referencias internas son íntegras, la numeración es coherente, no faltan archivos y la salida visual es legible y reproducible. La aprobación para publicación queda condicionada exclusivamente a cerrar la trazabilidad académica de las afirmaciones y a reconstruir el libro con la bibliografía resultante.
