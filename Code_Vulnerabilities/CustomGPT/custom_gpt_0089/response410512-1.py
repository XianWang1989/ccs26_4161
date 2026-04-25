
from flask import Flask, send_file, jsonify
import os
import time

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    # Simulate file creation
    file_path = '/tmp/dynamic_file.txt'
    with open(file_path, 'w') as f:
        f.write("This is a dynamically created file!")

    # Return the URL that Nginx will serve
    return jsonify(url=f'http://your-nginx-domain/static/{os.path.basename(file_path)}')

if __name__ == '__main__':
    app.run()
