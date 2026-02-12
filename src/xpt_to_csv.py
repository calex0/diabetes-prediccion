# xport example.xpt > example.csv

import pandas as pd
import xport

# Cargar el archivo XPT
with open("LLCP2014.XPT", "rb") as file:
    dataset = xport.to_dataframe(file)

# Guardar como CSV
dataset.to_csv("LLCP2014.csv", index=False)

print("Conversión completada: LLCP2014.csv generado.")

