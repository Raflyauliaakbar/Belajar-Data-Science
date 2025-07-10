# 🩺 Proyek Klasifikasi Diabetes

Repositori ini berisi proyek praktikum *data science* untuk membangun model *machine learning* yang dapat memprediksi apakah seorang pasien menderita diabetes atau tidak berdasarkan data diagnostik.

---

## Deskripsi Proyek
Tujuan utama proyek ini adalah untuk menerapkan dan membandingkan dua algoritma klasifikasi pada masalah klasifikasi biner. Prosesnya mencakup eksplorasi data, pra-pemrosesan, pembuatan model, hingga evaluasi performa kedua model dalam mengklasifikasikan pasien diabetes.

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
3.  **Pemodelan**: Membagi data menjadi set latih dan uji, kemudian melatih model klasifikasi menggunakan **Random Forest** dan **Naive Bayes**.
4.  **Evaluasi**: Mengukur dan membandingkan kinerja kedua model menggunakan metrik seperti *Accuracy*, *Precision*, *Recall*, dan *Confusion Matrix*.

---

## Perbandingan Model
Dalam proyek ini, dua model klasifikasi digunakan untuk memprediksi diabetes, yaitu Random Forest dan Naive Bayes. Masing-masing memiliki cara kerja, kelebihan, dan kekurangan yang berbeda.

### 🌳 Random Forest
Model ini bekerja dengan membangun banyak "pohon keputusan" (*decision tree*) secara acak dan menggabungkan hasilnya untuk mendapatkan prediksi yang lebih akurat dan stabil.

**Kelebihan:**
- **Akurasi Tinggi**: Sering kali memberikan hasil yang sangat akurat dan performa yang kuat.
- **Tahan Overfitting**: Dengan menggabungkan banyak pohon, model ini mengurangi risiko *overfitting* yang sering terjadi pada satu pohon keputusan.
- **Fleksibel**: Mampu menangani hubungan data yang kompleks dan non-linear.

**Kekurangan:**
- **Kompleks & Lambat**: Membutuhkan lebih banyak sumber daya komputasi dan waktu untuk melatih model.
- **Sulit Diinterpretasikan**: Bekerja seperti *"black box"*, sehingga sulit untuk memahami logika spesifik di balik setiap keputusannya.

### 🧮 Naive Bayes
Model ini adalah klasifikasi probabilistik yang menggunakan Teorema Bayes. Ia membuat asumsi "naif" bahwa setiap fitur bersifat independen atau tidak saling memengaruhi.

**Kelebihan:**
- **Sangat Cepat**: Proses pelatihan dan prediksi berlangsung sangat cepat karena perhitungannya sederhana.
- **Performa Baik pada Data Kecil**: Tetap bisa memberikan hasil yang baik meskipun dataset yang digunakan tidak terlalu besar.
- **Mudah Diinterpretasikan**: Logika di balik keputusannya mudah dipahami karena didasarkan pada probabilitas.

**Kekurangan:**
- **Asumsi yang Terlalu Sederhana**: Asumsi bahwa semua fitur independen jarang terjadi di dunia nyata, yang dapat membatasi akurasinya.
- **Kurang Andal untuk Data Kompleks**: Mungkin tidak dapat menangkap pola yang rumit dalam data sebaik model lain.

---

## Teknologi yang Digunakan
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Cara Menjalankan
1. Pastikan Anda memiliki Python dan Jupyter Notebook terpasang.
2. *Clone* repositori ini ke komputer lokal Anda.
   ```bash
   git clone [https://github.com/NAMA_USER/NAMA_REPO.git](https://github.com/NAMA_USER/NAMA_REPO.git)
   ```
3. Instal *library* yang dibutuhkan:
   ```bash
   pip install pandas scikit-learn matplotlib seaborn
   ```
4. Buka dan jalankan file `.ipynb` yang tersedia untuk melihat proses pelatihan masing-masing model.
