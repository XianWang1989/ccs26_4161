
from flask import Flask, jsonify, request
import os

app = Flask(__name__)
MEDIA_DIR = '/path/to/media'  # Change this to your media directory

@app.route('/generate-file', methods=['POST'])
def generate_file():
    # Generate your content (e.g., a PDF or image)
    filename = 'dynamic_file.txt'  # Change as needed
    filepath = os.path.join(MEDIA_DIR, filename)

    with open(filepath, 'w') as f:
        f.write("This is a dynamically generated file.")

    # Return URL to access the file
    file_url = f"http://yourdomain.com/media/{filename}"
    return jsonify({"url": file_url})

if __name__ == "__main__":
    app.run()
