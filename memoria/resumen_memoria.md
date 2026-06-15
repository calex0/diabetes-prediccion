Resumen


La diabetes mellitus tipo 2 (DM2) es una enfermedad crónica de gran difusión
cuyo diagnóstico tardío aumenta las complicaciones y costes sanitarios.
Los métodos clínicos tradicionales de cribado pueden resultar costosos
o poco accesibles para la población general. El objetivo de este trabajo es
diseñar un modelo predictivo que permitan identificar de manera temprana
el riesgo de DM2 a partir de datos obtenidos mediante encuestas telefóni-
cas de salud pública, concretamente el conjunto de datos BRFSS 2014 del
CDC (EEUU). El proyecto emplea una metodología basada en el proceso de
minería de datos y aprendizaje automático. Tras limpiar el conjunto de da-
tos original, se transformaron, se realizó la reducción de la dimensionalidad
del conjunto de datos mediante Recursive Feature Elimination (RFE) per-
mitiendo la selección de las variables más predictivas, se equilibró la variable
objetivo mediante técnicas de over-sampling (SMOTENC) para corregir el
desequilibrio de clases. Después se mitigó el sesgo por edad. A continuación
se entrenó un modelo de clasificación binaria supervisada (Regresión Logís-
tica). Al modelo se le aplicó SHAP, método para explicar las predicciones
del mismo. Finalmente se integró el modelo en una aplicación con interfaz
gráfica.
Como conclusión, el riesgo de diabetes depende tanto de parámetros clí-
nicos como de hábitos de vida, acceso a la atención médica y factores demo-
gráficos.



###### Abstract


Type 2 diabetes mellitus (T2DM) is a widespread chronic disease whose
delayed diagnosis increases complications and healthcare costs.
Traditional clinical screening methods can be expensive or inaccessible
to the general population. The aim of this work is to design a predictive
model that allows for the early identification of T2DM risk using data ob-
tained through public health telephone surveys, specifically the 2014 BRFSS
dataset from the CDC (USA). The project employs a methodology based
on data mining and machine learning. After cleaning the original dataset, it
was transformed, and dimensionality reduction was performed using Recursi-
ve Feature Elimination (RFE), allowing the selection of the most predictive
variables. The target variable was balanced using oversampling techniques
(SMOTENC) to correct class imbalance. Finally, age bias was mitigated.
A supervised binary classification model (Logistic Regression) was then trai-
ned. The SHAP method, used to explain the model’s predictions, was applied
to the model. Finally, the model was integrated into an application with a
graphical interface.
In conclusion, the risk of diabetes depends on clinical parameters, lifestyle
habits, access to healthcare, and demographic factors.
