# Credit Risk Analysis Project

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Un proyecto completo de Machine Learning para predecir el riesgo de incumplimiento (default) en préstamos personales, utilizando datos históricos de LendingClub y técnicas avanzadas de modelado predictivo.

## 📊 Objetivo del Proyecto

Desarrollar y evaluar modelos de clasificación que permitan:
- Predecir la probabilidad de incumplimiento de préstamos
- Optimizar decisiones de aprobación/rechazo
- Minimizar pérdidas financieras manteniendo tasas de aprobación competitivas
- Interpretar los factores de riesgo más relevantes

---

## 🗂️ Estructura del Proyecto

```
credit_risk/
├── data/
│   ├── raw/              # Datos originales (no incluidos en repo)
│   ├── processed/        # Datos procesados (no incluidos en repo)
│   └── sample_data.csv   # Muestra de 1000 registros anonimizados (DEMO)
│
├── notebooks/
│   ├── 01_eda.ipynb                    # Análisis exploratorio
│   ├── 02_models.ipynb                 # Modelos baseline
│   ├── 03_advanced_models.ipynb        # XGBoost, Random Forest
│   └── 04_explainability.ipynb         # SHAP, interpretabilidad
│
├── reports/
│   └── figures/          # Visualizaciones y gráficos
│
├── requirements.txt      # Dependencias Python
└── README.md            # Este archivo
```

---

## 📥 Cómo Obtener los Datos

**⚠️ IMPORTANTE: Este repositorio NO incluye los datos completos por privacidad.**

### Opción 1: Dataset Público de Kaggle (RECOMENDADO)

Los datos provienen del dataset público de LendingClub en Kaggle:

1. **Descarga desde Kaggle:**
   - Dataset: [LendingClub Loan Data](https://www.kaggle.com/datasets/wordsforthewise/lending-club)
   - Requiere cuenta gratuita de Kaggle

2. **Usando Kaggle API:**
   ```bash
   # Instalar Kaggle CLI
   pip install kaggle
   
   # Configurar credenciales (~/.kaggle/kaggle.json)
   # Descargar dataset
   kaggle datasets download -d wordsforthewise/lending-club
   
   # Descomprimir
   unzip lending-club.zip -d data/raw/
   ```

3. **Colocar archivos:**
   ```
   data/raw/
   ├── loan.csv              # Dataset principal (~2GB)
   └── LCDataDictionary.xlsx # Diccionario de variables
   ```

### Opción 2: Usar Datos de Ejemplo (DEMO)

Para pruebas rápidas, el repositorio incluye `data/sample_data.csv` con 1000 registros anonimizados.

**⚠️ Limitaciones:**
- Solo 1000 registros (vs ~2.2M completos)
- Datos anonimizados (sin nombres, descripciones)
- Suficiente para probar código, no para análisis robusto

---

## 🚀 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/[TU-USUARIO]/credit_risk.git
cd credit_risk
```

### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Obtener datos (ver sección anterior)

### 5. Ejecutar notebooks
```bash
jupyter notebook notebooks/
```

**Orden recomendado:**
1. `01_eda.ipynb` - Exploración inicial
2. `02_models.ipynb` - Modelos baseline (Regresión Logística)
3. `03_advanced_models.ipynb` - XGBoost, Random Forest
4. `04_explainability.ipynb` - SHAP, interpretabilidad

---

## 🔍 Resumen de Análisis

### 1. Análisis Exploratorio (EDA)
**Notebook:** `01_eda.ipynb`

- **Carga de datos:** Dataset de ~2.2M préstamos históricos
- **Definición del target:** Variable `target_bad` (1 = Default/Charged Off, 0 = Paid)
- **Limpieza:**
  - Eliminación de variables con data leakage (pagos futuros, recuperaciones)
  - Filtrado de columnas irrelevantes (IDs, textos libres)
- **Análisis descriptivo:** Distribuciones, correlaciones, patrones

### 2. Modelado Baseline
**Notebook:** `02_models.ipynb`

- **Preprocesamiento:**
  - Imputación de valores faltantes
  - Encoding de variables categóricas (OneHotEncoder)
  - Split temporal train/test
- **Modelo baseline:** Regresión Logística
- **Métricas:**
  - ROC-AUC Score
  - Precision-Recall
  - Tasa de aprobación vs Tasa de malos aprobados
- **Optimización de umbral:** Selección del punto de corte óptimo

### 3. Modelos Avanzados
**Notebook:** `03_advanced_models.ipynb`

- **Algoritmos:**
  - Random Forest
  - XGBoost (Gradient Boosting)
- **Feature engineering:** Creación de variables derivadas
- **Comparación de modelos:** Performance metrics
- **Tuning de hiperparámetros**

### 4. Explicabilidad
**Notebook:** `04_explainability.ipynb`

- **SHAP Values:** Interpretabilidad de predicciones
- **Feature importance:** Variables más relevantes
- **Análisis de casos:** Explicación de decisiones individuales

---

## 🔧 Tecnologías Utilizadas

- **Python 3.9+**
- **Pandas, NumPy:** Manipulación de datos
- **Scikit-learn:** Modelado y preprocesamiento
- **XGBoost:** Gradient Boosting avanzado
- **SHAP:** Interpretabilidad de modelos
- **Matplotlib, Seaborn:** Visualización
- **Jupyter Notebook:** Análisis interactivo

---

## 📈 Próximos Pasos (Roadmap)

- [ ] **Refactorización:** Mover lógica a scripts modulares en `src/`
- [ ] **Feature Engineering:** Ingeniería de características avanzada
- [ ] **Ensemble Methods:** Stacking, Voting Classifiers
- [ ] **Despliegue:** API REST con FastAPI/Flask
- [ ] **Monitoring:** Tracking de model drift
- [ ] **Dashboard:** Visualización interactiva con Streamlit/Dash

---

## ⚠️ Privacidad y Uso Responsable

**Este proyecto es solo con fines educativos y de investigación.**

- Los datos originales de LendingClub son públicos pero contienen información sensible
- **NUNCA** uses este código para tomar decisiones reales de crédito sin validación apropiada
- Respeta las regulaciones de privacidad (GDPR, CCPA) al manejar datos
- Los modelos mostrados son demostrativos y requieren validación rigurosa para uso productivo

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver archivo `LICENSE` para más detalles.

---

## 👤 Autor

**[Tu Nombre]**
- GitHub: [@[tu-usuario]](https://github.com/[tu-usuario])
- LinkedIn: [tu-perfil](https://linkedin.com/in/[tu-perfil])

---

## 🙏 Agradecimientos

- **LendingClub:** Por proveer los datos públicos
- **Kaggle:** Por hospedar y facilitar acceso al dataset
- Comunidad de Data Science por las herramientas open-source

