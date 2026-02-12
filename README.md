

# Predicción de Riesgo de Diabetes Tipo 2 con Aprendizaje Automático

**TFG – Carlos  A. Pérez Casares**

## Resumen del proyecto

Este proyecto desarrolla un modelo predictivo capaz de estimar el riesgo de diabetes mellitus tipo 2 (DM2) utilizando datos no invasivos procedentes de la encuesta de salud pública BRFSS 2014 (CDC, EE. UU.). Tras un proceso completo de minería de datos, se entrenó un modelo CatBoost optimizado y se seleccionaron las cinco variables más influyentes mediante SHAP. Finalmente, el modelo se integró en una aplicación interactiva que permite realizar un cribado rápido y accesible del riesgo de DM2.

------

## Objetivos del TFG

- Analizar y preparar el conjunto de datos BRFSS 2014.
- Mitigar sesgos y corregir el desequilibrio de clases.
- Seleccionar las variables más relevantes mediante RFE y SHAP.
- Entrenar y evaluar modelos de clasificación (Regresión Logística y CatBoost).
- Desarrollar una aplicación interactiva para el cribado del riesgo de DM2.
- Interpretar los resultados desde una perspectiva clínica y de salud pública.

------

## Tecnologías utilizadas

- **Python 3.x**
- **Pandas, NumPy, Scikit‑learn**
- **CatBoost**
- **SHAP**
- **SMOTENC**
- **Gradio / Streamlit** (interfaz de usuario)
- **Matplotlib / Seaborn** (visualización)

------

## Estructura del repositorio

```
├── app
│   ├── appGUI_diabetes.py
│   ├── modelosSHAP
│   │   ├── columnas_cb.pkl
│   │   └── modelo_cb.pkl
│   └── README.md
├── data
│   ├── DatasetLink.md
│   └── README.md
├── memoria
│   ├── memoria_TFG.pdf
│   └── resumen.md
├── notebooks
│   ├── 01-preprocesado_Fairnes_RFE_logistica.html
│   ├── 01-preprocesado_Fairnes_RFE_logistica.ipynb
│   ├── 02-catboost_SHAP.html
│   └── 02_catboost_SHAP.ipynb
├── README.md
├── requirements.txt
└── src
    └── xpt_to_csv.py

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
   - 02_catboost_SHAP.ipynb

------

## Cómo ejecutar la aplicación de cribado

Desde la carpeta principal:

```
python appGUI_diabetes.py
```

La aplicación se abrirá en tu navegador y permitirá introducir las cinco variables clave para obtener una predicción inmediata del riesgo de DM2.

------

## Resultados principales

- CatBoost obtuvo el mejor rendimiento global (AUC‑ROC, sensibilidad y especificidad).
- SHAP permitió identificar las cinco variables más influyentes.
- La aplicación final ofrece un cribado rápido, económico y accesible.
- El análisis confirma que el riesgo de DM2 depende de factores clínicos, conductuales y demográficos.

------

## Licencia

Este proyecto se distribuye bajo licencia MIT.

