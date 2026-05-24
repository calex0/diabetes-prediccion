#### Predicción diabetes tipo 2 a partir de un cuestionario telefónico

11 de febrero de 2026



#### Resumen

La diabetes mellitus tipo 2 (DM2) es una enfermedad crónica de elevada prevalencia cuyo diagnóstico tardío incrementa tanto las complicaciones clínicas como los costes sanitarios asociados. Los métodos tradicionales de cribado, basados en analíticas sanguíneas, pueden resultar costosos o poco accesibles para la población general. En este contexto, el objetivo de este trabajo es desarrollar un modelo predictivo capaz de identificar de forma temprana el riesgo de DM2 utilizando exclusivamente datos procedentes de encuestas telefónicas de salud pública, concretamente el conjunto de datos BRFSS 2014 del CDC (EE. UU.).

El proyecto sigue una metodología completa de minería de datos y aprendizaje automático. Tras la limpieza y transformación del conjunto de datos original, se aplicaron técnicas para mitigar sesgos y se realizó una reducción de dimensionalidad mediante *Recursive Feature Elimination* (RFE), seleccionando las variables con mayor capacidad predictiva. Para corregir el desequilibrio de clases, se empleó la técnica de *over‑sampling* SMOTENC. Posteriormente, se entrenaron y evaluaron dos modelos supervisados de clasificación —Regresión Logística y CatBoost— utilizando métricas como precisión, sensibilidad, especificidad y AUC‑ROC.

Al modelo CatBoost se le aplicó SHAP, un método de interpretabilidad que permite identificar la contribución de cada variable a las predicciones. A partir de esta explicación se seleccionaron las cinco variables más influyentes, que se integraron en una aplicación interactiva diseñada para realizar un cribado rápido y económico del riesgo de DM2.

Los resultados muestran que el riesgo de diabetes depende no solo de parámetros clínicos, sino también de hábitos de vida, acceso a la atención sanitaria y factores demográficos. El modelo final ofrece una herramienta accesible y eficiente para la detección temprana, especialmente útil en contextos donde no se dispone de pruebas diagnósticas inmediatas.

------

#### Predicting Type 2 Diabetes from a Telephone Survey

February 11, 2026

#### Abstract

Type 2 diabetes mellitus (T2DM) is a highly prevalent chronic disease whose delayed diagnosis increases both clinical complications and associated healthcare costs. Traditional screening methods, based on blood tests, can be expensive or inaccessible to the general population. In this context, the objective of this work is to develop a predictive model capable of identifying the risk of T2DM early using exclusively data from public health telephone surveys, specifically the 2014 BRFSS dataset from the CDC (USA).

The project follows a comprehensive data mining and machine learning methodology. After cleaning and transforming the original dataset, techniques were applied to mitigate biases, and dimensionality reduction was performed using Recursive Feature Elimination (RFE), selecting the variables with the greatest predictive capacity. To correct for class imbalance, the SMOTENC oversampling technique was used. Subsequently, two supervised classification models—Logistic Regression and CatBoost—were trained and evaluated using metrics such as accuracy, sensitivity, specificity, and AUC-ROC.

The CatBoost model was subjected to SHAP, an interpretability method that identifies the contribution of each variable to the predictions. Based on this analysis, the five most influential variables were selected and integrated into an interactive application designed for rapid and cost-effective screening of type 2 diabetes risk.

The results show that diabetes risk depends not only on clinical parameters but also on lifestyle habits, access to healthcare, and demographic factors. The final model offers an accessible and efficient tool for early detection, particularly useful in contexts where immediate diagnostic tests are unavailable.

