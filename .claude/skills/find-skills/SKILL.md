---
name: find-skills
description: Busca skills ya existentes por palabras clave antes de programar algo nuevo. Úsala cuando el usuario escriba /find-skills "<tema>", pregunte si ya hay una skill para algo, o antes de empezar un flujo de trabajo que podría estar resuelto (deploy, auditoría, reportes, PDF, Excel, etc.).
---

# find-skills

Objetivo: reutilizar antes de construir. Busca en este orden y detente en cuanto aparezca algo que sirva.

## 1. Skills del proyecto

Lista `.claude/skills/*/SKILL.md` y lee solo el bloque `description` del frontmatter de cada una (las primeras 5 líneas). No leas el cuerpo salvo que el nombre o la descripción encajen con la búsqueda.

## 2. Skills ya cargadas en la sesión

Revisa la lista de skills disponibles que el sistema muestra en la conversación (incluye las integradas como `loop`, `code-review`, `simplify`, `security-review` y las de `anthropic-skills:*`, por ejemplo `anthropic-skills:skill-creator`, `pdf`, `xlsx`, `docx`, `pptx`).

## 3. Skills de la cuenta de claude.ai

Si existen las herramientas `SearchSkills` / `ListSkills` (cárgalas con ToolSearch si aparecen como diferidas), llama a `SearchSkills` con 2 a 5 palabras clave del tema. Si una encaja y no está habilitada, ofrécela con `SuggestSkills`.

## 4. Plugins

Si existe `SearchPlugins`, búscalo con las mismas palabras clave.

## Respuesta

Devuelve una tabla corta: nombre, dónde está (proyecto / sesión / cuenta / plugin), para qué sirve en una línea y cómo invocarla. Si no hay nada que sirva, dilo en una línea y propone crearla con `anthropic-skills:skill-creator` solo si la tarea se va a repetir 3 o más veces.

## Reglas

- No inventes skills ni nombres: solo lo que encontraste.
- No instales nada sin que el usuario lo pida.
