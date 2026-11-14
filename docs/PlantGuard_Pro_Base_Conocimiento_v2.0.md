# PLANTGUARD PRO — BASE MAESTRA DE CONOCIMIENTO PARA CLAUDE

Proyecto de destino: FINANZAS Y CONTABILIDAD  
Subproyecto/expediente: PlantGuard Pro — evaluación económica y auditoría ROI  
Versión: 2.0 \| Fecha de consolidación: 14 de noviembre de 2026  
Idioma: Español (Chile) \| Moneda base: CHF \| Estado: PREFACTIBILIDAD CONDICIONADA

\===============================================================================

# 0\. PROPÓSITO E INSTRUCCIONES DE INTEGRACIÓN CON EL PROYECTO DE CLAUDE

\===============================================================================

Este archivo es una base documental autosuficiente destinada a incorporarse como  
conocimiento persistente del proyecto «Finanzas y Contabilidad» en Claude.  
Agrupa la calculadora original de PlantGuard Pro, el estudio financiero  
integral del 13-11-2026, un modelo numérico reproducible, una matriz de  
correspondencias con bibliografía alojada en Google Drive y un plan de  
validación empresarial.

REGLAS DE INCORPORACIÓN:  
\- Considerar este archivo como una FUENTE DE CONTEXTO DEL CASO, no como una  
  fuente que automáticamente sustituya la bibliografía contable, financiera  
  o las instrucciones existentes en Claude.  
\- Mantener PlantGuard Pro separado de otros negocios/proyectos (por ejemplo,  
  KAIJU); compartir criterios metodológicos, NO combinar presupuestos,  
  balances, cifras, cuentas o operaciones de entidades distintas.  
\- Nunca interpretar «ROI de la landing» como retorno sobre la inversión; es  
  un valor bruto potencial de producción recuperable.  
\- Etiquetar cada dato: \[DECLARADO POR FUENTE\], \[DERIVADO/CALCULADO\],  
  \[HIPÓTESIS ILUSTRATIVA\], \[NO VERIFICADO\] o \[EVIDENCIA DE GOOGLE DRIVE\].  
\- Si una conversación de Claude aporta nuevos datos comerciales, técnicos,  
  contables o de costos, NO cambiar silenciosamente esta línea base: crear  
  versión nueva, registrar fuente, fecha, responsable y efecto numérico.  
\- Ante contradicciones, dar prioridad a documentación original verificada,  
  datos transaccionales y ensayos de campo frente a estimaciones comerciales.  
\- Los enlaces a Drive constituyen REFERENCIAS DE PROCEDENCIA: no implican que  
  Claude tenga permiso de lectura o sincronización automática. Consultarlos  
  solo si hay acceso disponible y verificar la versión antes de citarlos.  
\- Si se solicita una decisión de inversión, advertir que no está disponible  
  todavía evidencia suficiente para pronunciarse favorablemente.  
\- Responder de preferencia como asesor financiero-contable de nivel directivo,  
  con cálculos auditables, trazabilidad, análisis de sensibilidad y medidas  
  concretas de control de gestión.

Esta versión fue elaborada con la información ya disponible en el expediente;  
NO se tuvo acceso directo al repositorio de código de PlantGuard y NO se  
registraron pruebas de campo del producto.

\===============================================================================

# 1\. RESUMEN EJECUTIVO Y DICTAMEN

\===============================================================================

PlantGuard Pro presenta en su landing un simulador que muestra el «valor  
anual estimado recuperado» en CHF. Los seis inputs actuales y su fórmula  
producen CHF 32.000/año para los valores predeterminados. Ese valor no es  
«ROI financiero»: no descuenta inversión de capital, gastos operacionales,  
costos variables, impuestos ni valor del dinero en el tiempo.

CONCLUSIÓN TÉCNICA CENTRAL:  
La operación aritmética es correcta si «mejora 5 %» significa «evitar el 5 %  
de la pérdida que originalmente se habría producido». En ese caso se evita  
0,5 % del valor bruto potencial de la producción (10 % de merma × 5 % de  
recuperación de dicha merma). Si «mejora 5 %» significa una caída de la tasa  
de merma del 10 % al 5 % —una reducción de cinco puntos porcentuales (pp)—,  
el monto bruto sería CHF 320.000/año, DIEZ VECES el valor mostrado por la  
landing. La diferencia es de interpretación del parámetro, no de álgebra.

ESTADO DE DECISIÓN: Prefactibilidad condicionada.  
DECISIÓN RECOMENDADA: Normalizar la semántica de las variables y validar  
beneficios, ventas adicionales realizables y CAPEX/OPEX antes de publicar  
cualquier promesa de rentabilidad o aprobar una inversión.

\===============================================================================

# 2\. TRAZABILIDAD DE LA CALCULADORA ORIGINAL

\===============================================================================

\[DECLARADO POR FUENTE\] Archivo: «calculadora-roi-plantguard.txt», recibido  
13-11-2026, y copia de fuente:  
«PlantGuard\_Pro\_Fuente\_Calculadora\_13NOV2026.txt».  
Ubicación de código atribuida por el documento aportado:  
  landing/index.html  \| sección \#roi \| función calc()  
Estado de verificación: NO se inspeccionó el repositorio original.

ID        DEFINICIÓN EN LA LANDING                         VALOR BASE    UNIDAD  
area      Superficie de cultivo                            500           m²  
gm2       Rendimiento actual                                400           g/m²  
precio    Valor referencial por gramo                       8             CHF/g  
perdida   Pérdida por variabilidad                         10            %  
mejora    Mejora estimada atribuida al control               5            %  
ciclos    Ciclos anuales de cultivo                          4            ciclos/año

Pseudocódigo atribuido al sitio web:

  gramosCiclo \= area \* gm2  
  valorCiclo  \= gramosCiclo \* precio  
  recuperado  \= valorCiclo \* (perdida/100) \* (mejora/100) \* ciclos

Salida única visible de acuerdo con la transcripción:  
  «Valor anual estimado recuperado».

CÁLCULO PASO A PASO \[DERIVADO/CALCULADO\]:  
\- Por ciclo: 500 m² × 400 g/m² \= 200.000 g/ciclo.  
\- Valor de un ciclo: 200.000 g × CHF 8/g \= CHF 1.600.000.  
\- Producción anual de referencia: 200.000 × 4 \= 800.000 g/año.  
\- Valor anual de referencia: CHF 1.600.000 × 4 \= CHF 6.400.000.  
\- Merma anual teórica al 10 % de la producción potencial: 80.000 g;  
  equivalentes a CHF 640.000.  
\- Recuperación de 5 % de ESA merma: 4.000 g/año, CHF 32.000/año.  
\- «Mejora» así entendida: la tasa de merma pasa de 10,0 % a 9,5 %  
  (reducción de 0,5 puntos porcentuales).

ALERTA: «pérdida × mejora» es una composición de porcentajes con distintos  
denominadores; NO hay base para afirmar que representa probabilidades  
independientes en sentido estadístico.

\===============================================================================

# 3\. TRES INTERPRETACIONES DE «MEJORA» Y SU IMPLICANCIA

\===============================================================================

Definir V \= valor bruto anual de producción potencial (CHF 6.400.000);  
L \= fracción de merma original (0,10).

ESCENARIO A — FRACCIÓN DE LA PÉRDIDA EVITADA \[BASE DEL SITIO\]:  
  R \= 5 % de la pérdida original; recuperación \= V × L × R.  
  6.400.000 × 0,10 × 0,05 \= CHF 32.000/año.  
  Volumen recuperado: 4.000 g/año.

ESCENARIO B — REDUCCIÓN EN PUNTOS PORCENTUALES:  
  D \= 5 pp \= 0,05 del valor potencial; 10 % \-\> 5 % de merma.  
  recuperación \= V × min(L, D).  
  6.400.000 × 0,05 \= CHF 320.000/año.  
  Volumen recuperado: 40.000 g/año.  
  NOTA: equivale a recuperar 50 % de las pérdidas originalmente esperadas.

ESCENARIO C — CRECIMIENTO RELATIVO DEL RENDIMIENTO NETO:  
  Si 800.000 g/año se define como producción NETA ya cosechada/vendida,  
  crecer 5 % respecto de esa base implicaría 40.000 g/año y CHF 320.000/año  
  de valor bruto adicional, si no hay restricciones de venta y se realiza  
  el mismo precio marginal. Este supuesto NO puede añadirse a A ni a B;  
  representa otra interpretación de la base productiva.

La interfaz del producto debe escoger UN significado operativo. No sumar  
alternativas ni usar las tres de forma intercambiable.

\===============================================================================

# 4\. RENDIMIENTO BRUTO VS RENDIMIENTO NETO

\===============================================================================

\[INCERTIDUMBRE CRÍTICA\] La etiqueta «rendimiento actual (g/m²)» no indica si  
400 g/m² corresponde a rendimiento potencial antes de merma (bruto) o a  
rendimiento realmente alcanzado después de merma (neto).

SI 400 g/m² ES BRUTO: usar V\_bruto \= área × rendimiento × ciclos × precio.  
\- Producción y valor bruto anual: 800.000 g y CHF 6.400.000.  
\- Pérdida teórica al 10 %: CHF 640.000.  
\- Recuperación de 5 % de la merma: CHF 32.000.  
\- Baja de 5 pp de merma: CHF 320.000.

SI 400 g/m² ES NETO, CON MERMA ORIGINAL DEL 10 % SOBRE POTENCIAL:  
  V\_potencial \= V\_neto / (1 − L)  
\- Valor anual neto observado base: CHF 6.400.000.  
\- Valor potencial estimado: CHF 7.111.111,11.  
\- Pérdida estimada: CHF 711.111,11.  
\- Recuperación de 5 % de esa pérdida: CHF 35.555,56.  
\- Baja de 5 pp sobre base potencial: CHF 355.555,56.

Son dos MARCOS ALTERNATIVOS. Su combinación duplicaría efectos y falsearía  
la evaluación. Confirmar el denominador con operaciones y agronomía.

\===============================================================================

# 5\. PUENTE DESDE VALOR BRUTO HASTA FLUJO DE CAJA Y VAN

\===============================================================================

La variable «recuperado» mide, como máximo, PRODUCCIÓN ADICIONAL VALORADA  
A UN PRECIO REFERENCIAL. No equivale necesariamente a ventas realizadas,  
ahorros contables, EBITDA, utilidad, flujo de caja o ROI.

Secuencia económica de análisis:  
1\) Volumen adicional atribuible: pérdida física evitada y validada (g).  
2\) Valor bruto potencial: gramos recuperados × precio marginal realizable.  
3\) Realización comercial: descontar unidades no vendibles, rechazo comercial,  
   calidad, capacidad o restricciones de comercialización.  
4\) Contribución incremental: valor realizable × margen de contribución  
   incremental; verificar costo variable directo de cosecha, procesamiento,  
   acondicionamiento, logística, comisiones, impuestos específicos cuando  
   corresponda, etc., sin doble contabilización.  
5\) OPEX incremental PlantGuard: licencias, soporte, datos, mantenimiento,  
   insumos, energía, personal y renovaciones si NO fueron incorporados  
   previamente al margen de contribución.  
6\) CAPEX incremental: adquisición, instalación, integración, puesta en  
   marcha y capital de trabajo inicial pertinente.  
7\) Flujo de caja incremental por año y período cero.  
8\) Evaluación: VAN/NPV, TIR/IRR cuando sea matemática y económicamente  
   interpretable, payback, ROI nominal simple, sensibilidad y riesgo.

FÓRMULAS DE EVALUACIÓN (SIMPLIFICADAS; antes de impuesto):  
  B \= volumen\_recuperado\_g × precio\_marginal\_efectivo\_CHF\_g  
  C \= B × porcentaje\_realización × margen\_contribución\_incremental  
  Flujo\_t \= C × factor\_adopción\_t − OPEX\_incremental\_t − CAPEX\_adicional\_t  
  VAN \= − CAPEX\_0 \+ sumatorio(Flujo\_t / (1 \+ tasa\_descuento)^t)  
  ROI\_simple \= (sumatorio(Flujo\_neto\_t) − CAPEX\_0) / CAPEX\_0

En el ROI, «Flujo\_neto\_t» de los años 1...N NO incluye otra vez CAPEX\_0.  
El modelo financiero base tiene horizonte de tres años y CAPEX solo en t=0.

Precaución técnica: si el margen incluye un costo, ese mismo concepto no  
puede volver a deducirse como OPEX. La tasa de descuento y los flujos deben  
ser consistentes (ambos nominales o reales; misma moneda, horizonte e  
impuestos). Se debe validar depreciación, impuestos, capital de trabajo,  
reposición de activos, variación de precios y valor residual antes de un  
caso formal de inversión. No atribuir a PlantGuard mejoras causadas por  
factores externos, cambios varietales, clima u otros controles.

\===============================================================================

# 6\. CASO ILUSTRATIVO DE PREFACTIBILIDAD — MODELO BASE

\===============================================================================

IMPORTANTE: CAPEX, OPEX, margen, factor de venta, tasa y rampa SON  
HIPÓTESIS ILUSTRATIVAS, no cifras de cotizaciones, contratos ni auditoría.

PARÁMETRO                                                       VALOR  
Área                                                              500 m²  
Rendimiento referencial bruto                                      400 g/m²  
Precio referencial                                                CHF 8/g  
Pérdidas base                                                     10 %  
Fracción de pérdida evitada                                         5 %  
Ciclos por año                                                      4  
Margen de contribución incremental                                 60 %  
Factor de realización comercial                                    85 %  
CAPEX inicial                                                      CHF 20.000  
OPEX incremental anual                                             CHF 9.000  
Tasa de descuento                                                  12 %/año  
Horizonte                                                          3 años  
Rampa año 1 / año 2 / año 3                                        60 % / 85 % / 100 %

DERIVACIONES \[DERIVADO/CALCULADO\]:  
\- Producción adicional valorada: CHF 32.000/año (bruta, régimen).  
\- Contribución incremental antes de ramp-up: 32.000 × 60 % × 85 %  
  \= CHF 16.320/año.  
\- Contribución neta de OPEX en régimen: 16.320 − 9.000  
  \= CHF 7.320/año.

FLUJO NOMINAL ILUSTRATIVO:  
Año    Contribución realizada    OPEX       CAPEX        Flujo neto  
0      —                         —          (20.000)     (20.000) CHF  
1      9.792                     (9.000)    —               792 CHF  
2      13.872                    (9.000)    —             4.872 CHF  
3      16.320                    (9.000)    —             7.320 CHF

RESULTADOS \[DERIVADO/CALCULADO\]:  
\- VAN de tres años a 12 %: CHF −10.198,70 ≈ CHF −10.199.  
\- ROI nominal simple acumulado: −35,08 %.  
\- No recupera la inversión inicial dentro de los tres años.  
\- Fracción mínima de pérdidas base que debe evitarse para VAN \= 0,  
  con TODAS las demás hipótesis invariantes: 6,6231 % de esas pérdidas.

Conclusión: con esos supuestos de EJEMPLO, el proyecto no crea valor. Esto  
NO equivale a afirmar que PlantGuard Pro, como producto real, tenga ROI  
negativo o que sus beneficios agronómicos sean insuficientes.

\===============================================================================

# 7\. ANÁLISIS DE ESCENARIOS Y PRUEBAS DE SENSIBILIDAD

\===============================================================================

Misma base productiva, calendario y supuestos financieros ilustrativos:

Escenario          Pérdidas originales evitadas   Valor bruto anual   VAN 3 años  
Conservador         5 %                          CHF 32.000         CHF −10.199  
Intermedio         20 %                          CHF 128.000        CHF 84.055  
Alto               50 %                          CHF 320.000        CHF 272.561

Los escenarios de 20 % y 50 % NO son eficacias verificadas del producto.  
Sirven para medir la sensibilidad del caso y establecer umbrales de  
viabilidad económica, NO para emitir pronósticos comerciales.

Matriz de sensibilidad recomendada:  
\- Fracción de pérdidas evitadas: 5, 10, 20, 30 y 50 %.  
\- Margen incremental: 40, 60 y 80 %.  
\- Precio marginal y tasa de merma: rangos realistas medidos.  
\- Variaciones adicionales: factor vendible, CAPEX, OPEX, horizonte, rampa,  
  descuento y disponibilidad operativa.  
\- Analizar escenarios en paralelo y nunca promediarlos sin una metodología  
  de probabilidades respaldada por evidencia.

\===============================================================================

# 8\. CRUCE CON BIBLIOGRAFÍA Y FUENTES DE GOOGLE DRIVE

\===============================================================================

Se identificaron y consultaron en la carpeta financiera de Google Drive  
los siguientes textos. Se registran los ENFOQUES METODOLÓGICOS derivados de  
las obras, no cifras nuevas de PlantGuard. Enlaces permanentes observados  
por la búsqueda del Drive asociado al usuario, sujetos a los permisos de  
acceso de cada cuenta.

GDR-01 \| FUNDAMENTOS DE FINANZAS CORPORATIVAS — Ross, Westerfield y Jordan  
URL: https\://drive.google.com/file/d/16bA6lbJdJLfhTIuvbgjO631huKNFOXbI/view  
Tema verificado en el texto: presupuestación de capital; VPN/VAN; flujos de  
caja incrementales; tratamiento de costos hundidos.  
CRUCE: requerir VAN de flujos atribuibles a PlantGuard, no confundir venta  
potencial con valor presente; evaluar solo costos y beneficios que cambian  
respecto del contrafactual sin PlantGuard.  
APLICACIÓN: secciones 5-7, matriz de aprobación PG-FIN-04/05.

GDR-02 \| FINANZAS CORPORATIVAS — Berk y DeMarzo  
URL: https\://drive.google.com/file/d/1BoTBVbii-3C88DtrMOZGBs2PM6I\_rEJ7/view  
Temas verificados: reglas de inversión, valor presente neto, presupuestación  
de capital, utilidades incrementales y costos hundidos; capítulos 3, 6 y 7  
según índice revisado.  
CRUCE: separar beneficio incremental real de inversiones irrecuperables  
anteriores; elaborar calendario de flujos de caja y tasa de oportunidad.  
APLICACIÓN: definición de flujo, VAN y decisión costo-beneficio.

GDR-03 \| CONTABILIDAD ADMINISTRATIVA: UN ENFOQUE GERENCIAL DE COSTOS  
URL: https\://drive.google.com/file/d/1ycERqRC9SUDYZFxUyA6mthTKikjvClYs/view  
Temas verificados: costos relevantes, fijos y variables, margen de  
contribución y análisis costo-volumen-utilidad/punto de equilibrio.  
CRUCE: medir contribución de producción adicional vendida y gastos  
incrementales, NO considerar todo CHF 8/g como margen de utilidad.  
APLICACIÓN: registro de costos, márgenes y break-even del proyecto.

GDR-04 \| PRESUPUESTOS EMPRESARIALES  
URL: https\://drive.google.com/file/d/1ghLquhejrf1ZiAe2HoGNDwQ1vFR2CF2g/view  
Tema verificado: cédulas de presupuesto de efectivo y presupuestación  
empresarial.  
CRUCE: consolidar CAPEX, OPEX, ramp-up, venta realizable y calendario de  
flujo de caja del proyecto con control de desvíos por período.  
APLICACIÓN: presupuesto de implantación y control mensual/trimestral.

GDR-05 \| MANUAL DE COSTOS Y PRESUPUESTOS  
URL: https\://drive.google.com/file/d/1yDruhNto5QctvmMZSAOm3UQC8DHFwmJw/view  
Temas verificados: costeo directo, margen de contribución, presupuesto de  
inversiones y presupuesto de caja.  
CRUCE: desagregar costos directos/indirectos y distinguir presupuesto de  
inversión inicial del presupuesto recurrente.  
APLICACIÓN: costo total de propiedad (TCO), punto de equilibrio y controles.

OTRAS REFERENCIAS COMPLEMENTARIAS IDENTIFICADAS EN DRIVE:  
GDR-06 \| COSTOS DE PRODUCCIÓN — Fabiola A. Pacheco Bautista  
https\://drive.google.com/file/d/1DqUZ0Aq\_j3pRDukCGjmNESqJzBv-6i9P/view  
Contexto contrastado: costos directos/indirectos; costo unitario; punto de  
equilibrio. Ayuda a definir costo incremental de cosecha/procesamiento.

GDR-07 \| CARPETA DE FUENTES FINANCIERAS DE GOOGLE DRIVE  
https\://drive.google.com/drive/folders/1kjtE7GvD9X2SLPW8oNYOGPsq-l52HF7d  
Carpeta identificada: «05\_Finanzas»; contiene la bibliografía anterior y  
textos adicionales de costos, finanzas y presupuestos. IMPORTANTE: aparece  
dentro de la biblioteca de otro proyecto empresarial; se utiliza SOLO como  
referencia académica transversal. NO se importan datos de negocios ajenos.

ALCANCE DEL CRUCE: se verificaron los temas metodológicos citados mediante  
lectura de documentos en Google Drive; NO se encontró dentro del Drive un  
archivo técnico de PlantGuard ni respaldo de precios, ensayos, contratos o  
presupuestos reales del producto. Ninguna fuente académica valida por sí sola  
que PlantGuard reduzca las pérdidas en 5 %, 20 % o 50 %.

\===============================================================================

# 9\. MATRIZ DE APLICACIÓN DE CONOCIMIENTO A PLANTGUARD

\===============================================================================

EJE                         CRITERIO / FUENTE     ESTADO Y BRECHA  
Valuación de inversiones     GDR-01, GDR-02        VAN ilustrativo; falta WACC o tasa validada.  
Contabilidad gerencial       GDR-03, GDR-05        Margen 60 % supuesto; falta costeo real.  
Costeo y punto de equilibrio GDR-03, GDR-06        Umbral 6,62 % ilustrativo; falta medir.  
Presupuesto de caja          GDR-04, GDR-05        CAPEX/OPEX ejemplo; falta proforma y TCO.  
Efectividad técnica          Fuente landing        «mejora 5 %» semánticamente ambigua.  
Precio/comercialización      Fuente landing        CHF 8/g referencial; falta precio neto real.  
Atribución causal            Control propuesto      Falta piloto contra grupo de comparación.  
Política de comunicación     Auditoría ROI         Prohibido denominar ROI a valor bruto.

\===============================================================================

# 10\. PROPUESTA DE REDISEÑO DE LA CALCULADORA EN LANDING

\===============================================================================

CAMBIAR ETIQUETAS:  
Actual: «Mejora estimada con el control (%)».  
Recomendada si se mantiene la fórmula actual:  
«Porcentaje de la pérdida original que se espera evitar (%)».

Actual: «Valor anual estimado recuperado».  
Recomendada sin costos reales:  
«Valor bruto anual potencialmente recuperable (estimación, no ROI)».

MEJORAS DEL FORMULARIO:  
\- Identificar rendimiento BRUTO antes de pérdidas o NETO después de pérdidas.  
\- Identificar qué porcentaje corresponde a fracción de pérdidas evitadas y,  
  si se ofrece otra modalidad, separar claramente reducción en pp.  
\- Indicar procedencia de tasa histórica de merma y fecha de actualización.  
\- Mostrar volumen físico recuperado, valor bruto, porcentaje de pérdidas  
  originales recuperadas y riesgos en pantalla.  
\- Si se quiere mostrar ROI, exigir CAPEX, OPEX, factor de realización,  
  margen incremental, horizonte, descuento y ramp-up, con explicaciones.  
\- Bloquear divisiones por cero, valores negativos, rangos de pérdida \>=100%,  
  fracciones de pérdida evitada \>100% y entradas no numéricas/infinitas.  
\- Redondear para la visualización, no para el motor de cálculo.  
\- No prometer recuperación o retorno garantizados.

PSEUDOCÓDIGO DE REFERENCIA:

  ventaBase \= area \* gm2 \* precio \* ciclos  
  L \= perdida / 100  
  R \= mejora / 100          // SOLO si mejora \= fracción de pérdida evitada  
  validar(0 \<= L \< 1, 0 \<= R \<= 1\)  
  potencial \= (baseRendimiento \== 'neto') ? ventaBase/(1-L) : ventaBase  
  perdidaPotencial \= potencial \* L  
  brutoRecuperable \= perdidaPotencial \* R  
  contribucion \= brutoRecuperable \* factorRealizacion \* margenIncremental  
  flujo\_t \= contribucion \* adopcion\_t \- opex\_t \- capex\_adicional\_t  
  van \= \-capex\_inicial \+ suma(flujo\_t/(1+tasa)^t, para t=1..N)

ATENCIÓN: la etiqueta y la definición de base «neto/bruto» deben corresponder  
al mismo dato físico. No usar este pseudocódigo como parche sin pruebas.

\===============================================================================

# 11\. PLAN DE VALIDACIÓN PILOTO / AUDITORÍA DE DATOS

\===============================================================================

Unidad mínima de observación: cultivo × lote/superficie × ciclo × tecnología  
PlantGuard/control × calidad de la producción × precio marginal.

# 1\. FIJAR DENOMINADOR Y LÍNEA BASE:

   Documentar producción bruta y neta, definición de merma, niveles de  
   variación histórica, condición agronómica y método de medición.

# 2\. CONFIGURAR GRUPO COMPARABLE / CONTRAFACTUAL:

   Diseñar ensayo con control o análisis antes/después ajustado por otras  
   variables; cuantificar incertidumbre y diferencias entre ciclos.

# 3\. MEDIR EFECTO ATRIBUIBLE:

   Estimar pérdidas realmente evitadas, repetibilidad, variabilidad y  
   validez de escala; expresar intervalos de confianza si procede.

# 4\. VERIFICAR VALOR MONETIZABLE:

   Precio marginal real neto, descuentos, calidad, pérdidas comerciales,  
   transporte, condiciones contractuales, límites de demanda y calendario.

# 5\. RECOLECTAR COSTOS INCREMENTALES:

   Cotizar hardware/software/implementación, capacitación, mantenimiento,  
   licencias, energía, almacenamiento, operación, reposición, distribución,  
   atención y costo adicional por gramo útil.

# 6\. PRESENTAR FINANZAS CON TRAZABILIDAD:

   Flujo de caja por período, impuestos, capital de trabajo, escenarios,  
   VAN, TIR si corresponde, payback y umbral de aceptación documentado.

# 7\. APROBAR DECISIÓN:

   Responsable financiero y técnico firman un acta de validación; usar  
   caso base y caso adverso y comprobar capacidad de capturar beneficios.

\===============================================================================

# 12\. PLAN DE ACCIÓN Y CONTROL DIRECTIVO

\===============================================================================

ID         ACCIÓN                                           DUEÑO SUGERIDO          EVIDENCIA  
PG-FIN-01  Precisar «mejora» (% merma o pp)                  Producto \+ agronomía     Ficha técnica firmada  
PG-FIN-02  Confirmar si 400 g/m² es bruto o neto            Operaciones              Metodología de rendimiento  
PG-FIN-03  Validar CHF 8/g como precio marginal realizable Comercial \+ finanzas     Precios/netbacks observados  
PG-FIN-04  Cuantificar CAPEX, OPEX y TCO                     Finanzas                 Cotizaciones presupuestadas  
PG-FIN-05  Piloto contra control y atribución causal        Operaciones \+ datos      Informe \+ dataset reproducible  
PG-FIN-06  Actualizar ROI web y someter a aprobación        Producto \+ finanzas      Acta de validación y pruebas  
PG-FIN-07  Revisar impuestos, WACC, working capital y TIR   Finanzas/contabilidad   Caso de negocio aprobado  
PG-FIN-08  Revalidar el discurso comercial                  Comercial/legal          Ficha de afirmaciones auditada

POLÍTICA DE REVISIÓN:  
\- Cada supuesto real debe tener su origen, fecha, unidad, intervalo plausible,  
  responsable de actualización y estado de evidencia.  
\- El estudio debe revisarse cuando cambien: etiqueta de «mejora», rendimiento  
  bruto/neto, precio, merma, CAPEX/OPEX, piloto, horizonte o tasa.  
\- Para cada modificación en el modelo guardar versiones:  
  fecha, autor, supuesto modificado, documento de respaldo,  
  resultado VAN antes/después y decisión de aprobación.

\===============================================================================

# 13\. INVENTARIO DEL EXPEDIENTE GENERADO Y ESTRUCTURA DE ARCHIVOS

\===============================================================================

Ya preparado en la Biblioteca de ChatGPT, ruta:  
  /Finanzas/PlantGuard Pro/

Versiones de origen del expediente:

# 1\. PlantGuard\_Pro\_Estudio\_Financiero\_Integral\_v1.pdf

   Informe técnico-financiero de 8 páginas, fechado 13-11-2026.

# 2\. PlantGuard\_Pro\_Estudio\_Financiero\_Integral\_v1.docx

   Versión editable del mismo estudio.

# 3\. PlantGuard\_Pro\_Modelo\_Financiero\_ROI\_v1.xlsx

   Modelo con siete pestañas:  
   00\_Resumen, 01\_Parametros, 02\_Validacion, 03\_Flujos,  
   04\_Escenarios, 05\_Sensibilidad, 06\_Diccionario.

# 4\. PlantGuard\_Pro\_Fuente\_Calculadora\_13NOV2026.txt

   Transcripción del funcionamiento atribuido a landing/index.html.

Este archivo maestro .TXT consolida el CONTENIDO NECESARIO PARA CONSULTA EN  
CLAUDE. Los nombres y la ruta anterior NO otorgan a Claude acceso automático  
a esos archivos; si se requieren tablas editables y fórmulas en el proyecto,  
se debe añadir aparte el XLSX o disponer de una conexión de archivos autorizada.  
El archivo maestro no contiene un código fuente verificado del repositorio.

\===============================================================================

# 14\. INSTRUCCIONES SUGERIDAS PARA «PROJECT INSTRUCTIONS» EN CLAUDE

\===============================================================================

Copiar este bloque SOLO si se desea ajustar las instrucciones generales del  
proyecto. Si el proyecto ya tiene reglas superiores, integrarlas sin borrarlas.

«Actúa como asesor financiero, contable y de control de gestión de nivel  
corporativo. Usa el archivo 'PlantGuard\_Pro\_Paquete\_Maestro\_Claude\_Finanzas\_  
Contabilidad.txt' como base factual del expediente PlantGuard Pro.  
Distingue información confirmada, calculada e ilustrativa. No asumas que  
CHF 32.000 es utilidad o ROI. Separa valor bruto recuperado, contribución  
incremental, flujo de caja, VAN y ROI simple. Verifica denominadores,  
unidades y significado de porcentajes (fracción de merma frente a puntos  
porcentuales). Cruza análisis con bibliografía financiera de Google Drive,  
priorizando flujos incrementales, VAN, costos relevantes, contribución y  
presupuestos, y cita el documento exacto y su vínculo. No atribuyas a  
PlantGuard una eficacia técnica que no ha sido demostrada mediante datos.  
Si faltan CAPEX/OPEX, precio marginal o evidencia causal, presenta escenarios  
y limitaciones en vez de asegurar rentabilidad. Propón planes de validación,  
controles y decisiones para la dirección. Mantén los proyectos comerciales  
separados y conserva trazabilidad de versiones.»

\===============================================================================

# 15\. CONSULTAS DE VERIFICACIÓN DE CARGA EN CLAUDE

\===============================================================================

Tras cargar el archivo como conocimiento del proyecto, las siguientes  
preguntas deben responderse SIN inventar cifras:

P1. ¿Cuál es exactamente la fórmula original de «recuperado»?  
Respuesta: area\*gm2\*precio\*(perdida/100)\*(mejora/100)\*ciclos.

P2. ¿Cuánto informa la web con los seis valores por defecto?  
Respuesta: CHF 32.000/año, sujeto a su definición de rendimiento.

P3. ¿Qué diferencia hay entre 5 % de las pérdidas y reducir 5 pp?  
Respuesta: CHF 32.000 vs CHF 320.000 de valor bruto anual usando V bruto.

P4. ¿Cuál es el VAN del ejemplo financiero?  
Respuesta: ≈ −CHF 10.199 a tres años y 12 % con hipótesis ilustrativas.

P5. ¿Cuál es el ROI REAL del producto PlantGuard?  
Respuesta: No disponible ni demostrable con la información aportada.

P6. ¿Qué bibliografía de Google Drive fundamenta el método?  
Respuesta: Ross/Westerfield/Jordan; Berk/DeMarzo; Contabilidad  
administrativa; Presupuestos Empresariales; Manual de Costos y  
Presupuestos, con enlaces identificados en la sección 8\.

P7. ¿Este TXT sincroniza automáticamente archivos de Drive o Claude?  
Respuesta: No. Es un snapshot de conocimiento documentado con enlaces.

\===============================================================================

# 16\. NOTAS DE CALIDAD Y DECLARACIÓN DE LÍMITES

\===============================================================================

A. Se transcribieron las seis entradas y la fórmula con base en un documento  
   del usuario; no se verificó contra el código fuente original.  
B. Los libros del Drive sustentan el MÉTODO financiero, no las cifras  
   agronómicas, el precio de mercado ni los costos de PlantGuard.  
C. El archivo no incluye cifras de otros proyectos ni información personal.  
D. La revisión de precios de mercado, regulación sectorial y datos técnicos  
   requiere fuentes externas nuevas cuando se solicite.  
E. El estudio del 13-11-2026 es una prefactibilidad: debe incorporarse  
   evidencia operacional para elevarse a un caso de inversión.  
F. Los supuestos del archivo XLSX pueden cambiar y generar otros VAN/ROI.  
   La presente base documenta únicamente el escenario inicial.  
G. La incorporación en Claude requiere que el usuario lo cargue en su cuenta  
   o lo sincronice mediante un sistema con permisos específicos. Ningún  
   acceso a Claude ni enlace continuo con Google Drive se crea por este TXT.

FIN DEL PAQUETE MAESTRO — PLANTGUARD PRO / CLAUDE / FINANZAS Y CONTABILIDAD