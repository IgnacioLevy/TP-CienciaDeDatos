# CD_04_02_01_RegresionLogistica

## Página 1

 
Unidad 4: Aprendizaje Supervisado 
Tema: Clasificación. Regresión Logística 
 
Ciencia de Datos 
 
Mgtr. Ing. Mariano Martín Gualpa (mgualpa@frc.utn.edu.ar) 


---

## Página 2

• 
El Problema de Clasificación. 
• 
Introducción Intuitiva a la Regresión Logística. 
• 
Fundamentación Teórica. 
• 
Frontera de Decisión. 
• 
Fronteras No Lineales. 
• 
Interpretación Probabilística. 
• 
Función de Costo para Regresión Logística. 
• 
Término de Regularización. 
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

•  Dados: (x(1), y(1)), (x(2), y(2)), …, (x(n), y(n)) 
•  Meta: encontrar la mejor función para predecir y. 
 
 
Introducción Intuitiva a la R. Logística 
1 
0 
y 
x 


---

## Página 11

•  Dados: (x(1), y(1)), (x(2), y(2)), …, (x(n), y(n)) 
•  Meta: encontrar la mejor función para predecir y. 
 
Introducción Intuitiva a la R. Logística 
1 
0 
y 
x 
✗ 
hw(x) = wTx 


---

## Página 12

•  Dados: (x(1), y(1)), (x(2), y(2)), …, (x(n), y(n)) 
•  Meta: encontrar la mejor función para predecir y. 
 
 
 
 
 
 
•  Problema:  
•  Valores positivos pueden cambiar dramáticamente la pendiente. 
•  Variable de salida y solo puede ser 0 ó 1. 
•  La hipótesis puede tomar valores mas grandes que 1 y menores que 0. 
Introducción Intuitiva a la R. Logística 
1 
0 
y 
x 
hw(x) = wTx 
✗ 


---

## Página 13

•  Dados: (x(1), y(1)), (x(2), y(2)), …, (x(n), y(n)) 
•  Meta: encontrar la mejor función para predecir y. 
 
 
 
 
 
•  Función Sigmoide o función Logística. 
•  Cruza 0,5 en el origen. 
•  Asintótica a 0 y 1. 
•  z = wTx 
Introducción Intuitiva a la R. Logística 
1 
0 
z 
g(z) = 
1 
(1+e-Z) 
✓ 
1 


---

## Página 14

  
 
Introducción Intuitiva a la R. Logística 


---

## Página 15

  
 
Introducción Intuitiva a la R. Logística 


---

## Página 16

(Página sin texto reconocible)


---

## Página 17

•  En regresión lineal, usamos la hipótesis: hw(x) = (wTx) 
•  En clasificación, usamos la hipótesis: hw(x)= g((wTx)) 
•  Definimos g(z) donde z es un número real. 
•  z se estima por wTx 
•  g(z) = 1 / (1 + e-z)      Función Sigmoide o Logística 
•  La hipótesis a utilizar para la salida será: 
 
 
 
•  Nuevamente, nuestro problema es ajustar w según los datos. 
Fundamentación Teórica 
hw(x) =
1
1+e−wTx =
1
1+e−(w0x0+w1x1+...+wmxm )
1 
0 
z 
g(z) 


---

## Página 18

• 
Dada una entrada x, hw(x) nos entrega una estimación de probabilidad de 
que y = 1. 
 
• 
Es decir:  hw(x) = P( y = 1 | x ; w) 
 
• 
“la probabilidad de que y sea igual a 1, dado x parametrizado por w”. 
 
• 
En clasificación binaria: 
•  P( y = 1 | x ; w) + P( y = 0 | x ; w) = 1 
•  P( y = 0 | x ; w) = 1 - P( y = 1 | x ; w) 
Interpretación 
hw(x) =
1
1+e−wTx =
1
1+e−(w0x0+w1x1+...+wmxm ) = g(wTx)
1 
0 
z 
g(z) 


---

## Página 19

(Página sin texto reconocible)


---

## Página 20

 
 
 
 
 
Frontera de Decisión 
x1 
x2 
0 


---

## Página 21

 
 
 
 
 
Frontera de Decisión 
x1 
x2 
0 


---

## Página 22

 
 
 
 
 
Frontera de Decisión 
x1 
x2 
0 


---

## Página 23

 
 
 
 
 
Frontera de Decisión 
x1 
x2 
0 


---

## Página 24

• 
Permite entender mejor que se calcula y como se ve la función de 
hipótesis. 
• 
La salida y puede valer 0 ó 1, la función entrega una probabilidad. 
• 
Una forma de usar la salida de h es: 
•  hw(x) = P( y = 1 | x ; w) ≥ 0,5  entonces predecir y = 1. 
•  Si no, predecir y = 0. 
• 
¿cuál es la condición para hw(x) ≥ 0,5?  
•  g(z) ≥ 0,5 cuando z ≥ 0    =>    si z es positiva, g(z) ≥ 0 
•  Recordando que z = wTx    =>    Cuando  wTx ≥ 0   =>    hw(x) ≥ 0,5  
• 
Es decir que la hipótesis predice y = 1 cuando wTx ≥ 0 
• 
Por otro lado, la hipótesis predice y = 0 cuando wTx ≤ 0. 
  
Frontera de Decisión 
1 
0 
z 
g(z) 
0,5 
hw(x) =
1
1+e−wTx =
1
1+e−(w0x0+w1x1+...+wmxm ) = g(wTx) = g(z)


---

## Página 25

• 
Tenemos hw(x) = g(z) = g((wTx))  
                                        = g(w0x0 + w1x1 + w2x2) 
• 
Supongamos: 
•  w0 = -5  ;  w1= 1  ;   w2 = 1   
•  Es decir: wT = [-5, 1, 1] 
• 
Como z = (wTx) entonces: 
•  Predecimos y = 1 si z ≥ 0, entonces: 
       w0x0 + w1x1 + w2x2 ≥ 0 
           -5 +  1 x1 + 1 x2 ≥ 0 
Se puede reescribir como: 
                       (x1 + x2) ≥ 5 
• 
Se decir: si se cumple que (x1 + x2 ≥ 5) 
entonces podemos predecir y = 1 
• 
Llamaremos frontera de decisión (“decision 
boundary”) a los puntos donde x1 + x2 = 5 
 
Frontera de Decisión 
1 
0 
z 
g(z) 
0,5 
hw(x) = g(wTx) = g(z)
x1 
x2 
0 


---

## Página 26

• 
Tenemos hw(x) = g(z) = g((wTx))  
                                        = g(w0x0 + w1x1 + w2x2) 
• 
Supongamos: 
•  w0 = -5  ;  w1= 1  ;   w2 = 1   
•  Es decir: wT = [-5, 1, 1] 
• 
Como z = (wTx) entonces: 
•  Predecimos y = 1 si z ≥ 0, entonces: 
       w0x0 + w1x1 + w2x2 ≥ 0 
           -5 +  1 x1 + 1 x2 ≥ 0 
Se puede reescribir como: 
                       (x1 + x2) ≥ 5 
• 
Se decir: si se cumple que (x1 + x2 ≥ 5) 
entonces podemos predecir y = 1 
• 
Llamaremos frontera de decisión (“decision 
boundary”) a los puntos donde x1 + x2 = 5 
 
Frontera de Decisión 
1 
0 
z 
g(z) 
0,5 
hw(x) = g(wTx) = g(z)
x1 
x2 
0 
5
5


---

## Página 27

• 
Tenemos hw(x) = g(z) = g((wTx))  
                                        = g(w0x0 + w1x1 + w2x2) 
• 
Supongamos: 
•  w0 = -5  ;  w1= 1  ;   w2 = 1   
•  Es decir: wT = [-5, 1, 1] 
• 
Como z = (wTx) entonces: 
•  Predecimos y = 1 si z ≥ 0, entonces: 
       w0x0 + w1x1 + w2x2 ≥ 0 
           -5 +  1 x1 + 1 x2 ≥ 0 
Se puede reescribir como: 
                       (x1 + x2) ≥ 5 
• 
Se decir: si se cumple que (x1 + x2 ≥ 5) 
entonces podemos predecir y = 1 
• 
Llamaremos frontera de decisión (“decision 
boundary”) a los puntos donde x1 + x2 = 5 
 
Frontera de Decisión 
1 
0 
z 
g(z) 
0,5 
hw(x) = g(wTx) = g(z)
x1 
x2 
0 
5
5
y = 1 
y = 0 


---

## Página 28

(Página sin texto reconocible)


---

## Página 29

• 
Al igual que en regresión polinomial, se pueden 
agregar términos de mayor orden. 
• 
Supongamos hw(x) = g(z) 
                                    = g(w0 + w1x1 + w3x1
2 + w4x2
2) 
• 
Supongamos: 
• 
w0 = -5  ;  w1= 0; w2 = 0 ; w3 = 1 ; w4 = 1 
• 
Es decir: wT = [-5, 0, 0, 1, 1] 
• 
Como z = (wTx) entonces: 
• 
Predecimos y = 1 si z ≥ 0, entonces: 
       w0x0 + w3x1
2 + w4x2
2
 ≥ 0 
           -5 +  1 x1
2 + 1 x2
2 ≥ 0 
Se puede reescribir como: 
                       (x1
2 + x2
2) ≥ 5 
• 
Se decir: si se cumple que (x1
2 + x2
2 ≥ 5) entonces 
podemos predecir y = 1 
• 
Mediante términos de mayor orden polinomial, es 
posible construir fronteras de decisión mas 
complejas.  
Frontera de Decisión No Lineal 
1 
0 
z 
g(z) 
0,5 
hw(x) = g(wTx) = g(z)
x1 
x2 
5


---

## Página 30

• 
Al igual que en regresión polinomial, se pueden 
agregar términos de mayor orden. 
• 
Supongamos hw(x) = g(z) = g((wTx))  
                                    = g(w0 + w1x1 + w3x1
2 + w4x2
2) 
• 
Supongamos: 
• 
w0 = -5  ;  w1= 0; w2 = 0 ; w3 = 1 ; w4 = 1 
• 
Es decir: wT = [-5, 0, 0, 1, 1] 
• 
Como z = (wTx) entonces: 
• 
Predecimos y = 1 si z ≥ 0, entonces: 
       w0x0 + w3x1
2 + w4x2
2
 ≥ 0 
           -5 +  1 x1
2 + 1 x2
2 ≥ 0 
Se puede reescribir como: 
                       (x1
2 + x2
2) ≥ 5 
• 
Se decir: si se cumple que (x1
2 + x2
2 ≥ 5) entonces 
podemos predecir y = 1 
• 
Mediante términos de mayor orden polinomial, es 
posible construir fronteras de decisión mas 
complejas.  
Frontera de Decisión No Lineal 
1 
0 
z 
g(z) 
0,5 
hw(x) = g(wTx) = g(z)
x1 
x2 
y = 1 
y = 0 
5


---

## Página 31

(Página sin texto reconocible)


---

## Página 32

Se va a modelar el logit del evento con un modelo lineal: 
 
 
 
 
Despejando el odds: 
 
 
 
Despejando pi: 
Interpretación Probabilística 
ln
pi
1−pi
⎛
⎝
⎜
⎞
⎠
⎟= w0x0 + w1x1 + w2x2 +...+ wmxm =
wjx j
j=0
m
∑
= wTx
pi
1−pi
= ewTx
pi = P(yi=1| x;w) =
ewTx
1+ewTx =
1
1+e−wTx =
1
1+e−(w0x0+w1x1+...+wmxm )


---

## Página 33

(Página sin texto reconocible)


---

## Página 34

Modelo de Regresión Lineal: 
 
 
 
Función de Costo en Regresión Lineal: 
 
 
 
 
El problema del aprendizaje  (en regresión lineal) con este modelo puede 
plantearse básicamente como: 
 
                                                                                                 Ordinary Least Square 
 
Función de Costo (REPASO) 
y = w0x0 + w1x1 + w2x2 +...+ wmxm =
wjx j
j=0
m
∑
= wTx
J(w) = 1
2
y(i) −ˆy(i)
(
)
2
i=1
n
∑
argmin
w
1
2
y(i) −w0 −
wjx j
(i)
j=1
m
∑
⎛
⎝
⎜⎜
⎞
⎠
⎟⎟
2
i=1
n
∑
⎡
⎣
⎢
⎢
⎤
⎦
⎥
⎥


---

## Página 35

•  Hipótesis: 
•  Se busca ajustar los parámetros wj. 
•  Para ello, se debe definir un problema de optimización. 
•  Entrenaremos con un conjunto de n ejemplos. 
(x(1), y(1)), (x(2), y(2)), …, (x(n), y(n)) 
•  Cada ejemplo tiene un vector de m+1 columnas. 
x = (x0, x1, … , xm)        donde x0 = 1 
•  La salida de la variable y pertenece a {0, 1} 
Función de Costo en Regresión Logística 
hw(x) =
1
1+e−wTx =
1
1+e−(w0x0+w1x1+...+wmxm )


---

## Página 36

• 
En regresión lineal, la función de loss es: 
• 
Podemos definir Cost(hw(x(i)), y(i)) = ½(hw(x(i)) - y(i))2 
• 
Entonces queda: 
• 
Se trata de una función no convexa cuando usamos la hipótesis de la 
función Sigmoide (pues no es lineal). 
•  Tiene muchos óptimos locales. 
•  El gradiente descendente podría no encontrar el mínimo global. 
• 
Se desea una función convexa que facilite convergencia a un mín. global. 
Función de Costo en Regresión Logística 
J(w) = 1
n
1
2 hw(x(i))−y(i)
(
)
2
i=1
n
∑
J(w) = 1
n
Cost hw(x(i)), y(i)
(
)
i=1
n
∑


---

## Página 37

• 
Costo: 
• 
Para solucionarlo se utiliza una función Cost() que sea convexa. 
Función de Costo en Regresión Logística 
J(w) = 1
n
Cost hw(x(i)), y(i)
(
)
i=1
n
∑
Cost(hw(x), y) = 
  -log( hw(x) )          si y = 1 
  -log( 1 - hw(x) )     si y = 0 


---

## Página 38

• 
Costo: 
• 
Para solucionarlo se utiliza una función Cost() que sea convexa. 
Función de Costo en Regresión Logística 
J(w) = 1
n
Cost hw(x(i)), y(i)
(
)
i=1
n
∑
Cost(hw(x), y) = 
  -log( hw(x) )          si y = 1 
  -log( 1 - hw(x) )     si y = 0 
•  Cuando hw(x) = 1, entonces el costo es 0. 
•  Si la predicción empieza a ser mala, el costo penaliza 
cada vez mas. 
•  Propiedades: 
•  Si y = 1 y hw(x) = 1   =>   el costo es 0. 
•  Si hw(x) se acerca a 0   =>  el costo tiende a infinito. 
•  En definitiva: si acierta el costo es 0, pero si hw(x) = 0 (la 
predicción P(y=1|x;w) = 0 entonces penaliza 
gravemente. 


---

## Página 39

• 
Costo: 
• 
Para solucionarlo se utiliza una función Cost() que sea convexa. 
Función de Costo en Regresión Logística 
J(w) = 1
n
Cost hw(x(i)), y(i)
(
)
i=1
n
∑
Cost(hw(x), y) = 
  -log( hw(x) )          si y = 1 
  -log( 1 - hw(x) )     si y = 0 
•  Cuando hw(x) = 0, entonces el costo es 0. 
•  Si la predicción empieza a ser mala, el costo penaliza 
cada vez mas. 
•  Propiedades: 
•  Si y = 0 y hw(x) = 0   =>   el costo es 0. 
•  Si hw(x) se acerca a 1   =>  el costo tiende a infinito. 
•  En definitiva: si acierta el costo es 0, pero si hw(x) = 1 (la 
predicción P(y=1|x;w) = 1 entonces penaliza 
gravemente. 


---

## Página 40

• 
Costo: 
• 
Para solucionarlo se utiliza una función Cost() que sea convexa. 
• 
A los efectos de simplificar la función de costo, juntaremos todo: 
Cost(hw(x), y) = -y log( hw(x) ) – (1-y) log( 1 - hw(x) )  
• 
Loss Function: 
Función de Costo en Regresión Logística 
J(w) = 1
n
Cost hw(x(i)), y(i)
(
)
i=1
n
∑
Cost(hw(x), y) = 
  -log( hw(x) )          si y = 1 
  -log( 1 - hw(x) )     si y = 0 
J(w) = −1
n
y(i) log(hw(x(i)))+(1−y(i))log(1−hw(x(i)))
i=1
n
∑
⎡
⎣
⎢
⎤
⎦
⎥


---

## Página 41

• 
Loss Function: 
• 
Existen muchas posibilidades, pero esta función de costo: 
•  Es una función convexa (facilitará encontrar el óptimo global). 
•  Puede ser derivada desde la estadística utilizando el principio de estimación de 
máxima verosimilitud (maximum likelihood estimation). 
•  La verosimilitud es una función que mide lo verosímiles que son unos 
parámetros para un modelo estadístico a partir de un conjunto de 
observaciones. 
•  Esto significa que hay un supuesto Gaussiano relacionado a la distribución 
de los valores en las xj.
  
  
Función de Costo en Regresión Logística 
J(w) = −1
n
y(i) log(hw(x(i)))+(1−y(i))log(1−hw(x(i)))
i=1
n
∑
⎡
⎣
⎢
⎤
⎦
⎥


---

## Página 42

(Página sin texto reconocible)


---

## Página 43

• 
Loss Function: 
• 
Regularización L2: 
• 
Regularización L1: 
Término de Regularización 
J(w) = −1
n
y(i) log(hw(x(i)))+(1−y(i))log(1−hw(x(i)))
i=1
n
∑
⎡
⎣
⎢
⎤
⎦
⎥
J(w) = −1
n
y(i) log(hw(x(i)))+(1−y(i))log(1−hw(x(i)))
i=1
n
∑
⎡
⎣
⎢
⎤
⎦
⎥+ λ
2n
(wj)2
j=1
m
∑
J(w) = −1
n
y(i) log(hw(x(i)))+(1−y(i))log(1−hw(x(i)))
i=1
n
∑
⎡
⎣
⎢
⎤
⎦
⎥+ λ
n
wj
j=1
m
∑


---

## Página 44

  
 
¿Preguntas? 


---
