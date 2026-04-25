
from flask import Flask, jsonify
import os

app = Flask(__name__)

# Directory to save dynamic files
DYNAMIC_DIR = 'dynamic_files'

# Ensure the directory exists
os.makedirs(DYNAMIC_DIR, exist_ok=True)

@app.route('/generate_file/<filename>')
def generate_file(filename):
    # Create your dynamic file (example: a simple text file)
    file_path = os.path.join(DYNAMIC_DIR, filename)
    with open(file_path, 'w') as f:
        f.write("This is some dynamically generated content.")

    # Return the URL where Nginx can serve this file
    return jsonify({'url': f'/dynamic/{filename}'})

if __name__ == '__main__':
    app.run()
