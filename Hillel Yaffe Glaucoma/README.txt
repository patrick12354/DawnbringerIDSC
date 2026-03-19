Hillel Yaffe Glaucoma: AI-Based Glaucoma Detection from Fundus Images

Folder
Hillel Yaffe Glaucoma

Main Workspace
- idsc-dawnbringer_Glaucoma.ipynb

Project Summary
This folder contains the glaucoma track of the IDSC project. The main goal is
to detect glaucoma from retinal fundus images using a deep learning workflow
that covers preprocessing, augmentation, training, evaluation, and visual
explanation.

This folder is mostly notebook-based. It is the working area for checking the
image pipeline, training the model, reviewing clinical metrics, and inspecting
explainability outputs such as Grad-CAM.

What This Folder Is Used For
- Loading and preprocessing fundus images
- Applying augmentation to improve class balance and generalization
- Training CNN or transfer learning models for glaucoma classification
- Reviewing metrics such as AUC-ROC, sensitivity, specificity, accuracy, and F1-score
- Inspecting visual explanation outputs to understand model focus areas

Important Files
- idsc-dawnbringer_Glaucoma.ipynb
  Main notebook for EDA, preprocessing, training, evaluation, and explainability

Typical Workflow
1. Open the notebook in Jupyter Lab or Google Colab.
2. Confirm the dataset path or mounted storage is correct.
3. Install the required packages before running the workflow.
4. Run the notebook in order from top to bottom.
5. Review the metrics and Grad-CAM outputs before changing model settings.

How To Run
1. Install the basic dependencies:
   pip install numpy pandas pillow scikit-learn matplotlib seaborn torch torchvision
2. Open:
   idsc-dawnbringer_Glaucoma.ipynb
3. Mount Google Drive if needed, or update local dataset paths.
4. Run all cells sequentially.

Working Notes
- This workflow can be resource-heavy, so Colab or a GPU environment may be easier
- If the model behaves oddly, check image preprocessing and class balance first
- Explainability outputs are useful for sanity checks, not just presentation

Documentation Purpose
This README is intended to be a practical reference while working in the
glaucoma folder. It should help you quickly remember what the folder contains,
where to start, and what parts of the workflow deserve attention during
experimentation.

Disclaimer
This project is for academic and research use only. It is not intended for
clinical diagnosis or to replace specialist medical judgment.