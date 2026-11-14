"""Verifica que el Excel versionado coincide celda por celda con el que genera modelo/generar_modelo.py."""
import subprocess, sys, tempfile, shutil
from pathlib import Path

import openpyxl

raiz = Path(__file__).resolve().parent.parent
versionado = raiz / "modelo" / "PlantGuard_Pro_Modelo_ROI_v1.0.xlsx"
with tempfile.TemporaryDirectory() as tmp:
    copia = Path(tmp) / "generar_modelo.py"
    shutil.copy(raiz / "modelo" / "generar_modelo.py", copia)
    subprocess.run([sys.executable, "-I", str(copia)], check=True, capture_output=True)
    nuevo = openpyxl.load_workbook(Path(tmp) / versionado.name)
    viejo = openpyxl.load_workbook(versionado)
    difs = []
    if nuevo.sheetnames != viejo.sheetnames:
        difs.append(f"pestañas: {viejo.sheetnames} vs {nuevo.sheetnames}")
    for nombre in nuevo.sheetnames:
        a, b = viejo[nombre], nuevo[nombre]
        filas = max(a.max_row, b.max_row)
        cols = max(a.max_column, b.max_column)
        for r in range(1, filas + 1):
            for c in range(1, cols + 1):
                if a.cell(r, c).value != b.cell(r, c).value:
                    difs.append(f"{nombre}!{a.cell(r, c).coordinate}: {a.cell(r, c).value!r} vs {b.cell(r, c).value!r}")
if difs:
    print("El Excel versionado no coincide con el generador. Ejecuta: npm run modelo")
    print("\n".join(difs[:20]))
    sys.exit(1)
print("Excel OK: coincide con el generador")
