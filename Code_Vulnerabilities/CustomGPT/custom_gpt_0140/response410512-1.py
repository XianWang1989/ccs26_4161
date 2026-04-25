
from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

# Define a directory to store the files
UPLOAD_FOLDER = '/path/to/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/generate-file', methods=['POST'])
def generate_file():
    # Example content creation logic
    filename = 'dynamic_file.txt'
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Create and save content to file
    with open(file_path, 'w') as f:
        f.write('This is some dynamically generated content.')

    # Return the file URL for Nginx to serve
    return {'file_url': f'/media/{filename}'}

@app.route('/media/<path:filename>', methods=['GET'])
def serve_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run()
