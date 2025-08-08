Image-to-Text Extractor
A small, deployable Flask web app that extracts text from images using Tesseract OCR and returns plain, editable text. Built as a clean, multi-file project suitable as a code sample for applications (e.g., MLH Fellowship) and hackathons.

🚀 What it does
Users upload an image (PNG/JPG/TIFF/BMP). The app passes the image to Tesseract via pytesseract and returns the detected text. The extracted text can be displayed, copied, saved, or sent to a translation pipeline.

Short GitHub description:
Extracts text from images using Tesseract OCR for display, storage, or translation.

🔧 Features
Single-page Flask app with an upload form

Tesseract OCR integration via pytesseract

Lightweight, modular code (app.py, utils/text_detect.py, utils/translate.py)

Basic UI (HTML/CSS/JS) for a clean user experience

Safe file handling and small upload folder

Easy to run locally and simple to deploy to small cloud hosts

📁 Project structure
arduino
Copy
Edit
image-to-multilingual-text/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── utils/
│   ├── text_detect.py
│   └── translate.py
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   ├── styles.css
│   └── script.js
└── uploads/                # created at runtime
⚙️ Setup (Local)
1. Clone
bash
Copy
Edit
git clone https://github.com/<your-username>/image-to-multilingual-text.git
cd image-to-multilingual-text
2. Create & activate virtual environment
bash
Copy
Edit
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Windows (cmd)
venv\Scripts\activate
3. Install Python deps
bash
Copy
Edit
pip install -r requirements.txt
4. Install Tesseract OCR
Ubuntu / Debian

bash
Copy
Edit
sudo apt update
sudo apt install tesseract-ocr
macOS (Homebrew)

bash
Copy
Edit
brew install tesseract
Windows

Download the installer from the official Tesseract repo: https://github.com/tesseract-ocr/tesseract

Install and note the installation path (e.g., C:\Program Files\Tesseract-OCR\tesseract.exe).

In utils/text_detect.py set:

python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
▶️ Run the app
bash
Copy
Edit
python app.py
Open http://127.0.0.1:5000 in your browser.

📝 Usage
Open the web UI.

Click Select image and upload an image that contains printed or handwritten text.

(Optional) Choose a translation language if translation feature is enabled.

Click Extract & Translate.

View detected text and copy/save as needed.

Tips for better OCR results

Use clear, high-contrast images.

Crop to the area containing text before uploading.

Avoid angled or heavily noisy pictures. If available, rotate or deskew images first.

💡 Implementation notes
OCR is handled purely by Tesseract via pytesseract. No OpenCV steps are required for the minimal version, keeping the code simple and deployable.

The project is modular: utils/text_detect.py handles image reading + OCR; utils/translate.py (optional) handles translation.

File uploads are saved to an uploads/ folder (ignored by .gitignore) and removed after processing.

📦 Deployment notes
For small demos use Render, Railway, or Heroku (free tiers are usually fine for small traffic).

If deploying to a container, ensure Tesseract is installed in the container image.

Use environment variables for secrets (e.g., API keys for a paid translation API).

Example Procfile for Heroku:

makefile
Copy
Edit
web: python app.py
🧪 Tests & Improvements (suggestions)
Add unit tests for text_detect.extract_text_from_image.

Add integration tests for upload → OCR → result.

Add retry or fallback behavior if Tesseract fails.

Add option to download detected text (.txt) or copy to clipboard.

Add optional simple preprocessing (resize, grayscale) as an opt-in feature if OCR quality is poor.

🤝 Contributing
Contributions are welcome!

Fork the repo

Create a branch (feature/awesome-feature)

Make changes & add tests

Open a Pull Request with a clear description
