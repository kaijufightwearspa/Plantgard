---
name: motor-fallback
description: Plan de continuidad cuando se agota el saldo o el límite de uso, o el modelo actual está saturado. Úsala cuando el usuario diga que se le acabó el saldo o el límite, pida cambiar de modelo para gastar menos, o aparezca un error de límite de uso o de sobrecarga.
---

# motor-fallback

Claude Code no puede cambiar de proveedor ni consultar el saldo por sí mismo. Esta skill deja el trabajo listo para continuar con otro modelo o en otro momento sin perder contexto.

## 1. Guardar el estado primero

Antes de cualquier cambio, actualiza `handoff.md` en la raíz del repositorio (objetivo, estado, próximos pasos, archivos tocados, comandos para verificar). Si hay cambios sin guardar, haz commit y push a la rama de trabajo.

## 2. Bajar de modelo según la tarea

Dile al usuario qué escribir, porque solo él puede cambiar el modelo:

| Tarea pendiente | Modelo sugerido | Comando |
| --- | --- | --- |
| Diseño, depuración difícil, revisión financiera | el actual | — |
| Cambios acotados con tests claros | Sonnet | `/model sonnet` |
| Tareas mecánicas: renombrar, formatear, mover archivos, actualizar textos | Haiku | `/model haiku` |

Si Haiku no alcanza: esperar a que se reinicie el límite, o continuar en otra herramienta pegándole `handoff.md` como contexto.

## 3. Gastar menos mientras tanto

- Responde corto, sin repetir lo ya dicho.
- Usa `graphify query` en vez de leer archivos completos.
- Agrupa los cambios en una sola pasada.

## Reglas

- No afirmes que cambiaste el modelo o el proveedor: solo el usuario puede hacerlo.
- No borres trabajo para "ahorrar"; primero guarda en `handoff.md` y en git.
