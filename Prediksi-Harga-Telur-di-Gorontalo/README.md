# 🥚 Proyek Prediksi Harga Telur Ayam

Repositori ini berisi proyek *machine learning* untuk melakukan peramalan (*forecasting*) harga telur ayam ras di pasar modern. Model Jaringan Saraf Tiruan (JST) dibangun dan dilatih menggunakan data harga historis untuk memprediksi tren harga di masa mendatang.

---
## Deskripsi Proyek
Tujuan utama proyek ini adalah menerapkan model Jaringan Saraf Tiruan untuk masalah peramalan deret waktu (*time-series forecasting*). Alur kerja mencakup analisis data, pra-pemrosesan, perancangan arsitektur model, pelatihan, hingga evaluasi untuk mengukur akurasi prediksi harga.

---
## Dataset
Dataset yang digunakan adalah `harga-telur-ayam-di-pasar-modern-periode-juli-2024-2025.csv`, yang berisi data historis harga harian telur ayam ras di pasar modern.

---
## Alur Kerja Proyek
1.  **Eksplorasi Data**: Menganalisis dan memvisualisasikan data deret waktu untuk melihat pola dan tren harga.
2.  **Pra-pemrosesan Data**: Melakukan normalisasi data harga dan mengubahnya menjadi format sekuens (proses *windowing*) agar sesuai untuk model JST.
3.  **Pemodelan JST**: Membangun arsitektur Jaringan Saraf Tiruan (misalnya, MLP atau LSTM) menggunakan TensorFlow/Keras.
4.  **Pelatihan & Evaluasi**: Melatih model dengan data historis dan mengevaluasi kinerjanya menggunakan metrik seperti RMSE (*Root Mean Squared Error*).

---
## Teknologi yang Digunakan
* Python
* Jupyter Notebook
* Pandas
* Scikit-learn
* TensorFlow / Keras
* Matplotlib

---
## Cara Menjalankan
1.  Pastikan Anda memiliki Python dan Jupyter Notebook terpasang.
2.  *Clone* repositori ini ke komputer Anda.
3.  Instal *library* yang dibutuhkan:
    ```bash
    pip install pandas scikit-learn tensorflow matplotlib
    ```
4.  Buka dan jalankan file `PEMODELAN PREDIKSI HARGA TELUR_UAS_JST.ipynb`.