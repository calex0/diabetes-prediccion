####  LEERME — Conversión de datos SAS XPT a CSV

## Descripción

Este guión en Python permite convertir archivos en formato **XPT (SAS Transport Format)** al formato **CSV**, facilitando su uso en entornos de análisis como `pandas`, `scikit-learn` o `cuML`. El archivo original `LLCP2014.XPT` proviene del sistema estadístico **SAS** y contiene datos de salud pública utilizados en el proyecto.

------

## Requisitos

Antes de ejecutar el guión, hay que tener instaladas la siguiente dependencia:

```bash
pip install pandas xport
```

------

## Uso

Ejecución del guión desde la terminal o un entorno Python:

```bash
python xpt_to_csv.py
```

Esto realizará:

1. La lectura del archivo `LLCP2014.XPT`.
2. La conversión a un DataFrame de `pandas`.
3. La exportación del contenido a `LLCP2014.csv`.



## Notas

- El archivo `.XPT` debe estar en el mismo directorio que el guión.
- El formato XPT es común en estudios clínicos y epidemiológicos, y este guión permite su integración en flujos de trabajo reproducibles en Python.
- El CSV generado conserva la estructura original de las variables, facilitando su análisis posterior.

