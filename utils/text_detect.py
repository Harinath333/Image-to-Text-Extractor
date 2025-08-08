import cv2
import pytesseract
from PIL import Image
import numpy as np
import os
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Adjust this path as needed

# If Tesseract is not in PATH on your machine, set the tesseract_cmd:
# Example for Windows:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image_for_ocr(image_path):
    """Read image and apply preprocessing for better OCR results."""
    img = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        # fallback to PIL open
        img = cv2.cvtColor(np.array(Image.open(image_path)), cv2.COLOR_RGB2BGR)

    # Resize if too large (optional)
    max_dim = 1600
    h, w = img.shape[:2]
    if max(h, w) > max_dim:
        scale = max_dim / float(max(h, w))
        img = cv2.resize(img, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_AREA)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Remove noise and smooth
    gray = cv2.bilateralFilter(gray, 9, 75, 75)

    # Adaptive thresholding
    th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 11, 2)

    # optional morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    processed = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)

    return processed


def extract_text_from_image(image_path, lang="eng"):
    """Return text extracted from the given image path using pytesseract."""
    try:
        processed = preprocess_image_for_ocr(image_path)

        # pytesseract can accept numpy arrays via PIL
        pil_img = Image.fromarray(processed)

        # Basic config: LSTM OCR + page segmentation mode 3 (default)
        config = "--oem 3 --psm 3"
        text = pytesseract.image_to_string(pil_img, lang=lang, config=config)

        # Post-process: normalize whitespace
        text = "\n".join([line.strip() for line in text.splitlines() if line.strip()])

        return text
    except Exception as e:
        # In production, log the error
        return f"[ERROR] OCR failed: {e}"
