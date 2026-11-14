# PlantGuard Pro

Calculadora web de PlantGuard Pro, pensada para enlazarse o insertarse en otra página web. El repositorio guarda también el modelo financiero y la base de conocimiento de los que sale el cálculo.

> **Estado: prefactibilidad condicionada.** Las cifras precargadas son *hipótesis ilustrativas*. No hay todavía evidencia (piloto, cotizaciones, precios reales) para un dictamen favorable de inversión. Ver acciones PG-FIN-01 a PG-FIN-08.

## Contenido

| Ruta | Qué es |
| --- | --- |
| `web/index.html` | Calculadora web (se publica en Vercel). Muestra valor bruto recuperable, VAN, TIR, payback y ROI por escenario, y el flujo de caja año a año. |
| `web/roi.js` | Motor de cálculo. Misma lógica que el modelo Excel. |
| `tests/roi.test.mjs` | Pruebas del motor: reproduce la hoja original y el Excel recalculado (incluye impuestos, depreciación, reposición y rendimiento neto). |
| `tests/smoke.mjs` | Prueba en navegador real: escritorio, celular, modo insertado y versión publicada. |
| `tests/check_modelo.py` | Verifica que el Excel versionado coincide con su generador. |
| `.github/workflows/verificacion.yml` | Verificación automática en GitHub (ver abajo). |
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
npm test                     # pruebas del motor de cálculo
npm run smoke                # prueba en navegador (requiere Playwright)
node tests/smoke.mjs <url>   # prueba la versión publicada
npm run modelo               # regenera el Excel (requiere python3 + openpyxl)
python3 tests/check_modelo.py
```

## Verificación automática

GitHub Actions (pestaña **Actions** del repositorio) ejecuta todo lo anterior en cada cambio. Además, todos los días a las 08:17 (hora de Chile) y unos minutos después de cada cambio en `main`, prueba la web publicada en https://plantgard-kh23.vercel.app. Si algo falla, GitHub te avisa por correo.

Para ver la web en local, sirve la carpeta `web/` con cualquier servidor estático, por ejemplo `npx serve web`.

## Enlazar la calculadora desde una página web

Una vez publicada en Vercel tendrás una dirección como `https://plantgard.vercel.app` (la exacta la muestra Vercel).

**Opción 1: enlace o botón.** Abre la calculadora como página completa:

```html
<a href="https://plantgard.vercel.app">Calcula cuánto podrías recuperar</a>
```

**Opción 2: insertada dentro de la página.** Dentro de un iframe la calculadora oculta su título y su fondo, y avisa su altura para que no aparezcan barras de desplazamiento:

```html
<iframe id="plantguard-calc" src="https://plantgard.vercel.app" title="Calculadora PlantGuard Pro"
        style="width:100%;border:0;height:1100px" loading="lazy"></iframe>
<script>
  addEventListener("message", (e) => {
    if (e.data && e.data.plantguard === "altura")
      document.getElementById("plantguard-calc").style.height = e.data.altura + "px";
  });
</script>
```

Si el constructor de páginas (Wix, WordPress, etc.) no permite el `<script>`, basta con el `<iframe>`: se verá igual, con la altura fija indicada. Para ver el modo insertado sin iframe, agrega `?embed=1` a la dirección.

## Despliegue en Vercel

1. En https://vercel.com/new importa `kaijufightwearspa/Plantgard`.
2. Deja la configuración por defecto: `vercel.json` ya indica que se publica la carpeta `web/`.
3. Pulsa **Deploy**. Cada `push` a la rama principal vuelve a publicar automáticamente; las otras ramas generan una URL de vista previa.
