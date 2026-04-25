
from flask import Flask, request
import os
from werkzeug.utils import send_from_directory

app = Flask(__name__)

# Directory to temporarily store media files
MEDIA_DIR = '/path/to/media'

@app.route('/generate-file', methods=['POST'])
def generate_file():
    # Your logic to generate the content (example: a text file)
    content = "This is a dynamically created content."
    filename = "dynamic_file.txt"

    # Path where the file will be saved
    file_path = os.path.join(MEDIA_DIR, filename)

    # Write your content to the file
    with open(file_path, 'w') as f:
        f.write(content)

    # Serve the file via Nginx
    return f"File generated and available at: /media/{filename}"

# Serve files from MEDIA_DIR with Nginx
@app.route('/media/<path:filename>')
def serve_file(filename):
    return send_from_directory(MEDIA_DIR, filename)

if __name__ == '__main__':
    app.run()
