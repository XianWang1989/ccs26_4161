
from flask import Flask, send_from_directory
import os
import uuid

app = Flask(__name__)
media_folder = '/path/to/media'  # Update with your media directory

@app.route('/create_media')
def create_media():
    # Create a dynamically generated file
    filename = f"media_{uuid.uuid4()}.txt"
    file_content = "This is a dynamically generated file."

    # Save the file to the media folder
    file_path = os.path.join(media_folder, filename)
    with open(file_path, 'w') as f:
        f.write(file_content)

    # Return the file URL to the client
    return f"/media/{filename}", 201

@app.route('/media/<path:filename>')
def serve_media(filename):
    # Use Nginx to serve the file; this will allow Nginx to handle the response
    return send_from_directory(media_folder, filename)

if __name__ == '__main__':
    app.run()
