
from flask import Flask, send_from_directory
import os

app = Flask(__name__)
TEMP_DIR = 'tempfiles'

# Ensure the temporary directory exists
os.makedirs(TEMP_DIR, exist_ok=True)

@app.route('/generate')
def generate_file():
    file_path = os.path.join(TEMP_DIR, 'dynamic_file.txt')
    with open(file_path, 'w') as f:
        f.write("This is dynamically generated content.")
    return f"File created at {file_path}"

@app.route('/files/<path:filename>')
def serve_file(filename):
    return send_from_directory(TEMP_DIR, filename)

if __name__ == '__main__':
    app.run()
