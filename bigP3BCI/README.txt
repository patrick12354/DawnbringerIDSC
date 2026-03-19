bigP3BCI: Motor Imagery EEG Classification

Folder
bigP3BCI

Main Workspace
- idsc-dawnbringer-bigp3bci.ipynb

Project Summary
This folder contains the bigP3BCI track of the IDSC project. The work here
focuses on classifying motor imagery EEG signals so the system can distinguish
between imagined actions from non-invasive brain recordings.

The folder is built around a notebook workflow. It is the place to inspect
EEG data, run preprocessing, train models, and check whether the classifier
is learning useful signal patterns instead of noise.

What This Folder Is Used For
- Loading and preprocessing EEG recordings from the competition dataset
- Extracting useful signal features for classification
- Training and comparing machine learning or deep learning models
- Reviewing accuracy, kappa score, confusion matrices, and related outputs
- Iterating on a brain-computer interface proof of concept

Important Files
- idsc-dawnbringer-bigp3bci.ipynb
  Main notebook for EDA, preprocessing, training, and evaluation

Typical Workflow
1. Open the notebook in Jupyter Lab or Google Colab.
2. Confirm the EEG dataset is available and the paths are correct.
3. Install missing dependencies before execution.
4. Run the notebook sequentially so the preprocessing and training steps stay aligned.
5. Review the plots and metrics before making changes to features or models.

How To Run
1. Install the basic dependencies:
   pip install numpy pandas scipy scikit-learn matplotlib mne torch
2. Open:
   idsc-dawnbringer-bigp3bci.ipynb
3. Update any dataset paths if needed.
4. Run all cells from top to bottom.

Working Notes
- EEG pipelines are sensitive to preprocessing choices, so check filtering
  and feature extraction steps before judging model quality
- If performance drops unexpectedly, verify label handling and train-test split logic
- This folder is best treated as an experiment workspace, not a packaged app

Documentation Purpose
This README is meant to act as a practical working note for the bigP3BCI
folder. It should make it easier to jump back into the project, remember the
main entry point, and understand what this folder is responsible for.

Disclaimer
This project is for academic and research use only. It is not intended for
clinical diagnosis or treatment decisions.