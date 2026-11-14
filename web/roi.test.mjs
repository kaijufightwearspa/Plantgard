// node --test web/   — verifica el motor contra los valores de la hoja original (revisión 11)
import { test } from "node:test";
import assert from "node:assert/strict";
import { DEFAULTS, modelo, validar } from "./roi.js";

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
