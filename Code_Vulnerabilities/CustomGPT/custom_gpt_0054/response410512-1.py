
from flask import Flask, send_from_directory
import os

app = Flask(__name__)
media_dir = "/path/to/your/media"  # Same as in the Nginx config

@app.route('/generate-file/<filename>')
def generate_file(filename):
    # Generate your file dynamically and save it to media_dir
    file_path = os.path.join(media_dir, filename)

    # Example: Write some text to a file (this could be any type of media)
    with open(file_path, 'w') as f:
        f.write("Dynamic content here.")

    # Return the URL of the generated file for later access
    return f"File generated successfully! Access it at /media/{filename}"

@app.route('/media/<path:filename>')
def serve_file(filename):
    # Use Nginx to serve the file from the media directory
    return send_from_directory(media_dir, filename)

if __name__ == '__main__':
    app.run()
