
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
MEDIA_DIRECTORY = '/path/to/media'  # Directory where files will be saved

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file_path = os.path.join(MEDIA_DIRECTORY, file.filename)
        file.save(file_path)  # Save the file to the media directory
        # Return the URL to access the file via Nginx
        return jsonify({'url': f'http://yourdomain.com/media/{file.filename}'})

if __name__ == '__main__':
    app.run()
