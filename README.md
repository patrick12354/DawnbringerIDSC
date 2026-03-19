# 👁️ CorVision: Left Ventricle Segmentation

[![Live Interactive Prototype!](https://img.shields.io/badge/Live_Prototype-Streamlit_Cloud-FF4B4B?style=for-the-badge&logo=streamlit)](https://heartspect.streamlit.app/)

*(Bagi pembaca berbahasa Indonesia, silakan gulir ke bawah untuk versi Bahasa Indonesia / For Indonesian readers, please scroll down for the Indonesian version).*

## English Version

This project aims to build a Deep Learning model (using a 3D U-Net architecture) to automate the segmentation of the left ventricle in Myocardial Perfusion SPECT medical images. The evaluation is based on Dice Score, IoU, and 95% Hausdorff Distance metrics. This project was built to demonstrate **clinical applicability, safety, interpretability, and reproducibility** in automating myocardial perfusion scintigraphy (MPS) analysis.

---

### 🚀 Quick Start: Web Prototype

A ready-to-use local web prototype is provided to demonstrate the model's capabilities in real-time. It features a multi-plane 3D viewer, automatic inference, and a probability map (confidence overlay).

1. **Install Dependencies**
   ```bash
   pip install -r prototype/requirements.txt
   ```
   *(For GPU acceleration, install the appropriate CUDA PyTorch version from [pytorch.org](https://pytorch.org/).)*

2. **Run the Prototype**
   ```bash
   streamlit run prototype/app.py
   ```
   The app will automatically open in your browser at `http://localhost:8501`.

---

### 📁 Repository Structure

```text
heartSPECT/
├── models/             ← Trained PyTorch checkpoints (e.g., best_model.pth)
├── prototype/          ← Streamlit web app UI & inference pipeline
│   ├── app.py          ← Main Streamlit application
│   ├── model.py        ← UNet3D architecture definition
│   └── utils.py        ← Preprocessing and utility functions
├── notebooks/          ← Jupyter notebooks for EDA, training, and evaluation
├── scripts/            ← Utility scripts (e.g., metadata extraction)
├── outputs/            ← Visualizations, training curves, and evaluation plots
├── docs/               ← Dataset guidelines and licensing
└── data/               ← [IGNORED BY GIT] Raw DICOM and processed NIfTI data
```

> **Note on Data:** Due to medical data privacy guidelines and repository size limits, the raw DICOM files and preprocessed NIfTI datasets are **not included** in this GitHub repository. The `.gitignore` rule automatically safely excludes them. 
> 
> However, we have included **5 sample DICOM files** in `prototype/sample_data/` so the web app can be tested out-of-the-box. The trained model weights (~67MB) are also included.
>
> 📥 **Full Dataset Download:** To acquire the complete dataset used in this project, please download the ZIP file directly from [PhysioNet: Myocardial Perfusion SPECT (1.0.0)](https://physionet.org/content/myocardial-perfusion-spect/get-zip/1.0.0/) and extract the DICOM files into the `data/raw/DICOM/` directory.

---

### 🧠 Methodology

**1. Data Preprocessing**
- Volumetric resampling to a uniform `(64, 64, 64)` structure (Target Shape).
- Percentile-based intensity clipping (1st - 99th percentile) to handle anomalies.
- Z-score normalization for robust model input.

**2. Model Architecture**
- **3D U-Net** implemented in PyTorch.
- **Encoder:** 16, 32, 64, 128 channels.
- **Bottleneck:** 256 channels.
- **Output:** Sigmoid activation mapping to a probability mask.
- Total Parameters: **~5.6 Million**.

**3. Loss & Training**
- Mixed objective: `0.5 * Binary Cross Entropy (BCE) + 0.5 * Dice Loss` to handle the severe class imbalance (left ventricle is typically ~1% of the entire volume).
- **Optimizer:** AdamW with Cosine Annealing Learning Rate scheduling.

---

### 📊 Performance & Evaluation
Our model was rigorously evaluated on a held-out test set comprising unseen patient data. The 3D U-Net achieved state-of-the-art volumetric segmentation results:

| Metric | Score | Clinical Significance |
| :--- | :---: | :--- |
| **Dice Similarity Coefficient (DSC)** | **91.4%** | Excellent overlap between the AI's prediction and the expert cardiologist ground truth. |
| **Intersection over Union (IoU)** | **88.2%** | High precision in capturing the exact spatial boundaries of the left ventricle. |
| **ROC-AUC Score** | **0.99** | Exceptional discriminative ability distinguishing the left ventricle from background tissue and neighboring organs. |

*Detailed evaluation reports, including spatial variance and Hausdorff Distance (HD95) plots, can be found in the `outputs/` directory and the main Jupyter notebook.*

---
### ⚖️ Disclaimer

⚠️ **Academic & Research Use Only:** This tool is a research prototype. It is **NOT** intended for clinical diagnosis. Always consult a qualified medical professional for final diagnostic decisions.

<br><br><br>

---
---

## Versi Bahasa Indonesia

Proyek ini bertujuan untuk membangun model *Deep Learning* (menggunakan arsitektur 3D U-Net) guna melakukan otomatisasi segmentasi ventrikel kiri pada citra medis Myocardial Perfusion SPECT. Evaluasi dilakukan berdasarkan metrik Dice Score, IoU, dan Hausdorff Distance 95%. Proyek ini dibangun untuk mendemonstrasikan **aplikabilitas klinis, keamanan, interpretabilitas, dan reproduksibilitas** dalam otomatisasi analisis sintigrafi perfusi miokard.

---

### 🚀 Mulai Cepat: Prototipe Web

Prototipe web lokal yang siap pakai disediakan untuk mendemonstrasikan kemampuan model secara *real-time*. Prototipe ini memiliki penampil 3D multi-bidang, inferensi otomatis, dan peta probabilitas (tingkat keyakinan model).

1. **Instal Dependensi**
   ```bash
   pip install -r prototype/requirements.txt
   ```
   *(Untuk akselerasi GPU, instal versi CUDA PyTorch yang sesuai dari [pytorch.org](https://pytorch.org/).)*

2. **Jalankan Prototipe**
   ```bash
   streamlit run prototype/app.py
   ```
   Aplikasi akan otomatis terbuka pada *browser* Anda di alamat `http://localhost:8501`.

---

### 📁 Struktur Repositori

```text
heartSPECT/
├── models/             ← Checkpoint PyTorch terlatih (misal: best_model.pth)
├── prototype/          ← UI aplikasi web Streamlit & pipeline inferensi
│   ├── app.py          ← Aplikasi utama Streamlit
│   ├── model.py        ← Definisi arsitektur UNet3D
│   └── utils.py        ← Fungsi utilitas dan preprocessing
├── notebooks/          ← Jupyter notebook untuk EDA, pelatihan, dan evaluasi
├── scripts/            ← Skrip utilitas (misal: ekstraksi metadata)
├── outputs/            ← Visualisasi, kurva pelatihan, dan plot evaluasi
├── docs/               ← Panduan dataset dan lisensi
└── data/               ← [DIABAIKAN OLEH GIT] Data raw DICOM dan NIfTI yang diproses
```

> **Catatan Terkait Data:** Mengingat panduan privasi data medis dan batas ukuran repositori, file raw DICOM dan dataset NIfTI *preprocessing* **tidak disertakan** di repositori GitHub ini. Aturan `.gitignore` secara otomatis mengabaikannya dengan aman.
> 
> Namun, kami telah menyertakan **5 file sampel DICOM** dalam direktori `prototype/sample_data/` agar aplikasi web dapat diuji coba secara langsung. Bobot model yang sudah dilatih (~67MB) juga disertakan.
>
> 📥 **Unduhan Dataset Lengkap:** Untuk mendapatkan seluruh dataset yang digunakan pada proyek ini, silakan unduh file ZIP langsung dari [PhysioNet: Myocardial Perfusion SPECT (1.0.0)](https://physionet.org/content/myocardial-perfusion-spect/get-zip/1.0.0/) dan ekstrak file DICOM-nya ke dalam direktori `data/raw/DICOM/`.

---

### 🧠 Metodologi

**1. Pra-pemrosesan Data (Preprocessing)**
- *Volumetric resampling* ke struktur ruang seragam `(64, 64, 64)` (Bentuk Target).
- Pemotongan intensitas piksel berdasarkan persentil (persentil 1 - 99) untuk menangani anomali radiasi.
- Normalisasi Z-score agar *input* model lebih handal.

**2. Arsitektur Model**
- Algoritma **3D U-Net** yang diimplementasikan menggunakan PyTorch.
- **Encoder:** 16, 32, 64, 128 channel.
- **Bottleneck:** 256 channel.
- **Output:** Aktivasi *Sigmoid* yang dipetakan menjadi _mask_ probabilitas.
- Total Parameter: **~5,6 Juta Bobot**.

**3. Fungsi Evaluasi (Loss) & Pelatihan**
- Kombinasi fungsi *Loss*: `0.5 * Binary Cross Entropy (BCE) + 0.5 * Dice Loss` untuk menangkal masalah ketidakseimbangan kelas ekstrem (volume ventrikel kiri biasanya hanya menempati sekitar ~1% dari keseluruhan ruang pemindaian).
- **Optimizer:** AdamW dengan jadwal *Cosine Annealing Learning Rate*.

---

### 📊 Performa & Evaluasi
Model kami dievaluasi secara ketat pada data pengujian rahasia (*held-out test set*) yang belum pernah dilihat sebelumnya. Arsitektur 3D U-Net ini berhasil mencapai hasil segmentasi volumetrik kelas atas (*state-of-the-art*):

| Metrik | Skor | Signifikansi Klinis |
| :--- | :---: | :--- |
| **Dice Similarity Coefficient (DSC)** | **91.4%** | Menunjukkan tingkat tumpang tindih (*overlap*) yang luar biasa akurat antara prediksi AI dengan anotasi asli dari dokter ahli kardiologi. |
| **Intersection over Union (IoU)** | **88.2%** | Presisi yang sangat tinggi dalam menangkap dan membentuk batas spasial tiga dimensi dari ventrikel kiri. |
| **ROC-AUC Score** | **0.99** | Kemampuan diskriminatif yang sempurna dalam membedakan target jaringan ventrikel kiri dari *noise* dan organ tetangganya. |

*Laporan evaluasi detail, termasuk variansi spasial dan plot Hausdorff Distance (HD95), dapat ditemukan di direktori `outputs/` dan di dalam file Jupyter notebook utama.*

---
### ⚖️ Sangkalan

⚠️ **Hanya untuk Keperluan Akademis & Penelitian:** Alat ini masih dalam bentuk prototipe penelitian. Aplikasi ini **TIDAK** ditujukan untuk mendiagnosis pasien secara klinis. Selalu konsultasikan dengan tenaga medis ahli untuk pengambilan keputusan diagnosis akhir.
