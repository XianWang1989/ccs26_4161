
from flask import Flask, request, send_file
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = '/path/to/upload'  # Set this to a directory on your server
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']

    if file.filename == '':
        return "No selected file", 400

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return f"File uploaded successfully, access it at /files/{filename}", 200

@app.route('/files/<filename>')
def serve_file(filename):
    # Make sure the file exists in the upload folder
    full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if os.path.exists(full_path):
        return send_file(full_path)
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run()
