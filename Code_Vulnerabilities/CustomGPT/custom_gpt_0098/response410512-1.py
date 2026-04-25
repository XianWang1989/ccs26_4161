
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    # Example of generating a file
    filename = 'dynamic_file.txt'
    file_path = os.path.join('/path/to/your/tmp/files', filename)

    with open(file_path, 'w') as f:
        f.write("This is a dynamically created file.")

    # Return the URL to access the file
    file_url = f"http://your_domain.com/media/{filename}"
    return jsonify({"file_url": file_url})

if __name__ == '__main__':
    app.run()
