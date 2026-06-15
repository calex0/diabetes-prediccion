import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import joblib
from sklearn.impute import SimpleImputer

# -----------------------
# Variables seleccionadas
# -----------------------
columnas = [
    '_RFHLTH', '_AGE_G','_BMI5CAT', '_RACEG21','WTCHSALT',
    'ASBIRDUC', 'CTELNUM1', 'CTELENUM', 'SCNTMEL1'
]

cat_cols = [
    '_RFHLTH', '_AGE_G','_BMI5CAT', '_RACEG21','WTCHSALT',
    'ASBIRDUC', 'CTELNUM1', 'CTELENUM', 'SCNTMEL1'
]



# -----------------------
# Cargar modelo
# -----------------------
modelo_rl = joblib.load("modelo_rl.pkl")
columnas_rl = joblib.load("columnas_rl.pkl")

# -----------------------
# Opciones de combobox
# -----------------------
opciones_combobox = {
    "_RFHLTH": {
        0: "Good/Excellent",
        1: "Fair",
        2: "Poor"
    },

    "_AGE_G": {
        0: "18-24",
        1: "25-34",
        2: "35-44",
        3: "45-54",
        4: "55-64",
        5: "65+"
    },

    "_BMI5CAT": {
        0: "Underweight",
        1: "Normal",
        2: "Overweight",
        3: "Obese"
    },

    "_RACEG21": {
        0: "White",
        1: "Black",
        2: "Other"
    },

    "WTCHSALT": {
        0: "No",
        1: "Yes",
        2: "Don't know",
        3: "Refused"
    },

    "ASBIRDUC": {
        0: "No",
        1: "Yes",
        2: "Don't know",
        3: "Refused"
    },

    "CTELNUM1": {
        0: "None",
        1: "One phone",
        2: "Two or more"
    },

    "CTELENUM": {
        0: "No",
        1: "Yes",
        2: "Don't know"
    },

    "SCNTMEL1": {
        0: "0 days",
        1: "1–7 days",
        2: "8–14 days",
        3: "15–21 days",
        4: "22–30 days",
        5: "31–60 days",
        6: "61–90 days",
        7: "90+ days"
    }
}


# -----------------------
# GUI
# -----------------------
root = tk.Tk()
root.title("Predicción de Diabetes (Regresión Logística)")
root.geometry("900x750")

# Estilo grande
style = ttk.Style()
style.configure("TCombobox", font=("Arial", 18), padding=6)
root.option_add('*TCombobox*Listbox.font', ('Arial', 18))

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

form_frame = tk.Frame(frame)
form_frame.grid(row=0, column=0, columnspan=8, pady=12, sticky="w")

entry_vars = {}

# -----------------------
# Crear widgets
# -----------------------
row = 0

for col in columnas:
    tk.Label(form_frame, text=col, font=("Arial", 18), width=22, anchor="w").grid(row=row, column=0, padx=6, pady=10)

    if col in cat_cols:
        combo = ttk.Combobox(form_frame, font=("Arial", 18), width=40, state="readonly")
        opciones = [f"{k} - {v}" for k, v in opciones_combobox[col].items()]
        combo["values"] = opciones
        combo.grid(row=row, column=1, padx=6, pady=10)
        entry_vars[col] = combo
    else:
        entry = tk.Entry(form_frame, font=("Arial", 18), width=20)
        entry.grid(row=row, column=1, padx=6, pady=10)
        entry_vars[col] = entry

    row += 1

# -----------------------
# Parseo
# -----------------------
def parse_entry_values():
    values = {}

    for col in columnas:
        widget = entry_vars[col]

        if col in cat_cols:
            s = widget.get().strip()
            if s == "":
                values[col] = np.nan
                continue
            codigo = int(s.split(" - ")[0])
            values[col] = codigo
        else:
            s = widget.get().strip()
            try:
                values[col] = float(s)
            except:
                values[col] = np.nan

    return values

# -----------------------
# Resultado
# -----------------------
resultado_var = tk.StringVar()
tk.Label(frame, textvariable=resultado_var, font=("Arial", 22), fg="darkblue").grid(row=1, column=0, columnspan=8, pady=20)

# -----------------------
# Predicción
# -----------------------
def predecir():
    try:
        input_values = parse_entry_values()
        print("VALORES FORMULARIO:", input_values)

        # Crear DataFrame con TODAS las columnas que espera el modelo
        entrada_df = pd.DataFrame(index=[0], columns=columnas_rl)

        # Inicializar todo a NaN
        entrada_df.loc[0, :] = np.nan

        # Rellenar solo las 10 variables del formulario
        for col, val in input_values.items():
            if col in entrada_df.columns:
                entrada_df.loc[0, col] = val

        # NO imputamos manualmente: el pipeline ya tiene SimpleImputer
        probas = modelo_rl.predict_proba(entrada_df)
        idx_clase0 = list(modelo_rl.classes_).index(0)
        proba = probas[0][idx_clase0]

        clase = modelo_rl.predict(entrada_df)[0]
        
        proba_si = probas[0][0]
        proba_no = probas[0][1]

        interpretacion = "Sí diabetes" if clase == 1 else "No diabetes"
        resultado_var.set(
             f"Resultado: {interpretacion}\n"
             f"Prob. diabetes No: {proba_si:.3f}\n"
             f"Prob. diabetes Sí: {proba_no:.3f}"
)

    except Exception as e:
        resultado_var.set(f"Error: {e}")
        print("Error:", e)


# Botón
tk.Button(frame, text="Predecir", command=predecir, font=("Arial", 20), bg="lightblue").grid(row=3, column=0, pady=20)

root.mainloop()

