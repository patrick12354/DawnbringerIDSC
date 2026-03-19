==============================================================
  Brugada: AI-Based Brugada Syndrome Detection from 12-Lead ECG
==============================================================

ENGLISH VERSION
---------------

Folder: Brugada
Notebook: idsc-dawnbringer-brugada.ipynb

OVERVIEW
--------
This folder contains the full machine learning pipeline for AI-assisted
detection of Brugada syndrome from 12-lead ECG signals. This project was
developed as part of the IDSC (International Data Science Competition)
project "Dawnbringer".

Brugada syndrome is a genetic cardiac disorder associated with malignant
ventricular arrhythmias and sudden cardiac death, often in patients whose
hearts appear structurally normal. Early identification is clinically
important because subtle ECG patterns can be difficult to detect
consistently, especially in screening settings.

WHAT THIS PROJECT DOES
-----------------------
- Loads and preprocesses 12-lead ECG recordings from the Brugada dataset.
- Extracts handcrafted ECG features, including signal statistics,
  morphology-related descriptors, heart rate variability, ST amplitude,
  and frequency-domain information.
- Trains and evaluates multiple models, including feature-based machine
  learning and deep learning approaches on raw ECG signals.
- Incorporates quality-aware modeling using per-lead signal quality / SNR
  information to improve robustness on noisy recordings.
- Produces clinically relevant evaluation metrics such as AUC-ROC,
  sensitivity, specificity, F1-score, PPV, and NPV.
- Supports interpretable analysis and subgroup-oriented evaluation for
  medically meaningful risk assessment.

POTENTIAL MEDICAL APPLICATIONS
-------------------------------
- Early screening support for Brugada syndrome in outpatient or
  cardiovascular screening workflows.
- Decision support for identifying patients who may require further
  electrophysiology evaluation.
- Risk-oriented triage tools to help flag ECG recordings that warrant
  specialist review.
- Research support for studying ECG biomarkers linked to sudden cardiac
  death risk.

CONTENTS
--------
  idsc-dawnbringer-brugada.ipynb: Main Jupyter Notebook containing the
                                  full preprocessing, feature engineering,
                                  model training, evaluation, calibration,
                                  and interpretability pipeline.
  IDSC2026_explanation.txt: Narrative explanation of the broader IDSC 2026
                            multi-dataset study and the role of the
                            Brugada project within it.

HOW TO RUN
----------
1. Open the notebook in Jupyter Lab or Google Colab.
2. Ensure the required libraries are installed:
   pip install numpy pandas scipy scikit-learn matplotlib seaborn xgboost torch
3. Adjust the dataset path if needed so the notebook can access the ECG files.
4. Run all cells sequentially from top to bottom.
5. Results, metrics, plots, and analysis outputs will be displayed inline.

DISCLAIMER
----------
This project is for academic and research purposes only. It is NOT
intended for clinical diagnosis or medical treatment decisions.

==============================================================

VERSI BAHASA INDONESIA
-----------------------

Folder: Brugada
Notebook: idsc-dawnbringer-brugada.ipynb

RINGKASAN
---------
Folder ini berisi pipeline machine learning lengkap untuk deteksi sindrom
Brugada berbasis AI dari sinyal ECG 12-lead. Proyek ini dikembangkan
sebagai bagian dari proyek IDSC (International Data Science Competition)
"Dawnbringer".

Sindrom Brugada adalah kelainan jantung genetik yang berhubungan dengan
aritmia ventrikel ganas dan sudden cardiac death, sering kali pada pasien
dengan struktur jantung yang tampak normal. Identifikasi dini sangat
penting secara klinis karena pola ECG-nya dapat halus dan sulit dikenali
secara konsisten, terutama pada konteks skrining.

APA YANG DILAKUKAN PROYEK INI
------------------------------
- Memuat dan memproses rekaman ECG 12-lead dari dataset Brugada.
- Mengekstrak fitur ECG handcrafted, termasuk statistik sinyal,
  deskriptor morfologi, heart rate variability, amplitudo ST, dan
  informasi domain frekuensi.
- Melatih dan mengevaluasi beberapa model, termasuk pendekatan machine
  learning berbasis fitur dan deep learning pada sinyal ECG mentah.
- Menggunakan quality-aware modeling berbasis informasi kualitas sinyal /
  SNR per lead agar model lebih robust terhadap rekaman yang noisy.
- Menghasilkan metrik evaluasi yang relevan secara klinis seperti AUC-ROC,
  sensitivity, specificity, F1-score, PPV, dan NPV.
- Mendukung analisis interpretabilitas dan evaluasi subgroup untuk
  penilaian risiko yang lebih bermakna secara medis.

POTENSI APLIKASI MEDIS
-----------------------
- Dukungan skrining dini sindrom Brugada pada alur kerja rawat jalan
  atau pemeriksaan kardiovaskular.
- Pendukung keputusan untuk mengidentifikasi pasien yang memerlukan
  evaluasi elektrofisiologi lebih lanjut.
- Alat triase berbasis risiko untuk menandai rekaman ECG yang perlu
  ditinjau oleh spesialis.
- Dukungan riset untuk mempelajari biomarker ECG yang berkaitan dengan
  risiko sudden cardiac death.

ISI FOLDER
----------
  idsc-dawnbringer-brugada.ipynb: Notebook Jupyter utama yang memuat
                                  seluruh preprocessing, feature
                                  engineering, pelatihan model,
                                  evaluasi, kalibrasi, dan pipeline
                                  interpretabilitas.
  IDSC2026_explanation.txt: Dokumen penjelasan naratif mengenai studi
                            multi-dataset IDSC 2026 yang lebih luas
                            serta posisi proyek Brugada di dalamnya.

CARA MENJALANKAN
----------------
1. Buka notebook di Jupyter Lab atau Google Colab.
2. Pastikan library yang dibutuhkan sudah terinstal:
   pip install numpy pandas scipy scikit-learn matplotlib seaborn xgboost torch
3. Sesuaikan path dataset bila diperlukan agar notebook dapat mengakses
   file ECG.
4. Jalankan semua sel secara berurutan dari atas ke bawah.
5. Hasil, metrik, plot, dan output analisis akan ditampilkan secara inline.

SANGKALAN
---------
Proyek ini hanya untuk keperluan akademis dan penelitian. Proyek ini TIDAK
dimaksudkan untuk diagnosis klinis atau keputusan perawatan medis.

==============================================================
