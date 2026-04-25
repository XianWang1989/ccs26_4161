
from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/download/<filename>')
def download_file(filename):
    # Create the file dynamically
    file_path = f'/tmp/{filename}'  # Temporary storage
    with open(file_path, 'w') as f:
        f.write('This is your dynamic content!')

    # Return the file path for Nginx to serve
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run()
