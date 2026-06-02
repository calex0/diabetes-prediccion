

## **Crear un entorno con Python 3.9**

CatBoost funciona perfecto en:

- Ubuntu 22.04
- Python 3.9
- CPU‑only



```bash
cd ~/diabetes-prediccion-main/app
```

Crear un entorno así:

```bash
sudo apt install python3.9 python3.9-venv
python3.9 -m venv app_diabetes_env39
source app_diabetes_env39/bin/activate
pip install --upgrade pip
pip install catboost
```

