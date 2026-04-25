
from flask import Flask, send_from_directory
import os
import tempfile

app = Flask(__name__)
TEMP_DIR = tempfile.gettempdir()

@app.route('/create-file')
def create_file():
    filename = 'dynamic_file.txt'
    file_path = os.path.join(TEMP_DIR, filename)

    # Create a dynamic file
    with open(file_path, 'w') as f:
        f.write("This is dynamically generated content.")

    # Return the URL to the user
    return f'File created. Access it <a href="/media/{filename}">here</a>.'

@app.route('/media/<path:filename>')
def send_file(filename):
    return send_from_directory(TEMP_DIR, filename)

if __name__ == "__main__":
    app.run()
