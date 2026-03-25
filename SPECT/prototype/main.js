(function () {
  const sampleFiles = [
    "1.2.840.4267.32.102843376980518437893525476318362476257.dcm",
    "1.2.840.4267.32.113412595772340035961437115035537970349.dcm",
    "1.2.840.4267.32.117076509617201664779117387663005758527.dcm",
    "1.2.840.4267.32.118564058634314627767242469443335771432.dcm",
    "1.2.840.4267.32.118665136185166160396570866271079771944.dcm"
  ];

  const config = window.CorVisionConfig || {};
  const backendStatus = document.getElementById("backend-status");
  const threshold = document.getElementById("threshold");
  const thresholdValue = document.getElementById("threshold-value");
  const sampleCase = document.getElementById("sample-case");
  const responseOutput = document.getElementById("response-output");
  const form = document.getElementById("predict-form");
  const resetButton = document.getElementById("reset-button");
  const submitButton = document.getElementById("submit-button");
  const fileInput = document.getElementById("dicom-file");

  sampleFiles.forEach((name) => {
    const option = document.createElement("option");
    option.value = name;
    option.textContent = name;
    sampleCase.appendChild(option);
  });

  threshold.addEventListener("input", () => {
    thresholdValue.textContent = Number(threshold.value).toFixed(2);
  });

  const hasBackend = Boolean(config.inferenceApiUrl);

  if (hasBackend) {
    backendStatus.className = "status-box status-ok";
    backendStatus.textContent =
      "Inference backend configured. Uploads will be sent to the external API.";
  } else {
    backendStatus.className = "status-box status-warn";
    backendStatus.textContent =
      "Demo mode. No inference API configured yet. Set inferenceApiUrl in config.js to enable uploads.";
  }

  submitButton.disabled = !hasBackend;

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    if (!hasBackend) {
      responseOutput.textContent =
        "No request sent. This deploy is frontend-only until inferenceApiUrl is configured in config.js.";
      return;
    }

    if (!fileInput.files.length) {
      responseOutput.textContent = "Choose a DICOM file before sending a request.";
      return;
    }

    submitButton.disabled = true;
    submitButton.textContent = "Sending...";

    const payload = new FormData();
    payload.append(config.uploadFieldName || "dicom", fileInput.files[0]);
    payload.append(config.thresholdFieldName || "threshold", threshold.value);

    if (sampleCase.value) {
      payload.append("sampleCase", sampleCase.value);
    }

    const headers = {};
    if (config.apiKey) {
      headers.Authorization = `Bearer ${config.apiKey}`;
    }

    try {
      const response = await fetch(config.inferenceApiUrl, {
        method: "POST",
        headers,
        body: payload
      });

      const text = await response.text();

      try {
        const parsed = JSON.parse(text);
        responseOutput.textContent = JSON.stringify(parsed, null, 2);
      } catch (jsonError) {
        responseOutput.textContent = text;
      }
    } catch (error) {
      responseOutput.textContent = `Request failed: ${error.message}`;
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = "Send to Inference API";
    }
  });

  resetButton.addEventListener("click", () => {
    form.reset();
    threshold.value = "0.5";
    thresholdValue.textContent = "0.50";
    responseOutput.textContent = "No request sent yet.";
  });
})();
