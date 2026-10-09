# CD_02_02_ETL

## Página 1

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Mgtr. Ing. Mariano Martín Gualpa
CIENCIA DE DATOS


---

## Página 2

FUENTES DE DATOS


---

## Página 3

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Fuentes de Datos
Fuentes de Datos
•
Puede ser el sitio original donde se crean los datos o donde 
se digitaliza por primera vez la información física.
•
Pueden ser (entre otras): 
•
base de datos
•
archivo plano
•
mediciones en tiempo real
•
datos en línea extraídos
•
datos estáticos o de transmisión disponibles en 
internet.
•
Se clasifican en primarias y secundarias.


---

## Página 4

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Fuentes de Datos
Existen diferentes clasificaciones para las fuentes de 
datos. 
•
Según su Procedencia Institucional.
•
Según su Temporalidad.
•
Según su Estructura.
•
Según otros criterios.


---

## Página 5

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Fuentes de Datos
Clasificaciones de fuentes de datos. 
Según su Procedencia Institucional:
•
Fuentes de Datos Internos:
o
Generados dentro de la organización.
o
Alta calidad y control.
o
Fuente principal para BI y predicciones 
operativas.
•
Fuentes de Datos Externos:
o
Provienen desde afuera de la organización.
o
Permiten enriquecer modelos y para 
ciencia de datos predictiva y descriptiva.
o
Se incluye externos públicos, adquiridos y 
de socios.


---

## Página 6

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Fuentes de Datos
Clasificaciones de fuentes de datos. 
Según su Temporalidad:
•
Datos Batch (históricos):
o
Procesados en bloques en momentos 
específicos.
o
Utilizados en data lakes y data warehouses.
•
Datos en streaming (tiempo real):
o
Generados y procesados al instante.
o
Relevantes en arquitecturas event-driven y 
real-time analytics.


---

## Página 7

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Fuentes de Datos
Clasificaciones de fuentes de datos. 
Según su estructura:
•
Datos estructurados:
o
Organizados en tablas (filas y columnas)
o
Muy utilizados en BI, modelos de Ciencia de 
Datos en general.
•
Datos semiestructurados:
o
Formato flexible (JSON, XML, YAML, logs, etc).
o
Muy utilizados en integración de sistemas, APIs, 
y streaming.
•
Datos no estructurados
o
Tienen una estructura interna, pero no están 
predefinidos mediante un modelo de datos.
o
Texto plano, imágenes, video, audio, etc.


---

## Página 8

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Fuentes de Datos
Fuentes de Datos Típicas
•
Bases de Datos:
•
Relacionales
•
NoSql
•
APIs (Application Programming Interfaces):
•
Datos en texto sin formato
•
XML
•
HTML
•
JSON
•
Multimedia
•
Web Scraping
•
Data Streams


---

## Página 9

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Fuentes de Datos
Algunos Repositorios de Datos Públicos
•
CONICET: repositorio con producción de actividades científicas de los investigadores. Contiene 
artículos y otros resultados. Link: https://ri.conicet.gov.ar/
•
Datos Argentina: datos públicos nacionales. Link: https://datos.gob.ar/
•
NASA: centraliza datos abiertos geoespaciales con más de 40.000 conjuntos de datos. Link: 
https://data.nasa.gov/
•
Copernicus: programa de observación de la Tierra de la Unión Europea. Link: 
https://www.copernicus.eu/es/acceso-los-datos/plataformas-convencionales-de-acceso-los-datos
•
Climate Data Online: agencia del gobierno norteamericana con datos meteorológicos y climáticos 
históricos a nivel mundial. Link: https://www.ncdc.noaa.gov/cdo-web/
•
Registry of Research Data Repositories: Herramienta con catálogo de información sobre repositorios 
internacionales existentes de datos para invesigadores. Link: https://www.re3data.org/
•
Kaggle: plataforma web de comunidad Data Science, con recursos y competencias. Link: 
https://www.kaggle.com/datasets/
•
Banco Mundial: datos sobre el desarrollo en el mundo. Link: https://datos.bancomundial.org/


---

## Página 10

EXTRACCIÓN-TRANSFORMACIÓN-CARGA


---

## Página 11

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Procesos ETL
¿Que es ETL?
• Significa Extracción-Transformación-Carga 
(Extract-Transform-Load).
• Proceso de integración de datos que 
combina datos de múltiples fuentes en un 
almacén de datos único y consistente.
• Existe también el ELT.


---

## Página 12

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Procesos ETL


---

## Página 13

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Procesos ELT


---

## Página 14

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Procesos ETL
Extracción-Transformación-Carga
•
Los datos sin procesar se copian o exportan desde las 
ubicaciones origen al área de preparación.
•
Múltiples fuentes de datos, estructurados y no 
estructurados.
•
Ejemplos:
o
Servidores de Relacionales y NoSQL.
o
Sistemas CRM y ERP.
o
Archivos planos.
o
Correo electrónico.
o
Páginas web.
o
Multimedia (audios, imágenes, videos, etc).


---

## Página 15

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Procesos ETL
Extracción-Transformación-Carga
•
En el área de preparación, se procesan los datos.
•
Se transforman y consolidan para el caso de uso analítico.
•
Puede implicar las siguientes tareas:
o
Filtrar, limpiar, deduplicar, validar y autenticar los datos.
o
Realizar cálculos, traducciones o resúmenes de datos.
o
Convertir monedas, unidades de medida, editar cadenas 
de texto, cambiar encabezados de fila y columna.
o
Realizar auditorías para garantizar calidad.
o
Eliminar, cifrar o proteger datos restringidos (por gobierno 
o industria). Procesos de anonimización si corresponde.
o
Formatear datos para que coincidan con el esquema de 
destino de los datos.


---

## Página 16

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Procesos ETL
Extracción-Transformación-Carga
•
Los datos se mueven desde el área de preparación a un 
almacén de datos de destino. 
•
Implica la carga inicial, seguida de cargas periódicas 
incrementales y eventualmente actualizaciones completas 
para borrar y reemplazar datos.
•
En la mayoría de las organizaciones, es un proceso:
o
Automatizado
o
Bien definido
o
Continuo 
o
Controlado por lotes (hay excepciones)
•
Normalmente ETL se lleva a cabo fuera del horario laboral.


---

## Página 17

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Procesos ETL
Otros Métodos de Integración de Datos
•
Change Data Capture (CDC):
o
Identifica y captura solo los datos que han cambiado en el origen y los 
mueve al destino.
o
También se puede usar para mover datos desde el Data Lake u otro 
repositorio en tiempo real.
•
Replicación de Datos: 
o
Copia los cambios en las fuentes en tiempo real o en lotes a una base 
central.
o
Con frecuencia se utiliza para copias de seguridad.
•
Virtualización de Datos: 
o
Se crea una capa de abstracción con una vista de los datos unificada, 
integrada y totalmente utilizable, sin copiar.
•
Stream Data Integration (SDI):
o
Consume flujos de datos en tiempo real, los transforma y los carga para 
su análisis.


---

## Página 18

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Procesos ETL
Beneficios de ETL
•
Mejoran la calidad al realizar una limpieza de datos antes 
de cargarlos en un repositorio diferente.
•
ETL se recomienda con mayor frecuencia para crear 
repositorios de datos de destino más pequeños que 
requieren actualización menos frecuentes.
•
Otros métodos de integración de datos (ELT, captura de 
datos modificados y virtualización) se utilizan para integrar 
volúmenes cada vez mayores de datos que cambian o flujos 
de datos en tiempo real.


---

## Página 19

DATA WAREHOUSE


---

## Página 20

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Warehouse


---

## Página 21

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Warehouse
Data Warehouse
• Repositorio central de datos
• Formato estructurado
• Datos previamente procesados
• Objetivo: análisis e inteligencia de negocios.


---

## Página 22

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Warehouse
Esquema de un Data Warehouse


---

## Página 23

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Warehouse
Esquema de un Data Warehouse


---

## Página 24

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Warehouse
Herramientas de Visualización


---

## Página 25

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Warehouse
Data Mart
• Repositorio de datos con información 
específica de una unidad de negocio.
• Contiene un subconjunto pequeño y 
específico de los datos que la organización 
almacena.
• Datos orientados a analizar información 
específica de cada departamento 
eficientemente.
• Objetivo: brinda datos resumidos a partes 
interesadas clave.


---

## Página 26

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Warehouse
OLAP: Online Analytical Processing


---

## Página 27

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Warehouse
OLAP: Online Analytical Processing


---

## Página 28

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Warehouse
OLAP: Online Analytical Processing


---

## Página 29

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Warehouse
OLAP: Online Analytical Processing


---

## Página 30

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Warehouse
OLAP: Online Analytical Processing


---

## Página 31

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Warehouse
OLAP: Online Analytical Processing


---

## Página 32

DATA LAKE


---

## Página 33

Considerando las necesidades modernas de
la analítica y aprovechamiento de los
datos:
¿Cuál podría considerarse la limitación
principal de los Data Warehouse?
UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Lake


---

## Página 34

• Repositorio central de datos.
• Formato
estructurado,
semi
y
no
estructurado, sin procesar.
• Desafío: los datos se almacenan sin
supervisión de los contenidos (catalogar
y proteger los datos).
• Objetivo: se pueden ejecutar diferentes
tipos
de
análisis,
desde
paneles
y
visualización hasta análisis en tiempo
real y machine learning.
UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Lake


---

## Página 35

Principios de Data Lakes:
•
Almacenamiento en formato nativo.
•
Centralización e infraestructura escalable.
•
Schema on Read:
o
Los datos no son validades ni estructurados
durante el proceso de escritura.
•
In-Place Analytics
o
Los datos pueden ser leídos de distinta forma
desde el mismo archivo.
•
ELT vs. ETL
•
Acceso flexible y democratización de datos.
•
Gobernanza, seguridad y calidad.
UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Lake


---

## Página 36

Conceptos importantes:
• Archivos inmutables.
• Bucket o Container.
• Blobs u Objects.
¿Cuales son los desafíos principales del 
Data Lake?
UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Lake


---

## Página 37

DATA LAKEHOUSE


---

## Página 38

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Lakehouse


---

## Página 39

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Data Lakehouse


---

## Página 40

ESQUEMAS DE ARQUITECTURA DE DATOS


---

## Página 41

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Esquema de Arquitectura


---

## Página 42

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
Áreas de Roles Asociados


---

## Página 43

UNIDAD 2: EXTRACCIÓN-TRANSFORMACIÓN-CARGA
¡Muchas Gracias!


---
