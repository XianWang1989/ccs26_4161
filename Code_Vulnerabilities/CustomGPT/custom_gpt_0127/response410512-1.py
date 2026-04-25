
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/dynamic/media'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = os.path.join(MEDIA_FOLDER, file.filename)
    file.save(file_path)

    return jsonify({'message': 'File uploaded successfully', 'url': f'/media/{file.filename}'})

if __name__ == '__main__':
    app.run()
