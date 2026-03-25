# CorVision Vercel Frontend

Folder ini sekarang khusus untuk deployment frontend statis di Vercel.

Struktur Streamlit lama sudah dihapus dari `SPECT/prototype`, sehingga folder ini tidak lagi memuat runtime Python, PyTorch, atau entrypoint Streamlit. Tujuannya sederhana: root deploy ini harus bersih dan jelas untuk static hosting di Vercel.

## File Penting

- `index.html`
  Entry page aplikasi
- `styles.css`
  Styling utama
- `main.js`
  Logic form upload dan komunikasi ke backend inference
- `config.js`
  Konfigurasi endpoint inference
- `vercel.json`
  Konfigurasi deployment Vercel
- `assets/`
  Asset visual
- `sample_data/`
  Referensi nama file sample yang dipakai di UI

## Deploy ke Vercel

Set root directory project ke:

```text
SPECT/prototype
```

Frontend ini tidak memerlukan build step khusus. `vercel.json` sudah disetel untuk static deployment.

## Konfigurasi Backend Inference

Secara default frontend berjalan tanpa backend aktif. Untuk menghubungkan endpoint inference, edit `config.js`:

```js
window.CorVisionConfig = {
  inferenceApiUrl: "https://your-inference-service.example.com/predict",
  apiKey: "",
  demoMode: true,
  uploadFieldName: "dicom",
  thresholdFieldName: "threshold"
};
```

Jika `inferenceApiUrl` belum diisi, frontend tetap bisa dideploy dan dipakai sebagai landing page serta shell integrasi.

## Catatan

- Inference model 3D U-Net tidak lagi dijalankan di folder ini.
- Untuk produksi, backend inference sebaiknya dipisahkan ke service tersendiri yang memang cocok untuk PyTorch.
