import streamlit as st
import requests
st.title("CNC Machine Health Dahboard")

st.subheader("Enter Sensor Data")
spindle_speed=st.number_input("Spindle Speed (RPM)", value=0.0)
vibration = st.number_input("Vibration (mm/s)", value=0.0)
temp = st.number_input("Temperature (°C)", value=0.0)
prev_temp = st.number_input("Previous Temperature (°C)", value=0.0)
prev_vibration = st.number_input("Previous Vibration (mm/s)", value=0.0)

if st.button("Predict"):
    payload={
        "spindle_speed_rpm": spindle_speed,
        "vibration_mm_s": vibration,
        "temperature_c": temp,
        "prev_temperature_c": prev_temp,
        "prev_vibration_mm_s": prev_vibration
    }
    
    response=requests.post("http://127.0.0.1:8000/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        if result["prediction"] == 1:
            st.error(f"Warning: {result['warning']}")
        else:
            st.success(f"Status: {result['warning']}")

    else:
        st.error("Error connecting to the API")