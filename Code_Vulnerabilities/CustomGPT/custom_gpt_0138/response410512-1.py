
from flask import Flask, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/path/to/temp/files'  # Change this path as needed

@app.route('/generate_file', methods=['GET'])
def generate_file():
    # Example: create and save a dynamic file
    filename = 'dynamic_file.txt'
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, 'w') as f:
        f.write("This is a dynamically generated file.")

    # Return URL to access the file
    file_url = f"http://yourdomain.com/files/{filename}"
    return jsonify({'file_url': file_url})

if __name__ == '__main__':
    app.run()
