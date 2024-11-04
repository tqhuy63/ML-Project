from flask import Flask, render_template, request, redirect, url_for
from utils.ocr import perform_ocr
import os
# import pytesseract

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            text = perform_ocr(file_path)
            return render_template('index.html', text=text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
