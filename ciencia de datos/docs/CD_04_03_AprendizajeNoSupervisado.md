# CD_04_03_AprendizajeNoSupervisado

## Página 1

1
Unidad 4: Aprendizaje No Supervisado
Temas: Reducción de Dimensionalidad, Clustering
Ciencia de Datos
Mgtr. Ing. Mariano Martín Gualpa (mgualpa@frc.utn.edu.ar)


---

## Página 2

2
•
Aprendizaje No Supervisado.
•
Reducción de Dimensionalidad.
•
Análisis de Componentes Principales (PCA).
•
Agrupamiento.
•
Agrupamiento Jerárquico.
•
Agrupamiento No Jerárquico.
•
Agrupamiento: Problemas Prácticos.
•
Validación de los Grupos.
•
Otras Consideraciones.
•
Interpretación de Resultados.
Temario de la Clase


---

## Página 3

3


---

## Página 4

4
Tipos de Aprendizaje:
• Aprendizaje Supervisado.
• Aprendizaje No Supervisado.
• Aprendizaje Semi-Supervisado.
• Aprendizaje por Refuerzo.
Aprendizaje No Supervisado


---

## Página 5

5
Objetivos:
• Reducción de Dimensionalidad
• Agrupamiento (Clustering)
• Generación de Jerarquías
• Sistemas de Recomendación
• Reglas de Asociación
• Visualización
• Detección de Anomalías.
Aprendizaje No Supervisado


---

## Página 6

6


---

## Página 7

7
Se han estudiado diferentes formas de controlar la varianza:
•
Usando un subconjunto de las variables originales.
•
Reduciendo sus coeficientes a cero.
Ahora
estudiaremos
otra
aproximación,
a
partir
de
transformar
los
predictores.
En definitiva:
A partir de los predictores originales X1, X2,…, Xp , se busca una
representación basada en los predictores Z1, Z2, …, ZM donde M < p
Reducción de Dimensionalidad


---

## Página 8

8
En los modelos estudiados, utilizamos los predictores originales X1, X2,…, Xp.
Sean Z1, Z2, …, ZM representantes de M < p combinaciones lineales de nuestros p 
predictores originales. Es decir:
Para algunas constantes Φ1m, Φ2m …, Φpm, m =1,…,M. Usando mínimos cuadrados, 
podemos ajustar el modelo de regresión lineal: 
Si las constantes son elegidas sabiamente, a menudo pueden mejorar la 
regresión de mínimos cuadrados.   
donde
Reducción de Dimensionalidad


---

## Página 9

9
En los modelos estudiados, utilizamos los predictores originales X1, X2,…, Xp.
Sean Z1, Z2, …, ZM representantes de M < p combinaciones lineales de nuestros p 
predictores originales. Es decir:
Para algunas constantes Φ1m, Φ2m …, Φpm, m =1,…,M. Usando mínimos cuadrados, 
podemos ajustar el modelo de regresión lineal: 
Si las constantes son elegidas sabiamente, a menudo pueden mejorar la 
regresión de mínimos cuadrados.   
donde
Reducción de Dimensionalidad


---

## Página 10

10
donde
•
Puede ser tratado como un caso especial del modelo de regresión lineal original 
ya estudiado. 
•
La reducción de dimensión sirve para restringir los coeficientes estimados β.
•
Esta restricción sobre la forma de los coeficientes, tiene el potencial de sesgar las 
estimaciones.
•
Sin embargo, cuando p es grande en relación a n, seleccionar un valor de M<<p 
puede reducir significativamente la varianza de los coeficientes ajustados.
•
Si M = p, y todos los Zm son linealmente independientes, no hay reducción y el 
resultado es equivalente a usar los p predictores originales.
p dims
M dims
Reducción de Dimensionalidad


---

## Página 11

11
Todos los métodos de reducción de dimensionalidad
trabajan en dos pasos:
1. Obtener los predictores transformados Z1, Z2…ZM.
2. Ajustar el modelo con esos M predictores.
No obstante, existen diferentes formas de obtener 
dichos predictores.
Reducción de Dimensionalidad


---

## Página 12

12
Análisis de Componentes Principales (PCA)


---

## Página 13

13
Análisis de Componentes Principales (PCA)


---

## Página 14

14
Análisis de Componentes Principales (PCA)


---

## Página 15

15
Análisis de Componentes Principales (PCA)


---

## Página 16

16
Análisis de Componentes Principales (PCA)


---

## Página 17

17
La primer componente principal de un conjunto X1, X2,…,Xp es la combinación lineal 
normalizada (normalized linear combination):
que tiene la varianza más grande. Por normalizada nos referimos a:
Esta restricción normaliza el vector de loadings, para que siempre tenga módulo 1, 
pues solo nos interesa su dirección (genera una esfera de un espacio multidim.).
Puede demostrarse que sin esta restricción, los loadings crecerían indefinidamente al 
maximizar la varianza.
Análisis de Componentes Principales (PCA)


---

## Página 18

18
La primer componente principal de un conjunto X1, X2,…,Xp es la combinación lineal 
normalizada (normalized linear combination):
que tiene la varianza más grande. Por normalizada nos referimos a:
Los elementos Φ11,…,Φp1 son llamados “loadings” de la primer componente 
principal, formando el “loading vector” Φ1 = (Φ11, Φ21,…,Φp1)T.
La restricción de que sumen 1 ya que de establecerlos grandes en valor absoluto 
podrían resultar en una varianza arbitrariamente grande.
Como solo estamos interesados en la varianza, asumimos que cada una de las 
variables en X está centrada en la media cero.
Cada valor de la combinación lineal se calcula como: 
Que tiene la mayor varianza de las muestras, sujetas a la restricción
Análisis de Componentes Principales (PCA)


---

## Página 19

19
La primer componente principal de un conjunto X1, X2,…,Xp es la combinación lineal 
normalizada (normalized linear combination):
Que tiene la varianza más grande. Por normalizada nos referimos a:
En otras palabras, el vector de loadings de la primer componente principal resuelve el 
problema de optimización:
Que podemos expresar también  como:
Análisis de Componentes Principales (PCA)
𝑚𝑎𝑥𝑖𝑚𝑖𝑧𝑒фభ 𝑉𝑎𝑟𝑋фଵ
  𝑠𝑢𝑏𝑗𝑒𝑐𝑡 𝑡𝑜 фଵ
= 1
𝑍ଵ


---

## Página 20

20
Partiendo del modelo:
Puede demostrarse que:
Donde S es la matriz de covarianza muestral centrada de X.
En definitiva, el problema es:
Cuando se resuelve por multiplicadores de Langrange: 
Derivando respecto a ф resulta el mismo problema que define cual es el autovector. 
Entonces:
•
Los vectores фi que maximizan la varianza son autovectores de la matriz de 
covarianza S.
•
Los autovalores λi indican cuanta varianza explica cada componente.
•
Como S es simétrica, entonces sus autovectores son ortogonales.
Análisis de Componentes Principales (PCA)
𝑚𝑎𝑥𝑖𝑚𝑖𝑧𝑒фభ 𝑉𝑎𝑟𝑋фଵ
  𝑠𝑢𝑏𝑗𝑒𝑐𝑡 𝑡𝑜 фଵ
ଶ
= 1
𝑉𝑎𝑟𝑋фଵ= фଵ்𝑆 фଵ
𝑚𝑎𝑥𝑖𝑚𝑖𝑧𝑒фభ фଵ்𝑆 фଵ  𝑠𝑢𝑏𝑗𝑒𝑐𝑡 𝑡𝑜 фଵ
ଶ
= 1
L ф, λ = ф்𝑆 ф − λ ф்ф −1
∇фL = 2 𝑆 ф −2 λ ф = 0     ⇒  𝑆 ф = λ ф


---

## Página 21

21
Una componente principal puede ser definida como una combinación lineal de las 
observaciones, óptimamente ponderadas. 
Propiedades:
•
Los componentes principales son combinaciones lineales de las variables 
originales.
•
El vector de pesos en esta combinación es el autovector encontrado que a su vez 
satisface el principio de mínimos cuadrados.
•
Los componentes principales son ortogonales.
•
La variación de las Componentes Principales disminuye a medida que pasamos 
de la 1ra a la última (es decir, disminuye su importancia).
Las componentes principales menos importantes son a veces útiles en regresión, 
detección de outliers, etc. Eliminarlas, puede ayudar a eliminar ruido.
Análisis de Componentes Principales (PCA)


---

## Página 22

22
¿Cuanto de la varianza en los datos no está contenida en las primeras 
componentes principales?
Se busca conocer la proporción de la varianza explicada (PVE) de cada 
componente principal.
Análisis de Componentes Principales (PCA)


---

## Página 23

23
El total de la varianza del dataset (asumiendo variables centradas con media 0) se 
define como:
La varianza explicada por la componente principal m-ésima:
Entonces, la proporción de varianza explicada (“proportion of variance
explained”, PVE) es:
Análisis de Componentes Principales (PCA)


---

## Página 24

24


---

## Página 25

25
Objetivos:
• Dados ejemplos sin etiquetar, agruparlos siguiendo algún 
criterio predefinido:
• Aprendizaje Paramétrico: parámetros asumidos, por ejemplo que los 
datos siguen una función de densidad de probabilidad específica.
• Aprendizaje No Paramétrico: alguna medida de distancia.
Agrupamiento (Clustering)


---

## Página 26

26
Los algoritmos de clustering no pueden diferenciar entre variables relevantes
e irrelevantes. Es importante elegir cuidadosamente las variables basado en
el algoritmo que iniciará la identificación de patrones/grupos. Es muy
importante porque los clusters pueden ser muy dependientes de las
variables incluidas.
Un buen algoritmo de clustering puede ser evaluado en base a dos objetivos 
primarios:
•
Alta similaridad dentro de cada grupo (intra-class).
•
Baja similaridad entre grupos (inter-class).
Agrupamiento (Clustering)


---

## Página 27

27
Elementos críticos:
• ¿cuántos grupos tiene el conjunto?
• ¿cómo se determina el grupo al que pertenece una instancia?
Agrupamiento (Clustering)


---

## Página 28

28
C
Xn
…
Xj
…
X1
C(1)
x1n
…
x1j
…
x11
(x(1),C(1))
1
…
…
…
…
…
…
…
C(i)
xin
…
xij
…
xi1
(x(i),C(i))
i
…
…
…
…
…
…
…
C(N)
xNn
…
xNj
…
xN1
(x(N),C(N))
N
???
xN+1,n
…
xN+1,j
…
xN+1,1
X(N+1)
N + 1
Agrupamiento (Clustering)
En agrupamiento, esta 
fase es opcional.
En agrupamiento, no 
tenemos etiquetas.


---

## Página 29

29
•
Encontrar
agrupamientos
naturales
en
un
conjunto
de
datos
no
etiquetados.
•
Homogeneidad dentro de las clases y heterogeneidad entre las distintas
clases.
•
A veces, se busca predecir la etiqueta de un ejemplo nuevo, con los
grupos ya definidos.
Agrupamiento (Clustering)
C
Xn
…
Xj
…
X1
C(1)
x1n
…
x1j
…
x11
(x(1),C(1))
1
…
…
…
…
…
…
…
C(i)
xin
…
xij
…
xi1
(x(i),C(i))
i
…
…
…
…
…
…
…
C(N)
xNn
…
xNj
…
xN1
(x(N),C(N))
N
???
xN+1,n
…
xN+1,j
…
xN+1,1
X(N+1)
N + 1


---

## Página 30

30
Ejemplos:
Marketing: diferentes grupos de clientes.
Seguros: identificar carácterísticas de los grupos con alto costo 
promedio.
Planeamiento Gubernamental: identificar grupos de familias 
para esquemas sociales, en base a atributos como tamaño, 
ingresos, etc. 
Taxonomías: los biólogos usan clustering para crear árboles de 
taxonomías de grupos y subgrupos de especies similares.
Agrupamiento (Clustering)


---

## Página 31

31
¿qué consideramos un grupo? 
es una definición que puede ser ambigua
Agrupamiento (Clustering)
k = 1


---

## Página 32

32
¿qué consideramos un grupo? 
es una definición que puede ser ambigua
Agrupamiento (Clustering)
k = 1
k = 2


---

## Página 33

33
¿qué consideramos un grupo? 
es una definición que puede ser ambigua
Agrupamiento (Clustering)
k = 1
k = 2
k = 4


---

## Página 34

34
¿qué consideramos un grupo? 
es una definición que puede ser ambigua
Agrupamiento (Clustering)
k = 1
k = 2
k = 4
k = 6


---

## Página 35

35
Tipos de Agrupamiento:
• Jerárquico: busca agrupar los datos de forma natural 
mediante una estructura de árbol.
• No Jerárquico: 
• Particional: forma particiones naturales de los dato en un número de 
grupos (normalmente parámetro). Similar al problema de clasificación, 
pero no se tienen las etiquetas. Normalmente basado en técnicas de 
optimización.
• Probabilísticas: suele asumir densidades condicionales para los 
clusters (por ejemplo Gaussianas) y estima los parámetros de las 
mismas.
Agrupamiento (Clustering)


---

## Página 36

36
Otra clasificación de tipos de agrupamiento:
•
Connectivity Models: la medida es la distancia de conectividad entre 
observaciones (ej: jerárquicos).
•
Centroids Models: la medida es la distancia desde el valor de media de 
cada observación/cluster (ej: kmeans, kmedoids). 
•
Distribution Models: la medida es la significancia de la distribución 
estadística de variables en el dataset (ej: algoritmos de maximización de 
expectativa).
•
Density models: la medida es la densidad en el espacio de los datos (ej: 
DBSCAN). 
Agrupamiento (Clustering)


---

## Página 37

37
Pasos del análisis de cluster:
• Seleccionar una medida de similaridad.
• Elegir la técnica a usar (jerárquica, no jerárquica).
• Elegir el método o algoritmo dentro de la técnica.
• Si corresponde, decidir cuantos clusters hacer.
• Interpretar los clusters formados (deducir las propiedades 
que dividen).
Agrupamiento (Clustering)


---

## Página 38

38
Interpretación Geométrica
Formar grupos homogéneos de las observaciones x(i), respecto 
a las variables.
Similares, homogéneos: depende del objetivo de estudio. Se 
busca cohesión interna, aislamiento externo.
Agrupamiento (Clustering)


---

## Página 39

39


---

## Página 40

40
.
Agrupamiento Jerárquico


---

## Página 41

41
.
Agrupamiento Jerárquico


---

## Página 42

42
.
Agrupamiento Jerárquico


---

## Página 43

43
.
Agrupamiento Jerárquico


---

## Página 44

44
.
Agrupamiento Jerárquico


---

## Página 45

45
Algoritmo Jerárquico:
1.
Empezar con n observaciones y una métrica (como distancia 
Euclidea) de todas los (n) = n (n-1)/2 disimilaridades por 
pares. Tratar a cada observaciones como su propio cluster.
2.
Para i en (n, n-1, …, 2): 
a)
Examinar todas las diferencias entre grupos por pares e identificar el 
par que es menos diferente (es decir, más similar). Fusionar estos 
grupos. La diferencia entre estos grupos indica la altura en el 
dendograma a la que debe colocarse la fusión.
b)
Calcular las nuevas diferencias por pares entre los i – 1 grupos 
restantes. 
Agrupamiento Jerárquico


---

## Página 46

46
Tipos de Enlace:
Agrupamiento Jerárquico
Descripción
Linkage
Máxima disimilitud entre clusters. Calcular todas las disimilitudes 
de a pares entre las observaciones del cluster A y las del B, y 
registrar la mayor de todas.
Complete
Mínima disimilitud entre clusters.  Calcular todas las disimilitudes 
entre las observaciones del cluster A y las del cluster B, y registrar 
la mas pequeña de todas. 
Single
Disimilitud media entre clusters. Calcular todos los pares de 
disimilitudes entre las observaciones en el cluster y las del B, y 
registrar el promedio de las mismas.
Average
Disimilitud entre el centroide para el cluster A (un vector de medias 
de longitud p) y el centroide del clusted B.
Centroid


---

## Página 47

47
Complete Linkage:
•
Máxima disimilitud entre clusters. Calcular todas las disimilitudes de a 
pares entre las observaciones del cluster A y las del B, y registrar la mayor 
de todas.
Agrupamiento Jerárquico


---

## Página 48

48
Single Linkage:
•
Mínima disimilitud entre clusters.  Calcular todas las disimilitudes entre las 
observaciones del cluster A y las del cluster B, y registrar la más pequeña 
de todas. 
•
Puede dar como resultado clusters extendidos y finales en los que las 
observaciones individuales se fusionan una a la vez.
Agrupamiento Jerárquico


---

## Página 49

49
Average Linkage:
•
Disimilitud media entre clusters. Calcular todos los pares de disimilitudes 
entre las observaciones en el cluster A y las del B, y registrar el promedio 
de las mismas.
Agrupamiento Jerárquico


---

## Página 50

50
Centroid Linkage:
•
Disimilitud entre el centroide para el cluster A (un vector de medias de 
longitud p) y el centroide del cluster B.
Agrupamiento Jerárquico


---

## Página 51

51
Agrupamiento Jerárquico


---

## Página 52

52


---

## Página 53

53
El objetivo del algoritmo K-Means es dividir M puntos en N dimensiones en K 
grupos de modo que se minimice la suma de cuadrados dentro del grupo. No 
es práctico exigir que la solución tenga una suma mínima de cuadrados 
contra todas las particiones, excepto cuando M, N son pequeños y K=2. En 
cambio, buscamos “óptimos locales”, una solución tal que no haya 
movimiento de un punto de un grupo a otro que reduzca dicha suma de 
cuadrados entre clusters.
Donde suma de cuadrados dentro del cluster (within cluster sum of squares, 
WCSS) m es la suma de los cuadrados de las distancias de cada 
observación en un cluster a su centroide.
Agrupamiento No Jerárquico: K-Means


---

## Página 54

54
Algoritmo k-means
En su forma más sencilla, consta de dos pasos:
• Asignación: asignar cada observación al cluster que da la 
menor suma de cuadrados dentro del cluster (Within Cluster
Sum o Squares, WCSS).
• Actualización: Actualizar el centroide por tomar la media de 
todas las observaciones dentro del cluster.
Se ejecutan estos pasos hasta que las asignaciones en dos 
iteraciones consecutivas no cambian, significando que se ha 
encontrado un óptimo local o global (no siempre garantizado)
Agrupamiento No Jerárquico: K-Means


---

## Página 55

55
.
Agrupamiento No Jerárquico: K-Means


---

## Página 56

56
Curva de codo (elbow)
Agrupamiento No Jerárquico: K-Means


---

## Página 57

57
K-Means
Propiedades a satisfacer:
1.
Cada observación pertenece al menos a uno de los K clusters.
2.
Los clusters no están solapados: ninguna observación pertenece a más 
de un cluster.
Agrupamiento No Jerárquico: K-Means


---

## Página 58

58
K-Means
Se busca resolver el problema:
Donde:
Es decir:
Agrupamiento No Jerárquico: K-Means


---

## Página 59

59
Algoritmo K-Means:
1.
Aleatoriamente asignar un número, desde 1 a K, para cada 
una de las observaciones. Esto sirve como una asignación 
inicial de cluster para las observaciones.
2.
Iterar hasta que la asignación de clusters pare de cambiar:
a)
Por cada uno de los K clusters, calcular el centroide del cluster
(cluster centroid).  El centroide del k-ésimo cluster es el vector de las 
medias de las p variables para las observaciones dentro de dicho 
cluster.
b)
Asignar cada observación al cluster cuyo centroide sea mas cercano 
(donde cercano se define usando la distancia Euclidea).
Agrupamiento No Jerárquico: K-Means


---

## Página 60

60
Agrupamiento No Jerárquico: K-Means


---

## Página 61

61
Problema:
Es
muy
sensible
a
la
asignación aleatoria inicial.
Agrupamiento No Jerárquico: K-Means


---

## Página 62

62
Otra implementación:
Agrupamiento No Jerárquico: K-Means


---

## Página 63

63
Agrupamiento No Jerárquico: K-Means


---

## Página 64

64
K-Medoids: Algoritmo PAM (Partitioning Around Medoids):
1.
Inicialización: seleccionar k de los n puntos como medoids para 
minimizar el costo.
2.
Asociar cada punto al medoid más cercano.
3.
Mientras el costo de la configuración disminuya:
a.
Para cada medoid m y para cada no medoid o:
I.
Intercambiar m y o, calcular el costo del cambio (suma de los puntos a sus medoids).
II.
Si el costo del cambio es el actualmente mejor, recordar esta combinación de m y o.
b.
Realizar el mejor intercambio de mbest y obest. si este decrementa la 
función de costo. Si no, termina el algoritmo.
Considerar:
Agrupamiento No Jerárquico: K-Medoids


---

## Página 65

65
Agrupamiento Basado en Densidad: DBSCAN
• Density-based spartial clustering of application with noise
(DBSCAN).
• Propuesto por Martin Ester, Hans-Peker Kriegel, Jörg Sander
y Xiaowei Xi, en 1996.
• Trabaja sobre una aproximación paramétrica. Los dos 
parámetros son:
• ε: El radio de vecinos alrededor del punto de dato p.
• minPts: El mínimo número de puntos de dato que queremos en un 
vecindario para definir un cluster.
Agrupamiento No Jerárquico: DBSCAN


---

## Página 66

66
El algoritmo divide los puntos de dato en tres tipos de punto:
•
Core points: p es core point si al menos minPts están dentro de una 
distancia ε (incluyendo a p).
•
Border points: q es border point de p si hay una ruta p1, …pn con p1 = p 
y pn = q, donde cada pi+1 es accesible desde pi (todos los puntos sobre 
la ruta deben ser core points, con la posible excepción de q).
•
Outliers: todos los puntos no accesibles desde otro punto son outliers.
Agrupamiento No Jerárquico: DBScan


---

## Página 67

67
Algoritmo DBSCAN:
1.
Tomar
un
punto
aleatorio
que
no
esté
asignado
a
un
cluster
y
calcular
su
vecindario. Si en el mismo, este punto tiene
minPts, enconces hacer un cluster alrededor
de el. Si no, marcarlo como outlier.
2.
Una vez que encontró todos los core points,
empezar a expandir hasta incluir border
points.
3.
Repetir estos pasos hasta que todos los
puntos sean asignados a un cluster o se los
considere outliers.
Agrupamiento No Jerárquico: DBScan


---

## Página 68

68
.
Agrupamiento No Jerárquico: DBScan


---

## Página 69

69


---

## Página 70

70
El coeficiente silhouette contrasta la distancia promedio a elementos en el
mismo cluster con la distancia promedio a los elementos en otros clusters.
Los objetos con un alto valor de silhouette son considerados bien agrupados,
los objetos con valor bajo, podrían ser outliers.
1.
Definimos a(i) la media de la distancia entre i y todos los demás puntos
del cluster en el que está i:
2.
Además, definimos b(i) como la media de la distancia entre i a todos los
puntos fuera del cluster de i.
Agrupamiento: Evaluación Interna


---

## Página 71

71
1.
Definimos a(i) la media de la distancia entre i y todos los demás puntos
del cluster en el que está i:
2.
Además, definimos b(i) como la media de la distancia entre i a todos los
puntos fuera del cluster de i.
3.
Definimos entonces el coeficiente s(i) como:
Agrupamiento: Evaluación Interna


---

## Página 72

72
.
Agrupamiento: Evaluación Interna


---

## Página 73

73


---

## Página 74

74
Decisiones importantes:
•
¿Estandarizar el dataset antes? Es muy importante!
•
En el caso de clustering jerárquico:
•
¿que medida de disimilitud debería usarse?
•
¿qué tipo de linkage debería usarse?
•
¿dónde debería cortarse el dendograma para obtener los clusters?
•
En el caso de clustering particional (K-Means, etc):
•
¿cuantos clusters deberíamos buscar en los datos?
Estas decisiones tienen impactos importantes en los resultados.
En la práctica, se prueban diferentes opciones, y se toma la solución 
más útil o interpretable. 
No hay una única respuesta correcta (cada solución expone algún 
aspecto interesante a considerar sobre los datos).
Agrupamiento: Problemas Prácticos


---

## Página 75

75
Validación de Clusters Obtenidos:
• A veces buscamos obtener subgrupos verdaderamente 
representativos en los datos.
• Otras veces, buscamos detectar ruido.
• Existen técnicas para asignar un p-value a un cluster.
• No hay consenso sobre una única mejor aproximación.
• Conocimiento de dominio.
• Análisis exploratorio.
Agrupamiento: Problemas Prácticos


---

## Página 76

76
¿Preguntas?
Ciencia de Datos


---

## Página 77

77
¡Muchas Gracias!
Ciencia de Datos


---
