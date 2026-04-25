
from flask import Flask, send_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/path/to/temp/files/'

@app.route('/generate-file')
def generate_file():
    # Create a dynamic file
    file_path = os.path.join(UPLOAD_FOLDER, 'dynamic_file.txt')
    with open(file_path, 'w') as f:
        f.write("This is dynamically generated content.")

    # Return the URL to access the file
    return f'File generated! Access it <a href="/files/dynamic_file.txt">here</a>.'

if __name__ == '__main__':
    app.run()
