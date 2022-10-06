![Captura de Pantalla 2022-10-03 a la(s) 4 23 27 p  m](https://user-images.githubusercontent.com/110174766/193601574-bf38296f-64e3-4099-8e3f-9d4635d9cb93.png)
# Modelo de Machine Learning para la Predicción de Ictus

Presentamos este proyecto que tiene por objetivo evaluar un modelo predictor para la enfermedad de Ictus, llevado a cabo con 11 variables de información con origen de un dataset, en el que se incluyen 4,200 registros de casos positivos y negativos.

El modelo se basa en el desarrollo, evaluación y selección de algoritmos de Clasificación de Machine Learning. Para ello se utiliza un programa de tipo CLI,  que utilizará al modelo   a traves de preguntas que se formulan al usuario y ayuden a la predicción del Ictus.

## Descripción del proyecto 
* Alcance--> Entregables:  
** Un programa que por línea de comandos pida un input de datos y devuelva una predicción binaria 
** Algoritmo de clasificacion con un overfitting menor al 5%
** Informe de clasificacion con Analisis exploratorio de datos y sustentacion del modelo de machine learning
* Plazo: 8 dias
### Desarrollo del proyecto 
* Analisis de datos : EDA (Exploracion basica de datos, inputacion de valores perdidos, tratamiento y limpieza de datos e ingenieria de caracteristicas) y formulacion de hipotesis
* Visualización: correlaciones entre variables, graficas que sustenten hipótesis, , como estan balanceados los datos, detectar valores atípicos, reconocer tendencias y patrones, y extraer conclusiones signifitativas del conjunto de datos,asi como para poder representar visualmente toda informacion de interes para el proyecto
* Seleccion del modelo de machine Learning : metodos de balanceo de datos, entrenamiento de modelo de clasificacion, ajuste de hiperparametros (tunning) y analisis de pesos de caracteristicas
* Metricas analizadas para seleccion del modelo: accuracy, precission, recall, f1 , curvas ROC y evaluacion del overfitting
* Programa Command Line input: Menu interactivo en consola de terminal, que solicita unas respuestas al usuario, que serviran de entradas para ser procesadas por el modelo de machine learning, y hacer una prediccion. Ademas, está la opción de responder unas preguntas complementarias (que surjen de la investigacion previa) ; esta recoleccion de datos servira para mejorar el rendimiento del modelo de ML en el futuro
* Dashboard: Aplicacion hecha en dash, que se estructura en cuatro pestañas: Presentacion, analisis y visualizacion de datos,seleccion de modelo predictor, informe de clasificacion y repositorio del proyecto (Con codigo QR enlazado al repositorio github). En la seccion de visualizacion se muestran las relaciones entre las variables y su incidencia en la prediccion de ictus. En la seccion de seleccion de modelo, se visualizan 
las distintas metricas de evaluacion para cada metodo de balanceo de datos para los distintos algoritmos de clasificacion evaluados. En el informe de clasificacion se representan visualmente las metricas con matriz de confusion y reporte de clasificacion del modelo de ML seleccionado
* Cuardernos de jupyter: Desglose de todo el desarrollo del analisis exploratorio de datos --> preparacion, procesamiento , analisis de los datos y sus respectivas visualizaciones graficas
![Colorful Web Domain Price List Instagram Post (1)](https://user-images.githubusercontent.com/110173993/193646445-89ec56bb-ae7b-434f-a617-7fe5af4818fb.png)

## Capturas de aplicacion integrada

### Presentación dashboard
![presenatcion](https://user-images.githubusercontent.com/73450522/193939242-01d33370-6a01-453f-bcd6-7c0a6db037b7.jpg)

### Visualizacion dashboard
![visualizacion de datos](https://user-images.githubusercontent.com/73450522/193939276-42370e16-c337-435c-863b-e78acc4da329.jpg)

### Modelo ML dashboard
![seleccion del modelo](https://user-images.githubusercontent.com/73450522/193939310-64d06dd4-60a0-4015-9a66-6746f43e877f.jpg)
![modelo](https://user-images.githubusercontent.com/73450522/193939316-793d4f03-8539-49a0-99a5-3c4491961d10.jpg)

### Codigo QR dashboard
![repo](https://user-images.githubusercontent.com/73450522/193939332-bc6e538e-7cfe-493b-b3bc-a0d663d942dc.jpg)

### Programa CLI
![menu](https://user-images.githubusercontent.com/73450522/193939351-112acd46-6a4a-45d3-b53a-df30108784d9.jpg)
![mandatory questions](https://user-images.githubusercontent.com/73450522/193939370-5ad6bd01-6a75-4c1c-9bf9-889cdda125cd.jpg)
![prediccion](https://user-images.githubusercontent.com/73450522/193939388-0bcaeaf1-a3f2-4ca6-9015-2bb13492826b.jpg)
![questions complementary](https://user-images.githubusercontent.com/73450522/193939402-2cd9cd85-a00d-4da1-bfae-5e848397da85.jpg)

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

 **Clonar repositorio** 
```
git clone https://github.com/pdegaudenci/Stroke-Predictor.git
```
**Moverse a la carpeta**
```
cd Stroke-Predictor/
```
### Pre-requisitos 📋

_Instalar dependencias y librerias de python del proyecto_

```
pip install -r requirements.txt
```

## Despliegue 📦

_Ejecutar para despleglar dashboard_
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
** Manejo del teclado, consola de texto y terminal -> libreria curses
** Estilos de fuente --> libreria colorama y tabulate
** Menu y validaciones de entrada de usuario -> librerias Pyinquirer y prompt
** Persistencia de datos -> libreria pickle y joblib
* Dashboard -> libreria dash
* Gestor de paquetes y dependencias -> pip 
* Analisis de datos -> jupyter notebook, notebook de kaggle y librerias pandas y numpy
* Visualizacion de datos -> librerias seaborn, matplotlib y plotly
* Analisis, seleccion, entrenamiento y ajuste de modelo de Machine Learning -> librerias scikit-learn ,catboost ,imbalanced-learn,statistics, statsmodels, xgboost y scipy



## Versionado 📌

* Sistema de Control de versiones : git
* Version actual : 1.0

## Autores ✒️


* **Pedro Sebastian Degaudenci
* **Stephany Valderrama
* **Celeste Saquiche
* **Begoña Ortiz


---

