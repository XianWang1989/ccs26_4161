
from flask import Flask, send_file, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/path/to/upload'  # Change to your upload directory

@app.route('/generate-file/<filename>', methods=['GET'])
def generate_file(filename):
    # Generate your file content
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, 'w') as f:
        f.write("This is dynamic content for " + filename)

    # Return a JSON response with the URL to access the file
    return jsonify({"file_url": f"/media/{filename}"})

if __name__ == '__main__':
    app.run()
