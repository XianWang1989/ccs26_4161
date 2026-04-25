
from flask import Flask, request, send_from_directory
import os
import tempfile

app = Flask(__name__)

@app.route('/generate-media')
def generate_media():
    # Generate a temporary media file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    temp_file_path = temp_file.name

    # Simulate creating content (e.g., saving an image)
    with open(temp_file_path, 'wb') as f:
        f.write(os.urandom(1024))  # Replace with actual content generation

    return {
        "file_url": f"/media/{os.path.basename(temp_file_path)}"
    }

@app.route('/media/<filename>')
def serve_media(filename):
    # Serve the file created in the temp directory
    return send_from_directory(os.path.dirname(filename), filename)

if __name__ == '__main__':
    app.run()
