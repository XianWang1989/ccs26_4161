
from flask import Flask, jsonify, request
import os
import tempfile

app = Flask(__name__)
MEDIA_DIR = '/path/to/media'  # Ensure this directory is writable

@app.route('/generate-media', methods=['POST'])
def generate_media():
    # Simulate dynamic file creation
    content = request.json.get('content', 'Default content')
    filename = 'dynamic_file.txt'
    file_path = os.path.join(MEDIA_DIR, filename)

    # Write content to a file
    with open(file_path, 'w') as f:
        f.write(content)

    # Return the URL to access the file
    file_url = f'/media/{filename}'
    return jsonify({'url': file_url})

if __name__ == '__main__':
    app.run()
