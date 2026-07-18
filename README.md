# CNC Predictive Maintenance System

Bu proje, CNC makinelerinden gelen sensör verilerini kullanarak makinenin arızalanma riskini önceden tahmin eden uçtan uca bir "Kestirimci Bakım" (Predictive Maintenance) sistemidir.

## Proje Hakkında
Sistem, makine sensörlerinden gelen verileri (spindle speed, vibration, temperature vb.) işleyerek Random Forest algoritması ile arıza tahmini yapar. FastAPI ile bir backend servisi ve Streamlit ile kullanıcı dostu bir dashboard içerir.

## Kullanılan Teknolojiler
- **Python**
- **Machine Learning:** Scikit-Learn (Random Forest)
- **Backend:** FastAPI
- **Frontend/Dashboard:** Streamlit
- **Veri İşleme:** Pandas, Joblib, Pathlib

## Proje Yapısı
- `/api`: FastAPI backend servis dosyaları.
- `/data`: Ham ve işlenmiş veri setleri.
- `/models`: Eğitilmiş ML modelleri ve scaler dosyaları.
- `/notebooks`: EDA ve model eğitim adımlarının bulunduğu Jupyter dosyaları.
- `dashboard.py`: Streamlit ile hazırlanan kullanıcı arayüzü.

## Kurulum ve Çalıştırma

1. **Gerekli kütüphaneleri yükleyin:**
   ```bash
   pip install -r requirements.txt

2. **Backend (API) servisini başlatın:**
   ```bash
   uvicorn api.main:app --reload

3. **Dashboard'u başlatın (Ayrı bir terminalde):**
   ```bash
   streamlit run dashboard.py

4. **Tarayınızda açın:**
   http://localhost:8501 adresine giderek dashboard'u kullanabilirsiniz.

