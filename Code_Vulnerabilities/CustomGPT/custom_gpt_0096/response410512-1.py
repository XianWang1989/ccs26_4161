
from flask import Flask, jsonify
import os
import tempfile

app = Flask(__name__)

@app.route('/generate_file')
def generate_file():
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
    with open(temp_file.name, 'w') as f:
        f.write("This is some dynamic content!")

    # Generate URL (assuming your Nginx serves from '/media')
    file_url = f'/media/{os.path.basename(temp_file.name)}'

    return jsonify({"file_url": file_url})

if __name__ == '__main__':
    app.run()
