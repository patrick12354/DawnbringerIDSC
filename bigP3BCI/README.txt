==============================================================
  bigP3BCI — Motor Imagery EEG Classification (BCI Competition)
==============================================================

ENGLISH VERSION
---------------

Folder: bigP3BCI
Notebook: idsc-dawnbringer-bigp3bci.ipynb

OVERVIEW
--------
This folder contains the full machine learning pipeline for classifying
Motor Imagery EEG (Electroencephalography) signals, developed as part of
the IDSC (International Data Science Competition) project "Dawnbringer".

The system is designed to decode brain signals from non-invasive EEG
recordings, enabling a Brain-Computer Interface (BCI) that can distinguish
between different imagined motor actions (e.g., left hand vs. right hand
movement) without any physical movement from the subject.

WHAT THIS PROJECT DOES
-----------------------
- Loads and preprocesses raw EEG data from the BCI Competition dataset
- Extracts meaningful features from EEG time-series signals
- Trains and evaluates machine learning / deep learning classification models
- Produces evaluation metrics (accuracy, kappa score, confusion matrix, etc.)
- Demonstrates that AI can reliably decode human intent from brain signals,
  serving as a proof-of-concept for non-invasive BCI medical applications

POTENTIAL MEDICAL APPLICATIONS
-------------------------------
- Assistive technology for patients with severe motor disabilities
  (e.g., ALS, locked-in syndrome, spinal cord injuries)
- Rehabilitation systems for stroke patients to regain motor function
- Communication tools for patients who cannot speak or move

CONTENTS
--------
  idsc-dawnbringer-bigp3bci.ipynb  — Main Jupyter Notebook containing
                                     the full EDA, preprocessing, model
                                     training, and evaluation pipeline.

HOW TO RUN
----------
1. Open the notebook in Jupyter Lab or Google Colab
2. Ensure required libraries are installed:
   pip install numpy pandas scipy scikit-learn matplotlib mne torch
3. Run all cells sequentially from top to bottom
4. Results, plots, and metrics will be displayed inline

DISCLAIMER
----------
This project is for academic and research purposes only. It is NOT
intended for clinical diagnosis or medical treatment decisions.

==============================================================

VERSI BAHASA INDONESIA
-----------------------

Folder: bigP3BCI
Notebook: idsc-dawnbringer-bigp3bci.ipynb

RINGKASAN
---------
Folder ini berisi pipeline machine learning lengkap untuk melakukan
klasifikasi sinyal EEG (Electroencephalography) Motor Imagery, yang
dikembangkan sebagai bagian dari proyek IDSC (International Data Science
Competition) "Dawnbringer".

Sistem ini dirancang untuk mendekode sinyal otak dari rekaman EEG non-invasif,
sehingga memungkinkan sebuah Brain-Computer Interface (BCI) yang dapat
membedakan berbagai aksi motorik yang dibayangkan (misalnya: gerakan tangan
kiri vs. tangan kanan) tanpa adanya gerakan fisik dari subjek.

APA YANG DILAKUKAN PROYEK INI
------------------------------
- Memuat dan memproses data EEG mentah dari dataset BCI Competition
- Mengekstrak fitur bermakna dari sinyal time-series EEG
- Melatih dan mengevaluasi model machine learning / deep learning
- Menghasilkan metrik evaluasi (akurasi, kappa score, confusion matrix, dll.)
- Membuktikan bahwa AI dapat mendekode niat manusia dari sinyal otak secara
  andal, sebagai bukti konsep untuk aplikasi medis BCI non-invasif

POTENSI APLIKASI MEDIS
-----------------------
- Teknologi bantu untuk pasien dengan disabilitas motorik berat
  (contoh: ALS, locked-in syndrome, cedera tulang belakang)
- Sistem rehabilitasi untuk pasien stroke agar dapat memulihkan fungsi motorik
- Alat komunikasi bagi pasien yang tidak dapat berbicara atau bergerak

ISI FOLDER
----------
  idsc-dawnbringer-bigp3bci.ipynb  — Notebook Jupyter utama yang memuat
                                     seluruh EDA, preprocessing, pelatihan
                                     model, dan pipeline evaluasi.

CARA MENJALANKAN
----------------
1. Buka notebook di Jupyter Lab atau Google Colab
2. Pastikan library yang dibutuhkan sudah terinstal:
   pip install numpy pandas scipy scikit-learn matplotlib mne torch
3. Jalankan semua sel secara berurutan dari atas ke bawah
4. Hasil, grafik, dan metrik akan ditampilkan secara inline

SANGKALAN
---------
Proyek ini hanya untuk keperluan akademis dan penelitian. Proyek ini TIDAK
dimaksudkan untuk diagnosis klinis atau keputusan perawatan medis.

==============================================================
