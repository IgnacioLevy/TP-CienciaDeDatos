# CD_04_01_RegresionLineal

## Página 1

Unidad 4: Aprendizaje Supervisado
Tema: Regresión Lineal
Ciencia de Datos
Mgtr. Ing. Mariano Martín Gualpa (mgualpa@frc.utn.edu.ar)


---

## Página 2

•
Fundamentos Aprendizaje Automático.
•
Aprendizaje Automático Supervisado.
•
Repaso de conceptos básicos.
•
Problemática a resolver.
•
Visión General del Proceso.
•
Aspectos a considerar.
•
El Modelo de Regresión Lineal.
•
Regresión Lineal Simple.
•
Regresión Lineal Múltiple.
•
Aprendizaje con Regresión Lineal.
•
Evaluación del Desempeño del Modelo de Regresión.
•
Práctica de Programación 1.
•
Regresión Polinomial.
•
Error de Sesgo (Bias) vs Error de Varianza (Variance).
•
Complejidad del Modelo.
•
Efecto de Escalar Variables
•
Práctica de Programación 2.
•
Parámetro de Regularización.
•
Ridge
•
LASSO
•
ElasticNet.
•
Elementos que Ayudan a Mejorar el Modelo
•
Otros Algoritmos para Regresión.
Temario de la Clase


---

## Página 3

(Página sin texto reconocible)


---

## Página 4

Paradigma Tradicional:
Aprendizaje Automático
Computadora
Datos
Programa
Salida


---

## Página 5

Paradigma Tradicional:
Aprendizaje Automático:
Aprendizaje Automático
Computadora
Datos
Programa
Salida
Computadora
Datos
Salida
Programa
(modelo)


---

## Página 6

Paradigma Tradicional:
Aprendizaje Automático:
Aprendizaje Automático
Computadora
Datos
Programa
Salida
Computadora
Datos
Salida
Programa
(modelo)
Computadora
Datos
Salida


---

## Página 7

Tipos de Aprendizaje:
• Aprendizaje Supervisado.
• Aprendizaje No Supervisado.
• Aprendizaje Semi-Supervisado.
• Aprendizaje por Refuerzo.
Aprendizaje Automático


---

## Página 8

Tipos de Aprendizaje:
• Aprendizaje Supervisado.
• Datos + Salida
• Salida: 
• Regresión: Variable Continua.
• Clasificación: Variable categórica.
• Aprendizaje No Supervisado.
• Aprendizaje Semi-Supervisado.
• Aprendizaje por Refuerzo.
Aprendizaje Automático


---

## Página 9

Tipos de Aprendizaje:
• Aprendizaje Supervisado.
• Aprendizaje No Supervisado.
• Datos con salida no disponible.
• Clustering.
• Asociación.
• Detección de anomalías.
• Reducción de dimensionalidad.
• Aprendizaje Semi-Supervisado.
• Aprendizaje por Refuerzo.
Aprendizaje Automático


---

## Página 10

Tipos de Aprendizaje:
• Aprendizaje Supervisado.
• Aprendizaje No Supervisado.
• Aprendizaje Semi-Supervisado.
• Datos + algunas salidas
• Clasificación.
• Clustering.
• Aprendizaje por Refuerzo.
Aprendizaje Automático


---

## Página 11

Tipos de Aprendizaje:
• Aprendizaje Supervisado.
• Aprendizaje No Supervisado.
• Aprendizaje Semi-Supervisado.
• Aprendizaje por Refuerzo.
• Entorno y recompensas. 
• Establecer que es un estado deseado.
• Problemas de búsqueda de políticas.
Aprendizaje Automático


---

## Página 12

Paradigma Tradicional:
Aprendizaje Automático:
Aprendizaje Automático Supervisado
Computadora
Datos
Programa
Salida
Computadora
Datos: 
emails
Salida: 
Spam/No 
Spam
Programa
(modelo)
Computadora
Datos: 
Nuevos 
emails
Salida: 
Spam/No 
Spam


---

## Página 13

Paradigma Tradicional:
Aprendizaje Automático:
Aprendizaje Automático Supervisado
Computadora
Datos
Programa
Salida
Computadora
Datos: 
Clientes
Salida: 
Mora
Programa
(modelo)
Computadora
Datos: 
Nuevos 
Clientes
Salida: 
Mora


---

## Página 14

Paradigma Tradicional:
Aprendizaje Automático:
Aprendizaje Automático Supervisado
Computadora
Datos
Programa
Salida
Computadora
Datos: 
Mediciones
Salida: 
Humedad
Programa
(modelo)
Computadora
Datos: 
Nuevas 
Mediciones
Salida: 
Humedad


---

## Página 15

Paradigma Tradicional:
Aprendizaje Automático:
Aprendizaje Automático Supervisado
Computadora
Datos
Programa
Salida
Computadora
Datos: 
Cotizaciones
Salida: 
Valor
Programa
(modelo)
Computadora
Datos: 
Nuevas 
Cotizaciones
Salida: 
Valor


---

## Página 16

Paradigma Tradicional:
Aprendizaje Automático:
Aprendizaje Automático Supervisado
Computadora
Datos
Programa
Salida
Computadora
Datos: Med. 
Sensores
Salida: 
Estado
Programa
(modelo)
Computadora
Datos: 
Sensores
Salida: 
Estado


---

## Página 17

Paradigma Tradicional:
Aprendizaje Automático:
Aprendizaje Automático Supervisado
Computadora
Datos
Programa
Salida
Computadora
Datos: 
Imágen
Salida: 
Etiqueta
Programa
(modelo)
Computadora
Datos: 
Nuevos 
Imágenes
Salida: 
Etiqueta


---

## Página 18

Aprendizaje Automático Supervisado
Computadora
Aprendizaje:
Encontrar h perteneciente a H
sujeta a:
yi ≈ h(xi)
Datos: X
Salida: y
ŷ = h(x)
Datos de 
entrenamiento


---

## Página 19

Aprendizaje Automático Supervisado
Computadora
Aprendizaje:
Encontrar h perteneciente a H
sujeta a:
yi ≈ h(xi)
Datos: X
Salida: y
ŷ = h(x)
Datos de 
entrenamiento
Nuevos 
datos:
x
Salida:
Pred.


---

## Página 20

(Página sin texto reconocible)


---

## Página 21

•
Escalar: en general, se refiere a un número real.
α = 0,5      ;        λ = 3      ;    x1 = 1.500
•
Vector: una tupla de m elementos (números en nuestro caso).
x = (x1, x2, x3, …, xm) 
•
Matriz: arreglo bidimensional de números. 
X =                                             = 
Repaso de Algunos Temas Básicos
xm
(1)
…
x2
(1)
x1
(1)
xm
(2)
…
x2
(2)
x1
(2)
…
…
…
…
xm
(n)
…
x2
(n)
x1
(n)
x(1)
x(2)
…
x(n)


---

## Página 22

(Página sin texto reconocible)


---

## Página 23

•
La meta de la regresión lineal es modelar relaciones entre un 
conjunto de variables explicativas (explanatory variables) y una 
variable objetivo continua (target variable).
•
Variables:
•
Variables explicativas: x = (x1, x2, x3,… , xm)
•
Variable objetivo: y
•
Meta: encontrar la mejor función h.
•
Tal que aproxime ŷ = h(x)
•
En regresión lineal, el modelo h que relaciona estas variables es un 
modelo lineal.
•
¿Desde donde? A partir de un conjunto suficientemente grande de 
pares x e y.
Problemática a Resolver


---

## Página 24

1.
Construir el conjunto de ejemplos de entrenamiento.
1.
Recolectar datos.
2.
Del conjunto, establecer características discriminativas, relevantes, que no sean 
fácilmente afectadas por el ruido. <= Análisis Exploratorio.
2.
Elegir un modelo que constituya una generalización aproximada, 
determinando un espacio de hipótesis.
3.
Elegir una función de error que permita discriminar según el 
desempeño de las diferentes hipótesis.
4.
Elegir un algoritmo de entrenamiento que permita seleccionar la mejor 
hipótesis.
5.
Realizar el proceso de entrenamiento.
6.
Evaluar modelos obtenidos y seleccionar.
Visión General del Proceso 


---

## Página 25

(Página sin texto reconocible)


---

## Página 26

Modelo de Regresión Lineal Simple:
w0: coordenada al origen (intercept).
w1: coeficiente de peso de la variable (slope).
El Modelo de Regresión Lineal
ˆy = w0 + w1x


---

## Página 27

Modelo de Regresión Lineal Múltiple:
w: vector de coeficientes de pesos correspondientes a las variables.
x: vector de variables independientes.
w0: coordenada al origen (intercept).
x0 = 1
El Modelo de Regresión Lineal
ˆy = w0x0 + w1x1 + w2x2 +...+ wmxm
ˆy =
wixi
i=0
m
å
= wTx


---

## Página 28

(Página sin texto reconocible)


---

## Página 29

Modelo de Regresión Lineal:
El problema del aprendizaje con este modelo puede plantearse básicamente 
como:
Ordinary Least Square
Aprendizaje con Regresión Lineal
ˆy = w0x0 + w1x1 + w2x2 +...+ wmxm =
wjx j
j=0
m
å
= wTx
J(w) = 1
2
y(i) - ˆy(i)
(
)
2
i=1
n
å
argmin
w
1
2
y(i) - w0 -
wjx j
(i)
j=1
m
å
æ
è
çç
ö
ø
÷÷
2
i=1
n
å
é
ë
ê
ê
ù
û
ú
ú


---

## Página 30

(Página sin texto reconocible)


---

## Página 31

Supuestos de la Regresión Lineal
Imagen: https://www.geeksforgeeks.org/machine-learning/assumptions-of-linear-regression


---

## Página 32

Linealidad: 
• La relación entre las variables dependientes e 
independiente es lineal.
Supuestos de la Regresión Lineal
Imagen: https://www.geeksforgeeks.org/machine-learning/assumptions-of-linear-regression


---

## Página 33

Homocedasticidad de residuos: 
•
Los residuos (las diferencias entre los 
valores observados y predichos) 
deben tener una varianza constante 
en todos los niveles de la(s) 
variable(s) independiente(s).
•
Es decir: la dispersión de los errores 
debe ser relativamente uniforme, 
independientemente del valor del 
predictor.
Supuestos de la Regresión Lineal
Imagen: https://www.geeksforgeeks.org/
Imagen: https://www.wikipedia.org/


---

## Página 34

Supuestos de la Regresión Lineal
Imagen: https://www.fuenterrebollo.com/Economicas/TEORICA-I/2-bidimensional.pdf


---

## Página 35

Normalidad multivariante -
Distribución normal: 
•
Los residuos (las diferencias entre 
los valores observados y 
predichos) deben seguir una 
distribución normal al considerar 
múltiples predictores en conjunto. 
Supuestos de la Regresión Lineal
Imagen: https://www.geeksforgeeks.org/


---

## Página 36

Independencia de los errores: 
•
Los residuos (las diferencias 
entre los valores observados y 
predichos) no estén 
correlacionados entre sí. 
Supuestos de la Regresión Lineal
Imagen: https://www.geeksforgeeks.org/
Imagen: https://www.analyticsvidhya.com/


---

## Página 37

Falta de multicolinealidad: 
•
Las variables independientes 
no están altamente 
correlacionadas entre sí. 
Supuestos de la Regresión Lineal
Imagen: https://www.codetodevs.com/correlacion-variables-pairplot-seaborn/
Imagen: https://www.kaggle.com/code/abonaplata/analisis-
exploratorio-de-datos-con-python/notebook


---

## Página 38

Ausencia de endogeneidad: 
•
Las variables independientes del 
modelo de regresión no deben 
estar correlacionadas con el 
término de error.
•
Si se viola este supuesto, se 
obtienen estimaciones sesgadas e 
inconsistentes de los coeficientes 
de regresión. 
Supuestos de la Regresión Lineal
Imagen: https://www.geeksforgeeks.org/
Imagen: https://blog.shakirm.com/


---

## Página 39

(Página sin texto reconocible)


---

## Página 40

Gráfico de Residuos:
Evaluación de Desempeño del M. de Reg.
e(i) = ˆy(i) - y(i)


---

## Página 41

y(x,w) = w0x0 + w1x1 + w2x2 +...+ wmxm = ˆy
Modelo de Regresión:
Gráfico QQ:
Evaluación de Desempeño del M. de Reg.


---

## Página 42

MSE: Media del Error Cuadrático (Mean Squared Error)
RMSE: Raíz de la Media del Error Cuadrático (Root Mean 
Squared Error)
Evaluación de Desempeño del M. de Reg.
MSE = 1
n
y(i) - ˆy(i)
(
)
2
i=1
n
å
RMSE =
1
n
y(i) - ˆy(i)
(
)
2
i=1
n
å


---

## Página 43

R2: Coeficiente de Determinación
Evaluación de Desempeño del M. de Reg.
R2 =1- SSE
SST
SSE: Sum of squared errors
SST: Total sum of squared
R2 =1- SSE
SST =1-
y(i) - ˆy(i)
(
)
2
i=1
n
å
y(i) -my
(
)
2
i=1
n
å
R2 =1-
1
n
y(i) - ˆy(i)
(
)
2
i=1
n
å
1
n
y(i) -my
(
)
2
i=1
n
å
R2 =1- MSE
Var(y)


---

## Página 44

(Página sin texto reconocible)


---

## Página 45

(Página sin texto reconocible)


---

## Página 46

Modelo de Regresión Polinomial:
d: grado del polinomio
Transformación: Dado un valor para d por cada x(i) aplicamos una 
transformación RR1x(d+1) tal que:
x (x0, x1, x2, …, xd)  donde (x0, x1, x2, …, xd) será (x0, x1, x2, …, xd)
El Modelo de Regresión Lineal
ˆy = w0 + w1x + w2x
2 +...+ wdx
d


---

## Página 47

Entendiendo el Undefitting y Overfitting


---

## Página 48

Los diferentes modelos pueden tener diferentes “grados de 
libertad”. 
Modelo:
Error de Sesgo vs Error de Varianza
ˆy = w0 + w1x + w2x2 +...+ wmxm


---

## Página 49

Modelo: 
Error de Sesgo vs Error de Varianza
ˆy = w0 + w1x + w2x
2 +...+ wmx
m


---

## Página 50

Modelo: 
Error de Sesgo vs Error de Varianza
ˆy = w0 + w1x + w2x
2 +...+ wmx
m


---

## Página 51

Modelo: 
Error de Sesgo vs Error de Varianza
ˆy = w0 + w1x + w2x
2 +...+ wmx
m


---

## Página 52

Modelo: 
Error de Sesgo vs Error de Varianza
ˆy = w0 + w1x + w2x
2 +...+ wmx
m


---

## Página 53

Modelo: 
Error de Sesgo vs Error de Varianza
ˆy = w0 + w1x + w2x
2 +...+ wmx
m


---

## Página 54

Modelo: 
Error de Sesgo vs Error de Varianza
ˆy = w0 + w1x + w2x
2 +...+ wmx
m


---

## Página 55

¿cómo evolucionó el error?
Error de Sesgo vs Error de Varianza


---

## Página 56

Error de Sesgo vs Error de Varianza


---

## Página 57

Error vs Complejidad del Modelo


---

## Página 58

(Página sin texto reconocible)


---

## Página 59

Efecto del Escalar las Variables


---

## Página 60

(Página sin texto reconocible)


---

## Página 61

(Página sin texto reconocible)


---

## Página 62

Regresión Lineal:
Modelos de Regresión Lineal Regularizada
y(x,w) = w0x0 + w1x1 + w2x2 +...+ wmxm = ˆy
J(w) = 1
2
y(i) - ˆy(i)
(
)
2
i=1
n
å


---

## Página 63

Ridge Regression:
Modelos de Regresión Lineal Regularizada
y(x,w) = w0x0 + w1x1 + w2x2 +...+ wmxm = ˆy
J w
( )Ridge =
y(i) - ˆy(i)
(
)
2 + l w 2
2
i=1
n
å
L2 : l w 2
2 = l
(wj)2
j=1
m
å


---

## Página 64

Ridge Regression:
Modelos de Regresión Lineal Regularizada


---

## Página 65

Ridge Regression:
Modelos de Regresión Lineal Regularizada


---

## Página 66

LASSO (Least Absolute Shrinkage and Selection Operator):
Modelos de Regresión Lineal Regularizada
y(x,w) = w0x0 + w1x1 + w2x2 +...+ wmxm = ˆy
J w
( )LASSO =
y(i) - ˆy(i)
(
)
2 + l w 1
i=1
n
å
L1: l w 1 = l
wj
j=1
m
å


---

## Página 67

LASSO (Least Absolute Shrinkage and Selection Operator):
Modelos de Regresión Lineal Regularizada


---

## Página 68

LASSO (Least Absolute Shrinkage and Selection Operator):
Modelos de Regresión Lineal Regularizada


---

## Página 69

Regresión Lineal vs Ridge vs LASSO
Modelos de Regresión Lineal Regularizada


---

## Página 70

Regresión Lineal vs Ridge vs LASSO
Modelos de Regresión Lineal Regularizada


---

## Página 71

J w
( )ElasticNet =
y(i) - ˆy(i)
(
)
2 + l1
(wj)2
j=1
m
å
+ l2
wj
j=1
m
å
i=1
n
å
ElasticNet:
En Sklearn o en R:
Modelos de Regresión Lineal Regularizada
y(x,w) = w0x0 + w1x1 + w2x2 +...+ wmxm = ˆy
J w
( )ElasticNet =
y(i) - ˆy(i)
(
)
2 + l1 w 1
2 + l2 w 1
i=1
n
å
J w
( )ElasticNet =
y(i) - ˆy(i)
(
)
2 + l
1- rl1
(
)
(wj)2
j=1
m
å
+ rl1
wj
j=1
m
å
æ
è
çç
ö
ø
÷÷
i=1
n
å


---

## Página 72

(Página sin texto reconocible)


---

## Página 73

Existen muchos elementos que pueden ayudar con el 
sobreajuste son:
• Validación cruzada adecuada.
• Complejidad del modelo.
• Aumentar la cantidad de datos.
• Agregar regularización para penalizar los wj en la loss
function. 
• Afecta al tamaño de los coeficientes wj.
• Afecta a la cantidad de términos en el polinomio.
• Normalizar las features (xi) para que no afecte el orden de 
magnitud.
• Agregar mas features antes de ajustar el modelo.
Elementos que Ayudan a Mejorar el Modelo


---

## Página 74

(Página sin texto reconocible)


---

## Página 75

Existen otros modelos y algoritmos para regresión:
• Regresión de N vecinos más próximos (Kneighbors
Regression).
• Regresión con Árboles de Decisión.
• Regresión con Random Forest.
• Redes Neuronales.
• Entre otras.
Otros Algoritmos para Regresión


---

## Página 76

¿Preguntas?
y = w01+ w1x1 + w2x2 +...+ wmxm


---

## Página 77

¡Muchas gracias!
Ciencia de Datos


---
