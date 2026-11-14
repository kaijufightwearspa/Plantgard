---
name: plantguard-error-prevention
description: Lista de control obligatoria antes de cambiar o publicar la calculadora, el modelo ROI o los textos financieros de PlantGuard Pro. Úsala al tocar web/, modelo/, tests/ o docs/, al cambiar fórmulas, supuestos, etiquetas o mensajes al cliente, y antes de cualquier commit, pull request o despliegue en Vercel.
---

# plantguard-error-prevention

Errores que este proyecto no puede permitirse: cifras distintas entre la web y el Excel, prometer rentabilidad sin evidencia, y romper el despliegue.

## Antes de cambiar

1. Ubica lo afectado con `graphify query "<tema>"` o `graphify explain "<función>"`; lee solo esas líneas.
2. Fuente de verdad del cálculo: `web/roi.js`. El Excel (`modelo/generar_modelo.py`) debe implementar la misma lógica.

## Reglas de contenido (base de conocimiento v2.0)

- «Valor bruto recuperable» **no es ROI**. Nunca etiquetar el valor bruto como ROI, ahorro ni utilidad.
- «Eficacia» = % de la pérdida actual que se evita, **no** puntos porcentuales (PG-FIN-01).
- Rendimiento bruto y neto son marcos alternativos: nunca sumar ni mezclar ambos.
- Los valores precargados son hipótesis ilustrativas: el texto visible debe decirlo y no prometer resultados.
- No mezclar datos de otros proyectos o empresas.

## Verificación obligatoria (todas deben pasar)

```bash
npm test                         # motor vs. valores de la hoja original
python3 modelo/generar_modelo.py # si cambió la lógica del modelo
```

Valores de control con los datos de ejemplo: valor bruto 32.000 / 128.000 / 320.000 CHF; VAN −10.199 / 84.055 / 272.561 CHF; umbral de equilibrio 6,6 %. Si cambia uno de estos números sin que se haya pedido cambiar un supuesto, es un error: detente y revisa.

Si cambió `web/index.html`: abre la página en Chromium a 1200 px y a 390 px, sin desborde horizontal ni errores de consola, y también dentro de un iframe (modo insertado).

## Antes de publicar

- Un solo commit o pull request con todos los cambios agrupados.
- `vercel.json` sigue publicando solo `web/` (nada de `docs/` ni `modelo/`).
- Nunca saltar, desactivar ni borrar una prueba para que pase.
- Actualiza `handoff.md`.
