# PlantGuard Pro

Repositorio de trabajo de PlantGuard Pro: la calculadora web, el modelo financiero por cliente y la base de conocimiento del expediente.

> **Estado: prefactibilidad condicionada.** Las cifras precargadas son *hipótesis ilustrativas*. No hay todavía evidencia (piloto, cotizaciones, precios reales) para un dictamen favorable de inversión. Ver acciones PG-FIN-01 a PG-FIN-08.

## Contenido

| Ruta | Qué es |
| --- | --- |
| `web/index.html` | Calculadora web (se publica en Vercel). Muestra valor bruto recuperable, VAN, TIR, payback y ROI por escenario. |
| `web/roi.js` | Motor de cálculo. Misma lógica que el modelo Excel. |
| `web/roi.test.mjs` | Pruebas: verifican que el motor reproduce los valores de la hoja original. |
| `modelo/PlantGuard_Pro_Modelo_ROI_v1.0.xlsx` | Modelo ROI por cliente con fórmulas (Resultados, Entradas, Flujos, Sensibilidad, Guía de datos). |
| `modelo/generar_modelo.py` | Regenera el .xlsx desde código. |
| `docs/PlantGuard_Pro_Base_Conocimiento_v2.0.md` | Base maestra de conocimiento v2.0 (exportada de Google Drive, 14-11-2026). |

## Origen de los datos

- **Base de conocimiento v2.0**: Google Doc «PlantGuard Pro | Conocimiento financiero maestro para Claude | v2.0».
- **Modelo ROI v1.0**: hoja «PlantGuard Pro — Modelo ROI por cliente v1.0» (Claude Sheets, revisión 11).

Resultados del caso ilustrativo (deben coincidir en la web, el Excel y la hoja):

| Escenario (% de la pérdida que se evita) | Valor bruto/año | VAN 3 años al 12 % | ROI simple |
| --- | --- | --- | --- |
| Conservador (5 %) | CHF 32.000 | CHF −10.199 | −35,1 % |
| Base (20 %) | CHF 128.000 | CHF 84.055 | 564,7 % |
| Optimista (50 %) | CHF 320.000 | CHF 272.561 | 1.764,2 % |

Umbral de equilibrio: hay que evitar al menos el **6,6 %** de la pérdida actual para que el VAN sea 0.

## Uso

```bash
npm test          # pruebas del motor de cálculo
npm run modelo    # regenera el Excel (requiere python3 + openpyxl)
```

Para ver la web en local, sirve la carpeta `web/` con cualquier servidor estático, por ejemplo `npx serve web`.

## Despliegue en Vercel

1. En https://vercel.com/new importa `kaijufightwearspa/Plantgard`.
2. Deja la configuración por defecto: `vercel.json` ya indica que se publica la carpeta `web/`.
3. Pulsa **Deploy**. Cada `push` a la rama principal vuelve a publicar automáticamente; las otras ramas generan una URL de vista previa.
