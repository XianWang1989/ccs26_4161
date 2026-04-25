
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/generate_file')
def generate_file():
    # Create dynamic content
    file_path = '/path/to/media/directory/my_file.txt'
    with open(file_path, 'w') as f:
        f.write('This is some dynamic content.')

    return jsonify({'message': 'File created successfully!', 'file_url': f'/media/my_file.txt'})

if __name__ == '__main__':
    app.run()
