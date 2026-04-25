
from flask import Flask, send_file
import os

app = Flask(__name__)
MEDIA_DIR = '/path/to/media/directory'

@app.route('/generate-file')
def generate_file():
    # Create your dynamic content
    filename = 'dynamic_file.txt'
    filepath = os.path.join(MEDIA_DIR, filename)

    with open(filepath, 'w') as f:
        f.write('This is dynamic content!')

    return f'File generated: <a href="/media/{filename}">Download</a>'

if __name__ == '__main__':
    app.run()
