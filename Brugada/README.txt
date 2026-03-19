Brugada: AI-Based Brugada Syndrome Detection from 12-Lead ECG

Folder
Brugada

Main Workspace
- idsc-dawnbringer-brugada.ipynb
- IDSC2026_explanation.txt

Project Summary
This folder contains the Brugada track of the IDSC project. The main goal is
to detect Brugada syndrome from 12-lead ECG recordings using a machine
learning workflow that combines preprocessing, feature extraction, modeling,
and evaluation.

This folder is mainly centered around one working notebook. Most of the
practical project flow happens there, from loading ECG data to reviewing final
metrics and interpretation results.

What This Folder Is Used For
- Loading and preparing ECG recordings for analysis
- Extracting signal and morphology-based features
- Training machine learning or deep learning models for classification
- Evaluating the model with clinically relevant metrics
- Reviewing the broader project context through the explanation document

Important Files
- idsc-dawnbringer-brugada.ipynb
  Main notebook for preprocessing, feature engineering, training, and evaluation
- IDSC2026_explanation.txt
  Extra background on the wider IDSC project and how this folder fits into it

Typical Workflow
1. Open the notebook in Jupyter Lab or Google Colab.
2. Confirm the ECG dataset path is correct.
3. Install any missing libraries before running the notebook.
4. Run the notebook from top to bottom so preprocessing and training stay in order.
5. Review the resulting metrics, plots, and model behavior notes.

How To Run
1. Install the basic dependencies:
   pip install numpy pandas scipy scikit-learn matplotlib seaborn xgboost torch
2. Open:
   idsc-dawnbringer-brugada.ipynb
3. Update dataset paths if needed.
4. Run all cells sequentially.

Working Notes
- This folder is notebook-driven, so broken file paths are the most common issue
- ECG quality information matters here, especially if the workflow uses per-lead
  signal quality or SNR features
- If results look inconsistent, check preprocessing settings before changing
  the model section

Documentation Purpose
This README is written as a working reference for the Brugada folder. It is
meant to help during day-to-day project work, especially when reopening the
folder after some time and needing a quick reminder of what lives here and how
to restart the workflow.

Disclaimer
This project is for academic and research use only. It is not intended for
clinical diagnosis or treatment decisions.