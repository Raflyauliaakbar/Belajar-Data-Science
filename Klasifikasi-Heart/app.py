import streamlit as st
import numpy as np
import pandas as pd
import joblib

# --- Muat Model dan Scaler ---
# Pastikan file-file ini berada di folder yang sama dengan app.py
try:
    model = joblib.load("model_jantung.sav")
    scaler = joblib.load("scaler_jantung.sav")
except FileNotFoundError:
    st.error("File model atau scaler tidak ditemukan. Pastikan file .sav sudah ada di folder yang sama.")
    st.stop()

# --- Judul dan Deskripsi Aplikasi ---
st.set_page_config(page_title="Prediksi Penyakit Jantung", layout="wide")
st.title("🩺 Aplikasi Prediksi Penyakit Jantung")
st.write("""
Aplikasi ini menggunakan model **Random Forest** untuk memprediksi kemungkinan seseorang menderita penyakit jantung berdasarkan data medis mereka.
Masukkan data Anda pada panel di sebelah kiri.
""")

# --- Sidebar untuk Input Pengguna ---
st.sidebar.header("Masukkan Data Pasien:")

def user_input_features():
    age = st.sidebar.slider('Usia (Age)', 29, 77, 55)
    sex = st.sidebar.selectbox('Jenis Kelamin (Sex)', ('Laki-laki (1)', 'Perempuan (0)'))
    cp = st.sidebar.selectbox('Tipe Nyeri Dada (CP)', ('Tipe 0', 'Tipe 1', 'Tipe 2', 'Tipe 3'))
    trestbps = st.sidebar.slider('Tekanan Darah (trestbps)', 94, 200, 120)
    chol = st.sidebar.slider('Kolesterol (chol)', 126, 564, 240)
    fbs = st.sidebar.selectbox('Gula Darah Puasa > 120 mg/dl (fbs)', ('Tidak (0)', 'Ya (1)'))
    restecg = st.sidebar.selectbox('Hasil Elektrokardiografi (restecg)', ('Normal (0)', 'Abnormalitas ST-T (1)', 'Hipertrofi Ventrikel (2)'))
    thalach = st.sidebar.slider('Detak Jantung Maksimum (thalach)', 71, 202, 150)
    exang = st.sidebar.selectbox('Angina Akibat Olahraga (exang)', ('Tidak (0)', 'Ya (1)'))
    oldpeak = st.sidebar.slider('Depresi ST (oldpeak)', 0.0, 6.2, 1.0)
    slope = st.sidebar.selectbox('Kemiringan Segmen ST (slope)', ('Naik (0)', 'Datar (1)', 'Menurun (2)'))
    ca = st.sidebar.selectbox('Jumlah Pembuluh Darah Utama (ca)', ('0', '1', '2', '3'))
    thal = st.sidebar.selectbox('Thalassemia (thal)', ('Normal (0)', 'Cacat Tetap (1)', 'Cacat Reversibel (2)'))

    # Konversi input menjadi format angka
    sex_val = 1 if sex.startswith('Laki-laki') else 0
    cp_val = int(cp.split(' ')[1])
    fbs_val = 1 if fbs.startswith('Ya') else 0
    restecg_val = int(restecg.split('(')[1][0])
    exang_val = 1 if exang.startswith('Ya') else 0
    slope_val = int(slope.split('(')[1][0])
    ca_val = int(ca)
    thal_val = int(thal.split('(')[1][0])

    data = {
        'age': age, 'sex': sex_val, 'cp': cp_val, 'trestbps': trestbps,
        'chol': chol, 'fbs': fbs_val, 'restecg': restecg_val, 'thalach': thalach,
        'exang': exang_val, 'oldpeak': oldpeak, 'slope': slope_val, 'ca': ca_val,
        'thal': thal_val
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# --- Tampilkan Data Input ---
st.subheader("Data Input Pasien:")
st.write(input_df)

# --- Tombol Prediksi ---
if st.button('Lakukan Prediksi'):
    # Scaling data input
    input_scaled = scaler.transform(input_df)
    
    # Lakukan prediksi
    prediction = model.predict(input_scaled)
    prediction_proba = model.predict_proba(input_scaled)

    st.subheader('Hasil Prediksi:')
    if prediction[0] == 1:
        st.error(f"**Pasien Terindikasi Menderita Penyakit Jantung** (Probabilitas: {prediction_proba[0][1]*100:.2f}%)")
    else:
        st.success(f"**Pasien Tidak Terindikasi Menderita Penyakit Jantung** (Probabilitas: {prediction_proba[0][0]*100:.2f}%)")