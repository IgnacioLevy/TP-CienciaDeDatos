# CD_02_03_Preprocesamiento

## Página 1

UNIDAD 2: ETL - PREPROCESAMIENTO
Mgtr. Ing. Mariano Martín Gualpa
CIENCIA DE DATOS


---

## Página 2

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
PREPROCESAMIENTO
Tipos de Variables:
• Variables Categóricas
• Variables Numéricas
• Variables Mixtas
• Variables Fecha-Hora


---

## Página 3

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
PREPROCESAMIENTO
Tipos de Variables:
• Variables Categóricas
• Nominal 
• Ordinal
• Dicotómica vs Politómica
• Variables Numéricas
• Variables Mixtas
• Variables Fecha-Hora


---

## Página 4

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
PREPROCESAMIENTO
Tipos de Variables:
• Variables Categóricas
• Variables Numéricas
• Continuas
• Discretas
• Variables Mixtas
• Variables Fecha-Hora


---

## Página 5

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
PREPROCESAMIENTO
Tipos de Variables:
• Variables Categóricas
• Variables Numéricas
• Variables Mixtas
• Números o Categorías
• Números y Categorías
• Variables Fecha-Hora


---

## Página 6

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
PREPROCESAMIENTO
Tipos de Variables:
• Variables Categóricas
• Variables Numéricas
• Variables Mixtas
• Variables Fecha-Hora
• Fecha
• Hora
• Fecha y Hora


---

## Página 7

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
PREPROCESAMIENTO
Métodos de Preprocesamiento:
• Limpieza de Datos.
• Integración de Datos y Transformación 
de Datos.
• Reducción de Datos. 
• Discretización y Generación de 
Jerarquías Conceptuales.


---

## Página 8

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
FUENTES DE ERRORES EN LOS DATOS
Características indeseables en los datos
• Faltantes
• Irregulares u Outliers
• Inconsistentes
• Innecesarios


---

## Página 9

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
FUENTES DE ERRORES EN LOS DATOS
Características indeseables en los datos
Valores Faltantes
•
Atributos no disponibles
•
No se consideraron importantes
•
No se grabaron por malentendidos o fallas.
•
Se perdió el historial de modificaciones


---

## Página 10

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
FUENTES DE ERRORES EN LOS DATOS
Características indeseables en los datos
Valores Irregulares u Outliers
• Instrumentos de recolección defectuosos
• Errores humanos o computadoras en el ingreso de 
los datos
• Limitaciones tecnológicas, por ejemplo tamaño de 
buffer.


---

## Página 11

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
FUENTES DE ERRORES EN LOS DATOS
Características indeseables en los datos
Valores Inconsistentes
•
Convención de nombres o códigos
•
Tuplas duplicadas
¿Córdoba, Cordoba, 
cordoba, CORDOBA?


---

## Página 12

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
FUENTES DE ERRORES EN LOS DATOS
Tipos de Errores:
• Datos Incompletos
• Datos con Ruido
• Datos Inconsistentes


---

## Página 13

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
FUENTES DE ERRORES EN LOS DATOS
Fuentes de Errores:
•
Datos Incompletos:
•
Atributos no siempre disponibles.
•
No incluidos inicialmente por considerarse 
irrelevantes.
•
No registrados por malentendidos o fallas en 
equipos.
•
Falla el registro histórico de actualizaciones 
del dato.
•
Podrían necesitar inferirse. 
•
Datos con Ruido
•
Datos Inconsistentes


---

## Página 14

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
FUENTES DE ERRORES EN LOS DATOS
Fuentes de Errores:
•
Datos Incompletos
•
Datos con Ruido: valores incorrectos en los 
atributos.
•
Instrumentos de recolección defectuosos.
•
Errores durante el ingreso (humanos o 
equipos).
•
Limitaciones tecnológicas (ej: tamaño de 
buffer en Tx).
•
Datos Inconsistentes


---

## Página 15

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
FUENTES DE ERRORES EN LOS DATOS
Tipos de Errores:
•
Datos Incompletos
•
Datos con Ruido
•
Datos Inconsistentes:
•
Inconsistencias en convenciones de nombres 
o códigos.
•
Tuplas duplicadas.


---

## Página 16

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
PASOS DE PRE-PROCESAMIENTO DE LOS DATOS
Pasos correspondientes al pre-procesamiento 
de datos:
•
Limpieza de los datos.
•
Integración de los datos.
•
Transformación de los datos.
•
Reducción de datos.


---

## Página 17

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
LIMPIEZA DE DATOS
Valores Faltantes:
Algunas tuplas no tienen valores registrados para 
algunos atributos.
Técnicas:
•
Ignorar la tupla completa.
•
Llenar el valor manualmente.
•
Usar una constante global para llenar el valor.
•
Usar una medida estadística para completar.
•
Usar la media de los atributos para todos los 
ejemplos pertenecientes a la misma clase de la 
tupla con valor faltante.
•
Usar el valor más probable para completar.


---

## Página 18

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
LIMPIEZA DE DATOS
Valores Faltantes:
Algunas tuplas no tienen valores registrados para 
algunos atributos.
Técnicas:
•
Ignorar la tupla completa.
•
Llenar el valor manualmente.
•
Usar una constante global para llenar el valor.
•
Usar una medida estadística para completar.
•
Usar la media de los atributos para todos los 
ejemplos pertenecientes a la misma clase de la 
tupla con valor faltante.
•
Usar el valor más probable para completar.


---

## Página 19

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
LIMPIEZA DE DATOS
Valores Faltantes:
Algunas tuplas no tienen valores registrados para 
algunos atributos.
Técnicas:
•
Ignorar la tupla completa.
•
Llenar el valor manualmente.
•
Usar una constante global para llenar el valor.
•
Usar una medida estadística para completar.
•
Usar la media de los atributos para todos los 
ejemplos pertenecientes a la misma clase de la 
tupla con valor faltante.
•
Usar el valor más probable para completar.
Estos métodos no influyen en los datos
A1


---

## Página 20

Slide 19
A1 
Author, 9/11/2024


---

## Página 21

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
LIMPIEZA DE DATOS
Datos con Ruido:
Error aleatorio o variación en una variable medida que 
afecta la calidad de los datos.
Técnicas:
•
Encajado (binning).
•
Agrupar.
•
Combinación de Inspección Humana y 
Computarizada.
•
Regresión.
•
Discretización (similar a encajado, jerarquías 
conceptuales).


---

## Página 22

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
LIMPIEZA DE DATOS
Datos Inconsistentes:
Inconsistencias en los datos obtenidos de 
determinadas transacciones.
Técnicas:
•
Chequeo de lo ingresado.
•
Rutinas para detección de inconsistencias.
•
Conocer dependencias funcionales entre 
atributos.


---

## Página 23

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
INTEGRACIÓN Y TRANSFORMACIÓN DE DATOS
Integración de Datos:
• Asegurar que claves en diferentes fuentes se 
refieren a la misma entidad.
• Redundancias:
• Puede haber por tuplas o por columnas.
• Correlación
• Valores de diferentes fuentes pueden diferir 
(ej: unidad de medida).
rA,B =
(A - A)×(B - B)
å
(n -1)×s A ×s B


---

## Página 24

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
INTEGRACIÓN Y TRANSFORMACIÓN DE DATOS
Transformación de Datos:
•
Suavizamiento (smoothing):
•
Utilizando binning, clustering y regresión.
•
Agregación.
•
Generalización de los Datos (ej: utilizando 
jerarquías conceptuales).
•
Normalización.
•
Min-Max
•
Z-Score
•
Ajuste decimal
•
Construcción de Atributos.


---

## Página 25

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
INTEGRACIÓN Y TRANSFORMACIÓN DE DATOS
Transformación de Datos:
•
Suavizamiento (smoothing):
•
Utilizando binning, 
clustering y regresión.
•
Agregación.
•
Generalización de los Datos 
(ej: utilizando jerarquías 
conceptuales).
•
Normalización.
•
Min-Max
•
Z-Score
•
Ajuste decimal
•
Construcción de Atributos.


---

## Página 26

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
INTEGRACIÓN Y TRANSFORMACIÓN DE DATOS
Transformación de Datos:
•
Suavizamiento (smoothing):
•
Utilizando binning, 
clustering y regresión.
•
Agregación.
•
Generalización de los Datos 
(ej: utilizando jerarquías 
conceptuales).
•
Normalización.
•
Min-Max
•
Z-Score
•
Ajuste decimal
•
Construcción de Atributos.


---

## Página 27

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
INTEGRACIÓN Y TRANSFORMACIÓN DE DATOS
Transformación de Datos:
•
Suavizamiento (smoothing):
•
Utilizando binning, 
clustering y regresión.
•
Agregación.
•
Generalización de los Datos 
(ej: utilizando jerarquías 
conceptuales).
•
Normalización.
•
Min-Max
•
Z-Score
•
Ajuste decimal
•
Construcción de Atributos.


---

## Página 28

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
INTEGRACIÓN Y TRANSFORMACIÓN DE DATOS
Transformación de Datos:
•
Suavizamiento (smoothing):
•
Utilizando binning, 
clustering y regresión.
•
Agregación.
•
Generalización de los Datos 
(ej: utilizando jerarquías 
conceptuales).
•
Normalización.
•
Min-Max
•
Z-Score
•
Ajuste decimal
•
Construcción de Atributos.
Donde j es el entero más chico para el cual 
Max(|X’A|)<1
XA
' = XA -mA
s A
XA
' =
XA - MinA
MaxA - MinA
XA
' = XA
10 j


---

## Página 29

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
INTEGRACIÓN Y TRANSFORMACIÓN DE DATOS
Transformación de Datos:
•
Suavizamiento (smoothing):
•
Utilizando binning, 
clustering y regresión.
•
Agregación.
•
Generalización de los Datos 
(ej: utilizando jerarquías 
conceptuales).
•
Normalización.
•
Min-Max
•
Z-Score
•
Ajuste decimal
•
Construcción de Atributos.


---

## Página 30

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
REDUCCIÓN DE DATOS
Estrategias de Reducción de 
Datos:
•
Agregado de Cubo de 
Datos.
•
Reducción de Dimensión.
•
Compresión de Datos 
(codificación).
•
Reducción Numérica.
•
Discretización y 
Generación de Jerarquías 
Conceptuales


---

## Página 31

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
REDUCCIÓN DE DATOS
Estrategias de Reducción de 
Datos:
•
Agregado de Cubo de 
Datos.
•
Reducción de Dimensión.
•
Compresión de Datos 
(codificación).
•
Reducción Numérica.
•
Discretización y 
Generación de Jerarquías 
Conceptuales


---

## Página 32

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
REDUCCIÓN DE DATOS
Estrategias de Reducción de 
Datos:
•
Agregado de Cubo de 
Datos.
•
Reducción de Dimensión.
•
Compresión de Datos 
(codificación).
•
Reducción Numérica.
•
Discretización y 
Generación de Jerarquías 
Conceptuales
Feature Selection
Dimensional Reduction


---

## Página 33

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
REDUCCIÓN DE DATOS
Estrategias de Reducción de 
Datos:
•
Agregado de Cubo de 
Datos.
•
Reducción de Dimensión.
•
Compresión de Datos 
(codificación).
•
Reducción Numérica.
•
Discretización y 
Generación de Jerarquías 
Conceptuales
Reducción de 
dimensionalidad por 
transformación de datos.


---

## Página 34

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
REDUCCIÓN DE DATOS
Estrategias de Reducción de 
Datos:
•
Agregado de Cubo de 
Datos.
•
Reducción de Dimensión.
•
Compresión de Datos 
(codificación).
•
Reducción Numérica.
•
Discretización y 
Generación de Jerarquías 
Conceptuales


---

## Página 35

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
REDUCCIÓN DE DATOS
Estrategias de Reducción de 
Datos:
•
Agregado de Cubo de 
Datos.
•
Reducción de Dimensión.
•
Compresión de Datos 
(codificación).
•
Reducción Numérica.
•
Discretización y 
Generación de Jerarquías 
Conceptuales


---

## Página 36

UNIDAD 2: ETL (PRE-PROCESAMIENTO)
¡Muchas gracias!


---
