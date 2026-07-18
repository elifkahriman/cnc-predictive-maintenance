# Predictive Maintenance System

## 📌 Business Problem & Project Objective
Unexpected machine failures in production lines lead to significant downtime and financial losses. This project implements an end-to-end machine learning pipeline that analyzes machine sensor data to proactively predict potential failures and optimize maintenance schedules.

## ⚙️ System Architecture
1. **Data Processing & Modeling:** Time-series feature engineering (lag/window functions) and anomaly prediction using a Random Forest classifier. A chronological split is applied to prevent data leakage.
2. **Backend API:** Fast and asynchronous API service built with FastAPI for model inference.
3. **User Interface:** Interactive Streamlit dashboard for field engineers to monitor real-time machine health and risk status.

## 🚀 Tech Stack
* **Modeling:** scikit-learn, Pandas, NumPy
* **Backend:** FastAPI, Uvicorn
* **Frontend:** Streamlit
* **Database:** SQLite

## 🔧 Installation & Usage

1. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt

2. **Start the Backend (API) service:**
   ```bash
   uvicorn api.main:app --reload

3. **Start the Dashboard (in a separate terminal):**
   ```bash
   streamlit run dashboard.py

4. **Access the application:**
   Open your web browser and navigate to http://localhost:8501


