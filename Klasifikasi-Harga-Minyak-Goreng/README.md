# 🥥 Proyek Klasifikasi Harga Minyak Goreng

Repositori ini berisi proyek *machine learning* untuk membangun model klasifikasi menggunakan **Jaringan Saraf Tiruan (JST)**. Tujuan model ini adalah untuk mengkategorikan harga minyak goreng (misalnya: murah, sedang, mahal) berdasarkan fitur-fitur tertentu.

---
## Deskripsi Proyek
Proyek ini mengimplementasikan JST untuk menyelesaikan masalah klasifikasi multi-kelas. Alur kerja mencakup persiapan data, pembuatan arsitektur model JST, pelatihan, dan evaluasi untuk melihat seberapa akurat model dapat mengklasifikasikan harga minyak goreng.

---
## Dataset
Dataset yang digunakan adalah `harga_minyak_dummy.csv`, yang merupakan data sampel berisi atribut-atribut produk minyak goreng seperti:
- **Merek**
- **Volume (ml)**
- **Jenis Kemasan**
- **Lokasi Penjualan**
- **Kategori_Harga** (Variabel target)

---
## Alur Kerja Proyek
1.  **Eksplorasi Data (EDA)**: Menganalisis dan memahami data awal.
2.  **Pra-pemrosesan Data**: Menangani data kategorikal (misalnya dengan *One-Hot Encoding*) dan melakukan penskalaan pada data numerik.
3.  **Pemodelan JST**: Merancang arsitektur Jaringan Saraf Tiruan menggunakan TensorFlow/Keras.
4.  **Pelatihan & Evaluasi**: Melatih model dengan data training dan mengevaluasi kinerjanya menggunakan metrik seperti *Accuracy* dan *Confusion Matrix*.

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
1.  Pastikan Python dan Jupyter Notebook sudah terpasang.
2.  *Clone* repositori ini ke komputer Anda.
3.  Instal *library* yang dibutuhkan:
    ```bash
    pip install pandas scikit-learn tensorflow matplotlib
    ```
4.  Buka dan jalankan file `JstKlasifikasiHargaminyak.ipynb`.