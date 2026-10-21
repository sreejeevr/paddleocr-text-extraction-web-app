import os

# Fix PaddlePaddle Windows/oneDNN issue
os.environ["FLAGS_enable_pir_api"] = "0"

from paddleocr import PaddleOCR

# Initialize OCR
ocr = PaddleOCR(
    lang="en",
    enable_mkldnn=False
)

image_path = "test.jpg"

# Run OCR
results = ocr.predict(image_path)

for result in results:

    # Get recognized text
    texts = result["rec_texts"]

    # Get confidence scores
    scores = result["rec_scores"]

    print("\n" + "=" * 50)
    print("                OCR RESULT")
    print("=" * 50)

    for text in texts:
        print(text)

    print("=" * 50)

    # Calculate average confidence
    if scores:
        average_confidence = sum(scores) / len(scores)
        print(f"Average Confidence: {average_confidence * 100:.2f}%")

    print("=" * 50)