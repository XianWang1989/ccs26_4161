
from flask import Flask, send_from_directory
import os

app = Flask(__name__)
MEDIA_DIR = 'media'  # Directory where files will be saved

@app.route('/generate-file/<filename>')
def generate_file(filename):
    # Create the file and save it to MEDIA_DIR
    file_path = os.path.join(MEDIA_DIR, filename)

    with open(file_path, 'w') as f:
        f.write("This is dynamically generated content!")

    return f"File generated: {filename}"

@app.route('/media/<path:filename>')
def serve_file(filename):
    # Serve the file from the MEDIA_DIR
    return send_from_directory(MEDIA_DIR, filename)

if __name__ == '__main__':
    app.run()
