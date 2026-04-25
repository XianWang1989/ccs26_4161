
from flask import Flask, request
import os

app = Flask(__name__)
MEDIA_DIR = '/path/to/media'  # Set this to your media directory

@app.route('/generate_file', methods=['POST'])
def generate_file():
    content = request.json.get('content', 'Hello World!')
    filename = 'dynamic_file.txt'
    file_path = os.path.join(MEDIA_DIR, filename)

    # Create and save the file
    with open(file_path, 'w') as f:
        f.write(content)

    # Return the URL to the client
    return {'url': f'/media/{filename}'}, 200

if __name__ == '__main__':
    app.run()
