
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
media_folder = '/path/to/your/media'

@app.route('/generate_file', methods=['POST'])
def generate_file():
    filename = 'dynamic_file.txt'
    # Example: creating a dynamic file
    with open(os.path.join(media_folder, filename), 'w') as f:
        f.write('This is a dynamically generated file.')

    # Return the URL to access the file
    file_url = f'http://yourdomain.com/media/{filename}'
    return jsonify({'file_url': file_url})

if __name__ == '__main__':
    app.run()
