
from flask import Flask, request, send_file
import os
import tempfile

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    # Dynamic content creation
    content = "This is some dynamically created content."

    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp_file:
        tmp_file.write(content.encode('utf-8'))
        tmp_file_path = tmp_file.name

    # Return the file path
    # Note: You should implement cleanup for the temp file afterward
    return tmp_file_path

if __name__ == '__main__':
    app.run()
