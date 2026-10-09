# CD_04_02_04_ClasificacionMulticlase

## Página 1

 
Unidad 4: Aprendizaje Supervisado 
Tema: Clasificación Multiclase 
 
Ciencia de Datos 
Mgtr. Ing. Mariano Martín Gualpa (mgualpa@frc.utn.edu.ar) 


---

## Página 2

• 
El Problema de Clasificación. 
• 
Problemas de Clasificación Multiclase. 
• 
Actividad Práctica 
Temario de la Clase 


---

## Página 3

(Página sin texto reconocible)


---

## Página 4

•  La meta de la regresión logística es modelar relaciones entre 
un conjunto de variables predictoras y una variable objetivo 
categórica (target variable). 
•  ¿Desde donde? A  partir de  un  conjunto suficientemente 
grande de  pares x e y. 
•  Objetivos: 
•  Determinar presencia o ausencia de relación entre variables predictoras 
y la variable dependiente. 
•  Predecir la probabilidad de respuesta de cada valor posible, en función 
de la entrada. 
•  Utilizar estas probabilidades para clasificar observaciones futuras. 
Problemática a Resolver 


---

## Página 5

Variables: 
 
•  Variables predictoras o covariables: x = (x1, x2, x3,… , xm). 
•  Variable objetivo categórica: y 
•  Cantidad de Clases: 
•  Clasificación Binaria: dos clases. 
•  Clasificación Multiclase: mas de dos clases. 
•  Tipo de Variable Categórica: 
•  Variable Categórica Nominal. 
•  Variable Categórica Ordinal. 
Problemática a Resolver 


---

## Página 6

•  Dados: (x(1), y(1)), (x(2), y(2)), …, (x(n), y(n)) 
•  Meta: encontrar la mejor función h. 
•  Tal ŷ = h(x) corresponda a la categoría correcta y con una alta 
probabilidad. 
 
Problemática a Resolver 
1 
0 
y 
x 


---

## Página 7

•  Dados: (x(1), y(1)), (x(2), y(2)), …, (x(n), y(n)) 
•  Meta: encontrar la mejor función h. 
•  Tal ŷ = h(x) corresponda a la categoría correcta y con una alta 
probabilidad. 
 
Problemática a Resolver 
1 
0 
y 
x 
( x(i), y(i) ) 


---

## Página 8

•  Dados: (x(1), y(1)), (x(2), y(2)), …, (x(n), y(n)) 
•  Meta: encontrar la mejor función h. 
•  Tal ŷ = h(x) corresponda a la categoría correcta y con una alta 
probabilidad. 
 
Problemática a Resolver 
1 
0 
y 
x 
x 
ŷ = 0 
ŷ = 1 


---

## Página 9

(Página sin texto reconocible)


---

## Página 10

Clasificación Binaria  
(Binary Classification): 
 
 
 
 
 
Clasificación Multiclase 
x1 
x2 
0 
Clasificación Multiclase  
(Multi-class Classification): 
 
 
 
 
 
x1 
x2 
0 


---

## Página 11

Se obtiene la clasificación multiclase usando one vs. all: 
• 
Se corta el problema en varios problemas separados de clasificación binaria (uno 
por cada clase de y). 
• 
En el ejemplo se establecen tres hw: 
•  hw
(1)(x) :  Círculos (1) vs Cruces (0) y Cuadrados (0). 
•  hw
(2)(x) :  Cruces (1) vs Círculos (0) y Cuadrados (0). 
•  hw
(3)(x) :  Cuadrados (1) vs Círculos (0) y Cruces(0). 
 
 
 
 
 
Clasificación Multiclase 
 
 
 
 
 
 
x1
x2 
0 


---

## Página 12

Se obtiene la clasificación multiclase usando one vs. all: 
• 
Se corta el problema en varios problemas separados de clasificación binaria (uno 
por cada clase de y). 
• 
En el ejemplo se establecen tres hw: 
•  hw
(1)(x) :  Círculos (1) vs Cruces (0) y Cuadrados (0). 
•  hw
(2)(x) :  Cruces (1) vs Círculos (0) y Cuadrados (0). 
•  hw
(3)(x) :  Cuadrados (1) vs Círculos (0) y Cruces(0). 
 
 
 
 
 
Clasificación Multiclase 
 
 
 
 
 
 
x1
x2 
0 


---

## Página 13

Se obtiene la clasificación multiclase usando one vs. all: 
• 
Se corta el problema en varios problemas separados de clasificación binaria (uno 
por cada clase de y). 
• 
En el ejemplo se establecen tres hw: 
•  hw
(1)(x) :  Círculos (1) vs Cruces (0) y Cuadrados (0). 
•  hw
(2)(x) :  Cruces (1) vs Círculos (0) y Cuadrados (0). 
•  hw
(3)(x) :  Cuadrados (1) vs Círculos (0) y Cruces(0). 
 
 
 
 
 
Clasificación Multiclase 
 
 
 
 
 
 
x1
x2 
0 
x1
x2 
0 


---

## Página 14

Se obtiene la clasificación multiclase usando one vs. all: 
• 
Se corta el problema en varios problemas separados de clasificación binaria (uno 
por cada clase de y). 
• 
En el ejemplo se establecen tres hw: 
•  hw
(1)(x) :  Círculos (1) vs Cruces (0) y Cuadrados (0). 
•  hw
(2)(x) :  Cruces (1) vs Círculos (0) y Cuadrados (0). 
•  hw
(3)(x) :  Cuadrados (1) vs Círculos (0) y Cruces(0). 
 
 
 
 
 
Clasificación Multiclase 
 
 
 
 
 
 
x1
x2 
0 
x1
x2 
0 


---

## Página 15

Se obtiene la clasificación multiclase usando one vs. all: 
• 
Se corta el problema en varios problemas separados de clasificación binaria (uno 
por cada clase de y). 
• 
En el ejemplo se establecen tres hw: 
•  hw
(1)(x) :  Círculos (1) vs Cruces (0) y Cuadrados (0). 
•  hw
(2)(x) :  Cruces (1) vs Círculos (0) y Cuadrados (0). 
•  hw
(3)(x) :  Cuadrados (1) vs Círculos (0) y Cruces(0). 
 
 
 
 
 
Clasificación Multiclase 
 
 
 
 
 
 
x1
x2 
0 
x1
x2 
0 
x1
x2 
0 


---

## Página 16

Se obtiene la clasificación multiclase usando one vs. all: 
• 
Se corta el problema en varios problemas separados de clasificación binaria (uno 
por cada clase de y). 
• 
En el ejemplo se establecen tres hw: 
•  hw
(1)(x) :  Círculos (1) vs Cruces (0) y Cuadrados (0). 
•  hw
(2)(x) :  Cruces (1) vs Círculos (0) y Cuadrados (0). 
•  hw
(3)(x) :  Cuadrados (1) vs Círculos (0) y Cruces(0). 
 
 
 
 
 
Clasificación Multiclase 
 
 
 
 
 
 
x1
x2 
0 
x1
x2 
0 
x1
x2 
0 


---

## Página 17

Se obtiene la clasificación multiclase usando one vs. all: 
• 
Se corta el problema en varios problemas separados de clasificación binaria (uno 
por cada clase de y). 
• 
En el ejemplo se establecen tres hw: 
•  hw
(1)(x) :  Círculos (1) vs Cruces (0) y Cuadrados (0). 
•  hw
(2)(x) :  Cruces (1) vs Círculos (0) y Cuadrados (0). 
•  hw
(3)(x) :  Cuadrados (1) vs Círculos (0) y Cruces(0). 
 
Para utilizar: 
•  Entrenar los clasificadores de regresión logística hw
(i)(x) para 
cada clase i, buscando predecir la probabilidad de y = i 
•  Para cada nueva x, hacer la predicción y asignar la clase i 
que maximiza la probabilidad de que hw
(i)(x) = 1 
Clasificación Multiclase 
 
 
 
 
 
 


---

## Página 18

Problemas usando one vs. all: 
 
Esta descomposición no siempre 
funciona. 
 
 
 
 
 
 
 
 
Clasificación Multiclase 
 
 
 
 
 
 
x1
x2 
0 
x1
x2 
0 
x1
x2 
0 


---

## Página 19

Problemas usando one vs. all: 
 
Esta descomposición no siempre 
funciona. 
 
 
 
 
 
 
 
 
Clasificación Multiclase 
 
 
 
 
 
 
x1
x2 
0 
x1
x2 
0 
x1
x2 
0 
x1 
x2 
0 


---

## Página 20

Clasificación All-vs-All (a veces One-vs-One) 
Asumiendo que cada par de clases es separable, entonces: 
 
Entrenamiento:  
• 
Dado un conjunto de datos D = {x(i), y(i)}, donde x(i) ∈ Rm , y ∈ {1, 2,…,k} 
• 
Por cada par de etiquetas (j, k), crear un clasificador binario donde: 
• 
Los ejemplos positivos son todos los ejemplos con etiqueta j.  
• 
Los ejemplos negativos son todos los ejemplos con etiqueta k.  
• 
Entrenar                  clasificadores que separen cada par de etiquetas. 
Predicción:  
• 
Por cada etiqueta, tomar k-1 votos. 
• 
Combinar los votos: 
• 
Seleccionar la etiqueta con mayor cantidad de votos. 
• 
Organizar torneos entre las etiquetas: iniciar con k/2 pares y continuar con los ganadores. 
Clasificación Multiclase 
 
 
 
 
 
 
k
2
⎛
⎝
⎜
⎞
⎠
⎟= k(k −1)
2


---

## Página 21

Clasificación All-vs-All (a veces One-vs-One) 
 
Problemas: 
 
• 
Muchos vectores de pesos para entrenar y almacenar. O(K2). 
• 
Por algunos pares de etiquetas, el tamaño del conjunto de entrenamiento 
podría ser muy pequeño => overfitting. 
• 
Problemas de posible inestabilidad con la predicción: 
• 
¿Secuencia del torneo? 
• 
¿Empate en votos? 
 
Otros enfoques para clasificación multiclase:  
• 
Error Correcting Output Codes (ECOC) 
• 
Específicos del Modelo o Algoritmo: por ejemplo regresión logística. 
Clasificación Multiclase 
 
 
 
 
 
 


---

## Página 22

  
 
Ciencia de Datos 
 
 
¿Preguntas? 


---

## Página 23

  
 
Ciencia de Datos 
 
 
¡Muchas gracias! 


---
