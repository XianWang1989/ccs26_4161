
from flask import Flask, request, jsonify, url_for
import os
import tempfile

app = Flask(__name__)

# Directory to serve files from
MEDIA_DIR = '/path/to/media'

@app.route('/generate-file', methods=['POST'])
def generate_file():
    content = request.json.get('content')
    filename = 'dynamic_file.txt'

    # Write content to a file
    file_path = os.path.join(MEDIA_DIR, filename)
    with open(file_path, 'w') as f:
        f.write(content)

    # Return the URL of the generated file
    file_url = url_for('media_file', filename=filename)
    return jsonify({'file_url': file_url})

@app.route('/media/<filename>', methods=['GET'])
def media_file(filename):
    # Nginx will serve this file
    return '', 204  # Placeholder response

if __name__ == '__main__':
    app.run()
