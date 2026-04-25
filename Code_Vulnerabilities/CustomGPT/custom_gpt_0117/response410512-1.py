
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/path/to/your/uploads'

@app.route('/generate-file', methods=['POST'])
def generate_file():
    # Simulate creating a dynamic file
    content = request.json.get('content', 'Default content')
    file_name = 'dynamic_file.txt'
    file_path = os.path.join(UPLOAD_FOLDER, file_name)

    with open(file_path, 'w') as f:
        f.write(content)

    # Return the URL where Nginx can serve the file
    return jsonify({'file_url': f'/media/{file_name}'})

if __name__ == '__main__':
    app.run()
