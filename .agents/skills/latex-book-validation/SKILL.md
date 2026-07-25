---
name: latex-book-validation
description: Compila y valida el libro LaTeX, identifica errores, referencias o citas indefinidas, etiquetas duplicadas, figuras faltantes y advertencias relevantes. Usar al terminar ediciones o cuando el usuario pida compilar, verificar o diagnosticar el proyecto.
---

# Objetivo

Demostrar que los cambios se integran correctamente en el libro y documentar cualquier problema preexistente.

# Procedimiento

## 1. Descubrir el flujo real

Buscar, en este orden:

1. instrucciones en `AGENTS.md` y archivos anidados;
2. `README`;
3. `Makefile` o scripts equivalentes;
4. `latexmkrc`;
5. configuración del editor o CI;
6. archivo principal que contenga `\documentclass` y `\begin{document}`.

No asumir `main.tex` ni `pdflatex` si el repositorio indica otra cosa.

## 2. Revisar el estado antes de compilar

- identificar archivos modificados;
- confirmar que no se editaron artefactos generados;
- comprobar rutas relativas de figuras y bibliografía;
- registrar errores conocidos si ya estaban documentados.

## 3. Ejecutar validación estática

Ejecutar, ajustando la ruta al repositorio:

```bash
python .agents/skills/latex-book-validation/scripts/check_latex_project.py .
```

Tratar el resultado como una ayuda heurística, no como un parser completo de LaTeX.

Ejecutar también los linters ya configurados. No instalar herramientas nuevas sin autorización.

## 4. Compilar

Usar el comando oficial del repositorio. Si no existe, proponer un comando `latexmk` compatible con el motor detectado.

Capturar:

- código de salida;
- primer error real;
- referencias indefinidas;
- citas indefinidas;
- etiquetas duplicadas;
- archivos ausentes;
- `Overfull \hbox` relevantes;
- ciclos de compilación incompletos.

No intentar corregir automáticamente problemas ajenos al alcance sin informar al usuario.

## 5. Inspección visual

Cuando cambien figuras, tablas, ecuaciones o maquetación:

- renderizar o abrir las páginas afectadas;
- revisar cortes, solapamientos, tamaños, ubicación y legibilidad;
- confirmar que la figura coincide con su epígrafe y referencia.

## 6. Resultado

Informar:

- comando ejecutado;
- resultado de compilación;
- validaciones estáticas;
- advertencias nuevas;
- advertencias preexistentes relevantes;
- páginas inspeccionadas;
- problemas pendientes.

No declarar éxito cuando el comando de compilación haya fallado.
