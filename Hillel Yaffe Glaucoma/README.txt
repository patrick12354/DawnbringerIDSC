==============================================================
  Hillel Yaffe Glaucoma: AI-Based Glaucoma Detection from Fundus Images
==============================================================

ENGLISH VERSION
---------------

Folder: Hillel Yaffe Glaucoma
Notebook: idsc-dawnbringer_Glaucoma.ipynb

OVERVIEW
--------
This folder contains the full machine learning pipeline for AI-assisted
glaucoma detection from retinal fundus images. It was developed as part
of the IDSC (International Data Science Competition) project "Dawnbringer",
in partnership with the Hillel Yaffe Medical Center dataset.

Glaucoma is one of the leading causes of irreversible blindness worldwide.
Early detection is critical, yet it requires specialist expertise and
expensive equipment. This project aims to democratize early diagnosis
by automating the detection process through deep learning on fundus
photography, which is a widely available and non-invasive imaging modality.

WHAT THIS PROJECT DOES
-----------------------
- Loads and preprocesses retinal fundus images from the Hillel Yaffe dataset.
- Applies data augmentation to handle class imbalance.
- Trains a Convolutional Neural Network (CNN) or transfer learning model to
  classify fundus images as Glaucomatous or Healthy.
- Evaluates the model using clinical metrics: AUC-ROC, sensitivity,
  specificity, accuracy, and F1-score.
- Generates visual explanations, such as Grad-CAM, to highlight regions
  of interest that influenced the model's decision.

POTENTIAL MEDICAL APPLICATIONS
-------------------------------
- Automated screening tools for glaucoma in primary care clinics and
  rural or remote areas where ophthalmologists are unavailable.
- Second-opinion support tools for ophthalmologists.
- Population-scale screening programs using telemedicine platforms.
- Integration with existing fundus camera systems for point-of-care diagnosis.

CONTENTS
--------
  idsc-dawnbringer_Glaucoma.ipynb: Main Jupyter Notebook containing the
                                   full EDA, preprocessing, model training,
                                   evaluation, and explainability pipeline.

HOW TO RUN
----------
1. Open the notebook in Jupyter Lab or Google Colab.
   (Google Colab is recommended due to the large dataset and GPU requirements)
2. Ensure the required libraries are installed:
   pip install numpy pandas pillow scikit-learn matplotlib seaborn torch torchvision
3. Mount your Google Drive (if using Colab) or adjust the dataset path locally.
4. Run all cells sequentially from top to bottom.
5. Results, classification reports, ROC curves, and Grad-CAM visualizations
   will be displayed inline.

DISCLAIMER
----------
This project is for academic and research purposes only. It is NOT
intended for clinical diagnosis or to replace the judgment of a
qualified ophthalmologist.

==============================================================

VERSI BAHASA INDONESIA
-----------------------

Folder: Hillel Yaffe Glaucoma
Notebook: idsc-dawnbringer_Glaucoma.ipynb

RINGKASAN
---------
Folder ini berisi pipeline machine learning lengkap untuk deteksi glaukoma
berbasis AI dari citra fundus retina. Proyek ini dikembangkan sebagai bagian
dari IDSC (International Data Science Competition) "Dawnbringer" menggunakan
dataset dari Hillel Yaffe Medical Center.

Glaukoma adalah salah satu penyebab utama kebutaan permanen di seluruh dunia.
Deteksi dini sangatlah krusial, namun memerlukan keahlian spesialis serta
peralatan mahal. Proyek ini bertujuan untuk mendemokratisasi diagnosis dini
melalui otomatisasi deteksi menggunakan deep learning pada foto fundus, yang
merupakan modalitas pencitraan non-invasif dan tersedia luas.

APA YANG DILAKUKAN PROYEK INI
------------------------------
- Memuat dan memproses citra fundus retina dari dataset Hillel Yaffe.
- Menerapkan augmentasi data untuk menangani ketidakseimbangan kelas.
- Melatih model Convolutional Neural Network (CNN) atau transfer learning untuk
  mengklasifikasikan citra fundus sebagai Glaukoma atau Sehat.
- Mengevaluasi model menggunakan metrik klinis: AUC-ROC, sensitivitas,
  spesifisitas, akurasi, dan F1-score.
- Menghasilkan penjelasan visual seperti Grad-CAM untuk menyoroti area
  yang memengaruhi keputusan model.

POTENSI APLIKASI MEDIS
-----------------------
- Alat skrining glaukoma otomatis di klinik perawatan primer serta daerah
  terpencil yang kekurangan dokter spesialis mata.
- Alat pendukung opini kedua bagi dokter spesialis mata (ophthalmologis).
- Program skrining skala populasi melalui platform telemedicine.
- Integrasi dengan sistem kamera fundus yang ada untuk diagnosis di titik
  perawatan (point-of-care).

ISI FOLDER
----------
  idsc-dawnbringer_Glaucoma.ipynb: Notebook Jupyter utama yang memuat
                                   seluruh EDA, preprocessing, pelatihan
                                   model, evaluasi, dan pipeline
                                   explainability.

CARA MENJALANKAN
----------------
1. Buka notebook di Jupyter Lab atau Google Colab.
   (Google Colab direkomendasikan karena dataset besar dan kebutuhan GPU)
2. Pastikan library yang dibutuhkan sudah terinstal:
   pip install numpy pandas pillow scikit-learn matplotlib seaborn torch torchvision
3. Mount Google Drive (jika menggunakan Colab) atau sesuaikan path dataset
   secara lokal.
4. Jalankan semua sel secara berurutan dari atas ke bawah.
5. Hasil, laporan klasifikasi, kurva ROC, dan visualisasi Grad-CAM akan
   ditampilkan secara inline.

SANGKALAN
---------
Proyek ini hanya untuk keperluan akademis dan penelitian. Proyek ini TIDAK
dimaksudkan untuk diagnosis klinis atau menggantikan penilaian dokter
spesialis mata yang berkualifikasi.

==============================================================
