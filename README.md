![Captura de Pantalla 2022-10-03 a la(s) 4 23 27 p  m](https://user-images.githubusercontent.com/110174766/193601574-bf38296f-64e3-4099-8e3f-9d4635d9cb93.png)
# Modelo de Machine Learning para la Predicción de Ictus (Python)

Presentamos este proyecto que tiene por objetivo evaluar un modelo predictor para la enfermedad de Ictus, llevado a cabo con 11 variables de información con origen de un dataset, en el que se incluyen 4,200 registros de casos positivos y negativos.

El modelo se basa en el desarrollo, evaluación y selección de algoritmos de Clasificación de Machine Learning. Para ello se utiliza un programa con una interfaz de usuario de tipo CLI (Command Line Interface),  que utilizará al modelo   a traves de preguntas que se formulan al usuario y ayuden a la predicción del Ictus.

## Descripción del proyecto 
* Alcance--> Entregables:  
** Un programa que por línea de comandos pida un input de datos y devuelva una predicción binaria 
** Algoritmo de clasificacion con un overfitting menor al 5%
** Informe de clasificacion con Analisis exploratorio de datos y sustentacion del modelo de machine learning
* Plazo: 8 dias
### Desarrollo del proyecto 
* Análisis de datos : EDA (Exploración básica de datos, inputación de valores perdidos, tratamiento y limpieza de datos e ingenieria de características) y formulación de hipótesis.
* Visualización: correlaciones entre variables, gráficas que sustenten hipótesis, , como están balanceados los datos, detectar valores atípicos, reconocer tendencias y patrones, y extraer conclusiones significativas del conjunto de datos,así como poder representar visualmente toda información de interés del proyecto.
* Selección del modelo de machine Learning : metodos de balanceo de datos, entrenamiento de modelo de clasificación, ajuste de hiperparametros (tunning) y análisis de pesos de características
* Métricas analizadas en la selección del modelo: accuracy, precission, recall, f1 , curvas ROC y evaluación del overfitting
* Programa con interfaz de usuario de tipo CLI: Menu interactivo en consola de terminal, que solicita una serie de respuestas al usuario, que servirán de entradas para ser procesadas por el modelo de machine learning, el cual hará una predicción. Además, está la opción de responder unas preguntas complementarias (que surjen de la investigacion previa) ; cuyas respuestas servirán para mejorar el rendimiento predictivo del modelo de ML en el futuro.
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
* Command Line Input Program -> Python
** Manejo del teclado, consola de texto y terminal -> libreria curses y modulos subprocess y os 
** Estilos de fuente --> libreria colorama y tabulate
** Menu y validaciones de entrada de usuario -> librerias Pyinquirer y prompt
** Persistencia de datos -> libreria pickle y joblib
* Dashboard -> libreria dash
* Gestor de paquetes y dependencias -> pip 
* Análisis de datos -> jupyter notebook, notebook de kaggle y librerias pandas y numpy
* Visualización de datos -> librerias seaborn, matplotlib y plotly
* Análisis, selección, entrenamiento y ajuste del modelo de Machine Learning -> librerias scikit-learn ,catboost ,imbalanced-learn,statistics, statsmodels, xgboost y scipy



## Versionado 📌

* Sistema de Control de versiones : git
* Version actual : 1.0

## Autores ✒️


* **Pedro Sebastian Degaudenci
* **Stephany Valderrama
* **Celeste Saquiche
* **Begoña Ortiz


---

