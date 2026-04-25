
import os
from flask import Flask, send_from_directory, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = '/path/to/upload/folder'  # Set your upload folder path
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/generate-file', methods=['POST'])
def generate_file():
    # Simulating dynamic content creation
    content = "This is some dynamically generated content."
    filename = f"dynamic_file_{request.remote_addr}.txt"  # Unique filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))

    # Write content to a file
    with open(file_path, 'w') as f:
        f.write(content)

    # Return the URL to access the file
    file_url = f'/media/{filename}'
    return jsonify({'file_url': file_url})

@app.route('/media/<path:filename>')
def serve_media(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run()
