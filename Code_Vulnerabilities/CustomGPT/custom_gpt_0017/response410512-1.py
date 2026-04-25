
from flask import Flask, send_from_directory
import os

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media'

@app.route('/generate_file')
def generate_file():
    # Replace this with your dynamic content generation logic
    filename = 'dynamic_content.txt'
    file_path = os.path.join(MEDIA_FOLDER, filename)

    with open(file_path, 'w') as f:
        f.write("This is dynamically generated content.")

    return f"File created: {filename}"

@app.route('/media/<path:filename>')
def serve_file(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == '__main__':
    app.run()
