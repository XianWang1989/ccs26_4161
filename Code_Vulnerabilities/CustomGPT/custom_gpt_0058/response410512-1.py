
from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/path/to/uploaded_files'  # Change this to your actual folder

@app.route('/generate-file', methods=['POST'])
def generate_file():
    # Logic to create your file (for example purposes, we create a simple txt file)
    filename = 'dynamic_content.txt'
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    with open(filepath, 'w') as f:
        f.write("This is dynamically generated content.")

    # After generating, you can return the URL to access the file
    return {'file_url': f'/files/{filename}'}

@app.route('/files/<path:filename>', methods=['GET'])
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run()
