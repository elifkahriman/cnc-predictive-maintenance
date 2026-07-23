from pathlib import Path
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="CNC Predictive Maintenance API")

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "models" / "xgboost_model.pkl")
scaler = joblib.load(BASE_DIR / "models" / "robust_scaler.pkl")
 
class SensorData(BaseModel):
    spindle_speed_rpm: float
    prev_temperature_c: float
    prev_vibration_mm_s: float

@app.get("/")
def read_root():
    return {"status":"API is running"}

@app.post("/predict")
def predict_failure(data: SensorData):
    input_df = pd.DataFrame([data.model_dump()])
    scaled_features = scaler.transform(input_df)
    
    probabilities = model.predict_proba(scaled_features)[0]
    failure_prob = probabilities[1]
    
    # Lowered threshold for higher sensitivity to anomalies
    THRESHOLD = 0.30
    prediction = 1 if failure_prob>= THRESHOLD else 0
    
    warning = "High Risk of Failure" if prediction == 1 else "Normal Operation"
    
    return {
        "prediction": int(prediction), 
        "warning": warning,
        "failure_probability": float(failure_prob)
    }