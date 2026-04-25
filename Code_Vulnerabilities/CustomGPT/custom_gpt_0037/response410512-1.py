
from flask import Flask, request, jsonify
import os
import tempfile

app = Flask(__name__)

@app.route('/generate-file', methods=['POST'])
def generate_file():
    # Generate your dynamic content here
    content = "This is dynamic content."

    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as temp_file:
        temp_file.write(content.encode())
        temp_file_path = temp_file.name

    # Make sure the file is accessible by Nginx
    return jsonify({'file_url': f'/media/{os.path.basename(temp_file_path)}'})

if __name__ == '__main__':
    app.run()
