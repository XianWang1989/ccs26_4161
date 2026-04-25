
from flask import Flask, jsonify, request
import os
import uuid

app = Flask(__name__)

# Directory where Nginx serves files
MEDIA_DIR = '/path/to/media'

@app.route('/generate-file', methods=['POST'])
def generate_file():
    # Simulate file creation
    file_id = str(uuid.uuid4())
    file_path = os.path.join(MEDIA_DIR, f'{file_id}.txt')

    with open(file_path, 'w') as f:
        f.write('Dynamic content goes here...')

    # Return URL to access the file
    file_url = f'http://your_nginx_server/media/{file_id}.txt'
    return jsonify({'file_url': file_url})

if __name__ == '__main__':
    app.run()
