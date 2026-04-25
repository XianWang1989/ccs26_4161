
from flask import Flask, send_from_directory
import os
from tempfile import gettempdir

app = Flask(__name__)

@app.route('/generate-file/<filename>')
def generate_file(filename):
    # Simulating dynamic content creation
    file_path = os.path.join(gettempdir(), filename)

    with open(file_path, 'w') as f:
        f.write("This is the dynamically created content.")

    return f"File generated: {filename}. You can access it at /serve/{filename}"

@app.route('/serve/<filename>')
def serve_file(filename):
    return send_from_directory(gettempdir(), filename)

if __name__ == '__main__':
    app.run()
