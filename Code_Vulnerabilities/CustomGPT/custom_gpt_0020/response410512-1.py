
from flask import Flask, send_from_directory, request, jsonify
import os
import tempfile

app = Flask(__name__)
UPLOAD_FOLDER = '/path/to/temp/directory'  # Replace with your temp directory

@app.route('/generate-file', methods=['GET'])
def generate_file():
    # Example of dynamic content creation
    content = "This is your dynamically generated file."

    # Create a temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False, dir=UPLOAD_FOLDER)
    temp_file.write(content.encode())
    temp_file.close()

    # Return the file path (can also be a URL for Nginx to access)
    file_url = f"/files/{os.path.basename(temp_file.name)}"
    return jsonify({'file_url': file_url})

@app.route('/files/<filename>', methods=['GET'])
def serve_file(filename):
    # Serve the file dynamically created
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run()
