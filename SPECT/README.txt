CorVision: Left Ventricle Segmentation from Myocardial Perfusion SPECT

Folder
SPECT

Main Workspaces
- notebooks/
- prototype/
- models/
- scripts/
- outputs/
- docs/
- data/

Project Summary
This folder contains the SPECT track of the IDSC project. The goal is to
segment the left ventricle from myocardial perfusion SPECT scans using a
3D U-Net pipeline. In practice, this folder is the working area for model
training, evaluation, result review, and prototype demos.

The project is set up to show both the research side and the practical side
of the work. The notebooks cover experimentation and analysis, while the
prototype folder provides a simple app for running inference and reviewing
results in a more visual way.

What This Folder Is Used For
- Preparing and organizing volumetric SPECT data for experiments
- Training and evaluating the 3D U-Net segmentation model
- Reviewing metrics such as Dice, IoU, and related segmentation results
- Running the Streamlit prototype for demos and quick model checks
- Keeping supporting documentation, scripts, and output artifacts in one place

Important Files And Folders
- notebooks/
  Main notebooks for exploration, training, validation, and evaluation
- prototype/
  Streamlit application and inference utilities for the SPECT demo
- models/
  Saved model weights and checkpoints
- outputs/
  Generated plots, visual comparisons, and evaluation artifacts
- scripts/
  Utility scripts used during preprocessing or dataset handling
- docs/
  Supporting documentation, references, and dataset notes
- data/
  Local raw and processed data storage
- run_prototype.bat
  Quick launcher for the Streamlit demo on Windows

Typical Workflow
1. Place or connect the dataset inside the expected local data structure.
2. Use the notebooks and scripts to inspect, preprocess, and prepare volumes.
3. Train or load the segmentation model.
4. Review the evaluation outputs and saved visualizations.
5. Run the prototype if you need a demo-ready interface for inference.

How To Run The Prototype
1. Install the required packages:
   pip install -r prototype/requirements.txt
2. Start the app:
   streamlit run prototype/app.py
3. Open the local Streamlit address shown in the terminal, usually:
   http://localhost:8501

Working Notes
- Large medical datasets are usually kept outside version control
- Model files and sample inputs may already exist for quick testing
- If paths break, check notebook path settings and the local data layout first
- The prototype is useful for demonstration, but most experimentation still
  happens in notebooks

Documentation Purpose
This README is meant to be a practical guide while working inside this folder.
It is not just a project description. It should help you remember where the
main pieces live, what the folder is for, and how to pick the right starting
point depending on whether you are training, evaluating, or demoing the model.

Disclaimer
This project is for academic and research use only. It is not intended for
clinical diagnosis or treatment decisions.
