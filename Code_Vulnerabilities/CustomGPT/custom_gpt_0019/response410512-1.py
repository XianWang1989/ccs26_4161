
from flask import Flask, request, send_file
import os
import tempfile

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as temp_file:
        temp_file.write(b'Some dynamic content here.')
        temp_file_path = temp_file.name

    # This is the URL that Nginx will use to serve the file
    return f'/serve-file/{os.path.basename(temp_file_path)}'

if __name__ == '__main__':
    app.run()
