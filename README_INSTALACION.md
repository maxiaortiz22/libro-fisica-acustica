# Instalación y uso en Codex

## 1. Copiar los archivos

Copiá en la raíz del repositorio del libro:

```text
AGENTS.md
.agents/
```

La estructura debería quedar así:

```text
mi-libro/
├── AGENTS.md
├── main.tex                 # o el archivo principal que ya utilices
├── ...
└── .agents/
    └── skills/
        ├── acoustic-book-authoring/
        ├── acoustic-book-review/
        ├── acoustic-figure-workflow/
        └── latex-book-validation/
```

No hace falta “instalar” estas skills ni registrarlas en otro archivo cuando se encuentran dentro de `.agents/skills` del repositorio.

## 2. Abrir Codex desde el repositorio

Codex descubre `AGENTS.md` y las skills en función del directorio de trabajo. Abrí el proyecto en el IDE o iniciá Codex desde la raíz o desde una subcarpeta del mismo repositorio.

Después de copiar o editar los archivos, conviene comenzar una sesión nueva. Las skills suelen actualizarse automáticamente; si una no aparece, reiniciá Codex.

## 3. Verificar que fueron detectados

En Codex CLI podés pedir:

```text
Indicá qué archivos AGENTS.md cargaste y qué skills están disponibles para este repositorio.
```

También podés ejecutar `/skills` o escribir `$` para ver las skills disponibles.

Para verificar específicamente `AGENTS.md`:

```bash
codex --ask-for-approval never "Resumí las instrucciones activas del proyecto e indicá de qué archivos provienen."
```

## 4. Invocación automática y explícita

`AGENTS.md` se carga automáticamente al iniciar la ejecución o sesión. No hace falta nombrarlo en cada prompt.

Las skills pueden activarse de dos maneras:

- **Implícita:** Codex decide usarlas cuando el pedido coincide con su descripción.
- **Explícita:** se menciona la skill mediante `$nombre-de-la-skill`.

Para tareas importantes conviene la invocación explícita, al menos durante las primeras iteraciones.

Ejemplos:

```text
$acoustic-book-authoring Ampliá la sección sobre impedancia acústica de la Unidad 4. Conservá el nivel matemático del resto del capítulo y agregá un ejemplo aplicado al oído medio.
```

```text
$acoustic-book-review Revisá la Unidad 1 en modo científico y pedagógico. Primero entregá un informe de hallazgos; no modifiques archivos todavía.
```

```text
$acoustic-figure-workflow Creá una figura reproducible que compare presión instantánea, presión RMS y valor medio para una sinusoide. Integrala en la Unidad 4.
```

```text
$latex-book-validation Compilá el libro, revisá referencias, citas, figuras y advertencias relevantes. Corregí solamente los problemas provocados por los cambios actuales.
```

## 5. Qué archivo usar para cada cosa

- `AGENTS.md`: reglas permanentes que deben cumplirse en todas las tareas del repositorio.
- `SKILL.md`: procedimiento especializado para un tipo de trabajo repetible.
- `references/`: criterios, mapas y plantillas que la skill consulta cuando se activa.
- `scripts/`: validaciones deterministas que complementan al modelo.
- Prompt: objetivo concreto de la tarea actual.

## 6. Skills globales opcionales

Estas skills están pensadas para este libro, por eso se incluyen en el repositorio. Si quisieras que una skill estuviera disponible en cualquier proyecto, podrías colocarla en:

```text
$HOME/.agents/skills/
```

No conviene hacerlo con reglas exclusivas de este libro, porque podrían activarse en repositorios no relacionados.

## 7. Ajustes recomendados

Antes del primer uso, revisá en `AGENTS.md`:

- el nombre real del archivo principal;
- el motor de LaTeX utilizado;
- el comando de compilación;
- la convención bibliográfica;
- la estructura real de carpetas.

El archivo está escrito para descubrir esas decisiones en el repositorio y no imponerlas, por lo que puede utilizarse aun antes de completar esos datos.
