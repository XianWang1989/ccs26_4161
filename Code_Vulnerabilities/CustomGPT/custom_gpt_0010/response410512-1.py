
from flask import Flask, jsonify
import os

app = Flask(__name__)
MEDIA_DIR = '/path/to/media'  # Ensure this directory exists and is writable by your app

@app.route('/generate-file/<filename>', methods=['GET'])
def generate_file(filename):
    content = 'This is the content of the dynamic file.'
    file_path = os.path.join(MEDIA_DIR, filename)

    with open(file_path, 'w') as f:
        f.write(content)

    return jsonify({'message': 'File created', 'file_url': f'/media/{filename}'})

if __name__ == '__main__':
    app.run()
