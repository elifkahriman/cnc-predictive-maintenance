# CNC Predictive Maintenance Pipeline

An end-to-end predictive maintenance project utilizing synthetic data, FastAPI, and Streamlit. This project demonstrates how to predict potential CNC machine failures based on historical sensor readings and operational parameters.

## 📌 Project Overview
* **Data Generation:** Synthetic sensor data generated to simulate CNC machine behavior under normal and failure conditions (`np.random.seed(42)`).
* **Feature Engineering:** Partially executed via SQL window functions for creating lagged features (e.g., `prev_temperature_c`, `prev_vibration_mm_s`).
* **Machine Learning:** Classification models trained to predict failure risk using historical context.
* **Deployment:** A FastAPI backend serving the champion model (XGBoost) and an interactive Streamlit interface where engineers can input current spindle speed and previous sensor readings to get an instant failure risk prediction.

## ⚠️ Methodology & Data Notes

**1. Data Leakage Fix:**
Earlier versions of this model included current sensor readings (temperature, vibration) as features. Since these simultaneous values were used to generate the failure labels, this caused data leakage and artificially inflated accuracy (~96-99%).

The model was retrained using only forward-looking features (previous readings + spindle speed), better reflecting a true predictive maintenance scenario. This resulted in more realistic performance metrics, shown below.

**2. Synthetic Data Limitations:**
The synthetic failure injection creates isolated single-point anomalies rather than gradual degradation trends. As a result, lagged features carry limited predictive signal — a known limitation of this synthetic dataset. A production-grade dataset would model progressive sensor drift (e.g., vibration slowly increasing over hours) leading up to a failure event.

## 📊 Model Performance (After Leakage Fix)

| Model | Accuracy | Precision (Failure) | Recall (Failure) | F1-Score (Failure) |
|---|---|---|---|---|
| **Logistic Regression** | 0.55 | 0.05 | 0.62 | 0.10 |
| **Random Forest**       | 0.96 | 0.00 | 0.00 | 0.00 |
| **XGBoost (Champion)**  | 0.75 | 0.06 | 0.38 | 0.11 |

*Note: XGBoost was selected as the champion model as it provided the most realistic balance of identifying failures in a highly imbalanced synthetic dataset without collapsing to the majority class.*

## 📂 Project Structure
```text
├── api/
│   └── main.py                          # FastAPI application and endpoint logic
├── data/                                # Raw, cleaned, and feature-engineered datasets
├── models/                              # Serialized champion model and scaler (.pkl)
├── notebooks/
│   ├── 01_data_generation.ipynb         # Synthetic sensor data + failure injection
│   ├── 02_eda_and_visualization.ipynb   # Correlation analysis, visual exploration
│   ├── 03_data_preprocessing.ipynb      # Null handling, text normalization
│   ├── 04_sql_feature_engineering.ipynb # SQL LAG() window functions
│   └── 05_modeling.ipynb                # Model training, evaluation, export
├── dashboard.py                         # Streamlit user interface
├── README.md
└── requirements.txt
```

## 🚀 Installation & Usage

1. **Clone the repository:**
```bash
   git clone https://github.com/elifkahriman/cnc-predictive-maintenance.git
   cd cnc-predictive-maintenance
```

2. **Install required dependencies:**
```bash
   pip install -r requirements.txt
```

3. **Start the Backend (API) service:**
```bash
   uvicorn api.main:app --reload
```

4. **Start the Dashboard (in a separate terminal):**
```bash
   streamlit run dashboard.py
```

5. **Access the application:**
   Open your web browser and navigate to `http://localhost:8501`

