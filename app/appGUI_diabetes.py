import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import joblib
from sklearn.impute import SimpleImputer

# -----------------------
# Configuración
# -----------------------
MISSING_VALUES = {888.0, 88.0, 77.0, 99.0}
columnas = ['EYEEXAM', 'PREDIAB1', 'INSULIN', '_AGE_G', '_BMI5CAT']
cat_cols_cb = ['PREDIAB1', '_BMI5CAT']

# -----------------------
# Cargar modelo CatBoost
# -----------------------
modelo_cb = joblib.load("modelosSHAP/modelo_cb.pkl")
columnas_cb = joblib.load("modelosSHAP/columnas_cb.pkl")

# -----------------------
# Opciones de los combobox
# -----------------------
opciones_combobox = {
    "EYEEXAM": {
        1: "Within the past month", 2: "Within the past year", 3: "Within the past 2 years",
        4: "2 or more years", 7: "Don’t know/Not sure", 8: "Never", 9: "Refused"
    },
    "PREDIAB1": {
        1: "Yes", 2: "Yes, during pregnancy", 3: "No", 7: "Don’t know/Not Sure", 9: "Refused"
    },
    "INSULIN": {
        1: "Yes", 2: "Yes, during pregnancy", 3: "No", 7: "Don’t know/Not Sure", 9: "Refused"
    },
    "_AGE_G": {
        1: "Age 18 to 24", 2: "Age 25 to 34", 3: "Age 35 to 44",
        4: "Age 45 to 54", 5: "Age 55 to 64", 6: "Age 65 or older"
    },
    "_BMI5CAT": {
        1: "Underweight", 2: "Normal Weight", 3: "Overweight", 4: "Obese"
    }
}

# -----------------------
# GUI
# -----------------------
root = tk.Tk()
root.title("Predicción de Diabetes Tipo 2 (CatBoost)")
root.geometry("700x500")

frame = tk.Frame(root, padx=12, pady=12)
frame.pack(fill="both", expand=True)

# -----------------------
# Formulario
# -----------------------
form_frame = tk.Frame(frame)
form_frame.grid(row=0, column=0, columnspan=8, pady=12, sticky="w")

entry_vars = {}

for i, col in enumerate(columnas):
    tk.Label(form_frame, text=col, font=("Arial", 12), width=20, anchor="w").grid(row=i, column=0, padx=4, pady=6)
    combo = ttk.Combobox(form_frame, font=("Arial", 12), width=40, state="readonly")
    opciones = [f"{k} - {v}" for k, v in opciones_combobox[col].items()]
    combo["values"] = opciones
    combo.grid(row=i, column=1, padx=4, pady=6)
    entry_vars[col] = combo

# -----------------------
# Parseo de valores
# -----------------------
def parse_entry_values():
    values = {}
    for col in columnas:
        s = entry_vars[col].get().strip()
        if s == "":
            values[col] = np.nan
            continue
        try:
            codigo = int(s.split(" - ")[0])
        except:
            codigo = np.nan
        if codigo in MISSING_VALUES:
            codigo = np.nan
        values[col] = float(codigo)
    return values

# -----------------------
# Resultado
# -----------------------
resultado_var = tk.StringVar()
tk.Label(frame, textvariable=resultado_var, font=("Arial", 14), fg="darkblue").grid(row=1, column=0, columnspan=8, pady=12)

# -----------------------
# Predicción
# -----------------------
def predecir():
    resultado_var.set("")
    try:
        input_values = parse_entry_values()
        print("VALORES FORMULARIO:", input_values)

        entrada_df = pd.DataFrame([{col: input_values.get(col, np.nan) for col in columnas_cb}])

        num_cols = entrada_df.select_dtypes(include=[np.number]).columns
        if len(num_cols) > 0:
            entrada_df[num_cols] = SimpleImputer(strategy="mean").fit_transform(entrada_df[num_cols])

        for col in cat_cols_cb:
            if col in entrada_df.columns:
                entrada_df[col] = entrada_df[col].apply(
                    lambda x: "missing" if pd.isna(x)
                    else str(int(x)) if isinstance(x, (float, int)) and not pd.isna(x)
                    else str(x)
                )

        clase = modelo_cb.predict(entrada_df)[0]
        interpretacion_txt = "Sí diabetes" if clase == 1 else "No diabetes"
        resultado_var.set(f"Resultado: {interpretacion_txt}")

    except Exception as e:
        resultado_var.set(f"Error en la predicción: {e}")
        print("Error:", e)

# Botón
tk.Button(frame, text="Predecir", command=predecir, font=("Arial", 12), bg="lightblue").grid(row=3, column=0, pady=12)

root.mainloop()

