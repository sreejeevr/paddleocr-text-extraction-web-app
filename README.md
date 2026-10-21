# PaddleOCR Text Extraction Web App

A web-based Optical Character Recognition (OCR) application built using Python, Flask, and PaddleOCR to extract text from images and scanned documents.

## Overview

This project provides a simple web interface for uploading documents and extracting readable text using OCR technology. It demonstrates the integration of deep learning-based text recognition with a Flask web application.

## Features

- Upload images for text extraction
- Extract text using PaddleOCR
- Web interface built with Flask, HTML, and CSS
- Process sample images and documents for OCR testing
- Organized application code and dependencies

## Technologies Used

- **Programming Language:** Python
- **OCR Engine:** PaddleOCR
- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **Tools:** VS Code, GitHub

## Project Structure

```text
paddleocr-text-extraction-web-app/
├── app.py
├── requirements.txt
├── test_ocr.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/sreejeevr/paddleocr-text-extraction-web-app.git
cd paddleocr-text-extraction-web-app
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open the local address displayed in the terminal in your web browser.

## Testing

The project includes `test_ocr.py` for OCR-related testing. Run it with:

```bash
python test_ocr.py
```

## Learning Outcomes

- Understanding OCR and text recognition
- Integrating machine learning tools into a Python application
- Developing a web application using Flask
- Processing image-based text with PaddleOCR

## Future Improvements

- Add PDF text extraction and downloadable results
- Improve image preprocessing for better recognition
- Support multiple document formats
- Deploy the application online

## Author

**Sreejeev R Chandran**

GitHub: [@sreejeevr](https://github.com/sreejeevr)

---

*Developed as a Python and AI/ML project focused on OCR-based text extraction.*
