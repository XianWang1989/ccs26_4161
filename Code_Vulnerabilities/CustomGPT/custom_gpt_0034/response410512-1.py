
from flask import Flask, request
import os

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media'  # Ensure Nginx can access this path.

@app.route('/generate-file')
def generate_file():
    # Create a dynamic file
    filename = 'dynamic_file.txt'
    file_path = os.path.join(MEDIA_FOLDER, filename)

    with open(file_path, 'w') as f:
        f.write('This is a dynamically generated file.')

    return f'File created: {filename}'

if __name__ == '__main__':
    app.run()
