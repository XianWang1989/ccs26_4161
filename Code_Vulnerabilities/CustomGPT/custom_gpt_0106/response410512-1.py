
from flask import Flask, send_from_directory, request
import os
import tempfile

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media'  # Directory where files are saved

@app.route('/create-file', methods=['GET'])
def create_file():
    # Generate dynamic content
    content = "This is the dynamic content."

    # Save to a temporary file
    file_path = os.path.join(MEDIA_FOLDER, 'dynamic_file.txt')
    with open(file_path, 'w') as f:
        f.write(content)

    return {"message": "File created", "url": f"/media/dynamic_file.txt"}

@app.route('/media/<path:filename>', methods=['GET'])
def serve_file(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == '__main__':
    app.run()
