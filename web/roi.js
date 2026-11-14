// Motor de cálculo PlantGuard Pro — misma lógica que modelo/PlantGuard_Pro_Modelo_ROI_v1.0.xlsx
// (pestañas Entradas → Flujos → Resultados). Sin redondeos: se redondea solo al mostrar.

export const DEFAULTS = Object.freeze({
  area: 500,               // m²
  rendimiento: 400,        // g/m² por ciclo
  base: "bruto",           // "bruto" | "neto"
  ciclos: 4,               // ciclos/año
  perdida: 0.10,           // fracción del potencial
  precio: 8,               // CHF/g neto realizable
  realizacion: 0.85,
  margen: 0.60,
  hardware: 20000, instalacion: 0, capacitacion: 0, capitalTrabajo: 0,
  licencia: 9000, mantenimiento: 0,
  reposicion: 0, anioReposicion: 0, valorResidual: 0,
  tasa: 0.12, horizonte: 3, impuesto: 0, vidaUtil: 5,
  eficacias: { conservador: 0.05, base: 0.20, optimista: 0.50 },
  rampa: [0.60, 0.85, 1.0, 1.0, 1.0],
});

export function validar(p) {
  const errores = [];
  const num = (k) => typeof p[k] === "number" && Number.isFinite(p[k]);
  for (const k of ["area", "rendimiento", "ciclos", "perdida", "precio", "realizacion", "margen",
    "hardware", "instalacion", "capacitacion", "capitalTrabajo", "licencia", "mantenimiento",
    "tasa", "horizonte", "impuesto", "vidaUtil"]) {
    if (!num(k)) errores.push(`${k}: debe ser un número`);
    else if (p[k] < 0) errores.push(`${k}: no puede ser negativo`);
  }
  if (num("perdida") && p.perdida >= 1) errores.push("perdida: debe ser menor que 100 %");
  if (num("realizacion") && p.realizacion > 1) errores.push("realizacion: máximo 100 %");
  if (num("horizonte") && (p.horizonte < 1 || p.horizonte > 5 || !Number.isInteger(p.horizonte)))
    errores.push("horizonte: entero entre 1 y 5");
  if (p.base !== "bruto" && p.base !== "neto") errores.push('base: "bruto" o "neto"');
  for (const [k, v] of Object.entries(p.eficacias ?? {}))
    if (!Number.isFinite(v) || v < 0 || v > 1) errores.push(`eficacia ${k}: entre 0 y 100 %`);
  return errores;
}

export function derivados(p) {
  const declarada = p.area * p.rendimiento * p.ciclos;
  const potencial = p.base === "neto" ? declarada / (1 - p.perdida) : declarada;
  const perdidaFisica = potencial * p.perdida;
  return {
    declarada, potencial, perdidaFisica,
    valorPerdida: perdidaFisica * p.precio,
    inversion: p.hardware + p.instalacion + p.capacitacion + p.capitalTrabajo,
    baseDepreciable: p.hardware + p.instalacion,
  };
}

function irr(flujos) {
  const npv = (r) => flujos.reduce((s, f, t) => s + f / (1 + r) ** t, 0);
  let lo = -0.9999, hi = 100;
  if (npv(lo) * npv(hi) > 0) return null;
  for (let i = 0; i < 300; i++) {
    const mid = (lo + hi) / 2;
    if (npv(lo) * npv(mid) <= 0) hi = mid; else lo = mid;
  }
  return (lo + hi) / 2;
}

export function escenario(p, eficacia) {
  const d = derivados(p);
  const filas = [];
  for (let n = 0; n <= 5; n++) {
    if (n === 0) {
      filas.push({ n, flujo: -d.inversion, descontado: -d.inversion });
      continue;
    }
    const activo = n <= p.horizonte ? 1 : 0;
    const rampa = (p.rampa[n - 1] ?? 1) * activo;
    const gramos = d.perdidaFisica * eficacia * rampa;
    const bruto = gramos * p.precio;
    const ingreso = bruto * p.realizacion;
    const contribucion = ingreso * p.margen;
    const opex = -(p.licencia + p.mantenimiento) * activo;
    const ebitda = contribucion + opex;
    const dep = n <= p.vidaUtil && activo ? -d.baseDepreciable / p.vidaUtil : 0;
    const impuesto = -p.impuesto * (ebitda + dep);
    const inv = n === p.anioReposicion && activo ? -p.reposicion : 0;
    const rec = n === p.horizonte ? p.capitalTrabajo + p.valorResidual : 0;
    const flujo = ebitda + impuesto + inv + rec;
    filas.push({ n, gramos, bruto, contribucion, opex, flujo, descontado: flujo / (1 + p.tasa) ** n });
  }
  const flujos = filas.map((f) => f.flujo);
  let acum = 0, payback = null;
  flujos.forEach((f, t) => { acum += f; if (payback === null && acum >= 0) payback = t; });
  const f0 = flujos[0];
  return {
    eficacia, filas,
    brutoRegimen: d.valorPerdida * eficacia,
    van: filas.reduce((s, f) => s + f.descontado, 0),
    tir: irr(flujos),
    payback,
    roi: f0 === 0 ? null : (flujos.slice(1).reduce((a, b) => a + b, 0) + f0) / -f0,
  };
}

export function modelo(p = DEFAULTS) {
  const errores = validar(p);
  if (errores.length) return { errores };
  const esc = Object.fromEntries(Object.entries(p.eficacias).map(([k, e]) => [k, escenario(p, e)]));
  // El VAN es lineal en la eficacia: umbral de equilibrio por interpolación exacta.
  const v0 = escenario(p, 0).van, v1 = escenario(p, 1).van;
  const umbral = v1 === v0 ? null : -v0 / (v1 - v0);
  return { errores: [], derivados: derivados(p), escenarios: esc, umbral, vanSinEficacia: v0 };
}
