# 🩺 Proyek Klasifikasi Diabetes

Repositori ini berisi proyek praktikum *data science* untuk membangun model *machine learning* yang dapat memprediksi apakah seorang pasien menderita diabetes atau tidak berdasarkan data diagnostik.

---
## Deskripsi Proyek
Tujuan utama proyek ini adalah untuk menerapkan alur kerja *data science* pada masalah klasifikasi biner. Prosesnya mencakup eksplorasi data, pra-pemrosesan, pembuatan model, hingga evaluasi performa model dalam mengklasifikasikan pasien diabetes.

---
## Dataset
Dataset yang digunakan adalah `diabetes.csv`, yang mencakup beberapa fitur medis, di antaranya:
- **Pregnancies**: Jumlah kehamilan
- **Glucose**: Konsentrasi glukosa plasma
- **BloodPressure**: Tekanan darah
- **SkinThickness**: Ketebalan lipatan kulit trisep
- **Insulin**: Kadar insulin serum
- **BMI**: Indeks massa tubuh (Body Mass Index)
- **DiabetesPedigreeFunction**: Fungsi silsilah diabetes
- **Age**: Usia (tahun)
- **Outcome**: Variabel target (0 = tidak diabetes, 1 = diabetes)

---
## Alur Kerja Proyek
1.  **Eksplorasi Data (EDA)**: Menganalisis dan memvisualisasikan data untuk memahami distribusi dan korelasi antar fitur.
2.  **Pra-pemrosesan Data**: Menangani data yang hilang (jika ada) dan melakukan penskalaan fitur agar siap untuk pemodelan.
3.  **Pemodelan**: Membagi data menjadi set latih dan uji, kemudian melatih model klasifikasi (contoh: Logistic Regression, K-Nearest Neighbors, dll.).
4.  **Evaluasi**: Mengukur kinerja model menggunakan metrik seperti *Accuracy*, *Precision*, *Recall*, dan *Confusion Matrix*.

---
## Teknologi yang Digunakan
* Python
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook

---
## Cara Menjalankan
1.  Pastikan Anda memiliki Python dan Jupyter Notebook terpasang.
2.  *Clone* repositori ini.
3.  Instal *library* yang dibutuhkan:
    ```bash
    pip install pandas scikit-learn matplotlib seaborn
    ```
4.  Buka dan jalankan file `praktikum_data_science_klasifikasi_diabetes_6b.ipynb`.