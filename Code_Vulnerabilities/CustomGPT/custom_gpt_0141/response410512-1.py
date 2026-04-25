
from flask import Flask, jsonify, request
import os
from datetime import datetime

app = Flask(__name__)
MEDIA_DIR = '/path/to/media'  # Update with your media directory path

@app.route('/generate-file', methods=['POST'])
def generate_file():
    # Generate dynamic content (for example purposes, this is a text file)
    filename = f"file_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    file_path = os.path.join(MEDIA_DIR, filename)

    with open(file_path, 'w') as f:
        f.write('This is a dynamically created file.')

    # Return the URL to access the file
    file_url = f"http://yourdomain.com/media/{filename}"
    return jsonify({'file_url': file_url})

if __name__ == '__main__':
    app.run()
