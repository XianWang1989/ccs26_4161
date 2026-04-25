
from flask import Flask, request, send_from_directory
import os
import tempfile

app = Flask(__name__)
MEDIA_DIR = '/path/to/media'  # Ensure this matches your Nginx configuration

@app.route('/generate')
def generate_file():
    # Create dynamic content
    content = "This is some dynamic content."

    # Save to a temporary file
    filename = "dynamic_content.txt"
    file_path = os.path.join(MEDIA_DIR, filename)

    with open(file_path, 'w') as f:
        f.write(content)

    return f"File created: <a href='/media/{filename}'>Download</a>"

@app.route('/media/<path:filename>')
def serve_file(filename):
    # Serve the file through Nginx
    return send_from_directory(MEDIA_DIR, filename)

if __name__ == '__main__':
    app.run()
