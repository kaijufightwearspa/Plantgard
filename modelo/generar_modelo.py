"""Genera PlantGuard_Pro_Modelo_ROI_v1.0.xlsx con las mismas fórmulas que la hoja
«PlantGuard Pro — Modelo ROI por cliente v1.0» (Claude Sheets, revisión 11, 14-11-2026).

Uso:  python3 modelo/generar_modelo.py
"""
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation

OUT = Path(__file__).with_name("PlantGuard_Pro_Modelo_ROI_v1.0.xlsx")

CHF = '"CHF" #,##0;-"CHF" #,##0'
CHF2 = '"CHF" #,##0.00'
PCT1 = "0.0%"
PCT0 = "0%"
NUM = "#,##0"
BOLD = Font(bold=True)
TITLE = Font(bold=True, size=14)
HEAD_FILL = PatternFill("solid", fgColor="DCEFE3")
SECTION_FILL = PatternFill("solid", fgColor="F1F5F2")

H = "Hipótesis ilustrativa"
NV = "No verificado"
C = "Calculado"


def entradas(ws):
    ws["A1"] = "PlantGuard Pro — Entradas del modelo ROI por cliente (uso interno)"
    ws["A1"].font = TITLE
    ws["A2"] = ("Valores precargados = caso ilustrativo del paquete maestro v2.0 [HIPÓTESIS ILUSTRATIVA]. "
                "Reemplazar por datos del cliente y cotizaciones reales. Solo editar la columna B.")
    rows = {
        4: ("Parámetro", "Valor", "Unidad", "Estado del dato", "Fuente / cómo obtenerlo"),
        5: ("1. DATOS DEL CLIENTE",),
        6: ("Cliente", "Ejemplo (reemplazar)", "—", H, "Razón social del cliente"),
        7: ("Cultivo y variedad", "—", "—", NV, "Ficha del cliente"),
        8: ("Superficie cultivada", 500, "m²", H, "Planos o registro de superficie productiva"),
        9: ("Rendimiento por ciclo", 400, "g/m²", H, "Registros de cosecha de los últimos 4 a 8 ciclos (PG-FIN-02)"),
        10: ("Base del rendimiento", "bruto", "bruto / neto", NV,
             "Bruto = potencial antes de pérdidas; neto = lo realmente cosechado. Los registros de cosecha suelen ser netos (PG-FIN-02)"),
        11: ("Ciclos por año", 4, "ciclos/año", H, "Calendario productivo del cliente"),
        12: ("Pérdida actual por variabilidad", 0.10, "% del rendimiento potencial", H,
             "Registros de merma y descarte por ciclo; definir por escrito qué cuenta como pérdida"),
        13: ("Precio neto realizable", 8, "CHF/g", NV,
             "Facturas recientes: precio después de descuentos, comisiones y flete (PG-FIN-03)"),
        14: ("Realización comercial", 0.85, "% de lo recuperado que se vende", H,
             "Capacidad de venta y calidad del producto adicional"),
        15: ("Margen de contribución incremental", 0.60, "% del ingreso", H,
             "(Precio − costo variable de cosecha, proceso, empaque y logística) / precio. Estos costos no se vuelven a restar como OPEX"),
        16: ("2. COSTOS DE PLANTGUARD (COTIZACIÓN)",),
        17: ("Hardware y sensores", 20000, "CHF, año 0", H, "Cotización formal (PG-FIN-04)"),
        18: ("Instalación e integración", 0, "CHF, año 0", H, "Cotización formal (PG-FIN-04)"),
        19: ("Capacitación y puesta en marcha", 0, "CHF, año 0", H, "Cotización; en este modelo no se deprecia"),
        20: ("Capital de trabajo inicial", 0, "CHF, año 0", H,
             "Insumos o inventario adicional; se recupera al final del horizonte"),
        21: ("Suscripción o licencia", 9000, "CHF/año", H, "Lista de precios PlantGuard (PG-FIN-04)"),
        22: ("Mantenimiento, datos y energía", 0, "CHF/año", H, "Cotización; excluir lo que ya está dentro del margen"),
        23: ("Reposición de equipos", 0, "CHF", H, "Vida útil de sensores según fabricante"),
        24: ("Año de reposición", 0, "año (0 = no aplica)", H, "Vida útil de sensores según fabricante"),
        25: ("Valor residual al final del horizonte", 0, "CHF", H, "Criterio conservador: 0"),
        26: ("3. PARÁMETROS FINANCIEROS",),
        27: ("Tasa de descuento", 0.12, "% anual, nominal, en CHF", H,
             "WACC o costo de oportunidad del cliente (PG-FIN-07). Flujos y tasa ambos nominales"),
        28: ("Horizonte de evaluación", 3, "años (1 a 5)", H, "Duración del contrato o vida útil del equipo"),
        29: ("Tasa de impuesto sobre utilidades", 0, "%", H,
             "0 % = antes de impuestos. Validar con especialista tributario local (PG-FIN-07)"),
        30: ("Vida útil para depreciación", 5, "años", H, "Normativa tributaria aplicable"),
        31: ("4. EFICACIA: % DE LA PÉRDIDA ACTUAL QUE SE EVITA (HIPÓTESIS HASTA EL PILOTO, PG-FIN-05)",),
        32: ("Escenario conservador", 0.05, "% de la pérdida actual", H, "Reemplazar por el resultado del piloto con grupo de control"),
        33: ("Escenario base", 0.20, "% de la pérdida actual", H, "Reemplazar por el resultado del piloto con grupo de control"),
        34: ("Escenario optimista", 0.50, "% de la pérdida actual", H, "Reemplazar por el resultado del piloto con grupo de control"),
        35: ("5. RAMPA DE ADOPCIÓN",),
        41: ("6. DERIVADOS (NO EDITAR)",),
        42: ("Producción declarada", "=B8*B9*B11", "g/año", C, "Superficie × rendimiento × ciclos"),
        43: ("Producción potencial antes de pérdidas", '=IF(B10="neto",B42/(1-B12),B42)', "g/año", C,
             "Si es neto: declarada / (1 − pérdida)"),
        44: ("Pérdida anual física", "=B43*B12", "g/año", C, "Potencial × pérdida"),
        45: ("Valor bruto de la pérdida actual", "=B44*B13", "CHF/año", C,
             "No es ahorro ni ROI: es lo que hoy se pierde a precio neto"),
        46: ("Inversión inicial total", "=SUM(B17:B20)", "CHF", C,
             "Hardware + instalación + capacitación + capital de trabajo"),
        47: ("Base depreciable", "=B17+B18", "CHF", C, "Hardware + instalación"),
        48: ("Validación de entradas",
             '=IF(OR(B12<0,B12>=1,B28<1,B28>5,B28<>INT(B28),B8<0,B9<0,B13<0,B14<0,B14>1,'
             'MIN(B32:B34)<0,MAX(B32:B34)>1,B32=B33,AND(B10<>"bruto",B10<>"neto")),"REVISAR ENTRADAS","OK")',
             "—", C, "Pérdida < 100 %, horizonte entero 1–5, eficacias entre 0 y 100 % y conservador ≠ base"),
    }
    for i, pct in zip(range(36, 41), (0.60, 0.85, 1.0, 1.0, 1.0)):
        rows[i] = (f"Año {i - 35}", pct, "% del efecto en régimen", H, "Curva de aprendizaje observada en el piloto")
    for r, vals in rows.items():
        for c, v in enumerate(vals, start=1):
            ws.cell(r, c, v)
        if len(vals) == 1:
            ws.cell(r, 1).font = BOLD
            for c in range(1, 6):
                ws.cell(r, c).fill = SECTION_FILL
    for c in range(1, 6):
        ws.cell(4, c).font = BOLD
        ws.cell(4, c).fill = HEAD_FILL
    for r in (12, 14, 15, 27, 29, 32, 33, 34, 36, 37, 38, 39, 40):
        ws.cell(r, 2).number_format = PCT1
    ws["B13"].number_format = CHF2
    for r in (17, 18, 19, 20, 21, 22, 23, 25, 45, 46, 47):
        ws.cell(r, 2).number_format = CHF
    for r in (42, 43, 44):
        ws.cell(r, 2).number_format = NUM
    estados = DataValidation(type="list", allow_blank=True,
                             formula1='"Verificado,Declarado por cliente,No verificado,Hipótesis ilustrativa,Calculado"')
    for rng in ("D6:D15", "D17:D25", "D27:D30", "D32:D34", "D36:D40", "D42:D48"):
        estados.add(rng)
    base = DataValidation(type="list", formula1='"bruto,neto"')
    base.add("B10")
    ws.add_data_validation(estados)
    ws.add_data_validation(base)
    ws.freeze_panes = "A5"
    for col, w in zip("ABCDE", (44, 22, 28, 22, 80)):
        ws.column_dimensions[col].width = w


def bloque_flujo(ws, top, nombre, efic):
    """Escribe un bloque de flujo de caja de 22 filas empezando en `top` (fila del título)."""
    E = "Entradas!"
    t = top
    ws.cell(t, 1, f'="Escenario {nombre}: se evita el "&ROUND({E}{efic}*100,1)&" % de la pérdida actual [HIPÓTESIS]"').font = BOLD
    hdr = t + 1
    for c, v in enumerate(["Concepto (CHF salvo indicación)"] + [f"Año {n}" for n in range(6)], start=1):
        ws.cell(hdr, c, v).font = BOLD
        ws.cell(hdr, c).fill = HEAD_FILL
    n, act, ramp, prod, bruto, ing, contr, opex, ebitda, dep, imp, inv, rec, flujo, acum, desc = range(hdr + 1, hdr + 17)
    labels = {
        n: "Año (n)", act: "Activo en el horizonte (1 = sí)", ramp: "Rampa de adopción",
        prod: "Producción recuperada (g)", bruto: "Valor bruto recuperado",
        ing: "Ingreso realizado (× realización)", contr: "Contribución incremental (× margen)",
        opex: "OPEX PlantGuard", ebitda: "EBITDA incremental", dep: "Depreciación (solo para impuesto)",
        imp: "Impuesto", inv: "Inversión y reposición",
        rec: "Recuperación capital de trabajo + valor residual", flujo: "FLUJO DE CAJA NETO",
        acum: "Flujo acumulado", desc: "Flujo descontado",
    }
    for r, lab in labels.items():
        ws.cell(r, 1, lab)
    ws.cell(flujo, 1).font = BOLD
    for i, col in enumerate("BCDEFG"):
        ws[f"{col}{n}"] = i
    ws[f"B{inv}"] = f"=-{E}$B$46"
    ws[f"B{flujo}"] = f"=B{inv}"
    ws[f"B{acum}"] = f"=B{flujo}"
    ws[f"B{desc}"] = f"=B{flujo}/(1+{E}$B$27)^B{n}"
    prev = "B"
    for col in "CDEFG":
        f = {
            act: f"=IF({col}{n}<={E}$B$28,1,0)",
            ramp: f"=INDEX({E}$B$36:$B$40,{col}{n})*{col}{act}",
            prod: f"={E}$B$44*{E}${efic[0]}${efic[1:]}*{col}{ramp}",
            bruto: f"={col}{prod}*{E}$B$13",
            ing: f"={col}{bruto}*{E}$B$14",
            contr: f"={col}{ing}*{E}$B$15",
            opex: f"=-({E}$B$21+{E}$B$22)*{col}{act}",
            ebitda: f"={col}{contr}+{col}{opex}",
            dep: f"=IF(AND({col}{n}<={E}$B$30,{col}{act}=1),-{E}$B$47/{E}$B$30,0)",
            imp: f"=-{E}$B$29*({col}{ebitda}+{col}{dep})",
            inv: f"=IF(AND({col}{n}={E}$B$24,{col}{act}=1),-{E}$B$23,0)",
            rec: f"=IF({col}{n}={E}$B$28,{E}$B$20+{E}$B$25,0)",
            flujo: f"={col}{ebitda}+{col}{imp}+{col}{inv}+{col}{rec}",
            acum: f"={prev}{acum}+{col}{flujo}",
            desc: f"={col}{flujo}/(1+{E}$B$27)^{col}{n}",
        }
        for r, formula in f.items():
            ws[f"{col}{r}"] = formula
        prev = col
    for r in range(prod, desc + 1):
        for col in "BCDEFG":
            ws[f"{col}{r}"].number_format = NUM
    for col in "CDEFG":
        ws[f"{col}{ramp}"].number_format = PCT0
    van, tir, pb, roi = desc + 1, desc + 2, desc + 3, desc + 4
    ws.cell(van, 1, "VAN").font = BOLD
    ws[f"B{van}"] = f"=SUM(B{desc}:G{desc})"
    ws[f"B{van}"].number_format = NUM
    ws.cell(tir, 1, "TIR")
    ws[f"B{tir}"] = f'=IFERROR(IRR(B{flujo}:G{flujo}),"No calculable")'
    ws[f"B{tir}"].number_format = PCT1
    ws.cell(pb, 1, "Payback (año en que el acumulado llega a ≥ 0)")
    # Excel clásico no tiene XMATCH; MATCH sobre una matriz booleana es equivalente.
    ws[f"B{pb}"] = f'=IFERROR(MATCH(TRUE,INDEX(B{acum}:G{acum}>=0,0),0)-1,"No recupera en el horizonte")'
    ws.cell(roi, 1, "ROI simple acumulado")
    ws[f"B{roi}"] = f'=IF(B{flujo}=0,"n/a",(SUM(C{flujo}:G{flujo})+B{flujo})/-B{flujo})'
    ws[f"B{roi}"].number_format = PCT1
    return van, tir, pb, roi


def flujos(ws):
    ws["A1"] = "PlantGuard Pro — Flujo de caja incremental por escenario (calculado, no editar)"
    ws["A1"].font = TITLE
    ws["A2"] = ("Solo flujos incrementales vs. el escenario sin PlantGuard. El margen ya incluye costos variables: "
                "no se restan de nuevo como OPEX. Años fuera del horizonte = 0.")
    out = {}
    for top, nombre, efic in ((4, "conservador", "B32"), (28, "base", "B33"), (52, "optimista", "B34")):
        out[nombre] = bloque_flujo(ws, top, nombre, efic)
    ws.freeze_panes = "B1"
    ws.column_dimensions["A"].width = 48
    for col in "BCDEFG":
        ws.column_dimensions[col].width = 14
    return out


def resultados(ws, refs):
    ws["A1"] = "PlantGuard Pro — ROI por cliente: resumen"
    ws["A1"].font = TITLE
    ws["A2"] = ("Uso interno. No es oferta ni garantía de resultados. Mientras no se cierren PG-FIN-01 a 05, "
                "no hay evidencia para un dictamen favorable.")
    ws["A3"] = '="Cliente: "&Entradas!B6&"  |  Estado de las entradas: "&Entradas!B48'
    for c, v in enumerate(("Indicador", "Conservador", "Base", "Optimista"), start=1):
        ws.cell(5, c, v).font = BOLD
        ws.cell(5, c).fill = HEAD_FILL
    cols = (("B", "B32", "conservador"), ("C", "B33", "base"), ("D", "B34", "optimista"))
    labels = {
        6: "Pérdida actual que se evita [HIPÓTESIS]",
        7: "Valor bruto de la pérdida actual (CHF/año)",
        8: "Valor bruto recuperado en régimen (CHF/año)",
        9: "Contribución incremental en régimen (CHF/año)",
        10: "OPEX PlantGuard (CHF/año)",
        11: "Inversión inicial (CHF)",
        12: "VAN (CHF)", 13: "TIR", 14: "Payback (año)", 15: "ROI simple acumulado",
    }
    for r, lab in labels.items():
        ws.cell(r, 1, lab)
    for col, efic, nombre in cols:
        van, tir, pb, roi = refs[nombre]
        ws[f"{col}6"] = f"=Entradas!{efic}"
        ws[f"{col}7"] = "=Entradas!B45"
        ws[f"{col}8"] = f"={col}7*{col}6"
        ws[f"{col}9"] = f"={col}8*Entradas!$B$14*Entradas!$B$15"
        ws[f"{col}10"] = "=-(Entradas!$B$21+Entradas!$B$22)"
        ws[f"{col}11"] = "=-Entradas!$B$46"
        ws[f"{col}12"] = f"=Flujos!B{van}"
        ws[f"{col}13"] = f"=Flujos!B{tir}"
        ws[f"{col}14"] = f"=Flujos!B{pb}"
        ws[f"{col}15"] = f"=Flujos!B{roi}"
        ws[f"{col}6"].number_format = PCT1
        for r in range(7, 13):
            ws[f"{col}{r}"].number_format = CHF
        ws[f"{col}13"].number_format = PCT1
        ws[f"{col}15"].number_format = PCT1
    ws["A17"] = "Umbral de equilibrio"
    ws["A17"].font = BOLD
    ws["A18"] = "% de la pérdida actual que PlantGuard debe evitar para que VAN = 0"
    ws["B18"] = '=IFERROR(Entradas!B32-Flujos!B22*(Entradas!B33-Entradas!B32)/(Flujos!B46-Flujos!B22),"n/a")'
    ws["B18"].number_format = PCT1
    ws["A19"] = "Lectura"
    ws["B19"] = ('=IF(ISNUMBER(B18),IF(B18>1,"Ni evitando el 100 % de la pérdida se recupera la inversión",'
                 'IF(B18<=0,"VAN positivo incluso sin eficacia: revisar entradas",'
                 '"El piloto debe demostrar al menos este % para crear valor")),"Revisar entradas")')
    ws["A20"] = "VAN con eficacia 0 % (solo costos, CHF)"
    ws["B20"] = '=IFERROR(Flujos!B22-Entradas!B32*(Flujos!B46-Flujos!B22)/(Entradas!B33-Entradas!B32),"n/a")'
    ws["B20"].number_format = CHF
    ws["A21"] = "VAN adicional por cada punto porcentual de eficacia (CHF)"
    ws["B21"] = '=IFERROR((Flujos!B46-Flujos!B22)/(Entradas!B33-Entradas!B32)/100,"n/a")'
    ws["B21"].number_format = CHF
    ws["A23"] = "Notas"
    ws["A23"].font = BOLD
    notas = [
        "1. «Eficacia» = % de la pérdida actual que se evita (no puntos porcentuales). Ver PG-FIN-01.",
        "2. El valor bruto no es ROI: el ROI exige restar margen, OPEX e inversión y descontar en el tiempo.",
        "3. El umbral supone VAN lineal en la eficacia, válido con este modelo (sin límite de capacidad de venta).",
        "4. Impuesto aplicado como si el cliente tuviera otras utilidades (las pérdidas generan ahorro tributario). "
        "Validar con especialista local (PG-FIN-07).",
        "5. Metodología: VAN de flujos incrementales (Ross-Westerfield-Jordan; Berk-DeMarzo); margen de contribución "
        "(Contabilidad Administrativa).",
    ]
    for i, nota in enumerate(notas, start=24):
        ws.cell(i, 1, nota)
    ws.column_dimensions["A"].width = 62
    for col in "BCD":
        ws.column_dimensions[col].width = 26


def sensibilidad(ws):
    ws["A1"] = "VAN (CHF) según eficacia y margen de contribución"
    ws["A1"].font = BOLD
    efic = (0.05, 0.10, 0.20, 0.30, 0.50)
    ws["A2"] = "Pérdida evitada \\ Margen"
    for col, m in zip("BCD", (0.4, 0.6, 0.8)):
        ws[f"{col}2"] = m
        ws[f"{col}2"].number_format = PCT0
    for i, e in enumerate(efic, start=3):
        ws[f"A{i}"] = e
        ws[f"A{i}"].number_format = PCT0
        for col in "BCD":
            ws[f"{col}{i}"] = f"=Resultados!$B$20+$A{i}*Resultados!$B$21*100*{col}$2/Entradas!$B$15"
            ws[f"{col}{i}"].number_format = NUM
    ws["A9"] = "VAN (CHF) según eficacia y precio neto (% del precio ingresado)"
    ws["A9"].font = BOLD
    ws["A10"] = "Pérdida evitada \\ Precio"
    for col, p in zip("BCD", (0.7, 1.0, 1.3)):
        ws[f"{col}10"] = p
        ws[f"{col}10"].number_format = PCT0
    for i, e in enumerate(efic, start=11):
        ws[f"A{i}"] = e
        ws[f"A{i}"].number_format = PCT0
        for col in "BCD":
            ws[f"{col}{i}"] = f"=Resultados!$B$20+$A{i}*Resultados!$B$21*100*{col}$10"
            ws[f"{col}{i}"].number_format = NUM
    ws["A17"] = ("Supuesto: el VAN es lineal en la eficacia, el margen y el precio (sin límite de capacidad de venta). "
                 "Los márgenes de 40/60/80 % y precios de 70/100/130 % son rangos de prueba, no datos del cliente.")
    ws.column_dimensions["A"].width = 30
    for col in "BCD":
        ws.column_dimensions[col].width = 14


def guia(ws):
    filas = [
        ("#", "Dato que se pide al cliente", "Para qué sirve en el modelo", "Documento de respaldo", "Control"),
        (1, "Superficie productiva (m²) por cultivo", "Escala de producción", "Planos, registro de superficie", "PG-FIN-02"),
        (2, "Rendimiento por ciclo (g/m²) de los últimos 4–8 ciclos", "Base de producción", "Registros de cosecha", "PG-FIN-02"),
        (3, "¿El rendimiento es antes o después de pérdidas?", "Evita subestimar o duplicar la pérdida", "Metodología de medición", "PG-FIN-02"),
        (4, "Ciclos por año", "Producción anual", "Calendario productivo", "—"),
        (5, "Pérdida por variabilidad (% del potencial) y cómo se mide", "Tamaño del problema que ataca PlantGuard",
         "Registros de merma, descarte y reclamos", "PG-FIN-01"),
        (6, "Precio neto realizado (CHF/g) tras descuentos, comisiones y flete", "Valorización del volumen recuperado",
         "Facturas de los últimos 6–12 meses", "PG-FIN-03"),
        (7, "¿Puede vender más volumen? ¿Con qué calidad?", "Factor de realización comercial",
         "Contratos, cupos, rechazos de calidad", "PG-FIN-03"),
        (8, "Costo variable por gramo adicional (cosecha, proceso, empaque, logística)", "Margen de contribución incremental",
         "Estado de costos o centro de costos", "PG-FIN-04"),
        (9, "Tasa de descuento o costo de capital", "VAN y comparación con otras inversiones", "Política financiera del cliente", "PG-FIN-07"),
        (10, "Tasa de impuesto y vida útil tributaria", "Flujo después de impuestos", "Asesor tributario local", "PG-FIN-07"),
        (11, "Horizonte de decisión (años)", "Periodo de evaluación", "Plazo del contrato o vida útil", "PG-FIN-04"),
        (12, "Cotización PlantGuard: hardware, instalación, capacitación", "Inversión inicial", "Cotización formal firmada", "PG-FIN-04"),
        (13, "Cotización PlantGuard: suscripción, mantenimiento, datos, energía", "OPEX anual", "Cotización formal firmada", "PG-FIN-04"),
        (14, "Eficacia: % de la pérdida que se evita", "Escenarios conservador, base y optimista", "Piloto con grupo de control", "PG-FIN-05"),
    ]
    for r, fila in enumerate(filas, start=1):
        for c, v in enumerate(fila, start=1):
            ws.cell(r, c, v)
    for c in range(1, 6):
        ws.cell(1, c).font = BOLD
        ws.cell(1, c).fill = HEAD_FILL
    for col, w in zip("ABCDE", (5, 62, 42, 40, 12)):
        ws.column_dimensions[col].width = w


def main():
    wb = Workbook()
    ws_res = wb.active
    ws_res.title = "Resultados"
    ws_ent = wb.create_sheet("Entradas")
    ws_flu = wb.create_sheet("Flujos")
    ws_sen = wb.create_sheet("Sensibilidad")
    ws_gui = wb.create_sheet("Guía de datos")
    entradas(ws_ent)
    refs = flujos(ws_flu)
    assert refs["conservador"][0] == 22 and refs["base"][0] == 46 and refs["optimista"][0] == 70
    resultados(ws_res, refs)
    sensibilidad(ws_sen)
    guia(ws_gui)
    wb.save(OUT)
    print(f"Generado: {OUT}")


if __name__ == "__main__":
    main()
