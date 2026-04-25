
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
TEMP_DIR = '/path/to/temp/dir'  # Ensure this directory exists and is writable

@app.route('/generate-file', methods=['POST'])
def generate_file():
    # Create your dynamic content
    content = 'Dynamic content goes here'
    file_name = 'dynamic_file.txt'  # You can use dynamic naming as needed
    file_path = os.path.join(TEMP_DIR, file_name)

    # Write to the file
    with open(file_path, 'w') as f:
        f.write(content)

    # Return URL for Nginx to serve
    return jsonify(url=f'/static/{file_name}')

if __name__ == '__main__':
    app.run()
