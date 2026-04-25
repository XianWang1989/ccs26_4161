
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Directory where files will be saved
MEDIA_DIR = '/path/to/media'

@app.route('/create-file', methods=['POST'])
def create_file():
    content = request.json.get('content', '')

    # Create a dynamic filename (e.g., using a timestamp)
    filename = f"file_{int(time.time())}.txt"
    file_path = os.path.join(MEDIA_DIR, filename)

    # Save the content to a file
    with open(file_path, 'w') as f:
        f.write(content)

    # Return the URL of the created file
    return jsonify({"url": f"http://your-nginx-server/{filename}"}), 201

if __name__ == '__main__':
    app.run()
