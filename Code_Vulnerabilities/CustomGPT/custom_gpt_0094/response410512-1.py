
from flask import Flask, send_from_directory, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/path/to/upload'  # Ensure this folder is writable by Nginx
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/generate-file', methods=['POST'])
def generate_file():
    # Generate your file dynamically (dummy example)
    filename = 'dynamic_file.txt'
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    with open(file_path, 'w') as f:
        f.write("This is dynamically generated content.")

    # Return the URL to access the file
    return jsonify({"url": f"/files/{filename}"})

@app.route('/files/<path:filename>', methods=['GET'])
def serve_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run()
