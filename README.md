![Captura de Pantalla 2022-10-03 a la(s) 4 23 27 p  m](https://user-images.githubusercontent.com/110174766/193601574-bf38296f-64e3-4099-8e3f-9d4635d9cb93.png)
# Modelo de Machine Learning para la Predicción de Ictus (Python)

Este proyecto que tiene por objetivo servir un modelo predictor de Ictus, entrenado con informacion proveniente de un dataset con 4200 registros etiquetados de pacientes que han sufrido ictus y desplegada en una aplicación de usuario por linea de comandos. Se componen de 11 caracteristicas o variables de entrada y su correspondiente columna etiquetada de salida (Si/No).
Debido a que son datos etiquetados , es posible abordar la solución desde un enfoque de aprendizaje supervisado en el marco del Machine Learning.

Se realizaron 6 etapas fundamentales: Analisis Exploratorio de datos, limpieza e ingenieria de caracteristicas , preprocesado y transformacion de los datos , entrenamiento y evaluacion del modelo, desarrollo de la aplicacion de despliegue del modelo e implemntación.

El modelo fue seleccionado, luego de evaluar los rendimientas de diferentes algoritmos de Clasificación de Machine Learning preentrenados, con el objetivo de poder predecir la probabilidad que una persona padezca Ictus en el corto plazo , dado un conjunto de caracteristicas personales.
Para ello se despliega el modelo dentro de un programa con una interfaz de usuario de tipo CLI (Command Line Interface),  cuyo fin es recolectar cierta informacion del usuario (a traves de preguntas), la cual es preprocesada e ingresada al modelo para la generacion de una predicción de Ictus que se visualiza al usuario por pantalla.
Este programa será el cliente que usará el modelo de M.L generado. 

El desarrollo del proyecto se realizó segun las siguientes fases:
* Limpieza de los datos: para controlar errores,imputacion de valores perdidos , tratamiento de valores atípicos o outliers, etc.
* Aplicar técnicas estadísticas para comprender mejor los datos y cómo se puede esperar que la muestra represente la población de datos del mundo real, teniendo en cuenta la variación aleatoria. Además ,al ser un problema de clasificación binaria, se evalua si los datos están balanceados en sus etiquetas de predicción.
* Visualización :examen de los datos sin procesar,  utilizando tecnicas de estadistica descriptiva para proporcionar una evaluación cualitativa rápida de los datos, a fin de entender los resultados, encontrar valores atípicos, comprender la distribución de los valores las variables numericas,medidas de tendencia central (media,moda , mediana y varianza),función de densidad de probabilidad,etc.
* Preparar datos: Procesamiento, limpieza y transformacion de los datos (normalización)
* Entrenar  los modelos: Division de los datos en dos conjuntos (datos de entrenamiento y datos de validación). Entrenamiento del modelo con datos de entrenamiento y, posteriormente, evaluacion del rendimiento modelo de  mediante el conjunto de datos de validación. 
* Evaluar el rendimiento: Comparacion de la proximidad de las predicciones del modelo con las etiquetas conocidas, basandome en determinadas métricas del modelo, tales como precision, exactitud o sensibilidad.
* Seleccion del modelo y optimizacion para mejorar su rendimiento. Elaboracion de informe de rendimiento en Dash (Python)
* Implementación del servicio predictivo: Uso efectivo del modelo predictivo a traves de una aplicacion cliente, desarrollada en Python, con una aplicacion CLI. Esta es la solucion final que puede ser desplegada  en un servidor o dispositivo para que otros usuarios puedan usarlo.

<b>El detalle de las etapas de exploracion y visualizacion,limpieza y procesamiento de los datos junto con las etapas de entrenamiento-evaluacion y seleccion del modelo se encuentran en los cuadernos de jupyter contenidos en la carpeta MODELO. </b> 


## Descripción del proyecto 
Alcance--> Entregables:  
* Un programa que por línea de comandos pida un input de datos y devuelva una predicción binaria 
* Algoritmo de clasificacion con un overfitting menor al 5%
* Informe de clasificacion con Analisis exploratorio de datos y sustentacion del modelo de machine learning
* Plazo: 8 dias
### Desarrollo del proyecto 
* Análisis de datos : EDA (Exploración básica de datos, inputación de valores perdidos, tratamiento y limpieza de datos e ingenieria de características) y formulación de hipótesis.
* Visualización: correlaciones entre variables, gráficas que sustenten hipótesis, , como están balanceados los datos, detectar valores atípicos, reconocer tendencias y patrones, y extraer conclusiones significativas del conjunto de datos,así como poder representar visualmente toda información de interés del proyecto.
* Selección del modelo de machine Learning : metodos de balanceo de datos, entrenamiento de modelo de clasificación, ajuste de hiperparametros (tunning) y análisis de pesos de características
* Métricas analizadas en la selección del modelo: accuracy, precission, recall, f1 , curvas ROC y evaluación del overfitting
* Programa con interfaz de usuario de tipo CLI: Menu interactivo en consola de terminal, que solicita una serie de respuestas al usuario, que servirán de entradas para ser procesadas por el modelo de machine learning, el cual hará una predicción binaria. Además, está la opción de responder unas preguntas complementarias (que surjen de la investigacion previa) ; cuyas respuestas servirán para mejorar el rendimiento predictivo del modelo de ML en el futuro.
* Dashboard: Aplicación hecha en dash, que se estructura en cuatro pestañas: Presentación, análisis y visualización de datos,seleccion de modelo predictor, informe de clasificación y repositorio del proyecto (Con codigo QR enlazado al repositorio github). En la sección de visualizacion se muestran las relaciones entre las variables y su incidencia en la prediccion de ictus. En la sección de selección de modelo, se visualizan 
las distintas métricas de evaluación para cada método de balanceo de datos para los distintos algoritmos de clasificación evaluados. En el informe de clasificación se representan visualmente las métricas, matriz de confusión y reporte de clasificación del modelo de ML seleccionado
* Cuardernos de jupyter: Desglose de todo el desarrollo del analisis exploratorio de datos --> preparacion, procesamiento , analisis de los datos y sus respectivas visualizaciones gráficas para confirmar/ descartar hipótesis de datos.
![Colorful Web Domain Price List Instagram Post (1)](https://user-images.githubusercontent.com/110173993/193646445-89ec56bb-ae7b-434f-a617-7fe5af4818fb.png)

## Capturas de aplicación integrada

### Presentación dashboard
![presenatcion](https://user-images.githubusercontent.com/73450522/193939242-01d33370-6a01-453f-bcd6-7c0a6db037b7.jpg)

### Visualización dashboard
![visualizacion de datos](https://user-images.githubusercontent.com/73450522/193939276-42370e16-c337-435c-863b-e78acc4da329.jpg)

### Modelo ML dashboard
![seleccion del modelo](https://user-images.githubusercontent.com/73450522/193939310-64d06dd4-60a0-4015-9a66-6746f43e877f.jpg)
![modelo](https://user-images.githubusercontent.com/73450522/193939316-793d4f03-8539-49a0-99a5-3c4491961d10.jpg)

### Código QR dashboard
![repo](https://user-images.githubusercontent.com/73450522/193939332-bc6e538e-7cfe-493b-b3bc-a0d663d942dc.jpg)

### Programa CLI
![menu](https://user-images.githubusercontent.com/73450522/193939351-112acd46-6a4a-45d3-b53a-df30108784d9.jpg)
![mandatory questions](https://user-images.githubusercontent.com/73450522/193939370-5ad6bd01-6a75-4c1c-9bf9-889cdda125cd.jpg)
![prediccion](https://user-images.githubusercontent.com/73450522/193939388-0bcaeaf1-a3f2-4ca6-9015-2bb13492826b.jpg)
![questions complementary](https://user-images.githubusercontent.com/73450522/193939402-2cd9cd85-a00d-4da1-bfae-5e848397da85.jpg)

## Comenzando 🚀

_Estas instrucciones le permitirán obtener una copia del proyecto en funcionamiento en su máquina local para propósitos de desarrollo y pruebas._

 **Clonar repositorio** 
```
git clone https://github.com/pdegaudenci/Stroke-Predictor.git
```
**Moverse a la carpeta**
```
cd Stroke-Predictor/
```
### Pre-requisitos 📋

_Instalar dependencias y librerias de python requeridas para la ejecución del proyecto_

```
pip install -r requirements.txt
```

## Despliegue 📦

_Ejecutar para despliegue del  dashboard_
```
cd DASHBOARD
```
```
python brain_dash.py
```
_Ejecutar CLI_
```
cd CLI
```
```
python main.py
```
## Construido con 🛠️

_Tecnologias usadas:_
* Lenguaje de programacion -> Python
* Dashboard -> libreria dash
* Gestor de paquetes y dependencias -> pip 
* Análisis de datos -> jupyter notebook, notebook de kaggle y librerias pandas y numpy
* Visualización de datos -> librerias seaborn, matplotlib y plotly
* Análisis, selección, entrenamiento y ajuste del modelo de Machine Learning -> librerias scikit-learn ,catboost ,imbalanced-learn,statistics, statsmodels, xgboost y scipy
* Command Line Input Program -> Python
<ul><h5>Librerias de python usadas en la aplicación:</h5>
  <li>Manejo del teclado, consola de texto y terminal -> libreria curses y modulos subprocess y os </li>
  <li> Estilos de fuente --> libreria colorama y tabulate</li>
  <li>Menu y validaciones de entrada de usuario -> librerias Pyinquirer y prompt</li>
  <li>Persistencia de datos -> libreria pickle y joblib</li>
  </ul>




## Versionado 📌

* Sistema de Control de versiones : git
* Version actual : 1.0

## Autores ✒️


* **Pedro Sebastian Degaudenci
* **Stephany Valderrama
* **Celeste Saquiche
* **Begoña Ortiz


---

