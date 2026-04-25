
from flask import Flask, jsonify
import os

app = Flask(__name__)
MEDIA_DIR = '/path/to/media'  # Ensure this is accessible by Nginx

@app.route('/generate-file/<filename>', methods=['GET'])
def generate_file(filename):
    file_path = os.path.join(MEDIA_DIR, filename)

    # Simulate dynamic content
    with open(file_path, 'w') as f:
        f.write("Dynamic content for " + filename)

    return jsonify({"message": "File generated", "url": f"/media/{filename}"})

if __name__ == '__main__':
    app.run()
