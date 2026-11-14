# PlantGuard Pro — instrucciones para Claude Code

Proyecto: calculadora web de PlantGuard Pro (`web/`), modelo ROI en Excel (`modelo/`) y base de conocimiento (`docs/`). Se publica en Vercel desde `main` (solo la carpeta `web/`). Idioma de trabajo: español (Chile).

## Protocolo de ahorro de tokens (siempre activo)

1. **Graphify antes de grep/read.** Para buscar símbolos, quién llama a qué, impacto de un cambio o qué prueba cubre algo: `graphify query`, `graphify explain` o `graphify path` primero (detalle abajo). Lee solo las líneas que el grafo señala.
2. **Subagentes baratos para lo mecánico.** Renombrar, formatear, mover archivos, búsquedas amplias o actualizar textos repetitivos: delega a un subagente con `model: "haiku"` y un prompt autocontenido (incluye la regla de graphify). El razonamiento financiero y las decisiones se quedan en la sesión principal.
3. **Una sola pasada.** Agrupa los cambios, un commit o un pull request por tarea, ediciones puntuales en vez de reescribir archivos enteros.
4. **Contexto mínimo.** No vuelvas a leer lo que ya está en la conversación; usa `offset`/`limit` al leer; respuestas cortas.
5. **`handoff.md` al día.** Al cerrar una tarea o antes de cambiar de modelo, actualiza objetivo, estado y próximos pasos.

## Skills

- **Antes de programar algo nuevo**, usa `/find-skills "<tema>"` para ver si ya existe una skill.
- **Si un trabajo se repite 3 o más veces**, créale una skill con `anthropic-skills:skill-creator` y guárdala en `.claude/skills/`.
- **Tareas recurrentes o de seguimiento:** `/loop`.
- **Si se agota el saldo o el límite:** `/motor-fallback` (guarda el estado; el usuario cambia con `/model sonnet` o `/model haiku`).
- **Al tocar la calculadora, el modelo o textos financieros:** sigue `/plantguard-error-prevention` antes de hacer commit.

## graphify (detalle)

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- When graphify-out/graph.json exists, run `graphify query "<question>"` before your first grep, search or source-file read for a codebase question, and put this rule in every subagent prompt that explores code. Read raw files only for lines the graph or an earlier read already located. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
- A committed graphify-out/graph.json is rewritten whole on every build, so a large diff to it in a pull request is expected. Do not flag it as churn or suggest skipping the graph rebuild or its hooks.
