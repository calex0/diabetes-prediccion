#### Predicción diabetes tipo 2 a partir de un cuestionario telefónico

11 de febrero de 2026



#### Resumen

La diabetes mellitus tipo 2 (DM2) es una enfermedad crónica de elevada prevalencia cuyo diagnóstico tardío incrementa tanto las complicaciones clínicas como los costes sanitarios asociados. Los métodos tradicionales de cribado, basados en analíticas sanguíneas, pueden resultar costosos o poco accesibles para la población general. En este contexto, el objetivo de este trabajo es desarrollar un modelo predictivo capaz de identificar de forma temprana el riesgo de DM2 utilizando exclusivamente datos procedentes de encuestas telefónicas de salud pública, concretamente el conjunto de datos BRFSS 2014 del CDC (EE. UU.).

El proyecto sigue una metodología completa de minería de datos y aprendizaje automático. Tras la limpieza y transformación del conjunto de datos original, se aplicaron técnicas para mitigar sesgos y se realizó una reducción de dimensionalidad mediante *Recursive Feature Elimination* (RFE), seleccionando las variables con mayor capacidad predictiva. Para corregir el desequilibrio de clases, se empleó la técnica de *over‑sampling* SMOTENC. Posteriormente, se entrenaron y evaluaron dos modelos supervisados de clasificación —Regresión Logística y CatBoost— utilizando métricas como precisión, sensibilidad, especificidad y AUC‑ROC.

Al modelo CatBoost se le aplicó SHAP, un método de interpretabilidad que permite identificar la contribución de cada variable a las predicciones. A partir de esta explicación se seleccionaron las cinco variables más influyentes, que se integraron en una aplicación interactiva diseñada para realizar un cribado rápido y económico del riesgo de DM2.

Los resultados muestran que el riesgo de diabetes depende no solo de parámetros clínicos, sino también de hábitos de vida, acceso a la atención sanitaria y factores demográficos. El modelo final ofrece una herramienta accesible y eficiente para la detección temprana, especialmente útil en contextos donde no se dispone de pruebas diagnósticas inmediatas.



