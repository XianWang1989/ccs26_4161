
from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)
MEDIA_DIR = '/path/to/media/directory'  # Set this to your desired media directory

@app.route('/generate_file')
def generate_file():
    # Here, create and save your file dynamically.
    file_name = 'dynamic_file.txt'
    file_path = os.path.join(MEDIA_DIR, file_name)

    with open(file_path, 'w') as f:
        f.write('This is a dynamically generated file.')

    # Return the URL to the generated file
    return jsonify({"url": f"/media/{file_name}"})

@app.route('/media/<path:filename>', methods=['GET'])
def serve_file(filename):
    return send_from_directory(MEDIA_DIR, filename)

if __name__ == "__main__":
    app.run()
