# CD_04_02_02_Metricas

## Página 1

 
Unidad 4: Aprendizaje Supervisado 
Tema: Métricas 
 
Ciencia de Datos 
Mgtr. Ing. Mariano Martín Gualpa (mgualpa@frc.utn.edu.ar) 


---

## Página 2

• 
Matriz de Confusión 
• 
Métricas Principales en Clasificación Binaria 
• 
Curva ROC 
• 
Métodos de Evaluación Cruzada 
• 
Actividad Práctica 
Temario de la Clase 


---

## Página 3

(Página sin texto reconocible)


---

## Página 4

Matriz de Confusión 
x1 
x2 
0 
5
5
ŷ = 1 
ŷ = 0 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 
TP 
  
FN 
    
P 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 
FP 
  
TN 
    
N 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 


---

## Página 5

Matriz de Confusión 
x1 
x2 
0 
5
5
ŷ = 1 
ŷ = 0 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 
TP 
  
FN 
    
P: 8 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 
FP 
  
TN 
    
N 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 


---

## Página 6

Matriz de Confusión 
x1 
x2 
0 
5
5
ŷ = 1 
ŷ = 0 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 
TP 
  
FN 
    
P: 8 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 
FP 
  
TN 
    
N: 8 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 


---

## Página 7

Matriz de Confusión 
x1 
x2 
0 
5
5
ŷ = 1 
ŷ = 0 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 TP: 7   
FN 
    
P: 8 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 
FP 
  
TN 
    
N: 8 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 


---

## Página 8

Matriz de Confusión 
x1 
x2 
0 
5
5
ŷ = 1 
ŷ = 0 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 TP: 7   FN: 1     
P: 8 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 
FP 
  
TN 
    
N: 8 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 


---

## Página 9

Matriz de Confusión 
x1 
x2 
0 
5
5
ŷ = 1 
ŷ = 0 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 TP: 7   FN: 1     
P: 8 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 FP: 2   
TN 
    
N: 8 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 


---

## Página 10

Matriz de Confusión 
x1 
x2 
0 
5
5
ŷ = 1 
ŷ = 0 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 TP: 7   FN: 1     
P: 8 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 FP: 2   TN: 6     
N: 8 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 


---

## Página 11

Matriz de Confusión 
x1 
x2 
0 
5
5
ŷ = 1 
ŷ = 0 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 TP: 7   FN: 1     
P: 8 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 FP: 2   TN: 6     
N: 8 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 


---

## Página 12

Matriz de Confusión 
x1 
x2 
0 
5
5
ŷ = 1 
ŷ = 0 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 TP: 7   FN: 1     
P: 8 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 FP: 2   TN: 6     
N: 8 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 
Error 
Tipo I 


---

## Página 13

Matriz de Confusión 
x1 
x2 
0 
5
5
ŷ = 1 
ŷ = 0 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 TP: 7   FN: 1     
P: 8 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 FP: 2   TN: 6     
N: 8 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 
Error 
Tipo I 
Error 
Tipo II 


---

## Página 14

(Página sin texto reconocible)


---

## Página 15

Métricas 
x1 
x2 
0 
5
5
ŷ = 1 
ŷ = 0 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 TP: 7   FN: 1     
P: 8 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 FP: 2   TN: 6     
N: 8 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 


---

## Página 16

ACC (Accuracy) 
Métricas 
x1 
x2 
0 
5
5
ŷ = 1 
ŷ = 0 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 TP: 7   FN: 1     
P: 8 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 FP: 2   TN: 6     
N: 8 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 
ACC = TP +TN
P + N
=
TP +TN
TP + FN + FP + FN
ACC = TP +TN
P + N
= 7+ 6
16 = 0,8125


---

## Página 17

TPR (True Positive Rate), Recall, Sensitivity o Hit Rate 
Métricas 
x1 
x2 
0 
5
5
ŷ = 1 
ŷ = 0 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 TP: 7   FN: 1     
P: 8 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 FP: 2   TN: 6     
N: 8 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 
TPR = TP
P =
TP
TP + FN =1−FNR
TPR = TP
P = 7
8 = 0,875


---

## Página 18

TNR (True Negative Rate), Specificity o Selectivity 
Métricas 
x1 
x2 
0 
5
5
ŷ = 1 
ŷ = 0 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 TP: 7   FN: 1     
P: 8 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 FP: 2   TN: 6     
N: 8 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 
TNR = TN
N =
TN
TN + FP =1−FPR
TNR = TN
N = 6
8 = 0,75


---

## Página 19

PPV (Positive Predictive Value), Precision 
Métricas 
x1 
x2 
0 
5
5
ŷ = 1 
ŷ = 0 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 TP: 7   FN: 1     
P: 8 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 FP: 2   TN: 6     
N: 8 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 
PPV =
TP
TP + FP =1−FDR
PPV =
TP
TP + FP = 7
9 = 0,7778


---

## Página 20

F-Measure, F1 Score 
Métricas 
x1 
x2 
0 
5
5
ŷ = 1 
ŷ = 0 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 TP: 7   FN: 1     
P: 8 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 FP: 2   TN: 6     
N: 8 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 
F −Measure = 2 × Precision × Recall
Precision + Recall
F −Measure = 2×0,7778×0,875
0,7778+ 0,875
= 0,8235


---

## Página 21

F-Measure, F1 Score 
Métricas 
  
  
Clase Predicha 
   
  
  
  
V 
  
F 
      
Clase Real 
  
  
 
 
 
 
  
  
  
V 
 TP: 7   FN: 1     
P: 8 
 
 
 
 
 
 
  
  
 
 
 
 
 
 
 
  
  
 
F 
 FP: 2   TN: 6     
N: 8 
  
  
  
  
  
  
  
  
  
TP: Verdaderos Positivos      
FN: Falsos Negativos 
FP: Falsos Positivos              
TN: Verdaderos Negativos 
F −Measure = 2 × Precision × Recall
Precision + Recall
F −Measure = 2×0,7778×0,875
0,7778+ 0,875
= 0,8235
MediaArmónica=
1
1
Presicion +
1
Recall
2
MediaArmónica=
2
1
Precision +
1
Recall
MediaArmónica=
2
Recall + Precision
Precision× Recall
F −Measure = 2 × Precision × Recall
Presicion + Recall
La media 
armónica es la 
adecuada 
cuando se 
calcula media 
de ratios. 


---

## Página 22

(Página sin texto reconocible)


---

## Página 23

•  Una vez construido un modelo de clasificación (por ejemplo 
con regresión logística), puede obtenerse la probabilidad 
P(y=1 | x, w).  
•  Debería definirse un Umbral de Clasificación. 
Curva ROC 
1 
0 
Verdadero 
Falso 
P(y=1 | x,w) 
1 
0 
z 
g(z) 
? 


---

## Página 24

•  Una vez construido un modelo de clasificación (por ejemplo 
con regresión logística), puede obtenerse la probabilidad 
P(y=1 | x, w).  
•  Debería definirse un Umbral de Clasificación. 
Curva ROC 
1 
ŷ = 0 
ŷ = 1 
0 
Umbral de Clasificación 
Verdadero 
Falso 
P(y=1 | x,w) 
1 
0 
z 
g(z) 
? 


---

## Página 25

Curva ROC 
TPR = sensibility = TP
P =
TP
TP + FN
TNR = specificity = TN
N =
TN
TN + FP


---

## Página 26

a)                                               b) 
 
 
 
 
c)  d) 
 
Curva ROC 


---

## Página 27

a)                                  b) 
 
 
 
 
c)                                  d) 
 
 
Area Under the ROC Curve (AUC) 
• 
El área bajo la curva 
ROC (AUC), es una 
medida de la bondad 
del clasificador. 
• 
Independiente del 
umbral escogido. 
• 
Permite comparar 
diferentes 
clasificadores. 


---

## Página 28

(Página sin texto reconocible)


---

## Página 29

Evaluación Cruzada: Método de Retención 
 
 
 
 
 
 


---

## Página 30

Evaluación Cruzada: K-Fold Cross Validation 
 
 
 
 
 
 


---

## Página 31

Evaluación Cruzada: K-Fold Cross Validation 
 
 
 
 
 
 


---

## Página 32

Evaluación Cruzada: K-Fold Cross Validation 
 
 
 
 
 
 


---

## Página 33

Evaluación Cruzada: K-Fold Cross Validation 
 
 
 
 
 
 
•  Existe una versión estratificada, que asegura que cada fold incluya la 
misma proporción de etiquetas para cada clase. 
•  Consideraciones especiales en series temporales. 


---

## Página 34

Validación Cruzada Aleatoria 
 
 
 
 
 
 


---

## Página 35

Leave-one-out cross-fold-validation (LOOCV) 
 
 
 
 
 
 


---

## Página 36

Ciencia de Datos 
 
 
 
 
 
 
¿Preguntas? 


---

## Página 37

Ciencia de Datos 
 
 
 
 
 
 
¡Muchas gracias! 


---
