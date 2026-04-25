
from flask import Flask, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media/directory'

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file_path = os.path.join(MEDIA_FOLDER, file.filename)
        file.save(file_path)  # Save the file
        return redirect(url_for('serve_file', filename=file.filename))

@app.route('/media/<filename>')
def serve_file(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == '__main__':
    app.run()
