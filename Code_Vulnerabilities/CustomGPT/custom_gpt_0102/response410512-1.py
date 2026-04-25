
from flask import Flask, request, jsonify, send_from_directory
import os
import tempfile

app = Flask(__name__)
UPLOAD_FOLDER = '/path/to/temp/directory'  # Set this to a desired temp directory

@app.route('/generate-file', methods=['GET'])
def generate_file():
    # Dynamically create content (for example, a text file)
    content = "This is dynamically generated content."

    # Save the file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, dir=UPLOAD_FOLDER, suffix='.txt') as tmp_file:
        tmp_file.write(content.encode())
        filename = os.path.basename(tmp_file.name)

    # Return the URL for Nginx to serve the file
    return jsonify({"file_url": f"/files/{filename}"})

@app.route('/files/<path:filename>', methods=['GET'])
def serve_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run()

