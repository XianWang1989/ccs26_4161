
from flask import Flask, jsonify
import os

app = Flask(__name__)
MEDIA_DIR = '/path/to/media'  # Set your media directory

@app.route('/generate/<filename>')
def generate_file(filename):
    # Create a dynamic file (for example, a text file)
    file_path = os.path.join(MEDIA_DIR, filename)
    with open(file_path, 'w') as f:
        f.write("This is dynamic content for " + filename)

    # Return the URL to access the file
    return jsonify({"url": f"/media/{filename}"}), 200

if __name__ == "__main__":
    app.run()
