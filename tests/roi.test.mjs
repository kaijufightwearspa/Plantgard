// npm test   — verifica el motor contra los valores de la hoja original (revisión 11)
import { test } from "node:test";
import assert from "node:assert/strict";
import { DEFAULTS, modelo, validar } from "../web/roi.js";

const close = (a, b, tol = 0.01) => assert.ok(Math.abs(a - b) < tol, `${a} ≠ ${b}`);

test("caso ilustrativo v2.0 reproduce la hoja", () => {
  const m = modelo(DEFAULTS);
  assert.deepEqual(m.errores, []);
  close(m.derivados.valorPerdida, 640000);
  const { conservador: c, base: b, optimista: o } = m.escenarios;
  close(c.brutoRegimen, 32000);
  close(c.van, -10198.697157434402);
  close(b.van, 84054.65561224488);
  close(o.van, 272561.36115160346);
  close(c.tir, -0.15676983652156526, 1e-6);
  close(b.tir, 1.7346619772796317, 1e-6);
  close(c.roi, -0.3508, 1e-9);
  close(b.roi, 5.6468, 1e-9);
  assert.equal(c.payback, null);
  assert.equal(b.payback, 1);
  close(m.umbral, 0.06623077088147139, 1e-9);
  close(m.vanSinEficacia, -41616.48141399416);
});

test("rendimiento neto eleva el potencial", () => {
  const m = modelo({ ...DEFAULTS, base: "neto" });
  close(m.derivados.valorPerdida, 711111.11);
  close(m.escenarios.conservador.brutoRegimen, 35555.56);
});

test("valida entradas", () => {
  assert.ok(validar({ ...DEFAULTS, perdida: 1 }).length > 0);
  assert.ok(validar({ ...DEFAULTS, horizonte: 6 }).length > 0);
  assert.ok(validar({ ...DEFAULTS, area: NaN }).length > 0);
  assert.ok(validar({ ...DEFAULTS, eficacias: { a: 1.2 } }).length > 0);
});

test("escenario completo coincide con el Excel recalculado (impuesto, depreciación, reposición, residual, neto, 5 años)", () => {
  // Valores de referencia: modelo/PlantGuard_Pro_Modelo_ROI_v1.0.xlsx con estas entradas, recalculado en LibreOffice.
  const p = {
    ...DEFAULTS, area: 750, rendimiento: 320, base: "neto", ciclos: 3, perdida: 0.18, precio: 6.5,
    realizacion: 0.9, margen: 0.55, hardware: 30000, instalacion: 5000, capacitacion: 2000, capitalTrabajo: 4000,
    licencia: 7000, mantenimiento: 1500, reposicion: 8000, anioReposicion: 3, valorResidual: 3000,
    tasa: 0.1, horizonte: 5, impuesto: 0.27, vidaUtil: 4,
    eficacias: { conservador: 0.08, base: 0.25, optimista: 0.6 }, rampa: [0.5, 0.8, 0.95, 1, 1],
  };
  const m = modelo(p);
  assert.deepEqual(m.errores, []);
  const excel = {
    conservador: [82185.3658536585, 34357.2163876887, 0.342113124982853, 3, 1.52780849494349],
    base: [256829.268292683, 232097.625819105, 1.34890077640933, 1, 8.06944727840571],
    optimista: [616390.243902439, 639210.233472021, 3.06357730648244, 1, 21.5375271267103],
  };
  for (const [k, [bruto, van, tir, payback, roi]] of Object.entries(excel)) {
    const e = m.escenarios[k];
    close(e.brutoRegimen, bruto);
    close(e.van, van);
    close(e.tir, tir, 1e-6);
    assert.equal(e.payback, payback);
    close(e.roi, roi, 1e-9);
  }
  close(m.umbral, 0.050462654534288, 1e-9);
  close(m.vanSinEficacia, -58697.0939329778);
});
