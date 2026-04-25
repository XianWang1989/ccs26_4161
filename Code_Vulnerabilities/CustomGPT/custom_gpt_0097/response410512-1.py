
from flask import Flask, jsonify
import os

app = Flask(__name__)
MEDIA_FOLDER = 'media'  # Ensure this directory is accessible by Nginx

@app.route('/generate-file')
def generate_file():
    file_path = os.path.join(MEDIA_FOLDER, 'dynamic_file.txt')
    with open(file_path, 'w') as f:
        f.write('This is a dynamically created file.')

    return jsonify({"message": "File created", "file_url": f"/{file_path}"})

if __name__ == '__main__':
    app.run()
