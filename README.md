

# Predicción de Riesgo de Diabetes Tipo 2 con Aprendizaje Automático

**TFG – Carlos  A. Pérez Casares**

## Resumen del proyecto

Este proyecto desarrolla un modelo predictivo capaz de estimar el riesgo de diabetes mellitus tipo 2 (DM2) utilizando datos no invasivos procedentes de la encuesta de salud pública BRFSS 2014 (CDC, EE. UU.). Tras un proceso completo de minería de datos, se entrenó un modelo de regresión logística y se seleccionaron varias variables mediante RFE. Finalmente, el modelo se integró en una aplicación interactiva que permite realizar un cribado rápido (screening) accesible del riesgo de DM2.

------

## Project Summary

This project develops a predictive model capable of estimating the risk of type 2 diabetes mellitus (T2DM) using non-invasive data from the 2014 BRFSS public health survey (CDC, USA). After a comprehensive data mining process, a logistic regression model was trained, and several variables were selected using RFE. Finally, the model was integrated into an interactive application that allows for accessible, rapid screening of T2DM risk.
------

## Objetivos del TFG

- Analizar y preparar el conjunto de datos BRFSS 2014.
- Mitigar sesgos y corregir el desequilibrio de clases.
- Seleccionar las variables más relevantes mediante RFE.
- Entrenar y evaluar modelos de clasificación (Regresión Logística).
- Desarrollar una aplicación interactiva para el cribado del riesgo de DM2.
- Interpretar los resultados desde una perspectiva clínica y de salud pública.

------

## Tecnologías utilizadas

- **Python 3.9**
- **Pandas, NumPy, Scikit‑learn**
- **SHAP**
- **SMOTENC**
- **TK/Tkinter** (interfaz de usuario)
- **Matplotlib / Seaborn** (visualización)

------

## Estructura del repositorio

```
├── app
│   ├── predecir_diabetes_rl_3.py
│   ├── modelosSHAP
│   |── columnas_rl.pkl
│   |── modelo_rl.pkl
│   └── README.md
├── data
│   ├── DatasetLink.md
│   └── README.md
├── memoria
│   ├── memoria_TFG.pdf
│   └── resumen_memoria.md
├── notebooks
│   ├── 01-preprocesado_Fairnes_RFE_logistica.html
│   ├── 01-preprocesado_Fairnes_RFE_logistica.ipynb
│   
├── README.md
├── requirements.txt
└── src
    └── xpt_to_csv-v2.py


```

------

## Cómo reproducir el análisis

1. Clona el repositorio:

   ```
   git clone https://github.com/calex0/diabetes-prediccion.git
   ```

2. Instala las dependencias:

   ```
   pip install -r requirements.txt
   ```

3. Ejecuta los notebooks en orden:

   - 01-preprocesado_Fairnes_RFE_logistica.ipynb
   
------

## Cómo ejecutar la aplicación de cribado

Fichero requirements.txt mínimo (con las las dependencias mínimas):

```
aif360==0.6.1
catboost==1.2.7
graphviz==0.21
matplotlib==3.9.4
numpy==1.26.4
pandas==1.5.3
plotly==6.4.0
pyreadstat==1.3.5
scikit-learn==1.2.2
scipy==1.13.1
seaborn==0.13.2
xgboost==2.1.4

```



Esta versión:

    - Funciona en Python 3.9
    
    - Es CPU‑only
    
    - No incluye dependencias internas
    
    - No incluye paquetes de NVIDIA
    
    - Es reproducible y limpia

Desde la carpeta principal de un entorno virtual de python (versión 3.9):

```
python3 appGUI_diabetes.py
```

La aplicación se abrirá mostrando un formulario que permitirá introducir las cinco variables clave para obtener una predicción inmediata del riesgo de DM2.

------

## Resultados principales

- CatBoost obtuvo el mejor rendimiento global (AUC‑ROC, sensibilidad y especificidad).
- SHAP permitió identificar las cinco variables más influyentes.
- La aplicación final ofrece un cribado rápido, económico y accesible.
- El análisis confirma que el riesgo de DM2 depende de factores clínicos, conductuales y demográficos.

------

## Licencia

Este proyecto se distribuye bajo licencia MIT.

