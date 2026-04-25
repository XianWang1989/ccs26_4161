
from flask import Flask, send_file, jsonify
import os

app = Flask(__name__)

# Directory to save dynamic files
DYNAMIC_MEDIA_DIR = '/path/to/static/media'

@app.route('/generate-file/<filename>', methods=['GET'])
def generate_file(filename):
    # Simulate file creation
    file_path = os.path.join(DYNAMIC_MEDIA_DIR, filename)
    with open(file_path, 'w') as f:
        f.write("Dynamic content here...")

    # Instead of sending the file through Flask, redirect to Nginx
    return jsonify({'url': f'/media/{filename}'})

if __name__ == '__main__':
    app.run()
