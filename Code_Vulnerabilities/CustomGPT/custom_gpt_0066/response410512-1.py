
from flask import Flask, send_file, jsonify
import os

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    # Generate the file dynamically
    filename = 'example.txt'
    filepath = f'/var/www/media/{filename}'

    with open(filepath, 'w') as f:
        f.write('This is a dynamically generated file.')

    # Return the URL to access the file
    return jsonify({"url": f"/media/{filename}"})

if __name__ == '__main__':
    app.run()
