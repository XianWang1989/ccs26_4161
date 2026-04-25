
from flask import Flask, send_file, redirect, url_for
import os
import tempfile

app = Flask(__name__)
app.config['MEDIA_FOLDER'] = '/path/to/media'  # Set path to your media directory

@app.route('/generate_media')
def generate_media():
    # Generate your media content here
    media_content = b"Some dynamically created content"

    # Create a temporary file and save the content
    temp_file = tempfile.NamedTemporaryFile(delete=False, dir=app.config['MEDIA_FOLDER'])
    temp_file.write(media_content)
    temp_file.close()

    # Return the URL to access the media file via Nginx
    return redirect(url_for('serve_media', filename=os.path.basename(temp_file.name)))

@app.route('/media/<filename>')
def serve_media(filename):
    # Nginx will handle serving this file
    return send_file(os.path.join(app.config['MEDIA_FOLDER'], filename))

if __name__ == '__main__':
    app.run()
