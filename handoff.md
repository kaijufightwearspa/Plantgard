# Handoff — PlantGuard Pro

_Actualizado: 14-11-2026_

## Objetivo
Calculadora web de PlantGuard Pro, publicada en Vercel, para enlazar (y más adelante insertar) en la futura web de PlantGuard.

## Estado
- Calculadora en `main` (PR #1 fusionado): `web/index.html` + `web/roi.js`. Pruebas: `npm test` (3/3).
- Modelo ROI v1.0 en Excel (`modelo/`) y base de conocimiento v2.0 (`docs/`) rescatados desde Google Drive y Claude Sheets.
- Artifact de prueba (privado): https://claude.ai/artifact/XxcNPXutosGQ4GGTJLemco — incluye tabla de flujo año a año que la versión web aún no tiene.
- Claude Code configurado: graphify (grafo de código + hooks), skills `find-skills`, `motor-fallback`, `plantguard-error-prevention`, protocolo en `CLAUDE.md`.

## Próximos pasos
1. Usuario: importar el repositorio en Vercel y obtener la URL pública.
2. Verificar la calculadora publicada en esa URL.
3. Decidir si la versión web incorpora la tabla de flujo año a año del artifact.
4. Decidir si el repositorio pasa a privado (hoy es público y expone `docs/` y `modelo/`).

## Verificar
```bash
npm test
graphify query "calculo del VAN"
```
