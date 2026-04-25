
from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
MEDIA_FOLDER = 'media'

@app.route('/generate', methods=['POST'])
def generate_file():
    # Example content generation
    filename = 'dynamic_file.txt'
    content = 'This is dynamically created content!'

    # Save the content to the media folder
    os.makedirs(MEDIA_FOLDER, exist_ok=True)
    with open(os.path.join(MEDIA_FOLDER, filename), 'w') as f:
        f.write(content)

    return {'message': 'File created', 'url': f'/media/{filename}'}

@app.route('/media/<path:filename>', methods=['GET'])
def send_file(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == '__main__':
    app.run()
