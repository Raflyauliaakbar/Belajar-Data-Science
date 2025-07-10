# 🩺 Proyek Klasifikasi Penyakit Jantung

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NAMA_USER_ANDA/NAMA_REPO_ANDA/blob/main/Klasifikasi_Heart_Praktikum_Random_forest_model.ipynb)

Repositori ini berisi proyek *data science* untuk membangun dan mengevaluasi model *machine learning* yang dapat memprediksi keberadaan penyakit jantung pada pasien berdasarkan atribut medis. Proyek ini mencakup analisis data mendalam, perbandingan beberapa model, optimasi, hingga persiapan untuk *deployment*.

---

##  Deskripsi Proyek
Tujuan utama proyek ini adalah untuk menerapkan alur kerja *end-to-end* dalam ilmu data, mulai dari eksplorasi data hingga menemukan model klasifikasi dengan performa terbaik. Model yang telah dioptimalkan kemudian disimpan untuk dapat digunakan dalam aplikasi web interaktif.

---

## Dataset
Dataset yang digunakan adalah `heart_desease_data.csv`, yang berisi 14 atribut medis, termasuk variabel target yang menunjukkan keberadaan penyakit jantung (1) atau tidak (0).

**Fitur utama:**
- **age**: Usia pasien
- **sex**: Jenis kelamin (1 = laki-laki; 0 = perempuan)
- **cp**: Tipe nyeri dada (*chest pain type*)
- **trestbps**: Tekanan darah saat istirahat
- **chol**: Kadar kolesterol
- **thalach**: Detak jantung maksimum yang tercapai
- **target**: 0 = Tidak ada penyakit jantung, 1 = Ada penyakit jantung

---

## ⚙️ Alur Kerja Proyek
Proyek ini mengikuti alur kerja yang sistematis untuk memastikan hasil yang robust dan andal:
1.  **Eksplorasi Data (EDA)**: Menganalisis data secara visual untuk memahami distribusi, korelasi antar fitur, dan hubungannya dengan variabel target menggunakan *heatmap*, *countplot*, dan *histogram*.
2.  **Pra-pemrosesan Data**: Melakukan penskalaan fitur menggunakan `StandardScaler` untuk menormalisasi rentang nilai data.
3.  **Perbandingan Model**: Melatih dan mengevaluasi 5 model klasifikasi yang berbeda (Logistic Regression, Naive Bayes, SVM, Decision Tree, dan Random Forest) untuk menemukan algoritma dengan performa dasar terbaik.
4.  **Optimasi Model (Hyperparameter Tuning)**: Menggunakan `GridSearchCV` untuk mencari kombinasi *hyperparameter* terbaik dari model Random Forest yang terpilih, guna meningkatkan akurasinya.
5.  **Validasi Akhir**: Mengevaluasi model yang telah dioptimalkan menggunakan **10-Fold Cross-Validation** untuk mendapatkan estimasi performa yang stabil dan meyakinkan.
6.  **Penyimpanan Model**: Menyimpan model final yang telah dilatih dan *scaler* ke dalam file `.sav` menggunakan `joblib` untuk persiapan *deployment*.

---

## 📊 Hasil & Performa Model
Setelah melalui proses perbandingan dan optimasi, ditemukan bahwa **Random Forest** memberikan performa terbaik.

- **Akurasi Awal (Default):** 81.96%
- **Akurasi Setelah Tuning:** **86.88%** 🚀

Evaluasi akhir dengan *10-Fold Cross-Validation* pada model yang telah dioptimalkan menunjukkan **akurasi rata-rata yang stabil**, membuktikan bahwa model ini dapat diandalkan.

---

## 🛠️ Teknologi yang Digunakan
- **Analisis Data:** Python, Pandas, Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Deployment (Direncanakan):** Streamlit, Joblib
- **Lingkungan Kerja:** Jupyter Notebook / Google Colab

---

## Cara Menjalankan

### 1. Menjalankan Notebook Analisis
1.  Pastikan Anda memiliki Python dan Jupyter Notebook terpasang.
2.  *Clone* repositori ini:
    ```bash
    git clone [https://github.com/NAMA_USER_ANDA/NAMA_REPO_ANDA.git](https://github.com/NAMA_USER_ANDA/NAMA_REPO_ANDA.git)
    ```
3.  Instal *library* yang dibutuhkan:
    ```bash
    pip install pandas scikit-learn matplotlib seaborn jupyter
    ```
4.  Buka dan jalankan file `Klasifikasi_Heart_Praktikum_Random_forest_model.ipynb`.

### 2. Menjalankan Aplikasi Web (Jika `app.py` sudah dibuat)
1.  Pastikan semua file (`app.py`, `model_jantung.sav`, `scaler_jantung.sav`) berada di dalam satu folder.
2.  Instal Streamlit:
    ```bash
    pip install streamlit
    ```
3.  Jalankan aplikasi dari terminal:
    ```bash
    streamlit run app.py
    ```