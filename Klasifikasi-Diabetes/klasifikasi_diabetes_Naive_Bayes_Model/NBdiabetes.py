import streamlit as st
import numpy as np
import joblib

# Muat model Naive Bayes dan scaler
# PERUBAHAN: Menggunakan model Naive Bayes yang baru
model = joblib.load("naive_bayes_model.sav")
scaler = joblib.load("scaler.sav")

# Fungsi prediksi
def predict_diabetes(input_data):
    # Normalisasi input menggunakan scaler
    input_data_scaled = scaler.transform(np.array(input_data).reshape(1, -1))
    prediction = model.predict(input_data_scaled)
    return prediction[0] # Mengembalikan hasil prediksi (0 atau 1)

# Streamlit UI
st.title("Sistem Prediksi Diabetes Menggunakan Naïve Bayes")
st.write("Masukkan data pasien untuk memprediksi kemungkinan diabetes.")

# Input fitur dari pengguna
pregnancies = st.number_input("Jumlah Kehamilan (Pregnancies)", 0, 20, step=1)
glucose = st.number_input("Kadar Glukosa (Glucose)", 0.0, 300.0, step=1.0)
blood_pressure = st.number_input("Tekanan Darah (Blood Pressure)", 0.0, 200.0, step=1.0)
skin_thickness = st.number_input("Ketebalan Kulit (Skin Thickness)", 0.0, 100.0, step=1.0)
insulin = st.number_input("Kadar Insulin (Insulin)", 0.0, 900.0, step=1.0)
bmi = st.number_input("Indeks Massa Tubuh (BMI)", 0.0, 70.0, step=0.1)
dpf = st.number_input("Fungsi Silsilah Diabetes (Diabetes Pedigree Function)", 0.0, 2.5, step=0.01)
age = st.number_input("Usia (Age)", 0, 120, step=1)


# Tombol untuk prediksi
if st.button("Prediksi"):
    input_features = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]
    
    # Lakukan prediksi
    result = predict_diabetes(input_features)
    
    # Tampilkan hasil
    st.subheader("Hasil Prediksi:")
    if result == 1:
        st.error("Pasien terindikasi **Diabetes**.")
    else:
        st.success("Pasien terindikasi **Tidak Diabetes**.")