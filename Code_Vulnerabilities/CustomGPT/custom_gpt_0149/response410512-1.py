
from flask import Flask, redirect, url_for
import os

app = Flask(__name__)
MEDIA_DIR = '/path/to/media/'

@app.route('/generate-file')
def generate_file():
    # Example: generate a dynamic text file
    file_path = os.path.join(MEDIA_DIR, 'dynamic_file.txt')
    with open(file_path, 'w') as f:
        f.write("This is a dynamically created file.")
    return redirect(url_for('serve_file', filename='dynamic_file.txt'))

@app.route('/media/<filename>')
def serve_file(filename):
    return redirect(f'/media/{filename}', code=302)

if __name__ == '__main__':
    app.run()
