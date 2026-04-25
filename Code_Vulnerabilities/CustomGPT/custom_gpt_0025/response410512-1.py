
from flask import Flask, jsonify
import os

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media'

@app.route('/generate-file/<filename>', methods=['GET'])
def generate_file(filename):
    content = "This is dynamically created content."
    file_path = os.path.join(MEDIA_FOLDER, filename)

    # Write content to the file
    with open(file_path, 'w') as f:
        f.write(content)

    # Return the URL to access the file
    file_url = f"http://yourdomain.com/media/{filename}"
    return jsonify({"file_url": file_url})

if __name__ == '__main__':
    app.run()
