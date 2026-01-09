# Datos

Este repositorio no incluye datos crudos ni procesados.

## Descarga (Kaggle CLI)
1) Configura kaggle.json en ~/.kaggle/
2) Descarga el dataset a data/raw

Comando:
kaggle datasets download -d ranadeep/credit-risk-dataset -p data/raw --unzip

## Estructura
data/raw: datos originales descargados
data/processed: datos limpios generados por el notebook
