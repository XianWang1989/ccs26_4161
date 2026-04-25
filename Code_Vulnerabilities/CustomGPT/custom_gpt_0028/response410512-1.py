
from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media'  # Set your media directory here

@app.route('/generate-file')
def generate_file():
    # Your code for generating the file
    filename = 'dynamic_file.txt'  # Example file name
    file_path = os.path.join(MEDIA_FOLDER, filename)

    # Simulating file creation
    with open(file_path, 'w') as f:
        f.write('This is some dynamic content.')

    # Return the URL for the file
    file_url = f'/media/{filename}'  # Nginx will serve this
    return jsonify({'file_url': file_url})

@app.route('/media/<path:filename>')
def serve_file(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == '__main__':
    app.run()
