
from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

# Directory for storing generated media files
MEDIA_DIR = '/path/to/media'

@app.route('/generate-file', methods=['POST'])
def generate_file():
    # Simulate file creation
    content = request.form.get('content', 'Default Content')
    filename = 'dynamic_file.txt'

    # Saving the file
    with open(os.path.join(MEDIA_DIR, filename), 'w') as f:
        f.write(content)

    # Return the URL to access the file
    return f'File created. Access it at: /media/{filename}'

@app.route('/media/<path:filename>', methods=['GET'])
def media_file(filename):
    return send_from_directory(MEDIA_DIR, filename)

if __name__ == '__main__':
    app.run()
