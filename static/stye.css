/* =========================================================
   RESET
========================================================= */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}


/* =========================================================
   BODY
========================================================= */

body {
    font-family: Arial, sans-serif;
    background: #f1f3f8;
    color: #1f2937;
    min-height: 100vh;
}


/* =========================================================
   MAIN CONTAINER
========================================================= */

.container {
    width: 100%;
    max-width: 1050px;
    margin: 40px auto;
    padding: 0 25px 40px;
}


/* =========================================================
   HEADER
========================================================= */

header {
    text-align: center;
    margin-bottom: 30px;
}

header h1 {
    font-size: 38px;
    margin-bottom: 10px;
    color: #1f2937;
}

header p {
    font-size: 17px;
    color: #6b7280;
}


/* =========================================================
   TABS
========================================================= */

.tabs {
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-bottom: 25px;
}

.tab-button {
    border: none;
    background: white;
    color: #374151;
    padding: 14px 25px;
    border-radius: 10px;
    font-size: 15px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.25s;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.tab-button:hover {
    transform: translateY(-2px);
}

.tab-button.active {
    background: #111827;
    color: white;
}


/* =========================================================
   TAB CONTENT
========================================================= */

.tab-content {
    display: none;
    width: 100%;
}

.tab-content.active {
    display: block;
}


/* =========================================================
   CARDS
========================================================= */

.card,
.result-card {
    background: white;
    border-radius: 20px;
    padding: 30px;
    margin-bottom: 25px;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.10);
}

.card h2,
.result-card h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

.description {
    color: #6b7280;
    margin-bottom: 25px;
    line-height: 1.5;
}


/* =========================================================
   UPLOAD AREA
========================================================= */

.upload-area {
    border: 2px dashed #aeb6c4;
    border-radius: 15px;
    min-height: 220px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    transition: 0.25s;
}

.upload-area:hover {
    border-color: #111827;
    background: #f9fafb;
}

.upload-area input[type="file"] {
    display: none;
}

.upload-area label {
    cursor: pointer;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}

.upload-icon {
    font-size: 48px;
}

.upload-title {
    font-size: 18px;
    font-weight: bold;
}

.upload-area small {
    color: #6b7280;
}


/* =========================================================
   BUTTONS
========================================================= */

.primary-button,
.secondary-button,
.word-button,
.pdf-button,
.stop-button {
    border: none;
    border-radius: 10px;
    padding: 14px 22px;
    font-size: 15px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.25s;
}

.primary-button {
    background: #111827;
    color: white;
}

.primary-button:hover {
    background: #000000;
    transform: translateY(-2px);
}

.secondary-button {
    background: #e5e7eb;
    color: #1f2937;
}

.secondary-button:hover {
    background: #d1d5db;
}

.stop-button {
    background: #dc2626;
    color: white;
}

.stop-button:hover {
    background: #b91c1c;
}

.word-button {
    background: #2563eb;
    color: white;
}

.word-button:hover {
    background: #1d4ed8;
}

.pdf-button {
    background: #dc2626;
    color: white;
}

.pdf-button:hover {
    background: #b91c1c;
}


/* =========================================================
   CAMERA
========================================================= */

.camera-container {
    width: 100%;
    text-align: center;
}

.camera-preview {
    width: 100%;
    max-width: 700px;
    height: 400px;
    margin: 20px auto;
    background: #111827;
    border: 3px solid #374151;
    border-radius: 15px;
    overflow: hidden;
    position: relative;
}

.camera-preview video {
    width: 100%;
    height: 100%;
    display: block;
    object-fit: cover;
}

.camera-placeholder {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 18px;
    pointer-events: none;
}


/* =========================================================
   CAPTURED IMAGE PREVIEW
========================================================= */

.captured-preview {
    display: none;
    width: 100%;
    max-width: 700px;
    margin: 25px auto;
    text-align: left;
}

.captured-preview.show {
    display: block;
}

.captured-preview h3 {
    margin-bottom: 12px;
    color: #1f2937;
}

#captured-image {
    width: 100%;
    max-height: 450px;
    object-fit: contain;
    display: block;
    border: 2px solid #d1d5db;
    border-radius: 12px;
}


/* =========================================================
   PROCESSING BAR
========================================================= */

.processing-container {
    display: none;
    width: 100%;
    max-width: 700px;
    margin: 20px auto;
}

.processing-container.show {
    display: block;
}

.processing-container p {
    text-align: center;
    font-weight: bold;
    margin-bottom: 12px;
}

.progress-bar {
    width: 100%;
    height: 12px;
    background: #e5e7eb;
    border-radius: 20px;
    overflow: hidden;
}

.progress-fill {
    width: 0%;
    height: 100%;
    background: #2563eb;
    border-radius: 20px;
}

.processing-container.show .progress-fill {
    animation: processing 1.5s ease-in-out infinite;
}

@keyframes processing {

    0% {
        width: 0%;
    }

    50% {
        width: 80%;
    }

    100% {
        width: 100%;
    }

}


/* =========================================================
   CAMERA BUTTONS
========================================================= */

.camera-buttons {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 15px;
    margin-top: 20px;
}

.camera-buttons button {
    min-width: 190px;
}


/* =========================================================
   RESULT
========================================================= */

.result-card {
    border-top: 5px solid #111827;
}

.result-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    margin-bottom: 20px;
}

.confidence {
    background: #ecfdf5;
    color: #047857;
    padding: 10px 15px;
    border-radius: 10px;
    white-space: nowrap;
}

.result-text {
    width: 100%;
    min-height: 400px;
    resize: vertical;
    border: 1px solid #d1d5db;
    border-radius: 12px;
    padding: 20px;
    font-family: Arial, sans-serif;
    font-size: 15px;
    line-height: 1.6;
    color: #1f2937;
    background: #fafafa;
    outline: none;
}

.result-text:focus {
    border-color: #111827;
    background: white;
}


/* =========================================================
   ACTION BUTTONS
========================================================= */

.action-buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 20px;
}

.download-form {
    display: inline-block;
}

.action-buttons button {
    min-width: 155px;
}


/* =========================================================
   ERROR
========================================================= */

.error-box {
    background: #fee2e2;
    color: #b91c1c;
    border: 1px solid #fecaca;
    border-radius: 12px;
    padding: 15px 20px;
    margin-bottom: 20px;
    text-align: center;
}


/* =========================================================
   MOBILE RESPONSIVE
========================================================= */

@media (max-width: 700px) {

    .container {
        margin: 20px auto;
        padding: 0 15px 30px;
    }

    header h1 {
        font-size: 28px;
    }

    .tabs {
        flex-direction: column;
    }

    .tab-button {
        width: 100%;
    }

    .card,
    .result-card {
        padding: 20px;
        border-radius: 15px;
    }

    .camera-preview {
        height: 280px;
    }

    .camera-buttons {
        flex-direction: column;
    }

    .camera-buttons button {
        width: 100%;
    }

    .result-header {
        flex-direction: column;
        align-items: flex-start;
    }

    .action-buttons {
        flex-direction: column;
    }

    .download-form,
    .action-buttons button {
        width: 100%;
    }

}
