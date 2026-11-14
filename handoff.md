# Handoff — PlantGuard Pro

_Actualizado: 14-11-2026 (ronda de mejora continua 1)_

## Objetivo
Calculadora web de PlantGuard Pro, publicada en Vercel, para enlazar (y más adelante insertar) en la futura web de PlantGuard.

## Estado
- Calculadora en `main` (PR #1 fusionado): `web/index.html` + `web/roi.js`. Pruebas: `npm test` (3/3).
- Modelo ROI v1.0 en Excel (`modelo/`) y base de conocimiento v2.0 (`docs/`) rescatados desde Google Drive y Claude Sheets.
- Artifact de prueba (privado): https://claude.ai/artifact/XxcNPXutosGQ4GGTJLemco. La web ya tiene sus mejoras (flujo año a año, «Volver al ejemplo», campos en rojo).
- Verificación automática en GitHub Actions: pruebas del motor, Excel vs. generador, navegador, y la web publicada a diario.
- Paridad comprobada web = Excel también con impuesto, depreciación, reposición, capital de trabajo, residual, rendimiento neto y horizonte 5.
- Publicada en Vercel: https://plantgard-kh23.vercel.app (pendiente verificarla; la red de la sesión en la nube no llega a ese dominio).
- Claude Code configurado: graphify (grafo de código + hooks), skills `find-skills`, `motor-fallback`, `plantguard-error-prevention`, protocolo en `CLAUDE.md`.

## Próximos pasos
1. Usuario: verificar la calculadora en https://plantgard-kh23.vercel.app (escritorio y celular).
2. Opcional: dominio propio en Vercel (Settings → Domains).
3. Decidir si el repositorio pasa a privado (hoy es público y expone `docs/` y `modelo/`).

## Verificar
```bash
npm test
npm run smoke
python3 tests/check_modelo.py
graphify query "calculo del VAN"
```
