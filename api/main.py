from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from pathlib import Path 

app=FastAPI(title='CNC Predictive Maintenance API')

BASE_DIR= Path(__file__).resolve().parent.parent

rf_model = joblib.load(BASE_DIR / "models" / "random_forest_model.pkl")
scaler = joblib.load(BASE_DIR / "models" / "robust_scaler.pkl")

class SensorData(BaseModel):
    spindle_speed_rpm: float
    vibration_mm_s: float
    temperature_c: float
    prev_temperature_c: float
    prev_vibration_mm_s: float

@app.get("/")
def read_root():
    return {"status": "API is runnning"}

@app.post("/predict")
def predict_failure(data: SensorData):
    input_data=pd.DataFrame([data.model_dump()])

    scaled_features= scaler.transform(input_data)
    prediction=rf_model.predict(scaled_features)[0]

    return {
        "prediction": int(prediction),
        "warning": "Failure Risk Detected" if prediction == 1 else "Machine Normal"
    }