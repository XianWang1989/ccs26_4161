
from flask import Flask, jsonify
import os

app = Flask(__name__)

BASE_DIR = '/path/to/your/media/files'

@app.route('/generate-file')
def generate_file():
    # Simulate generating a file
    filename = "dynamic_file.txt"
    file_path = os.path.join(BASE_DIR, filename)

    with open(file_path, 'w') as f:
        f.write("This is dynamically generated content.")

    # Return the URL to access the file
    file_url = f"http://yourdomain.com/media/{filename}"
    return jsonify({"file_url": file_url})

if __name__ == '__main__':
    app.run()
