import pyreadstat

# Leer archivo XPT con codificación robusta
df, meta = pyreadstat.read_xport("LLCP2014.XPT", encoding="latin1")

# Guardar como CSV
df.to_csv("LLCP2014.csv", index=False)

print("Conversión completada.")

