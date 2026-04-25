
from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
MEDIA_DIR = '/path/to/media'

@app.route('/generate-file')
def generate_file():
    # Example logic to generate a file
    file_name = 'dynamic_file.txt'
    file_content = 'This is a dynamically created file.'

    # Save the file
    with open(os.path.join(MEDIA_DIR, file_name), 'w') as f:
        f.write(file_content)

    # Return the URL of the file
    return f'/media/{file_name}', 201

@app.route('/media/<filename>')
def serve_file(filename):
    return send_from_directory(MEDIA_DIR, filename)

if __name__ == '__main__':
    app.run()
