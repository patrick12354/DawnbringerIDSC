# 🌅 Dawnbringer IDSC — AI for Medicine: A Proof of Concept

> *"The dawn of a new era — where Artificial Intelligence stands beside the physician."*

[![SPECT Prototype](https://img.shields.io/badge/Live_Demo-CorVision_SPECT-FF4B4B?style=for-the-badge&logo=streamlit)](https://heartspect.streamlit.app/)

*(For Indonesian readers / Bagi pembaca berbahasa Indonesia, silakan gulir ke bawah untuk versi Bahasa Indonesia.)*

---

## English Version

### 🎯 What Is This Repository?

**Dawnbringer** is a collection of independent AI/Machine Learning projects developed for the **IDSC (International Data Science Competition)**, all unified by a single, bold thesis:

> **Artificial Intelligence, trained on the right data, can learn to see what the human eye struggles to see — and will become an indispensable tool in modern medicine.**

This repository is not just a competition submission. It is **a proof of concept for the future of AI-assisted healthcare**. Each sub-project tackles a distinct, real-world medical problem — demonstrating that AI is not limited to one specialty, but can generalize across fields, from cardiology to neurology to ophthalmology.

---

### 🧩 Projects in This Repository

| Folder | Medical Domain | Task | Key Technology |
|:---|:---|:---|:---|
| [`SPECT/`](./SPECT/) | **Cardiology** | Left ventricle segmentation from Myocardial Perfusion SPECT scans | 3D U-Net (PyTorch) |
| [`bigP3BCI/`](./bigP3BCI/) | **Neurology / BCI** | Motor imagery EEG signal classification for Brain-Computer Interface | CNN / Deep Learning on EEG |
| [`Hillel Yaffe Glaucoma/`](./Hillel%20Yaffe%20Glaucoma/) | **Ophthalmology** | Glaucoma detection from retinal fundus images | CNN / Transfer Learning |

---

### 💡 The Core Argument: Why AI Will Transform Medicine

For decades, medical diagnosis has depended entirely on human expertise — years of training, high cognitive load, and inevitably, human error and fatigue. AI does not replace this expertise. Rather, it *amplifies* it.

Here is why each project in this repository matters:

#### 🫀 1. SPECT — CorVision (Cardiology)
Myocardial Perfusion SPECT is a nuclear imaging technique used to assess blood flow to the heart. Manually delineating the left ventricle in 3D volumetric scans is a time-consuming, expert-dependent process. Our **3D U-Net** model achieves:
- **Dice Score: 91.4%** — near-perfect overlap with expert cardiologist annotations
- **AUC-ROC: 0.99** — virtually perfect discrimination ability
- **A live, interactive Streamlit prototype** deployed to the cloud

This proves that AI can perform expert-level cardiac image segmentation — **reliably, instantly, at scale**.

#### 🧠 2. bigP3BCI — Motor Imagery EEG (Neurology / BCI)
Brain-Computer Interfaces open doors that were once permanently closed. For patients with ALS, locked-in syndrome, or severe spinal cord injuries, the ability to communicate or control assistive devices through thought alone is life-changing. Our EEG classification pipeline demonstrates that AI can decode intended motor actions from raw brain signals — a critical step toward **non-invasive, real-time BCI systems** accessible beyond specialized neurology labs.

#### 👁️ 3. Hillel Yaffe Glaucoma (Ophthalmology)
Glaucoma causes irreversible vision loss, often undetected until significant damage has already occurred. Specialist ophthalmologists are scarce in low-resource settings. Our fundus image classification model demonstrates that AI can screen for glaucoma from routine retinal photographs — enabling **population-scale, low-cost early detection** that could prevent millions of cases of preventable blindness worldwide.

---

### 🔭 A Vision for the Future

These three projects, taken together, demonstrate a pattern:

1. **AI learns from expert-labeled data** — absorbing knowledge that took doctors years to accumulate.
2. **AI generalizes to new, unseen patients** — with performance metrics that approach or match clinical standards.
3. **AI deploys at scale** — a trained model can run inference on thousands of scans per second, at a fraction of the cost of a specialist consultation.

The implication is profound: **not every patient in the world needs access to a cardiologist, neurologist, or ophthalmologist — they need access to a device running an AI model trained by one.**

This is the promise of AI in medicine. **Dawnbringer is the proof.**

---

### ⚖️ Disclaimer

> ⚠️ **All projects in this repository are strictly for academic and research purposes.** None of the models, prototypes, or tools presented here are intended for, nor should they be used for, clinical diagnosis or medical treatment decisions without the oversight of qualified medical professionals.

---
---

## Versi Bahasa Indonesia

### 🎯 Apa Itu Repositori Ini?

**Dawnbringer** adalah kumpulan proyek AI/Machine Learning independen yang dikembangkan untuk **IDSC (International Data Science Competition)**, yang semuanya bersatu dalam satu tesis yang berani:

> **Kecerdasan Buatan, yang dilatih dengan data yang tepat, dapat belajar untuk melihat apa yang sulit dilihat oleh mata manusia — dan akan menjadi alat yang sangat penting dalam dunia medis modern.**

Repositori ini bukan sekadar submission kompetisi. Ini adalah **bukti konsep untuk masa depan layanan kesehatan berbantuan AI**. Setiap sub-proyek menangani masalah medis nyata yang berbeda — membuktikan bahwa AI tidak terbatas pada satu spesialisasi, tetapi dapat digeneralisasikan lintas bidang, mulai dari kardiologi hingga neurologi dan oftalmologi.

---

### 🧩 Proyek dalam Repositori Ini

| Folder | Domain Medis | Tugas | Teknologi Utama |
|:---|:---|:---|:---|
| [`SPECT/`](./SPECT/) | **Kardiologi** | Segmentasi ventrikel kiri dari citra Myocardial Perfusion SPECT | 3D U-Net (PyTorch) |
| [`bigP3BCI/`](./bigP3BCI/) | **Neurologi / BCI** | Klasifikasi sinyal EEG Motor Imagery untuk Brain-Computer Interface | CNN / Deep Learning pada EEG |
| [`Hillel Yaffe Glaucoma/`](./Hillel%20Yaffe%20Glaucoma/) | **Oftalmologi** | Deteksi glaukoma dari citra fundus retina | CNN / Transfer Learning |

---

### 💡 Argumen Utama: Mengapa AI Akan Mentransformasi Dunia Medis

Selama beberapa dekade, diagnosis medis sepenuhnya bergantung pada keahlian manusia — bertahun-tahun pelatihan, beban kognitif yang tinggi, dan tak terhindarkan, kesalahan manusia dan kelelahan. AI tidak menggantikan keahlian ini. Sebaliknya, AI *memperkuatnya*.

Berikut adalah alasan mengapa setiap proyek dalam repositori ini penting:

#### 🫀 1. SPECT — CorVision (Kardiologi)
Myocardial Perfusion SPECT adalah teknik pencitraan nuklir yang digunakan untuk menilai aliran darah ke jantung. Mendelineasi ventrikel kiri secara manual dalam pemindaian volumetrik 3D adalah proses yang memakan waktu dan sangat bergantung pada keahlian. Model **3D U-Net** kami mencapai:
- **Dice Score: 91.4%** — tumpang tindih yang hampir sempurna dengan anotasi dokter kardiologi ahli
- **AUC-ROC: 0.99** — kemampuan diskriminasi yang nyaris sempurna
- **Prototipe Streamlit interaktif langsung** yang di-deploy ke cloud

Ini membuktikan bahwa AI dapat melakukan segmentasi citra jantung setara ahli — **secara andal, instan, dan dalam skala besar**.

#### 🧠 2. bigP3BCI — EEG Motor Imagery (Neurologi / BCI)
Brain-Computer Interface membuka pintu yang tadinya tertutup permanen. Bagi pasien dengan ALS, *locked-in syndrome*, atau cedera tulang belakang parah, kemampuan untuk berkomunikasi atau mengendalikan perangkat bantu melalui pikiran saja adalah hal yang mengubah hidup. Pipeline klasifikasi EEG kami menunjukkan bahwa AI dapat mendekode aksi motorik yang ingin dilakukan dari sinyal otak mentah — sebuah langkah kritis menuju **sistem BCI non-invasif dan real-time** yang dapat diakses di luar laboratorium neurologi khusus.

#### 👁️ 3. Hillel Yaffe Glaucoma (Oftalmologi)
Glaukoma menyebabkan kehilangan penglihatan yang tidak dapat dipulihkan, seringkali tidak terdeteksi hingga kerusakan signifikan telah terjadi. Dokter spesialis mata langka di daerah yang kekurangan sumber daya. Model klasifikasi citra fundus kami menunjukkan bahwa AI dapat melakukan skrining glaukoma dari foto retina rutin — memungkinkan **deteksi dini berskala populasi dengan biaya rendah** yang berpotensi mencegah jutaan kasus kebutaan yang seharusnya dapat dicegah di seluruh dunia.

---

### 🔭 Visi untuk Masa Depan

Ketiga proyek ini, diambil bersama-sama, menunjukkan sebuah pola:

1. **AI belajar dari data berlabel ahli** — menyerap pengetahuan yang butuh bertahun-tahun bagi para dokter untuk kumpulkan.
2. **AI menggeneralisasi ke pasien baru yang belum pernah dilihat** — dengan metrik kinerja yang mendekati atau setara dengan standar klinis.
3. **AI di-deploy dalam skala besar** — model yang sudah dilatih dapat menjalankan inferensi pada ribuan pemindaian per detik, dengan biaya yang jauh lebih rendah dari konsultasi spesialis.

Implikasinya sangat mendalam: **tidak setiap pasien di dunia perlu memiliki akses ke kardiolog, neurolog, atau dokter spesialis mata — mereka hanya perlu akses ke sebuah perangkat yang menjalankan model AI yang dilatih oleh seorang ahli.**

Inilah janji AI dalam dunia medis. **Dawnbringer adalah buktinya.**

---

### ⚖️ Sangkalan

> ⚠️ **Semua proyek dalam repositori ini murni untuk keperluan akademis dan penelitian.** Tidak ada model, prototipe, atau alat yang disajikan di sini yang ditujukan untuk, atau seharusnya digunakan dalam, diagnosis klinis atau keputusan pengobatan tanpa pengawasan tenaga medis profesional yang berkualifikasi.
