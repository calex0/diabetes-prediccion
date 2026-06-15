

## **Crear un entorno con Python 3.9**

Regresión logística:

- Ubuntu 22.04
- Python 3.9
- CPU‑only



```bash
cd ~/diabetes-prediccion-main/app
```

Antes de crear un entorno env hay que instalar Python 3.9. En Ubuntu 26.04 hay que hacer lo siguiente:

```bash
sudo apt update
sudo apt install software-properties-common

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

sudo apt install python3.9 python3.9-venv python3.9-dev python3.9-tk
```
Ahora creamos el entorno python:
```bash
python3.9 -m venv app_diabetes_env39
source app_diabetes_env39/bin/activate
```
