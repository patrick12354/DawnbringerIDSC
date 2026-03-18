"""
Heart SPECT Segmentation — Streamlit Prototype & Landing Page
Left Ventricle Segmentation using 3D U-Net on Cardiac SPECT Imaging
"""

import os
import sys
import tempfile
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import load_model
from utils import predict_volume, save_mask_as_nifti, TARGET_SHAPE

# --- Config ---
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKPOINT_PATH = os.path.join(PROJECT_ROOT, "models", "best_model.pth")
SAMPLE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_data")

st.set_page_config(
    page_title="Heart SPECT AI",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS ---
st.markdown("""
<style>
    .main-title {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #aaaaaa;
        font-size: 1.2rem;
        margin-top: 0;
        margin-bottom: 2rem;
    }
    .section-title {
        margin-top: 2rem;
        margin-bottom: 1rem;
        color: #667eea;
        font-weight: 700;
        border-bottom: 1px solid #333;
        padding-bottom: 10px;
    }
    .metric-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        border: 1px solid #333;
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        border: 1px solid #667eea;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #667eea;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #aaa;
        margin-top: 4px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .cta-container {
        display: flex;
        justify-content: center;
        margin-top: 3rem;
        margin-bottom: 3rem;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def get_model():
    """Load model once and cache it."""
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    if not os.path.exists(CHECKPOINT_PATH):
        return None, None, device
    model, info = load_model(CHECKPOINT_PATH, device)
    return model, info, device


def render_slice(img_slice, mask_slice=None, prob_slice=None, title="",
                 cmap_img='gray', alpha=0.4):
    """Render a 2D slice with optional mask overlay."""
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.imshow(img_slice.T, cmap=cmap_img, origin='lower', aspect='equal')

    if mask_slice is not None:
        mask_rgba = np.zeros((*mask_slice.T.shape, 4))
        mask_rgba[mask_slice.T > 0] = [1, 0.2, 0.2, alpha]
        ax.imshow(mask_rgba, origin='lower', aspect='equal')

    if prob_slice is not None:
        ax.imshow(prob_slice.T, cmap='hot', origin='lower', aspect='equal',
                  alpha=0.5, vmin=0, vmax=1)

    ax.set_title(title, fontsize=11, fontweight='bold', color='white')
    ax.axis('off')
    fig.patch.set_facecolor('#0e1117')
    plt.tight_layout()
    return fig


def show_landing_page():
    """Landing page view for product pitching."""
    st.markdown('<h1 class="main-title">🫀 Heart SPECT AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Automated Left Ventricle Segmentation on Cardiac SPECT Imaging</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<h3 class="section-title">🔍 Latar Belakang Masalah</h3>', unsafe_allow_html=True)
        st.write("""
        Penyakit kardiovaskular masih menjadi penyebab kematian utama secara global. 
        Kajian visual dari **Myocardial Perfusion SPECT (MPS)** sangat penting untuk mendiagnosis gangguan aliran darah dan 
        kinerja jantung. 
        
        Namun, dokter spesialis kedokteran nuklir dituntut bekerja secara manual 
        menganalisa struktur 3D (volumetrik), memisahkan area *Left Ventricle* dengan akurat tanpa terganggu *background noise* (ekstra-kardiak).
        Proses ini sangat memakan waktu, rentan miskalkulasi kuantitatif, dan berpotensi tinggi dipengaruhi oleh faktor kelelahan (_fatigue_).
        """)

    with col2:
        st.markdown('<h3 class="section-title">💡 Solusi Pintar: 3D U-Net</h3>', unsafe_allow_html=True)
        st.write("""
        Kami menghadirkan AI berarsitektur mutakhir **3D U-Net**. Model *Deep Learning* kami dirancang khusus 
        untuk menginterpretasikan ruang tiga dimensi (Z, Y, X axis) sekaligus! 
        
        Sistem secara konklusif mengenali organ sasaran dan melakukan deteksi tepi (*contour segmentation*) 
        pada Ventrikel Kiri secara _full-automated_. Proses kompleks yang tadinya memakan waktu bermenit-menit 
        kini tuntas secara konsisten hanya dalam hitungan detik.
        """)
        
    st.markdown('<h3 class="section-title">🏥 Dampak Kesehatan (Clinical Impact)</h3>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("#### ⏱️ Efisiensi Waktu Maksimal\nMengurangi dramatis _turnaround time_ pemeriksaan. Dokter bisa jauh lebih fokus pada pengambilan keputusan klinis (_decision making_) ketimbang corat-coret manual batas organ.")
    with c2:
        st.success("#### 🎯 Akurasi & Konsistensi\nMenghilangkan variabilitas observasi antar spesialis (_inter-observer variability_). Hasil kuantifikasi anatomi otot jantung selalu ajek dan stabil standarnya di rumah sakit mana pun.")
    with c3:
        st.warning("#### 📈 Deteksi Abnormalitas Dini\nKemampuan penghitungan volume (Voxels) yang sangat presisi oleh AI membantu mengenali anomali deformitas pada stadium awal sebelum bermanifestasi kritis.")
        
    st.markdown('<h3 class="section-title">📊 Pembuktian Evaluasi Model</h3>', unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('''<div class="metric-card"><div class="metric-value">91.4%</div><div class="metric-label">Dice Similarity Coefficient</div></div>''', unsafe_allow_html=True)
    with m2:
        st.markdown('''<div class="metric-card"><div class="metric-value">84.5%</div><div class="metric-label">Intersection over Union (IoU)</div></div>''', unsafe_allow_html=True)
    with m3:
        st.markdown('''<div class="metric-card"><div class="metric-value">0.992</div><div class="metric-label">AUC - ROC Performance</div></div>''', unsafe_allow_html=True)
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown('<div class="cta-container">', unsafe_allow_html=True)
    # Gunakan Use Container Width untuk membesarkan tombol CTA di tengah
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("🚀 TRY OUT THE PROTOTYPE NOW", use_container_width=True, type="primary"):
            st.session_state.page = "app"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


def show_app_page():
    """Main application view for segmentation interactive UI."""
    # Navigation Back Button
    if st.sidebar.button("← Back to Landing Page"):
        st.session_state.page = "landing"
        st.rerun()

    st.sidebar.markdown("---")
    
    # Header
    st.markdown('<h2 class="main-title" style="font-size:2rem;">🔬 Prototype Engine</h2>',
                unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Run segmentation interactively</p>',
                unsafe_allow_html=True)
    st.markdown("---")

    # Load model
    model, model_info, device = get_model()

    # Sidebar Tools
    with st.sidebar:
        st.header("⚙️ Settings")

        if model is not None:
            st.success(f"Model loaded on **{device}**")
            if model_info:
                st.caption(f"Epoch: {model_info.get('epoch', 'N/A')} | "
                          f"Val Dice: {model_info.get('val_dice', 'N/A'):.4f}")
        else:
            st.error("Model checkpoint not found!")
            st.caption(f"Expected: `{CHECKPOINT_PATH}`")

        st.markdown("---")
        threshold = st.slider("Segmentation Threshold", 0.1, 0.9, 0.5, 0.05)
        overlay_alpha = st.slider("Overlay Opacity", 0.1, 0.8, 0.4, 0.05)

        st.markdown("---")
        st.markdown("### 📂 Input Source")
        input_mode = st.radio("", ["Use Sample Data", "Upload DICOM"],
                              label_visibility="collapsed")

    # Get DICOM file
    dicom_path = None

    if input_mode == "Upload DICOM":
        uploaded = st.file_uploader(
            "Upload a DICOM file (.dcm)",
            type=["dcm"],
            help="Upload a cardiac SPECT DICOM file for segmentation"
        )
        if uploaded:
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".dcm")
            tmp.write(uploaded.read())
            tmp.close()
            dicom_path = tmp.name

    else:
        if os.path.exists(SAMPLE_DIR):
            samples = sorted([f for f in os.listdir(SAMPLE_DIR) if f.endswith('.dcm')])
            if samples:
                selected = st.selectbox("Select sample DICOM to test:", samples)
                dicom_path = os.path.join(SAMPLE_DIR, selected)
            else:
                st.warning("No .dcm files found in sample directory.")
        else:
            st.warning(f"Sample directory not found: `{SAMPLE_DIR}`")

    # Run inference
    if dicom_path and model is not None:
        with st.spinner("Running deep learning segmentation..."):
            try:
                img, pred_bin, prob_map = predict_volume(
                    dicom_path, model, device,
                    TARGET_SHAPE, threshold
                )
            except Exception as e:
                st.error(f"Inference failed: {e}")
                return

        # --- Metrics ---
        voxel_count = int(pred_bin.sum())
        total_voxels = pred_bin.size
        mask_ratio = (voxel_count / total_voxels) * 100
        mean_confidence = float(prob_map[pred_bin > 0].mean()) if voxel_count > 0 else 0.0
        max_confidence = float(prob_map.max())

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{voxel_count:,}</div>
                <div class="metric-label">Voxels Detected</div>
            </div>""", unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{mask_ratio:.2f}%</div>
                <div class="metric-label">L. Ventricle Ratio</div>
            </div>""", unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{mean_confidence:.3f}</div>
                <div class="metric-label">Mean Confidence</div>
            </div>""", unsafe_allow_html=True)
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{max_confidence:.3f}</div>
                <div class="metric-label">Peak Confidence</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("---")

        # --- Visualization Tabs ---
        tab1, tab2, tab3 = st.tabs(["🔬 Multi-Plane Viewer", "🎯 Segmentation Result", "🌡️ Probability Heatmap"])

        with tab1:
            st.subheader("Interactive Multi-Plane Viewer")
            c1, c2, c3 = st.columns(3)

            with c1:
                ax_idx = st.slider("Axial (X)", 0, img.shape[0]-1, img.shape[0]//2, key="ax")
                fig = render_slice(img[ax_idx, :, :], pred_bin[ax_idx, :, :],
                                   title=f"Axial — slice {ax_idx}", alpha=overlay_alpha)
                st.pyplot(fig)
                plt.close(fig)

            with c2:
                cor_idx = st.slider("Coronal (Y)", 0, img.shape[1]-1, img.shape[1]//2, key="cor")
                fig = render_slice(img[:, cor_idx, :], pred_bin[:, cor_idx, :],
                                   title=f"Coronal — slice {cor_idx}", alpha=overlay_alpha)
                st.pyplot(fig)
                plt.close(fig)

            with c3:
                sag_idx = st.slider("Sagittal (Z)", 0, img.shape[2]-1, img.shape[2]//2, key="sag")
                fig = render_slice(img[:, :, sag_idx], pred_bin[:, :, sag_idx],
                                   title=f"Sagittal — slice {sag_idx}", alpha=overlay_alpha)
                st.pyplot(fig)
                plt.close(fig)

        with tab2:
            st.subheader("Automated Segmentation Outline")
            c1, c2, c3 = st.columns(3)

            mid = [s // 2 for s in img.shape]

            with c1:
                fig, axes = plt.subplots(1, 2, figsize=(8, 4))
                fig.patch.set_facecolor('#0e1117')
                axes[0].imshow(img[mid[0], :, :].T, cmap='gray', origin='lower')
                axes[0].set_title("SPECT", color='white', fontweight='bold')
                axes[0].axis('off')
                axes[1].imshow(pred_bin[mid[0], :, :].T, cmap='inferno', origin='lower')
                axes[1].set_title("Segmentation", color='white', fontweight='bold')
                axes[1].axis('off')
                plt.suptitle("Axial View", color='white', fontweight='bold')
                plt.tight_layout()
                st.pyplot(fig)
                plt.close(fig)

            with c2:
                fig, axes = plt.subplots(1, 2, figsize=(8, 4))
                fig.patch.set_facecolor('#0e1117')
                axes[0].imshow(img[:, mid[1], :].T, cmap='gray', origin='lower')
                axes[0].set_title("SPECT", color='white', fontweight='bold')
                axes[0].axis('off')
                axes[1].imshow(pred_bin[:, mid[1], :].T, cmap='inferno', origin='lower')
                axes[1].set_title("Segmentation", color='white', fontweight='bold')
                axes[1].axis('off')
                plt.suptitle("Coronal View", color='white', fontweight='bold')
                plt.tight_layout()
                st.pyplot(fig)
                plt.close(fig)

            with c3:
                fig, axes = plt.subplots(1, 2, figsize=(8, 4))
                fig.patch.set_facecolor('#0e1117')
                axes[0].imshow(img[:, :, mid[2]].T, cmap='gray', origin='lower')
                axes[0].set_title("SPECT", color='white', fontweight='bold')
                axes[0].axis('off')
                axes[1].imshow(pred_bin[:, :, mid[2]].T, cmap='inferno', origin='lower')
                axes[1].set_title("Segmentation", color='white', fontweight='bold')
                axes[1].axis('off')
                plt.suptitle("Sagittal View", color='white', fontweight='bold')
                plt.tight_layout()
                st.pyplot(fig)
                plt.close(fig)

        with tab3:
            st.subheader("Model Validation (Probability Map)")
            c1, c2, c3 = st.columns(3)

            with c1:
                prob_idx = st.slider("Axial (X)", 0, img.shape[0]-1, img.shape[0]//2, key="prob_ax")
                fig = render_slice(img[prob_idx, :, :], prob_slice=prob_map[prob_idx, :, :],
                                   title=f"Probability — axial {prob_idx}")
                st.pyplot(fig)
                plt.close(fig)

            with c2:
                prob_idx2 = st.slider("Coronal (Y)", 0, img.shape[1]-1, img.shape[1]//2, key="prob_cor")
                fig = render_slice(img[:, prob_idx2, :], prob_slice=prob_map[:, prob_idx2, :],
                                   title=f"Probability — coronal {prob_idx2}")
                st.pyplot(fig)
                plt.close(fig)

            with c3:
                prob_idx3 = st.slider("Sagittal (Z)", 0, img.shape[2]-1, img.shape[2]//2, key="prob_sag")
                fig = render_slice(img[:, :, prob_idx3], prob_slice=prob_map[:, :, prob_idx3],
                                   title=f"Probability — sagittal {prob_idx3}")
                st.pyplot(fig)
                plt.close(fig)

        # --- Download ---
        st.markdown("---")
        st.subheader("📥 Export & API")

        col1, col2 = st.columns(2)
        with col1:
            tmp_mask = tempfile.NamedTemporaryFile(delete=False, suffix=".nii.gz")
            save_mask_as_nifti(pred_bin, tmp_mask.name)
            with open(tmp_mask.name, 'rb') as f:
                st.download_button(
                    label="Download Segmentation Mask (.nii.gz)",
                    data=f.read(),
                    file_name="predicted_mask.nii.gz",
                    mime="application/gzip"
                )

        with col2:
            tmp_prob = tempfile.NamedTemporaryFile(delete=False, suffix=".nii.gz")
            save_mask_as_nifti(prob_map, tmp_prob.name)
            with open(tmp_prob.name, 'rb') as f:
                st.download_button(
                    label="Download Probability Map (.nii.gz)",
                    data=f.read(),
                    file_name="probability_map.nii.gz",
                    mime="application/gzip"
                )

        # Safety disclaimer
        st.markdown("---")
        st.caption("⚠️ **Disclaimer:** This tool is a research prototype for academic purposes only. "
                   "It is NOT intended for clinical diagnosis. Always consult qualified medical professionals "
                   "for diagnostic decisions.")

    elif model is None:
        st.info("👆 Please ensure the model checkpoint exists at the expected path.")
    else:
        st.info("👆 Upload a DICOM file or select sample data to begin segmentation.")


def main():
    # Initialize State Control
    if 'page' not in st.session_state:
        st.session_state.page = "landing"

    # Routing
    if st.session_state.page == "landing":
        show_landing_page()
    elif st.session_state.page == "app":
        show_app_page()

if __name__ == '__main__':
    main()
