# Credit Risk Analysis Project

Este proyecto tiene como objetivo desarrollar un modelo de Machine Learning para predecir el riesgo de incumplimiento (default) en préstamos. El enfoque es analizar datos históricos, limpiar y procesar la información, y entrenar modelos predictivos para clasificar a los solicitantes.

## Estructura del Proyecto

El proyecto está organizado en las siguientes fases o secciones:

### 1. Análisis Exploratorio de Datos (EDA)
**Ubicación:** `notebooks/01_eda.ipynb`

En esta etapa inicial nos enfocamos en entender los datos crudos. Las actividades principales incluyen:
*   **Carga de Datos:** Importación del dataset `loan.csv`.
*   **Definición del Target:** Construcción de la variable objetivo `target_bad`. Se define qué estados del préstamo constituyen un "incumplimiento" (ej. Charged Off, Default) vs "cumplimiento".
*   **Limpieza y Selección de Variables:** Identificación de columnas irrelevantes (IDs, textos libres) y columnas con "data leakage" (información del futuro, como pagos realizados, recuperaciones, etc.) que no deben usarse para predicción.
*   **Análisis Descriptivo:** Revisión de tipos de datos, valores nulos y distribuciones básicas.

### 2. Modelado Predictivo (Baseline)
**Ubicación:** `notebooks/02_models.ipynb`

Desarrollo del primer modelo base para establecer un punto de comparación.
*   **Preprocesamiento:** Imputación de valores faltantes y codificación de variables categóricas (OneHotEncoding).
*   **Entrenamiento:** Uso de Regresión Logística como modelo baseline.
*   **Evaluación:** Análisis de métricas técnicas (ROC-AUC, Recall, Precision) y métricas de negocio (Tasa de Aprobación, Tasa de Malos Aprobados).
*   **Optimización de Umbral:** Selección del punto de corte óptimo para la decisión de aprobación/rechazo.

### Siguientes Pasos (Roadmap)
*   **Refactorización:** Mover la lógica de limpieza y entrenamiento a scripts modulares en la carpeta `src/`.
*   **Ingeniería de Características:** Crear nuevas variables predictivas.
*   **Modelos Avanzados:** Experimentar con algoritmos más complejos como Random Forest, XGBoost o LightGBM para mejorar el rendimiento.
