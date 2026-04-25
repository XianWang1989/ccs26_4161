
from flask import Flask, jsonify
import os

app = Flask(__name__)
MEDIA_DIR = 'media_files'  # directory to store generated files

@app.route('/generate-file', methods=['POST'])
def generate_file():
    filename = 'my_dynamic_file.txt'
    filepath = os.path.join(MEDIA_DIR, filename)

    # Simulate file generation (e.g., create or write to file)
    with open(filepath, 'w') as f:
        f.write('This is a dynamically generated file.')

    # Return the URL where the file can be accessed by Nginx
    return jsonify({'file_url': f'/media/{filename}'})

if __name__ == '__main__':
    app.run()
