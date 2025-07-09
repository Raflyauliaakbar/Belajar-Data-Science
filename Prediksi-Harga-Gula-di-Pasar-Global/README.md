# 📈 Proyek Prediksi Harga Gula Pasir

Repositori ini berisi proyek *machine learning* untuk melakukan peramalan (*forecasting*) harga gula pasir lokal di pasar modern. Dengan menggunakan data harga historis, sebuah model dilatih untuk memprediksi tren harga di masa depan.

---
## Deskripsi Proyek
Proyek ini mengimplementasikan pemodelan deret waktu (*time series*) untuk memprediksi harga sebuah komoditas. Alur kerja mencakup analisis data historis, pra-pemrosesan, pembuatan model prediktif, dan evaluasi untuk mengukur akurasi prediksi.

---
## Dataset
Dataset yang digunakan adalah `harga-gula-pasir-lokal-di-pasar-modern-periode-mei-2024-2025.csv`. Dataset ini berisi data deret waktu mengenai harga harian gula pasir lokal di pasar modern.

---
## Alur Kerja Proyek
1.  **Eksplorasi Data (EDA)**: Menganalisis dan memvisualisasikan data deret waktu untuk mengidentifikasi pola, tren, dan musiman.
2.  **Pra-pemrosesan Data**: Melakukan normalisasi data dan mengubah data menjadi format sekuens (*windowing*) agar dapat diproses oleh model.
3.  **Pemodelan**: Membangun arsitektur model Jaringan Saraf Tiruan (JST), seperti LSTM atau GRU, yang cocok untuk data sekuensial.
4.  **Pelatihan & Evaluasi**: Melatih model dengan data historis dan mengevaluasi kinerjanya menggunakan metrik seperti MAE (Mean Absolute Error) atau RMSE (Root Mean Squared Error).

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
2.  *Clone* repositori ini.
3.  Instal *library* yang dibutuhkan:
    ```bash
    pip install pandas scikit-learn tensorflow matplotlib
    ```
4.  Buka dan jalankan file `PEMODELAN_PREDIKSI_HARGA_Gula_pasir_lokal_di_pasar_modern.ipynb`.