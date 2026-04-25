
from flask import Flask, send_file
import os

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media'  # Set your media folder path

@app.route('/generate')
def generate_file():
    file_path = os.path.join(MEDIA_FOLDER, 'dynamic_file.txt')

    # Create and write content to the file
    with open(file_path, 'w') as f:
        f.write("This is a dynamically generated file.")

    # Return a URL that points to the file
    return f'File created! You can download it at /media/dynamic_file.txt'

if __name__ == '__main__':
    app.run()
