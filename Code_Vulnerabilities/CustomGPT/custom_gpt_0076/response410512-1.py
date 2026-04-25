
from flask import Flask, jsonify
import os

app = Flask(__name__)
MEDIA_DIR = '/path/to/media/directory'  # Change this to your media directory

@app.route('/generate-file')
def generate_file():
    # Simulate file generation
    file_name = 'dynamic_content.txt'
    file_path = os.path.join(MEDIA_DIR, file_name)

    with open(file_path, 'w') as f:
        f.write('This is some dynamically created content.')

    # Return the URL to access the generated file
    return jsonify({'file_url': f'/media/{file_name}'})

if __name__ == '__main__':
    app.run()
