
from flask import Flask, send_from_directory
import os
import tempfile

app = Flask(__name__)
media_dir = os.path.join(tempfile.gettempdir(), 'dynamic_media')

# Create the directory if it doesn't exist
if not os.path.exists(media_dir):
    os.makedirs(media_dir)

@app.route('/generate_media')
def generate_media():
    # Here, create your dynamic media file
    file_name = 'example.txt'  # Name your file as needed
    file_path = os.path.join(media_dir, file_name)

    # Write example content to the file
    with open(file_path, 'w') as f:
        f.write('This is an example of dynamically created content.')

    # Construct the URL to the file to serve via Nginx
    file_url = f"/media/{file_name}"
    return {'url': file_url}

# Serve dynamically created media using Nginx (via a separate route)
@app.route('/media/<path:filename>')
def serve_media(filename):
    return send_from_directory(media_dir, filename)

if __name__ == '__main__':
    app.run()
