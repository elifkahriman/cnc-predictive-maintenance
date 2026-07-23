import streamlit as st
import requests

st.title("CNC Machine Health Dashboard")
st.subheader("Enter Sensor Data (based on previous readings)")

spindle_speed = st.number_input("Spindle Speed (RPM)", value=0.0)
prev_temp = st.number_input("Previous Temperature (°C)", value=0.0)
prev_vibration = st.number_input("Previous Vibration (mm/s)", value=0.0)

if st.button("Predict"):
    payload = {
        "spindle_speed_rpm": spindle_speed,
        "prev_temperature_c": prev_temp,
        "prev_vibration_mm_s": prev_vibration
    }
    
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        response.raise_for_status()
        result = response.json()
        
        prob = result.get("failure_probability", 0.0)
        st.info(f"Calculated Failure Risk: {prob:.1%}")
        
        if result["prediction"] == 1:
            st.error(f"Warning: {result['warning']}")
        else:
            st.success(f"Status: {result['warning']}")
            
    except requests.exceptions.RequestException:
        st.error("Error connecting to the API")