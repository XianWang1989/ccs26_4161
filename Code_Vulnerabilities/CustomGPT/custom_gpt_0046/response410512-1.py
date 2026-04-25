
from flask import Flask, request, jsonify
import os
import tempfile

app = Flask(__name__)

# Directory where Nginx serves files
MEDIA_DIR = '/path/to/nginx/media/'  # Change this to your Nginx media directory

@app.route('/generate', methods=['POST'])
def generate_file():
    content = request.json.get('content', 'Hello, World!')

    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, dir=MEDIA_DIR) as temp_file:
        temp_file.write(content.encode('utf-8'))
        temp_file_path = temp_file.name

    return jsonify({'url': f'http://yourdomain.com/media/{os.path.basename(temp_file_path)}'})

if __name__ == '__main__':
    app.run()
