
from flask import Flask, request
import os

app = Flask(__name__)
media_folder = '/path/to/media/folder'  # Ensure this path is accessible by Nginx

@app.route('/create_media/<filename>', methods=['GET'])
def create_media(filename):
    # Simulate dynamic content creation
    file_path = os.path.join(media_folder, filename)
    with open(file_path, 'w') as f:
        f.write('This is dynamically created content.')

    return f'Dynamic content created at {file_path}'

if __name__ == '__main__':
    app.run()
