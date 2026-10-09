# CD_04_02_03_ArbolesDeDecision

## Página 1

UNIDAD 4. CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Mgtr. Ing. Mariano Mar;n Gualpa 
Ciencia de Datos 


---

## Página 2

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
    TEMARIO: 
•  Introducción 
•  Deﬁnición 
•  Aplicaciones 
•  Caso de Estudio 
•  Algoritmo 
•  Algoritmo ID3 
•  Sobreajuste 
•  Familias de Algoritmos 


---

## Página 3

INTRODUCCIÓN 


---

## Página 4

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
INTRODUCCIÓN: CLASIFICACIÓN 
“Deﬁnimos como clasiﬁcación el proceso de encontrar un 
conjunto de modelos (o funciones) que describen y disNnguen 
clases de datos o conceptos, con el propósito de hacer posible 
uNlizarlo para predecir la clase de objeto para el cual su 
eNqueta de clase es desconocida. El modelo derivado esta 
basado en el análisis de un conjunto de datos de 
entrenamiento.” [Jiawei Han y Micheline Kamber] 
 
 


---

## Página 5

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Árboles de Decisión: Deﬁnición 
“Un árbol de decisión es un grafo con estructura de árbol, donde cada nodo 
denota un test sobre un valor de atributo, cada rama representa un 
resultado del test, y cada hoja representa clases o distribuciones de clases. 
Los árboles de decisión pueden ser fácilmente converNdos en reglas de 
clasiﬁcación.” [Han Kamber] 


---

## Página 6

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Árboles de Decisión: Deﬁnición 
“Un árbol de decisión es un grafo con estructura de árbol, donde cada nodo 
denota un test sobre un valor de atributo, cada rama representa un 
resultado del test, y cada hoja representa clases o distribuciones de clases. 
Los árboles de decisión pueden ser fácilmente converNdos en reglas de 
clasiﬁcación.” [Han Kamber] 
•  Hipótesis    f: X->Y 
•  Cada nodo interno evalúa un 
atributo xi. 
•  Una bifurcación por cada posible 
valor de atributo xi=v 
•  Se asigna a cada hoja una clase y. 
•  Para clasiﬁcar la entrada x: 
recorrer el árbol desde la raíz, 
hasta la hoja correspondiente. 


---

## Página 7

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Árbol de Decisión: Aplicaciones 
Se  recomienda el uso de árboles de decisión cuando se quiere: 
• 
Aplicar un esquema de segmentación a un conjunto de datos que 
reﬂejan un grupo de potenciales clientes. 
• 
IdenNﬁcar posibles relaciones interacNvas entre variables en una 
forma que  le permita entender como el cambio de una variable 
puede afectar a otra. 
• 
Proveer una representación visual de las relaciones entre 
variables en la forma de un árbol, que es una forma 
relaNvamente fácil de entender la naturaleza de los datos que 
residen en su base de datos. 
• 
Simpliﬁcar la mezcla de atributos y categorías, manteniéndose 
solo con las necesarias para hacer predicciones. 
• 
Explorar datos para idenNﬁcar variables importantes en 
conjuntos de datos que pueden eventualmente ser usados como 
objeNvos.  
 
 


---

## Página 8

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Árbol de Decisión: Caso de Estudio 
“Patrones de morosidad para un producto crediLcio usando la 
técnica de árbol de clasiﬁcación CART” [Salinas, 2005] 
Variables: mora, edad, sexo, estado civil, carga familiar (personas 
dependientes), si posee teléfono parNcular, si posee teléfono laboral, si 
Nene “autovaluo”, si es aval de otro cliente, anNgüedad laboral, si Nene 
renta ﬁja o variable y la ubicación geográﬁca donde se aprobó el crédito. 
 
 
 
UNlizando el algoritmo CART se 
detectaron patrones diferentes para los 
morosos y los no morosos, lo que ha   
permiNdo  la  automaNzación  del 
proceso de crédito. Se obtuvo un 
93,75% de clasiﬁcación correcta para los 
morosos y un 86,42% de clasiﬁcación 
correcta para los no morosos.  
 


---

## Página 9

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Árbol de Decisión: Algoritmo 
“Un algoritmo de árbol de decisión analiza los datos y crea una 
serie de ramiﬁcaciones hasta que no puede hacer alguna 
relevante. El resultado ﬁnal es una estructura de árbol binario 
donde los cortes en las ramas pueden ser seguidos a lo largo de 
un criterio especíﬁco para encontrar el resultado mas 
deseado.” [Seidman] 
 


---

## Página 10

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Teoría de Información: IncerLdumbre 
 
CanLdad de Información 
Supongamos este conjunto de cartas: 
 
 
 
Haremos extracciones sin reemplazo, asumiendo igual probabilidad 
de extracción para cada carta.  
Se deﬁnen los sucesos: 
 A = {sacar una carta negra (trébol)}  donde P(A) = 1/10 
 B = {sacar una carta roja (corazón)}  donde P(B) = 9/10 
  
 
 
 


---

## Página 11

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Teoría de Información: IncerLdumbre 
 
CanLdad de Información 
Supongamos este conjunto de cartas: 
 
 
 
Haremos extracciones sin reemplazo, asumiendo igual probabilidad 
de extracción para cada carta.  
Se deﬁnen los sucesos: 
 A = {sacar una carta negra (trébol)}  donde P(A) = 1/10 
 B = {sacar una carta roja (corazón)}     donde P(B) = 9/10 
 
Al realizar la primer extracción, resulta: 
 
¿Cuánta información aporta este suceso?  


---

## Página 12

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Teoría de Información: IncerLdumbre 
 
CanLdad de Información 
Supongamos este conjunto de cartas: 
 
 
 
 
 A = {sacar una carta negra (trébol)} 
 B = {sacar una carta roja (corazón)} 
 
•  Al extraer una carta roja, este suceso B proporciona poca 
información, pues la incerNdumbre en la próxima extracción 
varía muy poco: 
 P(A|B) = 1/9   y    P(B|B) = 8/9 
•  Si la carta hubiese sido negra, este suceso A proporciona mucha 
información, pues la incerNdumbre sobre la próxima extracción 
desaparece: 
 P(A|A) = 0    y     P(B|A) = 1 
 


---

## Página 13

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Teoría de Información: IncerLdumbre 
 
La Teoría de la información [Shannon, 1948] permite cuanNﬁcar la 
canNdad de información y la entropía.  
Supongamos este conjunto de cartas: 
 
 
 
Hay una de entre cuatro posibilidades de sacar una carta negra 
(trébol).  
 
Para el evento, se Nene una variable aleatoria con un grado de 
indeterminación k=4 (hay cuatro estados posibles), con una 
probabilidad p = 1/k = 0,25.  
 
 


---

## Página 14

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Teoría de Información: IncerLdumbre 
 
CanLdad de Información 
Supongamos este conjunto de cartas: 
 
 
 
Hay una de entre cuatro posibilidades de sacar una carta negra (trébol).  
Para el evento, se Nene una variable aleatoria con un grado de 
indeterminación k=4 (hay cuatro estados posibles), con una probabilidad 
p = 1/k = 0,25.  
Se deﬁne la canNdad de información ci: 
 
ci = log2(k) = log2 [1 / (1/k)] = log2(1 / p) = log2(1) – log2(p) = - log2(p) 
 
Entonces: 
       c1 = log2(4) = - log2(0,25) = 2 bits 
 
 


---

## Página 15

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Teoría de Información: IncerLdumbre 
 
Entropía 
CuanNﬁca el nivel de desorganización o incerNdumbre asociado a una variable 
aleatoria. 
Se la deﬁne como el valor esperado de la canNdad de la información aportada 
por cada estado: 
 
H(X) = - p(x1) log2 p(x1) - p(x2) log2 p(x2) … - p(xk) log2 p(xk) 
 
H(X) = - Σi p(xi) log2 p(xi) 
 
• 
Siempre está acotada en H(X) ≤ - log2(k)  
• 
Es máxima cuando p1 = p2 = …  = pk = 1/k 
• 
Es 0 si algún pj = 1 y los demás 0 (solo uno de los k estados puede aparecer). 
 
 
Supongamos este conjunto de cartas: 
En el ejemplo: 
 c1 = - log2(p1) = - log2(0,25) = 2 bits 
 c2 = - log2(p2) = - log2(0,75) = 0,415 bits 
 H(X) = - 0,25 * log2(0,25) -  0,75 * log2(0,75) = 0,811 


---

## Página 16

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Teoría de Información: IncerLdumbre 
 
Entropía 
•  Ante resultados ciertos (p = 0 ó p = 1) la entropía es 0. 
•  Ante resultados inciertos, la entropía crece. 
•  Ante resultados igualmente probables, la entropía es máxima. 
 
Lanzamiento de una moneda: 
 
 H(X) = - Σi p(xi) log2 p(xi) 
 
H(X) = - 0,50 * log2(0,50) -  0,50 * log2(0,50) = 1 
 
 
 


---

## Página 17

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Teoría de Información: IncerLdumbre 
 
CanLdad de Información 
 
¿A que juego preﬁeres jugar? 
¿Adivinar el color de la carta o adivinar el lado de la moneda? 
 
 
 
 
 


---

## Página 18

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Teoría de Información: IncerLdumbre 
 
X1: 
COLOR 
X2: PAR 
O IMPAR 
Y 
R: ROJO 
P: PAR 
P: PERDIO 
R: ROJO 
I: IMPAR 
P: PERDIO 
R: ROJO 
P: PAR 
P: PERDIO 
R: ROJO 
I: IMPAR 
P: PERDIO 
N: NEGRO 
P: PAR 
P: PERDIO 
N: NEGRO 
I: IMPAR 
G: GANO 
Entropía 
Se propone un juego: 
Dadas las seis cartas del conjunto, Pipo 
debe reNrar una sola carta. Si la misma 
es un AS DE TRÉBOL, gana.  
Sin ver la carta, debes adivinar si ganó 
o perdió. 
 
 
 
 


---

## Página 19

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Teoría de Información: IncerLdumbre 
 
X1: 
COLOR 
X2: PAR 
O IMPAR 
Y 
R: ROJO 
P: PAR 
P: PERDIO 
R: ROJO 
I: IMPAR 
P: PERDIO 
R: ROJO 
P: PAR 
P: PERDIO 
R: ROJO 
I: IMPAR 
P: PERDIO 
N: NEGRO 
P: PAR 
P: PERDIO 
N: NEGRO 
I: IMPAR 
G: GANO 
Entropía 
Se propone un juego: 
Dadas las seis cartas del conjunto, Pipo 
debe reNrar una sola carta. Si la misma 
es un AS DE TRÉBOL, gana.  
Sin ver la carta, debes adivinar si ganó 
o perdió. 
 
P(Y = P) = 5/6 
P(Y = G) = 1/6 
 
H(Y) = - 5/6 log2(5/6) - 1/6 log2(1/6) = 0,65 
 
 
 


---

## Página 20

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Teoría de Información: IncerLdumbre 
 
Entropía Condicional 
El conocimiento de determinada información, podría afectar el nivel de 
incerNdumbre que tenemos respeto al resultado de un evento.  
 
Se deﬁne la entropía condicional de una variable aleatoria Y, condicionada por 
una variable aleatoria X como: 
 
 
 
 
 
 
 


---

## Página 21

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Teoría de Información: IncerLdumbre 
 
X1: 
COLOR 
X2: PAR 
O IMPAR 
Y 
R: ROJO 
P: PAR 
P: PERDIO 
R: ROJO 
I: IMPAR 
P: PERDIO 
R: ROJO 
P: PAR 
P: PERDIO 
R: ROJO 
I: IMPAR 
P: PERDIO 
N: NEGRO 
P: PAR 
P: PERDIO 
N: NEGRO 
I: IMPAR 
G: GANO 
Entropía Condicional 
 
En nuestro Ejemplo, dado X1: 
 
 
P(X1 = R) = 4/6 
P(X1 = N) = 2/6 
 
 
 
H(Y | X1) = - 4/6 (1 log2 1 + 0 log2 0 )  
                         - 2/6 ( ½ log2 ½ + ½ log2 ½) = 2/6 
 
 
 
Y = P 
Y = G 
X1 = R 
4 
0 
X1 = N 
1 
1 


---

## Página 22

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Teoría de Información: IncerLdumbre 
 
X1: 
COLOR 
X2: PAR 
O IMPAR 
Y 
R: ROJO 
P: PAR 
P: PERDIO 
R: ROJO 
I: IMPAR 
P: PERDIO 
R: ROJO 
P: PAR 
P: PERDIO 
R: ROJO 
I: IMPAR 
P: PERDIO 
N: NEGRO 
P: PAR 
P: PERDIO 
N: NEGRO 
I: IMPAR 
G: GANO 
Ganancia de Información 
Es el decremento en la entropía (es decir en la 
incerNdumbre) dada determinada información. 
    
IG(X) = H(Y) – H(Y | X) 
 
Si IG(X) > 0    =>   Se ha ganado información 
 
En nuestro Ejemplo, dado X1: 
 
H(Y) = - 5/6 log2(5/6) - 1/6 log2(1/6) = 0,65 
 
H(Y | X1) = - 4/6 (1 log2 1 + 0 log2 0 )  
                         - 2/6 ( ½ log2 ½ + ½ log2 ½) = 2/6 
 
IG(X1) = H(Y) – H(Y | X1) = 0,65 – 0,33 = 0,32 
 
 


---

## Página 23

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Índice de Gini (Impureza) 
El índice de Gini mide la impureza de un nodo. Se calcula como: 
 
 
En el caso de clasiﬁcación binaria, la fórmula sería: 
 
Por ejemplo: Si tenemos en un nodo 5 muestras, 3 de la clase 0 
y 2 de la clase 1, el índice de Gini será: 
 
Gini = 1 – 0.62 – 0.42 = 0.48 
 
El máximo se da cuando todas las clases Nenen igual 
probabilidad. Ej: 
Gini = 1 – 0,252 – 0,252 – 0,252 – 0,252 = 0,75 


---

## Página 24

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Árbol de Decisión: Algoritmo 
En forma general, el algoritmo puede resumirse como: 
 
•  Inicial desde un árbol de decisión vacío. 
•  Crear ramas sobre el mejor atributo (“feature”). Para 
hacerlo, debe idenNﬁcarlo, usando por ejemplo la ganancia 
de información con el atributo seleccionado: 
arg maxi IG(Xi) = arg maxi H(Y) – H(Y|Xi) 
•  Iterar hasta un criterio de corte. 
 


---

## Página 25

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Árbol de Decisión: Algoritmo ID3 
 
 
 
 


---

## Página 26

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Árbol de Decisión: Algoritmo ID3 
Árbol de Decisión: Algoritmo ID3 
 
 
 
 


---

## Página 27

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Árbol de Decisión: Algoritmo ID3 
Árbol de Decisión: Algoritmo ID3 
 
 
 
 


---

## Página 28

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Árbol de Decisión: Algoritmo ID3 
Árbol de Decisión: Algoritmo ID3 
 
 
 
 


---

## Página 29

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Árbol de Decisión: Algoritmo ID3 
Árbol de Decisión: Algoritmo ID3 
 
 
 
 
Cielo 
Humedad 
+ 
Viento 
- 
+ 
- 
+
Sol 
Nublado 
Lluvia 
Alta 
Normal 
Fuerte 
Débil 


---

## Página 30

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Árbol de Decisión: Algoritmo ID3 
Ejercicio: Suponga que solo Nene los atributos cielo y humedad. ¿cómo 
queda el árbol? 
 
 
 
 


---

## Página 31

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Árboles de Decisión: Sobreajuste (OverﬁLng) 
•  Los árboles de decisión estándar no Nenen sesgo 
(bias) de aprendizaje. 
• 
El error del conjunto de entrenamiento siempre es 0 
(sin un criterio de corte). 
• 
Mucha varianza. 
• 
Se debe introducir algún sesgo hacia árboles mas 
simples. 
•  Existen diferentes estrategias para simpliﬁcar 
árboles. 
• 
Establecer el nivel de profundidad. 
• 
Mínimo número de observaciones por hoja. 
•  Random Forests. 


---

## Página 32

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Árbol de Decisión: Familias de Algoritmos 
•  Familia CART: CART, Tree(S), etc. Su propósito inicial es la 
predicción estadísNca. Se basan en la realización de 
divisiones binarias únicamente, recurriendo a la validación 
cruzada y a la poda con el ﬁn de determinar el tamaño 
correcto del árbol. Acepta como variable dependiente una 
del Npo cuanLtaLva o nominal. Las variables predictoras 
pueden ser nominales u ordinales, aunque las úlNmas 
versiones también admiten variables conNnuas. 
 
•  Familia CLS: CLS, ID3, C4.5, C5.0, etc. Detectan relaciones 
estadísNcas complejas, siendo el número de ramas que 
puede originar un número entre entre dos y el número de 
categorías del predictor. Para determinar el tamaño del 
árbol uNliza tests de signiﬁcación estadísNca (con ajustes de 
mulNplicidad en las úlNmas versiones).  
 
 


---

## Página 33

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Árbol de Decisión: Familias de Algoritmos 
•  Métodos de Lpo discriminante: FACT y QUEST. Su propósito 
inicial es solucionar problemas de los métodos exhausNvos. En 
concreto, tratan de eliminar el denominado sesgo de selección 
de la variable, que presentan métodos como CART y que consiste 
en la tendencia a seleccionar en primer lugar las variables con más 
categorías. QUEST logra eliminar este sesgo, sea la VD nominal u 
ordinal. En primer caso, diseñados para trabajar con variables 
dependientes categóricas como conLnuas. FACT divide a la 
población en tantos grupos como categorías Nene la variable 
seleccionada, QUEST establece divisiones binarias. 
 
•  Combinaciones lineales: OC1, Árboles SE, etc. Su propósito inicial 
es detectar relaciones lineales combinadas con el aprendizaje de 
conceptos. El número de ramas varía entre dos y el número de 
categorías del predictor. 
 
 


---

## Página 34

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
Árbol de Decisión: Familias de Algoritmos 
•  Modelos Híbridos: IND, Knowledge Seeker, etc. Su propósito 
inicial es combinar métodos de otras familias. IND combina 
el CART y C4.5, así como métodos bayesianos y de 
codiﬁcación mínima. Knowledge Seeker combina CHAID y el 
ID3 con un novedoso ajuste de mulNplicidad. 
 
Se aclara además, que “los tres procedimientos arborescentes 
que actualmente gozan de una mayor aceptación tanto en los 
ámbitos teórico como aplicado son: los árboles CHAID (Kass, 
1980), CART (Breiman es al., 1984) y QUEST (Loh y Shih, 1997)”. 
 
 
 


---

## Página 35

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
    Árboles de Decisión 
¿Preguntas? 
 


---

## Página 36

UNIDAD 4: CLASIFICACIÓN. ÁRBOLES DE DECISIÓN 
    Árboles de Decisión 
Muchas gracias. 
 


---
