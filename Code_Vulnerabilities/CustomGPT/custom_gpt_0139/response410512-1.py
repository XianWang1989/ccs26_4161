
from flask import Flask, request
import os

app = Flask(__name__)

# Directory where you save dynamic files
MEDIA_DIR = '/path/to/media'

@app.route('/generate_content', methods=['POST'])
def generate_content():
    # Get data from the request
    content = request.form['content']

    # Generate a filename (could be timestamped, etc.)
    filename = 'dynamic_content.txt'
    filepath = os.path.join(MEDIA_DIR, filename)

    # Write the content to a file
    with open(filepath, 'w') as f:
        f.write(content)

    # Return the URL for Nginx to serve
    return f'http://your-domain.com/media/{filename}'

if __name__ == '__main__':
    app.run(debug=True)
