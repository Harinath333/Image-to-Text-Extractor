import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from utils.text_detect import extract_text_from_image
from utils.translate import translate_text

# Configuration
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "bmp", "tiff"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = os.environ.get("FLASK_SECRET", "dev-secret")  # change in prod

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/translate", methods=["POST"])
def translate():
    # check if the post request has the file part
    if "image" not in request.files:
        flash("No file part", "error")
        return redirect(url_for("index"))

    file = request.files["image"]
    target_lang = request.form.get("language", "en")

    if file.filename == "":
        flash("No selected file", "error")
        return redirect(url_for("index"))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        saved_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(saved_path)

        # OCR
        extracted_text = extract_text_from_image(saved_path)

        if not extracted_text.strip():
            flash("No text detected in the image. Try a clearer or higher-resolution image.", "warning")
            return redirect(url_for("index"))

        # Translate
        translated_text = translate_text(extracted_text, target_lang)

        # Optionally remove uploaded file to save space
        try:
            os.remove(saved_path)
        except Exception:
            pass

        return render_template(
            "result.html",
            original_text=extracted_text,
            translated_text=translated_text,
            language=target_lang.upper(),
        )
    else:
        flash("Unsupported file type. Allowed types: png, jpg, jpeg, bmp, tiff", "error")
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
