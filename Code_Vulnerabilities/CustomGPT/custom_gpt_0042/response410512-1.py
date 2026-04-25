
from flask import Flask, send_from_directory, request
import os

app = Flask(__name__)
MEDIA_FOLDER = 'media'  # Directory for dynamic media files

# Ensure the media directory exists
os.makedirs(MEDIA_FOLDER, exist_ok=True)

@app.route('/create_file', methods=['POST'])
def create_file():
    # Example: dynamically create a file
    filename = 'my_dynamic_file.txt'
    content = 'This is a dynamically generated file content.'

    file_path = os.path.join(MEDIA_FOLDER, filename)
    with open(file_path, 'w') as f:
        f.write(content)

    return {'message': 'File created', 'file': filename}, 201

@app.route('/media/<path:filename>')
def serve_file(filename):
    # Serve the generated file through Nginx
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == "__main__":
    app.run()
