
from flask import Flask, send_from_directory
import os

app = Flask(__name__)
MEDIA_DIR = '/path/to/media'  # Change to your media directory

@app.route('/generate/<filename>')
def generate_file(filename):
    # Simulate file creation (e.g., generate a PDF or image)
    file_path = os.path.join(MEDIA_DIR, filename)
    with open(file_path, 'w') as f:
        f.write("This is a dynamically created file!")

    return f"File {filename} created."

@app.route('/media/<path:filename>')
def serve_media(filename):
    return send_from_directory(MEDIA_DIR, filename)

if __name__ == '__main__':
    app.run()
